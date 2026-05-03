# Validation Report (follow-up)

- `python tools/repo_inventory/classify_paths.py --out docs/registers/reorg/path_inventory.tsv` => PASS (`7478` paths)
- `python tools/repo_inventory/check_reorg_manifest.py docs/registers/reorg` => PASS
- `python tools/repo_inventory/check_doc_orphans.py` => WARN (`orphan_count=10`, pre-existing families in `docs/catalog`, `docs/governance`, `docs/runtime`)
- `python tools/repo_inventory/check_public_path_boundaries.py` => WARN (doctrinal + test references detected by regex)
- `pytest tests/repo_inventory -q` => PASS (4 passed)
- bounded old-path search => PASS outside rollback and reorg manifest artifacts.
