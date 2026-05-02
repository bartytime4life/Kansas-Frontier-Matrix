import json, subprocess, tempfile
from pathlib import Path

ROOT=Path("tests/fixtures/tile_runtime")
EMITTER=["node","tools/mobile-emu/src/emit_runtime_receipt.ts"]
VALIDATOR=["python","tools/validators/tile_runtime/validate_tile_runtime_receipt.py"]

def run_emit(metrics="valid_metrics.json",trace="valid_trace_redacted.json",release="valid_release_manifest_ref.json",evidence="valid_evidence_refs.json"):
    td=Path(tempfile.mkdtemp())
    cp=subprocess.run(EMITTER+["--metrics",str(ROOT/metrics),"--trace",str(ROOT/trace),"--release-manifest-ref",str(ROOT/release),"--evidence-refs",str(ROOT/evidence),"--out-dir",str(td)],capture_output=True,text=True)
    return cp,td

def test_valid_receipt_and_manifest_pass():
    cp,td=run_emit(); assert cp.returncode==0
    v=subprocess.run(VALIDATOR+["--receipt",str(td/"tile_runtime_receipt.json"),"--trace-manifest",str(td/"tile_runtime_trace_manifest.json"),"--metrics",str(ROOT/"valid_metrics.json"),"--trace",str(ROOT/"valid_trace_redacted.json"),"--public-summary",str(td/"tile_runtime_public_summary.json")])
    assert v.returncode==0

def test_budget_exceeded_fails():
    cp,_=run_emit(metrics="invalid_budget_exceeded_metrics.json")
    assert cp.returncode!=0

def test_raw_url_leak_fails(): assert run_emit(trace="invalid_raw_url_leak_trace.json")[0].returncode!=0

def test_missing_evidence_fails(): assert run_emit(evidence="invalid_missing_evidence_refs.json")[0].returncode!=0

def test_missing_release_fails(): assert run_emit(release="invalid_missing_release_manifest_ref.json")[0].returncode!=0

def test_deterministic_receipt_id_and_spec_hash():
    a,ta=run_emit(); b,tb=run_emit();
    ra=json.loads((ta/"tile_runtime_receipt.json").read_text()); rb=json.loads((tb/"tile_runtime_receipt.json").read_text())
    assert ra["receipt_id"]==rb["receipt_id"] and ra["spec_hash"]==rb["spec_hash"]

def test_public_summary_no_urls():
    cp,td=run_emit(); assert cp.returncode==0
    s=(td/"tile_runtime_public_summary.json").read_text(); assert "http://" not in s and "https://" not in s
