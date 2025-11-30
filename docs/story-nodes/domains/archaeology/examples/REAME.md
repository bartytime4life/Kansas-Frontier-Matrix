---
title: "🏺 KFM v11.2.2 — Archaeology Story Node Examples"
path: "docs/story-nodes/domains/archaeology/examples/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Annual · Archaeology Domain Board · FAIR+CARE Council"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:storynodes:archaeology:examples:v11.2.2"
semantic_document_id: "kfm-storynodes-archaeology-examples"
event_source_id: "ledger:storynodes/archaeology/examples"
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
doc_kind: "Example Collection"
intent: "kfm-archaeology-storynode-examples"
lifecycle_stage: "stable"

fair_category: "F1-A1-I1-R2"
care_label: "Culturally Sensitive · Indigenous-Linked"
classification: "Generalized / Public-Safe"
jurisdiction: "Kansas / United States"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "36 months"
sunset_policy: "Superseded by v12 example set"
---

<div align="center">

# 🏺 **Archaeology Story Node Examples (KFM v11)**  
### *Generalized, Public-Safe Example Nodes for Reference*  

`docs/story-nodes/domains/archaeology/examples/README.md`

**Purpose**  
Provide **curated, safe, public-ready** example Story Nodes demonstrating  
correct structure, masking, metadata, relations, and narrative alignment  
for the archaeology domain.

</div>

---

## 🗂️ Directory Layout

~~~text
docs/story-nodes/domains/archaeology/examples/
├── 📄 README.md                           # This file
├── 🏞️ protohistoric-wichita-site.json     # Generalized Protohistoric example
├── 🧲 fort-larned-geophysics.json         # Non-invasive survey Story Node
└── 📂 ...                                 # Additional safe public examples
~~~

All examples in this directory are:

- **generalized** (no sensitive coordinates)  
- **FAIR+CARE-compliant**  
- **Story Node v11 schema validated**  
- **safe for public release**  
- **structured to match templates and domain rules**  

---

## 🎯 Purpose of This Directory

This directory exists to give authors **real, fully-compliant examples**, showing:

- How to use **generalized geometries** (H3, county masks, watershed polygons)  
- How to model **multi-phase sites**, **surveys**, **excavations**, and **reinterpretations**  
- How to correctly apply **relations** from the domain’s `relation-patterns.md`  
- How to structure **metadata**, **spacetime**, **media**, and **provenance**  
- How to handle **ethical masking** and **sovereignty flags**  

These examples are safe to share publicly and do not expose restricted content.

---

## 🧪 Validation Requirements

Every example Story Node must:

- Validate against `story-node.schema.json`  
- Pass sovereignty/CARE CI checks  
- Pass STAC/DCAT link validation (if assets are referenced)  
- Use **only** allowed relation patterns  
- Use **generalized** geometries  
- Include proper spacetime precision  

---

## 📘 Example Types Included

### 🏞️ *Generalized Site Narratives*  
- Protohistoric / Historic era generalized sites  
- Multi-phase occupations  
- Masked rural village and camp contexts  

### 🧲 *Geophysics-Only Examples*  
- Magnetometry  
- GPR  
- Resistivity  
- Generalized rasters with STAC hints  

### 🏛️ *Historic Fort / Public-Site Examples*  
- Public locations (e.g., forts, historic parks)  
- Non-sensitive footprints  
- Linked reports and archival resources  

---

## 🚫 What Will Never Appear Here

- Precise unprotected coordinates  
- Burial/sacred site examples  
- Restricted tribal knowledge  
- Internal excavation notes or forms  
- Sensitive photos  
- Unpublished site numbers  

All restricted examples live only in internal, access-controlled directories.

---

## 🕰️ Version History

| Version | Date       | Summary                                                         |
|--------:|------------|-----------------------------------------------------------------|
| v11.2.2 | 2025-11-30 | Initial governed archaeology example set; synced with templates. |
| v11.2.1 | 2025-11-29 | Added initial generalized examples (Protohistoric + geophysics). |

---

<div align="center">

© 2025 Kansas Frontier Matrix — CC-BY 4.0  
[📚 Docs Home](../../../../README.md) · [📏 Standards Index](../../../standards/README.md) · [🛡 Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>

