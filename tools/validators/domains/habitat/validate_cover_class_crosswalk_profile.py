#!/usr/bin/env python3
"""Validate fixture-only Habitat cover-class crosswalk candidates.

PASS proves bounded synthetic consistency only. The validator does not recode
source data, activate sources, resolve evidence, decide policy, approve review,
transform a renderer, authorize release, publish, or authorize public use.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[4]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = (
    ROOT
    / "schemas/contracts/v1/domains/habitat/land_cover/cover_class_crosswalk_profile.schema.json"
)
FIXTURES = ROOT / "fixtures/domains/habitat/land_cover/crosswalk/profile_cases.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:cover-class-crosswalk:"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    profile_state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("CROSSWALK_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("CROSSWALK_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("CROSSWALK_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("CROSSWALK_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("CROSSWALK_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("CROSSWALK_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("CROSSWALK_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("CROSSWALK_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"candidate_id", "spec_hash"}
    }
    spec_hash = compute_spec_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _version_bound(scheme: Mapping[str, Any]) -> bool:
    return scheme["ontology_ref"].endswith("@" + scheme["scheme_version"])


def expected_summary(value: Mapping[str, Any]) -> dict[str, Any]:
    source_codes = set(value["source_scheme"]["class_codes"])
    mappings = value["mappings"]
    accounted = {
        code
        for row in mappings
        for code in row["source_codes"]
        if code in source_codes
    }
    explicitly_unmapped = {
        code
        for row in mappings
        if row["mapping_state"] in {"DENIED", "UNMAPPED"}
        for code in row["source_codes"]
        if code in source_codes
    }
    missing = source_codes - accounted
    return {
        "ontology_versions_bound": (
            _version_bound(value["source_scheme"])
            and _version_bound(value["target_scheme"])
        ),
        "source_class_count": len(source_codes),
        "accounted_source_class_count": len(accounted),
        "unmapped_source_class_count": len(explicitly_unmapped | missing),
        "mapping_row_count": len(mappings),
        "lossy_row_count": sum(bool(row["lossy"]) for row in mappings),
        "caveat_row_count": sum(bool(row["caveat_required"]) for row in mappings),
        "profile_state": "REVIEW_REQUIRED",
        "silent_recode_authorized": False,
        "reverse_use_authorized": False,
        "production_use_authorized": False,
    }


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("CROSSWALK_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("CROSSWALK_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("CROSSWALK_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def _order_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    for name in ("source_scheme", "target_scheme"):
        codes = value[name]["class_codes"]
        if codes != sorted(codes):
            findings.add(Finding("CROSSWALK_CLASS_CODE_ORDER_INVALID", f"/{name}/class_codes"))
    rows = value["mappings"]
    row_ids = [row["row_id"] for row in rows]
    if row_ids != sorted(row_ids):
        findings.add(Finding("CROSSWALK_ROW_ORDER_INVALID", "/mappings"))
    if len(row_ids) != len(set(row_ids)):
        findings.add(Finding("CROSSWALK_ROW_ID_DUPLICATE", "/mappings"))
    for index, row in enumerate(rows):
        for field in ("source_codes", "target_codes", "evidence_refs"):
            if row[field] != sorted(row[field]):
                findings.add(
                    Finding(
                        "CROSSWALK_ROW_VALUE_ORDER_INVALID",
                        f"/mappings/{index}/{field}",
                    )
                )
    evidence_refs = value["crosswalk"]["evidence_refs"]
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding("CROSSWALK_EVIDENCE_ORDER_INVALID", "/crosswalk/evidence_refs"))
    return findings


def _mapping_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    source_inventory = set(value["source_scheme"]["class_codes"])
    target_inventory = set(value["target_scheme"]["class_codes"])
    seen: set[str] = set()

    for index, row in enumerate(value["mappings"]):
        path = f"/mappings/{index}"
        source_codes = row["source_codes"]
        target_codes = row["target_codes"]
        state = row["mapping_state"]

        if seen.intersection(source_codes):
            findings.add(Finding("CROSSWALK_SOURCE_CODE_DUPLICATE", "/mappings"))
        seen.update(source_codes)
        if any(code not in source_inventory for code in source_codes):
            findings.add(Finding("CROSSWALK_SOURCE_CODE_UNKNOWN", f"{path}/source_codes"))
        if any(code not in target_inventory for code in target_codes):
            findings.add(Finding("CROSSWALK_TARGET_CODE_UNKNOWN", f"{path}/target_codes"))

        if state == "EXACT":
            if len(source_codes) != 1 or len(target_codes) != 1:
                findings.add(Finding("CROSSWALK_EXACT_SHAPE_INVALID", path))
            if row["lossy"] or row["caveat_required"]:
                findings.add(Finding("CROSSWALK_EXACT_POSTURE_INVALID", path))
        elif state == "AGGREGATED":
            if len(source_codes) < 2 or len(target_codes) != 1:
                findings.add(Finding("CROSSWALK_AGGREGATION_SHAPE_INVALID", path))
            if not row["lossy"]:
                findings.add(Finding("CROSSWALK_AGGREGATION_NOT_LOSSY", f"{path}/lossy"))
            if not row["caveat_required"]:
                findings.add(Finding("CROSSWALK_AGGREGATION_CAVEAT_REQUIRED", f"{path}/caveat_required"))
        elif state == "SPLIT":
            if len(source_codes) != 1 or len(target_codes) < 2:
                findings.add(Finding("CROSSWALK_SPLIT_SHAPE_INVALID", path))
            if not row["lossy"]:
                findings.add(Finding("CROSSWALK_SPLIT_NOT_LOSSY", f"{path}/lossy"))
            if not row["caveat_required"]:
                findings.add(Finding("CROSSWALK_SPLIT_CAVEAT_REQUIRED", f"{path}/caveat_required"))
        elif state == "AMBIGUOUS":
            if not target_codes:
                findings.add(Finding("CROSSWALK_AMBIGUOUS_TARGET_REQUIRED", f"{path}/target_codes"))
            if not row["lossy"] or not row["caveat_required"]:
                findings.add(Finding("CROSSWALK_AMBIGUOUS_POSTURE_INVALID", path))
        elif state == "NODATA":
            if target_codes or row["lossy"] or not row["caveat_required"]:
                findings.add(Finding("CROSSWALK_NODATA_POSTURE_INVALID", path))
        else:
            if target_codes or not row["caveat_required"]:
                findings.add(Finding("CROSSWALK_UNMAPPED_POSTURE_INVALID", path))
            findings.add(Finding("CROSSWALK_UNMAPPED_CLASS_DENIED", path))

    missing = source_inventory - seen
    if missing:
        findings.add(Finding("CROSSWALK_SOURCE_CLASS_UNACCOUNTED", "/mappings"))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings = _order_findings(value)
    findings.update(_mapping_findings(value))

    if value["source_scheme"]["scheme_id"] == value["target_scheme"]["scheme_id"]:
        findings.add(Finding("CROSSWALK_SCHEME_ID_COLLISION", "/target_scheme/scheme_id"))
    for name in ("source_scheme", "target_scheme"):
        if not _version_bound(value[name]):
            findings.add(
                Finding("CROSSWALK_ONTOLOGY_VERSION_MISMATCH", f"/{name}/ontology_ref")
            )
    if value["crosswalk"]["directionality"] != "FORWARD_ONLY":
        findings.add(
            Finding(
                "CROSSWALK_REVERSE_USE_REVIEW_REQUIRED",
                "/crosswalk/directionality",
            )
        )
    if value["summary"] != expected_summary(value):
        findings.add(Finding("CROSSWALK_SUMMARY_MISMATCH", "/summary"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)

    findings = _semantic_findings(value)
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("CROSSWALK_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("CROSSWALK_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["candidate_id"] != expected_id:
            findings.add(Finding("CROSSWALK_ID_MISMATCH", "/candidate_id"))

    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if not case.get("preserve_summary", False):
        document["summary"] = expected_summary(document)
    document["spec_hash"], document["candidate_id"] = canonical_identity(document)
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "candidate_id_override" in case:
        document["candidate_id"] = case["candidate_id_override"]
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.profile_state != case["expected_profile_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_profile_state": case["expected_profile_state"],
                    "actual_profile_state": result.profile_state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "recodes_source_data": False,
                "activates_sources": False,
                "resolves_evidence": False,
                "decides_policy": False,
                "approves_review": False,
                "controls_renderer": False,
                "authorizes_release": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [
                {"code": item.code, "path": item.path} for item in result.findings
            ],
            "outcome": result.outcome,
            "profile_state": result.profile_state,
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
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
