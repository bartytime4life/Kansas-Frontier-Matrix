#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

SOURCE_NAME = "soilgrids_status_distribution"

class ExitCode(int, Enum):
    SUCCESS = 0; DRY_RUN = 5; WARNING = 10; SOURCE_VALIDATION = 20; MALFORMED_INPUT = 30; OBJECT_PLAN = 40; LOCAL_MIRROR = 50; UPLOAD = 60; REMOTE_VALIDATION = 70; RESOLVER_VALIDATION = 80; UNSAFE_PATH = 90; SECRET = 100; INTERNAL = 110

class DistributionMode(str, Enum):
    PLAN_ONLY="plan-only"; LOCAL_MIRROR="local-mirror"; BUILD_RESOLVER="build-resolver"; S3_COMPATIBLE="s3-compatible"; VALIDATE_REMOTE="validate-remote"; DRY_RUN="dry-run"

REQUIRED_SOURCE_FILES=["trust_status_receipt.json","registry/trust_status_registry.json","registry/trust_status_snapshot.json","lists/trust_revocation_list.json","lists/trust_suspension_list.json","checksums.sha256"]


def _utc_now() -> str: return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def _canonical_bytes(data:Any)->bytes: return json.dumps(data,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def _sha256_bytes(data:bytes)->str: return hashlib.sha256(data).hexdigest()
def _sha256_file(p:Path)->str: return _sha256_bytes(p.read_bytes())

def write_canonical_json(path:Path,data:Any)->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(data,sort_keys=True,indent=2)+"\n",encoding="utf-8")

def compute_status_distribution_spec_hash(spec:Dict[str,Any])->str: return _sha256_bytes(_canonical_bytes(spec))

def validate_status_distribution_spec(spec:Dict[str,Any])->None:
    if not isinstance(spec,dict): raise ValueError("malformed")
    if spec.get("schema")!="StatusDistributionSpec.v1": raise ValueError("unsupported schema")
    for k in ("status_distribution_id","dataset_id"):
        if not spec.get(k): raise ValueError("missing required")

def _safe_rel(s:str)->bool:
    p=Path(s)
    return not (p.is_absolute() or ".." in p.parts)

def infer_content_type(path:str,allow_octet_stream:bool=False)->str:
    ext=Path(path).suffix.lower(); m={".json":"application/json",".html":"text/html; charset=utf-8",".js":"application/javascript",".css":"text/css",".sha256":"text/plain; charset=utf-8"}
    if ext in m: return m[ext]
    if allow_octet_stream: return "application/octet-stream"
    raise ValueError("unknown")

def infer_cache_control(relative_path:str,spec:Dict[str,Any])->str:
    if relative_path in {"latest-status.json","status-index.json","revocations.json","suspensions.json"}: return "public, max-age=60"
    return "public, max-age=31536000, immutable"

def _scan_secret(text:str)->bool:
    return bool(re.search(r"AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC )?PRIVATE KEY-----",text))

def validate_trust_status_source(root:Path)->Dict[str,Any]:
    for rel in REQUIRED_SOURCE_FILES:
        if not (root/rel).exists(): raise FileNotFoundError(rel)
    data={
        "receipt":json.loads((root/"trust_status_receipt.json").read_text()),
        "registry":json.loads((root/"registry/trust_status_registry.json").read_text()),
        "snapshot":json.loads((root/"registry/trust_status_snapshot.json").read_text()),
        "revocations":json.loads((root/"lists/trust_revocation_list.json").read_text()),
        "suspensions":json.loads((root/"lists/trust_suspension_list.json").read_text()),
    }
    if data["receipt"].get("status") not in {"success","warning","verified"}: raise ValueError("bad receipt")
    if data["snapshot"].get("registry_hash") and data["snapshot"]["registry_hash"]!=data["registry"].get("registry_hash"): raise ValueError("registry hash mismatch")
    if data["snapshot"].get("snapshot_hash") and data["snapshot"]["snapshot_hash"]!=_sha256_bytes(_canonical_bytes(data["snapshot"].get("snapshot",{}))): raise ValueError("snapshot hash mismatch")
    return data

def build_status_resolver_index(status_distribution_id:str,run_id:str,registry:Dict[str,Any],snapshot:Dict[str,Any])->Dict[str,Any]:
    objs=[]
    for o in registry.get("objects",[]):
        oid=o["trust_object_id"]
        objs.append({"trust_object_id":oid,"path":f"status/objects/{oid}.json","current_status":o.get("current_status","active")})
    idx={"schema":"StatusResolverIndex.v1","status_distribution_id":status_distribution_id,"status_distribution_run_id":run_id,"created_at_utc":_utc_now(),"objects":objs,"trust_status_snapshot_hash":snapshot.get("snapshot_hash")}
    idx["resolver_index_hash"]=_sha256_bytes(_canonical_bytes({k:v for k,v in idx.items() if k!="resolver_index_hash"}))
    return idx

def build_status_resolver_openapi()->Dict[str,Any]:
    return {"openapi":"3.1.1","info":{"title":"Status Resolver","version":"1.0.0"},"paths":{"/latest-status.json":{"get":{}},"/status-index.json":{"get":{}},"/status/objects/{trust_object_id}.json":{"get":{}},"/revocations.json":{"get":{}},"/suspensions.json":{"get":{}}},"components":{"schemas":{"StatusResolverIndex.v1":{},"TrustObjectStatusResolution.v1":{},"TrustRevocationList.v1":{},"TrustSuspensionList.v1":{},"TrustStatusSnapshot.v1":{}}}}

def _write_portal(out:Path):
    (out/"portal").mkdir(parents=True,exist_ok=True)
    (out/"portal/index.html").write_text("<!doctype html><html><head><meta http-equiv='Content-Security-Policy' content=\"default-src 'self'\"></head><body><script src='assets/status_portal.js'></script><link rel='stylesheet' href='assets/status_portal.css'/></body></html>")
    (out/"portal/status_portal_config.json").write_text("{}")
    (out/"portal/assets").mkdir(exist_ok=True)
    (out/"portal/assets/status_portal.js").write_text("const x=1;")
    (out/"portal/assets/status_portal.css").write_text(":focus{outline:2px solid #00f;} @media (prefers-reduced-motion: reduce){*{animation:none}}")

def write_checksums_file(root:Path):
    files=sorted([p for p in root.rglob("*") if p.is_file() and p.name!="checksums.sha256"])
    (root/"checksums.sha256").write_text("\n".join(f"{_sha256_file(p)}  {p.relative_to(root).as_posix()}" for p in files)+"\n")

def run_status_distribution(status_distribution_spec:Path, output_root:Path, mode:str, trust_status_run_root:Optional[Path]=None, deterministic_run_id:bool=False, overwrite:bool=False)->Tuple[Path,ExitCode]:
    spec=json.loads(status_distribution_spec.read_text())
    validate_status_distribution_spec(spec)
    if mode!=DistributionMode.VALIDATE_REMOTE.value and not trust_status_run_root: raise ValueError("missing trust_status_run_root")
    run_id=(spec["status_distribution_id"]+"_det") if deterministic_run_id else f"{spec['status_distribution_id']}_{mode}_{compute_status_distribution_spec_hash(spec)[:10]}"
    out=output_root/run_id
    if out.exists() and not overwrite: raise FileExistsError("exists")
    if out.exists() and overwrite: shutil.rmtree(out)
    out.mkdir(parents=True,exist_ok=True)
    if trust_status_run_root:
        src=validate_trust_status_source(trust_status_run_root)
        idx=build_status_resolver_index(spec["status_distribution_id"],run_id,src["registry"],src["snapshot"])
        write_canonical_json(out/"status-index.json",idx)
        for o in idx["objects"]:
            write_canonical_json(out/o["path"],{"schema":"TrustObjectStatusResolution.v1","trust_object_id":o["trust_object_id"],"status":o["current_status"],"revoked":o["current_status"]=="revoked","suspended":o["current_status"]=="suspended"})
        write_canonical_json(out/"revocations.json",src["revocations"])
        write_canonical_json(out/"suspensions.json",src["suspensions"])
    write_canonical_json(out/"api/status_resolver_openapi.json",build_status_resolver_openapi())
    _write_portal(out)
    receipt={"schema":"StatusDistributionReceipt.v1","status":"planned" if mode=="plan-only" else "success","status_distribution_run_id":run_id}
    write_canonical_json(out/"status_distribution_receipt.json",receipt)
    write_checksums_file(out)
    code=ExitCode.SUCCESS
    if mode==DistributionMode.DRY_RUN.value: code=ExitCode.DRY_RUN
    return out/"status_distribution_receipt.json",code

def _build_parser()->argparse.ArgumentParser:
    p=argparse.ArgumentParser(); p.add_argument("--status-distribution-spec",required=True); p.add_argument("--output-root",required=True); p.add_argument("--mode",required=True,choices=[m.value for m in DistributionMode]); p.add_argument("--trust-status-run-root"); p.add_argument("--deterministic-run-id",action="store_true"); p.add_argument("--overwrite",action="store_true"); return p

def main()->int:
    a=_build_parser().parse_args()
    try:
        receipt,code=run_status_distribution(Path(a.status_distribution_spec),Path(a.output_root),a.mode,Path(a.trust_status_run_root) if a.trust_status_run_root else None,a.deterministic_run_id,a.overwrite)
        print(receipt.as_posix())
        return int(code)
    except FileNotFoundError:
        err={"status":"error","error_count":1,"status_distribution_receipt_path":None,"status_distribution_run_id":None}; print(json.dumps(err),file=os.sys.stderr); return int(ExitCode.SOURCE_VALIDATION)
    except ValueError:
        err={"status":"error","error_count":1,"status_distribution_receipt_path":None,"status_distribution_run_id":None}; print(json.dumps(err),file=os.sys.stderr); return int(ExitCode.MALFORMED_INPUT)
    except Exception:
        err={"status":"error","error_count":1,"status_distribution_receipt_path":None,"status_distribution_run_id":None}; print(json.dumps(err),file=os.sys.stderr); return int(ExitCode.INTERNAL)

if __name__=="__main__":
    raise SystemExit(main())
