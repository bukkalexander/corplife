from datetime import datetime
import json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import logging
import os

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


@app.get("/questions", response_model=List[Question])
async def get_questions():
    return QUESTIONS


@app.api_route("/user/score", methods=["GET", "POST"])
async def get_user_score(request: Request):
    """Extract the raw AWS Lambda event."""
    scope = request.scope
    event = scope.get("aws.event", {})  # Access the Lambda event from scope
    logger.debug(f"Raw Lambda event: {event}")
    claims = event.get("requestContext", {}).get("authorizer", {}).get("claims", {})
    user_id = claims.get("sub", "unknown")

    return {"userId": user_id, "score": 42}


@app.post("/score", response_model=ScoreData)
async def create_score(score_data: ScoreData):
    
    scores = read_scores()
    
    # Find the highest existing ID and increment by 1
    max_id = max((score['id'] for score in scores), default=0)
    score_data.id = max_id + 1
    score_data.timestamp = datetime.utcnow().isoformat()

    scores.append(score_data.dict())
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
