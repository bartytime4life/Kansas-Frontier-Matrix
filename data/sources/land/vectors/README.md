<div align="center">

# 🧩 Kansas-Frontier-Matrix — Land & Cadastral Vector Datasets  
`data/sources/land/vectors/`

**Mission:** Curate **vector-format land datasets** (PLSS grids, parcels, soils, land cover, vegetation)  
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

- Store **processed vector layers** for Kansas cadastral and land datasets  
- Provide **canonical geometries + attributes** for PLSS, parcels, soils, land cover, vegetation  
- Support **time-enabled layers** (historic vs. modern parcels, land cover change)  
- Maintain **provenance & licensing** with MCP rigor  
- Enable **cross-domain linking**: land ↔ treaties ↔ hazards ↔ settlements  

---

## 📂 Directory Layout

```text
data/sources/land/vectors/
├── plss.geojson              # Township, range, section PLSS grid
├── parcels.geojson           # County parcels (where available)
├── soils_ssurgo.geojson      # USDA NRCS SSURGO polygons
├── landcover_nlcd.geojson    # NLCD land cover (1992–present)
├── landcover_historic.geojson# Historic vegetation / land use
└── README.md                 # This file

⚠️ Raw shapefiles/GeoDBs → data/raw/land/ (ignored).
✅ Converted, simplified, normalized outputs → data/sources/land/vectors/.
🗄️ Large statewide versions → data/processed/land/ (LFS).

⸻

🧭 Vector Schema Rules
	•	Format: GeoJSON (.geojson) preferred; TopoJSON allowed for light layers
	•	CRS: EPSG:4326 (WGS84 lon/lat)
	•	Attributes:
	•	PLSS: trs_id, township, range, section
	•	Parcels: parcel_id, county, owner, year
	•	Soils: mukey, component, texture, erodibility
	•	Landcover (NLCD): class, code, year
	•	Historic vegetation: class, source, year
	•	Provenance: retain original field mappings in _meta.json
	•	Checksums: every file has .sha256

⸻

🌍 Integration Notes
	•	PLSS Grid: anchor for georeferencing plats, deeds, surveys
	•	Parcels: connect to Register of Deeds & tract book scans
	•	Soils: tie to agriculture expansion, erosion models, fertility maps
	•	Landcover: enable change detection (1992 → present); integrate with hazards
	•	Historic Vegetation: support treaty-era baseline comparisons

⸻

✅ Best Practices
	•	Convert shapefiles → GeoJSON via ogr2ogr or make vectors
	•	Simplify geometries when necessary (TopoJSON for large parcels)
	•	Maintain retrieval timestamps + checksums
	•	Add confidence flags for incomplete coverage
	•	Automate with:

make fetch land-vectors
make vectors
make stac
make validate-stac


⸻

🔍 Debugging & Validation

make validate-sources   # validate against schema
make fetch              # download raw shapefiles
make vectors            # convert → GeoJSON
make stac               # build STAC items
make validate-stac      # STAC 1.0.0 compliance
make checksums          # update .sha256 integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Land Vector Descriptors\n(data/sources/land/*.json)] -->|fetch| R[Raw Shapefiles\n(data/raw/land/)]
  R -->|convert| V[GeoJSON/TopoJSON\n(data/sources/land/vectors/)]
  V -->|index| C[STAC Items & Collections\n(stac/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> VWR[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	BLM PLSS Grid
	•	USDA NRCS SSURGO / STATSGO2 Soils
	•	NLCD (1992–2021) Land Cover Database
	•	Kansas Ecological Systems Map (2017–18 Sentinel-2)
	•	Kansas Historical Society — Historic Vegetation Maps
	•	County Assessor / Register of Deeds Parcel Data

⸻

✦ Summary

data/sources/land/vectors/ provides normalized vector layers for cadastral, soils, and land cover datasets.
They are CRS-consistent, provenance-tracked, and integrated into the STAC catalog, knowledge graph, and MapLibre viewer for Kansas frontier research.