from pathlib import Path
import json
from kfm.air_quality.airnow.snapshot_preservation.run_snapshot_preservation_plan import run_snapshot_preservation_plan

MAN=Path("tests/fixtures/air_quality/airnow/layer20/manifests")

def run_one(name,tmp_path):
 return run_snapshot_preservation_plan(str(MAN/name), str(tmp_path), "2026-01-01T00:00:00Z")
def test_caveats(tmp_path):
 run_one("snapshot_preservation_valid_manifest.json",tmp_path); d=json.loads((tmp_path/"snapshot_preservation_caveat_register.json").read_text()); assert "AIRNOW_PRELIMINARY_DATA" in d["caveats"]
