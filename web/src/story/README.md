---
title: "KFM Web — Story & Focus Mode (README)"
path: "web/src/story/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:web:story:readme:v1.0.0"
semantic_document_id: "kfm-web-story-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:readme:v1.0.0"
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

# KFM Web — Story & Focus Mode

## 📘 Overview

### Purpose
This directory contains the **web UI primitives** for:
- Rendering **Story Nodes** (evidence-linked Markdown narrative).
- Driving the **Focus Mode** experience (story panel + provenance/audit + map/timeline synchronization).

This README governs **UI-layer responsibilities and constraints** for story rendering and Focus Mode behavior.

### Scope

| In Scope | Out of Scope |
|---|---|
| Focus Mode UI state and routing patterns | Neo4j / graph queries (backend responsibility) |
| Story Node Markdown rendering + citation UX | ETL / catalog build / provenance generation |
| Provenance/audit presentation affordances | Authoring Story Nodes (lives in docs/reports) |
| Strict gating for AI/predictive content (opt-in, labeled) | API contract definitions (live under API boundary) |
| Tests for story rendering / citation behavior | Data model / ontology changes |

### Audience
- Primary: Frontend engineers implementing Focus Mode + story rendering.
- Secondary: API engineers (contract alignment), curators (how story nodes surface), governance reviewers.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc: **Story Node**, **Focus Mode**, **Context bundle**, **Provenance**, **Citation**, **Redaction**, **Layer registry**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Pipeline ordering + “no uncited narrative” constraints |
| v13 redesign contracts | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical paths + contract-first expectations |
| Story Node authoring template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Governance | Required front-matter + optional focus controls |
| Story Nodes repository | `docs/reports/story_nodes/` | Curators | Canonical home for published story nodes |
| Story Node schema | `schemas/storynodes/` | Schemas | Validation target for story node structure (if present) |
| UI schema(s) | `schemas/ui/` | Schemas | Layer registry + UI-contract validation (if present) |
| API contracts | `src/server/contracts/` | API | UI must consume story/focus data via API boundary |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory responsibilities and boundaries are explicit (no “mystery dependencies”)
- [ ] Focus Mode invariants (provenance-only by default; opt-in AI) are captured
- [ ] Rendering expectations for citations are documented
- [ ] Validation/testing checklist is actionable and repeatable

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/story/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend app | `web/` | React + map client(s), Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` | Governed narrative artifacts with citations |
| API boundary | `src/server/` | API layer (UI never queries graph directly) |
| API contracts | `src/server/contracts/` | OpenAPI/GraphQL contracts + tests |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/storynodes/ui/telemetry) |
| Provenance bundles | `data/prov/` | PROV artifacts consumed for audit / focus context |

### Expected file tree for this sub-area
> This is a **recommended layout**. Adjust to match the actual codebase (folder names may differ).

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        ├── 📄 README.md
        ├── 📁 focus/                 # Focus Mode container + sub-views (recommended)
        ├── 📁 components/            # Story panel, sources panel, citation UI (recommended)
        ├── 📁 renderers/             # Markdown + citation rendering utilities (recommended)
        ├── 📁 hooks/                 # Focus state + map/timeline sync hooks (recommended)
        ├── 📁 types/                 # TypeScript types for focus/story payloads (recommended)
        └── 📁 __tests__/             # Unit/integration tests for story rendering (recommended)
~~~

---

## 🧭 Context

### Background
KFM’s canonical experience is: **map → select entity/story → Focus Mode → provenance-linked narrative + evidence**.

At a UI level, Focus Mode is expected to:
- Enter a focused state based on an entity/story selection.
- Fetch a **context bundle** from the API boundary.
- Render narrative text **with citations**, alongside structured evidence data for map/timeline highlighting.
- Provide an **audit/provenance** surface so users can trace claims back to sources.

### Assumptions
- Frontend is a SPA under `web/`.
- Focus Mode is a distinct UI mode/state (routing- or state-driven).
- Story Nodes are written in Markdown and include inline citation markers.

### Constraints / invariants (non-negotiable)
- Preserve canonical pipeline ordering: **ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode**.
- UI consumes story/focus data via **API contracts** only (no direct graph access).
- **No uncited narrative by default**: Focus Mode must not display assertions without provenance.
- Predictive / AI-generated content:
  - must be **opt-in**,
  - must be clearly **labeled**,
  - must include **uncertainty/confidence** metadata,
  - must never appear as unmarked fact.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Where is the canonical Focus API client located in `web/src/`? | TBD | TBD |
| What is the canonical citation rendering behavior (popover, footnote list, external link, etc.)? | TBD | TBD |
| What is the current Story Node schema validation mechanism in CI? | TBD | TBD |

### Future extensions
- Citation UX upgrades (source previews, “open evidence” drawers, side-by-side quote context).
- Evidence panels for media assets (images/audio) with attribution.
- Accessibility improvements: keyboard navigation, screen reader-friendly citation semantics.

---

## 🗺️ Diagrams

### System / dataflow diagram (context for Story + Focus Mode)

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Boundary]
  D --> E[Web UI]
  E --> F[Story Nodes Rendered]
  F --> G[Focus Mode]
~~~

### Focus Mode sequence (UI perspective)

~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI (Focus Mode)
  participant API as API Boundary
  participant Graph as Graph Layer

  User->>UI: Select entity/story
  UI->>API: Request focus context bundle (entity_id + flags)
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Subgraph + IDs/refs
  API-->>UI: Context bundle (story markdown + sources + hints)
  UI-->>User: Render story + citations + audit panel + map/timeline focus
~~~

---

## 📦 Data & Metadata

### UI contract expectations (shape, not implementation)
The story/focus UI should treat the API response as a **context bundle** containing:
- Narrative text (often Markdown for Story Node content).
- A resolvable **sources/evidence list** (dataset/document IDs, STAC/DCAT/PROV refs, attribution).
- Related entities for link-outs/pivots.
- Optional UI hints for Focus Mode (center/time/layers).

~~~ts
// PSEUDOTYPES — adjust to match API contracts in src/server/contracts/
export type FocusContextBundle = {
  entity: {
    id: string;
    type: string;          // e.g., Place | Person | Event | StoryNode
    display_name: string;
  };

  story?: {
    id: string;
    markdown: string;      // Story Node markdown (with citations)
    // Optional Focus Mode controls may be embedded or provided structurally
    focus_center?: [number, number];  // [lon, lat]
    focus_time?: string;              // ISO or domain-specific range
    focus_layers?: string[];          // layer ids to toggle
  };

  sources: Array<{
    id: string;            // stable evidence id (STAC/DCAT/PROV/document id)
    label: string;
    kind: string;          // e.g., stac_item | dcat | prov | document
    url?: string;          // optional, if externally resolvable
    attribution?: string;
    sensitivity?: "public" | "restricted";
  }>;

  related_entities?: Array<{ id: string; type: string; display_name: string }>;

  ai_insight?: {
    enabled: boolean;      // should be false/absent by default
    text?: string;         // only if opt-in
    confidence?: number;   // required if present
    source_ids?: string[]; // what evidence it summarizes
  };
};
~~~

### Citation rendering expectation
Story Node Markdown uses a citation marker convention (e.g., `【source†Lx-Ly】`-style references).
Minimum UI requirements:
- Render citations distinctly from body text.
- Make citations interactive (open source details, show provenance, or link to evidence viewer).
- If a citation cannot be resolved against `sources[]`, render a warning state (do not silently drop).

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”
Story Nodes are expected to:
- Carry provenance annotations.
- Link to graph entity IDs and evidence IDs.
- Provide optional Focus Mode controls (e.g., focus_center / focus_time / focus_layers).

### Focus Mode behavior expectations
- **Default view:** provenance-linked narrative only.
- **Audit/provenance panel:** always available (or one click away).
- **Map/timeline sync:** apply focus_center/focus_time hints when present.
- **AI/predictive sections:** hidden by default; revealed only by explicit user action; always labeled.

---

## 🧪 Validation & CI/CD

### Validation steps (UI-facing)
- [ ] Lint + typecheck passes
- [ ] Story Markdown renders without crashes
- [ ] Citations resolve (or show explicit “unresolved citation” warnings)
- [ ] Focus Mode toggles AI sections only when opt-in flags are set
- [ ] Accessibility checks: keyboard nav and screen reader semantics for citations/panels
- [ ] Unit/integration tests cover Focus Mode’s critical flows

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) install deps
# 2) run lint + typecheck
# 3) run unit tests
# 4) run e2e tests (if configured)
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates
Changes in this directory should trigger governance review when they introduce:
- New UI behaviors that could expose sensitive layers or restricted locations.
- New “AI insight” presentation behaviors or defaults.
- New external data source rendering (attribution, licensing, or sovereignty implications).

### CARE / sovereignty considerations
- Respect any `sensitivity` metadata provided by the API.
- Do not display restricted geometries or locations unless explicitly authorized and properly redacted.

### AI usage constraints
- Ensure any AI narrative behavior is **opt-in** and clearly labeled.
- Never present AI output as unmarked factual narrative.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for web story + focus mode module | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

