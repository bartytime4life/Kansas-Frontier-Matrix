---
title: "KFM Templates — README"
path: "docs/templates/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
status: "draft"
doc_kind: "Directory README"
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

doc_uuid: "urn:kfm:doc:templates:readme:v1.0.0"
semantic_document_id: "kfm-templates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:templates:readme:v1.0.0"
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

# 🧩 KFM Documentation Templates

> **Purpose (required):** Provide the canonical governed templates under `docs/templates/` and a single, consistent set of rules for using them across the KFM pipeline (ETL → catalogs → graph → API → UI → Story Nodes → Focus Mode).

## 📘 Overview

### What this folder contains

This directory is the **canonical source** for KFM governed documentation templates. These templates exist to ensure:

- consistent front‑matter (IDs, sensitivity/classification, protocol versions)
- consistent section structure (approved headings, checklists, footers)
- consistent linkage to evidence products (STAC/DCAT/PROV identifiers and run IDs)
- consistent architecture boundaries (UI uses contracted APIs, not direct graph access)

### Template selection rule

Use exactly one governed template per new document:

- **Default:** `TEMPLATE__KFM_UNIVERSAL_DOC.md`
- **Narrative + Focus Mode artifact:** `TEMPLATE__STORY_NODE_V3.md`
- **REST/GraphQL contract change:** `TEMPLATE__API_CONTRACT_EXTENSION.md`

If a doc type does not map cleanly to one of the above, mark it as **not confirmed in repo** and propose adding a new governed template before writing ad‑hoc docs.

### Audience

- Contributors authoring or maintaining docs across ETL, catalogs, graph, API, UI, and story layers
- Reviewers enforcing governance, reproducibility, and provenance integrity

### Definitions

- **STAC/DCAT/PROV:** discovery + dataset metadata + provenance lineage
- **Story Node:** governed narrative artifact intended to be rendered in Focus Mode
- **Focus Mode:** UI experience where narrative + map/timeline are presented; all claims must be provenance‑linked
- **Contract‑first API:** schemas (OpenAPI / GraphQL) are the source of truth for API behavior

`docs/glossary.md` is referenced in several project documents, but is **not confirmed in repo**.

### Key artifacts

| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | System + pipeline source of truth |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default governed doc template |
| Story Node Template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story Nodes + Focus Mode narratives |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Contract changes for REST/GraphQL |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | **not confirmed in repo** |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | required reference for governed docs (existence **not confirmed in repo**) |
| Ethics policy | `docs/governance/ETHICS.md` | required reference for governed docs (existence **not confirmed in repo**) |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | required reference for governed docs (existence **not confirmed in repo**) |

### Definition of done

- [ ] Front‑matter complete and valid, and `path:` matches file location
- [ ] Exactly one governed template used (Universal / Story Node / API Contract Extension)
- [ ] H2 headings conform to the approved heading registry used by the templates
- [ ] Internal references resolve (no broken paths)
- [ ] Any system rule stated is backed by the Master Guide or explicitly marked *not confirmed in repo*
- [ ] Validation steps are listed and repeatable (CI‑ready)
- [ ] Governance + CARE/sovereignty considerations explicitly stated when relevant
- [ ] No implied prohibited AI actions (see `ai_transform_prohibited`)

## 🗂️ Directory Layout

### This document

- `path`: `docs/templates/README.md`

### Expected file tree for this sub-area

~~~text
📁 docs/
├── 📁 templates/
│   ├── 📄 README.md
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
~~~

### Templates catalog

| Template | Intended use | Typical reviewers | Notes |
|---|---|---|---|
| `TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default for most docs (designs, runbooks, domain readmes, standards drafts) | Domain owners + Docs reviewers + Governance when sensitive | Includes standard sections + checklists |
| `TEMPLATE__STORY_NODE_V3.md` | Story Nodes rendered in Focus Mode (narrative must be evidence‑linked) | Narrative curators + Governance + Editor | Every factual claim maps to dataset/document ID |
| `TEMPLATE__API_CONTRACT_EXTENSION.md` | Document an API change (REST/GraphQL), plus tests and schema placement | API owners + Security/Governance + UI owners | Contract-first; includes redaction rules and provenance hooks |

## 🧭 Context

### Canonical pipeline ordering

KFM’s pipeline order is non‑negotiable:

ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode.

Documentation templates exist to keep this ordering explicit in every doc and to prevent “shortcuts” that bypass provenance, contracts, or governance.

### Formatting invariants used by governed templates

- **Path fidelity:** `path:` in front‑matter must match the file’s repository location.
- **Stable IDs:** `doc_uuid` and `semantic_document_id` must be stable across edits; bump `version` when semantics change.
- **AI constraints:** `ai_transform_permissions` and `ai_transform_prohibited` must be respected by authors and reviewers.
- **Fencing convention:** use outer backticks only for chat wrappers; inside repo docs, prefer inner tildes for code/trees/mermaid blocks (see Data & Metadata section).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Neo4j Graph]
  C --> D[API Contracts]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  T1["Universal Doc Template"] --- A
  T1 --- B
  T1 --- C
  T1 --- D
  T1 --- E

  T2["Story Node Template v3"] --- F
  T2 --- G

  T3["API Contract Extension Template"] --- D
~~~

## 📦 Data & Metadata

### Front-matter expectations

All governed templates require YAML front‑matter. Minimum expectations:

- `title`, `path`, `version`, `last_updated`, `status`, `doc_kind`, `license`
- protocol versions (KFM‑MDP / MCP‑DL / KFM‑ONTO / KFM‑PPC)
- governance and sensitivity fields (`fair_category`, `care_label`, `sensitivity`, `classification`, `jurisdiction`)
- stable identifiers (`doc_uuid`, `semantic_document_id`, `event_source_id`)
- AI usage constraints (`ai_transform_permissions`, `ai_transform_prohibited`)
- integrity placeholder (`doc_integrity_checksum`)

### Minimal example snippet

~~~yaml
---
title: "TBD"
path: "docs/<area>/<doc>.md"
version: "v1.0.0"
last_updated: "YYYY-MM-DD"
status: "draft"
doc_kind: "Guide"
license: "CC-BY-4.0"

doc_uuid: "urn:kfm:doc:<namespace>:v1.0.0"
semantic_document_id: "kfm-<namespace>-v1.0.0"
event_source_id: "ledger:kfm:doc:<namespace>:v1.0.0"
commit_sha: "<latest-commit-hash>"
doc_integrity_checksum: "sha256:<calculate-and-fill>"
---
~~~

## 🌐 STAC, DCAT & PROV Alignment

### Required linkage

When a document describes data, outputs, or claims, it should link to identifiers in:

- **STAC**: collection IDs and item IDs
- **DCAT**: dataset identifiers and distributions
- **PROV**: activity/run IDs and derivation chains

### Round-trip traceability

Graph nodes should store **references** back to catalog identifiers (STAC/DCAT) rather than duplicating large payloads. This enables round‑trip traceability between graph and catalogs and keeps provenance first‑class.

## 🧱 Architecture

### Contract-first + API boundary

- APIs are contract‑first: OpenAPI/GraphQL schemas are the authoritative contract.
- UI must consume data via contracted APIs or static catalogs, **never** by directly reading Neo4j.
- Any new interactive UI feature must have corresponding API support and tests.

### Where changes land

| Layer | Canonical location | Notes |
|---|---|---|
| ETL/pipelines | `src/pipelines/` | Deterministic, reproducible runs |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Validate schemas + integrity |
| Graph | `src/graph/` | Ontology aligned; store catalog references |
| API | `src/server/` | Contracts + tests required |
| UI | `web/` | No direct graph calls |
| Story Nodes | `docs/reports/story_nodes/` | Evidence-linked narrative |

Some exact subpaths may vary by repo revision; if a path is missing, mark as **not confirmed in repo** and reconcile with the Master Guide before proceeding.

## 🧠 Story Node & Focus Mode Integration

### Narrative integrity rule

Story Nodes must be written in a neutral, evidence-led tone, and **every factual claim must map to a cited dataset/document ID**.

### Focus Mode expectations

Focus Mode content must be provenance-linked (no “orphan facts”). Any AI-generated elements must be clearly indicated and must not imply prohibited actions (e.g., inferring sensitive locations).

## 🧪 Validation & CI/CD

### Recommended checks

- [ ] `markdown-lint`
- [ ] `schema-lint` (STAC/DCAT/PROV where applicable)
- [ ] `footer-check` (required refs present)
- [ ] `accessibility-check`
- [ ] `diagram-check`
- [ ] `metadata-check`
- [ ] `provenance-check`
- [ ] `secret-scan`
- [ ] `pii-scan`

### Reproduction

~~~bash
# Replace with repo-specific commands once confirmed.
# 1) validate schemas (STAC/DCAT/PROV)
# 2) run unit/integration tests
# 3) run doc lint / markdown checks
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Trigger governance/security review when:

- changing classification or sensitivity of an artifact
- publishing derived datasets from sensitive or restricted inputs
- adding a UI layer that could reveal sensitive locations by interaction or zoom

### CARE / sovereignty considerations

When content intersects with community-defined sensitive areas, ensure redaction/generalization is applied and decisions are documented.

### AI usage constraints

- Allowed AI actions should match `ai_transform_permissions`.
- Prohibited AI actions must remain prohibited; do not imply “policy generation” or “sensitive location inference” in docs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-27 | Initial templates README | TBD |

---

Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md` (not confirmed in repo)
- Sovereignty: `docs/governance/SOVEREIGNTY.md` (not confirmed in repo)
- Ethics: `docs/governance/ETHICS.md` (not confirmed in repo)
---
