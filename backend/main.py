from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI(title="AI Platform", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PredictionRequest(BaseModel):
    input_text: str
    model_name: str = "default"

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    model_used: str

@app.get("/")
async def root():
    return {"message": "AI Platform API", "version": "1.0.0"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/models")
async def list_models():
    return {
        "models": ["text-classifier", "sentiment-analyzer", "text-generator"],
        "total": 3
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Mock prediction logic
    return PredictionResponse(
        prediction="Sample prediction result",
        confidence=0.95,
        model_used=request.model_name
    )

@app.post("/upload-model")
async def upload_model(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "status": "uploaded successfully"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
