<div align="center">

# 🗂️ Kansas-Frontier-Matrix — Derivative Tiles  
`data/derivatives/tiles/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)

**Mission:** Hold **versioned, distributable tile layers** (raster + vector) derived from  
canonical sources for long-term reproducibility.  
Unlike `data/tiles/` (scratch outputs), this directory is for **archived PMTiles/MBTiles**  
that are registered in STAC and integrated into the web viewer.  

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Derivatives\n(data/derivatives/*)"] --> B["Tile Generation\n(make tiles-*)"]
  B --> C["Tiles\n(data/derivatives/tiles)"]
  C --> D["STAC Items\n(stac/items/tiles_*)"]
  D --> E["Validate\n(stac-validate)"]
  C --> F["Web Viewer\n(web/tiles, MapLibre)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ tiles/
      ├─ raster/                 # Raster tiles (hillshade, landcover)
      │  └─ hillshade.pmtiles
      ├─ vector/                 # Vector tiles (streams, parcels, treaties)
      │  └─ streams.pmtiles
      ├─ hybrid/                 # Raster+vector MBTiles
      │  └─ nlcd_change_2001_2021.mbtiles
      ├─ qc/                     # QA previews, reports
      │  └─ tile_preview.png
      └─ README.md


⸻

✅ What Belongs Here
	•	Raster tiles → PMTiles/MBTiles pyramids from DEMs, hillshade, landcover.
	•	Vector tiles → PMTiles from GeoJSON/Parquet (streams, hazards, parcels, treaties).
	•	Hybrid tiles → MBTiles with both raster + vector.
	•	QA artifacts → coverage maps, sample tiles, reports.

🚫 Does Not Belong
	•	Raw COGs or vectors (data/derivatives/*/).
	•	Ephemeral z/x/y tiles (use data/tiles/ instead).

⸻

🛠 Workflow & Make Targets

# Build raster PMTiles from a COG
make tiles-raster INPUT=data/derivatives/terrain/hillshade/hillshade_1m_state.tif \
  OUT=data/derivatives/tiles/raster/hillshade.pmtiles

# Build vector PMTiles from GeoJSON
make tiles-vector INPUT=data/derivatives/hydrology/streams/streams.geojson \
  OUT=data/derivatives/tiles/vector/streams.pmtiles

# Build MBTiles (raster+vector hybrid)
make tiles-mbtiles

# Register and validate STAC items
make stac stac-validate


⸻

📜 Naming & Metadata

Filename pattern

<topic>[_<interval>|_<theme>].pmtiles|mbtiles

Examples:
	•	hillshade.pmtiles
	•	streams.pmtiles
	•	nlcd_change_2001_2021.mbtiles

STAC Item requirements
	•	properties.topic → hillshade, streams, nlcd_change, etc.
	•	proj:epsg → 4326 for published layers
	•	kfm:method → tile tool (tippecanoe, rio-mbtiles, pmtiles convert)
	•	kfm:lineage → input derivative(s) + commit ref
	•	qa:status → draft, provisional, verified

⸻

🔬 QA & Uncertainty
	•	Raster tiles → check tile edges, compression artifacts, color ramps.
	•	Vector tiles → verify attributes, topology, simplification thresholds.
	•	Coverage maps → confirm extents match source datasets.
	•	Viewer test → ensure rendering in MapLibre + Google Earth.

⸻

🚀 Publishing
	•	Prefer PMTiles for modern single-file web delivery.
	•	Use MBTiles where compatibility is required.
	•	Register as STAC Items in stac/items/tiles/.
	•	Validate in CI (stac-validate.yml).
	•	Reference in web/config/layers.json for integration.

⸻

📑 Example STAC Item (Hillshade PMTiles)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_tiles_hillshade",
  "properties": {
    "title": "Kansas Hillshade (PMTiles)",
    "description": "Statewide hillshade tiles derived from 1m DEM hillshade raster.",
    "start_datetime": "2020-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "rio-mbtiles --format=pmtiles",
    "kfm:lineage": [
      "data/derivatives/terrain/hillshade/hillshade_1m_state.tif"
    ],
    "processing:software": "rio-mbtiles 1.3.0 (Docker image ghcr.io/bartytime4life/kfm-tiles:1.3.0)",
    "qa:status": "verified"
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
      "href": "../../../stac/collections/tiles.json"
    }
  ],
  "assets": {
    "pmtiles": {
      "href": "../../../data/derivatives/tiles/raster/hillshade.pmtiles",
      "title": "Hillshade PMTiles",
      "type": "application/vnd.pmtiles",
      "roles": ["data", "tiles"]
    }
  }
}


⸻

👩‍💻 Contributor Notes
	•	Implement recipes in scripts/tiles/ with explicit parameters.
	•	Document tile-building methods in docs/methods/tiles.md.
	•	Always generate .sha256 checksums for provenance.
	•	Publish outputs in EPSG:4326 for widest compatibility.
	•	Update STAC items + web/config/layers.json whenever adding new tiles.