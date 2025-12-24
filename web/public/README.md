---
title: "KFM Web Public Assets"
path: "web/public/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:public:readme:v1.0.1"
semantic_document_id: "kfm-web-public-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:public:readme:v1.0.1"
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

- `web/public/` contains **static, version-controlled assets** that are served verbatim to the browser by the Web UI toolchain.
- This README defines what is allowed in `web/public/`, and what must live elsewhere (datasets, catalogs, governed narratives), preserving:
  - the **canonical pipeline ordering**, and
  - the **API boundary rule** (UI consumes governed content via contracted APIs; no direct graph reads).

### Scope

| In Scope | Out of Scope |
|---|---|
| UI-only static assets (favicons, logos, UI icons, placeholder images, `robots.txt`, `site.webmanifest`, browser config files) | Any dataset outputs (`.geojson`, `.tif/.tiff`, `.parquet`, `.csv`, etc.), STAC/DCAT/PROV artifacts, or cached API responses |
| Styling/runtime assets needed by the UI (fonts, sprites, map UI chrome) **when they do not encode sensitive information** | Story Node markdown, Focus Mode narrative text, evidence bundles, citation data, or extracted dataset excerpts |
| Public legal/attribution text needed for the UI | Secrets/config files (`.env`, API keys), user uploads, generated build artifacts, or internal-only assets |

### Audience

- Primary: Frontend contributors working in `web/`
- Secondary: API/graph contributors (to keep governed data out of `public/`); governance reviewers

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*

Terms used here:
- **Public asset**: A file served **as-is** to the browser (no runtime governance/redaction applied).
- **API boundary**: The rule that the UI consumes graph + catalog data through `src/server/` endpoints, not by reading Neo4j directly.
- **Story Node**: A governed narrative artifact rendered in Focus Mode (canonical home: `docs/reports/story_nodes/`).
- **Evidence artifacts**: STAC/DCAT/PROV products that support traceability; these are not stored in `web/public/`.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical “ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode” ordering |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Defines UI/API boundary + Story Node placement rules |
| UI schemas (if present) | `schemas/ui/` | UI + Schemas | Layer registry + UI registry validation (not confirmed in repo) |
| Story Nodes directory | `docs/reports/story_nodes/` | Story maintainers | Governed narrative sources; not stored in `web/public/` |
| This README | `web/public/README.md` | UI maintainers | Directory contract for public assets |

### Definition of done (for this document)

- [ ] Front-matter complete and `path` matches `web/public/README.md`
- [ ] Scope table clearly separates static assets vs governed data artifacts
- [ ] Expected file tree reflects **actual** `web/public/` contents (keep synchronized)
- [ ] Any third-party asset added includes attribution + license note (see inventory table)
- [ ] Validation steps are listed and repeatable (commands may be placeholders if tooling is not confirmed in repo)
- [ ] Governance + CARE/sovereignty considerations are explicit for publicly served assets

## 🗂️ Directory Layout

### This document

- `path`: `web/public/README.md`

Update this README when you:
- add/remove public assets with user-visible impact (icons, logos, manifest, etc.)
- change how the UI references or loads static assets
- introduce new constraints for static content (e.g., assets moved out of `public/` due to sensitivity)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React/map client code + tooling/config |
| Frontend public assets | `web/public/` | Static assets served verbatim |
| API boundary | `src/server/` | Contracted endpoints for catalogs, graph queries, focus bundles; applies redaction/generalization |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog builders |
| Schemas | `schemas/` | JSON Schemas (including UI schemas if present) |
| STAC outputs | `data/stac/` | STAC collections + items |
| DCAT outputs | `data/catalog/dcat/` | DCAT 3 dataset records |
| PROV outputs | `data/prov/` | W3C PROV activities + entities |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative sources (versioned) |

### Expected file tree for this sub-area

The exact contents depend on the chosen frontend toolchain. Keep `web/public/` limited to static assets that are safe to expose publicly.

~~~text
📁 web/
├── 📁 public/
│   ├── 📄 README.md
│   ├── 📄 robots.txt                  # optional
│   ├── 📄 site.webmanifest            # optional
│   ├── 📄 browserconfig.xml           # optional
│   ├── 🖼️ favicon.ico                 # optional
│   ├── 🖼️ logo.svg                    # optional
│   ├── 📁 icons/                      # optional (UI icons)
│   │   └── 🖼️ kfm-marker.svg
│   ├── 📁 images/                     # optional (UI images)
│   │   └── 🖼️ placeholder.png
│   └── 📁 fonts/                      # optional (web fonts; license must permit redistribution)
│       └── 🔤 example.woff2
└── … (React app source, build config, etc.)
~~~

## 🧭 Context

### Background

`web/public/` is served “as-is” by the frontend host/dev-server. Because **no runtime redaction, provenance checks, or access controls** occur for these files, anything placed here is effectively **published content**.

### Assumptions

- The frontend toolchain treats `web/public/` (or an equivalent directory) as the static root for browser requests. *(If your toolchain differs, update this README to match reality.)*
- The UI references assets by stable, version-controlled paths.

### Constraints / invariants

- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The API boundary is mandatory: governed content is consumed via APIs, not via `web/public/`.
- Treat everything in `web/public/` as:
  - **public**, and
  - **non-redactable at request time**.

**Hard prohibitions for `web/public/`:**
- datasets and derived dataset extracts (including `.geojson`, `.parquet`, `.csv`, `.tif/.tiff`, `.fgb`, `.mbtiles`, `.pmtiles`)
- STAC/DCAT/PROV artifacts or bundles (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` outputs)
- cached API responses or “seed data” JSON intended to power the app
- Story Node narrative content or evidence/citation bundles
- any asset that reveals restricted/sensitive locations (explicit coordinates, protected site names, annotated maps that pinpoint sensitive sites)

**Allowed file types (typical examples):**
- Images: `.svg`, `.png`, `.jpg/.jpeg`, `.webp`, `.ico`
- Text/config: `.txt` (e.g., `robots.txt`), `.webmanifest` (PWA), `.xml` (browser config)
- Fonts: `.woff2` (preferred), `.woff` (if necessary) — *ensure redistribution is permitted*

### Decision guide: `web/public/` vs API-served content

| If the asset… | Then… | Why |
|---|---|---|
| Is purely UI chrome (logo/icon/placeholder) and safe to publish | Put it in `web/public/` | No governance needed at request time |
| Encodes data, evidence, or narrative (even “just an image derived from a dataset”) | Serve it via the API and treat it as an evidence asset | Enables provenance, access control, and redaction/generalization |
| Could enable triangulation of restricted knowledge | Do **not** publish via `public/` | Static assets bypass policy enforcement |

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Does our chosen frontend build tool treat `web/public/` as the final static root? | UI maintainers | TBD |
| Do we have CI checks blocking restricted file extensions and large binaries in `web/public/`? | Maintainers | TBD |

### Future extensions

- CI checks (if not already present) to prevent:
  - large binaries,
  - disallowed file types,
  - missing third-party attribution entries.
- A repo-wide “third-party notices” pattern (if adopted) to consolidate asset attribution.

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
| UI icons | SVG/PNG | UI maintainers | Prefer generic icons (avoid sensitive place names) |
| Static browser config | TXT/JSON/XML | UI maintainers | e.g., `robots.txt`, `site.webmanifest`, `browserconfig.xml` |
| Web fonts | WOFF2 | UI maintainers | Must include license + redistribution permission |

### Outputs

| Output | Sensitivity | Consumed by | Notes |
|---|---|---|---|
| Public static assets | public | Browsers | No governance/redaction applied at request time |

### Sensitivity and redaction

- Treat everything in `web/public/` as **public**.
- If an asset might encode restricted knowledge (annotated maps, site-specific diagrams, imagery that pinpoints sensitive places), do not place it here. Serve it via an API that can enforce policy.

### Quality signals

- Assets are optimized (lossless where needed) and named consistently (prefer deterministic, human-readable names).
- File sizes remain reasonable for web delivery.
- Third-party assets include attribution and license notes (inventory kept current).

## 🌐 STAC, DCAT & PROV Alignment

- `web/public/` does **not** store catalog artifacts.
- Catalog + provenance are produced and stored under:
  - `data/stac/`
  - `data/catalog/dcat/`
  - `data/prov/`
- If the UI needs dataset-derived imagery (rendered tiles, thumbnails, charts, annotated figures), treat it as an **evidence artifact**:
  - catalog it (STAC/DCAT as applicable),
  - link it via PROV lineage,
  - and deliver it through the API boundary so provenance and redaction rules are consistently enforced.

## 🧱 Architecture

### Components

| Component | Responsibility | Owner |
|---|---|---|
| `web/public/` | Serve static UI assets | UI maintainers |
| `web/` app | Render map UI + Focus Mode | UI maintainers |
| `src/server/` | Serve catalog + focus bundles (apply governance/redaction) | API maintainers |
| `src/graph/` + Neo4j | Store/query semantic graph + provenance refs | Graph maintainers |

### Interfaces / contracts

- Static assets: referenced by deterministic paths (e.g., `/logo.svg`) and served directly.
- Governed content: requested from API endpoints returning provenance-linked payloads (Story Nodes, focus bundles, layer registries).

### Extension points checklist

- [ ] Add a new icon/image → confirm it is public-safe and add attribution (if third-party)
- [ ] Reference the asset from UI code or layer registry (if applicable)
- [ ] If the asset is derived from datasets/evidence → do **not** place in `web/public/`; serve via API and catalog it instead
- [ ] Update this README’s file tree and “third-party assets inventory” table (below)

### Third-party assets inventory

> This table is the minimum audit surface for public static assets. If it grows large, consider moving it to a dedicated file and linking it here *(not confirmed in repo)*.

| Asset path | License | Source | Reviewed by | Notes |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

## 🧠 Story Node & Focus Mode Integration

- Story Nodes are governed narrative artifacts and should live under `docs/reports/story_nodes/` (not in `web/public/`).
- `web/public/` may include **presentation-only** resources for Story Node rendering (icons, UI chrome), but must not include narrative text, citations, or evidence bundles.
- Focus Mode must present provenance/evidence panels driven by API payloads, not static hard-coding.

## 🧪 Validation & CI/CD

### Directory validation checklist

- [ ] No restricted file types or dataset artifacts are committed into `web/public/`
- [ ] No secrets/config files are present (`.env`, API keys, private endpoints)
- [ ] Third-party assets inventory updated (if applicable)
- [ ] Links in this README resolve within the repo
- [ ] UI build/lint/test passes (see `web/` tooling docs)

### Reproduction

~~~text
# TBD: add repo-specific commands once the web toolchain is finalized.
# Example:
#   cd web
#   <install>
#   <lint>
#   <test>
#   <build>
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Static asset inventory | repo tree | `web/public/README.md` |
| UI build status | CI | `.github/workflows/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI maintainers review all additions to `web/public/`.
- Governance review required if an asset could relate to:
  - sensitive locations,
  - communities under sovereignty protections,
  - restricted material or culturally sensitive imagery.

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
| v1.0.1 | 2025-12-24 | Clarified prohibitions/allowed types; added API-vs-public decision guide; tightened provenance alignment language | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`