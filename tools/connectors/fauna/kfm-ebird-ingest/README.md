# KFM eBird ingest - Layer 21
Provides `kfm-ebird-quality` and `kfm-ebird-triage` CLIs for synthetic, offline QA governance and triage.


## Layer 22 CLIs
- `kfm-ebird-remediate`
- `kfm-ebird-corrective-release`

## Layer 23 (Rerun remediation and backfill)
- `kfm-ebird-rerun-remediation`: governed full-rerun planning/validation/candidate workflow for data-affecting remediation.
- `kfm-ebird-backfill`: local-only historical backfill planning/validation.

Both commands are local-only, require no network calls, and enforce the governed checklist predicate and public-safety posture.

## Layer 25: Gate + Control-plane Registration

New CLIs:
- `kfm-ebird-gate` - computes unified go/no-go across lane artifacts, writes catalog and public-safe gate summaries.
- `kfm-ebird-register` - builds local control-plane handoff artifacts (registration, capability manifest, command inventory, health status).

Both CLIs are local-only, require no credentials, and perform no network calls.

