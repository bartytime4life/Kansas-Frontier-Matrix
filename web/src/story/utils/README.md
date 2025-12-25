---
title: "KFM Web — Story Utils"
path: "web/src/story/utils/README.md"
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
fair_category: "FAIR-F1A1I1R1"
care_label: "CARE-C1"
sensitivity: "Low"
classification: "Public"
jurisdiction: "Kansas / US"

doc_uuid: "urn:kfm:doc:web:story:utils:readme:v1.0.0"
semantic_document_id: "kfm-web-story-utils-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:story:utils:readme:v1.0.0"
commit_sha: "<latest-commit-hash>"

ai_transform_permissions:
  - "summarize"
  - "structure_extract"
  - "translate"
  - "keyword_index"

ai_transform_prohibited:
  - "speculative_additions"
  - "infer_sensitive_locations"
  - "generate_policy"
  - "remove_required_headers"

doc_integrity_checksum: "<sha256>"
---

# 🧰 KFM Web — Story Utils

> **Purpose (required):** Define the scope, constraints, and expected conventions for utilities under `web/src/story/utils/` that support Story Node rendering and Focus Mode behavior in the web UI—especially **provenance-linked citations**, **deterministic focus controls**, and **redaction-safe presentation**.

---

## 📘 Overview

### Purpose

These utilities exist to keep Story / Focus Mode behaviors **consistent, testable, and governed** across the UI:
- parsing and normalizing Story Node content and metadata (as delivered to the UI),
- handling KFM citation syntax (e.g., `【source†Lx-Ly】`) in a way that supports auditability,
- computing Focus Mode “hints” (layers, time window, map center) into UI state changes,
- enforcing UI-side *presentation rules* that prevent leaking sensitive/restricted information.

### Scope

| In Scope | Out of Scope |
|---|---|
| Pure (or near-pure) helpers: parsing, normalization, mapping Story metadata → UI state | Direct Neo4j access (UI never reads the graph directly) |
| Citation parsing + rendering helpers (to support audit affordances) | Authoring Story Nodes (that belongs under `docs/reports/story_nodes/**`) |
| Redaction-aware rendering helpers (honor API / content flags) | API/business logic; schema ownership; ontology design |
| Deterministic transforms that are easy to unit test | Heavy React components (belongs in `web/src/story/**` components) |

### Audience

- Primary: Web UI engineers working on Story panels and Focus Mode.
- Secondary: Narrative curators and reviewers who need predictable citation/audit behavior.

### Definitions

- **Story Node**: Curated narrative capsule used for exploration; must be evidence-led and source-linked.
- **Focus Mode**: Immersive UI view for a single story/entity; v3 requires provenance-linked content and clear AI labeling.
- **Provenance-linked narrative rule**: Every displayed claim must trace to a dataset/record/asset ID.

> Glossary link: `docs/glossary.md` (**not confirmed in repo**).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Notes |
|---|---|---|
| Master Guide (canonical pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | Source of system ordering and boundary rules |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Defines structure + Focus controls + validation expectations |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governs doc metadata + required sections |
| v13 redesign blueprint (design intent) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Contract-first repo layout and CI gates (**draft / may vary**) |
| Story Nodes (content) | `docs/reports/story_nodes/**` | Canonical home for story content (draft/published split recommended) |

---

## 🗂️ Directory Layout

### This directory

- You are here: `web/src/story/utils/README.md`
- Folder: `web/src/story/utils/`

### Expected structure (recommended)

> This is a **recommended** folder breakdown; adjust to actual codebase conventions (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 story/
        └── 📁 utils/
            ├── 📄 README.md
            ├── 📁 citations/
            ├── 📁 focus/
            ├── 📁 markdown/
            ├── 📁 provenance/
            ├── 📁 redaction/
            └── 📁 __tests__/
~~~

### Related repository paths

| Area | Path | Notes |
|---|---|---|
| UI root | `web/` | Frontend SPA home (React/MapLibre/Cesium suggested in implementation docs) |
| Story subsystem | `web/src/story/` | Story panels + Focus Mode UI (name/location may vary) |
| Schemas | `schemas/**` | v13 design calls for schema-first validation (**may be incomplete**) |
| Story Nodes | `docs/reports/story_nodes/**` | Draft/published content lanes recommended |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Canonical catalog/provenance homes |

---

## 🧭 Context

### Canonical ordering and boundary rules

KFM preserves the canonical ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**:contentReference[oaicite:3]{index=3}

UI-side Story utilities must respect two non-negotiables:
1. **API boundary**: UI never reads Neo4j directly; the UI consumes contracted APIs.:contentReference[oaicite:4]{index=4}
2. **Focus Mode integrity**: Focus Mode v3 content must be provenance-linked; AI elements must be clearly indicated.:contentReference[oaicite:5]{index=5}

### Why `web/src/story/utils/` exists

Story + Focus Mode are the primary place where users interpret narrative claims. That makes this code “high trust surface area”:
- the UI must not render unsourced claims as if they are factual,
- the UI must provide citation/audit affordances (tooltips/panels) so users can inspect provenance,
- the UI must not leak restricted/sensitive location detail through rendering, tooltips, or debug UI.

### Assumptions

- Story content is delivered to the UI as either:
  - Markdown Story Nodes (with KFM citation syntax), and/or
  - structured JSON returned from a Focus/Story API.
  (**Exact interface not confirmed in repo**.)

- Utilities in this folder should be:
  - deterministic (same input → same output),
  - side-effect free where feasible,
  - unit-testable without network access.

### Explicit constraints

- No direct graph access (no Neo4j drivers, no Cypher in the UI).
- Treat citation rendering as a security surface: prevent XSS, and do not “invent” sources.
- If evidence is missing/unresolvable, degrade safely:
  - show a warning badge,
  - hide or gray-out the claim if policy requires,
  - never fabricate a citation.

---

## 🗺️ Diagrams

### Story / Focus Mode flow (conceptual)

~~~mermaid
flowchart LR
  U[User selects story/entity] --> UI[Web UI]
  UI -->|API request| API[Focus/Story API]
  API -->|context bundle: narrative + evidence IDs + flags| UI
  UI --> Utils[web/src/story/utils]
  Utils --> R[Rendered story panel + audit affordances]
  Utils --> M[Map + timeline focus state]
~~~

### Citation resolution (conceptual)

~~~mermaid
flowchart TD
  MD[Story markdown with 【source†Lx-Ly】] --> P[parseCitations()]
  P --> C[citation tokens]
  C --> E[resolve to evidence bundle IDs]
  E --> UI[render: tooltip / sources panel]
  E -->|missing| W[warn + degrade]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### Standard citation syntax

Story Nodes use a bracket citation format (e.g., `【source†Lx-Ly】`). The UI must render this in an auditable way (links/tooltips/footnotes) without “hallucinated” sources.:contentReference[oaicite:6]{index=6}:contentReference[oaicite:7]{index=7}

### Optional Focus controls

Story Nodes may include optional structured Focus controls:

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

(See Story Node template v3.):contentReference[oaicite:8]{index=8}

Utilities in this folder should provide a single normalization path so components can rely on one stable shape for:
- layer toggles (registry IDs),
- time window normalization,
- map center/zoom application (if zoom is part of the UI state model — **not confirmed in repo**).

### What belongs in `utils/`

Recommended utility responsibilities:
- **Citations**
  - parse KFM citation tokens from Markdown,
  - map citations to evidence IDs / “sources” arrays returned by APIs,
  - render-ready models for tooltip / Sources panel.
- **Focus Mode state**
  - normalize focus hints → map state and timeline state,
  - compute “diff” state updates to avoid jarring UI resets.
- **Provenance and audit**
  - detect unresolved references and produce structured warnings,
  - support an audit panel (icons, warnings, lists of sources).
- **Redaction awareness**
  - honor flags indicating generalized coordinates, restricted layers, or redacted content,
  - ensure the UI does not reveal precision via hover details or debug views.

### AI content handling

If AI-generated narrative is ever displayed:
- it must be clearly labeled,
- it must be opt-in,
- it must include uncertainty/confidence metadata,
- it must never be shown as evidence-backed fact by default.:contentReference[oaicite:9]{index=9}:contentReference[oaicite:10]{index=10}

---

## 🧪 Validation & CI/CD

### Validation checklist (recommended)

- [ ] Markdown protocol: required front-matter + required H2 sections (for governed docs).
- [ ] Type/lint: UI lint + TypeScript checks (tooling **not confirmed in repo**).
- [ ] Unit tests: citation parsing, focus controls normalization, redaction behavior.
- [ ] Security: sanitize/escape any HTML derived from Story Markdown; prevent XSS.
- [ ] Accessibility: citations and audit affordances must be keyboard accessible (no hover-only meaning).:contentReference[oaicite:11]{index=11}

### Reproduction (placeholders)

~~~bash
# Replace with repo-specific commands (not confirmed in repo)
# 1) typecheck + lint
# 2) unit tests
# 3) story/focus integration tests (if present)
~~~

---

## 📦 Data & Metadata

### Inputs

Typical inputs these utilities may consume:
- Story Node Markdown (with `【…】` citations)
- Story Node metadata (focus controls, entity refs, evidence refs)
- Evidence bundles / sources arrays from APIs (dataset IDs, STAC/DCAT/PROV IDs, doc pointers)
- Redaction/sensitivity flags

### Outputs

Typical outputs these utilities may produce:
- Parsed citation tokens + resolved “source” models for tooltips/panels
- Normalized Focus state:
  - layer enable/disable actions
  - time window normalized to UI format
  - map center normalized to UI format
- Structured warnings suitable for an audit panel

### Quality signals

- No orphan citations (every citation resolves to a source/evidence ID)
- No “invented” sources (UI must not fabricate provenance)
- Redaction flags are always honored

---

## 🌐 STAC, DCAT & PROV Alignment

This folder does not author catalogs, but it must correctly *present* catalog/provenance identifiers to users.

Recommended alignment behaviors:
- If a citation targets a dataset:
  - show STAC Item/Collection IDs (when present),
  - show DCAT Dataset/Distribution IDs (when present),
  - show PROV Activity IDs for transformations (when present).
- When identifiers are missing:
  - surface as “unresolved evidence” and route to curator/developer workflows rather than guessing.

---

## 🧱 Architecture

### Placement and dependency rules

- `web/src/story/utils/**` should be dependency-light and test-first.
- Avoid circular dependencies with Story components.
- Avoid “hidden network” behavior (no fetch inside utility functions unless explicitly designed and reviewed).
- Treat citation parsing + markdown rendering as security-sensitive:
  - sanitize output,
  - restrict allowed markdown features if needed (policy belongs in governance docs).

### Interfaces

These utilities should be consumed by:
- Story rendering components (story panels, story feeds),
- Focus Mode orchestrators (map + timeline sync),
- Audit / Sources UI widgets.

Exact component locations are **not confirmed in repo**; this README governs the *responsibilities and constraints*, not a specific component tree.

---

## ⚖ FAIR+CARE & Governance

### Governance triggers

Changes in this folder may require governance review if they:
- alter how citations are displayed (risk: misleading provenance),
- change redaction/generalization behavior (risk: exposing sensitive locations),
- introduce or expand AI-generated narrative presentation (risk: unsourced claims).

Follow:
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`

### CARE / sovereignty considerations

Story + Focus Mode can surface culturally sensitive or sovereignty-controlled knowledge.
UI utilities must:
- preserve redaction/generalization,
- avoid backdoor precision leaks (e.g., tooltips, copy-to-clipboard, debug coordinates),
- clearly label restricted content and required handling.

### AI usage constraints

For Story/Fitness surfaces:
- no speculative additions,
- no inference of sensitive locations,
- no policy generation.

(See template front-matter `ai_transform_prohibited`.)

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-25 | Initial README for Story utilities scope, constraints, and integration expectations | (you) |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

