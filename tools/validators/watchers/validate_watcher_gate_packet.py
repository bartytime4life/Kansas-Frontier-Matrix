#!/usr/bin/env python3
"""Validate synthetic no-network WatcherGatePacket candidates."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
PROFILE_PATH = REPO_ROOT / "pipeline_specs/watchers/watcher_gate_profile.v1.json"
PROFILE_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/watchers/watcher_gate_profile.schema.json"
PACKET_SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/watchers/watcher_gate_packet.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/watchers/watcher_gate_packet"
MAX_JSON_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 50
ZERO_SHA256 = "sha256:" + "0" * 64
SCOPE = "watcher-gate-packet-fixture-only"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    packet: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.packet is not None and not self.findings


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    return (value, []) if isinstance(value, dict) else (None, [Finding("ROOT_NOT_OBJECT", "/")])


def _pointer(parts: Iterable[Any]) -> str:
    items = [str(item).replace("~", "~0").replace("/", "~1") for item in parts]
    return "/" + "/".join(items) if items else "/"


def _load_schema(path: Path) -> dict[str, Any]:
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def _schema_findings(value: Mapping[str, Any], schema_path: Path, code: str) -> list[Finding]:
    try:
        validator = Draft202012Validator(_load_schema(schema_path), format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings: list[Finding] = []
    for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator))):
        pointer = _pointer(error.absolute_path)
        mapped = "GOVERNANCE_VIOLATION" if pointer.startswith("/governance/") else code
        findings.append(Finding(mapped, pointer))
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical_without(value: Mapping[str, Any], field: str = "spec_hash") -> bytes:
    return json.dumps(
        {key: item for key, item in value.items() if key != field},
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _hash(value: Mapping[str, Any]) -> str:
    return "sha256:" + hashlib.sha256(_canonical_without(value)).hexdigest()


def _profile_findings(profile: Mapping[str, Any]) -> list[Finding]:
    findings = _schema_findings(profile, PROFILE_SCHEMA_PATH, "PROFILE_SCHEMA_INVALID")
    if findings:
        return findings
    declared = profile.get("spec_hash")
    if declared == ZERO_SHA256:
        return [Finding("DIGEST_PLACEHOLDER", "/spec_hash")]
    if declared != _hash(profile):
        return [Finding("PROFILE_HASH_MISMATCH", "/spec_hash")]
    thresholds = profile["thresholds"]
    if thresholds["deny_score_below"] >= thresholds["green_score_min"]:
        return [Finding("PROFILE_THRESHOLDS_INVALID", "/thresholds")]
    return []


def _expected(packet: Mapping[str, Any], profile: Mapping[str, Any]) -> tuple[str, int, list[str], list[str]]:
    prefilter = packet["prefilter"]
    thresholds = profile["thresholds"]
    reasons: list[str] = []
    if prefilter["asset_missing_count"] > 0:
        reasons.append("ASSET_MISSING")
    cloud = prefilter["median_cloud_percent"]
    if cloud is not None and cloud > thresholds["median_cloud_deny_above_percent"]:
        reasons.append("MEDIAN_CLOUD_TOO_HIGH")
    if prefilter["items_found"] == 0:
        reasons.append("NO_ITEMS")
    if packet["score"] < thresholds["deny_score_below"]:
        reasons.append("SCORE_BELOW_DENY")
    if reasons:
        return "DENY", profile["exit_codes"]["DENY"], sorted(reasons), ["BLOCK_PROMOTION", "ROUTE_STEWARD_REVIEW"]
    if prefilter["missing_etag"]:
        reasons.append("MISSING_ETAG")
    if packet["score"] < thresholds["green_score_min"]:
        reasons.append("SCORE_AMBER")
    if reasons:
        return "AMBER", profile["exit_codes"]["AMBER"], sorted(reasons), ["ROUTE_STEWARD_REVIEW"]
    return "GREEN", profile["exit_codes"]["GREEN"], ["ALL_GATES_GREEN"], []


def _packet_findings(packet: Mapping[str, Any], profile: Mapping[str, Any]) -> list[Finding]:
    findings = _schema_findings(packet, PACKET_SCHEMA_PATH, "PACKET_SCHEMA_INVALID")
    if findings:
        return findings
    declared = packet["spec_hash"]
    if declared == ZERO_SHA256:
        findings.append(Finding("DIGEST_PLACEHOLDER", "/spec_hash"))
    elif declared != _hash(packet):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    binding = packet["profile"]
    for field in ("profile_id", "profile_version", "spec_hash"):
        if binding[field] != profile[field]:
            findings.append(Finding("PROFILE_BINDING_MISMATCH", f"/profile/{field}"))
    expected_decision, expected_exit, expected_reasons, expected_obligations = _expected(packet, profile)
    if packet["decision"] != expected_decision:
        findings.append(Finding("DECISION_MISMATCH", "/decision"))
    if packet["process_exit_code"] != expected_exit:
        findings.append(Finding("EXIT_CODE_MISMATCH", "/process_exit_code"))
    if packet["reason_codes"] != sorted(set(packet["reason_codes"])):
        findings.append(Finding("REASON_CODES_NOT_CANONICAL", "/reason_codes"))
    elif packet["reason_codes"] != expected_reasons:
        findings.append(Finding("REASON_CODES_MISMATCH", "/reason_codes"))
    if packet["obligations"] != sorted(set(packet["obligations"])):
        findings.append(Finding("OBLIGATIONS_NOT_CANONICAL", "/obligations"))
    elif packet["obligations"] != expected_obligations:
        findings.append(Finding("OBLIGATIONS_MISMATCH", "/obligations"))
    return findings


def validate_packet(candidate_path: Path, profile_path: Path = PROFILE_PATH) -> ValidationResult:
    profile, findings = _read(profile_path)
    if profile is None:
        return ValidationResult(None, tuple(sorted(set(findings))))
    findings = _profile_findings(profile)
    if findings:
        return ValidationResult(None, tuple(sorted(set(findings))))
    packet, findings = _read(candidate_path)
    if packet is None:
        return ValidationResult(None, tuple(sorted(set(findings))))
    findings = _packet_findings(packet, profile)
    return ValidationResult(None if findings else packet, tuple(sorted(set(findings))))


def _serialize(path: Path, result: ValidationResult) -> str:
    payload: dict[str, Any] = {
        "file": path.as_posix(),
        "findings": [{"code": item.code, "field": item.field} for item in result.findings],
        "outcome": "PASS" if result.ok else "FAIL",
        "scope": SCOPE,
    }
    if result.packet:
        payload["decision"] = result.packet["decision"]
        payload["process_exit_code"] = result.packet["process_exit_code"]
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def run_fixture_profile() -> int:
    valid = sorted((FIXTURE_ROOT / "valid").glob("valid_*.json"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("invalid_*.json"))
    try:
        outputs = json.loads((FIXTURE_ROOT / "valid/expected_outputs_manifest.json").read_text(encoding="utf-8"))
        findings_manifest = json.loads((FIXTURE_ROOT / "invalid/expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    if not valid or not invalid:
        return 1
    passed = True
    for path in valid:
        result = validate_packet(path)
        print(_serialize(path, result))
        actual = {} if not result.packet else {"decision": result.packet["decision"], "exit_code": result.packet["process_exit_code"]}
        passed = passed and result.ok and actual == outputs.get(path.name)
    for path in invalid:
        result = validate_packet(path)
        print(_serialize(path, result))
        actual = sorted({item.code for item in result.findings})
        expected = sorted(findings_manifest.get(path.name, []))
        passed = passed and not result.ok and bool(expected) and actual == expected
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate inactive synthetic WatcherGatePacket candidates.")
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_PATH)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files or args.profile != PROFILE_PATH:
            parser.error("--fixtures cannot be combined with files or --profile")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or use --fixtures")
    failed = False
    for path in sorted(args.files, key=lambda item: item.as_posix()):
        result = validate_packet(path, args.profile)
        print(_serialize(path, result))
        failed = failed or not result.ok
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
