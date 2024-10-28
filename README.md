# Quiz app

An app for playing a quiz online.

## Web

Fronted part of the app.

### Requirements

You need `npm` to build the web app. 
You can either:
- use the `.devcontainer/devcontainer.json` to launch a dev container in VS Code, using the Dev Containers extension
- manuallly run the `.devcontainer/Dockerfile`
- install `npm` locally

### Change directory into `web`

All frontend related commands take place inside the folder `web`

```bash
cd web
```

### Install
Install react app dependencies

```bash
npm install
```

###  Dev / debug
build for dev (Hot reload)

```bash
npm run dev
```

You can also debug with VS Code using the following `.vscode/launch.json` configuration

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

The build can be found under `dist`

### Run unit tests (react components)

```bash
npm run test
```

This is currently not used.

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
