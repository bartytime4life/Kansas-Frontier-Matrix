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


def captured(**patch):
    """The valid fixture with fields changed and its deterministic snapshot_id recomputed."""
    doc = {**load(FIXTURE_ROOT / "valid/captured.json"), **patch}
    doc["snapshot_id"] = MODULE._snapshot_id(doc["source_id"], doc["source_url"], doc["retrieved_at"], doc["content_sha256"])
    return doc


def test_lowercase_rfc3339_separators_are_parsed_not_raised():
    # RFC 3339 allows lowercase "t" and "z"; the schema accepts them, so the semantic checks must too.
    assert MODULE.validate_doc(captured(retrieved_at="2026-08-08t01:30:00z", last_modified="2026-08-08t01:00:00z")) == []
    assert MODULE.validate_doc(captured(last_modified="2026-08-08t02:00:00z")) == [
        "last_modified cannot be later than retrieved_at"]


def test_last_modified_is_compared_as_an_instant():
    assert MODULE.validate_doc(captured(last_modified="2026-08-08T03:00:00+02:00")) == []
    assert MODULE.validate_doc(captured(last_modified="2026-08-08T01:30:01Z")) == [
        "last_modified cannot be later than retrieved_at"]
    assert MODULE.validate_doc(captured(last_modified=None)) == []


def test_unparseable_timestamp_is_reported(monkeypatch):
    def reject(_value):
        raise ValueError("unsupported")
    monkeypatch.setattr(MODULE, "_dt", reject)
    assert MODULE.validate_doc(captured()) == ["timestamp is not a parseable date-time: unsupported"]


def test_outcome_rules():
    no_bytes = {"content_sha256": None, "content_length": None}
    assert MODULE.validate_doc(captured(http_status=500)) == ["CAPTURED requires a 2xx HTTP status"]
    assert MODULE.validate_doc(captured(content_length=0)) == ["CAPTURED requires non-empty digest-bound bytes"]
    assert MODULE.validate_doc(captured(**no_bytes)) == ["CAPTURED requires non-empty digest-bound bytes"]
    assert MODULE.validate_doc(captured(retrieval_outcome="NOT_MODIFIED", http_status=304, **no_bytes)) == []
    assert MODULE.validate_doc(captured(retrieval_outcome="NOT_MODIFIED", http_status=304, content_sha256=None, content_length=0)) == []
    assert MODULE.validate_doc(captured(retrieval_outcome="NOT_MODIFIED", http_status=200, **no_bytes)) == [
        "NOT_MODIFIED requires HTTP 304"]
    assert MODULE.validate_doc(captured(retrieval_outcome="NOT_MODIFIED", http_status=304)) == [
        "NOT_MODIFIED cannot claim captured bytes"]
    assert MODULE.validate_doc(captured(retrieval_outcome="FAILED", http_status=503, **no_bytes)) == []
    assert MODULE.validate_doc(captured(retrieval_outcome="FAILED", http_status=503)) == ["FAILED cannot claim captured bytes"]


def test_identity_and_schema_are_enforced():
    doc = captured()
    doc["source_url"] = "https://example.gov/other.json"
    assert MODULE.validate_doc(doc) == ["snapshot_id does not match deterministic identity"]
    assert any("https://" in error for error in MODULE.validate_doc(captured(source_url="http://example.gov/demo.json")))
    assert MODULE.validate_doc({**captured(), "extra": 1})
    assert MODULE.validate_doc({**captured(), "public_use_allowed": True})


def test_cli_prints_the_validated_candidate(monkeypatch, capsys):
    argv = ["candidate", str(FIXTURE_ROOT / "payloads/demo.json"), "--source-id", "source:demo-official",
            "--source-url", "https://example.gov/demo.json", "--retrieved-at", "2026-08-08T01:30:00Z",
            "--media-type", "application/json", "--etag", "demo-v1", "--last-modified", "2026-08-08T01:00:00Z"]
    monkeypatch.setattr("sys.argv", argv)
    assert MODULE.main() == 0
    assert json.loads(capsys.readouterr().out) == load(FIXTURE_ROOT / "valid/captured.json")
    monkeypatch.setattr("sys.argv", [*argv[:-1], "2026-08-09T00:00:00Z"])
    assert MODULE.main() == 1
    assert capsys.readouterr().err.strip() == "last_modified cannot be later than retrieved_at"
