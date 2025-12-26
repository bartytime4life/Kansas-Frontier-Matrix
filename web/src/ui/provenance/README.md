---
title: "KFM Web UI — Provenance UI Module"
path: "web/src/ui/provenance/README.md"
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

doc_uuid: "urn:kfm:doc:web:ui:provenance:readme:v0.1.0-draft"
semantic_document_id: "kfm-web-ui-provenance-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:web:ui:provenance:readme:v0.1.0-draft"
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

# KFM Web UI — Provenance UI Module

Provenance rendering primitives for Focus Mode and Story Node experiences: **citations**, **evidence/source lists**, **audit flags**, and **source inspection**.

This module exists to support KFM’s non-negotiables:
- **Focus Mode is provenance-linked only** (no unsourced narrative).
- **UI provides audit affordances** (users can inspect provenance).
- **No hallucinated sources** (the UI must not attribute claims to sources unless they exist and resolve).

## 📘 Overview

### Purpose
- Provide reusable UI primitives to render provenance consistently across:
  - Focus Mode narrative panels
  - Story Node readers
  - Source sidebars / evidence drawers
  - Audit / warning indicators (missing citations, restricted fields, AI disclosure)
- Standardize how KFM renders the Story Node citation syntax (the `【…†Lx-Ly】` pattern).
- Make it hard to accidentally ship UI that shows claims without evidence pointers.

### Scope
| In Scope | Out of Scope |
|---|---|
| Rendering citations and “Sources” views | Generating provenance (ETL/catalog responsibility) |
| Showing audit flags/warnings from API | Querying Neo4j directly (API boundary only) |
| Linking to STAC/DCAT/PROV identifiers | Defining governance policy (human governance docs) |
| UI-side “missing provenance” safe fallbacks | Writing/curating Story Nodes (curation workflow) |
| Distinguishing opt-in AI content vs factual | Publishing new datasets (data lifecycle) |

### Audience
- Frontend engineers working in `web/` (React / MapLibre / Focus Mode)
- Backend/API engineers defining provenance payload contracts
- Curators and reviewers validating “evidence-first” narrative UX

### Key references (canonical)
- Master Guide: `../../../../docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `../../../../docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Story Node template: `../../../../docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract template: `../../../../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `../../../../docs/governance/ROOT_GOVERNANCE.md`

## 🗂️ Directory Layout

### This document
- `path`: `web/src/ui/provenance/README.md` (must match front matter)

### Related repository paths (canonical targets)
- ETL / pipelines: `../../../../src/pipelines/`
- Catalogs:
  - STAC: `../../../../data/stac/collections/` and `../../../../data/stac/items/`
  - DCAT: `../../../../data/catalog/dcat/`
  - PROV: `../../../../data/prov/`
- Graph: `../../../../src/graph/`
- API boundary + contracts: `../../../../src/server/` and `../../../../src/server/contracts/`
- Story Nodes: `../../../../docs/reports/story_nodes/`

### Module layout (recommended; not confirmed in repo)
~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        └── 📁 provenance/
            ├── 📄 README.md
            ├── 📄 index.ts                 # public exports (optional)
            ├── 📁 components/
            │   ├── 📄 ProvenancePanel.tsx  # combined panel (audit + sources)
            │   ├── 📄 SourcesSidebar.tsx   # list + filter + open source
            │   ├── 📄 CitationLink.tsx     # inline citation affordance
            │   └── 📄 AuditFlags.tsx       # warnings + status chips
            ├── 📁 hooks/
            │   ├── 📄 useProvenanceBundle.ts
            │   └── 📄 useCitationResolver.ts
            ├── 📁 lib/
            │   ├── 📄 citationSyntax.ts    # grammar + regex helpers
            │   ├── 📄 parseCitations.ts    # markdown -> tokens
            │   └── 📄 provenanceTypes.ts   # TS types for contracts
            └── 📁 __tests__/
                ├── 📄 parseCitations.test.ts
                └── 📄 ProvenancePanel.test.tsx
~~~

## 🧭 Context

### Why this module exists
KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This folder addresses the final leg: **how provenance is presented to users** so they can audit narrative claims, see evidence, and understand any redactions or AI disclosures.

### Constraints and invariants
- **API boundary invariant:** the UI must not query Neo4j directly; the API mediates all data access.
- **Evidence-first invariant:** if a narrative claim cannot be tied to evidence IDs/sources, the UI must:
  - show an audit warning, and/or
  - omit/disable the “publishable” rendering pathway (depending on app policy).
- **No hallucinated sources:** only render citations that resolve to a source record (or render them as broken/invalid with an explicit warning).
- **No YAML front-matter in code files:** keep YAML front matter to documentation markdown (like this README), not `.ts/.tsx` sources.

### Terminology (UI-friendly)
- **Citation token**: an inline reference inside narrative text. Example: `【source:foo†L10-L20】`
- **Source record**: metadata describing a cited thing (title, URL, excerpt, dataset IDs).
- **Evidence pointer**: stable identifiers that tie the source to KFM catalogs:
  - STAC Item ID / Collection ID
  - DCAT dataset ID
  - PROV activity ID
- **Audit flag**: structured warnings from API or UI validation (missing sources, restricted fields, AI disclosure).

## 🗺️ Diagrams

### Provenance in the end-to-end pipeline (UI perspective)
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[API Boundary]
  D --> E[Web UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph E2[UI Provenance Module]
    P1[Citation Parsing]
    P2[Sources Sidebar]
    P3[Audit Flags]
    P4[Evidence Links]
  end

  E --> E2
~~~

### Focus Mode context fetch and provenance handoff (example; endpoint names not confirmed)
~~~mermaid
sequenceDiagram
  participant User
  participant UI
  participant API
  participant Graph

  User->>UI: Select entity/story
  UI->>API: GET /focus/{entityId}
  API->>Graph: Fetch subgraph + provenance refs
  Graph-->>API: Context bundle
  API-->>UI: narrative + citations + sources + audit flags
  UI-->>User: Render story + provenance panel
~~~

### Citation resolution inside the UI
~~~mermaid
flowchart TB
  M[Story Markdown] --> R[Markdown Renderer]
  R --> T[Citation Tokenizer]
  T --> V[Validator: tokens -> sources[]]
  V -->|resolved| C[Render CitationLink]
  V -->|missing| W[Render warning / broken citation]
  C --> S[Sources Sidebar / Drawer]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus context bundle | JSON | API (Focus Mode endpoint) | Contract tests + schema validation (API-side) |
| Narrative text | Markdown | Story Node in response payload | Citation parse + audit checks (UI-side) |
| `sources[]` | JSON array | API payload | IDs must be stable + resolvable |
| `audit_flags[]` | JSON array | API payload or UI checks | Must render user-visible affordance |
| Optional AI blocks | JSON/Markdown | API payload (opt-in) | Must be labeled + confidence metadata |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Provenance panel UI | React | runtime | UI contracts + component tests |
| Source inspection views | React | runtime | safe-link policy + a11y |
| Optional telemetry events | JSON | telemetry (not confirmed in repo) | `schemas/telemetry/` (if adopted) |

### Sensitivity & redaction (UI rules)
- Never “reconstruct” restricted locations from partial hints.
- If a source record indicates restricted content, render:
  - a “Restricted” badge and explanation
  - generalized location (e.g., county-level) if provided
  - link suppression if policy requires (policy lives in governance docs; UI obeys payload)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- UI should treat STAC identifiers as the stable handles for evidence assets.
- Typical UI behaviors:
  - “Open STAC Item” (if exposed via an API/catalog endpoint)
  - “View STAC assets” (images, maps, documents) with attribution

### DCAT
- UI should provide dataset-level context when available:
  - dataset title/description/license
  - publisher/contact (if present)
- If the API provides a “dataset detail” route, provenance UI should link to it (route not confirmed in repo).

### PROV-O
- UI should expose transformation lineage when present:
  - “Generated by” activity (run ID, tool ID, timestamp)
  - “Derived from” upstream datasets/items
- Do not attempt to compute lineage client-side; render what the API provides.

### Versioning expectations
- If the backend provides predecessor/successor links:
  - show “Supersedes / Superseded by” in the provenance panel
- Versioning mechanism is **not confirmed in repo**; defer to API contracts.

## 🧱 Architecture

### Subsystem contracts (UI-side)
KFM expects the UI to provide:
- **Layer registry + a11y + audit affordances** (no hidden data leakage)
- Provenance rendering that supports Focus Mode’s “evidence-first” rule

### Components (recommended; not confirmed in repo)
| Component | Responsibility | Interface (suggested) |
|---|---|---|
| `parseCitations()` | Extract citation tokens from Markdown | `(markdown: string) => { html: string; citations: CitationRef[] }` |
| `CitationLink` | Render an inline citation with click/hover | `({ ref, onOpenSource })` |
| `SourcesSidebar` | Display all sources referenced in story node | `({ sources, activeSourceId })` |
| `AuditFlags` | Visualize warnings (missing citations, restricted, AI) | `({ flags })` |
| `ProvenancePanel` | One panel to rule them all | `({ bundle })` |

### Citation syntax (UI contract)
Story Nodes use a citation bracket syntax:

- Single citation:
  - `【source-id†L10-L20】`
- Multiple citations can appear back-to-back:
  - `...claim...【source-a†L1-L3】【source-b†L88-L90】`

Minimum UI expectations:
- Parse and render citation tokens as interactive elements.
- Resolve `source-id` against `sources[]` from the API payload.
- If `source-id` does not resolve, render a visible warning (do not silently drop it).

### Example provenance payload shape (illustrative; not confirmed in repo)
~~~json
{
  "entity": { "id": "place:leavenworth", "type": "Place", "name": "Leavenworth" },
  "storyNode": {
    "id": "story:fort-leavenworth-1827",
    "title": "Fort Leavenworth in the 1820s",
    "narrative_markdown": "Fort Leavenworth was established in 1827.【source:mil-archives†L10-L20】"
  },
  "sources": [
    {
      "id": "source:mil-archives",
      "title": "Military Archives",
      "url": "https://example.org/archive/123",
      "excerpt": "…",
      "stac_item_ids": ["stac:item:..."],
      "dcat_dataset_id": "dcat:dataset:...",
      "prov_activity_id": "prov:activity:..."
    }
  ],
  "audit_flags": [
    { "code": "OK", "severity": "info", "message": "All citations resolved." }
  ]
}
~~~

## 🧠 Story Node & Focus Mode Integration

### Focus Mode behavior expectations
- Focus Mode is a specialized UI state:
  - enter Focus Mode with an entity/story ID
  - fetch a context bundle from API
  - render narrative + citations + provenance panel
  - adjust map/timeline from story metadata when available
- Focus Mode should include subcomponents:
  - story narrative renderer (with citations)
  - “audit/provenance” panel
  - timeline (optional)
  - map (MapLibre/Cesium; optional)

### Audit affordances (must-have UX)
- Users must be able to:
  - click/hover citations to see source titles/excerpts (if provided)
  - open a Sources view listing all referenced sources
  - see warnings if content lacks citation
  - distinguish AI-generated content (opt-in) from factual narrative

### Optional Focus Mode controls (from Story Node metadata)
Story Nodes may include map/timeline hints such as:
- `focus_center`
- `focus_time`
- `focus_layers`

If provided in the payload, provenance UI should cooperate with the Focus Mode container to ensure the user sees the evidence context alongside these UI shifts.

## 🧪 Validation & CI/CD

### Validation checklist (UI module)
- [ ] Citation parser correctly identifies `【…†Lx-Ly】` tokens.
- [ ] Every rendered citation resolves to `sources[]` (or shows a warning).
- [ ] “Sources” panel is keyboard accessible and screen-reader friendly.
- [ ] External links use safe defaults (`rel="noopener noreferrer"`, etc.).
- [ ] AI content (if present) is labeled, opt-in, and includes confidence metadata.
- [ ] No direct graph access paths exist in the UI layer.

### Minimum CI gates (project-wide expectations)
- Markdown protocol validation
- Schema validation (STAC/DCAT/PROV/telemetry where applicable)
- API contract tests
- UI layer registry schema checks (where applicable)
- Security + sovereignty scanning gates (where applicable)

## ⚖ FAIR+CARE & Governance

### Governance review triggers (common)
- New sensitive layers or sensitive provenance rendering behaviors
- New AI narrative behaviors or new “AI explanation” UI blocks
- New external data sources exposed in Sources views
- New public-facing endpoints used by this module

### Sovereignty safety
- Follow redaction/generalization rules for restricted locations.
- Treat culturally sensitive knowledge as high-risk by default; obey API payload restrictions and governance policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0-draft | 2025-12-26 | Initial provenance UI module README | TBD |

---

Footer refs:
- Governance: `../../../../docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `../../../../docs/governance/ETHICS.md`
- Sovereignty: `../../../../docs/governance/SOVEREIGNTY.md`

