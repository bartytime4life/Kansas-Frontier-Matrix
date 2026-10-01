# Crop-CASMA 1 km tile preparation

This soil-domain pipeline consumes an unreleased `kfm.crop-casma-capture/v1` directory from `connectors/nass/crop_casma.py`. It verifies the preserved GeoTIFF digest, EPSG:5070 1,000 m numeric grid, no-data value, bounds, and volumetric-moisture range. It then uses nearest-neighbor reprojection to prepare EPSG:3857 PNG tiles at zooms 4–9. Every output pixel is colored from one original cell; no numerical interpolation or gap filling occurs. Its manifest records the source digest, day, unit, valid-cell count, min/max, tile hashes, and deterministic candidate ID.

This directory owns transformation under the existing `pipelines/domains/soil/` responsibility; source acquisition stays in `connectors/nass/`, and release decisions remain outside both. The output is always `UNRELEASED`. Run with a fresh external output directory and the isolated Python environment declared in `requirements-tiles.txt`:

```sh
python pipelines/domains/soil/crop_casma_tiles/prepare.py CAPTURE_DIR NEW_OUTPUT_DIR
python -m unittest discover -s pipelines/domains/soil/crop_casma_tiles -p 'test_*.py' -v
```

Rollback is deletion or archival of an unreleased output directory. Existing approved packages and active pointers are unaffected. The packaged map route verifies immutable manifest and tile hashes again before serving a separately approved package.
