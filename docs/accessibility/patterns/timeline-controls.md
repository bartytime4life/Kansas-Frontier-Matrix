---
title: "Timeline Controls (Accessibility Pattern)"
path: "docs/accessibility/patterns/timeline-controls.md"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:timeline-controls:v1.0.0"
semantic_document_id: "kfm-accessibility-patterns-timeline-controls-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:timeline-controls:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"
ai_transform_prohibited:
  - "generate_policy"
  - "infer_sensitive_locations"

doc_integrity_checksum: "sha256:0cfbf51c12dba2a68fc5012c8c0eff2d880e2d8f1ad46130926e7fa9d0a416c4"
---

# Timeline Controls

## 📘 Overview

### Purpose

- Define accessible, testable UI patterns for **timeline controls** in the KFM React/Map UI (time slider, optional play/pause, and supporting inputs).
- Govern the **interaction contract** between timeline controls and the rest of KFM (map layer filtering, API time filters, Focus Mode constraints, and URL snapshot state).
- Reduce risk of timeline features becoming “visual-only” (mouse-only, silent to assistive tech, or motion-heavy).

### Scope

| In Scope | Out of Scope |
|---|---|
| Keyboard semantics for time sliders and playback controls | Creating/curating temporal datasets (ETL + catalogs) |
| Screen reader naming/value exposure for timeline controls | Defining new REST/GraphQL endpoints (use API Contract Extension template) |
| Reduced motion + autoplay safeguards | Map styling decisions that are not accessibility-related |
| Focus Mode time constrain/lock patterns | Backfilling missing temporal metadata in catalogs |
| Validation checklist (a11y + governance) | Authoring Story Nodes (use Story Node template) |

### Audience

- Primary: Frontend engineers implementing timeline UI in `web/`
- Secondary: UX/design contributors, QA/a11y reviewers, governance/security reviewers (data leakage + sovereignty)

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Timeline control**: UI element that sets a current time or time window used to filter map layers/queries.
  - **Scrubbing**: continuous pointer/keyboard adjustments to inspect change over time.
  - **Commit**: the moment a time selection is applied (e.g., pointer-up, Enter, Apply).
  - **Playback**: auto-advancing the time control (play/pause).
  - **Temporal extent**: time coverage for a layer/asset (e.g., STAC temporal extent).
  - **Focus lock**: Focus Mode makes timeline readonly or constrained to a window.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + contracts) | `docs/MASTER_GUIDE_v12.md` | Core maintainers | UI must remain behind APIs |
| Layer registry (declarative layers + gating) | `web/cesium/layers/regions.json` (example) | Frontend | Schema-validated; prevents ad-hoc layer leakage |
| API time filtering contracts | `src/server/` + docs | Backend | Contract-governed; provenance + redaction |
| This pattern doc | `docs/accessibility/patterns/timeline-controls.md` | Frontend | Establishes a11y behavior + tests |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Scope and invariants are explicit (no direct graph access; timeline is UI-only)
- [ ] Timeline control keyboard + screen reader behaviors are specified
- [ ] Reduced motion + autoplay constraints are specified
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

---

## 🗂 Directory Layout

### This document

- `path`: `docs/accessibility/patterns/timeline-controls.md`

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
│  │  └─ 📄 timeline-controls.md
~~~

---

## 🧭 Context

### Background

- KFM’s map UI is explicitly time-aware: users browse historical periods and filter visible layers by year/era, and some designs include playback (“play”) and shareable snapshots (layer set + time).
- Timeline controls are a primary navigation control. If inaccessible, the system becomes effectively unusable for keyboard and screen-reader users for temporal exploration.

### Assumptions

- Timeline controls live in the **React/Map UI** (`web/`).
- Temporal extents are available via catalogs and/or API payloads (STAC/metadata + query endpoints).
- “Play mode” is optional; when present it must be pauseable and respect reduced motion preferences.

### Constraints / invariants

- Canonical pipeline ordering is preserved: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes contracts via APIs (no direct graph dependency).
- UI changes must not create side channels for sensitive/restricted layers (no hidden data leakage).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we standardize on “year” vs. ISO 8601 datetime in UI state and URL snapshots? | TBD | TBD |
| Are timeline ranges (two-thumb) a hard requirement or optional feature? | TBD | TBD |
| What is the approved announcement strategy for playback (coarse vs. per-tick)? | TBD | TBD |

### Future extensions

- Add an **events timeline list** synchronized with the map (select event → highlight on map; select map feature → focus timeline).
- Add **faceted temporal filtering** (era presets, confidence filters) sourced from API metadata rather than hard-coded lists.
- Add telemetry signals for a11y regressions (opt-in; privacy-safe).

---

## 🗺 Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  User["User input<br/>(keyboard / pointer / screen reader)"] --> TL["Timeline controls<br/>(UI state)"]
  TL -->|preview scrub| Map["Map layers<br/>(filtered visibility)"]
  TL -->|commit| API["API layer<br/>(time-filtered query)"]
  API -->|results + provenance refs| Map
  TL --> URL["URL snapshot state<br/>(shareable)"]
  FM["Focus Mode"] -->|constrain/lock time| TL
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
participant UI as Timeline UI
participant API as API Layer
participant Map as Map View
UI->>Map: update preview (scrub)
UI->>API: commit time change (apply filter)
API-->>UI: response (items + provenance refs)
UI->>Map: render updates (time-filtered)
note over UI: Focus Mode may lock/constrain time
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Temporal bounds (min/max) | ISO 8601 interval or derived year range | STAC extents or API summaries | Must parse; must be monotonic (min ≤ max) |
| Layer temporal extent | ISO 8601 interval(s) | Layer registry + catalogs/API | Must intersect correctly with selected time |
| Focus Mode time constraint (optional) | ISO 8601 interval or year range | Focus Mode context payload | Must narrow bounds; must be explainable to user |
| User preference: reduced motion | boolean | Client pref (`prefers-reduced-motion`) | Must disable autoplay by default |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Current time selection | year or ISO 8601 | `web/` UI state | UI state contract (not confirmed in repo) |
| Time window selection | start/end (year or ISO 8601) | `web/` UI state | UI state contract (not confirmed in repo) |
| API time filter parameter(s) | query params / GraphQL args | `src/server/` | Contract-governed; tests required |
| URL snapshot | query string / route state | `web/` | UI routing contract (not confirmed in repo) |

### Sensitivity & redaction

- Timeline controls MUST NOT disclose restricted layer names/availability to unauthorized users.
- Timeline-driven queries MUST rely on API enforcement for redaction/generalization of sensitive locations.

### Quality signals

- Range constraints: selected values are within bounds; `start <= end`.
- Keyboard coverage: every control is operable without pointer.
- Screen reader coverage: label + value + constraints are discoverable.
- Motion safety: autoplay is never forced; pause is always available.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: any collection with temporal extent used for time filtering (collection IDs not confirmed in repo).
- Items involved: items returned by time-filtered queries; items should provide `datetime` or equivalent temporal coverage.
- Extension(s): any KFM temporal conventions/extensions (not confirmed in repo).

### DCAT

- Dataset identifiers: the dataset IDs used in UI facets or layer metadata (not confirmed in repo).
- License mapping: UI must preserve dataset license/attribution when presenting time-filtered results.
- Contact / publisher mapping: surfaced via dataset metadata where required (not confirmed in repo).

### PROV-O

- `prov:wasDerivedFrom`: preserve dataset/asset IDs returned by API as provenance pointers.
- `prov:wasGeneratedBy`: preserve transform/job IDs when returned (run IDs, activity IDs).
- Activity / Agent identities: do not fabricate provenance; only display what the API returns.

### Versioning

- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- Timeline ranges should remain metadata-driven so new dataset versions naturally update time bounds.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Timeline controls (UI) | Select time or time window; expose value to AT | Semantic HTML (preferred) or ARIA slider |
| Layer registry | Declare layers + constraints + gating | JSON + schema validation |
| API layer | Execute time-filtered queries; apply redaction | REST/GraphQL contracts + tests |
| Focus Mode | Provide constrained/locked time contexts | Focus context bundle (provenance-linked) |
| Map view | Render time-filtered layers | WebGL map rendering + UI state |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Layer registry | `web/cesium/layers/regions.json` | Schema-validated; breaking changes require versioning |
| API schemas | `src/server/` + docs | Backward compat or version bump; contract tests required |
| UI time state (shape) | `web/` | Not confirmed in repo; document if stabilized |
| URL snapshot encoding | `web/` | Not confirmed in repo; avoid breaking share links |

### Extension points checklist (for future work)

- [ ] UI: add/modify timeline behavior with keyboard + SR tests
- [ ] UI: layer registry entry + access rules (no hidden data leakage)
- [ ] APIs: time filter changes documented + contract tests updated
- [ ] Focus Mode: time lock/constrain behaviors documented and provenance-linked
- [ ] Telemetry: optional new signals + schema version bump (if implemented)

### Implementation patterns

#### Pattern A — Native range input slider (preferred)

Use a native slider, plus a visible and programmatic value readout.

~~~html
<label for="kfm-time-slider">Time (year)</label>
<input
  id="kfm-time-slider"
  type="range"
  min="1800"
  max="1900"
  step="1"
  value="1850"
  aria-describedby="kfm-time-help kfm-time-value"
/>

<p id="kfm-time-help">
  Use left/right arrow keys to change the year. Home/End jumps to min/max.
</p>

<output id="kfm-time-value" for="kfm-time-slider">1850</output>
~~~

#### Pattern B — Custom ARIA slider (only when native cannot be used)

~~~html
<div
  role="slider"
  tabindex="0"
  aria-label="Time (year)"
  aria-valuemin="1800"
  aria-valuemax="1900"
  aria-valuenow="1850"
  aria-valuetext="1850"
/>
~~~

Keyboard behavior MUST support:

| Key | Action |
|---|---|
| ArrowRight / ArrowUp | Increase by `step` |
| ArrowLeft / ArrowDown | Decrease by `step` |
| PageUp | Increase by “large step” (e.g., 10× step) |
| PageDown | Decrease by “large step” |
| Home | Set to min |
| End | Set to max |

#### Pattern C — Range selection (start/end)

Prefer two independent sliders (or a slider + numeric inputs) with clear labels.

~~~html
<label for="kfm-start-year">Start year</label>
<input id="kfm-start-year" type="range" min="1800" max="1900" step="1" value="1850" />

<label for="kfm-end-year">End year</label>
<input id="kfm-end-year" type="range" min="1800" max="1900" step="1" value="1860" />

<output id="kfm-range-summary">Showing 1850–1860</output>
~~~

Minimum requirements:

- Enforce `start <= end`
- Associate errors/status messages via `aria-describedby`

#### Pattern D — Playback (play/pause) and reduced motion

If animation is provided:

- Pause MUST be available at all times
- Autoplay MUST NOT run by default when reduced motion is requested

~~~html
<button aria-pressed="false" aria-label="Play timeline">
  Play
</button>
~~~

Announcement guidance:

- Avoid announcing every tick while playing (screen reader overload).
- Prefer announcing only on pause/stop, or at coarse intervals.

#### Pattern E — Map synchronization and focus management

- Timeline changes MUST NOT steal focus.
- If time changes cause map updates, use a non-intrusive status message (optional) and avoid rapid-fire live regions.
- If selected time has no data, show inline message and associate it with the control.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode may set a default or constrained time window relevant to the selected entity/place/story.
- Timeline controls must represent:
  - **free**: user can select any time within global bounds
  - **constrained**: user can select within a narrowed window
  - **locked**: user cannot change time until exiting Focus Mode

### Provenance-linked narrative rule

- Focus Mode only consumes provenance-linked content.
- Timeline filtering must not introduce unsourced narrative; it only changes which evidence is eligible to display.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time:
  mode: "locked"          # free | constrained | locked
  start: "1850-01-01"
  end: "1860-12-31"
  granularity: "year"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV) — as applicable to layers being filtered
- [ ] Graph integrity checks — not directly impacted by this UI pattern
- [ ] API contract tests — time filter changes
- [ ] UI schema checks (layer registry)
- [ ] Accessibility checks (keyboard + screen reader + reduced motion)
- [ ] Security and sovereignty checks (no hidden data leakage; redaction enforced)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas
# 2) run unit/integration tests
# 3) run doc lint
# 4) run a11y checks
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Timeline playback used | UI event | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| A11y regression detected | CI/a11y tooling | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Accessibility reviewer sign-off is required for changes to timeline interactions and announcements.
- Governance/security review is required when timeline behavior could affect data exposure (layer gating, restricted locations).

### CARE / sovereignty considerations

- Timeline controls must not reveal restricted locations or sensitive layer existence via timing differences, labels, or disabled UI states.
- If sensitive data is time-scoped, ensure redaction/generalization rules are documented and enforced by the API and layer registry.

### AI usage constraints

- This doc’s AI permissions/prohibitions are governed by front-matter:
  - Allowed: summarize, structure_extract, translate, keyword_index
  - Prohibited: generate_policy, infer_sensitive_locations

---

## 🕰 Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial accessibility pattern for timeline controls | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
