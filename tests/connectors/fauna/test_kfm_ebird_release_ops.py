import json, subprocess, tempfile
from pathlib import Path


def mk_run(tmp:Path):
    work=tmp/'run'; work.mkdir()
    ev=work/'evidencebundle.json'; ev.write_text(json.dumps({'kfm:spec_hash':'sha256:'+'a'*64}))
    vr=work/'validation_report.json'; vr.write_text(json.dumps({'status':'pass'}))
    pub=tmp/'pub.jsonl'; pub.write_text('{"object_type":"AggregateOccurrence","policy_label":"public_aggregate","public_safe":true,"exact_points":"restricted","checklist_count":10}\n')
    pm=work/'pipeline_manifest.json'; pm.write_text(json.dumps({'run_id':'r1','kfm:spec_hash':'sha256:'+'a'*64,'suppression_min_n':10,'source_uri':'https://x?token=abc','query_predicate':'p','evidencebundle_path':str(ev),'validation_report_path':str(vr),'public_outputs':[str(pub)],'counts':{'rows_seen':1}}))
    return work,pm


def test_candidate_writes_artifacts():
    with tempfile.TemporaryDirectory() as d:
        t=Path(d); work,pm=mk_run(t)
        rel=t/'catalog/releases'
        subprocess.check_call(['python','tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_release_ops.py','--pipeline-manifest',str(pm),'--pipeline-run-dir',str(work),'--aggregate','huc12','--release-dir',str(rel)])
        root=next((rel/'huc12').glob('*'))
        for f in ['release_candidate.json','release_delta_report.json','release_quality_scorecard.json','public_changelog.json','public_changelog.md','release_receipt.json','rollback_plan.json','retention_plan.json']:
            assert (root/f).exists()


def test_dry_run_no_write():
    with tempfile.TemporaryDirectory() as d:
        t=Path(d); work,pm=mk_run(t); rel=t/'catalog/releases'
        subprocess.check_call(['python','tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_release_ops.py','--pipeline-manifest',str(pm),'--pipeline-run-dir',str(work),'--aggregate','huc12','--release-dir',str(rel),'--dry-run'])
        assert not rel.exists()
