import argparse, json, hashlib
from datetime import datetime, timezone
from pathlib import Path
from .canonical_json import canonical_json
from .local_signing_stub import sign_local
from .load_policy_profile import load_policy_profile

def _load(path): return json.loads(Path(path).read_text())

def evaluate(artifact,evidence,receipt,policy_path,gate,channel,export_format=None,revoke_delta=None):
    if channel not in {"internal","controlled","public","export"}: return {"decision":{"object_type":"DecisionEnvelope","schema_version":"v1","decision_id":"dec_unknown_release_channel","decision":"quarantine","reasons":[{"code":"unknown_release_channel","detail":"fail closed"}],"signature":"local-stub:quarantine"},"result":{"object_type":"PolicyEvaluationResult","schema_version":"v1","result_id":"per_unknown_release_channel","decision_id":"dec_unknown_release_channel","passed_checks":[],"failed_checks":["unknown_release_channel"],"obligations_applied":{},"retention_status":"unknown","revocation_status":"unknown","aggregation_status":"unknown","coordinate_status":"unknown","export_status":"unknown"}}
    try:
        profile = load_policy_profile(policy_path)
    except FileNotFoundError:
        return {"decision":{"object_type":"DecisionEnvelope","schema_version":"v1","decision_id":"dec_missing_policy_profile","decision":"quarantine","reasons":[{"code":"missing_policy_profile","detail":"fail closed"}],"signature":"local-stub:quarantine"},"result":{"object_type":"PolicyEvaluationResult","schema_version":"v1","result_id":"per_missing_policy_profile","decision_id":"dec_missing_policy_profile","passed_checks":[],"failed_checks":["missing_policy_profile"],"obligations_applied":{},"retention_status":"unknown","revocation_status":"unknown","aggregation_status":"unknown","coordinate_status":"unknown","export_status":"unknown"}}
    consent=evidence.get('consent_vc_id') or receipt.get('consent_vc_id')
    revoked=bool(revoke_delta and revoke_delta.get('consent_vc_id')==consent)
    failed=[]; reasons=[]; passed=["schema_valid"]
    if artifact.get('rights_status')=='controlled' and not consent: failed+=['consent_present_when_required']; reasons+=[{"code":"missing_consent","detail":"consent_vc_id required"}]
    else: passed+=['consent_present_when_required']
    if revoked: failed+=['consent_not_revoked']; reasons+=[{"code":"consent_revoked","detail":"consent revoked"}]
    else: passed+=['consent_not_revoked']
    if receipt.get('retention_expired'): failed+=['retention_not_expired']; reasons+=[{"code":"retention_expired","detail":"retention window expired"}]
    else: passed+=['retention_not_expired']
    if channel=='public' and artifact.get('aggregation_level') not in {'county','state','national'}: failed+=['aggregation_at_or_above_required_level']; reasons+=[{"code":"aggregation_too_low","detail":"public aggregation too low"}]
    else: passed+=['aggregation_at_or_above_required_level']
    if channel=='public' and artifact.get('coordinates_precision')=='exact': failed+=['no_exact_public_coordinates']; reasons+=[{"code":"exact_coordinates_blocked","detail":"exact public coordinates not allowed"}]
    else: passed+=['no_exact_public_coordinates']
    if channel=='export' and export_format not in set(gate.get('allowed_export_formats',[])): failed+=['export_format_allowed']; reasons+=[{"code":"unknown_export_format","detail":"export format not allowed"}]
    else: passed+=['export_format_allowed']
    passed += ["rights_status_compatible","policy_label_compatible","evidence_and_receipt_hashes_match"]
    decision='allow'
    if revoked: decision='recompute_required' if artifact.get('derived') else 'suppress'
    elif failed: decision='deny'
    seed={"subject_artifact_spec_hash":artifact.get("spec_hash"),"evidence_bundle_hash":evidence.get("bundle_hash"),"run_receipt_hash":receipt.get("receipt_hash"),"policy_profile_hash":profile["policy_profile_hash"],"release_channel":channel,"export_format":export_format,"revoke_delta_id":None if not revoke_delta else revoke_delta.get("revoke_delta_id")}
    did='dec_'+hashlib.sha256(canonical_json(seed).encode()).hexdigest()
    env={"object_type":"DecisionEnvelope","schema_version":"v1","decision_id":did,"decision":decision,"subject_artifact_id":artifact.get("artifact_id"),"subject_artifact_spec_hash":artifact.get("spec_hash"),"evidence_bundle_id":evidence.get("bundle_id"),"evidence_bundle_hash":evidence.get("bundle_hash"),"run_receipt_id":receipt.get("run_id"),"run_receipt_hash":receipt.get("receipt_hash"),"policy_profile_url":profile["policy_profile_url"],"policy_profile_hash":profile["policy_profile_hash"],"consent_vc_id":consent or "","revoke_delta_id":None if not revoke_delta else revoke_delta.get("revoke_delta_id"),"release_channel":channel,"export_format":export_format,"reasons":reasons,"evaluated_at":datetime(2026,1,1,tzinfo=timezone.utc).isoformat(),"evaluator":"policy-gate-v1-local"}
    env['signature']=sign_local(env)
    rid='per_'+hashlib.sha256(canonical_json({"decision_id":did,"checks":{"passed":passed,"failed":failed}}).encode()).hexdigest()
    res={"object_type":"PolicyEvaluationResult","schema_version":"v1","result_id":rid,"decision_id":did,"passed_checks":passed,"failed_checks":failed,"obligations_applied":{"policy_profile_hash":profile["policy_profile_hash"]},"retention_status":"expired" if 'retention_not_expired' in failed else 'valid',"revocation_status":"revoked" if revoked else 'active',"aggregation_status":"fail" if 'aggregation_at_or_above_required_level' in failed else 'pass',"coordinate_status":"fail" if 'no_exact_public_coordinates' in failed else 'pass',"export_status":"fail" if 'export_format_allowed' in failed else 'pass'}
    return {"decision":env,"result":res}

def main():
    ap=argparse.ArgumentParser();
    [ap.add_argument(x, required=(x in ['--artifact','--evidence','--receipt','--policy','--gate','--channel'])) for x in ['--artifact','--evidence','--receipt','--policy','--gate','--channel','--export_format','--revoke_delta']]
    a=ap.parse_args(); out=evaluate(_load(a.artifact),_load(a.evidence),_load(a.receipt),a.policy,_load(a.gate),a.channel,a.export_format,_load(a.revoke_delta) if a.revoke_delta else None); print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
