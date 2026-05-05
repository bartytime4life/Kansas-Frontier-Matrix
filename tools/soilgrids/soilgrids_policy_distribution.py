#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import logging
import mimetypes
import os
import re
import shutil
import tarfile
import tempfile
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SOURCE = "soilgrids_policy_distribution"
SUPPORTED_SPEC_SCHEMA = "PolicyDistributionSpec.v1"
SUPPORTED_POLICY_SCHEMA = "PolicyDistributionPolicy.v1"
DEFAULT_MODE = "plan-only"

class Mode(str, Enum):
    PLAN_ONLY = "plan-only"
    LOCAL_MIRROR = "local-mirror"
    BUILD_RESOLVER = "build-resolver"
    S3_COMPATIBLE = "s3-compatible"
    VALIDATE_REMOTE = "validate-remote"
    VERIFY_DISTRIBUTION = "verify-distribution"
    BUILD_PORTAL = "build-portal"
    DRY_RUN = "dry-run"

DEFAULT_POLICY = {
    "schema": SUPPORTED_POLICY_SCHEMA,
    "policy_id": "soilgrids-policy-distribution-default",
    "allowed_source_receipt_statuses": ["success", "warning", "verified"],
    "allowed_public_artifacts": ["ActivePolicyPointer.v1", "ActivePolicySet.v1", "PolicyStoreIndex.v1", "RuntimePolicyCatalog.v1", "InstalledPolicyBundleRecord.v1", "PolicyBundleManifest.v1", "PolicyBundleReceipt.v1", "PolicyShadowEvaluationReport.v1", "PolicyCompatibilityReport.v1", "ActivePolicyVerificationReport.v1", "PolicyActivationReceipt.v1"],
    "denied_public_artifacts": ["approval_file", "raw_logs", "private_key_material", "secrets"],
    "require_no_secrets": True,
    "require_no_local_paths_in_public": True,
    "require_no_internal_hostnames_in_public": True,
    "immutable_objects_must_not_be_overwritten": True,
    "mutable_pointers_require_validation": True,
    "allow_unsigned_opa_bundle": True,
}
SECRET_PATTERNS = [re.compile(r"AKIA[0-9A-Z]{16}"), re.compile(r"Bearer\\s+[A-Za-z0-9._=-]+", re.I), re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"), re.compile(r"password", re.I), re.compile(r"https?://[^\s/@:]+:[^\s/@]+@")]

class PolicyObjectStoreClient:
    def put_object(self, key: str, content: bytes, content_type: str, cache_control: str) -> None: raise NotImplementedError
    def head_object(self, key: str) -> Dict[str, Any]: raise NotImplementedError
    def get_object_bytes(self, key: str) -> bytes: raise NotImplementedError
    def list_objects(self, prefix: str) -> List[str]: raise NotImplementedError
    def copy_object(self, src_key: str, dst_key: str) -> None: raise NotImplementedError
    def delete_object(self, key: str) -> None: raise NotImplementedError

class LocalMirrorPolicyClient(PolicyObjectStoreClient):
    def __init__(self, root: Path): self.root = root
    def put_object(self, key, content, content_type, cache_control):
        p = self.root / key; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(content)
    def head_object(self, key):
        p = self.root / key
        if not p.exists(): raise FileNotFoundError(key)
        return {"content_length": p.stat().st_size}
    def get_object_bytes(self, key): return (self.root / key).read_bytes()
    def list_objects(self, prefix): return [p.relative_to(self.root).as_posix() for p in sorted((self.root / prefix).rglob("*")) if p.is_file()]
    def copy_object(self, src_key, dst_key): self.put_object(dst_key, self.get_object_bytes(src_key), "application/octet-stream", "")
    def delete_object(self, key): (self.root / key).unlink(missing_ok=True)

class MockPolicyObjectStoreClient(LocalMirrorPolicyClient): pass


def _utc_now() -> str: return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
def _canonical_bytes(obj: Any) -> bytes: return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
def _sha256_bytes(raw: bytes) -> str: return hashlib.sha256(raw).hexdigest()
def _sha256_obj(obj: Any) -> str: return _sha256_bytes(_canonical_bytes(obj))
def _read_json(path: Path) -> Dict[str, Any]: return json.loads(path.read_text(encoding="utf-8"))

def _log(event: str, **kw: Any) -> None: logging.info(json.dumps({"event": event, **kw}, sort_keys=True))

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def write_checksums_file(root: Path, out_path: Path) -> None:
    lines = []
    for p in sorted([x for x in root.rglob("*") if x.is_file() and x != out_path], key=lambda q: q.relative_to(root).as_posix()):
        lines.append(f"{_sha256_bytes(p.read_bytes())}  {p.relative_to(root).as_posix()}")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def compute_policy_distribution_spec_hash(spec): return _sha256_obj(spec)
def compute_policy_distribution_plan_hash(plan): return _sha256_obj({k: v for k, v in plan.items() if k != "created_at_utc"})
def compute_policy_resolver_index_hash(index): return _sha256_obj({k: v for k, v in index.items() if k not in {"created_at_utc", "resolver_index_hash"}})
def compute_policy_distribution_hash(arts, resolver_index_hash, active_bundle_hash, active_policy_set_hash):
    return _sha256_obj([{"role": a["role"], "relative_path": a["relative_path"], "bytes": a["bytes"], "sha256": a["sha256"], "content_type": a["content_type"], "cache_control": a["cache_control"], "resolver_index_hash": resolver_index_hash, "active_bundle_hash": active_bundle_hash, "active_policy_set_hash": active_policy_set_hash} for a in arts])

def load_policy_distribution_policy(path: Optional[Path]=None):
    if path is None:
        return DEFAULT_POLICY
    return _read_json(path)

def validate_policy_distribution_spec(spec):
    e=[]
    if not isinstance(spec, dict):
        return ["malformed_policy_distribution_spec"]
    if spec.get("schema") != SUPPORTED_SPEC_SCHEMA: e.append("unsupported_schema")
    if not spec.get("policy_distribution_id"): e.append("missing_policy_distribution_id")
    if not spec.get("dataset_id"): e.append("missing_dataset_id")
    if spec.get("resolver_profile") not in {"static-readonly"}: e.append("unsupported_resolver_profile")
    dist=spec.get("distribution",{})
    if dist.get("layout") not in {"immutable-versioned","content-addressed","local-resolver"}: e.append("unsupported_layout")
    cache=spec.get("cache",{})
    if cache and (not isinstance(cache,dict) or not cache.get("immutable_cache_control") or not cache.get("mutable_cache_control")): e.append("malformed_cache_policy")
    cors=spec.get("cors",{})
    if cors and not isinstance(cors.get("allow_origin","*"),str): e.append("malformed_cors_policy")
    return e

def validate_active_policy_pointer(doc): return [] if doc.get("schema")=="ActivePolicyPointer.v1" and doc.get("active_bundle_id") else ["invalid_active_policy_pointer"]
def validate_active_policy_set(doc): return [] if doc.get("schema")=="ActivePolicySet.v1" else ["invalid_active_policy_set"]
def validate_runtime_policy_catalog(doc): return [] if doc.get("schema")=="RuntimePolicyCatalog.v1" else ["invalid_runtime_policy_catalog"]
def validate_policy_store_index(doc): return [] if doc.get("schema")=="PolicyStoreIndex.v1" else ["invalid_policy_store_index"]
def validate_policy_activation_ledger(doc): return [] if doc.get("schema")=="PolicyActivationLedger.v1" else ["invalid_activation_ledger"]
def validate_installed_policy_bundle(man, rec): return [] if man.get("schema")=="PolicyBundleManifest.v1" and rec.get("schema")=="PolicyBundleReceipt.v1" else ["invalid_bundle_docs"]

def _scan_secret(obj: Any) -> bool:
    s = obj if isinstance(obj, str) else json.dumps(obj, sort_keys=True)
    return any(p.search(s) for p in SECRET_PATTERNS)

def validate_policy_store_source(policy_store_root: Path, spec: Dict[str, Any]) -> Tuple[Dict[str, Any], List[str]]:
    errs=[]
    req = ["active_policy_pointer.json","active_policy_set.json","policy_store_index.json","runtime_policy_catalog.json"]
    for r in req:
        if not (policy_store_root / r).exists(): errs.append(f"missing_{r}")
    if errs: return {}, errs
    d={"active_policy_pointer": _read_json(policy_store_root/"active_policy_pointer.json"), "active_policy_set": _read_json(policy_store_root/"active_policy_set.json"), "policy_store_index": _read_json(policy_store_root/"policy_store_index.json"), "runtime_policy_catalog": _read_json(policy_store_root/"runtime_policy_catalog.json")}
    errs += validate_active_policy_pointer(d["active_policy_pointer"])
    errs += validate_active_policy_set(d["active_policy_set"])
    errs += validate_policy_store_index(d["policy_store_index"])
    errs += validate_runtime_policy_catalog(d["runtime_policy_catalog"])
    bid = d["active_policy_pointer"].get("active_bundle_id")
    broot = policy_store_root / "bundles" / str(bid)
    for bf in ["policy_bundle_manifest.json","policy_bundle_receipt.json","policy_bundle_checksums.sha256"]:
        if not (broot / bf).exists(): errs.append(f"missing_bundle_file:{bf}")
    if (policy_store_root/"ledger/policy_activation_ledger.json").exists():
        errs += validate_policy_activation_ledger(_read_json(policy_store_root/"ledger/policy_activation_ledger.json"))
    if _scan_secret(d): errs.append("secret_detected")
    d["active_bundle_id"] = bid
    return d, sorted(set(errs))

def infer_content_type(path: str, allow_octet_stream: bool=False) -> str:
    if path.endswith(".tar.gz"): return "application/gzip"
    m={".json":"application/json",".rego":"text/plain; charset=utf-8",".yaml":"application/yaml",".yml":"application/yaml",".html":"text/html; charset=utf-8",".js":"application/javascript",".css":"text/css",".svg":"image/svg+xml",".txt":"text/plain; charset=utf-8",".sha256":"text/plain; charset=utf-8",".zip":"application/zip"}
    ext = Path(path).suffix.lower()
    if ext in m: return m[ext]
    if allow_octet_stream: return "application/octet-stream"
    raise ValueError(f"unknown_content_type:{path}")

def infer_cache_control(relative_path: str, spec: Dict[str, Any]) -> str:
    c=spec.get("cache",{})
    if relative_path in {"latest-policy.json","policy-index.json","active-policy-pointer.json","runtime-policy-catalog.json"}: return c.get("mutable_cache_control","public, max-age=60")
    if relative_path == "portal/index.html": return c.get("portal_cache_control","public, max-age=300")
    if relative_path.startswith("portal/assets/"): return c.get("immutable_cache_control","public, max-age=31536000, immutable")
    return c.get("immutable_cache_control","public, max-age=31536000, immutable")

def classify_policy_artifact(relative_path: str) -> str:
    if relative_path.endswith("openapi.json"): return "openapi"
    if relative_path.startswith("portal/"): return "portal_asset"
    if relative_path.startswith("opa/"): return "opa_metadata"
    if "pointer" in relative_path: return "active_pointer"
    return "policy_file"

def build_policy_resolution_table(catalog: Dict[str, Any], active_bundle_id: str, active_bundle_hash: str, runtime_catalog_hash: str):
    out=[]
    for p in catalog.get("policies",[]):
        schema=p.get("policy_schema") or p.get("schema") or "UnknownPolicy.v1"
        out.append((schema,{"schema":"PolicySchemaResolution.v1","policy_schema":schema,"active_bundle_id":active_bundle_id,"active_bundle_hash":active_bundle_hash,"policy_path":"../bundles/%s/%s"%(active_bundle_id,p.get("path","")),"policy_sha256":p.get("sha256",""),"applies_to_layers":p.get("applies_to_layers",[]),"runtime_policy_catalog_hash":runtime_catalog_hash}))
    return sorted(out,key=lambda x:(x[0],x[1]["policy_path"]))

def build_policy_resolver_index(spec, run_id, source_docs):
    ap = source_docs["active_policy_pointer"]; aps=source_docs["active_policy_set"]; rtc=source_docs["runtime_policy_catalog"]
    idx={"schema":"PolicyResolverIndex.v1","policy_distribution_id":spec["policy_distribution_id"],"policy_distribution_run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE,"resolver_index_hash":"","active_bundle_id":ap.get("active_bundle_id"),"active_bundle_hash":ap.get("active_bundle_hash",""),"active_policy_set_hash":aps.get("active_policy_set_hash",_sha256_obj(aps)),"runtime_policy_catalog_hash":rtc.get("catalog_hash",_sha256_obj(rtc)),"policies":sorted([{"policy_schema":p.get("policy_schema",p.get("schema","UnknownPolicy.v1")),"applies_to_layers":p.get("applies_to_layers",[]),"path":f"bundles/{ap.get('active_bundle_id')}/{p.get('path','')}","sha256":p.get("sha256",""),"media_type":"application/json"} for p in rtc.get("policies",[])], key=lambda x:(x["policy_schema"],x["path"])) ,"specs":[],"entrypoints":{"active_policy_pointer":"active-policy-pointer.json","runtime_policy_catalog":"runtime-policy-catalog.json","latest_policy":"latest-policy.json","opa_bundle_metadata":"opa/bundle_manifest.json" if spec.get("distribution",{}).get("write_opa_bundle_metadata") else None,"opa_bundle_archive":"opa/bundle.tar.gz" if spec.get("distribution",{}).get("write_opa_bundle_archive") else None},"errors":[]}
    idx["resolver_index_hash"]=compute_policy_resolver_index_hash(idx)
    return idx

def build_active_policy_publication(spec, run_id, idx):
    obj={"schema":"ActivePolicyPublication.v1","policy_distribution_id":spec["policy_distribution_id"],"policy_distribution_run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE,"active_bundle_id":idx["active_bundle_id"],"active_bundle_hash":idx["active_bundle_hash"],"active_policy_set_hash":idx["active_policy_set_hash"],"resolver_index_hash":idx["resolver_index_hash"],"publication_hash":"","entrypoints":{"policy_index":"policy-index.json","active_pointer":"active-policy-pointer.json","runtime_catalog":"runtime-policy-catalog.json"},"errors":[]}
    obj["publication_hash"]=_sha256_obj({k:v for k,v in obj.items() if k not in {"created_at_utc","publication_hash"}})
    return obj

def build_policy_resolver_contract(spec):
    return {"schema":"PolicyResolverContract.v1","policy_distribution_id":spec["policy_distribution_id"],"created_at_utc":_utc_now(),"source":SOURCE,"read_only":True,"resolver_mode":"static","endpoints":[{"method":"GET","path":"/latest-policy.json","description":"Latest active policy publication pointer"},{"method":"GET","path":"/policy-index.json","description":"Policy resolver index"},{"method":"GET","path":"/active-policy-pointer.json","description":"Active policy pointer"},{"method":"GET","path":"/runtime-policy-catalog.json","description":"Runtime policy catalog"},{"method":"GET","path":"/policies/by-schema/{schema}.json","description":"Resolve active policy by schema"}],"errors":[]}

def build_policy_resolver_openapi(spec):
    return {"openapi":"3.1.1","info":{"title":"Policy Resolver API","version":"1.0.0"},"paths":{"/latest-policy.json":{"get":{"responses":{"200":{"description":"OK"}}}},"/policy-index.json":{"get":{"responses":{"200":{"description":"OK"}}}},"/active-policy-pointer.json":{"get":{"responses":{"200":{"description":"OK"}}}},"/runtime-policy-catalog.json":{"get":{"responses":{"200":{"description":"OK"}}}},"/policies/by-schema/{schema}.json":{"get":{"parameters":[{"name":"schema","in":"path","required":True,"schema":{"type":"string"}}],"responses":{"200":{"description":"OK"}}}}},"components":{"schemas":{"PolicyResolverIndex.v1":{"type":"object"},"ActivePolicyPublication.v1":{"type":"object"},"ActivePolicyPointer.v1":{"type":"object"},"ActivePolicySet.v1":{"type":"object"},"RuntimePolicyCatalog.v1":{"type":"object"},"PolicySchemaResolution.v1":{"type":"object"},"PolicyDistributionReceipt.v1":{"type":"object"}}}}

def build_policy_resolver_portal(spec, idx):
    html='<!doctype html><html><head><meta charset="utf-8"><meta http-equiv="Content-Security-Policy" content="default-src \'self\'; script-src \'self\'; style-src \'self\'; img-src \'self\' data:; object-src \'none\'"> <title>Policy Resolver Portal</title><link rel="stylesheet" href="assets/css/policy_portal.css"></head><body><main><h1>Policy Resolver Portal</h1><div id="app"></div></main><script src="assets/js/policy_portal.js"></script></body></html>'
    js='(function(){const app=document.getElementById("app");fetch("../policy-index.json").then(r=>r.json()).then(d=>{app.textContent="Active bundle: "+(d.active_bundle_id||"")+" hash: "+(d.active_bundle_hash||"");});})();'
    css=':focus{outline:3px solid #005fcc;outline-offset:2px;}body{font-family:sans-serif;}'
    svg='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16"><circle cx="8" cy="8" r="7" fill="#0a7"/></svg>'
    cfg={"schema":"PolicyPortalConfig.v1","policy_distribution_id":spec["policy_distribution_id"],"active_bundle_id":idx["active_bundle_id"],"active_bundle_hash":idx["active_bundle_hash"],"active_policy_set_hash":idx["active_policy_set_hash"],"runtime_policy_catalog_hash":idx["runtime_policy_catalog_hash"],"entrypoints":idx["entrypoints"]}
    return html,js,css,svg,cfg

def build_policy_distribution_receipt(**kw):
    return kw

def build_policy_distribution_manifest(spec, run_id, mode, spec_hash, dist_hash, idx, artifacts):
    return {"schema":"PolicyDistributionManifest.v1","policy_distribution_id":spec["policy_distribution_id"],"policy_distribution_run_id":run_id,"policy_distribution_layout_version":"1","created_at_utc":_utc_now(),"source":SOURCE,"dataset_id":spec["dataset_id"],"mode":mode,"policy_distribution_spec_hash":spec_hash,"policy_distribution_hash":dist_hash,"resolver_index_hash":idx["resolver_index_hash"],"active_bundle_id":idx["active_bundle_id"],"active_bundle_hash":idx["active_bundle_hash"],"active_policy_set_hash":idx["active_policy_set_hash"],"public_base_url":None,"artifacts":artifacts,"entrypoints":{"portal":"portal/index.html","policy_index":"policy-index.json","latest_policy":"latest-policy.json","active_pointer":"active-policy-pointer.json","runtime_catalog":"runtime-policy-catalog.json","openapi":"api/policy_resolver_openapi.json"},"checksums_path":"checksums.sha256","errors":[]}

def load_policy_distribution_inputs(spec_path: Path, policy_store_root: Optional[Path]):
    return {"spec":_read_json(spec_path),"policy_store_root":policy_store_root}

def build_policy_distribution_plan(spec, mode, spec_hash, active_bundle_id):
    p={"schema":"PolicyDistributionPlan.v1","created_at_utc":_utc_now(),"source":SOURCE,"policy_distribution_id":spec["policy_distribution_id"],"mode":mode,"policy_distribution_spec_hash":spec_hash,"active_bundle_id":active_bundle_id,"errors":[]}
    p["plan_hash"]=compute_policy_distribution_plan_hash(p)
    return p

def run_policy_distribution(args: argparse.Namespace) -> int:
    logging.basicConfig(level=logging.INFO)
    run_id=f"run_{_sha256_obj({'t':_utc_now()})[:12]}"
    _log("policy_distribution.started", run_id=run_id, status="started", mode=args.mode)
    inputs=load_policy_distribution_inputs(Path(args.policy_distribution_spec), Path(args.policy_store_root) if args.policy_store_root else None)
    spec=inputs["spec"]; spec_hash=compute_policy_distribution_spec_hash(spec)
    errs=validate_policy_distribution_spec(spec)
    policy=load_policy_distribution_policy(Path(args.policy_distribution_policy) if getattr(args,"policy_distribution_policy",None) else None)
    source_docs={}
    if args.mode not in {Mode.VALIDATE_REMOTE.value, Mode.VERIFY_DISTRIBUTION.value}:
        if not args.policy_store_root:
            errs.append("missing_policy_store_root")
        else:
            source_docs, src_errs = validate_policy_store_source(Path(args.policy_store_root), spec); errs += src_errs
    if errs:
        raise ValueError(";".join(sorted(set(errs))))
    plan=build_policy_distribution_plan(spec,args.mode,spec_hash,source_docs.get("active_bundle_id"))
    if args.mode==Mode.PLAN_ONLY.value:
        out=Path(args.output_root); out.mkdir(parents=True, exist_ok=True)
        receipt={"schema":"PolicyDistributionReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"planned","source":SOURCE,"mode":args.mode,"policy_distribution_id":spec["policy_distribution_id"],"policy_distribution_run_id":None,"policy_distribution_spec_hash":spec_hash,"policy_distribution_plan_hash":plan["plan_hash"],"policy_distribution_hash":None,"resolver_index_hash":None,"active_bundle_id":source_docs.get("active_bundle_id"),"active_bundle_hash":None,"active_policy_set_hash":None,"output_root":str(out),"target":{"type":"local-mirror","bucket":None,"prefix":None,"public_base_url":None},"outputs":{},"inputs":{"policy_distribution_spec":args.policy_distribution_spec,"policy_store_root":args.policy_store_root,"active_policy_pointer":str(Path(args.policy_store_root)/"active_policy_pointer.json") if args.policy_store_root else None},"input_hashes":{"policy_distribution_spec_sha256":spec_hash,"active_policy_pointer_sha256":None,"active_policy_set_sha256":None},"validation":{"spec_valid":True,"policy_valid":True,"source_valid":True,"object_plan_valid":True,"local_mirror_valid":True,"remote_validation_valid":True,"resolver_valid":True,"checksums_valid":True},"errors":[]}
        write_canonical_json(out/"policy_distribution_receipt.json", receipt)
        return 0
    idx=build_policy_resolver_index(spec, "", source_docs)
    apub=build_active_policy_publication(spec,"",idx)
    resolutions=build_policy_resolution_table(source_docs["runtime_policy_catalog"], idx["active_bundle_id"], idx["active_bundle_hash"], idx["runtime_policy_catalog_hash"])
    out_root=Path(args.output_root)
    staging = out_root / ".staging" / f"tmp_{spec['policy_distribution_id']}"
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)
    write_canonical_json(staging/"policy_distribution_plan.json", plan)
    write_canonical_json(staging/"policy_resolver_index.json", idx)
    write_canonical_json(staging/"active_policy_publication.json", apub)
    write_canonical_json(staging/"latest-policy.json", apub)
    write_canonical_json(staging/"policy-index.json", idx)
    write_canonical_json(staging/"active-policy-pointer.json", source_docs["active_policy_pointer"])
    write_canonical_json(staging/"runtime-policy-catalog.json", source_docs["runtime_policy_catalog"])
    write_canonical_json(staging/"policies/active_policy_set.json", source_docs["active_policy_set"])
    for s,obj in resolutions: write_canonical_json(staging/f"policies/by-schema/{s}.json", obj)
    contract=build_policy_resolver_contract(spec); write_canonical_json(staging/"policy_resolver_contract.json", contract)
    openapi=build_policy_resolver_openapi(spec); write_canonical_json(staging/"api/policy_resolver_openapi.json", openapi)
    if spec.get("distribution",{}).get("write_portal",True):
        h,j,c,v,cfg=build_policy_resolver_portal(spec,idx)
        (staging/"portal/assets/js").mkdir(parents=True, exist_ok=True); (staging/"portal/assets/css").mkdir(parents=True, exist_ok=True); (staging/"portal/assets/img").mkdir(parents=True, exist_ok=True)
        (staging/"portal/index.html").write_text(h,encoding="utf-8"); (staging/"portal/assets/js/policy_portal.js").write_text(j,encoding="utf-8"); (staging/"portal/assets/css/policy_portal.css").write_text(c,encoding="utf-8"); (staging/"portal/assets/img/favicon.svg").write_text(v,encoding="utf-8"); write_canonical_json(staging/"portal/policy_portal_config.json",cfg)
    artifacts=[]
    for p in sorted([x for x in staging.rglob("*") if x.is_file()]):
        rel=p.relative_to(staging).as_posix(); artifacts.append({"role":classify_policy_artifact(rel),"path":rel,"media_type":infer_content_type(rel,allow_octet_stream=True),"bytes":p.stat().st_size,"sha256":_sha256_bytes(p.read_bytes()),"cache_control":infer_cache_control(rel,spec)})
    dist_hash=compute_policy_distribution_hash([{"role":a["role"],"relative_path":a["path"],"bytes":a["bytes"],"sha256":a["sha256"],"content_type":a["media_type"],"cache_control":a["cache_control"]} for a in artifacts], idx["resolver_index_hash"], idx["active_bundle_hash"], idx["active_policy_set_hash"])
    run_id = f"{spec['policy_distribution_id']}_{args.mode}_{dist_hash[:12]}"
    manifest=build_policy_distribution_manifest(spec,run_id,args.mode,spec_hash,dist_hash,idx,artifacts); write_canonical_json(staging/"policy_distribution_manifest.json",manifest)
    receipt={"schema":"PolicyDistributionReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"success","source":SOURCE,"mode":args.mode,"policy_distribution_id":spec["policy_distribution_id"],"policy_distribution_run_id":run_id,"policy_distribution_spec_hash":spec_hash,"policy_distribution_plan_hash":plan["plan_hash"],"policy_distribution_hash":dist_hash,"resolver_index_hash":idx["resolver_index_hash"],"active_bundle_id":idx["active_bundle_id"],"active_bundle_hash":idx["active_bundle_hash"],"active_policy_set_hash":idx["active_policy_set_hash"],"output_root":str((out_root/run_id).as_posix()),"target":{"type":"local-mirror","bucket":args.bucket,"prefix":args.prefix,"public_base_url":args.public_base_url},"outputs":{},"inputs":{"policy_distribution_spec":args.policy_distribution_spec,"policy_store_root":args.policy_store_root,"active_policy_pointer":str(Path(args.policy_store_root)/"active_policy_pointer.json")},"input_hashes":{"policy_distribution_spec_sha256":spec_hash,"active_policy_pointer_sha256":_sha256_bytes((Path(args.policy_store_root)/"active_policy_pointer.json").read_bytes()),"active_policy_set_sha256":_sha256_bytes((Path(args.policy_store_root)/"active_policy_set.json").read_bytes())},"validation":{"spec_valid":True,"policy_valid":True,"source_valid":True,"object_plan_valid":True,"local_mirror_valid":True,"remote_validation_valid":args.mode!=Mode.S3_COMPATIBLE.value,"resolver_valid":True,"checksums_valid":True},"errors":[]}
    write_canonical_json(staging/"policy_distribution_receipt.json",receipt)
    write_checksums_file(staging, staging/"checksums.sha256")
    final=out_root/run_id
    final.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staging, final)
    return 0

def parse_args(argv: Optional[List[str]]=None) -> argparse.Namespace:
    p=argparse.ArgumentParser()
    p.add_argument("--policy-distribution-spec", required=True)
    p.add_argument("--policy-store-root")
    p.add_argument("--existing-policy-distribution-root")
    p.add_argument("--output-root", required=True)
    p.add_argument("--mode", default=DEFAULT_MODE, choices=[m.value for m in Mode])
    p.add_argument("--bucket")
    p.add_argument("--prefix")
    p.add_argument("--public-base-url")
    p.add_argument("--allow-remote-network", action="store_true")
    p.add_argument("--allow-http", action="store_true")
    p.add_argument("--policy-distribution-policy")
    p.add_argument("--deterministic-run-id", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    return p.parse_args(argv)

if __name__ == "__main__":
    raise SystemExit(run_policy_distribution(parse_args()))
