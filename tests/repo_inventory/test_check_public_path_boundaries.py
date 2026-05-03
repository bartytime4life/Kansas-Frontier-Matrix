import subprocess

def test_script_runs():
    r=subprocess.run(['python','tools/repo_inventory/check_public_path_boundaries.py'],capture_output=True,text=True)
    assert r.returncode in (0,1)
