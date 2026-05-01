from pathlib import Path
import subprocess, json, tempfile

def test_smoke_package_and_qa(tmp_path: Path):
    src = tmp_path/'cand'; src.mkdir()
    (src/'candidate_reentry_manifest.json').write_text('{}')
    (src/'candidate_reentry_package.json').write_text('{}')
    (src/'candidate_reentry_promotion_decision.json').write_text('{}')
    post = tmp_path/'post.json'; post.write_text('{"result":"pass_fixture"}')
    aud = tmp_path/'aud.json'; aud.write_text('{"result":"pass"}')
    led = tmp_path/'led.json'; led.write_text('{"chain_hash":"ok"}')
    out = tmp_path/'out'
    subprocess.check_call(['python','tools/operations/air/build_air_reentry_release_candidate_refresh_package.py','--candidate-reentry-refresh-dir',str(src),'--candidate-reentry-refresh-ledger',str(led),'--candidate-reentry-refresh-postcheck',str(post),'--candidate-reentry-refresh-audit',str(aud),'--out-dir',str(out),'--fixture-only'])
    pkg = out/'reentry_release_candidate_refresh_package.json'
    assert pkg.exists()
    out2 = tmp_path/'out2'
    subprocess.check_call(['python','tools/operations/air/run_air_reentry_qa_revalidation_refresh.py','--release-candidate-refresh-package',str(pkg),'--out-dir',str(out2),'--allow-fixture-qa'])
    rep=json.loads((out2/'reentry_qa_revalidation_refresh_report.json').read_text())
    assert rep['result']=='pass_fixture'
