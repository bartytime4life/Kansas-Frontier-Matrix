---
title: "src/kfm — KFM Core Package README"
path: "src/kfm/README.md"
version: "v0.1.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:src:kfm:readme:v0.1.0"
semantic_document_id: "kfm-src-kfm-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:src:kfm:readme:v0.1.0"
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

# src/kfm

## 📘 Overview

### Purpose
`src/kfm/` is reserved for **core, shared KFM code** used across subsystems (pipelines, graph, API, UI, agents, etc.).  
It is intended to reduce duplication by centralizing cross-cutting primitives like IDs, config loading, provenance helpers, validation utilities, and shared types.

> Note: Concrete module contents may be **not confirmed in repo** until implemented. This README defines the **intended responsibilities and boundaries** for this package.

### Scope

| In Scope | Out of Scope |
|---|---|
| Shared primitives (IDs/keys, common types, config parsing/validation, provenance helpers) | ETL domain logic for a specific dataset (belongs in `src/pipelines/`) |
| Cross-cutting governance helpers (redaction/generalization utilities, audit payload helpers) | Neo4j direct access from UI (UI consumes API contracts only) |
| Reusable utilities that support deterministic pipelines | Derived datasets (must live under `data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| Shared error types + logging conventions | One-off scripts (prefer `tools/` or `src/pipelines/` as appropriate) |

### Audience
- Primary: KFM developers (pipeline, graph, API, UI)
- Secondary: contributors extending new domains and features

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: STAC, DCAT, PROV, provenance, redaction, Focus Mode

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Source of truth for ordering + boundaries |
| Pipeline code | `src/pipelines/` | Data engineering | ETL + catalog generation + graph build steps |
| Graph code | `src/graph/` | Graph engineering | Ontology bindings, migrations, constraints |
| API layer | `src/api/` and/or `src/server/` | Backend | Serves contracts; UI never reads graph directly |
| UI | `web/` | Frontend | Map + narrative rendering |
| Story Nodes | `docs/reports/.../story_nodes/` | Editorial | Provenance-linked narrative artifacts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Responsibilities and boundaries are clearly stated
- [ ] “Not confirmed in repo” areas are labeled
- [ ] Links to canonical docs and adjacent subsystems are present

## 🗂️ Directory Layout

### This document
- `path`: `src/kfm/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Core shared package | `src/kfm/` | Shared primitives + cross-cutting helpers |
| Pipelines | `src/pipelines/` | ETL + catalogs + graph build steps |
| Graph | `src/graph/` | Neo4j modeling + ontology bindings |
| APIs | `src/api/` and/or `src/server/` | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` | React/Map UI + Focus Mode UX |
| Data products | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Docs | `docs/` | Canonical governed documentation |

### Expected file tree for this sub-area
> This is the **recommended** structure. Update to match actual contents as the package evolves (**not confirmed in repo**).

~~~text
📁 src/
└── 📁 kfm/
    ├── 📄 README.md
    ├── 📁 config/            # shared config parsing + validation (not confirmed in repo)
    ├── 📁 ids/               # stable ID/key helpers (not confirmed in repo)
    ├── 📁 provenance/        # PROV/STAC/DCAT linkage helpers (not confirmed in repo)
    ├── 📁 security/          # redaction/generalization helpers (not confirmed in repo)
    ├── 📁 types/             # shared typed models (not confirmed in repo)
    └── 📁 utils/             # small shared utilities (not confirmed in repo)
~~~

## 🧭 Context

### Background
KFM is a geospatial + historical knowledge system that moves from governed ingestion to cataloged assets, to a graph, and then out through contracted APIs into a map + narrative UI. This package exists to keep shared, cross-cutting logic consistent across those layers.

### Assumptions
- The system pipeline ordering is preserved:
  **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.
- Frontend consumes data via the API layer (no direct Neo4j dependency).
- Deterministic + reproducible transforms are preferred for data processing.

### Constraints / invariants
- **API boundary:** UI never reads Neo4j directly; contracts live at the API layer.
- **Data placement:** derived artifacts and datasets must not be written into `src/`; they belong under `data/`.
- **Provenance-first:** if a helper emits narrative or evidence, it must carry provenance pointers (STAC/DCAT/PROV IDs).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What language/runtime is the primary implementation for `src/kfm/` (Python/TS/other)? | TBD | TBD |
| Where are canonical shared types defined today (if any)? | TBD | TBD |
| Do we enforce stable ID conventions via schemas/tests? | TBD | TBD |

### Future extensions
- Shared provenance utilities that standardize how STAC/DCAT/PROV references are attached to API responses.
- Shared redaction utilities to prevent sensitive location leakage in public outputs.

## 🗺️ Diagrams

### System / dataflow diagram (context for this package)
~~~mermaid
flowchart LR
  subgraph Pipeline["Canonical KFM pipeline (context)"]
    A["ETL"] --> B["STAC/DCAT/PROV Catalogs"]
    B --> C["Neo4j Graph"]
    C --> D["APIs"]
    D --> E["React/Map UI"]
    E --> F["Story Nodes"]
    F --> G["Focus Mode"]
  end

  subgraph K["src/kfm (shared)"]
    K1["IDs + shared types"]
    K2["Config + validation"]
    K3["Provenance + redaction helpers"]
    K1 --> K2 --> K3
  end

  K --> A
  K --> C
  K --> D
  K --> E
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Shared config | YAML/JSON | repo config paths | schema validation (TBD) |
| Shared schemas | JSON Schema | `schemas/` | schema lint |
| Provenance refs | IDs/URIs | catalogs + graph | referential integrity checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Shared types/helpers | code | `src/kfm/` | unit tests + lint |
| Provenance bundles (helpers) | JSON-LD / JSON | emitted by callers | PROV/STAC/DCAT profiles |

### Sensitivity & redaction
- Any helper that formats user-facing location output must respect:
  - sovereignty policy (`docs/governance/SOVEREIGNTY.md`)
  - “no inferred sensitive locations” rule
  - API-layer enforcement of redaction rules

### Quality signals
- Deterministic behavior (same input → same output)
- Stable IDs/keys
- Schema-valid payloads for catalogs/contracts (where applicable)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- This package may host shared helpers for linking domain outputs to:
  - STAC Collection IDs and Item IDs
  - Asset pointers for evidence artifacts (if applicable)

### DCAT
- This package may host mapping helpers for dataset-level metadata (DCAT 3) when assembling catalog views.

### PROV-O
- This package may host helpers for:
  - `prov:wasDerivedFrom` source IDs
  - `prov:wasGeneratedBy` activity/run IDs
  - stable Agent/Activity identity conventions (TBD)

### Versioning
- Prefer explicit versioning for shared contracts and shared types:
  - SemVer for this package boundary (TBD)
  - clear changelogs when shared interfaces change (TBD)

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| `src/kfm` | shared primitives + cross-cutting helpers | import/use by other modules |
| `src/pipelines` | ETL + catalog generation | configs + run logs |
| `src/graph` | graph build + constraints | API-mediated access |
| API layer | contracted access | REST/GraphQL |
| UI | consumes contracts | API calls |

### Interfaces / contracts
- Any code in `src/kfm` that shapes API responses must obey:
  - schema-first contracts (OpenAPI/GraphQL) (**not confirmed in repo**)
  - redaction requirements for sensitive content
  - provenance references in payloads that power Focus Mode

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Shared helpers can standardize:
  - how evidence pointers are attached to narratives
  - how citations are rendered from provenance IDs
  - how “AI explanation” or uncertainty metadata is represented (if applicable)

### Provenance-linked narrative rule
- Every narrative claim must trace to a dataset / record / asset ID (enforced at Story Node + Focus Mode layers).

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] Lint/typecheck for `src/kfm` language (not confirmed in repo)
- [ ] Unit tests for ID generation + redaction utilities (if present)
- [ ] Contract tests for any shared API payload helpers (if present)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) lint
# 2) unit tests
# 3) doc lint
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to redaction/generalization helpers: **requires human review**
- Changes that affect public output schemas: **requires contract review**
- Changes that touch sovereignty policy enforcement: **requires governance review**

### CARE / sovereignty considerations
- Do not add functionality that infers or exposes sensitive locations.
- Ensure generalized outputs remain useful without violating protection rules.

### AI usage constraints
- This doc inherits template constraints:
  - allowed: summarize/structure_extract/keyword_index
  - prohibited: generate_policy, infer_sensitive_locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-19 | Initial README scaffold for `src/kfm` | TBD |
---
Footer refs:
- Master pipeline + invariants: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
