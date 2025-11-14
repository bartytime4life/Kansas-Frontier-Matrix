---
title: "🛰️ Kansas Frontier Matrix — STAC Pipelines Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/stac/README.md"
version: "v10.3.1"
last_updated: "2025-11-14"
review_cycle: "Quarterly · FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-stac-overview-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — STAC Pipelines Overview**  
`src/pipelines/stac/README.md`

**Purpose:**  
Provide the top-level architecture, directory structure, standards, FAIR+CARE governance requirements, and telemetry integration for all **STAC-related pipelines** within the Kansas Frontier Matrix (KFM).  
This includes monitoring, validation, normalization, publishing, lineage capture, and governance-linked storage of STAC Items and Collections.

<img alt="STAC" src="https://img.shields.io/badge/STAC-1.0_Compliant-blue"/>
<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Enforced-orange"/>
<img alt="Telemetry" src="https://img.shields.io/badge/Telemetry-Linked-green"/>
<img alt="Status" src="https://img.shields.io/badge/Status-Active-success"/>

</div>

---

## 📘 Overview

KFM STAC pipelines provide:

- **Continuous ingestion** of STAC Items from NOAA/USGS/NASA/other providers  
- **Conditional polling** using HTTP ETag / If-None-Match  
- **Great Expectations validation** with schema + semantic rules  
- **FAIR+CARE governance enforcement** and sovereignty safety checks  
- **Normalization and augmentation** into KFM-compliant STAC metadata  
- **Immutable publishing** to the KFM STAC catalog  
- **Neo4j graph hydration** for Scenes, Datasets, Themes  
- **Telemetry logging** (operational + sustainability + CARE signals)

These pipelines form the backbone of the geospatial ingestion layer for the Kansas Frontier Matrix.

---

## 🗂️ Directory Layout (Authoritative)

~~~~~text
src/pipelines/stac/
├── README.md
│
├── monitor-validate-publish/        # STAC ingestion orchestrator (poll → validate → publish)
│   ├── README.md
│   ├── monitor.py
│   ├── publish.py
│   ├── transform.py
│   ├── etag_cache.json
│   ├── expectations/
│   │   ├── great_expectations.yml
│   │   ├── checkpoints/
│   │   └── expectations/
│   ├── data/
│   │   ├── incoming/
│   │   ├── quarantine/
│   │   ├── published/
│   │   ├── geometry/
│   │   └── telemetry/
│   └── .github/
│       ├── README.md
│       └── workflows/
│           └── README.md
│
└── utils/                           # Optional helpers for STAC filtering, merging, metadata extension
    ├── stac_helpers.py
    ├── asset_tools.py
    └── metadata_tools.py
~~~~~

---

## 🧩 High-Level Pipeline Architecture

~~~~~mermaid
flowchart TD
  A["STAC Provider API<br/>Item Search"] --> B["Monitor.py<br/>ETag Polling"]
  B -->|304| Z["No Change · Telemetry Only"]
  B -->|200| C["Incoming Batch<br/>data/incoming/**"]
  C --> D["Validation Gate<br/>Great Expectations"]
  D -->|FAIL| Q["Quarantine<br/>data/quarantine/**"]
  D -->|PASS| E["Normalize<br/>transform.py"]
  E --> F["Publish<br/>data/published/**"]
  F --> G["Hydrate Neo4j<br/>Scenes · Datasets · Themes"]
  G --> H["Telemetry Export<br/>JSONL → focus-telemetry.json"]
  Q --> H
~~~~~

---

## ⚙️ Pipeline Responsibilities

### 1. **monitor.py**
- Poll STAC API Item Search  
- Use **ETags** for conditional requests  
- Write raw batches to `data/incoming/`  
- Emit telemetry (fetch count, 304 status, latency, CO₂e, energy)

### 2. **Great Expectations Validation**
Validates:

- Schema  
- Link relation correctness  
- Projection metadata  
- Cloud cover / sensor ranges  
- CARE label presence  
- Sovereignty intersection checks  
- KFM metadata compliance

### 3. **transform.py**
- Normalize STAC Items (datetime, roles, MIME types)  
- Inject KFM metadata (`kfm:*` fields)  
- Fix broken hrefs  
- Add ingest version and provenance skeletons  
- Apply CARE masking (if needed)

### 4. **publish.py**
- Write immutable STAC Collections & Items  
- Ensure SemVer versioning for dataset roots  
- Hydrate Neo4j graph nodes/relationships  
- Emit publishing telemetry

### 5. **Governance**
- Quarantine failures  
- Sovereignty / tribal territory checks  
- CARE restrictions  
- Provenance completeness  
- Versioning ledger updates  

---

## 📦 Storage Model

### Incoming (untrusted)

~~~~~text
data/stac/incoming/<timestamp>/items.jsonl
~~~~~

### Quarantine (blocked)

~~~~~text
data/stac/quarantine/<timestamp>/
~~~~~

### Published (immutable)

~~~~~text
data/stac/published/collections/<collection>.json
data/stac/published/items/<collection>/<item>.json
~~~~~

### Geometry (authoritative AOI)

~~~~~text
data/geometry/kansas_aoi.geojson
~~~~~

### Telemetry

~~~~~text
data/telemetry/<timestamp>.jsonl
../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🧠 FAIR+CARE Governance Rules

### Required for ALL STAC Items/Collections:

- `kfm:care_label`  
- `kfm:checksum`  
- `kfm:ingest_version`  
- `kfm:provenance`  
- Masking rules for sensitive datasets  
- Sovereignty notes (if applicable)  
- No unmasked archaeological/cultural points  

### Governance ledgers impacted:

~~~~~text
docs/reports/audit/versioning_ledger.json
docs/reports/audit/data_provenance_ledger.json
docs/reports/fair/data_care_assessment.json
~~~~~

---

## 📡 Telemetry Specification

Each orchestrator run logs:

- STAC polling counts  
- Schema/CARE failures  
- Publish counts  
- Graph hydration success  
- ETag behavior  
- Energy usage (Wh)  
- Carbon emissions (gCO₂e)  
- Governance status  

Telemetry aggregated into:

~~~~~text
../../../releases/v10.3.0/focus-telemetry.json
~~~~~

---

## 🛠️ Tools & Dependencies

Required Python libs:

~~~~~text
requests
jsonschema
great-expectations
neo4j
shapely
h3
~~~~~

Optional:

- geopandas  
- rasterio (for asset inspection)  
- planetary-computer SDKs  

---

## 🧪 Local Development

~~~~~bash
python src/pipelines/stac/monitor-validate-publish/monitor.py
great_expectations checkpoint run stac_items \
  --config src/pipelines/stac/monitor-validate-publish/expectations/great_expectations.yml \
  --suite stac_item_suite
python src/pipelines/stac/monitor-validate-publish/publish.py
~~~~~

---

## 🕰️ Version History

| Version | Date       | Author | Summary |
|---------|------------|--------|---------|
| v10.3.1 | 2025-11-14 | STAC Pipelines Team | Complete top-level STAC pipeline overview; aligned with FAIR+CARE, telemetry v1, and orchestrator updates. |

---

<div align="center">

**Kansas Frontier Matrix — STAC Pipelines Overview**  
Continuous Ingestion × Immutable Publishing × FAIR+CARE Governance × Telemetry Provenance  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

</div>
