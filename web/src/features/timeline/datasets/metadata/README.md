---
title: "🧾 Timeline Dataset Metadata — STAC & DCAT Provenance Records (KFM-Ready)"
path: "web/src/features/timeline/datasets/metadata/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/web-timeline-datasets-metadata-v1.json"
governance_ref: "../../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🧾 **Timeline Dataset Metadata — STAC & DCAT Provenance Records**  
`web/src/features/timeline/datasets/metadata/README.md`

**Purpose:**  
Provide a consistent structure for **metadata files describing timeline datasets** (PMTiles, GeoJSON, or raster assets).  
Ensures compliance with **STAC 1.0**, **DCAT 3.0**, and **FAIR+CARE governance**, providing clear provenance, licensing, and temporal-spatial context for every KFM dataset.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Certified-orange)](../../../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

Each file in this directory (`*.json`) represents a **metadata record** for a timeline dataset under `web/src/features/timeline/datasets/`.  
These records follow the **SpatioTemporal Asset Catalog (STAC)** and **DCAT** standards, enabling discoverability, reproducibility, and ethical governance.

**Why it matters**
- 🧭 Enables interoperability with geospatial catalogs and FAIR data portals.  
- 🔐 Guarantees provenance, attribution, and licensing for all timeline data.  
- ⚙️ Supports STAC/DCAT → Neo4j graph ingestion and audit tracking.  
- 🌎 Used by MapLibre timeline and AI Focus Mode for dataset context and citation.

---

## 🗂️ Directory Layout

```plaintext
web/src/features/timeline/datasets/metadata/
├─ README.md               # This file — Metadata overview and schema
├─ settlements.json        # Settlements (1700–2025)
├─ hydrology.json          # Hydrological datasets (rivers, floods)
├─ landcover.json          # Land cover transitions
├─ ownership.json          # Land ownership & grants
└─ species.json            # Biodiversity / species range datasets
```

---

## 🧩 Metadata Template (STAC/DCAT Hybrid)

```json
{
  "id": "settlements-v2025",
  "type": "Feature",
  "stac_version": "1.0.0",
  "dcat_version": "3.0",
  "title": "Kansas Settlements (1700–2025)",
  "description": "Spatial dataset of Kansas settlements over time with attributes for start/end year, population, and class.",
  "license": "CC-BY 4.0",
  "keywords": ["settlements", "Kansas", "timeline", "historical geography"],
  "providers": [
    { "name": "Kansas Historical Society", "roles": ["producer"] },
    { "name": "Kansas Frontier Matrix", "roles": ["processor", "publisher"] }
  ],
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.6, 40.0]] },
    "temporal": { "interval": [["1700-01-01T00:00:00Z", "2025-12-31T00:00:00Z"]] }
  },
  "assets": {
    "pmtiles": {
      "href": "pmtiles://datasets/settlements.pmtiles",
      "type": "application/vnd.pmtiles",
      "roles": ["data"]
    },
    "thumbnail": {
      "href": "/assets/thumbs/settlements.png",
      "type": "image/png",
      "roles": ["preview"]
    }
  },
  "links": [
    {
      "rel": "derived_from",
      "href": "https://www.kshs.org/",
      "title": "Kansas Historical Society Archives"
    },
    {
      "rel": "license",
      "href": "https://creativecommons.org/licenses/by/4.0/"
    }
  ],
  "checksum:sha256": "abcd1234...",
  "created": "2025-11-07T00:00:00Z",
  "mcp_metadata": {
    "governance": { "care_tag": "public", "ethical_review": "approved" },
    "data_contract_ref": "docs/contracts/data-contract-v3.json",
    "sbom_ref": "releases/v9.9.0/sbom.spdx.json"
  }
}
```

---

## ⚙️ Metadata Validation

Each record is validated by CI against:
1. **STAC schema** (`stac-item-spec.json`)  
2. **DCAT JSON schema** (`dcat-dataset-v3.json`)  
3. **KFM timeline metadata schema** (`web-timeline-datasets-metadata-v1.json`)  

**Validation workflow:**  
`.github/workflows/stac-validate.yml` → outputs `reports/validation/stac_summary.json`.

> ✅ Valid metadata guarantees dataset discoverability, licensing clarity, and temporal alignment.

---

## 🧱 Required Fields

| Field | Description | Standard | Required |
|-------|--------------|-----------|-----------|
| `id` | Unique dataset identifier | STAC/DCAT | ✅ |
| `title` | Human-readable name | STAC/DCAT | ✅ |
| `description` | Summary of dataset contents | DCAT | ✅ |
| `extent.spatial.bbox` | Bounding box (WGS84) | STAC | ✅ |
| `extent.temporal.interval` | Time coverage range | STAC | ✅ |
| `license` | Usage license or legal status | STAC/DCAT | ✅ |
| `assets.pmtiles.href` | Path to PMTiles or dataset file | STAC | ✅ |
| `checksum:sha256` | Dataset integrity hash | KFM extension | ✅ |
| `mcp_metadata.governance.care_tag` | Ethical classification (public/restricted/sensitive) | FAIR+CARE | ✅ |

---

## 🧠 FAIR+CARE Governance

Metadata records encode **ethical stewardship** and **cultural protection**.  
Each dataset includes a `care_tag` that dictates its access and rendering policy:

| Tag | Meaning | UI Behavior |
|-----|----------|-------------|
| `public` | Fully accessible, no restrictions. | Visible by default. |
| `restricted` | Requires authentication or approval. | Dimmed / masked in UI. |
| `sensitive` | Hidden; accessible only to council-approved users. | Omitted from public maps. |

All tags are enforced by the frontend via governance middleware and validated in CI.

---

## 🧾 Citation Block (auto-generated)

Example output used by Focus Mode and Timeline legends:

```text
Dataset: Kansas Settlements (1700–2025) · CC-BY 4.0  
Source: Kansas Historical Society · Processed by KFM · Bounding Box: -102.05,36.99 → -94.6,40.0  
Temporal Coverage: 1700–2025 · DOI: N/A  
Checksum (SHA-256): abcd1234...  
FAIR+CARE Tag: Public
```

---

## 🧩 Example Integration (MapLibre + Metadata)

Metadata JSONs can be read dynamically to build map sources:

```ts
import meta from './metadata/settlements.json';

map.addSource('settlements', {
  type: 'vector',
  url: meta.assets.pmtiles.href
});

console.log(`Loaded ${meta.title} (${meta.extent.temporal.interval[0].join(' → ')})`);
```

---

## 🔍 Governance & Telemetry Hooks

When a dataset loads, KFM logs its metadata into `focus-telemetry.json` for reproducibility:

```json
{
  "event": "dataset-load",
  "dataset_id": "settlements-v2025",
  "timestamp": "2025-11-08T12:01:00Z",
  "user": "public",
  "governance": "public",
  "status": "ok"
}
```

Telemetry records align with the schema:  
`schemas/telemetry/web-timeline-datasets-metadata-v1.json`.

---

## 🧪 Validation Checklist

- [x] File name matches dataset (e.g., `settlements.pmtiles` → `settlements.json`)  
- [x] Includes spatial + temporal extent  
- [x] Includes checksum & license link  
- [x] Contains CARE tag in governance block  
- [x] CI passes `stac-validate.yml`  

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|--------:|------------|--------|----------|
| v9.9.0  | 2025-11-08 | `@kfm-web` | Added metadata schema & governance structure for timeline datasets. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Metadata Provenance × FAIR+CARE Governance × Sustainable Architecture*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Dataset Docs](../README.md) · [Timeline Docs](../../README.md) · [Governance Charter](../../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

