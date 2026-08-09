#!/usr/bin/env python3
"""Deterministic fixture validator for InspectableClaimCarrierAssessment."""
from __future__ import annotations
import argparse, copy, hashlib, json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
FIXTURES = ROOT / "fixtures/contracts/v1/governance/inspectable_claim_carrier_assessment"
PROFILE = "kfm.governance.inspectable-claim-carrier-assessment.v1"
CORE_NEGATIVE = {"ABSTAIN", "DENY", "ERROR", "STALE"}
PUBLIC_NEGATIVE = CORE_NEGATIVE | {"CORRECTED", "WITHDRAWN"}
CARRIERS = {"MAP_LAYER","TILE_ARTIFACT","GRAPH_PROJECTION","DASHBOARD","EXPORT","STORY","AI_ANSWER","THREE_D_SCENE"}
REF_PREFIXES = {"claim_ref":"kfm:claim:","evidence_bundle_ref":"kfm:evidence-bundle:","policy_decision_ref":"kfm:policy-decision:","release_manifest_ref":"kfm:release-manifest:","correction_ref":"kfm:correction:","rollback_ref":"kfm:rollback:"}
EFFECTS = {"creates_claim","creates_evidence","approves_policy","promotes","releases","deploys","publishes"}
TOP = {"profile","assessment_id","carrier_kind",*REF_PREFIXES,"negative_states","public_exposure","effects"}

def canonical(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")

def expected_id(obj: dict[str, Any]) -> str:
    subject = copy.deepcopy(obj); subject.pop("assessment_id", None)
    return "kfm:claim-carrier:" + hashlib.sha256(canonical(subject)).hexdigest()

def validate(obj: Any) -> tuple[str, list[str]]:
    if not isinstance(obj, dict): return "ERROR", ["NOT_OBJECT"]
    findings: list[str] = []
    if set(obj) != TOP: return "ERROR", ["SHAPE_MISMATCH"]
    if obj.get("profile") != PROFILE or obj.get("carrier_kind") not in CARRIERS: return "ERROR", ["VOCABULARY_INVALID"]
    if obj.get("assessment_id") != expected_id(obj): return "ERROR", ["IDENTITY_MISMATCH"]
    for field, prefix in REF_PREFIXES.items():
        value = obj.get(field)
        if not isinstance(value, str) or not value.startswith(prefix) or len(value) <= len(prefix): findings.append("MISSING_TRUST_BINDING")
    states = obj.get("negative_states")
    if not isinstance(states, list) or states != sorted(states) or len(states) != len(set(states)): return "ERROR", ["NEGATIVE_STATE_ORDER_INVALID"]
    state_set = set(states)
    if not CORE_NEGATIVE.issubset(state_set): findings.append("NEGATIVE_STATE_VISIBILITY_MISSING")
    if obj.get("public_exposure") is True and not PUBLIC_NEGATIVE.issubset(state_set): findings.append("PUBLIC_CORRECTION_STATE_MISSING")
    effects = obj.get("effects")
    if not isinstance(effects, dict) or set(effects) != EFFECTS: return "ERROR", ["EFFECT_SHAPE_INVALID"]
    if any(value is not False for value in effects.values()): findings.append("AUTHORITY_OVERREACH")
    if obj.get("public_exposure") not in {True, False}: return "ERROR", ["PUBLIC_EXPOSURE_INVALID"]
    return ("DENY", sorted(set(findings))) if findings else ("PASS", [])

def mutate(base: dict[str, Any], mutations: dict[str, Any]) -> dict[str, Any]:
    item = copy.deepcopy(base)
    for key, value in mutations.items():
        if "." in key:
            parent, child = key.split(".", 1); item[parent][child] = value
        else: item[key] = value
    if "assessment_id" not in mutations: item["assessment_id"] = expected_id(item)
    return item

def run_fixtures() -> int:
    base = json.loads((FIXTURES / "valid.json").read_text(encoding="utf-8"))
    outcome, findings = validate(base)
    if outcome != "PASS": print(f"ERROR valid fixture: {outcome} {findings}"); return 2
    cases = json.loads((FIXTURES / "cases.json").read_text(encoding="utf-8"))
    for case in cases:
        obj = mutate(base, case["mutations"]); outcome, findings = validate(obj)
        if outcome != case["expected"]: print(f"ERROR {case['name']}: expected {case['expected']} got {outcome} {findings}"); return 2
    print(f"PASS: valid fixture + {len(cases)} exact-polarity cases"); return 0

def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("path", nargs="?"); parser.add_argument("--fixtures", action="store_true"); args = parser.parse_args()
    if args.fixtures: return run_fixtures()
    if not args.path: parser.error("path required unless --fixtures is used")
    try: obj = json.loads(Path(args.path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc: print(f"ERROR: {type(exc).__name__}"); return 2
    outcome, findings = validate(obj); print(outcome + (": " + ",".join(findings) if findings else "")); return {"PASS":0,"DENY":6,"ERROR":2}[outcome]

if __name__ == "__main__": raise SystemExit(main())
