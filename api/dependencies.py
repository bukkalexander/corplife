
from fastapi import Depends
from api.repo.quiz_repo import QuizRepo


def get_dynamodb():
    if IS_LOCALHOST:
        mock = mock_dynamodb2()
        mock.start()
        dynamodb_resource = boto3.resource("dynamodb")
        # Setup mock tables and data here
        try:
            yield dynamodb_resource
        finally:
            mock.stop()
    else:
        yield boto3.resource("dynamodb")

def get_quiz_repo(dynamodb=Depends(get_dynamodb)) -> QuizRepo:
    table = dynamodb.Table(DYNAMODB_TABLE_NAME_QUIZ)
    return QuizRepo(table)