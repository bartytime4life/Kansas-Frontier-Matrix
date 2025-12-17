---
title: "KFM Accessibility Tokens"
path: "docs/accessibility/tokens.md"
version: "v1.0.0-draft"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Standard"
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

doc_uuid: "urn:kfm:doc:accessibility:tokens:v1.0.0-draft"
semantic_document_id: "kfm-accessibility-tokens-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:accessibility:tokens:v1.0.0-draft"
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

# KFM Accessibility Tokens

## 📘 Overview

### Purpose
- Define a governed **accessibility-oriented design token set** for KFM’s UI (map, timeline, Story Nodes, Focus Mode panels).
- Standardize **naming**, **token layers**, and **minimum accessibility constraints** (contrast, focus indication, target size, reduced motion).
- Ensure component implementations do not hard-code UI decisions that should remain adjustable for accessibility and theming.

### Scope
| In Scope | Out of Scope |
|---|---|
| Token taxonomy (primitive → semantic → component) | Full component ARIA markup and interaction logic (see patterns) |
| Token naming conventions + formats (CSS vars / JSON) | Visual brand decisions (exact palette, typography choices) |
| A11y-critical token groups: color/contrast, focus, target size, typography, motion | Map style authoring for data layers (cartography spec) |
| Requirements + validation checklist for token changes | Backend/API contracts |

### Audience
- Primary: Frontend engineers, UI/UX designers, QA/a11y reviewers
- Secondary: Product owners, content authors (Story Node authors who need accessible content display defaults)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Design token**: Named value used consistently across UI.
  - **Primitive token**: Raw values (e.g., a specific spacing step or base color).
  - **Semantic token**: Meaning-based token (e.g., “text”, “surface”, “focus-ring”) mapped to primitives per theme.
  - **Component token**: Component-scoped override (e.g., timeline thumb size).
  - **Focus indicator**: Visual styling for keyboard focus (outline/ring).
  - **Reduced motion**: Styling behavior when users prefer less motion.
  - **Forced colors / high contrast**: OS/browser overrides to enforce strong contrast.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Accessibility checklist | `docs/accessibility/checklist.md` | UX/QA | Cross-check requirements for PR review |
| Timeline controls pattern | `docs/accessibility/patterns/timeline-controls.md` | Frontend | Keyboard + screen reader behavior |
| Story Node content pattern | `docs/accessibility/patterns/story-node-content.md` | Frontend | Headings/links/citations structure |
| Accessibility tokens (this doc) | `docs/accessibility/tokens.md` | Frontend | Governed token catalog + constraints |
| Token source-of-truth (implementation) | `web/` | Frontend | Exact path TBD; must be single canonical source |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Token taxonomy + naming conventions defined
- [ ] A11y-critical token groups defined (color/contrast, focus, target size, typography, motion)
- [ ] Timeline + Story Node component token coverage included
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/tokens.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Accessibility docs | `docs/accessibility/` | Checklist, tokens, patterns |
| Frontend | `web/` | React/map UI, styles, components |
| Governance | `docs/governance/` | Policy + sovereignty constraints |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 accessibility/
    ├── 📄 checklist.md
    ├── 📄 tokens.md
    └── 📁 patterns/
        ├── 📄 timeline-controls.md
        └── 📄 story-node-content.md
~~~

## 🧭 Context

### Background
KFM’s UI includes interaction-heavy surfaces (maps, layers, timelines, Story Nodes, Focus Mode dashboards). Accessibility issues often come from inconsistent styling decisions (insufficient contrast, invisible focus rings on map canvas, small hit targets in controls). Centralizing these decisions into tokens:
- improves consistency,
- enables systematic testing,
- supports theming and user preference modes (reduced motion / forced colors),
- reduces regressions when components evolve.

### Assumptions
- KFM’s UI styling can consume a **single source of truth** for tokens (CSS custom properties and/or generated tokens).
- The UI will support keyboard navigation and screen reader usage across interactive components (map controls, timeline, Story Node panels).

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes system contracts via APIs (no direct graph dependency).
- Accessibility styling must not become a workaround for governance constraints:
  - Sensitive/sovereign content handling is not solved by styling alone.
  - Do not rely on color-only cues to indicate sensitive classifications; always pair with text/iconography.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical token implementation file in `web/`? | Frontend | TBD |
| Is theming runtime (CSS vars) or build-time (compiled tokens) the target? | Frontend | TBD |
| Which baseline palettes (light/dark/high-contrast) are considered supported themes? | UX | TBD |
| Do we require WCAG AA for all UI surfaces, including map canvas overlays? | Governance/UX | TBD |

### Future extensions
- Token build pipeline (e.g., JSON → CSS vars → TS types) with CI validation.
- Explicit “High Contrast” theme tokens and “Reduced Motion” theme overrides.
- Tokenized map-style rules for common layer semantics (selected/hovered/focused features).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Token Source of Truth<br/>(CSS vars / JSON tokens)] --> B[Build or Runtime Theme Layer]
  B --> C[UI Components<br/>Map / Timeline / Panels]
  C --> D[User Interaction<br/>Keyboard / Screen Reader / Pointer]
  D --> E[Accessibility Outcomes<br/>Contrast / Focus / Target Size / Motion]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI
  participant Tokens as Theme Tokens
  User->>UI: Enables reduced motion / high contrast
  UI->>Tokens: Apply theme override tokens
  Tokens-->>UI: Updated semantic & component token values
  UI-->>User: Motion reduced; focus + contrast maintained
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Accessibility requirements | Text | `docs/accessibility/*` | Checklist review |
| Theme primitives | CSS/JSON | `web/` | Contrast + focus tests |
| Component needs | Tickets/PRs | Repo issues/PRs | UI review + QA |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Token catalog standard | Markdown | `docs/accessibility/tokens.md` | This doc |
| Token implementation | CSS/JSON/TS | `web/` | TBD (must be documented) |
| A11y verification artifacts | Notes/test outputs | `mcp/runs/` or CI logs | TBD |

### Sensitivity & redaction
- Tokens may define styling for “restricted/sensitive” UI badges or warning banners, but **styling must not reveal protected locations**.
- When sensitive locations are generalized/blurred, ensure UI communicates this accessibly (not by color alone).

### Quality signals
- Contrast meets target levels for text and non-text UI (where applicable).
- Focus indicators are highly visible and not obscured by overlays.
- Minimum pointer target sizes are met for interactive controls.
- Motion is reduced or disabled when user preferences request it.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not directly applicable (tokens are UI-level), but tokenized UI must support consistent display of STAC-linked asset metadata (e.g., provenance badges/links).

### DCAT
- Not directly applicable.

### PROV-O
- Not directly applicable, except that UI presentation must maintain the visibility and readability of provenance (“show sources”) affordances.

### Versioning
- Token names are contracts for the UI. Renames are breaking changes for components; treat them as “API-like” changes:
  - Deprecate before removal when feasible.
  - Keep a changelog in this document.

---

## 🧩 Token Model

### Token layers
1) **Primitive tokens (lowest level)**
   - Raw steps (spacing scale, typography scale, base colors).
   - Should rarely be referenced directly in components.

2) **Semantic tokens (preferred for most usage)**
   - Meaning-based tokens mapped to primitives per theme.
   - Components should generally only consume semantic tokens.

3) **Component tokens**
   - Limited overrides for specific components when semantic tokens are insufficient.
   - Must be documented and kept minimal to avoid divergence.

### Naming conventions

#### CSS custom property naming
- Prefix: `--kfm-`
- Use kebab-case.
- Suggested structure:
  - `--kfm-prim-<category>-<name>`
  - `--kfm-sem-<category>-<name>`
  - `--kfm-comp-<component>-<name>`

#### JSON token naming (optional)
- `kfm.prim.<category>.<name>`
- `kfm.sem.<category>.<name>`
- `kfm.comp.<component>.<name>`

### Units and scaling
- Use `rem` for font sizes and spacing to support browser zoom and user font settings.
- Use `px` only when needed for pixel-precise rendering (e.g., hairline borders) and ensure those are not the only cues for focus/selection.

---

## 🎛️ Accessibility Token Catalog

### 1) Color & contrast tokens (semantic)
| Token | Description | Notes / constraints |
|---|---|---|
| `--kfm-sem-color-bg` | App background | Must support text contrast with `--kfm-sem-color-text` |
| `--kfm-sem-color-surface` | Panel / card background | Used for Story Node panels, tooltips |
| `--kfm-sem-color-text` | Primary text | Meet minimum contrast requirements vs bg/surface |
| `--kfm-sem-color-text-muted` | Secondary text | Must remain readable; avoid using for critical info |
| `--kfm-sem-color-border` | Non-text boundary | Must meet non-text contrast where required |
| `--kfm-sem-color-link` | Link color | Must remain distinguishable beyond color (underline recommended in content) |
| `--kfm-sem-color-focus` | Focus indicator color | Must be high contrast against surrounding pixels |
| `--kfm-sem-color-danger` / `warning` / `success` / `info` | Status colors | Do not rely on color alone—pair with icon + text |

**Non-color cues (required):**
- Use shape, underline, text labels, and icons to convey state.
- Never encode sensitive classification only via color.

### 2) Focus indicator tokens
| Token | Description | Notes / constraints |
|---|---|---|
| `--kfm-sem-focus-ring-width` | Focus outline width | Set to a visually strong minimum (avoid 1px-only) |
| `--kfm-sem-focus-ring-offset` | Outline offset | Ensure focus ring not hidden by borders/shadows |
| `--kfm-sem-focus-ring-style` | Outline style | Prefer solid over dotted for clarity |
| `--kfm-sem-focus-ring-color` | Focus color | Must remain visible on map + panels |
| `--kfm-sem-focus-shadow` | Optional focus glow | Useful on complex backgrounds (map tiles) |

### 3) Pointer target size tokens
| Token | Description | Notes / constraints |
|---|---|---|
| `--kfm-sem-target-min-size` | Minimum interactive target size | Applies to buttons, icon buttons, thumbs/handles |
| `--kfm-sem-target-padding` | Padding to reach min size | Useful for small icons |
| `--kfm-sem-target-gap` | Minimum spacing between targets | Reduces mis-taps on dense controls |

### 4) Typography & readability tokens
| Token | Description | Notes / constraints |
|---|---|---|
| `--kfm-sem-font-size-base` | Base text size | Use `rem`; do not hard-lock user zoom |
| `--kfm-sem-line-height-body` | Body line height | Avoid cramped line-height |
| `--kfm-sem-letter-spacing-body` | Body letter spacing | Avoid negative spacing that harms readability |
| `--kfm-sem-font-weight-body` | Default weight | Ensure legibility on low-contrast screens |
| `--kfm-sem-text-max-width` | Readable line length cap | Use for narrative panels/Story Node content |

### 5) Motion & animation tokens
| Token | Description | Notes / constraints |
|---|---|---|
| `--kfm-sem-motion-duration-fast` | Short transitions | Must be overridden in reduced motion |
| `--kfm-sem-motion-duration-medium` | Standard transitions | Must be overridden in reduced motion |
| `--kfm-sem-motion-duration-slow` | Long transitions | Avoid for essential interactions |
| `--kfm-sem-motion-ease-standard` | Easing curve | Keep consistent |
| `--kfm-sem-motion-reduced-multiplier` | Multiplier for reduced motion | 0–0.2 recommended; can become 0 |

---

## 🧱 Component Token Coverage

### Timeline controls (component tokens)
| Token | Description | Why it matters |
|---|---|---|
| `--kfm-comp-timeline-track-height` | Track thickness | Non-text contrast and usability |
| `--kfm-comp-timeline-thumb-size` | Thumb/handle size | Pointer target size + visibility |
| `--kfm-comp-timeline-tick-label-size` | Tick label size | Readability |
| `--kfm-comp-timeline-focus-ring-color` | Focus ring on thumb | Keyboard visibility |
| `--kfm-comp-timeline-focus-ring-offset` | Prevent ring clipping | Avoid obscured focus |

### Story Node content (component tokens)
| Token | Description | Why it matters |
|---|---|---|
| `--kfm-comp-story-heading-size` | Heading scale | Semantic structure; readability |
| `--kfm-comp-story-body-size` | Body scale | Reading comfort |
| `--kfm-comp-story-link-style` | Link decoration | Must be distinguishable beyond color |
| `--kfm-comp-story-citation-badge-bg` | Citation badge background | Contrast for provenance links |
| `--kfm-comp-story-citation-badge-text` | Citation badge text | Contrast and legibility |
| `--kfm-comp-story-callout-border` | Callout emphasis | Non-color cue for emphasis |

---

## 🧪 Example (Non-Normative) Implementation

> This section is illustrative only. The canonical implementation location in `web/` must be defined and kept as the single source of truth.

### Example CSS vars
~~~css
:root {
  /* Semantic: core surfaces */
  --kfm-sem-color-bg: #ffffff;
  --kfm-sem-color-surface: #f6f7f9;
  --kfm-sem-color-text: #111111;
  --kfm-sem-color-text-muted: #3d3d3d;
  --kfm-sem-color-border: #2b2b2b;
  --kfm-sem-color-link: #0b57d0;
  --kfm-sem-color-focus: #0b57d0;

  /* Focus */
  --kfm-sem-focus-ring-width: 3px;
  --kfm-sem-focus-ring-offset: 2px;
  --kfm-sem-focus-ring-style: solid;
  --kfm-sem-focus-ring-color: var(--kfm-sem-color-focus);
  --kfm-sem-focus-shadow: 0 0 0 2px rgba(11, 87, 208, 0.25);

  /* Target size */
  --kfm-sem-target-min-size: 24px;
  --kfm-sem-target-padding: 8px;
  --kfm-sem-target-gap: 8px;

  /* Typography */
  --kfm-sem-font-size-base: 1rem;
  --kfm-sem-line-height-body: 1.5;
  --kfm-sem-text-max-width: 70ch;

  /* Motion */
  --kfm-sem-motion-duration-fast: 120ms;
  --kfm-sem-motion-duration-medium: 200ms;
  --kfm-sem-motion-duration-slow: 320ms;
  --kfm-sem-motion-ease-standard: ease;
  --kfm-sem-motion-reduced-multiplier: 0.0;

  /* Component: timeline */
  --kfm-comp-timeline-track-height: 6px;
  --kfm-comp-timeline-thumb-size: 24px;
  --kfm-comp-timeline-tick-label-size: 0.875rem;
  --kfm-comp-timeline-focus-ring-color: var(--kfm-sem-focus-ring-color);
  --kfm-comp-timeline-focus-ring-offset: var(--kfm-sem-focus-ring-offset);
}

/* Reduced motion override */
@media (prefers-reduced-motion: reduce) {
  :root {
    --kfm-sem-motion-duration-fast: 0ms;
    --kfm-sem-motion-duration-medium: 0ms;
    --kfm-sem-motion-duration-slow: 0ms;
  }
}
~~~

### Focus ring usage (example)
~~~css
.kfm-focusable:focus-visible {
  outline-width: var(--kfm-sem-focus-ring-width);
  outline-style: var(--kfm-sem-focus-ring-style);
  outline-color: var(--kfm-sem-focus-ring-color);
  outline-offset: var(--kfm-sem-focus-ring-offset);
  box-shadow: var(--kfm-sem-focus-shadow);
}
~~~

### Forced colors / high-contrast mode (example)
~~~css
@media (forced-colors: active) {
  .kfm-focusable:focus-visible {
    outline: 2px solid CanvasText;
    outline-offset: 2px;
    box-shadow: none;
  }
}
~~~

---

## ✅ Validation Steps (Repeatable)

1) **Contrast checks**
   - Verify text vs background/surface meets contrast thresholds for all core surfaces.
   - Verify non-text controls (borders, focus indicators, track/thumb) remain visible.

2) **Keyboard focus checks**
   - Navigate the UI using only keyboard:
     - Map controls, timeline slider, Story Node panel links/buttons.
   - Confirm focus is always visible and not obscured by overlays.

3) **Pointer target checks**
   - Inspect common icon buttons and slider thumbs:
     - Ensure targets meet minimum size and have adequate spacing.

4) **Reduced motion**
   - Enable reduced motion at OS/browser level and confirm:
     - Timeline transitions, panel animations, map layer transitions reduce/stop.

5) **Forced colors**
   - Test forced colors/high-contrast mode and confirm:
     - Focus indicator is visible.
     - Text remains readable and interactive controls are distinguishable.

---

## 🧾 Change log
| Date | Version | Change |
|---|---|---|
| 2025-12-17 | v1.0.0-draft | Initial governed draft for accessibility tokens |


---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`