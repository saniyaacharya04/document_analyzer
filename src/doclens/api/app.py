from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Dict

from doclens.core.analyzer import analyze_url

app = FastAPI(
    title="DocLens AI API",
    description="Analyze technical documentation for quality, clarity, and structure.",
    version="1.0.0"
)

# ======================================================
# Request / Response Schemas
# ======================================================

class AnalyzeRequest(BaseModel):
    url: str = Field(
        ...,
        example="https://help.moengage.com/hc/en-us/articles/4415622460948-Push-Templates",
        description="Publicly accessible documentation URL"
    )

class TextAssessment(BaseModel):
    assessment: str

class AnalyzeResponse(BaseModel):
    url: str
    readability: Dict[str, float]
    structure_and_flow: TextAssessment
    completeness_and_examples: TextAssessment
    style_guidelines: TextAssessment

class HealthResponse(BaseModel):
    status: str = "ok"

# ======================================================
# API Endpoints
# ======================================================

@app.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Liveness probe for monitoring and orchestration."
)
def health():
    return {"status": "ok"}


@app.post(
    "/analyze",
    response_model=AnalyzeResponse,
    summary="Analyze a documentation page",
    description="Fetches documentation from a URL and returns structured quality analysis."
)
def analyze(req: AnalyzeRequest):
    return analyze_url(req.url)
