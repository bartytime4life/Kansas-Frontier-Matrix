---
title: "📦 NASA SMAP — Sample STAC Items & Mini Collections (Synthetic · Tutorial-Safe)"
path: "docs/data/satellites/smap/samples/stac/README.md"
version: "v11.2.2"
last_updated: "2025-11-29"

classification: "Public · Non-Sensitive · Synthetic Examples"
status: "Active / Public"
release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Annual · Documentation WG · FAIR+CARE Council Oversight"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
provenance_profile: "KFM-PROV-O v11.2"

commit_sha: "<latest-commit>"
previous_version_hash: "<prev-sha>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.2/data-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/sat-smap-v11.json"

governance_ref: "../../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-A (Public Training Use)"
indigenous_rights_flag: false
sensitivity_level: "None (Synthetic)"
public_exposure_risk: "Low"
risk_category: "Low"
redaction_required: false

data_steward: "Earth Systems WG · FAIR+CARE Council"

ontology_alignment:
  schema_org: "Dataset"
  cidoc: "E73 Information Object"
  prov_o: "prov:Entity"
  geosparql: "geo:Feature"
  owl_time: "TemporalEntity"

json_schema_ref: "../../../../../schemas/json/smap-sample-stac-v11.json"
shape_schema_ref: "../../../../../schemas/shacl/smap-sample-stac-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:data:smap:samples-stac-readme:v11.2.2"
semantic_document_id: "kfm-doc-data-smap-samples-stac"
event_source_id: "ledger:docs/data/satellites/smap/samples/stac/README.md"
immutability_status: "version-pinned"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "72 months"
sunset_policy: "Superseded upon sample-refresh cycle"
jurisdiction: "Kansas / United States"
---

<div align="center">

# 📦 **SMAP Sample STAC Collection & STAC Items**  
`docs/data/satellites/smap/samples/stac/`

**Purpose**  
Provide **synthetic, tutorial-grade STAC Items and a miniature STAC Collection**  
used for documentation, onboarding, STAC training, Focus Mode demos, and  
CI smoke testing. These STAC resources contain *no real SMAP data*, and  
are fully sovereignty-safe.

</div>

---

## 📘 1. Overview

This directory contains **small, synthetic STAC examples** modeled after real SMAP  
Collections/Items, but adapted for:

- 📚 documentation & tutorials  
- 🧪 CI smoke tests  
- 🗺️ web demo layers  
- 📖 Story Node & Focus Mode examples  
- 🌐 STAC browser UX demos  

All STAC files:

- are **synthetic**  
- contain safe, small geometries  
- use degraded or random values  
- are FAIR+CARE-pre-approved  
- fully validate under STAC 1.x, DCAT 3.0, JSON-LD, and PROV-O rules  

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Option A)

~~~text
docs/data/satellites/smap/samples/stac/
├── 📄 README.md                       # This file
│
├── 📚 collection.json                 # Mini STAC Collection (synthetic, tutorial-safe)
│
├── 📦 item_sm.json                    # Sample STAC Item — Soil Moisture
├── 📦 item_ft.json                    # Sample STAC Item — Freeze–Thaw
└── 📦 item_vwc.json                   # Sample STAC Item — Vegetation Water Content
~~~

---

## 🧩 3. File Responsibilities

### 📚 `collection.json`
Demonstrates:

- core STAC Collection structure  
- license, providers, keywords  
- spatial and temporal extents  
- "kfm:*" tutorial metadata fields  
- minimal asset schemas  
- PROV-O dataset lineage examples  

### 📦 `item_sm.json` — Soil Moisture Item
Shows:

- single-tile spatial footprint  
- safe synthetic soil-moisture raster asset  
- QA sample metadata  
- uncertainty + governance stubs  
- proper link structure (self/root/parent)  

### 📦 `item_ft.json` — Freeze–Thaw Item
Shows:

- categorical FT preview asset  
- synthetic geometry and timestamps  
- proper STAC roles (thumbnail, data, metadata)  

### 📦 `item_vwc.json` — Vegetation Water Content Item
Shows:

- vegetation-focused STAC Item template  
- minimal synthetic VWC field  
- correct asset media types  
- simplified uncertainty and QA examples  

---

## 🔐 4. FAIR+CARE & Sovereignty Notes

These STAC samples:

- contain **no real sovereign-sensitive geometry**  
- contain **no actual SMAP values**  
- are intentionally designed to be *non-representative*  
- carry optional `"kfm:*"` metadata only for tutorials  
- require **no H3 masking**, but demonstrate how it works  

All assets are considered **CARE-A public training data**.

---

## 🧪 5. Validation & CI Behavior

CI validates:

- full STAC 1.x compliance (schemas + extensions)  
- proper link graph  
- valid GeoJSON geometry  
- PROV-O lineage shape  
- DCAT compatibility  
- accessibility metadata (alt text)  
- presence of tutorial-friendly `"kfm:*"` blocks  

These tests ensure docs don’t silently drift out of STAC spec.

---

## 🔁 6. Relationship to SMAP ETL Pipelines

These **samples DO NOT** participate in the SMAP ETL process.

They are used for:

- documentation  
- onboarding  
- example notebooks  
- STAC demos  
- Story Node & Focus Mode examples  
- UI prototypes  

Production STAC content resides under:

```
data/satellites/smap/stac/
data/satellites/smap/qa/
data/satellites/smap/transforms/
```

---

## 🔮 7. Applications Across KFM

- 🌐 web documentation  
- 🧭 system training  
- 🧪 CI smoke tests  
- 📘 STAC tutorials  
- 🎓 educational material  
- 🗺️ MapLibre/Cesium examples  

---

## 🧭 8. Version History

| Version | Date       | Summary                                                                                              |
|--------:|------------|------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-29 | Initial sample STAC README; safe synthetic STAC Item templates; FAIR+CARE aligned; emoji-rich output.|

---

<div align="center">

© 2025 Kansas Frontier Matrix  
[⬅️ Back](../README.md) · [🧪 Sample Rasters](../rasters/README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

