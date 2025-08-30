import os
from fastapi import FastAPI

app = FastAPI()

API_KEY = os.environ.get("API_KEY")

@app.get("/")
def read_index():
    return {"hello": "world! go ahead"}

@app.get("/healthz")
def health_check():
    return {"status": "ok"}