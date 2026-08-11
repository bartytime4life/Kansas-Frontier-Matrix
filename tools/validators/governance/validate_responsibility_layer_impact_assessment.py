"""Validate fixture-only KFM responsibility-layer impact assessments.

The validator checks declared artifact ownership, responsibility-layer coverage,
cross-layer seams, validation references, rollback posture, and review state. It
does not place files, assign owners, decide policy, mutate data, execute runtime
work, or authorize review, release, deployment, or publication.
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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/responsibility_layer_impact_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/responsibility_layer_impact_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:responsibility-layer-impact:"
ABSTAIN_CODES = {"REVIEW_PENDING", "REVIEW_UNKNOWN", "SEAM_UNRESOLVED"}
PUBLIC_SURFACE_LAYERS = {"AI", "API", "UI"}
PUBLIC_CLOSURE_LAYERS = {"EVIDENCE", "POLICY", "RELEASE"}
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


def _artifact_findings(artifacts: list[object]) -> tuple[set[Finding], set[str], set[str]]:
    findings: set[Finding] = set()
    typed = [item for item in artifacts if isinstance(item, Mapping)]
    paths = [str(item["path"]) for item in typed]
    if paths != sorted(set(paths)):
        findings.add(Finding("ARTIFACTS_NOT_CANONICAL", "/artifacts"))

    primary_layers: set[str] = set()
    all_layers: set[str] = set()
    for index, artifact in enumerate(typed):
        path = str(artifact["path"])
        owning_root = str(artifact["owning_root"])
        primary = str(artifact["primary_layer"])
        related = artifact["related_layers"]
        assert isinstance(related, list)
        if not path.startswith(owning_root):
            findings.add(Finding("OWNING_ROOT_PATH_MISMATCH", f"/artifacts/{index}/owning_root"))
        if not _canonical_strings(related):
            findings.add(Finding("RELATED_LAYERS_NOT_CANONICAL", f"/artifacts/{index}/related_layers"))
        if primary in related:
            findings.add(Finding("PRIMARY_LAYER_REPEATED_AS_RELATED", f"/artifacts/{index}/related_layers"))
        primary_layers.add(primary)
        all_layers.add(primary)
        all_layers.update(str(item) for item in related)
    return findings, primary_layers, all_layers


def _impact_findings(
    impacts: list[object], primary_layers: set[str], all_layers: set[str]
) -> tuple[set[Finding], set[str]]:
    findings: set[Finding] = set()
    typed = [item for item in impacts if isinstance(item, Mapping)]
    layers = [str(item["layer"]) for item in typed]
    if layers != sorted(set(layers)):
        findings.add(Finding("LAYER_IMPACTS_NOT_CANONICAL", "/layer_impacts"))
    declared_layers = set(layers)
    if declared_layers != all_layers:
        findings.add(Finding("LAYER_IMPACT_COVERAGE_MISMATCH", "/layer_impacts"))

    for index, impact in enumerate(typed):
        layer = str(impact["layer"])
        expected_kind = "DIRECT" if layer in primary_layers else "RELATED"
        if impact.get("impact_kind") != expected_kind:
            findings.add(Finding("IMPACT_KIND_INCOHERENT", f"/layer_impacts/{index}/impact_kind"))
        if not _canonical_strings(impact.get("validation_refs")):
            findings.add(Finding("VALIDATION_REFS_NOT_CANONICAL", f"/layer_impacts/{index}/validation_refs"))
        if layer == "POLICY" and impact.get("decision_ref") is None:
            findings.add(Finding("POLICY_DECISION_REFERENCE_REQUIRED", f"/layer_impacts/{index}/decision_ref"))
        if layer == "RELEASE" and impact.get("rollback_ref") is None:
            findings.add(Finding("RELEASE_ROLLBACK_REFERENCE_REQUIRED", f"/layer_impacts/{index}/rollback_ref"))

    if declared_layers & PUBLIC_SURFACE_LAYERS and not PUBLIC_CLOSURE_LAYERS <= declared_layers:
        findings.add(Finding("PUBLIC_SURFACE_CLOSURE_INCOMPLETE", "/layer_impacts"))
    return findings, declared_layers


def _seam_findings(seams: list[object], declared_layers: set[str]) -> set[Finding]:
    findings: set[Finding] = set()
    typed = [item for item in seams if isinstance(item, Mapping)]
    keys = [
        (str(item["from_layer"]), str(item["to_layer"]), str(item["contract_ref"]), str(item["status"]))
        for item in typed
    ]
    if keys != sorted(set(keys)):
        findings.add(Finding("SEAMS_NOT_CANONICAL", "/cross_layer_seams"))

    graph = {layer: set() for layer in declared_layers}
    for index, seam in enumerate(typed):
        left = str(seam["from_layer"])
        right = str(seam["to_layer"])
        if left == right:
            findings.add(Finding("SEAM_SELF_REFERENCE", f"/cross_layer_seams/{index}"))
        if left not in declared_layers or right not in declared_layers:
            findings.add(Finding("SEAM_LAYER_NOT_DECLARED", f"/cross_layer_seams/{index}"))
        else:
            graph[left].add(right)
            graph[right].add(left)
        if seam.get("status") == "UNRESOLVED":
            findings.add(Finding("SEAM_UNRESOLVED", f"/cross_layer_seams/{index}/status"))

    if len(declared_layers) > 1:
        start = min(declared_layers)
        visited: set[str] = set()
        pending = [start]
        while pending:
            layer = pending.pop()
            if layer in visited:
                continue
            visited.add(layer)
            pending.extend(sorted(graph[layer] - visited))
        if visited != declared_layers:
            findings.add(Finding("LAYER_GRAPH_DISCONNECTED", "/cross_layer_seams"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    artifacts = candidate["artifacts"]
    impacts = candidate["layer_impacts"]
    seams = candidate["cross_layer_seams"]
    review = candidate["review"]
    assert isinstance(artifacts, list) and isinstance(impacts, list) and isinstance(seams, list)
    assert isinstance(review, Mapping)

    artifact_findings, primary_layers, all_layers = _artifact_findings(artifacts)
    findings.update(artifact_findings)
    impact_findings, declared_layers = _impact_findings(impacts, primary_layers, all_layers)
    findings.update(impact_findings)
    findings.update(_seam_findings(seams, declared_layers))

    review_state = review.get("state")
    review_refs = review.get("record_refs")
    if not _canonical_strings(review_refs):
        findings.add(Finding("REVIEW_RECORDS_NOT_CANONICAL", "/review/record_refs"))
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/review/state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/review/state"))
    elif not review_refs:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/review/record_refs"))

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
        description="Validate fixture-only responsibility-layer impact assessments."
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
