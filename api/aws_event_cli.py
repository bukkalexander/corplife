import argparse
import json
import requests
from urllib.parse import urlparse
from typing import Any, Dict
from mangum import Mangum
from api import app  # Import your FastAPI app


def generate_mock_request_payload(
    username: str,
    email: str = "test@example.com",
    http_method: str = "GET"
) -> Dict[str, Any]:
    """
    Generates a mock AWS event payload for FastAPI's Request object.
    """
    aws_event = {
        "version": "1.0",
        "resource": "/user/{proxy+}",
        "httpMethod": http_method.upper(),
        "headers": {
            "Authorization": "Bearer mock-token",
            "User-Agent": "MockUserAgent",
        },
        "requestContext": {
            "authorizer": {
                "claims": {
                    "cognito:username": username,
                    "email": email,
                    "email_verified": "true",
                }
            }
        },
        "stageVariables": None,
        "body": None,
        "isBase64Encoded": False,
    }

    return aws_event


def simulate_local_request(path: str, payload: Dict[str, Any], method: str) -> Dict[str, Any]:
    """
    Simulates a local request to the FastAPI app using Mangum, matching the production AWS Lambda event structure.
    """
    # Generate a mock Lambda event
    event = {
        "version": "1.0",
        "resource": "/user/{proxy+}",
        "path": path,
        "httpMethod": method.upper(),
        "headers": {
            "Content-Length": "0",
            "Host": "localhost",
            "User-Agent": "MockUserAgent",
            "X-Amzn-Trace-Id": "Root=1-6735eeda-4c18714619f2a08a3c2ca9da",
            "X-Forwarded-For": "127.0.0.1",
            "X-Forwarded-Port": "80",
            "X-Forwarded-Proto": "http",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate",
            "authorization": "Bearer mock-token",
        },
        "multiValueHeaders": {
            "Content-Length": ["0"],
            "Host": ["localhost"],
            "User-Agent": ["MockUserAgent"],
            "X-Amzn-Trace-Id": ["Root=1-6735eeda-4c18714619f2a08a3c2ca9da"],
            "X-Forwarded-For": ["127.0.0.1"],
            "X-Forwarded-Port": ["80"],
            "X-Forwarded-Proto": ["http"],
            "accept": ["*/*"],
            "accept-encoding": ["gzip, deflate"],
            "authorization": ["Bearer mock-token"],
        },
        "requestContext": {
            "accountId": "mock-account-id",
            "apiId": "mock-api-id",
            "authorizer": {
                "claims": {
                    "cognito:username": payload["requestContext"]["authorizer"]["claims"]["cognito:username"],
                    "email": payload["requestContext"]["authorizer"]["claims"]["email"],
                    "email_verified": "true",
                }
            },
            "domainName": "localhost",
            "domainPrefix": "",
            "httpMethod": method.upper(),
            "identity": {
                "sourceIp": "127.0.0.1",
                "userAgent": "MockUserAgent",
            },
            "path": path,
            "protocol": "HTTP/1.1",
            "requestId": "mock-request-id",
            "requestTime": "14/Nov/2024:12:36:42 +0000",
            "requestTimeEpoch": 1731587802544,
            "resourceId": "ANY /user/{proxy+}",
            "resourcePath": "/user/{proxy+}",
            "stage": "$default",
        },
        "pathParameters": {"proxy": path.split("/")[-1]},
        "queryStringParameters": None,
        "multiValueQueryStringParameters": None,
        "stageVariables": None,
        "body": None if payload.get("body") is None else json.dumps(payload["body"]),
        "isBase64Encoded": False,
    }

    # Use Mangum to handle the event
    handler = Mangum(app)
    response = handler(event, {})
    return response


def send_request(url: str, payload: Dict[str, Any], method: str) -> requests.Response:
    """
    Sends a request with the given payload to the specified URL using the appropriate HTTP method.
    """
    headers = {"Content-Type": "application/json"}
    method = method.upper()

    # Use `requests.request` for dynamic HTTP method handling
    response = requests.request(method, url, headers=headers, json=payload)

    return response


def is_local_url(url: str) -> bool:
    """
    Checks if the given URL points to a localhost server.
    """
    parsed_url = urlparse(url)
    return parsed_url.hostname in ["localhost", "127.0.0.1"]


def main():
    parser = argparse.ArgumentParser(description="CLI tool to generate AWS event payload and send requests.")
    parser.add_argument("--username", required=True, help="Username to include in the mock event payload.")
    parser.add_argument("--email", default="test@example.com", help="Email to include in the mock event payload.")
    parser.add_argument("--http-method", default="GET", help="HTTP method for the request (default: GET).")
    parser.add_argument("--url", required=True, help="Target URL to send the request.")
    parser.add_argument("--output", help="File to save the generated payload (optional).")

    args = parser.parse_args()

    # Extract path from URL
    parsed_url = urlparse(args.url)
    path = parsed_url.path

    # Generate the payload
    payload = generate_mock_request_payload(
        username=args.username,
        email=args.email,
        http_method=args.http_method
    )

    # Optionally save to file
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(payload, f, indent=4)
        print(f"Payload saved to {args.output}")

    # Check if the URL is local and invoke Mangum directly if true
    if is_local_url(args.url):
        try:
            response = simulate_local_request(path, payload, args.http_method)
            print(f"Response Status: {response['statusCode']}")
            print(f"Response Body: {response['body']}")
        except Exception as e:
            print(f"Error occurred during local simulation: {e}")
    else:
        # Otherwise, send the request over HTTP
        try:
            response = send_request(args.url, payload, args.http_method)
            print(f"Response Status: {response.status_code}")
            print(f"Response Body: {response.text}")
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
