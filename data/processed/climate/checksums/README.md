---
title: "🌡️ Kansas Frontier Matrix — Processed Climate Checksums (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "data/processed/climate/checksums/README.md"

version: "v11.0.0"
last_updated: "2025-11-20"
release_stage: "Stable / Governed"
review_cycle: "Continuous · FAIR+CARE Council Oversight"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:data-processed-climate-checksums-v11.0.0"
semantic_document_id: "kfm-doc-data-processed-climate-checksums-readme"
event_source_id: "ledger:data/processed/climate/checksums/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
data_contract_ref: "../../../docs/contracts/data-contract-v3.json"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/data-climate-processed-checksums-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0 / FAIR+CARE Certified"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Domain Integrity Registry"
intent: "processed-climate-checksums"
role: "climate-domain"
category: "Data · Climate · Integrity · Processed"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Dataset-dependent"
indigenous_rights_flag: "Low — environmental signals only"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Medium (downstream use dependent)"

ontology_alignment:
  cidoc: "E73 Information Object"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/data-climate-processed-checksums-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/data-climate-processed-checksums-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Restricted"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified climate claims"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
classification: "Public / Mixed Sensitivity"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Permanent"
sunset_policy: "Superseded upon next climate-domain checksums update"
---

<div align="center">

# 🌡️ **Kansas Frontier Matrix — Processed Climate Checksums**  
`data/processed/climate/checksums/README.md`

Authoritative, FAIR+CARE-certified **checksum registry** for:

- 🌍 Processed climate layers (temperature, precipitation, drought, ET)  
- 📦 Multi-format climate products (COG, Parquet, GeoJSON, NetCDF)  
- 🧪 Reproducible climate analyses & models  
- 🧠 Focus Mode v3 climate narratives & anomaly stories  
- 🌐 STAC/DCAT-based integrity verification  

All entries are **SHA-256 verified, pipeline-deterministic, schema-aligned, and ethically governed**.

</div>

---

## 1. 🌎 Domain Overview

The **processed climate checksums registry** governs integrity for all climate products residing under:

- `data/processed/climate/` (Q4 2025 and onward)

This includes cryptographic checksums for:

- Gridded temperature and precipitation composites (Daymet / PRISM / reanalysis blends)  
- Drought indices (SPI, SPEI, soil-moisture, NDVI-derived drought signals)  
- Evapotranspiration, heat index, and derived comfort/heatwave indicators  
- Climate hazard drivers (e.g., freeze risk, heatwave recurrence)  
- Long-term climatologies and anomalies relative to a baseline (e.g., 1991–2020 normals)  

Key properties:

- All climate files referenced here are normalized to **EPSG:4326** (unless explicitly documented)  
- Each file is covered by:
  - **ISO 19115** lineage entries  
  - **PROV-O** entity/activity/agent relationships  
  - **STAC** Item references and **DCAT** Dataset entries  
- Checksums provide a **hard integrity bound** for:
  - Reproducible ETL runs  
  - Model input validation  
  - External re-use by downstream tools and partners  

---

## 2. 🗂️ Directory Layout (GitHub-Safe)

~~~~text
data/processed/climate/checksums/
├── README.md                               ← this file
│
├── temp_composites_v11.0.0.sha256          ← Temperature raster checksums
├── precip_composites_v11.0.0.sha256        ← Precipitation raster checksums
├── drought_indices_v11.0.0.sha256          ← SPI/SPEI/soil moisture/NDVI drought checksums
├── climate_derivatives_v11.0.0.sha256      ← Derived hazard and comfort indicators
│
└── manifest.json                           ← Domain-level checksum manifest (JSON)