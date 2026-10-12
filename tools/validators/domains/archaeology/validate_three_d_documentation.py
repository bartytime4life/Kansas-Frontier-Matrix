#!/usr/bin/env python3
"""Validate fixture-only ThreeDDocumentation paradata declarations.

The validator is local and non-authoritative. It does not read 3D assets,
resolve references, execute processing, decide interpretation, evaluate policy,
approve review, release, publish, or authorize public use.
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

ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = ROOT / "schemas/contracts/v1/domains/archaeology/three_d_documentation.schema.json"
FIXTURE_PATH = ROOT / "fixtures/contracts/v1/domains/archaeology/three_d_documentation/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:archaeology:three-d-documentation:"


class DuplicateKeyError(ValueError):
    """Raised when JSON repeats an object key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-finite number token."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return [finding.code for finding in self.findings]


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
            return None, [Finding("INPUT_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT")]
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


def compute_identity(candidate: Mapping[str, object]) -> tuple[str, str]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("spec_hash", None)
    subject.pop("documentation_id", None)
    spec_hash = canonical_hash(subject)
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = list(
        Draft202012Validator(
            schema,
            format_checker=FormatChecker(),
        ).iter_errors(candidate)
    )
    return [] if not errors else [Finding("SCHEMA_INVALID")]


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


def _integrity_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    expected_hash, expected_id = compute_identity(candidate)
    if candidate.get("spec_hash") != expected_hash:
        findings.add(Finding("SPEC_HASH_MISMATCH"))
    if candidate.get("documentation_id") != expected_id:
        findings.add(Finding("DOCUMENTATION_ID_MISMATCH"))
    if not _is_utc(candidate.get("recorded_at")):
        findings.add(Finding("UTC_TIMESTAMP_REQUIRED"))

    capture = candidate["capture"]
    interpretation = candidate["interpretation"]
    assets = candidate["assets"]
    assert isinstance(capture, Mapping)
    assert isinstance(interpretation, Mapping)
    assert isinstance(assets, Mapping)
    arrays = [
        candidate["subject_refs"],
        capture["methods"],
        capture["device_refs"],
        interpretation["interpretive_step_refs"],
        assets["source_asset_refs"],
        assets["derived_asset_refs"],
        assets["public_safe_asset_refs"],
    ]
    for step in candidate["processing_steps"]:
        assert isinstance(step, Mapping)
        arrays.extend([step["input_asset_refs"], step["output_asset_refs"]])
    if not all(_canonical_strings(value) for value in arrays):
        findings.add(Finding("REFERENCE_ARRAY_NOT_CANONICAL"))
    return sorted(findings)


def _abstain_findings(candidate: Mapping[str, object]) -> list[Finding]:
    capture = candidate["capture"]
    spatial = candidate["spatial_reference"]
    interpretation = candidate["interpretation"]
    governance = candidate["governance"]
    assert isinstance(capture, Mapping)
    assert isinstance(spatial, Mapping)
    assert isinstance(interpretation, Mapping)
    assert isinstance(governance, Mapping)
    findings: set[Finding] = set()
    if capture["state"] in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"CAPTURE_{capture['state']}"))
    if governance["state"] in {"INCOMPLETE", "UNKNOWN"}:
        findings.add(Finding(f"GOVERNANCE_{governance['state']}"))
    if spatial["scale_state"] == "UNRESOLVED" or spatial["georeference_state"] == "UNRESOLVED":
        findings.add(Finding("SPATIAL_REFERENCE_UNRESOLVED"))
    if interpretation["knowledge_character"] == "UNKNOWN" or interpretation["representation_kind"] == "UNKNOWN":
        findings.add(Finding("INTERPRETATION_UNKNOWN"))
    return sorted(findings)


def _complete_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    capture = candidate["capture"]
    steps = candidate["processing_steps"]
    spatial = candidate["spatial_reference"]
    interpretation = candidate["interpretation"]
    assets = candidate["assets"]
    governance = candidate["governance"]
    assert isinstance(capture, Mapping)
    assert isinstance(spatial, Mapping)
    assert isinstance(interpretation, Mapping)
    assert isinstance(assets, Mapping)
    assert isinstance(governance, Mapping)

    if not capture["methods"] or capture["acquisition_receipt_ref"] is None or capture["method_statement"] is None:
        findings.add(Finding("CAPTURE_PARADATA_REQUIRED"))
    if not steps:
        findings.add(Finding("PROCESSING_HISTORY_REQUIRED"))

    sequences = [step["sequence"] for step in steps]
    if sequences != list(range(1, len(steps) + 1)):
        findings.add(Finding("PROCESS_SEQUENCE_INVALID"))

    source_assets = set(assets["source_asset_refs"])
    derived_assets = set(assets["derived_asset_refs"])
    public_assets = set(assets["public_safe_asset_refs"])
    overlap = source_assets & derived_assets
    if overlap:
        findings.add(Finding("ASSET_ROLE_COLLAPSE"))
    output_assets = {item for step in steps for item in step["output_asset_refs"]}
    if output_assets - derived_assets:
        findings.add(Finding("PROCESS_OUTPUT_UNDECLARED"))
    if not overlap and derived_assets - output_assets:
        findings.add(Finding("DERIVED_ASSET_WITHOUT_PROCESSING"))
    if public_assets - derived_assets:
        findings.add(Finding("PUBLIC_ASSET_NOT_DERIVED"))
    available = set(source_assets)
    for step in steps:
        if not set(step["input_asset_refs"]).issubset(available):
            findings.add(Finding("PROCESS_INPUT_LINEAGE_UNRESOLVED"))
        available.update(step["output_asset_refs"])

    if spatial["scale_state"] in {"APPROXIMATE", "MEASURED"} and (
        spatial["scale_statement"] is None or spatial["scale_receipt_ref"] is None
    ):
        findings.add(Finding("SCALE_CLOSURE_REQUIRED"))
    if spatial["georeference_state"] == "GEOREFERENCED" and (
        spatial["crs_ref"] is None
        or spatial["georeference_receipt_ref"] is None
        or spatial["orientation_statement"] is None
    ):
        findings.add(Finding("GEOREFERENCE_CLOSURE_REQUIRED"))
    if spatial["georeference_state"] == "LOCAL_FRAME" and (
        spatial["crs_ref"] is not None or spatial["georeference_receipt_ref"] is not None
    ):
        findings.add(Finding("LOCAL_FRAME_GEOREFERENCE_CLAIM_FORBIDDEN"))

    interpretive_steps = [step for step in steps if step["interpretive"]]
    if interpretation["knowledge_character"] in {"INTERPRETIVE", "MIXED"} and (
        not interpretation["interpretive_step_refs"]
        or interpretation["uncertainty_statement"] is None
        or not interpretive_steps
    ):
        findings.add(Finding("INTERPRETIVE_PARADATA_REQUIRED"))
    if interpretation["knowledge_character"] == "REALITY_BASED" and (
        interpretation["interpretive_step_refs"] or interpretive_steps
    ):
        findings.add(Finding("REALITY_BASED_INTERPRETIVE_COLLAPSE"))
    if interpretation["representation_kind"] == "TWO_POINT_FIVE_D" and interpretation["vertical_surface_loss_disclosed"] is not True:
        findings.add(Finding("VERTICAL_SURFACE_LOSS_DISCLOSURE_REQUIRED"))

    common_refs = [
        governance["evidence_bundle_ref"],
        governance["rights_ref"],
        governance["technical_review_ref"],
        governance["cultural_review_ref"],
        governance["policy_decision_ref"],
    ]
    if any(value is None for value in common_refs):
        findings.add(Finding("GOVERNANCE_REFERENCE_REQUIRED"))

    closure_keys = (
        "publication_transform_receipt_ref",
        "release_manifest_ref",
        "correction_ref",
        "rollback_ref",
    )
    if governance["intended_use"] == "PUBLIC_CANDIDATE":
        if not public_assets:
            findings.add(Finding("PUBLIC_SAFE_ASSET_REQUIRED"))
        if governance["sensitivity_state"] != "PUBLIC_SAFE_REVIEWED":
            findings.add(Finding("PUBLIC_SENSITIVITY_REVIEW_REQUIRED"))
        if spatial["georeference_state"] != "GEOREFERENCED":
            findings.add(Finding("PUBLIC_SPATIAL_REFERENCE_REQUIRED"))
        if any(governance[key] is None for key in closure_keys):
            findings.add(Finding("PUBLIC_RELEASE_CLOSURE_REQUIRED"))
    elif governance["intended_use"] == "INTERNAL_REVIEW" and any(
        governance[key] is not None for key in closure_keys
    ):
        findings.add(Finding("INTERNAL_RELEASE_REFERENCE_FORBIDDEN"))
    return sorted(findings)


def validate_candidate(candidate: Mapping[str, object]) -> Result:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(schema_findings))
    integrity = _integrity_findings(candidate)
    if integrity:
        return Result("DENY", tuple(integrity))
    capture = candidate["capture"]
    governance = candidate["governance"]
    assert isinstance(capture, Mapping)
    assert isinstance(governance, Mapping)
    if capture["state"] == "ERROR" or governance["state"] == "ERROR":
        return Result("ERROR", (Finding("DOCUMENTATION_ERROR"),))
    abstain = _abstain_findings(candidate)
    if abstain:
        return Result("ABSTAIN", tuple(abstain))
    complete = _complete_findings(candidate)
    return Result("DENY", tuple(complete)) if complete else Result("PASS", ())


def _merge(base: object, overlay: object) -> object:
    if isinstance(base, dict) and isinstance(overlay, dict):
        merged = copy.deepcopy(base)
        for key, value in overlay.items():
            merged[key] = _merge(merged[key], value) if key in merged else copy.deepcopy(value)
        return merged
    return copy.deepcopy(overlay)


def _resolve_base(manifest: Mapping[str, object], name: str) -> dict[str, object]:
    bases = manifest["bases"]
    assert isinstance(bases, Mapping)
    raw = copy.deepcopy(bases[name])
    assert isinstance(raw, dict)
    parent = raw.pop("extends", None)
    if parent is None:
        return raw
    assert isinstance(parent, str)
    resolved = _merge(_resolve_base(manifest, parent), raw)
    assert isinstance(resolved, dict)
    return resolved


def _replace(document: object, pointer: str, value: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize_fixture_case(manifest: Mapping[str, object], case: Mapping[str, object]) -> dict[str, object]:
    candidate = _resolve_base(manifest, str(case["base"]))
    for mutation in case.get("mutations", []):
        assert isinstance(mutation, Mapping)
        _replace(candidate, str(mutation["path"]), mutation.get("value"))
    spec_hash, documentation_id = compute_identity(candidate)
    candidate["spec_hash"] = case.get("spec_hash_override", spec_hash)
    candidate["documentation_id"] = case.get("documentation_id_override", documentation_id)
    return candidate


def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))
    results: list[dict[str, object]] = []
    for case in manifest["cases"]:
        result = validate_candidate(materialize_fixture_case(manifest, case))
        expected = case["expected_findings"]
        results.append(
            {
                "name": case["name"],
                "outcome": result.outcome,
                "findings": result.codes,
                "ok": result.outcome == case["expected_outcome"] and result.codes == expected,
            }
        )
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        for result in results:
            print(json.dumps(result, sort_keys=True, separators=(",", ":")))
        return 0 if all(result["ok"] for result in results) else 1
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    candidate, findings = load_json_object(args.input)
    result = Result("ERROR", tuple(findings)) if candidate is None else validate_candidate(candidate)
    print(json.dumps({"authority": "NONE", "execution_mode": "FIXTURE_ONLY", "outcome": result.outcome, "findings": result.codes}, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
