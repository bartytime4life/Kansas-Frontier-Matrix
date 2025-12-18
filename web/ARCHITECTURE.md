---
title: "KFM Web Frontend Architecture"
path: "web/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Architecture"
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

doc_uuid: "urn:kfm:doc:web:architecture:v1.0.0"
semantic_document_id: "kfm-web-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:web:architecture:v1.0.0"
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

# KFM Web Frontend Architecture

## 📘 Overview

### Purpose
- Define the architecture, module boundaries, and contracts for the `web/` frontend.
- Encode *non-negotiable* pipeline constraints as they apply to the UI: **UI consumes contracts via APIs** and **Focus Mode forbids unsourced narrative**.

### Scope
| In Scope | Out of Scope |
|---|---|
| Runtime architecture of the web UI (map + narrative + Focus Mode) | ETL implementation details |
| How the UI consumes STAC/DCAT/PROV artifacts and API responses | Neo4j ontology internals and migrations |
| Layer registry governance pattern (declarative layers + provenance hooks) | Full UI visual design system (colors/fonts/etc.) |
| Frontend CI/CD expectations (lint/tests/build) | API contract change documentation (use API template for that) |

### Audience
- Primary: Frontend contributors, UI maintainers, platform integrators
- Secondary: API/graph maintainers, data pipeline maintainers, governance/security reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Focus Mode**: topic-centric UI context that filters map/time/panels and enforces provenance
  - **Story Nodes**: curated narrative artifacts linked to graph entities + datasets
  - **Layer Registry**: declarative layer configuration (visibility, sources, provenance, sensitivity rules)
  - **Provenance-linked content**: UI content that can trace back to dataset / record / asset IDs
  - **CARE / sovereignty**: protection and governance rules affecting what can be shown and at what precision

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This architecture doc | `web/ARCHITECTURE.md` | Web maintainers | Architecture + invariants |
| Web readme | `web/README.md` | Web maintainers | Setup/run/dev workflow |
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Pipeline order + extension matrix |
| Design guidance | `docs/design/` | UX + web maintainers | Focus Mode UX, a11y (verify actual paths) |
| API contracts | `src/server/` + docs | API maintainers | REST/GraphQL contracts; contract tests |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Platform maintainers | Observability + governance signals |
| Layer registry (example) | `web/cesium/layers/regions.json` | Web maintainers | Verify actual path; must be schema-validated |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Diagrams reflect the current contract boundary (**UI → APIs**, not UI → graph)

## 🗂️ Directory Layout

### This document
- `path`: `web/ARCHITECTURE.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React app + map clients + Focus Mode UI |
| Data domains | `data/` | Raw/work/processed/stac outputs per domain |
| Catalogs | `data/stac/` + `docs/data/` | STAC/DCAT/PROV outputs + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, relations, migrations |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Schemas | `schemas/` | JSON schemas; telemetry schemas |
| Story Nodes | `docs/reports/.../story_nodes/` + graph | Versioned narratives w/ provenance |
| Security | `.github/SECURITY.md` + `docs/security/` | Policy + technical standards |

### Expected file tree for this sub-area
> Note: This is a **reference layout**. If the repo uses different tooling or paths, update this section to match the actual `web/` tree.

~~~text
web/
├─ 📄 README.md
├─ 📄 ARCHITECTURE.md
├─ 📄 package.json                         (not confirmed in repo)
├─ 📄 tsconfig.json                         (not confirmed in repo)
├─ 📄 index.html                            (not confirmed in repo)
├─ 📁 public/                               (not confirmed in repo)
│  └─ 🖼️ assets/                            (not confirmed in repo)
├─ 📁 src/                                  (not confirmed in repo)
│  ├─ 📁 app/                               (routing + app shell)
│  ├─ 📁 api/                               (API clients + DTOs)
│  ├─ 📁 map/                               (MapLibre + map adapters)
│  ├─ 📁 focus-mode/                        (Focus Mode state + panels)
│  ├─ 📁 story-nodes/                       (Story Node reader/viewer)
│  ├─ 📁 components/                        (shared UI components)
│  ├─ 📁 styles/                            (css/tokens)
│  └─ 📁 utils/                             (helpers)
├─ 📁 cesium/                               (optional; if Cesium 3D is enabled)
│  ├─ 📁 layers/
│  │  ├─ 📄 regions.json                    (layer registry; verify path)
│  │  └─ 📄 *.schema.json                   (recommended; not confirmed in repo)
│  └─ 📁 adapters/                          (Cesium → shared map interface)
└─ 📁 tests/                                (not confirmed in repo)
   ├─ 📁 unit/
   └─ 📁 e2e/
~~~

## 🧭 Context

### Background
- The web UI is designed to be **fast and broadly accessible**, primarily by loading **static pipeline outputs** in-browser.
- When the user needs dynamic graph-style queries (e.g., “related events within radius”), the UI uses a **lightweight API** rather than directly coupling to the graph.
- The UI stack is expected to be modern web tech (e.g., **React + MapLibre**), with modular components such as Map View, Timeline Slider, Layer Legend, Search Bar, etc.
- The UI should be deployable as a static site (e.g., GitHub Pages), with optional API services behind it.

### Assumptions
- Static artifacts (STAC catalogs, tiles/geojson, media) are served over HTTP(S) and cacheable by the browser.
- The UI can load a **pre-built search index** (JSON or similar) for client-side search when appropriate.
- Focus Mode context bundles returned from APIs include provenance references sufficient to cite sources and enforce redaction.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Focus Mode must enforce: **no content appears without a source** (provenance-linked only).
- Sensitive location handling must follow sovereignty policy and governance flags (precision reduction, blur/generalize, gated visibility).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical build tool + scripts (`npm`, `pnpm`, etc.)? | TBD | TBD |
| What is the canonical layer registry schema location (and versioning rule)? | TBD | TBD |
| Is Cesium required or optional for v1 web UI? | TBD | TBD |
| What telemetry schema(s) are required for Focus Mode governance audits? | TBD | TBD |

### Future extensions
- Offline-first search index + cached STAC subsets for low-connectivity use
- More Focus Mode panels (evidence panel, uncertainty panel, provenance graph viewer)
- Additional map engines (3D, vector tiles) behind a shared adapter interface
- Layer registry-driven feature flags (gated layers, sensitivity classes)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Static data assets<br/>GeoJSON, tiles, media]
  B --> D[Neo4j Graph]
  D --> E[APIs<br/>REST/GraphQL]
  C --> F[Web UI<br/>React + MapLibre (+ optional Cesium)]
  E --> F
  F --> G[Story Nodes Viewer]
  F --> H[Focus Mode UI]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI
  participant API
  participant Graph as Graph/Index

  User->>UI: Activate Focus Mode (entity/map/time)
  UI->>API: Focus query(entity_id, viewport, time_range, flags)
  API->>Graph: Fetch subgraph + provenance refs + sensitivity flags
  Graph-->>API: Context bundle (entities, evidence, citations, flags)
  API-->>UI: Focus payload (narrative blocks + citations + audit flags)
  UI-->>User: Recenter/lock map + update panels + show citations/audit
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC catalogs/collections/items | JSON | `data/stac/` and/or hosted endpoint | STAC validators + schema profiles |
| DCAT dataset records | JSON / JSON-LD | Generated alongside STAC | DCAT profile validation |
| PROV provenance records | JSON-LD | Generated in pipeline | PROV profile validation |
| Layer registry | JSON | `web/.../layers/*.json` | Schema-validated in CI |
| Search index (optional) | JSON | Pipeline output | Schema + size/perf budget |
| Focus Mode context bundle | JSON | API response | Contract tests + runtime guards |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map layers | runtime | browser memory | governed by layer registry |
| Focus state | runtime + URL | URL/query state | share-link contract (if present) |
| UI telemetry events (optional) | JSON events | `docs/telemetry/` + pipeline logs | `schemas/telemetry/` |
| Screenshots/snapshots (optional) | image/url | user-shared | must not leak sensitive precision |

### Sensitivity & redaction
- Do not display precise coordinates for sensitive sites when policy indicates generalization is required.
- Prefer server-provided *sensitivity flags* and *generalized geometries*; the UI must enforce “belt and suspenders” (server + client).
- Ensure sensitive layers are **off by default** and/or **zoom-limited** via the layer registry.

### Quality signals
- Surface data confidence/quality indicators where available (e.g., “confidence”, “coverage”, “last updated”).
- Highlight “missing provenance” as an error state in Focus Mode panels (content should not render without citations).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: (populate with your KFM collections)
- Items involved: (populate as needed)
- Extension(s): e.g., Versioning Extension (if enabled)

UI expectations:
- Treat STAC `bbox`/`geometry` and `datetime` (or temporal extents) as the authoritative bounds for map/time filtering.
- Prefer direct use of STAC links/assets instead of hardcoding URLs.

### DCAT
- Dataset identifiers: (populate)
- License mapping: read from DCAT and display in dataset/about panels
- Contact / publisher mapping: display where available

### PROV-O
- `prov:wasDerivedFrom`: show “source lineage” links from UI
- `prov:wasGeneratedBy`: show pipeline run/process identifiers
- Activity / Agent identities: display minimally for transparency + audit

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.
- UI should allow “pin to version” behavior for reproducibility when versioning is present.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| App shell | Routing + layout + shared state boundaries | UI routes + state store |
| Map adapter | Encapsulate MapLibre (+ optional Cesium) | `MapAdapter` API (internal) |
| Layer registry loader | Declarative layers, governance flags, provenance pointers | JSON schema + runtime guardrails |
| Static data loader | Load STAC + assets + search index | HTTP fetch + caching |
| API client | Contracted API calls for focus/search/graph queries | REST/GraphQL client modules |
| Story Nodes viewer | Render curated narratives + links to map/time | Story node schema + citations |
| Focus Mode UI | Topic-centric dashboard; enforce provenance + redaction | Focus payload schema + audit flags |
| Evidence/citation panel | Inline citations + link-out to datasets | provenance IDs + STAC/DCAT links |
| Audit panel (optional) | Show governance flags/redaction and “why” | sensitivity flags + policy refs |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| UI component contracts | `web/src/...` | Semver at module boundary; keep stable public props |
| Layer registry | `web/cesium/layers/regions.json` (verify) | Schema-validated; breaking changes require version bump |
| Focus Mode payload | API docs + client DTOs | Contract tests required; backward compatible by default |
| Story Node format | `docs/reports/.../story_nodes/` | Versioned artifacts; no silent rewrites |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode is activated from:
  - a map feature (click → “Focus”),
  - a story node (“Focus”),
  - or an advanced query result.
- Expected UX behaviors:
  - Map recenters and “locks” to the area of interest and time range.
  - Panels update to only show relevant narrative, evidence, and visualizations.
  - Citations are always present inline; clicking citations reveals source metadata.
  - If AI-generated insights are displayed, they must be labeled and optionally expandable via an “AI explanation” toggle.
  - Governance flags (e.g., redaction/generalization) are surfaced in an audit panel.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- If provenance is missing, Focus Mode must not render the claim (show an explicit error/omission state instead).

### Optional structured controls
~~~yaml
focus_layers:
  - "base:boundaries"
  - "events:floods"
focus_time: "1951-01-01/1951-12-31"
focus_center: [ -98.0000, 38.0000 ]
focus_zoom: 8
show_ai_explanations: false
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI lint + typecheck (tooling not confirmed in repo)
- [ ] Unit tests for map adapters + data loaders (tooling not confirmed in repo)
- [ ] Build step produces deterministic artifacts
- [ ] Layer registry schema validation
- [ ] Contract tests against Focus Mode payload schema (API-side) + client DTO alignment
- [ ] Security and sovereignty checks (sensitivity/generalization gates)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) install deps
# (npm|pnpm|yarn) install

# 2) lint + typecheck
# (npm|pnpm|yarn) run lint
# (npm|pnpm|yarn) run typecheck

# 3) unit tests
# (npm|pnpm|yarn) test

# 4) build
# (npm|pnpm|yarn) run build

# 5) validate layer registry schemas (if separate)
# (npm|pnpm|yarn) run validate:layers
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| `ui.focus_mode.activated` | UI | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.layer.toggled` | UI | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.citation.opened` | UI | `docs/telemetry/` + `schemas/telemetry/` |
| `ui.redaction.applied` | UI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes?
  - Web maintainers approve UI-only refactors.
  - Any changes affecting sensitivity handling, provenance rules, or layer gating require governance/security review (see refs below).
- What requires council/board sign-off?
  - Policy changes and sovereignty enforcement changes (TBD per governance docs).

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Ensure sensitive locations are generalized/blurred per `docs/governance/SOVEREIGNTY.md`.
- Ensure Focus Mode does not create “derived sensitive” outputs by combining non-sensitive layers into sensitive inference.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- AI assistance must not infer sensitive locations or fabricate provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial web frontend architecture doc | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`