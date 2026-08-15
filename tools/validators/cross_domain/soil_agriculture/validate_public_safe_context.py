#!/usr/bin/env python3
"""Validate fixture-only Soil-Agriculture public-safe context candidates."""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
GENERIC_PATH = REPO_ROOT / "tools/joins/join_candidates.py"
SPEC = importlib.util.spec_from_file_location("kfm_cross_lane_join_candidates", GENERIC_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("generic cross-lane join assessment module is unavailable")
GENERIC = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = GENERIC
SPEC.loader.exec_module(GENERIC)

CASES_PATH = REPO_ROOT / "fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json"
RELATION_PROFILE_REF = "kfm:relation-profile:soil-agriculture-public-safe-context:v1"
FIXTURE_PREFIX = "kfm:fixture:"
SCOPE = "soil-agriculture-public-safe-context-fixture-only-v1"

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    status: str
    findings: tuple[Finding, ...]
    @property
    def coherent(self) -> bool:
        return self.status == "PASS" and not self.findings

def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}

def _fixture_ref(value: object, nullable: bool = False) -> bool:
    return value is None if nullable and value is None else isinstance(value, str) and value.startswith(FIXTURE_PREFIX)

def validate_document(candidate: object) -> ValidationResult:
    generic = GENERIC.validate_document(candidate)
    if generic.findings:
        return ValidationResult("FAIL", tuple(sorted(Finding(f.code, f.path) for f in generic.findings)))
    if not isinstance(candidate, Mapping):
        return ValidationResult("FAIL", (Finding("PAIR_DOCUMENT_INVALID", "/"),))
    findings: set[Finding] = set()
    request = _mapping(candidate.get("request"))
    endpoints = _mapping(candidate.get("endpoints"))
    left, right = _mapping(endpoints.get("left")), _mapping(endpoints.get("right"))
    decision = _mapping(candidate.get("decision"))
    def add(code: str, path: str) -> None: findings.add(Finding(code, path))

    if request.get("relation_profile_ref") != RELATION_PROFILE_REF: add("RELATION_PROFILE_MISMATCH", "/request/relation_profile_ref")
    if request.get("predicate") != "SPATIAL_TEMPORAL": add("PAIR_PREDICATE_MISMATCH", "/request/predicate")
    if request.get("temporal_tolerance_seconds") != 0: add("PAIR_TEMPORAL_TOLERANCE_MISMATCH", "/request/temporal_tolerance_seconds")
    if left.get("domain") != "soil": add("ENDPOINT_DOMAIN_MISMATCH", "/endpoints/left/domain")
    if right.get("domain") != "agriculture": add("ENDPOINT_DOMAIN_MISMATCH", "/endpoints/right/domain")

    for side, endpoint in (("left", left), ("right", right)):
        for field in ("object_ref", "source_descriptor_ref", "spatial_cell_ref"):
            if not _fixture_ref(endpoint.get(field)): add("NON_FIXTURE_REF_DENIED", f"/endpoints/{side}/{field}")
        if not _fixture_ref(endpoint.get("evidence_ref"), nullable=True): add("NON_FIXTURE_REF_DENIED", f"/endpoints/{side}/evidence_ref")
        if endpoint.get("living_person") is not False: add("LIVING_PERSON_STATE_DENIED", f"/endpoints/{side}/living_person")

    if decision.get("validator_outcome") == "ALLOW":
        for side, endpoint in (("left", left), ("right", right)):
            if endpoint.get("sensitivity") != "PUBLIC_SAFE": add("ALLOW_SENSITIVITY_NOT_PUBLIC_SAFE", f"/endpoints/{side}/sensitivity")
            if endpoint.get("geometry_precision") != "GENERALIZED": add("ALLOW_GEOMETRY_NOT_GENERALIZED", f"/endpoints/{side}/geometry_precision")
            if endpoint.get("evidence_ref") is None: add("ALLOW_EVIDENCE_REF_MISSING", f"/endpoints/{side}/evidence_ref")
        if _mapping(decision.get("source_roles")).get("output_role") != "CANDIDATE_RELATION": add("ALLOW_OUTPUT_ROLE_INVALID", "/decision/source_roles/output_role")
        if any(value is not False for value in _mapping(decision.get("effects")).values()): add("ALLOW_EFFECTS_NOT_ALL_FALSE", "/decision/effects")
        agriculture_ref = right.get("object_ref")
        if isinstance(agriculture_ref, str) and any(token in agriculture_ref for token in ("private-farm", "operator", "parcel")):
            add("PRIVATE_AGRICULTURE_LINK_DENIED", "/endpoints/right/object_ref")

    return ValidationResult("FAIL" if findings else "PASS", tuple(sorted(findings)))

def _set_pointer(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [p.replace("~1", "/").replace("~0", "~") for p in pointer.lstrip("/").split("/")]
    parent: Any = candidate
    for part in parts[:-1]: parent = parent[int(part)] if isinstance(parent, list) else parent[part]
    if isinstance(parent, list): parent[int(parts[-1])] = copy.deepcopy(value)
    else: parent[parts[-1]] = copy.deepcopy(value)

def fixture_cases(path: Path = CASES_PATH):
    matrix = GENERIC.load_json_file(path)
    if not isinstance(matrix, Mapping) or not isinstance(matrix.get("base"), Mapping) or not isinstance(matrix.get("cases"), list): raise ValueError("fixture matrix invalid")
    base = GENERIC.seal(GENERIC.derive_outputs(matrix["base"]))
    result = []
    for raw in matrix["cases"]:
        candidate = copy.deepcopy(base)
        for mutation in raw.get("mutations", []): _set_pointer(candidate, mutation["path"], mutation["value"])
        if raw.get("rederive", True): candidate = GENERIC.derive_outputs(candidate)
        if raw.get("reseal", True): candidate = GENERIC.seal(candidate)
        result.append((raw["name"], candidate, validate_document(candidate), raw["expected"]))
    return result

def fixture_profile(path: Path = CASES_PATH) -> int:
    try: cases = fixture_cases(path)
    except Exception:
        print(json.dumps({"status":"FAIL","scope":SCOPE,"reason":"FIXTURE_MATRIX_INVALID"}, sort_keys=True)); return 1
    failed = []
    for name, candidate, result, expected in cases:
        decision = _mapping(candidate.get("decision"))
        if result.status != expected["validation_status"] or [f.code for f in result.findings] != expected["findings"] or decision.get("validator_outcome") != expected["validator_outcome"] or decision.get("status") != expected["decision_status"]: failed.append(name)
    print(json.dumps({"cases":len(cases),"failed_cases":failed,"scope":SCOPE,"status":"FAIL" if failed else "PASS"}, sort_keys=True, separators=(",",":")))
    return 1 if failed else 0

def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__); parser.add_argument("--fixtures", action="store_true"); parser.add_argument("files", nargs="*", type=Path); args = parser.parse_args(argv)
    if args.fixtures: return fixture_profile()
    if not args.files: parser.error("provide assessment files or --fixtures")
    rc = 0
    for path in sorted(args.files):
        try: result = validate_document(GENERIC.load_json_file(path))
        except Exception: result = ValidationResult("FAIL", (Finding("INPUT_OR_DEPENDENCY_ERROR", "/"),))
        print(json.dumps({"file":path.name,"findings":[{"code":f.code,"path":f.path} for f in result.findings],"scope":SCOPE,"status":result.status}, sort_keys=True, separators=(",",":")))
        rc = max(rc, 0 if result.coherent else 1)
    return rc

if __name__ == "__main__": raise SystemExit(run())
