---
title: "🧪 NASA SMAP — Governance & Sovereignty Masking Test Suite (CARE/H3 Enforcement) · ETL Stage 6"
path: "docs/data/satellites/smap/transforms/governance/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Sovereignty Working Group"
status: "Active / Enforced"

classification: "Public ETL Governance Test Documentation"
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

fair_category: "F1-A3-I2-R5"
care_label: "CARE-A / CARE-B (High-Sensitivity Governance Stage)"
indigenous_rights_flag: true
sensitivity_level: "High"
public_exposure_risk: "Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "FAIR+CARE Council · Sovereignty Working Group · Earth Systems Governance Subcommittee"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  geosparql: "geo:FeatureCollection"
  owl_time: "ProperInterval"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-governance-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-governance-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:governance-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-governance-tests"
event_source_id: "ledger:docs/data/satellites/smap/transforms/governance/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next governance-rule update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **NASA SMAP — Governance & Sovereignty Masking Test Suite (ETL Stage 6)**  
`docs/data/satellites/smap/transforms/governance/tests/README.md`

**Purpose**  
Validate **ethical correctness, sovereignty compliance, CARE label enforcement, H3 masking,  
uncertainty-floor preservation, and STAC/DCAT/PROV-O governance metadata** for the  
SMAP Governance & Masking Stage (ETL Stage 6).  
This ensures that no SMAP-derived dataset can reach the public or downstream systems  
unless it satisfies all KFM governance and Indigenous data sovereignty rules.

</div>

---

## 📘 1. Suite Overview

These tests validate that SMAP ETL Stage 6:

- 🔐 Applies H3-based sovereignty masking correctly  
- 🛡️ Preserves CARE labels through all transformations  
- 🌐 Maintains H3 sovereignty flags across raster operations  
- 📉 Applies sovereignty-aware uncertainty floors  
- 🧭 Generalizes spatial detail in sensitive areas  
- ⚠️ Prevents exposure of precise environmental values in INDIGENOUS PROTECTED REGIONS  
- 🧾 Inserts full governance metadata into STAC/DCAT outputs  
- 🧬 Records complete PROV-O governance lineage  
- 🛑 Blocks release of any dataset violating sovereignty or CARE policies  

All tests MUST pass for SMAP products to enter KFM's downstream layers  
(Story Nodes, Focus Mode, historical analyses, climate overlays, etc.).

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/transforms/governance/tests/
├── 📄 README.md                                      # This file
│
├── 🧪 test_masking.py                                # Tests H3 masking & spatial generalization
├── 🧪 test_h3_propagation.py                          # Ensures H3 sovereignty flags survive transforms
├── 🧪 test_care_preservation.py                       # CARE label preservation tests
├── 🧪 test_uncertainty_floor.py                       # Sovereignty-aware uncertainty-floor validation
├── 🧪 test_governance_metadata.py                     # STAC/DCAT governance metadata correctness
│
└── 🔧 fixtures/                                       # Synthetic governance test inputs
    ├── sample_pre_mask.tif
    ├── sample_post_mask_expected.tif
    ├── synthetic_h3_mask.json
    ├── governance_metadata_stub.json
    └── schema_expected.json
~~~

---

## 🧩 3. Test Domains

### 🔐 **H3 Sovereignty Masking**
Validates:

- correct masking of all sovereign H3 cells  
- correct spatial generalization  
- CRS- and pixel-alignment consistency  
- H3 indexing correctness  
- correct `"kfm:mask_required"` population  

### 🛡️ **CARE Label Enforcement**
Tests:

- preservation and propagation of CARE labels  
- `"kfm:care_label_reason"` correctness  
- no accidental removal of high-sensitivity CARE-B labels  

### 🧭 **Governance Metadata**
Validates:

- `kfm:h3_sensitive` present where required  
- `kfm:sovereignty-mask` correctness  
- all STAC governance fields present  
- DCAT sensitivity metadata correctness  
- correct JSON-LD/PROV annotations  

### 📉 **Uncertainty-Floor Enforcement**
Ensures:

- sovereignty-aware uncertainty floors applied  
- uncertainty never decreases in sensitive regions  
- floors match policy definitions  
- correct `"kfm:sovereignty_uncertainty_floor"` values  

### 🛑 **Forbidden Behaviors Tests**
Fails if:

- precise environmental values remain exposed in H3 zones  
- uncertainty decreases in sensitive areas  
- CARE or sovereignty flags disappear  
- governance lineage is incomplete  
- any masking rule produces invalid geometries  

---

## 🔐 4. Governance, FAIR+CARE, and Sovereignty Enforcement

These tests ensure ETL Stage 6 respects:

- Indigenous rights & data sovereignty  
- Care & custody responsibilities over environmental context datasets  
- Non-exposure of sensitive geospatial information  
- Ethical uncertainty communication  
- Transparency in masking & generalization decisions  
- Reproducibility and clear audit trails  

Governance validation run under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `data_pipeline.yml`  
- `stac_validate.yml`

Any violation blocks the entire SMAP pipeline.

---

## 🧪 5. CI Integration

This test suite executes under:

- **ci.yml**  
- **data_pipeline.yml**  
- **faircare_validate.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**

These ensure that governance logic is **non-optional** and **strictly enforced**.

---

## 🔁 6. Governance Stage in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → uncertainty propagation
 → governance masking  (this test suite)
 → STAC/DCAT creation
 → PROV-O lineage export
 → OpenLineage telemetry
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
Protected wetness, soil-layer, floodplain, and freeze–thaw signals.

### Climate  
Sovereignty-safe vegetation, drought, and VWC anomaly layers.

### Archaeology  
Ethically masked environmental reconstructions of sensitive cultural landscapes.

### Story Node v3  
Narratives showing “masked/aggregated environmental contexts” with governance explanations.

### Focus Mode v3  
Context-aware environmental reasoning grounded in sovereignty & CARE policies.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                     |
|--------:|------------|-------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | First complete governance-mask test suite; emoji-rich; H3/CARE enforcement; PROV/STAC/DCAT aligned; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Governance Fixtures](../fixtures/README.md) · [🛡 Standards](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

