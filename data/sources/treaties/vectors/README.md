<div align="center">

# 🧩 Kansas-Frontier-Matrix — Treaty & Land Transfer Vector Datasets  
`data/sources/treaties/vectors/`

**Mission:** Curate **digitized treaty, cession, and reservation boundaries** in vector form  
(GeoJSON, Shapefiles, TopoJSON), ensuring they are **traceable, reproducible, and discoverable**  
in the STAC catalog, and linked into the Frontier-Matrix **timeline + knowledge graph**.  

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

- Provide **digitized boundaries** of treaties, land cessions, and reservations  
- Store **canonical GeoJSON/TopoJSON outputs** for direct web + GIS integration  
- Maintain **temporal attributes** (start/end years, treaty signing dates)  
- Support **story maps and timeline queries**  
- Enable **cross-links** to treaty scans, documents, and oral histories  

---

## 📂 Directory Layout

```text
data/sources/treaties/vectors/
├── treaty_kansas_nebraska_1854.geojson     # Digitized 1854 Kansas–Nebraska Act cession boundaries
├── treaty_medicine_lodge_1867.geojson      # 1867 Medicine Lodge treaty polygons
├── tribal_reservations.geojson             # Reservation boundaries (historic + modern)
├── cessions_master_index.geojson           # Unified overlay of all cessions
└── README.md

⚠️ Raw scans → data/sources/treaties/scans/ (ignored by git).
✅ Digitized vectors → data/sources/treaties/vectors/.
🗄️ Large/lossless formats (original shapefiles, GeoPackages) → data/processed/treaties/ (LFS).

⸻

🧭 Vector Schema Rules
	•	Format: GeoJSON (.geojson) preferred; TopoJSON for lightweight rendering
	•	CRS: EPSG:4326 (WGS84 lon/lat)
	•	Attributes:
	•	treaty_id → unique identifier (e.g., 1854_kansas_nebraska)
	•	tribe → tribal nation(s) affected
	•	event_date → treaty signing date
	•	valid_until → supersession/end date
	•	source → archival reference (NARA, KHS, LoC, BIA, tribal records)
	•	confidence → high, medium, or low (boundary precision)
	•	Metadata: Original source references + digitization notes stored in _meta.json
	•	Checksums: Every file has .sha256 integrity record

⸻

🌍 Integration Notes
	•	Vectors must be time-enabled for the Frontier-Matrix timeline
	•	Cross-link nodes:
	•	Document → treaty scans, legal text
	•	Event → signing, ratification, land transfer
	•	Place → boundary polygons
	•	Organization → tribal nations, U.S. government
	•	Layers power story maps + narrative tours (e.g., Kansas land transfers 1825–1870)
	•	Overlay with settlement, hazards, and land cover for correlation studies

⸻

✅ Best Practices
	•	Convert shapefiles → GeoJSON via ogr2ogr or pipeline scripts
	•	Simplify geometries for large statewide datasets (TopoJSON for web performance)
	•	Keep retrieved timestamps + provenance logs current
	•	Record uncertainty + oral history references in metadata
	•	Automate updates with:

make fetch treaties-vectors
make vectors
make stac
make validate-stac


⸻

🔍 Debugging & Validation

make validate-sources   # schema compliance
make fetch              # download raw shapefiles/vectors
make vectors            # convert → GeoJSON
make stac               # build STAC items
make validate-stac      # validate STAC 1.0.0
make checksums          # update .sha256 integrity files


⸻

📊 Data Lifecycle

flowchart TD
  S[Treaty Descriptors\n(data/sources/treaties/*.json)] -->|fetch| R[Raw Scans\n(data/sources/treaties/scans/)]
  R -->|digitize| V[Digitized Vectors\n(data/sources/treaties/vectors/)]
  V -->|index| C[STAC Items & Collections\n(stac/items/treaties/)]
  C -->|link| G[Knowledge Graph\n(Neo4j + Ontologies)]
  G --> VWR[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	National Archives (NARA) — treaty texts & maps
	•	Kansas Historical Society — county plat books, atlases
	•	Library of Congress — treaty atlases and 19th-century maps
	•	Bureau of Indian Affairs (BIA) — reservation boundary datasets
	•	Tribal archives — oral histories & community maps

⸻

✦ Summary

data/sources/treaties/vectors/ contains digitized treaty and land transfer boundaries for Kansas.
These layers are schema-compliant, CRS-normalized, and provenance-tracked, powering STAC catalog entries, the Frontier-Matrix knowledge graph, and interactive viewer.