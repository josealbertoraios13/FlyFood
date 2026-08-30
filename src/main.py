from fastapi import FastAPI

from routes import router

app = FastAPI(title="FLyFood API")
app.include_router(router)

# uvicorn main:app --reload