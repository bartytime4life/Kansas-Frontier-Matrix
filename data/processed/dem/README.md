# Processed DEMs — Kansas Frontier Matrix

This folder contains **Digital Elevation Model (DEM) derivatives** that have been processed from raw sources
(e.g., USGS 1m DEMs, LiDAR tiles, statewide mosaics).  
All outputs here are reproducible from raw inputs (`data/raw/`) and are referenced in the STAC catalog
(`data/stac/items/dem/*.json`).

---

## Typical Contents

```

data/processed/dem/
ks_1m_dem_2018.tif       # 1m DEM (2018 statewide mosaic, COG)
ks_1m_dem_2020.tif       # 1m DEM (2020 update, COG)
ks_1m_dem_2018_hillshade.tif
ks_1m_dem_2018_slope.tif
ks_1m_dem_2018_aspect.tif

````

- **DEM rasters** are stored as **Cloud-Optimized GeoTIFFs (COG)** for fast tiling.  
- **Derivatives** include slope, aspect, and hillshade layers, created via GDAL/rio/Makefile recipes.

---

## Workflow

1. **Fetch raw DEM** from USGS/Kansas GIS Hub → `data/raw/`
2. **Mosaic / reproject** into EPSG:4326 (WGS84 lat/long) if needed
3. **Convert to COG** with overviews:
   ```bash
   rio cogeo create input.tif output.tif --overview-level=5 --web-optimized
````

4. **Generate derivatives**:

   ```bash
   make terrain   # produces slope, aspect, hillshade
   ```
5. **Place outputs** here in `data/processed/dem/`
6. **Compute checksum**:

   ```bash
   scripts/gen_sha256.sh data/processed/dem/*.tif
   ```
7. **Update STAC Item** in `data/stac/items/dem/`
8. **Validate** with:

   ```bash
   pre-commit run stac-validate --all-files
   ```

---

## Integration

* **STAC** → Each DEM and derivative has an Item JSON under `data/stac/items/dem/`
* **Web layers** → Referenced in `web/layers.json` or `web/config/layers.schema.json`
* **Experiments** → Used in terrain analysis, hydrology modeling, floodplain reconstructions, archaeology overlays

---

## Notes

* Store DEMs in **COG format only** — no raw `.tif` tiles here.
* Use **stable filenames** (`ks_1m_dem_<year>.tif`) to keep STAC and web configs valid.
* Track large files with **Git LFS or DVC**.
* Always link back to provenance (USGS metadata, KGS surveys) in the STAC Item.

---

✅ This folder ensures all Kansas DEM data are **processed, optimized, and discoverable** for both research and web visualization.

```
