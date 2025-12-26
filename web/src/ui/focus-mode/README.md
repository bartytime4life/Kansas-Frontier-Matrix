---
title: "KFM Focus Mode UI — README"
path: "web/src/ui/focus-mode/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:ui:focus-mode:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-ui-focus-mode-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:ui:focus-mode:readme:v0.1.0-draft"

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

# KFM Focus Mode UI — README

## 📘 Overview

### Purpose

This README governs **Focus Mode UI** within the KFM web client. It defines:

- What belongs in `web/src/ui/focus-mode/` and how this folder is owned.
- The **non‑negotiable invariants** for Focus Mode rendering:
  - **provenance-linked content only** (no uncited facts),
  - **API boundary enforced** (UI never reads the graph directly),
  - **opt‑in predictive/AI content** with **uncertainty/confidence metadata**,
  - **redaction/generalization respected** to prevent sensitive location leakage.

### Scope

| In Scope | Out of Scope |
|---|---|
| Focus Mode UI components, state orchestration, and rendering rules | ETL/crawlers, catalog generation, Neo4j ingest/ontology changes |
| Consuming Story Nodes + contracted Focus context payloads | Defining API contracts themselves (belongs under `src/server/contracts/**`) |
| Rendering citations / provenance links (STAC/DCAT/PROV IDs) | Authoring Story Node narrative content (belongs under `docs/reports/story_nodes/**`) |
| UX affordances for audit/redaction notices and evidence inspection | Governance policy authoring (belongs under `docs/governance/**`) |

### Audience

- Primary: Frontend contributors working under `web/`.
- Secondary: API + graph contributors ensuring contracts support Focus Mode; narrative curators reviewing Focus Mode behavior.

### Definitions

- Link: `docs/glossary.md` (**not confirmed in repo**).
- Terms used in this doc:
  - Focus Mode, Story Node v3, context bundle, provenance, redaction/generalization, layer registry, evidence IDs (STAC/DCAT/PROV).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | KFM core | Canonical pipeline + invariants |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM core | This README conforms to this template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Front-matter fields + evidence/citation rules |
| v13 redesign blueprint (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Evidence-first + contract-first + canonical paths |
| Story Nodes (canonical) | `docs/reports/story_nodes/**` | Curators | Draft/published narrative artifacts |
| API contracts | `src/server/contracts/**` | API | Contract tests + semver requirements |
| UI schemas | `schemas/ui/**` | Platform/UI | Layer registry schema validation |
| Story Node schemas | `schemas/storynodes/**` | Platform/Narrative | Story node schema validation |
| Catalogs + provenance | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Data/Catalog | Evidence products consumed downstream |

> Note: Some paths above may be **not confirmed in repo** for your current checkout. The v13 blueprint explicitly targets canonicalization and deduplication.

### Definition of done (for this document)

- [ ] Front-matter complete + `path:` matches file location
- [ ] Focus Mode invariants clearly stated (API boundary, provenance-only, opt-in AI)
- [ ] Directory ownership and recommended sub-structure documented
- [ ] Validation steps listed and repeatable
- [ ] Governance/CARE/sovereignty considerations included
- [ ] Footer refs present

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/focus-mode/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | Front-end application code (React + map client), including Focus Mode UI |
| UI schemas | `schemas/ui/**` | JSON Schemas for UI registries (layer registry, etc.) |
| Story nodes | `docs/reports/story_nodes/**` | Curated narratives, evidence-linked |
| Story node schemas | `schemas/storynodes/**` | Validation for Story Node v3 artifacts |
| API contracts | `src/server/contracts/**` | REST/GraphQL contracts + contract tests |
| Provenance | `data/prov/**` | Provenance bundles; referenced in audits and Focus Mode evidence panels |
| Catalogs | `data/stac/**`, `data/catalog/dcat/**` | Evidence artifacts referenced by story nodes and API |

### Expected file tree for this sub-area

> **Recommended structure.** Some folders may not exist yet (**not confirmed in repo**). Keep Focus Mode code isolated here.

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        └── 📁 focus-mode/
            ├── 📄 README.md
            ├── 📁 components/           # FocusMode shell + panels (recommended)
            ├── 📁 hooks/                # focus data fetching + orchestration hooks (recommended)
            ├── 📁 state/                # reducers/context + selectors (recommended)
            ├── 📁 adapters/             # API payload → view models (recommended)
            ├── 📁 rendering/            # markdown + citation rendering (recommended)
            ├── 📁 telemetry/            # Focus Mode interaction events (optional)
            └── 📁 __tests__/            # unit/integration tests (recommended)
~~~

---

## 🧭 Context

### Canonical pipeline placement

Focus Mode sits at the end of the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This ordering is a contract: Focus Mode is downstream of catalogs, graph, and API contracts.

### Focus Mode intent

Focus Mode is a **specialized UI state** used to “deep dive” into a single story or entity while still preserving broader context (map, timeline, related links). It should feel immersive while remaining academically traceable.

### Constraints and invariants

**Non-negotiables (must hold for every Focus Mode view):**

1. **API boundary only**
   - UI does not connect to Neo4j/graph directly.
   - All data arrives via contracted APIs (REST/GraphQL).

2. **Provenance-linked only**
   - Focus Mode must only display content that includes resolvable evidence/provenance.
   - If something has no source, it should not render as fact.

3. **Opt-in predictive/AI content**
   - Predictive/AI narrative content is off by default.
   - If enabled, it must be clearly labeled as machine-generated and include uncertainty/confidence metadata.

4. **Sensitivity, redaction, and sovereignty**
   - If a response includes redaction flags or generalized geometry, the UI must honor them.
   - The UI must not allow user interactions (zoom, inspect, export) to reveal restricted precision beyond what governance permits.

### Open questions (track in issues)

- What is the canonical Focus API endpoint shape and versioning strategy? (**not confirmed in repo**)
- Where is the layer registry stored and how is it validated at build time? (**not confirmed in repo**)
- What telemetry sink/schema is required for Focus Mode events? (**not confirmed in repo**)

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["ETL + normalization"] --> B["STAC/DCAT/PROV outputs"]
  B --> C["Graph (Neo4j ingest)"]
  C --> D["API (contracts + redaction)"]
  D --> E["UI (web/)"]
  E --> F["Story Nodes (curated narrative)"]
  F --> G["Focus Mode (provenance-linked view)"]
~~~

### Sequence diagram (Focus Mode context query)

~~~mermaid
sequenceDiagram
  participant UI as UI (Focus Mode)
  participant API as API (Focus endpoint)
  participant Graph as Graph (Neo4j)
  UI->>API: Focus query(entity_id, options)
  API->>Graph: fetch subgraph + provenance refs
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit/redaction flags
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Evidence-first narrative rule

- Story Nodes must be written so that **every factual claim** is evidence-linked.
- Focus Mode must only surface **provenance-linked** content (no hallucinated sources).

### Story Node fields that can drive UI focus

Story Node v3 allows optional “focus controls” that can guide the UI:

~~~yaml
focus_layers:
  - "<domain>:<layer-id>"
focus_time: "<iso8601 or range>"
focus_center: [-98.0000, 38.0000]
~~~

**UI usage pattern (recommended):**

- `focus_center` → initial map center (and zoom heuristic)
- `focus_time` → initial timeline window
- `focus_layers` → layer toggles/highlights (validated against the UI layer registry)

> Not confirmed in repo: whether focus controls are embedded in Story Node front-matter only, returned via API, or both.

### Markdown and citation rendering

Story nodes and narrative blocks may contain inline citations in the KFM-style bracket notation, e.g.:

- `Some claim here【source_id†L10-L20】`

Frontend rendering should treat citations as first-class UI elements:

- render as hyperlinks, footnotes, or popovers,
- allow opening an evidence panel listing STAC/DCAT/PROV identifiers,
- never strip or “simplify” citations in a way that loses traceability.

---

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks (front-matter present, required sections)
- [ ] Story Node schema validation (`schemas/storynodes/**`)
- [ ] UI registry schema validation (`schemas/ui/**`)
- [ ] Frontend unit tests for Focus Mode components and reducers
- [ ] Accessibility checks (keyboard nav, focus order, readable contrasts)
- [ ] Security scans (no secrets), PII/sensitive-location leakage checks where applicable

> Repo-specific commands are **not confirmed in repo**. Add concrete commands once CI tooling is present.

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) schema validation
# node tools/validate_schemas.js schemas/storynodes
# node tools/validate_schemas.js schemas/ui

# 2) frontend unit tests
# npm test -- web/src/ui/focus-mode

# 3) a11y checks
# npm run a11y -- web/
~~~

### Telemetry signals (recommended)

| Signal | When emitted | Notes |
|---|---|---|
| `focus_mode_entered` | Entering Focus Mode | include entity_id, story_node_id (if any) |
| `focus_mode_exited` | Exiting Focus Mode | include duration |
| `citation_opened` | User opens a citation | include evidence_id |
| `provenance_panel_opened` | Audit panel opened | include entity/story context |
| `include_ai_toggled` | User opts into AI content | include model/version if provided |
| `redaction_notice_shown` | Redaction/generalization notice displayed | include layer_id or field |

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API response | Contract tests + runtime type checks |
| Story Node markdown | Markdown + YAML front-matter | `docs/reports/story_nodes/**` | `schemas/storynodes/**` |
| Layer registry | JSON | `web/**` (canonical location TBD) | `schemas/ui/**` |
| Evidence identifiers | IDs + metadata | STAC/DCAT/PROV outputs | Schema validation at catalog stage |

### Outputs

| Output | Format | Where | Notes |
|---|---|---|---|
| UI render state | in-memory | browser | should not persist sensitive data by default |
| Telemetry | JSON/event stream | telemetry sink (TBD) | must be schema-versioned if implemented |
| Evidence browsing | UI panel | Focus Mode | must preserve attribution and provenance |

### Sensitivity & redaction

- If the API marks fields/layers as generalized/redacted, the UI must:
  - display a clear notice,
  - avoid “precision recovery” via tooltips/export,
  - ensure screenshots/exports (if any) follow governance rules (**not confirmed in repo**).

---

## 🌐 STAC, DCAT & PROV Alignment

Focus Mode is a **consumer** of evidence artifacts:

- **STAC**: item/collection IDs for spatial-temporal assets shown on maps/timelines.
- **DCAT**: dataset-level metadata (title/license/keywords) for display and attribution.
- **PROV**: lineage bundles for audit panels and “how was this produced” views.

UI rules:

- Treat evidence IDs as **opaque stable identifiers**.
- Prefer linking to evidence via API-resolved endpoints (do not assume file paths are public).
- Preserve attribution requirements surfaced by DCAT/provider metadata.

---

## 🧱 Architecture

### Recommended component boundaries

| Component / module | Responsibility | Notes |
|---|---|---|
| `FocusModeShell` | Orchestrate Focus Mode layout and routing | contains panels + shared state |
| `NarrativePanel` | Render story content with citations | must preserve provenance |
| `MapPanel` | Display and highlight layers relevant to the focus | uses layer registry |
| `TimelinePanel` | Time window controls + highlights | driven by `focus_time` and API |
| `AuditPanel` | Provenance + sources + redaction notices | “trust surface” for Focus Mode |
| `adapters/*` | Transform API payloads into view models | keep contracts stable |
| `state/*` | Reducers/selectors/context | single source of truth |

### Contract expectations (UI-side)

- API must provide:
  - focus entity/story identifier,
  - narrative content with citations,
  - provenance/evidence references,
  - redaction/generalization flags when applicable,
  - (optional) opt-in AI narrative blocks with uncertainty metadata.

> Field names and shapes are **not confirmed in repo**; this list is an interface expectation, not an implemented contract.

---

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when Focus Mode changes could:

- expand access to sensitive/restricted locations,
- introduce new AI narrative behaviors or change AI labeling,
- add UI layers that may reveal sensitive precision via interaction/zoom,
- alter how citations/provenance are displayed such that traceability is reduced.

### CARE / sovereignty considerations

- Follow repo-wide sovereignty rules per `docs/governance/SOVEREIGNTY.md`.
- Prefer coarse/aggregate public views when there is any risk of exposing protected places or culturally sensitive knowledge.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing (as governed).
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).
- Any predictive/AI narrative must be:
  - opt-in,
  - labeled as machine-generated,
  - accompanied by uncertainty/confidence metadata,
  - never presented as unmarked fact.

---

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v0.1.0-draft | 2025-12-26 | Initial Focus Mode UI README scaffold (contracts + invariants) | TBD | TBD |

---

### Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

