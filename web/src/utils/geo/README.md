---
title: "KFM Web UI — Geo Utilities (README)"
path: "web/src/utils/geo/README.md"
version: "v0.1.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "README"
license: "CC-BY-4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "MCP-DL v6.3"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/ethics/ETHICS.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-C1"
sensitivity: "Low"
classification: "Public"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:src:utils:geo:readme:v0.1.0"
semantic_document_id: "kfm-web-src-utils-geo-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:src:utils:geo:readme:v0.1.0"
commit_sha: "<fill>"

ai_transform_permissions: [ "summarize", "structure_extract", "translate", "keyword_index" ]
ai_transform_prohibited: [ "generate_policy", "infer_sensitive_locations" ]

doc_integrity_checksum: "sha256:<fill>"
---

# KFM Web UI — `utils/geo`

> **Purpose (required):** Provide deterministic, API-contract-safe geospatial helper utilities used by the KFM web UI (e.g., MapLibre/Cesium rendering + Focus Mode camera/extent logic) without introducing new “facts,” bypassing the API boundary, or leaking sensitive locations via unintended precision.

## 📘 Overview

### Purpose

This directory exists to:

- Centralize **coordinate, bounding box, and geometry normalization** logic used by the frontend.
- Reduce drift between map clients (2D/3D) by sharing **one** set of “geo primitives”.
- Keep geo computations **UI-scoped** (rendering + interaction), pushing “truth-making” GIS operations upstream into ETL/catalog/graph/API where provenance and governance are enforced.

### Scope

| In Scope | Out of Scope |
|---|---|
| UI-facing coordinate utilities (e.g., validation, normalization, wrapping) | Backend/ETL-grade GIS processing (buffering, conflation, topology repair, authoritative geocoding) |
| Bounding box helpers for map camera actions (fit bounds, padding, union) | Any direct graph access or Cypher logic (UI must not read Neo4j) |
| GeoJSON/STAC geometry *consumption* helpers (read/normalize) | Modifying STAC/DCAT/PROV artifacts (catalogs are produced upstream) |
| Display-oriented simplification / clipping *when explicitly marked as visualization-only* | “Upgrading” generalized geometry into higher precision (redaction bypass) |
| Light parsing/formatting for tooltips/legends | Calls to external geo services (geocoders, routing APIs) unless explicitly contracted + reviewed |

### Audience

- **Primary:** Frontend engineers working under `web/` building map layers, Focus Mode behaviors, and map/timeline synchronization.
- **Secondary:** API and data engineers reviewing UI-boundary invariants and redaction expectations.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering + non‑negotiables |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Governs this README structure |
| UI layer registry schema | `schemas/ui/` | Frontend + Platform | CI-validated UI configuration (not confirmed in repo) |
| UI layer registries | `web/**/layers/**` | Frontend | Layer configs (paths not confirmed in repo) |
| API boundary | `src/server/` | API Eng | UI must only talk to APIs (never Neo4j directly) |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] `path:` matches file location
- [ ] Folder responsibilities, boundaries, and “out-of-scope” items are explicit
- [ ] Geo invariants (CRS/units/ordering) are clearly stated
- [ ] Validation steps listed and repeatable (or marked **not confirmed in repo**)
- [ ] Governance + CARE/sovereignty considerations explicitly stated for location precision and redaction

## 🗂️ Directory Layout

### This document

- `path`: `web/src/utils/geo/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients; layer registry; Focus Mode UI |
| API boundary | `src/server/` | Contracted endpoints; redaction; monitoring |
| Graph | `src/graph/` | Ontology + ingest; graph build scripts |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts + lineage |
| Schemas | `schemas/` | JSON schemas for catalogs/APIs/UI config (not confirmed in repo) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts powering Focus Mode (location not confirmed in repo) |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some files may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 src/
    └── 📁 utils/
        └── 📁 geo/
            ├── 📄 README.md
            ├── 📄 index.(ts|js)            # barrel exports (not confirmed in repo)
            ├── 📄 lnglat.(ts|js)           # coordinate validation/normalization (not confirmed in repo)
            ├── 📄 bbox.(ts|js)             # bbox ops (union/pad/fit) (not confirmed in repo)
            ├── 📄 geojson.(ts|js)          # GeoJSON normalization helpers (not confirmed in repo)
            ├── 📄 stac.(ts|js)             # helpers for STAC geometry/bbox consumption (not confirmed in repo)
            ├── 📄 mercator.(ts|js)         # optional projection helpers (not confirmed in repo)
            └── 📄 __tests__/               # unit tests (not confirmed in repo)
~~~

## 🧭 Context

### Background

KFM’s UI layer is downstream of the canonical pipeline:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This means geo helpers in `web/src/utils/geo/` should assume:

- They are **consuming** geometry and metadata produced upstream (via API), not authoring new evidence.
- They must preserve the **API boundary**: no UI code (including utilities) should import Neo4j drivers, embed Cypher, or access the graph directly.
- They must not undermine governance/redaction by reintroducing or inferring sensitive locations.

### Geo invariants (UI-side)

These invariants keep map interactions consistent and auditable:

1) **Coordinate ordering:** always treat positions as `[longitude, latitude]` when representing geographic coordinates.
2) **CRS clarity:** every function that accepts or returns coordinates must either:
   - assume a single declared CRS (documented in the function/JSDoc), or
   - include the CRS in its type/name (e.g., `lngLatToWebMercatorMeters`).
3) **Units clarity:** explicitly differentiate:
   - degrees vs radians
   - meters vs “pixels” (screen space)
4) **Visualization-only transforms:** any simplify/clip/generalize operation must be explicitly marked as **display-only** so it is not mistaken for authoritative geometry.

### Non-negotiable boundary

- **No UI direct-to-graph reads.** Geo utilities must not bypass the API layer, even “just for geometry.” If geometry is missing, the fix belongs in API contracts or upstream artifacts—not in UI “workarounds.”

## 🗺️ Diagrams

### UI geo utility placement

~~~mermaid
flowchart LR
  A["API boundary (src/server)"] --> B["UI (web/)"]
  B --> C["web/src/utils/geo"]
  C --> D["Map engine (MapLibre / Cesium)"]
  B --> E["Focus Mode (narrative + audit)"]
~~~

### Focus Mode map targeting (conceptual)

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant GEO as Geo Utils (web/src/utils/geo)

  UI->>API: Focus query(entity_id)
  API-->>UI: context bundle (entities + evidence refs + geometry)
  UI->>GEO: derive view target (center/bbox) from bundle
  GEO-->>UI: camera target (bounds/center/zoom)
~~~

## 🧱 Architecture

### Responsibilities

| Responsibility | Why it belongs here | What it must NOT do |
|---|---|---|
| Normalize and validate incoming map geometry | Prevent inconsistent map behavior and UI bugs | “Repair” data quality issues that should be fixed upstream |
| Compute bounding boxes and unions | Drive `fitBounds` and focus highlights | Invent geometry when missing |
| Handle edge cases (dateline wrap, bbox padding) | Avoid broken zoom-to-feature behavior | Increase precision beyond what API provides |
| Provide small, testable primitives | Keep bundle small and deterministic | Pull data from network or graph |

### Design guidance (recommended)

- Prefer **pure functions** with explicit inputs/outputs.
- Avoid hidden global state or reliance on the DOM.
- Keep dependencies minimal to reduce web bundle weight.
- Favor typed helpers (TypeScript) or well-documented runtime checks (JavaScript).

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Geo utilities may be used to:

- compute a “focus extent” for the map from:
  - Story Node metadata (e.g., `focus_center`, `focus_layers`) *(exact structure depends on Story Node template / API contracts; not confirmed in repo)*,
  - API-provided feature geometry or STAC item `bbox`,
  - a set of relevant entities returned by Focus APIs.

### Provenance-linked narrative rule (UI implication)

- Geo utilities must never “upgrade” a narrative claim by inferring location precision or constructing new spatial assertions.
- When the UI highlights a geometry, it should be a **rendering of an evidence-backed artifact** (STAC/DCAT/PROV/graph evidence reference) returned by the API.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Lint/typecheck passes for `web/`
- [ ] Unit tests cover bbox math and edge cases (dateline wrap, invalid coords)
- [ ] CI “forbidden import” checks prevent Neo4j drivers/Cypher usage in `web/`
- [ ] Any layer registry changes validate against `schemas/ui/` (if present)

### Reproduction (placeholders)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run UI lint/typecheck
# npm run lint
# npm run typecheck

# 2) run tests
# npm test

# 3) (recommended) verify no forbidden graph usage in web bundle
# grep -R "neo4j://" web/ || true
# grep -R "cypher" web/ || true
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Feature geometry | GeoJSON-like | API responses | coordinate range checks + geometry shape checks (lightweight) |
| Evidence geometry metadata | STAC item `bbox` / `geometry` | API responses / STAC artifacts | treat as read-only; schema validated upstream |
| Focus targets | entity IDs + optional focus metadata | Focus API | presence checks; never infer missing geometry |

### Outputs

| Output | Format | Used by | Notes |
|---|---|---|---|
| Map camera targets | center/zoom or bounds | Map components | visualization only |
| Normalized coordinates | `[lng, lat]` arrays | Layer renderers | must preserve upstream precision policy |
| Derived display bbox | `[minX, minY, maxX, maxY]` | fit/zoom logic | deterministic |

### Sensitivity & redaction (UI considerations)

- If geometry is generalized/redacted upstream, UI code must not attempt to “reverse” it.
- Avoid adding features that expose more precision than intended (e.g., printing full coordinates in UI tooltips for sensitive layers) unless contracts explicitly allow it.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- UI geo utilities may **consume** `bbox` / `geometry` fields to:
  - zoom to an item,
  - draw outlines,
  - compute extents for a focus view.
- UI must not mutate or “correct” STAC artifacts; changes belong in upstream pipelines and schema validation.

### DCAT

- UI may surface dataset metadata (publisher/license) in layer tooltips/legends (if provided by API).
- Geo utilities should remain metadata-agnostic; keep display text concerns in UI components.

### PROV-O

- Provenance identifiers may appear in Focus Mode audit panels.
- Geo utilities should treat provenance references as opaque IDs: they can be passed through, but not interpreted as “permission” to infer locations.

## ⚖ FAIR+CARE & Governance

### Review gates

Changes require governance review when they:

- alter how sensitive layers are displayed (precision, zoom behavior, tooltip contents),
- introduce external geo service calls,
- change Focus Mode location targeting in a way that could reveal restricted geometry.

### CARE / sovereignty considerations

- Treat culturally sensitive locations as high-risk by default.
- Ensure UI behavior does not re-expose restricted sites through “helpful” coordinate displays, deep-link sharing, or high-precision measurement tools unless explicitly approved.

### AI usage constraints

- This document allows: summarize, structure extraction, translate, keyword indexing.
- Prohibited: generating policy, inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-26 | Initial `web/src/utils/geo/` README scaffold aligned to KFM pipeline + UI invariants | TBD |

---

Footer refs (do not remove):

- Governance: `docs/standards/governance/ROOT-GOVERNANCE.md`
- Ethics: `docs/standards/ethics/ETHICS.md`
- Sovereignty: `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`

