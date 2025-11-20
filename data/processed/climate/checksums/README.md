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
indigenous_rights_flag: "Low — environmental-only signals"
redaction_required: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low–Medium"

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

Official, FAIR+CARE-certified climate checksum registry supporting:

- 🌡️ Gridded temperature composites  
- 🌧️ Precipitation intensity & totals  
- 🌵 Drought indices (SPI/SPEI/NDVI/soil moisture)  
- 🔥 Derived hazard drivers (ET, freeze risk, heatwaves)  
- 🧠 Focus Mode v3 narratives & anomaly explanations  
- 🌐 STAC/DCAT discoverability, dataset integrity & reproducibility  

All assets listed here are **SHA-256 verified, provenance-linked, lineage-documented, and governance-approved**.

</div>

---

## 1. 🌎 Domain Overview

This registry governs all processed climate outputs in:

```
data/processed/climate/
```

**Purpose:**

- Provide cryptographic verification for climate rasters, time-series, derived indicators  
- Anchor pipeline determinism  
- Support anomaly detection & Focus Mode v3 reasoning  
- Register STAC Items & DCAT Datasets with validated checksums  
- Integrate ISO 19115 lineage + PROV-O chains  
- Facilitate environmental reproducibility, downstream modeling, and external audit  

All files referenced must:

- Pass schema validation  
- Be present in `manifest.json`  
- Include FAIR+CARE ethical metadata  
- Be accessible under CC-BY 4.0  

---

## 2. 🗂️ Directory Layout (GitHub-Safe, Mobile-Safe)

```text
data/processed/climate/checksums/
├── README.md
├── temp_composites_v11.0.0.sha256
├── precip_composites_v11.0.0.sha256
├── drought_indices_v11.0.0.sha256
├── climate_derivatives_v11.0.0.sha256
└── manifest.json
```

**Note:** Any additional `.sha256` files MUST:

- Be included in `manifest.json`
- Pass schema & governance validation  
- Include full provenance references  

---

## 3. 🔐 Role of Checksums in Climate Pipelines

Checksums uphold:

### 1. 🔁 Determinism  
Same pipeline → same outputs → same hashes.

### 2. 🧬 Provenance  
Every checksum file is a `prov:Entity` linked to:

- Generating ETL activity  
- Input datasets  
- Software version & configuration  
- KFM Data Council as responsible agent  

### 3. 🧠 Focus Mode Reliability  
Guarantees climate anomaly layers used in narratives are stable & validated.

### 4. 📦 External Reproducibility  
Third parties can validate file authenticity & reproduction.

---

## 4. 📊 Climate Asset Groups

| Group                 | Description                                | Formats                          |
|----------------------|--------------------------------------------|----------------------------------|
| temp_composites      | Temp fields (daily/monthly)                | COG GeoTIFF, NetCDF, Parquet     |
| precip_composites    | Precip intensity, totals, anomalies        | COG GeoTIFF, NetCDF, Parquet     |
| drought_indices      | SPI, SPEI, soil moisture, NDVI drought     | Parquet, GeoTIFF, CSV            |
| climate_derivatives  | Heatwaves, freeze risk, ET, composites     | Parquet, GeoTIFF, CSV            |

Each file’s checksum appears in its respective `.sha256` file.

---

## 5. 🧩 Checksum Manifest (Schema Requirements)

The domain manifest:

```
data/processed/climate/checksums/manifest.json
```

**MUST** include:

- Stable KFM ID  
- Domain = `"climate"`  
- Schema version  
- ISO timestamp of generation  
- Source pipeline ID  
- Per-asset entries with:
  - `asset_id`
  - `relative_path`
  - `sha256`
  - `source_pipeline`
  - `fairstatus`
  - Governance ledger reference  

---

## 6. ⚖️ FAIR+CARE Governance Requirements

Climate checksums are classified as:

- **FAIR:** Fully open, reusable, indexed  
- **CARE:** Low-risk but reviewed for misuse, misinterpretation, or harm to communities  

Governance files:

```
docs/standards/faircare/FAIRCARE-GUIDE.md
docs/reports/audit/data_provenance_ledger.json
```

---

## 7. 🔄 Validation, Telemetry & Sustainability

### Validation
- `checksum-generate.py`
- `checksum-verify.yml`
- `schema-validation.yml`

### Telemetry Collected
- `records_processed`
- `energy_wh`
- `carbon_gCO2e`
- `runtime_sec`

### Sustainability Thresholds
- ≤ 4.0 Wh per 1,000 assets hashed  

Aggregated into:

```
releases/v11.0.0/focus-telemetry.json
docs/reports/telemetry/data-climate-checksums-v11.json
```

---

## 8. 🕰️ Version History

| Version | Date       | Summary                                                 |
|--------:|------------|---------------------------------------------------------|
| v11.0.0 | 2025-11-20 | Full superset v11 rewrite; corrected directory layout   |
| v10.0.0 | 2025-11-10 | Initial registry & manifest                             |

<div align="center">

**Kansas Frontier Matrix — Climate Domain**  
🌡️ FAIR+CARE Certified · Integrity-Verified · Diamond⁹ Ω / Crown∞Ω  

© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Climate](../README.md) · [Data Architecture](../../ARCHITECTURE.md) · [Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>