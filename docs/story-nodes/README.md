---
title: "Story Nodes — README"
path: "docs/story-nodes/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:story-nodes:readme:v1.0.0"
semantic_document_id: "kfm-story-nodes-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:story-nodes:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Story Nodes

## 📘 Overview

### Purpose
Story Nodes are governed narrative artifacts designed to be **machine-ingestible** and **provenance-linked** for the KFM Story → Focus Mode experience. They connect human-readable narrative to catalog/graph evidence so Focus Mode can render context without unsourced claims.

### Scope
| In Scope | Out of Scope |
|---|---|
| Story Node authoring conventions and required fields | Full historical interpretation not supported by evidence |
| Provenance linking rules (STAC/DCAT/PROV + graph references) | UI styling/implementation details beyond contracted interfaces |
| Validation expectations for Story Nodes | Adding new governance policy text (requires governance docs) |

### Audience
- Primary: KFM contributors authoring Story Nodes.
- Secondary: Reviewers validating provenance, sensitivity handling, and Focus Mode readiness.

### Definitions
- Glossary: `docs/glossary.md` (not confirmed in repo)
- Key terms used here:
  - **Story Node**: A curated narrative document linked to evidence and graph entities.
  - **Focus Mode**: UI mode that consumes provenance-linked context bundles.
  - **Evidence**: Source documents/datasets/assets tracked through STAC/DCAT/PROV and the graph.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + invariants |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs maintainers | Required structure for Story Nodes |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review gates / policy roots |
| Ethics | `docs/governance/ETHICS.md` | Governance | Human review triggers |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | Governance | CARE / redaction rules |

### Definition of done
- [ ] Document follows `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- [ ] Every factual claim maps to a cited dataset/document ID (no unsourced narrative)
- [ ] Any sensitive information is generalized/redacted per governance refs
- [ ] Story Node includes references to STAC/DCAT/PROV identifiers where applicable
- [ ] Validation checklist completed (see below)

## 🗂️ Directory Layout

### This document
- `path`: `docs/story-nodes/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Templates | `docs/templates/` | Governed templates including Story Node v3 |
| Canonical guidance | `docs/MASTER_GUIDE_v12.md` | System pipeline + invariants |
| Story Nodes (canonical) | `docs/reports/.../story_nodes/` + graph | Story Node instances (per Master Guide) |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence catalogs + lineage |
| Graph | `src/graph/` | Ontology bindings + graph build |
| APIs | `src/server/` | Contracted access layer |
| UI | `web/` | Focus Mode + map/narrative experience |

> Note: This repo’s canonical Story Node instance directory is stated as `docs/reports/.../story_nodes/` in the Master Guide.
> If your implementation stores Story Nodes elsewhere (e.g., directly under `docs/story-nodes/`), update this README accordingly.
> (Directory convention beyond the Master Guide statement is not confirmed in repo.)

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 story-nodes/
    └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s pipeline explicitly preserves the ordering:
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

Story Nodes are the narrative layer that must remain **evidence-led** and **contracted** (UI does not read Neo4j directly; it consumes the API layer).

### Constraints / invariants
- Story Nodes must be provenance-linked; Focus Mode must not display hallucinated or unsourced claims.
- Any predictive/AI-generated content must be opt-in and include uncertainty/confidence metadata (if applicable).
- UI consumes Story Node and graph context only via API contracts (no direct graph dependency).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Exact on-disk Story Node instance layout and naming convention | TBD | TBD |
| Story Node identifier scheme (slug/uuid mapping) | TBD | TBD |
| Where “citation rendering” rules are specified in the UI | TBD | TBD |

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Primary source items] --> B[Extraction and curation activity]
  B --> C[Story Node]
  C --> D[Focus Mode narrative]
~~~

## 📦 Data & Metadata

### Minimum evidence bundle to reference
A Story Node should reference, at minimum, one or more of:
- STAC Item ID(s)
- DCAT Dataset identifier(s)
- PROV activity/run identifier(s)
- Graph entity IDs (Place/Event/Person/Organization/Document/etc.)

### Optional Focus Mode controls
(Use only when the UI/contract supports these fields; behavior is not confirmed in repo beyond the template.)
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🌐 STAC, DCAT & PROV Alignment

### Provenance requirements
Story Nodes should include:
- `prov:wasDerivedFrom`: list of source IDs (documents/datasets/assets)
- `prov:wasGeneratedBy`: pipeline activity/run ID (when produced by a pipeline step)
- Confidence/uncertainty fields **only if** predictive content is included

## 🧱 Architecture

### How story nodes are served
- API route(s): TBD (not confirmed in repo)
- UI component(s): TBD (not confirmed in repo)
- Required invariant: frontend consumes Story Nodes via APIs, not via direct graph access.

### Audit panel expectations
When Focus Mode renders a Story Node, it should be able to show:
- citations / source IDs
- sensitivity notices
- missing-reference warnings (if any)

(Exact UI behavior not confirmed in repo; keep this aligned with implemented contracts.)

## 🧠 Authoring workflow

### Create a new Story Node
1) Identify evidence:
   - source document IDs and/or STAC/DCAT entries
2) Copy the governed template:
   - `docs/templates/TEMPLATE__STORY_NODE_V3.md`
3) Fill the template with:
   - neutral, evidence-led narrative
   - explicit entity linkage (Place/Event/Person/Org) where applicable
   - cited source IDs for every factual claim
4) Add optional Focus Mode controls only if supported by current UI/API
5) Complete validation checklist before review

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Uses Story Node v3 template structure
- [ ] All referenced entities exist (or have creation tickets)
- [ ] All dataset IDs resolve to catalog entries
- [ ] No prohibited AI actions implied (no speculative additions, no inferring sensitive locations)
- [ ] Sensitive information handled correctly and consistently
- [ ] Links and IDs are stable (no “temporary” URLs where avoidable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate Markdown protocol
# 2) validate STAC/DCAT/PROV artifacts referenced
# 3) run contract tests (if Story Node is served by an endpoint)
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
Story Nodes should be flagged for additional review when they:
- introduce new sensitive places/layers
- reference new external data sources
- change public-facing narrative behavior in Focus Mode
- include predictive/AI-generated claims without uncertainty metadata

### CARE / sovereignty considerations
- Do not expose sensitive locations or culturally restricted knowledge.
- Apply generalization/redaction rules as required by governance docs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial Story Nodes README | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`