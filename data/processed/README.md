# Processed Data — Kansas Frontier Matrix

This folder contains **derived, cleaned, and ready-for-use geospatial and historical datasets**.  
All files here are outputs from ETL pipelines or experiment workflows, and are referenced in the STAC catalog (`data/stac/items/`).

---

## Principles

- **Immutable inputs, reproducible outputs**  
  Raw data lives under `data/raw/` or is fetched from authoritative sources.  
  All processed data here must be **reproducible** from scripts + configs.

- **STAC integration**  
  Every file in this folder should have a corresponding **STAC Item** (`data/stac/items/...json`) with metadata  
  (datetime, bbox, checksum, license, provenance).

- **Lightweight storage**  
  Large files (rasters, shapefiles) should be tracked with **Git LFS or DVC**.  
  This folder should only hold data necessary for experiments, web app layers, and reproducible analysis.

---

## Typical Contents

```

data/processed/
towns_points.json          # Settlement points (GeoJSON)
ks_treaties.json           # Treaty polygons
ks_railroads.json          # Historic railroad lines
hydrology.json             # Rivers and waterbodies
landcover_timeslices.json  # Land cover snapshots
...

````

- **Vector datasets** → GeoJSON (`*.json`, `*.geojson`)  
- **Tabular data** → CSV (`*.csv`) or Parquet (`*.parquet`)  
- **Derived rasters** (if small) → GeoTIFF/COG (`*.tif`)  
- **Schema** should match corresponding `web/config/layers.schema.json` entries.

---

## Workflow

1. **Fetch raw data** → `data/raw/`
2. **Transform / clean** with `scripts/` or notebooks (`experiments/*/notebooks/`)
3. **Save outputs** here in open formats (GeoJSON, CSV, COG)
4. **Generate checksum**:
   ```bash
   scripts/gen_sha256.sh data/processed/<file>
````

5. **Update STAC Item** (`data/stac/items/...json`) to reference the processed file
6. **Validate**:

   ```bash
   pre-commit run --all-files
   ```

---

## Example Entry (Vector GeoJSON)

* File: `data/processed/ks_treaties.json`
* STAC Item: `data/stac/items/vectors/ks_treaties.json`
* Linked Layer: `web/data/treaties.json`

---

## Notes

* **Do not manually edit processed files.** Always regenerate from raw + scripts.
* **Always document provenance** in the experiment or ETL config that produced the file.
* **Keep filenames stable** so that web configs, STAC, and experiments remain valid.

---

✅ This directory ensures Kansas Frontier Matrix datasets are **consistent, versioned, and reproducible** across experiments, STAC catalog, and web app layers.

```
