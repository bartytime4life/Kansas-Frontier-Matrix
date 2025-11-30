---
title: "📁 Sentinel-1 QA Fixtures — Wetlands (γ⁰ Wetness · Seasonal Hydrology · Coherence-Fusion)"
path: "docs/data/satellites/sentinel-1/qa/fixtures/wetlands/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity QA Fixtures (CARE-B · Ecohydrology · Sovereignty-Aware)"
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
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-wetlands-fixtures-v11.json"

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
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-wetlands-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-wetlands-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-fixtures-wetlands:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-fixtures-wetlands"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/fixtures/wetlands/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when wetlands QA models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Wetlands QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/fixtures/wetlands/`

Canonical **wetlands/saturation QA fixtures** used to validate  
γ⁰ wetness detection, seasonal hydrology models, and coherence-fusion logic  
across governed ecohydrological regions.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/fixtures/wetlands/
├── 📄 README.md
│
├── 🌿 wetlands_reference.tif               # Golden wetland/saturation mask (gamma0-based)
├── 🌿 seasonal_model_reference.json        # Seasonal hydrology truth (winter/spring/summer/fall)
└── 🔗 coherence_fusion_reference.json       # Truth metadata for coherence → wetness fusion
~~~

✔ Emoji BEFORE filenames  
✔ Matches flood/fixtures, radiometry/fixtures, coherence/fixtures, deformation/fixtures  
✔ Zero drift, box-safe  

---

## 📘 2. Purpose

These fixtures define the **truth set** against which wetlands QA tests validate:

- γ⁰ depression (wetness/saturation detection)  
- hydrology seasonal model integration  
- coherence-enhanced saturation detection  
- sovereignty metadata correctness  
- reproducibility across CPU/GPU environments  
- STAC-ready wetlands output metadata  

They anchor the wetlands QA pipeline in **deterministic, ecology-aligned hydrology**.

---

## 🧩 3. Fixture Descriptions

### 🌿 `wetlands_reference.tif`
Reference mask used to validate:

- γ⁰ wetness signature correctness  
- DEM-influenced moisture pooling  
- vegetation–moisture separation  
- hydrologic realism  
- deterministic spatial inference  

### 🌿 `seasonal_model_reference.json`
Defines expected **seasonal hydrology priors**, including:

- winter freeze states  
- spring soil saturation  
- summer drying  
- fall re-moistening patterns  

Used in `test_seasonal_models.py`.

### 🔗 `coherence_fusion_reference.json`
Truth metadata for validating coherence → wetness fusion behavior:

- correctness of coherence weighting  
- proper use of thresholds  
- distinction between flood decorrelation vs wetlands decorrelation  
- correct governance metadata inheritance  

Used in `test_coherence_fusion.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Requirements

Wetlands are inherently sensitive due to:

- tribal hydroscapes  
- culturally significant ecological corridors  
- environmentally protected wetlands  

Fixtures must enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:governance_notes"` present  
- readiness for sovereignty generalization in ETL transforms  

Fixtures **never** contain raw sovereign geometries.

---

## 🔗 5. PROV-O Lineage

Fixtures register as:

~~~json
{
  "prov:Entity": "s1_wetlands_fixture",
  "kfm:provenance_type": "qa-fixture",
  "kfm:care_label": "CARE-B"
}
~~~

Downstream wetlands QA uses these lineage tokens to validate metadata propagation.

---

## 🧪 6. CI Integration

CI checks ensure:

- γ⁰ wetness behavior is deterministic  
- seasonal model values match truth  
- coherence-fusion correctness  
- schema + SHACL compliance  
- correct `"kfm:*"` metadata propagation  
- pixel-perfect match against fixtures  

Any mismatch → **CI BLOCK**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict wetlands fixture README; emoji alignment validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Wetlands Tests](../../wetlands/tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

