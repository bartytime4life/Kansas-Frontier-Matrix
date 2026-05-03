import subprocess

def test_orphan_script_runs():
    r=subprocess.run(['python','tools/repo_inventory/check_doc_orphans.py'],capture_output=True,text=True)
    assert 'orphan_count=' in r.stdout
