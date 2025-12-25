---
title: "KFM Web UI — Story Model (Focus Mode View-Model Layer)"
path: "web/src/story/model/README.md"
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

doc_uuid: "urn:kfm:doc:web:story:model:readme:v1.0.0"
semantic_document_id: "kfm-web-story-model-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:model:readme:v1.0.0"
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

# 🧠 Story Model — `web/src/story/model`

> **Purpose (required):** Define the responsibilities, boundaries, and validation expectations for the **Story Model** layer of the KFM Web UI.  
> The Story Model converts **API-delivered Focus Mode context** and **Story Node v3 content** into deterministic, provenance-preserving **UI view models** (for narrative panels, citations, maps, and timelines).

## 📘 Overview

### Purpose

- Provide a single, predictable “model layer” for story rendering in the UI.
- Enforce **Focus Mode v3** constraints at the UI boundary:
  - **No orphan facts** (everything displayed is provenance-linked).
  - **AI-generated elements are explicitly labeled and gated** (only shown if enabled by product rules / user opt-in).  
- Prevent architecture drift by documenting **non-negotiable boundaries** (UI never queries Neo4j directly; UI consumes contracts via APIs).  

### Scope

| In Scope | Out of Scope |
|---|---|
| Transforming Focus Mode / Story APIs into view models (DTO → normalized model → selectors) | Implementing API endpoints or graph queries |
| Parsing + structuring Story Node v3 narrative for UI rendering (headings, citations, evidence bundles, focus controls) | Authoring/curating story content (Story Nodes live in `docs/`, not in UI code) |
| Provenance + citation integrity checks **inside the UI layer** (defensive validation) | Writing governance policy (lives in governed standards/docs) |
| Redaction/generalization handling in rendering (e.g., masking sensitive locations) | Defining new sovereignty rules (requires governance review) |

### Audience

- Primary: Web/UI engineers working under `web/`
- Secondary: Narrative curators verifying how Story Nodes render in Focus Mode
- Tertiary: API/Graph maintainers validating contract expectations and evidence handoff

### Definitions (link to glossary)

- Link: `docs/glossary.md` (**not confirmed in repo** — create if missing)
- Terms used in this doc:
  - **Focus Mode:** An interactive UI view combining narrative + map/timeline, constrained to provenance-linked content.
  - **Story Node (v3):** A governed narrative artifact with front-matter + citations and optional Focus Mode controls.
  - **Context bundle:** The API response that includes entity context, sources/evidence references, and story payload.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Canonical pipeline ordering + invariants |
| Story Node Template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Structure + citation expectations for Focus Mode |
| Universal Doc Template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs Team | Governed Markdown structure for this README |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**not confirmed in repo**; planned) | Arch Team | Canonical paths + contract locations |
| API Contract Extension Template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API Team | Use when adding/extending Focus Mode endpoints |
| This module | `web/src/story/model/` | Web Team | Story model types/adapters/selectors live here |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches)
- [ ] Scope + boundaries clearly prevent “UI reads Neo4j” drift
- [ ] Focus Mode v3 rules are explicit (provenance-only + AI labeling/gating)
- [ ] Validation steps are listed and repeatable (CI-friendly)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Footer refs present (do not remove)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/model/README.md` (must match front-matter)

### Related repository paths

> Note: Some paths below are “expected canonical” per architecture documents and may be **not confirmed in repo** yet.

| Area | Path | What lives here |
|---|---|---|
| Data lifecycle | `data/` | `raw/` → `work/` → `processed/` datasets |
| Catalogs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | STAC/DCAT/PROV evidence artifacts used downstream |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/UI/story nodes) |
| ETL/Pipelines | `src/pipelines/` | Deterministic ingestion + transformations |
| Graph | `src/graph/` | Neo4j graph build + ontology bindings |
| API | `src/server/` | API implementation (contract-first) |
| API Contracts | `src/server/contracts/` | OpenAPI/GraphQL schemas (contract source-of-truth) |
| UI (Web) | `web/` | React/Map UI + Focus Mode |
| Story Nodes | `docs/reports/story_nodes/` | `draft/` + `published/` story markdown (**not confirmed in repo**) |
| Runs/Experiments | `mcp/runs/` · `mcp/experiments/` | Run logs + reproducibility artifacts |
| CI/Automation | `.github/workflows/` | CI workflows for lint/schema/security checks |

### This module (local layout)

> Recommended structure (subfolders **not confirmed in repo**; align to this when adding new code).

~~~text
web/
└── 🌐 src/
    └── 📚 story/
        └── 🧠 model/
            ├── 🧾 README.md  — you are here
            ├── 🧩 adapters/  — API DTO → normalized model
            ├── 🧷 parsers/   — Story Node v3 Markdown → render model
            ├── 🧠 selectors/ — derived selectors for Focus Mode UI
            ├── 🛡 validators/ — provenance/citation/redaction checks
            ├── 🧱 types/     — shared Story/Focus types
            └── 🧪 __tests__/ — unit tests (model-level)
~~~

## 🧭 Context

### Placement in the canonical pipeline (non-negotiable ordering)

The Story Model is a **UI-layer** concern, downstream of catalogs, graph, and API:

- ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode

### Non-negotiable invariants for this module

- **UI never queries Neo4j directly.** All dynamic data access is via **contracted APIs** (or static catalogs) only.
- **No unsourced narrative in published Focus Mode.** Everything rendered must be provenance-linked.
- **Any AI-generated elements must be clearly indicated** and must not bypass citation/provenance requirements.
- **Sensitive location handling** must respect sovereignty and redaction rules (generalize/mask as required).

### What “Story Model” means in KFM (UI definition)

- A deterministic transformation layer:
  - **Input:** API “context bundle” + Story Node payload (and/or references to published story nodes)
  - **Output:** view models used by Focus Mode UI components (narrative blocks, citations, evidence panels, layer toggles, time ranges, map focus)

## 🗺️ Diagrams

### Story/Focus dataflow (UI boundary emphasized)

~~~mermaid
flowchart LR

  subgraph Upstream
    A["STAC/DCAT/PROV Evidence Artifacts"] --> B["Neo4j Graph (semantics)"]
    B --> C["API Layer (contract-first)"]
  end

  C --> D["Focus Mode Context Bundle (API response)"]
  D --> E["Story Model (this module)"]
  E --> F["Focus Mode UI: Narrative Panel"]
  E --> G["Focus Mode UI: Map/Timeline Controls"]
  E --> H["Focus Mode UI: Provenance/Audit Panel"]
~~~

### Model layering inside the UI (suggested)

~~~mermaid
flowchart TB

  A["API DTOs (contract types)"] --> B["Normalize + Validate"]
  B --> C["Story Render Model"]
  C --> D["Selectors (Focus Mode state)"]
  D --> E["Components (Narrative/Map/Timeline)"]
~~~

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- The Focus Mode UI should only render **published** Story Nodes that have passed validation (**not confirmed in repo** — implement validator + gating if missing).
- Story Nodes should be renderable even when the UI is offline from the graph (because the UI relies on **API outputs / static evidence references**, not direct graph access).

### Provenance-linked narrative rule (UI enforcement)

- Every factual claim shown in Focus Mode must be backed by:
  - a cited **dataset/document identifier**, and
  - a resolvable evidence reference in the provided context bundle.

If a claim’s evidence cannot be resolved, the UI must:
- either hide the claim (strict mode), or
- render it with a visible warning in an “audit” panel (review mode).

### Optional structured controls (Story Node v3)

Story Nodes may include optional Focus Mode controls (shape follows the Story Node template; exact parsing rules may vary by implementation):

~~~yaml
focus_layers:
  - "TBD-layer-id"
focus_time: "TBD-iso8601"
focus_center: [-98.0000, 38.0000]
~~~

**Story Model responsibilities for controls:**
- Validate that referenced layer IDs exist in the UI layer registry (**not confirmed in repo**).
- Validate time formats, coordinate shape, and any sensitivity constraints before applying to the map.

### AI content (strictly gated)

If AI-generated narrative or explanations exist:
- They must be **explicitly labeled** in the render model (never blended into “facts”).
- They must remain **citation-bound** (no hallucinated sources).
- They must be shown only when product rules and/or user settings allow it (**opt-in** behavior; exact mechanism not confirmed in repo).

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Type-level validation (TS types compile; contract types match expected shapes)
- [ ] Provenance integrity checks (every rendered claim resolves to evidence IDs)
- [ ] Citation rendering checks (no broken citation pointers; no empty sources)
- [ ] Redaction checks (sensitive location detail is masked/generalized as required)
- [ ] Accessibility checks for Focus Mode rendering (headings, links, citation widgets)

### Reproduction (placeholders)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run web lint + typecheck
# 2) run story model unit tests
# 3) run schema/contract validation (if applicable)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Focus render failures (invalid citations, missing evidence) | UI runtime logs | `docs/telemetry/` (**not confirmed in repo**) |
| Contract mismatch rate | integration tests | `tests/` (**not confirmed in repo**) |
| “Strict mode” gating count | UI counters | `docs/telemetry/` (**not confirmed in repo**) |

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus Mode context bundle | JSON | API response | Contract tests + runtime guards |
| Story Node payload | Markdown | API and/or `docs/reports/story_nodes/published/` | Story Node validator (CI) + parse checks |
| Evidence references | IDs/URIs | STAC/DCAT/PROV + API | Resolve + display in audit panel |
| UI layer registry | JSON/TS config | `web/` | Validate against `schemas/ui/` (**not confirmed in repo**) |

### Outputs

| Output | Format | Produced by | Used by |
|---|---|---|---|
| Narrative render model | Typed objects | Story Model | Focus Mode narrative panel |
| Citation + evidence model | Typed objects | Story Model | Citation renderer + audit panel |
| Map/timeline focus instructions | Typed objects | Story Model | MapLibre/Timeline components |
| Redaction flags / warnings | Typed objects | Story Model | UI safety + governance review UX |

### Sensitivity & redaction (UI perspective)

- Do not display:
  - secrets/tokens/keys,
  - private URLs,
  - or precise location details that violate sovereignty constraints.
- When content is “location-bearing,” prefer generalized geometry/centroids and show a visible “precision reduced” notice (**rules defined by governance docs**).

## 🌐 STAC, DCAT & PROV Alignment

### What this module must preserve

Even though this is UI code, it must preserve and surface evidence integrity:

- Maintain references to:
  - STAC Item/Collection IDs (where relevant)
  - DCAT dataset IDs
  - PROV activity/run IDs (where available)
- Do not “summarize away” evidence metadata in the model layer—carry IDs through to:
  - citation popovers,
  - evidence panels,
  - and audit views.

### Provenance requirements (UI rendering expectations)

- Each narrative block should be renderable alongside:
  - evidence links/identifiers,
  - any confidence/uncertainty metadata (if present),
  - and sensitivity flags.

## 🧱 Architecture

### Responsibilities (must do)

- Convert API context bundles into stable view models (normalize, validate, select).
- Provide a single place for:
  - citation parsing,
  - evidence resolution,
  - redaction handling,
  - Focus Mode control validation.
- Support contract-first development by aligning model inputs with API contracts (avoid duplicating contract definitions).

### Non-responsibilities (must NOT do)

- No Neo4j calls.
- No direct file reads from `data/` at runtime (except via approved static build steps — not confirmed in repo).
- No creation of new narrative content (UI renders curated stories; it does not invent facts).

### Example (illustrative) context bundle shape (not confirmed in repo)

~~~ts
// NOTE: Illustrative only. Prefer generated types from src/server/contracts/ if available.
export interface FocusModeContextBundle {
  entity: { id: string; type: string; label: string };
  story?: { id: string; markdown: string; status: "draft" | "published" };
  sources: Array<{ id: string; kind: "stac" | "dcat" | "prov" | "document"; ref: string }>;
  focus?: { layers?: string[]; time?: string; center?: [number, number] };
  ai?: { enabled: boolean; notes?: string; confidence?: number };
}
~~~

## ⚖ FAIR+CARE & Governance

### Review gates

Any of the following changes should trigger review (per governance roles/process):

- Changing citation parsing rules or evidence resolution logic
- Changing redaction/generalization behavior
- Adding or expanding AI-rendered narrative behavior
- Adding new Focus Mode control behaviors that could reveal sensitive locations through interaction/zoom

### CARE / sovereignty considerations

- This module must respect sovereignty policies for:
  - location precision,
  - community-controlled data visibility,
  - and “authority to control” constraints.
- If unsure, treat new story rendering features as **high-risk by default** and require review.

### AI usage constraints

- Allowed in this document/module context:
  - summarization/structure extraction for tooling (offline), translation, keyword indexing
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly),
  - presenting AI outputs as facts without evidence and labeling.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial Story Model README scaffold | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

