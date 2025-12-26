---
title: "KFM Web UI Styles — README"
path: "web/src/ui/styles/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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
care_label: "CARE Screened (UI styling)"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:ui:styles:readme:v1.0.0"
semantic_document_id: "kfm-web-ui-styles-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:ui:styles:readme:v1.0.0"

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

# KFM Web UI Styles — README

## 📘 Overview

### Purpose

This document governs **how styling is authored, organized, and reviewed** for the KFM web UI, with an emphasis on:
- consistent **design tokens and themes**,
- predictable **component styling conventions**, and
- map/narrative UX requirements (provenance visibility, redaction cues, accessibility).

> Note: The exact styling mechanism in this repo (CSS Modules vs global CSS vs CSS-in-JS, etc.) is **not confirmed in repo**. This README defines the *expected outcomes and conventions* regardless of tooling.

### Scope

| In Scope | Out of Scope |
|---|---|
| Design tokens (color/typography/spacing), theming conventions, component styling patterns, map style integration conventions, a11y style requirements, review gates for style changes | Implementing new UI features, defining new API endpoints, changing graph/ontology, authoring Story Nodes (see Story Node template), choosing a specific CSS framework (unless already adopted in repo) |

### Audience

- Primary: Web UI engineers (React/MapLibre/Cesium)
- Secondary: Narrative curators, data stewards, governance reviewers (for sensitive-layer UX impacts)

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Design token**: a named value (e.g., `--kfm-color-surface`) representing an agreed design decision.
  - **Semantic token**: a token named by purpose (e.g., “surface”, “text”, “danger”), not by raw color (“blue-500”).
  - **Theme**: a set of token values (e.g., light/dark/high-contrast).
  - **Audit affordance**: UI cues that make provenance, redaction, and uncertainty *visible* (badges, footnotes, callouts).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants |
| v13 Redesign Blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch Team | Contract-first UI + schema expectations |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Required structure + metadata |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Focus Mode provenance + citation rules |
| UI schemas | `schemas/ui/**` | UI/Arch | UI registry schema (layer registry, etc.) (**not confirmed in repo**) |
| UI layer registry | `web/**/layers/**` | UI | Layer availability + map styling metadata (**not confirmed in repo**) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout section reflects real repo paths (or marked “not confirmed in repo”)
- [ ] Style conventions cover tokens/themes/components/maps/a11y
- [ ] Governance + CARE/sovereignty implications of style changes are explicitly stated
- [ ] Validation steps are listed and repeatable (placeholders labeled)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/styles/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (frontend) | `web/` | React app, map components (MapLibre/Cesium), Focus Mode UI, layer registries |
| UI source | `web/src/` | UI implementation code |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL contracts consumed by UI (**not confirmed in repo**) |
| UI schemas | `schemas/ui/**` | JSON Schemas for UI registries (**not confirmed in repo**) |
| Story Nodes | `docs/reports/story_nodes/**` | Draft + published narratives displayed in Focus Mode (**not confirmed in repo**) |
| Governed docs | `docs/` | Canonical architecture + governance standards |

### Local layout (one-branch)

~~~text
📂 web/
└─ 📂 src/
   └─ 📂 ui/
      └─ 📂 styles/
         └─ 📄 README.md  — styling conventions (this file)
~~~

### Expected contents (conventional, may differ)

If/when this folder contains additional assets, prefer a structure like:

- `tokens.*` — design tokens (CSS variables and/or JSON for JS consumption)
- `themes.*` — theme definitions (light/dark/high-contrast)
- `components/` — shared component styles (if not co-located)
- `map/` — map-specific styling helpers (legend swatches, layer style adapters)
- `utilities/` — small utilities (visually-hidden, focus-ring helpers, etc.)

If the repo already uses a different structure, keep this README aligned with reality.

## 🧭 Context

KFM’s canonical architecture routes data and narrative through the API boundary into the UI, and Focus Mode must present **provenance-linked** information only (with AI/predictive content clearly marked when present). Styles are part of enforcing these UX guarantees.

Key constraints this styling folder must support:

- **API boundary rule**: UI must not connect to the graph directly; the API enforces provenance + redaction/generalization rules. Styling must not “paper over” missing provenance or hide audit cues.  
- **UI contract**: UI is responsible for “layer registry + a11y + audit affordances” and must avoid “hidden data leakage” (e.g., visual interactions that reveal restricted location detail).  
- **Layer registry integration**: map layers are configured via a UI layer registry, which defines layer availability and styling metadata and is schema-validated (where configured).

## 🧱 Architecture

### 1) Principles (non-negotiable)

1. **Semantic tokens first**: Prefer naming by meaning (“surface”, “text”, “accent”) instead of raw colors.
2. **Themeable by design**: All end-user visible colors should be token-driven so themes can swap values.
3. **A11y is a styling requirement**: Focus states, contrast, and reduced motion are part of “done”.
4. **Audit affordances are always visible**: Provenance badges, citations/footnotes, redaction notices, and AI/uncertainty markers must be styled as first-class UI elements.
5. **No style-driven leakage**: Hover/popup/outline/highlight patterns must not reveal sensitive geometry detail that governance intends to generalize or redact.

### 2) Design tokens

Preferred token categories (names illustrative):

- Color:
  - `--kfm-color-surface`
  - `--kfm-color-surface-muted`
  - `--kfm-color-text`
  - `--kfm-color-text-muted`
  - `--kfm-color-accent`
  - `--kfm-color-danger`
  - `--kfm-color-border`
- Typography:
  - `--kfm-font-family-sans`
  - `--kfm-font-size-1 …`
  - `--kfm-line-height-…`
- Spacing:
  - `--kfm-space-1 …`
- Radius/shadow:
  - `--kfm-radius-…`
  - `--kfm-shadow-…`
- Z-index:
  - `--kfm-z-tooltip`
  - `--kfm-z-modal`

Example token definition (format depends on repo tooling):

~~~css
:root {
  --kfm-color-surface: #ffffff;
  --kfm-color-text: #111111;
  --kfm-color-accent: #1f6feb;
  --kfm-focus-ring: 0 0 0 3px rgba(31, 111, 235, 0.35);
}
~~~

### 3) Themes

Preferred approach:
- Default theme is applied at the app root (e.g., `data-theme="light"`).
- Themes override token values only (components should not hardcode theme decisions).

Example (illustrative):

~~~css
:root[data-theme="dark"] {
  --kfm-color-surface: #0b0f14;
  --kfm-color-text: #e6edf3;
}
~~~

### 4) Component styling conventions

Because the styling tech is **not confirmed in repo**, apply these rules in whichever system exists:

- Keep selectors **shallow** (avoid deeply nested selectors that are hard to override).
- Prefer **class-based styling** to element selectors for maintainability.
- Avoid global leakage:
  - If using global CSS, scope with a root class (e.g., `.kfm-app …`) where possible.
  - If using CSS Modules, prefer local classes and map tokens via `var(--token)`.
- Always style:
  - keyboard focus states (`:focus-visible`),
  - disabled states,
  - error states,
  - loading/skeleton states (if present),
  - “audit” UI elements (citations, provenance badges).

### 5) Map styling integration (MapLibre / Cesium)

Map layer styling is part of the UI contract and typically flows from the **layer registry** (schema validated) into the map renderer.

Guidelines:
- Map layer colors should come from the same token palette (or a controlled map palette derived from tokens).
- Legends must match the layer style and remain readable in all themes.
- Selection/hover states must not reveal restricted detail (e.g., outlining polygons that have been generalized for governance reasons).

If map styles are defined in JSON (e.g., MapLibre style spec), consider a build-time or runtime step that injects token-derived color values rather than duplicating raw hex values in multiple places.

### 6) Z-index + overlay rules

Define and use a small, documented z-index scale (tokens recommended):
- Tooltips above popovers
- Popovers above drawers
- Drawers above modals
- Modals above everything else

Avoid ad-hoc z-index values in components.

### 7) Motion and reduced motion

Any transitions/animations must respect reduced motion:
- Avoid parallax or large movement animations by default.
- If animations exist, provide a reduced motion fallback.

Example:

~~~css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.001ms !important;
  }
}
~~~

## 🧠 Story Node & Focus Mode Integration

Styles must actively support Focus Mode’s evidence-first rules:

- **Citations are UI objects**: Footnotes/popovers/source links should be visually consistent and clearly associated with each claim.
- **Provenance cues are not optional**:
  - “Source” chips, evidence IDs, and audit flags must not be visually hidden behind low-contrast styling.
- **AI/predictive content must be unmistakable**:
  - Use a consistent badge + callout style (and a consistent placement) for AI/predicted elements.
  - Uncertainty/confidence metadata should have a visible, standardized affordance (e.g., tooltip, inline range, or “confidence chip”).
- **Redaction/generalization must be legible**:
  - If a layer is generalized/redacted, the UI should show a clear notice (banner/callout) with a consistent severity style.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks (front-matter + required sections)
- [ ] UI registry checks (layer registry schema validation), if configured
- [ ] Accessibility checks (keyboard focus visibility, contrast checks), if configured
- [ ] Visual regression checks for theme changes, if configured
- [ ] Security/governance scan expectations: ensure styles do not introduce “hidden data leakage” patterns

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) lint styles (if configured)
# npm run lint:styles

# 2) run UI unit/integration tests
# npm test

# 3) run accessibility checks (if configured)
# npm run test:a11y

# 4) validate UI registries (if configured)
# npm run validate:ui-registry
~~~

## ⚖ FAIR+CARE & Governance

### Review gates (styling-specific)

Escalate for governance review when a style change could:
- make sensitive layers easier to interpret or extract (e.g., stronger outlines, higher contrast, interaction affordances that expose geometry),
- change how provenance/citation information is displayed (risk of hiding or de-emphasizing evidence),
- introduce or change AI/predictive UI markers (risk of presenting AI output as fact).

### CARE / sovereignty considerations

- If any UI interaction (hover, click, tooltip, selection, export) increases the precision of location-bearing information, treat it as a governance-sensitive change.
- Prefer **coarse/aggregate** presentation for layers with restricted locations.
- Ensure redaction/generalization indicators are consistently styled and cannot be mistaken for “missing data”.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy; inferring sensitive locations (directly or indirectly)
- Human review remains required for changes that affect public interpretation of sensitive layers.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `web/src/ui/styles/README.md` defining styling conventions + governance/a11y expectations | TBD |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Redesign blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

