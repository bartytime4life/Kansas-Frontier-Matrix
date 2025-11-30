---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Templates"
path: "docs/story-nodes/domains/archaeology/templates/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:templates:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-templates"
event_source_id: "ledger:storynodes/archaeology/templates"
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
intent: "kfm-archaeology-storynode-templates"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
ttl_policy: "36 months"
sunset_policy: "Superseded by future v12 domain rewrite"
---

<div align="center">

# 🏺 **Archaeology Story Node Templates (KFM v11)**  
### *Authoring Patterns · Schema Skeletons · Relation Models*  

`docs/story-nodes/domains/archaeology/templates/README.md`

**Purpose**  
Provide **authoring templates**, **JSON skeletons**, and **relation-pattern guides**  
for constructing archaeology Story Nodes in a safe, consistent, FAIR+CARE-aligned way.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/archaeology/templates/
├── 📄 README.md                         # Template overview (this file)
├── 📝 story-node-archaeology.md         # Markdown authoring template
├── 🧩 story-node-archaeology.json       # JSON schema-aligned skeleton
└── 🔗 relation-patterns.md              # Common graph relations & patterns
~~~

All files in this directory must remain synchronized with:

- `story-node.schema.json`
- archaeology domain rules
- Focus Mode v3 requirements
- FAIR+CARE masking rules
- Neo4j graph relation conventions

---

## 📘 Overview

This directory provides **official templates** for archaeology Story Nodes.  
These templates enforce:

- **Generalized geometries** (H3, counties, broad regions)  
- **Proper temporal modeling** (`precision`, `original_label`, intervals)  
- **Correct graph relations** (`about`, `references`, `counterpoint`, `part-of`)  
- **CIDOC-CRM · GeoSPARQL · OWL-Time alignment**  
- **FAIR+CARE compliance**, especially for Indigenous-linked sites  

Use these templates when creating:

- Site-level nodes  
- Survey / excavation event nodes  
- Geophysics-only nodes  
- Reinterpretation / counterpoint nodes  
- Cultural landscape multi-phase narratives  

---

## 🧱 Template Types

### 📄 **Markdown Template — `story-node-archaeology.md`**
High-clarity, author-friendly template with:

- guidance text  
- markdown sections for:  
  - narrative  
  - space  
  - time  
  - relations  
  - sources  
  - CARE considerations  
- auto-extractable structure for Focus Mode  

### 🧩 **JSON Template — `story-node-archaeology.json`**
A **schema-valid** skeleton including:

- `type: "story-node"`  
- `id` placeholder (public-safe ID pattern)  
- `title`, `summary`, `narrative`  
- `spacetime.when` + `spacetime.geometry`  
- `relations[]` (with typed examples)  
- `provenance` blocks  
- optional `media[]` with STAC hints  

### 🔗 **Relation Patterns — `relation-patterns.md`**
Defines safe graph patterns such as:

- Site → Feature (`part-of`)  
- Site → Report (`references`)  
- Excavation → Person (`carried-out-by`)  
- Interpretation → Previous Understanding (`counterpoint`)  

All relation patterns avoid exposing sensitive content.

---

## 🧬 Compliance Notes

All templates in this directory:

- MUST remain compliant with **KFM-MDP v11.2.2**  
- MUST avoid precise coordinates in any example  
- MUST use clear observation → interpretation separation  
- MUST follow FAIR+CARE and Indigenous sovereignty rules  
- MUST validate automatically under CI  

Any update to `story-node.schema.json` requires **regenerating these templates**.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                  |
|--------:|------------|---------------------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed release of archaeology templates; synced with domain README. |
| v11.2.1 | 2025-11-29 | Added Markdown + JSON templates and relation-patterns scaffold.             |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

