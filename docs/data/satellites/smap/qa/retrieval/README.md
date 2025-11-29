---
title: "🎚️ NASA SMAP — Retrieval QA Layer (Soil Moisture · Freeze–Thaw · Vegetation Water Content)"
path: "docs/data/satellites/smap/qa/retrieval/README.md"
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
care_label: "CARE-A / CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium"
public_exposure_risk: "Low–Medium"
risk_category: "Medium"
redaction_required: true

data_steward: "SMAP QA Subcommittee · Earth Systems Working Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../schemas/json/smap-retrieval-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-retrieval-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:retrieval-qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-retrieval-qa"
event_source_id: "ledger:docs/data/satellites/smap/qa/retrieval/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon Retrieval QA schema upgrade"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🎚️ **NASA SMAP — Retrieval QA Layer**  
## Soil Moisture • Freeze–Thaw • Vegetation Water Content  
`docs/data/satellites/smap/qa/retrieval/README.md`

**Purpose**  
Document the **Retrieval QA Layer** derived from SMAP Level 2–3 retrievals (SM, FT, VWC).  
These QA products quantify retrieval reliability per pixel and directly influence  
uncertainty propagation, governance masking, and STAC metadata.

</div>

---

## 📘 1. Overview

The Retrieval QA Layer provides:

- 🎚️ **Soil Moisture retrieval confidence**  
- 🌡️ **Freeze–Thaw classification confidence**  
- 🌱 **Vegetation Water Content (VWC) retrieval confidence**  
- ⚠️ **Flags for low-quality or ambiguous retrievals**  
- 📉 **Pixel-level modifiers for uncertainty**  
- 🔗 **STAC/DCAT QA metadata fields**  
- 🛡 **CARE/H3 sovereignty-safe versions of retrieval QA**  
- 🧾 **PROV-O lineage for all retrieval QA entities**

Retrieval QA is essential for:

- ETL Stage 4 (QA integration)  
- ETL Stage 5 (Uncertainty propagation)  
- ETL Stage 6 (Governance masking)  
- KFM environmental modeling  
- Story Node v3 narratives  
- Focus Mode v3 contextual reasoning  

---

## 📂 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/retrieval/
├── 📄 README.md                               # This file
│
├── 🎚️ soil_moisture_conf.tif                  # Soil moisture retrieval confidence
├── 🌡️ freeze_thaw_conf.tif                     # Freeze–Thaw retrieval confidence
├── 🌱 vwc_conf.tif                             # Vegetation water content confidence
│
├── 📑 metadata.json                            # STAC/DCAT QA metadata (conf schema, governance)
│
├── 🧪 tests/                                    # Retrieval QA validation suite
│   ├── test_sm_confidence.py                   # Soil Moisture QA tests
│   ├── test_ft_confidence.py                   # Freeze–Thaw QA tests
│   ├── test_vwc_confidence.py                  # VWC QA tests
│   ├── test_metadata_integrity.py              # STAC/DCAT + governance metadata
│   └── fixtures/
│       ├── sample_sm_conf.tif
│       ├── sample_ft_conf.tif
│       ├── sample_vwc_conf.tif
│       ├── sample_metadata.json
│       ├── expected_sm_classification.json
│       ├── expected_ft_classification.json
│       ├── expected_vwc_classification.json
│       └── schema_expected.json
~~~

---

## 🧩 3. Retrieval QA Responsibilities

### 🎚️ Soil Moisture Retrieval Confidence  
Captures algorithm reliability for SM retrieval per pixel:

- instrument calibration drift  
- RFI-coupled uncertainty  
- vegetation attenuation  
- wet-surface effects  
- frozen soil interference  

### 🌡️ Freeze–Thaw Retrieval Confidence  
Identifies ambiguous or noisy FT transitions:

- early/late-season freeze–thaw boundaries  
- mixed-pixel contamination  
- RFI/atmospheric instability  

### 🌱 Vegetation Water Content Confidence  
Measures confidence in vegetation water content estimates:

- canopy structure  
- soil–canopy mixing  
- atmospheric perturbation  
- QC thresholds  

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Rules

Retrieval QA interacts with sovereignty concerns when:

- retrieval-confidence patterns reveal sensitive land-use  
- transitions (FT) overlap with tribal lands  
- VWC confidence reflects ecological/cultural boundaries  

Thus QA layers must enforce:

- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"` for sensitive H3 zones  
- `"kfm:care_label"` and `"kfm:care_label_reason"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  

And MUST NOT include:

- overly precise retrieval confidence in sovereign regions  
- speculative or low-support confidence estimates  

Governance validated by:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation Requirements

Validation ensures:

- correct confidence ranges  
- correct mapping to KFM unified QA schema  
- STAC compliance (`kfm:qa_values`, QA summaries)  
- spatial alignment integrity  
- uncertainty scaling integration  
- governance metadata presence  
- sovereignty-aware masking  
- temporal consistency  
- deterministic output  

Any QA errors → **release blocked**.

---

## 🔁 6. Role in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (this QA layer integrates here)
 → uncertainty propagation (uses retrieval QA)
 → governance masking
 → provenance building
 → stac_writer
 → retrieval QA dataset layer (this directory)
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Improve SM anomaly interpretation.

### Climate  
Better FT/VWC anomaly detection.

### Archaeology  
Reduce risk of misinterpreting noisy environmental states.

### Story Node v3  
Provide confidence-weighted contextual narratives.

### Focus Mode v3  
Confidence signals influence explanation detail & scoring.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                 |
|--------:|------------|---------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Retrieval QA README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.           |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🎚️ Retrieval QA Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

