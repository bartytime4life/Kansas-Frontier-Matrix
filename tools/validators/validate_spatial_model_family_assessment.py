"""Validate fixture-only spatial model family assessments.

The validator checks declaration coherence only. It does not inspect spatial
data, execute transformations, dispatch production validators, establish
fitness or scientific truth, mutate registries or layers, or grant authority.
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
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/spatial_model_family_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/common/spatial_model_family_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:spatial-family:"
EXPECTED_LIMITATIONS = [
    "ASSESSMENT_ONLY",
    "NO_FITNESS_OR_SCIENTIFIC_VALIDATION",
    "NO_REGISTRY_OR_LAYER_MUTATION",
    "NO_RELEASE_DEPLOYMENT_OR_PUBLICATION_AUTHORITY",
    "NO_VALIDATOR_DISPATCH_AUTHORITY",
]
ABSTAIN_CODES = {
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SPATIAL_FAMILY_UNRESOLVED",
}
FLAG_BY_FAMILY = {
    "POSITION": "position_identity",
    "NETWORK": "node_edge_topology",
    "FIELD": "continuous_support",
    "TRANSFORMATION": "input_output_derivation",
}
EVIDENCE_BY_FAMILY = {
    "POSITION": "position_method_refs",
    "NETWORK": "network_topology_refs",
    "FIELD": "field_support_refs",
    "TRANSFORMATION": "transformation_lineage_refs",
}
DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "kfm://raw/",
    "kfm://work/",
    "kfm://quarantine/",
)
QUERY_MARKERS = ("match (", "select *", "sparql ", "cypher:")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


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


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


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
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
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
    subject.pop("assessment_id", None)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def compute_assessment_id(candidate: Mapping[str, object]) -> str:
    return IDENTITY_PREFIX + compute_profile_hash(candidate).split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
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


def _walk_strings(value: object, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path or "/", value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_strings(item, f"{path}/{index}")
    elif isinstance(value, Mapping):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from _walk_strings(value[key], f"{path}/{escaped}")


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    characteristics = candidate["characteristics"]
    evidence = candidate["family_evidence"]
    uncertainty = candidate["uncertainty"]
    review = candidate["review"]
    assert all(isinstance(item, Mapping) for item in (characteristics, evidence, uncertainty, review))

    for path, value in (
        *( (f"/family_evidence/{key}", evidence[key]) for key in EVIDENCE_BY_FAMILY.values() ),
        ("/family_evidence/component_assessment_refs", evidence["component_assessment_refs"]),
        ("/uncertainty/shared_uncertainty_refs", uncertainty["shared_uncertainty_refs"]),
        ("/uncertainty/family_partition_refs", uncertainty["family_partition_refs"]),
        ("/review/record_refs", review["record_refs"]),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCES_NOT_CANONICAL", path))

    limitations = candidate["limitations"]
    if not _canonical_strings(limitations) or limitations != EXPECTED_LIMITATIONS:
        findings.add(Finding("LIMITATION_SET_MISMATCH", "/limitations"))

    for path, text in _walk_strings(candidate):
        lowered = text.lower()
        if any(marker in lowered for marker in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))

    family = candidate["declared_family"]
    active_flags = {key for key, value in characteristics.items() if value is True}
    evidence_arrays = {name: evidence[name] for name in EVIDENCE_BY_FAMILY.values()}

    if family in FLAG_BY_FAMILY:
        expected_flag = FLAG_BY_FAMILY[family]
        expected_evidence = EVIDENCE_BY_FAMILY[family]
        if active_flags != {expected_flag}:
            findings.add(Finding("FAMILY_CHARACTERISTICS_INCOHERENT", "/characteristics"))
        if not evidence_arrays[expected_evidence]:
            findings.add(Finding("FAMILY_EVIDENCE_REQUIRED", f"/family_evidence/{expected_evidence}"))
        if any(values for name, values in evidence_arrays.items() if name != expected_evidence):
            findings.add(Finding("CROSS_FAMILY_EVIDENCE_UNDECLARED", "/family_evidence"))
        if evidence["component_assessment_refs"]:
            findings.add(Finding("BASE_FAMILY_COMPONENTS_DENIED", "/family_evidence/component_assessment_refs"))
        if uncertainty["partitioned_by_family"] or uncertainty["family_partition_refs"]:
            findings.add(Finding("BASE_FAMILY_UNCERTAINTY_PARTITION_DENIED", "/uncertainty"))
    elif family == "COMPOSITE":
        if len(active_flags) < 2:
            findings.add(Finding("COMPOSITE_FAMILIES_REQUIRED", "/characteristics"))
        for base_family, flag in FLAG_BY_FAMILY.items():
            refs = evidence_arrays[EVIDENCE_BY_FAMILY[base_family]]
            if flag in active_flags and not refs:
                findings.add(Finding("FAMILY_EVIDENCE_REQUIRED", f"/family_evidence/{EVIDENCE_BY_FAMILY[base_family]}"))
            if flag not in active_flags and refs:
                findings.add(Finding("CROSS_FAMILY_EVIDENCE_UNDECLARED", "/family_evidence"))
        if len(evidence["component_assessment_refs"]) < 2:
            findings.add(Finding("COMPOSITE_COMPONENTS_REQUIRED", "/family_evidence/component_assessment_refs"))
        if not uncertainty["partitioned_by_family"] or len(uncertainty["family_partition_refs"]) < 2:
            findings.add(Finding("COMPOSITE_UNCERTAINTY_PARTITION_REQUIRED", "/uncertainty"))
    else:
        findings.add(Finding("SPATIAL_FAMILY_UNRESOLVED", "/declared_family"))
        has_assertions = (
            bool(active_flags)
            or any(evidence_arrays.values())
            or bool(evidence["component_assessment_refs"])
            or bool(uncertainty["shared_uncertainty_refs"])
            or bool(uncertainty["partitioned_by_family"])
            or bool(uncertainty["family_partition_refs"])
        )
        if has_assertions:
            findings.add(Finding("UNRESOLVED_FAMILY_HAS_ASSERTIONS", "/declared_family"))

    if family != "UNRESOLVED" and not uncertainty["shared_uncertainty_refs"]:
        findings.add(Finding("UNCERTAINTY_REFERENCE_REQUIRED", "/uncertainty/shared_uncertainty_refs"))

    review_state = review["state"]
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif not review["record_refs"]:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
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
    candidate["assessment_id"] = compute_assessment_id(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    if entry.get("tamper") == "assessment_id":
        candidate["assessment_id"] = "kfm:spatial-family:" + "f" * 24
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})},
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only spatial model family assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    if candidate is None:
        result = ValidationResult("ERROR", tuple(sorted(findings)))
    else:
        result = validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
