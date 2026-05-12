# Doctrine Artifact Preflight Runbook

This runbook defines the standard operator/CI flow for validating required doctrine artifacts.

## Prerequisites
- Python available in PATH.
- Registry file exists: `control_plane/document_registry_doctrine_required.yaml`.

## Single-command preflight
Run the composed preflight:

```bash
python scripts/maintenance/run_doctrine_artifact_preflight.py
```

Expected behavior:
- Exit `0` when the preflight executes correctly and rendering succeeds.
- `check_returncode` in output indicates artifact state:
  - `0`: all required artifacts present and aligned.
  - `1`: one or more required artifacts missing and/or status mismatches.
- Exit `2` indicates malformed registry input or runner-level execution failure.

## Targeted validation commands
Check registry/artifact alignment and write receipt:

```bash
python scripts/maintenance/check_required_doctrine_artifacts.py \
  --registry control_plane/document_registry_doctrine_required.yaml \
  --artifacts-dir docs/doctrine/artifacts \
  --output receipts/doctrine_artifacts/check_required_doctrine_artifacts.json
```

Render policy input from receipt:

```bash
python scripts/maintenance/render_doctrine_presence_input.py \
  receipts/doctrine_artifacts/check_required_doctrine_artifacts.json
```

Sync registry `status:` fields with disk state:

```bash
python scripts/maintenance/sync_doctrine_artifact_registry_status.py \
  --registry control_plane/document_registry_doctrine_required.yaml \
  --artifacts-dir docs/doctrine/artifacts \
  --output receipts/doctrine_artifacts/sync_doctrine_artifact_registry_status.json
```

## Failure interpretation
- `result: "error"` means malformed registry (e.g., duplicate filename, invalid status, missing `doc_id`).
- `result: "fail"` means registry is structurally valid but required artifacts are not yet in compliant state.
