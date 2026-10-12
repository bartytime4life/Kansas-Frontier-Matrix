"""Validate the fixture-first FrontierRouteTrustStatus projection.

The validator is deterministic and no-network. A pass establishes only schema
and cross-field conformance for a UI projection; it does not establish source
truth, policy approval, rights clearance, evidence closure, review authority,
release, promotion, deployment, or publication.
"""

from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/roads-rail-trade/frontier_route_trust_status.schema.json"
FIXTURES_ROOT = REPO_ROOT / "fixtures/domains/roads-rail-trade/frontier_route_trust_status"
MAX_JSON_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 50

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str

class DuplicateKeyError(ValueError):
    pass

class NonFiniteNumberError(ValueError):
    pass

def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result

def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError

def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed

def _load_json(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/", "symbolic links are denied")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/", "input is not a regular file")]
        if path.stat().st_size > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/", "input exceeds 2 MiB")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicate_keys, parse_constant=_reject_nonfinite, parse_float=_parse_finite_float)
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate object member")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/", "numbers must be finite")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/", "input is not valid JSON")]
    except (OSError, UnicodeError, RecursionError, ValueError):
        return None, [Finding("INPUT_UNREADABLE", "/", "input could not be read safely")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/", "root must be an object")]
    return value, []

def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())

def _schema_findings(payload: Mapping[str, object]) -> list[Finding]:
    errors = list(islice(_schema_validator().iter_errors(payload), MAX_SCHEMA_FINDINGS + 1))
    errors = sorted(errors, key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path), f"schema constraint failed: {error.validator}") for error in errors[:MAX_SCHEMA_FINDINGS]]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/", "schema findings truncated"))
    return findings

def _feature_rows(payload: Mapping[str, object]) -> list[Mapping[str, object]]:
    value = payload.get("features")
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict)]

def _expected_collection_decision(features: Sequence[Mapping[str, object]]) -> str | None:
    decisions = {item.get("decision") for item in features}
    if not decisions or not decisions.issubset({"publish", "quarantine", "deny"}):
        return None
    if decisions == {"publish"}:
        return "publish"
    if decisions == {"deny"}:
        return "deny"
    if "deny" in decisions:
        return "deny-partial"
    return "quarantine-partial"

def _semantic_findings(payload: Mapping[str, object]) -> list[Finding]:
    findings: list[Finding] = []
    features = _feature_rows(payload)
    seen: set[str] = set()
    for index, feature in enumerate(features):
        kfm_id = feature.get("kfm_id")
        if isinstance(kfm_id, str):
            if kfm_id in seen:
                findings.append(Finding("DUPLICATE_FEATURE_ID", f"/features/{index}/kfm_id", "kfm_id values must be unique within the projection"))
            seen.add(kfm_id)
        decision = feature.get("decision")
        visible = feature.get("visible_in_public_catalog")
        if isinstance(visible, bool) and visible != (decision == "publish"):
            findings.append(Finding("VISIBILITY_DECISION_MISMATCH", f"/features/{index}/visible_in_public_catalog", "public visibility must be true if and only if decision is publish"))
        release_id = feature.get("release_id")
        release_bound = isinstance(release_id, str) and bool(release_id)
        if (decision == "publish" and not release_bound) or (decision in {"quarantine", "deny"} and release_id is not None):
            findings.append(Finding("RELEASE_BINDING_MISMATCH", f"/features/{index}/release_id", "publish requires a release id; quarantine and deny require null"))
    expected = _expected_collection_decision(features)
    if expected is not None and payload.get("collection_decision") != expected:
        findings.append(Finding("COLLECTION_DECISION_MISMATCH", "/collection_decision", f"collection decision must be {expected} for the feature dispositions"))
    if payload.get("audience") == "public":
        leaked = [index for index, feature in enumerate(features) if feature.get("decision") != "publish" or feature.get("visible_in_public_catalog") is not True or not isinstance(feature.get("release_id"), str)]
        if leaked or payload.get("collection_decision") != "publish":
            findings.append(Finding("PUBLIC_PROJECTION_LEAK", "/features", "public projections may contain only released publish entries"))
    return findings

def validate_payload(path: Path) -> tuple[Finding, ...]:
    payload, findings = _load_json(path)
    if payload is None:
        return tuple(sorted(findings))
    schema_findings = _schema_findings(payload)
    if schema_findings:
        return tuple(sorted(set(schema_findings)))
    return tuple(sorted(set(_semantic_findings(payload))))

def _expected_code(path: Path) -> str | None:
    sidecar = path.with_suffix(".expected_code.txt")
    try:
        if sidecar.is_symlink() or not sidecar.is_file() or sidecar.stat().st_size > 128:
            return None
        value = sidecar.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError):
        return None
    return value or None

def run_fixtures() -> int:
    valid = sorted((FIXTURES_ROOT / "valid").glob("*.json"))
    invalid = sorted((FIXTURES_ROOT / "invalid").glob("*.json"))
    if not valid or not invalid:
        print("FRONTIER_ROUTE_TRUST_FIXTURES_ERROR nonempty valid and invalid lanes are required")
        return 2
    failures: list[str] = []
    for path in valid:
        if validate_payload(path):
            failures.append(f"valid/{path.name}")
    for path in invalid:
        findings = validate_payload(path)
        expected = _expected_code(path)
        if expected is None or expected not in {finding.code for finding in findings}:
            failures.append(f"invalid/{path.name}")
    if failures:
        for name in failures:
            print(f"FRONTIER_ROUTE_TRUST_FIXTURE_POLARITY_FAIL file={name}")
        return 1
    print(f"FRONTIER_ROUTE_TRUST_FIXTURES_VALID valid={len(valid)} invalid={len(invalid)} no_network=true projection_only=true")
    return 0

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser

def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        if args.payload is not None:
            raise SystemExit("--fixtures cannot be combined with a payload")
        return run_fixtures()
    if args.payload is None:
        raise SystemExit("payload is required unless --fixtures is used")
    findings = validate_payload(args.payload)
    if not findings:
        print(f"FRONTIER_ROUTE_TRUST_STATUS_VALID file={args.payload.name}")
        return 0
    for finding in findings:
        print(f"FRONTIER_ROUTE_TRUST_STATUS_INVALID code={finding.code} field={finding.field} detail={finding.detail}")
    return 1

if __name__ == "__main__":
    raise SystemExit(main())
