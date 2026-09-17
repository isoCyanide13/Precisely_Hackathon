from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/health", response_model=Dict[str, str], status_code=200)
def health_check() -> Dict[str, str]:
    """Health check endpoint to verify backend service liveness."""
    return {"status": "ok", "message": "Backend service is operational"}
