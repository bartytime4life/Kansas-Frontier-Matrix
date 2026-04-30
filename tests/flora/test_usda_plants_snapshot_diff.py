import json,subprocess,sys

def test_diff_lock(tmp_path):
 b={'snapshot_date':'2026-04-01','locked_files':[{'role':'checklist','sha256':'sha256:'+'0'*64}]};h={'snapshot_date':'2026-04-30','locked_files':[{'role':'checklist','sha256':'sha256:'+'1'*64}]}
 (tmp_path/'b.json').write_text(json.dumps(b));(tmp_path/'h.json').write_text(json.dumps(h));o=tmp_path/'o.json'
 subprocess.run([sys.executable,'tools/diff/flora/usda_plants_snapshot_diff.py','--base-lock',str(tmp_path/'b.json'),'--head-lock',str(tmp_path/'h.json'),'--generated-at','2026-04-30T00:00:00Z','--out',str(o)],check=True)
 assert json.loads(o.read_text())['summary']['changed']==1
