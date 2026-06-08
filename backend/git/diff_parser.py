def extract_added_lines(patch: str) -> str:
    """From a git diff patch, extract only the added lines (lines starting with '+')."""
    lines = patch.splitlines()
    added = [l[1:] for l in lines if l.startswith("+") and not l.startswith("+++")]
    return "\n".join(added)
