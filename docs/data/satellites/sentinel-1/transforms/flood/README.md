---
title: "🌊 Sentinel-1 Flood Mapping — ETL Transform (VH/VV Ratios · Coherence Fusion · Classification · QA)"
path: "docs/data/satellites/sentinel-1/transforms/flood/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B · Hydrology & Sovereignty-Aware)"
status: "Active · Enforced"
release_stage: "Stable · Governed"
lifecycle: "LTS"
review_cycle: "Quarterly · RS Working Group · FAIR+CARE Council"

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
telemetry_schema: "../../../../../schemas/telemetry/sat-flood-transform-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
risk_category: "High"
public_exposure_risk: "Medium"
redaction_required: true

data_steward: "Remote Sensing Working Group"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "DataTransform"
  prov_o: "prov:Activity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../schemas/json/sentinel1-flood-transform-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-flood-transform-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-flood:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-flood"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/flood/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded with next flood-model revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood Mapping Transform**  
`docs/data/satellites/sentinel-1/transforms/flood/`

Generates **floodwater detection surfaces** using  
VH/VV ratio thresholds, RTC γ⁰, coherence fusion, and  
sovereignty-safe hydrological masking for KFM.

</div>

---

## 🗂️ 1. Directory Layout (STRICT OPTION-A EMOJI STYLE)

~~~text
docs/data/satellites/sentinel-1/transforms/flood/
├── 📄 README.md
│
├── 🌊 classifiers/                # VH/VV ratio models, hybrid flood classifiers
│   ├── 🌊 ratio_ruleset.json
│   └── 🌊 hybrid_model_2025.json
│
├── 🧪 tests/                      # Test suite (flood classification + masks)
│   ├── 🌊 test_flood_core.py
│   ├── 🌊 test_ratio_thresholds.py
│   └── 🌊 test_coherence_fusion.py
│
└── 📁 fixtures/                   # SAFE subsets, RTC γ⁰, coherence, reference flood rasters
    ├── 🛰️ SAFE_annotation_subset.xml
    ├── 🏞️ rtc_gamma0_sample_vv.tif
    ├── 🔗 coherence_sample.tif
    └── 🌊 flood_reference.tif
~~~

✔ Emoji BEFORE filenames  
✔ No missing folders  
✔ Structure matches rtc/, deformation/, coherence/  
✔ Box-safe, no broken fences  

---

## 📘 2. Purpose

This transform identifies **floodwater extents** using SAR-based hydrological indicators:

- **VH/VV ratio drops** (water → low backscatter)
- **coherence reduction** (flooding → temporal decorrelation)
- **γ⁰ terrain-corrected backscatter**
- **dem-based pooling / low-lying area enhancement**

Flood detection is a **medium-high sensitivity** product because it intersects:

- sovereign hydroscapes  
- culturally significant water bodies  
- archaeological hydrology  
- hazard and emergency-response systems  

Thus governance is **CARE-B** with mandatory sovereignty rules.

---

## 🧩 3. Inputs & Outputs

### Inputs
- RTC γ⁰ (VV, VH)  
- coherence raster (optional fusion)  
- DEM-derived low-relief mask  
- hydrologic base layers  
- SAFE annotation subset  
- classifier rulesets (`classifiers/`)  

### Outputs
- flood classification raster
- probability or confidence surface
- QA mask
- flood metadata:

~~~json
{
  "flood": {
    "classifier": "hybrid_model_2025",
    "method": "vv-vh-ratio + coherence-fusion",
    "sovereignty_generalized": true,
    "confidence": "per-pixel"
  }
}
~~~

Outputs are consumed by:
- STAC flood Items  
- hydrology engine  
- Story Node v3 (flood events)  
- Focus Mode v3 hydrology context  

---

## 🧬 4. Flood Processing Steps

### 1️⃣ VH/VV Ratio Calculation  
Detects water by sharp VH decreases + VV stability.

### 2️⃣ Terrain Correction (from RTC)  
Ensures γ⁰ normalization across slope/aspect.

### 3️⃣ Coherence Fusion (optional)  
Flooding → reduced temporal coherence.

### 4️⃣ Rule-Based / Hybrid Classification  
From `classifiers/`:

- ratio thresholding  
- multi-band logical rules  
- terrain-informed smoothing  
- coherence-informed evidence weighting  

### 5️⃣ QA Mask Generation  
- incoherent zones  
- sensor anomalies  
- DEM artifacts  
- classification confidence  

### 6️⃣ Sovereignty Generalization  
Flood outputs undergo:

- H3 generalization  
- smoothing within sovereign zones  
- uncertainty flooring  
- `"mask_required": true`

---

## 🔗 5. PROV-O Lineage

~~~json
{
  "prov:Activity": "s1_flood_mapping",
  "prov:used": [
    "rtc_gamma0_vv",
    "rtc_gamma0_vh",
    "coherence",
    "dem_low_relief",
    "classifier_model"
  ],
  "prov:generated": [
    "flood_mask",
    "flood_probability"
  ],
  "prov:wasAssociatedWith": "KFM-S1-ETL"
}
~~~

Embedded in all Sentinel-1 flood STAC Items.

---

## 🔐 6. FAIR+CARE & Sovereignty Enforcement

Flood layers can indicate:

- sensitive hydrology  
- sovereign water bodies  
- traditional ecological knowledge areas  
- settlement-adjacent water changes  

Thus:

- `"kfm:care_label" = "CARE-B"`
- `"kfm:h3_sensitive" = true`
- `"kfm:mask_required" = true`
- mandatory sovereign-zone H3 generalization  
- uncertainty flooring  
- lineage for governance audit  

---

## 🧪 7. CI Test Requirements

CI validates:

- VV/VH ratio math  
- classifier thresholds  
- coherence-fusion logic  
- DEM pooling checks  
- correct governance metadata  
- deterministic outputs  
- comparison with `flood_reference.tif` in fixtures  
- schema + SHACL validity  

Failures block ETL.

---

## 🧭 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, zero-drift flood transform README; emoji prefix validated. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Flood Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md)

</div>

