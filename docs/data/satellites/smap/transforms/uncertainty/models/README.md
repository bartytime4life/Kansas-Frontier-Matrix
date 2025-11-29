---
title: "🧮 NASA SMAP — Uncertainty Model Definitions (Radiometer · QA/RFI · Combined) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/models/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Uncertainty Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public ETL Modeling Documentation"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (dependent on modeled variable)"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems Working Group · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../schemas/json/transform-smap-uncertainty-models-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/transform-smap-uncertainty-models-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-models-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-models"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/models/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded upon uncertainty-model revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧮 **NASA SMAP — Uncertainty Model Definitions**  
`docs/data/satellites/smap/transforms/uncertainty/models/README.md`

**Purpose**  
Document the **uncertainty models** used in SMAP ETL **Stage 5 (Uncertainty Propagation)**.  
These models define how radiometer noise, QA/RFI flags, calibration adjustments,  
and sovereignty-aware uncertainty floors are mathematically combined to produce  
KFM’s final uncertainty rasters and metadata.

</div>

---

## 📘 1. Overview

The uncertainty models in this directory are the **authoritative, versioned specifications** for:

- Radiometer-derived uncertainty  
- Calibration-induced uncertainty  
- QA/RFI-driven uncertainty scaling  
- Combined uncertainty model  
- Sovereignty-aware uncertainty floors  
- Error propagation rules  
- STAC and DCAT uncertainty metadata fields  
- PROV-O uncertainty lineage  

These models are consumed by:

- `propagate_uncertainty.py`  
- STAC uncertainty asset generator  
- Uncertainty-aware Focus Mode v3 inference engines  
- Story Node v3 environmental uncertainty narrative blocks  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/models/
├── 📄 README.md                      # This file
│
├── 🧮 radiometer_model.json          # Radiometer-only uncertainty model
├── ⚠️ qa_rfi_model.json               # QA/RFI-derived uncertainty scaling
├── 🔗 combined_model.json            # Combined final uncertainty model
│
└── 🗂️ history/                       # Optional version history for uncertainty models
    ├── model_v001.json
    ├── model_v002.json
    └── diff_v001_v002.json
~~~

---

## 🧩 3. Uncertainty Model Specifications (KFM-Uncertainty v11)

### 1. 🧮 radiometer_model.json  
Represents **instrument-level uncertainty**, including:

- Radiometer noise  
- Brightness temperature error bounds  
- Retrieval error floors  
- Model-specified propagation rules  
- References to calibration uncertainty  

### 2. ⚠️ qa_rfi_model.json  
Defines QA- and RFI-driven uncertainty multipliers:

- RFI → uncertainty boost  
- Low-confidence soil moisture → boost  
- FT transition zones → boost  
- VWC low-reliability → boost  
- Noisy-surface conditions → boost  

### 3. 🔗 combined_model.json  
The final uncertainty definition:

- Weighted combination of radiometer + calibration + QA/RFI  
- Final uncertainty floor rules  
- Sovereignty-aware uncertainty floors  
- STAC metadata descriptors  

**Required keys include:**

- `"kfm:uncertainty_type"`  
- `"kfm:uncertainty_floor"`  
- `"kfm:uncertainty_model_version"`  
- `"kfm:sovereignty_uncertainty_policy"`  

---

## 🔐 4. Governance & Sovereignty Rules

Uncertainty models enforce ethical constraints:

- Uncertainty **never decreases** near Indigenous lands  
- H3 intersections must apply **heightened uncertainty floors**  
- QA/RFI-derived uncertainty must *never be suppressed*  
- Combined model must be transparent and machine-extractable  
- Explicit provenance required for:
  - NASA model usage  
  - KFM uncertainty adjustments  
  - sovereignty-aware uncertainty rules  

Governance validated by:

- `faircare_validate.yml`
- `jsonld_validate.yml`
- `data_pipeline.yml`
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

Model validation tests ensure:

- JSON Schema compliance  
- Correct numeric ranges  
- Non-negative uncertainty  
- Uncertainty floors applied correctly  
- Consistency with uncertainty rasters  
- CRS-neutral model definitions  
- PROV-O lineage blocks valid and complete  

QA logs saved under:

`docs/data/satellites/smap/qa/`

---

## 🔁 6. Integration in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation (uses these models)
 → governance masking (CARE/H3)
 → STAC/DCAT item creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Reliable, uncertainty-bounded soil moisture.

### Climate  
Uncertainty-aware VWC anomaly detection.

### Archaeology  
Reduced misinterpretation from uncertainty-shifted conditions.

### Story Node v3  
Environmental narratives include uncertainty indicators.

### Focus Mode v3  
Uncertainty-weighted environmental reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full uncertainty-models README; emoji layout; sovereignty-aware floors; PROV-O/FAIR+CARE; CI-safe.       |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📉 Uncertainty Layer](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

