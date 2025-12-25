---
title: "KFM Web — Story Renderer (Focus Mode)"
path: "web/src/story/renderer/README.md"
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

doc_uuid: "urn:kfm:doc:web:story:renderer:readme:v1.0.0"
semantic_document_id: "kfm-web-story-renderer-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:renderer:readme:v1.0.0"
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

# KFM Web — Story Renderer (Focus Mode)

> **Purpose (required):** Define the **UI rendering contract** for **Story Nodes (v3)** inside **Focus Mode**, including how we render **citations**, **evidence/provenance**, and **map/timeline focus controls** while honoring the API boundary and redaction rules.

## 📘 Overview

### Purpose

This sub-area is responsible for turning a **Story Node v3** narrative into an interactive Focus Mode experience:

- Render Story Node Markdown into accessible UI (headings, lists, images, etc.).
- Detect and render **citations** (e.g., `【source-id†Lx-Ly】`) as interactive references (popover, footnote, or side panel).
- Apply optional **focus controls** (e.g., `focus_center`, `focus_time`, `focus_layers`) to synchronize map + timeline.
- Surface **audit signals** (missing citations, unresolved evidence IDs, sensitivity/redaction notices).
- Enforce UI-side safety requirements (sanitization, link safety, a11y).

### Scope

| In Scope | Out of Scope |
|---|---|
| Rendering Story Node v3 Markdown in Focus Mode | Authoring Story Nodes (curation workflows) |
| Citation token parsing and UX for evidence lookup | Generating new “facts” or narrative text |
| Applying focus hints to map/time/layer state | Direct graph access (Neo4j) from the browser |
| UI-safe sanitization and a11y conventions | Defining API endpoints/contracts (owned by API boundary) |

### Audience

- **Primary:** Frontend contributors implementing Focus Mode UX (React + map engine).
- **Secondary:** Narrative curators validating how Story Nodes render; reviewers verifying provenance/redaction integrity.

### Definitions

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used here: **Story Node**, **Focus Mode**, **citation**, **evidence**, **provenance**, **redaction/generalization**, **context bundle**.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + “do not break” rules |
| Story Node template v3 | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Defines Story Node structure, citations, focus controls |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Structure used by this README |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (**not confirmed in repo**) | Arch | Clarifies canonical homes + contract set |
| Story Nodes (content) | `docs/reports/story_nodes/` | Narrative | Draft/published story Markdown |
| API boundary (contracts) | `src/server/contracts/` | API | Contract-first payloads consumed by UI |
| Story Node schema | `schemas/storynodes/` (**not confirmed in repo**) | Contracts | Machine validation of Story Node payloads |
| UI layer registry schema | `schemas/ui/` (**not confirmed in repo**) | UI/Contracts | Validates layer definitions referenced by `focus_layers` |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches this file location).
- [ ] The **API boundary rule** is explicit: this renderer never talks to Neo4j directly.
- [ ] Citation behavior is documented (token format, UX, evidence resolution).
- [ ] Focus controls behavior is documented (map + timeline + layers).
- [ ] Safety expectations are documented (sanitization, external link rules, XSS).
- [ ] A11y expectations are documented (keyboard, screen readers, headings).
- [ ] Governance triggers are listed for any new rendering capability that can expose sensitive locations.

## 🗂️ Directory Layout

### This document

- `path`: `web/src/story/renderer/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| UI root | `web/` | React + map client (MapLibre/Cesium) |
| Layer registry | `web/**/layers/**` | Layer definitions referenced by story focus controls |
| Story Nodes | `docs/reports/story_nodes/` | Governed narratives rendered by Focus Mode |
| API boundary | `src/server/` | Graph + catalog access with redaction enforcement |
| API contracts | `src/server/contracts/` | Versioned response payload definitions for UI |
| Schemas | `schemas/` | STAC/DCAT/PROV + story + UI + telemetry schema families |
| Evidence catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Provenance-first evidence artifacts |

### Expected file tree for this sub-area

> Note: This tree is a **target layout** to document responsibilities and should be synchronized with the actual files present (**not confirmed in repo** beyond this README path).

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        └── 📁 renderer/
            ├── 📄 README.md
            ├── 📄 index.ts                      # public exports (not confirmed in repo)
            ├── 📄 StoryRenderer.tsx             # top-level renderer (not confirmed in repo)
            ├── 📁 components/                   # UI atoms/molecules (not confirmed in repo)
            │   ├── 📄 Citation.tsx
            │   ├── 📄 EvidencePanel.tsx
            │   ├── 📄 FocusControls.tsx
            │   ├── 📄 RedactionNotice.tsx
            │   └── 📄 EntityLink.tsx
            ├── 📁 parsing/                      # parsing + normalization (not confirmed in repo)
            │   ├── 📄 storyNodeFrontMatter.ts
            │   ├── 📄 citationTokens.ts
            │   ├── 📄 sanitize.ts
            │   └── 📄 linkResolver.ts
            ├── 📁 types/                        # UI-level types mirrored from contracts (not confirmed in repo)
            │   └── 📄 storyNode.ts
            └── 📁 __tests__/                    # renderer tests (not confirmed in repo)
                ├── 📄 storyNodeV3.render.spec.ts
                └── 📄 sanitize.spec.ts
~~~

## 🧭 Context

### Where this renderer sits in the canonical pipeline

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API Boundary → UI → Story Nodes → Focus Mode**

The Story Renderer is the **UI-side execution point** that turns a Story Node + context bundle into an interactive Focus Mode view (narrative + map + timeline).

### Non‑negotiables this renderer must preserve

- **Provenance-first:** Focus Mode must display **provenance-linked context only** (no orphan facts).
- **AI content is never unmarked fact:** If predictive / AI-generated content is present, it must be opt-in and clearly labeled with uncertainty metadata.
- **API boundary is canonical:** the browser must never query Neo4j directly; all graph reads go through `src/server/` and its contracts.
- **Redaction/generalization is enforced at the boundary, but honored in UI:** even if API redacts, the UI must not “reconstruct” restricted details via caching, deep links, or UI affordances.

### Trust boundary: Story Nodes are content, not code

Treat Story Node Markdown as **untrusted input**:

- sanitize before rendering (no arbitrary HTML execution),
- restrict dangerous link schemes,
- avoid rendering raw if validation fails (fail-closed where possible).

## 🗺️ Diagrams

### Focus Mode context flow (story rendering + map/timeline sync)

~~~mermaid
sequenceDiagram
  participant User
  participant UI as UI (web/)
  participant API as API Boundary (src/server)
  participant R as Story Renderer (web/src/story/renderer)

  User->>UI: Click entity / open story
  UI->>UI: Enter Focus Mode (entity_id / story_id)
  UI->>API: Fetch Focus Mode context bundle (contracted)
  API-->>UI: Story Node + evidence refs + audit flags
  UI->>R: Render(storyNode, evidenceMap)
  R-->>UI: Rendered narrative + citation UI + focus hints
  UI->>UI: Apply focus_center / focus_time / focus_layers to map + timeline
~~~

### Contracts and provenance boundaries (renderer perspective)

~~~mermaid
flowchart TB
  subgraph Content["Governed content"]
    SN["Story Node v3 (Markdown + front-matter)"]
  end

  subgraph Evidence["Evidence + provenance (IDs)"]
    STAC["STAC Items/Collections"]
    DCAT["DCAT Dataset Records"]
    PROV["PROV Activities/Bundles"]
  end

  subgraph APILayer["API boundary (contract-first)"]
    API["src/server + contracts"]
  end

  subgraph UI["UI (Focus Mode)"]
    R["Story Renderer"]
    M["Map + timeline state"]
    A["Audit panel"]
  end

  SN --> API
  STAC --> API
  DCAT --> API
  PROV --> API

  API --> R
  R --> M
  R --> A
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Source | Validation expectation |
|---|---|---|---|
| Story Node content | Markdown + YAML front-matter | `docs/reports/story_nodes/**` (or via API) | Story Node schema + “no orphan citations” checks |
| Focus controls | front-matter fields (e.g., `focus_center`, `focus_time`, `focus_layers`) | Story Node v3 | Validate types; ignore unknown fields (fail-safe) |
| Evidence map | JSON payload linking citation IDs → evidence metadata | API boundary | Contract tests + runtime validation |
| Layer registry | JSON/YAML/TS config (**not confirmed in repo**) | `web/**/layers/**` | Validate against `schemas/ui/` (if present) |
| User settings | UI state (e.g., “show AI explanations”) | UI store | Must default to safest option |

### Outputs

| Output | Consumer | Notes |
|---|---|---|
| Rendered narrative UI | Focus Mode | Must be sanitized and a11y-compliant |
| Citation interactions | Evidence panel / popovers | Click opens evidence details (IDs + provenance) |
| Map/timeline focus actions | Map + timeline subsystem | Apply focus hints; never reveal restricted precision |
| Audit warnings | Focus Mode audit panel | Missing evidence IDs, invalid citations, sensitivity notices |

## 🌐 STAC, DCAT & PROV Alignment

### What “provenance-linked” means at render time

The renderer should assume that citations and evidence references ultimately resolve to:

- **STAC** item/collection IDs (assets, footprints, raster/vector evidence),
- **DCAT** dataset IDs (discovery + dataset metadata),
- **PROV** activity/bundle IDs (lineage: how an artifact was produced).

The renderer must never “invent” provenance. If an evidence ID cannot be resolved, display a **warning** and render the claim as **uncorroborated** (or hide it, depending on Focus Mode policy).

### Citation tokens

Story Nodes are expected to cite sources in-text using a bracket token format (example):

- `【source-id†L12-L34】`

Renderer responsibilities:

1. Detect these tokens during Markdown rendering.
2. Convert them into interactive UI (link/footnote/popover).
3. Resolve `source-id` → evidence metadata via the API-provided evidence map (preferred) or a follow-up contracted lookup (not confirmed in repo).

## 🧱 Architecture

### Contract-first input shape (illustrative)

> This is illustrative only. Canonical payload definitions must come from `src/server/contracts/**` (or `schemas/storynodes/**` if used) and must be versioned and tested.

~~~ts
export type EvidenceKind = "stac" | "dcat" | "prov" | "document" | "other";

export interface EvidenceRef {
  id: string;              // e.g., "stac:item:land-treaty-1867-ml"
  kind: EvidenceKind;       // drives icon + panel layout
  locator?: string;         // e.g., "L12-L34" for line references
  title?: string;
  license?: string;
  sensitivity?: "public" | "restricted";
}

export interface StoryNodeFocusControls {
  focus_layers?: string[];
  focus_time?: string;            // ISO string or domain-specific time key (not confirmed)
  focus_center?: [number, number]; // [lon, lat]
}

export interface StoryNodePayload {
  id: string;
  version: string;                 // Story Node schema version
  frontMatter: Record<string, unknown>;
  markdown: string;                // narrative body
  focus?: StoryNodeFocusControls;
  evidence?: Record<string, EvidenceRef>; // evidence lookup by citation id
  auditFlags?: string[];           // warnings to show in audit panel
}
~~~

### Rendering pipeline (recommended)

1. **Validate** payload version and required fields (fail-safe / fail-closed depending on policy).
2. Parse Markdown to an AST (Markdown library choice **not confirmed in repo**).
3. Extract and normalize:
   - citation tokens (`【…†…】`),
   - entity links (if encoded),
   - media assets (images/maps) and their attribution.
4. **Sanitize** output:
   - strip unsafe HTML,
   - prevent `javascript:` / `data:` link injection,
   - enforce safe attributes (`rel="noopener noreferrer"`, etc.).
5. Render React components:
   - headings + anchor links,
   - citation components,
   - evidence panel hooks,
   - redaction notices (if any).
6. Apply focus controls (map/layer/time) through UI state, not side effects in render.

### Security notes

- Never render untrusted HTML directly.
- Treat all URLs as untrusted; prefer evidence IDs over raw URLs.
- Do not expose hidden precision (e.g., lat/lon) if data is classified or generalized upstream.

### Accessibility notes

Minimum expectations:

- Semantic headings (`h1`→`h2`→…; no skipped levels).
- Citations must be keyboard focusable and announce evidence metadata to screen readers.
- Evidence panel must trap focus when open and return focus on close.
- Avoid “color-only” encoding for warnings/sensitivity.

## 🧠 Story Node & Focus Mode Integration

### Focus controls (v3)

Story Nodes may provide optional focus controls such as:

- `focus_center`: where the map should center on open,
- `focus_time`: which timeline window to emphasize,
- `focus_layers`: which layer IDs to toggle on.

Renderer responsibilities:

- expose these controls as **data** back to Focus Mode state management,
- never assume layers exist — resolve via layer registry and warn if missing,
- ensure any “zoom-to” behavior respects redaction/generalization rules.

### Audit panel expectations

The Story Node template expects the UI to support an audit/provenance experience (warnings, citations, sensitivity notices). This renderer should provide the data and UI hooks that allow Focus Mode to show:

- citation list and resolution status,
- sensitivity notices / redaction applied,
- “AI explanation” toggle state (if present in the product).

## 🧪 Validation & CI/CD

### Validation checklist (renderer)

- [ ] Rendering output is deterministic (same input → same DOM structure).
- [ ] Citation tokens are detected and rendered consistently.
- [ ] Missing/unresolvable evidence IDs produce visible warnings (and telemetry if configured).
- [ ] Sanitization tests cover common XSS vectors.
- [ ] A11y checks for citation interactions pass (keyboard + SR).

### CI expectations (project-wide)

When configured, CI should enforce at least:

- Markdown protocol validation for governed docs.
- Schema validation for STAC/DCAT/PROV and (if present) `schemas/storynodes/` + `schemas/ui/`.
- Story Node validation (front-matter, citations, entity refs, redaction compliance).
- API contract tests for Focus Mode payloads.
- Security + sovereignty scanning gates (where applicable).

Local commands are intentionally not enumerated here (**not confirmed in repo**); use the scripts defined by the project’s root tooling for `web/`.

## ⚖ FAIR+CARE & Governance

### High-risk changes that require review

Changes to the renderer that can affect governance posture should trigger review, including:

- rendering new media types (external embeds, iframes),
- adding features that can reveal restricted locations via interaction/zoom,
- auto-expanding evidence into “summary facts” (risk of unsourced narrative),
- enabling any AI-generated narrative content without explicit labeling + opt-in.

### Sovereignty + redaction

If any story content involves culturally sensitive knowledge or restricted locations:

- follow `docs/governance/SOVEREIGNTY.md`,
- ensure redaction/generalization is enforced at API boundary,
- ensure UI does not provide affordances that undo redaction (e.g., “copy coordinates”).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-25 | Initial README for Story Renderer (Focus Mode) | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`

