from pydantic import BaseModel
from typing import Optional


class CodeReviewRequest(BaseModel):
    code: str
    language: Optional[str] = "auto"
    filename: Optional[str] = ""


class GithubReviewRequest(BaseModel):
    pr_url: str


class Bug(BaseModel):
    line: Optional[int] = None
    description: str
    severity: str
    fix: str


class CodeSmell(BaseModel):
    description: str
    suggestion: str


class SecurityIssue(BaseModel):
    description: str
    fix: str


class PerformanceIssue(BaseModel):
    description: str
    suggestion: str


class ReviewResponse(BaseModel):
    review_id: Optional[str] = None
    bugs: list
    code_smells: list
    security_issues: list
    performance_issues: list
    quality_score: int
    summary: str
