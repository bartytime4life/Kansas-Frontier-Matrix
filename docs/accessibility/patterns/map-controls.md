---
title: "Accessibility Pattern — Map Controls"
path: "docs/accessibility/patterns/map-controls.md"
version: "v0.1.0"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:map-controls:v0.1.0"
semantic_document_id: "kfm-accessibility-pattern-map-controls-v0.1.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:map-controls:v0.1.0"
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

# Accessibility Pattern — Map Controls

## 📘 Overview

### Purpose
- Define a reusable implementation pattern for **accessible map controls** in KFM’s React/Map UI (MapLibre/Leaflet/Cesium-backed).
- Ensure map navigation, time filtering, and layer interaction are **keyboard-operable** and **screen-reader-usable**, while respecting KFM’s **no hidden data leakage** and **CARE/sovereignty** requirements.

### Scope
| In Scope | Out of Scope |
|---|---|
| Map viewport controls (zoom, rotate, reset, fullscreen, locate) | API contract changes (OpenAPI/GraphQL) |
| Layer controls (toggle, legend, opacity, category grouping) | STAC/DCAT/PROV schema/profile changes |
| Timeline controls (year/era slider, stepper, play/pause) | Story Node content authoring |
| Feature inspection patterns (popups, dossiers/info panels) | Non-map UI (charts unrelated to map interaction) |
| A11y announcements + focus management + keyboard flow | Visual design system tokens (colors, typography) |
| Sensitive-layer safeguards (gating + coordinate redaction) | Backend redaction implementations |

### Audience
- Primary: Frontend engineers implementing map UI and controls in `web/`
- Secondary: UX/design, QA, governance reviewers (especially for sensitive layers + Focus Mode)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Map controls**: UI elements that modify map view/state (zoom, pan, layers, time, focus).
  - **Layer registry**: Declarative list of available layers and access rules used by the UI.
  - **Focus Mode**: Topic-centric UI mode that constrains map/time/layers and enforces provenance.
  - **Provenance-linked content**: UI-visible claims/assets traceable to dataset/record IDs.
  - **CARE gating**: Rules that prevent sensitive locations/data from being exposed.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This pattern doc | `docs/accessibility/patterns/map-controls.md` | UI/UX | Patterns + checklists |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + subsystem contracts |
| UI layer registry | `web/**/layers/*.json` (TBD) | UI | Declarative layer list + access rules |
| Map UI source | `web/` | UI | Components + map integration |
| Design docs | `docs/design/` | UI/UX | UI architecture notes + decisions |
| Governance docs | `docs/governance/*` | Governance | CARE/sovereignty + ethics |

### Definition of done (for this document)
- [x] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable (repo-specific commands filled in)
- [x] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/patterns/map-controls.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Accessibility docs | `docs/accessibility/` | A11y standards, patterns, checklists |
| Frontend | `web/` | React + map clients + control components |
| Schemas | `schemas/` | JSON schemas (incl. UI registry schemas if present) |
| Governance | `docs/governance/` | Policy + ethics + sovereignty rules |

### Expected file tree for this sub-area
~~~text
📁 docs
├── 📁 accessibility
│   └── 📁 patterns
│       └── 📄 map-controls.md
~~~

## 🧭 Context

### Background
KFM’s UI is a React-based web application with an interactive map and timeline, with layered overlays and control panels. The map layer list is driven by catalog/registry configuration, and Focus Mode can constrain map/time to a topic while enforcing provenance and governance rules.

Because map renderers often draw into canvas/WebGL, accessibility depends heavily on the surrounding **controls**, **focus order**, and **alternative representations** (e.g., lists/dossiers).

### Assumptions
- The map is rendered via MapLibre GL JS (and optionally Leaflet/Cesium in some contexts).
- UI panels include (at minimum) map view + layer controls + timeline controls + an info/dossier panel.
- Layer availability and access rules are centrally governed (layer registry).

### Constraints / invariants
- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- UI contract: **no hidden data leakage**; layer access is governed by registry + gating.
- Focus Mode contract: **provenance-linked content only**; sensitive locations may be blurred/generalized; no hallucinated sources.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical layer registry paths + schemas in `web/`? | TBD | TBD |
| Which map engines are active in production (MapLibre vs Leaflet vs Cesium)? | TBD | TBD |
| What automated a11y tooling is in CI (axe/playwright/storybook)? | TBD | TBD |
| Are keyboard shortcuts allowed and, if so, how are they documented + configurable? | TBD | TBD |

### Future extensions
- Add pattern docs for `timeline-controls.md`, `layer-panel.md`, `feature-popups.md`
- Provide a shared “MapControls” component library with consistent semantics + testing hooks
- Add user settings: reduce motion, high-contrast mode, and “simplify map interactions”

## ♿ Accessibility Pattern — Map Controls

### Goals
- **Keyboard operability**: Every map control action has a keyboard path.
- **Screen-reader support**: Controls have meaningful names/roles/states; key updates are announced.
- **Predictable focus**: Tab order is stable; focus never “disappears” into canvas.
- **Equivalent access**: Primary map content is also discoverable via a non-map UI (dossier/list/search results).
- **Governance-safe**: Control UI must not leak restricted locations/attributes (including via announcements).

### Non-goals
- Specify exact visual styling, icons, or color palette (handled by design system).
- Define backend redaction rules (handled in API/data governance).

### Regions, labels, and focus order
**Recommended landmark structure**
- A labeled region for the map (“Interactive map”)
- A labeled region for controls (“Map controls”)
- A labeled region for contextual details (“Details panel” / “Dossier”)
- Optional: a labeled region for provenance/audit (“Audit & sources”)

**Recommended tab order**
1. Skip link(s) (e.g., “Skip map” / “Skip to timeline”)
2. Map controls toolbar (zoom/rotate/reset/fullscreen)
3. Layer controls (panel toggle → layer list)
4. Timeline controls
5. Map canvas (if focusable; see note below)
6. Details/dossier panel
7. Audit/provenance panel (if present)

**Map canvas focusability**
- If the map canvas is focusable, it should:
  - Have a clear label and a short “how to use” hint available via a Help control.
  - Avoid trapping focus (Esc should return focus to controls).
- If the map canvas is not focusable, users must still be able to:
  - Navigate layers/time
  - Search/select features
  - Open the dossier/details for selected items

### Pattern: Viewport controls (zoom, rotate, reset, fullscreen, locate)
- Use **native `<button>`** elements.
- Each button provides:
  - Visible label or icon + accessible name (`aria-label` when icon-only)
  - State when applicable:
    - fullscreen: `aria-pressed="true|false"`
    - compass/rotation lock: `aria-pressed="true|false"` (if toggle)
- Provide a **Reset view** that restores a known baseline (extent + rotation + tilt).

**Touch targets**
- Controls must be large enough for touch/mobility access (avoid tiny icon-only hit areas).

### Pattern: Layer controls (toggle, groups, legends, opacity)
- The layer panel open/close control is a button with:
  - `aria-expanded`
  - `aria-controls` pointing at the panel container
- Prefer native inputs:
  - Layer on/off: `<input type="checkbox">`
  - Basemap selection: `<input type="radio">` within a `<fieldset>`
- Layer list items should include:
  - A concise label (layer name)
  - Optional short description (what it represents)
  - Time coverage summary (when relevant)
  - Provenance link or reference (when available)

**Legend**
- Legends must not rely on color alone:
  - Include labels and/or patterns/symbols
  - Ensure text alternatives are present for screen readers

**Opacity controls**
- Prefer `<input type="range">` with:
  - Visible label and/or `aria-label`
  - Current value exposed (e.g., “Opacity 70%”)
  - Keyboard operable (arrow keys adjust in steps)

### Pattern: Timeline controls (year/era slider, stepping, play/pause)
Because time is central to KFM, timeline controls must be accessible without drag:
- Timeline selection:
  - `<input type="range">` or ARIA slider pattern **with full keyboard support**
  - Provide a numeric input alternative (year/era entry) for precision
- Playback controls:
  - Play/pause is a button with `aria-pressed`
  - Step previous/next are buttons (not custom divs)
- Announcements:
  - When time changes, update an `aria-live="polite"` status like “Year set to 1870”
  - Avoid excessive announcements during continuous playback (throttle updates)

### Pattern: Feature inspection (selection, popup, dossier)
- Clicking a feature must have a keyboard equivalent:
  - Feature list/search results support Enter/Space to select
- If a popup is used:
  - Treat complex popups as a dialog-like surface:
    - Focus moves into the popup when opened
    - Close button is first/last focusable
    - Esc closes and returns focus to the trigger
- Prefer “Details panel / dossier” as the main accessible reading surface:
  - When a feature is selected, update the dossier panel content
  - Announce “Details updated for <Feature name>” (polite live region)

### Pattern: Screen reader announcements (status + changes)
Use a single, centralized live region to avoid duplicate announcements.
- Announce:
  - Layer toggles: “Layer Railroads enabled”
  - Time changes: “Year set to 1870”
  - Focus Mode activation: “Focus Mode enabled; map locked to <region> and <time>”
- Do **not** announce:
  - Raw coordinates (especially when sensitive layers are in use)
  - Rapid changes at high frequency (throttle)

Example skeleton:
~~~html
<div id="map-status" aria-live="polite" aria-atomic="true" class="sr-only"></div>
~~~

### Pattern: Keyboard shortcuts
Keyboard shortcuts are optional, but if implemented:
- They must be:
  - Documented in UI (Help / “Keyboard shortcuts” dialog)
  - Discoverable by screen readers
  - Disable-able (user preference)
- Avoid conflicting with browser/screen reader reserved shortcuts.

### Pattern: Focus Mode interactions
When Focus Mode is activated:
- Map/time/layer state changes should be:
  - Reflected in control UI (disabled/enabled states where appropriate)
  - Announced once (polite live region)
- Controls that could break Focus Mode constraints should be:
  - Disabled with explanation text (e.g., “Time locked by Focus Mode”)
- Ensure sensitive locations remain generalized/redacted in both:
  - Visual map rendering
  - Text announcements / dossier content

### Pattern: Sensitive data safeguards (CARE + no leakage)
- If the UI includes a coordinate readout or shareable permalink:
  - It must respect layer gating and sensitivity rules.
  - For restricted contexts, coordinates should be omitted or generalized.
- Any text alternative (e.g., screen reader labels, dossier summaries) must not expose restricted geometry detail.

### Implementation notes (non-binding)
- Prefer semantic HTML and native form controls over div-based widgets.
- Ensure visible focus styles (do not remove outline without replacement).
- Validate third-party map controls for a11y; wrap/replace if they do not meet requirements.

Example toolbar structure:
~~~html
<nav aria-label="Map controls">
  <div role="toolbar" aria-label="Map navigation">
    <button type="button" aria-label="Zoom in">+</button>
    <button type="button" aria-label="Zoom out">−</button>
    <button type="button" aria-label="Reset view">Reset</button>
    <button type="button" aria-pressed="false" aria-label="Fullscreen">Fullscreen</button>
  </div>
</nav>
~~~

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  U["User"] --> C["Map Controls UI (React)"]
  R["Layer Registry / Catalog JSON"] --> C
  C --> S["Map State"]
  S --> M["Map Engine (MapLibre / Leaflet / Cesium)"]
  S --> A11Y["ARIA Status / Live Region"]
  C --> API["APIs"]
  API --> G["Graph / Data Services"]
  C --> D["Dossier / Details Panel"]
  D --> A11Y
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI as React UI
  participant Reg as Layer Registry
  participant Map as Map Engine
  participant API as APIs
  User->>UI: Toggle layer ON
  UI->>Reg: Validate layer is allowed + gated
  Reg-->>UI: Layer config (source, access rules)
  UI->>API: Fetch metadata / tiles (as configured)
  API-->>UI: Data payload / URLs
  UI->>Map: Add source + render layer
  UI->>UI: Update aria-live ("Layer enabled")
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Layer registry entries | JSON | `web/**/layers/*.json` (TBD) | UI schema checks (if present) |
| Time context | UI state | Timeline control | UI unit/integration tests |
| Focus context | UI state + API response | Focus Mode activation | Contract + UI tests |
| User preferences | UI state | Settings (TBD) | UI tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Map controls UI | React components | `web/` | UI a11y checks |
| Accessible announcements | DOM (`aria-live`) | UI | Manual + automated a11y tests |
| Map rendering state | Map engine state | UI runtime | Smoke tests |

### Sensitivity & redaction
- If a layer or Focus Mode context is sensitive, the UI must:
  - Avoid displaying precise coordinates in text
  - Avoid announcing coordinates in live regions
  - Respect registry gating and default visibility rules (e.g., off-by-default, zoom-limited)

### Quality signals
- Keyboard-only navigation passes (no dead ends)
- Screen reader smoke test (labels + state changes understandable)
- Visible focus indicators on all interactive controls
- Sensitivity checks: no restricted details in text/announcements

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: N/A (UI pattern only)
- Items involved: N/A
- Extension(s): N/A

### DCAT
- Dataset identifiers: N/A
- License mapping: N/A
- Contact / publisher mapping: N/A

### PROV-O
- `prov:wasDerivedFrom`: N/A
- `prov:wasGeneratedBy`: N/A
- Activity / Agent identities: N/A

### Versioning
- This document is versioned independently; UI implementation changes should reference this doc in PRs/issues where applicable.

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
- Map controls must reflect Focus Mode constraints (locked time, constrained layers, pinned extent).
- Focus Mode activation should announce the new constrained context and expose provenance/audit affordances without leaking restricted details.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

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
- [ ] UI schema checks (layer registry)
- [ ] UI accessibility checks (automated + manual)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run markdown lint / protocol validation
# 2) run UI unit tests
# 3) run UI integration tests (keyboard)
# 4) run automated a11y checks (axe)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Map control usage events (toggle, zoom, time change) | UI | `docs/telemetry/` + `schemas/telemetry/` |
| A11y failures in CI | CI | CI logs / reports |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI maintainers approve map-control pattern and implementation changes.
- Governance review is required when:
  - New sensitive layers become user-visible
  - Coordinate display/sharing behaviors change
  - Focus Mode behavior could reveal restricted data through UI/announcements

### CARE / sovereignty considerations
- Sensitive locations must be protected in all user-facing modalities:
  - Visual map rendering
  - Text UI (tooltips, dossiers)
  - Screen-reader announcements (live regions)

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.
- Do not use AI tooling to infer or expose sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial draft pattern for accessible map controls | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
