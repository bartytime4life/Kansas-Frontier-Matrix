---
title: "Kansas Frontier Matrix — Architecture — README"
path: "docs/architecture/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:architecture:readme:v1.0.0"
semantic_document_id: "kfm-architecture-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:architecture:readme:v1.0.0"
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

# KFM — Architecture — README

> **Purpose (required):** Provide the canonical index for `docs/architecture/` and capture the **do‑not‑break invariants** (pipeline ordering, contract boundaries, provenance rules) that govern how KFM evolves.

Quick links (preferred order):
- Master guide (system + pipeline source of truth): `../MASTER_GUIDE_v12.md`
- v13 redesign blueprint (repo structure + contracts): `./KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision (end-to-end): `./KFM_VISION_FULL_ARCHITECTURE.md`
- Next stages blueprint (roadmap + vertical slices): `./KFM_NEXT_STAGES_BLUEPRINT.md`
- Templates (universal / story node / API contract): `../templates/`

---

## 📘 Overview

### Purpose
- Provide a single navigation entry point for architecture documentation.
- Keep cross-cutting rules stable as new domains, evidence products, and narratives are added.
- Make architecture decisions auditable by linking them to contracts (schemas, APIs, templates, tests).

### Scope

| In Scope | Out of Scope |
|---|---|
| Indexing architecture docs, ADRs, and diagrams | Implementing pipelines, APIs, UI, or graph code (belongs in their respective areas) |
| Summarizing the canonical pipeline ordering + invariants | Replacing the Master Guide |
| Guidance on where new architecture artifacts belong | Authoring governance policy text (belongs under `docs/governance/`) |

### Audience
- **Primary:** architecture maintainers + reviewers making cross-cutting decisions.
- **Secondary:** contributors working in ETL, catalogs, graph, API, UI, Story Nodes, Focus Mode.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(if missing, treat as **not confirmed in repo** and add/update accordingly)*.
- **ADR:** Architecture Decision Record (small, versioned decision note).
- **Contract artifact:** schemas, OpenAPI/GraphQL specs, Story Node templates, and other “must not break” interfaces.
- **Invariant:** a rule that must remain true across versions (pipeline ordering; API boundary; provenance-only Focus Mode).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (Draft) | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline + system inventory |
| v13 Redesign Blueprint (Draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch Team | Proposed repo structure + minimum contracts |
| Full Architecture Vision (Draft) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Arch Team | Comprehensive architecture context |
| Next Stages Blueprint (Draft) | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Arch Team | Roadmap: gaps + governance + vertical slice |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Team | Default governed doc structure |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Narrative artifacts for Focus Mode |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API Team | REST/GraphQL contract changes |

### Definition of done (for this document)
- [ ] Front-matter complete + `path:` matches `docs/architecture/README.md`
- [ ] Links resolve to canonical architecture docs *(or are marked **not confirmed in repo**)*
- [ ] Pipeline ordering and invariants match `docs/MASTER_GUIDE_v12.md`
- [ ] “Optional roots” are clearly labeled (skip if absent; fail if present but invalid)
- [ ] Version history updated for edits
- [ ] Governance links present in footer

---

## 🗂️ Directory Layout

### This document
- `path`: `docs/architecture/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | System + pipeline source of truth |
| Architecture | `docs/architecture/` | Architecture docs, ADRs, diagrams |
| Templates | `docs/templates/` | Universal docs, story nodes, API contracts |
| Standards | `docs/standards/` | Markdown protocol + profile docs *(may be partial; missing = not confirmed)* |
| Pipelines | `src/pipelines/` | Deterministic ETL + catalog + graph build |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC / DCAT / PROV outputs |
| Graph | `src/graph/` (+ `data/graph/`) | Ontology + ingest fixtures/import artifacts |
| API boundary | `src/server/` | Contracted access + redaction rules |
| UI | `web/` | React/Map UI + Focus Mode |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 architecture/
    ├── 📄 README.md                          # (this file)
    ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md       # repo restructuring + contract minimums
    ├── 📄 KFM_VISION_FULL_ARCHITECTURE.md     # end-to-end architecture guidance
    ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md        # roadmap / next-stage plan
    ├── 📁 diagrams/                          # optional; not confirmed in repo
    └── 📁 adr/                               # optional; not confirmed in repo
~~~

---

## 🧭 Context

### Background
KFM is a governed, provenance-first knowledge system that turns data into map + narrative experiences.

The canonical pipeline ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Architecture documents in this directory keep that ordering stable while the system expands into new domains, new evidence products, and richer narrative UX.

### Assumptions
- `docs/MASTER_GUIDE_v12.md` is the source of truth for pipeline ordering and system inventory.
- The v13 blueprint is an intended “contract hardening + repo structure cleanup” direction; adoption is repo-dependent.
- Optional directories referenced here should be treated as **optional**: if absent, that is not necessarily an error.

### Constraints / invariants
- **Pipeline ordering must not be inverted** (ETL before catalogs; catalogs before graph; graph behind APIs; UI consumes APIs).
- **API boundary is mandatory:** UI does not query Neo4j directly; it consumes contracted API responses.
- **Provenance is first-class:** Focus Mode content must be provenance-linked; AI-generated elements must be clearly labeled.
- **Determinism:** pipelines + validators are config-driven, replayable, and diffable; outputs are versioned.
- **Optional-root CI rule of thumb:** skip checks when optional roots are missing; fail deterministically when they exist but are invalid.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where should ADRs live and what template should they use? | TBD | TBD |
| What is the minimum diagram set for major architecture changes? | TBD | TBD |
| What are the exact review roles for architecture changes? | TBD | TBD |

### Future extensions
- Add an ADR template under `docs/templates/` and establish `docs/architecture/adr/` conventions.
- Add `docs/architecture/diagrams/` with versioned diagram sources (Mermaid and/or exported images).
- Add “contract inventory” pages that link architecture invariants directly to the schemas/tests that enforce them.

---

## 🗺️ Diagrams

### Canonical pipeline (high level)
~~~mermaid
flowchart LR
  A[ETL runs] --> B[STAC / DCAT / PROV catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Layer]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: request flow (UI → API → Graph)
~~~mermaid
sequenceDiagram
  participant UI as UI (React/Map)
  participant API as API
  participant Graph as Neo4j
  UI->>API: Request context (entity_id)
  API->>Graph: Query subgraph + provenance refs
  Graph-->>API: Result set
  API-->>UI: Contracted payload + provenance pointers
~~~

---

## 📦 Data & Metadata

This directory does not store datasets, but architecture decisions **must** stay aligned to the canonical data lifecycle and outputs:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/`, `data/prov/`)
- Published artifacts must be traceable to raw inputs via PROV activities and stable IDs.

---

## 🌐 STAC, DCAT & PROV Alignment

Architecture decisions that introduce new data products or “evidence artifacts” should describe:
- Which STAC collections/items are produced or extended.
- How DCAT dataset identifiers and distributions are emitted (minimum: title/description/license/keywords).
- Which PROV activities/agents capture lineage (run IDs, tools, timestamps), and how IDs link across layers.

If a decision changes profile expectations (KFM-STAC/KFM-DCAT/KFM-PROV), it is a versioned, governed change.

---

## 🧱 Architecture

### Documents in this directory

| Document | What it’s for | Status |
|---|---|---|
| `README.md` | Index + invariants for `docs/architecture/` | draft |
| `KFM_REDESIGN_BLUEPRINT_v13.md` | Proposed repo structure + contract hardening | draft |
| `KFM_VISION_FULL_ARCHITECTURE.md` | Long-form end-to-end architecture vision | draft |
| `KFM_NEXT_STAGES_BLUEPRINT.md` | Roadmap: gaps + governance + vertical slice plan | draft |

### When to use which governed template
- Use **Universal Doc** for architecture areas, module notes, and standards-aligned guidance.
- Use **API Contract Extension** for new/changed API endpoints or schema contracts (REST/GraphQL).
- Use **Story Node** for narrative artifacts intended for Focus Mode surfacing.

### Architecture change checklist (practical)
- Does the change affect more than one pipeline stage (Data/Catalog/Graph/API/UI/Story/Telemetry)?
- If yes: document the invariant/contract impact here and/or in an ADR.
- Ensure any contract change has a version bump + tests (schemas/contracts) and links in the relevant doc.
- Describe sensitivity and redaction behavior when outputs could expose restricted locations or PII.

---

## 🧠 Story Node & Focus Mode Integration

Architecture work is “done” only when it remains consumable by narrative and UI layers:
- **Story Nodes** are curated narrative artifacts with structured metadata and explicit provenance.
- **Focus Mode** must only surface provenance-linked content (no orphan facts), and any AI-generated elements must be clearly indicated.
- Predictive/uncertain outputs (if introduced) should carry confidence/uncertainty fields and be opt-in at the UI layer.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended for architecture docs)
- [ ] Markdown protocol check: front-matter present; required sections present; fence profile respected (outer backticks, inner tildes).
- [ ] Link checks for `docs/architecture/*` references.
- [ ] Secrets scan: no tokens/keys embedded.
- [ ] If this doc claims a contract change: the related schema/test/doc is updated and linked.

### Example placeholders — replace with repo-specific commands
~~~bash
# Markdown protocol validation (not confirmed in repo)
# python tools/validate_markdown_protocol.py docs/architecture/README.md

# Link check (not confirmed in repo)
# python tools/check_links.py docs/architecture

# Mermaid lint / render check (not confirmed in repo)
# python tools/validate_mermaid.py docs/architecture
~~~

---

## ⚖ FAIR+CARE & Governance

### Review triggers (architecture-level)
Governance review is required when an architecture change would:
- introduce a new sensitive or restricted dataset/layer,
- add new AI narrative behaviors (especially anything that could be mistaken for fact),
- add new external data sources,
- add or change public-facing endpoints.

### CARE / sovereignty considerations
- Assume culturally sensitive knowledge and restricted locations require extra care.
- If an architecture decision could expose precise locations through joins, interaction, or zoom: specify the generalization/redaction strategy and where it is enforced (data processing, API boundary, UI).

### AI usage constraints (for this document)
- Allowed transforms: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new governance policy; inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-27 | Initial `docs/architecture/` README scaffolding + doc index | AI-assisted draft |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (draft): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision (draft): `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Next stages blueprint (draft): `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
