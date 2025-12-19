---
title: "Kansas Frontier Matrix — Documentation Index"
path: "docs/README.md"
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

doc_uuid: "urn:kfm:doc:docs:readme:v1.0.0"
semantic_document_id: "kfm-docs-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:docs:readme:v1.0.0"
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

# Kansas Frontier Matrix — Documentation Index

## 📘 Overview

### Purpose
This document is the entry point for the `docs/` directory.
Use it when you’re asking:

- “Where do I put this documentation?”
- “Which governed template should I start from?”
- “What is the canonical source of truth for KFM’s pipeline and invariants?”

### Scope
| In Scope | Out of Scope |
|---|---|
| Navigation for `docs/` and how docs map to the KFM pipeline | Detailed implementation docs for any single subsystem |
| Pointers to canonical guides, templates, and governance references | Dataset-specific narratives and evidence writeups (see Story Nodes) |
| “Where do I put this?” placement rules for docs | API endpoint specifics (see API contract docs) |

### Audience
- Primary: Contributors (data, pipelines, graph, API, UI, story/narrative)
- Secondary: Reviewers, maintainers, and external integrators who need to locate the governing contracts

### Definitions
- Glossary: **not confirmed in repo** (expected at `docs/glossary.md`)
- “Canonical pipeline”: the non-negotiable ordering described in `MASTER_GUIDE_v12.md`
- “Governed doc”: a Markdown document with required front-matter and validation gates (see `docs/templates/`)

### Which template should I use?
- Use the **Universal doc template** for design docs, guides, subsystem documentation, and proposals.
- Use the **Story Node template** for narrative nodes and Focus Mode content.
- Use the **API Contract Extension template** when adding/changing REST/GraphQL contracts.

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (v12 draft) | [`docs/MASTER_GUIDE_v12.md`](MASTER_GUIDE_v12.md) | TBD | System map, invariants, pipeline ordering |
| Universal doc template | [`docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`](templates/TEMPLATE__KFM_UNIVERSAL_DOC.md) | TBD | Default template for governed docs |
| Story Node template | [`docs/templates/TEMPLATE__STORY_NODE_V3.md`](templates/TEMPLATE__STORY_NODE_V3.md) | TBD | Use for narrative nodes + Focus Mode content |
| API Contract Extension template | [`docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`](templates/TEMPLATE__API_CONTRACT_EXTENSION.md) | TBD | Use for REST/GraphQL contract changes |
| Governance references | `docs/governance/` | TBD | ROOT_GOVERNANCE / ETHICS / SOVEREIGNTY |
| Documentation standards | `docs/standards/` | TBD | Markdown protocol + doc lint rules |
| Story Node outputs | `docs/reports/**/story_nodes/` | TBD | Curated narrative artifacts with provenance linkage |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Links to internal docs resolve (no broken relative links)
- [ ] Canonical pipeline ordering is stated and unchanged
- [ ] Template choice guidance is present and consistent with `docs/templates/`
- [ ] Governance + CARE/sovereignty considerations are referenced

## 🗂️ Directory Layout

### Repo top-levels (expected)
~~~text
.github/
data/
docs/
mcp/
schemas/
src/
tests/
tools/
web/
releases/
~~~

### This document
- `path`: `docs/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Project master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline, system inventory, extension matrix |
| Standards | `docs/standards/` | Markdown protocol + validation rules (governed) |
| Templates | `docs/templates/` | Governed doc templates (universal / story / API contracts) |
| Data-domain docs | `docs/data/` | Domain-specific documentation + mappings to catalogs |
| Pipelines docs | `docs/pipelines/` | ETL + catalog build + graph build docs |
| Graph docs | `docs/graph/` | Ontology, labels/edges, migrations, integrity rules |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Frontend / design docs | `web/` + `docs/design/` | Map layers, Focus Mode UX, a11y |
| Governance | `docs/governance/` | Policy + ethics + sovereignty rules |
| Security | `.github/SECURITY.md` + `docs/security/` | Security posture + technical standards |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability and governance metrics |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV artifacts (validated) |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📄 README.md
├── 📄 MASTER_GUIDE_v12.md
├── 📁 standards/
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 data/
├── 📁 pipelines/
├── 📁 graph/
├── 📁 design/
├── 📁 governance/
├── 📁 security/
├── 📁 telemetry/
└── 📁 reports/
    └── 📁 <case-study>/
        └── 📁 story_nodes/
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system with governed data, catalogs, graph semantics, APIs, and a map/narrative UI.
Documentation in `docs/` is treated as a contract: it defines where things live, the invariants contributors must not break, and how new work fits into the overall system.

### Assumptions
- The canonical pipeline ordering remains the source of truth for how all subsystems connect.
- Templates in `docs/templates/` are the preferred starting point for new governed docs.
- New domains and outputs will continue to expand the documentation surface area (data, graph, APIs, UI, story nodes).

### Constraints / invariants
- The canonical pipeline ordering is preserved:
  - **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- Frontend consumes contracts via APIs (no direct graph dependency).
- Focus Mode only consumes provenance-linked content (no unsourced narrative).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical glossary (`docs/glossary.md`)? | TBD | TBD |
| Do we maintain a separate docs site nav (MkDocs/Docusaurus), or rely on repo browsing? | TBD | TBD |

### Future extensions
- Add a governed documentation “index of indexes” (by subsystem, by data domain, by release).
- Add doc automation for link checking and template conformance (if not already present).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant Contributor
  participant Docs as Docs Repo
  participant CI as CI Gates
  Contributor->>Docs: Add/Update governed Markdown doc
  Docs->>CI: Markdown protocol + schema validation
  CI-->>Contributor: Pass/Fail with actionable errors
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Documentation source files | Markdown | `docs/**` | Markdown protocol validation |
| Templates | Markdown | `docs/templates/**` | Markdown protocol validation |
| Catalog artifacts (referenced by docs) | JSON / JSON-LD | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | STAC/DCAT/PROV schema validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered docs (platform-dependent) | HTML | Git hosting / docs site | N/A (implementation-defined) |
| Story Nodes | Markdown | `docs/reports/**/story_nodes/**` | Story Node template + provenance rules |

### Sensitivity & redaction
- Documentation must not include secrets, credentials, or restricted-location details without following `docs/governance/` rules.
- If a doc references restricted locations, describe the generalization/redaction approach and the applicable governance policy.

### Quality signals
- Accuracy: statements are traceable to datasets, catalogs, or governed docs.
- Link integrity: internal doc links resolve.
- Consistency: terminology matches the ontology and the master guide invariants.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Docs should reference STAC Collection/Item identifiers when discussing spatial-temporal assets.
- STAC artifacts are expected under `data/stac/collections/` and `data/stac/items/`.

### DCAT
- Docs should reference DCAT dataset identifiers when describing datasets and distribution links.
- DCAT artifacts are expected under `data/catalog/dcat/`.

### PROV-O
- Docs should reference PROV activity/run identifiers when describing transforms and lineage.
- PROV artifacts are expected under `data/prov/`.

### Versioning
- When updating datasets or catalogs, document predecessor/successor relationships and keep versioning consistent across catalogs and graph lineage.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Documentation (`docs/`) | Canonical contracts + explanations | Markdown protocol |
| Templates (`docs/templates/`) | Governed doc scaffolds | Markdown protocol |
| Standards (`docs/standards/`) | Rules, linting expectations, schemas references | Markdown + (as applicable) JSON Schema |
| Governance (`docs/governance/`) | Ethics, sovereignty, review gates | Policy docs |
| Subsystem docs | Explain ETL/graph/API/UI/story specifics | Links to code + schemas |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Document templates | `docs/templates/` | Semver + version history in each template |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Draft until promoted; changes require review |
| STAC/DCAT/PROV schemas | `schemas/` | Semver + schema validation gates |
| API schemas | `src/server/` + contract docs | Backward compatible or version bump + tests |
| Layer registry | `web/` | Schema-validated + a11y reviewed |

### Extension points checklist (for future work)
- [ ] New data domain documented under `docs/data/<domain>/...`
- [ ] New pipeline behavior documented under `docs/pipelines/...`
- [ ] New ontology elements documented under `docs/graph/...`
- [ ] New endpoints documented with an API contract extension doc
- [ ] New UI layers documented under `docs/design/...` and registered under `web/...`
- [ ] New narrative behaviors documented as Story Nodes + Focus Mode rules

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Nodes provide curated, provenance-linked narrative content.
- Focus Mode consumes Story Nodes and graph-derived context bundles via the API layer.

### Provenance-linked narrative rule
- Every factual claim in Story Nodes must trace to a dataset / record / asset ID (catalog or source document).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + structure)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (where docs reference graph constraints)
- [ ] API contract tests (where docs describe endpoints/contracts)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Replace placeholders with repo-specific commands.
# 1) validate docs
# 2) validate schemas
# 3) run unit/integration tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Doc validation status | CI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Governance- or sovereignty-impacting changes require human review (**see `docs/governance/`**).
- API contract changes require contract tests and versioning review.

### CARE / sovereignty considerations
- If documentation touches culturally sensitive content or restricted locations, follow the applicable sovereignty policy and document any generalization/redaction applied.

### AI usage constraints
- Respect `ai_transform_permissions` / `ai_transform_prohibited` in this document’s front-matter.
- Do not introduce “new policy” text via AI without governance review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `docs/` README scaffold | TBD |

---
Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`