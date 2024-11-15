import os
import json
from pathlib import Path

# Define project path
PROJECT_DIR_PATH = Path(__file__).resolve().parents[1]

# Load configuration from JSON file if it exists
CONFIG_FILE_PATH = PROJECT_DIR_PATH / "web" / "public" / "config.json"
CONFIG = {}

if CONFIG_FILE_PATH.exists():
    CONFIG = json.loads(CONFIG_FILE_PATH.read_text())
else:
    print("Config file not found. Falling back to environment variables.")

# Backend API configuration
API_URL = CONFIG.get("apiUrl") or os.getenv("API_URL")
API_HOST = API_URL.split(":")[1].replace("//", "") if API_URL else None
API_PORT = int(API_URL.split(":")[2]) if API_URL else None

# AWS Region (used for local DynamoDB if applicable)
REGION = os.getenv("REGION", CONFIG.get("region", None))

# Load DynamoDB table names with fallback logic
DYNAMODB_TABLE_NAME_USERS = os.getenv("DYNAMODB_TABLE_NAME_USERS", CONFIG.get("DYNAMODB_TABLE_NAME_USERS", None))
DYNAMODB_TABLE_NAME_QUESTIONS = os.getenv("DYNAMODB_TABLE_NAME_QUESTIONS", CONFIG.get("DYNAMODB_TABLE_NAME_QUESTIONS", None))

# Validate critical configuration items
if not DYNAMODB_TABLE_NAME_USERS:
    raise ValueError("DYNAMODB_TABLE_NAME_USERS must be set in environment variables or config.json.")

if not DYNAMODB_TABLE_NAME_QUESTIONS:
    raise ValueError("DYNAMODB_TABLE_NAME_QUESTIONS must be set in environment variables or config.json.")
