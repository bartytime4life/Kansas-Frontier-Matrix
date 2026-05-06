import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools/publishers/air/build_air_release_candidate.py"


def run_cli(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=ROOT, capture_output=True, text=True)


def test_pass_creates_candidate_artifacts(tmp_path):
    out = tmp_path / "out"
    result = run_cli(
        "--qa-summary", "tests/fixtures/air/release_candidate/pass/qa_summary.json",
        "--run-receipt", "tests/fixtures/air/release_candidate/pass/run_receipt.json",
        "--out-dir", str(out),
        "--evidence-bundle", "tests/fixtures/air/release_candidate/pass/evidence_bundle.json",
    )
    assert result.returncode == 0
    assert (out / "promotion_decision.json").exists()
    assert (out / "release_manifest.json").exists()
    assert (out / "catalog_candidate/stac_item.json").exists()
    assert (out / "catalog_candidate/dcat_dataset.json").exists()
    assert (out / "catalog_candidate/prov.jsonld").exists()
    assert (out / "catalog_candidate/triplets.jsonl").exists()


def test_deny_high_nowcast_nonzero_without_allow(tmp_path):
    out = tmp_path / "deny"
    result = run_cli(
        "--qa-summary", "tests/fixtures/air/release_candidate/deny_high_nowcast/qa_summary.json",
        "--run-receipt", "tests/fixtures/air/release_candidate/deny_high_nowcast/run_receipt.json",
        "--out-dir", str(out),
    )
    assert result.returncode != 0
    decision = json.loads((out / "promotion_decision.json").read_text(encoding="utf-8"))
    assert decision["decision"] == "quarantine"
    assert not (out / "catalog_candidate/stac_item.json").exists()


def test_missing_receipt_fails_closed(tmp_path):
    out = tmp_path / "missing"
    result = run_cli(
        "--qa-summary", "tests/fixtures/air/release_candidate/deny_missing_receipt/qa_summary.json",
        "--run-receipt", "tests/fixtures/air/release_candidate/deny_missing_receipt/run_receipt.json",
        "--out-dir", str(out),
        "--allow-quarantine-output",
    )
    assert result.returncode == 0
    decision = json.loads((out / "promotion_decision.json").read_text(encoding="utf-8"))
    assert decision["gates"]["run_receipt_present"]["triggered"] is True


def test_nowcast_labeled_not_validated_aqs_truth(tmp_path):
    out = tmp_path / "label"
    result = run_cli(
        "--qa-summary", "tests/fixtures/air/release_candidate/pass/qa_summary.json",
        "--run-receipt", "tests/fixtures/air/release_candidate/pass/run_receipt.json",
        "--out-dir", str(out),
    )
    assert result.returncode == 0
    evidence = json.loads((out / "evidence_bundle.json").read_text(encoding="utf-8"))
    assert evidence["measurements"]["nowcast_truth_status"] == "operational_evidence_not_validated_aqs_truth"
