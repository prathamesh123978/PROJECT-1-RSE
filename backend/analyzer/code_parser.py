import ast
import textwrap


def chunk_code(code: str, max_chars: int = 3000) -> list[str]:
    """Split code into chunks under max_chars so it fits in LLM context."""
    if len(code) <= max_chars:
        return [code]

    lines = code.splitlines(keepends=True)
    chunks = []
    current = []
    current_len = 0

    for line in lines:
        if current_len + len(line) > max_chars and current:
            chunks.append("".join(current))
            current = []
            current_len = 0
        current.append(line)
        current_len += len(line)

    if current:
        chunks.append("".join(current))

    return chunks


def detect_language(filename: str) -> str:
    ext_map = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".go": "Go",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".rb": "Ruby",
        ".php": "PHP",
    }
    for ext, lang in ext_map.items():
        if filename.endswith(ext):
            return lang
    return "auto"


def extract_python_structure(code: str) -> dict:
    """Parse Python AST to extract function/class names."""
    try:
        tree = ast.parse(textwrap.dedent(code))
        functions = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
        classes = [n.name for n in ast.walk(tree) if isinstance(n, ast.ClassDef)]
        return {"functions": functions, "classes": classes}
    except SyntaxError:
        return {"functions": [], "classes": []}
