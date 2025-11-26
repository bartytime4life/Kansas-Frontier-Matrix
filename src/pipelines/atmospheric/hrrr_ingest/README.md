---
title: "🌪️ Kansas Frontier Matrix — HRRR Atmospheric Data Ingestion (Herbie + GRIB2 → Xarray → Zarr/COG) · v11.2"
path: "src/pipelines/atmospheric/hrrr_ingest/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Working Group"
content_stability: "stable"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

commit_sha: "<latest>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.0/focus-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/hrrr-ingest-v11.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

doc_kind: "Pipeline Module"
intent: "atmospheric-hrrr-ingest"
category: "Pipelines · Atmospheric · HRRR · Ingestion"

fair_category: "F1-A1-I2-R1"
care_label: "CARE: Ethical Spatial Stewardship"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
sensitivity: "Environmental/atmospheric; minimal cultural intersection; CARE screen applies when cross-linked with heritage layers."
risk_category: "Low"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "src/pipelines/atmospheric/hrrr_ingest/README.md@v11.1.0"
  - "HRRR ingestion prototypes v10.x"
  - "NOAA HRRR archive documentation"
  - "Atmospheric Working Group v11 notes"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true

json_schema_ref: "../../../../../schemas/json/atmospheric-hrrr-ingest-v11.schema.json"
shape_schema_ref: "../../../../../schemas/shacl/atmospheric-hrrr-ingest-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
requires_version_history: true

doc_uuid: "urn:kfm:doc:pipelines:atmospheric:hrrr-ingest:v11.2.0"
semantic_document_id: "kfm-atmospheric-hrrr-ingest"
event_source_id: "ledger:src/pipelines/atmospheric/hrrr_ingest/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

classification: "Public Document"
jurisdiction: "Kansas / United States"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by atmospheric-hrrr-ingest-v12"
---

<div align="center">

# 🌪️ **HRRR Atmospheric Data Ingestion Module**  
Herbie · GRIB2 · Xarray · Zarr/COG  
`src/pipelines/atmospheric/hrrr_ingest/README.md`

[![Atmosphere](https://img.shields.io/badge/Domain-Atmospheric%20%2F%20HRRR-2196f3)]()
[![Herbie](https://img.shields.io/badge/Herbie-HRRR%20Fetcher-4caf50)]()
[![STAC](https://img.shields.io/badge/STAC-v1.0.0-brightgreen)]()
[![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%2BCARE-gold)]()
[![Reliability](https://img.shields.io/badge/Reliability-Core_v11.2-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

**Purpose**  
Provide deterministic, reproducible ingestion of NOAA HRRR atmospheric model data via **Herbie**, including Kansas-subset extraction, GRIB2 → Xarray conversion, tiling, reprojection, and optimized storage (Zarr, NetCDF, COG), with complete STAC/DCAT metadata and PROV-O lineage.

</div>

---

## 📘 1. Overview

This module ingests the **High-Resolution Rapid Refresh (HRRR)** atmospheric forecast model from open NOAA archives (AWS/GCP/Azure/NOMADS).  
The ingestion DAG performs:

- GRIB2 → `xarray.Dataset` conversion  
- Kansas regional subsetting  
- Optional variable filtering  
- CF-compliant reprojection  
- Multi-format export (Zarr, NetCDF, COG)  
- PROV-O lineage & STAC/DCAT emission  
- Deterministic DAG behavior under LangGraph v11  

All processing is **idempotent**, reproducible, and WAL-backed.

---

## 🗂️ 2. Directory Layout (v11.2 Standard · Immediate + One Branch)

```text
📁 src/pipelines/atmospheric/hrrr_ingest/        — HRRR ingestion module root
│   📂 scripts/                                  — Fetch, subset, convert, export, provenance scripts
│   📂 configs/                                  — YAML config files (variables, bbox, storage policy)
│   📂 stac/                                     — STAC Collection + Item metadata for HRRR runs
│   📂 logs/                                     — Write-Ahead Logs + ingestion logs
│   📄 README.md                                 — This governed ingestion README
```

> This follows the **global v11.2 layout standard** you adopted.  
> I will now use this layout automatically across the entire KFM project.

---

## 🌐 3. Data Sources & Access

Primary source:  
- **AWS HRRR Public Dataset** (fastest mirror)

Fallbacks:  
- **GCP HRRR**  
- **Azure HRRR**  
- **NOMADS NOAA archive**

Herbie transparently resolves URIs and archives, preserving:

- Fetch URL  
- Run timestamp  
- Dataset SHA-256  
- Retrieved variables list  
- Storage path  

All fetches logged for reproducibility and governance.

---

## 🧬 4. Processing Workflow (DAG Summary)

**Step 1 — Retrieval**  
Fetch GRIB2 from cloud mirrors → verify checksum.

**Step 2 — GRIB2 → Xarray**  
Load via `cfgrib` backend with HRRR filters → produce `xarray.Dataset`.

**Step 3 — Kansas Subset**  
Use bounding box from configs → ROI extraction.

**Step 4 — Variable Selection**  
Controlled by config `hrrr_variables.yml`.

**Step 5 — Export Pipeline**  
- **Zarr** (chunked, cloud-optimized)  
- **NetCDF4** (CF-compliant)  
- **COG** (for 2D surface fields)  

**Step 6 — Registration**  
Emit STAC Item, lineage JSON-LD, metadata, and dataset checksums.

---

## ⚙️ 5. Configuration

Configurable parameters:

- Variables list  
- Bounding box  
- Temporal cadence  
- Chunking/compression  
- Storage policies  
- Retry + fallback logic  
- CARE/governance sensitivity flags  

Every config change is audit-logged and embedded into STAC metadata.

---

## 📦 6. Output Formats

### Zarr (Recommended)
- Cloud-native  
- Highly performant for ML  
- Lazy I/O, partial reads

### NetCDF4
- CF-compliant scientific archival format  
- Long-term reproducibility

### COG
- 2D fields  
- Web-map and tile-server friendly  

All outputs include:

- CRS metadata  
- Temporal metadata  
- Lineage hashes  
- Provenance headers  

---

## 🔁 7. Reliability & WAL Behavior

HRRR ingestion uses the **KFM Reliability Core v11**:

- WAL entries at every DAG step  
- Deterministic replays  
- Clean rollback + resume  
- Canary checks for:
  - GRIB2 index shifts  
  - Variable schema changes  
  - Corruption  
  - Partial downloads  

Full CI testing required for all WAL paths.

---

## 🧠 8. Integration with Graph & Story Nodes

Outputs feed:

- Hydrology/climate cross-domain modeling  
- Atmospheric ML pipelines  
- Focus Mode v3 weather overlays  
- Story Node v3 atmospheric context layers  

STAC Items expected under:

```
data/stac/atmospheric/hrrr/
```

Each Item linked to:

- HRRR timestamp entities  
- Spatial regions (Kansas AOI)  
- Atmospheric variable nodes  

---

## 🕰️ 9. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; directory layout corrected; metadata expanded; badges & governance hooks added. |
| **v11.1.0** | 2025-11-26 | Initial v11.1 standardized README. |

---

<div align="center">

**Kansas Frontier Matrix — HRRR Atmospheric Ingestion**  
*Cloud-Native · FAIR+CARE-Aware · Deterministic · Reproducible*

[⬅ Back to Pipelines Index](../README.md) ·  
[🏗 Repository Architecture](../../../../../ARCHITECTURE.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../../../schemas/telemetry/hrrr-ingest-v11.json)

</div>