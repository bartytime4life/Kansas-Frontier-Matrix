---
title: "Map Layer Registry (UI) — README"
path: "web/src/map/registry/README.md"
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

doc_uuid: "urn:kfm:doc:web:map:registry:readme:v1.0.0"
semantic_document_id: "kfm-web-map-registry-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:map:registry:readme:v1.0.0"

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

# 🗺️ Map Layer Registry (UI)

**Path:** `web/src/map/registry/`  
**Role:** Layer + source registry for the map UI (React / MapLibre, and optionally Cesium)

<img alt="doc_kind" src="https://img.shields.io/badge/doc_kind-Guide-0b5563?style=for-the-badge" />
<img alt="subsystem" src="https://img.shields.io/badge/subsystem-UI%20Map%20Registry-1f6feb?style=for-the-badge" />
<img alt="status" src="https://img.shields.io/badge/status-Draft-6e7781?style=for-the-badge" />
<img alt="protocol" src="https://img.shields.io/badge/KFM--MDP-v11.2.6-7c3aed?style=for-the-badge" />

</div>

---

> **Purpose (required):** Define **how the KFM map UI discovers, validates, and renders layers** using a governed **Layer Registry**, including:
> (1) registry responsibilities and constraints,  
> (2) how layers reference STAC/DCAT/PROV evidence,  
> (3) how sensitivity/access rules prevent “hidden data leakage”, and  
> (4) how Story Nodes / Focus Mode reliably target map layers by stable IDs.

## 📘 Overview

### What is the “Layer Registry”?

The Layer Registry is the **single source of truth** (in the UI) for:

- **What layers exist** (datasets, overlays, basemaps)
- **How they are fetched** (API endpoints, tiles, static assets; never direct Neo4j calls)
- **How they are rendered** (MapLibre/Cesium style and interaction behavior)
- **How they are governed** (sensitivity flags, access rules, attribution/licensing)
- **How they are referenced by narratives** (Story Nodes / Focus Mode `focus_layers`)

### Scope

| In scope | Out of scope |
|---|---|
| Declaring layers + sources + styling metadata | Shipping large data inside the UI bundle |
| Validation of registry entries (schema/type checks) | ETL pipelines and catalog generation |
| Provenance pointers (STAC/DCAT/PROV IDs) | Writing graph ingest logic / Cypher |
| Sensitivity gates + safe zoom/precision limits | Granting permissions / identity management (handled upstream) |

### Audience

- **UI engineers** adding, modifying, or debugging layers
- **API/Graph engineers** ensuring map layers align with contracts + redaction
- **Governance reviewers** approving sensitive layers or precision changes

### Definitions (quick)

- **Layer:** A renderable map overlay (vector/raster/geojson/feature-service)
- **Source:** Where a layer’s data comes from (tiles, API, static file)
- **Registry entry:** Declarative config that binds a layer ID → source + render + governance
- **Hidden data leakage:** Interactions (zoom, query, inspect) that expose sensitive precision even if the default view appears safe

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Registry implementation (this module) | `web/src/map/registry/` | Loader + validators + typed interfaces |
| Layer registry data | **not confirmed in repo** | May be JSON (e.g., `web/**/layers/*.json`) or TS exports |
| UI registry schema | **not confirmed in repo** (`schemas/ui/**`) | Schema validation is expected in CI |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story nodes refer to stable `focus_layers` IDs |
| Master guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |

### Definition of done (for changes in this area)

- [ ] A layer can be discovered via the registry with a **stable ID**
- [ ] Registry entries validate against the **UI registry schema** (if present)
- [ ] Every public-facing layer includes **license + attribution**
- [ ] Every data-bearing layer includes **STAC/DCAT/PROV pointers** (or explicit “not available” rationale)
- [ ] Sensitivity rules prevent **precision escalation** (zoom/query/export)
- [ ] No UI code directly reads Neo4j; all data access is via **contracted APIs**
- [ ] Story Nodes can reference the layer by ID (`focus_layers`) without breakage

## 🗂️ Directory Layout

### This document

- `web/src/map/registry/README.md` — what the registry is, how to extend it, and the governance rules

### Related repository paths (common touchpoints)

| Area | Path | Relationship to registry |
|---|---|---|
| UI app root | `web/` | Registry is used by map UI components |
| Map UI | `web/src/map/` | Map engine, controls, inspectors |
| API boundary | `src/server/` | Provides tiles/features/metadata; enforces redaction |
| Schemas | `schemas/` | JSON schemas for validation (registry schema expected) |
| Governance docs | `docs/governance/` | Sensitivity + sovereignty rules |

### Expected structure (recommended)

> **Note:** File names below are **recommended** to clarify responsibilities. Update this tree to match the actual implementation (some paths may be **not confirmed in repo**).

~~~text
📁 web/
└─ 📁 src/
   └─ 📁 map/
      └─ 📁 registry/
         ├─ 📄 README.md                 🧭 This guide
         ├─ 📄 index.ts                  📦 Public exports
         ├─ 📄 types.ts                  🧾 Layer/Source/Registry types
         ├─ 📄 loadRegistry.ts           🔄 Load + normalize registry data
         ├─ 📄 validateRegistry.ts       ✅ Schema/type validation
         ├─ 📄 registryDefaults.ts       🎛️ Default visibility/opacity/ordering
         ├─ 📁 adapters/                 🔌 MapLibre/Cesium adapters
         │  ├─ 📄 maplibreAdapter.ts     🗺️ MapLibre source/layer builder
         │  └─ 📄 cesiumAdapter.ts       🌐 Cesium layer builder (optional)
         └─ 📁 __tests__/                🧪 Registry unit tests
            └─ 📄 registry.spec.ts
~~~

## 🧭 Context

### Canonical KFM pipeline alignment (why the registry exists)

The registry sits in the **UI stage** of the canonical KFM flow:

ETL → STAC/DCAT/PROV → Graph (Neo4j) → API → **UI (Map)** → Story Nodes → Focus Mode

The UI must be able to:

- list layers that are available,
- render them safely,
- show provenance pointers (evidence, lineage),
- and **refuse** to render unsafe precision or restricted layers unless governance allows it.

### Non-negotiable invariants (UI)

- **API boundary enforced:** UI **does not** read Neo4j directly; all access is via contracted APIs.
- **No hidden data leakage:** layers that are sensitive must not become sensitive-by-interaction.
- **Evidence-first:** if a layer is used in narrative or Focus Mode, it should be traceable to evidence IDs (STAC/DCAT/PROV).
- **No secrets in the registry:** no tokens/keys embedded in JSON/TS configs.

### What “sensitivity” means for map layers

Sensitivity is not only a label; it is a **behavior contract**:

- Controls **what zoom levels** are allowed
- Controls **what inspect/query/export** operations are allowed
- Controls **how geometry is generalized** (or whether it is shown at all)
- Controls **which users** (or environments) may see it (RBAC details are upstream; UI enforces gating flags)

### “Not confirmed in repo” (where registry data lives)

KFM documentation describes a JSON-based layer registry pattern (e.g., `web/**/layers/*.json`) that the frontend can fetch on load, including sensitivity flags. If your implementation differs (TS exports, API-served registry, etc.), update this README and keep the invariants above.

## 🗺️ Diagrams

### Runtime data flow (registry → map render)

~~~mermaid
flowchart LR
  A[STAC/DCAT/PROV catalogs] --> B[API layer]
  C[Layer Registry config] --> D[Registry loader + validator]
  B --> E[UI map data fetch: tiles/features/metadata]
  D --> F[Map engine adapter]
  E --> F
  F --> G[Map UI render + controls]
  G --> H[Story Nodes / Focus Mode]
~~~

### Safety gate concept (“no hidden data leakage”)

~~~mermaid
flowchart TB
  L[Layer entry] --> S[Sensitivity rules]
  S --> Z[Allowed zoom range]
  S --> Q[Allowed queries / inspect]
  S --> R[Generalization / redaction]
  Z --> OK[Renderable]
  Q --> OK
  R --> OK
  S -->|Violation| BLOCK[Block / degrade / require review]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Registry entries | JSON/TS | **not confirmed in repo** (e.g., `web/**/layers/*.json`) | Schema/type validation |
| API endpoints (tiles/features) | HTTP | `src/server/**` | Contract tests (server) + runtime guards (UI) |
| Evidence references | IDs/URIs | STAC/DCAT/PROV catalogs | Cross-link checks (where tooling exists) |
| Styling rules | JSON/TS | UI code | Lint + unit tests |

### Outputs (runtime)

| Output | Format | Produced by | Contract / Schema |
|---|---|---|---|
| Normalized registry | Typed objects | `loadRegistry` | Type checks + unit tests |
| Map sources + layers | Engine-specific objects | adapter(s) | MapLibre/Cesium expectations |
| Layer selector metadata | UI-friendly model | registry normalizer | A11y + behavior tests |
| Provenance/attribution info | UI model | registry normalizer | Required fields in registry |

### Sensitivity & redaction (UI-facing)

- Prefer **server-side** redaction/generalization for sensitive layers; UI should not be the only line of defense.
- If UI must enforce additional safety:
  - cap `maxZoom`,
  - disable feature inspect,
  - disable exports,
  - show clear “redacted/generalized” notices.

### Quality signals (recommended)

- Registry validation passes in CI
- No broken ID references (layers referenced by Story Nodes exist)
- Attribution + license present for any externally sourced tiles/data
- Sensitivity constraints prevent precision escalation

## 🌐 STAC, DCAT & PROV Alignment

### STAC

For each data-bearing layer, prefer linking to:

- STAC Collection ID(s): where the dataset lives
- STAC Item ID(s): when a layer is tied to specific assets (time slices, scenes)

**UI rule:** the registry should **reference** STAC IDs, not duplicate catalog contents.

### DCAT

For each publishable dataset layer, prefer linking to:

- DCAT dataset identifier (and license/publisher details if needed)

### PROV-O

For each derived/processed layer, prefer linking to:

- `prov:Activity` (transform run or pipeline step)
- `prov:Entity` (artifact ID)
- `prov:Agent` (pipeline/tool identity)

### Versioning expectations

- Registry entry IDs should be **stable**; changes to IDs are breaking for Story Nodes and saved UI state.
- Treat layer config changes as versioned:
  - breaking changes → bump major (or follow repo’s UI versioning policy)
  - safe additions/metadata improvements → bump minor/patch

## 🧱 Architecture

### Responsibilities of this module

This directory should contain (at minimum):

- **Registry loading:** read registry entries from config or endpoint
- **Validation:** ensure entries match expected schema/type constraints
- **Normalization:** apply defaults (order, visibility, opacity, zoom)
- **Adapters:** translate registry entries to MapLibre/Cesium source/layer configs
- **Governance hooks:** enforce sensitivity behavior (caps, disable inspect, etc.)

### Interfaces / contracts (expected)

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas/contracts | `src/server/` + docs | Contract tests required |
| Layer registry | **not confirmed in repo** (example pattern: `web/**/layers/*.json`) | Schema-validated |

### Layer entry contract (recommended minimal shape)

> This is a **recommended** shape to keep the registry legible and safe. Align with the repo’s actual schema/types where they exist.

~~~ts
export type MapEngine = "maplibre" | "cesium" | "both";

export type LayerKind =
  | "vector-tiles"
  | "raster-tiles"
  | "geojson"
  | "feature-service"
  | "basemap";

export type SensitivityLevel =
  | "public"
  | "sensitive"
  | "restricted";

export interface ProvenanceRefs {
  stac_collection_ids?: string[];
  stac_item_ids?: string[];
  dcat_dataset_ids?: string[];
  prov_bundle_ids?: string[];
}

export interface LayerRegistryEntry {
  /** Stable, story-node-addressable ID (recommended: "<domain>:<kebab-slug>") */
  id: string;

  title: string;
  description?: string;

  engine: MapEngine;
  kind: LayerKind;

  source: {
    /** e.g., tile URL template, API endpoint, or static asset path */
    uri: string;
    /** Optional: MIME/type hints for adapters */
    format?: string;
  };

  render: {
    /** Engine-specific styling. Keep this thin; prefer shared style tokens. */
    style?: Record<string, unknown>;
    order_hint?: number;
    opacity_default?: number;
    min_zoom?: number;
    max_zoom?: number;
  };

  attribution: {
    required: string;
    license?: string;
    url?: string;
  };

  provenance?: ProvenanceRefs;

  sensitivity: {
    level: SensitivityLevel;
    /** Human-readable reason; helps governance review and UI messaging */
    notes?: string;

    /** Interaction gates to prevent hidden data leakage */
    gates?: {
      allow_inspect?: boolean;
      allow_export?: boolean;
      enforce_max_zoom?: number;
    };

    /** Access rules (RBAC specifics are upstream; keep flags declarative) */
    access?: {
      requires_auth?: boolean;
      allowed_roles?: string[]; // not confirmed in repo
    };
  };

  defaults?: {
    visible?: boolean;
  };

  tags?: string[];
}
~~~

### Example registry entry (JSON)

~~~json
{
  "id": "land_treaties:cession_boundaries",
  "title": "Land Treaties — Cession Boundaries",
  "description": "Cession boundary overlays for treaty-era territorial changes (generalized geometry where needed).",
  "engine": "maplibre",
  "kind": "geojson",
  "source": {
    "uri": "/api/map/layers/land_treaties/cession_boundaries",
    "format": "application/geo+json"
  },
  "render": {
    "order_hint": 420,
    "opacity_default": 0.65,
    "min_zoom": 4,
    "max_zoom": 10
  },
  "attribution": {
    "required": "Kansas Frontier Matrix (KFM) — curated historical boundary overlays",
    "license": "CC-BY-4.0"
  },
  "provenance": {
    "stac_collection_ids": ["kfm:collections:land-treaties"],
    "dcat_dataset_ids": ["kfm:dcat:land-treaties:cession-boundaries"],
    "prov_bundle_ids": ["kfm:prov:land-treaties:cession-boundaries:v1"]
  },
  "sensitivity": {
    "level": "public",
    "notes": "Generalized boundaries only; no site-scale sensitive locations.",
    "gates": {
      "allow_inspect": true,
      "allow_export": false,
      "enforce_max_zoom": 10
    }
  },
  "defaults": {
    "visible": false
  },
  "tags": ["history", "treaties", "boundaries"]
}
~~~

### Adding or updating a layer (practical checklist)

1) **Choose a stable `id`**  
   - Recommended: `<domain>:<kebab-slug>`  
   - Do not change IDs lightly (Story Nodes and saved UI state depend on them).

2) **Declare the data source**  
   - Prefer an API endpoint or tiles served via the API boundary.
   - Do not embed secrets/tokens.

3) **Attach attribution + license**  
   - Required for external tiles and data.

4) **Add provenance pointers** (when available)  
   - STAC/DCAT/PROV IDs; if missing, document why.

5) **Set sensitivity behavior**  
   - Cap zoom, disable inspect/export as needed.
   - Ensure you cannot recover sensitive precision by interaction.

6) **Validate + test**  
   - Schema/type validation for the registry.
   - Unit tests for loader/adapter behavior and safety gates.

7) **Document Story Node compatibility**  
   - If a story node uses the layer, ensure `focus_layers` references match.

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes should reference layer IDs via `focus_layers`.
- Layers used in narratives should be provenance-linked (STAC/DCAT/PROV IDs where possible).
- Any predictive/analytic overlays must be clearly labeled and governed (opt-in with uncertainty metadata).

### Provenance-linked narrative rule

- If a story makes a claim based on a layer, the UI should be able to show:
  - the layer ID,
  - its evidence pointers (STAC/DCAT/PROV),
  - and any redaction/generalization notices.

### Optional structured controls (Story Node → UI hints)

~~~yaml
focus_layers:
  - "land_treaties:cession_boundaries"
focus_time: "1860-01-01"
focus_center: [-98.0000, 38.0000]
~~~

### Compatibility constraint

- The registry is the canonical list of valid `focus_layers` values.
- Removing/renaming a layer ID is a **breaking change** for Story Nodes and Focus Mode.

## 🧪 Validation & CI/CD

### Validation steps (recommended)

- [ ] Markdown protocol checks (front matter + required sections)
- [ ] UI registry schema checks (layer registry)
- [ ] Link/reference checks (no orphan file pointers or IDs)
- [ ] Secrets scan (no tokens/keys in registry/config)
- [ ] PII / sensitive-location scans (where applicable)
- [ ] Accessibility checks for layer selector UI (where applicable)

### CI behavior contract (lineage gates)

- Validate if present: if `schemas/**` or registry files change, validate them.
- Fail if invalid: schema errors, broken refs, or unsafe gates should fail deterministically.
- Skip if not applicable: optional roots absent → skip without failing the overall pipeline.

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate UI registry schema
# make validate-ui-registry

# 2) run UI unit tests
# make test-ui

# 3) run markdown lint / protocol checks
# make lint-docs
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| `layer_registry_loaded` | UI runtime | **not confirmed in repo** (`docs/telemetry/**`) |
| `layer_toggle_changed` | UI runtime | **not confirmed in repo** |
| `sensitive_layer_blocked` | UI runtime | **not confirmed in repo** |
| `focus_layers_resolved` | Focus Mode | **not confirmed in repo** |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:

- adding a **new data source** (license + provenance verification),
- increasing precision/zoom/access in a way that could expose restricted locations,
- exposing a new layer to public/default visibility,
- changing sensitivity classification or access gating behavior.

### CARE / sovereignty considerations

- Identify impacted communities and protection rules for sensitive/restricted locations.
- Prefer aggregation/generalization for public outputs.
- Ensure provenance/audit logs do not re-expose restricted geometry or identifiers.

### AI usage constraints (for this README and registry work)

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy, inferring sensitive locations.
- AI may propose safe defaults, but **human review** must approve any sensitivity downgrade or precision increase.

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---:|---:|---|---|---|
| v1.0.0 | 2025-12-25 | Initial Map Layer Registry README scaffold | TBD | TBD |

---

Footer refs:

- Master guide: `docs/MASTER_GUIDE_v12.md`
- v13 blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---


