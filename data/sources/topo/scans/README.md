<div align="center">

# 🏔️ Kansas-Frontier-Matrix — Topographic Scanned Maps  
`data/sources/topo/scans/`

**Mission:** Curate **scanned topographic maps and atlases** (USGS quads, county topo sheets, historic survey maps)  
so they are **traceable, reproducible, and discoverable** in the STAC catalog,  
and fully integrated into the Frontier-Matrix **timeline + knowledge graph**.  

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

- Preserve **historic topographic maps** (USGS quads, military survey sheets, early atlases)  
- Provide **georeferenced rectifications** of topo scans for modern analysis  
- Enable **timeline visualizations** (pre-railroad, Dust Bowl, pre/post dam landscapes)  
- Connect topo maps to **hazards, settlements, and ecological change**  
- Ensure scans are **licensed, provenance-tracked, and reproducible**  

---

## 📂 Directory Layout

```text
data/sources/topo/scans/
├── usgs_quads_1890s.json      # Historic USGS topographic quadrangles
├── county_topo_1930s.json     # Depression-era topo surveys
├── military_surveys.json      # Early military topographic sheets
├── atlas_topo.json            # County/state topo atlases
├── *.tif / *.pdf              # Raw scans (stored in data/raw/topo/scans/)
└── README.md                  # This file

⚠️ Raw scans → data/raw/topo/scans/ (ignored).
✅ Processed/georeferenced outputs → data/processed/topo/scans/ (LFS).
📑 Only descriptors, metadata, and checksums live here.

⸻

🧭 Descriptor Schema

Each topo scan descriptor must follow
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "usgs_quads_1890s",
  "title": "USGS Kansas Topographic Quadrangles (1890s)",
  "type": "raster",
  "description": "Scanned USGS topo quads covering Kansas (1:125,000 scale, 1890s editions). Digitized and georeferenced.",
  "period": "1890-1900",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://ngmdb.usgs.gov/topoview/"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.usgs.gov/"
  },
  "provenance": {
    "attribution": "USGS Topographic Archive",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["topo", "USGS", "quads", "Kansas", "scan"]
}

Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	period → explicit (YYYY, YYYY–YYYY, or named era)
	•	Always include license + provenance
	•	urls[] → authoritative archives (USGS TopoView, Library of Congress, KHS)

⸻

🌍 Recommended Scan Sources
	•	USGS TopoView Archive — historic topo quadrangles
	•	Kansas Historical Society — county atlases & topo maps
	•	Library of Congress — historical topo atlases and surveys
	•	U.S. Army / Military Survey Maps — early frontier topo mapping
	•	Kansas GIS Archive Hub — scanned and digitized topo layers

⸻

🔗 Integration Notes
	•	Georeferencing: scans rectified to DEM/PLSS for alignment
	•	Timeline: support visualizing changes in terrain use across decades
	•	Cross-domain:
	•	Hazards (floods, droughts, fires) visible in maps
	•	Settlements (town growth, railroad expansion)
	•	Land cover (grassland → cropland conversion)
	•	Infrastructure (dams, canals, reservoirs)

⸻

✅ Best Practices
	•	Store raw scans → data/raw/topo/scans/
	•	Store rectified GeoTIFFs (COGs) → data/processed/topo/scans/
	•	Maintain .sha256 checksums + retrieval timestamps
	•	Record original CRS in _meta.json after rectification
	•	Automate ingestion with:

make fetch topo-scans
make cogs
make stac
make validate-stac

	•	Add confidence flags for incomplete coverage or poor georeferencing

⸻

🔍 Debugging & Validation

make validate-sources   # schema compliance
make fetch              # pull raw scans
make cogs               # convert scans → COGs
make stac               # rebuild STAC items
make validate-stac      # STAC 1.0.0 compliance
make checksums          # refresh integrity sidecars


⸻

📊 Data Lifecycle

flowchart TD
  S[Topo Scan Descriptors\n(data/sources/topo/scans/*.json)] -->|fetch| R[Raw Scans\n(data/raw/topo/scans/)]
  R -->|rectify| P[Processed GeoTIFF/COGs\n(data/processed/topo/scans/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	USGS TopoView Archive
	•	Kansas Historical Society — Map Collections
	•	Library of Congress — Historical Atlases & Topo Maps
	•	U.S. Army / Corps of Engineers Survey Maps
	•	Kansas GIS Archive Hub

⸻

✦ Summary

data/sources/topo/scans/ defines descriptors for scanned topographic maps and atlases.
They ensure topo history is digitized, georeferenced, timeline-aware, and provenance-tracked,
fully integrated into the STAC catalog, knowledge graph, and Frontier-Matrix viewer.