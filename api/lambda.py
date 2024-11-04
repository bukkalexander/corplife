"""Entrypoint for lambda function in aws."""
import mangum
from api import app


handler = mangum(app)
