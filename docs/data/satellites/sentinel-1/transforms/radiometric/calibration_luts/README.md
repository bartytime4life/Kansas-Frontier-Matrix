---
title: "📁 Sentinel-1 Radiometric Calibration LUTs — Reference Tables for σ⁰ VV/VH Calibration"
path: "docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Calibration Assets)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A"
indigenous_rights_flag: false
sensitivity_level: "Low"
risk_category: "Low"
public_exposure_risk: "Low"
redaction_required: false

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-calibration-lut-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-calibration-lut-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-radiometric-luts:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-radiometric-luts"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA LUT release"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Radiometric Calibration LUTs**  
`docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/`

Lookup tables (LUTs) used by the **radiometric calibration transform** to convert  
raw amplitude into **σ⁰ VV/VH backscatter** for all Sentinel-1 products in KFM.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/
├── 📄 README.md
│
├── 📄 lut_vv.json                 # ESA VV calibration LUT (current version)
├── 📄 lut_vh.json                 # ESA VH calibration LUT (current version)
│
└── 📁 history/                    # Archived LUT versions from ESA updates
    ├── 📄 README.md
    ├── 📄 lut_vv_2023.json
    ├── 📄 lut_vv_2024.json
    ├── 📄 lut_vh_2023.json
    └── 📄 lut_vh_2024.json
~~~

---

## 📘 2. Purpose

This directory stores **ESA radiometric calibration lookup tables (LUTs)** used by the  
Sentinel-1 σ⁰ calibration stage. These LUTs combine:

- radiometric gain/offset curves  
- incidence-angle sensitivity adjustments  
- antenna-pattern corrections  
- long-term calibration consistency parameters  
- instrument-drift compensation terms  

The radiometric transform uses these LUTs when converting **raw amplitude** to **σ⁰ VV/VH**.  
They are required inputs for:

- GRD / GRDH generation  
- RTC γ⁰ generation  
- all downstream coherence / flood / wetlands / deformation products (indirectly)

---

## 🧩 3. LUT Schema (Conceptual)

Each LUT JSON is structured to include, at minimum:

- `polarization` — `"VV"` or `"VH"`  
- `lut_version` — e.g. `"2025.1"`  
- `source` — typically `"ESA"`  
- `validity_start`, `validity_end` — ISO timestamps for LUT applicability  
- `angles[]` — incidence angles (degrees)  
- `gain_values[]` — per-angle calibration gains  
- `offset_values[]` — additive corrections  

Exact schema is enforced via:

- `sentinel1-calibration-lut-v11.json`  
- `sentinel1-calibration-lut-v11-shape.ttl`

---

## 🔗 4. Provenance & Lineage (PROV-O)

Each LUT is treated as a **prov:Entity** in the calibration pipeline so that:

- σ⁰ VV/VH products can declare which LUT version was used  
- downstream RTC / flood / wetlands / deformation products retain a reference to LUT usage  
- audits can reproduce radiometric conditions for a given release

Typical provenance usage in the calibration stage:

- `prov:used` → `lut_vv.json`, `lut_vh.json`  
- `prov:wasGeneratedBy` → `s1_radiometric_calibration` activity  

---

## 🔐 5. FAIR+CARE & Sovereignty Notes

Calibration LUTs:

- contain **no direct spatial or cultural information**  
- are considered **CARE-A**  
- require **no sovereignty masking**  
- must remain immutable once a release is tagged (versioned in `history/`)  

Even though these LUTs themselves are low-risk, they are crucial for  
**transparent, reproducible SAR processing** and must be fully documented.

---

## 🧪 6. CI Validation Requirements

KFM CI validates LUT files by:

- JSON Schema + SHACL validation  
- numeric sanity checks (no NaNs, no invalid angles)  
- angle array and gain/offset array length consistency  
- monotonic angle ordering  
- version-history integrity (`history/` vs current files)  

Any LUT schema or numeric failure blocks calibration-transform changes.

---

## 🧭 7. Version History

| Version | Date       | Summary                                                                |
|--------:|------------|------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Fixed single-box formatting; strict emoji layout; LUT docs stabilized. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Radiometric Tests](../tests/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

