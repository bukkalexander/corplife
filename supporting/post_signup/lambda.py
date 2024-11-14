# lambda_function.py

import os
import logging
import boto3
from botocore.exceptions import ClientError

# Log config
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.getLogger().setLevel(LOG_LEVEL)
logger = logging.getLogger()

DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME")

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(DYNAMODB_TABLE_NAME)

def handler(event, context):
    # Ensure it's triggered on PostConfirmation event
    if event['triggerSource'] == 'PostConfirmation_ConfirmSignUp':
        username = event['userName']
        # Keeping this in case we want more solid user representation
        # username = event['request']['userAttributes']['sub']

        item = {
            'username': username,
            'score': 0
        }

        try:
            table.put_item(Item=item)
            logging.info(f"User {username} added to DynamoDB with initial score of 0")
        except ClientError as e:
            logging.error(f"Error adding user {username} to DynamoDB: {e.response['Error']['Message']}")

    return event
