---
title: "🧪 NASA SMAP — Uncertainty Modifier Test Suite (QA → Uncertainty · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/uncertainty_modifiers/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public QA/Uncertainty Test Documentation"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"

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
telemetry_schema: "../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-uncertainty-modifiers-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-uncertainty-modifiers-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:uncertainty-modifiers-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-uncertainty-modifiers-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/uncertainty_modifiers/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next uncertainty propagation revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP QA → Uncertainty Modifier Test Suite**  
`docs/data/satellites/smap/qa/uncertainty_modifiers/tests/README.md`

**Purpose**  
Validate the ETL Stage 5 **Uncertainty Modifier Layer**, ensuring that pixel-level  
uncertainty multipliers derived from QA (Radiometer, RFI, SM/FT/VWC Retrieval QA)  
are correct, deterministic, FAIR+CARE compliant, and sovereignty-safe.

</div>

---

## 📘 1. Overview

The uncertainty modifiers tested here must:

- 📉 **integrate all QA sources** (RFI, Radiometer, SM/FT/VWC retrieval QA)  
- 🎚️ produce correct uncertainty-scaling behavior  
- 🗺 ensure CRS + spatial alignment  
- 🛡 propagate sovereignty metadata (H3, masking rules)  
- 📑 include valid STAC/DCAT metadata  
- 🔗 embed full PROV-O lineage  
- 🚫 avoid high-resolution leakage inside sensitive tribal lands  
- 🧭 behave deterministically across CI runs

Failure in any test → **hard block on SMAP release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/uncertainty_modifiers/tests/
├── 📄 README.md                                  # This file
│
├── 🧪 test_uncertainty_scaling.py               # QA → uncertainty scaling correctness
├── 🧪 test_metadata_integrity.py                 # STAC/DCAT + uncertainty metadata tests
├── 🧪 test_governance_preservation.py            # CARE/H3 sovereignty preservation
│
└── 🔧 fixtures/
    ├── sample_uncertainty_scale.tif              # Synthetic uncertainty multiplier raster
    ├── sample_metadata.json                      # Metadata stub (STAC/DCAT/CARE/H3)
    ├── expected_uncertainty_output.json          # Deterministic uncertainty decoding result
    └── schema_expected.json                      # Strict validation schema
~~~

---

## 🧩 3. Test Domains & Expectations

### 🧮 **Uncertainty Scaling Tests**
Validate:

- correct combination of QA inputs  
- expected scaling range (never negative, never > model max)  
- no reduction of uncertainty in sovereign H3 zones  
- deterministic behavior across tiles  

### 🎚️ **QA Integration Tests**
Ensure correct behavior from:

- Radiometer QA  
- RFI QA  
- SM, FT, VWC retrieval QA  
- seasonal + vegetation interactions  
- QA → uncertainty consistency  

### 🗺️ **Spatial Integrity Tests**
Validate:

- CRS correctness  
- pixel alignment  
- tile-boundary behavior  
- H3 alignment for sovereignty masking  

### 📑 **Metadata Integrity Tests**
Validate:

- `"kfm:uncertainty_schema"`  
- `"kfm:qa_values"` → uncertainty mapping  
- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:governance_notes"`  

### 🛡 **Governance Preservation Tests**
Ensure:

- sovereignty FLOORS applied (“uncertainty cannot decrease”)  
- generalization in sovereign H3 cells  
- CARE label retained  
- PROV-O lineage present  
- no sensitive detail leaked  

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Uncertainty modifiers interact deeply with sovereignty requirements:

- uncertainty must **increase or remain stable**, never decrease  
- sensitive transitions (SM/FT/VWC) must be generalized in sovereign regions  
- sovereign H3 metadata must propagate through the uncertainty layer  
- `"kfm:sovereignty_uncertainty_floor"` MUST be enforced  
- `"kfm:mask_required"` MUST be applied where needed  
- `"kfm:governance_notes"` MUST describe applied masking/generalization  

Compliance validated by:

- **faircare_validate.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **data_pipeline.yml**

---

## 🧪 5. CI Integration

Executed under:

- **ci.yml**  
- **data_pipeline.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**

Failure of any test → **full ETL block**.

---

## 🔁 6. Placement in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (SM / FT / VWC)
 → uncertainty propagation (THIS TEST SUITE)
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
Improved, uncertainty-aware soil-moisture anomaly interpretation.

### Climate  
Better FT/VWC anomaly modeling with sovereign-safe uncertainty constraints.

### Archaeology  
Reduces risk of misinterpretation of environmental states.

### Story Node v3  
Uncertainty modifiers impact narrative evidence weighting.

### Focus Mode v3  
Reasoning uses uncertainty-aware scoring for environmental context.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial uncertainty-modifier test-suite README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.    |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📂 Uncertainty Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

