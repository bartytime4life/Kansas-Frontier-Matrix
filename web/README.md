---
title: "KFM Web Frontend — README"
path: "web/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.0.0"
semantic_document_id: "kfm-web-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:readme:v1.0.0"
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

# KFM Web Frontend — README

## 📘 Overview

### Purpose
- This document describes the **KFM user-facing web frontend** under `web/`, including how it fits into KFM’s canonical pipeline, how it consumes data/contracts, and the governed expectations for **Map UI + Focus Mode** behavior.
- It is intended to be the first stop for developers adding UI features, layers, or Focus Mode integrations.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI structure, key concepts, local development workflow (repo-verified commands), layer registry usage, Focus Mode/Story Node integration expectations, and UI governance constraints | ETL implementation details, graph ontology changes, API contract design (use API contract template), STAC/DCAT/PROV generator internals, or Story Node authoring guidance beyond integration expectations |

### Audience
- Primary: Frontend engineers working in `web/`
- Secondary: Full-stack/API engineers, data/catalog engineers, QA/Accessibility reviewers, governance/security reviewers, editors maintaining Story Nodes

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Focus Mode**: A UI state that filters the system to a focused area/time/topic and shows an explainable, provenance-linked dashboard.
  - **Story Node**: Versioned narrative artifact (governed Markdown) with provenance-linked claims; used as building blocks in Focus Mode.
  - **Layer registry**: Declarative configuration describing available map layers, visibility defaults, sensitivity gating, and provenance pointers.
  - **STAC/DCAT/PROV**: Metadata/provenance standards used for cataloging and lineage.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Web frontend root | `web/` | Frontend | React/Map UI source + assets |
| Layer registry | `web/cesium/layers/regions.json` | Frontend + Governance | Declarative layers + sensitivity/provenance pointers |
| Design docs | `docs/design/` | Frontend/Design | UI architecture + UX contracts |
| Story Nodes | `docs/reports/.../story_nodes/` | Editorial/Historical | Versioned narratives referenced by Focus Mode |
| API layer | `src/server/` | API | Contracted access layer (REST/GraphQL); UI must not query graph directly |
| Catalogs | `data/stac/` + `docs/data/` | Data/Catalog | STAC/DCAT/PROV identifiers surfaced in UI |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Paths and “how to run” steps verified against the repo (e.g., `web/package.json` scripts) **before merge**
- [ ] Layer registry contract section matches current schema + validation rules
- [ ] Governance + CARE/sovereignty considerations explicitly stated (sensitivity/generalization)
- [ ] Validation steps listed and repeatable (CI-friendly)

## 🗂️ Directory Layout

### This document
- `path`: `web/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | Map UI, Focus Mode UX, a11y |
| Frontend design | `docs/design/` | UI architecture/decisions |
| Story Nodes | `docs/reports/.../story_nodes/` | Narrative artifacts with provenance |
| APIs | `src/server/` + docs | REST/GraphQL contracts + tests |
| Catalogs | `data/stac/` + `docs/data/` | STAC/DCAT/PROV catalogs + mappings |
| Schemas | `schemas/` | Validation for catalogs/UI contracts/telemetry |
| Tests | `tests/` | Integration/E2E/contract tests |

### `web/` (expected structure; verify against repo)
~~~text
📁 web/
├── 📄 README.md
├── 📁 cesium/
│   └── 📁 layers/
│       └── 📄 regions.json
├── 📁 src/                         # (verify in repo)
│   ├── 📁 components/              # (verify in repo)
│   ├── 📁 features/                # (verify in repo)
│   │   └── 📁 focus-mode/          # (verify in repo)
│   └── 📁 services/                # (verify in repo; API/STAC clients)
└── 📁 public/                      # (verify in repo; static assets)
~~~


## 🧭 Context

### Pipeline placement (non-negotiable)
KFM’s canonical ordering is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

The `web/` frontend sits at the **React/Map UI** stage and must consume the system through **contracted APIs + catalogs**, not by direct graph access.

### Security + sensitivity expectations
- **No unauthorized data leakage**: layer access and sensitive data must be governed (including default visibility and redaction/generalization rules).
- **Focus Mode provenance rule**: Focus Mode must not display content without provenance; unsourced narrative is forbidden.
- If sensitive locations exist, UI must render **generalized or blurred geometry** and surface governance flags/notice when constraints are applied.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL outputs] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j graph]
  C --> D[API layer (REST/GraphQL)]
  D --> E[web/ React + Map UI]
  F[Story Nodes (versioned markdown)] --> E
  E --> G[Focus Mode (provenance-linked narrative + dashboard)]
~~~

~~~mermaid
sequenceDiagram
  participant User
  participant Web as web/ UI
  participant API as API Layer
  participant Cat as STAC/DCAT/PROV
  User->>Web: Click feature / open Story Node / "Focus"
  Web->>API: Focus query (entity + params)
  API-->>Web: Context payload + provenance refs
  Web->>Cat: Resolve STAC/DCAT assets (by ID/links)
  Cat-->>Web: Item/asset metadata + links
  Web-->>User: Map/timeline updates + citations + optional AI explanations
~~~

## 📦 Data & Metadata

### Inputs the frontend consumes
| Input | Source | Sensitivity | Notes |
|---|---|---|---|
| Layer registry configuration | `web/cesium/layers/regions.json` | public/restricted | Governs layer availability + defaults + provenance pointers |
| Focus Mode context payload | API layer | public/restricted | Must include provenance references + governance flags |
| Story Node documents | `docs/reports/.../story_nodes/` | public/restricted | Markdown narratives with source-linked claims |
| STAC items/collections | `data/stac/` or STAC API | public/restricted | Used to resolve assets and show metadata/citations |
| Static map assets/tiles | infra + storage | public/restricted | Must respect access rules; avoid leaking restricted layers |

### Outputs the frontend produces
| Output | Where | Notes |
|---|---|---|
| Built static web bundle | deployment target | Static site build artifacts |
| UI events / telemetry (if enabled) | `docs/telemetry/` + `schemas/telemetry/` | Must be governed + avoid sensitive/PII leakage |
| User feedback (if supported) | pipeline intake | Should route via governed contribution workflow |

## 🌐 STAC, DCAT & PROV Alignment

- UI displays and links **STAC IDs** (items/collections) and their assets where appropriate.
- UI must be able to surface **provenance identifiers** (e.g., PROV activity/run IDs) for “how this was made” explanations.
- Story Nodes and Focus Mode must link every factual claim to a dataset/document/asset ID, consistent with FAIR+CARE expectations.

## 🧱 Architecture

### Frontend architecture summary
- `web/` is the user-facing mapping and narrative interface, implemented as a React UI with MapLibre/Cesium-based geospatial visualization.
- The frontend remains **behind contracts**:
  - **Graph access only via APIs**
  - **Dataset/asset discovery via STAC/DCAT/PROV catalogs**
  - **Layer availability via the declarative layer registry**

### Layer registry contract (minimum expectations; verify schema in repo)
The layer registry is a declarative list of map layers and must support:
- **Visibility defaults** (e.g., default enabled/disabled)
- **Zoom limits** (e.g., only visible above/below certain zoom)
- **Sensitivity/access gating** (e.g., public vs restricted layers)
- **Provenance pointers** (e.g., a STAC collection/item reference and/or provenance reference)

> Note: The definitive schema should live under `schemas/` (verify exact path and validator usage in repo).

### Local development (repo-verified commands required)
This section intentionally avoids hardcoding scripts that are not verified in this drafting context.

**Prereqs**
- Node.js (LTS recommended) + a package manager (npm/pnpm/yarn) — verify in repo.

**Common workflow (examples — replace with repo-specific commands)**
~~~bash
# from repo root
cd web

# install dependencies
# (verify package manager + lockfile in repo)
npm install

# start dev server (verify script name in package.json)
npm run dev

# production build (verify script name in package.json)
npm run build
~~~

**Config**
- If the UI needs an API base URL or catalog base URL, use the repo’s configured `.env*` files (verify exact variable names in repo).

## ✅ Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode is activated by user actions (e.g., focusing a story node or map entity).
- The UI must:
  - Recenter/lock map + time controls to the focused context
  - Filter panels (map, timelines, charts, narrative) to relevant content
  - Display citations linking back to source datasets/documents
  - Provide governance flags (e.g., sensitivity notices) and optionally an “AI explanation” toggle

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Any predictive or AI-based content must be explicitly labeled with uncertainty and be opt-in where required.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (for docs under governance)
- [ ] UI lint + typecheck (if applicable)
- [ ] UI build passes (dev + production build)
- [ ] UI schema checks (layer registry validation)
- [ ] Integration tests (API + UI interaction, where applicable)
- [ ] Security and sovereignty checks (as applicable)
- [ ] Accessibility checks (a11y baseline; keyboard nav; contrast; ARIA)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Frontend maintainers approve changes to `web/` implementation and UX.
- Governance/security review required when:
  - a new layer is introduced,
  - sensitivity/access rules change,
  - Focus Mode begins surfacing new categories of data,
  - telemetry changes might capture sensitive information.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Apply **generalization/redaction** for sensitive locations in both map rendering and Focus Mode narrative contexts.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not introduce UI behaviors that imply prohibited actions (e.g., inferring sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial `web/README.md` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`