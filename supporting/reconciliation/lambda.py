import os
import logging
import boto3
from botocore.exceptions import ClientError

# Log config
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
logging.getLogger().setLevel(LOG_LEVEL)
logger = logging.getLogger()

# Initialize clients
cognito_client = boto3.client('cognito-idp')
dynamodb_client = boto3.resource('dynamodb')

# Environment variables
USER_POOL_ID = os.environ.get("USER_POOL_ID")
DYNAMODB_TABLE_NAME = os.environ.get("DYNAMODB_TABLE_NAME")

# Reference to the DynamoDB table
table = dynamodb_client.Table(DYNAMODB_TABLE_NAME)

def list_cognito_users():
    """Fetch all users in the Cognito User Pool."""
    cognito_users = set()
    try:
        logger.debug("Starting to fetch users from Cognito.")
        paginator = cognito_client.get_paginator('list_users')
        for page in paginator.paginate(UserPoolId=USER_POOL_ID):
            for user in page['Users']:
                cognito_users.add(user['Username'])
                logger.debug(f"Added Cognito user: {user['Username']}")
        logger.info(f"Fetched {len(cognito_users)} users from Cognito.")
    except ClientError as e:
        logger.error(f"Error listing Cognito users: {e}")
    
    return cognito_users

def list_dynamodb_users():
    """Fetch all user IDs stored in DynamoDB."""
    dynamodb_users = set()
    try:
        logger.debug("Starting to fetch users from DynamoDB.")
        response = table.scan()
        for item in response['Items']:
            dynamodb_users.add(item['username'])
            logger.debug(f"Added DynamoDB user: {item['username']}")
        
        # Handling pagination if necessary
        while 'LastEvaluatedKey' in response:
            logger.debug("Fetching next page of DynamoDB users.")
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            for item in response['Items']:
                dynamodb_users.add(item['username'])
                logger.debug(f"Added DynamoDB user from next page: {item['username']}")
        
        logger.info(f"Fetched {len(dynamodb_users)} users from DynamoDB.")
    except ClientError as e:
        logger.error(f"Error listing DynamoDB users: {e}")
    
    return dynamodb_users

def delete_dynamodb_user(username):
    """Delete a user from DynamoDB by username."""
    try:
        logger.debug(f"Attempting to delete DynamoDB user: {username}")
        table.delete_item(
            Key={
                'username': username
            }
        )
        logger.info(f"Deleted user {username} from DynamoDB.")
    except ClientError as e:
        logger.error(f"Error deleting user {username} from DynamoDB: {e}")

def handler(event, context):
    logger.info("Starting user reconciliation process.")

    # Step 1: Get all users in Cognito and DynamoDB
    cognito_users = list_cognito_users()
    dynamodb_users = list_dynamodb_users()

    # Step 2: Find users in DynamoDB that are not in Cognito
    orphaned_users = dynamodb_users - cognito_users
    logger.debug(f"Identified {len(orphaned_users)} orphaned users in DynamoDB.")

    # Step 3: Delete orphaned users from DynamoDB
    for username in orphaned_users:
        delete_dynamodb_user(username)

    logger.info(f"Reconciliation complete. Removed {len(orphaned_users)} orphaned users from DynamoDB.")
    return {
        'statusCode': 200,
        'body': f"Reconciliation complete. Removed {len(orphaned_users)} orphaned users from DynamoDB."
    }
