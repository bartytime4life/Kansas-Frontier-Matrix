# Kansas River Hydrology — Kansas Frontier Matrix

This folder contains **processed hydrological datasets** for the Kansas River and its watershed.  
All data here are derived from authoritative sources (e.g., USGS NHD, FEMA, KGS) and/or DEM-derived analyses.  
Outputs are stored in open formats (GeoJSON, CSV, COG) and referenced in the STAC catalog (`data/stac/items/`) and web configs.

---

## Typical Contents

```

data/processed/hydrology/kansas_river/
kansas_river_centerline.json
kansas_river_watershed.json
kansas_river_floodplain_1890s.json
kansas_river_gauges.csv

````

- **Centerline** — generalized vector line of the Kansas River mainstem.  
- **Watershed** — polygon boundary of the Kansas River drainage area.  
- **Historic floodplains** — polygons reconstructed from maps, surveys, or DEM analysis (e.g., 1890s floodplain).  
- **Gauges & stations** — CSV or GeoJSON with USGS/NOAA gauge locations, IDs, metadata.  

---

## Workflow

1. **Raw sources**  
   - Download from USGS NHDPlus, NOAA NWIS, FEMA floodplain maps, or Kansas GIS Hub → `data/raw/`.  
   - Historical reconstructions come from topo maps or experiments (`experiments/<ID>_...`).

2. **Process & convert**  
   - Reproject to EPSG:4326 (WGS84).  
   - Clean topology (snap/merge, dissolve multi-geometries).  
   - Export to **GeoJSON** for vectors or **CSV** for tabular (gauges).

3. **Checksums**  
   ```bash
   scripts/gen_sha256.sh data/processed/hydrology/kansas_river/*
````

4. **STAC registration**

   * Add each dataset as an **Item** under `data/stac/items/hydrology/`.
   * Example (asset reference in STAC Item):

     ```json
     "kansas_river_centerline": {
       "href": "../../../processed/hydrology/kansas_river/kansas_river_centerline.json",
       "title": "Kansas River Centerline",
       "type": "application/geo+json",
       "roles": ["data"],
       "checksum:sha256": "<sha256sum>"
     }
     ```

---

## Integration

* **Web Viewer** — Linked into `web/config/layers.json` for toggling Kansas River hydrology layers.
* **Experiments** — Used in floodplain reconstruction, treaty boundary overlays, erosion studies, and archaeology context.
* **Knowledge Hub** — Cross-linked with treaties, settlements, and environmental datasets in the Knowledge Graph.

---

## Notes

* Always regenerate from raw authoritative or reproducible experiment outputs — never edit GeoJSON/CSV manually.
* Use stable filenames (`kansas_river_<layer>.json`) for consistent STAC + web references.
* Track large files with **Git LFS or DVC**.
* Document provenance and processing steps in the related `experiments/<ID>_.../experiment.md`.

---

✅ This folder ensures Kansas River hydrology datasets are **clean, versioned, and reproducible**, supporting both geospatial visualization and scientific analysis.

```
