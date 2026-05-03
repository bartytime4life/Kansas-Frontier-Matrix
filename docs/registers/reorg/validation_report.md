# Validation Report

## `python tools/repo_inventory/check_reorg_manifest.py docs/registers/reorg`
exit=1
```
move_plan missing columns

```
## `python tools/repo_inventory/check_doc_orphans.py`
exit=0
```
OK no doc orphans in docs/

```
## `python tools/repo_inventory/check_public_path_boundaries.py`
exit=1
```
BLOCKED direct raw/work/quarantine references detected:
apps/web/src/__tests__/tileReleasePublisher.test.js

```
## `pytest tests/repo_inventory -q`
exit=0
```
....                                                                     [100%]
4 passed in 0.23s

```
