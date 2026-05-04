# PR-002 Repo Inspection

## Truth Posture
- **CONFIRMED**: Commands listed below were executed in this Codex run and outputs were used.
- **UNKNOWN**: Mounted PDF doctrine files were not found/inspectable in this run.

## Commands Run (Phase 0)
- `pwd`
- `git status --short || true`
- `git branch --show-current || true`
- `git rev-parse --show-toplevel || true`
- `find . -maxdepth 2 -type f | sort | head -200`
- `find . -maxdepth 2 -type d | sort | head -200`
- `find . -maxdepth 3 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name Makefile -o -name README.md \) -print`
- `find . -maxdepth 4 -type f \( -path "*/docs/*" -o -path "*/schemas/*" -o -path "*/contracts/*" -o -path "*/policy/*" -o -path "*/tests/*" -o -path "*/apps/*" -o -path "*/packages/*" -o -path "*/tools/*" -o -path "*/fixtures/*" -o -path "*/release/*" -o -path "*/data/*" \) | sort | head -500`

## Results Summary
- Current branch: `work`.
- Dirty state at start: clean.
- Stack evidence: Python project (`pyproject.toml`) with unittest-based tests and Python validation scripts.
- Existing baseline files discovered under docs/schemas/contracts/policy/tests/apps/packages/tools/fixtures/release.
- Files intentionally preserved: existing root structure and baseline governance artifacts.

## Source PDF Availability
- **UNKNOWN**: The listed doctrine PDFs were not directly inspectable from discovered repo paths in this run.

## Repo Conventions Discovered
- Validation tooling in `tools/*.py` and focused validators in `tools/validators/*.py`.
- Unit tests use `python -m unittest discover tests`.
- Synthetic fixtures under `fixtures/` and dry-run manifests under `release/dry_runs/`.

## Unknowns / Needs Verification
- **NEEDS VERIFICATION**: production deployment posture and runtime endpoints.
- **NEEDS VERIFICATION**: official live-source rights/terms and activation criteria for USGS/FEMA/NOAA/WBD/NHDPlus.

## Adaptation for PR-002
- Kept changes constrained to synthetic hydrology evidence-closure hardening.
- Added finite-outcome enforcement paths (ANSWER/ABSTAIN/DENY/ERROR) with no network connector activation.
