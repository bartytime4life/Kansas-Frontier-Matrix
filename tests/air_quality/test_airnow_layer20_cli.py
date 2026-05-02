from pathlib import Path
import json
from kfm.air_quality.airnow.snapshot_preservation.run_snapshot_preservation_plan import run_snapshot_preservation_plan

MAN=Path("tests/fixtures/air_quality/airnow/layer20/manifests")

def run_one(name,tmp_path):
 return run_snapshot_preservation_plan(str(MAN/name), str(tmp_path), "2026-01-01T00:00:00Z")
from tools.air_quality.airnow_layer20_snapshot_preservation import main
import sys

def test_cli_ok(tmp_path, monkeypatch):
 monkeypatch.setattr(sys, "argv", ["prog","--manifest",str(MAN/"snapshot_preservation_valid_no_packet_manifest.json"),"--out-dir",str(tmp_path),"--created-at","2026-01-01T00:00:00Z"])
 try:
  main()
 except SystemExit as e:
  assert e.code==0
