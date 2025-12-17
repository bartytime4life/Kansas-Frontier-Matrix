---
title: "Accessibility Testing"
path: "docs/accessibility/testing.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:accessibility:testing:v1.0.0"
semantic_document_id: "kfm-accessibility-testing-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:testing:v1.0.0"
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

# Accessibility Testing

## 📘 Overview

### Purpose
- Define *how KFM tests accessibility* across the **React/Map UI**, **Story Nodes**, and **Focus Mode** experiences.
- Provide a repeatable approach (manual + automated) that can be used in local development and CI.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI accessibility (keyboard, focus, semantics, contrast, motion, zoom) | Defining new governance policy (handled in governance docs) |
| Story Node + Focus Mode accessibility (narrative, citations, audit panels) | Underlying data correctness (covered by data QA / schema validation) |
| Accessibility of documentation in `docs/` (readability, diagrams, alt text expectations) | Security testing (covered by `docs/security/`) |

### Audience
- Primary: frontend engineers, UI/UX designers, maintainers, QA.
- Secondary: story node authors/editors, governance reviewers, contributors.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): accessibility (a11y), assistive technology (AT), keyboard trap, focus order, accessible name, semantic HTML, ARIA (when needed).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Accessibility docs index | `docs/accessibility/README.md` | Maintainers | Entry point + conventions |
| Accessibility tooling | `docs/accessibility/tooling.md` | Maintainers | Tools + local setup + CI hooks |
| Frontend UI | `web/` | Frontend | Map UI + Focus Mode UX |
| Design docs | `docs/design/` | Design/Frontend | UX and UI contracts |
| Story Nodes | `docs/reports/visualization/focus_mode/story_nodes/` | Narrative | Versioned narrative artifacts |
| Tests | `tests/` | Eng | Automated checks (location may vary by test type) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Scope includes Map UI + Story Nodes + Focus Mode surfaces
- [ ] Manual checklist included and actionable
- [ ] Automated testing approach described (without assuming specific tools unless confirmed)
- [ ] Validation steps listed and repeatable (with placeholders where repo commands differ)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/testing.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | Standards + guides for inclusive UX |
| Frontend | `web/` | React + map clients + Focus Mode UX |
| Design docs | `docs/design/` | UI specs, interaction patterns |
| Tests | `tests/` | Automated test suites (unit/e2e/contract) |
| CI workflows | `.github/workflows/` | CI/CD pipelines + gates |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Observability + governance metrics |

### Expected file tree for this sub-area
~~~text
📁 docs/
  📁 accessibility/ ♿
    📄 README.md
    📄 tooling.md
    📄 testing.md
    📄 checklists.md                (optional; if split from testing.md)
    📁 reports/                     (optional; generated artifacts)
      📄 a11y-audit-YYYY-MM-DD.md
      📄 a11y-audit-YYYY-MM-DD.json
~~~

## 🧭 Context

### Background
- KFM’s UI includes a map-driven experience (map, timeline, layer controls) plus narrative experiences (Story Nodes, Focus Mode). These surfaces are high-interaction and must remain usable via keyboard, screen readers, and low-vision accommodations.

### Assumptions
- The frontend is built as a modern web application (React + mapping libraries).
- Map interactions may include WebGL/canvas-based rendering, which typically requires additional accessible affordances (e.g., equivalent controls and accessible feature details panels).
- KFM Story Node and Focus Mode content is provenance-led and includes citations/audit affordances.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode ordering is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Sovereignty/redaction rules (masking/generalization/omission) must remain effective even for AT users.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Target accessibility standard / level (e.g., WCAG version + conformance) | Governance + Frontend | TBD |
| Supported browsers + supported AT (screen readers, OS combinations) | Frontend | TBD |
| Automated a11y gate behavior in CI (fail on new issues vs warn) | Maintainers | TBD |
| Where to store a11y audit artifacts (docs vs telemetry vs releases) | Maintainers | TBD |

### Future extensions
- Add an accessibility “quality signal” into release telemetry (counts, severity, regressions).
- Maintain a small set of golden-path user tasks and require them to pass accessibility checks (keyboard + AT).
- Expand Story Node authoring lint to catch structural issues before ingestion.

## 🗺️ Diagrams

### System / dataflow diagram (testing focus)
~~~mermaid
flowchart LR
  Dev["Developer / Contributor"] --> PR["Pull Request"]
  PR --> CI["CI Gates (lint/tests/build)"]
  CI --> Preview["Preview Deploy (if enabled)"]
  Preview --> Manual["Manual A11y Review (keyboard/AT)"]
  Manual --> Merge["Merge"]
  Merge --> Release["Release / Publish"]
~~~

### Optional: sequence diagram (UI accessibility review loop)
~~~mermaid
sequenceDiagram
  participant Reviewer
  participant UI as KFM UI (Preview)
  participant Notes as A11y Notes/Checklist
  Reviewer->>UI: Navigate with keyboard only
  UI-->>Reviewer: Visible focus + usable controls
  Reviewer->>UI: Screen reader pass (key flows)
  UI-->>Reviewer: Correct labels/roles/state changes
  Reviewer->>Notes: Record issues + severity + repro steps
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Frontend UI | React/JS/TS + CSS | `web/` | build + tests |
| Story Nodes | Markdown | `docs/reports/visualization/focus_mode/story_nodes/` | template + content checks |
| UI catalogs (layer registry, etc.) | JSON | pipeline outputs | schema checks + UI parsing |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Automated a11y report (optional) | JSON/HTML/MD | `docs/accessibility/reports/` (or CI artifact store) | not confirmed in repo |
| Manual audit checklist | Markdown | `docs/accessibility/reports/` | this doc’s checklist |
| Issues / tickets | N/A | tracker | N/A |

### Sensitivity & redaction
- A11y artifacts **must not** contain sensitive coordinates, protected site identifiers, or screenshots that reveal redacted content.
- If screenshots are used for accessibility defect reports, verify masking/generalization remains in effect in the screenshot.

### Quality signals
- Zero keyboard traps in golden-path flows.
- No missing accessible names for primary controls (timeline, layer toggles, modal dialogs).
- Focus indicators visible for all focusable controls.
- No regressions in “critical” accessibility defects (definition below).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Not applicable for this document directly (this is a UI/testing guide).

### DCAT
- Not applicable for this document directly.

### PROV-O
- Optional (recommended): treat accessibility audits as provenance-linked evidence of UI quality.
  - `prov:Entity`: audit report artifact
  - `prov:Activity`: CI run / manual review session
  - `prov:Agent`: reviewer or CI system identity (as appropriate)

### Versioning
- Keep this document versioned via front-matter `version`.
- If accessibility gate rules change, record in Version History and link to the related CI/workflow change.

## 🧱 Architecture

### Accessibility testing layers (recommended)
1) **Static / author-time checks**
   - Catch obvious issues early (e.g., missing labels, incorrect semantics, invalid Story Node structure).
2) **Component-level tests**
   - Validate key components: Timeline slider, Layer toggles, dialogs/modals, citation widgets.
3) **End-to-end task tests**
   - Validate golden-path workflows (keyboard-only and AT-oriented checks).
4) **Manual audits**
   - Required for high-interaction surfaces: map UI, timeline interactions, Focus Mode dashboards.

### Test coverage matrix (minimum suggested)
| Surface | Keyboard | Screen reader | Contrast & zoom | Notes |
|---|---:|---:|---:|---|
| Map view (canvas) | ✅ | ⚠️ | ✅ | Requires accessible affordances (details panel, shortcuts) |
| Timeline slider | ✅ | ✅ | ✅ | Must announce value changes and have a label |
| Layer controls | ✅ | ✅ | ✅ | Toggles must have names + state |
| Popups/modals | ✅ | ✅ | ✅ | Focus trap + ESC close + restore focus |
| Story Node page | ✅ | ✅ | ✅ | Heading structure + link text + citations |
| Focus Mode | ✅ | ✅ | ✅ | Audit panel + evidence/citations must be accessible |

Legend: ✅ expected; ⚠️ higher-risk surface (requires extra attention and potentially specialized testing).

## 🧠 Story Node & Focus Mode Integration

### Story Nodes
Accessibility expectations for Story Nodes:
- Heading hierarchy is meaningful (H1 → H2 → H3, no skipping for visual style).
- Links are descriptive (citation links are distinguishable and usable via keyboard).
- Images/figures include text alternatives appropriate to the sensitivity context.

Testing steps:
- Verify Story Node content renders with:
  - correct reading order
  - usable keyboard navigation
  - citations as accessible links (not only icons)

### Focus Mode
Accessibility expectations for Focus Mode:
- Users can reach all controls and panels via keyboard.
- Evidence/citation interactions are accessible (focusable, labeled, and do not depend on hover-only UI).
- Audit/governance flags are conveyed without relying solely on color.

Testing steps:
- Keyboard-only pass of: enter Focus Mode → read narrative → open citations → return to map → exit Focus Mode.
- Screen reader pass of: navigate headings/regions → activate citations → interpret audit panel states.

## 🧪 Validation & CI/CD

> Note: exact commands depend on the repo’s package manager and test runner. Use `docs/accessibility/tooling.md` for the repo-confirmed commands.

### Local validation checklist
- [ ] Build frontend locally (no console errors that affect assistive tech)
- [ ] Run unit/component test suite
- [ ] Run any configured accessibility lint/check
- [ ] Perform the manual keyboard checklist below on the key flows you touched

### CI validation (recommended gates)
- [ ] Frontend build succeeds
- [ ] Tests succeed
- [ ] UI schema checks succeed (e.g., layer registry parsing)
- [ ] Accessibility check step (automated) runs and publishes a report artifact (if enabled)

### Manual keyboard checklist (minimum)
1) **Global navigation**
   - Can you reach primary navigation and main content without a mouse?
   - Is there a visible focus indicator at all times?
2) **Timeline**
   - Can you move the timeline value with keyboard controls?
   - Is the current value communicated (visually and semantically)?
3) **Layers**
   - Can you toggle layers with keyboard?
   - Do toggles have clear names and state?
4) **Dialogs**
   - When a modal opens, focus moves into it.
   - You can close via keyboard, and focus returns to the element that launched it.
5) **Map interactions**
   - If the map canvas cannot be fully operated by keyboard, confirm there is an accessible alternative for core tasks:
     - selecting an entity
     - opening its details
     - navigating evidence/citations

### Example placeholder commands
~~~bash
# Replace <pm> with the repo’s package manager (npm/pnpm/yarn) and <script> with actual scripts.
<pm> run build
<pm> test
<pm> run lint
# Optional (if configured):
<pm> run test:a11y
~~~

### Defect reporting guidance
When filing accessibility issues, include:
- Steps to reproduce (keyboard-only steps if possible)
- Expected vs actual behavior
- Affected surface (Map / Timeline / Layers / Story Node / Focus Mode)
- Severity (suggested):
  - Blocker: prevents completing a primary flow (keyboard trap, cannot activate primary control)
  - High: major usability barrier (focus lost, modal not reachable)
  - Medium: noticeable but workaround exists
  - Low: minor issue

## ⚖ FAIR+CARE & Governance

- Accessibility is part of making KFM usable and beneficial to a broad audience (Collective Benefit).
- Sovereignty and redaction rules must not be bypassable via accessibility layers:
  - Do not expose restricted data via hidden labels, `aria-label`s, or off-screen text.
  - Ensure masked/generalized values are the only values present in the DOM.
- Avoid “color-only” encoding for governance flags, warnings, or sensitivity indicators—use text + icons + semantics.

## 🕰️ Version History

| Version | Date | Summary |
|---|---:|---|
| v1.0.0 | 2025-12-17 | Initial accessibility testing guide (draft) |
