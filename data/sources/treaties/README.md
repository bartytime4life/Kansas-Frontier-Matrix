<div align="center">

# 📜 Kansas Geo Timeline — Treaty & Land Transfer Sources

This directory stores **treaty boundaries, land cessions, and reservation maps**  
relevant to Kansas history.  

These layers connect **documents** (treaty texts, oral histories, legal records)  
with **geospatial features** (boundary polygons, dates, attributes).  

[![Build & Deploy](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/site.yml)
[![STAC Validate](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/stac-badges.yml)
[![Pre-commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/bartytime4life/Kansas-Frontier-Matrix/.pre-commit-config.yaml)

</div>

---

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
	•	Document the changing geography of Native American lands in Kansas.
	•	Provide vector layers (GeoJSON, Shapefiles) for map overlays.
	•	Link treaties to source documents (scans, transcriptions, legal texts).
	•	Support timeline queries (e.g., boundary changes by year).
	•	Maintain provenance with checksums and license details.

⸻

📂 Directory layout

data/sources/treaties/
├── treaties_1854_kansas.json        # Kansas–Nebraska Act boundaries
├── treaties_1867_medicine_lodge.json
├── tribal_cessions_index.json       # Master index of treaties/cessions
├── scans/                           # Scanned originals (PDF, TIFF, JPG)
├── vectors/                         # Digitized boundaries (GeoJSON, Shapefiles)
└── README.md


⸻

🧭 Metadata requirements

Each treaty dataset (.json or .yml) follows a STAC-like schema:

{
  "id": "treaty_kansas_nebraska_1854",
  "title": "Kansas–Nebraska Act Treaty Boundaries (1854)",
  "type": "vector",
  "description": "Polygons representing tribal lands and cessions as defined by the 1854 Kansas–Nebraska Act.",
  "temporal": {
    "start": "1854-05-30",
    "end": "1867-10-21"
  },
  "spatial": {
    "bbox": [-102.05, 36.99, -94.61, 40.00]
  },
  "endpoints": [
    {
      "type": "http",
      "role": ["source"],
      "urls": [
        "https://www.archives.gov/…/treaties/1854_kansas.pdf"
      ]
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
  }
}


⸻

📚 Recommended sources
	•	National Archives (NARA) — treaty texts & microfilm scans.
	•	Kansas Historical Society — manuscripts, tribal records.
	•	Library of Congress — 19th-century treaty maps.
	•	Bureau of Indian Affairs (BIA) — reservation boundary records.
	•	Tribal archives — oral histories & community-provided boundaries.

⸻

🔗 Integration notes
	•	Treaties must be time-enabled (start/end dates per polygon).
	•	Link into the Knowledge Graph:
	•	Document node → treaty text.
	•	Event node → treaty signing.
	•	Place node → boundary polygon.
	•	Organization node → tribes, U.S. government.
	•	Support story map layers (timeline of land transfers, narrative tours).

⸻

📝 Best practices
	•	Keep raw scans (scans/) separate from digitized vectors (vectors/).
	•	Record confidence scores if boundaries are approximate.
	•	Reference tribal historians and oral accounts, not only federal records.
	•	Log every edit in data/provenance/.

⸻

📚 References
	•	STAC 1.0.0 Specification
	•	Kansas Frontier Matrix — Design Audit: Tribal Land Transfers & Treaties
	•	Historical Dataset Integration Report
	•	Kansas Historical Knowledge Hub — System Design

⸻

✅ Mission-grade principle: Treaty datasets must be traceable, time-aware, and STAC-linked,
integrating documents, maps, and oral histories into a reproducible knowledge system.

