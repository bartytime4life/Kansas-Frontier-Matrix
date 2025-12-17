---
title: "Accessibility Checklist"
path: "docs/accessibility/checklist.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Checklist"
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

doc_uuid: "urn:kfm:doc:accessibility:checklist:v1.0.0"
semantic_document_id: "kfm-accessibility-checklist-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:checklist:v1.0.0"
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

# Accessibility Checklist

## 📘 Overview

### Purpose
This document provides an implementation + review checklist for accessibility across KFM’s frontend map UI, Focus Mode, and Story Node rendering. It is intended to be used in PR reviews and release readiness checks.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI a11y for map, layers, timeline, Focus Mode, story rendering | Backend-only changes with no user-facing impact |
| Keyboard navigation, focus management, semantics, readable content | Accessibility conformance statements (VPAT / formal audits) |
| Non-leakage through accessible labels and screen-reader-only content | Organization-wide policies not owned by KFM |
| Testing guidance and CI gate suggestions | Tool procurement or vendor evaluations |

### Audience
- Primary: Frontend engineers, UI reviewers, QA, maintainers
- Secondary: Story Node authors, data product owners, governance reviewers

### Definitions
- Glossary: `docs/glossary.md`
- Terms used in this doc:
  - a11y (accessibility)
  - ARIA (Accessible Rich Internet Applications)
  - Focus Mode
  - Story Node
  - Layer registry
  - Provenance and citations
  - CARE / sovereignty redaction

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This checklist | `docs/accessibility/checklist.md` | Maintainers | PR-ready checks |
| Frontend source | `web/` | Frontend | Components + UI logic |
| Frontend UX docs | `docs/design/` | Frontend + Product | Interaction patterns |
| Story Nodes | `docs/reports/story_nodes/` | Editorial + Data | Narrative artifacts with provenance |
| Governance docs | `docs/governance/` | Governance | CARE / ethics / sovereignty rules |
| UI validation | `tests/` + `.github/workflows/` | Maintainers | Add a11y checks as needed |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Checklist sections reviewed for the change scope and results recorded in PR
- [ ] No hidden data leakage through accessible names, DOM, ARIA, tooltips, or “screen-reader only” content
- [ ] Validation steps listed are repeatable (local + CI)
- [ ] Governance and CARE/sovereignty considerations explicitly stated when relevant

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/checklist.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Governed documentation |
| Frontend | `web/` | React/Map UI, Focus Mode UX |
| Design docs | `docs/design/` | UX and interaction specs |
| Story Nodes | `docs/reports/story_nodes/` | Narrative markdown with provenance |
| Tests | `tests/` | Unit/integration/e2e tests |
| CI workflows | `.github/workflows/` | CI gates and validations |
| Schemas | `schemas/` | JSON schemas, layer registry schema, telemetry schemas |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |

### Expected file tree
~~~text
📁 docs
├── 📁 accessibility
│   └── 📄 checklist.md
~~~

## 🧭 Context

### Why accessibility matters in KFM
KFM combines dense, interactive geospatial visualization with narrative context. This creates a high-risk surface area for accessibility failures:
- Complex interactive controls (map, layers, time slider, filters)
- High information density and heavy visual reliance
- Narrative content with citations and provenance requirements
- Security and sovereignty constraints that must apply equally to visible UI and assistive-technology output

### Assumptions
- Accessibility is treated as a “must not regress” constraint for UI changes.
- Where exact conformance targets are not yet specified, this checklist defines the minimum internal expectations.

### Constraints and invariants
- Frontend remains behind APIs and contract-governed access. No direct graph access from UI.
- The layer registry and gating rules must prevent sensitive/unauthorized data from appearing anywhere in the UI, including:
  - DOM attributes
  - ARIA labels
  - Accessible descriptions
  - Offscreen / visually-hidden text
  - Tooltip or “copy link” affordances
- Focus Mode must remain provenance-linked: any displayed claim must be traceable to evidence artifacts.

### Open questions
- What external accessibility standard and conformance level should KFM formally target
- Supported assistive technology matrix for release (screen readers, browsers, mobile)
- Canonical color tokens and contrast requirements for map layers and categorical legends
- What is “minimum acceptable” for keyboard control of MapLibre/Cesium scenes versus alternative list-based navigation

### Future extensions
- Automated a11y gates in CI for UI changes
- A published accessibility statement for the KFM site
- Story Node authoring lint rules for headings, images, tables, and link text

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["Change proposal"] --> B["Implementation in web/ or docs/"]
  B --> C["Automated checks"]
  C --> D["Manual a11y checks"]
  D --> E["Governance review if sensitive"]
  E --> F["Merge and release"]
~~~

## 📦 Data & Metadata

### Inputs that commonly impact accessibility
| Input | Example | Risk |
|---|---|---|
| Layer metadata | layer names, legends, filters | Non-descriptive accessible names; color-only encoding |
| Feature properties | site name, dates, IDs | Sensitive values leaking via accessible output |
| Story Node markdown | headings, images, tables, citations | Broken heading structure; missing alt text; unreadable links |
| Time controls | slider range and labels | Inaccessible custom slider; poor keyboard support |
| Map interaction patterns | hover tooltips, click popovers | Hover-only content; focus loss; trap states |

### Outputs and required qualities
| Output | Required quality |
|---|---|
| Interactive UI | Keyboard operable, visible focus, robust semantics |
| Narrative UI | Readable structure, citations are navigable, links are descriptive |
| Map UI | Non-visual access path to key information, no hover-only gates |
| Error and loading states | Announced and recoverable, not color-only |

### Sensitivity and redaction
If any content is redacted, generalized, blurred, or gated:
- [ ] Redaction applies equally to:
  - Visual text
  - Accessible names and descriptions
  - Copy-to-clipboard content
  - URL parameters / deep links
- [ ] Screen-reader-only text does not include restricted details that are intentionally hidden visually
- [ ] “Details available on request” patterns remain accessible and do not block keyboard-only users

## 🌐 STAC, DCAT & PROV Alignment

### What this means for accessibility
Even though catalogs and provenance are data-layer concerns, the UI must surface provenance in an accessible way:
- [ ] Citations and dataset references are rendered as real, focusable links with descriptive link text
- [ ] Provenance “evidence panels” and audit trails are keyboard accessible and screen-reader readable
- [ ] Any “AI explanation” or “prediction” content is clearly labeled, opt-in where required, and includes uncertainty metadata when applicable

## 🧱 Architecture

### UI architecture considerations
- [ ] Controls have semantic HTML primitives whenever possible (button, input, select, dialog)
- [ ] Custom widgets include full keyboard interaction and ARIA roles only when necessary
- [ ] Map canvas has an adjacent, accessible pathway to key content (feature list, search results, selection summary)
- [ ] Virtualized lists are implemented in a way that remains usable with screen readers (focus does not jump unpredictably)

### Map and timeline high-risk components
- Map canvas, layer toggles, legends
- Feature inspection panel and “site dossier”
- Time slider and temporal filters
- Modal dialogs and drawers
- Focus Mode narrative + citation panel
- Audit panel and provenance UI

### Extension points checklist
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules + accessibility review
- [ ] Focus Mode: provenance references enforced + accessibility review
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- What entities become focusable:
  - [ ] Selected features and events can be reached without mouse-only interaction
  - [ ] Headings and sections in narratives are navigable by assistive tech
- What evidence must be shown:
  - [ ] Citations are present and operable
  - [ ] Evidence links are descriptive and do not rely on “click here”

### Provenance-linked narrative rule
- Every claim must trace to a dataset, record, or asset ID.

### Optional structured controls
If Story Nodes support structured focus controls, ensure they remain accessible:
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### PR accessibility checklist
Use the sections below as applicable to the change. If a section is not applicable, record “N/A” in the PR description.

#### Semantics and structure
- [ ] Page has a single H1 and logical heading order
- [ ] Landmarks are present (header, nav, main, footer) or equivalent structure
- [ ] Interactive elements are not div/span with click handlers without appropriate roles and keyboard support
- [ ] Icons have accessible names or are marked decorative as appropriate

#### Keyboard support
- [ ] All functionality is reachable and usable with keyboard only
- [ ] Tab order follows visual and logical order
- [ ] No keyboard traps
- [ ] Skip link or equivalent mechanism exists for bypassing repeated navigation

#### Focus management
- [ ] Focus is visible and meets internal visual standards
- [ ] When dialogs/panels open, focus moves into them and returns sensibly on close
- [ ] When content updates, focus does not jump unexpectedly
- [ ] Focus is not lost on map interactions, layer changes, or route changes

#### Labels, names, and instructions
- [ ] Form inputs have labels (not placeholder-only)
- [ ] Buttons and links have descriptive accessible names
- [ ] Error messages are specific, readable, and programmatically associated with inputs
- [ ] Required fields and constraints are conveyed without color-only cues

#### Color and visual encoding
- [ ] Information is not conveyed by color alone (legends include text, patterns, or icons)
- [ ] Contrast meets the project’s chosen threshold for text and UI controls
- [ ] Selected/hover states have non-color cues where feasible

#### Motion and time-based interactions
- [ ] Respects user motion preferences for fly-to animations, transitions, and autoplay
- [ ] Time slider is operable via keyboard and exposes current value in text

#### Map UI specifics
- [ ] Map controls are keyboard operable
- [ ] There is a non-map pathway to access key data (search results list, selected feature summary)
- [ ] Hover-only tooltips are not the only way to access information
- [ ] Feature selection provides an accessible text summary
- [ ] Coordinate readouts and deep links do not leak restricted location detail when redaction applies

#### Focus Mode and Story Node rendering
- [ ] Narrative content uses accessible markup: headings, lists, tables, images with alt text
- [ ] Citations are focusable, descriptive, and not truncated into meaningless labels
- [ ] Any collapsible evidence or audit sections are keyboard operable and announced to screen readers
- [ ] No “hallucinated sources” patterns appear in UI copy; provenance links are required where claims are presented

#### Performance and accessibility
- [ ] UI remains usable at reduced speed and with assistive tech enabled
- [ ] Loading states are announced and not purely spinners without text
- [ ] Large feature sets do not create focus thrash or screen-reader spam

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation where applicable (layer registry, Story Node schema)
- [ ] UI layer registry schema checks
- [ ] Accessibility checks appropriate to the change scope
- [ ] Security and sovereignty checks where applicable

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run lint
# 2) run unit tests
# 3) run e2e tests (including a11y checks if configured)
# 4) run markdown/doc lint
~~~

### Manual test matrix
- [ ] Keyboard-only navigation
- [ ] Screen reader smoke test (choose supported platform/tooling)
- [ ] Zoom to 200% and verify layout + reflow
- [ ] High contrast mode check (if applicable)
- [ ] Reduced motion preference check
- [ ] Map feature selection and Focus Mode entry without mouse

### Telemetry signals
If accessibility telemetry is added, document it here:
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- [ ] Frontend maintainers review UI changes that affect navigation, focus, map interactions, or Focus Mode
- [ ] Governance review triggered when changes impact sensitive layers, redaction, or narrative behaviors
- [ ] Security review triggered when changes affect deep links, export, copy-to-clipboard, or data exposure paths

### CARE and sovereignty considerations
- [ ] Identify impacted communities and ensure accessibility changes do not bypass redaction/generalization rules
- [ ] Ensure descriptive labels do not reveal restricted locations or sensitive attributes
- [ ] Avoid stigmatizing language in UI labels and Story Nodes; prefer neutral, evidence-led phrasing

### AI usage constraints
- [ ] Ensure this doc’s AI permissions and prohibitions match intended use

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial accessibility checklist | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
