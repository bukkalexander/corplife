from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from config import API_HOST, API_PORT, WEB_URL


RELOAD = True
ENTRYPOINT = "main:app"

QUESTIONS = [
    {
        "text": "What kind of storage is AWS S3",
        "answers": ["Object storage", "SQL database", "Block storage", "Document database"],
        "correctAnswer": 0,
    },
    {
        "text": "What does EC2 mean",
        "answers": ["Elastic Container Creator", "Elastic Compute Cloud", "Ephemeral Code Catalog", "Error Cloud 2"],
        "correctAnswer": 1,
    },
]

class Answer(BaseModel):
    questionIndex: int
    selectedAnswerIndex: int

class Question(BaseModel):
    text: str
    answers: List[str]
    correctAnswer: int

app = FastAPI()

# Allow requests from the Vite development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=[WEB_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/questions", response_model=List[Question])
async def get_questions():
    return QUESTIONS

@app.post("/answers")
async def submit_answers(answers: List[Answer]):
    # For now, we just return the answers back
    return JSONResponse(content={"submittedAnswers": answers})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(ENTRYPOINT, host=API_HOST, port=API_PORT, reload=RELOAD)
