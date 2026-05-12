# scripts/maintenance

Maintenance CLIs for doctrine-artifact preflight and registry hygiene.

## Doctrine artifact tooling

| Script | Purpose | Exit codes |
|---|---|---|
| `check_required_doctrine_artifacts.py` | Validate required doctrine artifacts against registry + filesystem and emit JSON receipt (`present`, `status_mismatches`). | `0=pass`, `1=fail`, `2=registry error` |
| `render_doctrine_presence_input.py` | Render `{ "present": ... }` from a checker receipt for policy consumers. | `0=success`, `1=invalid receipt` |
| `sync_doctrine_artifact_registry_status.py` | Reconcile registry `status:` fields (`present`/`missing`) against artifact files and emit sync receipt. | `0=success`, `2=registry error` |
| `run_doctrine_artifact_preflight.py` | Orchestrate checker + renderer and print a single summary payload for CI/operator use. | `0=preflight executed`, `2=execution/validation error` |

## Quick start

```bash
python scripts/maintenance/run_doctrine_artifact_preflight.py
```

Detailed operator flow: `docs/runbooks/DOCTRINE_ARTIFACT_PREFLIGHT.md`.
