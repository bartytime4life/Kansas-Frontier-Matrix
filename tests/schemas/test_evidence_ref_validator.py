import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools" / "validators" / "validate_evidence_ref.py"
FIXTURE_ROOT = ROOT / "fixtures" / "contracts" / "v1" / "evidence" / "evidence_ref"


def _run_validator(fixture: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(fixture.relative_to(ROOT))],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_evidence_ref_validator_accepts_valid_fixture() -> None:
    fixture = FIXTURE_ROOT / "valid" / "valid_1.json"

    result = _run_validator(fixture)

    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.strip() == f"OK {fixture.relative_to(ROOT)}"


def test_evidence_ref_validator_rejects_missing_ref() -> None:
    fixture = FIXTURE_ROOT / "invalid" / "invalid_1.json"

    result = _run_validator(fixture)

    assert result.returncode == 1, result.stdout + result.stderr
    assert result.stdout.startswith(f"FAIL {fixture.relative_to(ROOT)}:")
    assert "'ref' is a required property" in result.stdout
