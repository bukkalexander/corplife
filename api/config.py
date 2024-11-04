import json
from pathlib import Path

PROJECT_DIR_PATH = Path(__file__).resolve().parents[1]

# backend api server
CONFIG_FILE_PATH = PROJECT_DIR_PATH / "web" / "public" / "config.json"
CONFIG = json.loads(CONFIG_FILE_PATH.read_text())

API_URL = CONFIG["apiUrl"]
API_HOST = API_URL.split(":")[1].replace("//", "")
API_PORT = int(API_URL.split(":")[2])
