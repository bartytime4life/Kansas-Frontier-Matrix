import subprocess,sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_build(tmp_path):
 (tmp_path/'continuity/soil').mkdir(parents=True); (tmp_path/'continuity/soil/current_public_delivery_continuity.json').write_text('{"active_continuity_id":"soil-continuity-test"}')
 args=[sys.executable,ROOT/'tools/stability/soil/build_delivery_stability.py']
 for n in ['continuity','resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops','stability']:
  args += [f'--{n}-root',str(tmp_path)]
 args += ['--out-root',str(tmp_path),'--base-public-url','https://example.invalid/kfm/soil']
 p=subprocess.run(args,capture_output=True,text=True)
 assert p.returncode==0
 assert json.loads((tmp_path/'stability/soil/current_public_delivery_stability.json').read_text())['active_stability_id']
