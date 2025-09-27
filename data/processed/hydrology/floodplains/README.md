# Floodplains — Kansas Frontier Matrix

This folder contains **processed floodplain datasets** for Kansas.  
It includes both **authoritative FEMA maps** and **historic floodplain reconstructions** derived from DEMs, hydrological models, and archival sources (e.g., 1890s maps).  
All datasets here are reproducible, linked to provenance, and referenced in the STAC catalog (`data/stac/items/hydrology/floodplains/`).

---

## Typical Contents

```

data/processed/hydrology/floodplains/
fema_floodplain_2020.json
fema_floodplain_2022.json
kansas_river_floodplain_1890s.json
statewide_flood_zones.json

````

- **FEMA Floodplain Layers** — official datasets by year/version (FIRM, NFHL).  
- **Historic Reconstructions** — polygons digitized from historic maps (e.g., 1890s Kansas River floodplain).  
- **Modeled Layers** — flood depth or extent grids from DEM hydrology simulations.

---

## Workflow

1. **Raw sources**  
   - FEMA NFHL/FIRM data (shapefiles, GDBs) from FEMA Map Service Center.  
   - Historical maps scanned from USGS/Kansas archives (`data/raw/`).  
   - DEM-based hydrology runs (TauDEM, WhiteboxTools, GRASS).

2. **Process & Convert**  
   - Reproject to EPSG:4326 (WGS84).  
   - Clean/dissolve polygons as needed.  
   - Export to **GeoJSON** (`*.json`) for vectors, or **COG** (`*.tif`) for rasters.

3. **Checksum**  
   ```bash
   scripts/gen_sha256.sh data/processed/hydrology/floodplains/*
````

4. **Register in STAC**

   * Create Item JSON under `data/stac/items/hydrology/floodplains/`.
   * Example asset reference:

     ```json
     "fema_floodplain_2020": {
       "href": "../../../processed/hydrology/floodplains/fema_floodplain_2020.json",
       "title": "FEMA Floodplain (2020)",
       "type": "application/geo+json",
       "roles": ["data"],
       "checksum:sha256": "<sha256sum>"
     }
     ```

---

## Integration

* **Web Viewer** — Layers toggle-able in `web/config/layers.json`.
* **Experiments** — Used in flood risk analysis, treaty boundary overlays, settlement vulnerability studies.
* **Knowledge Hub** — Links to Kansas River hydrology, climate, and historical event datasets.

---

## Notes

* **Naming convention**: `<source>_<theme>_<year>.json`
  Example: `fema_floodplain_2020.json`, `kansas_river_floodplain_1890s.json`.
* **Provenance required**: Document sources (FEMA, USGS, archives) in `experiment.md` or STAC metadata.
* **Large rasters**: Use COG format, track with **Git LFS/DVC**.
* **Never edit by hand**: regenerate from raw or experiment scripts.

---

✅ This folder ensures Kansas floodplain datasets are **traceable, reproducible, and interoperable** across experiments, STAC, and the web map.

```
