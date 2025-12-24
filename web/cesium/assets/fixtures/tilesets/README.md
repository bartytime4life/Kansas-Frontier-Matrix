---
title: "🧱 Cesium Tileset Fixtures"
path: "web/cesium/assets/fixtures/tilesets/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:assets:fixtures:tilesets:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-fixtures-tilesets-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:fixtures:tilesets:readme:v1.0.0"
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

# 🧱 Cesium Tileset Fixtures

## 📘 Overview

### Purpose

This directory contains **small, self-contained 3D Tiles tilesets** used as **fixtures** for the KFM Cesium UI. Fixtures exist to support **deterministic local development**, **UI testing**, and **repeatable demos** without depending on external tile services.

Reveal and protect the key boundary:

- **Fixtures are UI support artifacts.**
- **Canonical tilesets intended as evidence** belong in the governed pipeline outputs (ETL → STAC/DCAT/PROV → Graph → API → UI), not in UI fixtures.

### Scope

| In Scope | Out of Scope |
|---|---|
| Minimal tilesets for dev/test/demo | Production-scale tilesets, canonical domain datasets, any tileset requiring restricted access |
| Deterministic static assets | Any tileset that must be provenance-linked and cited as evidence |
| Clearly licensed synthetic or open assets | Sensitive location disclosure, Indigenous show-and-tell sites, or anything requiring masking |

### Audience

- Primary: UI engineers working on Cesium integration, layer loading, and UI tests.
- Secondary: QA, reviewers, and data engineers who need to understand the boundary between **UI fixtures** and **governed evidence artifacts**.

### Definitions

- Glossary: `docs/glossary.md` (not confirmed in repo — add/repair link if it lives elsewhere)
- Tileset fixture: a small, locally served 3D Tiles package intended for deterministic UI behavior.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering and invariants |
| UI boundary rule | (implied by architecture) | Maintainers | UI consumes via APIs only; no direct graph calls |
| This README | `web/cesium/assets/fixtures/tilesets/README.md` | UI | Rules for what belongs here |

### Definition of done

- [ ] This README exists and matches `path` in front matter.
- [ ] Each fixture tileset is self-contained (all referenced assets resolve).
- [ ] Reveals **no sensitive locations** and includes only appropriately licensed content.
- [ ] Fixtures are not used as Story Node “evidence” unless promoted into the governed data pipeline with STAC/DCAT/PROV.

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/tilesets/README.md` (must match front matter)

### Related repository paths

| Area | Path | Notes |
|---|---|---|
| UI root | `web/` | React/MapLibre/Cesium UI lives here |
| Cesium integration | `web/cesium/` | Cesium-specific components, adapters, assets |
| Fixture assets | `web/cesium/assets/fixtures/` | Local-only artifacts for deterministic tests |
| Governed evidence outputs | `data/**` | Canonical home for ETL outputs and catalogs (STAC/DCAT/PROV) |

### Expected file tree for this sub-area

This is the expected structure for fixture tilesets. If your implementation differs, update this README to match.

~~~text
web/
└─ cesium/
   └─ assets/
      └─ fixtures/
         └─ tilesets/
            ├─ 📄 README.md
            └─ 📁 <tileset_id>/
               ├─ 📄 tileset.json
               ├─ 📁 content/                # b3dm/i3dm/pnts/glb/etc. (implementation-defined)
               └─ 📄 fixture.meta.json       # recommended (see metadata guidance below)
~~~

## 🧭 Context

### Background

Cesium UI work benefits from **repeatable** local tileset loading to validate:

- camera behavior and bounding volumes
- feature picking and styling
- performance regressions
- error handling for missing tiles or malformed content

Fixtures reduce flakiness by removing dependence on network services and external availability.

### Assumptions

- Tilesets are served as static assets by the UI dev server and/or build output.
- Tilesets are intentionally small and chosen to exercise UI logic rather than to represent canonical domain data.

### Constraints and invariants

- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- The UI **must not** directly query the graph database; all graph access is through contracted APIs.
- Fixtures must not become “shadow production data revealed through the UI.”
- No secrets, keys, or protected endpoints are stored here.
- Sensitive locations must be avoided or generalized, consistent with FAIR+CARE.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we want a tileset fixture index file (manifest) to enable deterministic test discovery? | TBD | TBD |
| Should CI enforce a maximum fixture footprint per tileset or per directory? | TBD | TBD |

### Future extensions

- Add a schema for `fixture.meta.json` under `schemas/ui/` (not confirmed in repo).
- Add a fixture manifest (suggested: `tilesets.manifest.json`) if automated test discovery is needed.
- Add automated validation that checks asset references inside each `tileset.json`.

## 🗺️ Diagrams

### System dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Cesium UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (Cesium Viewer)
  participant Static as Static Asset Server
  UI->>Static: GET /.../tilesets/<tileset_id>/tileset.json
  Static-->>UI: tileset.json
  UI->>Static: GET referenced tile content
  Static-->>UI: tile payloads
~~~

## 📦 Data and metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Fixture tileset package | 3D Tiles (tileset.json + payload files) | Stored locally under this directory | Load succeeds in viewer; no missing asset references |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Deterministic UI load | Runtime behavior | UI test harness | UI tests + optional visual regression |
| Optional fixture metadata | JSON | `fixture.meta.json` | Proposed schema (not confirmed in repo) |

### Suggested fixture metadata

If you add `fixture.meta.json`, keep it minimal and stable. Example fields:

- `id`, `title`, `description`
- `license`
- `source` (if derived from a public dataset) or `synthetic: true`
- `sensitivity_review` (e.g., `ok_public` / `requires_masking`)

### Sensitivity and redaction

- Use **synthetic** tilesets where possible.
- If real-world geometry is used, ensure it does not expose sensitive or restricted locations.
- Avoid representing Indigenous sacred or vulnerable sites in fixtures unless fully governed and generalized.

### Quality signals

- Loads without errors (no 404s, no unresolved references)
- Stable bounding volume and predictable camera framing
- No excessive textures/meshes for a fixture context
- Clearly stated license and source

## 🌐 STAC, DCAT and PROV alignment

### STAC

- Fixtures here are **not** STAC-cataloged by default.
- If a tileset becomes a canonical evidence artifact, it must move into the data lifecycle and be cataloged under `data/stac/` with appropriate links.

### DCAT

- Not applicable for fixtures by default.
- Canonical published tilesets should be discoverable via DCAT distributions.

### PROV-O

- Not applicable for fixtures by default.
- Canonical tilesets should include provenance linking source → transform → publish.

### Versioning

- Use semantic versions for this README.
- For fixtures themselves: treat folder names and contents as stable test assets. If a fixture changes, record it (or version the fixture ID) to avoid breaking regressions silently.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Fixture tileset | Deterministic tileset content | Static files under `tilesets/<id>/` |
| Cesium viewer layer | Loads and displays tilesets | UI code (CesiumJS) |
| UI tests | Ensure deterministic behavior | Test runner (implementation-defined) |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Fixture folder structure | This README | Update README with any structural changes |
| Optional fixture metadata schema | `schemas/ui/` (not confirmed in repo) | Semver + validation in CI if adopted |

### Extension points checklist

- [ ] Add a new folder under `tilesets/` with a stable `<tileset_id>`
- [ ] Ensure `tileset.json` references only local files
- [ ] Include license/source notes (in `fixture.meta.json` or adjacent text file)
- [ ] Add/adjust UI tests that load the fixture deterministically

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode

- Fixtures may be used for **developer demo layers** only.
- Fixtures must not be used as **evidence** in published narratives.

### Provenance-linked narrative rule

- Story Nodes must only make claims that trace to **cataloged evidence artifacts** (dataset/record/asset IDs) produced through the governed pipeline.
- If a tileset must be cited, publish it through ETL → catalogs → graph → API and reference that evidence, not this fixture directory.

### Optional structured controls

~~~yaml
focus_layers:
  - "fixtures:<tileset_id>"   # dev-only marker; do not publish without evidence artifacts
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation and CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] UI tests that load at least one fixture tileset (if tests exist)
- [ ] Optional: fixture reference validation (no missing files)
- [ ] License and sensitivity review for any non-synthetic fixture

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run UI unit/integration tests
# (not confirmed in repo)
npm test

# 2) start dev server and manually load a fixture tileset in Cesium
# (not confirmed in repo)
npm run dev
~~~

### Telemetry signals

| Signal | Purpose | Where to log |
|---|---|---|
| Tileset load failures | detect missing assets / malformed tileset.json | UI telemetry (path not confirmed in repo) |
| Network request count | catch regressions in fixture loading | UI telemetry (path not confirmed in repo) |

## ⚖ FAIR+CARE and governance

### Review gates

- Non-synthetic fixtures require a reviewer to confirm:
  - license compatibility
  - sensitivity risk (especially location disclosure)

### CARE and sovereignty considerations

- Do not include fixtures that expose sensitive Indigenous locations, cultural resources, or vulnerable sites.
- Prefer generalized or synthetic geometry for UI behavior tests.

### AI usage constraints

- AI may assist with generating **synthetic** test geometry, but:
  - do not generate from restricted sources
  - do not infer or include sensitive locations
  - record synthetic provenance in `fixture.meta.json` if used

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial tileset fixtures README | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
