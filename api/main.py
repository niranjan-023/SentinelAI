
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SRC_PATH = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_PATH)

from predict import predict_content

app = FastAPI(
    title="SentinelAI API",
    description="AI-Powered Content Moderation System",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContentRequest(BaseModel):
    text: str

@app.get("/")
def home():

    return {
        "message": "SentinelAI API is running"
    }

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }

@app.post("/predict")
def predict(request: ContentRequest):

    result = predict_content(request.text)

    return result
