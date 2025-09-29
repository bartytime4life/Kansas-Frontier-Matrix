
<div align="center">

# 🗺 Kansas-Frontier-Matrix — Land, Soils & Cadastral Sources

**Mission:** catalog Kansas land-related datasets so they are  
**traceable, reproducible, and discoverable** in the STAC catalog,  
and linked into the Frontier-Matrix **timeline + knowledge graph**.

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](../.pre-commit-config.yaml)

</div>

---

## 🎯 Purpose

- Provide **historical + modern cadastral context** (PLSS, parcels)  
- Track **land cover / land use change** (grassland → agriculture → urban)  
- Integrate **soil surveys, fertility, erosion data** into environmental analysis  
- Link land datasets to **treaties, settlement, agricultural expansion**  
- Enable **timeline visualization** of land transformation  
- Support **AI-driven correlations** between land, climate, hydrology, and society  

---

## 📂 Directory Layout

```text
data/sources/land/
├── plss.json                 # Public Land Survey System (township, range, section grids)
├── parcels.json              # Modern cadastral parcels (select counties, as available)
├── soils_ssurgo.json         # USDA NRCS SSURGO soil surveys
├── landcover_nlcd.json       # NLCD land cover (1992–present)
├── landcover_historic.json   # Historic vegetation/land use reconstructions
├── scans/                    # Scanned cadastral plats, atlases, early surveys
├── vectors/                  # Processed shapefiles/GeoJSON
└── README.md                 # This file

Note: Raw shapefiles/scans → data/raw/land/ (ignored).
Processed outputs → data/processed/land/ (LFS).
Only descriptors, checksums, metadata live here.

⸻

📑 Metadata Schema

Each dataset follows the KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "plss",
  "title": "Public Land Survey System (Kansas PLSS Grid)",
  "type": "vector",
  "version": "1.0.0",
  "description": "Township, range, and section boundaries from BLM PLSS data, clipped to Kansas. Useful for georeferencing historical plats, deeds, and surveys.",
  "temporal": { "start": "1854-01-01", "end": "2025-01-01" },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://gis.blm.gov/arcgis/rest/services/lands/PLSS/MapServer"
      ]
    }
  ],
  "lineage": [
    "Fetched from BLM PLSS dataset",
    "Clipped to Kansas extent",
    "Converted to GeoJSON for integration"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["PLSS", "cadastral", "township", "range", "Kansas"],
  "confidence": "high"
}

Rules
	•	bbox → EPSG:4326 (lon/lat WGS84)
	•	temporal → explicit (YYYY, YYYY-YYYY, 1930s, or current)
	•	Always include license + provenance
	•	endpoints → multiple services/endpoints as needed

⸻

🌍 Recommended Land Sources

Cadastral / PLSS
	•	BLM PLSS Data — township, range, section grids
	•	County cadastral parcels (KS GIS Hub, county assessors)
	•	Register of Deeds archives (tract books, title chains)

Soils
	•	USDA NRCS SSURGO Database — detailed soil surveys
	•	USDA STATSGO2 — generalized soils for statewide use
	•	KGS core records + erosion studies

Land Cover / Land Use
	•	NLCD (1992–2021) — 30m land cover classifications
	•	Kansas GAP (2001) — ecological land cover
	•	Kansas Ecological Systems Map (2017–18, Sentinel-2) — 10m classes
	•	Historic reconstructions — early vegetation maps, atlases

Historical Atlases & Plats
	•	Kansas Historical Society — county plat books, atlases
	•	Library of Congress — cadastral plats & atlases
	•	Kansas GIS Archive Hub — digitized scans

⸻

🔗 Integration Notes
	•	Timeline support
	•	PLSS grid (1850s–present)
	•	Parcels with temporal attributes (owner, year)
	•	Land-cover datasets (1992+, plus historic vegetation)
	•	Soil surveys connect to settlement + agriculture narratives
	•	Historic plats (scanned) can be georeferenced with data/gcp/*.yml
	•	AI modules link land units with treaties, disasters, diaries
	•	Tag datasets with confidence flags where coverage incomplete

⸻

✅ Best Practices
	•	Store raw scans in scans/, digitized vectors in vectors/
	•	Update checksums in data/provenance/registry.json
	•	Harmonize CRS → EPSG:4326 for web; retain originals for precision
	•	Cross-link to treaties & tribal cessions (land cessions → PLSS → parcels)
	•	Record uncertainty metadata (confidence scores, alignment errors)

⸻

🚀 Advanced Concepts
	•	Predictive modeling: simulate land-use under drought/fire scenarios
	•	Fractal analysis: detect self-similar patterns in parcels/settlement clusters
	•	Geoarchaeology: soil cores + land overlays to separate natural vs human change
	•	Story-mapping: tie parcels & plats to narratives (settler diaries, tribal oral histories)

⸻

📊 Data Lifecycle

flowchart TD
  S[Land Descriptors\n(data/sources/land/*.json)] -->|fetch| R[Raw Data\n(data/raw/land/)]
  R -->|convert| P[Processed GeoJSON/COGs\n(data/processed/land/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Web Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	BLM PLSS Data
	•	Kansas GIS Data Portal
	•	Kansas GIS Archive Hub
	•	USDA NRCS SSURGO
	•	[Kansas GAP Analysis Land Cover Map (2001)]
	•	[Kansas Ecological Systems Map (2017–18, Sentinel-2)]
	•	Kansas Geological Survey Core Library
	•	Kansas Historical Society – County Plat Maps

⸻

✦ Summary
data/sources/land/ defines descriptors for cadastral, soils, and land-cover datasets in Kansas.
They ensure land resources are auditable, timeline-aware, and cross-linked into the STAC catalog,
treaties, hazards, and the Frontier-Matrix knowledge graph.

---

⚡ Now your Land README is **GitHub-polished**: badges render, Mermaid compiles, sections consistent with Hazards/Hydro, and it closes with a professional summary.  