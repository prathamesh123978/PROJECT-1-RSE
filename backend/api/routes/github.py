from fastapi import APIRouter, HTTPException
from api.models import GithubReviewRequest
from git.github_client import fetch_pr_files
from git.diff_parser import extract_added_lines
from analyzer.bug_detector import analyze_code
from analyzer.code_parser import detect_language
from database.connection import get_db
from database.schemas import review_document

router = APIRouter()


@router.post("/review/github")
async def review_github_pr(request: GithubReviewRequest):
    try:
        files = fetch_pr_files(request.pr_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch PR: {str(e)}")

    if not files:
        raise HTTPException(status_code=404, detail="No reviewable files found in PR")

    all_results = []

    for f in files:
        code = extract_added_lines(f["content"])
        if not code.strip():
            continue

        language = detect_language(f["filename"])
        result = analyze_code(code, language)
        result["filename"] = f["filename"]
        all_results.append(result)

        # Save each file's review
        try:
            db = get_db()
            if db is not None:
                doc = review_document(code, language, result, source="github")
                doc["pr_url"] = request.pr_url
                doc["filename"] = f["filename"]
                await db.reviews.insert_one(doc)
        except Exception:
            pass

    return {"pr_url": request.pr_url, "files_reviewed": len(all_results), "results": all_results}
