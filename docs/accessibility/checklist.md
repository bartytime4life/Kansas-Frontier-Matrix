~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~
FILE: docs/accessibility/checklist.md
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~
---
title: "KFM Accessibility Checklist"
path: "docs/accessibility/checklist.md"
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

doc_uuid: "urn:kfm:doc:accessibility:checklist:v0.1.0"
semantic_document_id: "kfm-accessibility-checklist-v0.1.0"
event_source_id: "ledger:kfm:doc:accessibility:checklist:v0.1.0"
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

# KFM Accessibility Checklist

## 📘 Overview

### Purpose
- Provide a repeatable accessibility (a11y) checklist for KFM UI + docs changes.
- Use this checklist during PR review and release readiness checks for `web/` (React/Map UI) and `docs/` content that renders in Focus Mode (Story Nodes, reports, guides).

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI accessibility checks for navigation, components, map controls, Focus Mode, and Story Node rendering | Legal/compliance determinations or formal certification (must be handled by project governance) |
| Documentation accessibility (Markdown structure, headings, links, images/diagrams alt text) | Backend API “accessibility” beyond user-facing error message clarity |
| Repeatable validation steps (manual + automated), with evidence artifacts | Project-wide policy-setting (this doc is a checklist, not a policy) |

### Audience
- Primary: Frontend engineers, UI reviewers, UX/design contributors
- Secondary: Docs authors, Story Node authors/editors, QA/testers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (add to glossary as needed):
  - accessibility (a11y)
  - keyboard trap
  - focus order / focus visible
  - accessible name / accessible description
  - semantic HTML
  - ARIA
  - reduced motion
  - contrast ratio

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Accessibility entry point | `docs/accessibility/README.md` | TBD | Overview + how to apply a11y in KFM |
| Tooling details | `docs/accessibility/tooling.md` | TBD | Linters, scanners, CI hooks (repo-specific) |
| Testing guidance | `docs/accessibility/testing.md` | TBD | Manual test flows + expected evidence |
| Frontend implementation | `web/` | Frontend | React/Map UI + Focus Mode |
| UI/UX patterns | `docs/design/` | Design | Component patterns, map UX patterns |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs | Structure constraints for narrative artifacts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Links resolve to repo paths (no dead internal refs)
- [ ] Checklist is actionable for PR review + release review
- [ ] Validation steps are listed and repeatable (tool-agnostic placeholders OK if commands are TBD)
- [ ] Governance + CARE/sovereignty considerations explicitly stated (even if “N/A”)

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/checklist.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Accessibility docs | `docs/accessibility/` | A11y entry point, tools, testing, checklists |
| Frontend | `web/` | React + map clients + Focus Mode UI |
| Design docs | `docs/design/` | UX patterns + component guidance |
| Story Nodes | `docs/` (TBD subpath) | Story Node markdown artifacts used by Focus Mode |

### Expected file tree for this sub-area
~~~text
📁 docs/
  📁 accessibility/
    📄 README.md
    📄 checklist.md
    📄 testing.md
    📄 tooling.md
~~~

## 🧭 Context

### Background
- KFM includes a map + narrative UI that must be usable by keyboard-only users, screen reader users, and users with low vision or cognitive load constraints.
- Accessibility checks are easiest to maintain when they are performed at review-time (PR checklist) and at release-time (full checklist), with lightweight evidence artifacts.

### Assumptions
- KFM’s canonical pipeline ordering is preserved (ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode).
- Accessibility validation includes both automated checks and manual sanity checks for key flows.
- Accessibility conformance target (e.g., WCAG level) is **TBD** (see Open Questions). This checklist is written to be compatible with common web a11y expectations, but the project must confirm the specific target.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Accessibility fixes must not bypass sensitivity/redaction practices (e.g., text alternatives must respect any redaction/generalization rules defined elsewhere).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What accessibility conformance target does KFM claim (if any)? | TBD | TBD |
| Which automated a11y checks are required in CI (and what severity thresholds block merges)? | TBD | TBD |
| Which browsers + assistive tech combos are in-scope for release sanity checks? | TBD | TBD |
| Map accessibility strategy: what is the “non-map equivalent” view for critical map info? | TBD | TBD |

### Future extensions
- Add repo-specific “golden commands” in `docs/accessibility/testing.md` (unit/e2e/a11y scans).
- Add a component-level checklist (dialogs, menus, map controls) in `docs/design/`.
- Add a lightweight “a11y regression budget” (e.g., block on new serious violations).

## ✅ Accessibility Checklist

### How to use this checklist
- Use **PR Quick Checks** for any UI change, content change, or story-node rendering change.
- Use **Release Checks** before shipping a release or publishing a major story/collection.
- When an item is not applicable, mark it explicitly as N/A in the PR/release notes (do not silently skip).

### PR quick checks (must-pass for most UI changes)
- [ ] **Keyboard**: All new/modified interactive controls are reachable and usable with keyboard only (Tab/Shift+Tab, Enter/Space, Arrow keys where appropriate).
- [ ] **Focus**: Focus is visible on all interactive elements; focus order is logical and does not jump unexpectedly.
- [ ] **Names**: All icon buttons/controls have an accessible name (visible label or `aria-label`) that matches intent.
- [ ] **Semantics**: Use semantic HTML elements for controls (e.g., `button` for buttons) instead of click handlers on non-interactive elements.
- [ ] **No traps**: No keyboard traps in modals, drawers, or map widgets; Escape closes dialogs (where appropriate).
- [ ] **Errors**: Any new error state is announced clearly (and does not rely on color alone).
- [ ] **Contrast**: New text/iconography meets project contrast expectations (confirm target in Open Questions).
- [ ] **Headings**: Any new page/Focus Mode panel has a meaningful heading structure (no skipped levels for structure-only).
- [ ] **Map UI** (if touched): Map controls + layer toggles are keyboard accessible and have clear labels.

### Release checks (full checklist)

#### 1) Page structure & landmarks
- [ ] Each screen/view has a unique, descriptive page title (or Focus Mode panel title) that updates appropriately.
- [ ] Primary landmarks exist (header/nav/main/footer) or equivalent structure in the app shell.
- [ ] There is a clear “main content” region for screen readers.
- [ ] Heading levels reflect document structure (don’t skip levels to style text).

#### 2) Keyboard navigation & focus management
- [ ] Tab order follows visual/reading order.
- [ ] Custom components (menus, tabs, comboboxes) implement expected keyboard interactions.
- [ ] Focus is moved into dialogs on open and returned to the trigger on close.
- [ ] No focus is lost “behind” overlays (drawer/modal).
- [ ] No keyboard-only dead-ends (e.g., closing control unreachable).

#### 3) Forms, filters, and search
- [ ] Every input has a visible label or programmatic label (`label` / `aria-label`), and label text is meaningful.
- [ ] Required fields are indicated in more than one way (not color only).
- [ ] Inline validation errors are associated with the input and are announced in an accessible way.
- [ ] Error summary (if present) lists errors with links/focus targets.

#### 4) Buttons, links, and controls
- [ ] Link text is descriptive out of context (“Learn more” is avoided unless accompanied by context).
- [ ] Buttons have labels that describe the action (“Open layer legend”, “Filter results”, etc.).
- [ ] Icon-only controls have accessible names and sufficient hit target size.
- [ ] Disabled states are communicated to assistive tech (don’t fake disabled via CSS only).

#### 5) Color, contrast, and non-text cues
- [ ] Information is not conveyed by color alone (use text, icons with labels, patterns, etc.).
- [ ] Text contrast meets the project’s target (TBD: confirm WCAG level).
- [ ] Non-text contrast is acceptable for icons, focus rings, and control boundaries.

#### 6) Content readability & cognitive load
- [ ] Avoid unexplained abbreviations; expand on first use or provide a glossary reference.
- [ ] Long pages/panels have clear subheadings and chunked sections.
- [ ] Inline help uses plain language and avoids jargon unless unavoidable.

#### 7) Media: images, diagrams, audio/video
- [ ] Images have meaningful alt text, or empty alt (`alt=""`) when decorative.
- [ ] Complex diagrams include a short text summary or a link to a longer description.
- [ ] Video has captions; audio has transcripts (if present in KFM surfaces).

#### 8) Motion, animation, and flashing
- [ ] Animations respect “reduced motion” preferences where feasible.
- [ ] No flashing content that could trigger seizures.
- [ ] Autoplaying motion is avoided or user-controllable.

#### 9) Responsive & zoom
- [ ] Layout works at 200% zoom without horizontal scrolling for main content (where practical).
- [ ] Touch targets are usable on mobile/tablet and do not overlap.
- [ ] Content reflows and controls remain discoverable.

#### 10) Map-specific checks (React/Map UI)
- [ ] Map controls (zoom, reset, layer toggles, legend, time slider) are reachable and operable via keyboard.
- [ ] Controls have accessible names (avoid unlabeled icon buttons).
- [ ] There is a non-map equivalent for critical information (e.g., list/table view of features currently in focus, or a details panel).
- [ ] Popups/tooltips:
  - [ ] Do not require hover only (keyboard users can trigger).
  - [ ] Do not disappear before users can interact (timed hover popups are avoided).
- [ ] Layer legends:
  - [ ] Legend has a text description of symbology, not color-only keys.
- [ ] If the map is used to select features, there is an accessible alternative selection path (search/list).
- [ ] Any “sensitive/redacted” location representation remains consistent across map + text alternatives.

#### 11) Data tables, charts, and evidence panels
- [ ] Tables use `th` for headers and correct header associations.
- [ ] Sortable columns expose sort state to assistive tech.
- [ ] Charts have text summaries; key values are available in a table/list format.

#### 12) Docs and Story Nodes (Markdown → rendered content)
- [ ] Markdown uses a logical heading structure.
- [ ] Links are descriptive and not “click here”.
- [ ] Images/figures include alt text; citations are clear and consistently formatted.
- [ ] Story Node narrative avoids embedding meaning only in color or visuals (provide text equivalents).

### Evidence artifacts (recommended to attach for release)
- [ ] Automated a11y scan output (tooling TBD; attach report artifact or summary)
- [ ] Keyboard-only walkthrough notes for key flows (navigation → Focus Mode → details)
- [ ] Screen reader sanity check notes for at least one in-scope combo (combo(s) TBD)
- [ ] 200% zoom screenshots for key views
- [ ] Notes for any known exceptions + mitigation plan (if any)

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
  H[Accessibility checklist + tests] -.-> E
  H -.-> F
  H -.-> G
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI components + screens | code | `web/` | Checklist + tests |
| Docs + Story Nodes | markdown | `docs/` | Checklist + doc lint (TBD) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Accessible UI behavior | runtime UI | `web/` | Checklist items + automated scan thresholds (TBD) |
| Accessible docs/story rendering | rendered HTML | `docs/` → UI surfaces | Template + checklist |

### Sensitivity & redaction
- If content includes sensitive information, ensure text alternatives (alt text, tables, summaries) respect redaction/generalization requirements defined in governance docs.

### Quality signals
- Define accessibility quality checks for releases (examples; confirm in tooling docs):
  - “No new serious/critical automated a11y violations”
  - “Keyboard walkthrough completed for key flows”
  - “Screen reader sanity check completed for Focus Mode”

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: N/A (this doc does not define STAC collections)
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
- This document follows governed doc versioning in front-matter (SemVer-like string).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| APIs | Serve contracts to UI | REST/GraphQL (repo-defined) |
| UI | Map + narrative surfaces | API calls |
| Story Nodes | Curated narrative content | Markdown + template |
| Focus Mode | Contextual synthesis UI | Provenance-linked content |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | Update checklist + version history |
| Story Node structure | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Template versioning |
| UI component contracts | `web/` | Repo-defined (TBD) |
| Telemetry (if added) | `docs/telemetry/` + `schemas/telemetry/` | Schema + doc updates |

### Extension points checklist (for future work)
- [ ] UI: add/upgrade automated a11y scans in CI (tool + thresholds documented)
- [ ] UI: add component patterns for dialogs/menus/comboboxes (design docs)
- [ ] Focus Mode: add non-map equivalents for critical map interactions (list/table views)
- [ ] Telemetry: define signals for accessibility regressions (optional; governance review)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode panels and story rendering should remain keyboard-accessible and screen-reader-friendly.
- Evidence tables, citations, and supporting media should have text equivalents.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (per Story Node conventions).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (docs)
- [ ] UI a11y checks (automated; tool + severity thresholds TBD in `docs/accessibility/tooling.md`)
- [ ] Manual keyboard walkthrough for changed flows
- [ ] Screen reader sanity check for changed flows (combo(s) TBD)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (document in docs/accessibility/testing.md)
# 1) run doc lint / markdown protocol checks
# 2) run UI unit tests
# 3) run UI e2e tests
# 4) run automated accessibility scan(s)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes? TBD (align with `docs/governance/ROOT_GOVERNANCE.md`)
- What requires council/board sign-off? TBD

### CARE / sovereignty considerations
- Ensure accessibility improvements do not cause disclosure of sensitive location or culturally sensitive information via:
  - alt text
  - text-only equivalents
  - exported tables/lists
- When in doubt, follow the project’s sovereignty/redaction guidance.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial accessibility checklist | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~
