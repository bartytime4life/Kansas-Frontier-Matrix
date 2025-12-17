---
title: "Accessibility Testing"
path: "docs/accessibility/testing.md"
version: "v0.1.0-draft"
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

doc_uuid: "urn:kfm:doc:accessibility:testing:v0.1.0-draft"
semantic_document_id: "kfm-accessibility-testing-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:accessibility:testing:v0.1.0-draft"
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
This document defines a **repeatable accessibility (a11y) testing workflow** for KFM’s user-facing experiences (map UI, timeline, Focus Mode, Story Nodes), with an emphasis on:
- preventing regressions during UI iteration
- producing lightweight evidence artifacts (reports + checklists)
- ensuring changes remain usable with keyboard and assistive technologies

This is **v0.1.0-draft**: several implementation details are **TBD / not confirmed in repo** and are listed explicitly as open decisions.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI behavior (keyboard, focus, labels, announcements) | Backend API contract validation (see `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |
| Map + timeline controls and their accessible alternatives | ETL, STAC/DCAT/PROV build pipelines (except how UI test artifacts are referenced) |
| Focus Mode panels, “dossier” views, Story Node rendering | Ontology changes / graph schema changes |
| Regression testing across browsers/devices (manual spot-check) | Full usability studies (covered by separate UX research processes if present) |

### Audience
- Primary: Frontend contributors / maintainers (KFM UI)
- Secondary: Designers; Story Node authors/editors; QA reviewers; governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **a11y**: Accessibility
  - **Keyboard-only**: Operable without mouse/touch
  - **Focus order**: Logical tab order + visible focus indicator
  - **Screen reader**: AT that reads UI semantics (NVDA/JAWS/VoiceOver/etc.)
  - **WCAG**: Accessibility guidelines (target level/version is **TBD / not confirmed in repo**)
  - **ARIA**: Accessibility attributes for dynamic UI (must not replace semantic HTML)

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Accessibility index | `docs/accessibility/README.md` | TBD | High-level policy + principles (create if absent) |
| **This testing guide** | `docs/accessibility/testing.md` | TBD | Process + checks + CI hooks |
| Manual checklist | `docs/accessibility/checklist.md` | TBD | Human verification steps (create if absent) |
| UI source | `web/` | Frontend | Primary surface where a11y regressions occur |
| Tests | `tests/` and/or `web/**` | TBD | Exact location depends on repo conventions |
| CI workflows | `.github/workflows/` (or equivalent) | Maintainers | CI system is **TBD / not confirmed in repo** |
| Governance | `docs/governance/*` | Governance | Applies to test data + screenshots/logs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All “must” requirements are traceable to a repo standard (or explicitly marked TBD/not confirmed)
- [ ] Validation steps listed and repeatable (local + CI)
- [ ] Explicit guidance for sensitive content in logs/screenshots
- [ ] Reviewers + approvals identified

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/testing.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | Index + testing/checklists/tooling docs |
| Frontend | `web/` | React UI, map/timeline, Focus Mode panels |
| Design | `docs/design/` | UI design notes, component usage guidance |
| Tests | `tests/` (and/or `web/**`) | Unit/integration/E2E tests (TBD) |
| CI/CD | `.github/workflows/` (or equivalent) | CI jobs that run checks (TBD) |
| Telemetry | `docs/telemetry/`, `schemas/telemetry/` | Observability + governance signals (if present) |

### Expected file tree for this sub-area
~~~text
📁 docs/
  📁 accessibility/
    📄 README.md
    📄 testing.md
    📄 checklist.md                 (TBD — create if absent)
    📄 tooling.md                   (TBD — create if absent)
    📁 reports/                     (TBD — optional, generated artifacts)
      📄 a11y-summary.md            (optional)
      📄 a11y-violations.json       (optional)
~~~

## 🧭 Context

### Background
KFM’s user interface is a modern web application intended for **interactivity and accessibility**. The frontend is described as React-based and uses open-source mapping libraries (primarily MapLibre GL JS, with Leaflet as an alternative in some cases). This makes accessibility testing particularly important for complex UI patterns (maps, sliders, layered controls, dynamic panels). *(If this frontend stack differs in the actual repo, update this section accordingly.)*

### System constraints / invariants (must hold)
- Pipeline ordering remains: ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode.
- UI obtains data via **API contracts**; no direct graph access from the browser.
- Accessibility testing must not require privileged data access.
- Any testing artifacts (logs, screenshots) must respect sensitivity rules (do not leak restricted locations).

### Open decisions (TBD / not confirmed in repo)
| Decision | Options | Default in this doc | Owner |
|---|---|---|---|
| Accessibility conformance target | WCAG 2.x A/AA/AAA | **TBD** | Governance + frontend |
| Automated toolchain | axe-core, Lighthouse, other | **TBD** | Frontend |
| E2E runner | Playwright, Cypress, other | **TBD** | Frontend |
| Browser/AT matrix | Chrome/Firefox/Safari + SRs | **TBD** | QA + frontend |
| Where reports live | CI artifacts, `docs/accessibility/reports/`, `mcp/runs/` | **CI artifacts (default)** | Maintainers |

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A[Dev makes UI change] --> B[Local checks]
  B --> C[Pull Request]
  C --> D[CI: lint + unit tests]
  D --> E[CI: automated a11y checks]
  E -->|pass| F[Manual spot-check if needed]
  E -->|fail| G[Fix violations / add issue + waiver]
  F --> H[Review + merge]
~~~

## 📦 Data & Metadata

### Inputs
- UI code changes: components, routes/panels, CSS, theming/tokens
- UI configuration affecting controls (layers, menus, Focus Mode panels)
- Story Node rendering templates (markdown → UI)

### Outputs
Accessibility testing should produce **at least one** of:
- a machine-readable violations report (preferred)
- a human-readable summary (optional)
- CI logs indicating pass/fail gates

| Output artifact | Format | Suggested location | Sensitivity | Notes |
|---|---|---|---|---|
| Violations report | JSON | CI artifact | public | Avoid embedding sensitive content in node names/labels |
| Human summary | Markdown | CI artifact or `docs/accessibility/reports/` | public | Use as PR evidence |
| Screenshots (optional) | PNG | CI artifact | **review** | Do **not** capture restricted locations/content |

### Sensitivity & redaction
- Prefer **synthetic demo data** for a11y runs (especially for map layers that might include restricted locations).
- If screenshots are enabled, ensure the test scenario does not reveal restricted sites, precise coordinates, or culturally sensitive content.
- If a UI view displays potentially sensitive info, use a redacted test fixture or disable screenshot capture for that suite.

### Quality signals
(Thresholds are **TBD / not confirmed in repo**; below is a proposed schema to adopt.)
| Severity | Meaning | Default gating behavior |
|---|---|---|
| Critical | Keyboard trap, missing name/role/value on core controls, unreadable focus state | Must fail CI |
| Serious | Missing labels, broken heading structure, contrast failures on primary text | Must fail CI (or require waiver) |
| Moderate | Non-blocking issues (minor ARIA misuse, redundant labels) | Allowed with issue filed |
| Minor | Cosmetic or edge-case | Allowed |

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Accessibility test artifacts are not geospatial assets by default. If KFM chooses to catalog CI/test artifacts:
- treat reports as *derivative artifacts* linked from the relevant software release / build (TBD)
- do not introduce a new STAC extension without governance review (**not confirmed in repo**)

### DCAT
If test artifacts are published, they can be described as distributions of a “software quality” dataset (TBD). This is optional and likely overkill unless required for audits.

### PROV-O
Recommended provenance pattern (TBD implementation):
- Each test run is a `prov:Activity` (keyed by CI run ID).
- The produced report is a `prov:Entity` with `prov:wasGeneratedBy`.
- The activity references the code revision (commit SHA) and (optionally) PR number.

## 🧱 Architecture

### Testing layers (recommended structure)
1) **Static analysis (fast)**
- JSX/HTML semantic checks (e.g., missing labels)
- Focus style requirements (no “outline: none” regressions unless replaced)
- ARIA rules (avoid invalid/duplicate IDs, incorrect roles)

2) **Component/unit tests**
- Verify key components render accessible names/labels
- Verify keyboard behavior for interactive components
- Verify Story Node renderer produces semantic markup

3) **Integration/E2E tests**
- Navigate key flows (map, timeline, Focus Mode entry/exit)
- Verify no keyboard traps
- Verify focus is managed when dialogs/panels open/close
- Optional: run an automated scanner against key pages

4) **Manual checks (targeted)**
- Keyboard-only pass for changed features
- Screen reader smoke test for key flows
- Cross-browser spot-check when UI changes are significant

### Local commands (placeholders — update to match repo)
~~~bash
# (TBD) install
npm ci

# (TBD) lint
npm run lint

# (TBD) unit tests
npm test

# (TBD) accessibility checks
npm run test:a11y

# (TBD) e2e + a11y scan
npm run e2e:a11y
~~~

### Test data strategy
- Use fixtures that resemble real UI states but contain **no sensitive locations**.
- When map/timeline is involved, use a small bounding region and non-sensitive example layers.
- Keep fixtures deterministic for CI reproducibility.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes
If Story Nodes are rendered in the UI:
- preserve semantic heading structure (H1/H2/H3 ordering)
- avoid “click here” links; use descriptive link text
- ensure images (if allowed) have alt text or are marked decorative
- ensure citations/footnotes are keyboard reachable and readable

### Focus Mode
Focus Mode is a concentrated UI experience that may contain:
- dense text panels
- data tables or feature lists
- map + timeline controls

Minimum accessibility expectations for Focus Mode UI:
- clear visible focus indicator on all interactive controls
- predictable focus order when panels open/close
- accessible names for buttons/icons
- alternative access path for map-only interactions (e.g., list view of visible features)

## 🧪 Validation & CI/CD

### CI expectations (proposed; wire to actual CI system)
- [ ] Lint passes (including accessibility lint rules if adopted)
- [ ] Unit/component tests pass
- [ ] Automated a11y checks pass on a defined set of pages/components
- [ ] Reports uploaded as CI artifacts
- [ ] Manual spot-check completed for changes affecting navigation, Focus Mode, map/timeline, or Story Node rendering

### When to require manual spot-check
Manual checks are required when a change:
- introduces/changes a navigation pattern (menus, routing, dialogs)
- changes focus management (modals, drawers, panels)
- changes map controls, timeline slider, or keyboard interactions
- changes Story Node rendering rules or citation UI

### Exception handling (waivers)
If a violation cannot be fixed immediately:
- file an issue describing:
  - affected area
  - severity
  - reproduction steps
  - remediation plan + target date
- document the waiver in the PR description
- do not ship waivers for “Critical” issues

## ⚖ FAIR+CARE & Governance

### CARE + sensitivity considerations
Accessibility testing must not weaken governance protections:
- do not capture restricted site locations in screenshots/log output
- do not add test fixtures that encode sensitive locations or culturally sensitive content
- if a UI surface is redacted/generalized by policy, tests should confirm redaction behavior rather than bypass it

### Approvals (TBD / not confirmed in repo)
Recommended reviewers:
- Frontend maintainer
- Governance reviewer (if new tooling stores artifacts publicly)
- Documentation reviewer (if user-facing behavior changes)

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-17 | Initial draft of accessibility testing workflow | TBD |
