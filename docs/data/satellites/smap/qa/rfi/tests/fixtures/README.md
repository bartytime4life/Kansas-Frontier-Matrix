---
title: "📦 NASA SMAP — RFI QA Test Fixtures (Synthetic · Deterministic · FAIR+CARE/H3-Safe)"
path: "docs/data/satellites/smap/qa/rfi/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public Test Fixture Dataset"
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
telemetry_schema: "../../../../../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on simulated zones)"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-rfi-qa-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-rfi-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:rfi-qa-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-rfi-qa-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/qa/rfi/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon fixture schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP RFI QA — Test Fixtures (ETL QA Validation Assets)**  
`docs/data/satellites/smap/qa/rfi/tests/fixtures/README.md`

**Purpose**  
Provide **synthetic, deterministic, sovereignty-safe, FAIR+CARE aligned** RFI QA fixtures  
used to validate **bitfield decoding**, **contamination mask generation**,  
**governance metadata propagation**, and **STAC/DCAT/PROV-O correctness**  
for SMAP RFI QA outputs in the KFM v11 ETL chain.

</div>

---

## 📘 1. Overview

These fixtures ensure:

- bitfield → semantic QA decoding correctness  
- correct mapping of RFI codes  
- valid QA mask interpretation across resolution boundaries  
- consistent alignment with SMAP rasters (CRS + geolocation)  
- propagation of CARE/H3 sovereignty metadata  
- uncertainty-scaling behavior from RFI  
- no information leakage inside sensitive Indigenous geographies  
- correct STAC/DCAT metadata blocks for RFI  
- valid PROV-O lineage components for QA entities  

All fixtures contain **synthetic data only** to comply with sovereignty policy.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/rfi/tests/fixtures/
├── 📄 README.md                               # This file
│
├── 📡 sample_rfi_mask.tif                     # Synthetic RFI interference mask
├── 📝 sample_rfi_codes.json                   # Mapping of RFI bitfields → semantic QA indicators
├── 📑 sample_metadata.json                    # Synthetic STAC/DCAT governance-safe metadata
│
├── 🎯 expected_rfi_interpretation.json        # Expected decoded QA interpretation result
└── 🗂️ schema_expected.json                    # Validation schema for fixture structure & metadata
~~~

---

## 🧩 3. Fixture Responsibilities

### 📡 `sample_rfi_mask.tif`
Simulates:

- RFI-contaminated pixels  
- ambiguous contamination  
- clean radiometer readings  
- spatial patterns with synthetic clusters  

Used to validate:

- CRS correctness  
- pixel alignment  
- contamination classification  
- sovereignty masking (if mask intersects synthetic H3-sensitive zones)  

---

### 📝 `sample_rfi_codes.json`
Defines:

- valid bitfield ranges  
- contamination flags  
- ambiguous detection states  
- SMAP → KFM unified QA mapping  

Used to ensure deterministic decoding.

---

### 📑 `sample_metadata.json`
Tests metadata utilities by checking:

- QA schema fields  
- CARE/H3 sovereignty metadata  
- uncertainty-related fields  
- STAC/DCAT metadata completeness  
- `"kfm:governance_notes"` propagation  

---

### 🎯 `expected_rfi_interpretation.json`
Represents:

- expected decoded QA values  
- contamination-level classification  
- combined QA outputs for RFI → uncertainty → governance  
- sovereignty-aware masking decisions  

Used by multiple CI tests to validate correctness.

---

### 🗂️ `schema_expected.json`
Defines mandatory validation logic:

- allowed keys & ranges  
- expected QA JSON structures  
- sovereignty/H3 rules  
- uncertainty-scaling constraints  
- valid STAC/DCAT metadata structure  
- PROV-O lineage compliance  

Any fixture mismatch → **CI hard-fail**.

---

## 🔐 4. FAIR+CARE & Sovereignty Compliance

Fixtures enforce:

- `"kfm:care_label"` always present  
- `"kfm:h3_sensitive"` propagation in synthetic scenarios  
- `"kfm:mask_required"` where contamination intersects sovereign cells  
- `"kfm:sovereignty_uncertainty_floor"` applied  
- `"kfm:governance_notes"` required  

No fixture includes real-world RF-spectrum patterns or coordinates.

---

## 🧪 5. Validation Workflow

CI validates:

- numeric + bitfield decoding  
- H3 alignment for sovereignty simulation  
- correct metadata propagation  
- uncertainty multipliers  
- PROV-O JSON-LD shapes  
- deterministic ordering  
- cross-stage linkage with ETL Stage 4 (QA/RFI integration)  

---

## 🔁 6. RFI QA in the Overall ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (this fixture set supports tests here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
 → QA dataset layer (published)
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Better separation of RFI noise from soil-moisture anomalies.

### Climate  
Cleaner freeze–thaw and VWC classifications.

### Archaeology  
Governance-safe QA filtering of sensitive landscapes.

### Story Node v3  
Confidence scoring improved through QA insights.

### Focus Mode v3  
Weighted reasoning uses QA + RFI signals.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial RFI QA fixture README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV/O-ready; CI-safe; emoji-rich.        |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 RFI QA Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

