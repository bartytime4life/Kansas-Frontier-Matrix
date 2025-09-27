# DEM Overlays — Kansas Frontier Matrix

This folder contains **derived overlays** generated from processed DEMs in `../`.  
These products provide visual and analytical enhancements such as **hillshade**, **slope**, and **aspect**.  
All overlays are reproducible, lightweight compared to the base DEM, and referenced in the STAC catalog
(`data/stac/items/dem/*.json`) and web configs (`web/config/layers.json`).

---

## Typical Contents

```

data/processed/dem/overlays/
ks_1m_dem_2018_hillshade.tif
ks_1m_dem_2018_slope.tif
ks_1m_dem_2018_aspect.tif
ks_1m_dem_2020_hillshade.tif
ks_1m_dem_2020_slope.tif

````

- **Hillshade** — Shaded relief (illumination simulation) for visualization.  
- **Slope** — Gradient in degrees or percent rise.  
- **Aspect** — Compass direction of slope.  
- Other overlays (curvature, TPI, TRI) may be added later.

---

## Workflow

1. **Source DEM**  
   - Must exist in `data/processed/dem/` as a COG.  

2. **Generate overlays** (via Makefile or GDAL):  
   - Hillshade:  
     ```bash
     gdaldem hillshade ks_1m_dem_2018.tif ks_1m_dem_2018_hillshade.tif -compute_edges -co COMPRESS=LZW
     ```
   - Slope:  
     ```bash
     gdaldem slope ks_1m_dem_2018.tif ks_1m_dem_2018_slope.tif -compute_edges -co COMPRESS=LZW
     ```
   - Aspect:  
     ```bash
     gdaldem aspect ks_1m_dem_2018.tif ks_1m_dem_2018_aspect.tif -compute_edges -co COMPRESS=LZW
     ```

3. **Convert to COG** (if not already):  
   ```bash
   rio cogeo create ks_1m_dem_2018_hillshade.tif ks_1m_dem_2018_hillshade.tif --web-optimized
````

4. **Store here** under `data/processed/dem/overlays/`.

5. **Checksum**:

   ```bash
   scripts/gen_sha256.sh data/processed/dem/overlays/*.tif
   ```

6. **STAC Update**:

   * Add `assets` entries to the corresponding DEM STAC Item (`data/stac/items/dem/ks_1m_dem_2018.json`)
   * Example:

     ```json
     "hillshade": {
       "href": "../../../processed/dem/overlays/ks_1m_dem_2018_hillshade.tif",
       "title": "DEM Hillshade Overlay (2018)",
       "type": "image/tiff; application=geotiff; profile=cloud-optimized",
       "roles": ["visual"],
       "checksum:sha256": "<sha256sum>"
     }
     ```

---

## Integration

* **Web Viewer**:
  Overlays are referenced in `web/config/layers.json` for dynamic toggle in MapLibre.
* **Experiments**:
  Used in terrain analysis, archaeological site modeling, and hydrological reconstruction.
* **Reproducibility**:
  Always regenerate overlays from DEMs — never edit them manually.

---

## Notes

* File naming convention: `<dem_id>_<overlay>.tif`
  e.g., `ks_1m_dem_2018_hillshade.tif`
* Keep outputs compressed (LZW/DEFLATE).
* Track with **Git LFS or DVC** if file size >5 MB.
* Always include overlays in STAC Items to maintain discoverability.

---

✅ This directory ensures DEM overlays are **optimized, versioned, and linked** to both the STAC catalog and the web map for consistent visualization and analysis.

```
