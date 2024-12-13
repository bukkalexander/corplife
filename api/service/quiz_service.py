from typing import List
from fastapi import Depends
import boto3
from moto import mock_dynamodb2

from repo.quiz_repo import QuizRepo
from model.quiz import Quiz

IS_LOCALHOST = True  # Set this based on your environment

def get_dynamodb_resource():
    if IS_LOCALHOST:
        mock = mock_dynamodb2()
        mock.start()
        dynamodb_resource = boto3.resource("dynamodb")
        # Setup mock tables and data here
        return dynamodb_resource, mock
    else:
        return boto3.resource("dynamodb"), None


class QuizService:
    def __init__(self, quiz_repo: QuizRepo):
        self.quiz_repo = quiz_repo

    async def get_all_quizzes(self) -> List[Quiz]:
        quizzes = await self.quiz_repo.get_quizzes()
        return [quiz_entity_to_quiz(quiz) for quiz in quizzes]

def quiz_entity_to_quiz(quiz):
    return Quiz(
        id=quiz["id"],
        ownerId=quiz["ownerId"],
        title=quiz["title"],
        questions=quiz["questions"]
    )
