# Synthetic Release Dry-Run: What Is Proven vs Not Proven

## What this runbook proves
Running `bash scripts/check_synthetic_release_local.sh` proves that:
- Required synthetic/no-network validation gates execute successfully.
- A synthetic dry-run receipt is produced.
- Publish is refused by policy (`publish_decision=REFUSE`) even when gates pass.

## What this runbook does **not** prove
This runbook does not prove:
- Real external connectivity behavior (network is intentionally not used).
- Live-source freshness, uptime, or third-party API correctness.
- Production deployment readiness or operational SLO compliance.
- That publication occurred (it must not occur in this dry-run path).

## Commands
- Local: `bash scripts/check_synthetic_release_local.sh`
- Direct dry-run only: `python tools/synthetic_release_dry_run.py`

## Artifacts
- Dry-run receipt: `release/dry_runs/synthetic_release_dry_run_receipt.json`
