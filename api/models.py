from pydantic import BaseModel
from typing import List
# ----------------------------
# quiz
# ----------------------------

class Answer(BaseModel):
    text: str

class Question(BaseModel):
    id: str
    text: str
    answers: List[Answer]
    correctAnswerIndex: int

class Quiz(BaseModel):
    id: str
    ownerId: str
    title: str
    questions: List[Question]

# ----------------------------
# record
# ----------------------------

class QuestionRecord(BaseModel):
    questionId: str
    selectedAnswerIndex: int

class QuizRecord(BaseModel):
    id: str
    quizId: str
    userId: str
    questionRecords: List[QuestionRecord]