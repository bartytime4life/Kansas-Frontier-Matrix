<div align="center">

# 🗺️ Kansas-Frontier-Matrix — Hydrology Scanned Maps & Documents  
`data/sources/hydro/scans/`

**Mission:** Curate **historical scanned hydrology maps and documents**  
(floodplains, river surveys, dam blueprints, irrigation maps) so they are  
**traceable, reproducible, and discoverable** in the STAC catalog,  
and linked into the Frontier-Matrix **timeline + knowledge graph**.  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](../../../../.github/workflows/site.yml)  
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-validate.yml/badge.svg)](../../../../.github/workflows/stac-validate.yml)  
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../../../../.pre-commit-config.yaml)  
[![CodeQL](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/codeql.yml/badge.svg)](../../../../.github/workflows/codeql.yml)  
[![Trivy Security](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/trivy.yml/badge.svg)](../../../../.github/workflows/trivy.yml)  
[![Automerge](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/automerge.yml/badge.svg)](../../../../.github/workflows/automerge.yml)  
[![Docs](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/docs.yml/badge.svg)](../../../../.github/workflows/docs.yml)  
[![Coverage](https://img.shields.io/codecov/c/github/bartytime4life/Kansas-Frontier-Matrix)](https://app.codecov.io/gh/bartytime4life/Kansas-Frontier-Matrix)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](../../../../LICENSE)  

</div>

---

## 🎯 Purpose

- Preserve **scanned historical hydrology records** (maps, reports, flood insurance studies)  
- Provide **georeferenced rectifications** of historic river & floodplain maps  
- Link floodplain change to **events** (1903, 1951, 1993 Kansas River floods)  
- Connect **infrastructure blueprints** (dams, levees, irrigation projects) to events and places  
- Ensure scanned data is **discoverable, licensed, and provenance-tracked**  

---

## 📂 Directory Layout

```text
data/sources/hydro/scans/
├── floodplain_1951_fema.json   # 1951 Flood maps (FEMA/Kansas archives)
├── kansas_river_1903.json      # 1903 Kansas River flood historic survey maps
├── reservoir_blueprints.json   # USACE reservoir & dam construction scans
├── irrigation_maps.json        # Historic irrigation district plats
├── *.tif / *.pdf               # Scanned map files (stored in data/raw/hydro/scans/)
└── README.md                   # This file

⚠️ Scanned images → stored in data/raw/hydro/scans/ (ignored by git).
✅ Only descriptors, metadata, sidecars, and provenance files live here.
🗄️ Processed/georeferenced outputs → data/processed/hydro/scans/ (LFS).

⸻

🧭 Descriptor Schema

Each scanned dataset must follow
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "floodplain_1951",
  "title": "Kansas River Floodplain Map (1951)",
  "type": "raster",
  "description": "Historic floodplain extent map from the 1951 Kansas River flood. Digitized from FEMA/Kansas archives.",
  "period": "1951",
  "bbox": [-97.0, 38.8, -95.0, 39.2],
  "urls": [
    "https://msc.fema.gov/portal/search"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://msc.fema.gov/"
  },
  "provenance": {
    "attribution": "FEMA + Kansas Historical Society",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["flood", "Kansas River", "FEMA", "hydrology", "scan"]
}

Key Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	period → year or date range of the scan/document
	•	Always include license + provenance
	•	urls[] → authoritative archives (FEMA MSC, KGS, KDHE, USACE)

⸻

🌍 Recommended Scan Sources
	•	FEMA Flood Insurance Rate Maps (FIRM) — scanned + digital floodplains
	•	Kansas Historical Society — archival maps of rivers and reservoirs
	•	USACE archives — dam/reservoir blueprints, hydrology surveys
	•	USGS Historic Topographic Quadrangles — floodplain delineations
	•	KDHE/KGS Reports — water resource maps, irrigation surveys

⸻

🔗 Integration Notes
	•	Flood history: Link floodplain scans to hazards/floods.json descriptors
	•	Dams & reservoirs: Tie scanned dam/reservoir maps to lakes_reservoirs.json
	•	Cross-domain:
	•	Hazards (Event: floods, droughts, HABs)
	•	Settlements (towns inundated, relocated)
	•	Documents (FEMA studies, USACE reports)

⸻

✅ Best Practices
	•	Store raw scans → data/raw/hydro/scans/
	•	Store rectified GeoTIFFs → data/processed/hydro/scans/ (COG format)
	•	Maintain .sha256 checksums + retrieved date on updates
	•	Record original CRS (if rectified) in _meta.json
	•	Automate ingestion:

make fetch hydro-scans
make cogs
make stac

	•	Use confidence flags (kfm:confidence) for low-quality or partially georeferenced scans

⸻

🔍 Debugging & Validation

make validate-sources   # schema compliance
make fetch              # pull raw scans
make cogs               # convert scans → COGs
make stac               # rebuild STAC items
make validate-stac      # validate against STAC 1.0.0
make checksums          # refresh .sha256 integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Scan Descriptors\n(data/sources/hydro/scans/*.json)] -->|fetch| R[Raw Scans\n(data/raw/hydro/scans/)]
  R -->|rectify| P[Processed GeoTIFF/COGs\n(data/processed/hydro/scans/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	FEMA Flood Insurance Studies & Maps
	•	Kansas Historical Society Map Collection
	•	USACE Reservoir/Dam Archives
	•	USGS Historical Topographic Quadrangles
	•	KDHE & KGS Water Resources Reports

⸻

✦ Summary

data/sources/hydro/scans/ defines descriptors for scanned hydrology maps and documents —
flood studies, river surveys, irrigation plats, dam/reservoir blueprints.
They ensure Kansas hydrology history is digitized, georeferenced, auditable, and timeline-aware,
fully integrated into the STAC catalog, knowledge graph, and interactive Frontier-Matrix viewer.