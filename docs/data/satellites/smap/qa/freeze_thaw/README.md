---
title: "🌡️ NASA SMAP — Freeze–Thaw QA Layer (FT Classification Reliability · Seasonal Boundaries · Ambiguity Masks)"
path: "docs/data/satellites/smap/qa/freeze_thaw/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · SMAP QA Subcommittee · FAIR+CARE Council"
status: "Active / Enforced"

classification: "Public QA Dataset Layer"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I2-R4"
care_label: "CARE-A / CARE-B"
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
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-ft-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-ft-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:freeze-thaw-qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-freeze-thaw-qa"
event_source_id: "ledger:docs/data/satellites/smap/qa/freeze_thaw/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next FT QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌡️ **NASA SMAP — Freeze–Thaw (FT) QA Layer**  
`docs/data/satellites/smap/qa/freeze_thaw/README.md`

**Purpose**  
Document the **Freeze–Thaw Retrieval QA Layer**, which quantifies the reliability of SMAP’s  
FT classification, especially around seasonal boundaries, ambiguous transitions, and  
mixed-pixel conditions.  
This QA layer is essential for uncertainty propagation, sovereign masking, and  
environmental narrative accuracy in Story Node v3 and Focus Mode v3.

</div>

---

## 📘 1. Overview

FT QA measures the confidence of pixel-level FT state classification:

- 🌡️ *Frozen*  
- 💧 *Thawed*  
- ⚠️ *Ambiguous / transitional*  
- 🎚️ Confidence score (0–100 or normalized scale)

FT QA feeds into:

- ETL Stage 4: QA/RFI Integration  
- ETL Stage 5: Uncertainty Propagation  
- ETL Stage 6: Sovereignty Masking  
- STAC Item QA metadata  
- Story Node v3 seasonal narratives  
- Focus Mode v3 classification reliability scoring  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/freeze_thaw/
├── 📄 README.md                           # This file
│
├── 🌡️ freeze_thaw_conf.tif                 # FT retrieval confidence raster
├── ⚠️ ft_qa_mask.tif                       # Ambiguity mask (low-confidence or mixed pixels)
├── 📑 metadata.json                        # STAC/DCAT metadata (QA schema + governance)
│
├── 🧪 tests/                               # FT QA validation suite
│   ├── test_ft_confidence_ranges.py
│   ├── test_ft_ambiguity_mask.py
│   ├── test_ft_metadata_integrity.py
│   ├── test_governance_preservation.py
│   └── fixtures/
│       ├── sample_ft_conf.tif
│       ├── sample_ft_qa_mask.tif
│       ├── sample_metadata.json
│       ├── expected_ft_interpretation.json
│       └── schema_expected.json
~~~

---

## 🧩 3. FT QA Responsibilities

### 🎚️ Confidence Scoring  
FT confidence scores reflect:

- retrieval algorithm stability  
- vegetation attenuation  
- radiometer noise  
- RFI effects  
- seasonal edge conditions  

### ⚠️ Ambiguity Mask  
Flags pixels where classification is unreliable due to:

- mixed freeze–thaw states  
- snow/rain contamination  
- canopy interference  
- transitional periods (spring/fall)  

### 🗺️ Spatial Integration  
Integrates with:

- soil moisture time series  
- vegetation water content  
- uncertainty grids  
- sovereignty masking  

### 📉 Uncertainty Scaling  
Ambiguous FT pixels increase uncertainty in ETL Stage 5.

---

## 🔐 4. Governance, FAIR+CARE & Sovereignty Rules

FT behavior in Indigenous territories must be handled with extra care because:

- FT boundaries may reveal ecological-sensitive transitions  
- low-confidence FT regions may correlate with cultural land-use  
- ambiguous seasonal zones should be generalized  

Thus:

- `"kfm:h3_sensitive"` must propagate  
- `"kfm:mask_required"` triggered in sovereign H3 zones  
- `"kfm:care_label"` preserved  
- `"kfm:sovereignty_uncertainty_floor"` upheld  
- `"kfm:governance_notes"` included  

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  

---

## 🧪 5. QA & Validation Requirements

The FT QA dataset must:

- contain only valid confidence ranges  
- align spatially with base rasters  
- contain meaningful QA mask values  
- include complete STAC/DCAT metadata  
- correctly propagate sovereignty + CARE metadata  
- integrate cleanly into uncertainty propagation  
- include valid PROV-O lineage fields  

Any FT QA issue halts dataset release.

---

## 🔁 6. FT QA in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → FT retrieval QA (this layer)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Stable, reliable freeze–thaw state informs infiltration + runoff modeling.

### Climate  
Seasonal freeze lines and transitions impact ecological and hazard layers.

### Archaeology  
FT patterns interact with cultural landscape analysis.

### Story Node v3  
Narratives integrate sovereign-safe FT seasonal context.

### Focus Mode v3  
FT confidence influences explanation sensitivity indicators.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|------------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Freeze–Thaw QA dataset README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🌡️ FT QA Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

