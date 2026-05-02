import subprocess
from pathlib import Path

CMD = ["python", "tools/validators/governance/validate_decision_log.py"]
BUNDLE = "tests/fixtures/governance/policy_bundles/promotion_bundle_v1.json"


def run(path: str, run_receipt: str, policy_input: str):
    return subprocess.run(CMD + [path, run_receipt, BUNDLE, policy_input], capture_output=True, text=True)


def test_valid_fixtures_pass():
    cases = [
        (
            "tests/fixtures/governance/decision_log/valid_allow.json",
            "tests/fixtures/governance/run_receipts/valid_run_receipt_with_decision_log.json",
            "tests/fixtures/governance/policy_inputs/promotion_allow_input.json",
        ),
        (
            "tests/fixtures/governance/decision_log/valid_deny_with_obligations.json",
            "tests/fixtures/governance/run_receipts/valid_run_receipt_with_decision_log_deny.json",
            "tests/fixtures/governance/policy_inputs/promotion_deny_input.json",
        ),
    ]
    for decision_log, run_receipt, policy_input in cases:
        assert run(decision_log, run_receipt, policy_input).returncode == 0, decision_log


def test_invalid_fixtures_fail():
    for p in Path("tests/fixtures/governance/decision_log").glob("invalid_*.json"):
        r = run(
            str(p),
            "tests/fixtures/governance/run_receipts/valid_run_receipt_with_decision_log.json",
            "tests/fixtures/governance/policy_inputs/promotion_allow_input.json",
        )
        assert r.returncode != 0, p
