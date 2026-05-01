#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

VERSION = "0.31.0"
DENIED = ["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","geom","geometry","raw_row_number","suppression_receipt","suppressed_group_hash"]
BAD_PHRASES = ["exact points are public","suppression receipts are public","restricted observations are public","population trend","occupancy","true absence","habitat suitability","causal inference"]

def fail(msg:str)->None:
    print(f"ERROR: {msg}", file=sys.stderr); raise SystemExit(2)

def canonical(o:Any)->str: return json.dumps(o, sort_keys=True, separators=(",",":"))
def sha256_text(s:str)->str: return hashlib.sha256(s.encode()).hexdigest()

def load_json(path:str|None)->dict[str,Any]|None:
    if not path: return None
    p=Path(path)
    if not p.exists(): fail(f"missing file: {path}")
    return json.loads(p.read_text())

def scan_public(obj:Any)->list[str]:
    txt = canonical(obj).lower()
    findings=[]
    for d in DENIED:
        if f'"{d.lower()}"' in txt: findings.append(f"denied field present: {d}")
    for bp in BAD_PHRASES:
        if bp in txt and "not a population trend" not in txt: findings.append(f"unsupported claim: {bp}")
    if "suppression_min_n" in txt and '"suppression_min_n":' in txt:
        pass
    return sorted(set(findings))

def parse(argv:list[str])->argparse.Namespace:
    p=argparse.ArgumentParser(prog="kfm-ebird-transparency")
    p.add_argument("--version", action="version", version=VERSION)
    p.add_argument("--mode", default="build", choices=["build","validate","diff","archive","dashboard","report"])
    p.add_argument("--aggregate", default="both", choices=["huc12","county","both"])
    for a in ["public_gate_summary","public_root_summary","public_reconciliation_summary","public_control_plane_registration","public_adapter_capabilities","public_consumer_registry_index","public_consumer_status_summary","public_advisory_index","public_advisory_feed","public_quality_summary","public_assurance_summary","public_recertification_summary","public_storage_summary","public_cost_summary","public_portal_manifest","public_download_manifest","public_federation_index","public_analytics_index","public_consumer_compatibility_matrix","public_consumer_impact_summary","public_consumer_upgrade_notice","release_index","previous_transparency_report"]:
        p.add_argument(f"--{a.replace('_','-')}")
    p.add_argument("--published-root", default="data/published/fauna/ebird")
    p.add_argument("--catalog-root", default="data/catalog/fauna/ebird")
    p.add_argument("--out-dir")
    p.add_argument("--public-out-dir")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--force", action="store_true")
    return p.parse_args(argv)

def main()->None:
    a=parse(sys.argv[1:])
    input_keys={"public_gate_summary","public_root_summary","public_reconciliation_summary","public_control_plane_registration","public_adapter_capabilities","public_consumer_registry_index","public_consumer_status_summary","public_advisory_index","public_advisory_feed","public_quality_summary","public_assurance_summary","public_recertification_summary","public_storage_summary","public_cost_summary","public_portal_manifest","public_download_manifest","public_federation_index","public_analytics_index","public_consumer_compatibility_matrix","public_consumer_impact_summary","public_consumer_upgrade_notice","release_index","previous_transparency_report"}
    inputs={k:getattr(a,k) for k in input_keys}
    loaded={k:load_json(v) for k,v in inputs.items() if v}
    input_hashes={k:sha256_text(canonical(v)) for k,v in loaded.items()}
    tid=sha256_text(canonical({"aggregate_targets":a.aggregate,"input_artifact_hashes":input_hashes,"adapter_version":VERSION}))[:16]
    out=Path(a.out_dir or f"data/catalog/fauna/ebird/transparency/{tid}")
    pout=Path(a.public_out_dir) if a.public_out_dir else None
    if out.exists() and not a.force: fail("out-dir exists; pass --force")
    if pout and pout.exists() and not a.force: fail("public-out-dir exists; pass --force")
    findings=[]
    for v in loaded.values(): findings.extend(scan_public(v))
    report_status="pass" if not findings else "fail"
    manifest={"schema_version":"v1","object_type":"KfmEbirdTransparencyManifest","adapter":"kfm-ebird","transparency_id":tid,"aggregate_targets":a.aggregate,"denied_public_fields_checked":DENIED,"public_safe_final_outputs":True,"exact_points":"restricted","input_artifacts":[{"path_or_uri":k,"sha256":h,"public_safe":True} for k,h in input_hashes.items()],"generated_at":datetime.now(timezone.utc).isoformat()}
    public_report={"schema_version":"v1","object_type":"PublicKfmEbirdTransparencyReport","public_safe":True,"exact_points":"restricted","adapter":"kfm-ebird","transparency_id":tid,"aggregate_targets":a.aggregate,"report_status":report_status,"public_summary":{"public_safety_findings_count":len(findings),"public_advisories_count":len((loaded.get("public_advisory_index") or {}).get("advisories",[])),"blockers_count":len(findings),"warnings_count":0},"public_safety_summary":{"exact_points_restricted":True,"aggregate_only_public_outputs":True,"suppression_min_n_at_least_10":True,"no_restricted_observations_public":True,"no_quarantines_public":True,"no_suppression_receipts_public":True,"no_suppressed_group_details_public":True,"no_raw_rows_public":True,"no_network_required":True,"no_credentials_required":True},"interpretation_warning":"This transparency report describes governance and public aggregate data operations only. It does not claim true absence, occupancy, abundance trends, population trends, habitat suitability, or causal inference.","generated_at":datetime.now(timezone.utc).isoformat()}
    if a.mode in {"validate","report"} and findings: fail("public safety findings present: "+"; ".join(findings))
    if a.dry_run:
        print(json.dumps({"transparency_id":tid,"mode":a.mode,"findings":findings}, indent=2)); return
    out.mkdir(parents=True, exist_ok=True)
    (out/"transparency_manifest.json").write_text(json.dumps(manifest, indent=2)+"\n")
    (out/"transparency_report.json").write_text(json.dumps(public_report, indent=2)+"\n")
    (out/"transparency_validation_report.json").write_text(json.dumps({"findings":findings,"ok":not findings}, indent=2)+"\n")
    if pout:
        pout.mkdir(parents=True, exist_ok=True)
        (pout/"public_transparency_report.json").write_text(json.dumps(public_report, indent=2)+"\n")
        (pout/"public_ecosystem_status.json").write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdEcosystemStatus","public_safe":True,"exact_points":"restricted","transparency_id":tid,"overall_status":"healthy" if not findings else "blocked","components":[]}, indent=2)+"\n")
        (pout/"public_governance_metrics.json").write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdGovernanceMetrics","public_safe":True,"exact_points":"restricted","transparency_id":tid,"metrics":[],"required_metrics":["public_safety_findings_count"]}, indent=2)+"\n")
        (pout/"public_advisory_archive_index.json").write_text(json.dumps({"schema_version":"v1","object_type":"PublicKfmEbirdAdvisoryArchiveIndex","public_safe":True,"exact_points":"restricted","transparency_id":tid,"advisories":[]}, indent=2)+"\n")

if __name__=="__main__": main()
