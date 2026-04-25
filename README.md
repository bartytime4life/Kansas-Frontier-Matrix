# Kansas Frontier Matrix

Kansas Frontier Matrix (KFM) is a governed, evidence-first workspace for building inspectable claims from spatial and policy-aware artifacts.

## Current repository status (verified 2026-04-25)

- Repository type: docs-first with executable validation tooling.
- Baseline local verification command: `tools/ci/run_repo_baseline_local.sh`.
- Baseline CI workflow: `.github/workflows/verification-baseline.yml`.
- Current baseline test result from local run on 2026-04-25: `92 passed` in `tests/ci`.

## What this repository contains

### Governance and contracts

- `contracts/`: runtime and interface contract documentation.
- `schemas/contracts/v1/`: JSON schemas used by validation tooling.
- `policy/`: policy bundles and runtime policy tests.

### Tooling and validation

- `tools/ci/`: baseline verifiers, rendering helpers, and fixture validators.
- `tools/validators/`: contract/policy-oriented validators.
- `tools/receipts/`, `tools/proofs/`, `tools/registry/`: helper CLIs and proof/receipt/registry utilities.

### Applications

- `apps/governed-api/`: API-side runtime and route adapters.
- `apps/ui/`: UI-side mapping and adapter logic.
- `apps/web/`, `ui/`, `web/`: web and UI documentation surfaces.

### Documentation

- `docs/architecture/`: architecture references.
- `docs/adr/`: architecture decision records.
- `docs/runbooks/`: operational runbooks (including repository next-step planning).
- `docs/domains/`: domain-focused documentation lanes.

## Baseline workflow

The baseline workflow currently checks the following thin-slice path:

1. Repository and README path integrity checks.
2. Python syntax checks across repository Python files.
3. Baseline verifier checks.
4. Script-level schema and catalog checks.
5. Runtime policy fixture validation.
6. Renderer fixture validation.
7. Placeholder marker observability report.
8. `tests/ci` pytest suite.
9. Ecology API/UI boundary test slice (`apps/governed-api/ecology/tests` and `apps/ui/ecology/tests`).

This establishes a reliable minimum merge gate for repository integrity and fixture-level policy/rendering behavior.

## Local verification quickstart

From repository root:

```bash
# run full baseline verification locally
tools/ci/run_repo_baseline_local.sh

# run CI pytest slice directly
python3 -m pytest -q tests/ci
```

## Development priorities

The current priorities are tracked in:

- `docs/runbooks/repository-next-steps.md`

As of 2026-04-25, the highest-value sequence is:

1. Reduce ambiguity in root-level documentation claims.
2. Expand boundary-level contract tests for API/UI adapters.
3. Build one deterministic end-to-end governed artifact path in CI.
4. Systematically reduce unresolved documentation markers.

## Contribution expectations

When submitting changes:

- Keep claims in docs aligned with files, scripts, and tests that exist in this checkout.
- Prefer small, verifiable slices with explicit tests.
- Extend existing validators/tests instead of introducing parallel one-off checks.
- Update runbooks when operational expectations change.

## Useful paths

- Baseline workflow: `.github/workflows/verification-baseline.yml`
- Baseline local runner: `tools/ci/run_repo_baseline_local.sh`
- Baseline verifier: `tools/ci/verify_baseline.sh`
- Python syntax checker: `tools/ci/check_python_syntax.sh` (optional manifest mode supported)
- Placeholder marker report: `tools/ci/report_placeholder_markers.py`
- CI tests: `tests/ci/`
- Policy runtime fixtures: `policy/fixtures/runtime/`
- Next-step runbook: `docs/runbooks/repository-next-steps.md`

---

If you are looking for the immediate execution plan, start with `docs/runbooks/repository-next-steps.md`.
