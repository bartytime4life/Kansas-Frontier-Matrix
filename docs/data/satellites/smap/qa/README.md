---
title: "⚠️ NASA SMAP — QA Layer Overview (Radiometer QA · Retrieval QA · RFI Flags · Post-ETL QA Assets)"
path: "docs/data/satellites/smap/qa/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems QA · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public QA Dataset Overview"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · FAIR+CARE Council · QA Subcommittee"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../schemas/json/smap-qa-dataset-v11.json"
shape_schema_ref: "../../../../schemas/shacl/smap-qa-dataset-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-overview"
event_source_id: "ledger:docs/data/satellites/smap/qa/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next QA schema release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA Dataset Layer Overview (KFM v11.2.2)**  
`docs/data/satellites/smap/qa/README.md`

**Purpose**  
Document the **quality assurance (QA) dataset layer** for SMAP-derived KFM products,  
after full ETL processing (decode → reprojection → calibration → QA/RFI → uncertainty →  
governance → provenance → STAC).  
This README describes **final QA rasters, masks, metadata, STAC fields, and DCAT descriptors**.

</div>

---

## 📘 1. What This Directory Contains

The **SMAP QA Dataset Layer** includes:

- ⚠️ Radiometer QA masks  
- 🎚️ Retrieval confidence layers  
- 📡 RFI (Radio Frequency Interference) flags  
- 🌡️ Freeze–thaw QA layers  
- 🌱 Vegetation-water retrieval QA  
- 📉 QA-derived uncertainty multipliers  
- 🗺️ QA/STAC metadata blocks (kfm:qa_values, qa schemas, etc.)  
- 🔗 PROV-O lineage for QA entities  
- 🛡 Governance-compatible (CARE/H3) QA assets  
- 🧭 Summaries for STAC Collections (extent, temporal coverage, QA distributions)

These are the **final QA artifacts** exposed via STAC, DCAT, Story Node v3, Focus Mode v3,  
and the KFM web application.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/
├── 📄 README.md                             # This file
│
├── 🛰️ radiometer/                           # Radiometer QA products
│   ├── qa_flags.tif
│   ├── qa_codes.json
│   └── metadata.json
│
├── 📡 rfi/                                   # Radio Frequency Interference masks
│   ├── rfi_mask.tif
│   ├── rfi_codes.json
│   └── metadata.json
│
├── 🎚️ retrieval/                             # Retrieval confidence layers (SM, FT, VWC)
│   ├── soil_moisture_conf.tif
│   ├── freeze_thaw_conf.tif
│   ├── vwc_conf.tif
│   └── metadata.json
│
├── 🌡️ freeze_thaw/                           # QA for freeze-thaw classification
│   ├── ft_qa_mask.tif
│   └── metadata.json
│
├── 🌱 vegetation_water/                      # QA for VWC modeling
│   ├── vwc_qa_mask.tif
│   └── metadata.json
│
├── 📉 uncertainty_modifiers/                # QA-derived uncertainty adjustments
│   ├── qa_uncertainty_scale.tif
│   └── metadata.json
│
└── 🧪 tests/                                  # QA dataset-level validation suite
    ├── test_qa_masks.py
    ├── test_rfi_integrity.py
    ├── test_retrieval_confidence.py
    ├── test_uncertainty_modifiers.py
    └── fixtures/
        ├── sample_qa_mask.tif
        ├── sample_rfi_mask.tif
        ├── sample_retrieval_conf.tif
        ├── sample_uncertainty_scale.tif
        ├── sample_metadata.json
        └── schema_expected.json
~~~

---

## 🧩 3. QA Dataset Responsibilities

### ⚠️ Radiometer QA
Ensures radiometric stability, checks for corrupted beams, and warns of low-quality observations.

### 📡 RFI (Radio Frequency Interference)
Identifies and masks pixels corrupted by terrestrial or orbital RF contamination.

### 🎚️ Retrieval Confidence
Confidence scoring for:

- soil moisture  
- freeze–thaw  
- vegetation water content  

Used downstream by uncertainty propagation and Focus Mode v3.

### 🌡 Freeze–Thaw QA
Flags marginal or ambiguous FT classifications, especially during seasonal transitions.

### 🌱 Vegetation Water Content QA
Marks low-confidence retrievals near canopy boundaries or cloudy/mixed pixels.

### 📉 QA-Derived Uncertainty Modifiers
Propagates QA information into the uncertainty model from ETL Stage 5.

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty

QA layers enter public datasets **only after**:

- `"kfm:care_label"` propagation  
- `"kfm:h3_sensitive"` propagation  
- `"kfm:mask_required"` set where QA interacts with sensitive geographies  
- `"kfm:sovereignty_uncertainty_floor"` maintained  
- QA metadata blocks include `"kfm:governance_notes"`  
- Uncertainty floors preserved in sovereign lands  

Governance is validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

No QA asset may enter STAC if governance metadata is incomplete.

---

## 🧪 5. QA & Validation

Dataset-level tests validate:

- correct QA flag decoding  
- no NaN/invalid regions  
- CRS integrity  
- correct uncertainty scaling  
- correct STAC integration  
- correct DCAT metadata  
- correct PROV lineage  

All QA failures → **release blocked**.

---

## 🔁 6. Role in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (ETL Stage 4)
 → uncertainty propagation (Stage 5)
 → governance masking (Stage 6)
 → provenance building (Stage 7)
 → stac_writer (Stage 8)
 → QA DATASET LAYER (this directory)
~~~

This directory reflects **final, released QA data**.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
QA helps suppress noisy moisture anomalies.

### Climate  
QA informs VWC and FT anomaly classification stability.

### Archaeology  
QA layers guide responsible interpretation of environmental conditions.

### Story Node v3  
QA-backed context improves narrative reliability.

### Focus Mode v3  
QA metadata influences explanation weights and confidence scoring.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP QA Dataset README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [⚠️ QA Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

