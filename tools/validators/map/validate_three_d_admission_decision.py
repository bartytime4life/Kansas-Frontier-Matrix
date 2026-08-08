#!/usr/bin/env python3
"""Validate inactive, fixture-only ThreeDAdmissionDecision candidates.

ALLOW_RENDER_CANDIDATE proves local fixture coherence only. It does not boot a
renderer, install a plugin, evaluate policy, approve review, release, or publish.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/map/three_d_admission_decision.schema.json"
CASES = ROOT / "fixtures/contracts/v1/map/three_d_admission_decision/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "three-d-admission-decision-fixture-only-v1"
FALSE_EFFECTS = {
    key: False
    for key in (
        "renderer_booted", "plugin_installed", "policy_evaluated",
        "human_review_approved", "release_authorized", "deployed", "published",
    )
}
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE", "INPUT_SYMLINK_DENIED",
    "JSON_INVALID", "JSON_DUPLICATE_KEY", "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT",
    "SCHEMA_UNAVAILABLE", "HASHING_UNAVAILABLE", "SPEC_HASH_MISMATCH",
    "THREE_D_ADMISSION_ID_MISMATCH", "FIXTURE_MANIFEST_INVALID",
}
EXPECTED_LABEL = {
    "TERRAIN_3D": "TWO_POINT_FIVE_D",
    "FILL_EXTRUSION_2_5D": "TWO_POINT_FIVE_D",
    "GLOBE": "GLOBE",
    "OGC_3D_TILES": "TRUE_3D",
    "GLTF": "TRUE_3D",
    "POINT_CLOUD": "TRUE_3D",
}
EXPECTED_PLUGINS = {
    "TERRAIN_3D": set(), "FILL_EXTRUSION_2_5D": set(), "GLOBE": set(),
    "OGC_3D_TILES": {"3d-tiles-renderer", "three"},
    "GLTF": {"maplibre-three-plugin", "three"},
    "POINT_CLOUD": {"maplibre-gl-lidar"},
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
        return self.outcome == "ALLOW_RENDER_CANDIDATE"

class DuplicateKeyError(ValueError): pass
class NonFiniteNumberError(ValueError): pass

def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result: raise DuplicateKeyError
        result[key] = value
    return result

def _bad_number(_value: str) -> object: raise NonFiniteNumberError

def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed): raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink(): return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file(): return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES: return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_pairs,
                           parse_constant=_bad_number, parse_float=_finite_float)
    except DuplicateKeyError: return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError: return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError: return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError): return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict): return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []

def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"

def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
                        key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]

def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate)); subject.pop("decision_id", None); subject.pop("spec_hash", None); return subject

def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))

def expected_decision_id(candidate: Mapping[str, Any]) -> str:
    return "three-d-admission:" + canonical_spec_hash(candidate).removeprefix("sha256:")[:24]

def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate)); result["spec_hash"] = canonical_spec_hash(result); result["decision_id"] = expected_decision_id(result); return result

def _canonical(values: Any) -> bool:
    return isinstance(values, list) and values == sorted(set(values))

def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    arrays = [
        "evidence_bundle_refs", "source_descriptor_refs", "domain_contexts", "source_roles", "limitations"
    ]
    for key in arrays:
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/{key}"))
    sensitivity = candidate.get("sensitivity")
    if isinstance(sensitivity, Mapping) and not _canonical(sensitivity.get("transformation_receipt_refs")):
        findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", "/sensitivity/transformation_receipt_refs"))
    parity = candidate.get("parity")
    if isinstance(parity, Mapping):
        for key, value in parity.items():
            if not _canonical(value): findings.append(Finding("NONCANONICAL_REFERENCE_ARRAY", f"/parity/{key}"))

    mode = candidate.get("requested_mode")
    if candidate.get("geometry_label") != EXPECTED_LABEL.get(mode):
        findings.append(Finding("GEOMETRY_LABEL_MISMATCH", "/geometry_label"))
    if candidate.get("requested_use") == "VERTICAL_EVIDENCE" and candidate.get("geometry_label") == "TWO_POINT_FIVE_D":
        findings.append(Finding("TWO_POINT_FIVE_D_VERTICAL_EVIDENCE", "/requested_use"))
    if candidate.get("requested_use") == "SPECTACLE_ONLY":
        findings.append(Finding("EXPLANATORY_BURDEN_NOT_MET", "/requested_use"))

    if isinstance(sensitivity, Mapping):
        if sensitivity.get("living_person_present") is True:
            findings.append(Finding("LIVING_PERSON_GEOMETRY_DENIED", "/sensitivity/living_person_present"))
        if sensitivity.get("rare_species_precision") == "PRECISE":
            findings.append(Finding("RARE_SPECIES_PRECISION_DENIED", "/sensitivity/rare_species_precision"))
        if sensitivity.get("critical_infrastructure_precision") == "PRECISE":
            findings.append(Finding("CRITICAL_INFRASTRUCTURE_PRECISION_DENIED", "/sensitivity/critical_infrastructure_precision"))
        if sensitivity.get("archaeology_present") is True:
            meters = sensitivity.get("archaeology_generalization_meters")
            if not isinstance(meters, int) or meters < 5000:
                findings.append(Finding("ARCHAEOLOGY_GENERALIZATION_INSUFFICIENT", "/sensitivity/archaeology_generalization_meters"))

    if candidate.get("representation_kind") in {"MODELED", "SYNTHETIC", "RECONSTRUCTED"} and candidate.get("reality_boundary_note_ref") is None:
        findings.append(Finding("REALITY_BOUNDARY_NOTE_REQUIRED", "/reality_boundary_note_ref"))

    if isinstance(parity, Mapping):
        evidence = candidate.get("evidence_bundle_refs")
        if parity.get("two_d_evidence_refs") != parity.get("three_d_evidence_refs") or parity.get("three_d_evidence_refs") != evidence:
            findings.append(Finding("TWO_D_EVIDENCE_PARITY_MISMATCH", "/parity/three_d_evidence_refs"))
        if parity.get("drawer_fields_2d") != parity.get("drawer_fields_3d"):
            findings.append(Finding("EVIDENCE_DRAWER_PARITY_MISMATCH", "/parity/drawer_fields_3d"))
        if parity.get("correction_refs_2d") != parity.get("correction_refs_3d"):
            findings.append(Finding("CORRECTION_PARITY_MISMATCH", "/parity/correction_refs_3d"))
        if parity.get("release_refs_2d") != parity.get("release_refs_3d"):
            findings.append(Finding("RELEASE_PARITY_MISMATCH", "/parity/release_refs_3d"))
        if parity.get("sensitivity_labels_2d") != parity.get("sensitivity_labels_3d"):
            findings.append(Finding("SENSITIVITY_PARITY_MISMATCH", "/parity/sensitivity_labels_3d"))

    plugins = candidate.get("plugin_dependencies")
    if isinstance(plugins, list):
        names = [item.get("name") for item in plugins if isinstance(item, Mapping)]
        if names != sorted(set(names)):
            findings.append(Finding("NONCANONICAL_PLUGIN_ARRAY", "/plugin_dependencies"))
        if set(names) != EXPECTED_PLUGINS.get(mode, set()):
            findings.append(Finding("PLUGIN_SET_MISMATCH", "/plugin_dependencies"))
        for index, item in enumerate(plugins):
            if isinstance(item, Mapping) and item.get("license_status") != "VERIFIED":
                findings.append(Finding("PLUGIN_LICENSE_UNVERIFIED", f"/plugin_dependencies/{index}/license_status"))

    if candidate.get("review_state") != "HOLD": findings.append(Finding("REVIEW_STATE_OVERCLAIM", "/review_state"))
    if candidate.get("public_use_allowed") is not False: findings.append(Finding("PUBLIC_USE_OVERCLAIM", "/public_use_allowed"))
    if candidate.get("effects") != FALSE_EFFECTS: findings.append(Finding("AUTHORITY_EFFECT_OVERCLAIM", "/effects"))

    try:
        expected_hash = canonical_spec_hash(candidate); expected_id = expected_decision_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash: findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("decision_id") != expected_id: findings.append(Finding("THREE_D_ADMISSION_ID_MISMATCH", "/decision_id"))
    return findings

def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings: findings.extend(_semantic(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered: return ValidationResult("ALLOW_RENDER_CANDIDATE", ordered)
    if any(item.code in ERROR_CODES or item.code == "SCHEMA_INVALID" for item in ordered): return ValidationResult("ERROR", ordered)
    deny = any(item.code != "REALITY_BOUNDARY_NOTE_REQUIRED" for item in ordered)
    return ValidationResult("DENY" if deny else "ABSTAIN", ordered)

def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None: return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)

def _set(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/") if part]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    last = parts[-1]
    if isinstance(current, list): current[int(last)] = copy.deepcopy(value)
    else: current[last] = copy.deepcopy(value)

def _fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if document is None or findings or document.get("profile") != "kfm.map.three-d-admission-decision-fixtures.v1" or not isinstance(document.get("bases"), dict) or not isinstance(document.get("cases"), list):
        raise ValueError("invalid fixture manifest")
    return document

def materialize_case(document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    base = document["bases"][case["base"]]
    candidate = copy.deepcopy(base)
    for mutation in case.get("mutations", []): _set(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH": candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID": candidate["decision_id"] = "three-d-admission:" + "0" * 24
    elif mode != "RECOMPUTE": raise ValueError("unknown identity mode")
    return candidate

def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _fixture_document(); output=[]; names=set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names: raise ValueError("invalid fixture case")
        names.add(raw["name"]); output.append((raw, materialize_case(document, raw)))
    return output

def _serialize(result: ValidationResult, *, path: Path | None=None, case: str | None=None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": SCOPE,
        "authority": {key: False for key in ("renderer_boot", "plugin_install", "policy", "human_review", "release", "deployment", "publication", "public_use")},
    }
    if path is not None:
        try: payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError): payload["file"] = path.name
    if case is not None: payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))

def replay_fixtures() -> int:
    try: cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RecursionError):
        print(_serialize(ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),)), path=CASES)); return 1
    ok=True
    for definition, candidate in cases:
        result=validate_payload(candidate)
        expected=tuple(Finding(item["code"], item["path"]) for item in definition.get("expected_findings", []))
        matches=result.outcome==definition.get("expected_outcome") and result.findings==expected
        print(json.dumps({"case":definition["name"],"outcome":result.outcome,"findings":[{"code":x.code,"path":x.path} for x in result.findings],"matches_expected":matches,"scope":SCOPE},sort_keys=True,separators=(",",":")))
        ok &= matches
    return 0 if ok else 1

def main(argv: Sequence[str] | None=None) -> int:
    parser=argparse.ArgumentParser(description="Validate an inactive ThreeDAdmissionDecision candidate.")
    parser.add_argument("file", nargs="?", type=Path); parser.add_argument("--fixtures", action="store_true")
    args=parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures and args.file is not None: print("--fixtures cannot be combined with a file", file=sys.stderr); return 2
    if args.fixtures: return replay_fixtures()
    if args.file is None: print("a fixture file or --fixtures is required", file=sys.stderr); return 2
    result=validate_file(args.file); print(_serialize(result,path=args.file)); return 0 if result.ok else 1

if __name__ == "__main__": raise SystemExit(main())
