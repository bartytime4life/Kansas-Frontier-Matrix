# REPO_ORGANIZATION_AUDIT

Date: 2026-05-03 (UTC)  
Mode: SAFE_REORG_WITH_REPORT

## 1) Executive summary

- **CONFIRMED:** The repository contains a broad governance-oriented structure with major homes present for `apps/`, `packages/`, `data/`, `docs/`, `tests/`, `tools/`, `contracts/`, `schemas/`, `policy/`, and `policies/`.
- **CONFIRMED:** Data lifecycle directories exist (`raw`, `work`, `quarantine`, `processed`, `catalog`, `triplets`, `receipts`, `proofs`, `published`, `registry`).
- **CONFLICTED:** Both `contracts/` and `schemas/` are populated; both `policy/` and `policies/` are populated. Authority split exists and requires ADR-level confirmation before any structural merge or mass move.
- **CONFIRMED:** Root contains untracked `apps/web/node_modules/` (local dependency artifact). This is clutter-like but currently uncommitted and was **not moved/deleted**.
- **ACTION TAKEN (low-risk):** Added this audit report at `docs/registers/REPO_ORGANIZATION_AUDIT.md`.
- **NO FILE MOVES:** No tracked files were moved because clear canonical target conflicts remain for key families.

## 2) Commands run

- `pwd`
- `git rev-parse --show-toplevel`
- `git branch --show-current`
- `git status --short`
- `git ls-files | wc -l`
- `find . -maxdepth 2 -type d | sort`
- `find . -maxdepth 2 -type f | sort | sed -n '1,250p'`
- `rg --files -g 'AGENTS.md' -g 'README.md' -g 'CONTRIBUTING.md' -g 'Makefile' -g 'pyproject.toml' -g 'package.json' -g 'pnpm-lock.yaml' -g 'poetry.lock' docs/adr docs/registers docs/runbooks .`
- `sed -n '1,220p' README.md`
- `sed -n '1,220p' docs/adr/README.md`
- `sed -n '1,220p' docs/registers/README.md`
- `sed -n '1,220p' docs/runbooks/README.md`
- `sed -n '1,220p' apps/web/package.json`
- `sed -n '1,220p' pytest.ini`


## 2b) Baseline command outputs (captured)

- `pwd` -> `/workspace/Kansas-Frontier-Matrix`
- `git rev-parse --show-toplevel` -> `/workspace/Kansas-Frontier-Matrix`
- `git branch --show-current` -> `work`
- `git status --short` (baseline) -> `?? apps/web/node_modules/`
- `git ls-files | wc -l` -> `7452`

## 2c) Repo stack and validation entrypoints (CONFIRMED)

- **Python/pytest stack present:** `pytest.ini` at repo root and extensive `tests/` tree.
- **Node/Vite app stack present:** `apps/web/package.json` with `vite` and `vitest` scripts.
- **Makefile present in pipeline scope:** `pipelines/kansas_biodiversity_etl/Makefile` (pipeline-local, not asserted as repo-root default).
## 3) Current repo map (evidence-grounded)

### Top-level families checked

- **Present (CONFIRMED):** `.github/`, `apps/`, `packages/`, `runtime/`, `ui/`, `web/`, `connectors/`, `pipelines/`, `pipeline_specs/`, `control_plane/`, `contracts/`, `schemas/`, `jsonschema/`, `policy/`, `policies/`, `data/`, `docs/`, `tests/`, `fixtures/`, `tools/`, `scripts/`, `infra/`, `configs/`, `release/`, `styles/`, `viewer_templates/`.

### Data lifecycle homes

- **CONFIRMED present:**
  - `data/raw`
  - `data/work`
  - `data/quarantine`
  - `data/processed`
  - `data/catalog`
  - `data/triplets`
  - `data/receipts`
  - `data/proofs`
  - `data/published`
  - `data/registry`

### Docs control-plane homes

- **CONFIRMED present:**
  - `docs/adr`
  - `docs/architecture`
  - `docs/catalog`
  - `docs/control-plane`
  - `docs/domains`
  - `docs/registers`
  - `docs/runbooks`
  - `docs/sources`
  - `docs/standards`
  - `docs/tracking`
- **UNKNOWN/PROPOSED:** `docs/reports` (no clearly established `docs/reports` home detected at maxdepth-2 inspection).

## 4) CONFIRMED canonical homes

Based on present README/index signals and directory occupation:

- `docs/adr/` as ADR home (**CONFIRMED by path + ADR README intent**).
- `docs/registers/` as register home (**CONFIRMED by path + register index + existing register files**).
- `docs/runbooks/` as runbook home (**CONFIRMED by path + runbooks README index**).
- `apps/web/` as an active Node/Vite web shell home (**CONFIRMED by `package.json` scripts/deps**).
- Python test harness exists at repo level (**CONFIRMED by `pytest.ini` + substantial `tests/` tree**).

## 5) CONFLICTED / UNKNOWN homes

- `contracts/` vs `schemas/` = **CONFLICTED** (both active; no single-home resolution asserted here).
- `policy/` vs `policies/` = **CONFLICTED** (both active; both contain policy-like material).
- `apps/ui` vs `ui` vs `web` vs `apps/web` = **CONFLICTED/NEEDS_VERIFICATION** for canonical runtime app boundary.
- `tools/` vs `scripts/` = **NEEDS_VERIFICATION** for ownership and purpose boundaries (both heavily populated).
- `fixtures/` vs `tests/fixtures` = **NEEDS_VERIFICATION** (both exist and likely serve distinct scopes).

## 6) Misplaced file/folder table

| current_path | classification | issue | recommended_home | action_taken | reason | risk | references_updated | rollback |
|---|---|---|---|---|---|---|---|---|
| `apps/web/node_modules/` (untracked) | Root/project clutter artifact | Local dependency install appears in working tree | Keep local; ensure ignored by VCS policy | None | Not tracked, risky to alter repo ignore policy in audit-only pass | Low | N/A | N/A |
| `contracts/` and `schemas/` | Competing authority homes | Parallel contract/schema families | ADR resolution first | None | High blast radius, ambiguous authority | High | None | N/A |
| `policy/` and `policies/` | Competing authority homes | Parallel policy families | ADR + CI/runtime ref audit first | None | High risk to enforcement semantics | High | None | N/A |
| `ui/`, `web/`, `apps/ui/`, `apps/web/` | Competing app/UI homes | Multiple plausible UI homes | Determine built/deployed canonical path | None | Build/runtime ambiguity | High | None | N/A |

## 7) High-risk items intentionally not moved

- No moves under `data/` lifecycle directories.
- No merges/renames for `contracts/`/`schemas`.
- No merges/renames for `policy/`/`policies`.
- No app-path refactors across `apps/*`, `ui/`, `web/`.
- No source-authority, rights, sensitivity, proof, receipt, release, or promotion object moves.

## 8) Suggested ADRs (PROPOSED)

1. **Schema authority ADR update/confirmation** for `contracts/` vs `schemas` boundaries and allowed cross-links.
2. **Policy authority ADR** for `policy/` vs `policies` roles (engine-ready vs examples vs distribution).
3. **App surface canonicalization ADR** for `apps/web`, `web`, `ui`, and `apps/ui` with CI-validated build path.
4. **Fixtures boundary ADR or register note** for `fixtures/` vs `tests/fixtures` taxonomy.

## 9) Suggested next PRs (smallest-first)

1. Add explicit register entry linking this audit from `docs/registers/README.md`.
2. Add path-boundary matrix doc for `contracts/schemas` and `policy/policies` (no moves). **(Completed via `docs/adr/ADR-0012-authority-boundary-compatibility-map.md` on 2026-05-03.)**
3. Add CI check(s) that assert canonical app build/test entrypoint(s).
4. Decide and document handling of local `node_modules` artifacts (ignore hygiene) without changing governance artifacts.

## 10) Validation results

Validation executed after report creation:

- `git status --short`
- `git diff --stat`
- `git diff --name-status`
- `pytest -q tests/test_kfm_delta_apply.py`
- `(cd apps/web && npm run -s check:package)`

(Results recorded from command output in terminal session.)

## 11) Rollback plan

Only one tracked file was added in this change set:

- `docs/registers/REPO_ORGANIZATION_AUDIT.md`

Rollback options:

1. Unstaged rollback: `git restore docs/registers/REPO_ORGANIZATION_AUDIT.md` (if tracked state permits).
2. Staged/new-file rollback: `git rm docs/registers/REPO_ORGANIZATION_AUDIT.md` prior to commit.
3. Post-commit rollback: `git revert <commit_sha>`.

