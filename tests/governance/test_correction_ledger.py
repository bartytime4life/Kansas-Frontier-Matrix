import json,subprocess
CMD=["python","tools/governance/build_correction_ledger.py"]
P='tests/fixtures/governance/corrections/valid/'

def test_ledger_builder_deterministic():
    args=[P+'correction_notice_valid.json',P+'withdrawal_notice_valid.json',P+'rollback_execution_receipt_valid.json']
    a=subprocess.run(CMD+args,capture_output=True,text=True,check=True).stdout
    b=subprocess.run(CMD+args,capture_output=True,text=True,check=True).stdout
    assert json.loads(a)['chain_hash']==json.loads(b)['chain_hash']

def test_ledger_builder_rejects_duplicate_event_ids(tmp_path):
    p=tmp_path/'dup.json'; p.write_text(open(P+'correction_notice_valid.json').read())
    r=subprocess.run(CMD+[str(p),str(p)],capture_output=True,text=True)
    assert r.returncode!=0
