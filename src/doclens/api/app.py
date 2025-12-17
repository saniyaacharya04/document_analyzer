from fastapi import FastAPI
from pydantic import BaseModel

from doclens.core.analyzer import analyze_url

app = FastAPI(title="DocLens AI API")

class AnalyzeRequest(BaseModel):
    url: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(req: AnalyzeRequest):
    return analyze_url(req.url)
