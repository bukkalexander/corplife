# Quiz app


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

```bash
npm run build
```

The build can be found under `dist`

### Run unit tests (react components)

```bash
npm run test
```