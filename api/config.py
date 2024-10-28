import os
from dotenv import load_dotenv

load_dotenv("../.env")

# backend api
API_HOST = os.getenv("VITE_API_HOST")
API_PORT = int(os.getenv("VITE_API_PORT"))

# fronetend web app
WEB_HOST = os.getenv("WEB_HOST")
WEB_PORT = int(os.getenv("WEB_PORT"))
WEB_URL = f"http://{WEB_HOST}:{WEB_PORT}"
