from datetime import datetime


def review_document(code: str, language: str, result: dict, source: str = "paste") -> dict:
    """Build a MongoDB document for a completed review."""
    return {
        "source": source,            # "paste" or "github"
        "language": language,
        "code_snippet": code[:500],  # store first 500 chars only
        "bugs": result.get("bugs", []),
        "code_smells": result.get("code_smells", []),
        "security_issues": result.get("security_issues", []),
        "performance_issues": result.get("performance_issues", []),
        "quality_score": result.get("quality_score", 0),
        "summary": result.get("summary", ""),
        "created_at": datetime.utcnow(),
    }
