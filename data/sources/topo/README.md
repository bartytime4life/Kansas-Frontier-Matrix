<div align="center">

# 🏔 Kansas-Frontier-Matrix — Topographic & Elevation Sources  
`data/sources/topo/`

**Mission:** Catalog Kansas topographic and elevation datasets so they are  
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

- Provide **baseline terrain context** (DEM, contours, shaded relief)  
- Preserve **historic USGS topo sheets** (19th–20th century editions)  
- Enable **temporal comparisons** (historic topo vs. modern DEM)  
- Support **hydrology, soils, and land-use overlays** with terrain backdrops  
- Link terrain to **migration routes, forts, flood events, Dust Bowl studies**  

---

## 📂 Directory Layout

```text
data/sources/topo/
├── usgs_historic_topo.json   # Historic USGS topo map scans (GeoTIFF/COG)
├── ks_dem.json               # Kansas statewide DEM (1m LiDAR, 10m USGS NED)
├── hillshade.json            # Hillshade overlays (LiDAR-derived, statewide)
├── contours.json             # Derived contours from DEM
├── scans/                    # Raw scanned topo maps (GeoTIFF, MrSID, PDF)
├── vectors/                  # Contour shapefiles/GeoJSON
└── README.md                 # This file

⚠️ Raw scans → data/raw/topo/ (ignored).
✅ Processed outputs → data/processed/topo/ (LFS).
📑 Only descriptors, checksums, metadata live here.

⸻

🧭 Metadata Schema

Datasets follow the
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "usgs_historic_topo",
  "title": "USGS Historical Topographic Maps (Kansas)",
  "type": "raster",
  "version": "1.0.0",
  "description": "Georeferenced scans of historic USGS topo maps (1880s–2000s), clipped to Kansas. Includes 15', 7.5', and 1:24k series. Useful for tracing settlement, railroads, hydrology changes, and land use evolution.",
  "temporal": { "start": "1880-01-01", "end": "2000-12-31" },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://prd-tnm.s3.amazonaws.com/StagedProducts/Maps/HistoricalTopo/GeoTIFF/"
      ]
    }
  ],
  "lineage": [
    "Fetched from USGS Historical Topo Map Collection",
    "Converted to Cloud-Optimized GeoTIFF (COG)",
    "Clipped to Kansas boundary"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["topographic", "USGS", "Kansas", "historic maps", "terrain"],
  "confidence": "high"
}

Rules
	•	bbox → EPSG:4326 (lon/lat WGS84)
	•	temporal → explicit (year, year range, or current)
	•	Always include license + provenance
	•	endpoints[] → multiple sources supported

⸻

🌍 Recommended Topo & Elevation Sources

Historic Topographic Maps
	•	USGS Historical Topo Map Collection (GeoTIFF, 1880s–2000s)
	•	Kansas GIS Archive — county topo sheets, plats

Digital Elevation Models (DEM)
	•	USGS 3DEP — 10m DEM (nationwide)
	•	Kansas 1m LiDAR DEM (KARS / DASC)

Derived Terrain Products
	•	Hillshade, slope, aspect, roughness (from DEM)
	•	Contours (10–50 ft intervals, county/statewide)

⸻

🔗 Integration Notes
	•	Time-aware topo layers: historic sheets tagged by survey/publication year
	•	DEM derivatives: use make terrain for slope, aspect, TRI/TPI
	•	Georeferencing: all scans rectified to EPSG:4326 (WGS84)
	•	Cross-links:
	•	Trails & forts ↔ ridges, rivers, passes
	•	Dust Bowl overlays ↔ slope/erosion factors
	•	Flood studies ↔ DEM + hydrology integration

⸻

✅ Best Practices
	•	Store raw scans in scans/ (GeoTIFF/MrSID, unmodified)
	•	Convert to COGs for web tiling (rio cogeo create …)
	•	Standardize vectors (contours, boundaries) → GeoJSON EPSG:4326
	•	Update checksums in data/provenance/registry.json
	•	Always include temporal attributes (survey year, edition)

⸻

📊 Data Lifecycle

flowchart TD
  S[Topo Descriptors\n(data/sources/topo/*.json)] -->|fetch| R[Raw Scans\n(data/raw/topo/)]
  R -->|process| P[Processed DEMs & COGs\n(data/processed/topo/)]
  P -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> V[MapLibre Web Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	USGS Historical Topographic Map Collection
	•	Kansas GIS Archive Hub – Historical Datasets
	•	Kansas Data Access & Support Center (DASC)
	•	USGS 3DEP (National DEM)

⸻

✦ Summary

data/sources/topo/ defines descriptors for Kansas topographic & elevation datasets — historic maps, DEMs, and terrain derivatives.
They ensure terrain is auditable, timeline-aware, and cross-linked into the STAC catalog,
and integrated into hazards, hydrology, and settlement layers in the Frontier-Matrix knowledge graph.