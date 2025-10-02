<div align="center">

# 📜 Kansas-Frontier-Matrix — Land & Cadastral Scanned Maps  
`data/sources/land/scans/`

**Mission:** Curate **scanned cadastral plats, atlases, and early surveys**  
so they are **traceable, reproducible, and discoverable** in the STAC catalog,  
and integrated into the Frontier-Matrix **timeline + knowledge graph**.  

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

- Preserve **historic cadastral plats, atlases, and land survey scans**  
- Provide **georeferenced rectifications** of historical maps  
- Enable **timeline visualization** of settlement, ownership, and parcel changes  
- Link plats & atlases to **treaties, deeds, and tribal land cessions**  
- Ensure scans are **provenance-tracked, licensed, and reproducible**  

---

## 📂 Directory Layout

```text
data/sources/land/scans/
├── county_plats_1880s.json     # 1880s county plat atlas scans
├── cadastral_atlases.json      # Library of Congress / KHS atlases
├── early_surveys.json          # GLO/PLSS early land survey scans
├── deeds_register.json         # Register of Deeds tract book scans
├── *.tif / *.pdf               # Raw scans (stored in data/raw/land/scans/)
└── README.md                   # This file

⚠️ Raw scans → data/raw/land/scans/ (ignored by git).
✅ Processed/georeferenced outputs → data/processed/land/scans/ (LFS).
📑 Only descriptors, metadata, and checksums live here.

⸻

🧭 Descriptor Schema

Each scanned dataset must follow
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "county_plats_1880s",
  "title": "Kansas County Plat Atlases (1880s)",
  "type": "raster",
  "description": "Digitized scans of 1880s Kansas county plat atlases. Show township/range/section, land ownership, and early infrastructure.",
  "period": "1880-1890",
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "urls": [
    "https://www.kshs.org/p/county-atlases-and-maps/13859"
  ],
  "license": {
    "name": "Public Domain",
    "url": "https://www.kshs.org/"
  },
  "provenance": {
    "attribution": "Kansas Historical Society",
    "retrieved": "2025-09-21T00:00:00Z"
  },
  "keywords": ["plats", "atlases", "cadastral", "Kansas", "scan"]
}

Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	period → explicit (YYYY, YYYY–YYYY, or named era)
	•	Always include license + provenance
	•	urls[] → authoritative archives (KHS, LoC, Register of Deeds, BLM GLO)

⸻

🌍 Recommended Scan Sources
	•	Kansas Historical Society — county plat books, atlases
	•	Library of Congress — cadastral atlases & early plats
	•	BLM GLO Records — original PLSS survey plats (1850s–1900s)
	•	County Register of Deeds — tract book scans, early title records
	•	Kansas GIS Archive Hub — digitized cadastral scans

⸻

🔗 Integration Notes
	•	Georeferencing: scanned plats rectified to PLSS grids
	•	Timeline: link atlases to county formation + settlement periods
	•	Cross-domain:
	•	Treaties (land cessions ↔ plats)
	•	Hazards (flooded townsites in plats)
	•	Settlements (town plats ↔ census & deeds)
	•	Documents (tract books, diaries, land acts)

⸻

✅ Best Practices
	•	Store raw scans → data/raw/land/scans/
	•	Store rectified GeoTIFFs/COGs → data/processed/land/scans/
	•	Maintain .sha256 checksums + retrieval timestamps
	•	Record original CRS in _meta.json after georeferencing
	•	Automate ingestion with:

make fetch land-scans
make cogs
make stac

	•	Add confidence flags for low-quality scans or uncertain rectifications

⸻

🔍 Debugging & Validation

make validate-sources   # schema compliance
make fetch              # pull raw scans
make cogs               # convert scans → COGs
make stac               # rebuild STAC items
make validate-stac      # validate against STAC 1.0.0
make checksums          # update .sha256 integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Land Scan Descriptors\n(data/sources/land/scans/*.json)] -->|fetch| R[Raw Scans\n(data/raw/land/scans/)]
  R -->|rectify| P[Processed GeoTIFF/COGs\n(data/processed/land/scans/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	Kansas Historical Society — County Atlases & Plat Maps
	•	Library of Congress — Sanborn & cadastral atlases
	•	BLM General Land Office (GLO) Records
	•	Kansas GIS Archive Hub — cadastral scans
	•	County Register of Deeds archives

⸻

✦ Summary

data/sources/land/scans/ defines descriptors for historic cadastral plats, atlases, and land surveys.
They ensure Kansas land records are digitized, georeferenced, timeline-aware, and provenance-tracked,
fully integrated into the STAC catalog, treaty/cession datasets, and the Frontier-Matrix knowledge graph.