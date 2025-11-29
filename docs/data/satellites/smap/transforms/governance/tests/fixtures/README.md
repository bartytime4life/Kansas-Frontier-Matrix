---
title: "📦 NASA SMAP — Governance & Sovereignty Masking Test Fixtures (CARE/H3) · ETL Stage 6"
path: "docs/data/satellites/smap/transforms/governance/tests/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Sovereignty Working Group · FAIR+CARE Council"
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

fair_category: "F1-A3-I2-R5"
care_label: "CARE-A / CARE-B (High-Sensitivity Governance)"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "FAIR+CARE Council · Sovereignty Working Group · Earth Systems Governance Subcommittee"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../../schemas/json/tests-smap-governance-v11.json"
shape_schema_ref: "../../../../../../../../../schemas/shacl/tests-smap-governance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:governance-tests-fixtures-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-governance-tests-fixtures"
event_source_id: "ledger:docs/data/satellites/smap/transforms/governance/tests/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon fixture-set revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **NASA SMAP — Governance & Sovereignty Masking Test Fixtures**  
`docs/data/satellites/smap/transforms/governance/tests/fixtures/README.md`

**Purpose**  
Provide synthetic, deterministic, sovereignty-safe, FAIR+CARE-aligned test fixtures  
that validate SMAP ETL **Stage 6**:  
**H3 sovereignty masking**, **CARE label enforcement**, **uncertainty-floor protection**,  
and correctness of **STAC/DCAT governance metadata**.

</div>

---

## 📘 1. Overview

These fixtures simulate **protected geographies**, **sensitive H3 regions**,  
and **governance-metadata scenarios** needed to test:

- 🔐 Sovereignty-based spatial masking  
- 🧭 Spatial generalization (blur/aggregation) in sensitive areas  
- 🛡 CARE label preservation  
- 🌐 H3 propagation  
- 📉 Uncertainty-floor enforcement  
- 📄 STAC/DCAT governance metadata creation  
- 🧾 PROV-O governance lineage  
- 🚫 Prevention of precision leaks in Indigenous lands  

All fixtures are **non-real**, **synthetic**, and **CI-fast** while accurately reproducing the  
logical structures necessary to validate masking and governance behavior.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/governance/tests/fixtures/
├── 📄 README.md                               # This file
│
├── 🛰️ sample_pre_mask.tif                     # Raster BEFORE sovereignty masking
├── 🛰️ sample_post_mask_expected.tif           # Expected raster AFTER masking/governance enforcement
│
├── 🌐 synthetic_h3_mask.json                  # Synthetic H3 cells marking sovereignty-sensitive areas
├── 🛡 governance_metadata_stub.json           # CARE/H3 metadata used to test propagation & lineage
│
└── 🔧 schema_expected.json                    # Schema rules for validating fixture shapes & metadata
~~~

---

## 🧩 3. Fixture Responsibilities

### 🛰️ sample_pre_mask.tif  
Represents a **synthetic geophysical raster** (soil moisture / FT / VWC compatible),  
before application of H3 masking or CARE/H3 enforcement.

- Contains **invented values only**  
- Simulates borderline-sensitive environmental gradients  
- Used to test lossless → masked/generalized transformation workflows  

### 🛰️ sample_post_mask_expected.tif  
Defines the **expected** output after governance masking:

- Reduced spatial precision in H3-sensitive regions  
- Aggregated/blurred pixels  
- Regions marked `"kfm:mask_required": true`  
- Uncertainty floors enforced  
- Sovereignty-aware modification of pixel values  

This fixture drives exact output validation.

---

### 🌐 synthetic_h3_mask.json  
A synthetic H3 map defining:

- precise H3 cells flagged as **sovereignty-sensitive**  
- hierarchical inheritance (`parent`, `children` H3 cells)  
- test cases for:
  - adjacency  
  - partial overlap  
  - multi-resolution boundaries  

Used to test:

- H3 → raster mask alignment  
- propagation of `"kfm:h3_sensitive"`  
- region-based uncertainty floors  

---

### 🛡 governance_metadata_stub.json  
Holds miniaturized FAIR+CARE metadata used to test:

- CARE labels  
- sovereignty-sensitive flags  
- `"kfm:care_label_reason"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- provenance for governance decisions  

Ensures metadata is preserved through masking operations.

---

### 🔧 schema_expected.json  
Defines expected fixture structure:

- raster dimensions  
- acceptable value ranges  
- metadata keys  
- governance logic invariants  
- valid H3 structures  
- expected masking behaviors  
- acceptable uncertainty floor ranges  
- STAC governance extension requirements  

Any violation → **CI test fail**.

---

## 🔐 4. Governance & Sovereignty Compliance Requirements

Fixtures validate that ETL Stage 6:

- never exposes unmasked pixels inside sovereign H3 zones  
- never reduces uncertainty near sensitive areas  
- always propagates `"kfm:mask_required"`  
- always preserves or increases uncertainty in sensitive regions  
- always retains CARE labels and governance metadata  
- never removes `"kfm:h3_sensitive"`  
- applies generalization/blur exactly according to policy  
- outputs STAC Items that fully represent governance actions  

Compliance enforced through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`  

---

## 🧪 5. QA & Validation

Tests using these fixtures confirm:

- masking correctness  
- CRS/grid alignment  
- uncertainty-floor enforcements  
- correct H3 → raster application  
- preservation of governance metadata  
- correct STAC/DCAT governance metadata creation  
- accurate PROV-O lineage export  
- deterministic behavior across runs  
- no leakage of sensitive patterns  

Fixtures support tests in:

```
docs/data/satellites/smap/transforms/governance/tests/
```

---

## 🔁 6. Context in Full SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking  (validated here)
 → STAC/DCAT dataset creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

Governance fixtures validate the **final safety gate** before SMAP data is released.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Safeguards water-cycle indicators within sovereign areas.

### Climate  
Protects vegetation-water, drought, and FT patterns.

### Archaeology  
Prevents accidental exposure of culturally sensitive landscapes.

### Story Node v3  
Provides governance-backed narrative constraints (“This region is masked due to sovereignty rules”).

### Focus Mode v3  
Constraints AI reasoning to sovereignty-safe evidence only.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial governance-fixture README; emoji-rich; CARE/H3 aligned; sovereignty floors; STAC/PROV-compliant; CI-safe. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Governance Tests](../README.md) · [🛡 Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

