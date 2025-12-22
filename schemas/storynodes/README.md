---
title: "KFM Schemas — Story Nodes"
path: "schemas/storynodes/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:schemas:storynodes:readme:v1.0.0"
semantic_document_id: "kfm-schemas-storynodes-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:storynodes:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculate-and-fill>"
---

# Schemas — Story Nodes

## 📘 Overview

### Purpose
This README governs **what lives in** `schemas/storynodes/` and **how it is used** to validate KFM Story Node artifacts.

Specifically, it defines:
- The contract intent for **Story Node schema validation** (what must be validated).
- Expected directory layout and file naming for Story Node-related schema artifacts.
- Versioning and governance expectations for changing these contracts.

### Scope

| In Scope | Out of Scope |
|---|---|
| Story Node schema(s) and supporting shape bundles (JSON Schema + optional SHACL shapes) | Writing/curating Story Node narrative content itself |
| Validation intent for published Story Nodes (front-matter, citations, entity refs, redaction compliance) | API endpoint design (see `src/server/contracts/` + `docs/api/`) |
| Versioning expectations for these schema artifacts | UI rendering details (see `web/` and UI schema registry under `schemas/ui/`) |

### Audience
- **Primary:** maintainers of schema/CI validation and Story Node publish workflows
- **Secondary:** Story Node authors/curators, API/UI maintainers integrating Story Nodes into Focus Mode

### Definitions
- Glossary: `docs/glossary.md`
- Terms used in this doc:
  - **Story Node** (machine-ingestible narrative artifact)
  - **Focus Mode** (provenance-linked-only narrative view)
  - **Contract artifact** (a machine-validated schema/spec)
  - **Evidence IDs** (STAC/DCAT/PROV identifiers referenced by Story Nodes)
  - **Redaction / generalization** (rules applied for sensitive locations/content)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (canonical pipeline) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Source of non-negotiable ordering + invariants |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Authoring template + section expectations |
| Story Node corpus (canonical home) | `docs/reports/story_nodes/` | Curators | Published artifacts should validate |
| Story Node schema(s) | `schemas/storynodes/` | Schema/CI maintainers | This directory (contract artifacts) |
| v13 Blueprint (canonical homes + minimum contract set) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | **not confirmed in repo** (path referenced by design docs) |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Clear explanation of what must be validated for published Story Nodes
- [ ] Directory layout documented (including expected artifacts + statuses)
- [ ] Versioning rule documented for story node schemas
- [ ] Validation steps listed (even if tooling is “not confirmed in repo”)
- [ ] FAIR+CARE / sovereignty considerations stated (redaction/generalization expectations)

## 🗂️ Directory Layout

### This document
- `path`: `schemas/storynodes/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Schemas | `schemas/` | JSON Schemas + optional shape bundles for contract validation |
| Story Nodes | `docs/reports/story_nodes/` | Story Node markdown artifacts (draft/published structure may vary) |
| Templates | `docs/templates/` | Authoring templates, including Story Node v3 |
| CI workflows | `.github/workflows/` | Validation gates (exact jobs not described here) |
| Tests | `tests/` | Schema/contract tests (if implemented) |

### Expected file tree for this sub-area
> Items marked **not confirmed in repo** indicate *intended* artifacts that may be added later.

~~~text
📁 schemas/
└── 📁 storynodes/
    ├── 📄 README.md
    ├── 📄 storynode-v3.schema.json                # not confirmed in repo
    ├── 📄 storynode-v3.shacl.ttl                  # not confirmed in repo
    ├── 📄 CHANGELOG.md                            # not confirmed in repo
    └── 📁 examples/                               # not confirmed in repo
        ├── 📄 storynode_v3_minimal.md             # not confirmed in repo
        └── 📄 storynode_v3_full.md                # not confirmed in repo
~~~

## 🧭 Context

### Where this sits in the canonical pipeline
KFM’s pipeline ordering is:

**ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**

This directory exists because Story Nodes and Focus Mode are **contract-bound**: published Story Nodes must be machine-validatable, and Focus Mode must only consume **provenance-linked** content.

### What Story Node schemas are expected to enforce
At minimum, published Story Nodes should validate:
- **Front-matter** (required governed metadata fields + KFM Markdown protocol compliance)
- **Citations / evidence references** (every claim traces to a dataset/document/asset ID)
- **Entity references** (graph linkage IDs resolve or have creation tickets)
- **Redaction compliance** (no restricted locations leaked; generalization rules respected)

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[Story Node authoring<br/>docs/reports/story_nodes] --> B[Schema validation<br/>schemas/storynodes]
  B -->|pass| C[Published Story Node]
  B -->|fail| D[Fix: citations/entity refs/redaction/front-matter]
  C --> E[API serves Story Node<br/>src/server]
  E --> F[UI renders + Focus Mode view<br/>web]
~~~

## 📦 Data & Metadata

### What Story Nodes should carry (contract intent)
A Story Node is a narrative artifact that should be **machine-ingestible**:
- Links to **graph entity IDs** (e.g., Place/Event/Person/Organization)
- References to **evidence IDs** (STAC/DCAT/PROV identifiers)
- Local assets (if any) with attribution (images/maps/figures)
- Optional Focus Mode controls (layer/time/center hints), if supported

### Sensitivity considerations
If a Story Node touches restricted locations or culturally sensitive content:
- The artifact must follow documented generalization/redaction rules.
- Review gates may be required (see governance section below).

## 🌐 STAC, DCAT & PROV Alignment

Story Nodes should link back to the evidence chain:
- **STAC**: item IDs / asset identifiers used as evidence
- **DCAT**: dataset identifiers for attribution/licensing metadata
- **PROV**: run/activity IDs to show lineage of derived artifacts (if any)

## 🧱 Architecture

### Contract boundary reminder
- **UI never reads Neo4j directly.**
- Story Nodes should be served through the **API boundary**, so redaction/generalization rules can be enforced consistently.

### What belongs in this directory
- JSON Schemas and/or SHACL shapes used to validate Story Nodes and their referenced structures.
- A changelog for schema evolution (recommended).
- Example fixtures (recommended) for CI tests and author guidance.

## 🧪 Validation & CI/CD

### Validation checklist for published Story Nodes
- [ ] Front-matter present, complete, and protocol-compliant
- [ ] Citations/evidence refs present for factual claims
- [ ] Entity references are resolvable or have tracked creation tickets
- [ ] Redaction/generalization requirements satisfied
- [ ] No prohibited AI behaviors implied by the artifact metadata

### Reproduction
Tooling is **not confirmed in repo**. The following is a placeholder structure to keep validation repeatable:

~~~bash
# Placeholder example — replace with repo-specific commands

# 1) validate Story Node artifacts against Story Node schema(s)
#    (implementation not confirmed in repo)

# 2) run schema/unit tests (if present)
#    (implementation not confirmed in repo)

# 3) run markdown protocol linting
#    (implementation not confirmed in repo)
~~~

### Versioning expectations
- Schema artifacts under `schemas/` are versioned with **semantic versioning**.
- Any change to a schema increments its version and should be captured in a changelog.

## ⚖ FAIR+CARE & Governance

### Review gates
Changes here may require human review when they impact:
- Validation rules that affect published content
- Redaction/generalization behavior for sensitive locations
- Any schema that gates what can appear in Focus Mode

### CARE / sovereignty considerations
- Treat culturally sensitive knowledge and restricted locations as high-risk.
- Prefer enforcing protections at the API boundary, and ensure Story Nodes remain compliant.

### AI usage constraints
This README inherits KFM-governed AI transform rules:
- Allowed: summarize, structure extraction, translation, keyword indexing
- Prohibited: generating new policy or inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for Story Node schemas | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

