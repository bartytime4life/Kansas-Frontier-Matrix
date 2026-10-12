#!/usr/bin/env python3
"""Validate fixture-first representation fitness assessments."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA = REPO_ROOT / "schemas/contracts/v1/evidence/representation_fitness_assessment.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/evidence/representation_fitness_assessment"
MAX_BYTES = 2 * 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


def _pointer(parts: Iterable[object]) -> str:
    values = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(values) if values else "/"


def read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    except UnicodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_UNREADABLE", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("spec_hash", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _time(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00").astimezone(timezone.utc)
    except ValueError:
        return None


def schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    if value.get("spec_hash") != canonical_hash(value):
        findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    dimensions = value.get("dimensions")
    states: list[str] = []
    if isinstance(dimensions, dict):
        for name in ("positional", "thematic", "temporal", "completeness", "lineage"):
            item = dimensions.get(name)
            if isinstance(item, dict) and isinstance(item.get("outcome"), str):
                states.append(item["outcome"])
    derived = (
        "NOT_FIT" if "UNSUPPORTED" in states else
        "UNKNOWN" if "UNKNOWN" in states else
        "CONDITIONALLY_FIT" if "CONDITIONALLY_SUPPORTED" in states else
        "FIT"
    )
    if value.get("overall_outcome") != derived:
        findings.append(Finding("FITNESS_OUTCOME_MISMATCH", "/overall_outcome"))

    reasons = value.get("reason_codes")
    obligations = value.get("obligations")
    if derived in {"NOT_FIT", "UNKNOWN"} and (not isinstance(reasons, list) or not reasons):
        findings.append(Finding("FITNESS_REASON_REQUIRED", "/reason_codes"))
    if derived == "CONDITIONALLY_FIT" and (not isinstance(obligations, list) or not obligations):
        findings.append(Finding("FITNESS_OBLIGATION_REQUIRED", "/obligations"))

    subject = value.get("subject")
    use = value.get("intended_use")
    if isinstance(subject, dict):
        support = subject.get("spatial_support")
        if isinstance(support, dict):
            nominal = support.get("nominal_resolution_m")
            declared = support.get("declared_precision_m")
            if isinstance(nominal, (int, float)) and isinstance(declared, (int, float)) and declared < nominal:
                findings.append(Finding("REPRESENTATION_FALSE_PRECISION", "/subject/spatial_support/declared_precision_m"))
            if (
                support.get("generalized") is True
                and isinstance(use, dict)
                and use.get("consequence_level") == "HIGH"
                and derived == "FIT"
            ):
                findings.append(Finding("GENERALIZED_HIGH_CONSEQUENCE_FIT_DENIED", "/overall_outcome"))

        role = subject.get("source_role")
        use_class = use.get("use_class") if isinstance(use, dict) else None
        if role == "CANDIDATE" and derived in {"FIT", "CONDITIONALLY_FIT"}:
            findings.append(Finding("CANDIDATE_FITNESS_DENIED", "/subject/source_role"))
        if role == "SYNTHETIC":
            if use_class == "OPERATIONAL_DECISION" and derived in {"FIT", "CONDITIONALLY_FIT"}:
                findings.append(Finding("SYNTHETIC_OPERATIONAL_FITNESS_DENIED", "/intended_use/use_class"))
            if derived in {"FIT", "CONDITIONALLY_FIT"} and (not isinstance(obligations, list) or "REALITY_BOUNDARY_REQUIRED" not in obligations):
                findings.append(Finding("REALITY_BOUNDARY_OBLIGATION_REQUIRED", "/obligations"))

    evaluated = _time(value.get("evaluated_at"))
    expires = _time(value.get("expires_at")) if value.get("expires_at") is not None else None
    if evaluated is None or (expires is not None and expires <= evaluated):
        findings.append(Finding("FITNESS_TIME_INVALID", "/expires_at"))
    return findings


def validate(path: Path) -> Result:
    value, findings = read(path)
    if value is None:
        return Result(tuple(sorted(set(findings))))
    findings.extend(schema_findings(value))
    if not findings:
        findings.extend(semantic_findings(value))
    return Result(tuple(sorted(set(findings))))


def serialize(path: Path, result: Result) -> str:
    try:
        display = path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        display = path.name
    return json.dumps({"file": display, "findings": [{"code": item.code, "path": item.path} for item in result.findings], "outcome": "PASS" if result.ok else "FAIL", "scope": "representation-fitness-fixture-only"}, sort_keys=True, separators=(",", ":"))


def fixture_profile() -> int:
    valid = sorted((FIXTURES / "valid").glob("*.json"))
    invalid = sorted((FIXTURES / "invalid").glob("*.json"))
    if not valid or not invalid:
        return 1
    ok = True
    for path in valid:
        result = validate(path)
        print(serialize(path, result))
        ok = result.ok and ok
    for path in invalid:
        result = validate(path)
        print(serialize(path, result))
        ok = (not result.ok) and ok
    return 0 if ok else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return fixture_profile()
    if not args.files:
        parser.error("provide files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        result = validate(path)
        print(serialize(path, result))
        rc = max(rc, 0 if result.ok else 1)
    return rc


if __name__ == "__main__":
    raise SystemExit(run())
