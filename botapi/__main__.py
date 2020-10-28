import uvicorn
from botapi import app, config, PORT
from botapi.methods import ALL_METHODS
import importlib

for method in ALL_METHODS:
    imported_module = importlib.import_module("botapi.methods." + method)
    importlib.reload(imported_module)

if __name__ == "__main__":
    importlib.reload(importlib.import_module("botapi.methods"))
    uvicorn.run("botapi:app", host="0.0.0.0", port=int(PORT or config.get('server', 'port')), log_level="info")
