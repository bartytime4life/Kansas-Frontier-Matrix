# Crop-CASMA 1 km tile preparation

This soil-domain pipeline consumes an unreleased `kfm.crop-casma-capture/v1` directory from `connectors/nass/crop_casma.py`. It verifies the preserved GeoTIFF digest, EPSG:5070 1,000 m numeric grid, no-data value, bounds, and volumetric-moisture range. It then uses nearest-neighbor reprojection to prepare EPSG:3857 PNG tiles at zooms 4–9. Every output pixel is colored from one original cell; no numerical interpolation or gap filling occurs. Its manifest records the source digest, day, unit, valid-cell count, min/max, tile hashes, and deterministic candidate ID.

This directory owns transformation under the existing `pipelines/domains/soil/` responsibility; source acquisition stays in `connectors/nass/`, and release decisions remain outside both. The output is always `UNRELEASED`. Run with a fresh external output directory and Python 3.12 or newer in an isolated environment declared in `requirements-tiles.txt` and installed from its hash-locked `requirements-tiles.lock` (regenerate with the command in the lock header after changing a pin). The stack pins Pillow 13.0.0 in both files; installed-version and alert-state verification remain separate checks. The Crop CASMA Tile Compatibility workflow installs this stack on Python 3.12 and runs the existing synthetic tile and tamper-rejection tests.

The separate `dependency-scan / pip-audit-crop-casma` job audits the entire existing tile lock on Python 3.12 using the hash-locked audit tool. Findings and scanner errors fail the job; the audit does not install the tile stack or acquire source data. This advisory check complements the synthetic compatibility workflow. A passing audit does not establish that GitHub has closed its alerts or that any deployed environment uses this lock.

Candidate identity serializes integral floating statistics and checkpoints as JSON integers before hashing, matching the Site verifier's JavaScript number representation (for example, `0.0` hashes as `0`). The saved manifest keeps the original numeric values; this only fixes deterministic identity.

```sh
python -m pip install --require-hashes -r pipelines/domains/soil/crop_casma_tiles/requirements-tiles.lock
python -m pip check
python pipelines/domains/soil/crop_casma_tiles/prepare.py CAPTURE_DIR NEW_OUTPUT_DIR
python -m unittest discover -s pipelines/domains/soil/crop_casma_tiles -p 'test_*.py' -v
```

Rollback is deletion or archival of an unreleased output directory. Existing approved packages and active pointers are unaffected. The packaged map route verifies immutable manifest and tile hashes again before serving a separately approved package.
