---
title: "🧩 Cesium Metadata Fixtures — UI Test & Dev Payloads"
path: "web/cesium/assets/fixtures/metadata/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:web:cesium:fixtures:metadata-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-fixtures-metadata-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:fixtures:metadata-readme:v1.0.0"
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

# 🧩 `metadata/` — Cesium metadata fixtures

This folder contains **small, deterministic metadata fixtures** used by the Cesium UI for:

- UI development when backend services are unavailable
- unit/integration tests that must not rely on network calls
- demos and regression cases for metadata-driven UI panels

This directory is a **UI-stage helper**. It is **not** a canonical data source for KFM evidence artifacts.

> For the general fixture rules (what belongs in `fixtures/` vs elsewhere), see:  
> `web/cesium/assets/fixtures/README.md`

---

## 📘 Overview

### Purpose

Provide stable, minimal payloads that simulate or sample **metadata objects** the UI expects to render or inspect, such as:

- STAC Item or Collection JSON (metadata-only fixtures)
- DCAT dataset/distribution records (JSON-LD or simplified JSON)
- PROV-O lineage snippets (JSON-LD or simplified JSON)
- API response envelopes that wrap metadata for UI consumption

Fixtures here should be:
- **small** (fast to load in tests and dev)
- **version-pinned** (no implicit “latest” behavior)
- **sanitized** (no secrets, no PII, no sensitive locations)

### Scope

In scope:
- JSON / JSON-LD / GeoJSON metadata fixtures consumed by the Cesium UI
- “edge case” fixtures that exercise optional/rare fields
- fixtures that mirror contracted API responses, when the UI expects API-shaped payloads

Out of scope:
- canonical evidence artifacts (these belong under `data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- raw or processed domain datasets (these belong under `data/<domain>/{raw,work,processed}/`)
- large binaries (rasters, point clouds, 3D tiles, imagery) unless explicitly required and size-budgeted

### Audience

- Frontend contributors working on Cesium/UI metadata panels
- QA/reviewers validating deterministic UI behavior
- Backend/API contributors updating contracts who need matching UI fixtures

### Definitions linked to glossary

- Glossary: `docs/glossary.md` (not confirmed in repo — update link if glossary lives elsewhere)
- Terms used here: **fixture**, **contract**, **metadata**, **provenance**, **redaction**

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent fixtures index | `web/cesium/assets/fixtures/README.md` | UI | Canonical rules for the fixtures subtree |
| Master pipeline invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Pipeline ordering + boundary rules |
| Canonical STAC outputs | `data/stac/` | Data/Catalog | Source of truth for STAC evidence artifacts |
| Canonical DCAT outputs | `data/catalog/dcat/` | Data/Catalog | Source of truth for DCAT evidence artifacts |
| Canonical PROV outputs | `data/prov/` | Data/Catalog | Source of truth for provenance bundles |
| API contracts | `src/server/contracts/` (not confirmed in repo) | API | Fixtures should mirror these shapes where applicable |

### Definition of done for this document

- [x] Front-matter complete and `path` matches file location
- [x] Directory purpose and non-goals are explicit
- [x] Naming, versioning, and redaction rules are stated
- [x] Expected file tree provided
- [ ] Validation hooks listed and aligned to repo scripts if present
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/metadata/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI runtime | `web/` | Frontend code + runtime assets (including Cesium) |
| Cesium fixtures | `web/cesium/assets/fixtures/` | Small deterministic fixtures used by the UI |
| Data evidence artifacts | `data/` | Canonical datasets and their catalog/provenance outputs |
| STAC catalogs | `data/stac/` | STAC Collections + Items (canonical) |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset records (canonical) |
| PROV bundles | `data/prov/` | Provenance bundles (canonical) |
| API boundary | `src/server/` (not confirmed in repo) | Contracted access layer (UI must not read Neo4j directly) |

### Expected file tree for this sub-area

~~~text
web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 fixtures/
            ├── 📄 README.md
            └── 📁 metadata/
                ├── 📄 README.md
                ├── 📄 *.json
                ├── 📄 *.jsonld
                └── 📄 *.geojson
~~~

> Note: Only include formats the UI actually loads. Prefer JSON unless JSON-LD is required.

---

## 🧭 Context

### Background

Fixtures exist to keep UI work **deterministic and decoupled** from backend availability.

KFM’s canonical pipeline ordering remains the source of truth:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

UI fixtures may *represent* objects from upstream stages, but they must not replace those stages.

### Assumptions

- The frontend build can serve and/or import static assets under `web/`
- Tests and demos must be runnable without external network dependencies

### Constraints and invariants

- **API boundary is enforced:** UI does not read Neo4j directly; it consumes contracted API outputs.
- **No secrets:** Do not place tokens, credentials, private endpoints, or internal URLs in fixtures.
- **No sensitive/regulated content:** Avoid PII and culturally sensitive locations; generalize if needed.
- **Deterministic:** Same fixture content must yield identical UI behavior across machines and time.
- **Small and fast:** Keep fixtures minimal; avoid large assets unless explicitly budgeted.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Is there a JSON Schema for UI fixtures (metadata) under `schemas/`? | TBD | TBD |
| Do we want “minimal / edge / invalid” fixture buckets for UI metadata, similar to catalog fixtures? | TBD | TBD |
| Where is the canonical “fixture loader” interface documented for Cesium UI? | TBD | TBD |

### Future extensions

- Add a JSON Schema for fixture envelopes (if the UI expects a wrapper format)
- Add a CI check for fixture size limits and JSON parse validity
- Add a small index file (if needed) to enumerate fixtures used by storybook/demos

---

## 🗺️ Diagrams

### Metadata fixtures in the UI stage

~~~mermaid
flowchart LR
  A[Canonical evidence<br/>data/stac + data/catalog/dcat + data/prov] --> B[API boundary<br/>src/server]
  B --> C[UI runtime<br/>web/cesium]

  F[UI fixtures<br/>web/cesium/assets/fixtures/metadata] -. dev/test input .-> C

  note1[Invariant: UI consumes APIs<br/>never Neo4j directly] -. applies .-> C
~~~

---

## 📦 Data and Metadata

### Inputs

Common fixture payload types include:

- **STAC**: Item/Collection JSON for metadata UI panels
- **DCAT**: Dataset/Distribution records (JSON-LD or simplified JSON)
- **PROV**: Activity/entity/agent snippets (JSON-LD or simplified JSON)
- **API envelopes**: Objects shaped like the API contract response

### Outputs

Fixtures are used to:

- validate metadata rendering and parsing in the UI
- validate UI behavior for incomplete / edge-case metadata
- provide stable inputs for screenshot/regression testing

### Sensitivity and redaction

Before adding a fixture:

- Remove/replace any personal names, emails, phone numbers, exact home addresses
- Generalize sensitive locations (especially culturally sensitive sites)
- Ensure licenses/attributions remain valid if copying from real datasets

### Quality signals

A good metadata fixture:

- is under a reasonable size budget for fast UI loads
- is readable and minimal: includes only fields required for the test/demo
- uses stable IDs and deterministic ordering where it matters for snapshots
- is versioned or clearly dated so changes are intentional and reviewable

---

## 🌐 STAC, DCAT and PROV Alignment

### STAC

If a fixture claims to be a STAC object:

- keep `stac_version` pinned
- include only the extensions actually needed by the UI
- avoid external asset URLs unless tests explicitly allow network access

### DCAT

If a fixture claims to be DCAT:

- keep identifiers stable
- include minimal dataset/distribution fields used by UI views
- prefer local references over external fetches

### PROV-O

If a fixture claims to be PROV:

- keep entity/activity IDs stable
- ensure relationships are consistent within the snippet

### Versioning

Recommended options:

- include a version suffix in the filename (preferred), or
- include a `fixture_version` field inside the JSON (only if the UI expects it)

Do not rely on “latest” semantics for fixtures.

---

## 🧱 Architecture

### Components

- **Fixture files** stored under `web/cesium/assets/fixtures/metadata/`
- **UI loader** that reads/parses fixtures (implementation location not specified here)
- **UI components** that render metadata views (Cesium/UI)

### Interfaces and contracts

When a fixture is meant to mirror an API response:

- the fixture must match the **contracted shape** (OpenAPI/GraphQL schema, if present)
- contract changes require fixture updates in the same change set

### Extension points checklist

When adding a new fixture:

- [ ] pick the smallest possible payload that reproduces the UI behavior
- [ ] confirm it contains no secrets/PII/sensitive locations
- [ ] keep identifiers stable
- [ ] update any local index or test references (if present)
- [ ] ensure any snapshot tests are updated intentionally

---

## 🧠 Story Node and Focus Mode Integration

If metadata fixtures are used to demo or test Focus Mode metadata panels:

- do not include unsourced narrative text as “facts”
- prefer referencing a Story Node artifact under `docs/reports/story_nodes/` when the UI expects narrative content
- keep provenance references consistent with KFM’s provenance-linked narrative rule

### Provenance-linked narrative rule

Any narrative-like content in fixtures must be either:
- clearly marked as synthetic/demo-only, or
- traceable to a governed Story Node and its cited evidence artifacts

### Optional structured controls

~~~yaml
focus_layers:
  - "demo-layer"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

---

## 🧪 Validation and CI/CD

### Validation steps

Recommended minimum checks:

- [ ] JSON parse validity for all `*.json`, `*.geojson`, `*.jsonld`
- [ ] size budget checks (fixtures stay small)
- [ ] optional schema checks if fixture schemas exist under `schemas/` (not confirmed in repo)

### Reproduction

Run the repo’s frontend lint/test workflows (script names not confirmed in repo). If a fixture causes failures, fix the fixture first rather than weakening tests.

### Telemetry signals

If the UI emits telemetry for metadata parsing:
- include a fixture that triggers the telemetry path for at least one “good” and one “edge” case

---

## ⚖ FAIR+CARE and Governance

### Review gates

- Any fixture derived from real datasets should be reviewed for licensing and attribution requirements.
- Any fixture touching potentially sensitive content should receive governance review.

### CARE and sovereignty considerations

- Treat culturally sensitive sites as high-risk by default.
- If a fixture must represent such a case, generalize geometry/coordinates and remove identifying details.

### AI usage constraints

- Do not infer or fabricate sensitive locations.
- Keep AI-generated demo content explicitly labeled as synthetic.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial metadata fixtures README scaffold | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
