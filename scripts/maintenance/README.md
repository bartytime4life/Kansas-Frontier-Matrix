# scripts/maintenance

Maintenance CLIs for doctrine-artifact preflight and registry hygiene.

## Doctrine artifact tooling

| Script | Purpose | Exit codes |
|---|---|---|
| `check_required_doctrine_artifacts.py` | Validate required doctrine artifacts against registry + filesystem and emit JSON receipt (`present`, `status_mismatches`). | `0=pass`, `1=fail`, `2=registry error` |
| `check_doctrine_artifact_provenance.py` | Validate canonical source-link provenance registry shape for required doctrine artifacts. | `0=pass`, `1=fail`, `2=registry error` |
| `render_doctrine_presence_input.py` | Render `{ "present": ... }` from a checker receipt for policy consumers. | `0=success`, `1=invalid receipt` |
| `sync_doctrine_artifact_registry_status.py` | Reconcile registry `status:` fields (`present`/`missing`) against artifact files and emit sync receipt. | `0=success`, `1=changes needed (with --fail-on-change)`, `2=registry error` |
| `sync_doctrine_artifact_provenance_status.py` | Reconcile provenance `status` (`pending`→`verified`) when required artifact files are present; optional in-place write. | `0=success` |
| `run_doctrine_artifact_preflight.py` | Orchestrate checker + renderer and print a single summary payload for CI/operator use (timestamped receipts by default; `--stable-filenames` for deterministic names; optional `--presence-output` artifact). | `0=preflight executed`, `1=strict missing-artifact fail`, `2=execution/validation error` |

## Quick start

```bash
python scripts/maintenance/run_doctrine_artifact_preflight.py
```

Detailed operator flow: `docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md`.

## Test bundle

```bash
./scripts/maintenance/run_doctrine_artifact_test_suite.sh
```
