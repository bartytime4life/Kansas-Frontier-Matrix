# Hydrology Source Verification Inspection (Prompt 3)

Truth posture: **CONFIRMED** for commands and local repository observations in this Codex session.

## Commands run
- `pwd`
- `git status --short || true`
- `git branch --show-current || true`
- `git rev-parse --show-toplevel || true`
- `find . -maxdepth 2 -type f | sort | head -200`
- `find . -maxdepth 2 -type d | sort | head -200`
- `find . -maxdepth 4 -type f \( -path "*/docs/*" -o -path "*/schemas/*" -o -path "*/contracts/*" -o -path "*/policy/*" -o -path "*/tests/*" -o -path "*/fixtures/*" -o -path "*/connectors/*" -o -path "*/pipelines/*" -o -path "*/data/registry/*" \) | sort | head -500`
- `find . -maxdepth 4 \( -name package.json -o -name pyproject.toml -o -name go.mod -o -name Cargo.toml -o -name Makefile -o -name README.md \) -print`

## Results
- Prompt 1 foundation present: **CONFIRMED**.
- Prompt 2 hydrology proof slice present: **CONFIRMED**.
- Package/stack evidence: Python stdlib validators/tests and `pyproject.toml` present.
- Source PDFs: **NEEDS VERIFICATION** in this run (not directly inspected).
- Network access used: **no** (**CONFIRMED**).

## Unknowns
- Whether all listed external PDFs are mounted and canonical in this runtime (**UNKNOWN**).

## Adaptation
- Preserved existing repository conventions.
- Added Prompt 3 source-verification gate artifacts without enabling live ingestion or publication.
