from pathlib import Path
import re

ROOTS = [Path("connectors"), Path("pipelines")]
FORBIDDEN_TARGETS = ("data/catalog", "data/published", "release/")
PY_WRITE_CALL_PATTERN = re.compile(r"\b(write_text|write_bytes|open\s*\(|to_csv\s*\(|to_parquet\s*\(|dump\s*\()")
SHELL_WRITE_PATTERN = re.compile(r"\b(cp|mv|rsync|cat\s+.*>|tee)\b")


def _iter_files(root: Path):
    for ext in ("*.py", "*.sh", "*.yaml", "*.yml"):
        yield from root.rglob(ext)


def test_connectors_and_pipelines_do_not_write_to_publish_targets() -> None:
    for root in ROOTS:
        for file_path in _iter_files(root):
            text = file_path.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, start=1):
                is_write_context = bool(PY_WRITE_CALL_PATTERN.search(line) or SHELL_WRITE_PATTERN.search(line))
                if not is_write_context:
                    continue
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 2)])
                for target in FORBIDDEN_TARGETS:
                    assert target not in window, (
                        f"Forbidden publish-target write context in {file_path}:{idx} -> {target}"
                    )
