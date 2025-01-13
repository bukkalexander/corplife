
from fastapi import Depends, FastAPI
from api.config import Config, get_config
from api.repo.quiz_repo import QuizRepo
from api.service.quiz_service import QuizService

def create_dependencies(app: FastAPI, config: Config):
    def get_dynamodb():
        if config.local:
            mock = mock_dynamodb2()
            mock.start()
            dynamodb = boto3.resource("dynamodb")
            try:
                yield dynamodb
            finally:
                mock.stop()
        else:
            dynamodb = boto3.resource("dynamodb")
            return dynamodb

    def get_quiz_repo(dynamodb) -> QuizRepo:
        table = dynamodb.Table(DYNAMODB_TABLE_NAME_QUIZ)
        return QuizRepo(table)

    def get_quiz_service(config: Config = Depends(get_config)) -> QuizService:
        dynamodb = get_dynamodb(config)
        quiz_repo = get_quiz_repo(dynamodb)
        return QuizService(quiz_repo)