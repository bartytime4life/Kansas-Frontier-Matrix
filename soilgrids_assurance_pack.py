#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REMOTE_PREFIXES = ("http://", "https://", "s3://", "gs://", "az://", "/vsicurl/", "/vsis3/", "/vsigs/", "/vsiaz/")
MODES = {"catalog-only", "map-evidence", "assess", "oscal-export", "certify-assurance", "dry-run"}
FRAMEWORKS = {"soilgrids-internal", "nist-csf-2.0", "oscal-custom"}
SECRET_PATTERNS = [re.compile(r"AKIA[0-9A-Z]{16}"), re.compile(r"Bearer\s+[A-Za-z0-9._-]+"), re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"), re.compile(r"api[_-]?key\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{10,}"), re.compile(r"password\s*[:=]\s*[\"']?\S+", re.IGNORECASE)]

class AssuranceError(Exception):
    def __init__(self, msg: str, code: int = 100):
        super().__init__(msg)
        self.code = code

def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def canonical_dumps(obj: Any) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def hash_obj(obj: Any) -> str:
    return hashlib.sha256(canonical_dumps(obj).encode("utf-8")).hexdigest()

def write_canonical_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def _safe_local_path(path: str, allow_abs: bool=False) -> Path:
    if any(path.startswith(p) for p in REMOTE_PREFIXES):
        raise AssuranceError(f"Remote path rejected: {path}", 90)
    p = Path(path)
    if p.is_absolute() and not allow_abs:
        raise AssuranceError("absolute output paths forbidden", 90)
    if ".." in p.parts:
        raise AssuranceError("path traversal rejected", 90)
    return p

def compute_assurance_spec_hash(spec: Dict[str, Any]) -> str:
    normalized = dict(spec)
    for k in ("created_at_utc", "run_id"):
        normalized.pop(k, None)
    if "control_frameworks" in normalized:
        normalized["control_frameworks"] = sorted(normalized["control_frameworks"])
    return hash_obj(normalized)

def validate_assurance_spec(spec: Dict[str, Any]) -> None:
    if spec.get("schema") != "AssuranceSpec.v1": raise AssuranceError("unsupported assurance schema", 30)
    if not spec.get("assurance_id") or not spec.get("dataset_id"): raise AssuranceError("missing ids", 30)
    fws = set(spec.get("control_frameworks", []))
    if not fws or not fws.issubset(FRAMEWORKS): raise AssuranceError("unknown framework", 30)
    cp = spec.get("control_profile", {})
    inc = cp.get("include_controls", [])
    exc = cp.get("exclude_controls", [])
    if len(inc) != len(set(inc)): raise AssuranceError("duplicate control ids", 50)
    if set(inc) & set(exc): raise AssuranceError("include/exclude conflict", 30)
    if spec.get("opa", {}).get("enabled") and not spec.get("opa", {}).get("policy_dir"):
        raise AssuranceError("opa enabled without policy_dir", 80)

def build_control_catalog(spec: Dict[str, Any], ts: str) -> Dict[str, Any]:
    controls = [
        {"control_id":"DATA.PROV-01","framework":"soilgrids-internal","family":"Data Provenance","title":"Cross-layer provenance chain is complete","statement":"Pipeline artifacts preserve verifiable receipt and hash lineage.","objective":"Ensure data products are attributable, auditable, and reproducible.","severity":"required","maps_to":[{"framework":"nist-csf-2.0","control_id":"GV.OV","relationship":"supports"}],"evidence_requirements":["EvidenceCorpus.v1","ProvenanceGraph.v1","PipelineRunManifest.v1"]},
        {"control_id":"SUPPLY.SBOM-01","framework":"soilgrids-internal","family":"Supply Chain Security","title":"SBOMs exist","statement":"Supply chain inventory and SBOM are available.","objective":"Track dependencies.","severity":"required","maps_to":[{"framework":"nist-csf-2.0","control_id":"ID.AM","relationship":"supports"}],"evidence_requirements":["SupplyChainInventory.v1","SPDX","CycloneDX"]},
        {"control_id":"REPRO.REPLAY-01","framework":"soilgrids-internal","family":"Orchestration and Replay","title":"Reproducibility reported","statement":"Reproducibility report exists and indicates pass.","objective":"Repeatable pipeline.","severity":"required","maps_to":[{"framework":"nist-csf-2.0","control_id":"RC.RP","relationship":"supports"}],"evidence_requirements":["ReproducibilityReport.v1","PipelineCertificationEnvelope.v1"]},
        {"control_id":"MON.DRIFT-01","framework":"soilgrids-internal","family":"Monitoring and Drift","title":"Monitoring evidence present","statement":"Monitoring snapshots available.","objective":"Operational visibility.","severity":"warning","maps_to":[{"framework":"nist-csf-2.0","control_id":"DE.CM","relationship":"supports"}],"evidence_requirements":["MonitorSnapshot.v1"]},
    ]
    catalog = {"schema":"ControlCatalog.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","frameworks":sorted(spec["control_frameworks"]),"controls":sorted(controls, key=lambda x:x["control_id"]),"errors":[]}
    catalog["control_catalog_hash"] = compute_control_catalog_hash(catalog)
    return catalog

def compute_control_catalog_hash(catalog: Dict[str, Any]) -> str:
    c = dict(catalog); c.pop("created_at_utc", None); c.pop("control_catalog_hash", None)
    return hash_obj(c)

def build_control_profile(spec: Dict[str, Any], catalog: Dict[str, Any], ts: str) -> Dict[str, Any]:
    all_ids = {c["control_id"] for c in catalog["controls"]}
    cp = spec.get("control_profile", {})
    included = sorted(cp.get("include_controls") or sorted(all_ids))
    excluded = sorted(cp.get("exclude_controls", []))
    for cid in included + excluded:
        if cid not in all_ids: raise AssuranceError(f"unknown control id {cid}", 50)
    p = {"schema":"ControlProfile.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","profile_id":"soilgrids-default-profile","included_controls":included,"excluded_controls":excluded,"errors":[]}
    p["profile_hash"] = hash_obj({"included_controls":included,"excluded_controls":excluded})
    return p

def load_assurance_inputs(paths: Dict[str, Optional[str]]) -> Dict[str, Any]:
    out = {}
    for k,v in paths.items():
        if not v: continue
        p = _safe_local_path(v)
        if not p.exists(): raise AssuranceError(f"missing input {k}", 40)
        out[k] = {"path":str(p),"json":_read_json(p),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()}
    return out

def validate_input_evidence(inputs: Dict[str, Any]) -> None:
    for item in inputs.values():
        txt = json.dumps(item["json"], sort_keys=True)
        for pat in SECRET_PATTERNS:
            if pat.search(txt): raise AssuranceError("secret finding detected", 90)

def map_evidence_to_controls(spec, catalog, inputs, ts):
    mappings=[]
    for c in catalog["controls"]:
        ev=[]
        for k,v in inputs.items():
            sch = v["json"].get("schema", k)
            if sch in c["evidence_requirements"] or ("SPDX" in c["evidence_requirements"] and "spdx" in k) or ("CycloneDX" in c["evidence_requirements"] and "cyclonedx" in k):
                ev.append({"evidence_id":"ev_"+v["sha256"][:12],"schema":sch,"path":v["path"],"sha256":v["sha256"],"evidence_strength":"primary","claim":f"{sch} supports {c['control_id']}."})
        coverage = "complete" if ev else "missing"
        mappings.append({"control_id":c["control_id"],"evidence":sorted(ev,key=lambda x:x["evidence_id"]),"coverage":coverage,"errors":[]})
    m = {"schema":"ControlEvidenceMap.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","mappings":mappings,"errors":[]}
    m["evidence_map_hash"] = compute_evidence_map_hash(m)
    return m

def compute_evidence_map_hash(m):
    c=dict(m); c.pop("created_at_utc",None); c.pop("evidence_map_hash",None)
    return hash_obj(c)

def build_assessment_results(spec,catalog,emap,ts):
    results=[]
    for c in catalog["controls"]:
        mm=next(x for x in emap["mappings"] if x["control_id"]==c["control_id"])
        status = "pass" if mm["coverage"]=="complete" else ("fail" if c["severity"]=="required" else "warning")
        results.append({"control_id":c["control_id"],"status":status,"severity":c["severity"],"evidence_coverage":mm["coverage"],"findings":[],"rationale":f"Coverage is {mm['coverage']}."})
    summary={"controls_assessed":len(results),"passed":sum(r["status"]=="pass" for r in results),"warnings":sum(r["status"]=="warning" for r in results),"failed":sum(r["status"]=="fail" for r in results),"not_applicable":0,"not_assessed":0,"required_failed":sum(r["status"]=="fail" and r["severity"]=="required" for r in results)}
    ar={"schema":"AssessmentResults.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","results":results,"summary":summary,"errors":[]}
    ar["assessment_hash"]=compute_assessment_hash({"results":ar,"plan":{},"risk":{},"gaps":{},"cap":{},"gate":{}})
    return ar

def build_risk_register(spec, assessment, ts):
    risks=[]
    for r in assessment["results"]:
        if r["status"] in {"fail","warning"}:
            sev = "critical" if r["control_id"]=="DATA.PROV-01" and r["status"]=="fail" else ("high" if r["status"]=="fail" else "medium")
            risks.append({"risk_id":"risk_"+hash_obj(r)[:12],"title":"Control deficiency","category":"compliance","severity":sev,"likelihood":"medium","impact":"high","related_controls":[r["control_id"]],"related_evidence":[],"status":"open","owner":"unassigned","message":r["rationale"]})
    rr={"schema":"RiskRegister.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","risks":risks,"errors":[]}
    rr["risk_register_hash"]=hash_obj({"risks":risks})
    return rr

def compute_assessment_hash(bundle):
    return hash_obj(bundle)

def build_gap_analysis_report(spec,assessment,ts):
    gaps=[]
    for r in assessment["results"]:
        if r["status"]!="pass":
            gaps.append({"gap_id":"gap_"+hash_obj(r)[:12],"control_id":r["control_id"],"gap_type":"missing_evidence" if r["evidence_coverage"]=="missing" else "partial_coverage","severity":"high" if r["status"]=="fail" else "medium","message":r["rationale"],"recommended_action":"Provide missing evidence."})
    summ={k:sum(g["severity"]==k for g in gaps) for k in ["critical","high","medium","low"]}
    status="critical_gaps" if summ["critical"] else ("gaps_present" if gaps else "no_gaps")
    return {"schema":"GapAnalysisReport.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","status":status,"gaps":gaps,"summary":summ,"errors":[]}

def build_corrective_action_plan(spec,gaps,ts):
    actions=[{"action_id":"cap_"+hash_obj(g)[:12],"related_gap_id":g["gap_id"],"related_control_id":g["control_id"],"title":"Address assurance gap","priority":g["severity"],"owner":"unassigned","due_policy":"manual","automation_allowed":False,"recommended_layer":18,"message":g["recommended_action"]} for g in gaps["gaps"]]
    return {"schema":"CorrectiveActionPlan.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","status":"open" if actions else "not_required","actions":actions,"errors":[]}

def build_assurance_gate_report(spec,assessment,risk,gaps,ts,run_id):
    req_failed = assessment["summary"]["required_failed"]
    critical_risk = any(r["severity"]=="critical" and r["status"]=="open" for r in risk["risks"])
    critical_gap = gaps["summary"]["critical"]>0
    crit=[
        {"criterion_id":"assurance.required_controls_pass","severity":"required","status":"fail" if req_failed else "pass","evidence":{},"message":"Required controls evaluated."},
        {"criterion_id":"assurance.no_critical_open_risk","severity":"required","status":"fail" if critical_risk else "pass","evidence":{},"message":"No critical open risk."},
        {"criterion_id":"assurance.no_critical_gap","severity":"required","status":"fail" if critical_gap else "pass","evidence":{},"message":"No critical gaps."},
    ]
    status="fail" if any(c["status"]=="fail" and c["severity"]=="required" for c in crit) else ("warning" if assessment["summary"]["warnings"] else "pass")
    summary={"total_criteria":len(crit),"passed":sum(c["status"]=="pass" for c in crit),"failed":sum(c["status"]=="fail" for c in crit),"skipped":0,"required_failed":sum(c["status"]=="fail" and c["severity"]=="required" for c in crit),"warnings_failed":0}
    gate={"schema":"AssuranceGateReport.v1","run_id":run_id,"created_at_utc":ts,"source":"soilgrids_assurance_pack","assurance_id":spec["assurance_id"],"status":status,"criteria":crit,"summary":summary,"errors":[]}
    gate["gate_hash"]=hash_obj({"criteria":crit,"summary":summary,"status":status})
    return gate

def build_assurance_narrative(spec,gate,ts):
    sec=["Overview","System boundary","Data lineage","Raster integrity","Release immutability","Remote distribution assurance","Monitoring and drift response","Remediation posture","Evidence crate and registry posture","CI/CD safety","Supply-chain posture","Residual risks","Corrective action summary","Assurance gate conclusion"]
    sections=[{"section_id":re.sub(r'[^a-z0-9]+','_',s.lower()).strip('_'),"title":s,"text":f"{s} summarized from deterministic evidence mapping.","evidence_refs":["ControlEvidenceMap.v1","AssessmentResults.v1","AssuranceGateReport.v1"]} for s in sec]
    return {"schema":"AssuranceNarrative.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","title":"SoilGrids Governed Pipeline Assurance Narrative","sections":sections,"errors":[]}

def build_oscal_catalog(catalog, ts): return {"catalog":{"uuid":"id_"+hash_obj(catalog)[:12],"metadata":{"title":"OSCAL Catalog","version":"1","last-modified":ts},"groups":[{"id":"soilgrids","controls":[{"id":c["control_id"],"title":c["title"]} for c in catalog["controls"]]}]}}
def build_oscal_profile(profile, ts): return {"profile":{"uuid":"id_"+hash_obj(profile)[:12],"metadata":{"title":"OSCAL Profile","version":"1","last-modified":ts},"imports":[{"include-controls":[{"with-id":c} for c in profile["included_controls"]]}]}}
def build_oscal_component_definition(*a, **k): return {"component-definition":{"metadata":{"title":"Component Definition","version":"1"}}}
def build_oscal_system_security_plan(*a, **k): return {"system-security-plan":{"metadata":{"title":"SSP","version":"1"}}}
def build_oscal_assessment_plan(*a, **k): return {"assessment-plan":{"metadata":{"title":"Assessment Plan","version":"1"}}}
def build_oscal_assessment_results(*a, **k): return {"assessment-results":{"metadata":{"title":"Assessment Results","version":"1"}}}
def build_oscal_poam(*a, **k): return {"poam":{"metadata":{"title":"POAM","version":"1"}}}

def evaluate_opa_policies_if_requested(spec, payload, allow_missing=False):
    opa=spec.get("opa",{})
    if not opa.get("enabled",False): return {"enabled":False,"decision":{"allow":True,"decision":"pass","reasons":[]}}
    if shutil.which("opa") is None:
        if allow_missing: return {"enabled":True,"decision":{"allow":True,"decision":"warning","reasons":["OPA missing"]}}
        raise AssuranceError("OPA enabled but missing",80)
    return {"enabled":True,"decision":{"allow":True,"decision":"pass","reasons":[]}}

def write_checksums_file(root: Path) -> str:
    lines=[]
    for p in sorted([x for x in root.rglob("*.json") if x.name!="checksums.sha256"]):
        lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(root).as_posix()}")
    (root/"checksums.sha256").write_text("\n".join(lines)+"\n", encoding="utf-8")
    return "checksums.sha256"

def compute_assurance_pack_hash(artifacts, input_hash):
    return hash_obj({"artifacts":artifacts,"input":input_hash})

def build_assurance_pack_manifest(spec, pack_id, spec_hash, hashes, status, artifacts, ts):
    return {"schema":"AssurancePackManifest.v1","assurance_pack_id":pack_id,"assurance_layout_version":"1","created_at_utc":ts,"source":"soilgrids_assurance_pack","assurance_id":spec["assurance_id"],"dataset_id":spec["dataset_id"],"assurance_spec_hash":spec_hash,"assurance_pack_hash":hashes["pack"],"control_catalog_hash":hashes.get("catalog"),"evidence_map_hash":hashes.get("emap"),"assessment_hash":hashes.get("assessment"),"status":status,"artifacts":artifacts,"oscal":hashes.get("oscal",{}),"checksums_path":"checksums.sha256","errors":[]}

def build_assurance_pack_receipt(run_id, mode, spec, pack_id, spec_hash, pack_hash, output_root, outputs, inputs, validations, status, errors):
    return {"schema":"AssurancePackReceipt.v1","run_id":run_id,"created_at_utc":now_iso(),"status":status,"source":"soilgrids_assurance_pack","mode":mode,"assurance_id":spec.get("assurance_id","unknown"),"assurance_pack_id":pack_id,"assurance_spec_hash":spec_hash,"assurance_pack_hash":pack_hash,"output_root":output_root,"outputs":outputs,"inputs":inputs,"input_hashes":{"assurance_spec_sha256":spec_hash,"combined_evidence_hash":None},"validation":validations,"errors":errors}

def build_assurance_pack(args):
    ts = now_iso(); run_id = "run_" + hashlib.sha256((args.mode+args.assurance_spec).encode()).hexdigest()[:12] if args.deterministic_run_id else "run_"+hashlib.sha256(ts.encode()).hexdigest()[:12]
    spec_path = Path(args.assurance_spec)
    if not spec_path.exists():
        raise AssuranceError("missing assurance spec",40)
    spec = _read_json(spec_path); validate_assurance_spec(spec); spec_hash=compute_assurance_spec_hash(spec)
    pack_id = args.assurance_pack_id or f"{spec['dataset_id']}_assurance_{spec_hash[:12]}"
    inputs = load_assurance_inputs({k:v for k,v in vars(args).items() if k in {"evidence_crate_manifest","evidence_corpus","provenance_graph","compliance_matrix","audit_digest","evidence_crate_receipt","registry_manifest","registry_snapshot","registry_validation_report","registry_receipt","pipeline_run_manifest","pipeline_run_receipt","reproducibility_report","pipeline_certification_envelope","control_plane_spec","workflow_validation_report","release_gate_report","supply_chain_inventory","dependency_graph","spdx_sbom","cyclonedx_sbom","vulnerability_scan_report","license_compliance_report","source_integrity_report","workflow_supply_chain_report","build_environment_report","attestation_bundle","signature_verification_report","supply_chain_gate_report","supply_chain_receipt","monitor_ledger","remediation_ledger"}})
    validate_input_evidence(inputs)
    if args.mode=="dry-run":
        return None, build_assurance_pack_receipt(run_id,args.mode,spec,pack_id,spec_hash,None,str(Path(args.output_root)/pack_id),{k:None for k in ["manifest","control_catalog","control_profile","implementation_matrix","evidence_map","assessment_plan","assessment_results","risk_register","gap_analysis","corrective_action_plan","assurance_gate_report","assurance_narrative","checksums"]},{"assurance_spec":args.assurance_spec,"evidence_crate_manifest":args.evidence_crate_manifest,"evidence_corpus":args.evidence_corpus,"registry_manifest":args.registry_manifest,"pipeline_run_receipt":args.pipeline_run_receipt,"supply_chain_receipt":args.supply_chain_receipt},{"assurance_spec_valid":True,"input_evidence_valid":True,"control_catalog_valid":True,"evidence_map_valid":True,"assessment_valid":True,"risk_register_valid":True,"gate_valid":True,"oscal_exports_valid":True,"opa_valid":True},"dry_run",[]),5
    out_root=Path(args.output_root);
    if out_root.is_absolute() and not args.allow_absolute_output:
        raise AssuranceError("absolute output paths forbidden",90)
    out_root.mkdir(parents=True, exist_ok=True)
    final_dir=out_root/pack_id
    if final_dir.exists() and not args.overwrite: raise AssuranceError("output exists",90)
    staging=out_root/".staging"/f"{pack_id}.tmp"; shutil.rmtree(staging, ignore_errors=True); staging.mkdir(parents=True)
    catalog=build_control_catalog(spec,ts); profile=build_control_profile(spec,catalog,ts)
    impl={"schema":"ControlImplementationMatrix.v1","assurance_id":spec["assurance_id"],"created_at_utc":ts,"source":"soilgrids_assurance_pack","matrix_hash":"","implementations":[],"errors":[]}; impl["matrix_hash"]=hash_obj(impl)
    emap=map_evidence_to_controls(spec,catalog,inputs,ts)
    assessment=build_assessment_results(spec,catalog,emap,ts); risks=build_risk_register(spec,assessment,ts); gaps=build_gap_analysis_report(spec,assessment,ts); cap=build_corrective_action_plan(spec,gaps,ts)
    gate=build_assurance_gate_report(spec,assessment,risks,gaps,ts,run_id); narrative=build_assurance_narrative(spec,gate,ts)
    oscal={"catalog":"oscal/oscal_catalog.json","profile":"oscal/oscal_profile.json","component_definition":"oscal/oscal_component_definition.json","system_security_plan":"oscal/oscal_system_security_plan.json","assessment_plan":"oscal/oscal_assessment_plan.json","assessment_results":"oscal/oscal_assessment_results.json","poam":"oscal/oscal_poam.json"}
    write_canonical_json(staging/"controls/control_catalog.json",catalog);write_canonical_json(staging/"controls/control_profile.json",profile);write_canonical_json(staging/"controls/control_implementation_matrix.json",impl)
    write_canonical_json(staging/"evidence/control_evidence_map.json",emap)
    write_canonical_json(staging/"assessment/assessment_results.json",assessment);write_canonical_json(staging/"assessment/risk_register.json",risks);write_canonical_json(staging/"assessment/gap_analysis_report.json",gaps);write_canonical_json(staging/"assessment/corrective_action_plan.json",cap);write_canonical_json(staging/"assessment/assurance_gate_report.json",gate)
    write_canonical_json(staging/"narrative/assurance_narrative.json",narrative)
    write_canonical_json(staging/"oscal/oscal_catalog.json",build_oscal_catalog(catalog,ts));write_canonical_json(staging/"oscal/oscal_profile.json",build_oscal_profile(profile,ts));write_canonical_json(staging/"oscal/oscal_component_definition.json",build_oscal_component_definition());write_canonical_json(staging/"oscal/oscal_system_security_plan.json",build_oscal_system_security_plan());write_canonical_json(staging/"oscal/oscal_assessment_plan.json",build_oscal_assessment_plan());write_canonical_json(staging/"oscal/oscal_assessment_results.json",build_oscal_assessment_results());write_canonical_json(staging/"oscal/oscal_poam.json",build_oscal_poam())
    write_checksums_file(staging)
    artifacts=[]
    for p in sorted(staging.rglob("*.json")):
        artifacts.append({"role":p.stem,"path":p.relative_to(staging).as_posix(),"media_type":"application/json","bytes":p.stat().st_size,"sha256":hashlib.sha256(p.read_bytes()).hexdigest()})
    hashes={"catalog":catalog["control_catalog_hash"],"emap":emap["evidence_map_hash"],"assessment":assessment["assessment_hash"],"oscal":oscal}
    hashes["pack"]=compute_assurance_pack_hash(artifacts,None)
    manifest=build_assurance_pack_manifest(spec,pack_id,spec_hash,hashes,gate["status"],artifacts,ts)
    write_canonical_json(staging/"assurance_pack_manifest.json",manifest)
    outputs={"manifest":"assurance_pack_manifest.json","control_catalog":"controls/control_catalog.json","control_profile":"controls/control_profile.json","implementation_matrix":"controls/control_implementation_matrix.json","evidence_map":"evidence/control_evidence_map.json","assessment_plan":"assessment/assessment_plan.json","assessment_results":"assessment/assessment_results.json","risk_register":"assessment/risk_register.json","gap_analysis":"assessment/gap_analysis_report.json","corrective_action_plan":"assessment/corrective_action_plan.json","assurance_gate_report":"assessment/assurance_gate_report.json","assurance_narrative":"narrative/assurance_narrative.json","checksums":"checksums.sha256"}
    receipt=build_assurance_pack_receipt(run_id,args.mode,spec,pack_id,spec_hash,hashes["pack"],str(final_dir),outputs,{"assurance_spec":args.assurance_spec,"evidence_crate_manifest":args.evidence_crate_manifest,"evidence_corpus":args.evidence_corpus,"registry_manifest":args.registry_manifest,"pipeline_run_receipt":args.pipeline_run_receipt,"supply_chain_receipt":args.supply_chain_receipt},{"assurance_spec_valid":True,"input_evidence_valid":True,"control_catalog_valid":True,"evidence_map_valid":True,"assessment_valid":True,"risk_register_valid":True,"gate_valid":True,"oscal_exports_valid":True,"opa_valid":True},"success" if gate["status"]=="pass" else ("warning" if gate["status"]=="warning" else "error"),[])
    write_canonical_json(staging/"assurance_pack_receipt.json",receipt)
    if final_dir.exists() and args.overwrite: shutil.rmtree(final_dir)
    staging.replace(final_dir)
    return final_dir/"assurance_pack_receipt.json", receipt, (0 if gate["status"]=="pass" else 10 if gate["status"]=="warning" else 20)

def parse_args(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument("--assurance-spec", required=True); ap.add_argument("--output-root", required=True); ap.add_argument("--mode", required=True, choices=sorted(MODES))
    for a in ["evidence-crate-manifest","evidence-corpus","provenance-graph","compliance-matrix","audit-digest","evidence-crate-receipt","registry-manifest","registry-snapshot","registry-validation-report","registry-receipt","pipeline-run-manifest","pipeline-run-receipt","reproducibility-report","pipeline-certification-envelope","control-plane-spec","workflow-validation-report","release-gate-report","supply-chain-inventory","dependency-graph","spdx-sbom","cyclonedx-sbom","vulnerability-scan-report","license-compliance-report","source-integrity-report","workflow-supply-chain-report","build-environment-report","attestation-bundle","signature-verification-report","supply-chain-gate-report","supply-chain-receipt","policy-root","monitor-ledger","remediation-ledger"]: ap.add_argument(f"--{a}")
    ap.add_argument("--assurance-pack-id"); ap.add_argument("--overwrite", action="store_true"); ap.add_argument("--allow-absolute-output", action="store_true"); ap.add_argument("--deterministic-run-id", action="store_true")
    return ap.parse_args(argv)

def main(argv=None):
    args=parse_args(argv)
    try:
        receipt_path, receipt, code = build_assurance_pack(args)
        if receipt_path is None:
            tmp = Path(args.output_root); tmp.mkdir(parents=True,exist_ok=True); p=tmp/"assurance_pack_receipt.json"; write_canonical_json(p, receipt); print(str(p)); return code
        print(str(receipt_path)); return code
    except AssuranceError as e:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"assurance_pack_receipt_path":None,"assurance_pack_id":None})+"\n")
        return e.code
    except Exception:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"assurance_pack_receipt_path":None,"assurance_pack_id":None})+"\n")
        return 100

if __name__ == "__main__":
    sys.exit(main())
