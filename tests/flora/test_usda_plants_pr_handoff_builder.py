import json,subprocess,sys

def test_handoff(tmp_path):
 for n in ['r.json','d.json','w.json']:(tmp_path/n).write_text('{}')
 o=tmp_path/'h.json'
 subprocess.run([sys.executable,'tools/release/flora/usda_plants_pr_handoff_builder.py','--release-candidate',str(tmp_path/'r.json'),'--snapshot-diff',str(tmp_path/'d.json'),'--watcher-run-receipt',str(tmp_path/'w.json'),'--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out',str(o)],check=True)
 assert 'branch_suggestion' in json.loads(o.read_text())
