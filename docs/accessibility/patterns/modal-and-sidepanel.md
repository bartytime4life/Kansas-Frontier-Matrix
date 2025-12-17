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

doc_integrity_checksum: "sha256:<calculate-and-fill>"
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
| Alert dialogs (destructive confirmations) | Non-overlay UI components (tooltips, popovers) |
| Side panels (non-blocking or semi-blocking) | App-wide design system tokens (colors/typography) |
| Background suppression strategies (inert/aria-hidden) | Content policy and narrative editorial standards |
| Escape key / click-outside rules | Data governance policy text |

### Audience

- Primary: Frontend engineers (`web/`), UX designers, QA.
- Secondary: API engineers (to understand overlay-driven query flows), governance reviewers (sensitivity and audit requirements).

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc: modal, dialog, alert dialog, drawer, side panel, focus trap, inert, aria-hidden, scroll lock.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Overlay components | `web/` | Frontend | Modal and side panel components, focus utilities |
| Focus Mode panels | `web/` | Frontend | Often implemented as side panels |
| Accessibility tests | `tests/` / E2E | QA | Focus trap, return focus, keyboard-only flows |
| Governance refs | `docs/governance/*` | Governance | Sensitivity rules that may affect panel contents |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Modal and side panel semantics defined (roles, labels, focus)
- [ ] Dismiss behavior defined (ESC, close button, click outside rules)
- [ ] Focus trap and focus return rules defined and testable
- [ ] Background suppression rules defined (inert preferred)
- [ ] Validation steps listed (unit + e2e + manual SR smoke test)
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

KFM’s React/Map UI uses overlays for actions like: layer legend/details, entity details, provenance/audit info, help/onboarding, settings, and confirmations.

Overlays create predictable accessibility failure modes if not governed:

- Keyboard focus can disappear behind overlays or land in hidden content.
- Screen readers can continue to read background content while the overlay is open.
- Users can be trapped, unable to close or return.
- Scroll behaviors can become confusing or physically uncomfortable.

### Assumptions

- KFM uses React for UI composition and can centralize focus management in shared components.
- Overlay contents may include sensitive or governed information (e.g., restricted site details), so overlays must integrate with redaction and audit UX.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → React/Map UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Overlays must not create unsourced narrative; citations and provenance links remain visible.
- Overlays must work with keyboard-only and screen readers.
- Reduced-motion and input modality preferences are respected.

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
  Overlay -->|focus trap: modal| Focus["Keyboard focus stays inside"]
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
| Trigger action | keyboard/pointer | UI event | Deterministic open/close behavior |
| Overlay type | enum | component props | “modal”, “alertDialog”, “sidePanel” |
| Accessibility labels | strings | props/content | Present and non-empty |
| Sensitivity context | flags | API response / UI state | Enforce redaction behavior |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Overlay DOM subtree | HTML | UI | a11y contract below |
| Focus movement | programmatic | UI | deterministic focus targets |
| Background suppression | inert/aria-hidden | UI | consistent, reversible |
| Audit/provenance hints | UI strings | UI | rendered when provided by API |

### Sensitivity & redaction

- Side panels commonly show detailed context. If content can be sensitive, the panel must:
  - render redaction notices
  - avoid revealing restricted details
  - surface “why withheld” messaging (governance-owned text, not invented here)

### Quality signals

- Overlay open/close is reversible and does not leak focus.
- Background is not reachable by keyboard while a modal is open.
- Screen reader does not read background content while a modal is open.
- Focus returns to a predictable element.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Overlays may render dataset metadata (items/collections) and time/space extents; the UI should present these without altering the catalog.

### DCAT

- Overlays may surface DCAT “dataset view” fields (title/description/license). These are display-only.

### PROV-O

- Overlay content often includes provenance: the UI should render provenance references returned by APIs (and avoid implying new provenance).
- If overlay content includes “AI explanation”, it must link to evidence/provenance artifacts (not confirmed in repo for exact UI fields).

### Versioning

- Overlays do not create new versions; they display versioned data (story node versions, dataset versions) per API responses.

---

## 🧱 Architecture

### Overlay types and required semantics

#### Modal (dialog)

- Behavior: blocks interaction with rest of page.
- Requirements:
  - Focus moves into modal on open.
  - Focus is trapped within modal while open.
  - Background content is suppressed (prefer `inert`).
  - Escape closes (unless destructive flow requires explicit confirmation).
  - Closing restores focus to trigger (or fallback).

#### Alert dialog

- Behavior: requires immediate user attention (destructive or critical).
- Requirements:
  - Strong labeling and clear actions.
  - Escape may be disabled depending on risk (must be consistent).

#### Side panel (drawer)

- Behavior: often non-blocking; can be “modal-like” if it blocks background.
- Requirements:
  - If non-blocking: background remains reachable; do not apply focus trap.
  - If blocking: treat as modal (focus trap + suppression).
  - Always provide a visible close button reachable by keyboard.
  - For narrow viewports, side panel may become modal (responsive behavior must be consistent).

### Focus management contract

- Initial focus target priority:
  1) First focusable element with `data-autofocus` (or equivalent)
  2) Heading/landmark within overlay
  3) Close button
- Focus return:
  - Return to trigger element if still mounted and focusable.
  - Else return to a safe fallback (e.g., app root landmark).

### Background suppression contract

Preferred: `inert` on background root (when supported).

Fallback: `aria-hidden="true"` on background root **plus** ensure focus cannot move into background via keyboard.

### Dismiss behavior

- Always provide a visible close button.
- ESC:
  - Modal: closes (default)
  - Alert dialog: may require explicit action (document rationale per component)
  - Side panel: closes (default)
- Click outside:
  - Modal: optional (dangerous for forms); if enabled, do not lose data silently.
  - Side panel: optional; must be consistent.

### Scroll lock

- If overlay is modal-like, background scroll should be locked.
- Overlay content area should be scrollable (if long), without trapping scroll.

### Reduced motion

- Opening/closing animations must respect reduced motion preferences.
- No “slide-in” animation if reduced motion is requested (use minimal change).

---

## 🧠 Story Node & Focus Mode Integration

- Side panels are commonly used for Focus Mode “details” views.
- Overlay UI must support:
  - citation rendering within overlay content
  - provenance/audit panels (links or IDs returned by API)
  - sensitivity notices and redaction states
- “AI explanation” toggles, if present, must not fabricate content; it should show evidence references and uncertainty when applicable.

---

## 🧪 Validation & CI/CD

### Validation checklist

- [ ] Keyboard-only open/close; no focus trap leaks
- [ ] Screen reader labels present (dialog name, described-by if needed)
- [ ] Modal suppresses background (inert/aria-hidden + focus exclusion)
- [ ] Escape behavior matches overlay type
- [ ] Close button reachable and visible
- [ ] Focus returns to trigger (or fallback) on close
- [ ] Reduced motion respected
- [ ] Side panel responsive behavior documented (non-blocking vs blocking)

### Suggested tests

- Unit tests:
  - focus moves to correct initial target
  - focus returns to trigger/fallback
  - background suppression toggles on open/close
- E2E tests:
  - tab order and focus trap behavior
  - escape closes (or does not) as specified
  - screen reader smoke test (manual)
- Accessibility lint:
  - ensure dialog has accessible name
  - ensure no duplicated IDs in overlay content

---

## ⚖ FAIR+CARE & Governance

### Governance approvals required (if any)

- FAIR+CARE council review: TBD (if panels expose sensitive data workflows)
- Security council review: TBD (if overlays show restricted details)
- Historian/editor review: TBD (if overlay content includes narrative claims)

### Notes

- Overlays must not infer sensitive locations.
- Side panels often show details; if any content is restricted, show governed notices and avoid leaking redacted fields.

---

## 🕰 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial governed accessibility pattern for modals and side panels | TBD |
