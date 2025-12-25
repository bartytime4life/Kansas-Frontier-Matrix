---
title: "KFM Web UI Styles — README"
path: "web/src/styles/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:styles:readme:v1.0.0"
semantic_document_id: "kfm-web-styles-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:styles:readme:v1.0.0"
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

> **Purpose (required):** Define the **styling contract** for the KFM Web UI (React + Map UI), including **design tokens, theming, CSS architecture**, and **map-style integration points** (MapLibre/Cesium), with **accessibility**, **determinism**, and **governance** considerations.

## 📘 Overview

### Purpose

- Provide a single, repo-local reference for **how styles are organized, named, and validated** in the KFM UI.
- Establish **stable styling contracts** (tokens, theming, layering rules) so UI work stays deterministic and reviewable.
- Define how the UI should **consume dataset-provided cartographic styles** (e.g., MapLibre style JSON + legend YAML) without coupling UI code to data internals.

### Scope

| In Scope | Out of Scope |
|---|---|
| Design tokens (colors, typography, spacing), theming strategy, and CSS layering rules | Authoring domain cartography from scratch (belongs with the dataset/domain; UI consumes published styles) |
| Component styling conventions (scoped styles, naming, composition) | Backend/API contract definitions (see API contract docs) |
| UI accessibility styling requirements (focus rings, reduced motion, contrast) | Neo4j/graph access patterns (UI must not query Neo4j directly; via API only) |
| Guidance for loading/validating map style assets (MapLibre JSON, legend YAML) | ETL/catalog generation details (see `src/pipelines/**`, `data/**`) |

### Audience

- Primary: Web/UI contributors (React components, Map UI, Focus Mode UI)
- Secondary: Accessibility reviewers; governance reviewers; data/domain owners publishing map styles

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc:
  - **Design tokens**: Named, versioned values used across UI (e.g., spacing scale, colors).
  - **Theme**: A coherent set of tokens (e.g., light/dark/high-contrast).
  - **UI chrome**: Panels/controls/labels around the map (CSS-driven).
  - **Map style**: Renderer-driven styling (e.g., MapLibre style JSON), not CSS.
  - **Legend YAML**: Machine-readable legend definitions that can drive UI legends.
  - **Focus Mode**: Immersive narrative + map/timeline view; must display provenance-linked content only.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/src/styles/README.md` | UI | Contract for styling conventions |
| Tokens (CSS variables) | `web/src/styles/tokens.css` (**not confirmed in repo**) | UI | Prefer `--kfm-*` variables |
| Theme(s) | `web/src/styles/theme*.css` (**not confirmed in repo**) | UI | Light/dark/high-contrast (as adopted) |
| Global reset/base | `web/src/styles/reset.css` (**not confirmed in repo**) | UI | Normalize + base element styles |
| Component styles | `web/src/**/<Component>.module.css` (**not confirmed in repo**) | UI | Preferred: component-scoped styles |
| Layer registry | `web/**/layers/*.json` (**not confirmed in repo**) | UI | UI-extensible layer config registry |
| Dataset “styles pack” example | `extras/styles/*.json` + `extras/styles/*.yaml` (**pattern; not confirmed in repo**) | Data domain | MapLibre style JSON + legend YAML for deterministic styling across clients |
| Governance refs | `docs/governance/*` | Governance | Required review gates + sovereignty rules |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Scope clearly separates **UI CSS** vs **renderer map styles**
- [ ] “Not confirmed in repo” labels used wherever paths/tools are speculative
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Version history present

## 🗂️ Directory Layout

### This document

- `path`: `web/src/styles/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + STAC/DCAT/PROV outputs |
| Documentation | `docs/` | Canonical governed docs + templates |
| Pipelines | `src/pipelines/` | Deterministic ETL/transforms producing outputs |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV metadata + lineage |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` (**or repo-defined equivalent; not confirmed**) | Contracts + redaction + query services |
| UI | `web/` | React + Map UI, Focus Mode UX |
| Schemas | `schemas/` | JSON schemas + optional shapes |
| Tests | `tests/` | Unit/integration/contract tests |

### Expected file tree for this sub-area

> This is a **target layout** to keep styles predictable. Adjust to the repo’s actual UI stack.

~~~text
📁 web/
└── 📁 src/
    └── 📁 styles/
        ├── 📄 README.md                           # (this file)
        ├── 📄 tokens.css                          # design tokens as CSS variables (target; not confirmed)
        ├── 📄 theme.light.css                     # theme override (target; not confirmed)
        ├── 📄 theme.dark.css                      # theme override (target; not confirmed)
        ├── 📄 theme.high-contrast.css             # a11y theme (target; not confirmed)
        ├── 📄 reset.css                           # base reset/normalize (target; not confirmed)
        ├── 📄 globals.css                         # global element styles (target; not confirmed)
        ├── 📁 utilities/                          # small opt-in utilities (target; not confirmed)
        │   └── 📄 visually-hidden.css              # a11y helper (target; not confirmed)
        ├── 📁 components/                         # shared component style modules (target; not confirmed)
        │   └── 📄 <Component>.module.css           # example
        └── 📁 map/                                # map UI chrome styles (target; not confirmed)
            ├── 📄 map-chrome.css                   # panels/controls/overlays (target; not confirmed)
            └── 📄 attribution.css                  # attribution/license UI (target; not confirmed)
~~~

### Extension points checklist (for future work)

- [ ] Data: If UI styling depends on dataset-specific styling artifacts, ensure they are **versioned** and **referenced** (not inlined ad-hoc).
- [ ] Catalog: If datasets publish styles, consider linking them as catalog assets (STAC/DCAT) (**pattern may vary; not confirmed in repo**).
- [ ] Graph: No direct styling dependencies; UI should consume style references via API payloads where appropriate.
- [ ] APIs: If style references are served dynamically, define/extend an API contract (**not in this doc**).
- [ ] UI: Theme toggles, high-contrast mode, legend rendering, map layer toggles.
- [ ] Focus Mode: Ensure narrative/citation UI styling supports provenance display.
- [ ] Telemetry: Theme changes, contrast mode toggles, redaction notice display (recommended; schema/versioning **not confirmed in repo**).

## 🧭 Context

### Background

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Lineage and provenance are first-class so **Story Nodes and Focus Mode can only surface provenance-linked content**, and missing links should be caught via CI. The **API boundary is mandatory**: the UI never queries Neo4j directly; it consumes contracted API responses.

### Where “styles” fit

UI styling spans three distinct (and intentionally separated) concerns:

1. **UI chrome CSS** (this folder): typography/layout/controls/panels, Focus Mode readability, a11y affordances.
2. **Renderer styles** (MapLibre/Cesium): how polygons/lines/points are colored and labeled on the map.
3. **Legend + cartography metadata** (often dataset-owned): machine-readable legend definitions that the UI can display consistently.

### Map UI assumptions

- The frontend is expected to be an SPA under `web/` (React components, map view, story panels, search). (**not confirmed in repo**)  
- Map rendering may use MapLibre GL JS (2D) and optionally Cesium (3D). (**not confirmed in repo**)  
- A layer registry may exist as JSON configuration describing map layers (name, sources, sensitivity flags). (**not confirmed in repo**)

### Constraints / invariants

- **Determinism:** Token names and theme variables should be stable and version-controlled.
- **Accessibility:** UI must remain navigable and legible (keyboard, reduced motion, contrast).
- **Governance:** UI styling and UI-layer additions must not accidentally increase access to sensitive/restricted information (e.g., by enabling interaction/zoom that reveals sensitive locations).

## 🗺️ Diagrams

### UI styling flow (conceptual)

~~~mermaid
flowchart LR
  subgraph StyleArtifacts["Versioned style artifacts"]
    Tokens["Design tokens\n(CSS variables / JSON)"]
    Themes["Themes\n(light/dark/high-contrast)"]
    MapStyles["Map styles\n(MapLibre JSON + legend YAML)"]
  end

  Tokens --> CSS["CSS output\n(globals + modules)"]
  Themes --> CSS
  CSS --> UI["React UI components\n(map + panels + Focus Mode)"]

  MapStyles --> Map["MapLibre / Cesium renderers"]
  UI --> Focus["Focus Mode\n(narrative + citations + audit cues)"]
~~~

### CSS layering model (recommended)

~~~mermaid
flowchart TD
  Reset["reset / base"] --> Tokens["tokens (CSS vars)"]
  Tokens --> Theme["theme overrides"]
  Theme --> Globals["globals (element styles)"]
  Globals --> Components["component-scoped styles"]
  Components --> MapChrome["map chrome styles"]
~~~

## 🧠 Story Node & Focus Mode Integration

Focus Mode is an immersive UI view with the narrative alongside maps/timelines. In Focus Mode v3, content displayed must be provenance-linked, and any AI-generated elements must be clearly indicated.

**Style implications for Focus Mode:**

- Make citations visually distinct and consistently placed (e.g., inline citation chips + “provenance” panel styling).
- Ensure warning banners and redaction notices are highly visible (do not allow “pretty” themes to hide governance cues).
- Provide accessible typography defaults (line length, spacing, headings) for long-form reading.

### Optional: Story Node-driven UI controls (shape)

(Provided for styling context; actual Story Node schema is governed elsewhere.)

~~~yaml
focus_mode:
  focus_center: [ -98.0, 38.5 ]   # lon,lat
  focus_time: "1854-01-01/1861-12-31"
  focus_layers:
    - "trails_overview"
    - "settlements_points"
  ui_prefs:
    theme: "dark"
    high_contrast: false
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol check (front-matter present; required sections present; footer refs present)
- Style linting (if configured): CSS lint + formatting consistency (**not confirmed in repo**)
- Build/test gates (if configured): UI build, unit tests, and accessibility checks (**not confirmed in repo**)
- Contrast checks (recommended): enforce AA/AAA thresholds for key UI text (**not confirmed in repo**)
- Map style validation (recommended): validate MapLibre style JSON shape before shipping (**not confirmed in repo**)

### Reproduction (deterministic)

~~~bash
# Example placeholders — replace with repo-specific commands

# Lint styles (if configured)
# npm run lint:css

# Run UI a11y checks (if configured)
# npm run test:a11y

# Build UI
# npm run build
~~~

### Telemetry signals (recommended)

- `ui_theme_changed` (theme_id)
- `ui_high_contrast_toggled` (enabled)
- `focus_mode_entered` (entity_id)
- `focus_mode_redaction_notice_shown` (layer_id, method)

(Exact telemetry schemas/locations are **not confirmed in repo**.)

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Design token definitions | CSS/JSON | UI team | Naming conventions + review |
| Theme overrides | CSS | UI team | Contrast + a11y review |
| Map style packs | JSON + YAML | Data domains (recommended) | Schema/shape checks (recommended) |
| Layer registry | JSON | UI config (recommended) | Schema validation (recommended) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| UI tokens | CSS variables | `web/src/styles/tokens.css` (**not confirmed**) | Naming + review |
| UI themes | CSS variables | `web/src/styles/theme.*.css` (**not confirmed**) | Contrast/a11y checks |
| UI chrome styles | CSS | `web/src/styles/**` | Lint + visual review |
| Legend UI render | UI component | `web/src/**` (**not confirmed**) | Must match legend YAML contract (if adopted) |

### Sensitivity & redaction

- UI styles must not embed secrets, private URLs, or internal-only endpoints.
- Avoid styling patterns that could “hide” access-control indicators (e.g., low-contrast warning banners).
- If a dataset/layer is sensitive, ensure the UI has a clear visual representation of:
  - restricted visibility,
  - generalization applied,
  - redaction status.

## 🌐 STAC, DCAT & PROV Alignment

This styles area does **not** produce STAC/DCAT/PROV directly, but it must align with how KFM publishes and links artifacts:

- **If datasets publish a canonical visualization style** (recommended), treat style packs as **first-class artifacts**:
  - Link them from dataset metadata (e.g., STAC collection/assets) (**pattern varies; not confirmed in repo**).
  - Include a legend definition so the UI can render consistent legends across clients.

- **PROV:** If a style is generated or converted (e.g., Mapbox → MapLibre), record a provenance activity (preferred under `data/prov/**` or `mcp/runs/**`; exact convention **not confirmed in repo**).

## 🧱 Architecture

### Principles

- **Token-first:** Use named design tokens; avoid “magic” colors/spacings scattered across components.
- **Scoped by default:** Prefer component-scoped styles; keep global CSS minimal and intentional.
- **Accessible by default:** Always-visible focus states; reduced motion support; readable typography.
- **Deterministic and diffable:** Style changes should be reviewable in PRs and stable across environments.

### Design tokens

**Recommendation:** Use CSS custom properties as the primary token interface.

- Prefix all tokens with `--kfm-` (e.g., `--kfm-color-text`, `--kfm-space-2`).
- Use `rem` for typography/spacing where practical.
- Keep z-indexes tokenized to avoid collisions.

Example token set (illustrative):

~~~css
:root {
  --kfm-color-bg: #ffffff;
  --kfm-color-text: #111111;
  --kfm-color-accent: #1f6feb;

  --kfm-font-sans: system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
  --kfm-font-mono: ui-monospace, SFMono-Regular, Menlo, monospace;

  --kfm-space-1: 0.25rem;
  --kfm-space-2: 0.5rem;
  --kfm-space-3: 0.75rem;
  --kfm-space-4: 1rem;

  --kfm-z-base: 0;
  --kfm-z-overlay: 100;
  --kfm-z-modal: 1000;
}
~~~

### Theming

- Implement themes as **variable overrides**, not duplicated CSS rules.
- Support user preferences:
  - `prefers-color-scheme` (optional)
  - `prefers-reduced-motion` (required)
  - high contrast (recommended)

Example (illustrative):

~~~css
[data-theme="dark"] {
  --kfm-color-bg: #0b0f14;
  --kfm-color-text: #e6edf3;
}
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
~~~

### Component styling conventions

- Prefer:
  - CSS Modules (e.g., `<Component>.module.css`) (**not confirmed in repo**), or
  - a consistent component style colocation pattern if using a different approach (**not confirmed in repo**).
- Avoid:
  - deep selector chains (`.a .b .c .d`)
  - global element overrides beyond `globals.css`
  - inline styles except for truly dynamic values

### Map UI styling vs map renderer styles

**Key rule:** CSS styles UI chrome; **MapLibre/Cesium styles are renderer-driven**.

- Use CSS for:
  - map container sizing and layout
  - overlays (legend, attribution, scale bar, layer toggles)
  - Focus Mode panels and narrative typography
- Use MapLibre/Cesium styles for:
  - feature fills/strokes/labels
  - zoom-dependent styling rules
  - symbol placement

### Dataset “style pack” pattern (example)

A dataset may ship an additive “styles pack” to ensure deterministic styling across clients:

- Mapbox style JSON (optional)
- MapLibre style JSON
- Legend YAML
- Scale-dependent generalization rules (for tile production)

(Exact locations depend on domain module layout; this doc only defines how UI should *consume* these artifacts.)

### Accessibility requirements (styling)

- Always provide visible focus indicators (`:focus-visible`) for keyboard navigation.
- Ensure minimum contrast for:
  - body text
  - interactive controls
  - warning/error banners
- Avoid “information by color alone” (e.g., add patterns/icons/labels where needed).
- Respect reduced motion user preferences.

### Performance guidelines

- Keep selectors shallow and fast.
- Prefer transforms for animations (when motion is enabled).
- Avoid heavy box-shadows and expensive filters on frequently updating UI elements.

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when changes could expand access to sensitive/restricted information, including **adding a new UI layer that could reveal sensitive locations by interaction/zoom**.

### CARE / sovereignty considerations

- If UI styling affects how culturally sensitive or sovereignty-controlled information is displayed:
  - ensure authority-to-control expectations are respected (see sovereignty policy),
  - prefer coarse/aggregate public presentation when required,
  - make redaction/generalization visually explicit.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing
- Prohibited:
  - generating new policy
  - inferring sensitive locations (directly or indirectly)
- AI may propose changes, but **human review** must approve any classification/sensitivity implications.

### PR checklist (styling)

- [ ] No new UI affordance enables deeper inspection of restricted layers without review (e.g., zoom-to, hover-tooltips on restricted points)
- [ ] Focus Mode warnings/citations remain visible in all themes
- [ ] Reduced motion honored
- [ ] Contrast checked for key UI surfaces
- [ ] No secrets/PII embedded in CSS or static assets

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-25 | Initial styles README (tokens/theming/CSS architecture + map style integration guidance) | TBD | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
