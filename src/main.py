from fastapi import FastAPI

from routes import router

app = FastAPI(title="FLyFood API")
app.include_router(router)

# From the project root: .venv/bin/uvicorn main:app --app-dir src --reload
