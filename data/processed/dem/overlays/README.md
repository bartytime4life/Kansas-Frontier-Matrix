<div align="center">

# 🏔️ Kansas Geo Timeline — DEM Overlays

This folder contains **DEM-derived overlays** generated from processed DEMs in `../`.  
Overlays emphasize terrain characteristics and enhance visualization.  

They are reproducible from base DEMs and linked in:  
- **STAC catalog** → `data/stac/items/dem/*.json`  
- **Web configs** → `web/config/layers.json`  
- **KML exports** → `data/kml/` (Google Earth KMZ overlays)  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

```mermaid
flowchart TD
  A["Processed DEMs\n(data/processed/dem/**)"] --> B["Generate overlays\n(gdaldem hillshade · slope · aspect)"]
  B --> C["Overlay rasters\n(data/processed/dem/overlays/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Item assets\n(data/stac/items/dem/**)"]
  E --> F["Validate\n(stac-validate)"]
  F --> G["Viewer integration\n(web/data/dem_layers.json)"]
  F --> H["Earth exports\n(data/kml/**)"]

<!-- END OF MERMAID -->



⸻

📂 Typical contents

data/processed/dem/overlays/
├── ks_1m_dem_2018_hillshade.tif
├── ks_1m_dem_2018_slope.tif
├── ks_1m_dem_2018_aspect.tif
├── ks_1m_dem_2020_hillshade.tif
├── ks_1m_dem_2020_slope.tif
└── ks_1m_dem_2020_aspect.tif

Core overlays
	•	Hillshade → shaded relief (azimuth + altitude).
	•	Slope → gradient (degrees or percent rise).
	•	Aspect → slope orientation (0–360°).

Optional overlays
	•	Curvature → concavity/convexity.
	•	TRI / TPI → terrain ruggedness / topographic position index.
	•	Roughness → local variability.

⸻

🔄 Workflow
	1.	Source DEM
	•	Must exist in data/processed/dem/ as a COG.
	•	Example: ks_1m_dem_2018.tif.
	2.	Generate overlays

# Hillshade
gdaldem hillshade ks_1m_dem_2018.tif ks_1m_dem_2018_hillshade.tif \
  -compute_edges -az 315 -alt 45 -co COMPRESS=LZW

# Slope
gdaldem slope ks_1m_dem_2018.tif ks_1m_dem_2018_slope.tif \
  -compute_edges -co COMPRESS=LZW

# Aspect
gdaldem aspect ks_1m_dem_2018.tif ks_1m_dem_2018_aspect.tif \
  -compute_edges -co COMPRESS=LZW


	3.	Convert to COG

rio cogeo create ks_1m_dem_2018_hillshade.tif \
  ks_1m_dem_2018_hillshade.tif --web-optimized


	4.	Store outputs in data/processed/dem/overlays/.
	5.	Compute checksums

scripts/gen_sha256.sh data/processed/dem/overlays/*.tif


	6.	Update STAC items for parent DEMs (data/stac/items/dem/ks_1m_dem_2018.json):

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

🔗 Integration
	•	Web viewer → referenced in web/data/dem_layers.json, validated against layers.schema.json.
	•	Google Earth (KML/KMZ) → overlays exported under data/kml/.
	•	Experiments → used in archaeological models, hydrology analysis, floodplain mapping, erosion studies.
	•	STAC → attached as assets under parent DEM Items.

⸻

📝 Notes
	•	Naming convention → <dem_id>_<overlay>.tif
	•	Example: ks_1m_dem_2018_hillshade.tif
	•	Compression → LZW or DEFLATE for size efficiency.
	•	Storage → large files tracked with Git LFS or DVC.
	•	Reproducibility → regenerate overlays from DEMs; never hand-edit.
	•	Consistency → overlays must be linked in STAC and web configs.

⸻

📚 See also
	•	../ → Base processed DEMs.
	•	../vectors/ → Contours and terrain vectorizations.
	•	data/kml/ → KMZ exports of hillshades and styled rasters.
	•	data/stac/items/dem/ → STAC items for DEMs + overlays.
	•	experiments/ → MCP logs + configs for DEM workflows.

⸻

✅ Mission-grade principle: DEM overlays must be optimized, reproducible, and traceable across STAC, web configs, Makefile workflows, and Earth/KML exports.

