#!/usr/bin/env python3
"""Validate the proposed fixture-first PlaceIdentity separation profile.

A pass proves only bounded schema and semantic invariants for synthetic records.
It grants no legal status, census status, source admission, EvidenceBundle
closure, policy approval, release, deployment, publication, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "schemas/contracts/v1/domains/settlements-infrastructure/place-identity.schema.json"
PROFILE = ROOT / "fixtures/contracts/v1/domains/settlements-infrastructure/place_identity/fixture_profile.json"
MAX_BYTES = 1_048_576


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def error(self) -> bool:
        return any(
            finding.code.startswith(("FILE_", "JSON_", "INPUT_", "SCHEMA_UNAVAILABLE"))
            for finding in self.findings
        )


def _object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _constant(_: str) -> None:
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
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_object,
            parse_constant=_constant,
            parse_float=_float,
        )
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/")]
    return value, []


def _canonical_hash(candidate: Mapping[str, Any]) -> str:
    value = dict(candidate)
    value.pop("spec_hash", None)
    payload = json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        if any(validator.iter_errors(candidate)):
            return [Finding("SCHEMA_INVALID", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return []


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else None


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    supplied = candidate.get("spec_hash")
    if isinstance(supplied, str) and supplied != _canonical_hash(candidate):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    family = candidate.get("identity_family")
    legal = candidate.get("legal_status_claimed")
    census = candidate.get("census_status_claimed")

    if family == "Municipality" and (legal is not True or census is not False):
        findings.append(Finding("MUNICIPALITY_CENSUS_COLLAPSE", "/identity_family"))
    elif family == "CensusPlace" and (legal is not False or census is not True):
        findings.append(Finding("CENSUSPLACE_MUNICIPALITY_COLLAPSE", "/identity_family"))
    elif family in {"Settlement", "Townsite", "GhostTown", "Fort", "Mission", "ReservationCommunity"}:
        if legal is not False or census is not False:
            findings.append(Finding("NON_SPECIALIZED_STATUS_CLAIM", "/identity_family"))

    valid_time = candidate.get("valid_time")
    if isinstance(valid_time, dict):
        start = _time(valid_time.get("start"))
        end = _time(valid_time.get("end"))
        if start is not None and end is not None and end < start:
            findings.append(Finding("VALID_TIME_ORDER", "/valid_time"))

    if candidate.get("release_manifest_ref") is not None:
        if candidate.get("policy_decision_ref") is None:
            findings.append(Finding("RELEASE_WITHOUT_POLICY", "/policy_decision_ref"))
        if candidate.get("rollback_ref") is None:
            findings.append(Finding("RELEASE_WITHOUT_ROLLBACK", "/rollback_ref"))

    return findings


def validate(candidate: Mapping[str, Any]) -> Result:
    findings = _schema_findings(candidate) + _semantic(candidate)
    return Result(tuple(sorted(set(findings))))


def _deep_merge(target: dict[str, Any], patch: Mapping[str, Any]) -> dict[str, Any]:
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_merge(target[key], value)
        else:
            target[key] = copy.deepcopy(value)
    return target


def materialize_fixture(base: Mapping[str, Any], patch: Mapping[str, Any]) -> dict[str, Any]:
    candidate = _deep_merge(copy.deepcopy(dict(base)), patch)
    candidate["spec_hash"] = _canonical_hash(candidate)
    return candidate


def _load_profile() -> dict[str, Any]:
    value, findings = _read(PROFILE)
    if value is None:
        raise RuntimeError(",".join(finding.code for finding in findings))
    return value


def validate_fixtures() -> int:
    profile = _load_profile()
    base = profile["base"]
    rows: list[dict[str, Any]] = []
    ok = True

    for name, case in sorted(profile["valid"].items()):
        candidate = materialize_fixture(base, case["patch"])
        result = validate(candidate)
        passed = result.ok
        rows.append(
            {"fixture": name, "expected": "PASS", "actual": "PASS" if passed else "FAIL",
             "findings": [finding.code for finding in result.findings]}
        )
        ok = ok and passed

    for name, case in sorted(profile["invalid"].items()):
        candidate = materialize_fixture(base, case["patch"])
        result = validate(candidate)
        actual = sorted({finding.code for finding in result.findings})
        expected = sorted(case["expected_findings"])
        passed = actual == expected
        rows.append(
            {"fixture": name, "expected": expected, "actual": actual,
             "outcome": "PASS" if passed else "FAIL"}
        )
        ok = ok and passed

    print(json.dumps({"profile": profile["profile_id"], "ok": ok, "cases": rows},
                     sort_keys=True, separators=(",", ":")))
    return 0 if ok else 1


def _emit(path: Path, result: Result) -> None:
    print(json.dumps(
        {
            "path": path.as_posix(),
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "findings": [{"code": finding.code, "field": finding.field} for finding in result.findings],
        },
        sort_keys=True,
        separators=(",", ":"),
    ))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        if args.paths:
            parser.error("--fixtures does not accept file paths")
        return validate_fixtures()
    if not args.paths:
        parser.error("supply at least one JSON file or --fixtures")

    exit_code = 0
    for path in args.paths:
        candidate, read_findings = _read(path)
        result = Result(tuple(read_findings)) if candidate is None else validate(candidate)
        _emit(path, result)
        if result.error:
            exit_code = max(exit_code, 3)
        elif not result.ok:
            exit_code = max(exit_code, 2)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
