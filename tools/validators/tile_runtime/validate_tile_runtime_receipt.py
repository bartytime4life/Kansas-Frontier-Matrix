#!/usr/bin/env python3
import argparse, copy, hashlib, json, re
from pathlib import Path
from jsonschema import validate

URL_RE = re.compile(r"https?://", re.IGNORECASE)
INT_RE = re.compile(r"(^|[\s/])(?:/workspace|/home|/tmp|[A-Za-z]:\\)")

def canonical(o): return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
def sha(o): return "sha256:" + hashlib.sha256(canonical(o).encode()).hexdigest()
def shabytes(b): return "sha256:" + hashlib.sha256(b).hexdigest()

def recompute_spec_hash(doc):
    d=copy.deepcopy(doc); d.pop("spec_hash",None); d.pop("created_at",None); return sha(d)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--receipt",required=True); ap.add_argument("--trace-manifest",required=True)
    ap.add_argument("--metrics",required=True); ap.add_argument("--trace",required=True); ap.add_argument("--public-summary",required=True)
    args=ap.parse_args()
    rp,tp,mp,trp,sp=[Path(x) for x in [args.receipt,args.trace_manifest,args.metrics,args.trace,args.public_summary]]
    r=json.loads(rp.read_text()); t=json.loads(tp.read_text()); m=json.loads(mp.read_text()); tr=json.loads(trp.read_text()); s=json.loads(sp.read_text())
    rs=json.loads(Path("schemas/tile_runtime/tile_runtime_performance_receipt.schema.json").read_text())
    ts=json.loads(Path("schemas/tile_runtime/tile_runtime_trace_manifest.schema.json").read_text())
    validate(r,rs); validate(t,ts)
    assert recompute_spec_hash(r)==r["spec_hash"],"receipt spec_hash mismatch"
    assert recompute_spec_hash(t)==t["spec_hash"],"trace manifest spec_hash mismatch"
    rid="trpr_"+hashlib.sha256(canonical({k:r[k] for k in ["run_id","harness_version","runtime_profile","cpu_throttle","network_profile","verifier_worker_count","max_parallel_fetches","tile_count","verified_tile_count","failed_tile_count","mean_verify_decode_ms","p95_verify_decode_ms","peak_renderer_memory_mb"]}).encode()).hexdigest()[:16]
    assert rid==r["receipt_id"],"receipt_id mismatch"
    assert t["trace_sha256"]==shabytes(trp.read_bytes())
    assert t["metrics_sha256"]==shabytes(mp.read_bytes())
    reasons=[]; b=m["budget"]
    if m["failed_tile_count"]>0: reasons.append("failed_tile_count")
    if m["mean_verify_decode_ms"]>b["max_mean_verify_decode_ms"]: reasons.append("mean_verify_decode_ms")
    if m["p95_verify_decode_ms"]>b["max_p95_verify_decode_ms"]: reasons.append("p95_verify_decode_ms")
    if m["peak_renderer_memory_mb"]>b["max_peak_renderer_memory_mb"]: reasons.append("peak_renderer_memory_mb")
    if m["max_parallel_fetches"]>b["max_parallel_fetches"]: reasons.append("max_parallel_fetches")
    if m["verifier_worker_count"]>b["max_verifier_workers"]: reasons.append("verifier_worker_count")
    expected="deny" if reasons else "allow"
    assert r["budget_decision"]==expected
    if expected=="deny": assert r["failure_reasons"]
    st=canonical(s)
    assert not URL_RE.search(st),"raw URL leak"
    assert not INT_RE.search(st),"internal path leak"
    assert not s.get("contains_sensitive_geometry", False),"sensitive geometry leak"
    assert r.get("evidence_bundle_refs") and r.get("release_manifest_ref")
    print("OK")

if __name__=="__main__": main()
