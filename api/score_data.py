from pydantic import BaseModel
from typing import Optional

class ScoreData(BaseModel):
    id: Optional[int]
    score: int
    nbrOfQuestions: int
    timestamp: Optional[str]