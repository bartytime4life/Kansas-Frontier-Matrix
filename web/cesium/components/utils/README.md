---
title: "Cesium UI Utilities — README"
path: "web/cesium/components/utils/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "README"
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

doc_uuid: "urn:kfm:doc:web:cesium:components:utils:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-components-utils-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:components:utils:readme:v1.0.0"
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

# Cesium UI Utilities — README

## 📘 Overview

### Purpose
This directory contains **shared utilities** used by Cesium-facing UI components under `web/cesium/`.
The goal is to keep Cesium-specific logic **consistent, testable, and reusable**, and to reduce
duplication across components.

This doc governs:
- What **belongs** in `web/cesium/components/utils/`
- What **does not** belong here (React components, state, direct data access)
- Guardrails that preserve the KFM architecture (UI consumes data via APIs; no direct graph access)

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure helpers (formatting, guards, math, coordinate transforms *as needed by UI*) | React components, hooks, pages |
| Thin adapters around Cesium primitives (small, composable) | Direct Neo4j/graph access from UI |
| Common error handling patterns for Cesium component code | Business logic owned by API layer |
| UI-side generalization/redaction helpers *when driven by API-provided flags* | Inferring sensitive locations or generating new “hidden” coordinates |

### Audience
- Primary: Frontend engineers working in `web/cesium/`
- Secondary: Reviewers validating UI boundary + governance constraints

### Definitions (link to glossary)
- Link: `../../../../docs/glossary.md`
- Terms used in this doc:
  - **UI boundary**: The frontend does not query the graph directly; it consumes contracted payloads via APIs.
  - **Cesium viewer context**: Any wrapper/state used to interact with Cesium runtime objects (viewer/scene/camera).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| KFM pipeline ordering + UI boundary | `../../../../docs/MASTER_GUIDE_v12.md` | KFM Maintainers | Canonical architecture constraints |
| Markdown doc structure standard | `../../../../docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Maintainers | This README follows Universal template |
| Cesium UI code | `../../` | UI | Components consume these utilities |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and boundaries are explicit
- [ ] No repo-unknown specifics presented as fact
- [ ] Validation steps listed and repeatable (with placeholders clearly marked)

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/components/utils/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Documentation | `docs/` | Canonical governed docs |
| Schemas | `schemas/` | Data/API/telemetry schemas (if present) |
| Frontend | `web/` | React + map clients (MapLibre/Cesium) |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms |
| Graph | `src/graph/` | Ontology bindings + graph build |
| MCP | `mcp/` | Experiments, model cards, SOPs |

### Expected file tree for this sub-area
~~~text
📁 web/
└── 📁 cesium/
    └── 📁 components/
        └── 📁 utils/
            └── 📄 README.md
            └── 📄 <utility-module>.<ts|js>            (not confirmed in repo)
            └── 📁 __tests__/                           (optional; not confirmed in repo)
                └── 📄 <utility-module>.test.<ts|js>    (not confirmed in repo)
~~~

## 🧭 Context

### Background
Cesium UI code tends to accumulate small, repeated patterns (viewer guards, safe accessors,
units conversions, defensive checks around async scene readiness). Centralizing these patterns
reduces drift and makes review easier.

### Assumptions
- Cesium is used as part of the UI mapping stack and may coexist with 2D map views.
- Utilities in this folder should remain **small** and **component-facing** (not “app domain” utilities).

### Constraints / invariants
- **Canonical pipeline ordering is preserved**: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **UI never reads Neo4j directly**; all data access is mediated through the API layer.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the preferred coordinate reference convention in UI (lon/lat vs. Cesium Cartesian)? | TBD | TBD |
| What is the preferred error/reporting pattern for Cesium runtime failures? | TBD | TBD |

### Future extensions
- Add “golden path” utility patterns for common Cesium flows (camera moves, selection, highlighting), if they remain small and composable.
- Add explicit typing contracts for utility I/O (as applicable to the repo’s chosen language/tooling).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  UI[Cesium Components] --> U[utils/ (this folder)]
  UI --> API[API Client / Fetch Layer]
  API --> SVC[KFM API Layer]
  SVC --> G[Graph + Provenance]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant C as Cesium Component
  participant U as Utils
  participant A as API Client
  participant S as KFM API

  C->>U: computeViewModel(inputs)
  C->>A: fetchFocusBundle(entity_id)
  A->>S: GET /focus/{entity_id}
  S-->>A: contracted payload (+ provenance refs, redaction flags)
  A-->>C: data for rendering
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Cesium runtime objects (viewer/scene/camera) | runtime object | Cesium integration code | Defensive null/ready checks |
| Contracted API payloads | JSON | API layer | Schema/contract tests (owned by API) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| UI-safe derived values (e.g., computed camera targets, display strings) | JS/TS values | in-memory | N/A (unit tests recommended) |

### Sensitivity & redaction
- Utilities must **not** infer or reconstruct sensitive locations.
- If the UI needs location generalization/redaction, it should rely on **API-provided flags/fields** and apply only the transformations explicitly required for presentation.

### Quality signals
- Deterministic output for deterministic inputs
- Clear behavior for null/undefined inputs (fail fast vs. safe fallback), documented per function

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: N/A (UI utilities do not generate catalogs)
- Items involved: N/A
- Extension(s): N/A

### DCAT
- Dataset identifiers: N/A
- License mapping: N/A
- Contact / publisher mapping: N/A

### PROV-O
- `prov:wasDerivedFrom`: N/A (UI utilities do not mint provenance)
- `prov:wasGeneratedBy`: N/A
- Activity / Agent identities: N/A

### Versioning
- When utility changes alter user-visible interpretation (labels, formatting), treat as a UI behavior change and document in PR notes/release notes as applicable.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
This folder may support Focus Mode by providing:
- small helpers that interpret Focus Mode UI state (e.g., “selected entity”, “active layers”) **without owning the state**
- display helpers for showing citations/provenance pointers provided by APIs

### Provenance-linked narrative rule
- Any narrative claims shown in UI must trace to dataset/record IDs; utilities should help render these references but must not fabricate them.

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
- [ ] UI lint/type checks (not confirmed in repo)
- [ ] UI unit tests for utilities (not confirmed in repo)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)
# 1) run formatter / lint
# 2) run unit tests
# 3) run markdown/doc validation
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Standard PR review for UI changes
- If a change impacts how sensitive data could be shown or generalized, follow governance and sovereignty docs referenced in front-matter.

### CARE / sovereignty considerations
- Assume some locations/events may be culturally sensitive.
- Do not add utilities that “guess” or “fill in” restricted details that the API did not provide.

### AI usage constraints
- This document permits summarization/structure extraction but prohibits generating policy or inferring sensitive locations (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for Cesium UI utilities folder | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
