---
title: "🔗 Sentinel-1 Coherence — STAC Directory (Temporal Coherence · Disturbance · Flood Damage · Land-Change Signals)"
path: "docs/data/satellites/sentinel-1/stac/coherence/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council Oversight"

license: "CC-BY 4.0 (ESA Open Data)"
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
telemetry_schema: "../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R4"
care_label: "CARE-B (Coherence Disturbance Inference)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "High"
redaction_required: true

data_steward: "Remote Sensing Working Group · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/sentinel1-coherence-collection-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/sentinel1-coherence-collection-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-coherence-overview:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-coherence"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/coherence/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA coherence reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🔗 **Sentinel-1 Coherence STAC Directory**  
`docs/data/satellites/sentinel-1/stac/coherence/`

Governed STAC Collections & Items for  
**temporal SAR coherence**, used in  
**flood damage**, **disturbance mapping**, **agricultural change**, and **land-change detection**.

</div>

---

## 📘 1. Overview

This directory contains the full governed STAC structure for **temporal coherence** derived from Sentinel-1 SAR:

- coherence loss after storms/tornadoes  
- flood-induced coherence change  
- agricultural disturbance  
- vegetation removal / harvest cycles  
- land-cover transitions  
- infrastructure damage (sovereignty-generalized)  

Coherence is *highly sensitive* because it reveals disturbance patterns, therefore it requires:

- sovereignty masking  
- H3 generalization  
- CARE-B governance  
- uncertainty floors  
- strict lineage tracking  

All STAC items/collections here are:

- STAC 1.x valid  
- JSON-LD enriched  
- DCAT compatible  
- PROV-O lineage complete  
- FAIR+CARE + sovereignty compliant  
- CI-validated  

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/coherence/
├── 📄 README.md                           # This file
│
├── 🗂️ collections/                        # Coherence STAC Collections
│   └── collection_coherence.json
│
└── 📦 items/                               # Coherence STAC Items (scene-pair tiles)
    ├── S1A_IW_COH_20250101_20250113.json
    ├── S1B_IW_COH_20250314_20250326.json
    └── …
~~~

---

## 🧩 3. Coherence STAC Collection Responsibilities

The coherence Collection defines:

- `"sar:product_type" = "COHERENCE"`  
- master/slave acquisition pair metadata  
- platform/instrument parameters  
- bounding box + geometry  
- time span of coherence pairs  
- `"kfm:*"` governance inheritance  
- DCAT dataset metadata  
- JSON-LD contexts for SAR + governance  
- PROV-O lineage anchors  

CI validates:

- STAC schema  
- DCAT compatibility  
- JSON-LD context links  
- sovereignty generalization rules  
- `"kfm:*"` governance fields  

---

## 🧩 4. Coherence STAC Items (Overview)

Scene-level Items represent:

- coherence rasters (0–1)  
- masked/uncertainty regions  
- sovereign-generalized tiles  
- QA maps (coherence quality, noise, threshold ambiguity)  
- optional amplitude/RTC supporting assets  
- complete provenance graph  

Full details appear in:

```
docs/data/satellites/sentinel-1/stac/items/coherence/README.md
```

---

## 🔐 5. FAIR+CARE & Sovereignty Controls

Coherence is often sensitive because it reveals:

- disturbance from storms  
- agricultural field state  
- infrastructure damage  
- culturally protected landscapes  

Thus Collections & Items MUST include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Governance validated through:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 6. CI Requirements

Coherence STAC structures must pass:

- STAC schema validation  
- SAR + coherence extension validation  
- correct link structure  
- geometry ↔ bbox integrity  
- governance metadata completeness  
- H3 sovereignty generalization  
- PROV-O lineage structure  
- DCAT dataset compatibility  

Any failure → **release blocked**.

---

## 🔁 7. Coherence in the Sentinel-1 ETL Pipeline

~~~text
ESA ingest
 → orbit correction
 → radiometric calibration
 → speckle filtering
 → master/slave pair selection
 → coherence computation
 → sovereignty masking (mandatory)
 → coherence QA
 → STAC Item generation
 → coherence Collection update
 → governed release bundle
~~~

---

## 🔮 8. Applications Across KFM

- tornado/wind damage assessment  
- flood-induced coherence loss  
- agricultural disturbance detection  
- ecological landscape change  
- cultural landscape impact monitoring  
- Focus Mode v3 signal evidence  
- Story Node v3 environmental narrative support  

---

## 🧭 9. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial Sentinel-1 coherence STAC directory README; H3/CARE-B enforced; STAC/DCAT/PROV integrated; CI-safe.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🗂 Coherence Collections](../collections/README.md) · [🛡 Governance](../../../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

