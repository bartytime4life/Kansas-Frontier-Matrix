---
title: "🧰 KFM v11 — Autonomous Pipeline Utilities (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/autonomous/utils/README.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Daily · Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/telemetry/autonomous-pipelines.json"
telemetry_schema: "../../../../schemas/telemetry/autonomous-utils-v1.json"
governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
data_contract_ref: "../../../../docs/contracts/data-contract-v3.json"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Module"
semantic_document_id: "kfm-autonomous-utils-v11"
doc_uuid: "urn:kfm:pipelines:autonomous:utils:v11"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
immutability_status: "version-pinned"
---

<div align="center">

# 🧰 **Autonomous Pipeline Utilities (v11)**  
`src/pipelines/autonomous/utils/README.md`

**Purpose:**  
Provide the shared utility modules powering all **Autonomous KFM v11 pipelines**, including hydrology, climate, hazards, and future autonomous ingestion systems.  
These utilities enforce **deterministic ETL**, **OpenLineage**, **STAC correctness**, **checksum integrity**,  
and **Neo4j-safe graph writes** across the entire autonomous micro-pipeline ecosystem.

</div>

---

# 📘 Overview

This module contains **core, reusable utilities** used across all autonomous pipeline DAGs:

- Lineage emission (OpenLineage v2.5)  
- Checksum management (SHA-256, multihash)  
- STAC building & validation helpers (STAC 1.0 + KFM extensions)  
- Neo4j write/sync utilities  
- Cloud + HTTP helpers (etag, last-modified)  
- File system & manifest helpers  
- JSON/Parquet normalization helpers  

These utilities must remain:

- Deterministic  
- Side-effect minimal  
- Documented with MCP-DL v6.3  
- Aligned with KFM-MDP v11.0.0  
- CI-validated and schema-safe  

---

# 🗂 Directory Layout (v11)

```text
src/pipelines/autonomous/utils/
│
├── README.md                    # This file
│
├── lineage.py                   # OpenLineage event helpers
├── stac_tools.py                # STAC Item/Collection builders + validation
├── checksum_tools.py            # SHA-256 generation, manifest diffing
├── neo4j_tools.py               # Safe graph writes (CIDOC-CRM + GeoSPARQL mappings)
├── file_io.py                   # HTTP fetch, ETag/Last-Modified checks, retries
├── json_tools.py                # JSON normalization, safe writes
└── parquet_tools.py             # Parquet normalization, stable schema enforcement
```

---

# 🧬 Utility Responsibilities (v11)

## 🛰 lineage.py  
Implements:

- `emit_start`, `emit_complete`, `emit_failure`  
- Namespace: `kfm.autonomous.<pipeline>`  
- Supports OpenLineage 2.5 Job/Run events  
- Ensures deterministic provenance blocks:  
  - `prov:activity`  
  - `prov:generatedAtTime`  
  - `prov:wasAssociatedWith`  

---

## 🗂 stac_tools.py

Provides:

- STAC Item/Collection constructors  
- KFM **geo**, **vertical-axis**, **hydrology**, **heritage**, and **checksum** extensions  
- Required STAC validation wrapper  
- Helpers for bbox, geometry, datetime, temporal intervals  
- JSON-LD context injection  
- Automatic PROV-O lineage embedding

---

## 🔐 checksum_tools.py

Functions:

- `sha256(file)`  
- Compare file hashes against `manifest.json`  
- Build/update manifest (if policy allows)  
- Multi-hash support for STAC assets  
- CI-safe diff mode

---

## 🧠 neo4j_tools.py

Responsibilities:

- Create/update nodes for:  
  - STAC Items  
  - Collections  
  - Entities (People, Places, Events, Datasets)  
- Apply KFM mapping rules:  
  - **CIDOC-CRM**: E7 Activity, E53 Place, E52 Time-Span  
  - **GeoSPARQL**: geometry → WKT literal  
  - **OWL-Time**: interval mapping  
- Refresh graph indexes (spatial + temporal)  
- Produce graph write telemetry

---

## 📥 file_io.py

Provides:

- HTTP GET with retries  
- ETag + Last-Modified extraction  
- Conditional fetching  
- Timeouts + exponential backoff  
- Safe local writes  
- Provider declaration compliance

---

## 📦 json_tools.py

Tools for:

- Stable JSON dumps (sorted keys, UTF-8)  
- Safe atomic file writes  
- JSON schema validation  
- Deep-merge utilities for metadata blocks  

---

## 📐 parquet_tools.py

Provides:

- Normalized Parquet schema enforcement  
- Column type validation  
- Nullability contract enforcement  
- Deterministic ordering of columns  
- Compression: ZSTD or Snappy

---

# 🔍 CI/CD Requirements

All utilities must pass:

- **pylint + mypy**  
- **pytest** (unit + smoke)  
- **schema-lint** (`*.schema.json`)  
- **OpenLineage event integrity**  
- **KFM lineage validator**  
- **STAC 1.0 validator**  
- **Deterministic serialization tests**  

Any utility update triggers CI rebuild for **all pipelines** using this module.

---

# 🧭 Integration in Autonomous Pipelines

Used by:

- `hydrology-refresh`  
- `climate-refresh`  
- `hazards-refresh`  
- Future wildfire, sediment, or atmospheric pipelines  

Utilities ensure:

- Consistent STAC generation  
- Reproducible transformations  
- Self-healing pipeline execution  
- Distributed daily autonomous operation  

---

# 🕰 Version History

- **v11.0.0 (2025-11-22)** — Initial utilities module under KFM v11.

---

<div align="center">

**Kansas Frontier Matrix — Autonomous Pipeline Utilities (v11)**  
*Shared · Deterministic · Provenance-Driven*

</div>

---

### 🔗 Footer  
[⬅ Back to Autonomous Pipelines](../README.md) · [🔁 Hydrology Refresh](../hydrology-refresh/README.md) · [🏛 Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

