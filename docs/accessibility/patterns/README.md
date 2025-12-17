---
title: "Accessibility Patterns — README"
path: "docs/accessibility/patterns/README.md"
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

doc_uuid: "urn:kfm:doc:accessibility:patterns:readme:v1.0.0"
semantic_document_id: "kfm-accessibility-patterns-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:accessibility:patterns:readme:v1.0.0"
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

# Accessibility Patterns — README

## 📘 Overview

### Purpose
- This README is the index + contribution guide for KFM accessibility (a11y) patterns.
- It defines how KFM documents, implements, and validates accessible interaction patterns across the **UI → Story Nodes → Focus Mode** layer of the pipeline.

### Scope
| In Scope | Out of Scope |
|---|---|
| UI interaction patterns (keyboard, focus, ARIA, screen-reader affordances) | Backend feature development (unless it impacts UI accessibility contracts) |
| Map + timeline + layer-control accessibility patterns | ETL/catalog/graph implementation details (covered elsewhere) |
| Evidence/provenance presentation patterns (citations, disclosure, audit affordances) | Non-governed “style opinions” not tied to accessibility outcomes |
| a11y validation approach (manual + automated, where available) | Formal compliance certification (unless explicitly adopted by governance) |

### Audience
- Primary: Frontend engineers (React/map UI), UX designers
- Secondary: Story Node authors/editors, QA/testers, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: a11y, focus order, focus trap, accessible name, landmark regions, ARIA, Story Node, Focus Mode, provenance, redaction/generalization

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| System pipeline + subsystem “do not break” rules | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline order + UI/Focus Mode constraints |
| Governance + ethics + sovereignty rules | `docs/governance/` | Governance | Applies to public UX and sensitive-location handling |
| Accessibility patterns (this area) | `docs/accessibility/patterns/` | UI + Docs maintainers | Each pattern is a governed doc |
| Frontend UI implementation | `web/` | UI | Apply patterns in components + interaction models |
| Tests and checks (if present) | `tests/` + `.github/` | QA + Maintainers | a11y checks should be deterministic + CI-clean |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Patterns index present (with clear “planned vs implemented” status)
- [ ] Pattern docs specify: problem, users affected, interaction contract, anti-patterns, validation steps
- [ ] Governance + CARE/sovereignty considerations explicitly stated (esp. for maps + sensitive places)
- [ ] Validation steps listed and repeatable (manual steps always; automated where available)

### Patterns index
> Note: Pattern files listed as **(planned)** are scaffolding targets and may not exist yet.

| Pattern | File | Status | Applies to | Notes |
|---|---|---:|---|---|
| Pattern authoring guide | `pattern-template.md` | planned | Docs | Standardizes how to write new patterns |
| Keyboard navigation + focus management | `keyboard-focus-and-navigation.md` | planned | UI | Tab order, roving tabindex, focus restoration |
| Panels, modals, toasts | `panels-modals-toasts.md` | planned | UI | Focus trapping rules, dismissal, announcements |
| Map controls (MapLibre/Cesium) | `map-controls.md` | planned | UI | Keyboard alternatives for pan/zoom/layers |
| Timeline + time controls | `timeline-and-time-controls.md` | planned | UI | Sliders, scrubbing, time-range selection |
| Color/contrast + symbology | `color-contrast-and-symbology.md` | planned | UI | Contrast, non-color cues, legend semantics |
| Data viz accessibility | `data-visualization.md` | planned | UI | Text equivalents, table fallbacks, descriptions |
| Citations + provenance presentation | `citations-and-provenance.md` | planned | Story Nodes + Focus Mode | Evidence is readable + navigable |
| Testing + tooling | `testing-and-tooling.md` | planned | UI + QA | Manual steps + optional automation hooks |

## 🗂️ Directory Layout

### This document
- `path`: `docs/accessibility/patterns/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Accessibility docs | `docs/accessibility/` | a11y standards, patterns, checklists |
| UI | `web/` | React + map clients |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Tests | `tests/` | Unit/integration/e2e tests |
| CI | `.github/` | CI workflows and gates |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 accessibility/
    └── 📁 patterns/
        ├── 📄 README.md
        ├── 📄 pattern-template.md                 (planned)
        ├── 📄 keyboard-focus-and-navigation.md    (planned)
        ├── 📄 panels-modals-toasts.md             (planned)
        ├── 📄 map-controls.md                     (planned)
        ├── 📄 timeline-and-time-controls.md       (planned)
        ├── 📄 color-contrast-and-symbology.md     (planned)
        ├── 📄 data-visualization.md               (planned)
        ├── 📄 citations-and-provenance.md         (planned)
        └── 📄 testing-and-tooling.md              (planned)
~~~

## 🧭 Context

### Background
- KFM’s delivery pipeline culminates in a public-facing UI (map + narrative) and Focus Mode experiences.
- Accessibility patterns ensure KFM’s interactive exploration is usable by keyboard-only users, screen-reader users, and users with low vision or cognitive load constraints.
- This folder is meant to prevent “one-off” accessibility implementations by documenting **repeatable patterns**.

### Assumptions
- UI is built as a client that consumes data via APIs (and does not couple directly to the graph store).
- Map + timeline + layer controls are core interactive surfaces and must have accessible alternatives.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- UI must include a11y + audit affordances and must not leak hidden/sensitive data through UI behaviors.
- Focus Mode must remain provenance-linked; predictive/uncertain content (if present) must be clearly labeled and user-controlled.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Target accessibility standard/level (e.g., WCAG conformance target) — **not confirmed in repo** | TBD | TBD |
| Canonical a11y tooling stack (linting, e2e, axe checks) — **not confirmed in repo** | TBD | TBD |
| Map keyboard interaction contract (pan/zoom/feature inspection) | TBD | TBD |

### Future extensions
- Add a dedicated **pattern template** document that standardizes required sections for each pattern.
- Add repo-integrated automated a11y checks (where tooling exists) and a CI gate policy for regressions.
- Add “known exceptions” register (explicitly justified + time-bounded).

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

  P[Accessibility Patterns] --> E
  P --> F
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant UI
  participant API

  User->>UI: Keyboard navigation / screen reader interaction
  UI->>API: Fetch contracted content (with redaction rules)
  API-->>UI: Narrative + citations + audit flags
  UI-->>User: Accessible controls + provenance-linked content
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Accessibility requirements | Text | Governance + UX decisions | Review + sign-off (as applicable) |
| UI interaction specs | Markdown/design docs | UI/UX | Peer review |
| Audit findings | Issues/notes | QA + community feedback | Triage + reproduction steps |
| Components + UI states | Code | `web/` | Tests + manual checks |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Pattern docs | Markdown | `docs/accessibility/patterns/*.md` | Markdown protocol validation |
| Checklists | Markdown | `docs/accessibility/` | Markdown protocol validation |
| Test steps | Markdown | `docs/accessibility/patterns/testing-and-tooling.md` | Deterministic + repeatable |

### Sensitivity & redaction
- Pattern examples must not include precise sensitive locations or restricted details.
- If examples must reference sensitive domains, they should demonstrate **generalization** and **disclosure controls** (and remain consistent with sovereignty policy).

### Quality signals
- Keyboard-only completion of core flows (no mouse required).
- No focus traps; focus visibly indicated; focus restoration on close/route change.
- Accessible names/roles/states for interactive controls.
- Citations/provenance content is navigable and readable by assistive tech.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: TBD (pattern docs are not STAC assets by default)
- Items involved: UI patterns should support displaying STAC item IDs/asset labels in accessible ways
- Extension(s): TBD

### DCAT
- Dataset identifiers: UI patterns should support readable dataset IDs, licenses, and publishers (where surfaced)
- License mapping: ensure license display is not “visual-only” (screen-reader accessible text)

### PROV-O
- Ensure provenance references (derivation/activity/agent) can be rendered in accessible disclosure widgets.
- Avoid “hover-only” provenance; provide keyboard + screen-reader accessible expansion.

### Versioning
- Treat pattern docs as versioned governed documents; track changes via Version History and commit history.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Story Node rendering must preserve semantic structure (headings, lists, tables) and keep citations navigable.
- Focus Mode controls (layer toggles, time selection, evidence expansion) must be operable with keyboard and readable with assistive tech.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (and must remain accessible to users consuming via assistive tech).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI keyboard navigation smoke test (manual)
- [ ] Screen-reader smoke test (manual)
- [ ] Map controls: keyboard operability + alternative affordances (manual)
- [ ] Focus Mode: citations/provenance discoverable without hover (manual)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run doc lint / markdown protocol validation
# 2) run UI tests
# 3) run any configured a11y checks (if present)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes that affect how sensitive locations or culturally sensitive narratives are displayed require governance review.
- Major UI interaction changes that affect Focus Mode evidence presentation should be reviewed for auditability and accessibility impact.

### CARE / sovereignty considerations
- Accessibility must not conflict with sovereignty protections: “more accessible” must not mean “more revealing.”
- Provide accessible explanations of why content is generalized/redacted when applicable.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use (no policy generation; no inference of sensitive locations).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial accessibility patterns README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
