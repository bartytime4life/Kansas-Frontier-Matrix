---
title: "KFM Web Public Assets"
path: "web/public/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:public:readme:v1.0.0"
semantic_document_id: "kfm-web-public-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:public:readme:v1.0.0"
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

# KFM Web Public Assets

## 📘 Overview

### Purpose
- `web/public/` contains **static, version-controlled assets** that are served verbatim to the browser by the web client.
- This README defines what is allowed in `web/public/` and what must live elsewhere (datasets, catalogs, governed narratives, etc.), preserving KFM’s pipeline ordering and API boundary.

### Scope
| In Scope | Out of Scope |
|---|---|
| UI-only static assets (favicons, logos, UI icons, placeholder images, `robots.txt`, `site.webmanifest`) | Any dataset outputs (`.geojson`, `.tif`, `.parquet`, etc.), STAC/DCAT/PROV catalogs, or cached API responses |
| Styling assets needed by the UI (e.g., fonts, sprites) **when they do not encode sensitive information** | Story Node markdown, Focus Mode narrative text, evidence bundles, or citation data |
| Public legal/attribution text needed by the UI | Secrets/config files (`.env`, API keys), user uploads, or generated build artifacts |

### Audience
- Primary: Frontend contributors working in `web/`
- Secondary: API/graph contributors who expose catalog + focus bundles to the UI; governance reviewers

### Definitions
- Glossary: `docs/glossary.md`
- Terms used here:
  - **Public asset**: A file served as-is to the browser (no runtime governance/redaction applied).
  - **API boundary**: The rule that UI consumes graph + catalog data through `src/server/` endpoints, not by reading Neo4j directly.
  - **Story Node**: A governed narrative artifact rendered in Focus Mode (stored under `docs/reports/story_nodes/` per the v13 blueprint).

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical “ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode” ordering |
| v13 redesign blueprint | `docs/architecture/` (blueprint reference) | Architecture | Defines UI/API boundary + Story Node placement |
| UI schemas | `schemas/ui/` | UI maintainers | Validates layer registries and UI configuration |
| Story nodes directory | `docs/reports/story_nodes/` | Story maintainers | Governed narrative sources; not stored in `web/public/` |
| This README | `web/public/README.md` | UI maintainers | Directory contract |

### Definition of done
- [ ] Front-matter complete and `path` matches `web/public/README.md`
- [ ] Scope table clearly separates static assets vs governed data artifacts
- [ ] File tree reflects the actual contents of `web/public/`
- [ ] Any third-party asset added includes attribution + license note
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations are explicit for public assets

## 🗂️ Directory Layout

### This document
- `path`: `web/public/README.md`
- Update when:
  - Adding/removing any public asset with user-visible impact (icons, logos, manifest, etc.)
  - Changing how the UI references/loads static assets
  - Introducing new governance constraints for static content (e.g., redaction rules that require moving assets out of `public/`)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map client code |
| Frontend public assets | `web/public/` | Static assets served verbatim |
| API layer | `src/server/` | Contracted endpoints for catalogs, graph queries, focus bundles |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas (including UI schemas) |
| STAC outputs | `data/stac/` | STAC collections + items |
| DCAT outputs | `data/catalog/dcat/` | DCAT 3 dataset records |
| PROV outputs | `data/prov/` | W3C PROV activities + entities |
| Story nodes | `docs/reports/story_nodes/` | Narrative sources (versioned) |

### Expected file tree for this sub-area
The exact contents depend on the chosen frontend build tooling. Keep `web/public/` limited to static assets that are safe to expose publicly.

~~~text
📁 web/
├── 📁 public/
│   ├── 📄 README.md
│   ├── 📄 robots.txt            # optional
│   ├── 📄 site.webmanifest      # optional
│   ├── 🖼️ favicon.ico           # optional
│   ├── 🖼️ logo.svg              # optional
│   ├── 📁 icons/                # optional (UI icons)
│   │   └── 🖼️ kfm-marker.svg
│   └── 📁 images/               # optional (UI images)
│       └── 🖼️ placeholder.png
└── … (React app source, build config, etc.)
~~~

## 🧭 Context

### Background
`web/public/` is served “as-is” by the frontend host/dev-server. Because no runtime redaction or provenance checks occur for these files, anything placed here is effectively **published content**.

### Assumptions
- The frontend toolchain treats `web/public/` as the static root for browser requests.
- The UI references assets by stable, version-controlled paths (avoid runtime-generated filenames when possible).

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes governed data only via the API layer (no direct graph access).
- `web/public/` must not contain:
  - raw/processed datasets
  - STAC/DCAT/PROV JSON outputs
  - cached API responses
  - sensitive location details (explicit coordinates, site names under restriction, etc.)
- Any UI element that communicates “evidence” or “provenance” should be driven by API payloads (IDs, citations, run logs), not hard-coded in static files.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Does our chosen frontend build tool treat `web/public/` as the final static root? | UI maintainers | TBD |

### Future extensions
- Add a lightweight inventory table below for tracking third-party assets, licenses, and review sign-off.
- Add CI checks (if not already present) to prevent large binaries or restricted file types from landing in `web/public/`.

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

### Sequence diagram
~~~mermaid
sequenceDiagram
  participant Browser
  participant Static as web/public (static)
  participant API as src/server (API)
  participant Graph as Neo4j

  Browser->>Static: GET /logo.svg (static asset)
  Browser->>API: GET /v1/focus/{entity_id}
  API->>Graph: Query (apply governance/redaction + attach provenance)
  Graph-->>API: Context bundle + provenance refs
  API-->>Browser: Narrative + citations + evidence panel data
~~~

## 📦 Data & Metadata

### Inputs
| Input | Typical format | Source | Notes |
|---|---|---|---|
| UI brand assets | SVG/PNG/ICO | Design system / UI maintainers | Must be safe for public release |
| UI icons | SVG/PNG | UI maintainers | Prefer generic icons (no sensitive place names) |
| Static config for browser | TXT/JSON | UI maintainers | e.g., `robots.txt`, `site.webmanifest` |

### Outputs
| Output | Sensitivity | Consumed by | Notes |
|---|---|---|---|
| Public static assets | public | Browsers | No governance/redaction applied at request time |

### Sensitivity and redaction
- Treat everything in `web/public/` as **public**.
- If an asset might encode restricted knowledge (e.g., an annotated map image, a site-specific diagram, or anything tied to sensitive locations), it must not be stored here. Serve it via an API that can enforce policy.

### Quality signals
- File sizes remain reasonable for web delivery.
- Assets are optimized (lossless where needed) and named consistently.
- Any third-party asset includes attribution and license notes.

## 🌐 STAC, DCAT & PROV Alignment
- `web/public/` does **not** store catalog artifacts.
- Catalog + provenance are produced and stored under:
  - `data/stac/`
  - `data/catalog/dcat/`
  - `data/prov/`
- The UI accesses catalogs and provenance through API endpoints so governance can be applied consistently.

## 🧱 Architecture

### Components
| Component | Responsibility | Owner |
|---|---|---|
| `web/public/` | Host static UI assets | UI maintainers |
| `web/` app | Render map UI + Focus Mode | UI maintainers |
| `src/server/` | Serve catalog + focus bundles (apply governance/redaction) | API maintainers |
| `src/graph/` + Neo4j | Store/query semantic graph + provenance refs | Graph maintainers |

### Interfaces / contracts
- Static assets: referenced by deterministic paths (e.g., `/logo.svg`) and served directly.
- Governed data: requested from API endpoints that return provenance-linked payloads (Story Nodes, focus bundles, layer registries).

### Extension points checklist
- [ ] Add a new icon/image → ensure it is public-safe and add attribution (if third-party)
- [ ] Reference the asset from UI code or layer registry (if applicable)
- [ ] If the asset represents dataset-derived output → do **not** place in `web/public/`; serve via API instead
- [ ] Update this README’s file tree and “third-party assets” inventory (below)

### Third-party assets inventory
| Asset path | License | Source | Reviewed by | Notes |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## 🧠 Story Node & Focus Mode Integration
- Story Nodes are governed narrative artifacts and should live under `docs/reports/story_nodes/` (not in `web/public/`).
- `web/public/` may include **presentation-only** resources for Story Nodes (icons, UI chrome), but must not include narrative text, evidence bundles, or dataset extracts.
- Focus Mode must present provenance/evidence panels driven by API payloads, not static hard-coding.

## 🧪 Validation & CI/CD
- [ ] No restricted file types or dataset artifacts are committed into `web/public/`
- [ ] No secrets/config files are present
- [ ] Third-party assets inventory updated (if applicable)
- [ ] Links in this README resolve within the repo
- [ ] UI build/lint/test passes (see `web/` tooling docs)

### Reproduction
~~~text
# TBD: add repo-specific commands once the web toolchain is finalized
# Example:
#   cd web
#   <install>
#   <test>
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Static asset inventory | repo tree | `web/public/README.md` |
| UI build status | CI | `.github/workflows/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI maintainers review all additions to `web/public/`.
- Governance review required if an asset could relate to sensitive locations, communities, or restricted material.

### CARE / sovereignty considerations
- Do not publish assets that could reveal culturally sensitive or restricted site information.
- Prefer serving such content through governed APIs that can generalize or redact as required.

### AI usage constraints
- Allowed: summarize/structure/translate/index this README.
- Prohibited: generating new governance policy or inferring sensitive locations from asset content.

## 🕰️ Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/public/` README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
