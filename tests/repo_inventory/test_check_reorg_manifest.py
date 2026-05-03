import subprocess

def test_manifest_checker_runs():
    p = subprocess.run(['python','tools/repo_inventory/check_reorg_manifest.py','docs/registers/reorg'],capture_output=True,text=True)
    assert p.returncode == 0, p.stdout + p.stderr
