"""Validate fixture-only rolling-metric window disclosures.

The validator checks local declaration coherence. It does not inspect source
values, generate or execute SQL, calculate a metric, prove engine parity,
resolve evidence, decide policy or review, release, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/rolling_metric_window_disclosure.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/rolling_metric_window_disclosure/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "CLAIM_SCOPE_UNRESOLVED",
    "ENGINE_PARITY_UNRESOLVED",
    "TIME_DEFINITION_UNRESOLVED",
}
OFFSET_KINDS = {"OFFSET_PRECEDING", "OFFSET_FOLLOWING"}


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when a JSON number is not finite."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (
            tuple(str(part) for part in error.absolute_path),
            str(error.validator),
        ),
    )
    return [
        Finding(
            "SCHEMA_INVALID",
            "/" + "/".join(str(part) for part in error.absolute_path),
        )
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _bound_offset_is_coherent(bound: Mapping[str, object]) -> bool:
    kind = bound["kind"]
    offset = bound["offset"]
    return (kind in OFFSET_KINDS and isinstance(offset, int)) or (
        kind not in OFFSET_KINDS and offset is None
    )


def _bound_position(bound: Mapping[str, object]) -> float:
    kind = bound["kind"]
    offset = bound["offset"]
    if kind == "UNBOUNDED_PRECEDING":
        return -math.inf
    if kind == "UNBOUNDED_FOLLOWING":
        return math.inf
    if kind == "CURRENT_ROW":
        return 0.0
    assert isinstance(offset, int)
    return float(-offset if kind == "OFFSET_PRECEDING" else offset)


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    claim_scope = candidate["claim_scope"]
    assert isinstance(claim_scope, Mapping)
    if claim_scope["resolution"] == "UNRESOLVED":
        findings.add(Finding("CLAIM_SCOPE_UNRESOLVED", "/claim_scope/resolution"))

    partition = candidate["partition"]
    assert isinstance(partition, Mapping)
    partition_keys = partition["keys"]
    if not _canonical_strings(partition_keys):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/partition/keys"))
    if (partition["mode"] == "GLOBAL" and partition_keys) or (
        partition["mode"] == "KEYED" and not partition_keys
    ):
        findings.add(Finding("PARTITION_DECLARATION_MISMATCH", "/partition"))

    ordering = candidate["ordering"]
    assert isinstance(ordering, Mapping)
    ordering_keys = ordering["keys"]
    assert isinstance(ordering_keys, list)
    field_refs = [item["field_ref"] for item in ordering_keys]
    if len(field_refs) != len(set(field_refs)):
        findings.add(Finding("ORDERING_FIELD_DUPLICATE", "/ordering/keys"))
    window_time_positions = [
        index for index, item in enumerate(ordering_keys) if item["role"] == "WINDOW_TIME"
    ]
    if window_time_positions != [0]:
        findings.add(Finding("TIME_ORDERING_KEY_INVALID", "/ordering/keys"))
    if not ordering["unique_order_guaranteed"] and not any(
        item["role"] == "TIE_BREAKER" for item in ordering_keys
    ):
        findings.add(Finding("ORDERING_TIE_BREAKER_REQUIRED", "/ordering/keys"))

    time_definition = candidate["time_definition"]
    assert isinstance(time_definition, Mapping)
    if time_definition["resolution"] == "UNRESOLVED":
        findings.add(
            Finding("TIME_DEFINITION_UNRESOLVED", "/time_definition/resolution")
        )
    if ordering_keys and time_definition["field_ref"] != ordering_keys[0]["field_ref"]:
        findings.add(
            Finding("TIME_FIELD_ORDERING_MISMATCH", "/time_definition/field_ref")
        )

    frame = candidate["frame"]
    assert isinstance(frame, Mapping)
    start = frame["start"]
    end = frame["end"]
    assert isinstance(start, Mapping) and isinstance(end, Mapping)
    offsets_coherent = True
    for name, bound in (("start", start), ("end", end)):
        if not _bound_offset_is_coherent(bound):
            offsets_coherent = False
            findings.add(Finding("FRAME_OFFSET_MISMATCH", f"/frame/{name}"))
    if offsets_coherent and _bound_position(start) > _bound_position(end):
        findings.add(Finding("FRAME_BOUNDS_INVALID", "/frame"))
    has_offset = start["kind"] in OFFSET_KINDS or end["kind"] in OFFSET_KINDS
    if frame["unit"] == "RANGE":
        if has_offset and frame["offset_unit_ref"] is None:
            findings.add(Finding("RANGE_OFFSET_UNIT_REQUIRED", "/frame/offset_unit_ref"))
        if not has_offset and frame["offset_unit_ref"] is not None:
            findings.add(Finding("FRAME_OFFSET_UNIT_UNEXPECTED", "/frame/offset_unit_ref"))
    elif frame["offset_unit_ref"] is not None:
        findings.add(Finding("FRAME_OFFSET_UNIT_UNEXPECTED", "/frame/offset_unit_ref"))

    missing_data = candidate["missing_data"]
    assert isinstance(missing_data, Mapping)
    treatment = missing_data["treatment"]
    method_required = treatment in {
        "IMPUTE_DECLARED",
        "ZERO_FILL_DECLARED",
        "SOURCE_DEFINED",
    } or missing_data["partial_window_behavior"] == "SOURCE_DEFINED"
    if method_required and missing_data["method_ref"] is None:
        findings.add(Finding("MISSING_DATA_METHOD_REQUIRED", "/missing_data/method_ref"))
    if not method_required and missing_data["method_ref"] is not None:
        findings.add(Finding("MISSING_DATA_METHOD_UNEXPECTED", "/missing_data/method_ref"))

    engine_parity = candidate["engine_parity"]
    assert isinstance(engine_parity, Mapping)
    engine_refs = engine_parity["engine_refs"]
    parity_refs = engine_parity["parity_fixture_refs"]
    for field, value in (("engine_refs", engine_refs), ("parity_fixture_refs", parity_refs)):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/engine_parity/{field}"))
    engine_state = engine_parity["state"]
    if (len(engine_refs) == 1) != (engine_state == "SINGLE_ENGINE_DECLARED"):
        findings.add(
            Finding("ENGINE_PARITY_DECLARATION_MISMATCH", "/engine_parity/state")
        )
    if engine_state == "SINGLE_ENGINE_DECLARED" and parity_refs:
        findings.add(
            Finding(
                "ENGINE_PARITY_DECLARATION_MISMATCH",
                "/engine_parity/parity_fixture_refs",
            )
        )
    if engine_state == "SYNTHETIC_PARITY_DECLARED" and not parity_refs:
        findings.add(
            Finding(
                "ENGINE_PARITY_DECLARATION_MISMATCH",
                "/engine_parity/parity_fixture_refs",
            )
        )
    if engine_state == "UNRESOLVED":
        findings.add(Finding("ENGINE_PARITY_UNRESOLVED", "/engine_parity/state"))
    elif engine_state == "MISMATCH":
        findings.add(Finding("CROSS_ENGINE_PARITY_MISMATCH", "/engine_parity/state"))

    disclosure = candidate["disclosure"]
    assert isinstance(disclosure, Mapping)
    review_refs = disclosure["review_record_refs"]
    if not _canonical_strings(review_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/disclosure/review_record_refs"))
    if disclosure["intended_use"] == "PUBLIC_CANDIDATE":
        if not review_refs:
            findings.add(
                Finding("PUBLIC_REVIEW_REFERENCE_REQUIRED", "/disclosure/review_record_refs")
            )
        if disclosure["release_manifest_ref"] is None:
            findings.add(
                Finding("PUBLIC_RELEASE_REFERENCE_REQUIRED", "/disclosure/release_manifest_ref")
            )
    elif disclosure["release_manifest_ref"] is not None:
        findings.add(
            Finding("INTERNAL_RELEASE_REFERENCE_UNEXPECTED", "/disclosure/release_manifest_ref")
        )

    if not _canonical_strings(candidate["evidence_refs"]):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/evidence_refs"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(
    path: Path = FIXTURE_PATH,
) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [
            {
                "name": "fixture_manifest",
                "ok": False,
                "observed": {
                    "outcome": "ERROR",
                    "codes": sorted({item.code for item in load_findings}),
                },
            }
        ]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append(
            {
                "name": entry["name"],
                "ok": observed == expected,
                "expected": expected,
                "observed": observed,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only rolling-metric window disclosures."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(
        json.dumps(
            {"outcome": result.outcome, "codes": result.codes},
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
