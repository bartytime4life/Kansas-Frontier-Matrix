---
title: "KFM Web UI Components — README"
path: "web/src/app/_components/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:src:app:_components:readme:v1.0.0"
semantic_document_id: "kfm-web-src-app-components-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:app:_components:readme:v1.0.0"
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

# KFM Web UI Components — README

Reusable UI components for the KFM web application.

This directory exists to keep UI building blocks **composable**, **testable**, and **architecture-safe**:
- UI reads data **only** through contracted APIs (no direct graph access).
- Focus Mode renders **provenance-linked** narrative with visible citations and audit affordances.
- Sensitive content must remain protected (redaction/generalization is enforced by policy and should be respected by UI).

---

## 📘 Overview

### Purpose

- Define conventions for reusable components under `web/src/app/_components/`.
- Encode KFM UI invariants: **API boundary**, **provenance-linked narrative**, **Focus Mode composition**, **accessibility**, and **governance awareness**.
- Provide a stable “how to add a component” checklist so UI growth stays CI-clean and contract-compliant.

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable UI components and feature composites in this folder | API implementation and contracts (`src/server/`) |
| Focus Mode UI composition patterns (map + story + audit + timeline) | Graph model, Neo4j queries, ontology work (`src/graph/`) |
| Story Node Markdown rendering + citation UX expectations | Authoring Story Nodes (lives under `docs/reports/story_nodes/`) |
| A11y/performance conventions for shared components | Governance/policy authoring (`docs/governance/`) |

### Audience

- **Primary:** Frontend contributors implementing KFM UI features.
- **Secondary:** Reviewers validating architecture invariants and narrative curators verifying Focus Mode behavior.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this README:
  - **Focus Mode**: a UI state showing a story/entity in detail.
  - **Story Node**: governed Markdown narrative with citations.
  - **Context bundle**: API response that supplies entity + narrative + provenance refs for Focus Mode.
  - **Audit panel**: UI surface that exposes sources, provenance, warnings, and AI markers.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | *(not confirmed in repo)* |
| Universal governed-doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governed Markdown rules |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | YAML front-matter + Focus hints |
| API layer contracts | `src/server/contracts/` | API | Canonical contract location per blueprint |
| UI schemas | `schemas/ui/` | Platform/UI | Schema validation for registries *(not confirmed in repo)* |

### Definition of done

- [ ] Front-matter is complete and matches the KFM Universal template shape
- [ ] Directory layout section includes an emoji tree
- [ ] All architecture invariants are explicitly stated
- [ ] Story Node + Focus Mode rendering expectations are documented
- [ ] Validation steps are listed (or clearly marked “not confirmed in repo”)
- [ ] Footer refs include Master Guide + templates + governance links

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/app/_components/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI routes/layouts | `web/src/app/` | Route segments, layouts, server components, data wiring |
| Shared UI components | `web/src/app/_components/` | Reusable building blocks (this directory) |
| API boundary | `src/server/` | API code, redaction rules, contract enforcement |
| Graph build + ontology | `src/graph/` | Neo4j ingest, ontology bindings, integrity checks |
| Story Nodes | `docs/reports/story_nodes/` | Markdown narrative content (governed) |
| Schemas | `schemas/` | STAC/DCAT/PROV + UI schemas *(UI schemas not confirmed in repo)* |
| Governance | `docs/governance/` | FAIR+CARE, ethics, sovereignty rules |

### Expected structure

This folder is intentionally “feature-oriented.” Keep components grouped by user-facing capability (map, timeline, narrative) rather than by framework internals.

~~~text
web/
└── 📁 src/
    └── 📁 app/
        ├── 📁 _components/
        │   ├── 📄 README.md                          # 📘 This file
        │   ├── 📁 focus-mode/                        # Focus Mode composites (not confirmed in repo)
        │   ├── 📁 story/                             # Story Node rendering helpers (not confirmed in repo)
        │   ├── 📁 map/                               # MapLibre/Cesium wrappers (not confirmed in repo)
        │   ├── 📁 timeline/                          # Timeline components (not confirmed in repo)
        │   └── 📁 ui/                                # Reusable primitives (buttons, panels) (not confirmed in repo)
        └── …                                         # route segments, layouts, etc.
~~~

---

## 🧭 Context

### Architectural invariants

These are non-negotiable for anything in `_components/`:

1. **API boundary is strict**
   - UI must not query Neo4j (or any graph store) directly.
   - UI must consume data via contracted endpoints (REST/GraphQL), using contract types where available.

2. **Provenance-linked narrative only**
   - Story Nodes must include citations.
   - Focus Mode must display audit affordances (sources panel, citation interactions, warnings).

3. **Predictive and AI-generated content is opt-in**
   - If the API supports `includeAI` or similar, UI defaults must be “off.”
   - Any AI-generated content must be labeled and paired with confidence/uncertainty metadata.

4. **Sensitive content must not be re-exposed**
   - If a layer/dataset is sensitive, UI must respect redaction/generalization and show user-facing notices when required.
   - No “clever” client-side inference of restricted coordinates.

### What belongs in `_components_`

- Presentational primitives and composable composites that can be reused across routes.
- UI-only logic: formatting, rendering, interaction handling, a11y behavior.
- Integration wrappers for browser-only libraries (MapLibre, Cesium), isolated as client components.

What should **not** live here:
- Page-level data fetching that couples a component to a specific route segment (prefer route-level wiring).
- Direct dependency on graph identifiers without going through the API contract.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Graph Build + Neo4j]
  C --> D[API Layer]
  D --> E[Web UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph E[Web UI]
    R[Routes & Layouts]
    Cmp[_components]
    R --> Cmp
  end
~~~

---

## 📦 Data & Metadata

### Inputs this UI typically consumes

- **Layer registry** describing map layers (sources, attribution, sensitivity flags).
- **Focus Mode context bundle** from an API endpoint (entity + story node + sources + warnings).
- **Story Node Markdown** including citations of the form `【source†Lx-Ly】`.

### Recommended contract-first pattern

- Keep API response parsing at the route or in a dedicated “container” component.
- Pass validated, typed props into shared components.

~~~ts
// Illustrative only — not confirmed in repo.
// Prefer generated types from API contracts if available.
export type FocusContextBundle = {
  entity: { id: string; type: string; label: string };
  storyNode?: {
    id: string;
    markdown: string;
    frontMatter?: Record<string, unknown>;
  };
  sources: Array<{
    id: string;
    title?: string;
    uri?: string;
    license?: string;
  }>;
  warnings?: Array<{ code: string; message: string }>;
};
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

UI does not generate catalogs, but it **must not break the chain of evidence**:

- If a map layer comes from a STAC Item/Asset, UI should prefer showing:
  - dataset title/description (DCAT),
  - provenance links (PROV),
  - license/attribution fields,
  - stable IDs (dataset_id, stac_item_id) over raw file paths.

Recommended UI affordances:
- “View sources” drawer that lists the datasets used in the current Focus Mode context.
- “Provenance” panel that links (by ID) to catalog/prov records when available.

---

## 🧱 Architecture

### Component tiers

Use a simple tier model:

- **Primitives**: buttons, panels, badges, icons.
- **Composites**: legend panels, layer toggles, citation popovers.
- **Feature shells**: Focus Mode layout, map+timeline coordination wrappers.

### Server vs client components

Because `web/src/app/` suggests a Next.js App Router structure:

- Prefer **server components** by default for layout and data wiring.
- Use **client components** only when required for:
  - MapLibre/Cesium instances,
  - event listeners, DOM APIs, local UI state,
  - interactive citation popovers.

Guideline:
- Keep “use client” at the shallowest possible leaf boundary.
- Avoid making an entire page client-only just to support one map control.

### Naming and exports

Recommended (adjust to repo conventions if different):

- Component folders: `kebab-case/`
- Component names: `PascalCase`
- Barrel export per folder: `index.ts` *(not confirmed in repo)*

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode flow

Expected user flow:

1) User clicks an entity (map feature, search result, or link in narrative)  
2) App enters **Focus Mode** using that entity/story ID  
3) UI calls a Focus API endpoint to fetch a **context bundle**  
4) UI renders:
   - narrative text (Markdown + citations),
   - audit/provenance panel,
   - map + timeline state adjusted to the story context

### Focus Mode component composition

Recommended component composition (feature shell + subcomponents):

- `FocusModeShell`
  - `StoryPanel` (Markdown + citations)
  - `AuditPanel` (sources, warnings, sensitivity notices, AI badges)
  - `TimelinePanel` (time slider / highlights)
  - `MapViewport` (map remains visible; layers filtered/highlighted)

### Story Node Focus hints

Story Nodes may include optional Focus hints in YAML front-matter (from Story Node template), such as:

- `focus_layers`: which layer IDs to enable
- `focus_time`: which time range to apply
- `focus_center`: longitude/latitude to center the map

UI expectations:
- Apply these hints when entering Focus Mode.
- Do not “lock” the user — hints set the initial view, but the user can pan/zoom/toggle layers.

### Citation rendering requirements

Story Nodes are authored with inline citations like:

- `【source†L10-L20】`

UI should:
- Parse citations and render them as clickable elements (links or popovers).
- Provide a Sources/Audit panel so users can inspect the referenced material.
- Never allow “citation-looking text” to be used as a fake source; citations should resolve to known sources returned by the API (or be flagged).

Implementation note:
- Use a Markdown renderer (choice not confirmed in repo) and add a post-pass to transform `【…】` markers into structured citation components.

---

## 🧪 Validation & CI/CD

### Validation checklist for component changes

- [ ] No direct Neo4j/graph access added to UI code
- [ ] Any new Focus Mode feature consumes contract types and includes audit affordances
- [ ] New interactive UI passes accessibility review (keyboard nav, focus states, ARIA labels)
- [ ] No secrets/tokens added
- [ ] Any new layer toggle/control respects sensitivity flags and redaction behavior

### Recommended commands

Commands depend on repo tooling; replace with actual scripts.

~~~bash
# not confirmed in repo — replace with actual commands
# pnpm -C web lint
# pnpm -C web test
# pnpm -C web typecheck
~~~

If UI layer registries exist and are schema-validated, ensure:
- schema validation runs in CI,
- registry edits are reviewed for sensitivity impacts.

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when UI changes could:

- reveal sensitive locations via interaction/zoom,
- introduce new user-visible AI narrative behavior,
- publish or expose derived layers built from restricted inputs,
- bypass audit/provenance display expectations.

Approvals and roles are **not confirmed in repo**; follow:
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`

### AI usage constraints

- Allowed AI transforms for governed docs are limited (see front-matter).
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).

UI implication:
- Avoid “smart” client-side inference that could reconstruct restricted detail.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for `web/src/app/_components/` conventions | TBD |

---

## Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo)*
---

