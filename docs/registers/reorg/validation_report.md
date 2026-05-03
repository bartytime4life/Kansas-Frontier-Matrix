# Validation Report (2026-05-03)

## Phase command evidence
- CONFIRMED: `pwd`, `git rev-parse --show-toplevel`, `git branch --show-current`, `git status --short`, `git diff --stat`, and `git ls-files | wc -l` executed.
- CONFIRMED: max-depth inventory commands for directories/files (excluding `.git*` and `apps/web/node_modules*`) executed.
- CONFIRMED: governing-file inspections executed for README/ignore/testing/package and policy/ADR/register/runbook homes.

## Reorg bundle checks
- CONFIRMED: `python tools/repo_inventory/classify_paths.py --output docs/registers/reorg/path_inventory.tsv`.
- CONFIRMED: `python tools/repo_inventory/check_reorg_manifest.py docs/registers/reorg` returned `OK: manifest bundle complete`.
- CONFIRMED: existing `check_doc_orphans.py` and `check_public_path_boundaries.py` tooling present.

## Safety and blocker summary
- BLOCKED: large-scale move subset for this run. Evidence: manifest already contains a large pre-planned move list spanning multiple authority-adjacent doc surfaces, but executing those moves in this run would require expansive reference rewrites across `docs/`, `.github/`, and domain runbooks and risks crossing unresolved authority lines without narrower lane-by-lane acceptance.
- CONFIRMED: lifecycle directories (`data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published`) were not moved.
- CONFIRMED: no machine schema moves between `contracts/` and `schemas`; no policy engine moves between `policy/` and `policies`.
