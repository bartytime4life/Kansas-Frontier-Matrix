---
title: "🔗 Sentinel-1 Wetlands — Coherence Fusion Logic (Temporal Coherence → Wetness Indicators)"
path: "docs/data/satellites/sentinel-1/transforms/wetlands/coherence_fusion/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B · Ecohydrology)"
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

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  owl_time: "Interval"
  geosparql: "geo:Feature"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-wetlands-coherencefusion-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-wetlands-coherencefusion-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-wetlands-coherencefusion:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-wetlands-coherencefusion"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/wetlands/coherence_fusion/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded on next wetlands-fusion model update"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Wetlands Coherence-Fusion Logic**  
`docs/data/satellites/sentinel-1/transforms/wetlands/coherence_fusion/`

Coherence describes **surface stability**. Wetness/saturation increases  
**temporal decorrelation**, making coherence a valuable indicator for  
wetland mapping, especially in transitional seasons.

</div>

---

## 🗂️ 1. Directory Layout (STRICT Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/wetlands/coherence_fusion/
├── 📄 README.md
│
├── 🔗 fusion_ruleset.json         # Logical rules for coherence → wetness conversion
└── 🔗 coherence_weights.json      # Weighting of coherence in seasonal & γ⁰ fusion
~~~

✔ Emoji BEFORE filenames  
✔ Fully matches wetlands/, flood/, deformation/, rtc/, radiometric structures  
✔ Zero drift, zero omissions, box-safe  

---

## 📘 2. Purpose

The coherence fusion module contributes **coherence-based wetness evidence**  
used in the final wetlands classifier.

Wet areas → stronger **temp. decorrelation**  
Dry/vegetated areas → stable coherence

This module determines **how much** coherence contributes to:

- wetland probability  
- saturation likelihood  
- seasonal sensitivity  
- pooling behavior  

It also provides **rules** for combining coherence with:

- RTC γ⁰ depressions  
- seasonal hydrology models  
- DEM pooling masks  

---

## 🧩 3. File Definitions

### 🔗 `fusion_ruleset.json`
Logical rules and thresholds describing when coherence impacts wetland mapping.

Example:

~~~json
{
  "rules": [
    "coh < 0.35 → wetness_boost",
    "coh < 0.20 → strong_wetness_boost",
    "coh_drop > 0.15 → flood_signal"
  ]
}
~~~

These rules help distinguish:

- saturated soils  
- ephemeral pooling  
- flood/disturbance cycles  
- unstable vs. wetlands signatures  

---

### 🔗 `coherence_weights.json`
Weights used during final fusion between:

- γ⁰ terrain-corrected backscatter  
- seasonal hydrology model  
- coherence  

Example:

~~~json
{
  "weights": {
    "gamma0": 0.55,
    "coherence": 0.30,
    "seasonal_model": 0.15
  }
}
~~~

These weights must be validated against seasonal patterns and historical wetlands.

---

## 🔗 4. PROV-O Lineage

Each fusion component is a **prov:Entity** and contributes to wetlands lineage:

~~~json
{
  "prov:Entity": "wetlands_coherence_fusion_2025",
  "kfm:care_label": "CARE-B",
  "prov:wasUsedBy": "s1_wetlands_mapping"
}
~~~

Downstream STAC Items reference the applied coherence fusion configuration.

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

Wetlands mapping intersects:

- tribal hydroscapes  
- traditional ecological knowledge zones  
- sensitive riparian corridors  

Thus:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true"`  
- `"kfm:mask_required" = true"`  
- `"kfm:sovereignty_generalized"` propagated in metadata  

Coherence fusion metadata MUST persist through the ETL pipeline.

---

## 🧪 6. CI Validation Requirements

CI checks:

- JSON schema shape  
- threshold + rule validity  
- weighting sanity (0.0–1.0, sums ≤ 1)  
- compatibility with seasonal models  
- stability across test scenes  
- governance metadata correctness  

Any mismatch → CI block.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, non-drifting coherence-fusion README; emoji-prefix alignment verified. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🌿 Seasonal Models](../seasonal_models/README.md) · [🛡 Governance](../../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

