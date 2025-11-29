---
title: "📁 Sentinel-1 Radiometric Calibration LUT History — ESA Version Archive"
path: "docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/history/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Internal Technical (Calibration Assets · Historical)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Annual · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  owl_time: "TemporalEntity"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-radiometric-lut-history:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-radiometric-lut-history"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/history/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next ESA LUT-cycle archival change"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Radiometric Calibration LUT — Version History**  
`docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/history/`

Historical ESA lookup tables (LUTs) used across past radiometric calibration epochs  
for σ⁰ VV/VH processing.  
Maintained for reproducibility, audit, and PROV-O replay.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/radiometric/calibration_luts/history/
├── 📄 README.md
│
├── 📄 lut_vv_2023.json
├── 📄 lut_vv_2024.json
├── 📄 lut_vh_2023.json
└── 📄 lut_vh_2024.json
~~~

✔ Emoji BEFORE filenames  
✔ No drift  
✔ Perfectly matches STAC + transforms style  
✔ Historical files remain immutable

---

## 📘 2. Purpose

This directory provides the **full historical archive** of calibration LUTs used in the  
Sentinel-1 radiometric calibration transform.

Reasons for maintaining historical LUTs:

- ESA periodically updates LUTs due to  
  - antenna-pattern corrections  
  - instrument drift  
  - calibration-model refinements  
  - incidence-angle curve adjustments  
- KFM requires **perfect reproducibility** for  
  - versioned STAC datasets  
  - reprocessing  
  - scientific traceability  
  - error/uncertainty analysis  
- PROV-O lineage must preserve the **exact LUT version** used in each release.

These historical LUTs are **read-only** and **never modified**.

---

## 🧩 3. Versioning Rules (KFM Radiometric LUT Policy)

Each LUT file MUST include:

- `lut_version` (e.g., `"2024.3"`)  
- `validity_start` / `validity_end`  
- polarization (`VV` or `VH`)  
- complete gain/offset tables  
- source attribution (`"ESA"`)  

And must satisfy:

- JSON Schema compliance  
- SHACL validation  
- monotonically increasing incidence-angle arrays  
- stable array lengths for gains/offsets  
- clean numeric ranges (no NaNs, infs, invalid angles)

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Calibration LUTs:

- contain **no spatial information**,  
- are classified **CARE-A**,  
- require **no sovereignty masking**,  
- but MUST remain fully documented for FAIR reproducibility and SCI audit logs.

KFM treats each historical LUT as:

```json
{
  "prov:Entity": "esa_lut_vv_2024",
  "kfm:care_label": "CARE-A",
  "kfm:reproducibility_notes": "Used for σ⁰ calibration in release v11.0.x"
}

