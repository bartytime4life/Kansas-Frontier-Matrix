#!/usr/bin/env python3
"""Validate the inactive, fixture-only LayerManifest candidate profile.

The legacy permissive id-only profile remains accepted. Strict candidates get
closed-schema and deterministic semantic checks only; PASS creates no evidence,
policy, review, release, publication, signature, registry, or public-use authority.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:  # fail closed in hosted validation
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_IMPORT_ERROR: Exception | None = exc
else:
    HASH_IMPORT_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/data/layer_manifest.schema.json"
FIXTURES = ROOT / "fixtures/data/layer_manifest"
MANIFEST = FIXTURES / "expected_findings_manifest.json"
SCOPE = "layer-manifest-fixture-only-v1"
MAX_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
FLOATING_LATEST = re.compile(r"(^|[:/@._-])latest($|[:/@._-])", re.I)
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "HASHING_UNAVAILABLE",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_value: str) -> object:
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
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda e: (_pointer(e.absolute_path), str(e.validator)))
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("id", None)
    subject.pop("spec_hash", None)
    return subject


def compute_manifest_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_IMPORT_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing package unavailable") from HASH_IMPORT_ERROR
    return compute_spec_hash(identity_subject(candidate))


def compute_manifest_id(candidate: Mapping[str, Any]) -> str:
    digest = compute_manifest_spec_hash(candidate).removeprefix("sha256:")
    return "layer-manifest:" + digest[:24]


def _canonical(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _dt(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
    except ValueError:
        return None


def _iter_refs(candidate: Mapping[str, Any]) -> Iterable[tuple[str, object]]:
    scalar = ("catalog_ref", "release_manifest_ref", "promotion_decision_ref", "style_manifest_ref")
    for name in scalar:
        yield f"/{name}", candidate.get(name)
    for name in ("source_descriptor_refs", "evidence_bundle_refs", "policy_decision_refs", "review_record_refs"):
        value = candidate.get(name)
        if isinstance(value, list):
            for index, item in enumerate(value):
                yield f"/{name}/{index}", item
    representation = candidate.get("representation")
    if isinstance(representation, Mapping):
        yield "/representation/artifact_ref", representation.get("artifact_ref")
    exposure = candidate.get("exposure")
    if isinstance(exposure, Mapping):
        for index, item in enumerate(exposure.get("transform_receipt_refs", []) if isinstance(exposure.get("transform_receipt_refs"), list) else []):
            yield f"/exposure/transform_receipt_refs/{index}", item
    lineage = candidate.get("lineage")
    if isinstance(lineage, Mapping):
        yield "/lineage/previous_manifest_ref", lineage.get("previous_manifest_ref")
        yield "/lineage/rollback_ref", lineage.get("rollback_ref")
        for index, item in enumerate(lineage.get("correction_refs", []) if isinstance(lineage.get("correction_refs"), list) else []):
            yield f"/lineage/correction_refs/{index}", item
    provenance = candidate.get("provenance")
    if isinstance(provenance, Mapping):
        yield "/provenance/run_receipt_ref", provenance.get("run_receipt_ref")


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    if candidate.get("object_type") != "LayerManifest":
        return []
    findings: set[Finding] = set()
    try:
        if candidate.get("spec_hash") != compute_manifest_spec_hash(candidate):
            findings.add(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("id") != compute_manifest_id(candidate):
            findings.add(Finding("MANIFEST_ID_MISMATCH", "/id"))
    except (TypeError, ValueError, RuntimeError, RecursionError):
        findings.add(Finding("HASHING_UNAVAILABLE", "/spec_hash"))

    for name in ("source_descriptor_refs", "evidence_bundle_refs", "policy_decision_refs", "review_record_refs"):
        if not _canonical(candidate.get(name)):
            findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/{name}"))
    exposure = candidate.get("exposure")
    if isinstance(exposure, Mapping):
        for name in ("public_field_allowlist", "transform_receipt_refs"):
            if not _canonical(exposure.get(name)):
                findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", f"/exposure/{name}"))
    lineage = candidate.get("lineage")
    if isinstance(lineage, Mapping) and not _canonical(lineage.get("correction_refs")):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL", "/lineage/correction_refs"))

    roles: list[str] = []
    for path, value in _iter_refs(candidate):
        if isinstance(value, str):
            roles.append(value)
            if FLOATING_LATEST.search(value):
                findings.add(Finding("FLOATING_REFERENCE_DENIED", path))
    if len(roles) != len(set(roles)):
        findings.add(Finding("REFERENCE_ROLE_COLLAPSE", "/"))

    representation = candidate.get("representation")
    if isinstance(representation, Mapping):
        protocol = representation.get("protocol")
        source_layer = representation.get("source_layer")
        if protocol in {"PMTILES", "XYZ"} and not isinstance(source_layer, str):
            findings.add(Finding("SOURCE_LAYER_REQUIRED", "/representation/source_layer"))
        if protocol in {"COG", "GEOJSON_FIXTURE"} and source_layer is not None:
            findings.add(Finding("SOURCE_LAYER_FORBIDDEN", "/representation/source_layer"))
        if isinstance(representation.get("min_zoom"), int) and isinstance(representation.get("max_zoom"), int) and representation["min_zoom"] > representation["max_zoom"]:
            findings.add(Finding("ZOOM_RANGE_INCOHERENT", "/representation"))
        bounds = representation.get("bounds")
        if isinstance(bounds, list) and len(bounds) == 4 and all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in bounds):
            west, south, east, north = bounds
            if not (-180 <= west < east <= 180 and -90 <= south < north <= 90):
                findings.add(Finding("BOUNDS_INCOHERENT", "/representation/bounds"))

    temporal = candidate.get("temporal")
    if isinstance(temporal, Mapping):
        start, end = _dt(temporal.get("valid_from")), _dt(temporal.get("valid_to"))
        if start is not None and end is not None and start > end:
            findings.add(Finding("TEMPORAL_WINDOW_INCOHERENT", "/temporal"))

    if isinstance(exposure, Mapping):
        public = exposure.get("audience") == "PUBLIC"
        if public and exposure.get("rights_status") != "APPROVED":
            findings.add(Finding("PUBLIC_RIGHTS_NOT_APPROVED", "/exposure/rights_status"))
        if public and exposure.get("sensitivity_status") not in {"PUBLIC_SAFE", "TRANSFORM_REQUIRED"}:
            findings.add(Finding("PUBLIC_SENSITIVITY_NOT_APPROVED", "/exposure/sensitivity_status"))
        if public and not exposure.get("public_field_allowlist"):
            findings.add(Finding("PUBLIC_FIELD_ALLOWLIST_REQUIRED", "/exposure/public_field_allowlist"))
        if exposure.get("sensitivity_status") == "TRANSFORM_REQUIRED" and (
            exposure.get("generalized_geometry") is not True or not exposure.get("transform_receipt_refs")
        ):
            findings.add(Finding("TRANSFORM_EVIDENCE_REQUIRED", "/exposure"))

    governance = candidate.get("governance")
    if isinstance(governance, Mapping) and any(value is not False for value in governance.values()):
        findings.add(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))
    return sorted(findings)


def _outcome(findings: Sequence[Finding]) -> str:
    return "ERROR" if any(item.code in ERROR_CODES for item in findings) else ("FAIL" if findings else "PASS")


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is not None:
        schema_findings = _schema_findings(candidate)
        findings.extend(schema_findings)
        if not schema_findings:
            findings.extend(_semantic(candidate))
    ordered = tuple(sorted(set(findings)))
    return ValidationResult(_outcome(ordered), ordered)


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "authority_created": False,
            "file": _display(path),
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    manifest, _ = _read(MANIFEST)
    if manifest is None:
        return 1
    passed, seen = True, set()
    for group in ("valid", "invalid"):
        cases = manifest.get(group)
        if not isinstance(cases, Mapping):
            return 1
        for filename, expected in sorted(cases.items()):
            if not isinstance(filename, str) or not isinstance(expected, Mapping):
                passed = False
                continue
            path = FIXTURES / group / filename
            result = validate_record(path)
            print(serialize(path, result))
            actual = sorted({item.code for item in result.findings})
            if result.outcome != expected.get("outcome") or actual != expected.get("findings"):
                passed = False
            seen.add(f"{group}/{filename}")
    actual_files = {path.relative_to(FIXTURES).as_posix() for path in FIXTURES.glob("*/*.json")}
    return 0 if passed and seen == actual_files else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        return run_fixture_profile()
    if not args.files:
        parser.error("provide one or more files or --fixtures")
    results = [validate_record(path) for path in args.files]
    for path, result in zip(args.files, results):
        print(serialize(path, result))
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
