~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FILE: docs/templates/TEMPLATE__STORY_NODE_V3.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
---
title: "TEMPLATE — Story Node v3"
path: "docs/templates/TEMPLATE__STORY_NODE_V3.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "template"
doc_kind: "Template"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-ONTO v4.1.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"

governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:templates:story-node-v3:v1.0.0"
semantic_document_id: "kfm-template-story-node-v3-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:story-node-v3:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# TEMPLATE — Story Node v3

## 📘 Overview

### Title
- (Short, human-readable)

### Narrative (factual + source-linked)
- Write in neutral, evidence-led tone.
- Every factual claim must map to a cited dataset/document ID.

### Key entities (graph linkage)
| Entity type | Canonical name / ID | Relationship |
|---|---|---|
| Place | TBD | ABOUT |
| Event | TBD | ABOUT |
| Person/Org | TBD | RELATED |

## 🗂️ Directory Layout

### Where the story node lives
- Markdown: (path)
- Graph node ID: (if applicable)
- STAC item(s): (IDs)

## 🧭 Context

### Why this story node exists
- What question it helps answer in Focus Mode.

### Sensitivity considerations
- If sensitive: describe generalization/redaction expected.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Primary source items] --> B[Extraction and curation activity]
  B --> C[Story Node v3]
  C --> D[Focus Mode narrative]
~~~

## 📦 Data & Metadata

### Source bundle
| Source | Identifier | Notes |
|---|---|---|
| STAC item | TBD | TBD |
| Document | TBD | TBD |
| Map/layer | TBD | TBD |

### Optional Focus Mode controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
- `prov:wasDerivedFrom`: list source IDs
- `prov:wasGeneratedBy`: pipeline activity/run ID
- Confidence/uncertainty fields (if predictive content is included)

## 🧱 Architecture

### How this story node is served
- API route(s) that fetch it
- UI component(s) that render it
- Audit panel expectations (warnings, citations, sensitivity notices)

## 🧠 Story Node & Focus Mode Integration

### Focus Mode behavior expectations
- Map/timeline changes
- Layer toggles
- Citation rendering
- “AI explanation” toggle behavior (if present)

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] All referenced entities exist (or have creation tickets)
- [ ] All dataset IDs resolve to catalog entries
- [ ] No prohibited AI actions implied
- [ ] Sensitive information handled correctly

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)
- FAIR+CARE council review: yes/no
- Security council review: yes/no
- Historian/editor review: yes/no

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
