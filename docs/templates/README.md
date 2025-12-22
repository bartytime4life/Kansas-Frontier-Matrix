---
title: "KFM Templates — README"
path: "docs/templates/README.md"
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

# KFM Templates

## 📘 Overview

### Purpose

- Provide a governed, copy-first set of Markdown templates for KFM documentation.
- Keep documentation aligned with the canonical pipeline ordering and contract boundaries.
- Reduce drift by making consistent structure the default.

### Template selection

Use the template that matches the artifact you are producing:

- Universal documentation: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Nodes and Focus Mode narratives: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API changes and contract updates: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

### Scope

| In Scope | Out of Scope |
|---|---|
| Template selection guidance and “how to use” notes | Implementing pipeline code, schemas, or APIs |
| The templates under `docs/templates/` | One-off docs that intentionally do not follow governed templates |
| Minimal rules for front matter, IDs, and doc hygiene | Governance decisions that belong in `docs/governance/` |

### Audience

- Primary: Contributors writing governed docs and contracts.
- Secondary: Reviewers validating doc consistency, CI gates, and repository structure.

### Definitions

- Glossary: `docs/glossary.md`
- Governed doc: a Markdown document with KFM front matter and CI-validatable structure.
- Story Node: a narrative document that is provenance-linked and machine-ingestible.
- Contract extension: a governed addition/update to an API contract (REST/OpenAPI or GraphQL).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default for most docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Narrative + citations + evidence |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | Endpoint/schema changes |

### Definition of done

- [ ] Selected the correct template for the document type.
- [ ] Copied the template and fully populated front matter.
- [ ] `path` in front matter matches the file location.
- [ ] Any claims about data/schemas/contracts reference canonical IDs/paths.
- [ ] Validation and review steps are listed and repeatable.

## 🗂️ Directory Layout

### This document

- `path`: `docs/templates/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Templates | `docs/templates/` | Governed Markdown templates |
| Governing guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline ordering + invariants |
| Governance | `docs/governance/` | Review gates, ethics, sovereignty |
| Standards | `docs/standards/` | STAC/DCAT/PROV/ontology + repo standards |
| Schemas | `schemas/` | JSON Schemas and validation bundles |
| API boundary | `src/server/` | Contracts, services, redaction, query boundary |
| UI | `web/` | React-based map UI, layer registry |
| Story Nodes | `docs/reports/story_nodes/` | Canonical in the v13 blueprint; not confirmed in repo on older branches |

### Expected file tree for this sub-area

~~~text
📁 docs/
└── 📁 templates/
    ├── 📄 README.md
    ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
    ├── 📄 TEMPLATE__STORY_NODE_V3.md
    └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
~~~

## 🧭 Context

### Background

KFM documentation is part of the system contract. A small set of standardized templates makes it easier to:

- Keep the canonical pipeline ordering intact.
- Keep contract boundaries clear, especially at the API boundary.
- Make Story Nodes and Focus Mode auditable by requiring citations and provenance links.

### Assumptions

- CI enforces (or will enforce) Markdown protocol checks and schema validation for contract artifacts.
- Templates are versioned. Breaking structural changes require a version bump and review.
- Template consumers treat front matter as machine-readable metadata.

### Constraints and invariants

- Do not change front-matter keys without governance review.
- The UI must not read Neo4j directly; all graph access is via the API boundary (`src/server/`).
- Published Story Nodes must be provenance-linked and validate before publication.
- Predictive or AI-generated narrative content is opt-in and must carry uncertainty metadata.

### Open questions

| Question | Owner | Target |
|---|---|---|
| Do we want a dedicated “Doc Index” template separate from Universal docs? | Docs governance | TBD |
| Should templates be mirrored under Story Node canonical paths for curator workflow? | Story + governance | TBD |

### Future extensions

- Add specialized templates under `docs/templates/` for:
  - Data domain runbooks
  - Ontology change proposals
  - Threat models and security reviews
- Introduce template linting checks that confirm:
  - required keys exist
  - `path` matches filesystem path
  - IDs are unique within the repo

## 🗺️ Diagrams

### How templates fit the pipeline

~~~mermaid
flowchart LR
  A[Docs authored<br/>using templates] --> B[CI validation<br/>front matter + schema checks]
  B --> C[Governed docs in repo]
  C --> D[Consumed by stage owners<br/>ETL / Catalog / Graph / API / UI / Story]
~~~

## 📦 Data & Metadata

### Front-matter rules

When you create a new doc from a template:

- Copy the entire template file.
- Update at minimum:
  - `title`
  - `path`
  - `version`
  - `last_updated`
  - `status`
  - `doc_kind`
  - `doc_uuid`
  - `semantic_document_id`
  - `event_source_id`
  - `commit_sha`
  - `doc_integrity_checksum`
- Keep the key set intact.

### Evidence linkage

For Story Nodes and anything that can surface in Focus Mode:

- Link claims to evidence identifiers where possible:
  - STAC Item / Collection IDs
  - DCAT dataset IDs
  - PROV activity IDs
  - graph entity IDs
- Treat uncited narrative as a validation failure for published content.

## 🧠 Story Node and Focus Mode Integration

### Provenance-linked narrative rule

- Every factual claim should trace to a dataset, record, or asset identifier.
- Story Nodes are intended to be machine-ingestible for UI rendering and auditing.

### Optional structured controls

Some Story Node documents may include structured Focus Mode hints.

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI/CD

### Validation steps

- [ ] Markdown protocol validation
- [ ] Schema validation for any referenced STAC/DCAT/PROV assets
- [ ] Story Node checks for citations, entity references, and redaction compliance
- [ ] API contract tests when updating/adding endpoint contracts
- [ ] UI schema checks when touching layer registry or UI contracts
- [ ] Security and sovereignty checks when handling restricted knowledge

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate markdown protocol
# 2) validate schemas
# 3) run contract tests
~~~

## ⚖ FAIR+CARE and Governance

### Review gates

- Use `docs/governance/` as the canonical source for approval requirements.
- Treat changes that affect:
  - sensitive locations
  - culturally sensitive content
  - public API contracts
  - Story Node publication rules
  as requiring human review.

### AI usage constraints

- Ensure the doc’s AI permissions and prohibitions match the intended use.
- Never allow policy generation output to become a governance artifact without explicit review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial templates README | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`