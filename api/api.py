from datetime import datetime, timezone
import boto3
from botocore.exceptions import ClientError
import json
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import logging
import os
from score_data import ScoreData

# Cofigure logger
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.getLogger("mangum").setLevel(LOG_LEVEL)
logger = logging.getLogger("mangum")

DYNAMODB_TABLE_NAME_QUESTIONS =  os.getenv('DYNAMODB_TABLE_NAME_QUESTIONS', None)
DYNAMODB_TABLE_NAME_USERS =  os.getenv('DYNAMODB_TABLE_NAME_USERS', None)
SCORES_FILE = Path("scores.json")

from data import QUESTIONS_0 as QUESTIONS
from question import Question

app = FastAPI()

# Allow requests from the web server domain origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DynamoDB client
dynamodb = boto3.resource("dynamodb")
users_table = dynamodb.Table(DYNAMODB_TABLE_NAME_USERS)

@app.get("/questions", response_model=List[Question])
async def get_questions():
    return QUESTIONS


@app.get("/user/score")
async def get_user_score(request: Request):
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
        response = users_table.get_item(Key={"username": username})
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


@app.post("/score", response_model=ScoreData)
async def create_score(score_data: ScoreData):
    
    scores = read_scores()
    
    # Find the highest existing ID and increment by 1
    max_id = max((score['id'] for score in scores), default=0)
    score_data.id = max_id + 1
    score_data.timestamp = datetime.now(timezone.utc).isoformat()

    scores.append(score_data.model_dump())
    write_scores(scores)
    return score_data

def read_scores() -> List[ScoreData]:
    if not SCORES_FILE.exists():
        return []
    with open(SCORES_FILE, "r") as file:
        return json.load(file)

def write_scores(scores: List[ScoreData]):
    with SCORES_FILE.open("w") as file:
        json.dump(scores, file, indent=4)


@app.get("/scores", response_model=List[ScoreData])
async def get_scores():
    scores = read_scores()
    return scores
