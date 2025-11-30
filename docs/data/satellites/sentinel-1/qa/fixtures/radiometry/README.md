---
title: "📁 Sentinel-1 QA Fixtures — Radiometry (σ⁰ · γ⁰ · DEM Alignment)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/radiometry/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA Fixtures (CARE-B · Sovereignty-Aware)"
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

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-radiometry-fixtures-v11.json"

fair_category: "F3-A2-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E84 Information Carrier"
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-radiometry-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-radiometry-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures-radiometry:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures-radiometry"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/radiometry/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded upon radiometry QA update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Radiometry QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/fixtures/radiometry/`

Reference σ⁰/γ⁰ & DEM-alignment datasets used to validate  
**radiometric calibration, terrain normalization, and angle-geometry correctness**  
in Sentinel-1 radiometry QA and downstream ETL pipelines.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/radiometry/
├── 📄 README.md
│
├── 📄 sigma0_reference_vv.tif         # Calibrated σ⁰ VV backscatter reference
├── 🌍 gamma0_reference_vv.tif         # RTC γ⁰ VV terrain-normalized reference
└── 🗺️ dem_alignment_reference.json    # Truth DEM–incidence alignment metadata
~~~

✔ Emojis BEFORE filenames  
✔ Exact match to radiometry/tests and master QA fixture design  
✔ Zero drift, 100% box-safe

---

## 📘 2. Purpose

These fixtures supply **deterministic radiometry ground-truth** for QA tests validating:

- σ⁰ calibration math  
- γ⁰ RTC terrain normalization  
- DEM–burst footprint overlap  
- incidence-angle alignment  
- radiometric reproducibility across CPU/GPU architectures  
- sovereignty-safe metadata propagation  
- FAIR+CARE compliance for downstream hydrology, wetlands, and deformation products  

Correct radiometry is essential for:

- flood and wetlands γ⁰ depression detection  
- coherence stability  
- InSAR deformation quality  
- STAC Items for S1 radiometry collections  
- Focus Mode environmental reasoning  

---

## 🧩 3. Fixture Descriptions

### 📄 `sigma0_reference_vv.tif`
Used to validate:

- correct σ⁰ calibration LUT application  
- noise-floor behavior  
- projection geometry (slant → ground conversion)  
- stable VV radiometric range  

### 🌍 `gamma0_reference_vv.tif`
Validates:

- terrain-normalized γ⁰ correctness  
- DEM slope/aspect conditioning  
- γ⁰ domain compliance (linear/dB)  
- stable angular correction  
- geolocation and projection fidelity  

### 🗺️ `dem_alignment_reference.json`
Validates:

- DEM footprint alignment  
- incidence-angle statistics  
- elevation → γ⁰ influence logic  
- correct DEM cell sampling & interpolation metadata  

Used in:  
`test_dem_incidence_alignment.py`

---

## 🔐 4. FAIR+CARE & Sovereignty Enforcement

Even radiometry carries inherited governance obligations because  
it supports hydrologically and culturally sensitive derivative products.

Fixtures enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"` (inherited)  
- `"kfm:mask_required" = true"` (downstream requirement)  
- `"kfm:governance_notes"` present  
- sovereignty-generalization readiness for dependent ETL transforms  

---

## 🔗 5. PROV-O Lineage

Fixtures register as:

~~~json
{
  "prov:Entity": "s1_radiometry_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

All radiometry QA lineage references this fixture dataset chain.

---

## 🧪 6. CI Integration

CI uses these fixtures for:

- σ⁰/γ⁰ calibration consistency checks  
- DEM alignment identity checks  
- raster equivalence comparisons  
- schema + SHACL validation  
- deterministic cross-platform behavior  
- governance metadata enforcement  

Any deviation → **pipeline blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial nested radiometry-QA fixture README; emoji/structure validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Radiometry Tests](../../../radiometry/tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

