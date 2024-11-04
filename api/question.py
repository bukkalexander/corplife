from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    text: str
    answers: List[str]
    correctAnswer: int