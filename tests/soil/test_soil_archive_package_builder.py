from pathlib import Path
import json,subprocess,sys

def run(cmd):
    return subprocess.run([sys.executable,*cmd],capture_output=True,text=True)

def test_builder_and_check(tmp_path):
    pr=tmp_path/'pres'; rr=tmp_path/'rec'; fr=tmp_path/'fed'; dr=tmp_path/'disc'; pub=tmp_path/'pub'; ops=tmp_path/'ops'; out=tmp_path/'arch'
    pid='soil-preservation-test'; rid='soil-release-test'
    (pr/f'preservation/soil/packages/{pid}').mkdir(parents=True)
    manifest={'object_type':'SoilPreservationManifest','preservation_status':'PRESERVATION_READY','preservation_id':pid,'reconciliation_id':'r1','federation_id':'f1','discovery_id':'d1','release_id':rid,'records':[{'bundle_id':'b1','sensitivity':'public','publication_status':'PUBLISHED','rights_status':'open','evidence_bundle_ref':'ev'}]}
    receipt={'decision':'pass','signatures':{'x':1},'live_archive_upload_performed':False,'live_doi_minting_performed':False}
    fix={'artifacts':{}}
    merkle={'leaves':[],'merkle_root':''}
    for n,p in [('preservation_manifest.json',manifest),('preservation_receipt.json',receipt),('fixity_manifest.json',fix),('merkle_tree.json',merkle)]: (pr/f'preservation/soil/packages/{pid}/{n}').write_text(json.dumps(p))
    (pr/'preservation/soil').mkdir(parents=True,exist_ok=True); (pr/'preservation/soil/current_preservation.json').write_text(json.dumps({'active_preservation_id':pid}))
    (ops/'ops/soil/status').mkdir(parents=True); (ops/'ops/soil/status/current_status.json').write_text(json.dumps({'public_access_allowed':True,'latest_probe':{'decision':'pass'},'active_incidents':[]}))
    (pub/'published/soil').mkdir(parents=True); (pub/'published/soil/current.json').write_text(json.dumps({'current_release_id':rid}))
    cp=run(['tools/archive/soil/build_archive_package.py','--preservation-root',str(pr),'--reconciliation-root',str(rr),'--federation-root',str(fr),'--discovery-root',str(dr),'--published-root',str(pub),'--ops-root',str(ops),'--out-root',str(out),'--base-public-url','https://example.invalid/kfm/soil'])
    assert cp.returncode==0,cp.stdout+cp.stderr
    ck=run(['tools/validators/soil/archive_package_check.py','--archive-root',str(out)])
    assert ck.returncode==0
