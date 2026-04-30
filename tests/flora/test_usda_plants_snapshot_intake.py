import json,subprocess

def test_snapshot_intake_good(tmp_path):
 out=tmp_path/'raw/flora/usda_plants/2026-04-30'
 subprocess.run(['python','tools/intake/flora/usda_plants_snapshot_intake.py','--raw-dir','tests/fixtures/flora/usda_plants/operator_snapshot/good','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out-dir',str(out)],check=True)
 m=json.loads((out/'raw_snapshot_manifest.json').read_text()); assert m['status']=='pass'
