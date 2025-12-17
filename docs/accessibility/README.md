---
title: "Accessibility — README"
path: "docs/accessibility/README.md"
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

doc_uuid: "urn:kfm:doc:accessibility:readme:v0.1.0"
semantic_document_id: "kfm-accessibility-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:accessibility:readme:v0.1.0"
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

# Accessibility — README

## 📘 Overview

### Purpose
- Provide a single entry-point for accessibility (a11y) guidance in KFM.
- Define baseline expectations for user-facing surfaces (React/Map UI, Story Nodes, Focus Mode) and how accessibility is validated in CI/CD.

### Scope
| In Scope | Out of Scope |
|---|---|
| Web UI accessibility (React UI, map controls, timeline controls, modals/panels) | Third-party site accessibility (external links / external viewers) |
| Story Nodes + Focus Mode presentation (narratives, citations, media, controls) | Non-user-facing services (internal-only pipelines) |
| Docs/content accessibility (Markdown structure, images, tables) | Accessibility conformance certification processes (unless added later) |
| A11y testing strategy + “definition of done” for UI changes | Product support/IT device accommodation policies |

### Audience
- Primary: Frontend engineers, UI/UX designers, Story Node authors/editors
- Secondary: API engineers (to preserve accessible content contracts), data engineers (to preserve provenance + redaction), QA reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (non-exhaustive): accessibility (a11y), WCAG, WAI-ARIA, accessible name, focus order, keyboard trap, reduced motion, contrast, screen reader

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline “source of truth” |
| UI codebase | `web/` | TBD | React + map clients (MapLibre/Cesium as applicable) |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | TBD | Narrative + evidence structure |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | TBD | Governs structure of this document |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | TBD | Review gates + compliance references |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | TBD | Redaction + protection rules (must apply to a11y surfaces too) |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All actionable guidance is linked to repo artifacts (components, docs, schemas) where possible
- [ ] Validation steps listed and repeatable (even if some commands remain placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Accessibility docs | `docs/accessibility/` | A11y guidance, checklists, test notes |
| Documentation | `docs/` | Canonical governed docs |
| Frontend | `web/` | React + map clients |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Telemetry | `docs/telemetry/` | Telemetry conventions and signals (if used) |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |
| Templates | `docs/templates/` | Governed doc templates |

### Expected file tree for this sub-area
~~~text
📁 docs/
  📁 accessibility/
    📄 README.md
    📄 checklist.md                # (future) Quick, practical UI checklist
    📄 testing.md                  # (future) Manual + automated testing guide
    📁 patterns/                   # (future) Reusable UI patterns for KFM
      📄 map-controls.md
      📄 timeline-controls.md
      📄 modal-and-sidepanel.md
      📄 story-node-content.md
~~~

## 🧭 Context

### Background
- KFM’s UI includes interactive maps, a time slider/timeline, layer toggles, and narrative story surfaces. These are powerful—but can become inaccessible without deliberate keyboard, focus, and screen-reader support.
- This folder exists so accessibility expectations are documented once and reused across UI work (including Story Nodes and Focus Mode).

### Assumptions
- KFM’s primary UI is a web app (React) with an interactive map component and time-based navigation.
- Accessibility is treated as a product quality requirement (not a one-time audit).
- Automated tests will catch some issues, but manual keyboard and screen-reader checks are still necessary.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Provenance and redaction rules must apply to *all* UI surfaces, including:
  - visible text,
  - ARIA labels / accessible names,
  - alt text,
  - “sr-only” content,
  - downloadable exports.

### Accessibility baseline (project guidance)
- **Keyboard first**: every core interaction must be operable without a mouse.
- **No keyboard traps**: focus can always move forward/backward and escape modals/panels.
- **Predictable focus**: opening a modal/panel moves focus inside; closing returns focus to the launcher.
- **Accessible names**: interactive controls have programmatic names (labels/ARIA) that match what users see.
- **Meaning beyond color**: status/selection is not conveyed by color alone (add text/icons/patterns).
- **Reduced motion**: respect user preferences when adding animation (timeline “play”, fly-to, etc.).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What WCAG target level (if any) will KFM adopt as a formal goal? | TBD | TBD |
| Which automated tooling is standardized for CI (axe, Lighthouse, Playwright-a11y, etc.)? | TBD | TBD |
| What “non-map alternative view” is required for key workflows (search, filter, compare, export)? | TBD | TBD |
| How will we represent redacted/generalized locations accessibly (text + map + SR output)? | TBD | TBD |

### Future extensions
- Extension point D (APIs): add fields that improve a11y (e.g., explicit titles, summaries, alt-text-ready captions) without coupling UI to the graph.
- Extension point E (UI): implement reusable accessible patterns for map controls, timelines, modals, and Story Node panels.
- Extension point F (Telemetry): capture aggregate a11y quality signals (counts, regression detection), without logging sensitive user data.

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
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as UI (Accessible controls)
  participant API as API
  participant Graph as Graph

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| UI components + styles | TS/TSX/CSS | `web/` | Lint + unit/integration tests (repo-specific) |
| Story Node content | Markdown | Story Node sources under `docs/` (location TBD) | Markdown protocol checks + template validation |
| Catalog metadata surfaced in UI (labels/titles) | JSON (via API) | `src/` services via `web/` consumers | Contract tests + UI smoke tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Accessible UI behaviors | Web app runtime | `web/` build output | UI contracts + component APIs |
| A11y test artifacts (reports) | JSON/HTML (tool-specific) | (TBD) `mcp/runs/` or CI artifacts | Tool-defined |
| Accessibility docs | Markdown | `docs/accessibility/` | KFM-MDP + template compliance |

### Sensitivity & redaction
- If a location is generalized/blurred due to sovereignty or safety policies, ensure:
  - any accessible names and alt text reflect the generalized form,
  - no hidden DOM content leaks exact coordinates or restricted place names,
  - exports respect the same redaction rules.

### Quality signals
- Automated: count of new a11y violations (tool-specific), lighthouse accessibility score trend (optional)
- Manual: keyboard walkthrough completed for core screens; at least one screen-reader spot-check for major UI changes

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: (TBD)
- Items involved: (TBD)
- Extension(s): (TBD)
- Accessibility note: when rendering thumbnails/previews from STAC assets, provide meaningful text alternatives and ensure controls for media (if any) are accessible.

### DCAT
- Dataset identifiers: (TBD)
- License mapping: (TBD)
- Contact / publisher mapping: (TBD)
- Accessibility note: dataset titles/descriptions used in UI should be human-readable and usable as accessible labels.

### PROV-O
- `prov:wasDerivedFrom`: (TBD)
- `prov:wasGeneratedBy`: (TBD)
- Activity / Agent identities: (TBD)
- Accessibility note: provenance indicators must not be “icon-only”; provide text labels and screen-reader access to citations/lineage.

### Versioning
- Track doc revisions in “Version History” below.
- For UI changes that affect accessible behavior, capture the change in PR description and (when applicable) add or update an accessibility test.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests (if accessibility requires new fields)
- [ ] UI: layer registry entry + access rules (including accessible names/labels)
- [ ] Focus Mode: provenance references enforced (accessible presentation)
- [ ] Telemetry: new signals + schema version bump (if added)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities (examples): Story Nodes, dataset layers, map features, time range selections.
- Evidence that must be shown accessibly:
  - citations/provenance links,
  - uncertainty flags and governance warnings,
  - any redaction/generalization notices.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (and be presented in a way that is accessible to screen readers and keyboard users).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI lint/tests (repo-specific)
- [ ] Accessibility automated checks (tooling TBD)
- [ ] Keyboard navigation manual check for affected screens
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) docs: run markdown protocol checks
# <TBD: command(s)>

# 2) web: run unit/integration tests
# <TBD: command(s)>

# 3) web: run accessibility checks (e.g., axe/lighthouse/playwright-a11y)
# <TBD: command(s)>
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| a11y_violation_count | CI a11y tool (TBD) | `docs/telemetry/` + `schemas/telemetry/` |
| keyboard_nav_regression | QA checklist (TBD) | (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes? TBD
- What requires council/board sign-off? TBD

### CARE / sovereignty considerations
- Accessibility content must not create a side-channel that reveals protected information (especially precise locations or restricted place names).
- If the UI includes “blurred” or generalized map representations, the accessible equivalent must also be generalized.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not auto-generate accessibility “policy” statements without governance review (add proposals as TBD and route through the documented review gate).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-17 | Initial accessibility README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
