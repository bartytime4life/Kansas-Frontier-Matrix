<div align="center">

# 🏔️ Kansas-Frontier-Matrix — Terrain Derivatives  
`data/derivatives/terrain/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Derive **analysis-ready terrain layers** from DEMs and elevation sources —  
including **hillshade, slope, aspect, roughness, curvature, and terrain classes** —  
to support Kansas **geomorphology, hydrology, hazards, and historical analysis**.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["DEM inputs\n(data/cogs/dem/*)"] --> B["Terrain Derivation\n(make terrain)"]
  B --> C["Terrain Layers\n(data/derivatives/terrain)"]
  C --> D["STAC Items\n(stac/items/terrain_*)"]
  D --> E["Validate\n(stac-validate)"]
  C --> F["Tiles / PMTiles\n(web/tiles)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ terrain/
      ├─ hillshade/             # Hillshade rasters
      │  └─ hillshade_1m_state.tif
      ├─ slope/                 # Slope in degrees or %
      │  └─ slope_1m_state.tif
      ├─ aspect/                # Aspect (0–360°)
      │  └─ aspect_1m_state.tif
      ├─ roughness/             # Terrain ruggedness indices
      │  └─ roughness_1m_state.tif
      ├─ curvature/             # Profile & plan curvature
      │  └─ curvature_1m_state.tif
      ├─ classes/               # Terrain classification maps
      │  └─ slope_classes_1m_state.tif
      ├─ qc/                    # QA checks & reports
      │  └─ terrain_qc_report.md
      └─ README.md


⸻

✅ What Belongs Here
	•	DEM-derived products → hillshade, slope, aspect, curvature, roughness.
	•	Classified maps → slope classes, aspect sectors, terrain position index.
	•	Supporting rasters → QA masks, residuals, normalized terrain metrics.

🚫 Does Not Belong
	•	Raw DEMs (data/cogs/dem/).
	•	Change detection products (data/derivatives/change/).
	•	Hydrology-specific layers (flowdir/flowacc → data/derivatives/hydrology/).

⸻

🛠 Workflow & Make Targets

# Core terrain derivatives
make terrain-hillshade
make terrain-slope
make terrain-aspect
make terrain-roughness
make terrain-curvature

# Terrain classification
make terrain-slope-classes
make terrain-aspect-sectors

# Register & validate
make stac stac-validate

# Build tiles for web viewer
make tiles-terrain


⸻

📜 Naming & Metadata

Filename pattern

<metric>_<resolution>_<region>.tif

Examples:
	•	slope_1m_state.tif
	•	aspect_1m_state.tif
	•	hillshade_1m_state.tif
	•	slope_classes_1m_state.tif

STAC Item requirements
	•	properties.topic → slope, aspect, curvature, etc.
	•	proj:epsg → 4326 for published outputs
	•	kfm:method → algorithm/tool (GDAL, RichDEM, GRASS, WhiteboxTools)
	•	kfm:lineage → DEM sources + commit ref
	•	qa:status → draft, provisional, verified

⸻

🔬 QA & Uncertainty
	•	Hillshade → visually compare against known relief maps.
	•	Slope/Aspect → cross-check against USGS/NRCS slope class datasets.
	•	Curvature → validate using synthetic test DEMs.
	•	Classes → confirm bin thresholds (e.g., NRCS slope breaks).
	•	Document assumptions, processing parameters, and DEM vertical accuracy.

⸻

🚀 Publishing
	•	Rasters → publish as COG (with overviews + compression).
	•	Classes → color-relatable legends for web viewer (STAC assets:legend).
	•	Register as STAC Items in stac/items/terrain/.
	•	Validate in CI with stac-validate.yml.

⸻

📑 Example STAC Item (Slope, 1m statewide)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_slope_1m_state",
  "properties": {
    "title": "Kansas Slope (1m)",
    "description": "Slope (degrees) derived from statewide 1m LiDAR DEM mosaics.",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "GDAL DEM slope (degrees)",
    "kfm:lineage": [
      "data/cogs/dem/ks_1m_2018.tif",
      "data/cogs/dem/ks_1m_2020.tif"
    ],
    "processing:software": "GDAL 3.9.0 (Docker image ghcr.io/bartytime4life/kfm-gdal:3.9.0)",
    "qa:status": "provisional"
  },
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-102.05, 40.00],
      [-94.59, 40.00],
      [-94.59, 36.99],
      [-102.05, 36.99]
    ]]
  },
  "links": [
    {
      "rel": "collection",
      "href": "../../stac/collections/terrain.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../data/derivatives/terrain/slope/slope_1m_state.tif",
      "title": "Slope (1m, statewide)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    }
  }
}


⸻

👩‍💻 Contributor Notes
	•	Implement derivations in scripts/terrain/ (e.g., slope.py, aspect.py).
	•	Document methods in docs/methods/terrain.md.
	•	Always add .sha256 sidecars for provenance.
	•	Use EPSG:4326 for published outputs; retain native CRS for intermediate QA.
	•	When publishing classes, provide a color legend (JSON + PNG).