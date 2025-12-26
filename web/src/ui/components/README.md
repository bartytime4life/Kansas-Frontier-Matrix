---
title: "KFM Web UI — Components"
path: "web/src/ui/components/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:web:ui:components-readme:v1.0.0"
semantic_document_id: "kfm-web-ui-components-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:ui:components-readme:v1.0.0"
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

# KFM Web UI — Components

---

> **Purpose (required):** Define conventions and hard constraints for UI components under `web/src/ui/components/`, ensuring the UI stays downstream of the API boundary and that Focus Mode + Story Node rendering remain provenance-linked.

## 📘 Overview

### Purpose

- Provide **component taxonomy + conventions** for the KFM web UI.
- Encode **non-negotiable architecture rules** that UI code must follow (API boundary, provenance-only Focus Mode).
- Make review easier by standardizing where component types live and how they connect to contracts/schemas.

### Scope

| In Scope | Out of Scope |
|---|---|
| Reusable UI components under `web/src/ui/components/` | Changing API contracts, graph queries, or data pipelines |
| Map UI composition (Map view wrappers, layer controls, legends) | Defining new ontology labels/relationships |
| Story Node and citation rendering components | Writing/curating Story Nodes (see `docs/reports/story_nodes/`) |
| Focus Mode panel/view components | Governance policy creation (handled under `docs/governance/`) |

### Audience

- Primary: Front-end contributors working in `web/`
- Secondary: Reviewers validating API/UI boundaries; Story Node curators verifying narrative + citation rendering; CI maintainers enforcing UI gates

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc:
  - **API boundary**: UI never reads Neo4j/graph directly; it uses contracted APIs only.
  - **Layer registry**: JSON/config that declares which layers exist and how they render (validated by `schemas/ui/**`).
  - **Story Node**: governed Markdown narrative used by Focus Mode.
  - **Focus Mode**: UI view that immerses a user in a story/analysis; must display provenance-linked content only.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + stage boundaries |
| v13 Redesign Blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Contract-first repo structure (some paths may be *not confirmed in repo*) |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governing structure used here |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative Curators | Citation + provenance rules for narratives |
| UI schemas | `schemas/ui/` | Platform | Layer registry schema + UI contract validation (exact contents *not confirmed in repo*) |
| API contracts | `src/server/contracts/` | API Team | UI consumes these shapes (legacy locations *not confirmed in repo*) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative Curators | Draft/published story nodes used in Focus Mode |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (path matches `web/src/ui/components/README.md`)
- [ ] Directory layout reflects actual component organization (or explicitly marked “recommended / not confirmed”)
- [ ] Constraints/invariants match the Master Guide + v13 contract-first rules
- [ ] Validation steps are repeatable (and don’t bypass governance gates)
- [ ] Accessibility expectations are stated for all user-facing component work
- [ ] Story Node + Focus Mode rules are explicit (provenance-linked content; AI labeling where applicable)

## 🗂️ Directory Layout

### This document

- `path`: `web/src/ui/components/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React + map clients, layer registry, Focus Mode UI |
| UI components | `web/src/ui/components/` | Reusable UI building blocks (this README governs) |
| API boundary | `src/server/` | API services; UI fetches data from here |
| API contracts | `src/server/contracts/` | Contract definitions (OpenAPI/GraphQL/etc.) |
| UI schemas | `schemas/ui/` | Schemas for layer registry + UI config |
| Story Nodes | `docs/reports/story_nodes/` | Narrative content rendered in Focus Mode |
| Governance | `docs/governance/` | Redaction, ethics, sovereignty rules |

### Expected file tree for this sub-area

> **Note:** This is a recommended organization. Some directories may not exist yet (*not confirmed in repo*).

~~~text
📁 web/
└── 📁 src/
    └── 📁 ui/
        └── 📁 components/
            ├── 📄 README.md
            ├── 📁 base/            # buttons, icons, typography, layout primitives (recommended)
            ├── 📁 map/             # map wrappers + controls (recommended)
            ├── 📁 layers/          # layer list, legend, style helpers (recommended)
            ├── 📁 story/           # Story Node renderer + citation widgets (recommended)
            ├── 📁 focus/           # Focus Mode panels + layouts (recommended)
            ├── 📁 timeline/        # timeline widgets used by Focus Mode (recommended)
            └── 📁 provenance/      # evidence chips, provenance panels, audit UI (recommended)
~~~

## 🧭 Context

### Background

KFM’s canonical flow is:

ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.

UI components live late in the pipeline: they **must not mutate upstream artifacts** and must not bypass the API boundary.

### Assumptions

- The UI is a React single-page app under `web/` (framework specifics beyond React are *not confirmed in repo*).
- Map rendering uses MapLibre and/or Cesium (exact choice per view is *not confirmed in repo*).
- Layer availability is declared via a “layer registry” config validated against `schemas/ui/**` (registry file locations are *not confirmed in repo*).

### Constraints / invariants (non-negotiable)

- **No direct graph access:** UI code does not connect to Neo4j or call graph services directly. All graph access is mediated by contracted APIs.
- **Provenance-only Focus Mode:** Focus Mode must only display provenance-linked content; any AI-generated content must be clearly labeled and/or opt-in.
- **Schema-validated configuration:** Any layer registry or UI config is validated against `schemas/ui/**` before use.
- **Redaction-respecting UI:** If the API redacts/generalizes sensitive locations, the UI must not reconstruct or “reveal by interaction” via overlays, zoom, or UI hints.
- **No secrets in the client:** Do not embed tokens, keys, or privileged endpoints in UI code or docs.

### Open questions (track as issues)

- Are we using TypeScript for components, or JS only? *(not confirmed in repo)*
- What is the canonical layer registry file path (e.g., `web/**/layers/*.json`)? *(not confirmed in repo)*
- What is the standard Story Node “citation token” format expected by the UI renderer? (Template exists; UI parser behavior *not confirmed in repo*)
- What is the canonical UI test runner (Jest/RTL/Cypress/Playwright)? *(not confirmed in repo)*

### Future extensions (safe, contract-first)

- Add a small “component catalogue” (storybook-style) that renders locally without calling real APIs *(not confirmed in repo)*.
- Add automated checks that story markdown renders with a11y-safe semantics and safe link handling.
- Add contract snapshot tests to ensure UI components handle API evolution gracefully.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Upstream["Upstream pipeline (context)"]
    ETL[ETL / pipelines] --> CATS[STAC/DCAT/PROV]
    CATS --> GRAPH[Graph (Neo4j)]
    GRAPH --> API[API boundary]
  end

  API --> UI[Web UI]
  UI --> STORY[Story Nodes rendered]
  STORY --> FOCUS[Focus Mode]
  FOCUS --> UI

  subgraph UIComponents["This folder: UI components"]
    BASE[base/*] --> VIEWS[focus/* + map/*]
    STORYUI[story/*] --> VIEWS
    PROVUI[provenance/*] --> VIEWS
  end

  UI --> UIComponents
~~~

## 📦 Data & Metadata

### Inputs (what components should expect)

- **API responses**: entities/events/collections, map layer payloads, story node payloads, provenance pointers (IDs/URIs).
- **Layer registry config**: a schema-validated declaration of available layers and their UI metadata (titles, categories, styles).
- **Story Node markdown**: governed narrative content (draft/published) that includes citations and entity linkage.

### Outputs (what components produce)

- Rendered UI: map layers, narratives, legends, timelines, evidence/provenance panels.
- User interaction events (optional): selections, filters, timeline scrubs (telemetry schema *not confirmed in repo*).

### Sensitivity & redaction

- Assume some datasets contain sensitive locations or culturally sensitive information.
- Components that can reveal location or identity via interaction (hover, zoom, search, export) must be treated as higher-risk and reviewed.

### Quality signals (UI-level)

- Evidence/provenance UI is present wherever a user can interpret a claim as factual.
- Story Node citations are clickable/inspectable and link back to evidence identifiers (not “orphan text”).

## 🌐 STAC, DCAT & PROV Alignment

UI components do not author STAC/DCAT/PROV artifacts. They:

- **Consume** catalog/provenance information via the API (or via published artifacts served by the API layer).
- **Display** dataset IDs, collection IDs, and provenance references when presenting data-driven claims.
- **Avoid** embedding hard-coded facts that are not traceable to upstream evidence.

Practical UI conventions:

- Prefer displaying an **evidence ID** (dataset/document/prov activity ID) alongside derived values.
- When a view aggregates multiple datasets, show a compact “sources” list and link out to details.

## 🧱 Architecture

### Component groups (recommended)

| Component group | Responsibility | Interface |
|---|---|---|
| `base/` | UI primitives (buttons, chips, layout, typography) | props-only; no data fetching |
| `map/` | Map container, controls, view state adapters | consumes layer registry + API data hooks |
| `layers/` | Layer list, legend, symbology UI | consumes registry metadata + style helpers |
| `story/` | Render Story Node markdown; citations; entity links | consumes story node payload + evidence links |
| `provenance/` | Evidence chips, provenance panel, audit widgets | consumes provenance pointers from API |
| `focus/` | Focus Mode layouts/panels; narrative + map + timeline composition | consumes story nodes + selection state |

### Interfaces / contracts (do not bypass)

| Contract | Location | Versioning rule |
|---|---|---|
| API contracts | `src/server/contracts/**` | semver + contract tests |
| UI layer registry schema | `schemas/ui/**` | semver + schema validation |
| Story Node schema/template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | semver + narrative validation |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | semver + changelog |

### Extension points checklist (adding new UI capability)

When adding a new component that surfaces data (map layer, table, chart, narrative element):

- [ ] Confirm the **API endpoint + contract** exists for the data shape
- [ ] Confirm the layer is declared in the **layer registry** and validates against `schemas/ui/**`
- [ ] Ensure the UI exposes **provenance/evidence links** (dataset IDs, PROV bundle IDs, document IDs)
- [ ] If any sensitive location/people risk exists: flag for **governance review**
- [ ] Add tests for rendering + a11y (at least keyboard navigation and semantics)

## 🧠 Story Node & Focus Mode Integration

### Story Node rendering expectations

- Story Nodes are governed Markdown with front-matter + citation rules (see template).
- The UI renderer should:
  - Preserve headings and semantics for accessibility.
  - Render citations as interactive affordances (evidence panel / link-out).
  - Avoid “free text” facts that cannot be traced back to evidence.

### Focus Mode composition

Focus Mode is an interactive view that pairs:

- Narrative (Story Node)
- Map state (layer + selection)
- Timeline state (time range + scrub)
- Provenance/audit panel

**Rule:** all Focus Mode content must remain provenance-linked. If AI assistance is used for summaries or suggestions, it must be explicitly labeled.

### Example: evidence-first UI primitive (illustrative)

~~~tsx
// Example only (exact framework conventions not confirmed in repo)
export function EvidenceChip({ label, evidenceId, onOpen }: {
  label: string;
  evidenceId: string;
  onOpen: (id: string) => void;
}) {
  return (
    <button type="button" onClick={() => onOpen(evidenceId)}>
      {label} · {evidenceId}
    </button>
  );
}
~~~

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- Markdown protocol check (front-matter + required sections) for this README
- UI lint + formatting (tooling *not confirmed in repo*)
- Unit tests for critical renderers (story markdown, citations, Focus Mode panels)
- Schema validation for any UI registry/config changes (`schemas/ui/**`)
- Static checks to prevent forbidden direct graph access (scan for `neo4j://`, Bolt drivers, etc.)

### CI expectations (if configured)

- Fail builds if UI registry/config is invalid against `schemas/ui/**`
- Fail builds if UI bundle includes forbidden direct graph access patterns
- Enforce accessibility gates for key UI flows (Focus Mode, map controls) *(not confirmed in repo)*

### Local checks (placeholder)

~~~bash
# Placeholder only — exact package manager/scripts not confirmed in repo
# (Examples: npm run lint / test / typecheck / build)
~~~

## ⚖ FAIR+CARE & Governance

- UI components are where users *experience* the system; they must uphold:
  - **FAIR**: evidence is findable + referenceable (IDs surfaced in UI)
  - **CARE**: culturally sensitive content is handled with review gates and redaction
- Any component that could allow a user to infer restricted locations (zoom/hover/export) must be reviewed.
- Do not add new AI-driven text generation to Focus Mode without:
  - clear labeling,
  - provenance links, and
  - explicit opt-in behavior.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial governed README for `web/src/ui/components/` conventions + constraints | (you) |

---

Footer refs (do not remove):

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (draft): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

