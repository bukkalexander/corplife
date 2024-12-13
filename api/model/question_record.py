from pydantic import BaseModel


class QuestionRecord(BaseModel):
    questionId: str
    selectedAnswerIndex: int