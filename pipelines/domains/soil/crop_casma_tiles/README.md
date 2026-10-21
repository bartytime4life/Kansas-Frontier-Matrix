# Crop-CASMA 1 km tile preparation

This soil-domain pipeline consumes an unreleased `kfm.crop-casma-capture/v1` directory from `connectors/nass/crop_casma.py`. It verifies the preserved GeoTIFF digest, EPSG:5070 1,000 m numeric grid, no-data value, bounds, and volumetric-moisture range. It then uses nearest-neighbor reprojection to prepare EPSG:3857 PNG tiles at zooms 4–9. Every output pixel is colored from one original cell; no numerical interpolation or gap filling occurs. Its manifest records the source digest, day, unit, valid-cell count, min/max, tile hashes, and deterministic candidate ID.

This directory owns transformation under the existing `pipelines/domains/soil/` responsibility; source acquisition stays in `connectors/nass/`, and release decisions remain outside both. The output is always `UNRELEASED`. Run with a fresh external output directory and Python 3.12 or newer in an isolated environment declared in `requirements-tiles.txt`. The stack pins Pillow 13.0.0, which includes the fixes for the nine Pillow dependency alerts affecting the previous pin. The Crop CASMA Tile Compatibility workflow installs this stack on Python 3.12 and runs the existing synthetic tile and tamper-rejection tests.

Candidate identity serializes integral floating statistics and checkpoints as JSON integers before hashing, matching the Site verifier's JavaScript number representation (for example, `0.0` hashes as `0`). The saved manifest keeps the original numeric values; this only fixes deterministic identity.

```sh
python -m pip install -r pipelines/domains/soil/crop_casma_tiles/requirements-tiles.txt
python -m pip check
python pipelines/domains/soil/crop_casma_tiles/prepare.py CAPTURE_DIR NEW_OUTPUT_DIR
python -m unittest discover -s pipelines/domains/soil/crop_casma_tiles -p 'test_*.py' -v
```

Rollback is deletion or archival of an unreleased output directory. Existing approved packages and active pointers are unaffected. The packaged map route verifies immutable manifest and tile hashes again before serving a separately approved package.
