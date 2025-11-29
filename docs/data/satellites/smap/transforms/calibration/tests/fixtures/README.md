---
title: "📦 NASA SMAP — Calibration Test Fixtures (Synthetic Inputs & Expected Outputs) · ETL Stage 3"
path: "docs/data/satellites/smap/transforms/calibration/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Calibration QA · FAIR+CARE Council Oversight"
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
care_label: "CARE-A / CARE-B (dependent on context tests)"
indigenous_rights_flag: true
sensitivity_level: "Low (synthetic test rasters and tables)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Calibration Subcommittee · Earth Systems QA · KFM FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-calibration-v11.schema.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-calibration-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:calibration-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-calibration-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/calibration/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "30 months"
sunset_policy: "Superseded upon fixture-format update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Calibration Test Fixtures (ETL Stage 3)**  
`docs/data/satellites/smap/transforms/calibration/tests/fixtures/README.md`

**Purpose**  
Provide the **synthetic, deterministic, FAIR+CARE-safe** calibration test fixtures  
used to validate SMAP ETL Stage 3 (Calibration): drift, gain, offset corrections,  
uncertainty propagation, and calibration-epoch alignment.

</div>

---

## 📘 1. Overview

These fixtures simulate pre- and post-calibration rasters, calibration tables,  
and calibration metadata used by unit + integration tests:

- 🎚️ Pre-calibration synthetic rasters  
- 🎚️ Expected post-calibration rasters  
- 🧮 Synthetic coefficient tables  
- 🗂️ Calibration-epoch metadata  
- 📉 Uncertainty-before/after rasters  
- 🔐 CARE/H3 sovereignty-flag stubs for governance tests

They ensure:

- deterministic behavior  
- reproducibility  
- FAIR+CARE governance compliance  
- schema correctness  
- no real-world environmental data

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/calibration/tests/fixtures/
├── 📄 README.md                               # This file
│
├── 🛰️ sample_precal.tif                       # Synthetic raster before calibration
├── 🛰️ sample_postcal_expected.tif             # Expected result after calibration
│
├── 📉 sample_uncertainty_precal.tif           # Pre-calibration uncertainty raster
├── 📉 sample_uncertainty_postcal_expected.tif # Expected uncertainty after calibration
│
├── 🧮 coeff_stub.json                         # Synthetic calibration coefficient table
├── 🗂️ calibration_epoch_metadata.json         # Synthetic calibration epoch metadata
│
└── 🔧 schema_expected.json                    # Schema describing fixture expectations
~~~

---

## 🧩 3. Fixture Responsibilities

### 🛰️ sample_precal.tif  
- Tiny (e.g., 10×10) synthetic raster  
- Represents radiometer-derived variables  
- Used to test raw → calibrated transition logic  

### 🛰️ sample_postcal_expected.tif  
- Deterministic expected output  
- Tests drift, gain, and offset corrections  

### 📉 uncertainty rasters  
- Validate uncertainty propagation logic:  
  - must never decrease artificially  
  - must obey uncertainty floors  
  - must follow KFM uncertainty propagation rules  

### 🧮 coeff_stub.json  
Contains:

- gain  
- offset  
- drift_per_year  
- mode-specific corrections  
- version identifiers  

Synthetic, FAIR-safe values **only**.

### 🗂️ calibration_epoch_metadata.json  
Declares:

- calibration version  
- NASA product version  
- valid-from / valid-to  
- initialization of governance metadata  

Used by governance-preservation tests.

### 🔧 schema_expected.json  
Defines:

- valid shapes  
- valid metadata  
- required fields  
- accepted value ranges  
- governance metadata expectations  

---

## 🔐 4. Governance & FAIR+CARE Constraints

Fixtures MUST test:

- CARE label propagation  
- Sovereignty flag preservation (H3-sensitive regions)  
- No calibration-induced sharpening of environmental signals  
- No silent uncertainty reduction  
- Complete provenance propagation  

Governance validation is performed via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation

Fixture validation ensures:

- deterministic fixture behavior  
- no NaNs unless defined  
- coefficient tables load correctly  
- drift/gain/offset corrections match expected outputs  
- uncertainty propagation yields expected ranges  
- CRS consistency in raster fixtures  
- PROV-O fields are valid and extractable  

Tests run under:

```
docs/data/satellites/smap/transforms/calibration/tests/
```

---

## 🔁 6. Context in the Full ETL Pipeline

~~~text
decode
 → reprojection
 → calibration   (validated using these fixtures)
 → QA/RFI integration
 → uncertainty propagation
 → governance masking (CARE/H3)
 → STAC/DCAT output
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Fixtures guarantee the **foundation of calibration correctness**.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Accurate wetness/soil-moisture calibration across epochs.

### Climate  
Reliable VWC and freeze–thaw environmental layers.

### Archaeology  
Consistent vegetation & soil-state environmental context.

### Story Node v3  
Calibration-aware narrative provenance.

### Focus Mode v3  
Transparent calibration epoch reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                |
|--------:|------------|--------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Fully rebuilt file; corrected footer; governance-safe; emoji-rich; CI-stable; STAC/DCAT/PROV aligned. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Calibration Tests](../README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
