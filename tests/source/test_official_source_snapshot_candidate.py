import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).parents[2]
MODULE_PATH = ROOT / "tools/validators/source/official_source_snapshot_candidate.py"
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/source/official_source_snapshot_candidate"
SPEC = importlib.util.spec_from_file_location("official_source_snapshot_candidate", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_local_payload_build_is_deterministic_and_non_authoritative():
    built = MODULE.build_captured_candidate(
        FIXTURE_ROOT / "payloads/demo.json",
        source_id="source:demo-official",
        source_url="https://example.gov/demo.json",
        retrieved_at="2026-08-08T01:30:00Z",
        http_status=200,
        media_type="application/json",
        etag="demo-v1",
        last_modified="2026-08-08T01:00:00Z",
    )
    assert built == load(FIXTURE_ROOT / "valid/captured.json")
    assert MODULE.validate_doc(built) == []
    assert built["source_activation_authorized"] is False
    assert built["evidence_bundle_emitted"] is False
    assert built["public_use_allowed"] is False


def test_authority_escalation_fixture_fails_closed():
    errors = MODULE.validate_doc(load(FIXTURE_ROOT / "invalid/captured_with_evidence_authority.json"))
    assert errors


def test_digest_changes_when_payload_bytes_change(tmp_path):
    payload = tmp_path / "payload.json"
    payload.write_text('{"records":[]}\n', encoding="utf-8")
    first = MODULE.build_captured_candidate(
        payload,
        source_id="source:demo-official",
        source_url="https://example.gov/demo.json",
        retrieved_at="2026-08-08T01:30:00Z",
    )
    payload.write_text('{"records":[1]}\n', encoding="utf-8")
    second = MODULE.build_captured_candidate(
        payload,
        source_id="source:demo-official",
        source_url="https://example.gov/demo.json",
        retrieved_at="2026-08-08T01:30:00Z",
    )
    assert first["content_sha256"] != second["content_sha256"]
    assert first["snapshot_id"] != second["snapshot_id"]
