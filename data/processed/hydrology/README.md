# Hydrology — Kansas Frontier Matrix

This folder contains **processed hydrological datasets** derived from DEMs, USGS/NHD layers, FEMA flood maps, and Kansas GIS Hub sources.  
Outputs are stored in open formats (GeoJSON, CSV, Cloud-Optimized GeoTIFFs) and are **reproducible** from raw inputs in `data/raw/`.  
All datasets must be registered in the STAC catalog (`data/stac/items/hydrology/`) with metadata, checksums, and provenance.

---

## Structure

```

data/processed/hydrology/
kansas_river/                # Kansas River mainstem and watershed
watersheds/                  # Statewide or regional watershed polygons
floodplains/                 # Historic and modeled floodplain extents
stream_networks.json         # Generalized stream/river vector network
lakes_wetlands.json          # Major lakes and wetlands polygons

````

- **`kansas_river/`** → Kansas River–specific centerlines, watersheds, floodplains, gauges.  
- **`watersheds/`** → HUC-based watershed polygons (e.g., HUC8, HUC12).  
- **`floodplains/`** → FEMA flood maps, historic floodplain reconstructions.  
- **Other files** → statewide or general hydrology layers.

---

## File Conventions

- **Vectors**: GeoJSON (`*.json`, `*.geojson`)  
- **Rasters**: Cloud-Optimized GeoTIFFs (`*.tif`) for flood models, depth grids  
- **Tables**: CSV for gauges, time series, or metadata  
- **Projection**: EPSG:4326 (WGS84 lat/long) is required for all outputs

---

## Workflow

1. **Acquire raw sources** → `data/raw/` (USGS NHD, NOAA NWIS, FEMA, Kansas GIS Hub).  
2. **Process**  
   - Clean, reproject to EPSG:4326  
   - Simplify or dissolve geometries if needed  
   - Export to GeoJSON/COG/CSV
3. **Checksum**  
   ```bash
   scripts/gen_sha256.sh data/processed/hydrology/*
````

4. **Register in STAC**

   * Create/update Item JSON under `data/stac/items/hydrology/`
   * Link assets with `roles: ["data"]` and `checksum:sha256`
5. **Validate**

   ```bash
   pre-commit run stac-validate --all-files
   ```

---

## Integration

* **Web Viewer** — Hydrology layers appear in `web/config/layers.json` for MapLibre visualization.
* **Experiments** — Used for floodplain reconstructions, treaty overlays, archaeological site analysis, and erosion studies.
* **Knowledge Hub** — Hydrology data cross-links with treaties, settlements, geology, and environmental records.

---

## Notes

* Do **not** manually edit processed outputs — always regenerate from raw + scripts or notebooks.
* Use **stable filenames** (`<theme>_<year>.json`) so STAC + web configs remain valid.
* Track large files with **Git LFS or DVC**.
* Document provenance and methods in related `experiments/<ID>_.../experiment.md`.

---

✅ This folder ensures hydrology datasets are **consistent, reproducible, and discoverable** across the Kansas Frontier Matrix system.

```
