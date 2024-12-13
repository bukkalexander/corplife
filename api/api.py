from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models import Quiz

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/quizzes", response_model=List[Quiz])
async def get_quizzes(quiz_service: QuizService = Depends(get_quiz_service)):
    return await quiz_service.get_all_quizzes()
