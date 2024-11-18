
## AWS Lambda Event Mocking and Testing Tool (AWS EVENT CLI)

This tool simplifies the process of creating and testing payloads that mimic AWS API Gateway events for Lambda functions. 
It is especially useful for locally testing FastAPI endpoints secured by a Cognito Authorizer without the need to manually handle complex AWS payload structures.

### Features

- Generates mock AWS event payloads for Lambda functions.
- Simulates local requests to a FastAPI application using Mangum.
- Sends HTTP requests to local or remote URLs with generated payloads.
- Supports saving generated payloads to a file for reuse.


### Usage

#### Starting the FastAPI Server Locally

To test locally, first start the FastAPI application using Uvicorn. Run the following command:

```bash
python main.py
```

This will start the FastAPI application on `localhost:8181`.


#### CLI Options

```bash
python aws_event_cli.py --username <USERNAME> --url <URL> [OPTIONS]
```

| Option          | Description                                                                 | Required |
|------------------|-----------------------------------------------------------------------------|----------|
| `--username`    | Username to include in the mock event payload.                              | Yes      |
| `--email`       | Email to include in the mock event payload. Default: `test@example.com`.    | No       |
| `--http-method` | HTTP method for the request. Default: `GET`.                                | No       |
| `--url`         | Target URL to send the request.                                             | Yes      |
| `--output`      | File to save the generated payload (optional).                              | No       |

#### Example Commands

1. **Generate a mock payload and send a local request**

   ```bash
   python main.py --username testuser --url http://localhost:8181/user/profile --http-method GET
   ```

2. **Generate a mock payload and save it to a file**

   ```bash
   python main.py --username testuser --url http://localhost:8181/user/profile --output payload.json
   ```

3. **Send the payload to a remote endpoint**

   ```bash
   python main.py --username testuser --url https://api.example.com/user/profile
   ```

### Local Testing

For local endpoints, the tool uses `Mangum` to simulate AWS Lambda and API Gateway event handling. This eliminates the need for deploying to AWS to test Cognito-secured endpoints.

### Remote Testing

If the provided URL points to a remote server, the tool uses `requests` to send the payload. Make sure the target endpoint is accessible and configured to handle API Gateway events.

### Saving Payloads

To save a generated payload for later use, specify the `--output` option:

```bash
python aws_event_cli.py --username testuser --url http://localhost:8181/user/profile --output payload.json
```

### Error Handling

If errors occur during payload generation, local simulation, or remote requests, the tool provides detailed error messages to help debug the issue.

