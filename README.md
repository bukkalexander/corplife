
# Quiz App

## Overview

The Quiz App includes two main parts:
- **Frontend**: Located in the `web` directory, this contains the React-based UI for the app.
- **Backend and Infrastructure**: Managed under the `infra` directory, this includes setup for Lambda functions, OpenTofu (Terraform equivalent) infrastructure configuration, and dependency packaging.

This project uses `make` commands to simplify setup and deployment, with specific `make` targets for common workflows.

## Quick Start with Make

This app leverages `make` for efficient setup and deployment of both the backend and infrastructure. Here are some high-level `make` commands to get started quickly:

### Preparation Commands

- **Prepare Archives**: Packages dependencies and archives code for deployment.
  ```bash
  make prepare
  ```
  This command:
  - Installs Python dependencies for the Lambda function.
  - Creates an archive of the function code and its dependencies, ready for deployment to AWS Lambda.

### Infrastructure Commands

The infrastructure is managed using OpenTofu (similar to Terraform). The following commands initialize, plan, and apply infrastructure changes using OpenTofu configurations located in `infra/main`.

- **Initialize, Plan, and Apply Infrastructure**:
  ```bash
  make tofu-all
  ```
  This command runs the entire OpenTofu workflow, executing the following steps in sequence:
  - Initializes the environment (`tofu-init`).
  - Creates an infrastructure plan (`tofu-plan`).
  - Applies the saved plan (`tofu-apply`), ensuring exact changes are deployed as per the planned configuration.

- **Other Infrastructure Commands**:
  - **Initialize Only**:
    ```bash
    make tofu-init
    ```
  - **Plan Only**:
    ```bash
    make tofu-plan
    ```
  - **Apply a Saved Plan**:
    ```bash
    make tofu-apply
    ```
  - **Destroy Infrastructure**:
    ```bash
    make tofu-destroy
    ```

- **Clean Up Generated Files**:
  ```bash
  make clean
  ```
  Removes all generated archives and build artifacts.

---

## Web

The frontend part of the app is located in the `web` directory.

### Requirements

You need `npm` to build the web app. You can either:
- Use the `.devcontainer/devcontainer.json` to launch a dev container in VS Code, using the Dev Containers extension.
- Manually run the `.devcontainer/Dockerfile`.
- Install `npm` locally.

### Change Directory into `web`

All frontend-related commands take place inside the `web` directory:

```bash
cd web
```

### Install

Install React app dependencies:

```bash
npm install
```

### Dev / Debug

Build for development with hot reload:

```bash
npm run dev
```

You can also debug with VS Code using the following `.vscode/launch.json` configuration:

```json
{
    "configurations": [
        {
            "type": "chrome",
            "name": "http://localhost:5173/",
            "request": "launch",
            "url": "http://localhost:5173/",
            "webRoot": "${workspaceFolder}/web/src"
        }
    ]
}
```

### Build for production
Don't forget to set environment variables for API endpoints before building. Take a look inside `.env`, and set the ones prefixed with `VITE_`.

```bash
npm run build
```

The production build can be found in the `dist` directory.

### Run Unit Tests (React Components)

```bash
npm run test
```
## api

Used by the web app for exchanging quiz data.

```bash
cd api
```

### Install FastAPI

`FastAPI` is the python API framework for creating APIs, and `Uvicorn` is the server program that hosts the FastAPI application.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirments.txt
```

### Run FastAPI server
Don't forget to override the default environment variables in `.env` if you are running in production. This is done by setting environment variables with the same name. Currently, this is used for configuring the server endpoint, and also to allow CORS (Cross-Origin Resource sharing) for the web app.

```bash
python main.py
```

---

## Additional Information

- For backend and infrastructure setup, see `infra/README.md` for further details on Lambda functions and infrastructure configurations.
- For custom setup of dependencies or infrastructure, refer to the specific make commands listed above.

This setup simplifies the deployment process by automating common tasks and dependencies, ensuring an efficient workflow for both local development and deployment.
