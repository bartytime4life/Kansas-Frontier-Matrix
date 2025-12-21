---
title: "KFM Server (API Boundary) — src/server"
path: "src/server/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:src:server:readme:v1.0.0"
semantic_document_id: "kfm-src-server-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:server:readme:v1.0.0"
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

# KFM Server (API Boundary) — `src/server/`

## 📘 Overview

### Purpose
- Establish `src/server/` as the **single canonical home** for KFM’s API boundary.
- Define what belongs here (contracts, redaction, query services) and what does not (direct UI → graph access).

### Scope

| In Scope | Out of Scope |
|---|---|
| Creating `src/server/` canonical root + scaffolding | Choosing a runtime/framework (not confirmed in repo) |
| Reserving `src/server/contracts/` for OpenAPI/GraphQL artifacts | Implementing specific endpoints (tracked separately) |
| Stating invariants: contract-first + provenance + redaction | Cloud deployment specifics |

### Audience
- Primary: API developers, graph/query service developers, governance reviewers
- Secondary: UI developers integrating against API contracts; data engineers producing evidence IDs consumed by the API

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **API boundary**: Governed, contracted server layer between Graph and clients.
  - **Contract artifact**: Machine-validated schema/spec (OpenAPI, GraphQL SDL, JSON Schema) relied on by clients.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical home for APIs = `src/server/` |
| API Contract Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | KFM Core | Use for endpoint/contract changes |
| API contracts (future) | `src/server/contracts/` | API maintainers | OpenAPI/GraphQL + contract tests |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory `src/server/` exists in repo (via this README)
- [ ] Invariants are explicit (no direct UI → graph; contracts live here)
- [ ] `src/server/contracts/` reserved for contract artifacts

## 🗂️ Directory Layout

### This document
- `path`: `src/server/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| API boundary | `src/server/` | Contracts, redaction, query services |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 server/
    ├── 📄 README.md
    └── 📁 contracts/                 # reserved for OpenAPI/GraphQL/JSON Schema contracts
        └── 📄 .gitkeep               # placeholder until first contract lands
~~~

## 🧭 Context

### Background
- KFM v13 calls for exactly **one** canonical home for the API layer: `src/server/`.
- This root is where API contracts and API-facing redaction logic become first-class artifacts.

### Assumptions
- Server runtime/framework choice is **not confirmed in repo**.
- The server integrates with the graph through controlled query services (clients never query Neo4j directly).

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- Frontend consumes contracts via APIs (no direct graph dependency).
- Redaction / sovereignty controls are enforced at the API boundary and logged.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which server runtime/framework is canonical (FastAPI, Express, etc.)? | TBD | TBD |
| REST only, GraphQL only, or hybrid? | TBD | TBD |
| Where do contract tests live and how are they enforced in CI? | TBD | TBD |

### Future extensions
- Add first contract artifact under `src/server/contracts/` (OpenAPI YAML/JSON and/or GraphQL SDL).
- Add contract tests in `tests/` that validate schema + backwards compatibility.
- Implement the first vertical-slice endpoint(s) needed by UI + Focus Mode.

## 🗺️ Diagrams

### System / dataflow diagram
```mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D["API Boundary<br/>src/server"]
  D --> E["React/Map UI<br/>web/"]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

sequenceDiagram
  participant UI
  participant API as "API Boundary - src/server"
  participant Graph

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle (entities + evidence IDs)
  API-->>UI: contracted payload + citations + audit flags


## 📦 Data & Metadata

### What the API layer must preserve
- **Provenance hooks**: responses include IDs that trace back to STAC/DCAT/PROV evidence.
- **Sensitivity controls**: omit/generalize restricted locations + sensitive attributes per governance policy.
- **Determinism**: stable contracted responses for the same versioned inputs.

### Minimal contract expectation
- Contract artifacts live under `src/server/contracts/` and are validated in CI (schema lint + resolver tests).

## 🌐 STAC, DCAT & PROV Alignment

### Response linkage expectations
- STAC: reference Collection/Item IDs for geospatial assets.
- DCAT: reference dataset identifiers.
- PROV: reference activity/run IDs for returned evidence.

## 🧱 Architecture

### Responsibilities of `src/server/`
- Serve contracted APIs for:
  - map layer queries
  - entity / event search
  - Focus Mode context bundles
  - Story Node retrieval (published only, validated)
- Enforce:
  - authZ/authN (as applicable)
  - redaction/generalization rules
  - provenance completeness and audit flags

### Non-responsibilities
- UI rendering logic (lives in `web/`)
- Direct writes to raw domain data (lives in ETL/pipelines)
- Direct client access to Neo4j

## 🧩 Extension points checklist (for future work)
- [ ] APIs: contract version bump + tests
- [ ] Graph: new labels/relations mapped + migration plan (if endpoints need new shapes)
- [ ] Catalogs: ensure STAC/DCAT/PROV IDs are included in responses where applicable
- [ ] UI: layer registry entry + access rules (when new endpoints land)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- The API provides a **context bundle** for a focus entity/story:
  - related entities
  - evidence references (STAC/DCAT/PROV IDs)
  - audit flags / sensitivity notices

### Provenance-linked narrative rule
- Any narrative content exposed by the API must include evidence references (or be withheld from Focus Mode).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation checklist
- [ ] Markdown protocol checks (for this README)
- [ ] API contract tests (once contracts exist)
- [ ] Schema validation (STAC/DCAT/PROV references in responses)
- [ ] Security and sovereignty checks (as applicable)

## ⚖ FAIR+CARE & Governance

### Review gates
- This scaffolding: maintainers review.
- Any endpoint exposing potentially sensitive location/person data: requires governance + sovereignty review.

### CARE / sovereignty considerations
- Do not expose culturally sensitive locations or restricted knowledge.
- Apply redaction/generalization at the API boundary; log redaction actions for auditability.

### AI usage constraints
- Do not generate policy from this document.
- Do not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initialize `src/server/` canonical root + README scaffold | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`


# FILE: src/server/contracts/.gitkeep
# Intentionally present to keep `src/server/contracts/` in git until the first contract artifact lands.
