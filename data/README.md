# data/ — sources, artifacts, and catalogs

**Sources live in `data/sources/*.json`** (small, human-edited).  
**Artifacts are written into `data/processed/**`** by the pipeline.  
**STAC entries are in `data/stac/**`** for time/space discoverability.

## Workflow

1. Add/modify a source descriptor in `data/sources/*.json`
2. `make fetch` → raw pulls (or streams) based on source descriptors
3. `make cogs`  → rasters become COGs in `processed/`
4. `make terrain` → hillshade/slope/aspect from DEMs
5. `make stac`  → refresh STAC collections/items under `stac/`
6. `make kml` / `make site` → Earth & web deliverables

Each artifact writes a `_meta.json` with the exact command, timestamp, inputs, and SHA256.

## Provenance & Uncertainty

- Source JSON includes: `license`, `provenance.attribution`, `retrieved`, CRS & bbox.
- Optional `confidence` (0–1) in source JSON propagates to UI (e.g., lower opacity).
- Vector features may include `properties.confidence` and `properties.year`.

See `data/sources/schema.source.json` for allowed fields.
