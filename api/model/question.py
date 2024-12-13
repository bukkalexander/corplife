from typing import List
from pydantic import BaseModel

from api.models import Answer


class Question(BaseModel):
    id: str
    text: str
    answers: List[Answer]
    correctAnswerIndex: int