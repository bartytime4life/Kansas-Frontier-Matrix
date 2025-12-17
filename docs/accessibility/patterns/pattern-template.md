---
title: "TEMPLATE — Accessibility Pattern"
path: "docs/accessibility/patterns/pattern-template.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "template"
doc_kind: "Template"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:template:v1.0.0"
semantic_document_id: "kfm-accessibility-pattern-template-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:template:v1.0.0"
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

# TEMPLATE — Accessibility Pattern

## 📘 Overview

### Purpose
- This file is a **copy/paste template** for writing new Accessibility Patterns under `docs/accessibility/patterns/`.
- Accessibility Patterns describe **repeatable UI/content solutions** for common accessibility needs in KFM (keyboard, screen readers, focus management, reduced motion, etc.).
- This template governs:
  - The **minimum sections** every pattern doc must include.
  - The **validation + “definition of done”** checklist required before a pattern is treated as “accepted”.

**How to use this template**
1. Copy this file to a new pattern doc, e.g. `docs/accessibility/patterns/<pattern-slug>.md`.
2. Replace all `<...>` placeholders (and delete any sections marked “Optional” that do not apply).
3. Update front-matter (`title`, `path`, `doc_uuid`, `semantic_document_id`, `event_source_id`, `commit_sha`, `doc_integrity_checksum`).
4. Add the new pattern to `docs/accessibility/patterns/README.md` (index + cross-links).

### Scope
| In Scope | Out of Scope |
|---|---|
| Keyboard interaction models, focus management, semantic markup guidance, screen reader announcements, color/contrast and motion guidelines, accessible content conventions | Legal/compliance opinions, full accessibility audits, vendor-specific AT troubleshooting guides, non-KFM product documentation |

### Audience
- Primary: Frontend engineers, UI/UX designers, QA testers, documentation authors
- Secondary: Product owners, data/graph/API engineers (when UI patterns require contract changes)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (add/remove as needed):
  - WCAG, WAI-ARIA, “accessible name”, “focus order”, “keyboard trap”, “reduced motion”, “Focus Mode”, “Story Node”, “provenance/citation”.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Patterns index | `docs/accessibility/patterns/README.md` | Docs | List of patterns + naming conventions |
| Pattern template (this file) | `docs/accessibility/patterns/pattern-template.md` | Docs | Copy to start new pattern |
| Pattern doc (new) | `docs/accessibility/patterns/<pattern-slug>.md` | Pattern owner | This template, completed |
| Related implementation | `web/<...>` | Frontend | Repo path(s) where the pattern is implemented |
| Tests / QA artifacts | `<repo-specific>` | QA/Frontend | Test cases, snapshots, a11y test runs (if present) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Pattern summary filled (who it helps, where it applies, status/owner)
- [ ] Clear “Problem” and “Solution” statements (testable, not aspirational)
- [ ] Keyboard interaction and focus order explicitly specified
- [ ] Screen reader semantics specified (role/name/state + announcements as needed)
- [ ] Validation steps listed and repeatable (manual + automated where possible)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (including redaction risk in accessible text)
- [ ] Added to `docs/accessibility/patterns/README.md`

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/patterns/pattern-template.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | A11y standards, checklists, patterns |
| Accessibility patterns | `docs/accessibility/patterns/` | Pattern docs + this template |
| Frontend | `web/` | React + map UI implementations |
| Docs (general) | `docs/` | Governed docs, Story Nodes, governance references |

### Expected file tree for this sub-area
~~~text
📁 docs/
└─ 📁 accessibility/
   └─ 📁 patterns/
      ├─ 📄 README.md
      ├─ 📄 pattern-template.md
      ├─ 📄 <pattern-slug>.md
      └─ 📁 assets/                         (optional)
         └─ 📁 <pattern-slug>/              (optional)
            ├─ 🖼️ screenshot-01.png
            ├─ 🖼️ focus-order.png
            └─ 🖼️ sr-announcement-notes.png
~~~

## 🧭 Context

### Background
Fill this section in the **new pattern doc**.

**Pattern summary**
| Field | Value |
|---|---|
| Pattern name | `<PATTERN_NAME>` |
| Pattern slug | `<pattern-slug>` |
| Status | `draft \| review \| accepted \| deprecated` |
| Owner | `<team/person>` |
| Applies to | `<Focus Mode / Map / Filters / Timeline / Story Node viewer / ...>` |
| Primary users helped | `<keyboard-only / screen-reader / low-vision / cognitive / ...>` |
| WCAG mapping | `<SC references, e.g., 2.1.1, 2.4.3, 1.1.1>` |
| Linked issues/PRs | `<tickets/PRs/IDs>` |
| Last reviewed | `<YYYY-MM-DD>` |

**Problem statement**
- What breaks today for which users?
- What is the user impact (task they can’t complete, information they can’t access, etc.)?

**Solution statement**
- What is the minimum, testable behavior we are standardizing?
- What does “good” look like for keyboard + screen reader?

### Assumptions
- KFM UI is consumed through web user agents with a range of assistive technologies.
- UI changes must remain compatible with the KFM pipeline contract: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes data via APIs (no direct graph dependency).

### Constraints / invariants
- Prefer **native HTML semantics** first; use ARIA only when semantics cannot be achieved with native elements.
- Do not encode meaning using **color alone**; provide text/ARIA/state equivalents.
- Do not create “keyboard traps”; all interactive regions must be escapable with keyboard alone.
- “Focus Mode” narratives must remain **provenance-linked** and **readable via assistive tech** (citations must be perceivable without hover-only or color-only cues).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| TBD | TBD | TBD |

### Future extensions
- Extension point A: `<TBD>`
- Extension point B: `<TBD>`

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
U[User] -->|keyboard / pointer / touch| UI[React/Map UI]
U -->|assistive tech| AT[Screen reader / AT]
AT <--> UI
UI --> API[APIs]
API --> G[Graph + provenance refs]
G --> API
API --> UI
UI --> SN[Story Nodes]
SN --> UI
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
participant User
participant UI as UI Component
participant API
participant AT as Screen Reader / AT

User->>UI: Activate control (keyboard or pointer)
UI->>UI: Update state + manage focus
UI->>API: Fetch/update data (if needed)
API-->>UI: Response (data + provenance refs)
UI-->>AT: Expose updated role/name/state (and announce if needed)
UI-->>User: Visible update (no color-only cue)
~~~

## 📦 Data & Metadata

### Inputs
Use this table to document **user inputs + content inputs** relevant to the pattern.

| Input | Format | Where from | Validation |
|---|---|---|---|
| Keyboard interactions | DOM events | Browser | Manual keyboard test + automated UI tests (if present) |
| Pointer/touch interactions | DOM events | Browser | Manual + automated UI tests |
| Screen reader navigation | AT virtual cursor | NVDA/JAWS/VoiceOver/etc. | Manual SR checklist |
| Content (labels, alt text, captions) | Markdown/JSON/etc. | Docs + UI config | Content review + redaction review |

### Outputs
Use this table to document **what the user experiences** and where it is implemented.

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Accessible name/role/state | DOM / Accessibility Tree | `web/<...>` | HTML + ARIA mapping documented below |
| Focus behavior | DOM focus | `web/<...>` | “Focus order” documented + tested |
| Announcements (if used) | `aria-live` / status text | `web/<...>` | Announce rules documented + tested |

### Sensitivity & redaction
- If accessible text (labels, alt text, captions, descriptions) could reveal sensitive locations, identities, or culturally sensitive information:
  - Specify what must be generalized/redacted.
  - Specify who reviews the wording (role or team).

### Quality signals
- Define the quality checks for this pattern (examples; adjust to your pattern):
  - No keyboard traps; focus can reach and leave all interactive regions.
  - Focus order matches visual order and user task order.
  - Visible focus indicator present for interactive elements.
  - Screen reader announces meaningful updates (and does not spam).
  - Any non-text content has a text alternative when required.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `N/A` (unless this pattern changes how STAC assets are surfaced)
- Items involved: `N/A`
- Extension(s): `N/A`

### DCAT
- Dataset identifiers: `N/A`
- License mapping: `N/A`
- Contact / publisher mapping: `N/A`

### PROV-O
- `prov:wasDerivedFrom`: `N/A` (unless this pattern changes provenance display)
- `prov:wasGeneratedBy`: `N/A`
- Activity / Agent identities: `N/A`

### Versioning
- If this pattern results in contract changes (UI behavior guarantees, API changes, schema changes), specify:
  - What version is bumped (doc version, API contract version, schema version).
  - Backward compatibility notes (what breaks, what remains stable).

## 🧱 Architecture

### Components
List the main components and responsibilities for this pattern.

| Component | Responsibility | Interface |
|---|---|---|
| `<Component/feature name>` | `<What it does>` | `<props/events/routes>` |
| `<Accessibility semantics>` | `<role/name/state rules>` | `<HTML/ARIA mapping>` |
| `<Focus management>` | `<where focus moves + why>` | `<documented focus rules>` |
| `<Announcements (optional)>` | `<what gets announced>` | `<aria-live/status region>` |

### Data contracts
Use this section to document “contracts” as **testable guarantees**.

| Contract | Path | Notes |
|---|---|---|
| Keyboard mapping | `docs/accessibility/patterns/<pattern-slug>.md` | Define keys + expected behavior |
| Focus order | `docs/accessibility/patterns/<pattern-slug>.md` | Define entry/exit focus + order |
| Accessible name/role/state | `docs/accessibility/patterns/<pattern-slug>.md` | Define semantics and fallback rules |
| API contract impact (if any) | `<API doc / ticket>` | Only if needed; keep UI behind APIs |

### Interfaces
- UI ↔ AT: roles, names, states, focus, announcements
- UI ↔ APIs: data fetch/update; error/loading states must be perceivable (not spinner-only)
- Docs ↔ UI: if narrative or content is rendered, ensure headings, lists, and citations are accessible

### Security / privacy notes
- Avoid leaking sensitive details through accessible names/labels/alt text.
- Treat any user-provided content used in ARIA attributes as untrusted input; define sanitization expectations (repo-specific).

### Quality signals
- Automated checks (examples; use only what exists in repo):
  - Linting for semantic HTML / ARIA usage (`<repo-specific>`)
  - Automated a11y tests (`<repo-specific>`)
- Manual checks:
  - Keyboard-only walkthrough of critical tasks
  - Screen reader walkthrough for primary flows

### Extension points checklist (for future work)
- [ ] UI: component added/updated + documented behavior
- [ ] Focus Mode: narrative/citations remain accessible and provenance-linked
- [ ] APIs (only if required): contract updates + tests
- [ ] Telemetry (optional): signals for regressions (e.g., error rates, client-side a11y violations if collected)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- What entities/surfaces become focusable because of this pattern?
- What evidence must be shown, and how is it made perceivable without hover-only or color-only mechanisms?

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Citations must be usable with assistive tech (e.g., real links, not tooltip-only markers).

### Optional structured controls
~~~yaml
a11y_controls:
  keyboard_shortcuts: "TBD"
  focus_management: "TBD"
  announcements: "TBD"
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Manual keyboard test steps included + executed
- [ ] Manual screen reader test steps included + executed
- [ ] Automated UI/a11y tests run (if present in repo)
- [ ] Governance and sovereignty checks completed (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run unit/integration tests
# 2) run e2e tests (if present)
# 3) run accessibility checks (if present)
# 4) run doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| `<TBD>` | `<TBD>` | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- What requires accessibility review (and by whom)?
- What requires governance sign-off (and by whom)?
- What requires security review (and by whom)?

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- If this pattern affects how sensitive content is described (alt text, summaries), document the redaction/generalization rules.

### AI usage constraints
- Ensure the doc’s `ai_transform_permissions` / `ai_transform_prohibited` match intended use.
- Do not use AI to “fill in” sensitive place details or identities in accessible text.

## 🕰 Version History
| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial template | TBD |
---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
