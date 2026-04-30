import json, subprocess, tempfile
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def j(cmd): return json.loads(subprocess.check_output(cmd,text=True))

def test_cli_help_version():
 subprocess.check_call([str(BASE/'kfm-ebird-benchmark'),'--help'])
 subprocess.check_call([str(BASE/'kfm-ebird-capacity'),'--help'])
 assert j([str(BASE/'kfm-ebird-benchmark'),'--version'])['adapter']=='kfm-ebird'
 assert j([str(BASE/'kfm-ebird-capacity'),'--version'])['adapter']=='kfm-ebird'

def test_deterministic_ids_and_outputs():
 with tempfile.TemporaryDirectory() as td:
  o1=Path(td)/'o1'; o2=Path(td)/'o2'
  subprocess.check_call([str(BASE/'kfm-ebird-benchmark'),'--profile','tiny','--stages','ingest','--out-dir',str(o1),'--work-dir',str(Path(td)/'w1'),'--public-temp-dir',str(Path(td)/'p1'),'--seed','s'])
  subprocess.check_call([str(BASE/'kfm-ebird-benchmark'),'--profile','tiny','--stages','ingest','--out-dir',str(o2),'--work-dir',str(Path(td)/'w2'),'--public-temp-dir',str(Path(td)/'p2'),'--seed','s'])
  b1=json.loads((o1/'benchmark_plan.json').read_text())['benchmark_id']; b2=json.loads((o2/'benchmark_plan.json').read_text())['benchmark_id']
  assert b1==b2
  cap=Path(td)/'cap'; subprocess.check_call([str(BASE/'kfm-ebird-capacity'),'--performance-report',str(o1/'performance_report.json'),'--resource-profile',str(o1/'resource_profile.json'),'--artifact-size-report',str(o1/'artifact_size_report.json'),'--out-dir',str(cap)])
  assert (o1/'benchmark_results.jsonl').exists(); assert (cap/'capacity_plan.json').exists()
