# Changed-file audit — 2026-04-30

## Scope and evidence

This audit inspects files changed on 2026-04-30 from git history and validates current checkout alignment against KFM invariants.

## Truth labels

- **CONFIRMED**: verified from repository files and command output.
- **UNKNOWN**: not verifiable in this checkout.
- **NEEDS_VERIFICATION**: requires environment/dependency setup not present locally.

## Phase 0 evidence commands (CONFIRMED)

- `pwd`
- `git status --short`
- `git branch --show-current`
- `git rev-parse HEAD`
- `git diff --name-only --diff-filter=ACMRTUXB`
- `git diff --stat`
- `git diff --check`
- `find .github docs contracts schemas policy data tools tests apps packages pipelines migrations configs release -maxdepth 4 -type f`
- `git log --since="today 00:00" --name-only --pretty=format: | sed '/^$/d' | sort -u`

## Findings summary (changed today)

### CONFIRMED

- Changed files today are concentrated in governed API, web UI ecology surfaces, contracts/schema, tests, CI workflows, and doctrine docs.
- No uncommitted working tree drift is present after audit commands.
- No whitespace or patch hygiene failures from `git diff --check`.
- Governance-critical boundaries remain represented in code and tests:
  - governed API routes are present under `apps/governed_api`.
  - ecology EvidenceBundle resolver boundary tests exist under `tests/governed_api`.
  - public-safe map/evidence client boundaries remain under `apps/web/src/api` and `apps/web/src/map`.

### NEEDS_VERIFICATION

- Python governed API test execution is blocked in this environment because `fastapi` is not installed; collection fails before behavior assertions execute.
- End-to-end runtime/build validation for the web app was not executed in this pass.

### UNKNOWN

- CI runtime outcomes for today’s changes are unknown from local checkout alone.

## Cross-file alignment matrix

| Changed file family | Related files inspected | Issue found | Required patch | Status |
|---|---|---|---|---|
| API/runtime + tests | `apps/governed_api/server.py`, `tests/governed_api/*.py` | Local env missing FastAPI dependency for tests | None in repo code; run in provisioned env or install deps | NEEDS_VERIFICATION |
| UI ecology + map adapters | `apps/web/src/ecology/*`, `apps/web/src/map/*`, `apps/web/src/api/governedClient.js` | No broken-file references found in audited paths | None | CONFIRMED |
| Schema/contract + published manifest | `schemas/contracts/v1/ecology/layer_manifest.schema.json`, `data/published/ecology/dry-run/layer_manifest.json` | No immediate path-level mismatch observed in this pass | Schema validation execution recommended in CI | NEEDS_VERIFICATION |
| Docs/architecture + control-plane docs | `docs/architecture/*`, `docs/control-plane/*` | No direct contradiction found against current governed API/layout in this pass | None | CONFIRMED |
| CI/workflows | `.github/workflows/*.yml` touched today | Workflow command execution not replayed locally in this pass | Verify workflow jobs in CI run artifacts | NEEDS_VERIFICATION |

## Minimal patch decision

- **Applied patch:** add this audit artifact only.
- **Why minimal/safe:** records current evidence and unresolved verification blockers without altering runtime behavior, policy gates, or governance boundaries.

## Rollback path

- Revert this file with:
  - `git revert <commit>` (if committed), or
  - `git rm docs/architecture/changed-file-audit-2026-04-30.md` before commit.

## Suggested follow-up actions

1. In CI or a provisioned local environment, install governed API test dependencies and run `pytest tests/governed_api -q`.
2. Run schema validation for `data/published/ecology/dry-run/layer_manifest.json` against `schemas/contracts/v1/ecology/layer_manifest.schema.json`.
3. Execute the web build/runtime checks (for example `npm --prefix apps/web test` and `npm --prefix apps/web run build`) and capture artifact links.
4. Confirm `.github/workflows/*.yml` outcomes from today’s pipeline run artifacts and attach job IDs to this audit.
