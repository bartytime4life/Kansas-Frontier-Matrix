---
title: "⚠️ NASA SMAP — QA/RFI Integration Stage (Radiometer Quality · RFI · Retrieval Validity) · ETL Stage 4"
path: "docs/data/satellites/smap/transforms/qa_integration/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · QA Subcommittee · Earth Systems · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public ETL Documentation"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
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

fair_category: "F1-A1-I2-R3"
care_label: "CARE-A / CARE-B (dependent on derived spatial context)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems Working Group · QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../schemas/json/transform-smap-qa-integration-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/transform-smap-qa-integration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:transform:qa-integration-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-transform-qa"
event_source_id: "ledger:docs/data/satellites/smap/transforms/qa_integration/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded upon QA-schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **NASA SMAP — QA / RFI Integration Stage (ETL Stage 4)**  
`docs/data/satellites/smap/transforms/qa_integration/README.md`

**Purpose**  
Describe ETL **Stage 4**, where NASA SMAP radiometer QA fields and  
RFI (Radio Frequency Interference) indicators are integrated, normalized,  
and harmonized into KFM’s unified QA schema for soil-moisture, freeze–thaw,  
vegetation-water (VWC), and downstream uncertainty propagation.

</div>

---

## 📘 1. Overview

The **QA/RFI Integration Stage** is responsible for:

- ⚠️ Extracting radiometer QA codes (L2 + L3)  
- 📡 Decoding RFI interference signals  
- 🌡️ Integrating freeze–thaw QA flags  
- 🌱 Integrating vegetation-water QA masks  
- 🎚️ Normalizing QA codes to KFM-Standard QA schema  
- 📦 Producing QA COG assets (aligned with reprojection/calibration output)  
- 📉 Propagating QA-informed uncertainty multipliers  
- 🔐 Preserving CARE/H3 governance flags  
- 🧾 Writing QA metadata for STAC Items (`kfm:qa_values`, `kfm:qa_flag_schema`)  
- 🧬 Emitting PROV-O lineage entries  

This stage ensures **no dataset** is delivered without validated, harmonized QA information.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/qa_integration/
├── 📄 README.md                        # This file
│
├── ⚠️ integrate_qa.py                 # Main QA/RFI integration engine
├── 📡 decode_rfi.py                   # Decode RFI flags from NASA products
├── 🔢 qa_flag_schema.json             # KFM canonical QA schema (code → semantic meaning)
├── 🧬 qa_mappings.json                # Map NASA QA fields → KFM unified format
│
├── 🧪 tests/                           # QA Integration test suite
│   ├── test_integrate_qa.py
│   ├── test_rfi_decoding.py
│   ├── test_qa_mappings.py
│   ├── test_governance_preservation.py
│   └── fixtures/
│       ├── sample_preqa.tif
│       ├── sample_postqa_expected.tif
│       ├── sample_rfi_flags.json
│       └── sample_qa_metadata.json
~~~

---

## 🧩 3. QA Integration Responsibilities

### ⚠️ Merge Radiometer QA Fields  
- Validate presence of NASA QA groups  
- Normalize codes across L2/L3  
- Combine multiple QA layers where required  
- Ensure consistent representation across SM/FT/VWC  

### 📡 Decode RFI Interference  
- Extract RFI bitfields  
- Map values to KFM-semantic labels  
- Apply **RFI-based uncertainty scaling**  
- Flag affected pixels for downstream masking  

### 🧪 Validate Retrieval Confidence  
- Soil moisture retrieval confidence  
- Freeze–thaw classification validity  
- VWC retrieval confidence  

### 🌐 KFM Unified QA Schema  
Populate required fields:

- `kfm:qa_flag_schema`  
- `kfm:qa_values`  
- `kfm:qa_interpretation`  
- `kfm:qa_confidence_score`  

### 📉 Uncertainty Propagation  
- QA/RFI-derived uncertainty barriers  
- Inhibit certainty in noisy regions  
- Never reduce uncertainty improperly  
- Output masks consistent with KFM uncertainty rules  

### 🔐 Governance Flag Preservation  
- Maintain CARE/H3 flags in QA outputs  
- Mark `"kfm:mask_required": true` where sensitive regions intersect QA anomalies  
- Never sharpen or reveal sensitive patterns  

---

## 🔐 4. Governance & Sovereignty

Even QA fields can:

- encode vegetation stress  
- reveal soil/state patterns  
- correlate with sensitive Indigenous lands  
- produce false interpretive signals if misapplied  

Thus KFM mandates:

- CARE-A/B classification continuation  
- Sovereignty H3 review on QA-corrected regions  
- `"kfm:mask_required"` when QA reveals at-risk geographies  
- Provenance for all QA corrections  

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

QA integration tests ensure:

- correct mapping of NASA QA → KFM QA schema  
- RFI decoding correctness  
- uncertainty propagation correctness  
- no corruption of CRS or grid alignment  
- provenance correctness  
- governance preservation  
- consistency with STAC v11 projection/raster extensions  

QA logs stored under:

`docs/data/satellites/smap/qa/`

Telemetry exported to:

`releases/<version>/data-telemetry.json`

---

## 🔁 6. Integration in the Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (this stage)
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC Item/Collection creation
 → DCAT dataset registration
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
- Suppress unreliable soil-moisture anomalies  
- Improve floodplain modeling accuracy  

### Climate  
- QA-aware freeze–thaw detection  
- VWC trend stabilization  

### Archaeology  
- Reduce false context from QA-contaminated environmental signals  

### Story Node v3  
- Provide uncertainty + QA-driven corrections in narrative overlays  

### Focus Mode v3  
- Reliability indicators reinforced by QA + RFI metadata  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                    |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Full QA/RFI integration documentation; emoji layout; STAC/DCAT/PROV; governance/H3; CI-safe.               |
| v10.3.2 | 2025-11-14 | Pre-v11 minimal QA notes.                                                                                  |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [⚠️ QA Integration Tests](../README.md) · [🛡 Governance](../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

