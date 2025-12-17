---
title: "Accessibility Pattern — Keyboard Focus and Navigation"
path: "docs/accessibility/patterns/keyboard-focus-and-navigation.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Pattern"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:keyboard-focus-and-navigation:v1.0.0"
semantic_document_id: "kfm-accessibility-pattern-keyboard-focus-and-navigation-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:keyboard-focus-and-navigation:v1.0.0"
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

# Accessibility Pattern — Keyboard Focus and Navigation

## 📘 Overview

### Purpose
- Define how keyboard focus and navigation must work across the KFM UI (including map UI, panels, Focus Mode, and Story Node reading surfaces).
- Prevent “hidden data leakage” via the accessibility tree (e.g., offscreen/hidden UI accidentally reachable via Tab or screen readers), aligning to the UI subsystem contract in `docs/MASTER_GUIDE_v12.md`.

### Scope
| In Scope | Out of Scope |
|---|---|
| Tab order, focus visible rules, focus restoration, skip links, keyboard operation for custom widgets, modal/drawer focus management, map keyboard entry/exit patterns | Full visual design system specs, complete screen reader copywriting, mobile gesture design, color/contrast policy (except focus visibility requirements tied to keyboard use) |

### Audience
- Primary: Frontend engineers (React/UI), UI/UX designers, QA/test engineers
- Secondary: Security/governance reviewers (for gating + “no hidden data leakage”), content editors (Focus Mode/Story Nodes)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Focus order**: The order elements receive focus via Tab/Shift+Tab.
  - **Focus restoration**: Returning focus to the element that opened a dialog/panel.
  - **Keyboard trap**: Focus cannot escape a region using keyboard controls.
  - **Roving tabindex**: Composite widget pattern where one child is tabbable and arrows move focus.
  - **Inert**: A state where an element subtree is removed from sequential focus and interaction (implementation may vary by browser/stack).
  - **Focus Mode**: KFM context surface that must only present provenance-linked content (`docs/MASTER_GUIDE_v12.md`).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| KFM Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core | UI contract includes a11y + “no hidden data leakage” |
| Accessibility patterns index | `docs/accessibility/patterns/README.md` | UI | Index + rules for adding new patterns |
| Pattern template | `docs/accessibility/patterns/pattern-template.md` | UI | Local authoring template for new patterns |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review gates and approvals |
| Ethics | `docs/governance/ETHICS.md` | Governance | Accessibility is an ethics concern |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | Governance | Do not leak restricted locations via a11y surfaces |
| Frontend source | `web/` | UI | Implementation location (React map UI) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Requirements are testable (clear acceptance criteria + keyboard steps)
- [ ] Examples include both “what to do” and “what not to do”
- [ ] Validation steps listed and repeatable (manual + automated)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (including accessibility-tree leakage)

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/patterns/keyboard-focus-and-navigation.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | A11y guidance and standards |
| Pattern library | `docs/accessibility/patterns/` | Individual a11y patterns + index |
| Frontend implementation | `web/` | React + map UI code |
| UI/UX design docs | `docs/design/` | Design decisions (including a11y expectations) |
| Tests | `tests/` | Automated test suites (exact tooling not confirmed in repo) |
| Standards | `docs/standards/` | Governed standards (e.g., Markdown protocol) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 accessibility/
    └── 📁 patterns/
        ├── 📄 README.md
        ├── 📄 pattern-template.md
        └── 📄 keyboard-focus-and-navigation.md
~~~

## 🧭 Context

KFM’s UI is map-centric and panel-heavy (layers, filters, story panels, Focus Mode). These are the common failure modes this pattern addresses:

- **Lost focus**: opening a panel/modal moves focus nowhere (or to the page start), leaving keyboard users stranded.
- **Unreachable actions**: custom controls (layer toggles, time sliders, map popups) can’t be operated without a mouse.
- **Keyboard traps**: focus enters the map canvas or a panel and cannot escape.
- **Invisible focus**: UI suppresses outlines or focus ring is not visually apparent.
- **Accessibility-tree leakage**: “hidden” or gated UI is visually hidden but still keyboard-focusable or screen-reader discoverable, violating the UI contract (“no hidden data leakage”) and potentially exposing restricted content.

### Security + sensitivity
Even when `sensitivity: public`, UI behavior must not allow restricted information to appear in:
- Offscreen DOM nodes that remain tabbable
- Hidden popovers still present in the accessibility tree
- Live regions that announce sensitive coordinates or location details

If a panel/layer is gated by permissions, it must also be gated in the accessibility tree and tab order.

## 🗺️ Diagrams

~~~mermaid
sequenceDiagram
  participant User as Keyboard User
  participant UI as KFM UI
  participant Panel as Focus Mode Panel/Dialog

  User->>UI: Activate "Open Focus Mode" control (Enter/Space)
  UI->>Panel: Render + make visible
  UI->>Panel: Move focus to panel heading or first actionable control
  Note over Panel: Focus is trapped only if modal behavior is intended
  User->>Panel: Navigate content (Tab/Shift+Tab, arrows where applicable)
  User->>Panel: Close (Esc or Close button)
  Panel-->>UI: Unmount/hide
  UI-->>User: Restore focus to opener control
~~~

## 📦 Data & Metadata

### Inputs and outputs (UI-level “data”)
| Category | Input | Expected output behavior |
|---|---|---|
| Keyboard navigation | Tab / Shift+Tab | Predictable focus order; never enters hidden/gated UI |
| Activation | Enter / Space | Activates the focused control (buttons, toggles, list items with button semantics) |
| Escape | Esc | Closes dialogs/popovers where applicable; exits “map keyboard mode” if enabled |
| Directional nav | Arrow keys | Moves within composite widgets (menus, tabs, toolbars) using roving tabindex |
| Map interactions | Arrow keys, +/- | Only when map is intentionally “entered” for keyboard interaction |

### Provenance surfaces
If the UI presents provenance links (dataset IDs, source citations, STAC assets), those must be:
- Real links (`<a href=...>`) with accessible names
- Reachable by keyboard in a sensible order
- Not duplicated/hidden in a way that creates confusing extra tab stops

## 🌐 STAC, DCAT & PROV Alignment

This pattern does not define STAC/DCAT/PROV schemas. However, it governs **how provenance-linked UI is accessed**:

- When a Story Node or Focus Mode view presents citations, dataset identifiers, or provenance references, those elements must be keyboard reachable and focusable.
- If provenance references are gated (restricted locations, sensitive site details), they must not be present in the accessibility tree for unauthorized contexts.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)
| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

(See: `docs/MASTER_GUIDE_v12.md`.)

### Key components (overview)

| Component | Responsibilities | Keyboard expectations |
|---|---|---|
| Global nav / header | Site navigation, global actions | Includes skip links; logical Tab order; visible focus |
| Layer panel | Toggle/adjust layers, filters | Fully operable by keyboard; no custom “div button” |
| Map viewport (MapLibre/Cesium) | Spatial navigation/selection | Keyboard access via explicit entry/exit; no traps |
| Popovers/tooltips | Context actions, details | Proper focus management; closeable; not tabbable when hidden |
| Focus Mode (panel/dialog) | Provenance-linked narrative + evidence | Focus moved on open; restored on close; predictable reading order |

### Interfaces / contracts (what connects to what)

- **DOM order is the contract** for Tab order. Do not reorder focus with positive `tabindex`.
- **Visibility and interactivity must match**:
  - If visually hidden, must also be removed from sequential focus and interaction.
  - If gated by authorization, must be absent or inert for unauthorized users (not just “display:none” on the visible layer toggle).

### Pattern requirements

#### 1) Baseline keyboard support
- Every interactive UI element must be reachable and operable using keyboard only.
- Prefer native elements:
  - Use `<button>` for actions, `<a>` for navigation, `<input type="checkbox">` for toggles, `<input type="range">` for sliders.
- Never rely on `onClick` alone—ensure keyboard activation works via semantics (or explicit handlers if truly custom).

#### 2) Focus order rules
- Tab order must follow the visual and reading order.
- Do not use positive `tabindex` (e.g., `tabindex="1"`). If you need programmatic focus, use `tabindex="-1"` on the target element and focus it programmatically.
- Remove disabled/unavailable controls from tab order (native `disabled` works for form controls; otherwise ensure non-focusable).

#### 3) Focus visibility
- Do not remove focus outlines globally.
- Use `:focus-visible` for focus ring behavior so mouse users are not distracted while keyboard users always see focus.

~~~css
/* Example only — bind to existing design tokens if available */
:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 2px;
}
~~~

> Note: The exact focus styling/tokenization is not confirmed in repo; align to existing `web/` styles/design tokens if present.

#### 4) Skip links + landmarks
Provide skip links at the top of the page/app shell:
- “Skip to main content”
- “Skip to map”
- “Skip to filters/layers” (if present)

~~~html
<a class="skip-link" href="#main">Skip to main content</a>
<a class="skip-link" href="#map">Skip to map</a>
~~~

Use semantic landmarks (`<header>`, `<nav>`, `<main id="main">`, `<aside>`), or equivalent roles.

#### 5) Dialogs, modals, and popovers
When a dialog/modal opens:
- Move focus into the dialog (typically the heading, or first actionable element).
- If modal: trap focus within the dialog while open.
- Provide an accessible close button.
- Esc closes (unless there is a documented exception).

When closing:
- Restore focus to the element that opened it.

~~~js
// Pseudocode for focus restoration
let lastActiveElement = null;

function openDialog() {
  lastActiveElement = document.activeElement;
  // render dialog...
  // focus dialog heading or first control
}

function closeDialog() {
  // unmount dialog...
  if (lastActiveElement && lastActiveElement.focus) lastActiveElement.focus();
}
~~~

#### 6) Side panels and drawers (non-modal)
If a panel is non-modal (the rest of the UI remains usable):
- Do not trap focus.
- Ensure the panel is reachable by Tab and has a clear heading.
- If the panel is collapsed/hidden, it must not contain tabbable elements.

#### 7) Hidden UI must not be focusable
If UI is hidden (collapsed drawer, inactive tab panel, closed popover), ensure it is:
- Removed from sequential focus and pointer interaction
- Removed from the accessibility tree if appropriate

Implementation strategies (choose one consistent approach across the app):
- Unmount hidden content (preferred for popovers/modals where feasible)
- Apply `hidden` / `display:none` (removes from accessibility tree)
- Use `inert` where supported (or a framework equivalent) plus `aria-hidden="true"` for non-interactive hidden subtrees

#### 8) Composite widgets: roving tabindex
For toolbars, tablists, menus, listboxes, and similar composite widgets:
- One child is tabbable at a time (`tabindex="0"`)
- Arrow keys move focus among children
- Tab exits the widget (do not trap)

~~~html
<div role="toolbar" aria-label="Map tools">
  <button tabindex="0">Select</button>
  <button tabindex="-1">Measure</button>
  <button tabindex="-1">Export</button>
</div>
~~~

#### 9) Map keyboard entry/exit (MapLibre/Cesium)
Because the map surface is canvas/WebGL, keyboard support must be intentional and discoverable:

- Provide a focusable “Enter map” control (button) adjacent to the map region.
- When the user “enters map mode”:
  - Move focus to the map container
  - Enable keyboard map controls (pan/zoom) if supported by the map library
  - Provide a visible hint (and accessible description) of available keys
- Provide “Exit map” (Esc and/or button) that returns focus to a stable control (e.g., “Enter map” button or next UI section).

Minimum expectation:
- Keyboard users can reach map-adjacent content (layers list, feature lists, popups) without being forced to interact with the map canvas.

Recommended (where feasible):
- Provide an accessible list/table representation of features in view, enabling keyboard selection that also updates the map highlight.

#### 10) Preventing keyboard traps
- Always ensure there is a clear way to move focus away from any region using Tab/Shift+Tab.
- If a trap is intentional (modal dialog), it must be implemented correctly and escapable (close button + Esc).

### Extension points checklist (for future work)
- [ ] UI: standardize skip links in a shared app shell component
- [ ] UI: standardize dialog/panel focus management in a single component API
- [ ] UI: define a “map keyboard mode” contract (enter/exit, shortcuts, help affordance)
- [ ] UI: add automated regression tests for focus restoration and hidden content tabbability
- [ ] Telemetry: add optional signal for “keyboard trap detected” (if telemetry schema supports it)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode open/close must follow this doc’s focus rules (move focus in, restore focus out).
- Story Node reading experiences must preserve:
  - Logical reading order (headings → paragraphs → citations → evidence)
  - Keyboard access to provenance references
  - No focusable hidden panels containing restricted content

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (as governed elsewhere).
- This pattern adds: those provenance links must be reachable and usable by keyboard.

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
- [ ] UI keyboard walkthrough (manual): Tab/Shift+Tab through main flows (map, layers, Focus Mode, popovers)
- [ ] Automated accessibility checks where available (tooling not confirmed in repo)
- [ ] UI schema checks (layer registry) where applicable
- [ ] Security and sovereignty checks (as applicable), including “no hidden data leakage” via a11y tree

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) install deps (frontend)
# cd web && npm ci

# 2) run lint/typecheck
# npm run lint
# npm run typecheck

# 3) run unit tests
# npm test

# 4) run e2e/a11y checks (if configured)
# npm run test:e2e
# npm run test:a11y
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| keyboard_trap_events | UI runtime | `docs/telemetry/` + `schemas/telemetry/` |
| focus_restore_failures | UI runtime | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI changes that introduce new focus behavior (dialogs, map interactions, new panels) require:
  - Frontend review
  - Accessibility review (role may be a designated maintainer; exact assignment not confirmed in repo)
- Any change that could alter how gated/sensitive content is exposed must be reviewed against:
  - `docs/governance/ROOT_GOVERNANCE.md`
  - `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations
- Do not expose restricted locations through:
  - Focusable hidden elements
  - Screen-reader-visible DOM that is visually hidden
  - Live announcements containing restricted coordinates
- If content is redacted/generalized, ensure the UI does not preserve the original sensitive value anywhere in accessible labels or hidden text.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use (see front-matter).
- This pattern must not be used to infer sensitive locations or generate governance policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial pattern | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
