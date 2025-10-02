<div align="center">

# 💧 Kansas-Frontier-Matrix — Hydrology & Water Resources Sources  
`data/sources/hydro/`

**Mission:** Catalog Kansas hydrological datasets so they are  
**traceable, reproducible, and discoverable** in the STAC catalog,  
and linked into the Frontier-Matrix **timeline + knowledge graph**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../LICENSE)  

</div>

---

## 🎯 Purpose

- Represent **surface water networks** (streams, rivers, reservoirs, wetlands)  
- Integrate **groundwater and aquifer extents** (High Plains/Ogallala, Equus Beds, etc.)  
- Link hydrology to **historical events** (floods, irrigation projects, treaties)  
- Provide **baseline water-quality and monitoring data** (KDHE, USGS)  
- Enable **time-aware visualization** (pre-dam vs. post-dam courses, floodplains)  
- Connect water data to **hazards** (floods, droughts, HABs) and **land-use change**  

---

## 📂 Directory Layout

```text
data/sources/hydro/
├── rivers_streams.json       # NHD flowlines & waterbody polygons
├── lakes_reservoirs.json     # USACE & KDHE reservoirs/lakes
├── wetlands.json             # USFWS NWI wetlands polygons
├── aquifers.json             # USGS/KGS aquifer extents
├── groundwater_levels.json   # KGS monitoring wells
├── water_quality.json        # KDHE stream & lake monitoring sites
├── scans/                    # Historical floodplain & river maps (scanned)
├── vectors/                  # Processed shapefiles/GeoJSON layers
└── README.md                 # This file

⚠️ Raw shapefiles & rasters → data/raw/hydro/ (ignored).
✅ Processed outputs → data/processed/hydro/ (tracked with LFS).
📑 Only descriptors, checksums, metadata live here.

⸻

🧭 Descriptor Schema

Each dataset config must follow the
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "rivers_streams",
  "title": "Kansas Rivers and Streams (NHD Subset)",
  "type": "vector",
  "description": "Stream and river centerlines from the USGS National Hydrography Dataset (NHD), clipped to Kansas. Includes flowlines, waterbody polygons, stream order, and perennial/intermittent flow attributes.",
  "period": "current",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://prd-tnm.s3.amazonaws.com/NHD/HU4/0108/NHD_H_0108_GDB.zip"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.usgs.gov/national-hydrography"
  },
  "provenance": {
    "attribution": "USGS NHD",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["hydrology", "rivers", "streams", "Kansas"]
}

Key Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	period → explicit (YYYY, YYYY–YYYY, 1930s, or current)
	•	Always include license + provenance
	•	urls[] → multiple services/endpoints allowed

⸻

🌍 Recommended Hydrology Sources

Surface Water
	•	USGS National Hydrography Dataset (NHD) — rivers, streams, lakes
	•	USFWS National Wetlands Inventory (NWI) — wetlands polygons
	•	USACE & KDHE Reservoir Data — major dams/lakes (Tuttle Creek, Cheney, Milford, etc.)
	•	FEMA Flood Insurance Rate Maps (FIRM) — historical & modeled floodplains

Groundwater
	•	USGS/KGS Aquifer Extents (Ogallala, Equus Beds, Great Bend Prairie)
	•	KGS Groundwater-Level Monitoring Wells (time series)
	•	DWR/USGS Water Use Reports (irrigation, municipal, industrial)

Water Quality
	•	KDHE Surface Water Monitoring Program — 327 stream stations, 175 lakes
	•	EPA/STORET Water Quality Portal — chemistry, nutrients, HABs

⸻

🔗 Integration Notes
	•	Timeline-aware: reservoir construction, channel modifications
	•	Flood history: 1903, 1951, 1993 Kansas River floods → link to hazards (NOAA/FEMA)
	•	Aquifer depletion: Ogallala decline post-1950 → irrigation expansion
	•	Cross-domain links:
	•	Hazards (Event: floods, droughts)
	•	Settlements (Place: towns along rivers)
	•	Documents (USACE reports, KDHE advisories)

⸻

✅ Best Practices
	•	Store raw shapefiles/GeoDBs → data/raw/hydro/
	•	Store processed GeoJSON/COGs → data/processed/hydro/ (LFS)
	•	Update .sha256 checksums + retrieved date on refresh
	•	Normalize CRS → EPSG:4326 for viewer; record original CRS in _meta.json
	•	Automate with:

make fetch hydro
make vectors
make stac

	•	Add confidence flags for incomplete datasets (e.g., wells with short records)

⸻

🔍 Debugging & Validation

make validate-sources   # schema validation
make fetch              # pull raw data
make vectors            # shapefile → GeoJSON
make stac               # rebuild STAC items
make validate-stac      # STAC 1.0.0 compliance
make checksums          # refresh integrity sidecars


⸻

📊 Data Lifecycle

flowchart TD
  S[Hydrology Descriptors\n(data/sources/hydro/*.json)] -->|fetch| R[Raw Data\n(data/raw/hydro/)]
  R -->|convert| P[Processed GeoJSON/COGs\n(data/processed/hydro/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Web Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	USGS National Hydrography Dataset
	•	Kansas GIS Data Portal – Hydrology
	•	Kansas Geological Survey – Groundwater Data
	•	KDHE Water Quality Monitoring Strategy 2019–2028
	•	FEMA Flood Insurance Maps

⸻

✦ Summary

data/sources/hydro/ defines descriptors for Kansas hydrology datasets — rivers, lakes, wetlands, aquifers, and water quality.
They ensure water resources are auditable, timeline-aware, and cross-linked into the STAC catalog, hazard layers, and the Frontier-Matrix knowledge graph.