# Kansas-Frontier-Matrix — DEM Overlays

This folder contains **derived overlays** generated from processed DEMs in `../`.  
Overlays are lighter-weight derivatives that emphasize terrain characteristics and improve visualization.  
They are reproducible from base DEMs and are referenced in:

- **STAC catalog** → `data/stac/items/dem/*.json`  
- **Web configs** → `web/config/layers.json`  
- **KML exports** → `data/kml/` (Google Earth KMZ overlays)

---

## Typical Contents

data/processed/dem/overlays/
├── ks_1m_dem_2018_hillshade.tif
├── ks_1m_dem_2018_slope.tif
├── ks_1m_dem_2018_aspect.tif
├── ks_1m_dem_2020_hillshade.tif
├── ks_1m_dem_2020_slope.tif
└── ks_1m_dem_2020_aspect.tif

### Core overlay types
- **Hillshade** → Simulated shaded relief (illumination from azimuth/elevation).  
- **Slope** → Gradient of terrain in degrees or percent rise.  
- **Aspect** → Compass orientation of slope (0–360°).  

### Optional / advanced overlays
- **Curvature** → Slope concavity/convexity.  
- **TRI / TPI** → Terrain Ruggedness / Topographic Position Index.  
- **Roughness** → Local terrain variability.  

---

## Workflow

1. **Source DEM**  
   - Must exist in `data/processed/dem/` as a **COG**.  
   - Example: `ks_1m_dem_2018.tif`

2. **Generate overlays** (via Makefile or GDAL):  

   - Hillshade:  
     ```bash
     gdaldem hillshade ks_1m_dem_2018.tif ks_1m_dem_2018_hillshade.tif \
       -compute_edges -az 315 -alt 45 -co COMPRESS=LZW
     ```

   - Slope:  
     ```bash
     gdaldem slope ks_1m_dem_2018.tif ks_1m_dem_2018_slope.tif \
       -compute_edges -co COMPRESS=LZW
     ```

   - Aspect:  
     ```bash
     gdaldem aspect ks_1m_dem_2018.tif ks_1m_dem_2018_aspect.tif \
       -compute_edges -co COMPRESS=LZW
     ```

3. **Convert to COG** (if not written directly as one):  
   ```bash
   rio cogeo create ks_1m_dem_2018_hillshade.tif \
     ks_1m_dem_2018_hillshade.tif --web-optimized

	4.	Store outputs here (data/processed/dem/overlays/).
	5.	Generate checksums for provenance:

scripts/gen_sha256.sh data/processed/dem/overlays/*.tif


	6.	Update STAC Item for the parent DEM (data/stac/items/dem/ks_1m_dem_2018.json):

"assets": {
  "dem": {
    "href": "../../../processed/dem/ks_1m_dem_2018.tif",
    "roles": ["data"]
  },
  "hillshade": {
    "href": "../../../processed/dem/overlays/ks_1m_dem_2018_hillshade.tif",
    "title": "DEM Hillshade Overlay (2018)",
    "type": "image/tiff; application=geotiff; profile=cloud-optimized",
    "roles": ["visual"],
    "checksum:sha256": "<sha256sum>"
  }
}



⸻

Integration
	•	Web Viewer → Overlays referenced in web/data/dem_layers.json and validated against web/config/layers.schema.json.
	•	Google Earth (KML/KMZ) → Exported from overlays into data/kml/ for use in Earth desktop and web ￼.
	•	Experiments → Inputs for archaeological site modeling, hydrology analysis, floodplain mapping, and erosion studies ￼.
	•	STAC → All overlays attached to parent DEM Items for discoverability and reproducibility ￼.

⸻

Notes
	•	Naming convention → <dem_id>_<overlay>.tif
	•	Example: ks_1m_dem_2018_hillshade.tif
	•	Compression → Use LZW or DEFLATE for smaller file sizes.
	•	Storage → Track with Git LFS or DVC for large files.
	•	MCP reproducibility → Never hand-edit overlays; regenerate from DEMs with documented parameters.
	•	Consistency → Overlays must always be linked in STAC and web configs.

⸻

See Also
	•	../ → Base processed DEMs.
	•	../vectors/ → Contours and terrain vectorizations.
	•	data/kml/ → Google Earth–ready KMZ exports of hillshade and other styled rasters.
	•	data/stac/items/dem/ → STAC Items documenting DEMs and overlays.
	•	experiments/ → MCP logs and configs for DEM processing.

⸻

✅ This directory ensures DEM overlays are optimized, reproducible, and linked across STAC, Makefile workflows, web maps, and Earth/KML exports.

---