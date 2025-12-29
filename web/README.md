---
title: "Kansas Frontier Matrix — Web UI"
path: "web/README.md"
version: "v1.2.2"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:web:readme:v1.2.2"
semantic_document_id: "kfm-web-readme-v1.2.2"
event_source_id: "ledger:kfm:doc:web:readme:v1.2.2"
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

# Kansas Frontier Matrix — Web UI

`web/` is the canonical home for KFM’s user-facing **map + narrative application** (React + a map renderer such as MapLibre and/or Cesium; renderer choice is repo-specific).

**Canonical pipeline ordering is non-negotiable:**  
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

## ✅ UI invariants at a glance

- **API boundary is mandatory:** the UI consumes graph + catalog content **only** via contracted APIs and/or published catalog endpoints. The UI **must not** connect to Neo4j/graph storage directly.
- **Contract-first UI:** schema and API contracts are first-class artifacts; no “best-effort parsing” of registries or payloads.
- **No ad-hoc data in UI:** if a UI feature needs new data, extend **ETL/catalog/graph/API**—do not hard-code new datasets or scrape sources in the browser.
- **Audit affordances are required:** citations must be inspectable, copyable, and operable (keyboard + screen reader). No “trust me” narrative.
- **Provenance-first rendering:** every story paragraph, statistic, layer, or highlight must have a traceable evidence identifier (STAC/DCAT/PROV + graph IDs where applicable). Missing evidence ⇒ show a “missing provenance” state.
- **Layer registries are contract artifacts:** registries must validate against UI schema artifacts under `schemas/` (if present). No “best-effort” parsing.
- **Focus Mode is provenance-only:** Focus Mode consumes only provenance-linked context bundles. Any AI/predictive content must be opt-in, labeled, and carry uncertainty metadata; never infer sensitive locations.
- **Security + sovereignty:** treat markdown as untrusted input; sanitize; respect API redaction/generalization; never reconstruct restricted locations client-side.
- **Accessibility is a release gate:** keyboard-first + screen-reader compatible map interactions, Focus Mode, and citations.
- **Telemetry is governed if enabled:** never emit PII or precise sensitive coordinates; validate against telemetry schemas if present.

## 🔗 Quick links

Treat missing paths as **not confirmed in repo** and **do not create duplicates**.

- Master Guide v12 (canonical): `docs/MASTER_GUIDE_v12.md`
- Master Guide v13 (draft reference; may supersede v12): `docs/MASTER_GUIDE_v13.md` *(not confirmed in repo)*
- v13 redesign blueprint (draft reference): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo)*
- Next stages blueprint (draft reference): `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` *(not confirmed in repo)*
- Full architecture & vision (draft reference): `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` *(not confirmed in repo)*
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template v3: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- Schemas: `schemas/` (STAC/DCAT/PROV/story/ui/telemetry schemas; if present)
- Story Nodes: `docs/reports/story_nodes/` *(if present)*
- Markdown work protocol: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*
- Provenance rules: `docs/standards/KFM_PROVENANCE_RULES.md` *(not confirmed in repo)*

> **Repo reality check:** KFM follows “one canonical home per subsystem.” If a path referenced here does not exist in your checkout, treat it as **not confirmed in repo** and avoid creating duplicates. Fix the link, or open a ticket to align the repo to canonical homes.

---

## 📘 Overview

### Purpose

- Define what belongs in `web/` and how the Web UI participates in the canonical KFM pipeline.
- Make UI invariants explicit, reviewable, and testable (API boundary, provenance visibility, Focus Mode rules, layer registry schema validation).

### Scope

| In Scope | Out of Scope |
|---|---|
| Front-end application code under `web/` (map runtime, timelines, Story Node rendering, Focus Mode UI) | ETL / catalog generation (`src/pipelines/`) |
| UI layer registries + UI-side schema validation hooks | Graph build/migrations (`src/graph/`) |
| UI-side contract consumption (API clients, request/response typing, caching policy) | API contract definition/enforcement (`src/server/`) |
| UI testing, accessibility, performance budgets, telemetry hooks (if implemented) | Governance policy authoring (see `docs/governance/`) |

### Audience

- Primary: frontend engineers working in `web/`.
- Secondary: API engineers validating UI→API contracts; curators working on Story Nodes; reviewers for governance and accessibility.

### Definitions

- Glossary: `docs/glossary.md` *(expected; if missing, treat as not confirmed in repo)*

Key terms used in this doc:

- **Story Node** — governed narrative artifact, machine-ingestible, provenance-linked.
- **Focus Mode** — provenance-only deep-dive view; consumes only provenance-linked context bundles.
- **Layer registry** — schema-validated configuration describing map layers/sources/attribution/sensitivity.
- **Evidence artifacts** — STAC/DCAT/PROV products referenced by the UI for traceability and audit.
- **Context bundle** — contracted API payload for Focus Mode (narrative + citations + flags + map/timeline payload).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Required structure for Story Nodes |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Default governed doc structure |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | TBD | Use for REST/GraphQL contract changes |
| Schemas | `schemas/` | TBD | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) *(if present)* |

### Definition of done

- [ ] Front-matter complete and valid (`path` matches file location)
- [ ] Canonical pipeline and UI invariants are stated and testable
- [ ] All referenced paths are canonical or explicitly marked “not confirmed in repo”
- [ ] Validation steps listed and repeatable (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations stated (redaction, sensitivity, telemetry)
- [ ] No instructions imply prohibited AI actions (for example, inferring sensitive locations)

### What KFM is

KFM is an open-source geospatial + historical knowledge system (a “living atlas” of Kansas) that ingests heterogeneous sources, publishes governed metadata catalogs (STAC/DCAT/PROV), builds a semantically structured graph, and serves evidence through contracted APIs into a map + narrative UI. KFM is designed so that every narrative claim can be traced to versioned evidence, and every derived product has explicit lineage.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/README.md` (must match front-matter)

### Canonical subsystem homes

| Subsystem | Canonical home | Notes |
|---|---|---|
| Pipelines | `src/pipelines/` | ETL + catalog generation + validation |
| Graph build | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | Contracted access + redaction/generalization |
| UI | `web/` | This directory |
| Schemas | `schemas/` | JSON Schemas for contracts *(if present)* |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Published metadata artifacts |
| Data lifecycle | `data/raw/` + `data/work/` + `data/processed/` | Required staging |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts consumed by UI *(if present)* |
| MCP | `mcp/` | Runs, experiments, model cards, SOPs *(if present)* |

### Repo top-levels

Preferred roots (do not invent new roots without governance review):  
`.github/ · data/ · docs/ · mcp/ · schemas/ · src/ · tests/ · tools/ · web/ · releases/` *(some may be optional or absent)*

### Expected file tree

Update this tree to match repo reality, but keep “one canonical home per subsystem.”

~~~text
📁 web/
├── 📄 README.md
├── 📄 package.json                                  # if present
├── 📁 public/                                       # if present
├── 📁 src/                                          # if present
│   ├── 📁 api/                                      # API client + contract bindings
│   ├── 📁 app/                                      # routing + app shell (repo-specific)
│   ├── 📁 map/                                      # map runtime (MapLibre/Cesium/other)
│   ├── 📁 story/                                    # Story Node rendering + citations
│   ├── 📁 focus/                                    # Focus Mode panels + sync logic
│   ├── 📁 layers/                                   # registry loader/validators (code)
│   ├── 📁 ui/                                       # shared UI components
│   └── 📁 telemetry/                                # optional (schema-governed emitters)
└── 📁 layers/                                       # optional: layer registries (config); choose one canonical location
~~~

### Start here

Recommended reading order:

1) `docs/MASTER_GUIDE_v12.md` — canonical pipeline + invariants  
2) `docs/templates/TEMPLATE__STORY_NODE_V3.md` — Story Node structure consumed by UI  
3) `src/server/contracts/` — API contracts the UI must consume *(if present)*  
4) `schemas/` — UI + telemetry schemas *(if present)*  
5) `docs/reports/story_nodes/` — Story Nodes rendered in Focus Mode *(if present)*  
6) `docs/governance/` — redaction, sovereignty, ethics

### Quickstart

Commands and tooling are repo-specific. Prefer `web/package.json` scripts if present.

~~~bash
# Placeholders — replace with repo-approved tooling defined in web/package.json.

# cd web
# <install deps>         # e.g., npm ci / pnpm i / yarn
# <run dev server>       # e.g., npm run dev
# <run unit tests>       # e.g., npm test
# <run e2e tests>        # e.g., npm run e2e
# <validate registries>  # schema validation for layer registries (if wired)
~~~

---

## 🧭 Context

### Background

KFM’s Web UI is the presentation layer for evidence-backed mapping and narratives. It renders:

- map layers backed by cataloged evidence and governed sensitivity rules
- Story Nodes as machine-ingestible storytelling
- Focus Mode as a deep-dive view that packages narrative + citations + context (map + timeline) into one experience

### Assumptions

- Story content shown to users is curator-reviewed, provenance-linked, and versioned as repository artifacts and/or API-served equivalents.
- Redaction/generalization decisions are enforced at the API boundary and must be respected by the UI (no client-side reconstruction).
- Layer definitions are expressed as registries/config (not scattered hard-coded layer definitions).

### Constraints and invariants

- Preserve ordering: **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**
- No direct graph/Neo4j access from the browser; the UI is a contract consumer (APIs + catalogs).
- No ad-hoc data in UI: extend upstream, don’t hard-code.
- Focus Mode is provenance-only: missing evidence ⇒ explicit “missing provenance” state.
- Registry schemas are mandatory if present (`schemas/`).
- Markdown is untrusted input: sanitize before rendering; prevent script injection.
- Accessibility is a release gate (keyboard-first + screen-reader compatible citations).
- Telemetry is governed if enabled: no PII, no precise sensitive coordinates.

### Working mode

When in doubt, implement a vertical slice:

- dataset → catalogs (STAC/DCAT/PROV) → graph links → API contract → UI layer/view → one published Story Node

This avoids UI-only features that lack evidence, contracts, and governance review.

### Common UI change types

| Change | Usually requires | Notes |
|---|---|---|
| Add a new map layer | Layer registry entry + API endpoint/tiles + attribution | Validate registry schema; include sensitivity flags |
| Add a Focus Mode panel | API contract addition + UI component + accessibility checks | Must include evidence IDs + redaction notices |
| Add a new Story Node type | Story Node schema/template change + UI renderer update | Requires doc + schema review; likely governance review |
| Add AI-assisted feature | Opt-in controls + uncertainty metadata + governance review | Must not infer sensitive locations; label inference clearly |

### PR checklists

#### Add or change a map layer

- [ ] Upstream evidence exists and is referenced (STAC/DCAT/PROV IDs or resolvable links)
- [ ] API/catalog endpoint exists (or contract change included) and enforces redaction/generalization
- [ ] Layer registry updated with:
  - [ ] stable `layer_id` (no reuse for different meaning)
  - [ ] attribution + license surfaced in UI
  - [ ] sensitivity/classification flags set
- [ ] Layer registry validates against UI schema artifacts under `schemas/` *(if present)*
- [ ] UI interaction is keyboard accessible and screen-reader safe
- [ ] No client logs/telemetry include sensitive coordinates or PII
- [ ] Tests updated (unit + minimal end-to-end smoke)

#### Add or change a Focus Mode panel

- [ ] API contract provides a provenance-linked context bundle (IDs + flags)
- [ ] UI renders explicit missing-provenance and redaction states
- [ ] Any AI/predictive content is opt-in + labeled + has uncertainty metadata
- [ ] Citation UX is keyboard-first and copyable (IDs)
- [ ] Telemetry (if enabled) is schema-governed and does not emit PII

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which renderer is canonical (MapLibre, Cesium, or dual-mode)? | TBD | TBD |
| Where is the single canonical layer registry location (`web/layers/` vs `web/src/layers/`)? | TBD | TBD |
| Is telemetry enabled by default? If yes, which schema path governs it? | TBD | TBD |
| Are Story Nodes compiled into the UI build, fetched from API, or both? | TBD | TBD |

### Future extensions

- richer story formats (timeline-driven stories, comparative views), governed via template/schema review
- 3D views (Cesium) where appropriate, preserving provenance + redaction
- AI-assisted summaries in Focus Mode, strictly opt-in and labeled with uncertainty

---

## 🗺️ Diagrams

### System dataflow diagram

~~~mermaid
flowchart LR
  A["ETL — src/pipelines"] --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph (Neo4j)"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/ (React/Map)"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked only"]
~~~

### Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API Boundary
  participant Graph as Graph + Catalogs

  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch subgraph + evidence refs (STAC/DCAT/PROV IDs)
  Graph-->>API: context bundle + provenance identifiers
  API-->>UI: contracted payload (narrative + citations + flags)
~~~

---

## 📦 Data and Metadata

### Data lifecycle

Required staging:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/catalog/dcat/` + `data/prov/`)

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| API responses | JSON | `src/server/` endpoints | Contract tests + runtime guards |
| Catalog endpoints | JSON | STAC/DCAT/PROV outputs | Schema validation + link integrity |
| Layer registry | JSON/TS | `web/**/layers/**` | Validate against UI schema in `schemas/` *(if present)* |
| Story Nodes | Markdown | `docs/reports/story_nodes/**` | Story Node schema + lint *(if present)* |
| Evidence references | IDs/URLs | STAC/DCAT/PROV artifacts | Broken-link + ID integrity checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Web bundle | static build | repo-specific build output | CI build + accessibility gates |
| UI telemetry | JSON events | repo-specific | Telemetry schemas under `schemas/` *(if present)* |

### Sensitivity and redaction

- Treat API-delivered redaction/generalization as authoritative.
- Do not log PII or sensitive coordinates in client telemetry.
- Avoid persistent client storage of sensitive content unless governance-approved.

### Quality signals

- Layer registry schema validation must be deterministic and fail on errors.
- Citations must be keyboard operable and copyable; broken citations are treated as missing provenance.
- Focus Mode must refuse to render unsourced narrative.

---

## 🌐 STAC, DCAT and PROV Alignment

The UI must make provenance inspectable.

### STAC

- UI views should reference STAC Collection IDs and Item IDs when surfacing datasets and assets.
- Layer UX should surface attribution and license from STAC assets where applicable.

### DCAT

- UI should surface dataset-level metadata when relevant (title, publisher, license, description, keywords).

### PROV

- UI should expose lineage cues: source identifiers, run/activity identifiers, and (where allowed) agent/tool identities.
- If a view lacks evidence identifiers, it must present a missing-provenance state rather than implying certainty.

### Versioning

- When datasets or story artifacts have versions, the UI must surface the versioned identifier (not just a human label).

---

## 🧱 Architecture

### Major UI components

| Component | Responsibility | Interface |
|---|---|---|
| API client | Typed calls to API contracts | REST/GraphQL (repo-specific) |
| Map runtime | Render layers + interactions | Layer registry + API/catalog data |
| Story renderer | Render narrative + citations | Story Node v3 structure |
| Focus Mode | Provenance-first deep-dive UI | Context bundle payload |
| Registry loader | Load/validate layer configs | UI schema in `schemas/` *(if present)* |
| Telemetry | Emit governance-safe UX signals | Telemetry schema in `schemas/` *(if present)* |

### Subsystem contracts

| Subsystem | Contract artifacts | Do not break rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compatible or version bump |
| UI | layer registry + accessibility + audit affordances | no hidden data leakage |
| Story and Focus | provenance-linked context bundle | no hallucinated or unsourced claims |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/**/layers*.json` | Schema-validated |
| Story Nodes | `docs/reports/story_nodes/**` | Template/schema-governed |
| Telemetry | `schemas/**/telemetry*` | Schema + semver |

### Layer registries

Layer registries are contract artifacts. A registry typically:

- lists dataset layers, titles, descriptions, and styling rules
- is updated when new data is ingested and published
- is validated against a UI schema under `schemas/` (for example, `schemas/ui_layer_schema.json`, if present)

At minimum each registry entry must support:

- stable `layer_id` (never reuse IDs for different meaning)
- provenance pointers (STAC/DCAT/PROV identifiers or resolvable references)
- attribution + license surfaced in UI
- sensitivity/classification flags
- API/catalog source binding

### Citation rendering contract

Story Nodes are written in Markdown with citation markers. The UI must:

- render markdown safely (treat as untrusted input)
- custom-render citations so that evidence can be inspected
- provide an audit/provenance panel for Focus Mode

Recommended approach (implementation detail): parse markdown to HTML, then post-process citation markers into interactive elements (links/popovers/tooltips) that can open evidence details.

### Untrusted content and sanitization

Any markdown or remote content rendered in the UI must be treated as untrusted input:

- sanitize HTML/markdown rendering (no script injection)
- block unsafe links/embeds where required by governance
- do not enhance redacted data client-side (no join/zoom reconstruction)

### Contract boundaries

- UI never reads Neo4j directly; all access is via contracted APIs.
- API boundary is responsible for authorization + redaction/generalization decisions.
- UI is responsible for respecting policy flags (zoom gating, tooltip gating, hide/show).

---

## 🧠 Story Node and Focus Mode Integration

### Story Nodes as machine-ingestible storytelling

Story Nodes are governed Markdown artifacts consumed by the UI. Story Nodes must:

- link to graph entity IDs (Place, Person, Event, Document, Organization, Artifact)
- link to STAC/DCAT/PROV evidence identifiers
- separate fact vs inference vs hypothesis where applicable
- include citation anchors in a consistent, machine-resolvable format

### Focus Mode behavior expectations

Focus Mode should make it obvious:

- what entity/story is in focus (stable ID + canonical name)
- what evidence supports the view (copyable IDs + resolvable links)
- what is missing (explicit missing provenance state)
- what is redacted/generalized (clear notice + reason/category where allowed)

Focus Mode should also synchronize context:

- map focus to the relevant region
- timeline focus to the relevant period
- only relevant layers enabled by default

### Focus Mode rule

- Focus Mode consumes only provenance-linked content.
- Any predictive/AI-generated content must be opt-in, visibly labeled, and include uncertainty/confidence metadata.
- AI/predictive features must not infer or reveal sensitive locations.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD:layer_id"
focus_time: "TBD:YYYY or YYYY-MM-DD/YYYY-MM-DD"
focus_center: [-98.0000, 38.0000] # lon, lat (example only)
~~~

### Citation UX expectations

- Citations must be keyboard navigable and screen-reader compatible.
- Evidence identifiers must be copyable.
- Provide a consistent audit panel affordance for:
  - provenance links
  - sensitivity/redaction notices
  - missing provenance warnings

---

## 🧪 Validation and CI/CD

### CI behavior contract

- Validate if present: if a canonical root exists (or changes), validate its artifacts.
- Fail if invalid: schema errors, missing links, orphan references fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing the overall pipeline.

### Minimum validation steps

- [ ] Markdown protocol validation (front-matter + required sections)
- [ ] Link/reference checks (no orphan pointers)
- [ ] JSON schema validation (as applicable):
  - STAC/DCAT/PROV
  - Story Node schemas (if present)
  - Telemetry schemas (if present)
  - UI layer registry schemas (if present)
- [ ] API contract tests (OpenAPI/GraphQL schema + integration tests)
- [ ] UI unit tests + basic end-to-end smoke tests
- [ ] Accessibility checks (keyboard navigation, reduced motion, readable citations)
- [ ] Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Telemetry signals

If telemetry is enabled, recommended signals include:

- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

### Local reproduction

~~~bash
# Placeholders — replace with repo-specific commands defined in web/package.json (if present)

# 1) install deps
# 2) run lint
# 3) run unit tests
# 4) run e2e smoke tests
# 5) validate layer registry schema
~~~

---

## ⚖ FAIR+CARE and Governance

### Governance review triggers

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing or changing AI-generated narrative behavior visible to users
- Adding new external data sources surfaced in UI
- Adding new public-facing endpoints or share links
- Any classification/sensitivity change or publication derived from restricted inputs

### CARE and sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations (enforced at the API boundary).
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints

If the UI renders predictive/AI-generated content:

- it must be opt-in,
- must show uncertainty/confidence metadata,
- must not appear as unmarked fact,
- must not be used to infer sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial `web/README.md` | TBD |
| v1.1.0 | 2025-12-27 | Aligned to Universal governed-doc structure; tightened UI invariants; added CI expectations | TBD |
| v1.2.1 | 2025-12-28 | Re-structured for v13 “one canonical home”; clarified layer registry contract + Focus Mode context bundle expectations; added PR checklists | TBD |
| v1.2.2 | 2025-12-29 | Tightened contract-first UI language; aligned subsystem contracts and CI gates; clarified layer registry schema + citation rendering expectations | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`