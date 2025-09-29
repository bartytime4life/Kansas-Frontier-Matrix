
<div align="center">

# 🌪 Kansas-Frontier-Matrix — Hazards & Disasters Sources

**Mission:** Catalog Kansas hazard & disaster datasets so they are  
**traceable, reproducible, and discoverable** in the STAC catalog,  
and linked into the Frontier-Matrix **timeline + knowledge graph**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.pre-commit-config.yaml)

</div>

---

## 🎯 Purpose

- Track **hazard events** (tornadoes, floods, droughts, wildfires, storms)  
- Provide **geospatial layers** (vectors, rasters, tabular CSVs)  
- Link hazards to **documents and events** (e.g., Greensburg Tornado 2007)  
- Maintain **provenance & licensing** per Master Coder Protocol (MCP)  
- Enable **cross-domain reasoning**: climate ↔ settlement ↔ environment  

---

## 📂 Directory Layout

```text
data/sources/hazards/
├── tornado_tracks.json       # NOAA SPC tornado paths (1950–present)
├── severe_storms.json        # Hail / wind reports (1955–present)
├── fema_disasters.json       # FEMA declarations (1953–present)
├── drought_monitor.json      # US Drought Monitor (2000–present)
├── wildfire_perimeters.json  # NIFC & Kansas Forest Service polygons
├── scans/                    # Optional scanned maps / PDFs
├── vectors/                  # Converted shapefiles/GeoJSONs
└── README.md                 # This file

Note: Large binaries (shapefiles, rasters) → data/raw/ (ignored).
Processed outputs → data/processed/hazards/ (LFS).
Only descriptors, checksums, metadata live here.

⸻

📑 Descriptor Schema

Each hazard config must follow the
KFM Source Descriptor Schema (data/sources/schema.source.json).

{
  "id": "tornado_tracks",
  "title": "NOAA SPC Tornado Paths (1950–present)",
  "type": "vector",
  "description": "Tornado tracks across Kansas with EF scale, path width, fatalities, damage.",
  "period": "1950-2024",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": ["https://www.spc.noaa.gov/gis/svrgis/"],
  "license": {
    "name": "Public Domain",
    "url": "https://www.spc.noaa.gov/gis/svrgis/"
  },
  "provenance": {
    "attribution": "NOAA Storm Prediction Center",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["tornado", "hazard", "Kansas", "SPC"]
}

Key Rules
	•	bbox → EPSG:4326 (lon/lat WGS84)
	•	period → temporal extent for STAC & timeline
	•	Always include license & provenance
	•	urls[] → API endpoints, shapefile zips, or services

⸻

🌍 Recommended Hazard Sources
	•	NOAA Storm Events Database — multi-hazard archive (1950–present)
	•	NOAA SPC Severe Weather GIS — tornado tracks, hail, wind (1950–2024)
	•	FEMA Disaster Declarations — county-level, 1953–present
	•	U.S. Drought Monitor — weekly drought polygons (2000–present)
	•	NIFC Wildfire Perimeters — national dataset, 2000–present
	•	Kansas Forest Service — state wildfire perimeter datasets

⸻

🔗 Integration Notes
	•	Hazards are time-enabled: descriptors must include start/end dates
	•	Tornadoes: polylines with EF scale, path width, fatalities
	•	Droughts: polygons (D0–D4 categories), weekly snapshots = time series
	•	Floods: link FEMA declarations + NOAA Storm Events
	•	Wildfires: polygons with ignition date, acres burned, fire name

Hazards link into the Knowledge Graph:
	•	Event → e.g., Greensburg Tornado 2007
	•	Place → county, watershed, or polygon
	•	Document → FEMA reports, NOAA Storm Data, newspapers

⸻

✅ Best Practices
	•	Store raw shapefiles/CSVs → data/raw/hazards/
	•	Store converted GeoJSON/COGs → data/processed/hazards/
	•	Update .sha256 + retrieved date after pulls
	•	Use confidence flags if geometries incomplete
	•	Normalize CRS → EPSG:4326 for viewer; record original CRS in _meta.json
	•	Verify license compliance (NOAA/FEMA/NIFC = public domain; check Kansas Forest Service)

⸻

🔍 Debugging & Validation

make validate-sources   # schema validation
make fetch              # download hazard data
make vectors            # shapefile → GeoJSON
make stac               # build STAC Items/Collections
make validate-stac      # validate STAC 1.0.0
make checksums          # update integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Hazard Descriptors\n(data/sources/hazards/*.json)] -->|fetch| R[Raw Data\n(data/raw/hazards/)]
  R -->|convert| P[Processed GeoJSON/COGs\n(data/processed/hazards/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Web Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	NOAA Storm Events Database
	•	NOAA SPC Severe Weather GIS
	•	FEMA Disaster Declarations
	•	U.S. Drought Monitor
	•	NIFC Open Fire Data
	•	Kansas GIS Hub – Wildfire Perimeters

⸻

✦ Summary
data/sources/hazards/ defines the blueprints for hazard & disaster datasets.
They ensure tornadoes, floods, droughts, wildfires, and FEMA disasters are
auditable, reproducible, and time-aware — powering the Kansas-Frontier-Matrix
knowledge graph, STAC catalog, and interactive viewer.

---

⚡ Now it’s GitHub-ready: badges render, Mermaid compiles, and sections are cleanly structured.  