"""Validate fixture-only PLANTS taxa-drift assessment candidates.

The validator compares synthetic, attested taxa inventories under one taxonomy
version and checks non-public sensitivity posture. It does not contact PLANTS or
any occurrence source, resolve taxonomy or conservation status, admit a source,
create a SourceIntakeRecord, mutate lifecycle state, or authorize publication.
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

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/source/plants_taxa_drift_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/source/plants_taxa_drift_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:plants-taxa-drift:"
ABSTAIN_CODES = {
    "MATERIALITY_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
    "SENSITIVITY_INTERSECTION_UNKNOWN",
    "TAXONOMY_VERSION_DRIFT",
}
DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "raw/",
    "work/",
    "quarantine/",
)
QUERY_MARKERS = ("match (", "select *", "sparql ", "graph_query", "cypher:")


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


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z"):
        return None
    try:
        return datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None


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


def _snapshot_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    pair = candidate["snapshot_pair"]
    assert isinstance(pair, Mapping)
    prior = pair["prior"]
    current = pair["current"]
    assert isinstance(prior, Mapping) and isinstance(current, Mapping)

    prior_time = _parse_utc(prior.get("observed_at"))
    current_time = _parse_utc(current.get("observed_at"))
    assessed_time = _parse_utc(candidate.get("observed_at"))
    if prior_time is None:
        findings.add(Finding("PRIOR_OBSERVED_AT_NOT_UTC", "/snapshot_pair/prior/observed_at"))
    if current_time is None:
        findings.add(Finding("CURRENT_OBSERVED_AT_NOT_UTC", "/snapshot_pair/current/observed_at"))
    if assessed_time is None:
        findings.add(Finding("ASSESSED_AT_NOT_UTC", "/observed_at"))
    if prior_time is not None and current_time is not None and current_time <= prior_time:
        findings.add(Finding("CURRENT_SNAPSHOT_NOT_NEWER", "/snapshot_pair/current/observed_at"))
    if assessed_time is not None and current_time is not None and assessed_time < current_time:
        findings.add(Finding("ASSESSMENT_PRECEDES_CURRENT_SNAPSHOT", "/observed_at"))
    if prior.get("snapshot_ref") == current.get("snapshot_ref"):
        findings.add(Finding("SNAPSHOT_REFERENCE_REUSED", "/snapshot_pair"))
    if prior.get("taxonomy_version_ref") != current.get("taxonomy_version_ref"):
        findings.add(Finding("TAXONOMY_VERSION_DRIFT", "/snapshot_pair/current/taxonomy_version_ref"))
    return findings


def _delta_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    delta = candidate["set_delta"]
    pair = candidate["snapshot_pair"]
    assert isinstance(delta, Mapping) and isinstance(pair, Mapping)
    prior = pair["prior"]
    current = pair["current"]
    assert isinstance(prior, Mapping) and isinstance(current, Mapping)

    added = delta["added_taxon_refs"]
    removed = delta["removed_taxon_refs"]
    edges = delta["rename_edges"]
    assert isinstance(added, list) and isinstance(removed, list) and isinstance(edges, list)
    if not _canonical_strings(added):
        findings.add(Finding("ADDED_TAXA_NOT_CANONICAL", "/set_delta/added_taxon_refs"))
    if not _canonical_strings(removed):
        findings.add(Finding("REMOVED_TAXA_NOT_CANONICAL", "/set_delta/removed_taxon_refs"))
    if set(added) & set(removed):
        findings.add(Finding("DELTA_SET_OVERLAP", "/set_delta"))

    edge_keys = [
        (str(edge["source_taxon_ref"]), str(edge["target_taxon_ref"]), str(edge["relationship"]))
        for edge in edges
        if isinstance(edge, Mapping)
    ]
    if edge_keys != sorted(set(edge_keys)):
        findings.add(Finding("RENAME_EDGES_NOT_CANONICAL", "/set_delta/rename_edges"))
    sources: list[str] = []
    targets: list[str] = []
    for index, edge in enumerate(edges):
        assert isinstance(edge, Mapping)
        source = str(edge["source_taxon_ref"])
        target = str(edge["target_taxon_ref"])
        sources.append(source)
        targets.append(target)
        if source == target:
            findings.add(Finding("RENAME_SELF_REFERENCE", f"/set_delta/rename_edges/{index}"))
        if source not in removed:
            findings.add(Finding("RENAME_SOURCE_NOT_REMOVED", f"/set_delta/rename_edges/{index}/source_taxon_ref"))
        if target not in added:
            findings.add(Finding("RENAME_TARGET_NOT_ADDED", f"/set_delta/rename_edges/{index}/target_taxon_ref"))
    if len(sources) != len(set(sources)):
        findings.add(Finding("RENAME_SOURCE_REUSED", "/set_delta/rename_edges"))
    if len(targets) != len(set(targets)):
        findings.add(Finding("RENAME_TARGET_REUSED", "/set_delta/rename_edges"))

    has_delta = bool(added or removed or edges)
    materiality = candidate.get("materiality")
    if materiality == "CHANGE_CANDIDATE" and not has_delta:
        findings.add(Finding("CHANGE_CANDIDATE_WITHOUT_DELTA", "/materiality"))
    elif materiality == "NO_MATERIAL_CHANGE" and has_delta:
        findings.add(Finding("NO_MATERIAL_CHANGE_WITH_DELTA", "/materiality"))
    elif materiality == "UNRESOLVED":
        findings.add(Finding("MATERIALITY_UNRESOLVED", "/materiality"))
    if has_delta and prior.get("content_digest") == current.get("content_digest"):
        findings.add(Finding("DELTA_WITH_IDENTICAL_SNAPSHOT_DIGEST", "/snapshot_pair"))
    return findings


def _sensitivity_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    sensitivity = candidate["sensitivity"]
    assert isinstance(sensitivity, Mapping)
    if sensitivity.get("occurrence_join_performed") is True:
        findings.add(Finding("OCCURRENCE_JOIN_DENIED", "/sensitivity/occurrence_join_performed"))
    if sensitivity.get("exact_locations_present") is True:
        findings.add(Finding("EXACT_LOCATION_DENIED", "/sensitivity/exact_locations_present"))

    intersection = sensitivity.get("conservation_intersection_state")
    review_required = sensitivity.get("sensitivity_review_required")
    detail_mode = sensitivity.get("public_detail_mode")
    policy_ref = sensitivity.get("policy_decision_ref")
    if intersection == "UNKNOWN":
        findings.add(Finding("SENSITIVITY_INTERSECTION_UNKNOWN", "/sensitivity/conservation_intersection_state"))
        if detail_mode != "WITHHELD":
            findings.add(Finding("UNKNOWN_SENSITIVITY_NOT_WITHHELD", "/sensitivity/public_detail_mode"))
    elif intersection == "PRESENT":
        if detail_mode != "WITHHELD":
            findings.add(Finding("SENSITIVE_DETAIL_NOT_WITHHELD", "/sensitivity/public_detail_mode"))
        if policy_ref is None:
            findings.add(Finding("SENSITIVITY_POLICY_REFERENCE_REQUIRED", "/sensitivity/policy_decision_ref"))
    if intersection in {"PRESENT", "UNKNOWN"} and review_required is not True:
        findings.add(Finding("SENSITIVITY_REVIEW_REQUIRED", "/sensitivity/sensitivity_review_required"))
    if candidate.get("materiality") == "CHANGE_CANDIDATE" and review_required is not True:
        findings.add(Finding("CHANGE_REVIEW_REQUIRED", "/sensitivity/sensitivity_review_required"))
    return findings


def _attestation_output_review_findings(candidate: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    attestations = candidate["attestations"]
    output = candidate["output"]
    review = candidate["review"]
    assert isinstance(attestations, Mapping) and isinstance(output, Mapping) and isinstance(review, Mapping)

    snapshot_attestations = attestations.get("source_snapshot_attestation_refs")
    if not _canonical_strings(snapshot_attestations):
        findings.add(Finding("SNAPSHOT_ATTESTATIONS_NOT_CANONICAL", "/attestations/source_snapshot_attestation_refs"))
    if not isinstance(snapshot_attestations, list) or len(snapshot_attestations) < 2:
        findings.add(Finding("SOURCE_SNAPSHOT_ATTESTATIONS_INCOMPLETE", "/attestations/source_snapshot_attestation_refs"))
    if attestations.get("taxonomy_version_attestation_ref") is None:
        findings.add(Finding("TAXONOMY_VERSION_ATTESTATION_REQUIRED", "/attestations/taxonomy_version_attestation_ref"))

    materiality = candidate.get("materiality")
    if materiality == "CHANGE_CANDIDATE":
        if output.get("posture") != "WORK_CANDIDATE" or output.get("candidate_ref") is None:
            findings.add(Finding("CHANGE_OUTPUT_POSTURE_INCOHERENT", "/output"))
    else:
        if output.get("posture") != "NO_WORK_RECORD" or output.get("candidate_ref") is not None:
            findings.add(Finding("NONCHANGE_OUTPUT_POSTURE_INCOHERENT", "/output"))

    review_refs = review.get("record_refs")
    if not _canonical_strings(review_refs):
        findings.add(Finding("REVIEW_RECORDS_NOT_CANONICAL", "/review/record_refs"))
    state = review.get("state")
    if state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif not review_refs:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    findings.update(_snapshot_findings(candidate))
    findings.update(_delta_findings(candidate))
    findings.update(_sensitivity_findings(candidate))
    findings.update(_attestation_output_review_findings(candidate))

    for path, text in _walk_strings(candidate):
        lowered = text.casefold()
        if any(marker in lowered for marker in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))
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
    if isinstance(base, list) and isinstance(patch, Mapping) and all(
        isinstance(key, str) and key.isdigit() for key in patch
    ):
        target = copy.deepcopy(base)
        for key in sorted(patch, key=int):
            index = int(key)
            if index >= len(target):
                raise ValueError("fixture list patch index out of range")
            target[index] = _merge_patch(target[index], patch[key])
        return target
    if not isinstance(patch, Mapping):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, Mapping) else {}
    assert isinstance(target, dict)
    for key, value in patch.items():
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    if not isinstance(candidate, dict):
        raise ValueError("materialized fixture must be an object")
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    candidate["assessment_id"] = compute_assessment_id(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif entry.get("tamper") == "assessment_id":
        candidate["assessment_id"] = IDENTITY_PREFIX + "f" * 24
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
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
    parser = argparse.ArgumentParser(
        description="Validate fixture-only PLANTS taxa-drift assessments."
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
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
