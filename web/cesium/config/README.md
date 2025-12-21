---
title: "Cesium Config"
path: "web/cesium/config/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:web:cesium:config-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-config-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:config-readme:v1.0.0"
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

# Cesium Config

This folder contains **frontend configuration artifacts** that shape how the KFM web client initializes and runs Cesium-related functionality, including the expected ability to switch between **2D (MapLibre)** and **3D (Cesium)** rendering contexts without losing user state.

> Note: The exact config filenames and loader mechanism are **not confirmed in repo** from the materials available in this workspace. This README defines *what belongs here* and *how to document it*; update the “Key artifacts” table and file tree to match the actual implementation.

## 📘 Overview

### Purpose

- Document the intent and usage of configuration under `web/cesium/config/`.
- Make UI behavior extensible by configuration where appropriate (for example, adding UI-visible layers via registry-style config rather than code edits).

### Scope

| In Scope | Out of Scope |
|---|---|
| Config files for Cesium viewer defaults, provider selection, and feature flags | Secrets/credentials committed to the repo |
| Mappings between conceptual “layers” and renderers (2D/3D) | Backend ETL/catalog/graph changes |
| Validation expectations for config inputs | API contract changes (use API Contract Extension template) |

### Audience

- Primary: Frontend engineers working in `web/` (Cesium/MapLibre UI)
- Secondary: Platform engineers validating deploy-time environment configuration, QA reviewers verifying Focus Mode rendering behavior

### Definitions and glossary

- Glossary link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Layer registry**: a configuration-driven list of map layers the UI can render/toggle
  - **Focus Mode**: a dedicated story/entity view that adjusts map/timeline and shows provenance-linked narrative
  - **Provider**: imagery/terrain/data source used by Cesium to render base layers

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/config/README.md` | Web/UI | Governs expectations for this config area |
| Cesium config files | `web/cesium/config/*` | Web/UI | **Not confirmed in repo**: list concrete filenames here |
| Layer registry | `web/cesium/layers/*` | Web/UI | Suggested by KFM guidance; confirm actual path/name |
| Config schema | `schemas/web/*` | Platform | Recommended for CI validation; **not confirmed in repo** |

### Definition of done

- [ ] Front-matter complete and valid
- [ ] No secrets or tokens committed in config files
- [ ] Config keys documented with defaults and validation expectations
- [ ] Any layer-name used by Story/Focus has a deterministic mapping to a UI layer entry
- [ ] Validation steps listed and repeatable
- [ ] CARE/sovereignty and sensitivity considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/config/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend | `web/` | React + map clients (MapLibre/Cesium) |
| Cesium UI code | `web/cesium/` | Cesium integration code (not confirmed in repo) |
| Cesium config | `web/cesium/config/` | Data-only config artifacts for Cesium integration |
| Layer registry | `web/cesium/layers/` | Layer registry config (not confirmed in repo) |
| APIs | `src/server/` | Contracted access layer (UI does not read graph directly) |
| Schemas | `schemas/` | JSON schema validation inputs for CI (recommended) |
| Story nodes | `docs/reports/story_nodes/` | Narrative artifacts + Focus Mode controls (path not confirmed in repo) |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 config/
        └── 📄 README.md
        # Optional config artifacts (examples only — not confirmed in repo):
        # ├── 📄 viewer.defaults.json
        # ├── 📄 providers.imagery.json
        # ├── 📄 providers.terrain.json
        # ├── 📄 feature_flags.json
        # └── 📄 layer_renderer_map.json
~~~

## 🧭 Context

### Background

KFM’s UI layer is designed to support map exploration and an immersive narrative experience. KFM guidance explicitly anticipates a UI that can switch between 2D and 3D contexts (MapLibre ↔ Cesium) and remain extensible via configuration updates (for example, adding new layers through a config update rather than code changes). (See project implementation guidance.)

### Assumptions

- Configuration in this directory is **data-only** (JSON/YAML/TS constants) and does not execute side effects.
- Environment-specific values (tokens, service URLs) are provided via runtime env or deployment secrets manager.
- The UI uses **API contracts** to fetch data and provenance bundles for Focus Mode.

### Constraints and invariants

- The end-to-end pipeline ordering remains: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend consumes data via APIs and must not directly query the graph.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the exact config loader entrypoint and format (JSON vs TS)? | TBD | TBD |
| Where is the layer registry file located and what schema does it use? | TBD | TBD |
| What is the supported override order (defaults → env → runtime)? | TBD | TBD |

### Future extensions

- Add JSON Schema(s) under `schemas/` for each config artifact in this folder.
- Add CI validation to fail builds on unknown keys, invalid URLs, or missing required fields.
- Add a typed “normalized config” interface to prevent runtime drift between 2D/3D layer names.

## 🗺️ Diagrams

### Cesium config consumption flow

~~~mermaid
flowchart LR
  subgraph WebClient["Web Client (React)"]
    Cfg["web/cesium/config (data-only)"] --> Loader["Config loader / normalizer"]
    Loader --> Map2D["MapLibre (2D)"]
    Loader --> Map3D["Cesium (3D)"]
  end

  Map2D --> API["API layer (REST/GraphQL)"]
  Map3D --> API
  API --> Provenance["Provenance-linked payloads"]
~~~

## 📦 Data and metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Cesium config artifacts | JSON/YAML/TS | `web/cesium/config/` | Schema validation recommended |
| Environment variables | string | deploy/runtime | CI lint + runtime checks |
| Focus Mode hints | JSON fields in API payloads | API | Contract tests |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized viewer configuration | JS object | runtime | Type/interface recommended |
| Active base providers | viewer state | runtime | N/A |
| Layer renderer mapping | lookup table | runtime | Schema recommended |

### Sensitivity and redaction

- Never commit credentials (Cesium Ion tokens, API keys, signed URLs).
- If a layer is sensitive (culturally sensitive sites, human subjects, restricted locations), the UI must only render it when the API contract authorizes it and provides generalized geometry as required by governance policy.

### Quality signals

- Schema validation passes for all config files in this folder.
- “Unknown key” detection for config objects to prevent silent typos.
- Deterministic layer naming: story/Focus layer names resolve consistently across 2D and 3D renderers.

## 🌐 STAC, DCAT and PROV alignment

### STAC

- This config should not hardcode data values that belong in STAC Items/Collections.
- If this config references a dataset/layer, prefer stable identifiers (collection/item IDs) over ad-hoc URLs.

### DCAT

- If external providers are used for base imagery/terrain, document licensing and attribution requirements here or in a linked UI attribution doc (recommended).

### PROV-O

- Focus Mode and any narrative surfaces must preserve provenance pointers provided by the API.
- Config must not introduce “narrative facts”; it may only control presentation of provenance-linked content.

### Versioning

- If config changes affect user-visible behavior or interpretation of layer naming, treat as a UI contract change and version accordingly (release notes / changelog recommended).

## ✅ Extension points checklist

- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if applicable)

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode may request a “context bundle” from the API and then adjust map state (camera center/zoom) and active layers based on story metadata.
- Configuration here must ensure that any layer names referenced by story controls map deterministically to UI-available layers in both 2D and 3D contexts.

### Provenance-linked narrative rule

- In Focus Mode contexts, narrative claims must trace to a dataset/record/asset ID and remain inspectable via UI “Sources” or “Audit” panels.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD-layer-name"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI

### Validation steps

- [ ] Markdown protocol checks
- [ ] Config schema validation (if schemas exist)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate JSON schemas (config + layer registry)
# 2) run unit tests for config loader/normalizer
# 3) run doc lint / markdown protocol validation
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Config load success/failure | UI runtime | `docs/telemetry/` + `schemas/telemetry/` (not confirmed in repo) |
| Layer toggle usage | UI runtime | telemetry pipeline (not confirmed in repo) |

## ⚖ FAIR+CARE and governance

### Review gates

- Adding a new map layer that surfaces new datasets or sensitive content may require additional review (ethics / sovereignty / security) before release.
- Any change that affects provenance rendering or Focus Mode citation behavior should be treated as a governed UI change and reviewed accordingly.

### CARE and sovereignty considerations

- Identify impacted communities when adding layers involving culturally sensitive locations, and apply generalization/redaction rules as required.

### AI usage constraints

- This document allows summarization/structure extraction but prohibits generating policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for Cesium config area | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
