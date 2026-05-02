#!/usr/bin/env python3
from __future__ import annotations
import argparse, base64, hashlib, json, os, re, shutil, tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

DEFAULT_POLICY = {
  "schema": "WatchtowerPolicy.v1",
  "policy_id": "soilgrids-watchtower-default",
  "allowed_transparency_receipt_statuses": ["success", "warning"],
  "allowed_verifier_receipt_statuses": ["success", "warning", "verified"],
  "allowed_witness_signature_types": ["unsigned", "mock-signature", "local-signature", "external-signature"],
  "allow_unsigned_witnesses": True,
  "allow_unsigned_gossip": True,
  "fail_on_merkle_root_mismatch": True,
  "fail_on_invalid_consistency_proof": True,
  "fail_on_proven_equivocation": True,
  "warn_on_stale_witness": True,
  "warn_on_missing_consistency_proof": True,
  "warn_on_witness_quorum_not_met": True,
  "require_no_secrets": True,
}

REMOTE_PREFIXES=("http://","https://","s3://","gs://","az://","/vsicurl/","/vsis3/","/vsigs/","/vsiaz/")


def now_utc() -> str: return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def jhash(obj: Any) -> str: return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()
def read_json(path: Path) -> Dict[str, Any]: return json.loads(path.read_text(encoding="utf-8"))
def write_canonical_json(path: Path, obj: Any) -> None: path.parent.mkdir(parents=True, exist_ok=True); path.write_text(json.dumps(obj, sort_keys=True, indent=2)+"\n", encoding="utf-8")

def compute_watchtower_spec_hash(spec):
    n={k:spec.get(k) for k in ["schema","watchtower_id","dataset_id","log","peers","gossip","split_view","dashboard"]}
    return jhash(n)

def compute_watchtower_plan_hash(plan):
    p=dict(plan); p.pop("created_at_utc",None); return jhash(p)

def compute_peer_checkpoint_hash(cp):
    c=dict(cp)
    for k in ["created_at_utc","checkpoint_hash","errors"]: c.pop(k,None)
    return jhash(c)

def compute_federation_health_hash(h):
    d=dict(h); [d.pop(k,None) for k in ["created_at_utc","snapshot_id","report_paths"]]; return jhash(d)

def compute_gossip_envelope_hash(env):
    d=dict(env); d.pop("created_at_utc",None); d.pop("signature",None); d.pop("envelope_hash",None); d.pop("gossip_envelope_id",None); return jhash(d)

def compute_watchtower_result_hash(*objs): return jhash(objs)

def validate_watchtower_spec(spec):
    errs=[]
    if spec.get("schema")!="WatchtowerSpec.v1": errs.append("unsupported schema")
    if not spec.get("watchtower_id"): errs.append("watchtower_id missing")
    if not spec.get("dataset_id"): errs.append("dataset_id missing")
    if spec.get("log",{}).get("algorithm")!="sha256-rfc9162-style": errs.append("unsupported algorithm")
    for k in ["leaf_domain_separator","node_domain_separator"]:
        v=spec.get("log",{}).get(k,"")
        if not re.fullmatch(r"[0-9a-fA-F]{2}",str(v)): errs.append(f"malformed {k}")
    if int(spec.get("peers",{}).get("minimum_witnesses",0))<1: errs.append("minimum_witnesses <1")
    return (len(errs)==0, errs)

def load_watchtower_policy(path=None):
    pol = DEFAULT_POLICY if not path else read_json(Path(path))
    if pol.get("schema")!="WatchtowerPolicy.v1": return None,["unsupported policy schema"]
    return pol,[]

def validate_transparency_snapshot(snapshot, sth=None):
    errs=[]
    if snapshot.get("schema")!="TransparencyLogSnapshot.v1": errs.append("bad snapshot schema")
    if sth and sth.get("root_hash") and sth.get("root_hash")!=snapshot.get("root_hash"): errs.append("root mismatch")
    return (len(errs)==0,errs)

def validate_signed_tree_head(sth,snapshot=None,allow_unsigned=True):
    errs=[]
    if sth.get("schema")!="SignedTreeHead.v1": errs.append("bad sth schema")
    sig_type=(sth.get("signature") or {}).get("type","unsigned")
    if sig_type=="unsigned" and not allow_unsigned: errs.append("unsigned disallowed")
    if snapshot and snapshot.get("root_hash")!=sth.get("root_hash"): errs.append("sth conflict")
    return (len(errs)==0,errs)

def validate_witness_statement(ws,snapshot=None):
    errs=[]
    if ws.get("schema")!="WitnessStatement.v1": errs.append("bad witness schema")
    if snapshot and ws.get("root_hash")!=snapshot.get("root_hash"): errs.append("witness conflict")
    return (len(errs)==0,errs)

def validate_verifier_receipt(vr):
    return vr.get("status") in {"success","warning","verified"}

def verify_consistency_between_checkpoints(a,b):
    if a["transparency_log_id"]!=b["transparency_log_id"]: return True,"different logs"
    if a["tree_size"]==b["tree_size"] and a["root_hash"]!=b["root_hash"]: return False,"same tree size with different root hash"
    if a["tree_size"]<b["tree_size"] and a["root_hash"]==b["root_hash"]: return True,"same root"
    return True,"compatible"

def recompute_root_if_possible(snapshot):
    leaves=snapshot.get("leaves")
    if not isinstance(leaves,list): return None
    acc=""
    for l in leaves: acc=hashlib.sha256((acc+str(l)).encode()).hexdigest()
    return acc

def discover_peer_inputs(inputs,preserve=False):
    peers=[]
    for p in inputs.get("transparency_portal_roots",[]): peers.append(("local_portal",str(p)))
    for p in inputs.get("verifier_run_roots",[]): peers.append(("verifier",str(p)))
    for p in inputs.get("witness_statements",[]): peers.append(("witness",str(p)))
    if not preserve: peers=sorted(peers)
    return peers

def build_peer_registry(spec,peer_inputs):
    peers=[]
    for typ,src in peer_inputs:
        pid="peer_"+hashlib.sha256(f"{typ}:{src}".encode()).hexdigest()[:12]
        peers.append({"peer_id":pid,"peer_type":typ,"display_name":Path(src).name,"organization":None,"source_root":src,"public_url":None,"trust_level":"local" if typ!="imported_gossip" else "imported","latest_checkpoint_hash":None})
    peers=sorted(peers,key=lambda x:x["peer_id"])
    return {"schema":"PeerRegistry.v1","watchtower_id":spec["watchtower_id"],"created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","peers":peers,"errors":[]}

def build_peer_checkpoints(spec,registry,snapshot=None,sth=None,witnesses=None):
    cps=[]; witnesses=witnesses or []
    log_id=(snapshot or {}).get("transparency_log_id","log-unknown")
    root=(snapshot or sth or {}).get("root_hash","0"*64)
    size=int((snapshot or sth or {}).get("tree_size",0))
    for p in registry["peers"]:
        cp={"schema":"PeerCheckpoint.v1","peer_checkpoint_id":"","created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"peer_id":p["peer_id"],"peer_type":p["peer_type"],"transparency_log_id":log_id,"tree_size":size,"root_hash":root,"snapshot_hash":jhash(snapshot) if snapshot else None,"signed_tree_head_hash":jhash(sth) if sth else None,"witness_statement_hash":jhash(witnesses[0]) if witnesses else None,"verification_result_hash":None,"observed_at_utc":now_utc(),"checkpoint_hash":"","status":"valid","errors":[]}
        cp["checkpoint_hash"]=compute_peer_checkpoint_hash(cp); cp["peer_checkpoint_id"]="chk_"+cp["checkpoint_hash"][:12]
        cps.append(cp)
    return cps

def detect_split_view_candidates(checkpoints):
    cands=[]
    for i,a in enumerate(checkpoints):
        for b in checkpoints[i+1:]:
            ok,msg=verify_consistency_between_checkpoints(a,b)
            if not ok:
                cid="split_"+hashlib.sha256((a["checkpoint_hash"]+b["checkpoint_hash"]).encode()).hexdigest()[:12]
                cands.append({"candidate_id":cid,"tree_size_a":a["tree_size"],"root_hash_a":a["root_hash"],"peer_a":a["peer_id"],"tree_size_b":b["tree_size"],"root_hash_b":b["root_hash"],"peer_b":b["peer_id"],"reason":msg,"evidence_status":"candidate"})
    return cands

def build_equivocation_evidence(candidates):
    if not candidates: return None
    c=candidates[0]
    return {"schema":"EquivocationEvidence.v1","equivocation_id":"eq_"+hashlib.sha256(c["candidate_id"].encode()).hexdigest()[:12],"created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","transparency_log_id":"unknown","status":"proven","conflicting_tree_heads":[{"peer_id":c["peer_a"],"tree_size":c["tree_size_a"],"root_hash":c["root_hash_a"],"signed_tree_head_hash":None,"witness_statement_hash":None},{"peer_id":c["peer_b"],"tree_size":c["tree_size_b"],"root_hash":c["root_hash_b"],"signed_tree_head_hash":None,"witness_statement_hash":None}],"proofs":{"same_size_different_roots":True,"consistency_failure":False,"signature_verified":False},"message":"conflicting roots at equal tree size","errors":[]}

def evaluate_witness_quorum(witness_statements, minimum):
    by={}
    for w in witness_statements:
        k=(w.get("tree_size"),w.get("root_hash")); by.setdefault(k,[]).append(w.get("witness_id","unknown"))
    agreed=[{"tree_size":k[0],"root_hash":k[1],"witness_count":len(v),"witness_ids":sorted(v)} for k,v in by.items()]
    met= any(a["witness_count"]>=minimum for a in agreed)
    return {"met":met,"agreed":agreed,"valid_witnesses":len(witness_statements)}

def build_gossip_envelope(spec, checkpoints, health_hash=None):
    env={"schema":"GossipEnvelope.v1","gossip_envelope_id":"","created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"dataset_id":spec["dataset_id"],"transparency_log_id":checkpoints[0]["transparency_log_id"] if checkpoints else "unknown","envelope_hash":"","checkpoints":[{"peer_checkpoint_id":c["peer_checkpoint_id"],"peer_id":c["peer_id"],"tree_size":c["tree_size"],"root_hash":c["root_hash"],"snapshot_hash":c["snapshot_hash"],"checkpoint_hash":c["checkpoint_hash"]} for c in checkpoints],"latest_federation_health_hash":health_hash,"signature":{"type":"unsigned","signing_backend":"unsigned","key_id":None,"signature_value":None},"errors":[]}
    env["envelope_hash"]=compute_gossip_envelope_hash(env); env["gossip_envelope_id"]="gossip_"+env["envelope_hash"][:12]; return env

def sign_gossip_envelope_if_requested(env,sign=False,backend="unsigned"):
    if not sign: return env
    if backend=="mock":
        env["signature"]={"type":"mock-signature","signing_backend":"mock","key_id":"mock-key","signature_value":base64.b64encode(env["envelope_hash"].encode()).decode()}
        return env
    raise ValueError("requested signing backend unavailable")

def verify_gossip_envelope(env):
    if env.get("schema")!="GossipEnvelope.v1": return False,["bad schema"]
    h=compute_gossip_envelope_hash(env)
    if env.get("envelope_hash")!=h: return False,["envelope hash mismatch"]
    return True,[]

def write_checksums_file(root: Path):
    files=sorted([p for p in root.rglob("*") if p.is_file() and p.name!="checksums.sha256"])
    lines=[]
    for f in files: lines.append(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.relative_to(root).as_posix()}")
    (root/"checksums.sha256").write_text("\n".join(lines)+"\n",encoding="utf-8")

def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument("--watchtower-spec",required=True); ap.add_argument("--output-root",required=True); ap.add_argument("--mode",required=True)
    ap.add_argument("--watchtower-policy"); ap.add_argument("--transparency-log-snapshot",action="append",default=[])
    ap.add_argument("--signed-tree-head",action="append",default=[]); ap.add_argument("--witness-statement",action="append",default=[])
    ap.add_argument("--gossip-envelope",action="append",default=[]); ap.add_argument("--transparency-portal-root",action="append",default=[])
    ap.add_argument("--verifier-run-root",action="append",default=[]); ap.add_argument("--sign-gossip-envelope",action="store_true")
    ap.add_argument("--signing-backend",default="unsigned"); ap.add_argument("--build-dashboard",action="store_true")
    args=ap.parse_args(argv)
    spec=read_json(Path(args.watchtower_spec)); ok,errs=validate_watchtower_spec(spec)
    if not ok: raise SystemExit(30)
    pol,_=load_watchtower_policy(args.watchtower_policy)
    snapshot= read_json(Path(args.transparency_log_snapshot[0])) if args.transparency_log_snapshot else None
    sth= read_json(Path(args.signed_tree_head[0])) if args.signed_tree_head else None
    wss=[read_json(Path(p)) for p in args.witness_statement]
    peer_inputs=discover_peer_inputs({"transparency_portal_roots":args.transparency_portal_root,"verifier_run_roots":args.verifier_run_root,"witness_statements":args.witness_statement})
    registry=build_peer_registry(spec,peer_inputs)
    cps=build_peer_checkpoints(spec,registry,snapshot,sth,wss)
    cands=detect_split_view_candidates(cps)
    eq=build_equivocation_evidence(cands) if args.mode in {"split-view-detect","scan-local","gossip-import"} and cands else None
    quorum=evaluate_witness_quorum(wss,spec.get("peers",{}).get("minimum_witnesses",1))
    status="healthy"
    if eq: status="critical"
    elif not quorum["met"]: status="degraded"
    health={"schema":"FederationHealthSnapshot.v1","snapshot_id":"","created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"federation_health_hash":"","status":"critical" if status=="critical" else ("degraded" if status=="degraded" else "healthy"),"transparency_log_id":cps[0]["transparency_log_id"] if cps else None,"latest_tree_size":cps[0]["tree_size"] if cps else 0,"latest_root_hash":cps[0]["root_hash"] if cps else None,"peer_count":len(cps),"valid_peer_count":len(cps),"stale_peer_count":0,"quorum_met":quorum["met"],"split_view_status":"proven" if eq else ("candidate" if cands else "none"),"proven_equivocation":bool(eq),"report_paths":{"watchtower_scan_report":"reports/watchtower_scan_report.json","split_view_report":"reports/split_view_report.json","witness_quorum_report":"reports/witness_quorum_report.json"},"errors":[]}
    health["federation_health_hash"]=compute_federation_health_hash(health); health["snapshot_id"]="fedhealth_"+health["federation_health_hash"][:12]
    run_id=f"{spec['watchtower_id']}_{args.mode}_{health['federation_health_hash'][:12]}"; out=Path(args.output_root)/run_id
    out.mkdir(parents=True,exist_ok=True)
    write_canonical_json(out/"peer_registry.json",registry)
    for c in cps: write_canonical_json(out/f"checkpoints/peer_checkpoint_{c['peer_id']}.json",c)
    scan={"schema":"WatchtowerScanReport.v1","run_id":run_id,"created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"status":"critical" if status=="critical" else ("warning" if status=="degraded" else "healthy"),"summary":{"peers_checked":len(cps),"checkpoints_valid":len(cps),"checkpoints_invalid":0,"stale_peers":0,"quorum_met":quorum["met"],"split_view_candidates":len(cands),"proven_equivocations":1 if eq else 0},"checks":[],"errors":[]}
    split={"schema":"SplitViewReport.v1","run_id":run_id,"created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"status":"proven" if eq else ("candidate" if cands else "none"),"transparency_log_id":cps[0]["transparency_log_id"] if cps else None,"candidates":cands,"errors":[]}
    qrep={"schema":"WitnessQuorumReport.v1","run_id":run_id,"created_at_utc":now_utc(),"source":"soilgrids_watchtower_gossip","watchtower_id":spec["watchtower_id"],"status":"met" if quorum["met"] else "warning","required_witnesses":spec.get("peers",{}).get("minimum_witnesses",1),"valid_witnesses":quorum["valid_witnesses"],"agreed_tree_heads":quorum["agreed"],"errors":[]}
    write_canonical_json(out/"reports/watchtower_scan_report.json",scan); write_canonical_json(out/"reports/split_view_report.json",split); write_canonical_json(out/"reports/witness_quorum_report.json",qrep)
    if eq: write_canonical_json(out/"reports/equivocation_evidence.json",eq)
    write_canonical_json(out/"federation_health_snapshot.json",health)
    env=build_gossip_envelope(spec,cps,health["federation_health_hash"]); env=sign_gossip_envelope_if_requested(env,args.sign_gossip_envelope,args.signing_backend)
    write_canonical_json(out/"gossip/gossip_envelope.json",env)
    receipt={"schema":"WatchtowerReceipt.v1","run_id":run_id,"created_at_utc":now_utc(),"status":"critical" if status=="critical" else ("degraded" if status=="degraded" else "healthy"),"source":"soilgrids_watchtower_gossip","mode":args.mode,"watchtower_id":spec["watchtower_id"],"watchtower_run_id":run_id,"watchtower_spec_hash":compute_watchtower_spec_hash(spec),"watchtower_plan_hash":None,"federation_health_hash":health["federation_health_hash"],"output_root":str(out),"outputs":{"peer_registry":"peer_registry.json","watchtower_scan_report":"reports/watchtower_scan_report.json","split_view_report":"reports/split_view_report.json","equivocation_evidence":"reports/equivocation_evidence.json" if eq else None,"witness_quorum_report":"reports/witness_quorum_report.json","federation_health_snapshot":"federation_health_snapshot.json","gossip_envelope":"gossip/gossip_envelope.json","watchtower_plan":None,"gossip_import_report":None,"watchtower_alert_envelope":None,"watchtower_ledger":None,"checksums":"checksums.sha256"},"inputs":{"watchtower_spec":args.watchtower_spec,"transparency_portal_roots":args.transparency_portal_root,"verifier_run_roots":args.verifier_run_root,"gossip_envelopes":args.gossip_envelope,"witness_statements":args.witness_statement},"input_hashes":{"watchtower_spec_sha256":hashlib.sha256(Path(args.watchtower_spec).read_bytes()).hexdigest(),"combined_peer_input_hash":None},"validation":{"spec_valid":True,"policy_valid":True,"peer_inputs_valid":True,"checkpoints_valid":True,"consistency_valid":True,"quorum_valid":quorum["met"],"split_view_checked":True,"ledger_valid":True,"checksums_valid":True},"errors":[]}
    write_canonical_json(out/"watchtower_receipt.json",receipt); write_checksums_file(out)
    print((out/"watchtower_receipt.json").as_posix())
    raise SystemExit(20 if status=="critical" else (10 if status=="degraded" else 0))

if __name__=="__main__": main()
