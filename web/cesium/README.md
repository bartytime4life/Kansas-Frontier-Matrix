---
title: "KFM Web — Cesium Subsystem README"
path: "web/cesium/README.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v1.0.0"
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

# KFM Web — Cesium Subsystem README

## 📘 Overview

### Purpose
- Document the Cesium-related frontend subsystem under `web/cesium/`.
- Provide governance-safe patterns for adding/removing Cesium layers, integrating them with Focus Mode, and maintaining provenance and CARE gating.

### Scope
| In Scope | Out of Scope |
|---|---|
| Cesium module configuration + layer registry patterns | Backend generation of tiles/COGs/3D tiles |
| Sensitivity gating + provenance pointers for Cesium layers | Neo4j schema changes |
| Focus Mode interaction patterns from Cesium entities | Model inference workflows |

### Audience
- Primary: Frontend engineers working on 3D globe visualization.
- Secondary: Geospatial engineers producing 3D-friendly assets, governance reviewers.

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; add if missing)*
- Terms used in this doc: CesiumJS, terrain, imagery, 3D Tiles, layer registry, provenance.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Web architecture | `web/ARCHITECTURE.md` | Frontend | System invariants |
| Cesium layer registry (proposed) | `web/cesium/layers/regions.json` | Frontend | Path/schema not confirmed |
| Cesium registry schema (proposed) | `web/cesium/layers/regions.schema.v1.json` | Frontend | Not confirmed |
| Focus Mode API | `src/server/` + `docs/` | Backend | Click → focus context |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Frontend | `web/` | React + map clients |
| APIs | `src/server/` | Focus Mode + search endpoints |
| Catalogs | `data/` | STAC/DCAT/PROV outputs |

### Expected file tree for this sub-area
~~~text
🗂️ web/cesium/
├─ 📄 README.md
├─ 📁 layers/                      (not confirmed in repo)
│  ├─ 📄 regions.json               (not confirmed in repo)
│  └─ 📄 regions.schema.v1.json     (not confirmed in repo)
├─ 📁 adapters/                    (not confirmed in repo)
├─ 📁 assets/                      (not confirmed in repo)
└─ 📁 utils/                       (not confirmed in repo)
~~~

## 🧭 Context

### Background
- KFM’s UI is primarily 2D map-focused, but can be extended to richer 3D visualization. Cesium enables a 3D globe/terrain view and allows draping historical maps or datasets over terrain to help users interpret change in topography and land use.

### Assumptions
- Cesium is optional and should be treated as a subsystem that can be enabled without breaking the base 2D workflow.
- Layer configuration is declarative (registry-driven) rather than hardcoded layer-by-layer in UI code *(exact registry file locations are not confirmed in repo)*.

### Constraints / invariants
- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- No ad-hoc adding markers in front-end code without a registry entry (governance + reviewability).
- Sensitive layers must obey CARE rules: default off, zoom-limited, generalized geometry, and/or role-gated where required.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we use Cesium Ion assets (token-based), or only self-hosted terrain/imagery? | TBD | TBD |
| What is the authoritative layer registry schema for Cesium layers? | TBD | TBD |
| How is user role/scope communicated to the UI for restricted layers? | TBD | TBD |

### Future extensions
- 3D Tiles support for large feature sets (buildings, historical reconstructions).
- Evidence panels: show STAC-linked plots/images (e.g., time-series, annotated imagery) alongside Cesium map context.
- Offline “story packs” with pre-bundled Cesium-ready assets.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[STAC/DCAT/PROV catalogs] --> B[Layer registry JSON]
  A --> C[Static assets: tiles/COGs/3D]
  D[APIs] --> E[Focus Mode context bundle]
  B --> UI[Web UI]
  C --> UI
  E --> UI
  UI --> CZ[Cesium Engine]
~~~

### Optional: sequence diagram (Click → Focus Mode)
~~~mermaid
sequenceDiagram
  participant User
  participant CesiumUI
  participant API
  participant Graph
  User->>CesiumUI: Click feature/marker
  CesiumUI->>API: Focus query(entity_id)
  API->>Graph: Fetch subgraph + provenance refs (redaction rules)
  Graph-->>API: Context bundle
  API-->>CesiumUI: Narrative + citations + audit flags
  CesiumUI-->>User: Focus dashboard + provenance
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Cesium layer registry | JSON | `web/cesium/layers/*.json` *(proposed)* | JSON schema validation *(proposed)* |
| Terrain/imagery endpoints | URL/config | static hosting / services | availability + integrity (TBD) |
| Feature overlays | GeoJSON / tiles / 3D Tiles | pipeline outputs | geometry validity (TBD) |
| Focus Mode context | JSON | API | contract tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Cesium-rendered layers | runtime scene graph | browser runtime | performance budgets (TBD) |
| Click/hover events | UI events | telemetry (optional) | telemetry schemas |
| Provenance panel entries | UI state | browser runtime | must include IDs |

### Sensitivity & redaction
- Registry entries for sensitive layers MUST include gating rules (default off, zoom bounds, generalization requirement, and/or role gating).
- Focus Mode responses MUST not contain restricted coordinates unless authorized, and the UI MUST not attempt to “reconstruct” restricted detail client-side.

### Quality signals
- Time-to-first-render for Cesium scene is within acceptable bounds for target devices.
- Layer toggles do not cause uncontrolled memory growth.
- Every rendered dataset is attributable (STAC/DCAT/PROV IDs available to the user).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: TBD (each Cesium layer should reference a STAC collection ID when applicable).
- Items involved: TBD (clickable features should link to item IDs or observation IDs).
- Extension(s): Versioning + any domain extensions (TBD).

### DCAT
- Dataset identifiers: TBD (used for dataset metadata panels).
- License mapping: displayed from DCAT-aligned metadata.

### PROV-O
- `prov:wasDerivedFrom`: surfaced for evidence artifacts.
- `prov:wasGeneratedBy`: surfaced for model runs / transforms that produced overlays.

### Versioning
- Use STAC Versioning links and graph predecessor/successor relationships as applicable.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Clicking a Cesium feature should open an entity panel (or directly activate Focus Mode) using an entity ID that the API can resolve to a provenance-backed context bundle.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "cesium:<layer_id>"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

### Example Cesium layer registry entry (illustrative only; replace IDs/paths)
~~~json
{
  "id": "archaeology_candidates",
  "title": "Potential Archaeological Sites",
  "provenance": {
    "stac_id": "urn:kfm:stac:collection:archaeology:candidates:v1",
    "prov_activity_id": "urn:kfm:prov:activity:example:run:YYYYMMDD"
  },
  "visibility": {
    "default_enabled": false,
    "min_zoom": 8,
    "max_zoom": 18
  },
  "care": {
    "sensitivity_class": "public",
    "generalize": false
  },
  "render": {
    "engine": "cesium",
    "geometry": "point",
    "cluster": true
  }
}
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate layer registry json against schema
# 2) run UI unit tests
# 3) run e2e test that toggles a Cesium layer and verifies expected markers render
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Cesium render timing | browser metrics | `docs/telemetry/` + `schemas/telemetry/` |
| Layer toggle audit | UI events | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- Frontend maintainers approve Cesium module changes.
- Governance review required when adding layers with any sensitivity flags or when changing redaction/generalization behavior.

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- Enforce conservative defaults: default-off visibility and zoom gating for sensitive content.

### AI usage constraints
- Ensure doc’s AI permissions/prohibitions match intended use.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial Cesium subsystem README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`