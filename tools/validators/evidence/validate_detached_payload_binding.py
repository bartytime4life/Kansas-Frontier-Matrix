#!/usr/bin/env python3
"""Validate fixture-only KFM DetachedPayloadBinding candidates.

A PASS proves closed candidate metadata, safe/canonical HTTPS locations,
deterministic identity, exact local fixture byte binding, and explicit
non-authority only. The validator never performs network access.
"""

from __future__ import annotations

import argparse
import hashlib
import ipaddress
import json
import math
import os
import stat
import sys
import urllib.parse
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import compute_spec_hash  # noqa: E402

SCHEMA = ROOT / "schemas/contracts/v1/evidence/detached_payload_binding.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/detached_payload_binding"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_PAYLOAD_BYTES = 16 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "detached-payload-binding-candidate-only"
ERROR_CODES = frozenset(
    {
        "INPUT_NOT_FILE",
        "INPUT_READ_ERROR",
        "INPUT_SYMLINK_DENIED",
        "INPUT_TOO_LARGE",
        "JSON_DUPLICATE_KEY",
        "JSON_INVALID",
        "JSON_NONFINITE_NUMBER",
        "JSON_NOT_UTF8",
        "ROOT_NOT_OBJECT",
        "SCHEMA_INVALID",
        "SCHEMA_UNAVAILABLE",
        "PAYLOAD_INPUT_NOT_FILE",
        "PAYLOAD_INPUT_READ_ERROR",
        "PAYLOAD_INPUT_SYMLINK_DENIED",
        "PAYLOAD_INPUT_TOO_LARGE",
    }
)
HOLD_CODES = frozenset({"PAYLOAD_BYTES_UNVERIFIED"})


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
    findings: tuple[Finding, ...]

    @property
    def outcome(self) -> str:
        if any(item.code in ERROR_CODES for item in self.findings):
            return "ERROR"
        if any(item.code in HOLD_CODES for item in self.findings):
            return "HOLD"
        return "PASS" if not self.findings else "FAIL"

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_json(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            if not stat.S_ISREG(os.fstat(descriptor).st_mode):
                return None, [Finding("INPUT_NOT_FILE", "/")]
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                raw = stream.read(MAX_JSON_BYTES + 1)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_nonfinite,
            parse_float=_finite,
        )
    except FileNotFoundError:
        return None, [Finding("INPUT_NOT_FILE", "/")]
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(
                    schema, format_checker=FormatChecker()
                ).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_INVALID", "/"))
    return findings


def _safe_host(host: str | None) -> bool:
    if not host:
        return False
    normalized = host.rstrip(".").lower()
    if normalized == "localhost" or normalized.endswith(
        (".localhost", ".local", ".internal")
    ):
        return False
    try:
        address = ipaddress.ip_address(normalized)
    except ValueError:
        return True
    return not any(
        (
            address.is_private,
            address.is_loopback,
            address.is_link_local,
            address.is_multicast,
            address.is_reserved,
            address.is_unspecified,
        )
    )


def _safe_https_url(value: Any) -> bool:
    if not isinstance(value, str) or not value or any(ord(char) < 32 for char in value):
        return False
    parsed = urllib.parse.urlsplit(value)
    if parsed.scheme.lower() != "https" or parsed.username or parsed.password:
        return False
    if parsed.fragment:
        return False
    return _safe_host(parsed.hostname)


def _semantic(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    locations = value.get("locations")
    if isinstance(locations, list):
        urls = [
            item.get("url") for item in locations if isinstance(item, dict)
        ]
        expected = sorted(locations, key=lambda item: item.get("url", "") if isinstance(item, dict) else "")
        if locations != expected or len(urls) != len(set(urls)):
            findings.append(Finding("LOCATIONS_NOT_CANONICAL", "/locations"))
        primary_count = sum(
            1 for item in locations if isinstance(item, dict) and item.get("role") == "PRIMARY"
        )
        if primary_count != 1:
            findings.append(Finding("PRIMARY_LOCATION_INVALID", "/locations"))
        for index, item in enumerate(locations):
            if isinstance(item, dict) and not _safe_https_url(item.get("url")):
                findings.append(Finding("UNSAFE_LOCATION", f"/locations/{index}/url"))

    payload = value.get("payload")
    if isinstance(payload, dict):
        digest = payload.get("sha256")
        if isinstance(digest, str) and digest.startswith("sha256:"):
            expected_payload_id = (
                "kfm://evidence/detached-payload/" + digest.split(":", 1)[1][:24]
            )
            if payload.get("payload_id") != expected_payload_id:
                findings.append(Finding("PAYLOAD_ID_MISMATCH", "/payload/payload_id"))

    governance = value.get("governance")
    if isinstance(governance, dict) and any(item is not False for item in governance.values()):
        findings.append(Finding("AUTHORITY_OVERREACH", "/governance"))

    projection = {
        key: item
        for key, item in value.items()
        if key not in {"spec_hash", "binding_id"}
    }
    actual_hash = compute_spec_hash(projection)
    if value.get("spec_hash") != actual_hash:
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
    expected_binding_id = (
        "kfm://evidence/detached-payload-binding/"
        + actual_hash.split(":", 1)[1][:24]
    )
    if value.get("binding_id") != expected_binding_id:
        findings.append(Finding("BINDING_ID_MISMATCH", "/binding_id"))
    return findings


def _verify_payload(path: Path, value: Mapping[str, Any]) -> list[Finding]:
    try:
        if path.is_symlink():
            return [Finding("PAYLOAD_INPUT_SYMLINK_DENIED", "/payload_file")]
        flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        try:
            metadata = os.fstat(descriptor)
            if not stat.S_ISREG(metadata.st_mode):
                return [Finding("PAYLOAD_INPUT_NOT_FILE", "/payload_file")]
            if metadata.st_size > MAX_PAYLOAD_BYTES:
                return [Finding("PAYLOAD_INPUT_TOO_LARGE", "/payload_file")]
            digest = hashlib.sha256()
            size = 0
            with os.fdopen(descriptor, "rb") as stream:
                descriptor = -1
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    size += len(chunk)
                    digest.update(chunk)
        finally:
            if descriptor >= 0:
                os.close(descriptor)
    except FileNotFoundError:
        return [Finding("PAYLOAD_INPUT_NOT_FILE", "/payload_file")]
    except OSError:
        return [Finding("PAYLOAD_INPUT_READ_ERROR", "/payload_file")]

    payload = value.get("payload")
    if not isinstance(payload, dict):
        return []
    findings: list[Finding] = []
    if payload.get("byte_size") != size:
        findings.append(Finding("PAYLOAD_SIZE_MISMATCH", "/payload/byte_size"))
    actual = "sha256:" + digest.hexdigest()
    if payload.get("sha256") != actual:
        findings.append(Finding("PAYLOAD_DIGEST_MISMATCH", "/payload/sha256"))
    return findings


def validate(path: Path, payload_file: Path | None = None) -> ValidationResult:
    value, findings = _read_json(path)
    if value is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(value))
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_semantic(value))
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))
    if payload_file is None:
        findings.append(Finding("PAYLOAD_BYTES_UNVERIFIED", "/payload_file"))
    else:
        findings.extend(_verify_payload(payload_file, value))
    return ValidationResult(tuple(sorted(set(findings))))


def serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": path.as_posix(),
            "outcome": result.outcome,
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "scope": SCOPE,
            "network_attempted": False,
            "authority_created": False,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixtures() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        cases = manifest["cases"]
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError):
        return 1
    passed = True
    for case in cases:
        input_path = FIXTURES / case["input"]
        payload_path = FIXTURES / case["payload_file"]
        result = validate(input_path, payload_path)
        codes = sorted({finding.code for finding in result.findings})
        matched = (
            result.outcome == case["expected_outcome"]
            and codes == case["expected_findings"]
        )
        print(
            json.dumps(
                {
                    "case_id": case["case_id"],
                    "outcome": result.outcome,
                    "findings": codes,
                    "suite_match": matched,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        passed = passed and matched
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only DetachedPayloadBinding candidates."
    )
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--payload-file", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files or args.payload_file:
            parser.error("--fixtures cannot be combined with other inputs")
        return run_fixtures()
    files = args.files or [FIXTURES / "valid/valid_binding.json"]
    if len(files) > 1 and args.payload_file is not None:
        parser.error("--payload-file may be used with only one binding")
    exit_codes = {"PASS": 0, "FAIL": 1, "ERROR": 2, "HOLD": 3}
    code = 0
    for path in sorted(files, key=lambda candidate: candidate.as_posix()):
        result = validate(path, args.payload_file)
        print(serialize(path, result))
        code = max(code, exit_codes[result.outcome])
    return code


if __name__ == "__main__":
    raise SystemExit(main())
