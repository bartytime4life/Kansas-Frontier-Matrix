# Reorg validation report

## CONFIRMED checks in this sprint

- Inventory regenerated from tracked files only (`git ls-files`).
- `tools/repo_inventory/check_public_path_boundaries.py` hardened to scan only executable code extensions and fail non-zero by default.
- Dependency clutter guard updated with explicit `apps/web/node_modules/` ignore rule.
- No lifecycle or machine-authority moves were performed.

## BLOCKED / CONFLICTED context

- High-volume move target (>=75 path impacts) was BLOCKED by unresolved authority boundaries and low-confidence safe move candidates.
- `contracts/` vs `schemas/` and `policy/` vs `policies/` remain CONFLICTED; no machine-authority file relocations were attempted.

## Validation command outcomes

- `python tools/repo_inventory/classify_paths.py --tsv-out docs/registers/reorg/path_inventory.tsv` -> PASS.
- `python tools/repo_inventory/check_reorg_manifest.py docs/registers/reorg` -> PASS.
- `python tools/repo_inventory/check_doc_orphans.py` -> PASS.
- `python tools/repo_inventory/check_public_path_boundaries.py --allow-fail` -> PASS (report mode).
- `pytest tests/repo_inventory -q` -> PASS.
