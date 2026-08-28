"""Validate proposed KFM SourceArtifact metadata and optional local payload bytes.

Passing proves bounded shape, deterministic identity, and exact local-byte
binding only. It grants no source, evidence, lifecycle, release, or publication
authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from collections.abc import Mapping, Sequence
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

from tools.validators._source_artifact import (
    DuplicateKeyError,
    Finding,
    MAX_METADATA_BYTES,
    MAX_PAYLOAD_BYTES,
    NonFiniteNumberError,
    ValidationResult,
    finite_float,
    mapping,
    object_no_duplicates,
    read_json_object,
    read_regular_bytes,
    reject_nonfinite,
    schema_findings,
    strings,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/source_artifact.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/source/source_artifact"
_ZERO_DIGEST = "sha256:" + ("0" * 64)
_HEADER_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,79}$")
_STRUCTURED_MEDIA = {"application/json", "application/geo+json", "application/xml", "text/csv"}


def _sha256(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None else None


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    governance = mapping(candidate.get("governance"))
    parser = mapping(candidate.get("parser"))
    locator = mapping(candidate.get("source_locator"))
    content_digest = candidate.get("content_digest")
    for field, value in (
        ("/content_digest", content_digest),
        ("/governance/spec_hash", governance.get("spec_hash")),
        ("/parser/spec_digest", parser.get("spec_digest")),
        ("/source_locator/locator_digest", locator.get("locator_digest")),
    ):
        if value == _ZERO_DIGEST:
            findings.append(Finding("PLACEHOLDER_DIGEST", field, "all-zero digest is not an identity"))
    if isinstance(content_digest, str):
        if candidate.get("artifact_id") != f"source-artifact:{content_digest}":
            findings.append(Finding("ARTIFACT_ID_MISMATCH", "/artifact_id", "artifact_id must derive from content_digest"))
        if candidate.get("immutable_storage_ref") != f"cas:{content_digest}":
            findings.append(Finding("STORAGE_REF_MISMATCH", "/immutable_storage_ref", "storage ref must derive from content_digest"))

    kind, value = locator.get("kind"), locator.get("value")
    if isinstance(kind, str) and isinstance(value, str):
        if locator.get("locator_digest") != _sha256(f"{kind}\n{value}".encode()):
            findings.append(Finding("LOCATOR_DIGEST_MISMATCH", "/source_locator/locator_digest", "locator digest is unbound"))
        if any(ord(c) < 32 or ord(c) == 127 for c in value):
            findings.append(Finding("LOCATOR_UNSAFE", "/source_locator/value", "locator contains controls"))
        if kind in {"https_url", "api_record"}:
            parsed = urlsplit(value)
            if (parsed.scheme != "https" or not parsed.hostname or parsed.username is not None or parsed.password is not None or parsed.query or parsed.fragment or "\\" in value or any(token in value.lower() for token in ("%00", "%0a", "%0d"))):
                findings.append(Finding("LOCATOR_UNSAFE", "/source_locator/value", "network locator must be safe HTTPS"))
        if kind == "repository_object" and not value.startswith("repo:"):
            findings.append(Finding("LOCATOR_UNSAFE", "/source_locator/value", "repository locator must use repo:"))
        if kind == "file_reference" and not value.startswith("file-ref:"):
            findings.append(Finding("LOCATOR_UNSAFE", "/source_locator/value", "file locator must use file-ref:"))

    retrieved = _parse_time(candidate.get("retrieved_at"))
    source_time = _parse_time(candidate.get("source_reported_at"))
    rights_time = _parse_time(mapping(candidate.get("rights_snapshot")).get("captured_at"))
    if retrieved and source_time and source_time > retrieved:
        findings.append(Finding("SOURCE_TIME_AFTER_RETRIEVAL", "/source_reported_at", "source time follows retrieval"))
    if retrieved and rights_time and rights_time > retrieved:
        findings.append(Finding("RIGHTS_TIME_AFTER_RETRIEVAL", "/rights_snapshot/captured_at", "rights time follows retrieval"))

    surface, media = candidate.get("source_surface_type"), candidate.get("media_type")
    if surface == "api_record" and isinstance(media, str):
        base = media.split(";", 1)[0].strip().lower()
        if base not in _STRUCTURED_MEDIA and not base.endswith("+json"):
            findings.append(Finding("API_MEDIA_TYPE_INVALID", "/media_type", "API record requires structured media"))
    if surface == "pdf_document" and media != "application/pdf":
        findings.append(Finding("PDF_MEDIA_TYPE_INVALID", "/media_type", "PDF surface requires application/pdf"))
    if kind in {"https_url", "api_record"} and candidate.get("status_code") is None:
        findings.append(Finding("STATUS_CODE_REQUIRED", "/status_code", "network capture requires status"))
    if kind not in {"https_url", "api_record"} and candidate.get("status_code") is not None:
        findings.append(Finding("STATUS_CODE_UNEXPECTED", "/status_code", "non-network capture cannot claim HTTP status"))

    request = mapping(candidate.get("request_context"))
    params, headers = strings(request.get("parameter_names")), strings(request.get("header_names"))
    if params != sorted(set(params)):
        findings.append(Finding("REQUEST_ARRAY_NOT_CANONICAL", "/request_context/parameter_names", "parameter names must be canonical"))
    if headers != sorted(set(headers)):
        findings.append(Finding("REQUEST_ARRAY_NOT_CANONICAL", "/request_context/header_names", "header names must be canonical"))
    if any(not _HEADER_RE.fullmatch(item) for item in headers):
        findings.append(Finding("HEADER_NAME_INVALID", "/request_context/header_names", "header names must be lower-case tokens"))
    method = request.get("method")
    if kind in {"https_url", "api_record"} and method not in {"GET", "POST", "HEAD"}:
        findings.append(Finding("REQUEST_METHOD_MISMATCH", "/request_context/method", "network locator requires network method"))
    if kind == "repository_object" and method != "REPOSITORY":
        findings.append(Finding("REQUEST_METHOD_MISMATCH", "/request_context/method", "repository locator requires REPOSITORY"))
    if kind == "file_reference" and method != "FILE":
        findings.append(Finding("REQUEST_METHOD_MISMATCH", "/request_context/method", "file locator requires FILE"))

    lineage = mapping(candidate.get("lineage"))
    outcome = candidate.get("retrieval_outcome")
    conflict, supersedes = lineage.get("conflict_group_ref"), lineage.get("supersedes_artifact_ref")
    corrections = strings(lineage.get("correction_refs"))
    if outcome == "SOURCE_CONFLICT" and conflict is None:
        findings.append(Finding("CONFLICT_GROUP_REQUIRED", "/lineage/conflict_group_ref", "source conflict requires group"))
    if outcome != "SOURCE_CONFLICT" and conflict is not None:
        findings.append(Finding("CONFLICT_GROUP_UNEXPECTED", "/lineage/conflict_group_ref", "non-conflict cannot claim group"))
    if supersedes is not None and not corrections:
        findings.append(Finding("SUPERSESSION_CORRECTION_REQUIRED", "/lineage/correction_refs", "supersession requires correction"))
    if supersedes == candidate.get("artifact_id"):
        findings.append(Finding("SELF_SUPERSESSION", "/lineage/supersedes_artifact_ref", "artifact cannot supersede itself"))
    return findings


def validate_artifact(metadata_path: Path, payload_path: Path | None = None) -> ValidationResult:
    candidate, findings = read_json_object(metadata_path)
    if candidate is None:
        return ValidationResult(tuple(sorted(findings)))
    findings.extend(schema_findings(SCHEMA_PATH, candidate))
    findings.extend(_semantic_findings(candidate))
    if payload_path is not None:
        payload, payload_findings = read_regular_bytes(payload_path, MAX_PAYLOAD_BYTES)
        if payload is None:
            findings.extend(Finding(item.code, "/payload", item.detail) for item in payload_findings)
        else:
            if candidate.get("byte_length") != len(payload):
                findings.append(Finding("PAYLOAD_LENGTH_MISMATCH", "/byte_length", "declared length differs"))
            if candidate.get("content_digest") != _sha256(payload):
                findings.append(Finding("PAYLOAD_DIGEST_MISMATCH", "/content_digest", "declared digest differs"))
    return ValidationResult(tuple(sorted(set(findings))))


def _read_fixture_array(path: Path) -> list[Mapping[str, object]]:
    data, findings = read_regular_bytes(path, MAX_METADATA_BYTES)
    if data is None or findings:
        raise ValueError(f"fixture could not be read: {path.name}")
    try:
        value = json.loads(data.decode(), object_pairs_hook=object_no_duplicates, parse_constant=reject_nonfinite, parse_float=finite_float)
    except (UnicodeError, DuplicateKeyError, NonFiniteNumberError, json.JSONDecodeError, RecursionError, ValueError) as exc:
        raise ValueError(f"fixture is invalid: {path.name}") from exc
    if not isinstance(value, list) or not all(isinstance(item, Mapping) for item in value):
        raise ValueError(f"fixture must contain object array: {path.name}")
    return list(value)


def load_fixture_cases() -> dict[str, object]:
    return {
        "valid": _read_fixture_array(FIXTURE_ROOT / "valid_cases.json"),
        "invalid": _read_fixture_array(FIXTURE_ROOT / "invalid_cases.json"),
        "semantic_invalid": [*_read_fixture_array(FIXTURE_ROOT / "semantic_invalid_cases_a.json"), *_read_fixture_array(FIXTURE_ROOT / "semantic_invalid_cases_b.json")],
    }


def materialize_case(case: Mapping[str, object], root: Path) -> tuple[Path, Path | None]:
    name, metadata = case.get("name"), case.get("metadata")
    if not isinstance(name, str) or not isinstance(metadata, Mapping):
        raise ValueError("fixture case is malformed")
    metadata_path = root / f"{name}.json"
    metadata_path.write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n")
    payload_path = None
    if isinstance(case.get("payload_text"), str):
        payload_path = root / f"{name}.payload"
        payload_path.write_bytes(case["payload_text"].encode())
    return metadata_path, payload_path


def run_fixture_profile() -> int:
    try:
        corpus = load_fixture_cases()
    except ValueError as exc:
        print(json.dumps({"outcome":"FAIL","reason":str(exc)}, sort_keys=True, separators=(",", ":")))
        return 1
    ok = True
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        for lane in ("valid", "invalid", "semantic_invalid"):
            cases = corpus[lane]
            if not cases:
                return 1
            for case in cases:
                metadata, payload = materialize_case(case, root)
                result = validate_artifact(metadata, payload if lane == "valid" else None)
                actual = sorted({finding.code for finding in result.findings})
                expected = [] if lane == "valid" else sorted(case.get("expected_codes", []))
                case_ok = result.ok if lane == "valid" else (not result.ok and actual == expected)
                ok = ok and case_ok
                print(json.dumps({"case":case.get("name"),"findings":[{"code":f.code,"field":f.field} for f in result.findings],"outcome":"PASS" if case_ok else "FIXTURE_POLARITY_ERROR"}, sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate proposed KFM SourceArtifact metadata.")
    parser.add_argument("metadata", nargs="?", type=Path)
    parser.add_argument("--payload", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.metadata or args.payload:
            parser.error("--fixtures cannot be combined with metadata or --payload")
        return run_fixture_profile()
    if args.metadata is None:
        parser.error("provide metadata or use --fixtures")
    result = validate_artifact(args.metadata, args.payload)
    print(json.dumps({"file":args.metadata.as_posix(),"findings":[{"code":f.code,"field":f.field} for f in result.findings],"outcome":"PASS" if result.ok else "FAIL","scope":"source-artifact-shape-identity-and-local-byte-binding-only"}, sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
