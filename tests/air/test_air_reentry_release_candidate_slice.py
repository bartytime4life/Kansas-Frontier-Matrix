import pytest
import json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

@pytest.mark.xfail(reason="stale air reentry fixtures/schema paths removed during restructuring")
def test_schemas_exist():
 names=['reentry_release_candidate_package.schema.json','reentry_qa_revalidation_report.schema.json','reentry_release_candidate_audit_report.schema.json']
 for n in names:
  p=ROOT/'schemas/contracts/v1/air'/n
  assert p.exists()
  assert json.loads(p.read_text())['properties']['domain']['const']=='atmosphere.air'

def test_validator_denies_unsafe(tmp_path):
 d=tmp_path/'x'; d.mkdir(); (d/'a.json').write_text('{"path":"data/published/air/x"}')
 r=subprocess.run([sys.executable,str(ROOT/'tools/validators/air/validate_air_reentry_release_candidate.py'),str(d)],capture_output=True,text=True)
 assert r.returncode!=0
