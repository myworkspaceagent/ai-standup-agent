from fastapi import APIRouter
from services.summary_service import generate_daily_summary

router = APIRouter()

@router.get("/generate/summary")
def generate_summary():
    summary = generate_daily_summary()
    return {"summary": summary}
