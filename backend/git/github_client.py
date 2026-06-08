import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

_gh = Github(os.getenv("GITHUB_TOKEN"))


def fetch_pr_files(pr_url: str) -> list[dict]:
    """
    Given a GitHub PR URL like:
      https://github.com/owner/repo/pull/42
    Return a list of dicts: {filename, language, content}
    """
    # Parse URL
    parts = pr_url.rstrip("/").split("/")
    # Expected: ['https:', '', 'github.com', 'owner', 'repo', 'pull', '42']
    owner = parts[3]
    repo_name = parts[4]
    pr_number = int(parts[6])

    repo = _gh.get_repo(f"{owner}/{repo_name}")
    pr = repo.get_pull(pr_number)

    files = []
    for f in pr.get_files():
        if f.patch is None:
            continue
        files.append({
            "filename": f.filename,
            "content": f.patch,  # the diff/patch text
        })

    return files
