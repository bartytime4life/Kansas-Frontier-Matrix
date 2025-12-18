---
title: "KFM Web — Cesium Components README"
path: "web/cesium/components/README.md"
version: "v0.1.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:web:cesium:components:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-components-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:components:readme:v0.1.0"
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

# KFM Web — Cesium Components

## 📘 Overview

### Purpose
- Establish conventions for components in `web/cesium/components/`.
- Ensure Cesium’s imperative API is wrapped in React components without:
  - leaking memory/resources,
  - bypassing the layer registry,
  - losing provenance handles required by Focus Mode.

### Scope
| In Scope | Out of Scope |
|---|---|
| Component conventions, lifecycle rules, data adapter patterns, click/selection patterns, testing expectations | Full app architecture (see `web/ARCHITECTURE.md`), MapLibre components, backend API implementation |

### Audience
- Primary: Frontend engineers implementing Cesium features and layers.
- Secondary: Reviewers verifying governance compliance (provenance + CARE behaviors).

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Adapter component**: Component that translates a registry entry into a Cesium DataSource/Primitive.
  - **Provenance handle**: ID(s) used to trace a rendered feature back to a source.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium subsystem overview | `web/cesium/README.md` | TBD | Registry + governance rules |
| Web architecture | `web/ARCHITECTURE.md` | TBD | Whole-UI boundaries |
| Layer registry | `web/cesium/layers/<registry>.json` | TBD | Component inputs |
| Focus Mode rules | `docs/MASTER_GUIDE_v12.md` | TBD | Provenance-only Focus Mode |

### Definition of done (for this document)
- [ ] Component lifecycle + cleanup rules defined
- [ ] Registry-driven rendering rules defined
- [ ] Click/selection contracts defined (must include provenance handle)
- [ ] Testing expectations listed

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/components/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Cesium components | `web/cesium/components/` | React wrappers and adapters |
| Cesium registry | `web/cesium/layers/` | Registry JSON + schemas |
| Focus Mode feature | `web/src/features/focus-mode/` | Focus Mode state/views (confirm actual path) |

### Expected file tree for this sub-area
~~~text
📁 web/cesium/components/
└── 📄 README.md
~~~

## 🧭 Context

### Background
- Cesium’s API is largely imperative (viewer created once; data sources added/removed).
- React componentization must manage:
  - creation and cleanup of Cesium objects,
  - controlled side-effects,
  - rendering performance.

### Assumptions
- There is a single “Cesium Viewer root” component at runtime (name not mandated).
- Layer rendering is driven from a registry entry list (not hardcoded).
- Focus Mode integration requires click events to carry provenance handles.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No ad-hoc layers: adapters must take registry entries as inputs.
- Components must:
  - clean up on unmount,
  - avoid storing large data in React state,
  - avoid rerender loops that trigger repeated Cesium add/remove.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical way to access the Cesium Viewer instance (context/provider/hook)? | TBD | TBD |
| What testing framework is used for UI unit tests and E2E tests? | TBD | TBD |
| What is the canonical “feature click → Focus Mode” contract payload? | TBD | TBD |

### Future extensions
- Shared “evidence asset” component to render STAC-linked images/charts in a side panel.
- Performance instrumentation components (layer load duration, memory/tiles count).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Registry[Layer Registry JSON] --> LayerMgr[Layer Manager]
  LayerMgr --> Adapters[Adapter Components]
  Adapters --> Cesium[Cesium Viewer]

  Cesium --> Click[Feature Click]
  Click --> Focus[Focus Mode Trigger]
  Focus --> API[Focus Mode API]
~~~

### Optional: sequence diagram (adapter lifecycle)
~~~mermaid
sequenceDiagram
  participant React as React
  participant A as Adapter Component
  participant Ces as Cesium Viewer

  React->>A: mount
  A->>Ces: create datasource/primitive + add to viewer
  React->>A: props change (registry entry toggled)
  A->>Ces: update visibility/style (no full reload if possible)
  React->>A: unmount
  A->>Ces: remove datasource/primitive + destroy resources
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Registry entry | JSON object | registry list | schema-validated |
| Viewer instance | object | viewer root | must be stable reference |
| Focus callbacks | function | Focus Mode feature | must accept provenance handle |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Cesium primitives/datasources | runtime objects | viewer | must be cleaned up |
| Click events | event payload | UI runtime | must include provenance handle |

### Sensitivity & redaction
- Adapter components must respect registry-enforced sensitivity rules:
  - do not render restricted features for public contexts,
  - generalize geometry where required (if UI handles it),
  - show warnings if required by policy.

### Quality signals
- No resource leaks (viewer remains responsive after toggling layers repeatedly).
- Clicked features produce stable IDs usable for provenance display and Focus Mode.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Adapters should treat STAC identifiers as primary inputs for resolving assets.

### DCAT
- Components that display attribution should consume DCAT-aligned metadata where available.

### PROV-O
- Click payloads should include provenance references (IDs) so that Focus Mode can cite sources.

### Versioning
- If adapter behavior changes in a way that requires registry schema changes, bump schema version and add validation tests.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: registry entry + adapter support
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Components must support:
  - “feature click → focus entity” pathways,
  - layer presets that Story Nodes can request,
  - evidence display that references STAC assets.

### Provenance-linked narrative rule
- Feature click payload must include stable provenance handles; otherwise Focus Mode must not present narrative/evidence.

### Optional structured controls
~~~yaml
focus_layers:
  - "cesium:potential_sites"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Unit tests for adapters (mount/unmount cleanup)
- [ ] Registry schema validation
- [ ] E2E: toggle layer repeatedly (no crash, no exponential slowdown)
- [ ] E2E: click feature → Focus Mode opens (when configured)
- [ ] Performance smoke: large layer loads do not freeze UI

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# cd web
# npm ci
# npm run test
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ui.cesium.adapter.mount | UI | `docs/telemetry/` + `schemas/telemetry/` |
| ui.cesium.adapter.unmount | UI | `docs/telemetry/` + `schemas/telemetry/` |
| ui.cesium.adapter.leak_suspected | UI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Any new adapter enabling a new layer type requires review for:
  - provenance completeness,
  - sensitivity behavior,
  - performance.

### CARE / sovereignty considerations
- Adapters must enforce registry sensitivity labels and default visibility rules.
- Avoid implying certainty for predictive layers; show uncertainty and provenance.

### AI usage constraints
- AI-derived layers/components must be opt-in and must expose uncertainty + sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-18 | Initial Cesium components README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`