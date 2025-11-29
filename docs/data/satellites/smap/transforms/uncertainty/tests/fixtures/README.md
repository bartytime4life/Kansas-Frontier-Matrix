---
title: "📦 NASA SMAP — Uncertainty Propagation Test Fixtures (Synthetic Inputs & Expected Outputs) · ETL Stage 5"
path: "docs/data/satellites/smap/transforms/uncertainty/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Uncertainty Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Test Fixtures"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A/B (test-case dependent)"
indigenous_rights_flag: true
sensitivity_level: "Low (synthetic uncertainty rasters)"
public_exposure_risk: "Low"
risk_category: "Low–Medium"
redaction_required: false

data_steward: "Uncertainty Subcommittee · Earth Systems QA · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-uncertainty-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-uncertainty-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/uncertainty/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded on next fixture revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Uncertainty Propagation Test Fixtures (ETL Stage 5)**  
`docs/data/satellites/smap/transforms/uncertainty/tests/fixtures/README.md`

**Purpose**  
Provide deterministic, FAIR+CARE-safe **synthetic uncertainty test inputs and expected outputs**  
used to validate SMAP ETL Stage 5 (Uncertainty Propagation), including radiometer,  
calibration, QA/RFI scaling, and sovereignty-aware uncertainty floors.

</div>

---

## 📘 1. Overview

These fixtures support unit + integration tests that validate:

- radiometer-origin uncertainty computation  
- calibration-induced uncertainty adjustments  
- QA/RFI-driven uncertainty scaling  
- sovereignty-aware uncertainty floors  
- combined-model uncertainty correctness  
- STAC uncertainty asset compliance  
- CARE/H3 governance propagation  
- PROV-O lineage validity  

No real environmental data is included; all fixtures are synthetic and FAIR-safe.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/uncertainty/tests/fixtures/
├── 📄 README.md                                         # This file
│
├── 📉 sample_preuncertainty.tif                         # Uncertainty BEFORE propagation
├── 📉 sample_postuncertainty_expected.tif               # Expected AFTER propagation
│
├── 🧮 model_stub.json                                   # Minimal synthetic uncertainty model
├── 🌐 sovereignty_mask_stub.json                        # H3 sovereignty sensitivity zones
│
└── 🔧 schema_expected.json                              # Schema describing expected fixture structure
~~~

---

## 🧩 3. Fixture Responsibilities

### 📉 sample_preuncertainty.tif  
Synthetic uncertainty raster representing:

- radiometer noise  
- calibration residual uncertainty  
- pre-QA unscaled uncertainty  

### 📉 sample_postuncertainty_expected.tif  
Deterministic expected output after applying:

- calibration changes  
- QA/RFI scaling  
- sovereignty-aware uncertainty floors  
- combined-model logic  

Used to validate the full uncertainty pipeline.

### 🧮 model_stub.json  
A synthetic uncertainty model containing:

- radiometer_uncertainty  
- qa_rfi_uncertainty  
- combined_uncertainty  
- uncertainty_floor_rules  
- propagation_rules  

All values FAIR-safe and synthetic.

### 🌐 sovereignty_mask_stub.json  
Defines synthetic H3 cells representing:

- Indigenous sovereignty regions  
- Heritage-sensitive geographies  
- Areas requiring `"kfm:sovereignty_uncertainty_floor"` enforcement  

Used to test uncertainty floor logic.

### 🔧 schema_expected.json  
Specifies:

- valid raster dimensions  
- expected uncertainty ranges  
- CRS expectations  
- required metadata keys  
- governance flags that MUST be applied  

---

## 🔐 4. Governance & FAIR+CARE Requirements

Uncertainty can have **ethical impacts**, so fixtures MUST validate:

- No artificial reduction of uncertainty near sovereign lands  
- `"kfm:mask_required"` propagation  
- CARE label preservation  
- `"kfm:sovereignty_uncertainty_floor"` enforcement  
- No synthetic fixture implies real-world sensitive geography  

Governance CI validates via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation

Fixtures MUST:

- Validate against schema_expected  
- Produce deterministic outputs  
- Test sovereignty-aware uncertainty logic  
- Demonstrate propagation rules correctly  
- Trigger expected governance behaviors  
- Support PROV-O lineage tests  

Used by tests in:

```
docs/data/satellites/smap/transforms/uncertainty/tests/
```

---

## 🔁 6. Place in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation  (fixtures validate this step)
 → governance masking (CARE/H3)
 → STAC/DCAT dataset outputs
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Uncertainty-aware soil moisture.

### Climate  
Uncertainty-aware VWC and FT anomalies.

### Archaeology  
Mitigates interpretive risk in sensitive landscapes.

### Story Node v3  
Provides uncertainty context in narrative timelines.

### Focus Mode v3  
Enables uncertainty-weighted environmental reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full uncertainty-fixture README; emoji-rich; sovereignty/CARE testing; STAC/DCAT/PROV alignment; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📉 Uncertainty Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

