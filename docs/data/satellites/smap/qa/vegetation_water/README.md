---
title: "🌱 NASA SMAP — Vegetation Water Content (VWC) QA Layer (Retrieval Confidence · Ambiguity · Sovereignty-Safe)"
path: "docs/data/satellites/smap/qa/vegetation_water/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public QA Dataset Layer"
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
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-vwc-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-vwc-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:vwc-qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-vwc-qa"
event_source_id: "ledger:docs/data/satellites/smap/qa/vegetation_water/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon next VWC QA revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌱 **NASA SMAP — Vegetation Water Content (VWC) Retrieval QA Layer**  
`docs/data/satellites/smap/qa/vegetation_water/README.md`

**Purpose**  
Document the **Vegetation Water Content (VWC) Retrieval QA Layer**, which quantifies  
the reliability of SMAP vegetation-water retrievals and identifies ambiguous, noisy,  
or ecologically sensitive pixels requiring governance-safe treatment.

</div>

---

## 📘 1. Overview

The VWC QA layer measures **pixel-level retrieval confidence** for vegetation water content:

- 🌱 VWC reliability under canopy density  
- 🎚️ retrieval noise in mixed soil–canopy pixels  
- 📡 RFI influence on retrieval stability  
- 🌤️ atmospheric contamination patterns  
- ❄️ seasonal FT interference with VWC estimation  
- ⚠️ ambiguous / low-confidence retrieval zones  

This QA layer directly supports:

- ETL Stage 4 — QA/RFI Integration  
- ETL Stage 5 — Uncertainty Propagation  
- ETL Stage 6 — Sovereignty Masking  
- Story Node v3 environmental narratives  
- Focus Mode v3 reliability scoring  
- STAC/DCAT QA summaries & metadata  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/vegetation_water/
├── 📄 README.md                              # This file
│
├── 🌱 vwc_conf.tif                            # VWC retrieval confidence (synthetic or ETL product)
├── ⚠️ vwc_qa_mask.tif                         # Low-confidence / ambiguous retrieval mask
├── 📑 metadata.json                           # STAC/DCAT QA schema + governance metadata
│
├── 🧪 tests/                                  # VWC QA validation suite
│   ├── test_vwc_confidence.py
│   ├── test_vwc_ambiguity_mask.py
│   ├── test_vwc_metadata_integrity.py
│   ├── test_governance_preservation.py
│   └── fixtures/
│       ├── sample_vwc_conf.tif
│       ├── sample_vwc_qa_mask.tif
│       ├── sample_metadata.json
│       ├── expected_vwc_interpretation.json
│       └── schema_expected.json
~~~

---

## 🧩 3. VWC QA Responsibilities

### 🌱 VWC Retrieval Confidence  
Captures the retrieval algorithm’s reliability under:

- high biomass density  
- mixed pixels (soil + canopy)  
- sensor angle limitations  
- atmospheric moisture interference  
- seasonal FT state interactions  

### ⚠️ Ambiguity / Low-Confidence Mask  
Marks pixels where VWC retrieval is **unreliable**, including:

- dense canopy saturation  
- noisy radiometer signals  
- RFI-driven degradation  
- mixed FT → VWC misinterpretation  
- ecologically sensitive or unstable transition zones  

### 🎚️ Downstream Uncertainty Integration  
VWC QA contributes uncertainty scaling for ETL Stage 5:

- low confidence → strong uncertainty multiplier  
- medium confidence → moderate multiplier  
- high confidence → limited or no modification  

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Rules

VWC QA data intersects sovereignty concerns when:

- vegetation transitions overlap Indigenous ecological lands  
- canopy density changes correlate with cultural or land-use patterns  
- confidence variability might reveal sensitive ecological states  

Thus VWC QA MUST:

- propagate `"kfm:h3_sensitive"`  
- apply `"kfm:mask_required"` in sovereign H3 regions  
- preserve `"kfm:care_label"`  
- maintain `"kfm:sovereignty_uncertainty_floor"`  
- document `"kfm:governance_notes"`  
- avoid over-precision in sovereign territories  

Compliance validated under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation Requirements

VWC QA dataset must:

- contain valid confidence ranges  
- align spatially with processed SMAP rasters  
- produce stable ambiguity masks  
- include full STAC/DCAT QA metadata  
- reflect sovereignty-safe behavior  
- include complete PROV-O lineage  
- integrate deterministically with uncertainty propagation  

Any issue → **hard CI block**.

---

## 🔁 6. VWC QA in SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration
 → VWC retrieval QA (this layer)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
~~~

---

## 🔮 7. Applications Inside KFM

### Hydrology  
Vegetation water patterns improve attribution of moisture anomalies.

### Climate  
VWC informs seasonal & drought cycle modeling.

### Archaeology  
VWC QA provides safer environmental layers near cultural landscapes.

### Story Node v3  
Narratives use QA-weighted vegetation signals.

### Focus Mode v3  
Confidence levels influence explanation depth.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial VWC QA README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.                   |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🌱 VWC QA Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

