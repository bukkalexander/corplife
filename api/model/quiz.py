from typing import List
from pydantic import BaseModel

from api.models import Question


class Quiz(BaseModel):
    id: str
    ownerId: str
    title: str
    questions: List[Question]