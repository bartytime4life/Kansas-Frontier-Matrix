import pytest
import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIX=ROOT/'tests/fixtures/air/reentry_publication_materialization/pass_fixture_materialization_preview/publication_boundary'

def run(cmd):
 r=subprocess.run(cmd,capture_output=True,text=True)
 assert r.returncode==0,(cmd,r.stdout,r.stderr)

@pytest.mark.xfail(reason="stale air reentry fixtures/schema paths removed during restructuring")
def test_smoke(tmp_path):
 plan=tmp_path/'plan';prev=tmp_path/'prev';fin=tmp_path/'fin';rec=tmp_path/'rec';ref=tmp_path/'ref';led=tmp_path/'led';post=tmp_path/'post';aud=tmp_path/'aud'
 run([sys.executable,str(ROOT/'tools/publishers/air/plan_air_reentry_publication_materialization.py'),'--publication-boundary-dir',str(FIX),'--publication-boundary-ledger',str(FIX/'reentry_publication_boundary_ledger_manifest.json'),'--publication-boundary-postcheck',str(FIX/'reentry_publication_boundary_postcheck_report.json'),'--publication-boundary-audit',str(FIX/'reentry_publication_boundary_audit_report.json'),'--out-dir',str(plan),'--as-of','2026-04-30T00:00:00Z','--allow-fixture-plan'])
 run([sys.executable,str(ROOT/'tools/publishers/air/materialize_air_reentry_publication_preview.py'),'--materialization-plan',str(plan/'reentry_publication_materialization_plan.json'),'--publication-boundary-dir',str(FIX),'--out-dir',str(prev),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/publishers/air/finalize_air_reentry_publication_manifest_candidate.py'),'--artifact-preview-manifest',str(prev/'reentry_publication_artifact_preview_manifest.json'),'--publication-manifest-candidate',str(FIX/'reentry_publication_manifest_candidate.json'),'--publication-eligibility-decision',str(FIX/'reentry_publication_eligibility_decision.json'),'--out-dir',str(fin),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_receipt_candidate.py'),'--materialization-plan',str(plan/'reentry_publication_materialization_plan.json'),'--artifact-preview-manifest',str(prev/'reentry_publication_artifact_preview_manifest.json'),'--manifest-finalization-candidate',str(fin/'reentry_publication_manifest_finalization_candidate.json'),'--out-dir',str(rec),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/publishers/air/request_air_reentry_public_read_model_refresh.py'),'--publication-receipt-candidate',str(rec/'reentry_publication_receipt_candidate.json'),'--artifact-preview-manifest',str(prev/'reentry_publication_artifact_preview_manifest.json'),'--manifest-finalization-candidate',str(fin/'reentry_publication_manifest_finalization_candidate.json'),'--out-dir',str(ref),'--fixture-only'])
 run([sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_materialization_ledger.py'),'--materialization-dir',str(plan),'--materialization-dir',str(prev),'--materialization-dir',str(fin),'--materialization-dir',str(rec),'--materialization-dir',str(ref),'--out-dir',str(led),'--allow-fixture-ledger'])
 run([sys.executable,str(ROOT/'tools/publishers/air/run_air_reentry_publication_materialization_postcheck.py'),'--materialization-dir',str(plan),'--materialization-ledger',str(led/'reentry_publication_materialization_ledger_manifest.json'),'--out-dir',str(post),'--allow-fixture-postcheck'])
 run([sys.executable,str(ROOT/'tools/validators/air/validate_air_reentry_publication_materialization.py'),str(plan),str(prev),str(fin),str(rec),str(ref),str(led),str(post)])
 run([sys.executable,str(ROOT/'tools/auditors/air/audit_air_reentry_publication_materialization.py'),str(plan),str(prev),str(fin),str(rec),str(ref),str(led),str(post),'--out-dir',str(aud)])
