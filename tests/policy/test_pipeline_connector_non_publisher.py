from tests.policy.boundary_constants import FORBIDDEN_INTERNAL_STORE_PATHS
from pathlib import Path
import re

ROOTS = [Path("connectors"), Path("pipelines")]
FORBIDDEN_TARGETS = ("data/catalog", "data/published", "release/")
WRITE_CALL_PATTERN = re.compile(r"\b(write_text|write_bytes|open\s*\(|to_csv\s*\(|to_parquet\s*\(|dump\s*\()")


def test_connectors_and_pipelines_do_not_write_to_publish_targets() -> None:
    for root in ROOTS:
        for py_file in root.rglob("*.py"):
            text = py_file.read_text(encoding="utf-8")
            lines = text.splitlines()
            for idx, line in enumerate(lines, start=1):
                if not WRITE_CALL_PATTERN.search(line):
                    continue
                # check local context window for dangerous target literals
                window = "\n".join(lines[max(0, idx - 3): min(len(lines), idx + 2)])
                for target in FORBIDDEN_TARGETS:
                    assert target not in window, (
                        f"Forbidden publish-target write context in {py_file}:{idx} -> {target}"
                    )
