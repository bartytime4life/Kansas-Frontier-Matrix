---
title: "Modal and Side Panel (Accessibility Pattern)"
path: "docs/accessibility/patterns/modal-and-sidepanel.md"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:modal-and-sidepanel:v1.0.0"
semantic_document_id: "kfm-accessibility-patterns-modal-and-sidepanel-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:modal-and-sidepanel:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:3213be6768f59c57af3fbed11104f1b5f97b729543646d9a2cdedf98cc7cffd3"
---

# Modal and Side Panel

## 📘 Overview

### Purpose

- Define accessible, testable UI patterns for **modals** (dialogs/alert dialogs) and **side panels** (drawers) in the KFM React/Map UI (`web/`).
- Govern the **interaction contract** for overlays: focus management, keyboard support, screen-reader semantics, dismiss behavior, and reduced-motion requirements.
- Reduce the risk of overlays becoming “visual-only” (mouse-only, unreadable to assistive tech, or trapping users).

### Scope

| In Scope | Out of Scope |
|---|---|
| Modal dialogs (blocking overlays): open/close, focus trap, return focus | Defining new REST/GraphQL endpoints (use API Contract Extension template) |
| Alert dialogs (destructive/critical confirmations) | Authoring Story Nodes (use Story Node template) |
| Side panels/drawers (modal and non-modal variants) | Tooltips and small popovers that do not require focus management |
| Scroll locking and background interaction suppression | Content strategy, copywriting, or visual design polish |
| Reduced motion rules for overlay transitions | Map rendering performance tuning unrelated to a11y |
| Overlay stacking rules (modal-in-modal, modal over sidepanel) | Creating/curating datasets (ETL + catalogs) |

### Audience

- Primary: Frontend engineers implementing overlays in `web/`
- Secondary: UX/design contributors, QA/a11y reviewers, governance/security reviewers (data leakage + sovereignty)

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Modal**: an overlay that blocks interaction with the rest of the page until dismissed.
  - **Dialog**: a container presenting information and/or controls; may be modal or non-modal.
  - **Alert dialog**: a dialog requiring immediate user attention/decision (often destructive confirmation).
  - **Side panel / drawer**: a panel that slides in from an edge; may be modal (blocking) or non-modal (persistent/complementary).
  - **Focus trap**: keyboard focus cycles within the overlay while it is open.
  - **Return focus**: restoring focus to the trigger element (or a safe fallback) on close.
  - **Background suppression**: preventing pointer + keyboard + screen reader access to content behind the overlay (e.g., via `inert` or equivalent).
  - **Scroll lock**: preventing the document behind the overlay from scrolling.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + contracts) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | UI must remain behind APIs |
| Timeline controls pattern | `docs/accessibility/patterns/timeline-controls.md` | Frontend | Related focus + keyboard guidance |
| Layer registry (declarative layers + gating) | `web/cesium/layers/regions.json` (example) | Frontend | Schema-validated; prevents ad-hoc layer leakage |
| This pattern doc | `docs/accessibility/patterns/modal-and-sidepanel.md` | Frontend | Overlay a11y behavior + tests |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Modal vs side panel decision guidance is explicit
- [ ] Keyboard behavior is specified (open, close, tab order)
- [ ] Focus management rules are specified (initial focus, trap, return focus)
- [ ] Screen reader semantics are specified (names, descriptions, modality)
- [ ] Reduced motion + animation safety rules are specified
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂 Directory Layout

### This document

- `path`: `docs/accessibility/patterns/modal-and-sidepanel.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Graph build + ontology bindings |
| Pipelines | `src/pipelines/` | ETL + catalogs + transforms |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area

~~~text
📁 docs/
├─ 📁 accessibility/
│  ├─ 📁 patterns/
│  │  ├─ 📄 timeline-controls.md
│  │  └─ 📄 modal-and-sidepanel.md
~~~

---

## 🧭 Context

### Background

- KFM’s React/Map UI uses overlays for actions like: layer legends, filters, “share” flows, help/onboarding, provenance/details panels, and confirmations.
- Overlays create predictable accessibility failure modes:
  - Background content remains tabbable/readable to assistive technology
  - Focus gets lost or trapped incorrectly (keyboard users cannot escape)
  - ESC/backdrop click behavior conflicts with destructive actions
  - Motion-heavy transitions cause discomfort and disorientation

This doc standardizes behavior so overlays are consistent and testable across the app.

### Assumptions

- Overlays are implemented in the **React/Map UI** (`web/`), likely using a portal to render above the map canvas.
- The UI may contain sensitive/restricted datasets and locations; overlays must not leak restricted info through UI state.
- Reduced motion preferences must be respected for slide/fade transitions.

### Constraints / invariants

- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- UI overlays must not create side channels for sensitive/restricted layers (no “hidden” content discoverable by keyboard or screen reader).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we have a single shared Modal/SidePanel component, or multiple implementations? | TBD | TBD |
| Do we standardize on `inert` (preferred) or `aria-hidden` patterns for background suppression? | TBD | TBD |
| Are nested overlays allowed (dialog from sidepanel)? If yes, what is the max depth? | TBD | TBD |
| What is the canonical “focus return” fallback when the trigger element unmounts? | TBD | TBD |

### Future extensions

- Standardize an “overlay stack manager” to support nested overlays safely (single focus trap, proper aria-hidden/inert layering).
- Add telemetry signals for overlay open/close and focus-restore failures (privacy-safe; opt-in).

---

## 🗺 Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  Trigger["Trigger element<br/>(button/link/map action)"] -->|open| Overlay["Modal or Side Panel<br/>(overlay container)"]
  Overlay -->|focus trap (modal)| Focus["Keyboard focus stays inside"]
  Overlay -->|close| Return["Return focus to trigger (or fallback)"]
  Overlay --> Suppress["Background suppressed<br/>(inert / aria-hidden equivalent)"]
  Overlay --> Scroll["Scroll lock (optional)<br/>background does not scroll"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
participant User
participant UI as Overlay Component
participant Page as Background Content
User->>UI: Activate trigger (Enter/Space/Click)
UI->>Page: Suppress background (inert/aria-hidden)
UI->>UI: Move focus to initial target
loop while open (modal)
  User->>UI: Tab / Shift+Tab
  UI->>UI: Keep focus within overlay
end
User->>UI: Close (ESC / Close button)
UI->>Page: Restore background interactivity
UI->>UI: Restore focus to trigger (or fallback)
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Trigger element (open control) | DOM element reference | UI event handler | Must exist at open time |
| Overlay type | enum: `modal` / `alert` / `sidepanel-modal` / `sidepanel-nonmodal` | Component props/state | Must map to correct behavior |
| Overlay title/label | string or DOM id | UI props/content | Must provide accessible name |
| Close intent | enum: `explicit` / `escape` / `backdrop` / `programmatic` | UI events | Must be handled consistently |
| Reduced motion preference | boolean | `prefers-reduced-motion` | Must disable/limit animation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Open/closed state | boolean | `web/` UI state | UI state contract (not confirmed in repo) |
| Accessible name/description | ARIA attrs / DOM ids | `web/` DOM | Must be present and stable |
| Background suppression | `inert` / equivalent | `web/` DOM | Must prevent keyboard + SR access |
| Focus restoration target | DOM element | `web/` | Must be deterministic |
| Route/query updates (optional) | URL state | `web/` routing | Not confirmed in repo; avoid breaking share links |

### Sensitivity & redaction

- Overlays MUST NOT disclose restricted layer names/availability to unauthorized users.
- If an overlay presents location-based details, the content MUST be sourced from API responses that apply redaction/generalization rules (no client-only “hidden data”).

### Quality signals

- Keyboard-only: user can open, interact, and close overlay without getting stuck.
- Screen reader: overlay announces a clear name and can be navigated without background noise.
- Predictable close behavior: ESC and close button work as expected; destructive flows require explicit confirmation.
- Motion safety: reduced motion preference is respected.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Not directly impacted by this UI pattern; overlays must surface only metadata that comes from validated catalogs/APIs.

### DCAT

- Not directly impacted; overlays that present dataset details should respect license/attribution surfaced via API metadata.

### PROV-O

- Not directly impacted; overlays that display evidence MUST preserve provenance identifiers provided by the API and avoid fabricating provenance.

### Versioning

- UI overlay behavior should be stable across releases to avoid breaking user workflows and QA expectations.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Modal dialog (UI) | Present blocking overlay; trap focus; return focus | Semantic HTML + ARIA (`role="dialog"`, `aria-modal`) |
| Side panel (UI) | Present drawer; modal or non-modal behavior | `<aside>`/region semantics or modal dialog semantics |
| Overlay stack manager (optional) | Manage nested overlays; single active trap | Internal UI utility (not confirmed in repo) |
| API layer | Provide content with redaction/provenance | REST/GraphQL contracts + tests |
| Map view | Remains stable; does not steal focus | WebGL canvas + accessible controls |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| API schemas | `src/server/` + docs | Backward compat or version bump; contract tests required |
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated; breaking changes require versioning |
| Overlay component props/state | `web/` | Not confirmed in repo; document if stabilized |
| Overlay keyboard contract | This document | Changes require a11y review sign-off |

### Extension points checklist (for future work)

- [ ] UI: add/modify overlay behavior with keyboard + SR tests
- [ ] UI: add overlay stack manager if nested overlays are required
- [ ] APIs: document any new overlay-driven query flows + contract tests
- [ ] Focus Mode: ensure overlay content is provenance-linked and policy-safe
- [ ] Telemetry: optional overlay signals + schema version bump (if implemented)

### Implementation patterns

#### Pattern A — Choose the overlay type correctly

Use this decision rule:

- **Modal dialog** when the user must complete/dismiss the overlay before continuing.
- **Alert dialog** when the user must confirm/cancel a potentially destructive action.
- **Non-modal side panel** when the panel is complementary and users can still interact with the map/page.
- **Modal side panel** (drawer with backdrop) when the drawer blocks interaction (treat like a modal dialog).

If the side panel blocks the rest of the UI, it MUST implement the modal dialog requirements below.

#### Pattern B — Modal dialog (blocking)

Minimum requirements:

- Provide an accessible name:
  - Prefer `aria-labelledby="<id-of-title>"` referencing a visible heading
  - Or `aria-label="…"` when no visible title exists
- Ensure modality:
  - Use `aria-modal="true"` with `role="dialog"` (or a native dialog element)
- Focus management:
  - On open: store previously focused element
  - Move focus into the dialog (prefer close button or first interactive control)
  - Trap focus inside the dialog until closed
  - On close: restore focus to the trigger element (or a safe fallback)
- Dismissal:
  - Close button is always present (unless explicitly non-dismissible)
  - ESC closes the dialog unless it would create data loss or unsafe dismissal (if disabled, provide a clear on-screen explanation)
  - Backdrop click is optional; if enabled, it must behave the same as ESC (non-destructive only)

Example structure (framework-agnostic):

~~~html
<button type="button" id="open-settings" aria-haspopup="dialog">
  Open settings
</button>

<div class="kfm-backdrop" data-state="open"></div>

<div
  role="dialog"
  aria-modal="true"
  aria-labelledby="kfm-dialog-title"
  aria-describedby="kfm-dialog-desc"
  tabindex="-1"
>
  <h2 id="kfm-dialog-title">Settings</h2>
  <p id="kfm-dialog-desc">Update map and accessibility preferences.</p>

  <button type="button" aria-label="Close dialog">Close</button>

  <!-- dialog content -->
  <button type="button">Save</button>
</div>
~~~

Keyboard behavior MUST support:

| Key | Action |
|---|---|
| Tab | Move to next focusable element within the overlay |
| Shift+Tab | Move to previous focusable element within the overlay |
| Escape | Close (unless explicitly disabled for safety) |

Focus safety notes:

- The dialog container is focusable (`tabindex="-1"`) so focus can be moved into it deterministically.
- Do not move focus repeatedly during animation; focus should settle once on open.

#### Pattern C — Alert dialog (confirm/destructive)

Use an alert dialog ONLY when immediate attention/decision is required.

Minimum requirements (in addition to Pattern B):

- Use `role="alertdialog"` (or equivalent semantics in the chosen UI library).
- Put initial focus on the **least destructive** safe action (often “Cancel”) to reduce accidental activation.
- Do not allow backdrop-click dismissal for destructive confirmations.

Example:

~~~html
<div
  role="alertdialog"
  aria-modal="true"
  aria-labelledby="kfm-alert-title"
  aria-describedby="kfm-alert-desc"
  tabindex="-1"
>
  <h2 id="kfm-alert-title">Delete selection?</h2>
  <p id="kfm-alert-desc">This cannot be undone.</p>

  <button type="button">Cancel</button>
  <button type="button">Delete</button>
</div>
~~~

#### Pattern D — Side panel (non-modal / complementary)

A non-modal side panel should NOT trap focus.

Minimum requirements:

- Use an appropriate semantic container:
  - Prefer `<aside>` for complementary content
  - Ensure it has an accessible name via `aria-labelledby` or `aria-label`
- If toggled by a button:
  - The toggle button uses `aria-expanded` and `aria-controls`
  - Closing returns focus to the toggle button if the close action originated within the panel
- When closed, the panel must be removed from the tab order and accessibility tree (e.g., `hidden`, `display:none`, or `inert` + `aria-hidden` patterns).

Example:

~~~html
<button
  type="button"
  aria-controls="kfm-filters-panel"
  aria-expanded="false"
>
  Filters
</button>

<aside id="kfm-filters-panel" aria-labelledby="kfm-filters-title" hidden>
  <h2 id="kfm-filters-title">Filters</h2>

  <button type="button">Close</button>

  <!-- filter controls -->
</aside>
~~~

Recommended keyboard behavior:

- When opening via keyboard, move focus to the panel heading or first control **only if** the user intent is to interact with the panel immediately.
- Otherwise, keep focus on the toggle button and allow the user to Tab into the panel naturally.

#### Pattern E — Side panel (modal drawer)

If the side panel blocks interaction with the rest of the UI, treat it as a modal dialog:

- `role="dialog"` + `aria-modal="true"`
- Focus trap + return focus
- Background suppression + scroll lock

This avoids “half-modal” drawers that confuse keyboard and screen-reader users.

#### Pattern F — Background suppression + scroll lock

Background suppression MUST prevent:

- Keyboard focus from leaving the overlay (modal case)
- Screen readers from navigating “behind” the overlay
- Pointer interaction with background controls

Implementation approach:

- Prefer `inert` on the app root / background container when overlay is open.
- If `inert` is not available, use an equivalent approach that ensures background content is not focusable and not exposed to assistive tech.

Scroll lock:

- When a modal is open, background scrolling should be prevented.
- Allow scrolling inside the overlay if content exceeds viewport height.

#### Pattern G — Overlay stacking (nested overlays)

If nested overlays are allowed:

- Only the top-most overlay can be interactive.
- Only the top-most overlay traps focus (if modal).
- Underlays (including an open sidepanel beneath a modal) must be background-suppressed to prevent “focus leaks”.

If nested overlays are not supported, the UI must prevent opening a second overlay while one is already open (and provide a clear explanation).

#### Pattern H — Reduced motion and transitions

- Respect `prefers-reduced-motion`:
  - Reduce/disable slide/fade transitions
  - Avoid long easing animations
- Never move focus as a side-effect of animation frames.
- If using “closing” transitions, ensure the overlay is not left focusable while visually hidden.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode commonly uses side panels for “details” (entity context, evidence lists, provenance).
- Focus Mode overlays must:
  - Preserve provenance pointers (dataset/asset IDs) returned by APIs
  - Avoid injecting unsourced narrative into overlay UI
  - Respect any Focus Mode constraints (e.g., restricted layers hidden)

### Provenance-linked narrative rule

- Overlays that present narrative or evidence MUST be provenance-linked.
- Every claim shown in a Focus Mode overlay must trace to a dataset / record / asset ID (do not fabricate provenance).

### Optional structured controls

~~~yaml
focus_overlay:
  type: "sidepanel"   # modal | alert | sidepanel
  mode: "nonmodal"    # modal | nonmodal
  title: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] API contract tests — for overlay-driven query flows (if applicable)
- [ ] UI schema checks (layer registry)
- [ ] Accessibility checks:
  - [ ] Keyboard-only open/close; no focus trap leaks
  - [ ] Screen reader announces name + description
  - [ ] Background content is not reachable while modal is open
  - [ ] Reduced motion respected
- [ ] Security and sovereignty checks (no hidden data leakage; redaction enforced)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run unit/integration tests
# 2) run doc lint
# 3) run a11y checks (automated + manual smoke tests)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Overlay opened/closed | UI event | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| Focus restore failure | UI event/error boundary | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| A11y regression detected | CI/a11y tooling | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Accessibility reviewer sign-off is required for changes to overlay focus management and keyboard contracts.
- Governance/security review is required when overlay behavior could affect data exposure (restricted layers, sensitive locations).

### CARE / sovereignty considerations

- Overlays must not reveal restricted locations or sensitive layer existence via:
  - Disabled states that imply hidden content
  - Background content that is still discoverable to assistive technology
  - Timing differences (e.g., an unauthorized user can infer a hidden dataset exists because a “details” panel loads differently)
- If content is culturally sensitive or restricted, ensure UI gating is enforced by APIs and documented access rules.

### AI usage constraints

- This doc’s AI permissions/prohibitions are governed by front-matter:
  - Allowed: summarize, structure_extract, translate, keyword_index
  - Prohibited: generate_policy, infer_sensitive_locations

---

## 🕰 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial accessibility pattern for modals and side panels | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
