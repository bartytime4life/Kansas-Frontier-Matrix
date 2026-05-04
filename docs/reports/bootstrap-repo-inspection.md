# Bootstrap Repo Inspection

## Truth posture
- **CONFIRMED**: Command outputs captured in this Codex session.
- **NEEDS VERIFICATION**: PDF corpus was not directly inspectable in mounted workspace.

## Commands run
1. `pwd`
2. `git status --short || true`
3. `git branch --show-current || true`
4. `git rev-parse --show-toplevel || true`
5. `find . -maxdepth 2 -type f | sort | head -200`
6. `find . -maxdepth 2 -type d | sort | head -200`
7. `find . -maxdepth 3 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name Makefile -o -name README.md \) -print`
8. `find . -maxdepth 4 -type f \( -path "*/docs/*" -o -path "*/schemas/*" -o -path "*/contracts/*" -o -path "*/policy/*" -o -path "*/tests/*" -o -path "*/apps/*" -o -path "*/packages/*" \) | sort | head -300`

## Results (abridged)
- `pwd` => `/workspace/Kansas-Frontier-Matrix`.
- Branch => `work`.
- Git toplevel => `/workspace/Kansas-Frontier-Matrix`.
- `git status --short` => clean working tree at inspection time.
- Repository is **existing**, not empty: governance/control-plane/docs/schemas/contracts/tests/apps/tools already present.

## Package manager / stack evidence
- Python stdlib-based validation and unittest baseline is present (`tools/*.py`, `tests/*.py`).
- `pyproject.toml` exists for lightweight project metadata.
- No internet-required baseline dependency was needed for validation in this run.

## Source PDF availability
- The requested KFM PDFs were **not directly inspected** in this mounted workspace during this session.
- Source-ledger entries should remain **NEEDS VERIFICATION** for those IDs until files are mounted and checked.

## Unknowns
- Whether the referenced PDFs exist outside currently mounted paths.
- Whether external source terms/rights constraints are complete for live connector activation.

## Adaptation taken
- Preserved existing repository structure and conventions.
- Verified baseline governance membrane and hydrology synthetic slice via local no-network validators/tests.
- Kept implementation posture evidence-first, map-first, time-aware, fail-closed, and release-auditable.

