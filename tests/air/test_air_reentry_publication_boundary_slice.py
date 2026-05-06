import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FIX=ROOT/'tests/fixtures/air/reentry_publication_boundary/pass_fixture_publication_candidate/release_candidate'

def test_smoke(tmp_path):
 gate=tmp_path/'gate';aqs=tmp_path/'aqs';rev=tmp_path/'rev';dec=tmp_path/'dec';man=tmp_path/'man';pmc=tmp_path/'pmc';lin=tmp_path/'lin';led=tmp_path/'led';post=tmp_path/'post';aud=tmp_path/'aud'
 cmds=[
 [sys.executable,str(ROOT/'tools/publishers/air/create_air_reentry_gate_d_attestation.py'),'--release-candidate-dir',str(FIX),'--out-dir',str(gate),'--fixture-only','--as-of','2026-04-30T00:00:00Z'],
 [sys.executable,str(ROOT/'tools/publishers/air/refresh_air_reentry_aqs_reconciliation.py'),'--release-candidate-package',str(FIX/'reentry_release_candidate_package.json'),'--qa-revalidation',str(FIX/'reentry_qa_revalidation_report.json'),'--evidence-bundle',str(FIX/'reentry_release_evidence_bundle.json'),'--out-dir',str(aqs),'--status','not_required','--fixture-only'],
 [sys.executable,str(ROOT/'tools/publishers/air/review_air_reentry_publication_boundary.py'),'--out-dir',str(rev)],
 [sys.executable,str(ROOT/'tools/publishers/air/decide_air_reentry_publication_eligibility.py'),'--out-dir',str(dec)],
 [sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_candidate_manifest.py'),'--out-dir',str(man)],
 [sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_manifest_candidate.py'),'--out-dir',str(pmc)],
 [sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_lineage_bridge.py'),'--out-dir',str(lin)],
 [sys.executable,str(ROOT/'tools/publishers/air/build_air_reentry_publication_boundary_ledger.py'),'--out-dir',str(led)],
 [sys.executable,str(ROOT/'tools/publishers/air/run_air_reentry_publication_boundary_postcheck.py'),'--out-dir',str(post)],
 [sys.executable,str(ROOT/'tools/validators/air/validate_air_reentry_publication_boundary.py'),str(gate),str(aqs),str(rev),str(dec),str(man),str(pmc),str(lin),str(led),str(post)],
 [sys.executable,str(ROOT/'tools/auditors/air/audit_air_reentry_publication_boundary.py'),str(gate),str(aqs),str(rev),str(dec),str(man),str(pmc),str(lin),str(led),str(post),'--out-dir',str(aud)],
 ]
 for c in cmds:
  r=subprocess.run(c,capture_output=True,text=True)
  assert r.returncode==0, (c,r.stdout,r.stderr)
