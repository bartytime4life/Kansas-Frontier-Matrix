import json,subprocess,sys

def test_lock(tmp_path):
 raw=tmp_path/'raw';raw.mkdir();m={'status':'pass','raw_files':[{'role':'checklist','path':'raw/flora/usda_plants/2026-04-30/checklist.csv','sha256':'sha256:'+'0'*64,'size_bytes':1},{'role':'state_distribution','path':'raw/flora/usda_plants/2026-04-30/state_distribution.csv','sha256':'sha256:'+'1'*64,'size_bytes':1},{'role':'county_distribution','path':'raw/flora/usda_plants/2026-04-30/county_distribution.csv','sha256':'sha256:'+'2'*64,'size_bytes':1}]}
 (raw/'m.json').write_text(json.dumps(m));out=raw/'lock.json'
 subprocess.run([sys.executable,'tools/intake/flora/usda_plants_snapshot_lock_builder.py','--raw-snapshot-manifest',str(raw/'m.json'),'--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out',str(out)],check=True)
 assert json.loads(out.read_text())['lock_state']=='locked'
