"""Starts local server for development."""

import uvicorn
from api.api import app
from api.config import Config
from api.old_config import API_HOST, API_PORT


RELOAD = True

config = Config()

create_dependencies(app, config)

if __name__ == "__main__":
    uvicorn.run(app, host=API_HOST, port=API_PORT, reload=RELOAD)