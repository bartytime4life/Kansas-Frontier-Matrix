---
title: "🌊 Sentinel-1 Flood Mapping — Classifier Definitions (VV/VH Ratio Rules · Hybrid Models · Weighting)"
path: "docs/data/satellites/sentinel-1/transforms/flood/classifiers/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Medium–High Sensitivity (CARE-B Hydrology)"
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
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

governance_ref: "../../../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

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
  schema_org: "Dataset"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "Instant"

json_schema_ref: "../../../../../../../schemas/json/sentinel1-flood-classifiers-v11.json"
shape_schema_ref: "../../../../../../../schemas/shacl/sentinel1-flood-classifiers-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:transform-flood-classifiers:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-transform-flood-classifiers"
event_source_id: "ledger:docs/data/satellites/sentinel-1/transforms/flood/classifiers/README.md"
immutability_status: "version-pinned"
machine_extractable: true

accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "24 months"
sunset_policy: "Superseded by next hydrological classifier revision"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood Mapping — Classifier Library**  
`docs/data/satellites/sentinel-1/transforms/flood/classifiers/`

Contains the **rule-based** and **hybrid** classifiers used to generate  
flood masks from Sentinel-1 RTC γ⁰, VH/VV ratios, coherence inputs,  
and terrain/hydrological context.

</div>

---

## 🗂️ 1. Directory Layout (Strict Option-A Emoji Style)

~~~text
docs/data/satellites/sentinel-1/transforms/flood/classifiers/
├── 📄 README.md
│
├── 🌊 ratio_ruleset.json           # Simple VH/VV ratio-based flood classifier
└── 🌊 hybrid_model_2025.json       # Hybrid flood model (ratio + coherence fusion)
~~~

✔ Emoji BEFORE filenames  
✔ No drift, no omissions  
✔ Exact consistency across all transform directories  

---

## 📘 2. Purpose

Flood classifiers convert SAR backscatter indicators into an initial  
**floodwater likelihood** surface. These classifiers are the core decision  
logic inside the flood ETL pipeline:

- **VH/VV ratio detection**  
- **coherence-reduction indicators**  
- **terrain/slope-conditioned pooling logic**  
- **hydrologic adjacency weighting**  

The classifiers here are **inputs**, not outputs — the ETL pipeline reads these JSON  
definitions to produce the final flood rasters.

---

## 🧩 3. Classifier Types

### 🌊 `ratio_ruleset.json`
A deterministic, rule-based classifier using only VV/VH relationships.

Typical structure:

~~~json
{
  "thresholds": {
    "vv_vh_ratio": 0.65,
    "vh_drop": -3.0
  },
  "logic": [
    "vh < vh_drop",
    "vv/vh < vv_vh_ratio"
  ]
}
~~~

Used for:

- simple flood detection  
- baseline consistency checks  
- fallback when coherence data is missing  

---

### 🌊 `hybrid_model_2025.json`
A **fusion classifier** combining:

- VV/VH ratio  
- coherence drop  
- terrain masks  
- wetland/saturation priors  
- hydrologic adjacency  

Example (conceptual):

~~~json
{
  "model": "hybrid-2025",
  "components": {
    "ratio_weight": 0.6,
    "coherence_weight": 0.3,
    "terrain_weight": 0.1
  },
  "parameters": {
    "ratio_threshold": 0.62,
    "coherence_threshold": 0.35
  }
}
~~~

---

## 🔗 4. PROV-O Lineage

These classifier JSON files are **prov:Entity** inputs:

~~~json
{
  "prov:Entity": "s1_flood_classifier_2025",
  "prov:usedBy": "s1_flood_mapping",
  "kfm:care_label": "CARE-B",
  "kfm:governance_notes": "Hydrology classifier used in sovereign-sensitive regions"
}
~~~

All flood STAC Items include reference to the classifier model used.

---

## 🔐 5. FAIR+CARE & Sovereignty Enforcement

Because flood mapping intersects:

- tribal water bodies  
- culturally significant hydroscapes  
- archaeological hydrology  

classifiers must be:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:h3_sensitive" = true` (propagated)  
- `"kfm:mask_required" = true`  
- versioned and immutable  

Hydrology classification **cannot leak un-generalized flood patterns**.

---

## 🧪 6. CI Validation Requirements

CI validates:

- schema compliance  
- numeric sanity  
- threshold logic validity  
- deterministic classifier structure  
- prohibited speculative logic  
- consistency with fixtures in `../fixtures/`  
- correct `"kfm:*"` metadata field presence  

Any inconsistency → **merge blocked**.

---

## 🧭 7. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.2 | 2025-11-29 | Initial strict, no-drift flood classifier README; emoji-prefix enforced. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅ Back](../README.md) · [🧪 Flood Tests](../tests/README.md) · [📁 Fixtures](../fixtures/README.md) · [🛡 Governance](../../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

