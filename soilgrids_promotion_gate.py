from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import logging
import os
from pathlib import Path
import tempfile
import subprocess
from typing import Any, Dict, List, Optional, Tuple

MODULE_VERSION = "1.0.0"
REMOTE_PREFIXES = ("http://", "https://", "s3://", "gs://", "az://", "/vsicurl/", "/vsis3/", "/vsigs/", "/vsiaz/")

DEFAULT_POLICY = {
    "schema": "PolicyProfile.v1", "profile_id": "soilgrids-default-strict", "decision_mode": "strict",
    "required_stac_version": "1.1.0", "required_crs": "EPSG:4326", "allowed_asset_href_modes": ["relative", "absolute"],
    "allowed_sources": ["soilgrids_wcs", "soilgrids_cog_normalize", "soilgrids_stac_register"],
    "required_license": "CC-BY-4.0", "require_run_receipt": True, "require_cog_receipt": True, "require_stac_receipt": True,
    "require_cog_sha256_match": True, "require_cog_size_match": True, "require_stac_asset_checksum_match": True,
    "require_stac_item_linked_to_collection": True, "require_collection_linked_to_catalog": True, "require_no_remote_hrefs": True,
    "require_atomic_receipts": True, "min_checks_for_promotion": 1,
    "warning_checks": ["collection_extent_exact", "catalog_has_self_link", "stac_has_receipt_assets"],
    "reject_checks": ["missing_required_receipt", "failed_receipt_status", "checksum_mismatch", "size_mismatch", "broken_provenance_chain", "invalid_bbox", "invalid_geometry", "invalid_crs", "invalid_stac_version", "remote_href_detected"],
}

EXIT_CODES = {"promote": 0, "quarantine": 10, "reject": 20, "malformed": 30, "internal": 40, "policy": 50}


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_canonical_json(path: Path, payload: Dict[str, Any], overwrite: bool = True, keep_temp: bool = False) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"output exists: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    tmp_path = Path(tmp)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(payload, f, sort_keys=True, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        _read_json(tmp_path)
        os.replace(tmp_path, path)
    except Exception:
        if not keep_temp and tmp_path.exists():
            tmp_path.unlink()
        raise


def _is_remote(s: str) -> bool:
    return any(s.startswith(p) for p in REMOTE_PREFIXES)


def _check(checks, cid, title, sev, ok, expected=None, actual=None, msg=""):
    checks.append({"check_id": cid, "title": title, "severity": sev, "status": "pass" if ok else "fail", "evidence": {"expected": str(expected), "actual": str(actual)}, "message": msg})


def load_evidence_bundle(**kwargs) -> Dict[str, Any]:
    req = ["cog_receipt", "stac_receipt", "stac_item", "stac_collection", "stac_catalog"]
    for k in req:
        if not kwargs.get(k):
            raise ValueError(f"missing required input: {k}")
    bundle = {"schema": "EvidenceBundle.v1"}
    for k in ["run_receipt", "cog_receipt", "stac_receipt", "stac_item", "stac_collection", "stac_catalog"]:
        p = kwargs.get(k)
        bundle[k] = _read_json(Path(p)) if p else {}
    policy = kwargs.get("policy_profile")
    bundle["policy_profile"] = _read_json(Path(policy)) if policy else DEFAULT_POLICY
    bundle["local_files"] = {"cog_path": bundle["cog_receipt"].get("output_path", ""), "item_path": kwargs["stac_item"], "collection_path": kwargs["stac_collection"], "catalog_path": kwargs["stac_catalog"]}
    return bundle


def validate_receipt_chain(bundle, policy):
    checks = []
    rr, cr, sr = bundle.get("run_receipt", {}), bundle["cog_receipt"], bundle["stac_receipt"]
    if policy.get("require_run_receipt", True):
        _check(checks, "receipt.run.required", "Run receipt required", "required", bool(rr), True, bool(rr))
    if rr:
        _check(checks, "receipt.run.status", "Run receipt success", "required", rr.get("status") == "success", "success", rr.get("status"))
    _check(checks, "receipt.cog.status", "Cog receipt success", "required", cr.get("status") == "success", "success", cr.get("status"))
    _check(checks, "receipt.stac.status", "Stac receipt success", "required", sr.get("status") == "success", "success", sr.get("status"))
    if rr:
        _check(checks, "chain.run_to_cog", "Run spec hash linked to Cog source receipt", "required", cr.get("source_receipt", {}).get("spec_hash") == rr.get("spec_hash"), rr.get("spec_hash"), cr.get("source_receipt", {}).get("spec_hash"))
        _check(checks, "chain.run_to_stac", "Run spec hash linked to Stac source receipts", "required", sr.get("source_receipts", {}).get("run_spec_hash") == rr.get("spec_hash"), rr.get("spec_hash"), sr.get("source_receipts", {}).get("run_spec_hash"))
    _check(checks, "chain.cog_to_stac", "Cog spec hash linked to Stac source receipts", "required", sr.get("source_receipts", {}).get("cog_spec_hash") == cr.get("spec_hash"), cr.get("spec_hash"), sr.get("source_receipts", {}).get("cog_spec_hash"))
    return checks


def validate_asset_integrity(bundle, policy):
    checks=[]
    cr, sr = bundle["cog_receipt"], bundle["stac_receipt"]
    cog = Path(cr.get("output_path", ""))
    _check(checks, "cog.path.remote", "COG path not remote", "required", not _is_remote(str(cog)), False, _is_remote(str(cog)))
    _check(checks, "cog.exists", "COG exists", "required", cog.exists(), True, cog.exists())
    if cog.exists():
        b=cog.read_bytes(); h=_sha256_bytes(b); size=len(b)
    else:
        h=""; size=0
    _check(checks, "cog.sha256.receipt", "COG SHA-256 matches CogReceipt", "required", h==cr.get("output_sha256"), cr.get("output_sha256"), h)
    _check(checks, "cog.size.receipt", "COG size matches CogReceipt", "required", size==cr.get("output_bytes"), cr.get("output_bytes"), size)
    _check(checks, "cog.sha256.stac_receipt", "COG SHA-256 matches StacReceipt", "required", h==sr.get("asset_sha256"), sr.get("asset_sha256"), h)
    _check(checks, "cog.size.stac_receipt", "COG size matches StacReceipt", "required", size==sr.get("asset_bytes"), sr.get("asset_bytes"), size)
    return checks, {"cog_sha256": h, "cog_bytes": size}


def validate_stac_integrity(bundle, policy, cog_meta):
    checks=[]
    item, coll, cat = bundle["stac_item"], bundle["stac_collection"], bundle["stac_catalog"]
    cr = bundle["cog_receipt"]
    asset = next(iter(item.get("assets", {}).values()), {})
    href = asset.get("href", "")
    _check(checks, "stac.asset.href.remote", "Asset href not remote", "required", not _is_remote(href), False, _is_remote(href))
    _check(checks, "stac.version", "STAC version matches policy", "required", item.get("stac_version")==policy.get("required_stac_version"), policy.get("required_stac_version"), item.get("stac_version"))
    bbox=item.get("bbox", [])
    ok_bbox=isinstance(bbox,list) and len(bbox)==4 and bbox[0]<bbox[2] and bbox[1]<bbox[3]
    _check(checks, "stac.bbox.valid", "BBox valid order", "required", ok_bbox, "[xmin,ymin,xmax,ymax]", bbox)
    _check(checks, "stac.crs", "CRS matches policy", "required", cr.get("raster",{}).get("crs")==policy.get("required_crs"), policy.get("required_crs"), cr.get("raster",{}).get("crs"))
    _check(checks, "stac.license", "Collection license matches policy", "required", coll.get("license")==policy.get("required_license"), policy.get("required_license"), coll.get("license"))
    checksum = asset.get("file:checksum")
    _check(checks, "stac.asset.checksum", "STAC asset checksum matches COG", "required", checksum==("1220"+cog_meta["cog_sha256"]), "1220"+cog_meta["cog_sha256"], checksum)
    _check(checks, "warning.catalog_has_self_link", "Catalog has self link", "warning", any(l.get("rel")=="self" for l in cat.get("links",[])), True, any(l.get("rel")=="self" for l in cat.get("links",[])))
    return checks


def evaluate_policy_rules(checks, mode):
    severities={c["severity"] for c in checks}
    if any(s not in {"required","warning","info"} for s in severities):
        return "reject", "unknown severity"
    failed_required=[c for c in checks if c["severity"]=="required" and c["status"]=="fail"]
    failed_warning=[c for c in checks if c["severity"]=="warning" and c["status"]=="fail"]
    if failed_required:
        return "reject", "required checks failed"
    if mode=="strict" and failed_warning:
        return "quarantine", "warning checks failed in strict mode"
    if mode=="permissive":
        return "promote", "all required checks passed"
    if mode=="strict":
        return "promote", "all checks passed"
    return "reject", "unknown decision mode"

def build_validation_report(run_id, policy, mode, checks, hashes, errs, cross):
    summary={"total_checks":len(checks),"passed":sum(c['status']=='pass' for c in checks),"failed":sum(c['status']=='fail' for c in checks),"skipped":sum(c['status']=='skipped' for c in checks)}
    summary["required_failed"]=sum(c['status']=='fail' and c['severity']=='required' for c in checks)
    summary["warnings_failed"]=sum(c['status']=='fail' and c['severity']=='warning' for c in checks)
    return {"schema":"ValidationReport.v1","run_id":run_id,"created_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"status":"error" if errs else "success","source":"soilgrids_promotion_gate","policy_profile_id":policy.get("profile_id"),"decision_mode":mode,"summary":summary,"checks":checks,"evidence_hashes":hashes,"cross_layer":cross,"errors":errs}

def compute_decision_spec_hash(policy_hash, mode, hashes, bundle, checks, decision):
    payload={"module_version":MODULE_VERSION,"policy_profile_hash":policy_hash,"decision_mode":mode,"input_hashes":hashes,"cog_sha256":hashes.get("cog_sha256"),"run_spec_hash":bundle.get("run_receipt",{}).get("spec_hash"),"cog_spec_hash":bundle.get("cog_receipt",{}).get("spec_hash"),"stac_spec_hash":bundle.get("stac_receipt",{}).get("spec_hash"),"item_id":bundle.get("stac_item",{}).get("id"),"collection_id":bundle.get("stac_collection",{}).get("id"),"catalog_id":bundle.get("stac_catalog",{}).get("id"),"checks":sorted([{"check_id":c["check_id"],"severity":c["severity"],"status":c["status"]} for c in checks], key=lambda x:x["check_id"]),"decision":decision}
    return _sha256_bytes((json.dumps(payload,sort_keys=True,separators=(",",":"))).encode())

def build_decision_envelope(run_id, mode, decision, reason, spec_hash, report_path, inputs, summary, checks, errs, bundle, policy):
    return {"schema":"DecisionEnvelope.v1","run_id":run_id,"created_at_utc":dt.datetime.now(dt.timezone.utc).isoformat(),"source":"soilgrids_promotion_gate","decision":decision,"reason":reason,"policy_profile_id":policy.get("profile_id"),"decision_mode":mode,"spec_hash":spec_hash,"validation_report_path":str(report_path),"inputs":inputs,"promotion":{"eligible":decision=="promote","target_stage":"publishable","asset_path":bundle.get("cog_receipt",{}).get("output_path",""),"item_id":bundle.get("stac_item",{}).get("id",""),"collection_id":bundle.get("stac_collection",{}).get("id",""),"catalog_id":bundle.get("stac_catalog",{}).get("id","")},"summary":summary,"blocking_checks":[c["check_id"] for c in checks if c["severity"]=="required" and c["status"]=="fail"],"warnings":[c["check_id"] for c in checks if c["severity"]=="warning" and c["status"]=="fail"],"errors":errs}

def evaluate_promotion_gate(**kwargs):
    mode=kwargs.get("decision_mode") or "strict"
    output_dir=Path(kwargs["output_dir"])
    run_id="run-"+hashlib.sha256(str(sorted(kwargs.items())).encode()).hexdigest()[:16] if kwargs.get("deterministic_run_id") else dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d%H%M%S")
    bundle=load_evidence_bundle(**kwargs)
    policy=bundle["policy_profile"]
    if policy.get("schema")!="PolicyProfile.v1":
        raise ValueError("unsupported policy profile schema")
    if not kwargs.get("decision_mode"):
        mode=policy.get("decision_mode","strict")
    checks=[]
    checks += validate_receipt_chain(bundle, policy)
    asset_checks,cog_meta=validate_asset_integrity(bundle, policy); checks+=asset_checks
    checks += validate_stac_integrity(bundle, policy, cog_meta)
    if len({c["check_id"] for c in checks}) != len(checks):
        raise ValueError("duplicate check_id")
    decision,reason=evaluate_policy_rules(checks, mode)
    def fh(p):
        return _sha256_bytes(Path(p).read_bytes()) if p else None
    hashes={"run_receipt_sha256":fh(kwargs.get("run_receipt")) if kwargs.get("run_receipt") else None,"cog_receipt_sha256":fh(kwargs["cog_receipt"]),"stac_receipt_sha256":fh(kwargs["stac_receipt"]),"stac_item_sha256":fh(kwargs["stac_item"]),"stac_collection_sha256":fh(kwargs["stac_collection"]),"stac_catalog_sha256":fh(kwargs["stac_catalog"]),"cog_sha256":cog_meta["cog_sha256"]}
    cross={"run_spec_hash":bundle.get("run_receipt",{}).get("spec_hash"),"cog_spec_hash":bundle.get("cog_receipt",{}).get("spec_hash"),"stac_spec_hash":bundle.get("stac_receipt",{}).get("spec_hash"),"provenance_chain_valid":not any(c["check_id"].startswith("chain") and c["status"]=="fail" for c in checks)}
    vr=build_validation_report(run_id, policy, mode, checks, hashes, [], cross)
    policy_hash=_sha256_bytes(json.dumps(policy,sort_keys=True).encode())
    spec_hash=compute_decision_spec_hash(policy_hash, mode, hashes, bundle, checks, decision)
    report_path=output_dir/f"validation_report_{spec_hash[:12]}.json"
    write_canonical_json(report_path, vr, overwrite=kwargs.get("overwrite",True), keep_temp=kwargs.get("keep_temp",False))
    de=build_decision_envelope(run_id, mode, decision, reason, spec_hash, report_path, {k+"_path":kwargs.get(k) for k in ["run_receipt","cog_receipt","stac_receipt","stac_item","stac_collection","stac_catalog","policy_profile"]}, vr["summary"], checks, [], bundle, policy)
    dec_path=output_dir/f"decision_envelope_{spec_hash[:12]}.json"
    write_canonical_json(dec_path,de,overwrite=kwargs.get("overwrite",True),keep_temp=kwargs.get("keep_temp",False))
    return de, vr, dec_path

def _cli():
    ap=argparse.ArgumentParser()
    for a in ["run-receipt","cog-receipt","stac-receipt","stac-item","stac-collection","stac-catalog","policy-profile","output-dir","decision-mode","opa-policy","opa-query"]:
        ap.add_argument(f"--{a}")
    ap.add_argument("--allow-symlinks", action="store_true")
    ap.add_argument("--write-evidence-bundle", action="store_true")
    ap.add_argument("--keep-temp", action="store_true")
    ap.add_argument("--deterministic-run-id", action="store_true")
    ap.add_argument("--overwrite", action="store_true")
    ns=ap.parse_args()
    try:
        de, vr, dec_path = evaluate_promotion_gate(**vars(ns))
        print(str(dec_path))
        return EXIT_CODES[de["decision"]]
    except json.JSONDecodeError:
        print(json.dumps({"status":"error","decision":"reject","error_count":1}), file=os.sys.stderr)
        return EXIT_CODES["malformed"]
    except ValueError as e:
        print(json.dumps({"status":"error","decision":"reject","error_count":1,"message":str(e)}), file=os.sys.stderr)
        return EXIT_CODES["reject"]
    except Exception:
        print(json.dumps({"status":"error","decision":"reject","error_count":1}), file=os.sys.stderr)
        return EXIT_CODES["internal"]

if __name__ == "__main__":
    raise SystemExit(_cli())
