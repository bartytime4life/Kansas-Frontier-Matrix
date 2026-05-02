import json
import subprocess


def test_replay_allow_result():
    r = subprocess.run(
        [
            "python",
            "tools/validators/governance/replay_decision_log.py",
            "tests/fixtures/governance/policy_bundles/promotion_bundle_v1.json",
            "tests/fixtures/governance/policy_inputs/promotion_allow_input.json",
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert json.loads(r.stdout)["result"] == "allow"
