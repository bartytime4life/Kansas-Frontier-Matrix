---
title: "🗺️ Timeline Datasets — PMTiles & Temporal Layers (KFM-Ready)"
path: "web/src/features/timeline/datasets/README.md"
version: "v9.9.0"
last_updated: "2025-11-08"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v9.9.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v9.9.0/manifest.zip"
telemetry_ref: "../../../../releases/v9.9.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/web-timeline-datasets-v1.json"
governance_ref: "../../../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
---

<div align="center">

# 🗺️ **Timeline Datasets — PMTiles & Temporal Layers**  
`web/src/features/timeline/datasets/README.md`

**Purpose:**  
Describe the **data sources, file structure, and temporal design** for all **timeline-driven datasets** used in MapLibre visualizations.  
These layers support **year-aware filtering**, **animated transitions**, and **FAIR+CARE compliant metadata** across KFM’s **interactive timeline system**.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../../../../../docs/)
[![License](https://img.shields.io/badge/License-MIT-green)](../../../../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR+CARE-Validated-orange)](../../../../../docs/standards/)
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen)](#)

</div>

---

## 📘 Overview

Timeline datasets represent **spatial features evolving through time**.  
Each layer is stored as **PMTiles** or **vector tiles** and includes **temporal fields** (e.g., `year_start`, `year_end`, `epoch`).  
These layers allow the **timeline slider** to reveal changes in settlements, rivers, land use, ownership, and biodiversity.

### Core Goals
- 🧩 Unified schema for all temporal datasets.  
- ⚙️ Optimized for **MapLibre** streaming with **PMTiles** protocol.  
- 🛰️ Linked to **STAC/DCAT** metadata for provenance.  
- 🧠 Ready for **AI-driven Focus Mode** and FAIR+CARE audits.  

---

## 🗂️ Directory Layout

```plaintext
web/src/features/timeline/datasets/
├─ README.md                # This file — dataset overview & data contract
├─ settlements.pmtiles      # Settlements (1700–2025)
├─ hydrology.pmtiles        # Water systems & changes over time
├─ landcover.pmtiles        # Vegetation & land use transitions
├─ ownership.pmtiles        # Parcel & land grant history (BLM / GLO)
├─ species.pmtiles          # Wildlife migration & range changes
└─ metadata/
   ├─ settlements.json      # FAIR+CARE metadata
   ├─ hydrology.json
   ├─ landcover.json
   ├─ ownership.json
   └─ species.json
```

---

## 🧩 Dataset Summary

| Dataset | Description | Source | Temporal Coverage | Key Fields |
|---------|--------------|---------|------------------|------------|
| **settlements.pmtiles** | Historical settlement points & growth phases. | Kansas GIS Archive · KHS | 1700–2025 | `year_start`, `year_end`, `epoch`, `class` |
| **hydrology.pmtiles** | Historical rivers, lakes, and flood extents. | USGS NHD · NOAA | 1850–2025 | `year`, `epoch`, `flow_class` |
| **landcover.pmtiles** | Land cover transitions (prairie → agriculture). | NASA · NLCD · Kansas DASC | 1800–2020 | `year`, `class`, `area_ha` |
| **ownership.pmtiles** | Homesteads, railroads, and land transfers. | BLM GLO · Treaties DB | 1854–2020 | `grant_year`, `sold`, `owner_type` |
| **species.pmtiles** | Animal & plant distribution by era. | GBIF · eBird · KBS | 1800–2025 | `range_year`, `species`, `status` |

---

## 🧱 Temporal Schema (shared)

| Field | Type | Required | Description |
|-------|------|-----------|--------------|
| `year_start` | integer | ✅ | First active year of feature (inclusive). |
| `year_end` | integer | — | Last active year (inclusive, default `9999`). |
| `year` | integer | — | Snapshot or measurement year. |
| `epoch` | string | — | Era label (e.g., `pre1850`, `1900s`, `modern`). |
| `class` | string | — | Category or type (e.g., landcover, ownership). |
| `status` | string | — | For biological or ownership datasets (e.g., `active`, `extinct`, `sold`). |
| `source` | string | — | Provenance identifier (agency, dataset). |
| `license` | string | — | Data license (inherited from STAC/DCAT record). |

> *Validation:* enforced by ETL pipeline in `src/pipelines/validation/timeline-schema.json`.

---

## 🛰 STAC/DCAT Integration

Each dataset has a paired **metadata JSON** file (under `metadata/`) generated from STAC/DCAT exports.  
These include dataset lineage, checksum, bounding boxes, and versioning for reproducibility.

Example (`metadata/settlements.json`):

```json
{
  "id": "settlements-v2025",
  "title": "Kansas Settlements (1700–2025)",
  "license": "CC-BY 4.0",
  "stac_version": "1.0.0",
  "extent": {
    "spatial": { "bbox": [[-102.05, 36.99, -94.6, 40.0]] },
    "temporal": { "interval": [["1700-01-01T00:00:00Z", "2025-12-31T00:00:00Z"]] }
  },
  "assets": {
    "pmtiles": {
      "href": "pmtiles://datasets/settlements.pmtiles",
      "type": "application/vnd.pmtiles",
      "roles": ["data"]
    }
  },
  "checksum:sha256": "abcd1234...",
  "created": "2025-11-07T00:00:00Z"
}
```

---

## ⚙️ PMTiles & Protocol Setup

**Register PMTiles protocol once:**

```ts
import { Protocol } from 'pmtiles';
import maplibregl from 'maplibre-gl';
const protocol = new Protocol();
maplibregl.addProtocol('pmtiles', protocol.tile);
```

**Recommended tile settings:**
- Tile compression: gzip or brotli  
- Zoom range: `5–14` (auto-simplify beyond 14)
- Attribute index: include `year_start`, `year_end`, `epoch`  
- Tile size: ≤ 512 px  

> PMTiles sources defined in `timeline-style.json` for consistent referencing.

---

## 🧠 Focus Mode Integration

Timeline datasets feed **AI Focus Mode** by providing:
- Temporal context (year range) for narrative synthesis.  
- Spatial relations (e.g., “events near Fort Larned in 1867”).  
- Provenance references for ethical summarization.  

Each tile’s features are queryable by year range via:
```ts
map.queryRenderedFeatures({ filter: ["<=", ["get","year_start"], currentYear] });
```

Focus summaries automatically include dataset citations from metadata JSON.

---

## ♿ Accessibility & FAIR+CARE

| Aspect | Requirement | Implementation |
|--------|-------------|----------------|
| **Ethics** | Indigenous and sensitive data masked by governance role. | CARE layer tags in metadata. |
| **Accessibility** | Datasets available via open PMTiles and CSV fallback. | Download links in UI. |
| **Transparency** | Every dataset linked to its source STAC item. | UI tooltip + metadata modal. |
| **Reproducibility** | Each build logs checksums + version. | SBOM reference per dataset. |

---

## 🧪 Validation & Telemetry

**CI checks**
- Schema validation (`timeline-schema.json`)
- Metadata linkage (STAC/DCAT consistency)
- Performance metrics (tile load time, memory footprint)
- Governance checks (license, care_tag)

**Telemetry fields**
```json
{
  "dataset": "settlements",
  "tile_load_ms": 42,
  "visible_features": 13894,
  "active_year": 1880,
  "zoom": 8,
  "fps": 59.4
}
```
Logged to: `releases/v9.9.0/focus-telemetry.json`

---

## 🧾 Internal Citation

```text
Kansas Frontier Matrix (2025). Timeline Datasets — PMTiles & Temporal Layers (v9.9.0).
FAIR+CARE and MCP-DL v6.3 compliant geospatial layers for interactive timeline visualization.
```

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|--------:|------------|--------|----------|
| v9.9.0 | 2025-11-08 | `@kfm-web` | Added dataset documentation for PMTiles-based temporal layers. |

---

<div align="center">

**Kansas Frontier Matrix**  
*Temporal Data × FAIR+CARE Compliance × Sustainable Design*  
© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[Back to Timeline Docs](../README.md) · [Web Features Index](../../README.md) · [Governance Charter](../../../../docs/standards/governance/DATA-GOVERNANCE.md)

</div>

