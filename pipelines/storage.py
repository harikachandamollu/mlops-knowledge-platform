from pathlib import Path

def save_raw(path: Path, name: str, content: str):
    file_path = path / f"{name}.html"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)

def save_processed(path: Path, name: str, content: str):
    file_path = path / f"{name}.txt"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)