import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIX = ROOT / "tests/fixtures/air/reentry_publication_materialization/pass_fixture_materialization_preview"

PLAN = ROOT / "tools/publishers/air/plan_air_reentry_publication_materialization.py"
PREVIEW = ROOT / "tools/publishers/air/materialize_air_reentry_publication_preview.py"
FINALIZE = ROOT / "tools/publishers/air/finalize_air_reentry_publication_manifest_candidate.py"
RECEIPT = ROOT / "tools/publishers/air/build_air_reentry_publication_receipt_candidate.py"
REFRESH = ROOT / "tools/publishers/air/request_air_reentry_public_read_model_refresh.py"
LEDGER = ROOT / "tools/publishers/air/build_air_reentry_publication_materialization_ledger.py"
POSTCHECK = ROOT / "tools/publishers/air/run_air_reentry_publication_materialization_postcheck.py"
VALIDATE = ROOT / "tools/validators/air/validate_air_reentry_publication_materialization.py"
AUDIT = ROOT / "tools/auditors/air/audit_air_reentry_publication_materialization.py"

def run(args):
    return subprocess.run(args, capture_output=True, text=True)

def test_materialization_slice_smoke(tmp_path):
    b = FIX / "publication_boundary"
    pdir = tmp_path / "plan"
    mdir = tmp_path / "preview"
    fdir = tmp_path / "finalize"
    rdir = tmp_path / "receipt"
    qdir = tmp_path / "refresh"
    ldir = tmp_path / "ledger"
    cdir = tmp_path / "postcheck"
    adir = tmp_path / "audit"
    asof = "2026-04-30T00:00:00Z"
    assert run(["python", str(PLAN), "--publication-boundary-dir", str(b), "--publication-boundary-ledger", str(b/"reentry_publication_boundary_ledger_manifest.json"), "--publication-boundary-postcheck", str(b/"reentry_publication_boundary_postcheck_report.json"), "--publication-boundary-audit", str(b/"reentry_publication_boundary_audit_report.json"), "--out-dir", str(pdir), "--as-of", asof, "--allow-fixture-plan"]).returncode == 0
    assert run(["python", str(PREVIEW), "--materialization-plan", str(pdir/"reentry_publication_materialization_plan.json"), "--publication-boundary-dir", str(b), "--out-dir", str(mdir), "--as-of", asof, "--fixture-only"]).returncode == 0
    assert run(["python", str(FINALIZE), "--artifact-preview-manifest", str(mdir/"reentry_publication_artifact_preview_manifest.json"), "--publication-manifest-candidate", str(b/"reentry_publication_manifest_candidate.json"), "--publication-eligibility-decision", str(b/"reentry_publication_eligibility_decision.json"), "--out-dir", str(fdir), "--as-of", asof, "--fixture-only"]).returncode == 0
    assert run(["python", str(RECEIPT), "--materialization-plan", str(pdir/"reentry_publication_materialization_plan.json"), "--artifact-preview-manifest", str(mdir/"reentry_publication_artifact_preview_manifest.json"), "--manifest-finalization-candidate", str(fdir/"reentry_publication_manifest_finalization_candidate.json"), "--out-dir", str(rdir), "--as-of", asof, "--fixture-only"]).returncode == 0
    assert run(["python", str(REFRESH), "--publication-receipt-candidate", str(rdir/"reentry_publication_receipt_candidate.json"), "--artifact-preview-manifest", str(mdir/"reentry_publication_artifact_preview_manifest.json"), "--manifest-finalization-candidate", str(fdir/"reentry_publication_manifest_finalization_candidate.json"), "--out-dir", str(qdir), "--as-of", asof, "--fixture-only"]).returncode == 0
    assert run(["python", str(LEDGER), "--materialization-dir", str(pdir), "--materialization-dir", str(mdir), "--materialization-dir", str(fdir), "--materialization-dir", str(rdir), "--materialization-dir", str(qdir), "--out-dir", str(ldir), "--as-of", asof, "--allow-fixture-ledger"]).returncode == 0
    assert run(["python", str(POSTCHECK), "--materialization-dir", str(pdir), "--materialization-dir", str(mdir), "--materialization-dir", str(fdir), "--materialization-dir", str(rdir), "--materialization-dir", str(qdir), "--materialization-ledger", str(ldir/"reentry_publication_materialization_ledger_manifest.json"), "--publication-boundary-dir", str(b), "--out-dir", str(cdir), "--as-of", asof, "--allow-fixture-postcheck"]).returncode == 0
    assert run(["python", str(VALIDATE), str(pdir), str(mdir), str(fdir), str(rdir), str(qdir), str(ldir), str(cdir), "--publication-boundary-dir", str(b), "--as-of", asof]).returncode == 0
    assert run(["python", str(AUDIT), str(pdir), str(mdir), str(fdir), str(rdir), str(qdir), str(ldir), str(cdir), "--publication-boundary-dir", str(b), "--source-publication-boundary-dir", str(b), "--out-dir", str(adir), "--as-of", asof]).returncode == 0
