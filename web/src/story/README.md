---
title: "KFM Web Story Module — README"
path: "web/src/story/README.md"
version: "v1.0.1"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:web:src:story:readme:v1.0.1"
semantic_document_id: "kfm-web-src-story-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:src:story:readme:v1.0.1"
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

# `web/src/story/` — Story and Focus Mode UI

## 📘 Overview

### Purpose

This directory is the UI implementation home for KFM’s story experience:

- Rendering governed **Story Nodes** (Markdown) into the UI
- Operating **Focus Mode**, the deep-dive narrative state for an entity/story
- Enforcing **evidence-first presentation**, where citations and provenance are first-class UI affordances

KFM’s canonical ordering is preserved:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Hard rule:

- **Focus Mode consumes only provenance-linked context bundles**. No unsourced narrative is allowed in Focus Mode publication paths.

### Scope

| In Scope | Out of Scope |
|---|---|
| Story Node rendering (Markdown → UI) and citation UX (links, popovers, side panel) | Authoring/curating Story Nodes (lives under `docs/reports/story_nodes/`) |
| Focus Mode UI state + layout (narrative + provenance panel + map/timeline sync) | Any direct Neo4j access (UI must not query the graph directly) |
| Reading Focus hints from Story Nodes (layers/time/center metadata) | ETL, catalog build, or graph ingest logic |
| Calling contracted Focus/context APIs and rendering their results | Creating/modifying API contracts (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |
| UI handling of redaction/generalization flags | Redaction policy definition (API boundary responsibility) |

### Audience

- **Primary:** Frontend contributors implementing Story/Focus Mode UX.
- **Secondary:** API/graph contributors aligning Focus bundle shape and evidence semantics with UI needs.
- **Also useful:** Narrative curators validating how Story Nodes will surface in Focus Mode.

### Definitions

- Glossary link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used here:
  - **Story Node:** governed narrative artifact that is machine-ingestible and provenance-linked.
  - **Focus Mode:** UI state that renders a provenance-linked context bundle for a selected entity/story.
  - **Context bundle / Focus bundle:** contracted API response packaging narrative + evidence + redaction flags + focus hints.
  - **Evidence:** resolvable identifiers pointing to STAC/DCAT/PROV artifacts and/or document spans.
  - **Citation token:** the inline narrative marker that maps to one evidence record in the bundle.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Source of truth for the non-negotiable pipeline ordering and CI gates |
| Canonical subsystem homes + redesign rules | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | “One canonical home”, UI reads from APIs, Focus Mode is provenance-linked |
| Story Node structure + Focus hints | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Defines Story Node fields, provenance requirements, and optional focus controls |
| Governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | This README follows the universal governed doc structure |
| API contract changes | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Use for any Focus bundle contract change |
| UI layer registry schema | `schemas/ui/` | Platform | Exact schema filenames not confirmed; used to validate UI layer registries |

### Definition of done for this document

- [ ] Front-matter is complete and `path` matches `web/src/story/README.md`
- [ ] Non-negotiable invariants are stated (API-only access, provenance-only Focus Mode, opt-in AI)
- [ ] Directory responsibilities are explicit and separated from other subsystems
- [ ] Citation and evidence resolution requirements are explicit (token format + UX expectations)
- [ ] Validation checklist includes sanitization, determinism, a11y, and “no direct-to-graph reads”
- [ ] Unknowns are labeled **not confirmed in repo** and listed as open questions

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React + map client + Focus Mode UI |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts rendered in Focus Mode |
| Schemas | `schemas/` | JSON schemas for STAC/DCAT/PROV/story/ui/telemetry |
| Graph | `src/graph/` | Ontology bindings + graph ingest/build (UI never reads this directly) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Catalog outputs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | Evidence + lineage referenced by Focus Mode |
| Tests | `tests/` | Unit + integration tests (including contract tests) |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |

### Expected file tree for this sub-area

This is a recommended structure. Some folders may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        ├── 📄 README.md
        ├── 📁 focus_mode/                 # Focus Mode state + layout (recommended)
        │   ├── 📄 FocusMode.tsx
        │   ├── 📄 NarrativePanel.tsx
        │   ├── 📄 ProvenancePanel.tsx
        │   ├── 📄 FocusBreadcrumbs.tsx
        │   └── 📄 FocusControls.tsx
        ├── 📁 renderer/                   # Story Node Markdown + citations (recommended)
        │   ├── 📄 StoryMarkdown.tsx
        │   ├── 📄 CitationToken.tsx
        │   └── 📄 sanitize.ts
        ├── 📁 model/                      # TS types for story + focus bundles (recommended)
        │   ├── 📄 storyNode.ts
        │   ├── 📄 focusBundle.ts
        │   └── 📄 evidence.ts
        ├── 📁 services/                   # API clients (recommended)
        │   └── 📄 focusApi.ts
        ├── 📁 utils/                      # parsing helpers (recommended)
        │   ├── 📄 parseCitations.ts
        │   └── 📄 formatEvidenceIds.ts
        └── 📁 __tests__/                  # parsing/rendering tests (recommended)
            ├── 📄 parseCitations.test.ts
            └── 📄 StoryMarkdown.test.tsx
~~~

---

## 🧭 Context

### Background

KFM’s UI is the consumer layer of a governed, evidence-first pipeline. Focus Mode is the “deep dive” narrative surface that combines:

- a story narrative panel,
- a provenance and audit panel,
- synchronized map and timeline context.

### Assumptions

- Story content is governed and stored as Story Nodes (Markdown) under `docs/reports/story_nodes/`.
- The UI enters Focus Mode by selecting an entity/story and requesting a Focus bundle from the API.
- Story Nodes contain citations that must be rendered as interactive evidence links.
- The API enforces redaction/generalization; the UI must respect and surface those flags.

### Constraints and invariants

- **No UI direct-to-graph reads:** the web app must never connect to Neo4j directly.
- **Focus Mode is provenance-linked only:** content shown must be evidence-linked; uncited narrative is not shown in publication paths.
- **Contract-first:** the Focus bundle shape is a contract; changes require versioning and tests.
- **Deterministic rendering:** same bundle in → same rendered output out (no hidden randomization).
- **AI content is opt-in:** if present, it is labeled, includes uncertainty metadata, and is never displayed as fact.
- **No sensitive-location inference:** the UI must not attempt to reconstruct or increase precision beyond what the API returns.

### Open questions

| Question | Owner | Target date | Notes |
|---|---|---:|---|
| What is the exact Focus Mode endpoint and contract shape | API Eng | TBD | Example patterns exist; must be confirmed in repo |
| What is the canonical Story Node schema location | Platform | TBD | Likely under `schemas/` but filenames/paths not confirmed |
| How are citation tokens mapped to the evidence array | UI + API | TBD | Decide whether Story Nodes embed stable evidence IDs vs server-side resolution |
| What are the allowed evidence kinds for the UI | UI + Catalog | TBD | Align with STAC/DCAT/PROV and document span references |

### Future extensions

- Rich citation UX: popovers, side-by-side source viewer, and “open at span” behaviors.
- Multimedia Story Node support (images/audio/video), with provenance and licensing preserved.
- Optional 3D narrative context using Cesium while preserving Focus Mode state and provenance rules.

---

## 🗺️ Diagrams

### Story and Focus Mode in the canonical pipeline

~~~mermaid
flowchart LR
  A["ETL<br/>src/pipelines"] --> B["STAC/DCAT/PROV<br/>data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph<br/>src/graph (Neo4j)"]
  C --> D["API boundary<br/>src/server (contracts + redaction)"]
  D --> E["UI<br/>web/ (React + Map)"]
  E --> F["Story Nodes<br/>docs/reports/story_nodes"]
  F --> G["Focus Mode<br/>provenance-linked only"]
~~~

### Focus Mode request sequence

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j behind API)
  participant Catalog as Catalog (STAC/DCAT/PROV)

  UI->>UI: User selects entity/story
  UI->>API: Request Focus bundle (entity_id, time_window?, includeAI?)
  API->>Graph: Fetch subgraph + entity context
  API->>Catalog: Resolve evidence identifiers and redaction flags
  Graph-->>API: Entity context + linkable IDs
  Catalog-->>API: Evidence metadata + provenance refs
  API-->>UI: Focus bundle (narrative + citations + evidence + audit flags)
  UI->>UI: Render narrative + provenance panel + map/timeline focus
~~~

---

## 📦 Data and Metadata

### Inputs

| Input | Format | Source | Notes |
|---|---|---|---|
| Focus bundle | JSON | API boundary | Contracted payload; includes narrative + evidence list |
| Story Node narrative | Markdown | Focus bundle | Treat as untrusted input for XSS safety |
| Evidence list | JSON | Focus bundle | Must include stable IDs, optional spans, redaction flags |
| Focus hints | Structured fields | Focus bundle | Derived from Story Node optional focus controls |
| UI layer registry | JSON | UI config | Should validate via `schemas/ui/` (**not confirmed**) |

### Outputs

| Output | Format | Where used | Notes |
|---|---|---|---|
| Rendered story narrative | React UI | Focus Mode panel | Must preserve citation semantics |
| Provenance and audit view | React UI | Focus Mode panel | Evidence list, redaction notices, AI labeling |
| Map and timeline focus state | UI state | Map + timeline | Sync to story focus hints when safe |
| Telemetry events | JSON/logs | Telemetry sink | Sink path not confirmed; signals listed below |

### Sensitivity and redaction

If the Focus bundle indicates redaction or generalization:

- Display a clear notice in the audit panel
- Avoid UI affordances that imply false precision
- Do not attempt to increase coordinate precision or infer restricted locations

### Quality signals

- All citations in the narrative resolve to evidence entries in the bundle
- Focus Mode renders without uncited claims by default
- Rendering is deterministic given the same bundle
- Accessibility: citation controls and Focus panels are keyboard accessible

---

## 🌐 STAC, DCAT and PROV alignment

This directory does not generate STAC/DCAT/PROV. Focus Mode must be able to reference them.

### STAC

Evidence may reference:

- STAC Collection IDs for dataset-level provenance
- STAC Item IDs for asset-level provenance

The UI should display STAC-linked evidence with a stable, copyable identifier and a human label.

### DCAT

Evidence may reference DCAT dataset identifiers to surface:

- license,
- publisher/contact,
- update cadence.

### PROV-O

The audit panel should surface PROV activity IDs when available:

- what generated the evidence,
- when,
- and from which inputs.

If a Story Node claim is present but the Focus bundle lacks a resolvable provenance reference, treat the story as incomplete for Focus Mode publication.

---

## 🧱 Architecture

### Responsibilities of `web/src/story/`

1. Focus Mode UI state
   - Enter/exit Focus Mode based on user selection
   - Maintain layout and navigation state, including breadcrumbs

2. Story rendering
   - Parse Markdown safely
   - Render citations as first-class interactive elements

3. Citation and evidence resolution
   - Resolve citation tokens against the Focus bundle evidence list
   - Provide evidence affordances without leaking sensitive details

4. Presentation of AI or predictive content
   - Support opt-in UI toggles
   - Label AI text clearly and display uncertainty metadata

### Contracts and boundaries

- UI consumes **only** contracted endpoints; it does not query Neo4j directly.
- Redaction/generalization decisions are enforced at the API boundary; UI respects them.
- Story Node structure is governed by the Story Node template and validation rules.

### Citation token format and resolution

Story Nodes use an inline citation token that should be treated as a resolvable pointer to evidence.

Recommended constraints for the UI renderer:

- citation tokens are parsed into a stable key
- the key must resolve to an evidence record in the Focus bundle
- unresolved tokens produce a visible warning state in the audit panel

Example citation token pattern used in KFM narrative tooling:

~~~text
… narrative text … 【source_id†L10-L24】
~~~

### Suggested Focus bundle shape

This is illustrative guidance for UI typing. The actual contract must be confirmed and governed.

~~~ts
export type EvidenceId =
  | { kind: "stac_item"; id: string }
  | { kind: "stac_collection"; id: string }
  | { kind: "dcat_dataset"; id: string }
  | { kind: "prov_activity"; id: string }
  | { kind: "document_span"; id: string; line_start?: number; line_end?: number };

export interface FocusEvidenceRecord {
  evidence: EvidenceId;
  label?: string;
  notes?: string;
  redaction?: { applied: boolean; method?: string };
}

export interface FocusHints {
  focus_layers?: string[];
  focus_time?: string;
  focus_center?: [number, number];
}

export interface FocusBundle {
  entity_id: string;
  story_node_markdown: string;
  evidence: FocusEvidenceRecord[];
  focus_hints?: FocusHints;
  ai?: {
    enabled: boolean;
    summary_text?: string;
    confidence?: number;
    provenance?: EvidenceId[];
  };
}
~~~

### Security notes

- Treat Story Node Markdown as untrusted:
  - sanitize HTML output,
  - prefer a renderer with an allowlist,
  - test XSS regressions.
- Never embed secrets or credentials in the web bundle.
- Avoid client-side logic that can re-identify redacted locations.

---

## 🧠 Story Node and Focus Mode integration

### Focus hints

Story Nodes may define optional focus controls. These should be returned via the API bundle and applied by the UI.

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Focus Mode behavior expectations

- Map and timeline synchronization
  - If focus hints are present, center and constrain context accordingly
  - If hints are absent, preserve current user context and highlight the selected entity

- Layer toggles
  - If the story specifies focus layers, enable those layers if available
  - If layers are missing, surface a notice rather than silently failing

- Citation rendering
  - Clicking a citation reveals evidence metadata
  - The UI supports span-style references when provided

- AI toggle behavior
  - AI content must never appear as unmarked fact
  - When enabled by user opt-in, show:
    - AI label,
    - uncertainty/confidence,
    - provenance IDs used

### Minimum UI acceptance criteria for production Focus Mode

- [ ] Focus Mode enter/exit is stable and back navigation works
- [ ] Narrative renders without broken citations
- [ ] Evidence panel lists resolvable IDs and redaction notices
- [ ] Redaction flags are respected and displayed
- [ ] AI content is opt-in and labeled with uncertainty metadata
- [ ] Citation and panel controls meet accessibility expectations

---

## 🧪 Validation and CI/CD

### Validation checklist

- [ ] README front-matter conforms to the Markdown protocol and required sections
- [ ] No direct-to-graph dependencies are introduced in `web/` (no Neo4j driver, no Cypher)
- [ ] Story rendering sanitization is covered by tests
- [ ] Citation parser is deterministic and handles expected token formats
- [ ] Evidence resolution detects and reports broken references
- [ ] Accessibility checks for Focus Mode panels and citation controls
- [ ] Any new fields in Focus bundle are covered by contract tests

### Reproduction commands

Commands must be replaced with repo-accurate scripts (**not confirmed in repo**).

~~~bash
# Web unit tests
# npm test

# Typecheck and lint
# npm run typecheck
# npm run lint
~~~

### Telemetry signals

| Signal | When | Notes |
|---|---|---|
| `focus_mode_entered` | Enter Focus Mode | include entity_id (non-sensitive) |
| `focus_mode_exited` | Exit Focus Mode | include duration |
| `citation_opened` | User opens a citation | include evidence kind + ID (no sensitive coords) |
| `focus_mode_redaction_notice_shown` | UI displays a redaction/generalization notice | include method |
| `ai_toggle_enabled` | User opts into AI content | include model/version if provided by API |

---

## ⚖ FAIR+CARE and governance

### Review gates

Route through governance review when:

- UI changes could expose sensitive locations
- citation UX changes could misrepresent evidence
- new AI narrative behaviors are added or default behavior changes
- new layers or interactions could leak restricted information

### CARE and sovereignty considerations

If Story Nodes include culturally sensitive knowledge or restricted sites:

- respect redaction/generalization decisions
- avoid precision affordances when content is generalized
- do not attempt to infer or reconstruct restricted location detail

### AI usage constraints

- Allowed by this doc metadata: summarization, structure extraction, translation, keyword indexing
- Prohibited: generating new policy text; inferring sensitive locations

---

## 🕰️ Version history

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.1 | 2025-12-28 | Re-structured README to align more strictly with Universal template and Focus Mode invariants | TBD | TBD |
| v1.0.0 | 2025-12-25 | Initial `web/src/story` README scaffold aligned to Focus Mode invariants | TBD | TBD |

---

## Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- API contract extension: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---
