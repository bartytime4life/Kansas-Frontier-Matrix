---
title: "🌊 Sentinel-1 Flood — STAC Collections (Binary Flood · Multi-Class Flood · Probabilistic Water Surfaces)"
path: "docs/data/satellites/sentinel-1/stac/flood/collections/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public With Restrictions (Governed SAR Derivative)"
status: "Active / Enforced"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Remote Sensing WG · FAIR+CARE Council"

license: "CC-BY 4.0 (ESA Open Data)"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/sat-sentinel1-stac-v11.json"

governance_ref: "../../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F3-A1-I2-R5"
care_label: "CARE-B (Flood Mapping)"
indigenous_rights_flag: true
sensitivity_level: "Medium–High"
public_exposure_risk: "Medium"
risk_category: "Medium–High"
redaction_required: true

data_steward: "Remote Sensing WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E84 Information Carrier"
  prov_o: "prov:Entity"
  geosparql: "geo:FeatureCollection"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../../schemas/json/sentinel1-flood-collections-v11.json"
shape_schema_ref: "../../../../../../schemas/shacl/sentinel1-flood-collections-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:sentinel1:stac-flood-collections-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-sentinel1-stac-flood-collections"
event_source_id: "ledger:docs/data/satellites/sentinel-1/stac/flood/collections/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "36 months"
sunset_policy: "Superseded upon next ESA flood reprocessing cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 🌊 **Sentinel-1 Flood Mapping — Governed STAC Collections**  
`docs/data/satellites/sentinel-1/stac/flood/collections/`

High-level collections for:  
**binary flood masks · multi-class flood levels · probability flood surfaces**  
generated from Sentinel-1 SAR (RTC γ⁰, VH/VV ratios, coherence change).

</div>

---

## 📘 1. Overview

This directory defines the STAC **Collections** for flood-related Sentinel-1 SAR derivatives:

- **Binary Flood Masks**  
  (water / non-water)

- **Multi-Class Flood Depth / Severity Maps**

- **Flood Probability Surfaces**  
  (e.g., Bayesian or regression-based probability grids)

- **Coherence-Assisted Flood Layers**  
  (coherence loss integrated with VH/VV thresholds)

- **Hybrid Classifiers** integrating change detection + radiometric ratios

Because flood layers intersect **sovereign waterways, cultural landscapes, ecologically sensitive zones**,  
all products require strict governance controls and H3-based sovereignty generalization.

---

## 🗂️ 2. Directory Layout (Emoji-Strict Option A)

~~~text
docs/data/satellites/sentinel-1/stac/flood/collections/
├── 📄 README.md                         # This file
│
└── 🌊 collection_flood.json             # Primary flood STAC Collection
~~~

---

## 🧩 3. Flood Collection Structure

### 🌐 Core STAC Metadata  
- `stac_version = "1.x"`  
- `"sar:product_type" = "FLOOD"`  
- `"sar:instrument_mode" = "IW"`  
- `"sar:frequency_band" = "C"`  
- `license = "CC-BY-4.0"`  
- bounding region (bbox + geometry)  
- temporal extent  
- KFM governance metadata inheritance  

### 📦 Collection-Level Assets  
May include:

- `"extent_preview"` — PNG snapshot  
- `"water_occurrence"` — optional long-term composite  
- `"metadata"` — static metadata block  
- `"qa_overview"` — general QA summary  

### 🔗 STAC Links  
- `"self"`  
- `"root"`  
- `"parent"` (Sentinel-1 STAC root)  
- `"items"` → flood items directory  
- `"child"` links for sub-categories (multi-class, probability if separated)

### 🧬 PROV-O Lineage  
Root provenance anchors for:

- orbit correction  
- radiometric calibration  
- RTC gamma⁰  
- coherence-derived change metrics  
- flood classifier activities  
- sovereignty masking agents  

---

## 🔐 4. FAIR+CARE & Sovereignty Rules (Mandatory)

Flood mapping has high governance sensitivity.  
All collections MUST include:

- `"kfm:care_label" = "CARE-B"`  
- `"kfm:care_label_reason"`  
- `"kfm:h3_sensitive"`  
- `"kfm:mask_required"`  
- `"kfm:sovereignty_uncertainty_floor"`  
- `"kfm:governance_notes"`  
- `"kfm:data_steward"`  

Collections are validated under:

- `faircare_validate.yml`  
- `jsonld_validate.yml`  
- `stac_validate.yml`

---

## 🧪 5. CI Validation Requirements

A flood collection must pass:

- STAC 1.x schema validity  
- topology & geometry sanity  
- SAR extension validation  
- DCAT dataset compliance  
- JSON-LD context resolution  
- PROV-O lineage correctness  
- full governance field presence  
- sovereignty-masking logic  

Failures → **collection blocked** until corrected.

---

## 🔁 6. Flood Collection in the ETL Pipeline

~~~text
ESA ingest
 → RTC gamma0 generation
 → VH/VV ratio + coherence change modeling
 → flood classifiers (binary/multi-class/probability)
 → sovereignty masking (mandatory)
 → QA generation
 → STAC Item creation
 → Flood Collection update (this directory)
 → governed release bundle
~~~

---

## 🔮 7. Applications Inside KFM

- flood extent & severity products  
- hydrology + watershed modeling  
- disaster impact overlays  
- cultural landscape safety analysis  
- Story Node v3 flood narratives  
- Focus Mode v3 sovereign-safe environmental reasoning  
- wetlands/flood interaction modeling  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial flood STAC Collections README; FAIR+CARE/H3 aligned; STAC/DCAT/PROV integrated; CI-safe.          |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [📦 Flood Items](../items/README.md) · [🛡 Governance](../../..)

