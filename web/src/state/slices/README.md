---
title: "KFM Web UI State Slices — README"
path: "web/src/state/slices/README.md"
version: "v1.0.0"
last_updated: "2025-12-25"
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

doc_uuid: "urn:kfm:doc:web:state:slices:readme:v1.0.0"
semantic_document_id: "kfm-web-state-slices-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:state:slices:readme:v1.0.0"

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

# KFM Web UI State Slices — README

> **Purpose required:** Define **conventions and guardrails** for UI state “slices” used by the KFM web client so that map + narrative interactions remain **predictable**, **testable**, and **governance-safe**, especially for **Story Nodes** and **Focus Mode**.

## 📘 Overview

### Purpose

- Document the conventions for writing and organizing **state slices** in the KFM web UI.
- Ensure UI state supports:
  - map + layer interactions,
  - Story Node selection,
  - Focus Mode activation,
  - provenance-linked content presentation.

### Scope

| In Scope | Out of Scope |
|---|---|
| Slice boundaries, naming, state shape conventions | API contract design (belongs at API boundary) |
| Async request state patterns (loading/error/lastFetched) | Graph/Neo4j access (UI does not access graph directly) |
| Focus Mode and Story Node state patterns | UI component structure, styling, routing |
| Governance-safe state handling (no sensitive leakage via client state) | ETL/STAC/DCAT/PROV generation |

### Audience

- **Primary:** Frontend contributors maintaining `web/` state management.
- **Secondary:** Reviewers verifying UI invariants (API boundary, provenance-only Focus Mode rules, governance constraints).

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc: **slice**, **selector**, **reducer**, **action**, **async thunk/effect**, **Focus Mode**, **Story Node**, **provenance**, **layer registry**, **redaction**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | KFM flow and “non‑negotiables” (UI sits downstream of API) |
| Implementation guide (UI patterns) | `docs/` (see: “KFM Implementation Guide”) | KFM Core | Recommends a predictable state container; names Focus Mode state needs |
| v13 blueprint repo structure | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Confirms preferred roots and UI boundary rules |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Citation/provenance conventions for story content |
| Selectors conventions | `web/src/state/selectors/README.md` | Frontend | Companion doc (not confirmed in repo) |
| Store configuration | `web/src/state/` | Frontend | Store setup file name is **not confirmed in repo** |

### Definition of done

- [ ] Front-matter complete + `path` matches file location
- [ ] Slice boundaries + naming conventions are explicit
- [ ] Focus Mode + Story Node rules are represented in recommended state shapes
- [ ] “Do not store” and governance constraints are listed (serializable state, no sensitive leakage)
- [ ] Validation steps are listed (unit tests, lint, serialization checks)
- [ ] Footer refs included (master guide, template, governance links)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/state/slices/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed + catalog outputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence + discovery + lineage |
| Graph build | `src/graph/` | Ontology bindings + ingest tooling |
| API boundary | `src/server/` *(v13 target)* or legacy equivalent *(not confirmed in repo)* | Contracts, redaction, access controls |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts |
| Schemas | `schemas/` | Contract and metadata schemas (including UI schemas if present) |

### Expected file tree for this sub-area

> **not confirmed in repo** — example shape only; adapt to actual store and slice filenames.

~~~text
web/
└── 🌐 src/
    └── 🧠 state/
        ├── 📁 slices/
        │   ├── 📄 README.md
        │   ├── 📄 index.ts
        │   ├── 📄 mapSlice.ts
        │   ├── 📄 layersSlice.ts
        │   ├── 📄 focusModeSlice.ts
        │   ├── 📄 storyNodesSlice.ts
        │   ├── 📄 searchSlice.ts
        │   ├── 📄 userSettingsSlice.ts
        │   └── 📁 __tests__/
        │       └── 📄 focusModeSlice.test.ts
        ├── 📁 selectors/
        │   └── 📄 README.md
        └── 📄 store.ts
~~~

## 🧭 Context

### Background

KFM’s architecture is intentionally staged:

ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.

This folder exists to keep the **UI stage** deterministic and auditable: the same user interactions should produce the same state transitions and the same rendered narrative, and Focus Mode must remain provenance-linked.

### Pipeline placement

- Slices represent the UI’s **single source of truth** for application state:
  - current Focus Mode entity and context bundle,
  - which layers are active,
  - what filters/search constraints are applied,
  - UI preferences (panel open/closed, time slider range, etc.).
- UI state must be driven by **API responses** and user intent, not by direct graph access.

### Non-negotiables for KFM slices

- **API boundary preserved:** the UI must not query Neo4j directly (all graph access is via contracted APIs).
- **Provenance integrity:** Focus Mode must not show “orphan” facts; AI content (if present) must be opt-in and clearly labeled with uncertainty/confidence metadata.
- **Serializable state:** slices store JSON-serializable data only (no MapLibre objects, no DOM handles, no class instances).

## 🗺️ Diagrams

### Focus Mode state flow

~~~mermaid
flowchart LR
  User["User interaction<br/>map click / story click"] --> Dispatch["dispatch(selectEntity / enterFocusMode)"]
  Dispatch --> API["API request<br/>context bundle + citations"]
  API --> Slice["focusModeSlice reducer<br/>stores bundle + status"]
  Slice --> UI["Focus Mode UI<br/>renders narrative + map/timeline sync"]
  UI --> Sources["Sources panel<br/>renders provenance links"]
~~~

### State boundaries

~~~mermaid
flowchart TB
  subgraph UI["web/ (React/Map UI)"]
    Slices["state slices<br/>(this folder)"]
    Selectors["selectors<br/>(derived state)"]
  end

  subgraph API["src/server/ (API boundary)"]
    Contracts["contracted endpoints<br/>redaction + access control"]
  end

  subgraph Graph["Neo4j graph"]
    KG["knowledge graph"]
  end

  Slices --> Selectors
  UI --> Contracts
  Contracts --> KG
~~~

## 🧠 Story Node & Focus Mode Integration

### What slices must support

Story Nodes and Focus Mode are UI behaviors that require coherent state:

- **Story Nodes:** selection, reading state, and provenance links for narrative panels.
- **Focus Mode:** a “deep dive” view that synchronizes:
  - narrative panel,
  - map viewport and highlighted layers,
  - timeline focus.

### Provenance-first state rule

Focus Mode content must remain **traceable**:

- Store (and render) dataset/document references provided by the API.
- Do not “invent” missing sources client-side.
- If the UI shows AI-derived summaries, state must include:
  - whether the user opted in,
  - a visible disclaimer label,
  - uncertainty/confidence metadata (if provided).

### Recommended Focus Mode slice shape

> **not confirmed in repo** — example TypeScript shape only. Align with actual API contracts.

~~~ts
export type LoadStatus = "idle" | "loading" | "succeeded" | "failed";

export type ProvenanceRefs = {
  stac_item_ids?: string[];
  stac_collection_ids?: string[];
  dcat_dataset_ids?: string[];
  prov_activity_ids?: string[];
  source_document_ids?: string[]; // document/record ids returned by API
};

export type Citation = {
  citation_id: string;     // stable id
  label: string;           // human label
  kind: "stac" | "dcat" | "prov" | "document" | "external";
  ref?: string;            // url or internal route token (avoid raw URLs if policy requires)
};

export type FocusContextBundle = {
  focus_entity_id: string;
  focus_entity_type: string;
  focus_label: string;

  narrative_markdown?: string;     // story content, provenance-linked
  citations: Citation[];
  provenance: ProvenanceRefs;

  related_entities: Array<{ id: string; type: string; label: string }>;

  recommended_layers: Array<{
    layer_id: string;
    stac_collection_id?: string;
    api_route?: string;
    sensitivity?: "public" | "restricted" | "sensitive";
  }>;

  ai?: {
    enabled: boolean;              // user opt-in
    disclaimer: string;            // visible label text
    confidence?: number;           // 0..1 if provided
    model_id?: string;             // model/version if provided
  };
};

export type FocusModeState = {
  status: LoadStatus;
  error?: string;

  active: boolean;
  bundle?: FocusContextBundle;

  // UI-only flags
  sources_panel_open: boolean;
  ai_panel_open: boolean;

  // navigation affordances
  breadcrumb_entity_ids: string[];
};
~~~

### Slice vs selector responsibilities

- **Slices** store raw state (API payloads + user intent + request status).
- **Selectors** compute derived view models:
  - formatted citations lists,
  - “isFocusModeReady” guards,
  - map highlight sets from IDs.

See `web/src/state/selectors/README.md` (not confirmed in repo).

## 🧪 Validation & CI/CD

### Validation steps

- Reducers are pure and deterministic:
  - unit test state transitions for key actions.
- State remains serializable:
  - enforce serializable checks if using Redux tooling (not confirmed in repo).
- API usage stays within contracts:
  - if a slice adds a new endpoint call, ensure the API contract exists and is tested.
- Focus Mode integrity:
  - include at least one test (or runtime guard) that prevents rendering Focus Mode narrative when citations/provenance are missing.

### CI expectations

**not confirmed in repo** — typical gates that should pass for slice changes:

- Typecheck + lint on `web/`
- Unit tests for reducers/selectors
- No secrets/PII in committed fixtures
- Contract tests when API integration changes

## 📦 Data & Metadata

UI slices are not canonical data stores, but they often carry identifiers and metadata needed for traceability.

Recommended minimum metadata to keep in state when present in API responses:

- stable entity IDs and types,
- dataset IDs / STAC Item IDs / Collection IDs,
- provenance pointers (PROV activity IDs),
- sensitivity/classification markers (to display warnings and prevent unsafe interactions).

## 🌐 STAC, DCAT & PROV Alignment

Slices do not emit STAC/DCAT/PROV, but they must preserve references returned by APIs so the UI can:

- show “Sources” and “Lineage” panels,
- link to dataset/collection detail views,
- render provenance-linked Focus Mode content without lossy transformations.

Rules:

- Do not rewrite IDs.
- Do not “merge” provenance across unrelated entities client-side (risk of misleading lineage).
- Treat missing provenance as a rendering-blocking condition for Focus Mode narrative.

## 🧱 Architecture

### Slice boundaries

Use slices to mirror stable UI domains (example only):

- **map**: viewport, interaction state, selected feature IDs
- **layers**: layer registry, active layers, per-layer settings
- **focusMode**: active entity, context bundle, provenance/citations panels
- **storyNodes**: story node list, selected node, reading progress
- **search**: query, results, filters/facets
- **userSettings**: preferences (theme, units, basemap choice)

### Side effects

- Reducers must remain pure.
- API calls belong in:
  - async thunks/effects, or
  - a dedicated API layer (RTK Query or similar — not confirmed in repo).

### What not to store in slices

- MapLibre map instances, layer objects, style objects with circular refs
- Large raw geometries if not required (prefer IDs + fetch-on-demand)
- Any sensitive/unredacted coordinates not intended for client display
- Secrets/tokens of any kind

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when a UI change could expand access or inference risk, for example:

- adding a new layer or interaction pattern that could reveal sensitive locations by zooming, filtering, or combining datasets,
- storing richer location detail in client state than what the API exposes,
- presenting AI-derived narrative without explicit opt-in + labeling.

### CARE and sovereignty considerations

- Assume culturally sensitive narratives and locations are high-risk by default.
- Never “reverse” generalization (e.g., inferring precise coordinates from coarse geometry).
- Ensure the UI faithfully reflects access controls and redaction from the API boundary.

### AI usage constraints

- Allowed: summarization and presentation of *provenance-linked* content when opt-in.
- Prohibited: generating uncited facts or inferring sensitive locations through client-side synthesis.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README defining slice conventions for KFM web UI state | (you) |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

