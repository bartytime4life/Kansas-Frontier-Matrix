---
title: "📉 NASA SMAP — Uncertainty Propagation Stage (Radiometer · QA/RFI · Calibration-Adjusted) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Earth Systems · FAIR+CARE Council · QA/Uncertainty Subcommittee"
status: "Active / Enforced"

classification: "Public ETL Documentation"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
jsonld_profile: "KFM-JSONLD v11"

sbom_ref: "../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (elevated — uncertainty intersects sovereignty rules)"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Earth Systems Working Group · Uncertainty Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  prov_o: "prov:Activity"
  schema_org: "DataTransform"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-uncertainty-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-uncertainty-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:uncertainty-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-uncertainty"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded when uncertainty model changes"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📉 **NASA SMAP — Uncertainty Propagation Stage (ETL Stage 5)**  
`docs/data/satellites/smap/transforms/uncertainty/README.md`

**Purpose**  
Define ETL **Stage 5**, which computes, propagates, scales, and harmonizes  
uncertainty for all SMAP-derived geophysical variables after calibration and QA/RFI integration.  
This process ensures all downstream KFM datasets carry accurate, ethical, FAIR+CARE-aligned  
uncertainty metadata and rasters.

</div>

---

## 📘 1. Overview

This stage:

- Computes radiometer-driven uncertainty  
- Integrates uncertainty changes caused by calibration  
- Adjusts uncertainty using QA and RFI multipliers  
- Applies sovereignty-aware uncertainty floors  
- Ensures uncertainty is NEVER artificially decreased  
- Writes STAC uncertainty assets  
- Adds `kfm:uncertainty`, `kfm:uncertainty_type`, and `kfm:uncertainty_floor`  
- Updates provenance and lineage  
- Prepares data for Stage 6 (governance masking)

Uncertainty is **first-class metadata** in KFM, essential for scientific and ethical interpretation.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/
├── 📄 README.md                            # This file
│
├── 📉 propagate_uncertainty.py             # Core uncertainty propagation engine
├── 🧮 models/                              # Radiometer + QA uncertainty models
│   ├── radiometer_model.json
│   ├── qa_rfi_model.json
│   └── combined_model.json
│
└── 🧪 tests/                               # Uncertainty test suite
    ├── test_uncertainty_core.py
    ├── test_uncertainty_scaling.py
    ├── test_uncertainty_floor.py
    ├── test_governance_preservation.py
    └── fixtures/
        ├── sample_preuncertainty.tif
        ├── sample_postuncertainty_expected.tif
        ├── model_stub.json
        └── schema_expected.json
~~~

---

## 🧩 3. Responsibilities of the Uncertainty Stage

### ✔ Radiometer-Origin Uncertainty  
Derived from SMAP L2 brightness temperature and L3 retrieval confidence.

### ✔ Calibration-Induced Uncertainty  
Calibration changes (gain, offset, drift) MUST propagate additional uncertainty.

### ✔ QA/RFI Derived Scaling  
- RFI zones increase uncertainty  
- Low-retrieval-confidence regions increase uncertainty  
- Freeze–thaw transition areas increase uncertainty  

### ✔ Sovereignty-Aware Uncertainty Floors  
If a pixel intersects a protected Indigenous H3 region:

- A minimum uncertainty floor (policy-defined) is enforced  
- Uncertainty can **only increase**, never decrease  

### ✔ STAC Uncertainty Assets  
Each dataset must include:

- `uncertainty` asset  
- `kfm:uncertainty_type`  
- `kfm:uncertainty_floor`  
- `kfm:uncertainty_model`  

### ✔ PROV-O Uncertainty Lineage  
Include:

- `prov:used` → uncertainty model  
- `prov:wasGeneratedBy` → uncertainty propagation step  
- `prov:atLocation` → output file  

---

## 🔐 4. Governance & FAIR+CARE Requirements

Uncertainty rules enforce:

- Ethical transparency about model confidence  
- Protection of sovereign landscapes from misleading environmental certainty  
- Clear distinction between:
  - measured values  
  - modeled values  
  - uncertainty for both  

Uncertainty pipeline MUST:

- Preserve CARE labels  
- Maintain `"kfm:mask_required"` when appropriate  
- Enforce sovereignty-aware uncertainty floors  
- Prevent precision increases along sensitive boundaries  
- Provide transparent provenance explaining all uncertainty changes  

Governance validation runs through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  
- `stac_validate.yml`

---

## 🧪 5. QA & Validation

Tests validate:

- correct uncertainty computation  
- QA/RFI scaling behavior  
- uncertainty-floor compliance  
- no NaN leakage  
- CRS consistency  
- STAC extension validity  
- PROV-O lineage correctness  
- governance flag retention  

QA results stored in:

`docs/data/satellites/smap/qa/`

Telemetry emitted to:

`releases/<version>/data-telemetry.json`

---

## 🔁 6. Place in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation  (this stage)
 → governance masking (CARE/H3)
 → STAC/DCAT metadata output
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Stable soil-moisture uncertainty across calibration cycles.

### Climate  
Reliable VWC anomaly detection with transparent confidence.

### Archaeology  
Uncertainty-aware environmental context reduces misinterpretation.

### Story Node v3  
Narratives enriched with uncertainty bars and environmental confidence estimates.

### Focus Mode v3  
Context engines use uncertainty to weight entity/environmental explanations.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full uncertainty-stage README; emoji layout; ethical/sovereignty uncertainty floors; STAC/DCAT aligned. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📉 Uncertainty Tests](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

