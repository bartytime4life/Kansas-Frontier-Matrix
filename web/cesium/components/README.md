---
title: "Cesium UI Components"
path: "web/cesium/components/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:components-readme:v1.0.0-draft"
semantic_document_id: "kfm-web-cesium-components-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:web:cesium:components-readme:v1.0.0-draft"
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

# web/cesium/components

## 📘 Overview

This directory contains **frontend UI components** for KFM’s **Cesium-based 3D** mode (globe/terrain/3D scene). Components here should be:

- **Config-driven**: layers and defaults should come from configuration when possible.
- **API-fed**: data and provenance should come from the backend API boundary.
- **State-preserving**: able to toggle between 2D and 3D modes without losing user context.

> This file documents folder responsibilities and boundaries. It intentionally avoids listing exact component filenames unless they’re stabilized (not confirmed in repo).

## 🎯 Scope

### In scope

- Cesium viewer lifecycle wrappers (create/destroy viewer, context/provider, resize handling).
- Layer renderers/adapters (translate layer definitions into Cesium primitives/entities).
- Interaction components (pick/hover, selection, camera controls, time scrubbing).
- Cesium-coupled helpers (resource cleanup, event bridging).

### Out of scope

- ETL, catalog generation, or graph ingestion logic.
- API contract definitions (those belong in API contract docs).
- Secrets/credentials or deployment environment configuration.

## 🧭 Architecture alignment

### Pipeline placement

These components are part of the **UI stage** of the canonical KFM pipeline:

ETL → catalogs → graph → APIs → UI → Story Nodes → Focus Mode

**Implication:** components should consume **API outputs** as the contract boundary (no direct graph/database access; no backend filtering duplicated in UI).

### 2D/3D toggle expectation

KFM’s design supports switching between **2D (MapLibre)** and **3D (Cesium)** when required. The UI should preserve user context (e.g., layer selection, camera location, time selection) across toggles.

### Config-driven layers

KFM expects that layers can be extended by updating a **layer configuration** (rather than adding code for every layer). Components should therefore:

- Render from a layer definition model (ids, defaults, data sources, styling parameters).
- Avoid hard-coded layer lists inside components.
- Keep Cesium-specific rendering details in this folder; keep shared layer metadata in config.

See `web/cesium/config/README.md`.

## 🗂️ Directory layout

~~~text
📁 web/
└── 📁 cesium/
    ├── 📁 config/
    │   └── 📄 README.md
    └── 📁 components/
        └── 📄 README.md
~~~

## 🧩 Recommended component roles

The names below are **examples** (not canonical; align to actual code):

- **Viewer wrapper**: owns the Cesium `Viewer` instance and exposes it through context.
- **Layer renderer**: renders an enabled layer definition into Cesium primitives/entities.
- **Entity/feature interaction**: selection, hover, click-through; emits “selected entity” events upward.
- **Timeline/time controller**: binds Cesium clock/time and syncs to KFM’s time controls.

## 🔁 Data flow

A typical flow should look like:

1. Load *layer definitions* from `web/cesium/config`.
2. Obtain user context from app state (current time, filters, active story/focus state).
3. Fetch required data via **API endpoints** (e.g., features for current viewport/time range).
4. Render in Cesium using layer renderer adapters.
5. On interaction, emit events (selection/hover/camera change) to app state; request details via API as needed.

### Focus Mode hooks

When a user enters Focus Mode (or a story segment requests it), components should be able to apply:

- A target camera center/extent.
- A target time (or time range).
- A recommended set of layers (enable/disable).

Where those hints come from (story-node metadata, a Focus API “focus bundle”, etc.) is handled at the app level; components should accept the resulting “focus state” via props/context.

## 🧪 Testing and quality

- Prefer deterministic tests for rendering decisions and data mapping.
- Use integration tests sparingly for Cesium viewer init/cleanup (WebGL can be flaky in CI).
- Validate cleanup: unmounting the viewer should release event handlers and WebGL resources.

## 🔒 Security and governance notes

- Never embed API keys, access tokens, or service URLs that should be environment-scoped.
- Treat *what you render* as governed: **the API layer is responsible for filtering/redaction**, and UI must not bypass it.
- Avoid leaking sensitive identifiers into logs/telemetry.

## ✅ Definition of Done

- [ ] Component respects the API boundary (no direct database/graph access).
- [ ] Layer rendering is config-driven (no hard-coded layer ids).
- [ ] 2D/3D toggle preserves user context (camera/time/layer selection).
- [ ] Viewer resources are cleaned up on unmount (no memory leaks).
- [ ] Tests added/updated for the new behavior.
- [ ] README updated if a new pattern or folder convention is introduced.

## 🔗 References

- `docs/MASTER_GUIDE_v12.md`
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `web/cesium/config/README.md`
---
