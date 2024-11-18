from datetime import datetime, timezone
from contextlib import asynccontextmanager
import time
import boto3
from moto import mock_aws
from botocore.exceptions import ClientError
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import logging
from score_data import ScoreData
from config import API_HOST, DYNAMODB_TABLE_NAME_USERS, DYNAMODB_TABLE_NAME_QUESTIONS, REGION

# Configure logger
LOG_LEVEL = "INFO"
logging.getLogger("mangum").setLevel(LOG_LEVEL)
logger = logging.getLogger("mangum")

SCORES_FILE = Path("scores.json")

from data import QUESTIONS_0 as QUESTIONS
from question import Question

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Manage the application's lifespan with setup and teardown logic.
    """
    IS_LOCALHOST = API_HOST in ["localhost", "127.0.0.1"]
    if IS_LOCALHOST:
        print(f"Using Moto to mock DynamoDB for table {DYNAMODB_TABLE_NAME_USERS}.")

        # Start Moto mocking
        mock = mock_aws()
        mock.start()

        # Setup mocked DynamoDB
        dynamodb = boto3.resource("dynamodb", region_name=REGION)
        table = dynamodb.create_table(
            TableName=DYNAMODB_TABLE_NAME_USERS,
            KeySchema=[
                {"AttributeName": "username", "KeyType": "HASH"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "username", "AttributeType": "S"},
                {"AttributeName": "score", "AttributeType": "N"},
            ],
            ProvisionedThroughput={
                "ReadCapacityUnits": 5,
                "WriteCapacityUnits": 5,
            },
            GlobalSecondaryIndexes=[
                {
                    "IndexName": "ScoreIndex",
                    "KeySchema": [
                        {"AttributeName": "username", "KeyType": "HASH"},
                        {"AttributeName": "score", "KeyType": "RANGE"},
                    ],
                    "Projection": {"ProjectionType": "ALL"},
                }
            ],
        )

        # Insert sample data
        with table.batch_writer() as batch:
            batch.put_item({"username": "test_user", "score": 100})
            batch.put_item({"username": "another_user", "score": 200})
            batch.put_item({"username": "example_user", "score": 300})

        print(f"Moto DynamoDB setup complete with table {DYNAMODB_TABLE_NAME_USERS}.")
    else:
        mock = None

    yield

    # Clean up
    if IS_LOCALHOST and mock:
        print("Stopping Moto mocking for DynamoDB.")
        mock.stop()


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


@app.get("/questions", response_model=List[Question])
async def get_questions():
    return QUESTIONS


@app.get("/user/score")
async def get_user_score(request: Request):
    start_time = time.time()
    """Fetch user score from DynamoDB."""
    try:
        # Extract user claims from the request context
        scope = request.scope
        event = scope.get("aws.event", {})
        claims = event.get("requestContext", {}).get("authorizer", {}).get("claims", {})
        username = claims.get("cognito:username", None)

        if not username:
            # Raise an error if username is not present in the claims
            raise HTTPException(status_code=400, detail="Missing username in claims.")

        # Query DynamoDB to get the user's score
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
            "score": user_data.get("score", 0),
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
        logger.debug(f"Execution time for get_user_score: {elapsed_time:.4f} seconds")


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


def read_scores() -> List[ScoreData]:
    """Read scores from a file."""
    if not SCORES_FILE.exists():
        return []
    with open(SCORES_FILE, "r") as file:
        return json.load(file)


def write_scores(scores: List[ScoreData]):
    """Write scores to a file."""
    with SCORES_FILE.open("w") as file:
        json.dump(scores, file, indent=4)


@app.get("/scores", response_model=List[ScoreData])
async def get_scores():
    """Fetch all scores."""
    scores = read_scores()
    return scores
