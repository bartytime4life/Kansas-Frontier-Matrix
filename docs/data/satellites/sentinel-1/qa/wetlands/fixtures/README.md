---
title: "📁 Sentinel-1 Wetlands QA — Fixtures (Wetness Mask · Seasonal Hydrology · Coherence-Fusion Truth)"
path: "docs/data/satellites/sentinel-1/qa/wetlands/fixtures/README.md"
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
care_profile: "CARE-B"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sentinel1-wetlands-fixtures-v11.json"

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
  owl_time: "Interval"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../../schemas/json/sentinel1-wetlands-fixtures-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-wetlands-fixtures-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:qa-wetlands-fixtures:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-qa-wetlands-fixtures"
event_source_id: "ledger:docs/data/satellites/sentinel-1/qa/wetlands/fixtures/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

ttl_policy: "48 months"
sunset_policy: "Superseded when wetlands QA models update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📁 **Sentinel-1 Wetlands QA — Fixture Library**  
`docs/data/satellites/sentinel-1/qa/wetlands/fixtures/`

Golden-standard, sovereignty-aware reference datasets enabling  
deterministic validation of wetland/saturation inference  
(γ⁰ wetness, seasonal hydrology models, coherence-fusion).

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/qa/wetlands/fixtures/
├── 📄 README.md
│
├── 🌿 wetlands_reference.tif               # True wetland/saturation mask (terrain-normalized γ⁰)
├── 🌿 seasonal_model_reference.json        # Canonical seasonal hydrology priors (winter/spring/etc.)
└── 🔗 coherence_fusion_reference.json       # Truth metadata for coherence → wetness fusion logic
~~~

✔ Emoji BEFORE filenames  
✔ Perfect congruence with flood/fixtures, coherence/fixtures, radiometry/fixtures  
✔ Zero drift  
✔ Fully box-safe

---

## 📘 2. Purpose

These fixtures provide the **ground-truth reference set** for verifying all wetlands/saturation  
inference logic inside the QA + ETL chains:

- γ⁰ wetness signal interpretation  
- seasonal hydrology priors  
- coherence-based saturation detection  
- DEM-aligned hydrology behavior  
- sovereignty metadata inheritance  
- deterministic fusion across platforms (CPU/GPU parity)

Fixtures ensure wetlands outputs are:

- reproducible  
- hydrologically credible  
- sovereignty-safe  
- compliant with FAIR+CARE rules  

---

## 🧩 3. Fixture Descriptions

### 🌿 `wetlands_reference.tif`
Reference wetland/saturation mask.

Validates:

- γ⁰ depression detection  
- vegetation vs. moisture separation  
- basin/pooling hydrology  
- stable threshold behavior  
- agreement with seasonal priors and coherence fusion  

### 🌿 `seasonal_model_reference.json`
Defines expected seasonal hydrology signals:

- winter freeze  
- spring saturation  
- summer drying  
- fall transitional wetness  

Used to validate seasonal-model correctness in  
`test_seasonal_models.py`.

### 🔗 `coherence_fusion_reference.json`
Truth metadata for coherence → wetness fusion:

- coherence thresholds  
- fusion weights  
- low-SNR behavior  
- distinction between flood decorrelation vs wetlands decorrelation  
- sovereignty-appropriate handling  

Used by `test_coherence_fusion.py`.

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

Wetlands are eco-culturally sensitive; fixtures enforce:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:sovereignty_generalized"` at transform stage  
- no presence of raw sovereign geometries  

The fixtures reflect **sovereignty readiness**, not raw sensitive detail.

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

Downstream wetlands QA and ETL reference this lineage.

---

## 🧪 6. CI Integration

CI enforces:

- γ⁰ wetness detection consistency  
- seasonal-model alignment  
- coherence-fusion correctness  
- stability across DEM topography  
- schema + SHACL correctness  
- perfect match to fixture baselines  
- governance metadata propagation  

Any mismatch → **CI block**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict wetlands-QA fixtures README; emoji prefix validated; zero drift. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Wetlands Tests](../tests/README.md) · [🛡 Governance](../../../transforms/governance/README.md)

</div>

