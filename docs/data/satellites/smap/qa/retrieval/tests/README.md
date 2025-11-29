---
title: "🧪 NASA SMAP — Retrieval QA Test Suite (Soil Moisture · Freeze–Thaw · VWC)"
path: "docs/data/satellites/smap/qa/retrieval/tests/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public QA Test Documentation"
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

json_schema_ref: "../../../../../../../../schemas/json/tests-smap-retrieval-qa-v11.json"
shape_schema_ref: "../../../../../../../../schemas/shacl/tests-smap-retrieval-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-qa-tests-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-qa-tests"
event_source_id: "ledger:docs/data/satellites/smap/qa/retrieval/tests/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded on next QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **SMAP Retrieval QA Test Suite**  
`docs/data/satellites/smap/qa/retrieval/tests/README.md`

**Purpose**  
Validate **retrieval-level QA layers** for Soil Moisture, Freeze–Thaw, and VWC  
after KFM’s governed ETL processing.  
Ensures confidence rasters are **correct, aligned, governance-compliant, sovereign-safe**,  
and ready for **uncertainty propagation, provenance recording, and STAC publication**.

</div>

---

## 📘 1. Overview

This suite verifies that retrieval QA:

- 🎚️ correctly interprets retrieval confidence codes  
- 🌱 identifies low-confidence / ambiguous VWC pixels  
- 🌡️ identifies noisy FT transition pixels  
- 📊 propagates QA → uncertainty scaling rules  
- 🗺️ aligns spatially with radiometer & processed rasters  
- 🛡 carries CARE + sovereignty metadata (`kfm:*`)  
- 📑 passes STAC/DCAT metadata integrity checks  
- 🔗 embeds valid PROV-O lineage  
- 🚫 never exposes high-precision or sensitive retrieval cues in sovereign lands  

Any failure → **retrieval QA dataset is blocked from release**.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/retrieval/tests/
├── 📄 README.md                               # This file
│
├── 🧪 test_sm_confidence.py                    # Soil Moisture retrieval confidence tests
├── 🧪 test_ft_confidence.py                    # Freeze–Thaw confidence tests
├── 🧪 test_vwc_confidence.py                   # Vegetation Water Content confidence tests
├── 🧪 test_metadata_integrity.py               # STAC/DCAT + governance metadata tests
├── 🧪 test_governance_preservation.py          # CARE/H3 propagation & sovereignty rules
│
└── 🔧 fixtures/
    ├── sample_sm_conf.tif                      # Synthetic SM confidence layer
    ├── sample_ft_conf.tif                      # Synthetic FT confidence layer
    ├── sample_vwc_conf.tif                     # Synthetic VWC confidence layer
    ├── sample_metadata.json                    # QA metadata block
    ├── expected_sm_classification.json         # Expected SM confidence decoding
    ├── expected_ft_classification.json         # Expected FT confidence decoding
    ├── expected_vwc_classification.json        # Expected VWC confidence decoding
    └── schema_expected.json                    # Validation schema for fixtures & metadata
~~~

---

## 🧩 3. Test Domains & Responsibilities

### 🎚️ Soil Moisture Confidence Tests
Validate:

- confidence range correctness  
- handling of ambiguous retrievals  
- RFI/soil/snow contamination effects  
- alignment with uncertainty scaling rules  

### 🌡️ Freeze–Thaw Confidence Tests
Validate:

- ambiguous transition detection  
- season boundary instability  
- QA interaction with FT classification masks  
- sovereignty masking at sensitive boundaries  

### 🌱 VWC Confidence Tests
Validate:

- canopy-related retrieval instability  
- algorithm sensitivity in vegetated areas  
- ambiguous or low-confidence pixel clustering  
- expected sovereign safe-zones behavior  

### 📑 Metadata Integrity Tests
Validate:

- QA schema  
- STAC `kfm:qa_values`  
- DCAT quality notes  
- temporal + spatial extents  
- correct lineage references  

### 🛡 CARE & Sovereignty Preservation Tests
Validate:

- `"kfm:care_label"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:care_label_reason"`  
- `"kfm:governance_notes"`  

These metadata MUST propagate without loss.

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Retrieval QA interacts with sovereignty boundaries via:

- FT boundaries overlapping tribal ecologies  
- VWC patterns that could imply sensitive land use  
- confidence shifts in hydrological/cultural regions  

Thus tests enforce:

- sovereignty-generalized QA inside H3 zones  
- uncertainty floors not reduced  
- no precise retrieval confidences in restricted areas  
- correct governance masking behavior  

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. CI Integration

This suite runs under:

- **ci.yml**  
- **data_pipeline.yml**  
- **jsonld_validate.yml**  
- **stac_validate.yml**  
- **faircare_validate.yml**  

QA failure = **pipeline block**.

---

## 🔁 6. Role in Full SMAP ETL Chain

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → retrieval QA (validated here)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

Retrieval QA is central to downstream uncertainty and governance behavior.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Improved reliability of SM anomaly detection.

### Climate  
More trustworthy FT/VWC anomaly modeling.

### Archaeology  
Avoid misleading environmental interpretations.

### Story Node v3  
Retrieval QA informs narrative reliability scoring.

### Focus Mode v3  
Confidence weights influence entity reasoning.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                      |
|--------:|------------|---------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Retrieval QA Test Suite README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV ready; CI-safe; emoji-rich.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎯 Retrieval QA Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

