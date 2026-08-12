#!/usr/bin/env python3
"""Validate fixture-only SourceRetrievalEpisode records."""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from urllib.parse import urlsplit

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))

from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/source/source_retrieval_episode.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/source/source_retrieval_episode/cases.json"
PREFIX = "kfm:source-retrieval-episode:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100

_BODY_IDENTITY_FIELDS = (
    "body_digest",
    "body_bytes",
    "schema_fingerprint",
    "semantic_sentinel_digest",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(
            value[:-1] + "+00:00" if value.endswith("Z") else value
        )
    except ValueError:
        return None


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("RETRIEVAL_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("RETRIEVAL_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("RETRIEVAL_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("RETRIEVAL_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("RETRIEVAL_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("RETRIEVAL_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("RETRIEVAL_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"episode_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def recompute_result(value: Mapping[str, Any]) -> dict[str, Any]:
    category = value["transport"]["category"]
    method = value["method"]
    if category == "SUCCESS":
        if method == "HEAD":
            return {
                "status": "RETRY_REQUIRED",
                "reason_codes": ["FULL_GET_VERIFICATION_REQUIRED"],
            }
        return {
            "status": "CAPTURED",
            "reason_codes": ["RETRIEVAL_BODY_CAPTURED"],
        }
    if category == "NOT_MODIFIED":
        return {
            "status": "NO_CHANGE",
            "reason_codes": ["SOURCE_NOT_MODIFIED"],
        }
    if category == "TIMEOUT":
        return {
            "status": "RETRY_REQUIRED",
            "reason_codes": ["RETRIEVAL_TIMEOUT"],
        }
    if category == "RATE_LIMITED":
        return {
            "status": "RETRY_REQUIRED",
            "reason_codes": ["SOURCE_RATE_LIMITED"],
        }
    if category == "RETRY_EXHAUSTED":
        return {
            "status": "RETRY_REQUIRED",
            "reason_codes": ["RETRY_BUDGET_EXHAUSTED"],
        }
    if category == "CANCELLED":
        return {
            "status": "RETRY_REQUIRED",
            "reason_codes": ["RETRIEVAL_CANCELLED"],
        }
    if category == "AUTH_REQUIRED":
        return {"status": "BLOCKED", "reason_codes": ["AUTH_REQUIRED"]}
    if category == "ACCESS_DENIED":
        return {"status": "BLOCKED", "reason_codes": ["ACCESS_DENIED"]}
    if category == "NOT_FOUND":
        return {"status": "BLOCKED", "reason_codes": ["SOURCE_NOT_FOUND"]}
    if category == "RESPONSE_TOO_LARGE":
        return {
            "status": "BLOCKED",
            "reason_codes": ["RESPONSE_TOO_LARGE"],
        }
    if category == "INTEGRITY_MISMATCH":
        return {
            "status": "BLOCKED",
            "reason_codes": ["INTEGRITY_CHECK_FAILED"],
        }
    if category == "PARTIAL":
        return {
            "status": "BLOCKED",
            "reason_codes": ["PARTIAL_RESPONSE_DENIED"],
        }
    if category == "INVALID_RESPONSE_METADATA":
        return {
            "status": "BLOCKED",
            "reason_codes": ["INVALID_RESPONSE_METADATA"],
        }
    if category == "UNSAFE_METADATA":
        return {
            "status": "BLOCKED",
            "reason_codes": ["UNSAFE_RESPONSE_DENIED"],
        }
    return {"status": "ERROR", "reason_codes": ["TRANSPORT_ERROR"]}


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_FINDINGS + 1,
            )
        )
    except Exception:
        return (Finding("RETRIEVAL_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {
        Finding("RETRIEVAL_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_FINDINGS]
    }
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("RETRIEVAL_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _locator_is_safe(value: str) -> bool:
    try:
        parsed = urlsplit(value)
        _ = parsed.port
    except ValueError:
        return False
    return (
        parsed.scheme == "https"
        and bool(parsed.hostname)
        and parsed.username is None
        and parsed.password is None
        and not parsed.query
        and not parsed.fragment
    )


def _has_body_identity(transport: Mapping[str, Any]) -> bool:
    return any(transport[field] is not None for field in _BODY_IDENTITY_FIELDS)


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("RETRIEVAL_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(
                Finding("RETRIEVAL_SPEC_HASH_MISMATCH", "/spec_hash")
            )
        if value["episode_id"] != expected_id:
            findings.add(Finding("RETRIEVAL_ID_MISMATCH", "/episode_id"))

    if value["source_descriptor_ref"] != f"kfm://source/{value['source_id']}":
        findings.add(
            Finding(
                "RETRIEVAL_SOURCE_REF_MISMATCH",
                "/source_descriptor_ref",
            )
        )

    attempted = _time(value["attempted_at"])
    completed = _time(value["completed_at"])
    if not value["attempted_at"].endswith("Z"):
        findings.add(
            Finding("RETRIEVAL_TIMESTAMP_NOT_UTC", "/attempted_at")
        )
    if not value["completed_at"].endswith("Z"):
        findings.add(
            Finding("RETRIEVAL_TIMESTAMP_NOT_UTC", "/completed_at")
        )
    if attempted is None or completed is None or completed < attempted:
        findings.add(
            Finding("RETRIEVAL_TIME_ORDER_INVALID", "/completed_at")
        )

    if not _locator_is_safe(value["redacted_locator"]):
        findings.add(
            Finding("RETRIEVAL_LOCATOR_UNSAFE", "/redacted_locator")
        )

    request = value["request"]
    declared_conditional = (
        request["if_none_match_present"]
        or request["if_modified_since_present"]
    )
    if request["conditional"] != declared_conditional:
        findings.add(
            Finding("RETRIEVAL_CONDITIONAL_MISMATCH", "/request/conditional")
        )

    transport = value["transport"]
    category = transport["category"]
    method = value["method"]
    status = transport["http_status"]
    body_identity = _has_body_identity(transport)
    last_modified = _time(transport["last_modified"])

    if transport["last_modified"] is not None and (
        last_modified is None
        or completed is None
        or last_modified > completed
    ):
        findings.add(
            Finding(
                "RETRIEVAL_LAST_MODIFIED_AFTER_COMPLETION",
                "/transport/last_modified",
            )
        )

    if category == "SUCCESS":
        if not isinstance(status, int) or not 200 <= status <= 299:
            findings.add(
                Finding(
                    "RETRIEVAL_HTTP_STATUS_MISMATCH",
                    "/transport/http_status",
                )
            )
        if method == "GET":
            if (
                transport["body_digest"] is None
                or transport["body_bytes"] is None
                or transport["content_type"] is None
            ):
                findings.add(
                    Finding("RETRIEVAL_BODY_REQUIRED", "/transport")
                )
            if (
                transport["content_length"] is not None
                and transport["body_bytes"] is not None
                and transport["content_length"] != transport["body_bytes"]
            ):
                findings.add(
                    Finding(
                        "RETRIEVAL_CONTENT_LENGTH_MISMATCH",
                        "/transport/content_length",
                    )
                )
        else:
            if body_identity:
                findings.add(
                    Finding("RETRIEVAL_BODY_FORBIDDEN", "/transport")
                )
            if (
                transport["etag"] is None
                and transport["last_modified"] is None
                and transport["content_length"] is None
            ):
                findings.add(
                    Finding("RETRIEVAL_HEAD_SIGNAL_REQUIRED", "/transport")
                )
    elif category == "NOT_MODIFIED":
        if status != 304:
            findings.add(
                Finding(
                    "RETRIEVAL_HTTP_STATUS_MISMATCH",
                    "/transport/http_status",
                )
            )
        if method != "GET":
            findings.add(
                Finding("RETRIEVAL_METHOD_MISMATCH", "/method")
            )
        if body_identity:
            findings.add(Finding("RETRIEVAL_BODY_FORBIDDEN", "/transport"))
        if not request["conditional"] or (
            transport["etag"] is None and transport["last_modified"] is None
        ):
            findings.add(
                Finding("RETRIEVAL_VALIDATOR_REQUIRED", "/transport")
            )
    else:
        if body_identity:
            findings.add(Finding("RETRIEVAL_BODY_FORBIDDEN", "/transport"))
        expected_statuses = {
            "RATE_LIMITED": {429},
            "AUTH_REQUIRED": {401},
            "ACCESS_DENIED": {403, 451},
            "NOT_FOUND": {404},
            "PARTIAL": {206},
        }
        if category in expected_statuses and status not in expected_statuses[category]:
            findings.add(
                Finding(
                    "RETRIEVAL_HTTP_STATUS_MISMATCH",
                    "/transport/http_status",
                )
            )

    if value["result"] != recompute_result(value):
        findings.add(Finding("RETRIEVAL_RESULT_MISMATCH", "/result"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", schema_findings)
    semantic_findings = _semantic_findings(value)
    if semantic_findings:
        return Result("DENY", semantic_findings)
    status = value["result"]["status"]
    reasons = value["result"]["reason_codes"]
    if status in {"CAPTURED", "NO_CHANGE"}:
        return Result("PASS", ())
    if status == "RETRY_REQUIRED":
        return Result(
            "ABSTAIN",
            tuple(Finding(code, "/result/status") for code in reasons),
        )
    if status == "BLOCKED":
        return Result(
            "DENY",
            tuple(Finding(code, "/result/status") for code in reasons),
        )
    return Result(
        "ERROR",
        tuple(Finding(code, "/result/status") for code in reasons),
    )


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(
    manifest: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["result"] = copy.deepcopy(
        case.get("result_override", recompute_result(document))
    )
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["episode_id"] = case.get("episode_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    passed = True
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [
            {"code": finding.code, "path": finding.path}
            for finding in result.findings
        ]
        match = (
            result.outcome == case["expected_outcome"]
            and actual == case["expected_findings"]
        )
        print(
            json.dumps(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": actual,
                    "suite_match": match,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and match
    return 0 if passed else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix() if path else None,
            "findings": [
                {"code": finding.code, "path": finding.path}
                for finding in result.findings
            ],
            "non_effects": [
                "no_network",
                "no_source_activation",
                "no_source_artifact",
                "no_receipt",
                "no_evidence",
                "no_raw_write",
                "no_current_data_claim",
                "no_no-current-data_claim",
                "no_promotion",
                "no_release",
                "no_publication",
            ],
            "outcome": result.outcome,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
