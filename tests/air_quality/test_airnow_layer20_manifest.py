from pathlib import Path
import json
from kfm.air_quality.airnow.snapshot_preservation.run_snapshot_preservation_plan import run_snapshot_preservation_plan

MAN=Path("tests/fixtures/air_quality/airnow/layer20/manifests")

def run_one(name,tmp_path):
 return run_snapshot_preservation_plan(str(MAN/name), str(tmp_path), "2026-01-01T00:00:00Z")
def test_valid_manifest(tmp_path):
 r=run_one("snapshot_preservation_valid_manifest.json",tmp_path); assert r["validation_outcome"]=="PASS"

def test_missing_receipt_denied(tmp_path):
 r=run_one("snapshot_preservation_missing_layer19_receipt_manifest.json",tmp_path); assert r["validation_outcome"]=="FAIL"
