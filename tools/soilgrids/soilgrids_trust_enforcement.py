#!/usr/bin/env python3
from __future__ import annotations
import datetime, hashlib, json, mimetypes, os, re, shutil
from pathlib import Path
from typing import Any, Dict, List

EXIT={"ok":0,"dry":5,"warn":10,"review":15,"deny":20,"malformed":30,"resource":40,"decision":50,"policy":60,"audit":70,"gateway":80,"unsafe":90,"secret":100,"internal":110}
ALLOWED_DECISIONS={"allow","warn","review","block","unknown"}
ALLOWED_REQUEST_ACTIONS={"read","download","view","embed","cite","analyze","audit"}
ALLOWED_SUBJECT_TYPES={"human","service","job","anonymous"}


def _utc_now()->str: return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def _canon(o:Any)->bytes: return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def _sha_obj(o:Any)->str: return hashlib.sha256(_canon(o)).hexdigest()
def _sha_file(p:Path)->str:
    h=hashlib.sha256();
    with p.open("rb") as f:
        while True:
            b=f.read(1024*1024)
            if not b: break
            h.update(b)
    return h.hexdigest()

def write_json(p:Path,o:Any): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n",encoding="utf-8")
def read_json(p:str|Path)->dict: return json.loads(Path(p).read_text(encoding="utf-8"))

def classify_protected_resource(path:Path)->str:
    n=path.name.lower()
    if n.endswith((".tif",".tiff")): return "cog"
    if n.endswith(".pmtiles"): return "pmtiles"
    if n=="tilejson.json": return "tilejson"
    if n in {"index.html","app_config.json"}: return "viewer_bundle"
    if n.endswith(".json"):
        try:
            d=json.loads(path.read_text(encoding="utf-8"))
            if isinstance(d,dict) and (d.get("stac_version") or d.get("type") in {"Catalog","Collection","Feature"}): return "stac_json"
        except Exception: pass
    return "unknown"

def discover_protected_resources(roots:List[str])->List[dict]:
    out=[]
    for r in sorted(roots):
        for p in sorted(Path(r).rglob("*")):
            if p.is_file():
                sha=_sha_file(p)
                out.append({"protected_resource_id":"pres_"+hashlib.sha256(str(p).encode()).hexdigest()[:16],"path":str(p),"resource_role":classify_protected_resource(p),"bytes":p.stat().st_size,"sha256":sha,"media_type":mimetypes.guess_type(str(p))[0] or "application/octet-stream","object_sha256":sha})
    return out

def validate_enforcement_spec(spec:dict,args:dict)->List[str]:
    e=[]
    if spec.get("schema")!="EnforcementSpec.v1": e.append("schema")
    if not spec.get("enforcement_id"): e.append("enforcement_id")
    if not spec.get("dataset_id"): e.append("dataset_id")
    if spec.get("enforcement",{}).get("default_action")!="deny": e.append("default_action")
    mode=spec.get("decision_source",{}).get("mode")
    if mode not in {"trust-decision-envelope","trust-decision-cli","trust-decision-module"}: e.append("decision_source_mode")
    if spec.get("decision_source",{}).get("allow_warn_as_grant") and not args.get("allow_warn_grants"): e.append("warn-as-grant")
    if spec.get("decision_source",{}).get("allow_review_as_grant") and not args.get("allow_review_grants"): e.append("review-as-grant")
    if spec.get("gateway",{}).get("loopback_only") is False and not args.get("allow_public_bind"): e.append("public-bind")
    if spec.get("audit",{}).get("write_usage_audit_ledger") is False and not args.get("allow_no_audit"): e.append("no-audit")
    return e

def validate_access_request(req:dict,args:dict)->List[str]:
    e=[]
    if req.get("schema")!="AccessRequest.v1": e.append("schema")
    t=req.get("target",{})
    if not any(t.get(k) for k in ["protected_resource_id","resource_path","trust_object_id","object_sha256","object_id"]): e.append("target")
    if req.get("action") not in ALLOWED_REQUEST_ACTIONS and not args.get("allow_unknown_action"): e.append("action")
    st=req.get("subject",{}).get("subject_type")
    if st and st not in ALLOWED_SUBJECT_TYPES and not args.get("allow_unknown_subject"): e.append("subject_type")
    if req.get("request_id") is None: req["request_id"]="areq_"+_sha_obj({"t":t,"a":req.get("action")})[:12]
    sid=req.get("subject",{}).get("subject_id")
    if sid: req.setdefault("subject",{})["subject_hash"]=hashlib.sha256(sid.encode()).hexdigest()
    return e

def validate_trust_decision_envelope(env:dict)->List[str]:
    e=[]
    if env.get("schema")!="TrustDecisionEnvelope.v1": e.append("schema")
    if env.get("decision") not in ALLOWED_DECISIONS: e.append("decision")
    if not env.get("decision_hash"): e.append("decision_hash")
    else:
        c={k:v for k,v in env.items() if k!="decision_hash"}
        if _sha_obj(c)!=env.get("decision_hash"): e.append("decision_hash_mismatch")
    if not env.get("policy_hash"): e.append("policy_hash")
    if not isinstance(env.get("target"),dict): e.append("target")
    if not env.get("status"): e.append("status")
    if env.get("decision")=="allow" and env.get("status") in {"revoked","suspended","quarantined","expired","unknown"}: e.append("status_conflict")
    return e

def compute_enforcement_spec_hash(spec): return _sha_obj(spec)
def compute_enforcement_policy_hash(policy): return _sha_obj(policy)
def compute_access_request_hash(req): return _sha_obj({k:v for k,v in req.items() if k!="created_at_utc"})

def build_receipt(run_id,enforcement_id,mode,status):
    return {"schema":"EnforcementReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_enforcement","enforcement_id":enforcement_id,"mode":mode,"status":status}

def run_trust_enforcement(**args):
    spec=read_json(args["enforcement_spec"])
    policy=read_json(args.get("enforcement_policy")) if args.get("enforcement_policy") else read_json("enforcement/enforcement_policy_default.json")
    if (errs:=validate_enforcement_spec(spec,args)): return {"exit":EXIT["malformed"],"errors":errs}
    resources=discover_protected_resources(args.get("protected_resource_roots",[]))
    out_root=Path(args["output_root"]); run_id=args.get("enforcement_run_id") or f"{spec['enforcement_id']}_{args['mode']}"
    stage=out_root/".staging"/run_id; final=out_root/run_id
    if final.exists() and not args.get("overwrite"): return {"exit":EXIT["unsafe"],"errors":["output exists"]}
    if stage.exists(): shutil.rmtree(stage)
    stage.mkdir(parents=True,exist_ok=True)
    write_json(stage/"protected_resource_inventory.json",{"schema":"ProtectedResourceInventory.v1","resources":resources})
    status="planned"
    code=0
    if args["mode"] in {"enforce-once","dry-run"}:
        req=read_json(args["access_request"])
        if (re:=validate_access_request(req,args)): return {"exit":EXIT["malformed"],"errors":re}
        env=read_json(args["trust_decision_envelope"])
        if (de:=validate_trust_decision_envelope(env)): return {"exit":EXIT["decision"],"errors":de}
        d=env["decision"]
        if d=="allow": act="grant"; status="success"; code=0
        elif d=="review": act="review_required"; status="warning"; code=EXIT["review"]
        elif d=="warn": act="deny" if not args.get("allow_warn_grants") else "grant_with_warning"; status="warning"; code=EXIT["warn"]
        else: act="deny"; status="error"; code=EXIT["deny"]
        write_json(stage/"decisions/enforcement_decision.json",{"schema":"EnforcementDecision.v1","trust_decision":d,"enforcement_action":act,"decision_hash":"edh_"+_sha_obj({"d":d,"a":act})[:16]})
        write_json(stage/"audit/usage_audit_event.json",{"schema":"UsageAuditEvent.v1","request_id":req["request_id"],"subject":{"subject_hash":req.get("subject",{}).get("subject_hash"),"redacted":True}})
        if act.startswith("grant"): write_json(stage/"grants/access_grant.json",{"schema":"AccessGrant.v1","resource_sha256":resources[0]["sha256"] if resources else None,"trust_decision_hash":env["decision_hash"]})
        else: write_json(stage/"denials/access_denial.json",{"schema":"AccessDenial.v1","deny_reasons":["decision_"+d]})
    receipt=build_receipt(run_id,spec["enforcement_id"],args["mode"],status)
    write_json(stage/"enforcement_receipt.json",receipt)
    if args["mode"]=="dry-run":
        print(str(stage/"enforcement_receipt.json")); return {"exit":EXIT["dry"]}
    final.parent.mkdir(parents=True,exist_ok=True)
    if final.exists(): shutil.rmtree(final)
    os.replace(stage,final)
    print(str(final/"enforcement_receipt.json"))
    return {"exit":code}

def _parse(argv):
    out={"protected_resource_roots":[],"mode":"enforce-once"}
    i=0
    while i<len(argv):
        a=argv[i]
        if a.startswith("--"):
            k=a[2:].replace("-","_")
            if k=="protected_resource_root": out["protected_resource_roots"].append(argv[i+1]); i+=2; continue
            if i+1<len(argv) and not argv[i+1].startswith("--"): out[k]=argv[i+1]; i+=2; continue
            out[k]=True; i+=1; continue
        i+=1
    return out

def main(argv=None):
    a=_parse(argv or os.sys.argv[1:])
    try:
        r=run_trust_enforcement(**a)
        return r["exit"]
    except KeyError:
        os.sys.stderr.write(json.dumps({"status":"error","error_count":1,"enforcement_receipt_path":None,"enforcement_run_id":None})+"\n")
        return EXIT["malformed"]

if __name__=="__main__": raise SystemExit(main())
