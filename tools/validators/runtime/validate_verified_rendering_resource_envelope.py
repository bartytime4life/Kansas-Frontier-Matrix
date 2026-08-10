#!/usr/bin/env python3
"""Validate fixture-only verified-rendering worker traces and resource envelopes."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT / "packages/hashing/src"))

from hashing import compute_spec_hash

SCHEMA = REPO_ROOT / "schemas/contracts/v1/runtime/verified_rendering_resource_envelope.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/runtime/verified_rendering_resource_envelope/cases.json"
MAX_JSON_BYTES = 1024 * 1024
COMMON_STAGES = {
    "QUEUED",
    "FETCH_START",
    "FETCH_COMPLETE",
    "HASH_COMPLETE",
    "PROOF_CHECK",
    "SIGNER_CHECK",
    "VERIFY_COMPLETE",
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    status: str
    rendering_state: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("envelope_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_envelope_id(spec_hash: str) -> str:
    return f"kfm:render-envelope:{spec_hash.removeprefix('sha256:')[:24]}"


def expected_rendering_assessment(document: Mapping[str, Any]) -> dict[str, Any]:
    binding = document["release_binding"]
    request = document["request"]
    budgets = document["budgets"]
    observation = document["observation"]
    messages = document["worker_messages"]
    faults = document["faults"]
    message_types = {message["message_type"] for message in messages}
    codes: set[str] = set()

    required = set(COMMON_STAGES)
    if faults["worker_failed"]:
        required.add("WORKER_FAILED")
    elif request["cancellation_requested"]:
        required.add("CANCELLED")
    else:
        required.update({"DECODE_START", "RENDER_READY"})
    if required - message_types:
        codes.add("REQUIRED_STAGE_MISSING")

    if binding["declared_artifact_digest"] != binding["expected_artifact_digest"] or faults["digest_mismatch"]:
        codes.add("ARTIFACT_DIGEST_MISMATCH")
    if faults["replay_detected"]:
        codes.add("CHUNK_REPLAY_DETECTED")
    if faults["timed_out"]:
        codes.add("TIMEOUT")
    if faults["worker_failed"]:
        codes.add("WORKER_FAILURE")
    if request["cancellation_requested"]:
        codes.add("WORKER_CANCELLED")
    if request["fallback_mode"] != "NONE":
        codes.add("FALLBACK_PATH_DECLARED")

    chunk_total = sum(chunk["bytes_declared"] for chunk in observation["hash_chunks"])
    if chunk_total != observation["hashed_bytes"]:
        codes.add("CHUNK_ACCOUNTING_MISMATCH")
    if any(chunk["bytes_declared"] > budgets["hash_chunk_bytes"] for chunk in observation["hash_chunks"]):
        codes.add("HASH_CHUNK_BUDGET_EXCEEDED")
    if faults["truncated_input"] or observation["hashed_bytes"] != observation["artifact_bytes"]:
        codes.add("TRUNCATED_INPUT")

    resource_pairs = (
        ("fetched_bytes", "fetch_bytes"),
        ("decoded_bytes", "decode_bytes"),
        ("peak_heap_bytes", "heap_bytes"),
        ("cpu_ms", "cpu_ms"),
        ("max_queue_depth", "queue_depth"),
        ("max_concurrency", "concurrency"),
    )
    if any(observation[observed] > budgets[limit] for observed, limit in resource_pairs):
        codes.add("RESOURCE_BUDGET_EXCEEDED")

    verification_messages = [
        message for message in messages
        if message["message_type"] in {"PROOF_CHECK", "SIGNER_CHECK", "VERIFY_COMPLETE"}
    ]
    if any(message["result"] == "FAIL" for message in verification_messages):
        codes.add("VERIFICATION_DECLARATION_FAILED")
    verify_pass = [message["sequence"] for message in messages if message["message_type"] == "VERIFY_COMPLETE" and message["result"] == "PASS"]
    decode_or_render = [message["sequence"] for message in messages if message["message_type"] in {"DECODE_START", "RENDER_READY"}]
    if decode_or_render and (not verify_pass or min(decode_or_render) <= min(verify_pass)):
        codes.add("VERIFY_BEFORE_DECODE_VIOLATION")

    blocking_codes = codes - {"FALLBACK_PATH_DECLARED", "WORKER_CANCELLED", "WORKER_FAILURE"}
    if faults["worker_failed"]:
        state = "ERROR"
    elif request["cancellation_requested"]:
        state = "CANCELLED"
    elif blocking_codes:
        state = "BLOCKED"
    elif "FALLBACK_PATH_DECLARED" in codes:
        state = "DEGRADED"
    else:
        state = "READY_FOR_SEPARATE_EXECUTION"
    return {
        "rendering_state": state,
        "finding_codes": sorted(codes),
        "render_allowed": False,
        "unverified_content_visible": False,
        "cryptographic_verification_performed": False,
        "separate_runtime_integration_required": True,
    }


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _deny(code: str, path: str, rendering_state: str | None = None) -> ValidationResult:
    return ValidationResult("DENY", rendering_state, (Finding(code, path),))


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
    )
    if errors:
        return _deny("RENDER_ENVELOPE_SCHEMA_INVALID", _pointer(errors[0].absolute_path))

    messages = document["worker_messages"]
    sequences = [message["sequence"] for message in messages]
    types = [message["message_type"] for message in messages]
    if sequences != list(range(1, len(messages) + 1)) or len(types) != len(set(types)):
        return _deny("RENDER_ENVELOPE_TRACE_NOT_CANONICAL", "/worker_messages")
    chunks = document["observation"]["hash_chunks"]
    indexes = [chunk["chunk_index"] for chunk in chunks]
    if indexes != list(range(len(chunks))):
        return _deny("RENDER_ENVELOPE_CHUNKS_NOT_CANONICAL", "/observation/hash_chunks")

    request = document["request"]
    faults = document["faults"]
    cancelled_message = "CANCELLED" in types
    failed_message = "WORKER_FAILED" in types
    if request["cancellation_requested"] != cancelled_message:
        return _deny("RENDER_ENVELOPE_CANCELLATION_BINDING_INVALID", "/request/cancellation_requested")
    if faults["worker_failed"] != failed_message:
        return _deny("RENDER_ENVELOPE_WORKER_FAILURE_BINDING_INVALID", "/faults/worker_failed")

    expected = expected_rendering_assessment(document)
    if document["rendering_assessment"] != expected:
        return _deny("RENDER_ENVELOPE_REPORT_MISMATCH", "/rendering_assessment", expected["rendering_state"])
    spec_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], spec_hash):
        return _deny("RENDER_ENVELOPE_SPEC_HASH_MISMATCH", "/spec_hash")
    envelope_id = expected_envelope_id(spec_hash)
    if not hmac.compare_digest(document["envelope_id"], envelope_id):
        return _deny("RENDER_ENVELOPE_ID_MISMATCH", "/envelope_id")
    return ValidationResult("PASS", expected["rendering_state"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_assessment"):
        document["rendering_assessment"] = expected_rendering_assessment(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["envelope_id"] = expected_envelope_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "envelope_id_override" in case:
        document["envelope_id"] = case["envelope_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(stream, object_pairs_hook=_unique_object, parse_constant=_reject_constant, parse_float=_finite_float)
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.status != case["expected_status"]
            or result.rendering_state != case["expected_rendering_state"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append({"case_id": case["case_id"], "actual_status": result.status, "actual_rendering_state": result.rendering_state, "actual_findings": actual_findings})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult("ERROR", None, (Finding("JSON_DUPLICATE_KEY", "/"),))
    except NonFiniteNumberError:
        result = ValidationResult("ERROR", None, (Finding("JSON_NONFINITE_NUMBER", "/"),))
    except InputSymlinkError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_SYMLINK_DENIED", "/"),))
    except InputTooLargeError:
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_TOO_LARGE", "/"),))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", None, (Finding("JSON_INPUT_INVALID", "/"),))
    print(json.dumps({"status": result.status, "rendering_state": result.rendering_state, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True, separators=(",", ":")))
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
