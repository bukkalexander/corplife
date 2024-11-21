import boto3
from moto import mock_aws
from moto.core.models import MockAWS

def start_aws_mock(region, user_table_name) -> MockAWS:
    """
    Start the Moto mock for DynamoDB and create a table with sample data.
    """
    mock = mock_aws()
    mock.start()

    # Setup mocked DynamoDB for Users
    dynamodb = boto3.resource("dynamodb", region_name=region)
    table = dynamodb.create_table(
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

    # Insert sample data
    with table.batch_writer() as batch:
        batch.put_item({"username": "mock_user", "xp": 123})
        batch.put_item({"username": "super_real_user", "xp": 200})

    print(f"Mock DynamoDB setup complete with table {user_table_name}.")
    return mock

def stop_aws_mock(mock: MockAWS):
    """
    Stop the Moto mock for DynamoDB.
    """
    if mock:
        print("Stopping Moto mocking for DynamoDB.")
        mock.stop()
