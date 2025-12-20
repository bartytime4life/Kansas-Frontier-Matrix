---
title: "🧭 KFM — Patterns (Governed Index)"
path: "docs/patterns/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-20"
status: "active"
doc_kind: "Index"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:patterns:index:v12.0.0-draft"
semantic_document_id: "kfm-patterns-index-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:patterns:index:v12.0.0-draft"
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

# 🧭 KFM — Patterns (Governed Index)

## 📘 Overview

### Purpose
This document is the **governed index** for reusable KFM patterns. Patterns exist to:
- Reduce architectural drift (shared invariants + repeatable implementation guidance).
- Standardize reliability + governance outcomes (idempotency, lineage, sensitivity handling).
- Keep implementations architecture‑synced with the canonical KFM flow.

### Scope

| In Scope | Out of Scope |
|---|---|
| Cross‑cutting patterns used across the KFM pipeline (ETL, catalogs, graph load, API contracts, UI/Story behaviors) | Domain-specific dataset documentation (belongs under `docs/data/` + `data/<domain>/`) |
| Patterns that define invariants, reference designs, and validation expectations | Shipping production code “by doc”; patterns guide work but do not bypass review |
| Indexing + navigation for pattern documentation | UI-side polling hacks or frontend direct access to graph/object store |

### Audience
- Primary: Data‑Ops, Platform, Pipeline Maintainers
- Secondary: Governance reviewers, Curators, Story/UX maintainers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Pattern**: A reusable, governed approach to a recurring KFM problem (with invariants + validation).
  - **Invariant**: A non‑negotiable rule (e.g., canonical pipeline ordering; API boundary).
  - **Contract**: Schema or interface requirement (e.g., event payload schema; API schema; catalog profile).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Patterns index (this doc) | `docs/patterns/README.md` | Data‑Ops / Platform | Single entry point |
| Change Detection pattern | `docs/patterns/change-detection/README.md` | Reliability / Data‑Ops | Push-first + minimal polling |
| Idempotent Handler pattern | `docs/patterns/change-detection/idempotent-handler/README.md` | Reliability / Data‑Ops | Exactly‑once effects under at‑least‑once triggers |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Governance | Use for patterns unless Story/API templates apply |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Every listed pattern has a working relative link
- [ ] Canonical pipeline + API boundary stated and preserved
- [ ] Mermaid diagrams render (no `|` inside node labels; prefer `/` or line breaks)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document
- `path`: `docs/patterns/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Patterns | `docs/patterns/` | Reusable architectural + pipeline patterns |
| Pipelines | `src/pipelines/` | ETL + catalog builders + loaders |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Data catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV outputs |
| Graph | `src/graph/` | Ontology bindings + loaders/migrations |
| API | `src/api/` (or `src/server/`) | API boundary (UI never reads Neo4j directly) |
| Frontend | `web/` | React + map client(s) |

### Expected file tree for this sub-area
~~~text
docs/
└── patterns/
    ├── README.md
    └── change-detection/
        ├── README.md
        └── idempotent-handler/
            └── README.md
~~~

---

## 🧭 Context

### Background
KFM spans ingestion, catalogs, graph semantics, APIs, and narrative UX. Without patterns:
- teams re-solve the same problems inconsistently,
- reliability practices diverge (retries, idempotency, replay),
- provenance becomes noisy or incomplete,
- UI/Story Nodes can accidentally drift into “freshness without evidence.”

Patterns provide a governed way to keep implementations consistent and auditable.

### Assumptions
- Pattern docs are **docs-first** and must stay compatible with the canonical KFM pipeline.
- If a pattern implies an API change, it must be described using the **API Contract Extension** template (not here).
- If a pattern is a narrative unit, it must use **Story Node v3** (not here).

### Constraints / invariants
- Canonical ordering is preserved:
  - ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode
- Frontend consumes contracts via APIs (no direct graph dependency).
- Patterns must not introduce “governance bypass” behaviors.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we want an automated link-check + mermaid lint gate for `docs/patterns/**`? | Platform | TBD |
| Should each pattern have a “Reference implementation location” field (code pointers)? | Data‑Ops | TBD |

### Future extensions
- Add a lightweight “pattern registry” file (generated index) if the pattern set grows.
- Add CI checks for mermaid parse errors and broken intra-doc links.
- Add a minimal “pattern maturity model” (draft → active → deprecated) if needed.

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC, DCAT, PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React, Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

---

## 📚 Current governed patterns

| Pattern | Location | Pipeline stages | Notes |
|---|---|---|---|
| 🔔 Change Detection with Minimal Polling | `./change-detection/README.md` | ETL, Catalog | Push-first (webhooks/SSE) + conditional GET fallback |
| ✅ Idempotent Handler | `./change-detection/idempotent-handler/README.md` | ETL, Catalog | Exactly-once effects; WAL/ledger; deterministic rollback |

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Pattern documents | Markdown | `docs/patterns/**` | Markdown lint, link-check, mermaid render check |
| Schemas referenced by patterns | JSON Schema | `schemas/**` | Schema validation + versioning rules |
| Pipeline invariants | Markdown | `docs/MASTER_GUIDE_v12.md` | Consistency check during reviews |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Navigable pattern registry (this index) | Markdown | `docs/patterns/README.md` | Template compliance + link integrity |
| Reusable implementation guidance | Markdown + snippets | pattern subfolders | Must not contradict governed contracts |

### Sensitivity & redaction
- Pattern docs should be written assuming **public visibility**, unless explicitly marked otherwise.
- Do not embed secrets, tokens, or internal hostnames. Use placeholders and reference secret management docs.

### Quality signals
- Links resolve and do not create circular/ambiguous navigation.
- Diagrams render without parser errors (avoid `|` in node labels).
- Examples are deterministic and clearly scoped (pseudo-code labeled; contracts explicit).

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Patterns that affect data artifacts must specify:
  - Which Collections/Items change
  - Which extensions/properties are required (e.g., checksums, lineage markers)
  - Versioning behavior (links to predecessor/successor where applicable)

### DCAT
- Patterns that change publication/distribution behavior must specify:
  - dataset identifiers impacted
  - distribution versioning + checksum requirements
  - license mapping expectations

### PROV-O
- Patterns that change pipeline behavior must specify minimal lineage:
  - `prov:Entity` inputs/outputs
  - `prov:Activity` run identity
  - `prov:Agent` pipeline identity
  - link strategy for provenance artifacts from APIs/UI

### Versioning
- Prefer additive changes (new fields) over breaking ones.
- Breaking changes require:
  - schema version bump
  - contract tests
  - migration plan (where applicable)

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Patterns (docs) | Govern reusable approaches | Markdown + diagrams |
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validators |
| Graph | Neo4j | Cypher via API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs references |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/api/` + docs | Contract tests required |
| Catalog profiles | `docs/data/` + `data/stac/` | Schema-validated |
| Pattern docs | `docs/patterns/` | Template compliance + review |

### Extension points checklist (for future work)
- [ ] Pattern doc added under `docs/patterns/<pattern>/README.md`
- [ ] Linked from this index
- [ ] Diagram(s) render and avoid parser edge-cases
- [ ] Validation/CI expectations documented
- [ ] Security + sovereignty notes included (or explicitly “not applicable”)

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Patterns must state (where relevant):
- What “freshness” or “change” claims are allowed, and what evidence must accompany them.
- Whether any AI-generated summaries are permitted, and how they are labeled + linked to provenance.

### Provenance-linked narrative rule
- Every claim shown in Story Nodes / Focus Mode must trace to a dataset / record / asset ID.
- UI only receives provenance references via APIs (no direct graph reads).

### Optional structured controls
~~~yaml
pattern_index:
  surface_in_ui: true
  requires_api_contract: false
  requires_story_node_template: false
~~~

---

## 🧪 Validation & CI/CD

- [ ] Markdown lint (style, headings, front-matter keys)
- [ ] Link integrity check (relative links resolve)
- [ ] Mermaid render check (no parse errors)
- [ ] “Invariant check” review: canonical pipeline ordering preserved; API boundary preserved
- [ ] Sensitive content scan: no secrets/PII/internal-only endpoints

---

## ⚖ FAIR+CARE & Governance

- Patterns are **governance artifacts**: they guide implementations and reviews.
- No pattern may be used to justify bypassing review, licensing constraints, or sovereignty protections.
- If a pattern affects access, redaction, or exposure risk, it must be reviewed against:
  - `governance_ref`
  - `ethics_ref`
  - `sovereignty_policy`

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v12.0.0-draft | 2025-12-20 | Added governed patterns index and navigation; aligned to v12 Universal Doc template | <name/handle> |

---

<div align="center">

**Navigation**  
[⬅️ Docs Root](../README.md) ·
[📂 Patterns](./README.md)

© 2025 Kansas Frontier Matrix — CC‑BY‑4.0

</div>

