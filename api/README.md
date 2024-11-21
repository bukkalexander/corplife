
# Backend Local and Production Environment Documentation

## Overview

This documentation provides a comprehensive guide to running and testing the application backend in both **production** and **local development** environments. The guide covers:
- How the application resolves environment configurations.
- How the application uses middleware to inject mock AWS events.
- Local development with in-memory DynamoDB tables using `moto`.

---

## Production vs Local Development

### **Production**
- The application runs with real AWS infrastructure, including:
  - DynamoDB tables.
  - AWS API Gateway and Lambda.
  - Cognito for user authentication.

- No mocking tools are used, and all AWS services are accessed directly.

### **Local Development**
- The application runs on `localhost` with:
  - **Mock AWS events** injected via middleware.
  - **In-memory DynamoDB tables** created and managed by `moto`.
  - The ability to simulate different users via custom headers.

- **Key Differences:**
  - Middleware is added only in local environments to inject the AWS event context (`aws.event`) into requests.
  - DynamoDB tables are mocked using `moto` to avoid using real AWS resources.

---

## Configuration

### Environment Detection

The application determines whether it is running locally or in production based on the value of `API_HOST` from the configuration.

- **Localhost Detection:**
  ```python
  IS_LOCALHOST = API_HOST in ["localhost", "127.0.0.1"]
  ```
  If `IS_LOCALHOST` is `True`:
  - Middleware for mocking is added.
  - Mock DynamoDB tables are created using `moto`.

---

## Middleware for Mocking

### MockRequestMiddleware

This middleware is attached **only in local environments**. It:
- Injects a mock AWS event into the `request.scope`.
- Uses the `X-Mock-User` HTTP header to simulate different users.

[See middleware.py for more details](middleware.py)

### Usage
To simulate a different user in local development, include the `X-Mock-User` header in your request:
```bash
curl -H "X-Mock-User: test_user" http://localhost:8181/user/xp
```

---

## Mocking DynamoDB with `moto`

The application uses `moto` to mock DynamoDB tables in memory during local development.

### Setup
In local environments, the application:
1. Starts a `moto` mock instance.
2. Creates an in-memory DynamoDB table with predefined data.

[See mock.py for more details](mock.py)

### Clean Up
Ensure the `moto` mock is stopped after use:
```python
def stop_aws_mock(mock):
    if mock:
        mock.stop()
```

---

## Running the Application

### Local Development

1. **Start the Server:**
   ```bash
   python main.py
   ```

2. **Test Mocked Endpoints:**
   - Default user (`mock_user`):
     ```bash
     curl http://localhost:8181/user/xp
     ```

   - Simulate a different user (`test_user`):
     ```bash
     curl -H "X-Mock-User: test_user" http://localhost:8181/user/xp
     ```

3. **Verify Mocked DynamoDB Data:**
   - Example `GET` Request:
     ```bash
     curl http://localhost:8181/user/xp
     ```
   - Response:
     ```json
     {
         "username": "mock_user",
         "xp": 123
     }
     ```

### Production
1. Deploy the application to AWS Lambda.
2. Ensure all environment variables and AWS services are configured correctly.
3. Test endpoints with real AWS resources.

---

## Summary

This setup provides a seamless transition between local development and production environments. The middleware and `moto` ensure efficient local testing without requiring real AWS resources, while production uses actual AWS services for accurate data handling.
