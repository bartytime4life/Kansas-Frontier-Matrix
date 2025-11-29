---
title: "🧪 NASA SMAP — Vegetation Water Content (VWC) Retrieval QA Test Suite (Confidence · Ambiguity · Governance)"
path: "docs/data/satellites/smap/qa/vegetation_water/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public QA Test Documentation"
status: "Active / Enforced"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"

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

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "SoftwareTest"
  prov_o: "prov:Activity"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-vwc-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-vwc-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc-qa-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-qa-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/vegetation_water/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next VWC QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP Vegetation Water Content (VWC) Retrieval QA Test Suite**  
`docs/data/satellites/smap/qa/vegetation_water/tests/README.md`

**Purpose**  
Validate the **VWC Retrieval QA** dataset produced by KFM’s governed ETL.  
Ensures pixel-level confidence, ambiguity masks, governance metadata,  
and sovereignty-protected outputs are correct, deterministic, and compliant with  
KFM v11.2 requirements.

</div>

---

## 📘 1. Overview

This test suite verifies that VWC QA:

- 🌱 correctly interprets VWC retrieval confidence  
- 🎚️ applies valid confidence ranges & semantics  
- ⚠️ correctly identifies ambiguous or unstable retrieval zones  
- 🗺️ aligns spatially with SMAP core rasters  
- 🛡 enforces sovereignty masking (`kfm:mask_required`)  
- 📑 preserves CARE labels + governance metadata  
- 🔗 embeds complete PROV-O lineage  
- 📦 passes STAC/DCAT QA metadata requirements  
- 🚫 never exposes high-resolution or sensitive ecological boundaries  

Any issue → **KFM blocks VWC QA dataset release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/vegetation_water/tests/
├── 📄 README.md                                  # This file
│
├── 🧪 test_vwc_confidence.py                     # Validate VWC retrieval confidence values
├── 🧪 test_vwc_ambiguity_mask.py                 # Validate VWC low-confidence/ambiguous zones
├── 🧪 test_vwc_metadata_integrity.py             # STAC/DCAT metadata correctness
├── 🧪 test_governance_preservation.py            # CARE/H3 sovereignty preservation
│
└── 🔧 fixtures/
    ├── sample_vwc_conf.tif                       # Synthetic VWC confidence raster
    ├── sample_vwc_qa_mask.tif                    # Low-confidence mask (synthetic)
    ├── sample_metadata.json                      # Metadata block
    ├── expected_vwc_interpretation.json          # Deterministic QA classification
    └── schema_expected.json                      # Strict validation schema
~~~

---

## 🧩 3. Test Domains & Responsibilities

### 🌱 **VWC Confidence Tests**
Validate:

- correct 0–100 or normalized QA ranges  
- canopy-driven confidence variation  
- stable behavior across tiles  
- sovereignty-safe behavior in synthetic protected zones  

---

### 🎚️ **Ambiguity Mask Tests**
Validate:

- noisy or mixed-pixel detection  
- dense canopy saturation handling  
- seasonal transition instability  
- RFI-induced retrieval ambiguity  
- integration with uncertainty propagation  

---

### 🗺️ **Spatial Alignment Tests**
Validate:

- CRS integrity  
- pixel alignment with SMAP base rasters  
- compatibility with FT/SM QA fields  
- H3 alignment for sovereignty masking  

---

### 📑 **Metadata Integrity Tests**
Validate:

- STAC QA schema (`kfm:qa_values`, VWC schema entries)  
- DCAT quality notes  
- CARE/sensitivity metadata fields  
- temporal + spatial extents  
- PROV-O lineage attachments  

---

### 🛡 **Governance Preservation Tests**
Validate:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

No field may be dropped or altered.

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Vegetation water patterns can correlate with culturally or ecologically sensitive landscapes.  
Therefore VWC QA must:

- generalize or mask confidence in sovereign H3 regions  
- enforce uncertainty floors  
- avoid over-precise classification  
- preserve all CARE metadata  
- embed `"kfm:governance_notes"` for masking actions  

Governance enforced by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

Runs under:

- **ci.yml**  
- **data_pipeline.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**  

Any failure results in **dataset block**.

---

## 🔁 6. Position in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → VWC retrieval QA (validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Across KFM

### Hydrology  
VWC confidence clarifies vegetation–soil interactions.

### Climate  
Informs drought, phenology, and fuel-moisture estimations.

### Archaeology  
Stabilizes environmental indicators near sensitive cultural landscapes.

### Story Node v3  
VWC retrieval QA supports narrative reliability.

### Focus Mode v3  
Confidence → explanation weighting & interpretive safety.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|--------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial VWC QA test-suite README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe; emoji-rich.      |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🌱 VWC QA Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

