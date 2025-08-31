import os
from contextlib import asynccontextmanager
from fastapi import FastAPI
from api.db import db_init
from api.chat.routing import router as chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_init()
    yield

app = FastAPI(lifespan=lifespan, title="AI Agent")
app.include_router(chat_router, prefix="/api/chats", tags=["Chats"])

API_KEY = os.environ.get("API_KEY")

@app.get("/")
def read_index():
    return {"hello": "world! go ahead"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}