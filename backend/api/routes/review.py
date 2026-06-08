from fastapi import APIRouter, HTTPException
from api.models import CodeReviewRequest, ReviewResponse
from analyzer.bug_detector import analyze_code
from analyzer.code_parser import detect_language
from datetime import datetime
import uuid

router = APIRouter()

# In-memory storage (no MongoDB needed)
review_store = {}


@router.post("/review", response_model=ReviewResponse)
async def review_code(request: CodeReviewRequest):
    if not request.code.strip():
        raise HTTPException(status_code=400, detail="Code cannot be empty")

    language = request.language
    if language == "auto" and request.filename:
        language = detect_language(request.filename)

    try:
        result = analyze_code(request.code, language)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI review failed: {str(e)}")

    # Save to memory
    review_id = str(uuid.uuid4())
    review_store[review_id] = {
        "id": review_id,
        "language": language,
        "source": "paste",
        "code_snippet": request.code[:500],
        "created_at": datetime.utcnow().isoformat(),
        **result
    }

    return ReviewResponse(review_id=review_id, **result)