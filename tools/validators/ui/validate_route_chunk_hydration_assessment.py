"""Validate fixture-only route chunk hydration assessment candidates.

The validator checks closed shape, deterministic content identity, canonical
references, finite prerequisite states, and a derived hydration disposition. It
does not import a module, bind a route, resolve a reference, evaluate policy,
activate a layer, mutate a cache, or grant release or publication authority.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/ui/route_chunk_hydration_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/ui/route_chunk_hydration_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:route-chunk-hydration:"
ABSTAIN_CODES = {
    "VIEW_REGISTRY_HELD",
    "VIEW_REGISTRY_UNKNOWN",
    "RENDER_HINTS_HELD",
    "RENDER_HINTS_UNKNOWN",
    "EVIDENCE_PARTIAL",
    "EVIDENCE_MISSING",
    "EVIDENCE_UNKNOWN",
    "ACCESS_HELD",
    "ACCESS_UNKNOWN",
    "RELEASE_HELD",
    "RELEASE_UNKNOWN",
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


def _derive(prerequisites: Mapping[str, object]) -> tuple[str, list[str]]:
    deny_map = {
        ("view_registry_state", "DENY"): "VIEW_REGISTRY_DENIED",
        ("render_hints_state", "DENY"): "RENDER_HINTS_DENIED",
        ("access_state", "DENY"): "ACCESS_DENIED",
        ("release_state", "DENY"): "RELEASE_DENIED",
    }
    deny_codes = sorted(
        code for (field, state), code in deny_map.items() if prerequisites.get(field) == state
    )
    if deny_codes:
        return "REJECT", deny_codes

    hold_map = {
        ("view_registry_state", "HOLD"): "VIEW_REGISTRY_HELD",
        ("view_registry_state", "UNKNOWN"): "VIEW_REGISTRY_UNKNOWN",
        ("render_hints_state", "HOLD"): "RENDER_HINTS_HELD",
        ("render_hints_state", "UNKNOWN"): "RENDER_HINTS_UNKNOWN",
        ("evidence_state", "PARTIAL"): "EVIDENCE_PARTIAL",
        ("evidence_state", "MISSING"): "EVIDENCE_MISSING",
        ("evidence_state", "UNKNOWN"): "EVIDENCE_UNKNOWN",
        ("access_state", "HOLD"): "ACCESS_HELD",
        ("access_state", "UNKNOWN"): "ACCESS_UNKNOWN",
        ("release_state", "HOLD"): "RELEASE_HELD",
        ("release_state", "UNKNOWN"): "RELEASE_UNKNOWN",
    }
    hold_codes = sorted(
        code for (field, state), code in hold_map.items() if prerequisites.get(field) == state
    )
    return ("HOLD", hold_codes) if hold_codes else ("HYDRATE_READY", [])


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash = compute_profile_hash(candidate)
    if candidate.get("profile_spec_hash") != expected_hash:
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    chunk = candidate["chunk"]
    prerequisites = candidate["prerequisites"]
    derived = candidate["derived_state"]
    assert isinstance(chunk, Mapping)
    assert isinstance(prerequisites, Mapping)
    assert isinstance(derived, Mapping)

    if chunk.get("chunk_id") != f"kfm://ui-chunk/{chunk.get('chunk_name')}":
        findings.add(Finding("CHUNK_ID_NAME_MISMATCH", "/chunk/chunk_id"))
    for field, value in (
        ("/chunk/dependency_refs", chunk.get("dependency_refs")),
        ("/prerequisites/validation_refs", prerequisites.get("validation_refs")),
        ("/derived_state/reason_codes", derived.get("reason_codes")),
        ("/limitations", candidate.get("limitations")),
    ):
        if not _canonical_strings(value):
            findings.add(Finding("ARRAY_NOT_CANONICAL", field))

    role_refs = [
        candidate["route"]["view_registry_profile_ref"],
        prerequisites["render_hint_ref"],
        prerequisites["evidence_drawer_profile_ref"],
        prerequisites["access_policy_ref"],
        prerequisites["release_manifest_ref"],
    ]
    if len(set(role_refs)) != len(role_refs):
        findings.add(Finding("REFERENCE_ROLE_COLLAPSE", "/prerequisites"))

    for path, text in _walk_strings(candidate):
        lowered = text.casefold()
        if any(marker in lowered for marker in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))

    disposition, reason_codes = _derive(prerequisites)
    if derived.get("disposition") != disposition or derived.get("reason_codes") != reason_codes:
        findings.add(Finding("DERIVED_STATE_INCOHERENT", "/derived_state"))
    else:
        for code in reason_codes:
            findings.add(Finding(code, "/derived_state/reason_codes"))
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
        target[key] = None if value is None else _merge_patch(target.get(key), value)
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
        description="Validate fixture-only route chunk hydration assessments."
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
