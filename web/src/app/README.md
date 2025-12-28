---
title: "KFM Web UI — web/src/app README"
path: "web/src/app/README.md"
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

doc_uuid: "urn:kfm:doc:web:src-app:readme:v1.0.1"
semantic_document_id: "kfm-web-src-app-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:web:src-app:readme:v1.0.1"
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

> **Purpose required:** Define what belongs in `web/src/app/` and the non-negotiable rules for route-level UI code:
> **API boundary only**, **provenance-linked narrative only**, and **redaction and sensitivity respected end-to-end**.

# `web/src/app/` — Route and layout layer

This folder is the route tree and top-level layout entry point for the KFM web UI.

It defines:
- what routes exist and how they are grouped,
- global layout, providers, and app shell wiring,
- route-level loading, error, and not-found boundaries,
- the required route-level pattern for requesting KFM data through the API boundary.

If your routing framework differs, keep the invariants in this README and update:
- the expected file tree,
- route conventions and filenames,
- and any framework-specific examples.

---

## 📘 Overview

### Purpose
- Provide a governed contract for what belongs in `web/src/app/`.
- Keep the route layer aligned with KFM’s canonical pipeline ordering:
  **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- Prevent architectural drift by enforcing:
  - UI never reads Neo4j directly,
  - UI consumes only contracted APIs and published catalogs,
  - Focus Mode renders provenance-linked narrative only,
  - sensitivity and redaction are honored end-to-end.

### Scope

| In scope | Out of scope |
|---|---|
| Route folders/files, layout shells, provider wiring, route-level loading/error boundaries | Implementing the API service (belongs in `src/server/`) |
| Route-level patterns for data-fetching via the API boundary | Graph logic, ontology changes, ingest and migrations (belongs in `src/graph/`) |
| Rules for provenance display, citations, and redaction notices in route-level pages | ETL, catalog build, and provenance emission (belongs in `src/pipelines/` + `data/**`) |
| How to add routes for map, stories, and Focus Mode | Governance policy authoring (belongs in governed governance docs) |

### Audience
- Primary: Frontend maintainers and contributors working in `web/`.
- Secondary: API maintainers and narrative curators who need to understand UI consumption rules.

### Definitions and glossary link
- Glossary: `docs/glossary.md` (not confirmed in repo — update if located elsewhere)

Terms used in this doc:
- **API boundary:** The contracted REST/GraphQL layer that mediates all graph and catalog access for clients.
- **Story Node:** A governed narrative artifact that links claims to evidence identifiers.
- **Focus Mode:** A UI view that renders provenance-linked narrative with map/timeline context.
- **Layer registry:** A schema-validated list of map layers, toggles, legends, and access rules.

### Key artifacts this doc points to

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + CI gates |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical homes + contract rules |
| Web UI root | `web/` | Frontend | React + map client + narrative surfaces |
| UI schemas | `schemas/ui/**` | Platform | JSON Schemas for layer registries |
| Layer registries | `web/**/layers/**` | Frontend | Must validate against `schemas/ui/**` |
| API boundary | `src/server/**` | API | UI consumes contracts only |
| API contracts | `src/server/contracts/**` | API | Source-of-truth payload definitions |
| Story Nodes | `docs/reports/story_nodes/**` | Narrative | Focus Mode consumes governed story artifacts |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Provenance-linked story standard |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governed Markdown structure |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Required for API contract changes |

### Definition of done for this document
- [ ] Front-matter complete and `path` matches `web/src/app/README.md`
- [ ] States UI invariants clearly:
  - [ ] UI never reads Neo4j directly
  - [ ] UI consumes only API and catalog endpoints
  - [ ] Focus Mode renders provenance-linked content only
- [ ] Directory responsibilities and placement rules are explicit
- [ ] Route addition checklist is repeatable and framework-agnostic
- [ ] Mentions layer registry schema validation expectations
- [ ] Governance, sensitivity, and redaction obligations are explicit
- [ ] Version history updated

---

## 🗂️ Directory Layout

### This document
- `path`: `web/src/app/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI | `web/` | Web app code and UI registries |
| UI layer registries | `web/**/layers/**` | Layer toggles, legends, metadata and access rules |
| UI schemas | `schemas/ui/**` | JSON Schemas used to validate UI registries |
| API boundary | `src/server/**` | Contracted access layer with redaction enforcement |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL schemas and payload definitions |
| Graph | `src/graph/**` | Ontology bindings, ingest, migrations |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | Evidence, discovery, and lineage artifacts |
| Story Nodes | `docs/reports/story_nodes/**` | Governed narratives consumed by Focus Mode |

### Expected file tree for this sub-area
This is the recommended structure for an app-router style route tree. Filenames and conventions may differ.

~~~text
📁 web/
└── 📁 src/
    └── 📁 app/
        ├── 📄 README.md
        ├── 📄 layout.<ext>                     # global app shell + providers
        ├── 📄 page.<ext>                       # root route entry
        ├── 📄 error.<ext>                      # route error boundary
        ├── 📄 not-found.<ext>                  # 404 boundary
        ├── 📄 globals.<ext>                    # global styles
        │
        ├── 📁 (routes)/                        # optional route groups
        │   ├── 📁 explore/                     # map/timeline exploration
        │   ├── 📁 stories/                     # Story Node browsing
        │   └── 📁 focus/                       # Focus Mode routes
        │
        ├── 📁 _components/                     # route-local components
        └── 📁 _lib/                            # route-local helpers
~~~

---

## 🧭 Context

### How this fits the canonical pipeline
KFM’s UI layer is downstream of the API boundary.

Upstream outputs and identifiers:
- ETL emits staged datasets under `data/<domain>/{raw,work,processed}/`.
- Catalog build emits STAC/DCAT/PROV under:
  - `data/stac/collections/` and `data/stac/items/`
  - `data/catalog/dcat/`
  - `data/prov/`

Downstream consumption:
- The graph stores references to catalog identifiers and is accessed through the API boundary.
- The UI consumes:
  - contracted API responses,
  - published catalog endpoints,
  - governed story artifacts.

### Non-negotiable invariants
- UI does not connect to Neo4j directly.
  - No Neo4j drivers, no Cypher, no graph credentials in `web/`.
- API boundary is mandatory.
  - Route code calls only API endpoints and catalog endpoints.
- Focus Mode is provenance-linked only.
  - If a story element cannot produce evidence identifiers, it must not render as fact.
- Redaction and generalization must be respected.
  - If the API indicates redaction was applied, the UI must surface a clear notice and must not attempt to reconstruct detail.

### Practical placement rule
Keep `web/src/app/` thin:
- Routes and layouts compose screens from reusable UI building blocks.
- Data shaping and redaction logic lives at the API boundary, not in the route layer.

---

## 🧱 Route and layout responsibilities

### What belongs in `web/src/app/`
- Route segment definitions and grouping
- Layout shells and provider wiring
- Route-level boundaries:
  - loading states
  - error states
  - not-found states
- Route-level composition that assembles a page from existing components

### What does not belong in `web/src/app/`
- Domain feature logic that should be reused across multiple routes
- Complex client-side state machines for map and narrative features
- API payload reshaping that attempts to bypass redaction or classification
- Direct reads of `data/**` outputs

### Route conventions
Use route-level code to do only what routes must do:
- choose what data is needed,
- request it through the API boundary,
- render it with provenance and sensitivity signals.

Prefer reusable modules elsewhere in `web/src/**` for:
- map components and layer rendering,
- story rendering and citation UI,
- shared UI elements and services.

Paths for those modules vary by repo; update based on the actual `web/src/**` structure.

---

## 🔌 Data access pattern

### Required data sources
Route-level UI code may consume:
- API responses from `src/server/**` endpoints
- published STAC/DCAT/PROV catalogs
- Story Nodes served via API or a governed content pipeline

### Forbidden data sources
Route-level UI code must not:
- connect to Neo4j
- import or read raw/work/processed datasets from `data/**` via filesystem shortcuts
- render narrative text as fact without evidence identifiers

### Contract-first usage
When requesting data:
1. Use the API boundary and contract-defined payload shapes.
2. Validate and render classification/redaction flags, not just the “happy path”.
3. Treat contract changes as governed changes:
   - if you need a new field or endpoint, use the API Contract Extension template.

### Error and not-found behavior
- Use route-level boundaries to keep failure modes consistent:
  - missing entity or story node → not-found state
  - upstream service failure → error state with retry guidance
  - redaction applied → render with redaction notice, not as an error

### Example route request
~~~ts
// Pseudocode — adapt to your framework/router and API client.
// Key rule: call only the API boundary; do not connect to the graph.

async function loadFocusContext(focusId: string) {
  const res = await fetch(`/api/focus/${focusId}`); // endpoint shape not confirmed in repo
  if (res.status === 404) return { kind: "not_found" };
  if (!res.ok) return { kind: "error" };

  const payload = await res.json();

  // Required UI behavior:
  // - render citations/evidence IDs
  // - render redaction indicators if present
  // - do not infer or reconstruct sensitive locations
  return { kind: "ok", payload };
}
~~~

---

## 🧠 Story Node and Focus Mode integration

### What Focus Mode must guarantee
- Every factual claim displayed must trace to evidence identifiers:
  - STAC Item or Collection IDs
  - DCAT dataset identifiers
  - PROV activity or bundle identifiers
- The UI must provide an evidence surface:
  - citations, source metadata, and “view dataset” affordances
- The UI must preserve fact vs inference separation when story content includes interpretation.

### Recommended context bundle fields
When rendering a Story Node or Focus Mode context, ensure the UI can handle:
- canonical graph entity IDs (resolved via API)
- evidence identifiers (STAC/DCAT/PROV)
- licensing and attribution for assets
- sensitivity and redaction flags

### Optional structured controls
Story Nodes may include structured controls to guide Focus Mode. These are UI inputs and are not evidence.

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Sensitivity handling
If a Story Node or layer touches sensitive or restricted locations:
- prefer generalized geometry and coarse regions as provided by the API
- do not encourage precision zooming or “reconstruction by overlay”
- render a clear redaction or generalization notice when indicated by the API

---

## 🗺️ Diagrams

### System boundary view

~~~mermaid
flowchart TB
  subgraph UI["UI web"]
    A["Routes and layouts web/src/app"]
    L["Layer registries web/**/layers/**"]
    V["Views map timeline story focus"]
  end

  subgraph API["API boundary src/server"]
    C["Contracts src/server/contracts"]
    E["Endpoints REST or GraphQL"]
    R["Redaction and generalization enforcement"]
  end

  subgraph Evidence["Evidence and provenance"]
    S["STAC data/stac"]
    D["DCAT data/catalog/dcat"]
    P["PROV data/prov"]
  end

  subgraph Graph["Graph src/graph"]
    G["Neo4j graph layer"]
  end

  A --> E
  V --> E
  L --> V
  C --> E
  E --> R
  E --> S
  E --> D
  E --> P
  E --> G
~~~

---

## 📦 Data and metadata

### What the route layer consumes
Route-level code should consume:
- API responses shaped by contracts
- catalog endpoints that expose STAC/DCAT/PROV artifacts
- story artifacts that include evidence identifiers

### Provenance surface requirements
When displaying a dataset layer, evidence panel, or story claim, the UI should make it possible to:
- identify the dataset or artifact ID
- view license and attribution
- navigate to catalog context for STAC/DCAT/PROV records

### Layer registry rules
- Layer registries must validate against `schemas/ui/**`.
- Layers that reference evidence must include provenance pointers and must not bypass access rules.

---

## 🌐 STAC, DCAT and PROV alignment

When the UI displays:
- a map layer,
- a claim in Focus Mode,
- or a dataset metadata panel,

it must be possible to trace to:
- a STAC Item or Collection
- a DCAT dataset record where applicable
- a PROV activity or bundle that describes lineage

No orphan facts and no orphan datasets.

---

## 🧪 Validation and CI/CD

### Validation checklist
- [ ] Markdown protocol validation
- [ ] Link and reference checks
- [ ] UI lint and typecheck
- [ ] UI layer registry schema validation against `schemas/ui/**`
- [ ] Forbidden dependency checks for direct graph access in `web/`
- [ ] Accessibility checks
- [ ] Secrets and PII scanning
- [ ] Sensitive location leakage checks where applicable

### Reproduction commands
~~~bash
# Example placeholders — replace with repo-specific commands

# UI checks
# <pkg> lint
# <pkg> typecheck
# <pkg> test

# UI schema validation
# <validator> schemas/ui/** web/**/layers/**

# Forbidden dependency scan
# <grep-tool> "neo4j://" web/
# <grep-tool> "neo4j-driver" web/
~~~

### Telemetry signals
If telemetry is implemented, UI should emit signals that allow audits without exposing sensitive detail.

~~~text
- focus_mode_redaction_notice_shown (layer_id, redaction_method)
- promotion_blocked (reason, scan_results_ref)
~~~

---

## ⚖ FAIR+CARE and governance

### Review gates
Governance review is required when UI changes:
- expand access to sensitive or restricted location detail
- add export or download affordances for potentially sensitive layers
- change provenance and citation rendering
- introduce AI-generated narrative into user-visible surfaces

### CARE and sovereignty considerations
- Treat culturally sensitive locations as high-risk by default.
- Ensure interaction patterns do not undermine generalization:
  - zoom thresholds
  - clustering behavior
  - tooltips and coordinate precision
  - filtering and layer composition

### AI usage constraints
- Allowed: summarization and formatting that preserves evidence links and uncertainty labels.
- Prohibited: presenting generated content as fact, inferring sensitive locations, or bypassing governance rules.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.1 | 2025-12-28 | Re-structured to align with Universal template sections, clarified invariants, added route checklist and governance gates | (you) |
| v1.0.0 | 2025-12-25 | Initial `web/src/app/` README establishing route-layer responsibilities and invariants | (you) |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
