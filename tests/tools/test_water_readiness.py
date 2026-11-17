"""Read-only readiness replays the real candidate and serving gates, without promotion."""
import json
from datetime import datetime, timezone

import pytest

from tests.tools.test_water_release import OWNER, prepared
from tools.release import water_release

NOW = datetime(2026, 9, 30, 19, 0, tzinfo=timezone.utc)


def contents(root):
    return {path.relative_to(root).as_posix(): path.read_bytes()
            for path in root.rglob("*") if path.is_file()}


def decision_for(package_id):
    return water_release.build_decision(package_id, reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)


def test_missing_decision_is_hold_and_assessment_never_writes(tmp_path):
    root, package = prepared(tmp_path, admitted=True)
    before = contents(root)
    first = water_release.assess(root, package["package_id"], decision=None, now=NOW)
    second = water_release.assess(root, package["package_id"], decision=None, now=NOW)
    assert first == second
    assert contents(root) == before
    assert (first["outcome"], first["candidate_outcome"], first["decision_present"]) == ("HOLD", "HOLD", False)
    assert "REVIEW_REQUIRED" in first["reason_codes"]
    assert {row["outcome"] for row in first["views"].values()} == {"ABSTAIN"}
    assert not any(first["effects"].values())


def test_eligible_candidate_still_requires_operational_acceptance(tmp_path):
    root, package = prepared(tmp_path, admitted=True)
    before = contents(root)
    result = water_release.assess(root, package["package_id"], decision=decision_for(package["package_id"]), now=NOW)
    assert contents(root) == before
    assert result["candidate_outcome"] == "READY"
    assert result["outcome"] == "HOLD"
    assert set(result["views"]) == {"bootstrap", "layers", "evidence"}
    assert {row["outcome"] for row in result["views"].values()} == {"ANSWER"}
    assert result["evidence_ref_count"] == 2
    assert result["review_acceptance"] == "NOT_EVALUATED"
    assert "HOSTED_READBACK_REQUIRED" in result["reason_codes"]
    assert "OPERATOR_ROLLBACK_READBACK_REQUIRED" in result["reason_codes"]
    assert result["snapshot_sha256"].startswith("sha256:")
    assert result["candidate_id"] == package["candidate_id"]
    assert result["operational_state"] == "NOT_INSPECTED"
    assert not any(result["effects"].values())


@pytest.mark.parametrize(("change", "reason"), [
    ({"expires_at": "2026-09-30T19:00:00Z"}, "RELEASE_TIME_INVALID"),
    ({"correction_state": "WITHDRAWN"}, "CORRECTION_HOLD"),
    ({"package_id": "sha256:" + "f" * 64}, "RELEASE_BINDING_MISMATCH"),
    ({"decision": "DENIED"}, "RELEASE_NOT_APPROVED"),
])
def test_existing_negative_decisions_remain_withheld(tmp_path, change, reason):
    root, package = prepared(tmp_path, admitted=True)
    decision = decision_for(package["package_id"]) | change
    result = water_release.assess(root, package["package_id"], decision=decision, now=NOW)
    assert result["candidate_outcome"] == result["outcome"] == "HOLD"
    assert reason in result["reason_codes"]
    assert {row["outcome"] for row in result["views"].values()} == {"ABSTAIN"}


def test_unadmitted_candidate_cannot_be_made_ready_by_owner_self_release(tmp_path):
    root, package = prepared(tmp_path, admitted=False)
    result = water_release.assess(root, package["package_id"], decision=decision_for(package["package_id"]), now=NOW)
    assert result["candidate_outcome"] == "HOLD"
    assert "INDEPENDENT_REVIEW_REQUIRED" in result["reason_codes"]


def test_readiness_refuses_corrupt_snapshot_and_preserves_capture(tmp_path):
    root, package = prepared(tmp_path, admitted=True)
    snapshot = root / "release/candidates/hydrology" / package["package_id"].split(":")[1] / "snapshot.json"
    original = snapshot.read_bytes()
    snapshot.write_bytes(original.replace(b'"candidate.json"', b'"other.json"', 1))
    before = contents(root)
    with pytest.raises(ValueError):
        water_release.assess(root, package["package_id"], decision=None, now=NOW)
    assert contents(root) == before
    snapshot.write_bytes(original)
    assert water_release.assess(root, package["package_id"], decision=None, now=NOW)["candidate_outcome"] == "HOLD"


def test_cli_has_nonzero_hold_and_safe_finite_error(tmp_path, capsys):
    root, package = prepared(tmp_path, admitted=True)
    args = ["assess", "--root", str(root), "--package-id", package["package_id"]]
    before = contents(root)
    assert water_release.main(args) == 3
    assert json.loads(capsys.readouterr().out)["outcome"] == "HOLD"
    assert water_release.main(args + ["--decision", "../private-decision.json"]) == 1
    assert json.loads(capsys.readouterr().out) == {"outcome": "ERROR", "reason_code": "DECISION_PATH_INVALID"}
    args[-1] = "private/path/invalid"
    assert water_release.main(args) == 1
    assert json.loads(capsys.readouterr().out) == {"outcome": "ERROR", "reason_code": "PACKAGE_ID_INVALID"}
    assert contents(root) == before
