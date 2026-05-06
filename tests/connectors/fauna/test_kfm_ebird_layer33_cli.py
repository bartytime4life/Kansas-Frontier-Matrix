import json,subprocess
from pathlib import Path
BASE=Path('tools/connectors/fauna/kfm-ebird-ingest')

def test_help_version():
    assert subprocess.run([str(BASE/'kfm-ebird-audit-intake'),'--help'],check=False).returncode==0
    assert subprocess.run([str(BASE/'kfm-ebird-audit-response'),'--help'],check=False).returncode==0
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-audit-intake'),'--version'],text=True))['tool']=='audit-intake'
    assert json.loads(subprocess.check_output([str(BASE/'kfm-ebird-audit-response'),'--version'],text=True))['tool']=='audit-response'

def test_ids_deterministic(tmp_path):
    findings=tmp_path/'f.jsonl'; findings.write_text('{"finding_id":"f1","finding_type":"hash_mismatch","severity":"high","summary":"hash mismatch","public_safe":false,"exact_points":"restricted"}\n')
    cmd=[str(BASE/'kfm-ebird-audit-intake'),'--audit-finding-file',str(findings),'--out-dir',str(tmp_path/'o1'),'--public-out-dir',str(tmp_path/'p1')]
    a1=json.loads(subprocess.check_output(cmd,text=True)); a2=json.loads(subprocess.check_output(cmd,text=True)); assert a1['audit_intake_id']==a2['audit_intake_id']
    rcmd=[str(BASE/'kfm-ebird-audit-response'),'--verifier-finding-queue',str(tmp_path/'o1'/'verifier_finding_queue.jsonl'),'--decision','needs_remediation','--reason','x']
    r1=json.loads(subprocess.check_output(rcmd,text=True)); r2=json.loads(subprocess.check_output(rcmd,text=True)); assert r1['audit_response_id']==r2['audit_response_id']
