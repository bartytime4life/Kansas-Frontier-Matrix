<div align="center">

# 🌊 Kansas-Frontier-Matrix — Hydrology Derivatives  
`data/derivatives/hydrology/`

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../.github/workflows/stac-validate.yml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../.github/workflows/codeql.yml)  
[![Trivy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../.github/workflows/trivy.yml)

**Mission:** Hold **derived hydrology layers** computed from DEMs, NHD, flood extents, and water datasets —  
to support analysis of **rivers, streams, floodplains, wetlands, and watershed change** in Kansas.  
All products must be **reproducible, checksummed, and STAC-compliant**.

</div>

---

## 📈 Lifecycle

```mermaid
flowchart TD
  A["Inputs\n(data/cogs/dem, data/sources/nhd, flood, wetlands)"] --> B["Hydro Derivation\n(make hydrology)"]
  B --> C["Hydro Derivatives\n(data/derivatives/hydrology)"]
  C --> D["STAC Items\n(stac/items/hydrology_*)"]
  D --> E["Validate\n(stac-validate)"]
  C --> F["Tiles/PMTiles\n(web/tiles)"]

<!-- END OF MERMAID -->



⸻

📂 Directory Layout

data/
└─ derivatives/
   └─ hydrology/
      ├─ flowdir/               # Flow direction rasters
      │  └─ flowdir_1m_state.tif
      ├─ flowacc/               # Flow accumulation rasters
      │  └─ flowacc_1m_state.tif
      ├─ streams/               # Extracted stream networks
      │  └─ streams_threshold_100_cells.geojson
      ├─ floodplains/           # Derived floodplain extents
      │  └─ floodplain_100yr_kansas.tif
      ├─ wetlands/              # Wetland masks or deltas
      │  └─ wetlands_change_1992_2021.geojson
      ├─ qc/                    # QA reports, masks, residuals
      │  └─ hydro_qc_report.md
      └─ README.md


⸻

✅ What Belongs Here
	•	DEM-based hydrology products → flow direction, accumulation, sink-filled DEMs.
	•	Stream networks → extracted from flow accumulation thresholds.
	•	Floodplain rasters → derived from DEMs, flood profiles, FEMA DFIRMs.
	•	Wetlands & hydro change layers → mask rasters, vector outlines, deltas.

🚫 Does Not Belong
	•	Raw DEMs (data/cogs/dem/).
	•	NHD/HUC source vectors (data/sources/nhd/).
	•	Temporary flood event scratch layers (data/tiles/).

⸻

🛠 Workflow & Make Targets

# Build DEM → hydro derivatives
make hydrology-flowdir     # Flow direction raster
make hydrology-flowacc     # Flow accumulation raster
make hydrology-streams     # Extract stream network

# Flood & wetlands
make hydrology-floodplain  # 100yr flood extents
make hydrology-wetlands    # Wetland masks and deltas

# Register in STAC
make stac stac-validate

# Build tiles for web viewer
make tiles-hydrology


⸻

📜 Naming & Metadata

Filename pattern

<topic>_<resolution>_<region>[_<parameter>].tif|geojson|pmtiles

Examples:
	•	flowdir_1m_state.tif
	•	floodplain_100yr_kansas.tif
	•	streams_threshold_100_cells.geojson

STAC Item requirements
	•	properties.topic → flowdir, flowacc, streams, floodplain, wetlands
	•	proj:epsg → 4326 for published outputs
	•	kfm:method → algorithm (D8, D∞, HAND, etc.)
	•	kfm:lineage → DEM/NHD inputs + commit ref
	•	qa:status → draft, provisional, verified

⸻

🔬 QA & Uncertainty
	•	Flowdir/flowacc → verify drainage against NHD flowlines.
	•	Streams → cross-check against USGS gages + NHD flowline density.
	•	Floodplain extents → validate against FEMA DFIRMs, historical flood footprints (e.g., 1951 KS flood).
	•	Wetlands → compare against NWI polygons, NDWI/NDVI indices.
	•	Error budgets → report DEM vertical RMSE + flood model uncertainty.

⸻

🚀 Publishing
	•	Publish rasters as COG (with internal overviews).
	•	Publish vectors as GeoJSON/PMTiles.
	•	Register as STAC Items in stac/items/hydrology/.
	•	Validate with CI (stac-validate.yml).

⸻

📑 Example STAC Item (Flow Accumulation, 1m)

{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "ks_flowacc_1m_state",
  "properties": {
    "title": "Kansas Flow Accumulation (1m)",
    "description": "Flow accumulation raster derived from 1m LiDAR DEMs across Kansas.",
    "start_datetime": "2018-01-01T00:00:00Z",
    "end_datetime": "2020-12-31T23:59:59Z",
    "proj:epsg": 4326,
    "kfm:method": "RichDEM d8_flow_accumulation",
    "kfm:lineage": [
      "data/cogs/dem/ks_1m_2018.tif",
      "data/cogs/dem/ks_1m_2020.tif"
    ],
    "processing:software": "richdem 0.3.4 (Docker image ghcr.io/bartytime4life/kfm-hydro:0.3.4)",
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
      "href": "../../stac/collections/hydrology.json"
    }
  ],
  "assets": {
    "cog": {
      "href": "../../data/derivatives/hydrology/flowacc/flowacc_1m_state.tif",
      "title": "Flow Accumulation (1m, statewide)",
      "type": "image/tiff; application=geotiff; profile=cloud-optimized",
      "roles": ["data", "raster"]
    }
  }
}


⸻

👩‍💻 Contributor Notes
	•	Place new methods in scripts/hydrology/ (flowdir, HAND, stream extraction).
	•	Document workflows in docs/methods/hydrology.md.
	•	Always add .sha256 checksums for provenance.
	•	Default to EPSG:4326 for published products; keep local CRS only for QA.