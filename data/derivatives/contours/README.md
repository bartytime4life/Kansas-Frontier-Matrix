<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Contour Derivatives  
`data/derivatives/contours/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Generate and store **vector contour lines** derived from DEMs and terrain rasters,  
making Kansas elevation and topographic gradients **discoverable, reproducible, and STAC-compliant**.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["DEM sources\n(data/cogs/dem/*)"] --> B["Contour generation\nmake contours"]
  B --> C["Contours (GeoJSON/GeoPackage)\n(data/derivatives/contours)"]
  C --> D["Tiles / PMTiles\n(web/tiles)"]
  C --> E["STAC Items\n(stac/items)"]
  E --> F["Validate\n(stac-validate)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ contours/
      ├─ 10m/                   # 10-meter interval contours
      │  └─ contours_10m_state.geojson
      ├─ 50m/                   # 50-meter interval contours
      │  └─ contours_50m_state.geojson
      ├─ index/                 # PMTiles / MBTiles indexes for web
      │  └─ ks_contours_10m.pmtiles
      ├─ qc/                    # QA reports, masks, stats
      │  └─ contour_density.png
      └─ README.md


⸻

✅ What Belongs Here
	•	Contour derivatives generated from DEMs (e.g., 10m, 25ft, 50m intervals).
	•	Vectorized formats: GeoJSON, GeoPackage, or PMTiles for web.
	•	Optional hillshade/overlay tiles for QA.

🚫 Does Not Belong
	•	Raw DEMs or rasters (data/cogs/dem/).
	•	Temporary tiles (data/tiles/ → ephemeral only).

⸻

🛠 Workflow & Make Targets

# Generate 10m contours statewide
make contours INTERVAL=10m REGION=state

# Generate 50m contours per county
make contours INTERVAL=50m REGION=county

# Build PMTiles for web publishing
make tiles-contours

# Register and validate in STAC
make stac stac-validate


⸻

📜 Naming & Metadata

Filename pattern

contours_<interval>_<region>.geojson|gpkg|pmtiles

STAC Item requirements
	•	properties.interval → contour interval in meters/feet
	•	proj:epsg → target CRS (EPSG:4326 for published layers)
	•	kfm:method → algorithm (gdal_contour, richdem, etc.)
	•	kfm:lineage → DEM sources + commit refs
	•	processing:software → container / version tags

⸻

🔬 QA & Uncertainty
	•	Cross-check contour lines against DEM hillshade.
	•	Validate closure, topology, and snapping at tile edges.
	•	Compare against USGS topo contours for sanity check.
	•	Flag outputs with qa:status = draft | provisional | verified.

⸻

🚀 Publishing
	•	Store as GeoJSON or GeoPackage in data/derivatives/contours/.
	•	Build PMTiles for fast MapLibre/Google Earth visualization.
	•	Register as STAC Items in stac/items/ under contours.json.
	•	Validate in CI (stac-validate.yml).

⸻

📑 Example STAC Item (10m statewide contours)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_contours_10m_state",
  "properties": {
    "title": "Kansas Contours 10m (Statewide)",
    "description": "10-meter interval contour lines derived from 1m LiDAR DEM mosaics.",
    "start_datetime": "2012-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "interval": 10,
    "proj:epsg": 4326,
    "kfm:method": "gdal_contour -i 10",
    "kfm:lineage": [
      "data/cogs/dem/ks_lidar_2012.tif",
      "data/cogs/dem/ks_lidar_2020.tif"
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
      "href": "../../stac/collections/contours.json"
    }
  ],
  "assets": {
    "geojson": {
      "href": "../../data/derivatives/contours/10m/contours_10m_state.geojson",
      "title": "Contours 10m GeoJSON",
      "type": "application/geo+json",
      "roles": ["data", "vector"]
    },
    "pmtiles": {
      "href": "../../data/derivatives/contours/index/ks_contours_10m.pmtiles",
      "title": "Contours 10m PMTiles",
      "type": "application/vnd.pmtiles",
      "roles": ["data", "tiles"]
    }
  }
}


⸻

👩‍💻 Contributor Notes
	•	Add recipes/scripts under scripts/contours/ with parameters (interval, smoothing, CRS).
	•	Document methods in docs/methods/contours.md.
	•	Always generate SHA-256 sidecars for provenance.
	•	Prefer EPSG:4326 for published vectors; keep local projections only for internal QA.