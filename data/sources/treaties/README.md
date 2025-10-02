<div align="center">

# 📜 Kansas-Frontier-Matrix — Treaty & Land Transfer Sources  
`data/sources/treaties/`

**Mission:** Curate **treaty boundaries, land cessions, and reservation maps**  
relevant to Kansas history, making them **traceable, reproducible, and discoverable**  
in the STAC catalog, and linking them into the Frontier-Matrix **timeline + knowledge graph**.  

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

## 📊 Data Lifecycle

```mermaid
flowchart TD
  A["Raw treaty scans\n(data/sources/treaties/scans/**)"] --> B["Digitization\n(QGIS · OCR · transcription)"]
  B --> C["Vectors\n(data/sources/treaties/vectors/**)"]
  C --> D["Metadata JSON\n(data/sources/treaties/*.json)"]
  D --> E["Provenance + checksums\n(data/provenance/**)"]
  E --> F["STAC Items\n(data/stac/items/treaties/**)"]
  F --> G["Viewer integration\n(web/config/layers.json)"]
  G --> H["Knowledge Graph\n(Document ↔ Event ↔ Place ↔ Organization)"]

<!-- END OF MERMAID -->



⸻

🎯 Purpose
	•	Document the changing geography of Native American lands in Kansas
	•	Provide vector layers (GeoJSON, Shapefiles) for map overlays
	•	Link treaties to documents (scans, transcriptions, legal texts)
	•	Support timeline queries (boundary changes by year)
	•	Maintain provenance with checksums, lineage, and license details

⸻

📂 Directory Layout

data/sources/treaties/
├── treaties_1854_kansas.json        # Kansas–Nebraska Act boundaries
├── treaties_1867_medicine_lodge.json
├── tribal_cessions_index.json       # Master index of treaties/cessions
├── scans/                           # Scanned originals (PDF, TIFF, JPG)
├── vectors/                         # Digitized boundaries (GeoJSON, Shapefiles)
└── README.md

⚠️ Scans → data/raw/treaties/ (ignored by git).
✅ Processed vectors → data/processed/treaties/ (tracked via LFS).
📑 Only descriptors, checksums, metadata live here.

⸻

🧭 Metadata Schema

Each treaty dataset follows the
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "treaty_kansas_nebraska_1854",
  "title": "Kansas–Nebraska Act Treaty Boundaries (1854)",
  "type": "vector",
  "description": "Polygons representing tribal lands and cessions as defined by the 1854 Kansas–Nebraska Act.",
  "temporal": { "start": "1854-05-30", "end": "1867-10-21" },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": ["https://www.archives.gov/…/treaties/1854_kansas.pdf"]
    }
  ],
  "lineage": [
    "Scanned from NARA microfilm",
    "Digitized boundary via QGIS",
    "Saved as GeoJSON"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "abc123…"
  },
  "keywords": ["treaty", "cession", "reservation", "Kansas", "tribal lands"],
  "confidence": "high"
}

Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	temporal → explicit start/end (treaty signed, superseded)
	•	Always include license + provenance
	•	lineage → document every processing step

⸻

🌍 Recommended Sources
	•	National Archives (NARA): treaty texts & microfilm scans
	•	Kansas Historical Society: manuscripts, atlases, tribal records
	•	Library of Congress: 19th-century treaty maps
	•	Bureau of Indian Affairs (BIA): reservation boundary records
	•	Tribal archives: oral histories & community-provided boundaries

⸻

🔗 Integration Notes
	•	Treaties must be time-enabled (start/end dates per polygon)
	•	Knowledge Graph links:
	•	Document node → treaty text
	•	Event node → treaty signing date/place
	•	Place node → boundary polygon(s)
	•	Organization node → tribes, U.S. government
	•	Support story maps: timeline of cessions, guided narrative tours

⸻

✅ Best Practices
	•	Keep raw scans (scans/) separate from digitized vectors (vectors/)
	•	Record confidence scores if boundaries are approximate
	•	Reference tribal historians and oral accounts in addition to federal sources
	•	Log all edits in data/provenance/ with date + author
	•	Automate with:

make fetch treaties
make vectors
make stac
make validate-stac


⸻

📚 References
	•	STAC 1.0.0 Specification
	•	Kansas Frontier Matrix — Design Audit: Tribal Land Transfers & Treaties
	•	Historical Dataset Integration Report
	•	Kansas Historical Knowledge Hub — System Design

⸻

✦ Summary

data/sources/treaties/ defines descriptors for treaty, cession, and reservation datasets.
They ensure Kansas treaty history is digitized, time-aware, provenance-tracked, and STAC-compliant,
fully integrated into the Frontier-Matrix catalog, knowledge graph, and interactive viewer.