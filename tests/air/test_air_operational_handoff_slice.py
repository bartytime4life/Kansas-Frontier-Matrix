import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
FX=ROOT/'tests/fixtures/air/operational_handoff/pass_fixture_handoff_closure'

def run(*a): return subprocess.run([sys.executable,*map(str,a)],capture_output=True,text=True)

def test_pass(tmp_path):
 h=tmp_path/'handoff';w=tmp_path/'watch';n=tmp_path/'notice';e=tmp_path/'archive';c=tmp_path/'closure';a=tmp_path/'audit'
 assert run(ROOT/'tools/operations/air/build_air_operational_handoff.py','--cutover-dir',FX/'cutover','--authorization-dir',FX/'authorization','--deployment-readiness-dir',FX/'deployment_readiness','--delivery-dir',FX/'delivery','--out-dir',h,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-handoff').returncode==0
 assert run(ROOT/'tools/operations/air/evaluate_air_watch_window.py','--handoff-dir',h,'--cutover-dir',FX/'cutover','--out-dir',w,'--as-of','2026-04-30T00:00:00Z','--allow-fixture-watch').returncode==0
 assert run(ROOT/'tools/operations/air/finalize_air_stakeholder_notice_candidate.py','--stakeholder-notice-draft',FX/'cutover/stakeholder_notice_draft.json','--handoff-dir',h,'--ledger',FX/'cutover/release_ledger_manifest.json','--out-dir',n,'--fixture-only').returncode==0
 assert run(ROOT/'tools/operations/air/build_air_evidence_archive_manifest.py','--handoff-dir',h,'--cutover-dir',FX/'cutover','--authorization-dir',FX/'authorization','--deployment-readiness-dir',FX/'deployment_readiness','--delivery-dir',FX/'delivery','--out-dir',e,'--allow-fixture-archive').returncode==0
 assert run(ROOT/'tools/operations/air/prepare_air_release_closure_dossier.py','--handoff-dir',h,'--watch-evaluation',w/'watch_window_evaluation.json','--evidence-archive',e/'evidence_archive_manifest.json','--notice-finalization',n/'stakeholder_notice_finalization.json','--out-dir',c,'--fixture-only').returncode==0
 assert run(ROOT/'tools/validators/air/validate_air_operational_handoff.py',h,w,n,e,c).returncode==0
 assert run(ROOT/'tools/auditors/air/audit_air_operational_handoff.py',h,w,n,e,c,'--out-dir',a).returncode==0
