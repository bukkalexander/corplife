# Social media app for learning


## Web
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