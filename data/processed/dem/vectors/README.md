<div align="center">

# 🏔️ Kansas-Frontier-Matrix — DEM Overlays  
`data/processed/dem/overlays/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../.pre-commit-config.yaml)  
[![Docs](https://img.shields.io/badge/docs-MCP%20Standards-blue.svg)](../../../docs/)  
[![Data Provenance](https://img.shields.io/badge/provenance-verified✅-green.svg)](../../../stac/items/dem/)

**Mission:** Store **DEM-derived overlays** generated from processed DEMs in `../`.  
Overlays emphasize terrain characteristics and enhance visualization.

They are reproducible from base DEMs and linked in:  
- **STAC catalog** → `stac/items/dem/*.json`  
- **Web configs** → `web/config/layers.json`  
- **KML exports** → `data/kml/` (Google Earth KMZ overlays)

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Processed DEMs\n(data/processed/dem/**)"] --> B["Generate overlays\n(gdaldem hillshade · slope · aspect)"]
  B --> C["Overlay rasters\n(data/processed/dem/overlays/**)"]
  C --> D["Checksums + meta\n(.sha256 · .meta.json)"]
  C --> E["STAC Item assets\n(stac/items/dem/**)"]
  E --> F["Validate\n(make stac-validate)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]
  F --> H["Earth exports\n(data/kml/**)"]

<!-- END OF MERMAID -->



⸻

📂 Typical Contents

data/processed/dem/overlays/
├── ks_1m_dem_2018_hillshade.tif
├── ks_1m_dem_2018_slope.tif
├── ks_1m_dem_2018_aspect.tif
├── ks_1m_dem_2020_hillshade.tif
├── ks_1m_dem_2020_slope.tif
└── ks_1m_dem_2020_aspect.tif

Core overlays
	•	Hillshade → shaded relief (azimuth + altitude)
	•	Slope → gradient (degrees or percent rise)
	•	Aspect → slope orientation (0–360°)

Optional overlays
	•	Curvature → concavity/convexity
	•	TRI / TPI → terrain ruggedness / topographic position index
	•	Roughness → local variability

⸻

🔧 Parameters (reference)

Overlay	Tool/Arg	Recommended Defaults	Notes
Hillshade	gdaldem hillshade	-az 315 -alt 45 -compute_edges	Adjust az/alt for lighting experiments.
Slope	gdaldem slope	-compute_edges	Add -p for percent rise if desired.
Aspect	gdaldem aspect	-compute_edges	0–360°, 0/360 = North.

All outputs should be COG (tiled, overviews). Use LZW or DEFLATE compression.

⸻

🔄 Workflow
	1.	Source DEM

	•	Must exist in data/processed/dem/ as a COG
	•	Example: ks_1m_dem_2018.tif

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

	4.	Store outputs → data/processed/dem/overlays/
	5.	Checksums

scripts/gen_sha256.sh data/processed/dem/overlays/*.tif

	6.	Update STAC items (parent DEM)
Example: stac/items/dem/ks_1m_dem_2018.json

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

📑 Example STAC Item (DEM Hillshade Overlay)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_1m_hillshade_2018",
  "properties": {
    "title": "Kansas Hillshade (2018, 1m DEM)",
    "description": "Hillshade overlay generated from 2018 Kansas 1m DEM mosaic.",
    "datetime": "2018-06-01T00:00:00Z",
    "proj:epsg": 4326,
    "kfm:method": "gdaldem hillshade (az=315, alt=45)",
    "kfm:lineage": ["data/processed/dem/ks_1m_dem_2018.tif"],
    "qa:status": "provisional"
  },
  "links": [
    { "rel": "collection", "href": "../../../../stac/collections/terrain.json" }
  ],
  "assets": {
    "cog": {
      "href": "../../../../data/processed/dem/overlays/ks_1m_dem_2018_hillshade.tif",
      "title": "Hillshade (2018 DEM, 1m)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster", "visual"]
    }
  }
}


⸻

🧪 Make Targets (suggested)

overlays: hillshade slope aspect stac-overlays

hillshade:
\tgdaldem hillshade $(DEM) $(OUT_HS) -compute_edges -az 315 -alt 45 -co COMPRESS=LZW
\trio cogeo create $(OUT_HS) $(OUT_HS) --web-optimized

slope:
\tgdaldem slope $(DEM) $(OUT_SLP) -compute_edges -co COMPRESS=LZW
\trio cogeo create $(OUT_SLP) $(OUT_SLP) --web-optimized

aspect:
\tgdaldem aspect $(DEM) $(OUT_ASP) -compute_edges -co COMPRESS=LZW
\trio cogeo create $(OUT_ASP) $(OUT_ASP) --web-optimized

stac-overlays:
\t# script to patch parent DEM STAC items with overlay assets + checksums


⸻

✅ QA Checklist
	•	Outputs are COG with internal overviews
	•	Checksums generated and stored (.sha256)
	•	STAC items updated (assets → roles:["visual"], correct href, checksum)
	•	web/config/layers.json entries added/updated
	•	KMZ exports (if required) created under data/kml/
	•	Large files tracked by Git LFS or DVC

⸻

🔗 Integration
	•	Web viewer → overlays referenced in web/config/layers.json (schema validated)
	•	Google Earth (KML/KMZ) → exported under data/kml/
	•	Experiments → archaeology, hydrology, floodplain mapping, erosion studies
	•	STAC → overlays attached as assets under parent DEM items

⸻

📝 Notes
	•	Naming → <dem_id>_<overlay>.tif (e.g., ks_1m_dem_2018_hillshade.tif)
	•	Compression → LZW or DEFLATE
	•	Reproducibility → regenerate overlays; never hand-edit rasters
	•	Consistency → overlays must be linked in STAC + web configs

⸻

📚 See Also
	•	../ → Base processed DEMs
	•	../vectors/ → Contours and terrain vectorizations
	•	data/kml/ → KMZ exports of hillshades & styled rasters
	•	stac/items/dem/ → STAC items for DEMs + overlays
	•	experiments/ → MCP logs + configs for DEM workflows

⸻


<div align="center">


✅ Mission Principle
DEM overlays must be optimized, reproducible, and traceable across STAC, web configs, Makefile workflows, and KML exports.

</div>
```
