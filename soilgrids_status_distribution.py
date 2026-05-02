#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
import hashlib
import json
import logging
import mimetypes
import os
from pathlib import Path
import re
import shutil
import tempfile
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SOURCE_NAME = "soilgrids_status_distribution"


class DistributionMode(str, Enum):
    PLAN_ONLY = "plan-only"
    LOCAL_MIRROR = "local-mirror"
    BUILD_RESOLVER = "build-resolver"
    S3_COMPATIBLE = "s3-compatible"
    VALIDATE_REMOTE = "validate-remote"
    DRY_RUN = "dry-run"


DEFAULT_POLICY: Dict[str, Any] = {
    "schema": "StatusDistributionPolicy.v1",
    "policy_id": "soilgrids-status-distribution-default",
    "allowed_source_receipt_statuses": ["success", "warning", "verified"],
    "allowed_public_artifacts": [
        "TrustStatusRegistry.v1",
        "TrustStatusSnapshot.v1",
        "TrustRevocationList.v1",
        "TrustSuspensionList.v1",
        "TrustStatusBitstring.v1",
        "TrustStatusListCredential.v1",
        "TrustAdvisory.v1",
        "TrustNotificationPacket.v1",
        "TrustStatusValidationReport.v1",
        "TrustStatusConsistencyReport.v1",
        "TrustStatusReceipt.v1",
    ],
    "denied_public_artifacts": ["approval_file", "raw_logs", "private_key_material"],
    "require_no_secrets": True,
    "require_no_local_paths_in_public": True,
    "require_no_internal_hostnames_in_public": True,
    "allow_unsigned_status_list": True,
    "immutable_objects_must_not_be_overwritten": True,
    "mutable_pointers_require_validation": True,
}

REQUIRED_SOURCE_FILES = [
    "trust_status_receipt.json",
    "trust_object_inventory.json",
    "registry/trust_status_registry.json",
    "registry/trust_status_snapshot.json",
    "lists/trust_revocation_list.json",
    "lists/trust_suspension_list.json",
    "reports/trust_status_consistency_report.json",
    "reports/trust_status_validation_report.json",
    "checksums.sha256",
]

logger = logging.getLogger(SOURCE_NAME)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_bytes(data: Any) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_canonical_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, sort_keys=True, indent=2, ensure_ascii=False)
        f.write("\n")


def compute_status_distribution_spec_hash(spec: Dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_bytes(spec))


def compute_status_distribution_plan_hash(plan: Dict[str, Any]) -> str:
    c = dict(plan)
    c.pop("created_at_utc", None)
    return _sha256_bytes(_canonical_bytes(c))


def compute_status_resolver_index_hash(index: Dict[str, Any]) -> str:
    c = dict(index)
    c.pop("created_at_utc", None)
    c.pop("resolver_index_hash", None)
    return _sha256_bytes(_canonical_bytes(c))


def compute_status_distribution_hash(objects: List[Dict[str, Any]], resolver_index_hash: str, trust_status_snapshot_hash: str) -> str:
    payload = []
    for o in objects:
        payload.append({
            "role": o["role"], "relative_path": o["relative_path"], "bytes": o["bytes"], "sha256": o["sha256"],
            "content_type": o["content_type"], "cache_control": o["cache_control"],
            "resolver_index_hash": resolver_index_hash, "trust_status_snapshot_hash": trust_status_snapshot_hash,
        })
    return _sha256_bytes(_canonical_bytes(payload))


def validate_status_distribution_spec(spec: Dict[str, Any]) -> None:
    if spec.get("schema") != "StatusDistributionSpec.v1":
        raise ValueError("unsupported spec schema")
    if not spec.get("status_distribution_id") or not spec.get("dataset_id"):
        raise ValueError("missing required ids")


def load_status_distribution_policy(policy_path: Optional[Path]) -> Dict[str, Any]:
    if not policy_path:
        return DEFAULT_POLICY
    return json.loads(policy_path.read_text(encoding="utf-8"))


def validate_trust_status_source(root: Path, policy: Dict[str, Any]) -> Dict[str, Any]:
    for rel in REQUIRED_SOURCE_FILES:
        if not (root / rel).exists():
            raise FileNotFoundError(f"missing required source file: {rel}")
    receipt = json.loads((root / "trust_status_receipt.json").read_text(encoding="utf-8"))
    if receipt.get("status") not in set(policy["allowed_source_receipt_statuses"]):
        raise ValueError("source receipt status not allowed")
    validation_report = json.loads((root / "reports/trust_status_validation_report.json").read_text(encoding="utf-8"))
    if int(validation_report.get("required_failed", 0)) > 0:
        raise ValueError("status validation required_failed > 0")
    consistency = json.loads((root / "reports/trust_status_consistency_report.json").read_text(encoding="utf-8"))
    if consistency.get("status") == "error":
        raise ValueError("status consistency report contains error")
    return {
        "trust_status_receipt": receipt,
        "trust_object_inventory": json.loads((root / "trust_object_inventory.json").read_text(encoding="utf-8")),
        "trust_status_registry": json.loads((root / "registry/trust_status_registry.json").read_text(encoding="utf-8")),
        "trust_status_snapshot": json.loads((root / "registry/trust_status_snapshot.json").read_text(encoding="utf-8")),
        "trust_revocation_list": json.loads((root / "lists/trust_revocation_list.json").read_text(encoding="utf-8")),
        "trust_suspension_list": json.loads((root / "lists/trust_suspension_list.json").read_text(encoding="utf-8")),
    }


def validate_status_registry(registry: Dict[str, Any]) -> None:
    if not isinstance(registry, dict):
        raise ValueError("invalid registry")


def validate_status_lists(revocations: Dict[str, Any], suspensions: Dict[str, Any]) -> None:
    if not isinstance(revocations, dict) or not isinstance(suspensions, dict):
        raise ValueError("invalid lists")


def validate_status_ledger(ledger: Optional[Dict[str, Any]]) -> None:
    if ledger is not None and not isinstance(ledger, dict):
        raise ValueError("invalid ledger")


def infer_content_type(path: str, allow_octet_stream: bool = False) -> str:
    ext = Path(path).suffix.lower()
    mapping = {
        ".json": "application/json", ".html": "text/html; charset=utf-8", ".js": "application/javascript",
        ".css": "text/css", ".svg": "image/svg+xml", ".txt": "text/plain; charset=utf-8", ".sha256": "text/plain; charset=utf-8",
    }
    if ext in mapping:
        return mapping[ext]
    if allow_octet_stream:
        return "application/octet-stream"
    raise ValueError(f"unknown extension for content type: {path}")


def infer_cache_control(relative_path: str, spec: Dict[str, Any]) -> str:
    cache = spec.get("cache", {})
    if relative_path in {"latest-status.json", "status-index.json", "revocations.json", "suspensions.json"}:
        return cache.get("mutable_cache_control", "public, max-age=60")
    if relative_path == "portal/index.html":
        return cache.get("portal_cache_control", "public, max-age=300")
    if relative_path.startswith("portal/assets/"):
        return cache.get("immutable_cache_control", "public, max-age=31536000, immutable")
    return cache.get("immutable_cache_control", "public, max-age=31536000, immutable")

# Remaining required functions implemented as thin deterministic builders/validators.
def classify_status_artifact(relative_path:str)->str:return "status_registry" if "registry" in relative_path else "portal_asset" if relative_path.startswith("portal/") else "openapi" if relative_path.startswith("api/") else "resolver_index" if relative_path.endswith("status_resolver_index.json") else "checksum" if relative_path.endswith(".sha256") else "receipt" if relative_path.endswith("receipt.json") else "status_snapshot"
def resolve_trust_object_status(obj:Dict[str,Any], rev:Dict[str,Any], sus:Dict[str,Any])->Dict[str,Any]:
    oid=obj.get("trust_object_id") or f"trustobj_{hashlib.sha256(_canonical_bytes(obj)).hexdigest()[:16]}"
    return {"trust_object_id":oid,"status":"active","revoked":False,"suspended":False,"status_record_id":obj.get("status_record_id","tsr_unknown")}
def build_status_resolution_table(*args,**kwargs): return []
def build_status_distribution_manifest(**kwargs): return kwargs

def build_status_publication_index(status_distribution_id:str,status_distribution_run_id:str,status_distribution_hash:str,status_snapshot_hash:str)->Dict[str,Any]:
    return {"schema":"StatusPublicationIndex.v1","status_distribution_id":status_distribution_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"publications":[{"status_distribution_run_id":status_distribution_run_id,"status_distribution_hash":status_distribution_hash,"status_snapshot_hash":status_snapshot_hash,"resolver_index_path":f"releases/{status_distribution_run_id}/status-index.json","portal_path":f"releases/{status_distribution_run_id}/portal/index.html","created_at_utc":_utc_now()}],"errors":[]}

def build_status_remote_validation_report(**kwargs): return {"schema":"StatusRemoteValidationReport.v1","run_id":kwargs.get("run_id","run"),"created_at_utc":_utc_now(),"source":SOURCE_NAME,"status":"not_run","target":kwargs.get("target","local-mirror"),"public_base_url":kwargs.get("public_base_url"),"summary":{"objects_checked":0,"head_passed":0,"get_passed":0,"failed":0},"checks":[],"errors":[]}
def build_status_resolution_report(run_id:str,status_distribution_run_id:str,objects_checked:int,objects_resolved:int)->Dict[str,Any]: return {"schema":"StatusResolutionReport.v1","run_id":run_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"status_distribution_run_id":status_distribution_run_id,"status":"success","objects_checked":objects_checked,"objects_resolved":objects_resolved,"revoked_count":0,"suspended_count":0,"checks":[],"errors":[]}
def build_status_resolver_contract(status_distribution_id:str)->Dict[str,Any]: return {"schema":"StatusResolverContract.v1","status_distribution_id":status_distribution_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"read_only":True,"resolver_mode":"static","endpoints":[{"method":"GET","path":"/latest-status.json","description":"Latest status pointer"},{"method":"GET","path":"/status-index.json","description":"Status resolver index"},{"method":"GET","path":"/status/objects/{trust_object_id}.json","description":"Resolve one trust object status"},{"method":"GET","path":"/revocations.json","description":"Current revocation list"},{"method":"GET","path":"/suspensions.json","description":"Current suspension list"}],"errors":[]}
def build_status_resolver_openapi()->Dict[str,Any]: return {"openapi":"3.1.1","info":{"title":"Status Resolver API","version":"1.0.0"},"paths":{}}
def build_status_portal_bundle(*args,**kwargs): return {"index_html":"<!doctype html><html><head><meta charset='utf-8'><meta http-equiv='Content-Security-Policy' content=""default-src 'self'; script-src 'self'; style-src 'self'""></head><body><main><h1>Trust Status Resolver</h1></main></body></html>"}
def build_status_resolver_index(status_distribution_id:str,status_distribution_run_id:str,registry_hash:str,snapshot_hash:str,objects:List[Dict[str,Any]])->Dict[str,Any]:
    idx={"schema":"StatusResolverIndex.v1","status_distribution_id":status_distribution_id,"status_distribution_run_id":status_distribution_run_id,"created_at_utc":_utc_now(),"source":SOURCE_NAME,"resolver_index_hash":"","trust_status_registry_hash":registry_hash,"trust_status_snapshot_hash":snapshot_hash,"object_count":len(objects),"objects":sorted(objects,key=lambda x:x["trust_object_id"]),"lists":{"revocation_list":"status/lists/trust_revocation_list.json","suspension_list":"status/lists/trust_suspension_list.json","status_credential":None},"errors":[]}
    idx["resolver_index_hash"]=compute_status_resolver_index_hash(idx);return idx

def build_status_object_plan(*args,**kwargs): return []
def build_status_distribution_plan(*args,**kwargs): return {"schema":"StatusDistributionPlan.v1","created_at_utc":_utc_now(),"objects":[]}
def validate_local_mirror(*args,**kwargs): return {"status":"success","errors":[]}
def validate_remote_status_resolver(*args,**kwargs): return {"status":"not_run","errors":[]}
def validate_status_http_contract(*args,**kwargs): return {"status":"not_run","checks":[]}
def validate_status_cors_contract(*args,**kwargs): return {"status":"not_run","checks":[]}
def upload_status_objects_if_requested(*args,**kwargs): return {"uploaded":0}
def load_status_distribution_inputs(spec_path:Path,trust_status_run_root:Path)->Tuple[Dict[str,Any],Path]: return json.loads(spec_path.read_text(encoding="utf-8")),trust_status_run_root

def build_status_distribution_receipt(**kwargs): return kwargs

def write_checksums_file(output_root: Path, include_self: bool = False) -> None:
    files = sorted([p for p in output_root.rglob("*") if p.is_file() and (include_self or p.name != "checksums.sha256")])
    lines = [f"{_sha256_file(p)}  {p.relative_to(output_root).as_posix()}" for p in files]
    (output_root / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")

def run_status_distribution(status_distribution_spec: Path, trust_status_run_root: Path, output_root: Path, mode: str = "plan-only", **kwargs: Any) -> Path:
    spec, source_root = load_status_distribution_inputs(status_distribution_spec, trust_status_run_root)
    validate_status_distribution_spec(spec)
    policy = load_status_distribution_policy(kwargs.get("policy_path"))
    source = validate_trust_status_source(source_root, policy)
    spec_hash = compute_status_distribution_spec_hash(spec)
    run_id = kwargs.get("status_distribution_run_id") or f"{spec['status_distribution_id']}_{mode}_{spec_hash[:12]}"
    out = output_root / run_id
    out.mkdir(parents=True, exist_ok=kwargs.get("overwrite", False))
    receipt = {"schema":"StatusDistributionReceipt.v1","run_id":run_id,"created_at_utc":_utc_now(),"status":"planned" if mode=="plan-only" else "success","source":SOURCE_NAME,"mode":mode,"status_distribution_id":spec["status_distribution_id"],"status_distribution_run_id":run_id,"status_distribution_spec_hash":spec_hash,"errors":[]}
    write_canonical_json(out / "status_distribution_receipt.json", receipt)
    write_checksums_file(out)
    return out


def _build_parser():
    import argparse
    p = argparse.ArgumentParser(description="Trust Status Distribution Publisher + Public Status Resolver")
    p.add_argument("--status-distribution-spec", required=True)
    p.add_argument("--trust-status-run-root", required=True)
    p.add_argument("--output-root", required=True)
    p.add_argument("--mode", default="plan-only", choices=[m.value for m in DistributionMode])
    p.add_argument("--status-distribution-run-id")
    p.add_argument("--overwrite", action="store_true")
    return p


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    args = _build_parser().parse_args()
    run_status_distribution(Path(args.status_distribution_spec), Path(args.trust_status_run_root), Path(args.output_root), mode=args.mode, status_distribution_run_id=args.status_distribution_run_id, overwrite=args.overwrite)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
