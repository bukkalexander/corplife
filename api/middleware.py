from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from starlette.types import ASGIApp

class MockRequestMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        if request.scope["type"] == "http":
            # Check for custom mock username header
            mock_user = request.headers.get("X-Mock-User", "mock_user")

            # Create a mock AWS event
            mock_event = {
                "requestContext": {
                    "authorizer": {
                        "claims": {
                            "cognito:username": mock_user
                        }
                    }
                }
            }
            # Add the mocked AWS event to the scope
            request.scope["aws.event"] = mock_event

        # Pass the request to the next middleware or endpoint
        response = await call_next(request)
        return response
