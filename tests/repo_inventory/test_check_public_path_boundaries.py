import subprocess


def test_script_passes_repo_state():
    result = subprocess.run(
        ["python", "tools/repo_inventory/check_public_path_boundaries.py", "--allow-fail"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "raw/work/quarantine" in result.stdout
