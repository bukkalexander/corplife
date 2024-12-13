from typing import List
from pydantic import BaseModel

from api.models import QuestionRecord


class QuizRecord(BaseModel):
    id: str
    quizId: str
    userId: str
    questionRecords: List[QuestionRecord]