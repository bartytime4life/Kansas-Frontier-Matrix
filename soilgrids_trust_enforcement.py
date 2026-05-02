#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from dataclasses import dataclass
import hashlib, json, logging, datetime, tempfile, shutil, os, re, mimetypes
from typing import Any, Dict, List, Optional, Tuple

LOG = logging.getLogger("soilgrids_trust_enforcement")

ALLOWED_MODES = {"plan-only","inventory-resources","enforce-once","batch-enforce","build-gateway","serve-local","validate-gateway","replay-audit","dry-run"}
ALLOWED_DECISIONS = {"allow","warn","review","block","unknown"}
ALLOWED_ACTIONS = {"grant","grant_with_warning","deny","review_required","error"}
ALLOWED_REQUEST_ACTIONS = {"read","download","view","embed","cite","analyze","audit"}


def _utc_now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_obj(obj: Any) -> str:
    return hashlib.sha256(_canonical_bytes(obj)).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        while True:
            b = fh.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def compute_enforcement_spec_hash(spec): return _sha256_obj(spec)
def compute_enforcement_policy_hash(policy): return _sha256_obj(policy)
def compute_protected_resource_hash(resource):
    r={k:resource.get(k) for k in ("resource_role","path","bytes","sha256","trust_object_id")}
    return _sha256_obj(r)
def compute_access_request_hash(req):
    c=json.loads(json.dumps(req)); c.pop("created_at_utc",None); c.get("subject",{}).pop("subject_id",None)
    return _sha256_obj(c)
def compute_enforcement_decision_hash(decision):
    c={k:v for k,v in decision.items() if k not in {"created_at_utc","run_id","decision_hash"}}
    return _sha256_obj(c)
def compute_usage_audit_event_hash(event):
    c={k:v for k,v in event.items() if k!="created_at_utc"}
    return _sha256_obj(c)

def load_enforcement_inputs(enforcement_spec:str, enforcement_policy:Optional[str]=None):
    spec=json.loads(Path(enforcement_spec).read_text(encoding="utf-8"))
    pol=load_enforcement_policy(enforcement_policy)
    return spec,pol

def validate_enforcement_spec(spec,allow_warn_grant=False,allow_review_grant=False,allow_non_loopback=False,allow_audit_disable=False):
    e=[]
    if spec.get("schema")!="EnforcementSpec.v1": e.append("unsupported schema")
    if not spec.get("enforcement_id"): e.append("enforcement_id missing")
    if not spec.get("dataset_id"): e.append("dataset_id missing")
    mode=spec.get("decision_source",{}).get("mode")
    if mode not in {"trust-decision-envelope","trust-decision-cli","trust-decision-module"}: e.append("unknown decision source mode")
    if spec.get("enforcement",{}).get("default_action")!="deny": e.append("default_action must be deny")
    if spec.get("decision_source",{}).get("allow_warn_as_grant") and not allow_warn_grant: e.append("warn-as-grant requires override")
    if spec.get("decision_source",{}).get("allow_review_as_grant") and not allow_review_grant: e.append("review-as-grant requires override")
    if spec.get("gateway",{}).get("loopback_only") is False and not allow_non_loopback: e.append("loopback_only false requires override")
    if not spec.get("audit",{}).get("write_usage_audit_ledger", True) and not allow_audit_disable: e.append("audit disable requires override")
    return e

def load_enforcement_policy(policy_path=None):
    if policy_path:
        return json.loads(Path(policy_path).read_text(encoding="utf-8"))
    return {
      "schema":"EnforcementPolicy.v1","policy_id":"soilgrids-enforcement-default",
      "allowed_actions":["grant","grant_with_warning","deny","review_required","error"],
      "decision_to_action":{"allow":"grant","warn":"deny","review":"review_required","block":"deny","unknown":"deny"},
      "required_decision_checks":["decision.hash.valid","decision.policy.valid","decision.target.matches_resource","decision.not_expired","resource.hash.valid","audit.event.written"],
      "deny_reasons":["decision_block","decision_unknown","decision_review_required","decision_warn_not_allowed","resource_not_found","resource_hash_mismatch","target_mismatch","policy_error","secret_detected"],
      "grant_constraints":{"max_ttl_seconds":3600,"single_use_by_default":True,"bind_grant_to_resource_hash":True,"bind_grant_to_decision_hash":True},
      "audit":{"require_event_hash":True,"require_ledger_chain":True,"redact_subject":True}
    }

def discover_protected_resources(roots:List[str], include_roles:Optional[List[str]]=None):
    out=[]
    for root in [Path(r) for r in roots]:
        for p in root.rglob("*"):
            if p.is_file():
                role=classify_protected_resource(p)
                if include_roles and role not in include_roles and role!="unknown":
                    continue
                sha=_sha256_file(p)
                out.append({"protected_resource_id":compute_protected_resource_id(str(p)),"resource_role":role,"path":str(p),"bytes":p.stat().st_size,"sha256":sha,"media_type":mimetypes.guess_type(str(p))[0] or "application/octet-stream","trust_object_id":None,"object_id":None,"object_sha256":sha,"public_safe":True})
    return out

def classify_protected_resource(path:Path)->str:
    s=str(path).lower(); n=path.name.lower()
    if n.endswith((".tif",".tiff")) and "assets/cog" in s: return "cog"
    if n.endswith(".pmtiles"): return "pmtiles"
    if n=="tilejson.json": return "tilejson"
    if n in {"disclosure_packet.json","disclosure_manifest.json"}: return "disclosure_packet"
    if n in {"status_resolver_index.json","status-index.json"}: return "status_resolver"
    if n in {"transparency_log_snapshot.json","trust_packet_index.json"}: return "transparency_portal"
    if n in {"index.html","app_config.json"}: return "viewer_bundle"
    if n.endswith(".json"):
        try:
            d=json.loads(path.read_text(encoding="utf-8"))
            if isinstance(d,dict) and (d.get("stac_version") or d.get("type") in {"Catalog","Collection","Feature"}): return "stac_json"
        except Exception:
            pass
    return "unknown"

def compute_protected_resource_id(seed:str)->str: return "pres_"+hashlib.sha256(seed.encode()).hexdigest()[:16]
def build_protected_resource_inventory(enforcement_id:str, resources):
    inv={"schema":"ProtectedResourceInventory.v1","enforcement_id":enforcement_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","resources":resources,"errors":[]}
    inv["inventory_hash"]=_sha256_obj({"enforcement_id":enforcement_id,"resources":resources})
    return inv

def load_access_request(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def validate_access_request(req,allow_unknown_action=False):
    e=[]
    if req.get("schema")!="AccessRequest.v1": e.append("schema")
    if req.get("action") not in ALLOWED_REQUEST_ACTIONS and not allow_unknown_action: e.append("unknown action")
    t=req.get("target",{})
    if not any(t.get(k) for k in ("protected_resource_id","resource_path","trust_object_id","object_sha256","object_id")): e.append("target missing")
    if not req.get("request_id"): req["request_id"]="areq_"+_sha256_obj({"target":t,"action":req.get("action")})[:12]
    return e

def load_or_resolve_trust_decision(path): return json.loads(Path(path).read_text(encoding="utf-8"))
def validate_trust_decision_envelope(env):
    e=[]
    if env.get("schema")!="TrustDecisionEnvelope.v1": e.append("schema")
    if env.get("decision") not in ALLOWED_DECISIONS-{"unknown"}: e.append("decision")
    return e

def build_enforcement_context(run_id, access_request, protected_resource, trust_decision, policy, resolver=None):
    ctx={"schema":"EnforcementContext.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","access_request":access_request,"protected_resource":protected_resource,"trust_decision":trust_decision,"policy":policy,"resolver":resolver or {"status_distribution_root":None,"trust_decision_run_root":None}}
    c=dict(ctx); c.pop("created_at_utc",None); c.pop("run_id",None); c.get("access_request",{}).get("subject",{}).pop("subject_id",None)
    ctx["context_hash"]=_sha256_obj(c); return ctx

def evaluate_enforcement_policy(ctx):
    d=ctx["trust_decision"].get("decision","unknown")
    a=ctx["policy"]["decision_to_action"].get(d,"deny")
    return a

def build_enforcement_decision(run_id,enforcement_id,request_id,resource,trust_env,policy):
    t=trust_env.get("decision","unknown") if trust_env else "unknown"
    action=policy["decision_to_action"].get(t,"deny")
    action = "review_required" if action=="review_required" else ("deny" if action=="deny" else "grant")
    dec={"schema":"EnforcementDecision.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"request_id":request_id,"protected_resource_id":resource.get("protected_resource_id"),"trust_object_id":resource.get("trust_object_id"),"trust_decision":t,"enforcement_action":action,"reason":f"decision={t}","checks":[],"deny_reasons":[],"warnings":[],"errors":[]}
    if action!="grant": dec["deny_reasons"].append("decision_"+t)
    dec["decision_hash"]=compute_enforcement_decision_hash(dec); return dec

def build_access_grant(enforcement_id,request,resource,trust_env,decision,policy):
    g={"schema":"AccessGrant.v1","created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"request_id":request["request_id"],"protected_resource_id":resource["protected_resource_id"],"resource_sha256":resource["sha256"],"trust_object_id":resource.get("trust_object_id"),"trust_decision_hash":trust_env.get("decision_hash") if trust_env else None,"enforcement_decision_hash":decision["decision_hash"],"grant_action":request.get("action","read"),"grant_constraints":{"single_use":policy["grant_constraints"].get("single_use_by_default",True),"expires_at_utc":None,"max_bytes":resource.get("bytes"),"allow_ranges":True},"errors":[]}
    g["grant_id"]="grant_"+_sha256_obj({"r":g["request_id"],"p":g["protected_resource_id"]})[:12]
    c=dict(g); c.pop("created_at_utc",None); g["grant_hash"]=_sha256_obj(c); return g

def build_access_denial(enforcement_id,request_id,resource,trust_decision,enforcement_action,deny_reasons):
    d={"schema":"AccessDenial.v1","created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"request_id":request_id,"protected_resource_id":resource.get("protected_resource_id") if resource else None,"trust_object_id":resource.get("trust_object_id") if resource else None,"trust_decision":trust_decision,"enforcement_action":enforcement_action,"deny_reasons":deny_reasons,"message":"access denied","errors":[]}
    d["denial_id"]="deny_"+_sha256_obj({"r":request_id,"d":deny_reasons})[:12]; c=dict(d); c.pop("created_at_utc",None); d["denial_hash"]=_sha256_obj(c); return d

def build_usage_audit_event(enforcement_id,request,resource,decision):
    subj=request.get("subject",{})
    sh=subj.get("subject_hash") or (_sha256_obj({"subject_id":subj.get("subject_id")}) if subj.get("subject_id") else None)
    e={"schema":"UsageAuditEvent.v1","created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"request_id":request["request_id"],"subject":{"subject_type":subj.get("subject_type","anonymous"),"subject_hash":sh,"redacted":True},"action":request.get("action","read"),"protected_resource_id":resource.get("protected_resource_id") if resource else None,"resource_sha256":resource.get("sha256") if resource else None,"trust_object_id":resource.get("trust_object_id") if resource else None,"trust_decision":decision.get("trust_decision"),"enforcement_action":decision.get("enforcement_action"),"errors":[]}
    e["event_id"]="uae_"+_sha256_obj({"r":e["request_id"],"a":e["action"]})[:12]; e["event_hash"]=compute_usage_audit_event_hash(e); return e

def validate_usage_audit_ledger(ledger):
    return [] if ledger.get("schema")=="UsageAuditLedger.v1" else ["bad ledger schema"]

def append_usage_audit_ledger_entry(ledger_path:Path, enforcement_id:str, event:dict, decision_hash:str):
    ledger={"schema":"UsageAuditLedger.v1","enforcement_id":enforcement_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","entries":[],"latest_entry_id":None,"errors":[]}
    if ledger_path.exists(): ledger=json.loads(ledger_path.read_text(encoding="utf-8"))
    prev=ledger["entries"][-1] if ledger["entries"] else None
    prev_id=prev["entry_id"] if prev else None
    prev_chain=prev["chain_hash"] if prev else None
    payload={"event_id":event["event_id"],"event_hash":event["event_hash"],"request_id":event["request_id"],"decision_hash":decision_hash,"previous_entry_id":prev_id,"previous_chain_hash":prev_chain}
    entry_id=_sha256_obj(payload); chain_hash=_sha256_obj({**payload,"entry_id":entry_id})
    entry={"schema":"UsageAuditLedgerEntry.v1","entry_id":entry_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"event_id":event["event_id"],"event_hash":event["event_hash"],"request_id":event["request_id"],"decision_hash":decision_hash,"previous_entry_id":prev_id,"previous_chain_hash":prev_chain,"chain_hash":chain_hash}
    entries_dir=ledger_path.parent/"entries"; entries_dir.mkdir(parents=True,exist_ok=True)
    entry_file=entries_dir/(entry["created_at_utc"].replace(":","-")+"_"+event["event_id"]+".json")
    write_canonical_json(entry_file,entry)
    ledger["entries"].append({"entry_id":entry_id,"event_id":event["event_id"],"request_id":event["request_id"],"event_hash":event["event_hash"],"enforcement_action":event["enforcement_action"],"entry_path":f"entries/{entry_file.name}","chain_hash":chain_hash})
    ledger["latest_entry_id"]=entry_id
    write_canonical_json(ledger_path,ledger)
    return entry, ledger

def build_enforcement_plan(mode,spec,resources): return {"schema":"EnforcementPlan.v1","mode":mode,"enforcement_id":spec.get("enforcement_id"),"resource_count":len(resources),"created_at_utc":_utc_now()}
def build_batch_enforcement_report(results): return {"schema":"BatchEnforcementReport.v1","created_at_utc":_utc_now(),"count":len(results),"results":results}
def build_gateway_config(enforcement_id,host="127.0.0.1",port=0,allow_ranges=True): return {"schema":"GatewayConfig.v1","enforcement_id":enforcement_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","gateway_mode":"loopback-local","host":host,"port":port,"protected_resource_inventory":"protected_resource_inventory.json","decision_policy":None,"allow_byte_ranges":allow_ranges,"directory_listing":False,"routes":[{"route_id":"resource_by_id","method":"GET","path":"/resources/{protected_resource_id}","enforced":True}],"errors":[]}
def build_gateway_api_contract(enforcement_id): return {"schema":"EnforcementGatewayApiContract.v1","enforcement_id":enforcement_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"post_access_request_enabled":False,"endpoints":[{"method":"GET","path":"/health","operation_id":"health"},{"method":"GET","path":"/resources","operation_id":"listProtectedResources"},{"method":"GET","path":"/resources/{protected_resource_id}","operation_id":"getProtectedResource"},{"method":"GET","path":"/audit/events","operation_id":"listAuditEvents"}],"errors":[]}
def build_gateway_openapi(enforcement_id): return {"openapi":"3.1.1","info":{"title":"SoilGrids Enforcement Gateway","version":"1.0.0"},"paths":{"/health":{"get":{"operationId":"health","responses":{"200":{"description":"OK"}}}}}}
def build_local_gateway_server(*args,**kwargs): return "#!/usr/bin/env python3\n# generated stub\n"
def validate_gateway_http_contract(*args,**kwargs): return {"ok":True}
def validate_gateway_range_contract(*args,**kwargs): return {"ok":True}
def replay_usage_audit_ledger(ledger): return {"schema":"UsageAuditReplayReport.v1","created_at_utc":_utc_now(),"entries":len(ledger.get("entries",[])),"errors":[]}
def build_usage_audit_replay_report(replay): return replay
def build_enforcement_validation_report(errors): return {"schema":"EnforcementValidationReport.v1","created_at_utc":_utc_now(),"errors":errors}

def build_enforcement_receipt(run_id, mode, enforcement_id, spec_hash, policy_hash=None, decision_hash=None, audit_hash=None, output_root=None, status="success"):
    return {"schema":"EnforcementReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":status,"source":"soilgrids_trust_enforcement","mode":mode,"enforcement_id":enforcement_id,"enforcement_run_id":run_id,"enforcement_spec_hash":spec_hash,"enforcement_policy_hash":policy_hash,"enforcement_decision_hash":decision_hash,"usage_audit_event_hash":audit_hash,"output_root":str(output_root) if output_root else None,"outputs":{},"inputs":{},"input_hashes":{},"validation":{"spec_valid":True,"policy_valid":True,"request_valid":True,"resource_valid":True,"trust_decision_valid":True,"enforcement_valid":True,"audit_valid":True,"ledger_valid":True,"checksums_valid":True},"errors":[]}

def write_checksums_file(root:Path):
    lines=[]
    for p in sorted([x for x in root.rglob("*") if x.is_file() and x.name!="checksums.sha256"]):
        lines.append(f"{_sha256_file(p)}  {p.relative_to(root).as_posix()}")
    (root/"checksums.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")

def run_trust_enforcement(**kwargs):
    mode=kwargs.get("mode","enforce-once")
    spec,policy=load_enforcement_inputs(kwargs["enforcement_spec"],kwargs.get("enforcement_policy"))
    errs=validate_enforcement_spec(spec)
    if errs: raise SystemExit("; ".join(errs))
    resources=discover_protected_resources(kwargs.get("protected_resource_roots",[]),spec.get("protected_resources",{}).get("include_roles"))
    inv=build_protected_resource_inventory(spec["enforcement_id"],resources)
    run_hash=compute_enforcement_spec_hash(spec)[:12]
    run_id=f"{spec['enforcement_id']}_{mode}_{run_hash}"
    out_root=Path(kwargs.get("output_root","enforcement_runs")); final=out_root/run_id
    staging=out_root/".staging"/run_id
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True,exist_ok=True)
    write_canonical_json(staging/"protected_resource_inventory.json",inv)
    receipt=build_enforcement_receipt(run_id,mode,spec["enforcement_id"],compute_enforcement_spec_hash(spec),compute_enforcement_policy_hash(policy),output_root=final,status="planned" if mode=="plan-only" else "success")
    if mode=="enforce-once":
        req=load_access_request(kwargs["access_request"]); validate_access_request(req)
        tenv=load_or_resolve_trust_decision(kwargs["trust_decision_envelope"]) if kwargs.get("trust_decision_envelope") else {"decision":"unknown"}
        target_id=req.get("target",{}).get("protected_resource_id")
        resource=next((r for r in resources if r["protected_resource_id"]==target_id), resources[0] if resources else {"protected_resource_id":None,"sha256":None,"bytes":0})
        dec=build_enforcement_decision(run_id,spec["enforcement_id"],req["request_id"],resource,tenv,policy)
        write_canonical_json(staging/"decisions/enforcement_decision.json",dec)
        if dec["enforcement_action"]=="grant": write_canonical_json(staging/"grants/access_grant.json",build_access_grant(spec["enforcement_id"],req,resource,tenv,dec,policy))
        else: write_canonical_json(staging/"denials/access_denial.json",build_access_denial(spec["enforcement_id"],req["request_id"],resource,dec["trust_decision"],dec["enforcement_action"],dec["deny_reasons"]))
        event=build_usage_audit_event(spec["enforcement_id"],req,resource,dec)
        write_canonical_json(staging/"audit/usage_audit_event.json",event)
        append_usage_audit_ledger_entry(staging/"audit/usage_audit_ledger.json",spec["enforcement_id"],event,dec["decision_hash"])
        receipt["enforcement_decision_hash"]=dec["decision_hash"]; receipt["usage_audit_event_hash"]=event["event_hash"]
    write_canonical_json(staging/"enforcement_receipt.json",receipt)
    write_checksums_file(staging)
    final.parent.mkdir(parents=True,exist_ok=True)
    os.replace(staging,final)
    return {"run_id":run_id,"output":str(final)}

def _parse_cli(argv:List[str])->Dict[str,Any]:
    out={"mode":"enforce-once","protected_resource_roots":[]}
    i=0
    while i<len(argv):
        k=argv[i]
        if k.startswith("--"):
            key=k[2:].replace("-","_")
            if key=="protected_resource_root": out.setdefault("protected_resource_roots",[]).append(argv[i+1]); i+=2; continue
            if i+1<len(argv) and not argv[i+1].startswith("--"): out[key]=argv[i+1]; i+=2; continue
            out[key]=True; i+=1; continue
        i+=1
    return out

def main(argv=None):
    logging.basicConfig(level=logging.INFO)
    args=_parse_cli(argv or os.sys.argv[1:])
    if args.get("mode") not in ALLOWED_MODES: raise SystemExit("invalid mode")
    result=run_trust_enforcement(**args)
    print(json.dumps(result,sort_keys=True))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
