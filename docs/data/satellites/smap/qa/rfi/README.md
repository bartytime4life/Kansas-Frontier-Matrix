---
title: "📡 NASA SMAP — RFI QA Layer (Radio Frequency Interference · Contamination Masks · Bitfield Decoding)"
path: "docs/data/satellites/smap/qa/rfi/README.md"
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

data_steward: "SMAP QA Subcommittee · Earth Systems Group · FAIR+CARE Council"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  schema_org: "Dataset"
  owl_time: "TemporalEntity"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../schemas/json/smap-rfi-qa-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-rfi-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:rfi-qa-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-rfi-qa"
event_source_id: "ledger:docs/data/satellites/smap/qa/rfi/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "48 months"
sunset_policy: "Superseded upon RFI schema update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📡 **NASA SMAP — RFI QA Layer (Radio Frequency Interference Masking)**  
`docs/data/satellites/smap/qa/rfi/README.md`

**Purpose**  
Document the **RFI (Radio Frequency Interference) QA mask layer** derived from NASA SMAP  
radiometry (L1–L3), harmonized through KFM’s governed ETL.  
RFI represents one of the most significant contamination sources in SMAP products,  
impacting soil moisture, freeze–thaw, VWC, and uncertainty reliability.

</div>

---

## 📘 1. Overview

The **SMAP RFI QA Layer** provides:

- 📡 RFI bitfield decoding  
- 🚨 interference-likelihood classification  
- 🛰️ per-pixel RFI contamination status  
- ⚠️ downstream usability flags  
- 🎚️ uncertainty-scaling factors for contaminated zones  
- 🔗 STAC governance metadata integration  
- 🛡 sovereignty-aware masking rules  

RFI QA directly impacts:

- QA/RFI integration (ETL Stage 4)  
- Uncertainty propagation (Stage 5)  
- Governance masking (Stage 6)  
- PROV lineage (Stage 7)  
- STAC Writer (Stage 8)  
- Focus Mode v3’s reliability weighting  
- Story Node v3’s environmental context reliability  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/qa/rfi/
├── 📄 README.md                           # This file
│
├── 📡 rfi_mask.tif                       # RFI contamination mask (synthetic or SMAP-derived)
├── 📝 rfi_codes.json                      # Bitfield → semantic meaning (KFM unified RFI schema)
├── 📑 metadata.json                       # STAC/DCAT metadata for RFI layer
│
├── 🧪 tests/                               # RFI QA validation suite
│   ├── test_rfi_flag_values.py
│   ├── test_rfi_decoding.py
│   ├── test_rfi_mask_alignment.py
│   ├── test_rfi_metadata.py
│   └── fixtures/
│       ├── sample_rfi_mask.tif
│       ├── sample_rfi_codes.json
│       ├── sample_metadata.json
│       ├── expected_rfi_interpretation.json
│       └── schema_expected.json
~~~

---

## 🧩 3. What RFI QA Represents

### 📡 RFI Bitfield Interpretation  
SMAP radiometer QA captures:

- **Direct RFI detection**  
- **Probability of contamination**  
- **Spectral anomalies**  
- **Beam-by-beam interference signatures**  
- **Channel A/B contamination differences**  

### 🚨 RFI Contamination Mask  
A synthesized, ETL-governed mask:

- marks unusable pixels  
- flags contaminated regions  
- integrates with freeze–thaw/VWC masks  
- feeds uncertainty propagation  
- influences governance masks in sovereign lands  

### 🎚️ Uncertainty Scaling  
RFI → increased uncertainty multipliers for ETL Stage 5:

- partial → moderate boost  
- strong → significant boost  
- ambiguous → mild boost  
- clear → no boost  

### 🗺️ Downstream Impact  
RFI QA affects:

- soil moisture integrity  
- environmental anomalies  
- freeze–thaw thresholds  
- VWC validity  
- Story Node v3 behavioral context  

---

## 🔐 4. Governance, Sovereignty & FAIR+CARE Rules

RFI QA interacts with sovereignty in cases where:

- interference patterns intersect tribal lands  
- RFI-driven uncertainty may imply sensitive environmental information  
- spatial patterns require aggregation/generalization  

Thus:

- `"kfm:h3_sensitive"` must propagate  
- `"kfm:mask_required"` triggered where needed  
- `"kfm:care_label"` preserved  
- `"kfm:sovereignty_uncertainty_floor"` applied  
- `"kfm:governance_notes"` attached  

RFI QA **must not** reveal any precise signals inside sensitive H3 regions.

Governance validated via:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`  
- `data_pipeline.yml`

---

## 🧪 5. QA & Validation Requirements

Tests confirm:

- valid bitfield ranges  
- correct decoding (sample_rfi_codes.json)  
- alignment with base raster grids  
- STAC governance metadata correctness  
- DCAT QA field integrity  
- uncertainty-scaling logic  
- synchronous QA/uncertainty alignment  
- sovereignty-safe masking  
- deterministic outputs  

Any mismatch → **hard CI block**.

---

## 🔁 6. Role in the SMAP ETL Pipeline

~~~text
decode
 → reprojection
 → calibration
 → QA/RFI integration (this QA layer is central)
 → uncertainty propagation
 → governance masking
 → provenance building
 → stac_writer
 → RFI QA dataset layer (this directory)
~~~

RFI QA sits at the **core** of QA-driven reliability modeling.

---

## 🔮 7. Applications in KFM

### Hydrology  
Removes interference-driven soil-moisture anomalies.

### Climate  
Prevents RFI-driven FT/VWC misclassification.

### Archaeology  
Mitigates misinterpretation risks in sensitive landscapes.

### Story Node v3  
Evidence-scoring incorporates RFI-based confidence.

### Focus Mode v3  
Weighted environmental explanations include RFI reliability.

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial SMAP RFI QA dataset README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV-ready; CI-safe; emoji-rich.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📡 RFI QA Tests](./tests/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

