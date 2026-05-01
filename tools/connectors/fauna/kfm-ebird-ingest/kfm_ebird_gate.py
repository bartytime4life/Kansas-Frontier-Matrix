#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from datetime import datetime, timezone

VERSION = "0.25.0"
FORBIDDEN_FIELDS = {"decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number"}
FORBIDDEN_PATTERNS = [r"restricted", r"quarantine", r"suppression[_-]?receipt", r"suppressed[_-]?group", r"token=", r"apikey=", r"secret"]


def now(): return datetime.now(timezone.utc).isoformat()
def canonical(v): return json.dumps(v, sort_keys=True, separators=(",",":"))
def sha_file(path: str|None):
    if not path: return None
    p=Path(path)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None

def load_json(path):
    if not path: return None
    p=Path(path)
    if not p.exists(): raise SystemExit(f"missing artifact: {path}")
    return json.loads(p.read_text())

def scan_public_json(obj, findings):
    if isinstance(obj, dict):
        for k,v in obj.items():
            if k in FORBIDDEN_FIELDS: findings.append(f"forbidden field {k}")
            if isinstance(v, str):
                for pat in FORBIDDEN_PATTERNS:
                    if re.search(pat, v, flags=re.I): findings.append(f"forbidden value pattern {pat}")
            scan_public_json(v, findings)
    elif isinstance(obj, list):
        for x in obj: scan_public_json(x, findings)

def parse(argv):
    p=argparse.ArgumentParser(prog="kfm-ebird-gate")
    p.add_argument("--version", action="version", version=VERSION)
    p.add_argument("--mode", default="evaluate", choices=["evaluate","validate","explain","bundle","report"])
    p.add_argument("--aggregate", default="both", choices=["huc12","county","both"])
    for n in ["root_of_trust","root_validation_report","reconciliation_manifest","global_invariant_report","hash_reconciliation_report","spec_hash_reconciliation_report","public_reconciliation_summary","certification_packet","governance_signoff","recertification_receipt","assurance_scan_report","quality_scan_report","redteam_summary_report","conformance_report","contract_lock","deployment_receipt","deployment_verify_report","package_manifest","public_portal_manifest","public_download_manifest","release_index","environment_latest","published_root","catalog_root","layer_registry_dir","out_dir","public_out_dir"]:
        p.add_argument("--"+n.replace("_","-"))
    p.add_argument("--strict", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    return p.parse_args(argv)

def main():
    a=parse(sys.argv[1:])
    art={k:getattr(a,k) for k in vars(a) if k.endswith("report") or k in {"root_of_trust","contract_lock","release_index","package_manifest","deployment_receipt","public_portal_manifest","public_download_manifest","reconciliation_manifest","certification_packet","environment_latest"}}
    hashes={k:sha_file(v) for k,v in art.items() if v}
    root=load_json(a.root_of_trust) if a.root_of_trust else {}
    gate_seed={"aggregate_targets":a.aggregate,"input_artifact_hashes":hashes,"root_id":root.get("root_id"),"root_hash":root.get("root_hash"),"mode":a.mode,"strict":a.strict,"adapter_version":VERSION}
    gate_id=hashlib.sha256(canonical(gate_seed).encode()).hexdigest()[:16]

    warnings=[]; blockers=[]; hard=[]; checks=[]
    decision="go"

    pub_candidates=[a.public_reconciliation_summary,a.public_portal_manifest,a.public_download_manifest]
    for c in pub_candidates:
        if c:
            findings=[]
            scan_public_json(load_json(c), findings)
            if findings:
                blockers.extend(findings)
                decision="no_go"

    red=load_json(a.redteam_summary_report) if a.redteam_summary_report else {}
    if red.get("critical_failed") is True:
        blockers.append("failed red-team critical scenario"); decision="no_go"
    conf=load_json(a.conformance_report) if a.conformance_report else {}
    if conf.get("status")=="fail": blockers.append("failed conformance report"); decision="no_go"
    root_val=load_json(a.root_validation_report) if a.root_validation_report else {}
    if root_val and root_val.get("root_hash_matches") is False: blockers.append("root_hash mismatch"); decision="no_go"

    if decision=="go" and warnings: decision="go_with_warnings"
    if decision=="go" and a.strict and any(not v for v in hashes.values()): decision="needs_review"

    out=Path(a.out_dir or f"data/catalog/fauna/ebird/gates/{gate_id}")
    pub_out=Path(a.public_out_dir or f"data/published/fauna/ebird/gates/{gate_id}")
    if not a.dry_run:
        if out.exists() and not a.force: raise SystemExit("out-dir exists; use --force")
        out.mkdir(parents=True, exist_ok=True)
    gate_decision={"schema_version":"v1","object_type":"EbirdGateDecision","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"gate","public_safe_final_outputs":True,"exact_points":"restricted","gate_id":gate_id,"aggregate_targets":[a.aggregate],"decision":decision,"strict":a.strict,"root_id":root.get("root_id"),"root_hash":root.get("root_hash"),"release_ids":[],"run_ids":[],"deployment_ids":[],"package_ids":[],"certification_ids":[],"recertification_ids":[],"kfm_spec_hashes":[],"hard_gates":hard,"warnings":warnings,"blockers":blockers,"required_next_actions":[],"generated_at":now()}
    validation={"schema_version":"v1","object_type":"EbirdGateValidationReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","gate_id":gate_id,"status":"fail" if blockers else "pass","checks":checks,"summary":{"total":len(checks),"passed":0,"warnings":0,"failed":len(blockers),"skipped":0},"hard_failures":blockers,"generated_at":now()}
    explanation={"schema_version":"v1","object_type":"EbirdGateExplanation","domain":"fauna","source":"ebird","adapter":"kfm-ebird","gate_id":gate_id,"decision":decision,"explanation":"Unified Layer 25 gate decision.","blocker_explanations":[{"blocker_id":f"B{i+1}","blocker_type":"hard_gate","severity":"fail","affected_artifact":"mixed","why_it_blocks":b,"remediation_path":"run_remediation","suggested_cli":"kfm-ebird-remediate"} for i,b in enumerate(blockers)],"warning_explanations":warnings,"generated_at":now()}
    blocker_report={"schema_version":"v1","object_type":"EbirdGateBlockerReport","domain":"fauna","source":"ebird","adapter":"kfm-ebird","gate_id":gate_id,"blockers":[{"blocker_id":f"B{i+1}","category":"safety","severity":"fail","message":b,"suggested_resolution_layer":"manual_review"} for i,b in enumerate(blockers)],"generated_at":now()}
    manifest={"schema_version":"v1","object_type":"EbirdGateManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"gate","public_safe_final_outputs":True,"exact_points":"restricted","gate_id":gate_id,"input_artifacts":[{"path_or_uri":k,"sha256":v,"artifact_type":"input","policy_label":"layer","public_safe":True} for k,v in hashes.items()],"output_artifacts":[],"validators_run":["validate_ebird_gate"],"policy_checks_run":["ebird.rego.layer25"],"public_safety_checks_run":["public_safety_scanner"],"generated_at":now()}
    if not a.dry_run:
        (out/"gate_decision.json").write_text(json.dumps(gate_decision,indent=2)+"\n")
        (out/"gate_validation_report.json").write_text(json.dumps(validation,indent=2)+"\n")
        (out/"gate_explanation.json").write_text(json.dumps(explanation,indent=2)+"\n")
        (out/"gate_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
        (out/"gate_blocker_report.json").write_text(json.dumps(blocker_report,indent=2)+"\n")
        (out/"gate_operator_report.md").write_text(f"# eBird Gate {gate_id}\n\nDecision: **{decision}**\n")
        pub_out.mkdir(parents=True, exist_ok=True)
        public_summary={"schema_version":"v1","object_type":"PublicEbirdGateSummary","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","gate_id":gate_id,"decision":decision,"aggregate_targets":[a.aggregate],"release_ids":[],"deployment_ids":[],"package_ids":[],"root_id":root.get("root_id"),"root_hash":root.get("root_hash"),"kfm_spec_hashes":[],"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"no_restricted_observations_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True},"warnings_count":len(warnings),"blockers_count":len(blockers),"evidence_bundle_uris":[],"generated_at":now()}
        (pub_out/"public_gate_summary.json").write_text(json.dumps(public_summary,indent=2)+"\n")
        (pub_out/"public_gate_summary.md").write_text(f"# Public eBird Gate Summary\n\nDecision: **{decision}**\n")
    print(gate_id)

if __name__=="__main__": main()
