"""Starts local server for development."""

import uvicorn

from api import app
from api.old_config import API_HOST, API_PORT


RELOAD = True
ENTRYPOINT = "main:app"

if __name__ == "__main__":
    uvicorn.run(ENTRYPOINT, host=API_HOST, port=API_PORT, reload=RELOAD)