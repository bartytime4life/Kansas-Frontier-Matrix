<div align="center">

# 📜 Kansas-Frontier-Matrix — Treaty & Land Transfer Scanned Documents  
`data/sources/treaties/scans/`

**Mission:** Curate **scanned treaty documents, maps, and plats** (PDF, TIFF, JPG)  
so they are **traceable, reproducible, and discoverable** in the STAC catalog,  
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

- Preserve **original treaty documents and maps** (scanned PDFs, TIFFs, JPGs)  
- Provide **digitization-ready sources** for OCR, transcription, and vectorization  
- Link treaties to **legal texts, oral histories, and maps**  
- Maintain **provenance + licensing** for every scanned item  
- Enable **timeline visualization** of treaty events and land transfers  

---

## 📂 Directory Layout

```text
data/sources/treaties/scans/
├── treaty_1854_kansas.pdf         # Kansas–Nebraska Act scan
├── treaty_1867_medicine_lodge.tif # Medicine Lodge Treaty scan
├── reservation_plat_1873.jpg      # Reservation boundary plat scan
└── README.md

⚠️ Scans stored in data/raw/treaties/scans/ (ignored by git).
✅ Processed/rectified outputs → data/processed/treaties/scans/ (LFS).
📑 Only descriptors, checksums, and metadata live here.

⸻

🧭 Metadata Schema

Each scan dataset follows the
KFM Source Descriptor schema (data/sources/schema.source.json).

{
  "id": "treaty_1854_kansas",
  "title": "Kansas–Nebraska Act Treaty (1854) — Scanned Document",
  "type": "document",
  "description": "Scan of the Kansas–Nebraska Act treaty text and boundary map from 1854.",
  "temporal": { "start": "1854-05-30", "end": null },
  "spatial": { "bbox": [-102.05, 36.99, -94.61, 40.00] },
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
    "Stored as PDF/TIFF",
    "Prepared for OCR and vectorization"
  ],
  "license": "public-domain",
  "provenance": {
    "retrieved": "2025-09-21",
    "checksum_sha256": "placeholder123...",
    "filesize_bytes": null
  },
  "keywords": ["treaty", "Kansas", "scan", "cession", "reservation"],
  "confidence": "high"
}

Rules
	•	bbox → EPSG:4326 (WGS84 lon/lat)
	•	temporal → treaty signing date as start; end only if superseded
	•	Always include license + provenance
	•	lineage → document every transformation step

⸻

🌍 Recommended Sources
	•	National Archives (NARA): treaty texts & scans
	•	Kansas Historical Society (KHS): treaty manuscripts & atlases
	•	Library of Congress (LoC): treaty maps & legal atlases
	•	Bureau of Indian Affairs (BIA): reservation plats, archival scans
	•	Tribal archives: community-provided scans and oral history documents

⸻

🔗 Integration Notes
	•	Scans → digitization pipeline (OCR, transcription, boundary digitization)
	•	Link to vectors (data/sources/treaties/vectors/) and metadata JSONs
	•	Connect into knowledge graph:
	•	Document node → scan file
	•	Event node → treaty signing
	•	Place node → reservation or cession area
	•	Organization node → tribes & U.S. government

⸻

✅ Best Practices
	•	Store original scans in scans/ (unaltered TIFF/PDF/JPG)
	•	Save rectified/derived copies in data/processed/treaties/scans/
	•	Maintain .sha256 checksums + retrieved timestamps
	•	Record source + confidence in _meta.json
	•	Automate updates with:

make fetch treaties-scans
make cogs
make stac
make validate-stac


⸻

📊 Data Lifecycle

flowchart TD
  S[Treaty Scans\n(data/sources/treaties/scans/*.pdf|tif|jpg)] -->|OCR & transcription| T[Text & Metadata\n(data/sources/treaties/*.json)]
  S -->|digitize boundaries| V[Vectors\n(data/sources/treaties/vectors/)]
  V -->|index| C[STAC Items & Collections\n(stac/items/treaties/)]
  C -->|link| G[Knowledge Graph\n(Document ↔ Event ↔ Place ↔ Organization)]
  G --> VWR[MapLibre Viewer\n+ Timeline UI]

<!-- END OF MERMAID -->



⸻

📚 References
	•	National Archives — Treaties and Land Cessions (microfilm collections)
	•	Kansas Historical Society — Manuscripts & Maps
	•	Library of Congress — Treaty Atlases
	•	Bureau of Indian Affairs — Reservation Plat Records
	•	Tribal Historical Archives

⸻

✦ Summary

data/sources/treaties/scans/ defines descriptors for scanned treaty documents and maps.
These scans are preserved, provenance-tracked, and time-aware, serving as the foundation for digitization workflows,
and powering STAC catalog entries, the Frontier-Matrix knowledge graph, and interactive historical viewers.