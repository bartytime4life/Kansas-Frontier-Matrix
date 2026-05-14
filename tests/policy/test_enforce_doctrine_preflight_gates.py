import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "maintenance" / "enforce_doctrine_preflight_gates.sh"


def test_enforce_doctrine_preflight_gates_returns_nonzero_when_provenance_fails():
    cmd = [str(SCRIPT), "--stable-filenames"]
    res = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert res.returncode == 1
    assert '"provenance_returncode": 1' in res.stdout


def test_enforce_doctrine_preflight_gates_passes_required_flags_and_user_args(tmp_path: Path):
    argv_log = tmp_path / "argv.log"
    fake_python = tmp_path / "python"
    fake_python.write_text(
        "#!/usr/bin/env bash\n"
        f"printf '%s\\n' \"$@\" > {argv_log}\n"
        "exit 7\n",
        encoding="utf-8",
    )
    fake_python.chmod(0o755)

    env = dict(os.environ)
    env["PATH"] = f"{tmp_path}:{env.get('PATH', os.defpath)}"

    user_args = ["--stable-filenames", "--emit-normalized-only"]
    res = subprocess.run([str(SCRIPT), *user_args], cwd=ROOT, env=env, capture_output=True, text=True)
    assert res.returncode == 7

    argv = argv_log.read_text(encoding="utf-8").splitlines()
    assert "scripts/maintenance/run_doctrine_artifact_preflight.py" in argv
    assert "--strict" in argv
    assert "--strict-provenance" in argv
    assert "--require-consumer-readiness" in argv
    for arg in user_args:
        assert arg in argv
    strict_ix = argv.index("--strict")
    strict_prov_ix = argv.index("--strict-provenance")
    readiness_ix = argv.index("--require-consumer-readiness")
    first_user_ix = min(argv.index(arg) for arg in user_args)
    assert strict_ix < first_user_ix
    assert strict_prov_ix < first_user_ix
    assert readiness_ix < first_user_ix
