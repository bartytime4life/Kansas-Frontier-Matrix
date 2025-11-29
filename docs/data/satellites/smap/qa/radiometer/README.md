---
title: "⚠️ NASA SMAP — Radiometer QA Layer (Beam Health · Channel Integrity · L1-L3 QA Codes)"
path: "docs/data/satellites/smap/qa/radiometer/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council Oversight"
status: "Active / Enforced"

classification: "Public QA Dataset Layer"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B (depending on downstream governance)"
indigenous_rights_flag: true
sensitivity_level: "Low–Medium"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-radiometer-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-radiometer-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:radiometer-qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-radiometer-qa"
event_source_id: "ledger:docs/data/satellites/smap/qa/radiometer/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded with next QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# ⚠️ **SMAP Radiometer QA Layer — Beam Health & L1/L2/L3 Quality Flags**  
`docs/data/satellites/smap/qa/radiometer/README.md`

**Purpose**  
Document the **Radiometer QA outputs** derived from NASA SMAP L1–L3 products,  
after harmonization through KFM’s ETL pipeline.  
These QA layers underpin soil moisture, freeze–thaw, VWC, and uncertainty reliability  
within KFM.

</div>

---

## 📘 1. Overview

The **Radiometer QA Layer** provides:

- ⚠️ beam-level QA masks (L1)  
- 🔧 channel integrity diagnostics (A/B channels, L1B_TB)  
- 🛰️ surface condition flags (snow, rain, interference signals)  
- 📡 RFI susceptibility indicators  
- 🎚️ usable-pixel flags for L2/L3 retrievals  
- 🧮 retrieval-confidence modifiers  
- 📉 QA-derived uncertainty weighting factors  

Radiometer QA feeds directly into:

- ETL Stage 4 (QA/RFI integration)  
- ETL Stage 5 (Uncertainty propagation)  
- Story Node v3 environmental reliability  
- Focus Mode v3 evidence scoring  
- STAC metadata’s `kfm:qa_values` and `kfm:qa_flag_schema`  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/radiometer/
├── 📄 README.md                       # This file
│
├── ⚠️ qa_flags.tif                    # Radiometer QA mask (synthetic or real SMAP-derived)
├── 📝 qa_codes.json                   # Code → meaning mapping (KFM Unified QA schema)
├── 📑 metadata.json                   # DCAT/STAC governance metadata for QA layer
│
├── 🧪 tests/                           # Radiometer-level QA validation suite
│   ├── test_qa_flag_values.py
│   ├── test_qa_decoding.py
│   ├── test_radiometer_mask_alignment.py
│   └── fixtures/
│       ├── sample_qa_flags.tif
│       ├── sample_qa_codes.json
│       ├── sample_metadata.json
│       ├── sample_expected_mask.json
│       └── schema_expected.json
~~~

---

## 🧩 3. Radiometer QA Responsibilities

### ✓ Beam & Channel QA  
Covers:

- beam saturation  
- missing radiances  
- calibration error flags  
- ascending/descending pass artifacts  
- known instrument anomalies  

### ✓ RFI Susceptibility  
- RFI detection likelihood  
- channels likely corrupted  
- spatial consistency checks  

### ✓ Surface Condition QA  
- snow contamination  
- rain contamination  
- ice  
- wet-surface anomalies  

### ✓ Retrieval QA (L2/L3)  
Ensures downstream soil moisture, FT, VWC retrievals only use “usable” pixels.

### ✓ Uncertainty Modifiers  
QA contributes uncertainty-scaling factors for ETL Stage 5.

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Considerations

Radiometer QA may impact sovereign geographies if:

- QA flags imply sensitive environmental changes  
- RFI zones overlap with tribal territories  
- Pixel-level QA implies operational hazards  

Thus:

- `"kfm:h3_sensitive"` must propagate  
- `"kfm:mask_required"` applied when QA intersects sovereign lands  
- `"kfm:care_label"` retained  
- `"kfm:sovereignty_uncertainty_floor"` unchanged  

Governance validation runs via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

Validation ensures:

- correct QA decoding  
- no NaNs or invalid flag ranges  
- proper CRS & geolocation alignment  
- STAC metadata correctness  
- uncertainty & QA metadata sync  
- full governance metadata coverage  

Any invalid QA mask → **hard pipeline block**.

---

## 🔁 6. Role in the SMAP ETL Chain

~~~text
decode (L1B_TB)
 → reprojection
 → calibration
 → QA/RFI integration (uses radiometer QA)
 → uncertainty propagation
 → governance masking
 → provenance building
 → STAC Writer
 → final QA dataset (this directory)
~~~

Radiometer QA is foundational for all later reliability layers.

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Remove suspected wetness anomalies.

### Climate  
Improve FT and VWC classification stability.

### Archaeology  
Avoid misinterpreting low-quality environmental signals.

### Story Node v3  
Improve narrative confidence scoring.

### Focus Mode v3  
Factor QA into environmental evidence weighting.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP Radiometer QA dataset README; STAC/DCAT/PROV-ready; governance/H3 aligned; CI-safe.     |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [⚠️ QA Root](../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

