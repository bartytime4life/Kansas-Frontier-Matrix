# PR-008 Repo Inspection

## Commands run
- `pwd`
- `git status --short || true`
- `git branch --show-current || true`
- `git rev-parse --show-toplevel || true`
- `find . -maxdepth 2 -type f | sort | head -200`
- `find . -maxdepth 2 -type d | sort | head -200`
- `find . -maxdepth 3 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name Makefile -o -name README.md \) -print`
- `find . -maxdepth 4 -type f \( -path "*/docs/*" -o -path "*/schemas/*" -o -path "*/contracts/*" -o -path "*/policy/*" -o -path "*/policies/*" -o -path "*/tests/*" -o -path "*/apps/*" -o -path "*/packages/*" -o -path "*/tools/*" -o -path "*/fixtures/*" -o -path "*/release/*" -o -path "*/data/*" -o -path "*/connectors/*" -o -path "*/control_plane/*" \) | sort | head -500`

## Results
- Branch: `work` (CONFIRMED)
- Repo root: `/workspace/Kansas-Frontier-Matrix` (CONFIRMED)
- Dirty state before edits: clean (CONFIRMED)
- PR-001..PR-007 baseline files: present in docs/adr + docs/domains/hydrology and fixtures (CONFIRMED)
- Existing hydrology EvidenceBundle, claim, release candidate fixtures: present (CONFIRMED)
- Existing review/release/rollback: partial pre-PR-008 baseline present (CONFIRMED)
- Existing public API/mock UI/Evidence Drawer/Focus fixtures: present (CONFIRMED)
- Existing validators/tests: present under tools/validators and tests (CONFIRMED)
- Stack: Python (pyproject.toml, unittest, tool scripts) (CONFIRMED)
- Compatibility roots found: apps/web and apps/api (CONFIRMED)
- Source PDFs: not directly inspectable in this run (UNKNOWN)
- Files preserved intentionally: all existing PR-001..PR-007 assets (CONFIRMED)

## Adaptation
PR-008 implemented as synthetic fixture + validator + tests drill under responsibility roots with no network, no connectors enabled, and no real-source data access (CONFIRMED).
