---
title: "📁 Sentinel-1 Radiometry QA — Fixtures (σ⁰ · γ⁰ · DEM Alignment · Incidence Geometry)"
path: "docs/data/satellites/sentinel-1/qa/radiometry/fixtures/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA Fixtures (CARE-B)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"

review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"
license: "MIT"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-radiometry-fixtures-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  owl_time: "Instant"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/sentinel1-radiometry-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-radiometry-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-radiometry-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-radiometry-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/radiometry/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when radiometry QA models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Radiometry QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/radiometry/fixtures/`

Reference σ⁰, γ⁰, DEM-alignment, and incidence-angle fixtures used to ensure  
stable, reproducible, and governed **radiometric correctness** across the  
entire Sentinel-1 ETL pipeline.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/radiometry/fixtures/
├── 📄 README.md
│
├── 📄 sigma0_reference_vv.tif          # Reference σ⁰ VV (calibrated backscatter)
├── 🌍 gamma0_reference_vv.tif          # Reference γ⁰ VV (RTC terrain-normalized)
└── 🗺️ dem_alignment_reference.json     # DEM/incidence-angle alignment truth metadata
~~~

✔ Emoji BEFORE filenames  
✔ Identical structure to all KFM QA fixture directories  
✔ 100% box-safe  

---

## 📘 2. Purpose

These fixtures support **deterministic Radiometry QA**, validating:

- σ⁰ calibration correctness  
- γ⁰ terrain normalization  
- DEM-to-burst footprint alignment  
- incidence-angle computation  
- RTC projection fidelity  
- numerical stability across platforms  

These are the **ground-truth references** for radiometry QA tests.

---

## 🧩 3. Fixture Descriptions

### 📄 `sigma0_reference_vv.tif`
Reference **σ⁰ VV** calibrated backscatter raster.

Verifies:

- correct calibration LUT application  
- correct slant-to-ground geometry  
- correct polarization handling  
- consistent radiometric units  

---

### 🌍 `gamma0_reference_vv.tif`
Reference **gamma-naught (γ⁰)** raster produced after RTC terrain normalization.

Used to validate:

- DEM slope/aspect dependency  
- incidence-angle correction  
- orthorectification consistency  
- projection correctness  
- numerical match with RTC core outputs  

---

### 🗺️ `dem_alignment_reference.json`
Reference metadata that encodes:

- DEM tile source & CRS  
- expected DEM–burst overlap  
- expected incidence angle statistics  
- elevation → γ⁰ influence checks  

Used to validate:

- DEM alignment QA  
- incidence-angle QA  
- correct geolocation coupling between elevation and radiometry  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Radiometry fixtures:

- are **CARE-B** due to downstream sensitivity (wetlands, flood, deformation)  
- contain no raw sovereign geometry  
- must propagate `"kfm:h3_sensitive"` as inherited governance metadata  
- must not enable back-inference of precise deformation/wetness patterns  

Governance metadata must remain attached during tests.

---

## 🔗 5. PROV-O Lineage

Fixtures register as QA entities:

~~~json
{
  "prov:Entity": "s1_radiometry_fixture",
  "kfm:care_label": "CARE-B",
  "kfm:provenance_type": "qa-fixture"
}
~~~

Downstream QA lineage attaches this fixture provenance to every radiometry test run.

---

## 🧪 6. CI Integration

CI compares QA outputs against these fixtures to ensure:

- deterministic radiometric calibration  
- stable RTC terrain normalization  
- DEM alignment correctness  
- consistent incidence-angle models  
- schema + SHACL compliance  
- governance metadata preserved  

Any mismatch → **ETL pipeline failure**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict radiometry-QA fixtures README; zero drift; emojis validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Tests](../tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

