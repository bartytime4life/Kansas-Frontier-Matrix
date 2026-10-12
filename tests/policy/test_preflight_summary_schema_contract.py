import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas" / "contracts" / "v1" / "source" / "doctrine_artifact_preflight_summary.schema.json"


def _run_preflight(registry: Path, artifacts_dir: Path, outdir: Path) -> tuple[int, dict]:
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts_dir),
        "--output-dir",
        str(outdir),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    return res.returncode, json.loads(res.stdout)


def test_preflight_summary_output_conforms_schema_for_fail_state(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    receipts = tmp_path / "receipts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )

    code, payload = _run_preflight(registry, artifacts, receipts)
    assert code == 0

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(payload), key=lambda e: list(e.path))
    assert not errors


def test_preflight_summary_output_conforms_schema_for_error_state(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    receipts = tmp_path / "receipts"
    artifacts.mkdir()
    registry.write_text("required_doctrine_artifacts:\n", encoding="utf-8")

    code, payload = _run_preflight(registry, artifacts, receipts)
    assert code == 2

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(payload), key=lambda e: list(e.path))
    assert not errors
