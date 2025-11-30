---
title: "🌿 Sentinel-1 Wetlands & Saturation Mapping — ETL Transform (RTC γ⁰ · Coherence Fusion · Seasonal Models)"
path: "docs/data/satellites/sentinel-1/transforms/wetlands/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B · Ecohydrology)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · FAIR+CARE Council · Remote Sensing WG"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest>"
previous_version_hash: "<prev>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-wetlands-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "Interval"

json_schema_ref: "../../../../../schemas/json/sentinel1-wetlands-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-wetlands-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-wetlands:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-wetlands"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/wetlands/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next wetlands model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌿 **Sentinel-1 Wetlands & Soil Saturation Transform**  
`docs/data/satellites/sentinel-1/transforms/wetlands/`

Produces **wetland/saturation detection layers** using  
RTC γ⁰, coherence-loss indicators, and seasonal ecohydrology models.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/wetlands/
├── 📄 README.md
│
├── 🌿 seasonal_models/               # Seasonal wetness models (winter/spring/summer/fall)
│   ├── 🌿 seasonal_model_2024.json
│   └── 🌿 seasonal_model_2025.json
│
├── 🔗 coherence_fusion/             # Coherence → wetness fusion logic
│   ├── 🔗 fusion_ruleset.json
│   └── 🔗 coherence_weights.json
│
├── 🧪 tests/                         # Unit + integration test suite
│   ├── 🌿 test_wetlands_core.py
│   ├── 🌿 test_seasonal_models.py
│   └── 🌿 test_coherence_fusion.py
│
└── 📁 fixtures/                      # SAFE subsets, RTC γ⁰, coherence, reference wetland maps
    ├── 🛰️ SAFE_annotation_subset.xml
    ├── 🏞️ rtc_gamma0_sample_vv.tif
    ├── 🔗 coherence_sample.tif
    └── 🌿 wetlands_reference.tif
~~~

✔ Emoji BEFORE filenames  
✔ Everything present—no drift  
✔ 100% safe inside code block  

---

## 📘 2. Purpose

This transform identifies **wetlands, saturation zones, and ephemeral moisture areas**  
using multi-temporal SAR hydrology indicators:

- low backscatter zones (γ⁰ depression)  
- coherence reduction (ponding, saturated soils)  
- seasonal hydrological cycles  
- DEM-informed pooling and relief analysis  
- vegetation–soil moisture interaction  

This product is **CARE-B** because wetland regions often overlap:

- tribal ecological resources  
- protected habitats  
- culturally sensitive hydroscapes  

---

## 🧩 3. Inputs & Outputs

### Inputs

- RTC γ⁰ (VV/VH)
- coherence magnitude (optional fusion)
- seasonal wetness models (`seasonal_models/`)
- SAFE annotation subset
- DEM pooling masks
- fusion weighting logic (`coherence_fusion/`)

### Outputs

- wetlands/saturation classification raster  
- wetness probability surface  
- QA mask  
- metadata:

~~~json
{
  "wetlands": {
    "classifier": "hybrid_seasonal_2025",
    "components": ["gamma0", "coherence", "seasonal_model"],
    "sovereignty_generalized": true
  }
}
~~~

---

## 🧬 4. Processing Steps

### 1️⃣ Seasonal Model Interpretation  
Uses seasonal models (e.g., winter/spring) to weight γ⁰ expectations.

### 2️⃣ RTC-Based Wetness Signal  
Wet areas → low γ⁰ and damping of VV/VH structure.

### 3️⃣ Coherence Fusion  
Flooded or saturated areas → temporal decorrelation.

### 4️⃣ Terrain-Informed Wetness  
DEM pooling → local contributing zones.

### 5️⃣ Final Fusion  
Combine:  
- seasonal model  
- γ⁰  
- coherence  
- DEM  
into a final wetland probability surface.

### 6️⃣ Sovereignty-Aware Output (MANDATORY)  
Wetlands are sovereignty-sensitive:

- H3 coarse generalization  
- smoothing  
- uncertainty flooring  
- `"mask_required": true`  

---

## 🔗 5. PROV-O Lineage

~~~json
{
  "prov:Activity": "s1_wetlands_mapping",
  "prov:used": [
    "rtc_gamma0",
    "coherence",
    "seasonal_model",
    "dem_pooling"
  ],
  "prov:generated": [
    "wetland_mask",
    "wetland_probability"
  ],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
~~~

---

## 🔐 6. FAIR+CARE & Sovereignty Enforcement

Wetlands + saturation mapping intersects:

- sovereign water systems  
- protected environmental zones  
- cultural-ecological resources  

Rules:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true`  
- `"kfm:mask_required" = true`  
- `"kfm:sovereignty_generalized" = true`  

Generalization occurs at STAC stage but metadata must propagate here.

---

## 🧪 7. CI Validation

CI checks:

- γ⁰ wetness signal correctness  
- seasonal model application  
- coherence-fusion logic  
- hydrology pooling logic  
- schema + SHACL validity  
- deterministic outputs  
- governance metadata  

Any mismatch blocks merge.

---

## 🧭 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, zero-drift wetlands transform README; emojis validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Wetlands Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

