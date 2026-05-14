import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_preflight_runner_produces_presence_input_with_missing_artifacts(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    outdir = tmp_path / "receipts"

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n  - filename: b.pdf\n    doc_id: kfm://doc/b\n    status: missing\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--output-dir",
        str(outdir),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["check_returncode"] == 1
    assert payload["render_returncode"] == 0
    assert payload["presence_input"] == {"present": {"a.pdf": False, "b.pdf": False}}
    assert payload["check_receipt"].endswith(".json")
    assert len(payload["check_receipt_sha256"]) == 64
    assert "provenance_returncode" in payload
    assert payload["provenance_payload"]["check"] == "required_doctrine_artifact_provenance"
    assert "provenance_sync_returncode" in payload
    assert payload["provenance_sync_payload"]["check"] == "sync_doctrine_artifact_provenance_status"
    assert payload["provenance_sync_receipt"].endswith(".json")
    assert len(payload["provenance_sync_receipt_sha256"]) == 64
    assert payload["artifact_paths"]["check_receipt"] == payload["check_receipt"]
    assert payload["artifact_paths"]["provenance_sync_receipt"] == payload["provenance_sync_receipt"]
    assert payload["artifact_digests"]["check_receipt"] == payload["check_receipt_sha256"]
    assert payload["artifact_digests"]["provenance_sync_receipt"] == payload["provenance_sync_receipt_sha256"]
    assert "alignment_returncode" in payload
    assert payload["readiness_payload"]["check"] == "normalized_summary_consumer_readiness"
    assert payload["alignment_payload"]["check"] == "doctrine_registry_alignment"
    assert Path(payload["check_receipt"]).name.startswith("check_required_doctrine_artifacts")
    assert Path(payload["check_receipt"]).exists()


def test_preflight_runner_strict_mode_fails_when_artifacts_missing(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--strict",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1


def test_preflight_runner_stable_filename_mode(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    outdir = tmp_path / "receipts"

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--output-dir",
        str(outdir),
        "--stable-filenames",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert Path(payload["check_receipt"]).name == "check_required_doctrine_artifacts.json"


def test_preflight_skips_render_when_check_has_registry_error(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text("required_doctrine_artifacts:\n", encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 2
    payload = json.loads(res.stdout)
    assert payload["check_returncode"] == 2
    assert payload["render_returncode"] == 2
    assert payload["render_stderr"] == "skipped_due_to_check_error"
    assert payload["presence_input"] is None


def test_preflight_writes_presence_output_when_requested(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    outdir = tmp_path / "receipts"
    presence_out = tmp_path / "presence.json"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--output-dir",
        str(outdir),
        "--presence-output",
        str(presence_out),
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["presence_output"] == str(presence_out)
    assert len(payload["presence_output_sha256"]) == 64
    assert payload["artifact_paths"]["presence_output"] == payload["presence_output"]
    assert payload["artifact_digests"]["presence_output"] == payload["presence_output_sha256"]
    assert presence_out.exists()


def test_preflight_runner_strict_provenance_mode_fails_when_provenance_gate_fails(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()

    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )

    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--strict-provenance",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1


def test_preflight_runner_emit_normalized_only_drops_legacy_fields(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--emit-normalized-only",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert "artifact_paths" in payload and "artifact_digests" in payload
    assert "check_receipt" not in payload
    assert "check_receipt_sha256" not in payload
    assert "provenance_sync_receipt" not in payload
    assert "provenance_sync_receipt_sha256" not in payload
def test_preflight_runner_require_consumer_readiness_flag(tmp_path: Path):
    registry = tmp_path / "registry.yaml"
    artifacts = tmp_path / "artifacts"
    artifacts.mkdir()
    registry.write_text(
        """required_doctrine_artifacts:\n  - filename: a.pdf\n    doc_id: kfm://doc/a\n    status: missing\n""",
        encoding="utf-8",
    )
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "maintenance" / "run_doctrine_artifact_preflight.py"),
        "--registry",
        str(registry),
        "--artifacts-dir",
        str(artifacts),
        "--require-consumer-readiness",
    ]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 0
    payload = json.loads(res.stdout)
    assert payload["readiness_returncode"] == 0
