from __future__ import annotations
import argparse, base64, hashlib, json, logging, os, re, shutil, tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

DEFAULT_POLICY = {
  "schema": "TransparencyLogPolicy.v1",
  "policy_id": "soilgrids-transparency-default",
  "allowed_packet_statuses": ["success", "warning"],
  "allowed_disclosure_profiles": ["public-transparency", "auditor-full", "regulator", "internal-review"],
  "public_portal": {"allow_local_paths": False, "allow_internal_hostnames": False, "allow_raw_logs": False, "allow_packet_downloads": False, "allow_external_links": False},
  "redaction": {"require_redaction_report": True, "fail_on_secret_findings": True, "fail_on_approval_token_plaintext": True},
  "claims": {"require_evidence_refs": True, "deny_unsupported_claims": True},
  "signing": {"require_signed_tree_head": False, "allow_unsigned_tree_head": True},
}

class TransparencyError(Exception):
    def __init__(self, msg: str, code: int = 100):
        super().__init__(msg); self.code = code

def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def canonical_bytes(v: Any) -> bytes:
    return json.dumps(v, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode("utf-8")

def sha256_hex(v: bytes) -> str:
    return hashlib.sha256(v).hexdigest()

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

def compute_transparency_spec_hash(spec: Dict[str, Any], policy: Dict[str, Any]) -> str:
    return sha256_hex(canonical_bytes({"spec": spec, "policy": policy}))

def validate_transparency_log_spec(spec: Dict[str, Any], allow_public_packet_downloads: bool=False) -> None:
    if spec.get("schema") != "TransparencyLogSpec.v1": raise TransparencyError("unsupported schema",30)
    if not spec.get("transparency_log_id") or not spec.get("dataset_id"): raise TransparencyError("missing ids",30)
    if spec.get("log",{}).get("algorithm") != "sha256-rfc9162-style": raise TransparencyError("bad algorithm",30)
    if spec.get("log",{}).get("append_only") is not True: raise TransparencyError("append_only required",30)
    if spec.get("portal_profile") not in {"public","auditor","internal"}: raise TransparencyError("bad portal profile",30)
    if spec.get("portal",{}).get("include_packet_download_links") and not allow_public_packet_downloads:
        raise TransparencyError("packet downloads forbidden",30)

def load_transparency_policy(path: Optional[Path]) -> Dict[str, Any]:
    if path is None: return DEFAULT_POLICY
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "TransparencyLogPolicy.v1": raise TransparencyError("bad policy schema",30)
    return data

def compute_packet_leaf_hash(entry: Dict[str, Any], leaf_domain_separator: str="00") -> str:
    prefix = bytes.fromhex(leaf_domain_separator)
    return sha256_hex(prefix + canonical_bytes(entry))

def build_merkle_tree(leaf_hashes: List[str], node_domain_separator: str="01") -> List[List[str]]:
    if not leaf_hashes: return []
    levels=[leaf_hashes[:]]
    while len(levels[-1])>1:
        prev=levels[-1]; nxt=[]
        for i in range(0,len(prev),2):
            if i+1>=len(prev): nxt.append(prev[i])
            else: nxt.append(sha256_hex(bytes.fromhex(node_domain_separator)+bytes.fromhex(prev[i])+bytes.fromhex(prev[i+1])))
        levels.append(nxt)
    return levels

def compute_merkle_root(leaf_hashes: List[str], node_domain_separator: str="01") -> Optional[str]:
    t=build_merkle_tree(leaf_hashes,node_domain_separator)
    return t[-1][0] if t else None

def build_inclusion_proof(leaf_hashes: List[str], leaf_index: int, node_domain_separator: str="01") -> List[Dict[str,str]]:
    proof=[]; idx=leaf_index; level=leaf_hashes[:]
    while len(level)>1:
        if idx%2==0 and idx+1<len(level): proof.append({"position":"right","hash":level[idx+1]})
        elif idx%2==1: proof.append({"position":"left","hash":level[idx-1]})
        n=[]
        for i in range(0,len(level),2):
            if i+1>=len(level): n.append(level[i])
            else: n.append(sha256_hex(bytes.fromhex(node_domain_separator)+bytes.fromhex(level[i])+bytes.fromhex(level[i+1])))
        idx//=2; level=n
    return proof

def verify_inclusion_proof(leaf_hash: str, proof: List[Dict[str,str]], expected_root: str, node_domain_separator: str="01") -> bool:
    cur=leaf_hash
    for p in proof:
        if p["position"]=="left": cur=sha256_hex(bytes.fromhex(node_domain_separator)+bytes.fromhex(p["hash"])+bytes.fromhex(cur))
        else: cur=sha256_hex(bytes.fromhex(node_domain_separator)+bytes.fromhex(cur)+bytes.fromhex(p["hash"]))
    return cur==expected_root

def build_consistency_proof(old_leaves: List[str], new_leaves: List[str]) -> Dict[str,Any]:
    ok=len(old_leaves)<=len(new_leaves) and old_leaves==new_leaves[:len(old_leaves)]
    return {"proof_hashes":[],"verified":ok,"errors":[] if ok else ["append-only violation"]}

def verify_consistency_proof(old_leaves: List[str], new_leaves: List[str], proof: Dict[str,Any]) -> bool:
    return proof.get("verified") and old_leaves==new_leaves[:len(old_leaves)]

def build_signed_tree_head(log_id:str, tree_size:int, root_hash:str, snapshot_hash:str, backend:str="unsigned"):
    sig={"type":"unsigned","signing_backend":"unsigned","key_id":None,"signature_value":None}
    if backend=="mock":
        sig={"type":"mock-signature","signing_backend":"mock","key_id":"mock-key","signature_value":base64.b64encode(canonical_bytes([log_id,tree_size,root_hash,snapshot_hash])).decode()}
    return {"schema":"SignedTreeHead.v1","transparency_log_id":log_id,"created_at_utc":now_iso(),"source":"soilgrids_transparency_portal","tree_size":tree_size,"root_hash":root_hash,"snapshot_hash":snapshot_hash,"signature":sig,"errors":[]}

def compute_log_snapshot_hash(snapshot: Dict[str,Any]) -> str:
    c={k:v for k,v in snapshot.items() if k not in {"created_at_utc","snapshot_hash"}}
    return sha256_hex(canonical_bytes(c))

# simplified orchestrator

def build_transparency_log_and_portal(**kwargs) -> Dict[str,Any]:
    spec_path=Path(kwargs["transparency_log_spec"])
    if not spec_path.exists(): raise TransparencyError("missing spec",30)
    spec=json.loads(spec_path.read_text())
    policy=load_transparency_policy(Path(kwargs["transparency_log_policy"]) if kwargs.get("transparency_log_policy") else None)
    validate_transparency_log_spec(spec, kwargs.get("allow_public_packet_downloads",False))
    roots=[Path(p) for p in kwargs.get("disclosure_packet_roots",[])]
    mode=kwargs.get("mode","plan-only")
    if mode in {"append-packets","full"} and not roots: raise TransparencyError("missing disclosure roots",40)
    entries=[]
    for r in roots:
        packet=json.loads((r/"disclosure_packet.json").read_text())
        trust=json.loads((r/"trust_claim_set.json").read_text())
        red=json.loads((r/"redaction_report.json").read_text())
        entry={"disclosure_packet_id":packet["disclosure_packet_id"],"disclosure_packet_hash":sha256_hex(canonical_bytes(packet)),"trust_claim_set_hash":sha256_hex(canonical_bytes(trust)),"redaction_hash":sha256_hex(canonical_bytes(red)),"source_assurance_pack_hash":None,"packet_profile":packet.get("packet_profile","public-transparency"),"audience":packet.get("audience","public")}
        entry["leaf_hash"]=compute_packet_leaf_hash({k:entry[k] for k in entry if k!="leaf_hash"})
        entries.append(entry)
    entries.sort(key=lambda e:e["disclosure_packet_id"])
    leaves=[e["leaf_hash"] for e in entries]
    root=compute_merkle_root(leaves)
    snap={"schema":"TransparencyLogSnapshot.v1","transparency_log_id":spec["transparency_log_id"],"created_at_utc":now_iso(),"source":"soilgrids_transparency_portal","log_algorithm":"sha256-rfc9162-style","tree_size":len(leaves),"root_hash":root,"snapshot_hash":"","previous_snapshot_hash":None,"leaves":[{"leaf_index":i,**{k:v for k,v in e.items() if k!="leaf_hash"},"leaf_hash":e["leaf_hash"]} for i,e in enumerate(entries)],"errors":[]}
    snap["snapshot_hash"]=compute_log_snapshot_hash(snap)
    return {"spec":spec,"policy":policy,"snapshot":snap,"entries":entries}

def main(argv=None):
    ap=argparse.ArgumentParser()
    ap.add_argument("--transparency-log-spec", required=True)
    ap.add_argument("--output-root", required=True)
    ap.add_argument("--mode", default="plan-only")
    ap.add_argument("--disclosure-packet-root", action="append", default=[])
    ap.add_argument("--transparency-log-policy")
    args=ap.parse_args(argv)
    try:
        out=build_transparency_log_and_portal(transparency_log_spec=args.transparency_log_spec, transparency_log_policy=args.transparency_log_policy, disclosure_packet_roots=args.disclosure_packet_root, mode=args.mode)
        o=Path(args.output_root); o.mkdir(parents=True,exist_ok=True)
        rpath=o/"transparency_log_receipt.json"
        receipt={"schema":"TransparencyLogReceipt.v1","status":"planned" if args.mode=="plan-only" else "success","mode":args.mode,"transparency_log_id":out["spec"]["transparency_log_id"],"created_at_utc":now_iso(),"source":"soilgrids_transparency_portal","log_snapshot_hash":out["snapshot"]["snapshot_hash"],"tree_size":out["snapshot"]["tree_size"],"root_hash":out["snapshot"]["root_hash"]}
        write_canonical_json(rpath, receipt)
        print(str(rpath))
        return 0
    except TransparencyError as e:
        print(json.dumps({"status":"error","error_count":1,"transparency_log_receipt_path":None,"transparency_portal_id":None}), file=os.sys.stderr)
        return e.code

if __name__=="__main__":
    raise SystemExit(main())
