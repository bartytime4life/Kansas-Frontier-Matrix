---
title: "🌦️ KFM v11.2.2 — Climate Story Node Templates"
path: "docs/story-nodes/domains/climate/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Climate Systems Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:climate:templates:v11.2.2"
semantic_document_id: "kfm-storynodes-climate-templates"
event_source_id: "ledger:storynodes/climate/templates"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/storynode-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/storynodes-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Template Directory README"
intent: "kfm-climate-storynode-templates"
lifecycle_stage: "stable"

fair_category: "F1-A2-I2-R2"
care_label: "Environmental"
classification: "Public"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 climate templates"
---

<div align="center">

# 🌦️ **Climate Story Node Templates (KFM v11)**  
### *Authoring Patterns · Schema Skeletons · Relation Models*  

`docs/story-nodes/domains/climate/templates/README.md`

**Purpose**  
Provide **official templates**, **JSON skeletons**, and **relation-pattern guidance**  
for constructing climate Story Nodes safely, accurately, and consistently.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/climate/templates/
├── 📄 README.md                         # Template overview (this file)
├── 📝 story-node-climate.md             # Markdown authoring template
├── 🧩 story-node-climate.json           # JSON schema-aligned skeleton
└── 🔗 relation-patterns.md              # Common graph relation patterns for climate
~~~

All files here sync with:

- `story-node.schema.json`
- climate domain rules
- Focus Mode v3 needs
- STAC/DCAT conventions
- provenance standards (PROV-O)
- CF conventions (variables/units)
- KFM v11 ethics & narrative governance

---

## 📘 Overview

This directory hosts the **author-facing templates** used when creating Climate Story Nodes.

Climate nodes cover:

- storms, tornado outbreaks, derechos  
- heatwaves, cold spells  
- drought and precipitation anomalies  
- climate change trends  
- fire-weather conditions  
- model-driven outputs (HRRR, GFS, ERA5, GOES, CMIP6, etc.)  
- air-quality–relevant atmospheric events  
- seasonal cycles (ENSO, PDO, blocking patterns)

Templates ensure:

- proper spacetime structure  
- scientific rigor  
- data/mechanism clarity (models vs observations)  
- provenance completeness  
- standardized narrative layout  
- easy ingestion into Focus Mode v3  
- public-safe explanations  

---

## 🧱 Template Types

### 📝 **Markdown Template — `story-node-climate.md`**
Human-friendly authoring template with:

- narrative scaffolding  
- observation/interpretation distinctions  
- environmental impact subsections  
- spacetime structure  
- STAC/DCAT dataset linking guidance  
- Focus Mode alignment text blocks  
- data provenance prompts  

### 🧩 **JSON Template — `story-node-climate.json`**
Schema-valid JSON skeleton including:

- `type: "story-node"`  
- `id`, `title`, `summary`  
- `spacetime.when` interval + precision  
- `spacetime.geometry` (polygon, bbox, region, etc.)  
- `climate.context` structured fields (anomaly metadata, event classification)  
- `relations[]` using climate domain patterns  
- `provenance[]`  
- optional STAC `assets[]` references  

### 🔗 **Relation Patterns — `relation-patterns.md`**
Defines climate-specific graph-safe patterns:

- `about` → event  
- `references` → NOAA/NCEI/ERA5/HRRR analyses  
- `derived-from` → models, pipelines, reanalysis  
- `analog-of` → historical analog events  
- `counterpoint` → updated climate attribution  
- `affects` → hydrology, soil, ecology domains  

---

## 🧬 Compliance Notes

Climate Story Node templates must uphold:

- **KFM-MDP v11.2.2**  
- **FAIR+CARE** transparency (environmental justice framing)  
- **CF conventions** for units/variables  
- **PROV-O** lineage clarity  
- **GeoSPARQL** spatial semantics  
- **OWL-Time** temporal modeling  
- strict separation of **observations vs. model output**  
- **no exaggerated attribution claims**  

---

## 🧪 CI/CD Notes

Template changes require:

- Story Node schema re-validation  
- STAC/DCAT schema regression tests  
- markdown-protocol compliance  
- CF unit/variable checks (if applicable)  
- integrity hashes updated  
- governance sign-off for narrative pattern changes  

---

## 🕰️ Version History

| Version | Date       | Summary                                                        |
|--------:|------------|----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed climate template set; synced to v11 domain.  |
| v11.2.1 | 2025-11-29 | Added base Markdown/JSON templates + relation-pattern scaffold. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

