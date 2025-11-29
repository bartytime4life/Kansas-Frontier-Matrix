---
title: "📦 NASA SMAP — QA/RFI Integration Test Fixtures (Synthetic Inputs & Expected Outputs) · ETL Stage 4"
path: "docs/data/satellites/smap/transforms/qa_integration/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Test Fixtures"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-transforms-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R3"
care_label: "CARE-A/B (depending on test scenario)"
indigenous_rights_flag: true
sensitivity_level: "Low (synthetic QA/RFI data)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems QA Subcommittee · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-qa-integration-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-qa-integration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:qa-integration-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-qa-integration-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/qa_integration/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded upon fixture-set revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — QA/RFI Integration Test Fixtures (ETL Stage 4)**  
`docs/data/satellites/smap/transforms/qa_integration/tests/fixtures/README.md`

**Purpose**  
Provide the **synthetic QA + RFI test inputs and expected outputs** that validate  
ETL Stage 4 (QA/RFI Integration).  
These fixtures ensure that QA merges, RFI decoding, uncertainty scaling,  
governance preservation, and STAC-ready QA metadata all function consistently and safely.

</div>

---

## 📘 1. Overview

Fixtures simulate key QA + RFI scenarios without using any real environmental data:

- L2 + L3 QA codes  
- RFI bitfields  
- Synthetic pixel-level noise contamination  
- QA → uncertainty propagation  
- CARE/H3-sensitive regions for governance tests  
- Expected QA masks for STAC integrations  
- Expected post-QA rasters  

All fixtures are deterministic, FAIR-safe, sovereignty-safe, and CI-fast.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/qa_integration/tests/fixtures/
├── 📄 README.md                            # This file
│
├── 🛰️ sample_preqa.tif                     # Raster before QA/RFI integration
├── 🛰️ sample_postqa_expected.tif           # Raster after QA/RFI integration
│
├── 📡 sample_rfi_flags.json                # Synthetic RFI bitfield inputs
├── ⚠️ sample_qa_metadata.json              # Synthetic NASA QA metadata for scenario testing
│
├── 📉 sample_uncertainty_preqa.tif         # Pre-QA uncertainty raster
├── 📉 sample_uncertainty_postqa_expected.tif # Expected after QA uncertainty propagation
│
└── 🔧 schema_expected.json                 # Formal fixture schema (dimensions, types, QA rules)
~~~

---

## 🧩 3. Fixture Responsibilities

### 🛰️ sample_preqa.tif  
Simulates a pre-QA raster (soil moisture / FT / VWC compatible).  
Used to verify how QA masks modify data values and uncertainty.

### 🛰️ sample_postqa_expected.tif  
Expected output raster after integration of QA + RFI flags.

Verifies:

- masking logic  
- QA-influenced uncertainty  
- pixel-level correct propagation  

### 📡 sample_rfi_flags.json  
Contains synthetic RFI codes that represent:

- strong interference  
- weak interference  
- no interference  
- ambiguous RFI cases  

### ⚠️ sample_qa_metadata.json  
Defines metadata from NASA L2/L3 QA fields:

- retrieval confidence  
- freeze-thaw QA  
- VWC QA  
- quality flags  
- orbit-specific conditions  

Used to test QA unification logic.

### 📉 sample_uncertainty_preqa.tif / sample_uncertainty_postqa_expected.tif  
Validate uncertainty-propagation logic:

- Uncertainty must **never artificially shrink**  
- QA-based uncertainty multipliers must be applied  
- Sovereignty-aware uncertainty rules must hold  

### 🔧 schema_expected.json  
Defines:

- array shapes  
- CRS constraints  
- expected QA and RFI coding  
- required metadata keys  
- governance flags  
- STAC QA metadata structure (`kfm:qa_values`, `kfm:qa_flag_schema`)  

---

## 🔐 4. Governance & Sovereignty Requirements

Fixtures must enforce:

- CARE label propagation  
- H3-sensitive zone propagation  
- `"kfm:mask_required"` where QA flags imply sensitivity  
- No QA logic may sharpen environmental contrast in sovereignty-sensitive regions  
- No synthetic data may resemble real protected geographies  

Governance verification uses:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Fixture validation ensures:

- determinism  
- correct QA value mapping  
- correct RFI decoding  
- correct uncertainty scaling  
- no CRS divergence  
- correct STAC QA metadata  
- correct PROV-O lineage emissions  

Tests located at:

```
docs/data/satellites/smap/transforms/qa_integration/tests/
```

---

## 🔁 6. Relationship to the Full ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (validated by these fixtures)
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC/DCAT metadata production
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
QA-informed soil-moisture reliability.

### Climate  
QA-informed freeze-thaw interpretation.

### Ecology  
Less risk of false vegetation-water signals.

### Archaeology  
Reduced risk of using unreliable context layers.

### Story Node v3  
QA-aware narrative reliability scoring.

### Focus Mode v3  
RFI- and QA-aware environmental explanations.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                       |
|--------:|------------|----------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Complete QA-fixture README; emoji layout; governance/H3 compliance; STAC/DCAT/PROV alignment; CI-safe output. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 QA Integration Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

