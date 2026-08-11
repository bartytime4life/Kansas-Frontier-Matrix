"""Validate fixture-only correlation claim-boundary assessments.

The validator checks closed shape, deterministic identity, pinned composition
references, correlation-method disclosure, requested wording role, causal-design
posture, caveats, and canonical references. It does not calculate correlation,
resolve evidence, determine causal sufficiency, decide policy or review, promote,
release, publish, or authorize public use.
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

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/evidence/correlation_claim_boundary_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/evidence/correlation_claim_boundary_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
ABSTAIN_CODES = {
    "ANALYTIC_DISCLOSURE_UNRESOLVED",
    "CAUSAL_DESIGN_REVIEW_REQUIRED",
    "CAUSAL_DESIGN_UNRESOLVED",
    "CLAIM_WORDING_AMBIGUOUS",
    "CONDITION_RELATION_UNRESOLVED",
    "DISCLOSURE_INCOMPLETE",
    "DISCLOSURE_UNKNOWN",
    "METHOD_REGISTRY_UNRESOLVED",
    "STRONGER_CLAIM_REVIEW_REQUIRED",
    "STRONGER_CLAIM_SUPPORT_NOT_PROVIDED",
    "UNCERTAINTY_UNRESOLVED",
}
EXPECTED_WORDING = {
    "ASSOCIATION": "ASSOCIATIONAL",
    "CONTRIBUTION": "CONTRIBUTION_OR_EXPOSURE",
    "EXPOSURE": "CONTRIBUTION_OR_EXPOSURE",
    "CAUSE": "CAUSAL",
}
STRONGER_DESIGNS = {"QUASI_EXPERIMENTAL", "RANDOMIZED_EXPERIMENT", "MECHANISTIC", "OTHER"}


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
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
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
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def _load_schema() -> dict[str, object]:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def _schema_findings(candidate: object) -> list[Finding]:
    validator = Draft202012Validator(_load_schema(), format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(candidate), key=lambda error: (tuple(str(part) for part in error.absolute_path), str(error.validator)))
    return [Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path)) for error in errors[:100]]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(item, str) for item in value) and value == sorted(set(value))


def _causal_design_findings(design: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    resolution = design["resolution"]
    has_identity = design["ref"] is not None and design["digest"] is not None
    missing_identity = design["ref"] is None and design["digest"] is None
    if resolution == "NOT_PROVIDED":
        if not missing_identity or design["design_class"] != "NOT_PROVIDED":
            findings.add(Finding("CAUSAL_DESIGN_DECLARATION_MISMATCH", "/claim/causal_design"))
    elif resolution == "UNRESOLVED":
        if not has_identity or design["design_class"] != "UNKNOWN":
            findings.add(Finding("CAUSAL_DESIGN_DECLARATION_MISMATCH", "/claim/causal_design"))
    elif not has_identity or design["design_class"] in {"NOT_PROVIDED", "UNKNOWN"}:
        findings.add(Finding("CAUSAL_DESIGN_DECLARATION_MISMATCH", "/claim/causal_design"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED", "/observed_at"))

    statistic = candidate["statistic"]
    claim = candidate["claim"]
    disclosure = candidate["disclosure"]
    assert isinstance(statistic, Mapping) and isinstance(claim, Mapping) and isinstance(disclosure, Mapping)

    reference_checks = (
        (statistic["analytic_output_disclosure"], "ANALYTIC_DISCLOSURE_UNRESOLVED", "/statistic/analytic_output_disclosure/resolution"),
        (statistic["condition_relation"], "CONDITION_RELATION_UNRESOLVED", "/statistic/condition_relation/resolution"),
        (statistic["method"], "METHOD_REGISTRY_UNRESOLVED", "/statistic/method/resolution"),
        (statistic["uncertainty"], "UNCERTAINTY_UNRESOLVED", "/statistic/uncertainty/resolution"),
    )
    for binding, code, field in reference_checks:
        assert isinstance(binding, Mapping)
        if binding["resolution"] == "UNRESOLVED":
            findings.add(Finding(code, field))

    design = claim["causal_design"]
    assert isinstance(design, Mapping)
    findings.update(_causal_design_findings(design))

    if disclosure["state"] == "INCOMPLETE":
        findings.add(Finding("DISCLOSURE_INCOMPLETE", "/disclosure/state"))
    elif disclosure["state"] == "UNKNOWN":
        findings.add(Finding("DISCLOSURE_UNKNOWN", "/disclosure/state"))

    requested = claim["requested_role"]
    wording = claim["wording_class"]
    if wording == "AMBIGUOUS":
        findings.add(Finding("CLAIM_WORDING_AMBIGUOUS", "/claim/wording_class"))
    elif wording != EXPECTED_WORDING[requested]:
        code = "CAUSAL_WORDING_UNSUPPORTED" if wording == "CAUSAL" else "WORDING_CLASS_MISMATCH"
        findings.add(Finding(code, "/claim/wording_class"))

    expected_permitted = "ASSOCIATION_ONLY" if requested == "ASSOCIATION" else "CAUSAL_REVIEW_REQUIRED"
    if disclosure["permitted_role"] != expected_permitted:
        findings.add(Finding("PERMITTED_ROLE_MISMATCH", "/disclosure/permitted_role"))

    if requested in {"CONTRIBUTION", "EXPOSURE"}:
        if design["resolution"] == "NOT_PROVIDED":
            findings.add(Finding("STRONGER_CLAIM_SUPPORT_NOT_PROVIDED", "/claim/causal_design"))
        elif design["resolution"] == "UNRESOLVED":
            findings.add(Finding("CAUSAL_DESIGN_UNRESOLVED", "/claim/causal_design/resolution"))
        else:
            findings.add(Finding("STRONGER_CLAIM_REVIEW_REQUIRED", "/claim/causal_design"))
    elif requested == "CAUSE":
        if design["resolution"] == "NOT_PROVIDED":
            findings.add(Finding("CAUSAL_WORDING_UNSUPPORTED", "/claim/causal_design"))
        elif design["resolution"] == "UNRESOLVED":
            findings.add(Finding("CAUSAL_DESIGN_UNRESOLVED", "/claim/causal_design/resolution"))
        elif design["design_class"] in STRONGER_DESIGNS:
            findings.add(Finding("CAUSAL_DESIGN_REVIEW_REQUIRED", "/claim/causal_design"))
        else:
            findings.add(Finding("CAUSAL_WORDING_UNSUPPORTED", "/claim/causal_design/design_class"))

    caveats = disclosure["caveat_codes"]
    required_caveats = {"CONFOUNDING_NOT_EXCLUDED", "CORRELATION_NOT_CAUSATION", "SCOPE_BOUND"}
    if requested != "ASSOCIATION":
        required_caveats.add("CAUSAL_DESIGN_REVIEW_REQUIRED")
    if claim["intended_use"] == "PUBLIC_EXPLANATION":
        required_caveats.add("PUBLIC_EXPLANATION_REQUIRED")
    if not _canonical_strings(caveats):
        findings.add(Finding("CAVEAT_CODES_NOT_CANONICAL", "/disclosure/caveat_codes"))
    if not required_caveats.issubset(set(caveats)):
        findings.add(Finding("REQUIRED_CAVEAT_MISSING", "/disclosure/caveat_codes"))

    if claim["intended_use"] in {"PUBLIC_EXPLANATION", "RELEASE_REVIEW"} and not disclosure["review_record_refs"]:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/disclosure/review_record_refs"))
    if not _canonical_strings(disclosure["evidence_refs"]):
        findings.add(Finding("EVIDENCE_REFS_NOT_CANONICAL", "/disclosure/evidence_refs"))
    if not _canonical_strings(disclosure["review_record_refs"]):
        findings.add(Finding("REVIEW_REFS_NOT_CANONICAL", "/disclosure/review_record_refs"))
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


def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    assert isinstance(candidate, dict)
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{"name": "fixture_manifest", "ok": False, "observed": {"outcome": "ERROR", "codes": sorted({item.code for item in load_findings})}}]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({"name": entry["name"], "ok": observed == expected, "expected": expected, "observed": observed})
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate fixture-only correlation claim-boundary assessments.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = ValidationResult("ERROR", tuple(sorted(findings))) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
