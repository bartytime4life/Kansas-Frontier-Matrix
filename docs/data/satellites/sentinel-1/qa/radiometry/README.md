---
title: "🧪 Sentinel-1 Radiometry QA — σ⁰ & γ⁰ Validation (Calibration · RTC · DEM Alignment · Incidence Angle Checks)"
path: "docs/data/satellites/sentinel-1/qa/radiometry/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B, Sovereignty-Influenced QA)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/sentinel1-radiometry-qa-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  owl_time: "Instant"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../schemas/json/sentinel1-radiometry-qa-v11.json"
shape_schema_ref: "../../../../schemas/shacl/sentinel1-radiometry-qa-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-radiometry:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-radiometry"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/radiometry/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded on next radiometry QA standard update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🧪 **Sentinel-1 Radiometry QA**  
`docs/data/satellites/sentinel-1/qa/radiometry/`

Quality-assurance routines validating **σ⁰ calibrated backscatter**,  
**γ⁰ RTC terrain-normalized backscatter**, **DEM alignment**, and  
**incidence-angle consistency** before any SAR derivative (coherence, flood, wetlands, deformation) is allowed downstream.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/radiometry/
├── 📄 README.md
│
├── 🧪 tests/                     # Radiometry QA test suite
│   ├── 🧪 test_sigma0_calibration.py
│   ├── 🧪 test_rtc_gamma0_consistency.py
│   └── 🧪 test_dem_incidence_alignment.py
│
└── 📁 fixtures/                  # Reference σ⁰, γ⁰, DEM-aligned rasters
    ├── 📄 sigma0_reference_vv.tif
    ├── 🌍 gamma0_reference_vv.tif
    └── 🗺️ dem_alignment_reference.json
~~~

✔ Emoji BEFORE filenames  
✔ No drift, matches all QA directory conventions  
✔ No broken fences  

---

## 📘 2. Purpose

Radiometry QA ensures that Sentinel-1 backscatter processing is:

- calibrated  
- terrain-normalized  
- DEM-aligned  
- angle-consistent  
- ready for hydrology, coherence, and deformation ETL stages  
- sovereignty-safe and FAIR+CARE compliant  

Radiometric correctness is **foundational**—all downstream Sentinel-1 products depend on it.

---

## 🧩 3. QA Dimensions

### 1️⃣ σ⁰ Calibration QA
Checks:

- correct radar calibration constants  
- noise-floor handling  
- polarization parity (VV/VH)  
- slant-range to ground-range geometry  
- stable numeric ranges  

### 2️⃣ RTC γ⁰ QA
Ensures:

- correct terrain normalization  
- DEM slope/aspect compatibility  
- correct γ⁰ domain (e.g., backscatter in linear/dB units)  
- orthorectification consistency  
- projection fidelity (EPSG:32614)  

### 3️⃣ Incidence Angle & DEM Alignment QA
Validates:

- incidence-angle layer export  
- DEM-to-burst footprint alignment  
- correct angle-normalization behavior  
- no geometry drift  

These checks prevent distortions that would affect:

- wetness detection  
- wetlands classification  
- flood detection  
- coherence stability  
- deformation unwrapping  

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Radiometry QA must ensure:

- `"kfm:care_label" = "CARE-B"` (hydrology & deformation have downstream sensitivity)  
- `"kfm:h3_sensitive"` inherited from sovereign footprints  
- `"kfm:mask_required"` present for S1-derived hydrologic products  
- `"kfm:governance_notes"` documented  
- `"kfm:sovereignty_generalized"` flagged at later stages  

While radiometry itself is low-detail, it **enables** sensitive derivatives; hence QA enforces governance metadata correctness.

---

## 🔗 5. PROV-O Lineage

Radiometry QA outputs are recorded as:

~~~json
{
  "prov:Entity": "s1_radiometry_qa",
  "prov:wasGeneratedBy": "s1_radiometry_qa_pipeline",
  "kfm:care_label": "CARE-B",
  "kfm:qa_type": "radiometry"
}
~~~

These QA lineage entries appear in every RTC → downstream STAC Item.

---

## 🧪 6. CI Integration

CI validates:

- σ⁰ calibration reproducibility  
- γ⁰ consistency across resolutions  
- DEM alignment  
- projection + incidence correctness  
- cross-platform reproducibility  
- schema + SHACL conformance  
- governance metadata correctness  

Any mismatch → **ETL pipeline blocked.**

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict radiometry QA README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](./tests/README.md) · [📁 Fixtures](./fixtures/README.md)

</div>

