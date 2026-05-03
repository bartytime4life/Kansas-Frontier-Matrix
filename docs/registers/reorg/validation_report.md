# Validation Report

- `python tools/repo_inventory/classify_paths.py --out docs/registers/reorg/path_inventory.tsv` => PASS
- `python tools/repo_inventory/check_reorg_manifest.py docs/registers/reorg` => PASS
- `python tools/repo_inventory/check_doc_orphans.py` => WARN (10 known orphan docs)
- `python tools/repo_inventory/check_public_path_boundaries.py` => WARN (doctrinal references detected)
- `pytest tests/repo_inventory -q` => PASS (4 passed)
