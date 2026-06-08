import json
from llm.groq_client import call_groq
from llm.prompt_builder import build_review_prompt, build_system_prompt
from analyzer.code_parser import chunk_code


def analyze_code(code: str, language: str = "auto") -> dict:
    """
    Run full AI review on the given code.
    For large code, merge results from multiple chunks.
    """
    chunks = chunk_code(code)
    all_bugs = []
    all_smells = []
    all_security = []
    all_performance = []
    scores = []
    summaries = []

    for chunk in chunks:
        result = _review_chunk(chunk, language)
        all_bugs.extend(result.get("bugs", []))
        all_smells.extend(result.get("code_smells", []))
        all_security.extend(result.get("security_issues", []))
        all_performance.extend(result.get("performance_issues", []))
        if result.get("quality_score") is not None:
            scores.append(result["quality_score"])
        if result.get("summary"):
            summaries.append(result["summary"])

    avg_score = int(sum(scores) / len(scores)) if scores else 50

    return {
        "bugs": all_bugs,
        "code_smells": all_smells,
        "security_issues": all_security,
        "performance_issues": all_performance,
        "quality_score": avg_score,
        "summary": " ".join(summaries),
    }


def _review_chunk(code: str, language: str) -> dict:
    prompt = build_review_prompt(code, language)
    system = build_system_prompt()
    raw = call_groq(prompt, system)

    # Strip any accidental markdown fences
    raw = raw.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip().rstrip("```").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "bugs": [],
            "code_smells": [],
            "security_issues": [],
            "performance_issues": [],
            "quality_score": 50,
            "summary": raw[:500],
        }
