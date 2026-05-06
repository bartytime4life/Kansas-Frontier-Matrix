from test_soil_public_stability_builder import test_build,ROOT
import subprocess,sys

def test_gate(tmp_path):
 test_build(tmp_path)
 args=[sys.executable,ROOT/'tools/validators/soil/public_stability_gate.py','--stability-root',tmp_path]
 for n in ['continuity','resilience','closure','incident','observability','delivery','routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  args += [f'--{n}-root',str(tmp_path)]
 p=subprocess.run(args,capture_output=True,text=True)
 assert p.returncode==0
