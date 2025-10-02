<div align="center">

# 📜 Kansas-Frontier-Matrix — STAC Items (Documents)  
`data/stac/items/docs/`

**Mission:** Curate **document-based STAC Items** — treaties, scanned texts, oral histories, reports, legal filings —  
and make them **traceable, reproducible, and discoverable** in the STAC catalog.  

📌 Each Item = **one document instance** (e.g., treaty scan, PDF, transcription).  
📌 Items link **up** to the `docs.json` Collection and the **root catalog**.  
📌 Items link **out** to PDF/TIFF scans, transcriptions, or digital editions.  
📌 Items link **back** to provenance (`data/provenance/registry.json`).  

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

## 📂 Directory Layout

```text
data/stac/items/docs/
├── treaty_osage_1825.json     # Osage Treaty (1825)
├── treaty_kansas_nebraska.json# Kansas–Nebraska Act (1854)
├── flood_report_1951.json     # Kansas River Flood Report (1951)
└── README.md


⸻

🧾 Authoring Checklist (Docs Items)
	1.	STAC compliance
	•	Must conform to STAC 1.0.0.
	•	Required header:

{ "stac_version": "1.0.0", "type": "Feature", "id": "<unique_id>" }


	2.	IDs
	•	Lowercase, underscores, unique.
	•	Examples: treaty_osage_1825, flood_report_1951.
	3.	Datetime
	•	Use signing/publication date.
	•	Approximate? Use "YYYY-01-01T00:00:00Z".
	4.	Geometry + BBox
	•	Include where relevant (treaty areas, event location).
	•	CRS: EPSG:4326.
	•	For textual-only documents, use "null" geometry + Kansas-wide bbox.
	5.	Assets
	•	Scans (PDF/TIFF): application/pdf, image/tiff.
	•	Transcriptions (TXT/JSON): text/plain or application/json.
	•	Thumbnails: image/png.
	•	Every asset must include roles, title, checksum:sha256.
	6.	Links
	•	Must link to parent Collection (docs.json).
	•	Preferably link to provenance (registry.json).

⸻

📑 Example Item — Treaty Document

{
  "stac_version": "1.0.0",
  "type": "Feature",
  "id": "treaty_osage_1825",
  "collection": "docs",
  "properties": {
    "datetime": "1825-08-10T00:00:00Z",
    "license": "public-domain"
  },
  "bbox": [-102.05, 36.99, -94.61, 40.00],
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-102.05, 36.99],
      [-94.61, 36.99],
      [-94.61, 40.00],
      [-102.05, 40.00],
      [-102.05, 36.99]
    ]]
  },
  "assets": {
    "scan": {
      "href": "../../../../data/docs/treaties/treaty_osage_1825.pdf",
      "title": "Treaty with the Osage (1825) — Scan",
      "type": "application/pdf",
      "roles": ["data"],
      "checksum:sha256": "<sha256sum>"
    },
    "transcription": {
      "href": "../../../../data/docs/treaties/treaty_osage_1825.txt",
      "title": "Treaty with the Osage (1825) — Transcription",
      "type": "text/plain",
      "roles": ["metadata"],
      "checksum:sha256": "<sha256sum>"
    },
    "thumbnail": {
      "href": "../../../../media/thumbnails/treaty_osage_1825.png",
      "title": "Treaty (1825) Thumbnail",
      "type": "image/png",
      "roles": ["thumbnail"]
    }
  },
  "links": [
    { "rel": "collection", "href": "../../collections/docs.json", "type": "application/json" },
    { "rel": "derived_from", "href": "../../provenance/registry.json#treaty_osage_1825", "type": "application/json" }
  ]
}


⸻

🔗 Integration Notes
	•	Collections: All Items here belong to docs.json.
	•	Provenance: Each Item links to data/provenance/registry.json.
	•	Web Viewer: Used for popup text in MapLibre & timeline annotations.
	•	Cross-links:
	•	Document → Event (treaty signing, flood)
	•	Document → Place (reservation, floodplain)
	•	Document → Organization (tribe, government)

⸻

✅ Validation

Local

pre-commit run stac-validate --all-files

Makefile

make stac
make stac-validate

CI
	•	.github/workflows/stac-validate.yml blocks merges if invalid.

⸻

⚠️ Common Pitfalls
	•	❌ Missing checksum:sha256 for scans/transcriptions.
	•	❌ Inconsistent datetime (must be ISO8601).
	•	❌ Geometry omitted when relevant (e.g., treaty boundaries).
	•	❌ No link to Collection → breaks catalog navigation.
	•	❌ Wrong MIME types for assets.

⸻

✦ Summary

data/stac/items/docs/ contains STAC Items for Kansas historical documents — treaties, flood reports, manuscripts.
Each Item links to raw scans, transcriptions, metadata, provenance, and thumbnails, ensuring they are time-aware, provenance-tracked, and STAC-compliant.
These Items power the STAC catalog, knowledge graph, and interactive web viewer.