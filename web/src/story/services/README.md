---
title: "Web Story Services"
path: "web/src/story/services/README.md"
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

doc_uuid: "urn:kfm:doc:web:story:services:readme:v1.0.0"
semantic_document_id: "kfm-web-story-services-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:services:readme:v1.0.0"
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

<div align="center">

# 🧩 Web Story Services

Service-layer documentation for **Story Nodes** and **Focus Mode** in the KFM web UI.

**Location:** `web/src/story/services/`  
**This file:** `web/src/story/services/README.md`

</div>

> **Purpose (required):** Define the responsibilities, invariants, and contract expectations for Story/Focus services in the web UI so the UI remains **API-mediated**, **provenance-first**, and **testable**.

---

## 📘 Overview

### Purpose

This directory is the **service boundary** for Story/Focus Mode behaviors in the web UI:

- Fetching and validating **Focus Mode context bundles** from the API.
- Loading and interpreting **Story Node** content (Markdown + front-matter + citation syntax).
- Transforming API payloads into **UI-ready models** (map/timeline hints, audit/provenance panels, citation popovers).
- Enforcing “**no uncited narrative**” expectations by surfacing warnings when provenance is missing.

This directory is intentionally designed to keep story behavior **deterministic** and **unit-testable**, separate from React view logic.

### Scope

| In Scope | Out of Scope |
|---|---|
| API adapters for Focus/Story endpoints | Implementing server endpoints (`src/server/…`) |
| Parsing Story Node metadata (front-matter) | Authoring Story Nodes (`docs/reports/story_nodes/…`) |
| Citation extraction + mapping to evidence references | Writing new governance policy |
| Building audit/provenance view models | Rendering components (belongs in `web/src/story/components/…`) |
| Cache policy for story fetches | Direct Neo4j access (prohibited) |

### Audience

- Primary: Web UI developers working on Story Nodes, Focus Mode, map/timeline integration.
- Secondary: API contract owners, QA/test maintainers, curators validating story behavior.

### Definitions

- **Story Node:** A governed Markdown narrative that references entities and evidence; used by UI and Focus Mode.
- **Focus Mode:** A specialized UI state that displays a story/entity “deep dive” using a provenance-linked context bundle.
- **Context bundle:** The contracted API payload for Focus Mode (narrative + citations/evidence refs + audit flags + related entities + UI hints).
- **Citation token:** Inline citation syntax in Markdown (example form: `【source†Lx-Ly】`) that must resolve to evidence.
- **Provenance-first:** UI must be able to trace narrative claims back to evidence; “no assertion goes uncited.”

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM maintainers | Canonical pipeline + invariants |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story/Docs maintainers | Front-matter + citations rules |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs maintainers | Documentation structure |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Core maintainers | Evidence-first + contract-first rules |
| Focus/Story API contracts | `src/server/contracts/**` | API owners | **Not confirmed in repo**: exact paths may differ |
| Story Node corpus | `docs/reports/story_nodes/**` | Curators | Draft/published split may exist |
| Story Node schema | `schemas/storynodes/**` | Contracts owners | Required for validation |
| UI layer registry schema | `schemas/ui/**` | UI/contracts owners | Required for focus layer hints |

### Definition of done

- [ ] Front-matter complete and `path` matches file location
- [ ] Clearly states **service boundary** and **non-negotiable invariants**
- [ ] Describes how services handle **citations**, **audit panel models**, and **focus hints**
- [ ] Lists validation + testing expectations
- [ ] Notes any “**not confirmed in repo**” paths or assumptions

---

## 🗂️ Directory layout

### This directory

`web/src/story/services/` should contain **pure-ish** service code with minimal UI framework coupling:

- API request orchestration (via the web app’s API client)
- payload validation + normalization
- parsing utilities (citations, front-matter metadata)
- conversion to view models consumed by components

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Web UI root | `web/` | React/Map UI that consumes API payloads |
| Story UI area | `web/src/story/` | Story components, state, routing |
| API boundary | `src/server/` | API implementation; mediates graph access |
| API contracts | `src/server/contracts/**` | Contract snapshots + schemas (**not confirmed in repo**) |
| Graph build | `src/graph/` | Ontology + ingest + migrations |
| Story Nodes | `docs/reports/story_nodes/` | Authored story content |
| Schemas | `schemas/` | JSON schema validation targets |

### Suggested file tree for this sub-area

This is a recommended shape only. If the repo already has different filenames, preserve the **responsibility boundaries**.

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        └── 📁 services/
            ├── 📄 README.md                       # This doc
            ├── 📄 index.ts                        # Barrel exports
            ├── 📄 focusContext.service.ts         # Fetch + validate context bundles
            ├── 📄 storyNode.service.ts            # Load + normalize story node content
            ├── 📄 citations.service.ts            # Parse + map citations to evidence
            ├── 📄 auditModel.service.ts           # Build audit/provenance panel view models
            ├── 📄 focusHints.service.ts           # Apply focus_layers / focus_time / focus_center hints
            ├── 📄 cache.policy.ts                 # Cache keys + TTL + invalidation policy
            └── 📁 __tests__/                       # Unit tests for parsers/transformers
~~~

---

## 🧭 Context

### Background

KFM’s canonical ordering is non-negotiable:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Story Services sit at the UI side of this chain and exist to make sure:

- The UI only consumes data **via the API boundary**
- Focus Mode remains **provenance-linked**
- Story nodes render with **interactive citations**
- Optional Focus Mode metadata can steer map/timeline behavior

### Constraints and invariants

- **API boundary rule:** the UI does **not** connect to Neo4j directly. All access is mediated by contracted APIs that enforce redaction/provenance rules.
- **Provenance rule:** Focus Mode must only display provenance-linked narrative. If evidence links are missing, the UI must warn or suppress the claim.
- **Predictive/AI rule:** any predictive or AI-generated content is opt-in, includes uncertainty/confidence metadata, and never appears as unmarked fact.
- **No sensitive-location inference:** do not infer sensitive locations from user interactions, zoom behavior, or entity adjacency. Do not log precise sensitive coordinates if not permitted.

### Assumptions

- A Focus/Story API exists that can return a **context bundle** for a selected entity/story.
- Story nodes use Markdown with a citation syntax that must be rendered into interactive UI elements.
- Story nodes may include optional UI hints such as `focus_center`, `focus_time`, and `focus_layers`.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where is the authoritative Focus API contract snapshot stored? | API owners | TBD |
| Do we validate context bundles client-side against `schemas/storynodes/`? | UI + contracts | TBD |
| What is the caching policy for Focus Mode bundles (TTL vs version pin)? | UI | TBD |
| How are “restricted locations” generalized in API responses and signaled to UI? | Governance + API | TBD |

---

## 🗺️ Diagrams

### Focus Mode sequence

~~~mermaid
sequenceDiagram
  participant User
  participant UI as Web UI (FocusMode)
  participant Svc as Story Services
  participant API as API boundary (Focus/Story)
  participant Graph as Graph (Neo4j behind API)

  User->>UI: Select entity/story
  UI->>Svc: getFocusContext(entityId, options)
  Svc->>API: GET Focus context bundle (contracted)
  API->>Graph: Query with redaction + provenance rules
  Graph-->>API: Subgraph + provenance refs
  API-->>Svc: Context bundle (narrative + citations + audit flags + hints)
  Svc-->>UI: Normalized models (story HTML, citation index, audit model, focus hints)
  UI-->>User: Story + sources + map/timeline focus
~~~

### Service responsibilities map

~~~mermaid
flowchart LR
  A[API payload: context bundle] --> B[Validate + normalize]
  B --> C[Story Markdown render]
  B --> D[Citation extraction + evidence map]
  B --> E[Audit panel model]
  B --> F[Map/timeline focus hints]
  C --> G[UI components]
  D --> G
  E --> G
  F --> H[Map controller / timeline controller]
~~~

---

## 📦 Data and metadata

### Inputs

Typical inputs to services (from router/state/UI events):

- `entityId` or `storyNodeId`
- optional time window or view mode settings
- user preference flags for opt-in predictive/AI content (if supported by contracts)

### Outputs

Services should output UI-safe, typed models:

- `FocusContextModel` (normalized, defensive defaults)
- `RenderedStoryModel` (HTML + citation anchors)
- `CitationIndex` (citation → evidence reference → display metadata)
- `AuditPanelModel` (warnings, provenance, redaction notices)
- `FocusHints` (map center/zoom hints, timeline bounds, layer toggles)

### Sensitivity and redaction

- Never assume the client has clearance for sensitive fields.
- Do not persist sensitive payloads to long-lived storage unless explicitly approved.
- Any “restricted/generalized geometry” indicators from API should be surfaced in the audit panel.

### Telemetry signals

If telemetry is implemented for Focus Mode (optional), treat it as schema-governed:

| Signal | Source | Where recorded |
|---|---|---|
| `ui.focus.enter` | UI state transition | `docs/telemetry/` + `schemas/telemetry/` (**not confirmed in repo**) |
| `ui.focus.context_loaded` | API success | same |
| `ui.focus.citation.opened` | citation interaction | same |
| `ui.focus.ai_opt_in` | user toggle | same |

---

## 🌐 STAC, DCAT and PROV alignment

Even though this is UI code, the UI must preserve the traceability chain:

- Evidence references in the context bundle should link back to:
  - STAC Item IDs
  - DCAT dataset IDs
  - PROV activity/run IDs

Service code should:

- Preserve these identifiers when building the audit model.
- Provide stable “source cards” for citations so users can inspect evidence.
- Fail safely when evidence references are missing:
  - show an audit warning
  - avoid presenting an uncited claim as fact

---

## 🧱 Architecture

### Service design principles

- **Deterministic transforms:** given the same payload + options, produce the same models.
- **Side-effect boundaries:** isolate network calls; keep parsing/normalization pure.
- **Defensive validation:** assume payloads can be missing fields; validate before use.
- **Stable interfaces:** expose small, typed service functions.
- **Test-first:** citation parsing and normalization must have unit tests.

### Focus context service

Recommended interface shape:

~~~ts
export type FocusContextOptions = {
  includeAI?: boolean;        // opt-in only
  timeWindow?: { start: string; end: string };
};

export async function getFocusContext(
  entityId: string,
  options: FocusContextOptions
): Promise<FocusContextModel> {
  // 1) fetch contracted payload from API client
  // 2) validate/normalize
  // 3) render markdown + build citation index
  // 4) compute audit + focus hints
}
~~~

### Story node metadata hints

Story nodes may provide optional Focus Mode controls:

- `focus_center` (lon/lat)
- `focus_time` (time hint)
- `focus_layers` (layer toggles)

Services should interpret these hints and emit a `FocusHints` model for the map/timeline controllers.

### Citation rendering strategy

Story nodes use Markdown with citations in a token form such as:

- `【source†Lx-Ly】`

Recommended approach:

1. Compile Markdown → HTML using the project’s markdown renderer.
2. Post-process the HTML to detect citation tokens.
3. Replace citation tokens with clickable anchors that open source cards/popovers.
4. Ensure every citation token maps to an evidence reference supplied by the API; otherwise surface an audit warning.

### AI and predictive content handling

If the contract supports predictive/AI content:

- Treat it as **opt-in** only (`includeAI=true` style behavior).
- Render it in a visually distinct container with:
  - “machine-generated” labeling
  - uncertainty/confidence
  - evidence references (what was summarized/inferred from)
- Never merge AI text into the main narrative as if it were authored fact.

---

## 🧪 Validation and CI

### Minimum checks recommended for this area

- Unit tests:
  - citation token parser
  - story metadata parser (`focus_*` hints)
  - payload normalization defaults + error cases
- Integration tests:
  - Focus Mode flow renders story + citations with a sample payload
- Contract alignment:
  - service models match API contract shapes (ideally via generated types or schema validation)
- Security/privacy checks:
  - do not log raw payloads that may contain sensitive location details
- Accessibility:
  - citation affordances keyboard accessible
  - audit panel readable and navigable

---

## ⚖ FAIR+CARE and governance

### Review gates

Changes in this directory may require additional review when they:

- add new ways to display/derive location data
- alter citation behavior or allow uncited claims to display
- introduce new AI/predictive rendering paths
- add new telemetry that could expose sensitive interactions

### CARE and sovereignty considerations

- Do not “enhance” restricted locations via client-side inference (e.g., clustering + reverse inference).
- If story content intersects with protected knowledge, the UI must respect redaction/generalization outputs from the API and signal them clearly.

### AI usage constraints

- Allowed: summarization/structure extraction/translation/keyword indexing (as recorded in front-matter).
- Prohibited: generating new policy; inferring sensitive locations.

---

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README for Story Services boundary (Focus Mode + Story Nodes) | TBD |

---

## Footer refs

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Nodes: `docs/reports/story_nodes/`
- Schemas: `schemas/storynodes/` + `schemas/ui/` + `schemas/telemetry/`

---

