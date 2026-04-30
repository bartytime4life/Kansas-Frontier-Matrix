import json, subprocess
from pathlib import Path

def build_base(tmp_path):
    out=tmp_path/"out"
    subprocess.run(["python","tools/ingest/flora/usda_plants_fixture_loader.py","--checklist","tests/fixtures/flora/usda_plants/raw/checklist.csv","--states","tests/fixtures/flora/usda_plants/raw/state_distribution.csv","--counties","tests/fixtures/flora/usda_plants/raw/county_distribution.csv","--snapshot-date","2026-04-30","--out-dir",str(out)],check=True)
    subprocess.run(["python","tools/proofs/flora/usda_plants_proof_manifest.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--out",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json")],check=True)
    return out

def test_usda_plants_release_candidate_builder(tmp_path):
    out=build_base(tmp_path)
    subprocess.run(["python","tools/evidence/flora/usda_plants_evidence_link_builder.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--receipts-dir",str(out/"receipts/flora/usda_plants"),"--proof-manifest",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json"),"--snapshot-date","2026-04-30","--generated-at","2026-04-30T00:00:00Z","--out-dir",str(out/"evidence/flora/usda_plants")],check=True)
    subprocess.run(["python","tools/catalog/flora/usda_plants_catalog_builder.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--evidence-dir",str(out/"evidence/flora/usda_plants"),"--proof-manifest",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json"),"--snapshot-date","2026-04-30","--generated-at","2026-04-30T00:00:00Z","--out-dir",str(out/"catalog/flora/usda_plants")],check=True)
    subprocess.run(["python","tools/ui/flora/usda_plants_evidence_drawer_payload_builder.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--evidence-dir",str(out/"evidence/flora/usda_plants"),"--catalog-ref","catalog/flora/usda_plants/catalog.json","--release-candidate-ref","releases/flora/usda_plants/release_candidate_2026-04-30.json","--snapshot-date","2026-04-30","--out-dir",str(out/"ui/flora/usda_plants/evidence_drawer")],check=True)
    subprocess.run(["python","tools/maps/flora/usda_plants_map_layer_contract_builder.py","--snapshot-date","2026-04-30","--out",str(out/"maps/flora/usda_plants/county_presence.layer_contract.json")],check=True)
    rc=out/"releases/flora/usda_plants/release_candidate_2026-04-30.json"
    subprocess.run(["python","tools/release/flora/usda_plants_release_candidate_builder.py","--processed-dir",str(out/"processed/flora/usda_plants"),"--evidence-dir",str(out/"evidence/flora/usda_plants"),"--catalog-dir",str(out/"catalog/flora/usda_plants"),"--receipts-dir",str(out/"receipts/flora/usda_plants"),"--proof-manifest",str(out/"proofs/flora/usda_plants/spec_hash_manifest.json"),"--ui-dir",str(out/"ui/flora/usda_plants/evidence_drawer"),"--map-contract",str(out/"maps/flora/usda_plants/county_presence.layer_contract.json"),"--snapshot-date","2026-04-30","--generated-at","2026-04-30T00:00:00Z","--out",str(rc)],check=True)
    o=json.loads(rc.read_text()); assert o['promotion_state']=="not_promoted" and o['gates']['publication']=="blocked"
