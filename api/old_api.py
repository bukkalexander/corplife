from datetime import datetime, timezone
from contextlib import asynccontextmanager
import os
import random
import time
import logging
from typing import List

import boto3
from botocore.exceptions import ClientError
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from score_data import ScoreData
from api.old_config import API_HOST, DYNAMODB_TABLE_NAME_USERS, DYNAMODB_TABLE_NAME_QUESTIONS, REGION
from mocking import start_aws_mock, stop_aws_mock
from middleware import MockRequestMiddleware
from question import Question
from utilities import read_scores, write_scores

# Configure logger
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.getLogger("mangum").setLevel(LOG_LEVEL)
logger = logging.getLogger("mangum")


IS_LOCALHOST = API_HOST in ["localhost", "127.0.0.1"]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage the application's lifespan with setup and teardown logic.
    """

    if IS_LOCALHOST:
        print(f"Using Moto to mock DynamoDB for table {DYNAMODB_TABLE_NAME_USERS}.")

        # Start Moto mocking
        mock = start_aws_mock(region=REGION, user_table_name=DYNAMODB_TABLE_NAME_USERS, questions_table_name=DYNAMODB_TABLE_NAME_QUESTIONS)
    else:
        print("Calling real DynamoDB.")
        mock = None

    yield

    # Clean up
    if mock:
        stop_aws_mock(mock)


# Initialize the FastAPI app with the lifespan context
app = FastAPI(lifespan=lifespan)

# Allow requests from the web server domain origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if IS_LOCALHOST:
    app.add_middleware(MockRequestMiddleware)


@app.get("/questions", response_model=List[Question])
async def get_questions():
    """
    Fetch all questions from a random quiz ID in DynamoDB.
    """
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(DYNAMODB_TABLE_NAME_QUESTIONS)

    # Scan the DynamoDB table to fetch all unique quiz IDs
    response = table.scan(ProjectionExpression="quizID")
    quiz_ids = list({item["quizID"] for item in response.get("Items", [])})

    if not quiz_ids:
        return []  # Return an empty list if no quiz IDs are found

    # Pick a random quiz ID
    random_quiz_id = random.choice(quiz_ids)

    # Query for all questions belonging to the random quiz ID
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key("quizID").eq(random_quiz_id)
    )

    questions_data = response.get("Items", [])
    # Transform the items into Question objects
    questions = [
        Question(
            text=question["text"],
            answers=question["answers"],
            correctAnswer=int(question["correctAnswer"]),  # Ensure integer
        )
        for question in questions_data
    ]

    return questions


@app.get("/user/xp")
async def get_user_xp(request: Request):
    start_time = time.time()
    """Fetch user xp from DynamoDB."""
    try:
        # Extract user claims from the request context
        scope = request.scope
        event = scope.get("aws.event", {})
        claims = event.get("requestContext", {}).get("authorizer", {}).get("claims", {})
        username = claims.get("cognito:username", None)

        if not username:
            # Raise an error if username is not present in the claims
            raise HTTPException(status_code=400, detail="Missing username in claims.")

        # Query DynamoDB to get the user's xp
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(DYNAMODB_TABLE_NAME_USERS)
        response = table.get_item(Key={"username": username})
        user_data = response.get("Item", None)

        if not user_data:
            # Raise a 404 error if the user is not found in DynamoDB
            raise HTTPException(status_code=404, detail=f"User '{username}' not found in the database.")

        # Return user data if found
        return {
            "username": user_data["username"],
            "xp": user_data.get("xp", 0),
        }

    except ClientError as e:
        # Handle DynamoDB errors and raise an HTTPException
        raise HTTPException(
            status_code=500,
            detail=f"DynamoDB error: {e.response['Error']['Message']}"
        )

    except Exception as e:
        # Handle other unexpected errors
        raise HTTPException(
            status_code=500,
            detail=f"Unexpected error: {str(e)}"
        )
    
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        logger.debug(f"Execution time for get_user_xp: {elapsed_time:.4f} seconds")


@app.post("/score", response_model=ScoreData)
async def create_score(score_data: ScoreData):
    """Save a new score."""
    scores = read_scores()

    # Find the highest existing ID and increment by 1
    max_id = max((score['id'] for score in scores), default=0)
    score_data.id = max_id + 1
    score_data.timestamp = datetime.now(timezone.utc).isoformat()

    scores.append(score_data.model_dump())
    write_scores(scores)
    return score_data

@app.get("/scores", response_model=List[ScoreData])
async def get_scores():
    """Fetch all scores."""
    scores = read_scores()
    return scores
