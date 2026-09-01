from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from tools.validators.domains.fauna.validate_catalog_matrix import validate_catalog_matrix
from tools.validators.domains.fauna.validate_schema import validate_schema
from tools.validators.domains.fauna.validate_source_descriptor import validate_source_descriptor

REPO_ROOT = Path(__file__).resolve().parents[2]
README_PATH = REPO_ROOT / "docs" / "domains" / "fauna" / "README.md"


def test_fauna_readme_has_current_repository_grounded_status() -> None:
    text = README_PATH.read_text(encoding="utf-8")
    assert "repository-grounded" in text
    assert "Bounded validation" in text
    assert "CI TODO" not in text
    assert "CI: TODO" not in text
    assert "CI-todo" not in text.lower()


def test_fauna_validators_are_implemented_for_valid_candidates() -> None:
    source_descriptor = {
        "id": "kfm:source:fauna:synthetic:test",
        "source_family": "fauna",
        "source_type": "synthetic",
        "source_role": "synthetic",
        "rights_state": "approved",
        "sensitivity_state": "public_safe",
        "public_safe": True,
    }
    assert validate_source_descriptor(source_descriptor) == []

    catalog_matrix = {
        "id": "kfm:catalog:fauna:fixture-v1",
        "domain": "fauna",
        "version": "1.0",
        "entries": [
            {"id": "kfm:fauna:entry:001", "kind": "occurrence", "status": "active"}
        ],
    }
    assert validate_catalog_matrix(catalog_matrix) == []

    schema = {"type": "object", "properties": {"id": {"type": "string"}}}
    assert validate_schema(schema) == []


def test_fauna_cli_validators_do_not_raise_not_implemented(tmp_path: Path) -> None:
    valid_source = {
        "id": "kfm:source:fauna:cli:test",
        "source_family": "fauna",
        "source_type": "synthetic",
        "source_role": "synthetic",
        "rights_state": "approved",
        "sensitivity_state": "public_safe",
        "public_safe": True,
    }
    payload = tmp_path / "source_descriptor.json"
    payload.write_text(json.dumps(valid_source), encoding="utf-8")

    script = REPO_ROOT / "tools" / "validators" / "domains" / "fauna" / "validate_source_descriptor.py"
    result = subprocess.run(
        [sys.executable, str(script), str(payload)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr + result.stdout
    assert '"status":"PASS"' in result.stdout
