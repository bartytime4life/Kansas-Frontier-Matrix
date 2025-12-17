---
title: "Timeline Controls (Accessibility Pattern)"
doc_type: "pattern"
doc_kind: "Pattern"
status: "draft"
version: "v0.1.0"
last_updated: "2025-12-17"
created_by: "KFM Documentation System"
owner: "KFM UI/UX + Frontend"
repo: "Kansas-Frontier-Matrix"
path: "docs/accessibility/patterns/timeline-controls.md"
editors:
  - "KFM Maintainers"
reviewers:
  - "KFM Accessibility Reviewers"
tags:
  - "accessibility"
  - "a11y"
  - "ui-pattern"
  - "timeline"
  - "slider"
  - "react"
  - "maplibre"
  - "focus-mode"
depends_on:
  - "docs/MASTER_GUIDE_v12.md"
  - "docs/accessibility/checklist.md"
related_docs:
  - "docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md"
  - "docs/design/"
  - "web/"
commit_sha: "<latest-commit-hash>"
doc_integrity_checksum: "sha256:<calculate-and-fill>"
ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"
provenance_summary: "Drafted from governed KFM templates + internal system architecture notes describing timeline usage in the UI. Maintainers should validate implementation details against current `web/` components."
artifact_role: "governed-documentation"
lineages: []
sovereignty:
  jurisdiction: "US-KS"
  indigenous_context: "Present"
  data_sensitivity: "Moderate"
sensitivity: "public"
classification: "open"
license: "CC-BY-4.0"
user_facing: true
i18n_ready: false
machine_readable: false
canonical_schema: null
derived_from:
  - "docs/MASTER_GUIDE_v12.md"
links:
  - label: "Accessibility Checklist"
    path: "docs/accessibility/checklist.md"
notes: "Pattern describes user-facing behavior and accessibility contract for timeline UI. It does not prescribe a specific timeline library; any implementation must satisfy the interaction + a11y requirements."
---

# Timeline Controls (Accessibility Pattern)

## Overview

Timeline controls are a core KFM interaction pattern: users adjust time (single year or range) to filter what appears on the map and in accompanying panels.

This pattern defines an **accessibility contract** for timeline controls:
- Keyboard operability
- Screen reader support (role/value/state + readable value text)
- Focus management
- Reduced-motion behavior for playback

### Scope

**In scope**
- Single-value timeline slider (e.g., “Year: 1850”)
- Range selection (e.g., “1850–1860”) if supported
- Playback controls (play/pause, step forward/back)
- Era presets (buttons or menu of periods)
- “Locked timeline” state in Focus Mode (read-only/disabled)

**Out of scope**
- Backend temporal filtering semantics
- Map rendering performance tuning (except where it impacts announcements/focus)
- Final visual design tokens (colors, spacing)—covered elsewhere

### Not confirmed in repo (requires maintainer decision)

- Canonical timeline granularity (year-only vs month/day for some datasets)
- Supported assistive technology + browser matrix
- Whether range selection is first-class (two-handle slider) or implemented as two controls

## 🧱 Directory Layout

~~~text
📁 docs/
└─📁 accessibility/
  ├─📄 checklist.md
  └─📁 patterns/
    └─📄 timeline-controls.md
~~~

## 📌 Context

Timeline controls are frequently used while interacting with the map (panning/zooming/clicking story nodes). They must be accessible **without requiring drag** and without interfering with map navigation.

The pattern must also support Focus Mode behaviors where the timeline may become constrained or locked (read-only) to a specific period.

## 🧩 Diagrams

~~~mermaid
stateDiagram-v2
  [*] --> Idle
  Idle --> Scrubbing: pointer drag / keyboard step
  Scrubbing --> Idle: commit value
  Idle --> Playing: play
  Playing --> Idle: pause
  Playing --> Idle: reach end / stop
  Idle --> Locked: Focus Mode locks timeline
  Locked --> Idle: unlock / exit Focus Mode
~~~

## 🧾 Data & Metadata

### Inputs (recommended)
- `min` / `max` (numeric time domain, e.g., year range)
- `step` (e.g., 1 year; larger step for PageUp/PageDown)
- `value` (current time) OR `startValue` + `endValue` (range)
- `formatValue(value) -> string` used for:
  - visible label
  - `aria-valuetext`
  - announcements (if used)

### Outputs (recommended)
- `onChange(value)` for immediate preview (optional)
- `onCommit(value)` when user “commits” (mouse up / key up / Enter), recommended to reduce AT noise

### Sensitivity note
Do not expose redacted temporal details in:
- `aria-label`
- `aria-describedby`
- `aria-valuetext`
- hidden/offscreen text

If a dataset only has approximate dates, `aria-valuetext` should reflect that (e.g., “circa 1850”) **without revealing hidden precision**.

## 🔁 STAC, DCAT & PROV Alignment

When the UI derives timeline bounds from catalog/metadata:
- Use **temporal extents** consistently (collection/item ranges).
- Prefer formatting that matches user-facing conventions (e.g., year) while keeping provenance trace links elsewhere in UI.

## 🏗️ Architecture & Pipeline Fit

### Preferred control primitives

1) **Use native controls first**
- For single-value selection: prefer `<input type="range">` with an associated `<label>`.

2) **Custom slider only when necessary**
- If a custom slider is required, it must implement a complete slider accessibility contract (role/value/state + keyboard).

### Recommended component structure

- Label row
  - “Year” / “Time range” label
  - Current value text (visible)
- Control row
  - Step back button
  - Slider / range controls
  - Step forward button
  - Play/pause toggle (optional)
- Presets row (optional)
  - Era buttons or menu

## 🔌 Interfaces & Contracts

### Accessibility contract (single-value slider)

**Must provide:**
- A programmatic name (label / `aria-label` / `aria-labelledby`)
- Role and value semantics:
  - If native range input: default semantics are provided
  - If custom: `role="slider"` + `aria-valuemin`, `aria-valuemax`, `aria-valuenow`, and `aria-valuetext`
- Focusable via keyboard (`tabindex="0"` for custom)

### Accessibility contract (range selection)

If range selection is supported:
- Represent the range as **two accessible slider handles** (start/end), or as two native range inputs.
- Each handle must have a distinct accessible name:
  - “Start year”
  - “End year”
- Avoid “drag-only” range selection: provide keyboard operation for both handles.

## Keyboard Interaction

### Single-value slider (recommended mapping)

| Key | Action |
|---|---|
| Left / Down | Decrease by `step` |
| Right / Up | Increase by `step` |
| PageDown | Decrease by “large step” (e.g., 10× step) |
| PageUp | Increase by “large step” |
| Home | Jump to min |
| End | Jump to max |

**Notes**
- If the slider is inside a map UI, ensure arrow key handling is scoped so it does not break map keyboard navigation when the slider is not focused.

### Play/pause (if present)

- Use a `<button>` with:
  - Clear label (“Play timeline”, “Pause timeline”)
  - Optional `aria-pressed="true|false"` if modeled as a toggle button

### Era presets

- Render as buttons or menu items with clear names:
  - “Pre-Statehood”
  - “Civil War”
  - etc.
- Presets must be reachable by keyboard and not rely on hover to describe the action.

## Screen Reader Behavior

### `aria-valuetext` guidance

- `aria-valuetext` should be human-readable:
  - “1850”
  - “1850 to 1860”
  - “circa 1850”
- Do not use raw timestamps unless the UI itself is also timestamp-based.

### Announcements (live regions)

If announcements are used:
- Use a **polite** live region and update on **commit**, not on every micro-step while dragging.
- Avoid rapid updates during playback (or provide a user setting to limit announcements).

## Focus Management

- Tab order should be stable and predictable.
- When timeline changes trigger map rerender:
  - **Do not** steal focus from the currently focused timeline element.
- When opening a story node panel from timeline interactions:
  - Move focus intentionally to the panel header (or keep focus if panel is non-modal), consistent with UI modal/drawer rules.

## Reduced Motion

If playback animates through time:
- Respect `prefers-reduced-motion`:
  - Provide non-animated stepping alternatives
  - Default to paused or reduced animation speed where appropriate
- Always allow user to pause/stop playback.

## Empty / Disabled / Locked States

### Disabled (no temporal data)
- Show a visible message (“No temporal data available”).
- Disable slider and controls programmatically (`disabled` for native, `aria-disabled="true"` for custom).
- Ensure disabled controls are not focusable (or behave consistently if focusable).

### Locked (Focus Mode)
When Focus Mode locks timeline:
- Convey locked state visually (icon + text) and programmatically:
  - `aria-disabled="true"` or `disabled`
  - `aria-describedby` pointing to helper text (“Locked to 1951 for this Focus Mode view”)
- Provide a clear way to exit Focus Mode or unlock if that’s allowed.

## 🧯 Extension Points Checklist

When introducing a new timeline feature:
- [ ] Update this pattern doc with keyboard + screen reader implications.
- [ ] Update `docs/accessibility/checklist.md` if new checks are needed.
- [ ] Ensure layer registry / metadata provides necessary accessible labels (if driven by data).

## 🧭 Story Node & Focus Mode Integration

- Timeline controls must work with:
  - Story Node panels (opening/closing without focus loss)
  - Focus Mode locking or narrowing the time range
  - Governance/audit messaging that may accompany a time-locked view

## 🧪 Validation & CI/CD

**Recommended automated tests (not confirmed in repo)**
- [ ] Unit tests for keyboard interaction (keys listed above).
- [ ] Integration tests:
  - play/pause toggles correctly
  - focus remains on timeline control during map updates
- [ ] Automated a11y scan for:
  - slider labeled correctly
  - no ARIA violations
  - no focus traps

**Manual checks**
- [ ] Keyboard-only: can set year/range precisely without dragging
- [ ] Screen reader: slider announces value and boundaries; play/pause is understandable
- [ ] Reduced motion: playback respects system preference

## 🛡 FAIR+CARE & Governance

- Timeline labels and announcements must not expose redacted times or restricted layer information.
- If the timeline drives visibility of restricted layers, ensure gating is enforced before anything becomes perceivable (including via accessibility APIs).

## 📚 Version History

| Version | Date | Change | Author |
|---|---:|---|---|
| v0.1.0 | 2025-12-17 | Initial draft timeline controls accessibility pattern | KFM Documentation System |

## 🔚 Footer / References

- Accessibility checklist: `docs/accessibility/checklist.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
