"""Tests for fixture-only map manifest integrity assessments."""
from __future__ import annotations
import copy, importlib.util, json, sys
from pathlib import Path
REPO_ROOT=Path(__file__).resolve().parents[4]
MODULE_PATH=REPO_ROOT/"tools/validators/map/map_manifest_integrity_assessment/validate_map_manifest_integrity_assessment.py"
VALID=REPO_ROOT/"fixtures/map/map_manifest_integrity_assessment/valid"
INVALID=REPO_ROOT/"fixtures/map/map_manifest_integrity_assessment/invalid"
SPEC=importlib.util.spec_from_file_location("kfm_map_manifest_integrity",MODULE_PATH); assert SPEC and SPEC.loader
MODULE=importlib.util.module_from_spec(SPEC); sys.modules[SPEC.name]=MODULE; SPEC.loader.exec_module(MODULE)

def load(directory:Path,name:str)->dict[str,object]:
 value=json.loads((directory/name).read_text()); assert isinstance(value,dict); return value

def rehash(payload:dict[str,object])->None: payload["spec_hash"]=MODULE.canonical_spec_hash(payload)

def set_decision(payload:dict[str,object])->None:
 reasons=MODULE.expected_reasons(payload); payload["decision"]={"outcome":MODULE.expected_outcome(reasons),"reasons":reasons}; rehash(payload)

def test_verified_answer_is_valid_and_deterministic()->None:
 payload=load(VALID,"verified_answer.json"); first=MODULE.validate_payload(payload); second=MODULE.validate_payload(copy.deepcopy(payload)); assert first==second; assert first.ok; assert payload["decision"]=={"outcome":"ANSWER","reasons":[]}

def test_unsigned_manifest_is_valid_abstain()->None:
 payload=load(VALID,"unsigned_abstain.json"); assert MODULE.validate_payload(payload).ok; assert payload["decision"]["outcome"]=="ABSTAIN"

def test_unresolved_evidence_is_valid_abstain()->None:
 payload=load(VALID,"evidence_unresolved_abstain.json"); assert MODULE.validate_payload(payload).ok

def test_manifest_hash_mismatch_is_valid_deny()->None:
 payload=load(VALID,"hash_mismatch_denied.json"); assert MODULE.validate_payload(payload).ok; assert payload["decision"]=={"outcome":"DENY","reasons":["MANIFEST_SPEC_HASH_MISMATCH"]}

def test_signature_failure_requires_deny()->None:
 payload=load(VALID,"verified_answer.json"); payload["signature_verdict"]={"state":"FAILED"}; set_decision(payload); result=MODULE.validate_payload(payload); assert result.ok; assert payload["decision"]=={"outcome":"DENY","reasons":["SIGNATURE_FAILED"]}

def test_signature_error_precedes_deny_and_abstain()->None:
 payload=load(VALID,"verified_answer.json"); payload["signature_verdict"]={"state":"ERROR"}; payload["evidence_resolution"]["bundle_state"]="DENIED"; set_decision(payload); assert MODULE.validate_payload(payload).ok; assert payload["decision"]["outcome"]=="ERROR"

def test_signer_identity_mismatch_is_denied()->None:
 payload=load(VALID,"verified_answer.json"); payload["signature_verdict"]["signer_identity"]="https://example.invalid/other"; set_decision(payload); assert MODULE.validate_payload(payload).ok; assert "SIGNER_IDENTITY_MISMATCH" in payload["decision"]["reasons"]

def test_asset_hash_and_size_mismatch_are_denied()->None:
 payload=load(VALID,"verified_answer.json"); payload["asset_verification"]["observed_sha256"]="sha256:"+"1"*64; payload["asset_verification"]["observed_bytes"]=20; set_decision(payload); assert MODULE.validate_payload(payload).ok; assert payload["decision"]["reasons"]==["ASSET_HASH_MISMATCH","ASSET_SIZE_MISMATCH"]

def test_required_deep_verify_cannot_be_skipped()->None:
 payload=load(VALID,"verified_answer.json"); payload["asset_verification"]={"state":"SKIPPED"}; set_decision(payload); assert MODULE.validate_payload(payload).ok; assert payload["decision"]=={"outcome":"ABSTAIN","reasons":["ASSET_DEEP_VERIFY_SKIPPED"]}

def test_assets_must_be_canonical_and_unique()->None:
 payload=load(VALID,"verified_answer.json"); duplicate=copy.deepcopy(payload["manifest"]["assets"][0]); duplicate["asset_id"]="aaa"; payload["manifest"]["assets"].append(duplicate); payload["manifest"]["spec_hash"]=MODULE.canonical_manifest_spec_hash(payload["manifest"]); payload["expected_manifest_spec_hash"]=payload["manifest"]["spec_hash"]; set_decision(payload); result=MODULE.validate_payload(payload); assert MODULE.Finding("ASSETS_NOT_CANONICAL","/manifest/assets") in result.findings

def test_decision_mismatch_is_rejected()->None:
 payload=load(INVALID,"decision_mismatch.json"); result=MODULE.validate_payload(payload); assert MODULE.Finding("DECISION_REASONS_MISMATCH","/decision/reasons") in result.findings

def test_assessment_spec_hash_mismatch_is_rejected()->None:
 payload=load(VALID,"verified_answer.json"); payload["assessed_at"]="2026-04-11T18:06:00Z"; result=MODULE.validate_payload(payload); assert MODULE.Finding("SPEC_HASH_MISMATCH","/spec_hash") in result.findings
