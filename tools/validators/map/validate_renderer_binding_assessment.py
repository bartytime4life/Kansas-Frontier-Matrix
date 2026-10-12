"""Validate fixture-only KFM renderer-to-layer binding assessments.

The validator checks declared coherence only. It does not resolve references,
read stores, inspect artifacts, execute or register a renderer, evaluate policy,
or authorize review, release, deployment, publication, or public use.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/map/renderer_binding_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/map/renderer_binding_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:renderer-binding:"
ABSTAIN_CODES = {
    "BINDING_STATE_UNKNOWN",
    "DELIVERY_INPUT_UNKNOWN",
    "EVIDENCE_RESOLUTION_UNRESOLVED",
    "EVIDENCE_SUPPORT_UNRESOLVED",
    "INTERACTION_CONTEXT_UNKNOWN",
    "POLICY_SUPPORT_UNRESOLVED",
    "RELEASE_STATE_UNKNOWN",
    "RENDERER_FAMILY_UNKNOWN",
    "RENDERER_POLICY_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_SUPPORT_UNRESOLVED",
    "REVIEW_UNKNOWN",
    "RIGHTS_STATE_UNKNOWN",
    "RUNTIME_SURFACE_UNKNOWN",
    "SENSITIVITY_STATE_UNKNOWN",
}
INTERNAL_INPUT_CLASSES = {"INTERNAL_STORE", "QUARANTINE", "RAW", "WORK"}
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
    if not _is_utc(candidate.get("evaluated_at")):
        findings.add(Finding("EVALUATED_AT_NOT_UTC", "/evaluated_at"))

    renderer = candidate["renderer"]
    layer = candidate["layer"]
    delivery = candidate["delivery"]
    trust = candidate["trust"]
    interaction = candidate["interaction"]
    review = candidate["review"]
    assert all(
        isinstance(item, Mapping)
        for item in (renderer, layer, delivery, trust, interaction, review)
    )

    for field, value in (
        ("/trust/evidence_bundle_refs", trust["evidence_bundle_refs"]),
        ("/trust/policy_decision_refs", trust["policy_decision_refs"]),
        ("/trust/review_record_refs", trust["review_record_refs"]),
        ("/trust/correction_refs", trust["correction_refs"]),
        ("/review/record_refs", review["record_refs"]),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("REFERENCES_NOT_CANONICAL", field))

    family = renderer["renderer_family"]
    surface = renderer["runtime_surface"]
    binding_state = renderer["binding_state"]
    if family == "UNKNOWN":
        findings.add(Finding("RENDERER_FAMILY_UNKNOWN", "/renderer/renderer_family"))
    if surface == "UNKNOWN":
        findings.add(Finding("RUNTIME_SURFACE_UNKNOWN", "/renderer/runtime_surface"))
    if binding_state == "UNKNOWN":
        findings.add(Finding("BINDING_STATE_UNKNOWN", "/renderer/binding_state"))
    elif binding_state == "ACTIVE":
        findings.add(Finding("ACTIVE_BINDING_DENIED", "/renderer/binding_state"))
    if surface == "BROWSER" and family == "PEER_BROWSER_RENDERER":
        findings.add(Finding("RENDERER_POLICY_UNRESOLVED", "/renderer/renderer_family"))
    elif surface == "BROWSER" and family == "HEADLESS_RENDERER":
        findings.add(
            Finding("BROWSER_RENDERER_FAMILY_INCOHERENT", "/renderer/renderer_family")
        )

    layer_refs = [
        layer["layer_descriptor_ref"],
        layer["layer_manifest_ref"],
        layer["artifact_manifest_ref"],
    ]
    if layer["style_manifest_ref"] is not None:
        layer_refs.append(layer["style_manifest_ref"])
    if len(layer_refs) != len(set(layer_refs)):
        findings.add(Finding("LAYER_REFERENCE_ROLE_COLLAPSE", "/layer"))

    input_class = delivery["input_class"]
    if input_class == "UNKNOWN":
        findings.add(Finding("DELIVERY_INPUT_UNKNOWN", "/delivery/input_class"))
    elif input_class in INTERNAL_INPUT_CLASSES:
        findings.add(Finding("INTERNAL_INPUT_CLASS_DENIED", "/delivery/input_class"))
    if delivery["direct_store_access"]:
        findings.add(Finding("DIRECT_STORE_ACCESS_DENIED", "/delivery/direct_store_access"))
    if delivery["query_text_present"]:
        findings.add(Finding("QUERY_TEXT_DENIED", "/delivery/query_text_present"))

    release_state = trust["release_state"]
    evidence_refs = trust["evidence_bundle_refs"]
    policy_refs = trust["policy_decision_refs"]
    trust_review_refs = trust["review_record_refs"]
    if release_state == "UNKNOWN":
        findings.add(Finding("RELEASE_STATE_UNKNOWN", "/trust/release_state"))
    elif release_state == "WITHDRAWN":
        findings.add(Finding("WITHDRAWN_RELEASE_DENIED", "/trust/release_state"))

    if release_state == "PUBLISHED":
        if not evidence_refs or not policy_refs or not trust_review_refs:
            findings.add(Finding("PUBLISHED_TRUST_CLOSURE_REQUIRED", "/trust"))
        if trust["promotion_decision_ref"] is None:
            findings.add(Finding("PUBLISHED_PROMOTION_REQUIRED", "/trust/promotion_decision_ref"))
        if trust["release_manifest_ref"] is None:
            findings.add(Finding("PUBLISHED_RELEASE_REQUIRED", "/trust/release_manifest_ref"))
        if trust["rollback_ref"] is None:
            findings.add(Finding("PUBLISHED_ROLLBACK_REQUIRED", "/trust/rollback_ref"))
    else:
        if not evidence_refs:
            findings.add(Finding("EVIDENCE_SUPPORT_UNRESOLVED", "/trust/evidence_bundle_refs"))
        if not policy_refs:
            findings.add(Finding("POLICY_SUPPORT_UNRESOLVED", "/trust/policy_decision_refs"))
        if not trust_review_refs:
            findings.add(Finding("REVIEW_SUPPORT_UNRESOLVED", "/trust/review_record_refs"))

    if (
        input_class == "RELEASED_CARRIER" or release_state == "PUBLISHED"
    ) and not delivery["immutable_locator"]:
        findings.add(Finding("IMMUTABLE_LOCATOR_REQUIRED", "/delivery/immutable_locator"))

    sensitivity = trust["sensitivity_state"]
    rights = trust["rights_state"]
    if sensitivity == "UNKNOWN":
        findings.add(Finding("SENSITIVITY_STATE_UNKNOWN", "/trust/sensitivity_state"))
    elif sensitivity == "RESTRICTED":
        findings.add(Finding("RESTRICTED_SENSITIVITY_DENIED", "/trust/sensitivity_state"))
    if rights == "UNKNOWN":
        findings.add(Finding("RIGHTS_STATE_UNKNOWN", "/trust/rights_state"))
    elif rights == "RESTRICTED":
        findings.add(Finding("RESTRICTED_RIGHTS_DENIED", "/trust/rights_state"))

    context_mode = interaction["context_mode"]
    if context_mode == "UNKNOWN":
        findings.add(Finding("INTERACTION_CONTEXT_UNKNOWN", "/interaction/context_mode"))
    elif context_mode == "FEATURE_PROPERTIES_ONLY":
        findings.add(Finding("FEATURE_PROPERTIES_CONTEXT_DENIED", "/interaction/context_mode"))
    if interaction["evidence_resolution_ref"] is None:
        findings.add(Finding("EVIDENCE_RESOLUTION_UNRESOLVED", "/interaction/evidence_resolution_ref"))
    if interaction["feature_properties_as_authority"]:
        findings.add(
            Finding("FEATURE_PROPERTIES_AUTHORITY_DENIED", "/interaction/feature_properties_as_authority")
        )
    if interaction["client_side_policy_decision"]:
        findings.add(
            Finding("CLIENT_POLICY_AUTHORITY_DENIED", "/interaction/client_side_policy_decision")
        )
    if interaction["hidden_feature_inference"]:
        findings.add(Finding("HIDDEN_FEATURE_INFERENCE_DENIED", "/interaction/hidden_feature_inference"))
    if interaction["direct_internal_store_lookup"]:
        findings.add(
            Finding("DIRECT_INTERNAL_LOOKUP_DENIED", "/interaction/direct_internal_store_lookup")
        )

    review_state = review["state"]
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif not review["record_refs"]:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))

    for path, value in _walk_strings(candidate):
        lowered = value.casefold()
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
        outcome = "REVIEW_REQUIRED"
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
        description="Validate fixture-only renderer binding assessments."
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
    return 0 if result.outcome == "REVIEW_REQUIRED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
