import json
from pathlib import Path


PROJECT_DIR_PATH = Path(__file__).resolve().parents[1]
CONFIG_FILE_PATH = PROJECT_DIR_PATH / "web" / "public" / "config.json"

if not CONFIG_FILE_PATH.exists():
    raise FileNotFoundError("Config file not found. Please create a config.json file in the web/public directory.")
CONFIG = json.loads(CONFIG_FILE_PATH.read_text())
LOCAL_API_URL = CONFIG.get("apiUrl")
LOCAL_API_HOST = LOCAL_API_URL.split(":")[1].replace("//", "")
API_PORT = int(LOCAL_API_URL.split(":")[2])

LOCAL_DYNAMODB_TABLE_NAME_APP_PREFIX = "corp-life"
LOCAL_DYNAMODB_TABLE_NAME_PREFIX = f"{LOCAL_DYNAMODB_TABLE_NAME_APP_PREFIX}_local"
DYNAMODB_TABLE_NAME_USER = f"{LOCAL_DYNAMODB_TABLE_NAME_PREFIX}_users"
DYNAMODB_TABLE_NAME_QUIZ = f"{LOCAL_DYNAMODB_TABLE_NAME_PREFIX}_quizzes"
DYNAMODB_TABLE_NAME_QUESTION = f"{LOCAL_DYNAMODB_TABLE_NAME_PREFIX}_questions"
DYNAMODB_TABLE_NAME_QUIZ_RECORD = f"{LOCAL_DYNAMODB_TABLE_NAME_PREFIX}_quiz_records"
