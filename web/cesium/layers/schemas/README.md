---
title: "Cesium Layer Schemas — README"
path: "web/cesium/layers/schemas/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:layers:schemas:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-layers-schemas-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:layers:schemas:readme:v1.0.0"
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

# Cesium Layer Schemas

## 📘 Overview

### Purpose
- Define what belongs in `web/cesium/layers/schemas/` and how it is used.
- Provide a governed, reviewable place for **schema definitions** that validate **Cesium layer configuration** in the KFM web UI.
- Ensure layer configuration is **stable**, **lintable**, and safe to ship (no secrets / no direct graph dependencies).

### Scope
| In Scope | Out of Scope |
|---|---|
| Schemas used by the frontend to validate Cesium layer configuration (layer registry entries / layer specs) | Backend API contracts (use API contract docs + server schemas) |
| Documentation of conventions for adding/updating schemas | STAC/DCAT/PROV schema definitions (owned under `schemas/` + catalog tooling) |
| Guardrails that prevent unsafe config (e.g., secrets, direct DB endpoints) | Any UI logic that reads Neo4j directly (must go via API) |

### Audience
- Primary: Frontend engineers working on Cesium layers and the layer registry.
- Secondary: API engineers exposing layer metadata; data/catalog engineers publishing assets (e.g., CZML, 3D Tiles).

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Layer registry**: the UI-managed list of available map layers (validated and shipped with the web app).
  - **Layer spec**: a declarative configuration object describing how a Cesium layer is created.
  - **Schema**: a machine-checkable contract for a layer spec’s structure (often JSON Schema).
  - **CZML / 3D Tiles**: common Cesium data formats for temporal simulation and streamed 3D content (see system design references).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/layers/schemas/README.md` | Frontend | You are here |
| Cesium layer schemas | `web/cesium/layers/schemas/` | Frontend | Add schema files here (filenames TBD by implementation) |
| Layer registry (schema consumer) | `web/cesium/layers/` | Frontend | Registry location/filename is repo-specific; keep schema validation close to the registry |
| Global schemas | `schemas/` | Platform | Repository-wide JSON schemas (telemetry, shared contracts, etc.) |
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | Platform | Canonical ordering + API/UI boundary |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are explicit
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Schema/versioning conventions noted (and marked TBD where repo truth must be confirmed)

## 🗂 Directory Layout

### This document
- `path`: `web/cesium/layers/schemas/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Web UI | `web/` | React/Map UI (client-side) |
| Cesium integration | `web/cesium/` | Cesium-specific glue code, adapters, layer composition |
| Layer registry | `web/cesium/layers/` | Layer definitions/config used to build the UI map experience |
| Schemas (this folder) | `web/cesium/layers/schemas/` | Validation schemas for layer specs / registry entries |
| Server/API | `src/server/` + `docs/` | API layer (contracts and implementation) |
| STAC/DCAT/PROV outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog and lineage artifacts |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 layers/
        └── 📁 schemas/
            └── 📄 README.md
~~~

## 🧭 Context

### Background
- Cesium integration is commonly used to support **3D terrain/imagery streaming** and **temporal simulations**, often via formats such as **CZML** and **3D Tiles**.
- KFM’s architecture requires that the UI remains an API consumer (no direct graph access), and that changes remain consistent with the canonical pipeline ordering.

### Assumptions
- Layer configuration exists as declarative objects (JSON and/or TypeScript) that can be validated against schemas.
- The repository intends to run (or will add) **UI schema checks** as part of CI for the layer registry.

### Constraints / invariants
- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Neo4j graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumes data/contracts via **APIs** (no direct Neo4j dependency).
- Schemas must not encourage embedding secrets (API keys, signed URLs) into committed configs.
- If a layer references sensitive content (places, sites, culturally restricted content), governance rules apply (generalize/redact as appropriate upstream).

### Open questions
| Question | Why it matters | Where to confirm |
|---|---|---|
| What schema standard/draft is used (JSON Schema draft version, Zod, etc.)? | Tooling + CI validation compatibility | Existing frontend/tooling config |
| What is the layer registry filename/location? | Schemas should align with the registry | `web/cesium/layers/` |
| How are remote assets referenced (direct URLs vs STAC IDs vs API routes)? | Contract boundary + caching + security | API contract docs + UI layer loader |

### Future extensions
- Add one schema per layer type (e.g., imagery, terrain, 3D tiles, CZML/time-dynamic).
- Generate TypeScript types from schemas (or generate schemas from types) once the repo’s approach is confirmed.

## 🗺 Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[Web UI]
  S[Layer Schemas] -->|validate layer registry / specs| E
  E --> V[Cesium Viewer]
  E --> N[Story Nodes]
  N --> F[Focus Mode]
~~~

### Optional sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant VAL as Schema Validator
  participant API as API Layer
  participant CES as Cesium

  UI->>VAL: Validate layer spec / registry entry
  VAL-->>UI: ok | errors

  UI->>API: Request layer asset metadata (if needed)
  API-->>UI: Contracted payload (refs + provenance)
  UI->>CES: Instantiate Cesium layer(s)
  CES-->>UI: Layer ready
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Source | Validation |
|---|---|---|---|
| Layer spec / registry entry | JSON / TS object | `web/cesium/layers/` | Schemas in `web/cesium/layers/schemas/` |
| Asset references | URLs / IDs | API responses / config | Must not include secrets; prefer stable IDs |
| Optional provenance references | IDs/links | API payloads / story nodes | Must map to catalog/record IDs when used |

### Outputs
| Output | Format | Consumer | Notes |
|---|---|---|---|
| Validated layer registry | In-memory objects | Web UI | Blocks runtime errors + supports consistent UX |
| Cesium layer instances | Runtime objects | Cesium viewer | Created only after validation |

### Sensitivity & redaction
- Do not commit keys, tokens, signed URLs, or private endpoints into layer config.
- If layers can point to sensitive locations or restricted content, ensure:
  - access control and redaction happen upstream (API/data), and
  - the UI configuration does not leak restricted details.

### Quality signals
- Schema validation is deterministic and runs in CI.
- Schema changes include:
  - example layer specs (if repo uses examples),
  - regression tests for validation, and
  - clear migration notes for breaking changes.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If a layer references a dataset asset that is cataloged in STAC, prefer referencing **stable STAC IDs** (Item/Collection) instead of hardcoding ad-hoc URLs.
- Where applicable, map layer configuration fields to STAC assets in `data/stac/`.

### DCAT
- If the UI surfaces “dataset” metadata alongside layers, align identifiers with DCAT dataset identifiers in `data/catalog/dcat/` when available.

### PROV-O
- Prefer that provenance shown in the UI comes from API payloads (which can be backed by PROV outputs in `data/prov/`), not embedded directly in the UI config.

### Versioning
- Treat schema changes as versioned contracts:
  - Backward-compatible changes: minor/patch.
  - Breaking changes: major + clear migration notes (and update any registry entries accordingly).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Cesium layer registry | Declarative layer availability | Validated config |
| Cesium layer schemas (this dir) | Validate layer specs | Schema tooling |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas (global) | `schemas/` | Semver + changelog |
| API schemas/contracts | `src/server/` + `docs/` | Contract tests required |
| Layer registry schema | `web/cesium/layers/schemas/` | Schema-validated + reviewed |

### Extension points checklist (for future work)
- [ ] UI: new layer type added to registry + schema updated
- [ ] APIs: layer metadata endpoints documented/contracted (if applicable)
- [ ] Catalogs: STAC/DCAT references wired through API payloads
- [ ] Focus Mode: provenance references enforced when layers inform narrative

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Layer selection can influence what becomes “focusable” (places/events/documents).
- If layers support narrative, the UI should be able to show evidence/provenance for layer-driven claims.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (preferably via API payloads referencing catalogs).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI schema checks (validate layer registry against schemas in this directory)
- [ ] Contract boundary check: UI uses API payloads (no direct graph access)
- [ ] Security checks: no secrets or private endpoints committed in configs
- [ ] Sovereignty checks (as applicable): sensitive layers reviewed

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate layer schemas (and registry entries)
# 2) run unit/integration tests
# 3) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| layer_schema_validation_failures | Web UI | `docs/telemetry/` + `schemas/telemetry/` |
| layer_load_errors | Web UI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Frontend review required for any schema changes.
- Security review required if schemas introduce new kinds of remote references (e.g., new endpoint classes).
- Governance review required if layers depict culturally sensitive or restricted sites.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules for layers that can reveal sensitive locations.
- Prefer generalization/redaction upstream (data/API) so UI config remains safe to publish.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not use AI transforms to infer sensitive locations or generate new governance policy text.

## 🕰 Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for Cesium layer schema directory | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
