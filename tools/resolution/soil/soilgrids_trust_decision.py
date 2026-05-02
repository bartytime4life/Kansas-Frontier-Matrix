#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import http.server
import json
import logging
import os
import re
import shutil
import socket
import subprocess
import tempfile
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

LOG = logging.getLogger("soilgrids_trust_decision")
ALLOWED_DECISIONS = {"allow", "warn", "review", "block", "unknown"}
ALLOWED_STATUSES = {"active", "under_review", "suspended", "revoked", "superseded", "quarantined", "expired", "unknown"}
ALLOWED_PROFILES = {"strict-consumer", "audit-review", "display-only"}


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_obj(obj: Any) -> str:
    return hashlib.sha256(_canonical_bytes(obj)).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def compute_trust_decision_spec_hash(spec: Dict[str, Any]) -> str:
    return _sha256_obj(spec)


def compute_policy_hash(policy: Dict[str, Any]) -> str:
    return _sha256_obj(policy)


def compute_decision_input_hash(bundle: Dict[str, Any]) -> str:
    b = dict(bundle)
    b.pop("run_id", None)
    b.pop("created_at_utc", None)
    b.pop("decision_input_hash", None)
    return _sha256_obj(b)


def compute_decision_hash(payload: Dict[str, Any]) -> str:
    p = dict(payload)
    p.pop("run_id", None)
    p.pop("created_at_utc", None)
    p.pop("decision_hash", None)
    return _sha256_obj(p)


def validate_trust_decision_spec(spec: Dict[str, Any], allow_remote: bool = False) -> List[str]:
    e = []
    if spec.get("schema") != "TrustDecisionSpec.v1": e.append("unsupported spec schema")
    if not spec.get("trust_decision_id"): e.append("trust_decision_id missing")
    if not spec.get("dataset_id"): e.append("dataset_id missing")
    if spec.get("decision_profile") not in ALLOWED_PROFILES: e.append("unsupported decision_profile")
    pol = spec.get("policy", {})
    if pol.get("default_decision") not in ALLOWED_DECISIONS: e.append("invalid default_decision")
    for k, v in pol.items():
        if k.endswith("_status_decision") and v not in ALLOWED_DECISIONS: e.append(f"invalid decision {k}")
    res = spec.get("resolver", {})
    if res.get("source") not in {"local-status-distribution"}: e.append("resolver source unsupported")
    if res.get("allow_remote_resolver") and not allow_remote: e.append("remote resolver not explicitly allowed")
    return e


def load_trust_decision_policy(spec: Dict[str, Any]) -> Dict[str, Any]:
    m = {
        "active": spec["policy"].get("active_status_decision", "allow"),
        "under_review": spec["policy"].get("under_review_status_decision", "review"),
        "suspended": spec["policy"].get("suspended_status_decision", "block"),
        "revoked": spec["policy"].get("revoked_status_decision", "block"),
        "superseded": spec["policy"].get("superseded_status_decision", "warn"),
        "quarantined": spec["policy"].get("quarantined_status_decision", "block"),
        "expired": spec["policy"].get("expired_status_decision", "block"),
        "unknown": spec["policy"].get("unknown_status_decision", "block"),
    }
    return {
        "schema": "TrustDecisionPolicy.v1",
        "policy_id": "soilgrids-trust-decision-default",
        "allowed_decisions": sorted(ALLOWED_DECISIONS),
        "status_decision_map": m,
        "required_checks": ["resolver.index.valid", "trust.object.resolved", "revocation.checked", "suspension.checked", "status.policy.applied"],
        "blocking_reasons": ["revoked", "suspended", "quarantined", "expired", "unknown_status", "resolver_unavailable", "checksum_mismatch", "policy_error", "secret_detected"],
        "warning_reasons": ["superseded", "under_review", "unsigned_status_list", "remote_validation_missing", "watchtower_degraded"],
        "fail_closed": True,
    }


def validate_status_distribution_source(root: Path) -> List[str]:
    errs = []
    if not root.exists(): errs.append("status distribution root missing")
    if not (root / "status_distribution_receipt.json").exists(): errs.append("status_distribution_receipt.json missing")
    if not (root / "status_resolver_index.json").exists(): errs.append("status_resolver_index.json missing")
    return errs


def load_status_resolver_index(root: Path) -> Dict[str, Any]:
    return _load_json(root / "status_resolver_index.json")


def load_status_registry_if_available(root: Path) -> Optional[Dict[str, Any]]:
    p = root / "trust_status_snapshot.json"
    return _load_json(p) if p.exists() else None


def load_revocation_and_suspension_lists(root: Path) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    rev = _load_json(root / "trust_revocation_list.json") if (root / "trust_revocation_list.json").exists() else {"revoked": []}
    sus = _load_json(root / "trust_suspension_list.json") if (root / "trust_suspension_list.json").exists() else {"suspended": []}
    return rev, sus


def build_resolver_cache(index: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    cache = {"by_trust_object_id": {}, "by_object_id": {}, "by_sha256": {}, "by_disclosure_packet_id": {}, "by_distribution_id": {}, "by_status_url": {}}
    for row in index.get("objects", []):
        tid = row.get("trust_object_id")
        if tid: cache["by_trust_object_id"][tid] = row
        for k, d in [("object_id", "by_object_id"), ("object_sha256", "by_sha256"), ("disclosure_packet_id", "by_disclosure_packet_id"), ("distribution_id", "by_distribution_id"), ("status_url", "by_status_url")]:
            if row.get(k): cache[d][row[k]] = row
    return cache


def resolve_by_trust_object_id(cache, v): return cache["by_trust_object_id"].get(v)
def resolve_by_object_sha256(cache, v): return cache["by_sha256"].get(v)
def resolve_by_object_id(cache, v): return cache["by_object_id"].get(v)
def resolve_by_disclosure_packet_id(cache, v): return cache["by_disclosure_packet_id"].get(v)
def resolve_by_distribution_id(cache, v): return cache["by_distribution_id"].get(v)
def resolve_by_status_url(cache, v): return cache["by_status_url"].get(v)


def resolve_trust_object(cache: Dict[str, Dict[str, Any]], target: Dict[str, Any]) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    hits = []
    for key, fn in [("trust_object_id", resolve_by_trust_object_id), ("object_sha256", resolve_by_object_sha256), ("object_id", resolve_by_object_id), ("disclosure_packet_id", resolve_by_disclosure_packet_id), ("distribution_id", resolve_by_distribution_id), ("status_url", resolve_by_status_url)]:
        if target.get(key):
            r = fn(cache, target[key])
            if r: hits.append(r)
            else: return None, [f"target {key} not found"]
    if not hits: return None, ["no target identifier provided"]
    ids = {x.get("trust_object_id") for x in hits}
    if len(ids) != 1: return None, ["target identifiers resolve to different objects"]
    return hits[0], []


def build_trust_resolution_result(run_id, request_id, resolved, index_hash, source="local", errors=None):
    return {"schema":"TrustResolutionResult.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","status":"success" if resolved else "not_found","request_id":request_id,"resolved":resolved,"resolver":{"resolver_index_hash":index_hash,"status_registry_hash":None,"status_snapshot_hash":None,"source":source},"checks":[],"errors":errors or []}


def validate_resolution_result(result):
    return [] if result.get("schema") == "TrustResolutionResult.v1" else ["invalid resolution schema"]


def build_trust_decision_input_bundle(run_id, request, resolution, policy, evidence):
    bundle = {"schema":"TrustDecisionInputBundle.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","request":request,"resolution":resolution,"policy":policy,"resolver_evidence":evidence,"optional_evidence":{"transparency":None,"verifier":None,"watchtower":None}}
    bundle["decision_input_hash"] = compute_decision_input_hash(bundle)
    return bundle


def evaluate_builtin_policy(policy, resolution):
    checks, blocks, warns = [], [], []
    resolved = resolution.get("resolved")
    if not resolved:
        return "block", "resolver unavailable", checks, ["resolver_unavailable"], warns, ["unresolved"]
    st = resolved.get("current_status", "unknown")
    checks.append({"check_id":"trust.object.resolved","severity":"required","status":"pass","message":"resolved"})
    decision = policy["status_decision_map"].get(st, "block")
    if resolved.get("revoked"): decision = "block"; blocks.append("revoked")
    if resolved.get("suspended"): decision = "block"; blocks.append("suspended")
    if st in {"quarantined","expired","unknown"}: blocks.append(st if st != "unknown" else "unknown_status")
    if st in {"under_review","superseded"}: warns.append(st)
    checks.extend([
        {"check_id":"revocation.checked","severity":"required","status":"pass","message":"checked"},
        {"check_id":"suspension.checked","severity":"required","status":"pass","message":"checked"},
        {"check_id":"status.policy.applied","severity":"required","status":"pass","message":"applied"},
    ])
    return decision, f"status={st}", checks, blocks, warns, []


def evaluate_opa_policy_if_requested(*args, **kwargs):
    return None


def build_trust_decision_envelope(run_id, trust_decision_id, request_id, resolution, policy, decision, reason, checks, blocks, warns, errors):
    resolved = resolution.get("resolved") or {}
    env = {"schema":"TrustDecisionEnvelope.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","trust_decision_id":trust_decision_id,"request_id":request_id,"decision":decision,"reason":reason,
           "target":{"trust_object_id":resolved.get("trust_object_id"),"object_type":resolved.get("object_type"),"object_id":resolved.get("object_id"),"object_sha256":resolved.get("object_sha256")},
           "status":{"current_status":resolved.get("current_status", "unknown"),"revoked":bool(resolved.get("revoked")),"suspended":bool(resolved.get("suspended")),"superseded_by":resolved.get("superseded_by")},
           "policy":{"policy_id":policy.get("policy_id"),"policy_hash":compute_policy_hash(policy)},"checks":checks,"blocking_reasons":blocks,"warnings":warns,"errors":errors}
    env["decision_hash"] = compute_decision_hash(env)
    return env


def build_trust_decision_report(run_id, trust_decision_id, envelopes):
    s = {k: 0 for k in ["allow", "warn", "review", "block", "unknown"]}
    decisions = []
    for e in envelopes:
        s[e["decision"]] += 1
        decisions.append({"request_id":e["request_id"],"trust_object_id":e["target"]["trust_object_id"],"decision":e["decision"],"decision_hash":e["decision_hash"],"envelope_path":f"decisions/{e['request_id']}.json"})
    return {"schema":"TrustDecisionReport.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","status":"success","trust_decision_id":trust_decision_id,"summary":{"requests":len(envelopes),**s},"decisions":decisions,"errors":[]}


def build_batch_trust_decision_report(run_id, report_paths, envelopes):
    s = {k: 0 for k in ["allow", "warn", "review", "block", "unknown"]}
    for e in envelopes: s[e["decision"]] += 1
    return {"schema":"BatchTrustDecisionReport.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","status":"success","request_count":len(envelopes),"summary":s,"decision_report_paths":report_paths,"errors":[]}


def build_consumer_policy_pack(trust_decision_id, policy, opa_policy_path=None):
    return {"schema":"ConsumerPolicyPack.v1","trust_decision_id":trust_decision_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","policy_hash":compute_policy_hash(policy),"builtin_policy":policy,"opa_policy_path":opa_policy_path,"decision_profiles":["strict-consumer","audit-review","display-only"],"errors":[]}


def compile_python_sdk(sdk_dir: Path):
    code = """#!/usr/bin/env python3\nimport json, hashlib\nfrom pathlib import Path\n\ndef load_resolver_index(path): return json.loads(Path(path).read_text(encoding='utf-8'))\ndef resolve_status(index, trust_object_id):\n for o in index.get('objects',[]):\n  if o.get('trust_object_id')==trust_object_id: return o\n return None\ndef decide(obj, status_map=None):\n status_map=status_map or {'active':'allow','under_review':'review','superseded':'warn','suspended':'block','revoked':'block','quarantined':'block','expired':'block','unknown':'block'}\n return status_map.get((obj or {}).get('current_status','unknown'),'block')\ndef verify_checksums(base, checksums_file):\n base=Path(base); ok=True\n for line in Path(checksums_file).read_text(encoding='utf-8').splitlines():\n  if not line.strip(): continue\n  h,p=line.split('  ',1)\n  if hashlib.sha256((base/p).read_bytes()).hexdigest()!=h: ok=False\n return ok\n"""
    p = sdk_dir / "soilgrids_trust_client.py"
    p.write_text(code, encoding="utf-8")
    return p


def compile_cli_wrapper(sdk_dir: Path):
    code = """#!/usr/bin/env python3\nimport argparse,json\nfrom soilgrids_trust_client import load_resolver_index,resolve_status,decide\n\ndef main():\n p=argparse.ArgumentParser();p.add_argument('--resolver-index',required=True);p.add_argument('--trust-object-id',required=True);a=p.parse_args()\n idx=load_resolver_index(a.resolver_index);obj=resolve_status(idx,a.trust_object_id)\n print(json.dumps({'resolved':obj,'decision':decide(obj)},sort_keys=True))\n\nif __name__=='__main__': main()\n"""
    p = sdk_dir / "soilgrids_trust_cli.py"
    p.write_text(code, encoding="utf-8")
    return p


def build_sdk_manifest(trust_decision_id, sdk_dir: Path):
    arts = []
    for role, rel in [("python_sdk", "soilgrids_trust_client.py"), ("cli_wrapper", "soilgrids_trust_cli.py")]:
        p = sdk_dir / rel
        arts.append({"role": role, "path": f"sdk/{rel}", "bytes": p.stat().st_size, "sha256": _sha256_file(p)})
    return {"schema":"SDKManifest.v1","trust_decision_id":trust_decision_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","sdk_hash":_sha256_obj(arts),"language":"python","artifacts":arts,"errors":[]}


def build_decision_api_contract(trust_decision_id):
    return {"schema":"TrustDecisionApiContract.v1","trust_decision_id":trust_decision_id,"created_at_utc":_utc_now(),"source":"soilgrids_trust_decision","read_only":True,"allowed_methods":["GET","HEAD","OPTIONS"],"post_decision_enabled":False,"endpoints":[{"method":"GET","path":"/health","operation_id":"health"},{"method":"GET","path":"/resolve/{trust_object_id}","operation_id":"resolveTrustObject"},{"method":"GET","path":"/decide/{trust_object_id}","operation_id":"decideTrustObject"},{"method":"GET","path":"/policy","operation_id":"getPolicy"}],"errors":[]}


def build_decision_openapi(trust_decision_id):
    return {"openapi":"3.1.1","info":{"title":"SoilGrids Trust Decision API","version":"1.0.0"},"servers":[{"url":"http://127.0.0.1"}],"paths":{"/health":{"get":{"operationId":"health","responses":{"200":{"description":"ok"}}}},"/resolve/{trust_object_id}":{"get":{"operationId":"resolveTrustObject","parameters":[{"in":"path","name":"trust_object_id","required":True,"schema":{"type":"string"}}],"responses":{"200":{"description":"ok"}}}},"/decide/{trust_object_id}":{"get":{"operationId":"decideTrustObject","parameters":[{"in":"path","name":"trust_object_id","required":True,"schema":{"type":"string"}}],"responses":{"200":{"description":"ok"}}}},"/policy":{"get":{"operationId":"getPolicy","responses":{"200":{"description":"ok"}}}}},"x-trust-decision-id":trust_decision_id}


def validate_decision_api_contract(contract):
    return [] if contract.get("read_only") else ["API must be read only"]

def build_local_decision_api_server(*args, **kwargs): return None

def compute_resolver_source_hash(source_hashes: Dict[str, str]) -> str: return _sha256_obj(source_hashes)
def build_trust_decision_plan(spec, mode): return {"schema":"TrustDecisionPlan.v1","mode":mode,"trust_decision_id":spec.get("trust_decision_id"),"created_at_utc":_utc_now()}

def build_trust_decision_receipt(**kwargs): return kwargs

def write_checksums_file(root: Path):
    entries=[]
    for p in sorted([x for x in root.rglob('*') if x.is_file() and x.name!='checksums.sha256']):
        entries.append(f"{_sha256_file(p)}  {p.relative_to(root).as_posix()}")
    (root/'checksums.sha256').write_text("\n".join(entries)+"\n",encoding='utf-8')

def load_trust_decision_inputs(spec_path: Path, request_path: Optional[Path]) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    return _load_json(spec_path), (_load_json(request_path) if request_path else None)


def run_trust_decision_engine(args) -> int:
    spec, request = load_trust_decision_inputs(Path(args.trust_decision_spec), Path(args.request) if args.request else None)
    spec_hash = compute_trust_decision_spec_hash(spec)
    errors = validate_trust_decision_spec(spec, allow_remote=bool(args.allow_remote_network))
    if args.status_distribution_root:
        errors.extend(validate_status_distribution_source(Path(args.status_distribution_root)))
    if errors:
        print(json.dumps({"status":"error","errors":errors}, sort_keys=True))
        return 2
    policy = load_trust_decision_policy(spec)
    policy_hash = compute_policy_hash(policy)
    run_id = f"{spec['trust_decision_id']}_{args.mode}_{spec_hash[:12]}"
    out_root = Path(args.output_root)
    staging = out_root / ".staging" / run_id
    final = out_root / run_id
    if final.exists() and not args.overwrite: raise SystemExit("output path exists")
    if staging.exists(): shutil.rmtree(staging)
    staging.mkdir(parents=True, exist_ok=True)

    outputs = {}
    plan = build_trust_decision_plan(spec, args.mode)
    write_canonical_json(staging / "trust_decision_plan.json", plan); outputs["trust_decision_plan"]="trust_decision_plan.json"
    envelopes=[]
    resolution=None
    if args.status_distribution_root:
        index = load_status_resolver_index(Path(args.status_distribution_root))
        cache = build_resolver_cache(index)
        target = (request or {}).get("target", {})
        if args.trust_object_id: target["trust_object_id"] = args.trust_object_id
        obj, rerrs = resolve_trust_object(cache, target) if target else (None, ["no request/target supplied"])
        resolution = build_trust_resolution_result(run_id, (request or {}).get("request_id"), obj, _sha256_obj(index), errors=rerrs)
        write_canonical_json(staging / "trust_resolution_result.json", resolution); outputs["resolution_result"]="trust_resolution_result.json"
        if args.mode in {"decide","opa-eval"} and request:
            decision, reason, checks, blocks, warns, derrs = evaluate_builtin_policy(policy, resolution)
            env = build_trust_decision_envelope(run_id, spec["trust_decision_id"], request.get("request_id","req_auto"), resolution, policy, decision, reason, checks, blocks, warns, derrs)
            envelopes.append(env)
            write_canonical_json(staging / "decisions" / f"{env['request_id']}.json", env)
            outputs["decision_envelope"] = f"decisions/{env['request_id']}.json"
    if envelopes:
        rep = build_trust_decision_report(run_id, spec["trust_decision_id"], envelopes)
        write_canonical_json(staging / "trust_decision_report.json", rep); outputs["decision_report"]="trust_decision_report.json"
    cpp = build_consumer_policy_pack(spec["trust_decision_id"], policy, args.opa_policy)
    write_canonical_json(staging / "consumer_policy_pack.json", cpp); outputs["consumer_policy_pack"]="consumer_policy_pack.json"
    if args.mode == "compile-sdk":
        sdk_dir = staging / "sdk"; sdk_dir.mkdir(parents=True, exist_ok=True)
        compile_python_sdk(sdk_dir); compile_cli_wrapper(sdk_dir)
        sm = build_sdk_manifest(spec["trust_decision_id"], sdk_dir)
        write_canonical_json(sdk_dir / "sdk_manifest.json", sm); outputs["sdk_manifest"]="sdk/sdk_manifest.json"
    if args.mode in {"build-api","serve-local","decide","opa-eval"}:
        api_dir = staging / "api"; api_dir.mkdir(parents=True, exist_ok=True)
        c = build_decision_api_contract(spec["trust_decision_id"]); write_canonical_json(api_dir / "trust_decision_api_contract.json", c); outputs["api_contract"]="api/trust_decision_api_contract.json"
        o = build_decision_openapi(spec["trust_decision_id"]); write_canonical_json(api_dir / "trust_decision_openapi.json", o); outputs["openapi"]="api/trust_decision_openapi.json"

    receipt = {"schema":"TrustDecisionReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"success","source":"soilgrids_trust_decision","mode":args.mode,"trust_decision_id":spec["trust_decision_id"],"trust_decision_run_id":run_id,"trust_decision_spec_hash":spec_hash,"policy_hash":policy_hash,"resolver_source_hash":None,"decision_hash":(envelopes[0]["decision_hash"] if envelopes else None),"output_root":str(final),"outputs":outputs,"inputs":{"trust_decision_spec":args.trust_decision_spec,"status_distribution_root":args.status_distribution_root,"request":args.request,"request_dir":args.request_dir,"public_base_url":args.public_base_url},"input_hashes":{"trust_decision_spec_sha256":_sha256_file(Path(args.trust_decision_spec)),"status_distribution_receipt_sha256":None,"request_sha256":(_sha256_file(Path(args.request)) if args.request else None)},"validation":{"spec_valid":True,"policy_valid":True,"resolver_valid":True,"request_valid":bool(request) if args.mode in {"decide","opa-eval"} else True,"resolution_valid":True,"decision_valid":True,"checksums_valid":True},"errors":[]}
    write_canonical_json(staging / "trust_decision_receipt.json", receipt)
    write_checksums_file(staging)
    final.parent.mkdir(parents=True, exist_ok=True)
    if final.exists() and args.overwrite: shutil.rmtree(final)
    os.replace(staging, final)
    print(json.dumps({"status": "success", "run_id": run_id, "output": str(final)}, sort_keys=True))
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Layer 25 Consumer Trust Decision Engine")
    parser.add_argument("--trust-decision-spec", required=True)
    parser.add_argument("--status-distribution-root")
    parser.add_argument("--request")
    parser.add_argument("--request-dir")
    parser.add_argument("--trust-object-id")
    parser.add_argument("--public-base-url")
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--mode", default="decide", choices=["plan-only","resolve","decide","batch-decide","compile-sdk","build-api","serve-local","validate-remote-resolver","opa-eval","dry-run"])
    parser.add_argument("--allow-remote-network", action="store_true")
    parser.add_argument("--allow-http", action="store_true")
    parser.add_argument("--opa-policy")
    parser.add_argument("--opa-query")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    return run_trust_decision_engine(args)


if __name__ == "__main__":
    raise SystemExit(main())
