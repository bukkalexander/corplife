from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List


from data import QUESTIONS
from question import Question

app = FastAPI()

# Allow requests from the web server domain origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # needed locally, but will be overriden in API Gatewat in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/questions", response_model=List[Question])
async def get_questions():
    return QUESTIONS
