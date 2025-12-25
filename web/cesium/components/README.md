---
title: "KFM UI — Cesium Components README"
path: "web/cesium/components/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:components-readme:v1.0.1"
semantic_document_id: "kfm-web-cesium-components-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:cesium:components-readme:v1.0.1"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:<calculated-in-ci>"
---

# web/cesium/components — README

> **Purpose (required):** Define the **contract-driven** and **provenance-safe** conventions for Cesium-based UI components in KFM.
> This README governs `web/cesium/components/` behavior and boundaries. It **does not** define new backend endpoints or governance policy.

## 📘 Overview

### Purpose

This README governs **frontend conventions** for Cesium-based UI components in KFM, with special emphasis on:

- maintaining the **API boundary** (UI consumes API and catalog endpoints; UI does not query Neo4j directly)
- maintaining **provenance visibility** in Focus Mode and map interactions
- keeping Cesium usage compatible with the broader map UI architecture (e.g., **2D/3D switching** without losing state)
- validating **UI registries/config** against schema where available (e.g., `schemas/ui/` for layer registries)

### Scope

| In Scope | Out of Scope |
|---|---|
| Cesium component responsibilities, boundaries, patterns, lifecycle | Backend ETL, STAC/DCAT/PROV generation, graph modeling |
| Focus Mode map behaviors that Cesium components must support | Authoring Story Nodes themselves (see story node template) |
| UI safety rules: provenance display, opt-in predictive content behaviors | Defining/changing API endpoints/contracts (use API Contract Extension template) |

### Audience

- Primary: Frontend engineers working in `web/` on map UI and Cesium integration
- Secondary: API engineers verifying UI contract expectations, reviewers checking governance/a11y

### Definitions

- Glossary (if present): `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: Cesium, Viewer, Scene, DataSource, Entity, Layer, Focus Mode, Provenance, STAC, DCAT, PROV

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering + “do not break” rules |
| v13 redesign blueprint (contract-first paths) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Canonical roots + minimum CI gates (draft) |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Structure + CI expectations |
| Story node template (Focus hints) | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | `focus_center`, `focus_time`, `focus_layers` support |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API owners | Use when changing endpoints/contracts |
| UI layer registry schema (minimum contract set) | `schemas/ui/` | Maintainers | Expected to validate UI registries (if present) |

### Definition of done

- [ ] Front-matter complete + valid (path matches, version + last_updated updated)
- [ ] No repo-claims beyond what is verified (unknowns marked “not confirmed in repo”)
- [ ] Constraints/invariants listed and consistent with pipeline ordering and UI boundary
- [ ] Focus Mode + provenance rules are explicit (no unsourced narrative)
- [ ] Validation steps listed (doc checks + UI lifecycle checks + schema checks)
- [ ] Security/ethics considerations included (no sensitive leakage; no secret/tokens in repo)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/components/README.md`

### Related repository paths (canonical by stage)

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/` | Raw/work/processed outputs; published catalogs |
| STAC outputs | `data/stac/` | Collections + Items (catalog stage output) |
| DCAT outputs | `data/catalog/dcat/` | Dataset discovery metadata |
| PROV outputs | `data/prov/` | Lineage bundles used by audits + Focus Mode |
| Graph | `src/graph/` | Ontology bindings + ingest logic (UI never reads directly) |
| API boundary | `src/server/` | Contracted endpoints + redaction rules (no UI direct-to-graph reads) |
| UI | `web/` | React map clients (2D/3D), Focus Mode, citation rendering |
| UI layer registries | `web/**/layers/**` | Layer registry JSON/config consumed at runtime (exact location not confirmed) |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/storynodes/ui/telemetry) |
| Releases | `releases/` | Versioned bundles, manifests, SBOMs, telemetry snapshots (if used) |
| MCP | `mcp/` | Experiments, run logs, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 components/
        └── 📄 README.md
~~~

## 🧭 Context

### Background

KFM’s frontend is a map + narrative UI that can render geospatial content in **2D** and/or **3D**.
Cesium components exist to support 3D use cases (terrain, globe, time-dynamic visualization) while
preserving the same governance constraints used across the app.

### Assumptions

- Cesium usage is encapsulated in components that can be mounted/unmounted cleanly without memory leaks.
- Data shown in Cesium is sourced through the same **API boundary** and catalog endpoints used by the rest of the UI.
- If a 2D/3D toggle exists (e.g., MapLibre ↔ Cesium), it preserves user state (selected entity, active layers, focus context) across modes.

### Constraints / invariants

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

UI-specific invariants:

- **UI reads only from API endpoints and catalog endpoints.**
- **No UI direct-to-graph reads** (no Neo4j driver usage; no Cypher from UI).
- **Layer registries/config are schema-validated** when schemas are present (e.g., `schemas/ui/`).
- **Focus Mode is a view over provenance-linked context only.**
- Predictive/AI-generated content:
  - is opt-in,
  - includes uncertainty metadata,
  - never appears as unmarked fact.
- Sensitivity protections are enforced at boundaries:
  - geometry generalization/redaction where required,
  - API-level redaction,
  - Story Node review gates.
  Cesium components must **honor sensitivity flags** and must not “reconstruct” restricted precision client-side.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which specific folder(s) under `web/**/layers/**` are authoritative for 3D/Cesium layers? (not confirmed in repo) | UI | TBD |
| What is the chosen state management approach (Redux vs Context/Reducers)? (not confirmed in repo) | UI | TBD |
| Is Cesium Ion / terrain streaming used, and how are tokens configured? (not confirmed in repo) | UI/Security | TBD |
| Do we standardize on GeoJSON-only, or support CZML / 3D Tiles adapters? (not confirmed in repo) | UI/API | TBD |

### Future extensions

- Add adapter components for Cesium-native formats (e.g., CZML / 3D Tiles) when the data catalog provides them.
- Add richer provenance overlays (hover/click reveals STAC asset + PROV activity/run ID) when API contracts expose these fields.
- Add time-slider synchronization patterns for time-dynamic layers (clock ↔ timeline controls).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  LR["Layer registry JSON<br/>(web/**/layers/**)"] --> V["Cesium components<br/>(viewer + layer bridge)"]
  API["API + catalog endpoints<br/>(focus bundle + layer payloads + provenance refs)"] --> V
  V --> R["Viewer render<br/>(3D layers + entities)"]
  R --> E["UI events<br/>(hover/select/time)"]
  E --> API
~~~

### Optional: Focus Mode sequence diagram (contract-driven)

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as React UI
  participant API as API boundary
  participant C as Cesium Components

  U->>UI: Select entity / open story
  UI->>API: Request Focus Context Bundle (by entity/story ID)
  API-->>UI: Context bundle + provenance refs + focus hints
  UI->>C: Apply focus_center / focus_time / focus_layers
  C-->>UI: Emit select/hover events + provenance pointers
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API boundary (Focus API) | Contract tests + runtime guards |
| Layer registry/config | JSON | `web/**/layers/**` (exact path not confirmed) | JSON schema validation via `schemas/ui/` (if present) |
| Layer payloads | GeoJSON / tiles / Cesium-native (future) | API + catalog endpoints | Contract tests + adapter-level validation |
| User settings | UI state | Local state/store | Type checks + defaults |

### Outputs

| Output | Format | Where | Contract / Schema |
|---|---|---|---|
| Rendered 3D view | DOM/WebGL | Browser runtime | N/A |
| UI interaction events | JS events/state | Browser runtime | N/A |
| Telemetry events (if enabled) | JSON | Runtime → release/run artifacts (not confirmed) | `schemas/telemetry/` (if present) |

### Sensitivity & redaction

- Components must respect any sensitivity flags conveyed via API/config (e.g., “restricted layer”, “generalized geometry only”).
- If a layer/entity is restricted, Cesium components must not reveal precise geometry beyond what policy allows.

### Quality signals

- Avoid blocking the main thread with large parsing; prefer incremental loading and progressive rendering.
- Ensure deterministic rendering given the same inputs (where possible) to support reproducibility.
- Provide clean unmount behavior:
  - detach handlers,
  - remove data sources,
  - destroy viewer/resources.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Cesium UI should link visualized layers back to **STAC Item / Asset IDs** when provided by the API or catalog endpoints.
- Layer info panels should surface: item title, time range, spatial footprint summary, license/attribution, and asset links (when appropriate).

### DCAT

- Where dataset-level metadata is shown (layer info panels), prefer DCAT-aligned fields:
  - title, description, publisher, license, access URL, update frequency (if available).

### PROV-O

- When showing derived or transformed layers, surface a **PROV activity/run identifier** if available.
- In Focus Mode, provenance references should be visible and usable (audit/sources panel pattern).

### Versioning

- UI should tolerate versioned datasets and prefer stable identifiers and lineage links (predecessor/successor) when present.

## 🧱 Architecture

### Components

Recommended component boundary map (names are illustrative; not confirmed in repo):

| Component type | Responsibility | Interface |
|---|---|---|
| Viewer host | Own Cesium viewer lifecycle (mount/unmount) | Props: initial camera, clock/time, imagery/terrain flags |
| Layer bridge | Translate registry “layer config” → Cesium primitives | Input: layer registry + layer payload + metadata |
| Data adapters | Convert API/catalog payloads → Cesium DataSources/Entities | Input: GeoJSON-like data, time hints, styling rules |
| Interaction handlers | Click/hover/select → dispatch UI actions | Emits: selected entity ID + provenance pointers |
| Focus helpers | Apply focus hints (`focus_center`, `focus_time`, `focus_layers`) | Input: Focus Mode bundle |

### Interfaces / contracts

Cesium components must not query Neo4j or catalogs directly.

Cesium components consume:

- API boundary responses (contracted JSON)
- Catalog endpoint responses (STAC/DCAT/PROV JSON as exposed)
- UI registries/config (schema-validated when possible)
- user state

### Extension points checklist (for future work)

- [ ] UI: add new 3D layer entry in registry/config with attribution + sensitivity flags
- [ ] API: ensure contract exposes provenance refs (STAC/PROV IDs) for the layer
- [ ] UI: implement adapter for the new layer type (GeoJSON/CZML/3D Tiles/etc.)
- [ ] Focus Mode: support focus hints for the layer (auto-enable when relevant)
- [ ] Tests: add unit/integration coverage for rendering + provenance display
- [ ] Governance: confirm redaction/generalization behavior for sensitive geometries

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

When Focus Mode activates, Cesium components should:

- center/zoom camera to `focus_center` (if provided)
- align time controls to `focus_time` (if provided)
- enable/disable specific layers via `focus_layers` (if provided)
- preserve provenance affordances (“Sources/Audit” UI patterns)

### Provenance-linked narrative rule

- Any story/narrative UI rendered alongside Cesium must be provenance-linked.
- If AI/predictive content appears, it must be clearly labeled and opt-in, with uncertainty/confidence metadata.

### Optional structured controls (example)

~~~yaml
focus_layers:
  - "treaty_boundaries_1861"   # example only (not confirmed in repo)
  - "forts_and_trails_1850s"   # example only (not confirmed in repo)
focus_time: "1861-01-01"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Minimum validation expectations (align with v13 readiness)

- [ ] Markdown protocol validation (front-matter + structure)
- [ ] Schema validation:
  - UI layer registries validate against `schemas/ui/` (if present)
- [ ] Story Node validation (if UI renders published nodes)
- [ ] API contract tests (UI expectations remain in sync with API)
- [ ] Security + sovereignty scanning gates (secrets, sensitive content handling)

### UI-specific checks

- [ ] Unit test: Viewer lifecycle (mount/unmount/destroy) has no leaks
- [ ] Unit test: Focus hints apply idempotently (enter/exit Focus Mode repeatedly)
- [ ] Integration test: Focus Mode → Cesium shows provenance and does not leak restricted geometry
- [ ] Repo lint (recommended): scan UI for forbidden direct graph access patterns (e.g., Neo4j driver imports / `neo4j://` strings) (not confirmed in repo)
- [ ] Accessibility review for any Cesium-linked UI controls (keyboard, focus order, labels)

### Reproduction

~~~bash
# Replace with repo-specific commands (not confirmed in repo)
# 1) UI lint/typecheck
# 2) UI unit/integration tests
# 3) Markdown/doc lint
# 4) Schema validation for UI registries (schemas/ui)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| FocusModeEntered | UI routing/state | Run/release telemetry artifacts (not confirmed) |
| LayerToggled3D | Cesium layer bridge | Run/release telemetry artifacts (not confirmed) |
| ViewerMounted | Viewer host | Run/release telemetry artifacts (not confirmed) |

## ⚖ FAIR+CARE & Governance

### Review gates

- UI maintainers review for lifecycle/perf correctness and contract alignment
- Governance/ethics review required if:
  - new sensitive layers are introduced
  - new AI narrative behaviors are added
  - new public-facing endpoints/contracts are added

### CARE / sovereignty considerations

- If layers contain culturally sensitive locations or community-restricted knowledge:
  - ensure generalization/redaction rules are implemented at the API boundary and respected in UI
  - avoid “precision by default” (exact coordinates) unless explicitly approved

### AI usage constraints

- Ensure this doc’s AI permissions/prohibitions match intended use.
- Do not represent policy decisions as AI-generated content; defer to governed docs under `docs/governance/`.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial Cesium components README (governed) | TBD |
| v1.0.1 | 2025-12-24 | Aligned wording with v13 contract-first rules (UI registries + Focus Mode provenance-only); clarified validation expectations and 2D/3D state invariants | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
