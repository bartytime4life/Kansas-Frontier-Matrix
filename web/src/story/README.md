---
title: "KFM Web Story Module — README"
path: "web/src/story/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:src:story:readme:v1.0.0"
semantic_document_id: "kfm-web-src-story-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:src:story:readme:v1.0.0"
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

# `web/src/story/` — Story + Focus Mode UI

## 📘 Overview

### Purpose

This directory is the **UI implementation home** for KFM’s story experience, including:

- Rendering governed **Story Nodes** (Markdown) in the UI.
- Managing the **Focus Mode** UI state (a “deep dive” view over a single entity/story).
- Presenting **citations and provenance** so that Focus Mode stays evidence-first.

This aligns with KFM’s canonical ordering:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

> Non‑negotiable: Focus Mode must remain provenance-linked; uncited “orphan facts” are not permitted.

### Scope

| In Scope | Out of Scope |
|---|---|
| Story Node rendering (Markdown → UI) and citation UX (links/popovers) | Writing/curating Story Nodes themselves (lives under `docs/reports/story_nodes/`) |
| Focus Mode UI state + layout (narrative panel, provenance/audit panel, timeline/map synchronization) | Any direct Neo4j access (UI must not query the graph directly) |
| Integrating “Focus hints” from Story Nodes (e.g., focus center/time/layers) | Defining ETL, catalog, or graph ingest logic |
| Calling Focus/context APIs and displaying their results | Creating or modifying API contracts (use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`) |

### Audience

- **Primary:** Frontend contributors working on the narrative/Focus Mode UI.
- **Secondary:** API/graph contributors needing to understand UI expectations for focus bundles and citations.
- **Also useful for:** Narrative curators validating how Story Nodes will render in Focus Mode.

### Definitions

- Glossary link: `docs/glossary.md` (**not confirmed in repo**).
- Terms used here:
  - **Story Node:** governed Markdown narrative artifact rendered by the UI in Focus Mode.
  - **Focus Mode:** specialized UI state showing a story/entity in detail, with provenance and map/timeline context.
  - **Context bundle:** the API response that packages entity + narrative + evidence references for Focus Mode.
  - **Provenance:** STAC/DCAT/PROV + graph lineage links that back every claim.

### Key artifacts (what this README points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | ETL→…→Focus Mode ordering and “no unsourced narrative” invariants |
| v13 redesign / canonical homes | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch Team | UI is `web/`; Story Nodes are `docs/reports/story_nodes/`; Focus Mode is provenance-linked |
| Story Node structure + citation rules | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Defines required front-matter and “every factual claim is cited” rule |
| Governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Team | Template used by this README |
| Focus Mode UI flow (design guidance) | “KFM Implementation Guide” (PDF) | Platform | Focus Mode: click entity → API focus request → narrative + audit + map/timeline sync (**repo path not confirmed**) |
| UI layer registry schema | `schemas/ui/` | Platform | UI config must validate (exact schema filenames **not confirmed in repo**) |

### Definition of done (for this document)

- [ ] Front-matter is complete and `path` matches `web/src/story/README.md`.
- [ ] Clear statement of Focus Mode invariants (provenance-only, opt‑in AI).
- [ ] Directory responsibilities are explicit (what lives here vs. elsewhere).
- [ ] Citation rendering requirements are explicit (format + UI behavior).
- [ ] Validation checklist includes “no direct-to-graph reads” and sanitization expectations.
- [ ] Any unknowns are labeled **not confirmed in repo**.

---

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | React/Map UI; Focus Mode UX; layer registry (exact path **not confirmed in repo**) |
| API boundary | `src/server/` | Contracted access layer serving Focus Mode bundles (legacy may differ; **not confirmed in repo**) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts + assets, rendered in Focus Mode |
| Schemas | `schemas/` | Story Node schema, UI schema, telemetry schema (filenames **not confirmed in repo**) |
| Graph | `src/graph/` | Ontology bindings + ingest logic (UI never talks to this directly) |
| Catalog outputs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | Evidence + lineage that Focus Mode must be able to reference |

### Expected file tree for this sub-area

> This is a **recommended** structure. Some folders may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        ├── 📄 README.md
        ├── 📁 focus_mode/                 # Focus Mode UI state + layout (recommended)
        │   ├── 📄 FocusMode.tsx
        │   ├── 📄 NarrativePanel.tsx
        │   ├── 📄 ProvenancePanel.tsx
        │   ├── 📄 FocusBreadcrumbs.tsx
        │   └── 📄 FocusControls.tsx
        ├── 📁 renderer/                   # Story Node Markdown + citations (recommended)
        │   ├── 📄 StoryMarkdown.tsx
        │   ├── 📄 CitationLink.tsx
        │   └── 📄 sanitize.ts
        ├── 📁 model/                      # TS types for story + focus bundles (recommended)
        │   ├── 📄 storyNode.ts
        │   ├── 📄 focusBundle.ts
        │   └── 📄 sources.ts
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

KFM’s UI is the final consumer layer of a governed, evidence-first pipeline. The UI presents map/timeline context plus Story Nodes, and Focus Mode is the “deep dive” narrative view.

KFM’s Master Guide defines the canonical pipeline and extension planning model (“Extension Matrix”), and the v13 blueprint reinforces canonical homes and Focus Mode’s provenance-only constraint.

### Assumptions

- Story content is governed and stored as **Story Nodes** (Markdown) under `docs/reports/story_nodes/`.
- The UI enters Focus Mode by selecting a story/entity and then requesting a **context bundle** from the API.
- Story Nodes contain citations that must be rendered as interactive evidence links.

### Constraints / invariants (non-negotiables)

- **No UI direct-to-graph reads:** the web app must never connect to Neo4j directly; graph access is via contracted APIs only.
- **Focus Mode is provenance-linked only:** content shown must have evidence references; uncited narrative is not shown.
- **AI/predictive content is opt-in:** if present, it must be clearly labeled and include uncertainty/confidence metadata.
- **Redaction/generalization is enforced at the API boundary:** the UI must respect redaction flags and must not attempt to “reconstruct” restricted locations.

### Open questions

| Question | Owner | Notes |
|---|---|---|
| What is the exact Focus Mode endpoint and contract shape? | API Eng | Implementation guide examples mention `GET /focus/{entityId}` and an `includeAI` flag (**not confirmed in repo**) |
| What is the canonical Story Node schema location? | Platform | Likely under `schemas/storynodes/` (**not confirmed in repo**) |
| How are citation tokens mapped to the API “sources” array? | UI + API | Decide whether citations embed stable source IDs vs. are resolved by server |

### Future extensions

- Rich citation UX: popovers, side-by-side source viewer, “open document at line range.”
- Multimedia support (images/audio/video) for Story Nodes (must remain provenance-linked and licensed).
- Optional 3D narrative context (Cesium) while preserving Focus Mode state and provenance rules.

---

## 🗺️ Diagrams

### Story + Focus Mode in the canonical pipeline

~~~mermaid
flowchart LR
  A["ETL<br/>src/pipelines"] --> B["STAC/DCAT/PROV<br/>data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph<br/>src/graph (Neo4j)"]
  C --> D["API boundary<br/>src/server (contracts + redaction)"]
  D --> E["UI<br/>web/ (React + MapLibre/Cesium)"]
  E --> F["Story Nodes<br/>docs/reports/story_nodes"]
  F --> G["Focus Mode<br/>provenance-linked only"]
~~~

### Focus Mode sequence (UI ↔ API ↔ Graph)

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j behind API)

  UI->>UI: User selects entity/story
  UI->>API: Request Focus bundle (entity_id, time_window?, includeAI?)
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Entity context + evidence references
  API-->>UI: Focus bundle (narrative + citations + audit flags)
  UI->>UI: Render narrative + provenance panel + map/timeline focus
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Notes |
|---|---|---|---|
| Focus context bundle | JSON | API boundary | Contains entity + story node + sources/provenance refs |
| Story Node narrative | Markdown | API response | Must render citations; treat as untrusted input for XSS safety |
| Evidence/source records | JSON | API response | Should include stable IDs (STAC/DCAT/PROV, doc IDs, line ranges) |
| Focus controls | JSON/YAML-like fields | Story Node metadata | E.g., focus center/time/layers hints (if present) |
| UI layer registry | JSON | UI config | Layer toggles validated by UI schema (exact path **not confirmed**) |

### Outputs

| Output | Format | Where used | Notes |
|---|---|---|---|
| Rendered story narrative | React UI | Focus Mode panel | Must preserve citation semantics |
| Provenance/audit panel | React UI | Focus Mode panel | Shows evidence list, redaction notices, AI labels |
| Map/timeline focus state | UI state | Map + timeline | Sync to story’s focus center/time when available |
| Telemetry events | JSON/logs | Telemetry sink | Recommended signals listed below (sink path **not confirmed**) |

### Sensitivity & redaction

- The UI must never display exact restricted coordinates if redacted/generalized upstream.
- If the API indicates that geometry has been generalized or records redacted, the UI should:
  - display a clear notice in the audit panel,
  - avoid “zoom-to-precision” behaviors that imply false accuracy.

### Quality signals

- All citations in the narrative resolve to evidence entries in the bundle (no broken references).
- Focus Mode renders without uncited claims by default.
- Story rendering is deterministic (same input bundle → same UI output).
- Accessibility: citation controls, panels, and navigation are keyboard accessible.

---

## 🌐 STAC, DCAT & PROV Alignment

This directory does not generate STAC/DCAT/PROV, but **Focus Mode must be able to reference them**.

### STAC

- Evidence may reference:
  - STAC Collection IDs (dataset-level)
  - STAC Item IDs (asset-level)
- UI should render STAC-linked evidence in a stable, copyable form (ID + label + optional “open details” affordance).

### DCAT

- Evidence may reference a DCAT dataset identifier so users can see:
  - license,
  - publisher/contact,
  - update cadence (if provided).

### PROV-O

- Focus Mode audit panel should surface PROV activity IDs when available:
  - what generated the evidence,
  - when,
  - and from which inputs.

> If a story node contains claims but the Focus bundle lacks a resolvable STAC/DCAT/PROV reference, treat the story as incomplete (draft) for Focus Mode publication.

---

## 🧱 Architecture

### Responsibilities of `web/src/story/`

1. **Focus Mode UI state**
   - Enter/exit Focus Mode based on user selection.
   - Manage layout: story narrative, provenance panel, and map/timeline context.

2. **Story rendering**
   - Parse Markdown safely.
   - Render citations as first-class interactive elements.

3. **Citation + evidence resolution**
   - Map citation tokens (e.g., “source ID + line range”) to evidence entries provided by the API bundle.
   - Provide “open source” affordances (panel, link, modal) without leaking sensitive location details.

4. **AI/predictive content presentation**
   - If the API returns AI-generated content, it must be labeled and gated behind opt-in UI controls.

### Contracts and boundaries

- The UI consumes **only** contracted endpoints; it does not query Neo4j directly.
- Redaction/generalization decisions are enforced at the API boundary; UI respects them.
- Story Node structure is governed by the Story Node template and validation rules.

### Suggested (example) Focus bundle shape

> This is an illustrative shape to guide UI types; the actual contract is **not confirmed in repo**.

~~~ts
export type EvidenceId =
  | { kind: "stac_item"; id: string }
  | { kind: "stac_collection"; id: string }
  | { kind: "dcat_dataset"; id: string }
  | { kind: "prov_activity"; id: string }
  | { kind: "document"; id: string; line_start?: number; line_end?: number };

export interface FocusEvidenceRecord {
  evidence: EvidenceId;
  label?: string;
  notes?: string;
  redaction?: { applied: boolean; method?: string };
}

export interface FocusBundle {
  entity_id: string;
  story_node_markdown: string;
  evidence: FocusEvidenceRecord[];
  focus_hints?: {
    focus_layers?: string[];
    focus_time?: string;
    focus_center?: [number, number];
  };
  ai?: {
    enabled: boolean;
    summary_text?: string;
    confidence?: number;
    provenance?: EvidenceId[];
  };
}
~~~

### Security notes (UI)

- Treat Story Node Markdown as **untrusted**:
  - sanitize HTML output,
  - prefer a Markdown renderer that supports an allowlist.
- Never embed secrets or credentials in the web bundle.
- Avoid client-side logic that can re-identify redacted locations (no reverse-engineering from tiles, etc.).

---

## 🧠 Story Node & Focus Mode Integration

### Focus Mode behavior expectations

- **Map/timeline synchronization**
  - If a story provides `focus_center` and/or `focus_time`, the UI should center/zoom and set timeline context accordingly.
  - If focus hints are absent, default to preserving the user’s current map/timeline state and only highlight the selected entity.

- **Layer toggles**
  - If the story specifies `focus_layers`, enable those layers (if available) and record a UI notice when layers are unavailable.

- **Citation rendering**
  - Citations should be interactive:
    - clicking a citation reveals evidence metadata and (when safe) a source preview or link.
  - The UI should support line-range style references (e.g., source line spans) when provided.

- **AI toggle behavior**
  - AI text must never appear as unmarked fact.
  - If AI is enabled by user opt-in, show:
    - “AI-generated” label,
    - confidence/uncertainty,
    - and the evidence IDs it was derived from.

### Minimum UI acceptance criteria (for production Focus Mode)

- [ ] Focus Mode can enter/exit cleanly (back navigation works).
- [ ] Narrative renders without broken citations.
- [ ] Evidence panel shows resolvable IDs (STAC/DCAT/PROV/doc IDs).
- [ ] Redaction notices appear when flagged by API.
- [ ] AI content is opt-in and labeled with uncertainty fields.

---

## 🧪 Validation & CI/CD

### Validation checklist

- [ ] Markdown protocol checks for this README (front matter required keys present).
- [ ] No direct-to-graph dependencies are added to `web/` (no Neo4j driver, no Cypher).
- [ ] Story rendering sanitization is covered by tests (XSS regression tests recommended).
- [ ] Citation parser handles expected formats (including line ranges) deterministically.
- [ ] Accessibility checks for Focus Mode panels and citation controls.

### Reproduction (placeholder)

> Commands here are examples and must be replaced by repo-accurate scripts (**not confirmed in repo**).

~~~bash
# 1) Run web unit tests
# npm test

# 2) Run typecheck / lint
# npm run typecheck
# npm run lint
~~~

### Telemetry signals (recommended)

| Signal | When | Notes |
|---|---|---|
| `focus_mode_entered` | Enter Focus Mode | include entity_id (non-sensitive) |
| `focus_mode_exited` | Exit Focus Mode | include duration |
| `citation_opened` | User opens a citation | include evidence kind + ID (no sensitive coords) |
| `redaction_notice_shown` | UI displays a redaction/generalization notice | include method |
| `ai_toggle_enabled` | User opts into AI content | include model/version if provided by API |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Route through governance review when:

- story rendering changes could expose sensitive locations (e.g., map focus behavior, evidence previews),
- new AI narrative features are added or default behavior changes,
- citation UX changes alter how evidence is surfaced (risk of misrepresentation).

### CARE / sovereignty considerations

- If Story Nodes include culturally sensitive knowledge or restricted sites:
  - ensure the UI respects redaction/generalization decisions,
  - avoid “precision affordances” (e.g., showing exact points) when content is generalized.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing (per front matter).
- Prohibited: generating new policy text; inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-25 | Initial `web/src/story` README scaffold aligned to Focus Mode invariants | TBD | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

---
