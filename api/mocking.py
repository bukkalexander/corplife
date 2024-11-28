import boto3
from moto import mock_aws
from moto.core.models import MockAWS
import data  # Import questions data from data.py
import inspect


def get_all_question_sets(module):
    """
    Dynamically fetch all QUESTION_* variables from the given module.
    """
    questions = {}
    for name, obj in inspect.getmembers(module):
        if name.startswith("QUESTIONS_") and isinstance(obj, list):
            quiz_id = f"quiz_{name.split('_')[1]}"
            questions[quiz_id] = obj
    return questions


def start_aws_mock(region, user_table_name, questions_table_name) -> MockAWS:
    """
    Start the Moto mock for DynamoDB and create tables with sample data for users and questions.
    """
    mock = mock_aws()
    mock.start()

    # Setup mocked DynamoDB for Users
    dynamodb = boto3.resource("dynamodb", region_name=region)
    user_table = dynamodb.create_table(
        TableName=user_table_name,
        KeySchema=[
            {"AttributeName": "username", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "username", "AttributeType": "S"},
            {"AttributeName": "xp", "AttributeType": "N"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
        GlobalSecondaryIndexes=[
            {
                "IndexName": "XpIndex",
                "KeySchema": [
                    {"AttributeName": "username", "KeyType": "HASH"},
                    {"AttributeName": "xp", "KeyType": "RANGE"},
                ],
                "Projection": {"ProjectionType": "ALL"},
            }
        ],
    )

    # Insert sample user data
    with user_table.batch_writer() as batch:
        batch.put_item({"username": "mock_user", "xp": 123})
        batch.put_item({"username": "super_real_user", "xp": 200})

    print(f"Mock DynamoDB setup complete with Users table {user_table_name}.")

    # Setup mocked DynamoDB for Questions
    questions_table = dynamodb.create_table(
        TableName=questions_table_name,
        KeySchema=[
            {"AttributeName": "quizID", "KeyType": "HASH"},
            {"AttributeName": "questionID", "KeyType": "RANGE"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "quizID", "AttributeType": "S"},
            {"AttributeName": "questionID", "AttributeType": "S"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
    )

    # Insert sample questions data
    question_sets = get_all_question_sets(data)
    with questions_table.batch_writer() as batch:
        for quiz_id, questions in question_sets.items():
            for idx, question in enumerate(questions):
                question_id = str(idx + 1)  # Numeric question ID within the quiz
                batch.put_item({
                    'quizID': quiz_id,
                    'questionID': question_id,
                    'text': question['text'],
                    'answers': question['answers'],
                    'correctAnswer': question['correctAnswer'],
                })

    print(f"Mock DynamoDB setup complete with Questions table {questions_table_name}.")
    return mock


def stop_aws_mock(mock: MockAWS):
    """
    Stop the Moto mock for DynamoDB.
    """
    if mock:
        print("Stopping Moto mocking for DynamoDB.")
        mock.stop()
