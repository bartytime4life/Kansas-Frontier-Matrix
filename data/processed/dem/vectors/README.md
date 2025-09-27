# DEM-Derived Vectors — Kansas Frontier Matrix

This folder contains **vector products derived from Digital Elevation Models (DEMs)**.  
These datasets are extracted or modeled from DEM rasters in `../` and `../overlays/` and saved as **GeoJSON** for interoperability.  
All vectors must be reproducible, linked to provenance in the STAC catalog (`data/stac/items/dem/*.json`), and validated against the project’s JSON Schemas.

---

## Typical Contents

```

data/processed/dem/vectors/
ks_1m_dem_2018_contours_10m.json
ks_1m_dem_2018_watersheds_huc12.json
ks_1m_dem_2018_stream_network.json

````

- **Contours** — Elevation isolines at fixed intervals (e.g., 10 m).  
- **Watersheds / Basins** — HUC polygons derived from flow accumulation.  
- **Stream Networks** — River/stream centerlines extracted from flow routing.  
- **Other possible layers** — slope classes, aspect zones, landform polygons.

---

## Workflow

1. **Source DEM**  
   - Must exist as a processed COG in `data/processed/dem/`.

2. **Generate vector layers** (examples):
   - **Contours (10m):**  
     ```bash
     gdal_contour -a elev -i 10 ks_1m_dem_2018.tif ks_1m_dem_2018_contours_10m.shp
     ogr2ogr -f GeoJSON -t_srs EPSG:4326 ks_1m_dem_2018_contours_10m.json ks_1m_dem_2018_contours_10m.shp
     ```
   - **Watersheds (HUC12):**  
     Derived with TauDEM, WhiteboxTools, or GRASS GIS hydrology tools.
   - **Stream networks:**  
     Extracted from flow accumulation thresholds.

3. **Place outputs here** as GeoJSON.  
   - Always reproject to EPSG:4326 (WGS84 lat/long).  
   - Use stable, descriptive filenames.

4. **Checksum**  
   ```bash
   scripts/gen_sha256.sh data/processed/dem/vectors/*.json
````

5. **STAC Update**

   * Add each file as an `asset` in the corresponding DEM Item (`data/stac/items/dem/<id>.json`).
   * Example:

     ```json
     "contours_10m": {
       "href": "../../../processed/dem/vectors/ks_1m_dem_2018_contours_10m.json",
       "title": "DEM Contours 10m (2018)",
       "type": "application/geo+json",
       "roles": ["data"],
       "checksum:sha256": "<sha256sum>"
     }
     ```

---

## Integration

* **Web Viewer** — Added to `web/config/layers.json` for optional visualization.
* **Experiments** — Used in hydrology analysis, slope/erosion studies, and archaeology site modeling.
* **Reproducibility** — Never edit vectors manually. Always regenerate from DEMs using documented scripts.

---

## Notes

* Use **GeoJSON** (`*.json`) as the canonical format.
* For very large layers, consider tiling or converting to **MBTiles/PMTiles** (but always keep a GeoJSON copy here).
* Track large outputs with **Git LFS or DVC**.
* Document methods and parameters in the associated experiment (`experiments/<ID>_.../experiment.md`).

---

✅ This directory ensures DEM-derived vector products are **clean, reproducible, and discoverable** via STAC and the Kansas Frontier Matrix web map.

```
Want me to also **generate a starter STAC Item JSON** (e.g., `ks_1m_dem_2018_contours_10m.json` under `data/stac/items/dem/`) that links back to this folder, so you’ve got a working pattern to register vector derivatives right away?
```
