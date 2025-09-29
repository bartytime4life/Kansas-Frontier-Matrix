# Kansas-Frontier-Matrix — DEM-Derived Vectors

This folder contains **vector products derived from Digital Elevation Models (DEMs)**.  
These datasets are extracted or modeled from DEM rasters in `../` and `../overlays/` and stored as **GeoJSON** for interoperability.  

All vector layers must be:
- **Reproducible** from DEM inputs (no manual editing).  
- **Linked to provenance** in the STAC catalog (`data/stac/items/dem/*.json`).  
- **Schema-validated** against project JSON schemas (`web/config/layers.schema.json`).  

---

## Typical Contents

data/processed/dem/vectors/
├── ks_1m_dem_2018_contours_10m.json       # Elevation isolines
├── ks_1m_dem_2018_watersheds_huc12.json   # Watershed/basin polygons
├── ks_1m_dem_2018_stream_network.json     # Extracted stream centerlines
└── ks_1m_dem_2020_contours_5m.json        # Alternate interval contours

### Common vector types

- **Contours** → Elevation isolines at fixed intervals (e.g., 5 m, 10 m).  
- **Watersheds / Basins** → HUC-style polygons derived from flow accumulation.  
- **Stream networks** → Centerlines extracted from flow routing thresholds.  
- **Landform classes** → Slope classes, aspect zones, landform polygons.  

---

## Workflow

1. **Source DEM**  
   - Must exist as a **COG** in `data/processed/dem/`.  
   - Example: `ks_1m_dem_2018.tif`

2. **Generate vector layers** (examples):

   - **Contours (10m):**
     ```bash
     gdal_contour -a elev -i 10 \
       data/processed/dem/ks_1m_dem_2018.tif \
       /tmp/ks_1m_dem_2018_contours_10m.shp

     ogr2ogr -f GeoJSON -t_srs EPSG:4326 \
       data/processed/dem/vectors/ks_1m_dem_2018_contours_10m.json \
       /tmp/ks_1m_dem_2018_contours_10m.shp
     ```

   - **Watersheds (HUC12 equivalent):**  
     Derived using **TauDEM**, **WhiteboxTools**, or **GRASS GIS hydrology** toolchain:  
     - Flow direction  
     - Flow accumulation  
     - Stream/basin delineation  

   - **Stream networks:**  
     Extracted from flow accumulation thresholds:  
     ```bash
     # Example with WhiteboxTools
     wbt_breach_depressions --dem=ks_1m_dem_2018.tif --output=/tmp/filled.tif
     wbt_d8_flow_accumulation --dem=/tmp/filled.tif --out_type=catchment-area --output=/tmp/accum.tif
     wbt_extract_streams --flow_accum=/tmp/accum.tif --threshold=1000 --output=/tmp/streams.tif
     gdal_polygonize.py /tmp/streams.tif -f GeoJSON ks_1m_dem_2018_stream_network.json
     ```

3. **Reproject outputs** → Always to **EPSG:4326 (WGS84 lat/long)**.  

4. **Checksum**  
   ```bash
   scripts/gen_sha256.sh data/processed/dem/vectors/*.json

	5.	Update STAC
Add each vector as an asset in the parent DEM STAC item:

"contours_10m": {
  "href": "../../../processed/dem/vectors/ks_1m_dem_2018_contours_10m.json",
  "title": "DEM Contours 10m (2018)",
  "type": "application/geo+json",
  "roles": ["data"],
  "checksum:sha256": "<sha256sum>"
}



⸻

Integration
	•	STAC catalog → Ensures discoverability of contours, watersheds, and stream networks ￼.
	•	Web viewer → Layers referenced in web/data/dem_vectors.json and validated against web/config/layers.schema.json.
	•	KML exports → Important DEM vectors (e.g., contours) may also be exported to data/kml/ for Google Earth use.
	•	Experiments → Used in terrain analysis, archaeology modeling, hydrology studies, floodplain reconstructions ￼.
	•	Reproducibility → Outputs must always be regenerated via documented pipelines (Makefile targets or experiment notebooks).

⸻

Notes
	•	Canonical format = GeoJSON (*.json).
	•	For very large datasets, tile or convert to MBTiles / PMTiles for performance, but always keep a canonical GeoJSON here.
	•	Track large outputs with Git LFS or DVC.
	•	Document exact tools/parameters in the associated experiment log (experiments/<ID>_.../experiment.md).
	•	File naming convention: <dem_id>_<layer>_<parameters>.json
	•	Example: ks_1m_dem_2018_contours_10m.json

⸻

See Also
	•	../ → Base processed DEMs.
	•	../overlays/ → Raster derivatives (hillshade, slope, aspect).
	•	../../stac/items/dem/ → STAC items linking DEMs and vector derivatives.
	•	../../kml/ → KML/KMZ exports for Earth viewer use.
	•	experiments/ → MCP experiment logs & configs documenting workflows.

⸻

✅ This directory ensures DEM-derived vector products are clean, reproducible, STAC-linked, and ready for use in Kansas Frontier Matrix experiments and web mapping.

---