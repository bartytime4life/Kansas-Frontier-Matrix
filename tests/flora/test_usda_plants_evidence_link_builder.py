import json, subprocess
from pathlib import Path

def build_base(tmp_path):
    out=tmp_path/"out"
    subprocess.run(["python","tools/ingest/flora/usda_plants_fixture_loader.py","--checklist","tests/fixtures/flora/usda_plants/raw/checklist.csv","--states","tests/fixtures/flora/usda_plants/raw/state_distribution.csv","--counties","tests/fixtures/flora/usda_plants/raw/county_distribution.csv","--snapshot-date","2026-04-30","--out-dir",str(out)],check=True)
    subprocess.run(["python","tools/proofs/flora/usda_plants_proof_manifest.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--out",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json")],check=True)
    return out

def test_usda_plants_evidence_link_builder(tmp_path):
    out=build_base(tmp_path)
    subprocess.run(["python","tools/evidence/flora/usda_plants_evidence_link_builder.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--receipts-dir",str(out/"receipts/flora/usda_plants"),"--proof-manifest",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json"),"--snapshot-date","2026-04-30","--generated-at","2026-04-30T00:00:00Z","--out-dir",str(out/"evidence/flora/usda_plants")],check=True)
    assert len(list((out/"evidence/flora/usda_plants").glob("*.json")))==len(list((out/"processed/flora/usda_plants").glob("*.json")))
