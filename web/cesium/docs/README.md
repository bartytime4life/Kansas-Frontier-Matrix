---
title: "KFM Cesium UI — README"
path: "web/cesium/docs/README.md"
version: "v0.1.0"
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

doc_uuid: "urn:kfm:doc:web:cesium:readme:v0.1.0"
semantic_document_id: "kfm-web-cesium-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:web:cesium:readme:v0.1.0"
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

# KFM Cesium UI — README

## 📘 Overview

### Purpose
This README governs **how the KFM web UI integrates Cesium** for 3D/immersive map views, and how that integration must respect KFM’s **API boundary**, **provenance rules**, and **Focus Mode** behavior.

This doc is intended to be the “local source of truth” for work under `web/cesium/`—especially:
- 2D↔3D switching (conceptual layer parity)
- Layer registry–driven configuration
- Focus Mode hooks (focus center/time/layers)
- Provenance-first rendering expectations

### Scope
| In Scope | Out of Scope |
|---|---|
| Cesium integration patterns used by the KFM UI | Neo4j / graph query logic (must remain API-only) |
| Layer registry usage for 3D-capable layers | ETL/catalog generation (STAC/DCAT/PROV) |
| Focus Mode behavior as it relates to the 3D view | Authoring Story Nodes (see Story Node template/docs) |
| UI redaction and “sensitive layer” handling | API authorization/RBAC implementation details |

### Audience
- Primary: Frontend contributors working on map rendering + Focus Mode UX
- Secondary: API/graph contributors validating UI contract assumptions; reviewers checking governance compliance

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo; add if missing)*
- Terms used in this doc: Cesium, MapLibre, Layer Registry, Focus Mode, Provenance, Redaction, Story Node

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering: ETL→Catalog→Graph→API→UI→Story→Focus |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Defines narrative structure + focus hints |
| Cesium UI docs (this file) | `web/cesium/docs/README.md` | Web UI owners | Local Cesium integration guide |
| Layer registry (UI-configurable layers) | `web/cesium/layers/*.json` *(not confirmed exact filenames)* | Web UI owners | JSON config that drives layer toggles |
| Focus Mode API contract docs | `docs/api/` *(not confirmed in repo)* | API owners | Must document Focus bundle shape + provenance objects |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] UI invariants clearly stated (API boundary, provenance, redaction)
- [ ] Layer registry responsibilities documented (including sensitivity flags)
- [ ] Focus Mode ↔ map synchronization behavior documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/docs/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | React/Map UI (MapLibre, Cesium), Focus Mode UX |
| Cesium integration | `web/cesium/` | Cesium-specific code, assets, and layer config |
| Cesium docs | `web/cesium/docs/` | Cesium integration documentation (this file) |
| Layer registry | `web/cesium/layers/` *(not confirmed)* | JSON layer registry/config for toggles |
| API layer | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Schemas | `schemas/` | JSON schemas + validation rules (incl. UI schemas if present) |

## 🧭 Pipeline position & flow

KFM’s canonical ordering means the Cesium UI **consumes contracted API payloads** and **must not** bypass the API layer to query the graph directly.

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram (Focus Mode request)
~~~mermaid
sequenceDiagram
  participant UI as UI (MapLibre/Cesium + Focus Mode)
  participant API as API (Focus endpoint)
  participant Graph as Graph (Neo4j)

  UI->>API: Focus query(entity_id, includeAI?)
  API->>Graph: fetch subgraph + provenance refs (+ redaction)
  Graph-->>API: context bundle
  API-->>UI: narrative + citations + audit flags + map hints
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Focus Mode context bundle | JSON | API (Focus endpoint) | API contract tests + JSON schema (if defined) |
| Layer registry | JSON | `web/cesium/layers/*.json` *(not confirmed)* | JSON schema validation (UI) |
| Basemap/terrain/tiles | Tiles / assets | Configured providers *(not confirmed)* | Availability checks + attribution rules |
| Story Node narrative content | Markdown | API (story node content) | Markdown render tests + citation parsing tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered 3D map view | Runtime UI | N/A | Must match UI state model |
| User-selected layer state | Runtime UI | N/A | Deterministic state updates |
| (Optional) telemetry events | JSON | `docs/telemetry/` + `schemas/telemetry/` *(if present)* | Telemetry schema validation |

### Sensitivity & redaction
- **Sensitive data must be handled upstream** (API + contract). The UI should:
  - Respect layer-level sensitivity flags from the layer registry (e.g., hide, generalize, or gate).
  - Render “redacted” or “generalized” indicators when the API says content was filtered.
  - Avoid revealing precise restricted locations through camera jumps, overlays, or tooltips.

### Quality signals
- Layer load success/failure with actionable messages (no silent failure).
- Geometry validity and safe rendering (avoid crashing on bad GeoJSON/tiles).
- Deterministic layer toggling (same inputs → same visible state).
- Attribution completeness for every displayed layer.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: *(not confirmed in repo)*
- Items involved: *(not confirmed in repo)*
- Extension(s): *(not confirmed in repo)*

### DCAT
- Dataset identifiers: *(not confirmed in repo)*
- License mapping: must align to dataset metadata
- Contact / publisher mapping: must align to dataset metadata

### PROV-O
- `prov:wasDerivedFrom`: UI must display provenance references passed through API responses
- `prov:wasGeneratedBy`: if AI content is included, it must be opt-in and labeled (per API contract)
- Activity / Agent identities: surfaced via “audit/provenance panel” where available

### Versioning
- Use platform + API semantic versioning. For any UI contract changes, ensure compatibility or bump versions per contract rules.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Cesium-specific invariants
- **No direct graph dependency:** Cesium UI must only consume data via the API.
- **2D↔3D parity:** If 2D MapLibre + 3D Cesium are both present, switching should preserve state:
  - same conceptual layers, rendered differently
  - same focus entity, same focus_time, same focus_center
- **Layer registry–driven:** Adding/removing layers should be possible via registry updates (not hard-coded).
- **Provenance-first UI:** Every factual claim shown in Focus Mode must trace to a citation/provenance reference.

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Layer registry | `web/cesium/layers/regions.json` *(template example; not confirmed)* | Schema-validated |

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
- Focus Mode is a specialized UI state that deep-dives into one **entity/story**:
  - map zooms/centers to the relevant location
  - timeline narrows to the relevant period
  - narrative panel renders Story Node markdown **with citations**
  - provenance/audit panel remains available

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (via citations + sources bundle from the API).

### Markdown citations: rendering expectations
Story Nodes use Markdown and include citations in a bracketed reference format. The UI renderer must:
- Parse Markdown → HTML
- Detect citation markers
- Convert citations into clickable source links/popovers (or equivalent)
- Never render “hallucinated” references

### Optional structured controls
Story nodes (or the Focus Mode API response) may include structured hints for the map:

~~~yaml
focus_layers:
  - "TBD-layer-id"
focus_time: "TBD-ISO8601-or-era"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] UI schema checks (layer registry)
- [ ] API contract tests (Focus bundle shape + provenance)
- [ ] UI unit tests for layer toggling + focus application
- [ ] E2E tests for “enter Focus Mode → switch 2D/3D → exit Focus Mode” flows
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate UI schemas (layer registry)
# 2) run UI unit/integration tests
# 3) run E2E tests for Focus Mode flows
# 4) run markdown/doc lint
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| FocusModeEntered | UI | `docs/telemetry/` + `schemas/telemetry/` |
| MapModeSwitched (2D/3D) | UI | `docs/telemetry/` + `schemas/telemetry/` |
| LayerToggled | UI | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- UI changes that expose new datasets/layers should be reviewed for:
  - attribution completeness
  - sensitivity labeling
  - provenance visibility
  - a11y implications
- Changes that could reveal restricted locations or culturally sensitive sites: **requires human review**.

### CARE / sovereignty considerations
- Do not infer or reconstruct sensitive locations from partial context.
- If a layer or feature could enable harm (e.g., precise site discovery), default to:
  - generalization, gating, or omission
  - clear disclosure of what was redacted and why (where permitted)

### AI usage constraints
- AI-derived narrative content must be **opt-in** and labeled with uncertainty metadata, and never mixed indistinguishably with curated facts.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-21 | Initial Cesium UI README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
