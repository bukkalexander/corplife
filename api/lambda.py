"""Entrypoint for lambda function in aws."""
from mangum import Mangum
from api import app


handler = Mangum(app)
