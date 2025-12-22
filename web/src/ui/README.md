---
title: "KFM Web UI — web/src/ui"
path: "web/src/ui/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:web:ui:readme:v1.0.0"
semantic_document_id: "kfm-web-ui-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:ui:readme:v1.0.0"
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

# KFM Web UI — `web/src/ui`

## 📘 Overview

### Purpose

- Define **how shared UI primitives/components** are organized and implemented under `web/src/ui/`.
- Encode KFM’s UI invariants: **contract-only data access**, **provenance-first presentation**, and **accessible Focus Mode UX**. (See “Context” for non-negotiables.)

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable UI components/primitives used across the web app | ETL, catalog generation, graph ingest, Neo4j migrations |
| Citation/provenance rendering patterns (“audit affordances”) | Backend endpoint implementation details |
| Focus Mode UI composition patterns | Defining new Story Node schemas/templates |
| Map UI controls and layer toggles (presentation layer) | Authoring data products (STAC/DCAT/PROV) |

### Audience

- Primary: Frontend engineers working in `web/` (React + map UI).
- Secondary: API/contract engineers (to understand what the UI expects), curators/editors who publish Story Nodes consumed by the UI.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: **Story Node**, **Focus Mode**, **Layer Registry**, **Provenance**, **Audit affordances**, **Context bundle**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | TBD | Defines canonical pipeline ordering and invariants |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | TBD | Defines canonical homes + contract sets (incl. `schemas/ui/`) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Defines optional Focus Mode controls (`focus_center`, etc.) |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governs this README’s structure |
| API contracts | `src/server/contracts/**` | TBD | UI consumes **contracts**, not raw DB |
| UI schemas | `schemas/ui/**` | TBD | Schema validation for UI registries/config |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] UI invariants (API boundary, provenance rules, a11y) stated clearly
- [ ] Related paths and contracts are linked
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend app | `web/` | React/Map UI implementation |
| UI primitives/components | `web/src/ui/` | Shared UI building blocks, provenance UI patterns |
| API boundary | `src/server/` | REST/GraphQL endpoints + redaction + query services |
| API contracts | `src/server/contracts/**` | Contracted request/response types + tests |
| Story Nodes | `docs/reports/story_nodes/**` | Draft/published narrative artifacts consumed by UI |
| UI schemas | `schemas/ui/**` | UI registry schemas (layer registry, etc.) |
| Story Node schemas | `schemas/storynodes/**` | Validation of story node front-matter + refs |
| Governance | `docs/governance/**` | Ethics/sovereignty/redaction policies and review gates |

### Expected file tree for this sub-area

> This is an **example** layout for `web/src/ui/` (adapt to the current codebase). Do not treat the optional folders as guaranteed.

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        ├── 📄 README.md
        ├── 📁 components/                # optional: reusable UI components
        ├── 📁 focus-mode/                # optional: Focus Mode UI composition
        ├── 📁 map/                       # optional: map controls + layer toggles (UI only)
        ├── 📁 provenance/                # optional: citations + audit affordances
        ├── 📁 hooks/                     # optional: shared UI hooks
        └── 📁 styles/                    # optional: tokens/theme/a11y helpers
~~~

## 🧭 Context

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**:contentReference[oaicite:2]{index=2}

This directory sits in the **React/Map UI** stage. The UI is where KFM’s “evidence-first” design becomes visible: story panels, citations, sources lists, and Focus Mode deep-dives. Focus Mode is intended to be an immersive view that still enforces provenance (no uncited facts) and clearly marks any AI/predictive content as opt-in with uncertainty metadata:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}.

### Non-negotiable UI invariants

- 🚫 **UI must not query Neo4j directly.** The UI only speaks to the **API boundary** (REST/GraphQL) via contract-defined payloads:contentReference[oaicite:5]{index=5}:contentReference[oaicite:6]{index=6}.
- ✅ **Focus Mode consumes provenance-linked content only.** If an item has no source, it should not appear as factual narrative:contentReference[oaicite:7]{index=7}.
- ✅ **Audit affordances are required.** Provide a “Sources”/provenance panel and interactive citations so users can inspect evidence:contentReference[oaicite:8]{index=8}.
- ✅ **Predictive / AI-generated content is opt-in and labeled with uncertainty.** Never present it as unmarked fact:contentReference[oaicite:9]{index=9}.
- ✅ **Accessibility (a11y) is a governed feature.** Keyboard navigation, ARIA labels, and structured headings for story content are required:contentReference[oaicite:10]{index=10}.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  U[User] --> UI[React/Map UI<br/>web/]
  UI -->|contracted REST/GraphQL| API[API boundary<br/>src/server/]
  API --> G[Neo4j graph]
  API --> M[Catalog artifacts<br/>data/stac/** + data/catalog/dcat/** + data/prov/**]
  API --> SN[Story Nodes<br/>docs/reports/story_nodes/**]
  UI --> FM[Focus Mode UI<br/>provenance-linked view]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus Mode “context bundle” | JSON | API endpoint(s) (e.g., `/focus/{id}` pattern) | API contract tests + runtime checks |
| Story Node content | Markdown (+ front-matter) | `docs/reports/story_nodes/**` (or API served) | Story Node schema (`schemas/storynodes/**`) |
| Map layer registry | JSON | `web/**/layers/**` (or API served) | UI schema (`schemas/ui/**`) |
| STAC/DCAT/PROV references | JSON IDs/links | API payloads referencing `data/**` artifacts | Schema validation in `schemas/**` |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered map + narrative panels | UI runtime | `web/` build output | UI tests + a11y checks |
| Citation/audit UI | UI runtime | (within Focus Mode UI) | Must render evidence links reliably |
| Telemetry events (if enabled) | JSON records | `docs/telemetry/**` | `schemas/telemetry/**` |

### Sensitivity & redaction

- The **API is responsible** for redaction/generalization before data reaches the browser.
- The UI must treat any sensitivity flags as **presentation constraints**, not “nice-to-have” metadata:
  - do not re-derive restricted locations,
  - do not display suppressed geometries,
  - ensure Story Node assets are review-gated if required.

### Quality signals

- Citations render consistently and are discoverable (tooltips, clickable footnotes, or Sources panel).
- Focus Mode renders only provenance-linked narrative by default.
- a11y checks pass for interactive controls and reading flow.
- UI layer registry validates against `schemas/ui/**`.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI should be able to surface **STAC Collection/Item IDs** and provide “About this data” affordances where appropriate (especially for map layers and evidence artifacts).

### DCAT

- UI may display dataset-level metadata (publisher/license/coverage) when shown in dataset detail views.

### PROV-O

- UI should support provenance inspection (“what generated this?”) via:
  - PROV activity IDs,
  - derivation links,
  - and “sources” bundles returned by the API.

### Versioning

- When the API provides version lineage (previous/next/derived_from), the UI should display it in a consistent, non-confusing way.

## 🧱 Architecture

### Components (conceptual responsibilities)

| Component | Responsibility | Interface |
|---|---|---|
| Map UI | Render layers + interactions | MapLibre/Cesium wrapper(s) + layer registry |
| Focus Mode shell | Dedicated UI state for deep dive | Focus/context bundle endpoint(s) |
| Story renderer | Markdown → HTML with citation handling | Story Node markdown + sources map |
| Audit/Sources panel | Evidence inspection + provenance drilldown | Sources list + IDs/links from API |
| Layer toggles | Enable/disable layers safely | Registry-driven + schema validated |
| a11y helpers | Keyboard navigation + ARIA | Shared hooks/components |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/**` | Semver + changelog |
| API schemas/contracts | `src/server/contracts/**` | Contract tests required |
| UI layer registry schema | `schemas/ui/**` | Schema-validated registry/config |

### Extension points checklist (for UI work)

- [ ] New map layer: add to layer registry + validate against `schemas/ui/**`
- [ ] New Focus Mode panel/widget: must include evidence hooks and a11y checks
- [ ] New narrative rendering feature: must not allow “uncited facts” to render as fact
- [ ] New AI/predictive UI surface: opt-in only + show uncertainty metadata + label clearly
- [ ] Telemetry changes: update `schemas/telemetry/**` + docs as needed

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Focus Mode UI typically works like:

1) User clicks an entity/story marker or a linked entity in narrative  
2) UI enters Focus Mode state (routing/state management)  
3) UI calls the API to fetch a **context bundle** (story content, related entities, sources, and UI hints)  
4) UI renders narrative + citations and adjusts map/timeline accordingly:contentReference[oaicite:11]{index=11}

### Provenance-linked narrative rule

- Story nodes are Markdown and use a citation marker format like `【source_id†Lx-Ly】`.
- The UI must render citations as interactive affordances (link, tooltip, footnote, or a Sources panel jump), and must not imply a source exists if it does not (“no hallucinated sources”).:contentReference[oaicite:12]{index=12}

### Optional structured controls

Story Nodes may include structured hints for Focus Mode (e.g., map center/time/layers). The UI should support these hints without making them mandatory.

~~~yaml
focus_layers:
  - "TBD_layer_id"
focus_time: "TBD_time_range_or_anchor"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] UI unit tests for shared components (rendering, state behavior)
- [ ] Integration tests for Focus Mode flows (context bundle → narrative + citations)
- [ ] End-to-end tests for key user journeys (open Focus Mode, toggle layers, open sources):contentReference[oaicite:13]{index=13}
- [ ] UI registry/schema validation (`schemas/ui/**`)
- [ ] Story Node/schema validation where relevant (`schemas/storynodes/**`)
- [ ] a11y checks (keyboard navigation, ARIA labeling, heading structure):contentReference[oaicite:14]{index=14}

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) install deps
# npm ci

# 2) run unit tests
# npm test

# 3) run lint + a11y checks
# npm run lint
# npm run test:a11y

# 4) validate UI registries/schemas
# npm run validate:ui-schemas

# 5) run e2e tests (optional)
# npm run test:e2e
~~~

### Telemetry signals (if applicable)

Common UI events worth tracking (schema-governed):

- Focus Mode entered/exited
- Layer toggled
- Citation clicked / Sources panel opened
- AI content toggle opened (opt-in)

Record signals under `docs/telemetry/**` and validate under `schemas/telemetry/**`.

## ⚖ FAIR+CARE & Governance

### Review gates

Requires human review when UI changes introduce:

- new sensitive layers or exposure paths,
- new AI narrative behaviors,
- new public-facing endpoints/flows dependent on governance constraints.

### CARE / sovereignty considerations

- If UI work touches culturally sensitive knowledge or restricted locations, ensure:
  - API-level redaction/generalization is in place,
  - Story Node assets comply with review gates,
  - UI does not re-derive or “helpfully” reconstruct restricted detail.

### AI usage constraints

- AI/predictive content must be:
  - opt-in,
  - clearly labeled as AI/predictive,
  - accompanied by uncertainty/confidence metadata,
  - never presented as unmarked fact.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `web/src/ui` README (governed) | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

