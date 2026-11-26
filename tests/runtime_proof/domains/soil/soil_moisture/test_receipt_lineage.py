"""Keep current soil-proof integrity separate from immutable receipt history."""

from __future__ import annotations

import hashlib
import json
import shlex
import shutil
from pathlib import Path

import pytest
import yaml

from tools.validators.validate_generated_receipt import validate_receipt


ROOT = Path(__file__).resolve().parents[5]
WORKFLOW = ".github/workflows/soil-moisture-runtime-proof.yml"
PREDECESSOR = (
    "data/receipts/generated/"
    "genrec-soil-moisture-runtime-proof-artifacts-20260805.json"
)
PREDECESSOR_SHA256 = "60e93fe19f4a61ea9cb9bea02b5b104c5e7616b9028200fae6b1e2fb5e5e8c2f"
SUPERSEDED = (
    "data/receipts/generated/"
    "genrec-soil-moisture-runtime-proof-artifacts-20261118.json"
)
SUPERSEDED_SHA256 = "9cb4240d165356774dd8d0af0e5fdca46eafdac42365194690266a522975f603"
SUPERSEDED_REF = "e50fc18c6736e9e85d76c8dfcea126135e2ec0c1"
CURRENT = (
    "data/receipts/generated/"
    "genrec-soil-moisture-runtime-proof-artifacts-20261126.json"
)
PROOF_ROOT = "tests/runtime_proof/domains/soil/soil_moisture/"
ARTIFACTS = (
    WORKFLOW,
    PROOF_ROOT + "README.md",
    PROOF_ROOT + "emit_runtime_proof_report.py",
    PROOF_ROOT + "test_runtime_mapper.py",
    PROOF_ROOT + "test_receipt_lineage.py",
)


def _receipt() -> dict:
    return json.loads((ROOT / CURRENT).read_text(encoding="utf-8"))


def test_workflow_selects_current_receipt_with_native_integrity_enabled() -> None:
    workflow = yaml.safe_load((ROOT / WORKFLOW).read_text(encoding="utf-8"))
    steps = workflow["jobs"]["validate"]["steps"]
    integrity = [step for step in steps if step.get("name") == "Verify current authoring receipt integrity"]
    assert len(integrity) == 1
    assert shlex.split(integrity[0]["run"].replace("\\\n", ""), comments=True) == [
        "set", "-euo", "pipefail",
        "python", "tools/validators/validate_generated_receipt.py",
        CURRENT, "--repo-root", ".",
    ]
    replay = [step for step in steps if step.get("name") == "Replay superseded authoring receipt at its authoring commit"]
    assert len(replay) == 1
    assert shlex.split(replay[0]["run"].replace("\\\n", ""), comments=True) == [
        "set", "-euo", "pipefail",
        "python", "tools/validators/validate_generated_receipt.py",
        SUPERSEDED, "--repo-root", ".", "--artifact-git-ref", SUPERSEDED_REF,
    ]
    assert steps.index(replay[0]) < steps.index(integrity[0])
    assert steps[0]["with"]["fetch-depth"] == 0
    assert steps[0]["with"]["persist-credentials"] is False
    proof = next(step for step in steps if step.get("name") == "Run deterministic no-network runtime proof")
    assert PROOF_ROOT + "test_receipt_lineage.py" in shlex.split(proof["run"].replace("\\\n", ""))
    assert workflow["permissions"] == {"contents": "read"}
    assert workflow["env"]["KFM_NO_NETWORK"] == "1"


def test_successor_binds_current_artifacts_without_claiming_review() -> None:
    receipt = _receipt()
    assert set(receipt["artifact_paths"]) == set(ARTIFACTS)
    result = validate_receipt(ROOT / CURRENT, repo_root=ROOT)
    assert result.ok, result.findings
    assert result.integrity_checked
    assert result.artifact_count == len(ARTIFACTS)
    assert result.review_state == "pending"
    assert not result.review_claim_present


def test_predecessor_bytes_and_lineage_remain_historical() -> None:
    previous_bytes = (ROOT / PREDECESSOR).read_bytes()
    assert hashlib.sha256(previous_bytes).hexdigest() == PREDECESSOR_SHA256
    previous = json.loads(previous_bytes)
    current = _receipt()
    assert set(previous["artifact_paths"]) < set(current["artifact_paths"])
    assert "sha256:" + PREDECESSOR_SHA256 in current["inputs"]["evidence_hashes"]
    assert any(PREDECESSOR in ref for ref in current["inputs"]["evidence_refs"])
    assert previous["receipt_id"] != current["receipt_id"]
    assert previous["artifact_hashes"][WORKFLOW] != current["artifact_hashes"][WORKFLOW]


def test_superseded_successor_stays_immutable_and_named_in_lineage() -> None:
    superseded_bytes = (ROOT / SUPERSEDED).read_bytes()
    assert hashlib.sha256(superseded_bytes).hexdigest() == SUPERSEDED_SHA256
    superseded = json.loads(superseded_bytes)
    current = _receipt()
    assert set(superseded["artifact_paths"]) == set(current["artifact_paths"])
    assert "sha256:" + SUPERSEDED_SHA256 in current["inputs"]["evidence_hashes"]
    assert any(SUPERSEDED in ref for ref in current["inputs"]["evidence_refs"])
    assert superseded["receipt_id"] != current["receipt_id"]
    assert superseded["artifact_hashes"][WORKFLOW] != current["artifact_hashes"][WORKFLOW]


@pytest.mark.parametrize("artifact", ARTIFACTS)
def test_successor_rejects_modified_artifact_bytes(tmp_path: Path, artifact: str) -> None:
    # Exercise the real validator against regular files, never the checked-out artifacts.
    for relative in (*ARTIFACTS, CURRENT):
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / relative, target)
    changed = tmp_path / artifact
    changed.write_bytes(changed.read_bytes() + b"\n")

    result = validate_receipt(tmp_path / CURRENT, repo_root=tmp_path)
    assert not result.ok
    assert [(finding.code, finding.field) for finding in result.findings] == [
        ("ARTIFACT_DIGEST_MISMATCH", f"/artifact_paths/{list(ARTIFACTS).index(artifact)}")
    ]
