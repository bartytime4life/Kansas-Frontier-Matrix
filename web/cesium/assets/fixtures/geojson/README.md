---
title: "Cesium GeoJSON Fixtures — README"
path: "web/cesium/assets/fixtures/geojson/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:fixtures:geojson:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-fixtures-geojson-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:fixtures:geojson:readme:v1.0.0"
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

# Cesium GeoJSON Fixtures — README

> Purpose (required): Document what belongs in `web/cesium/assets/fixtures/geojson/`, how these GeoJSON fixtures are used by the Cesium UI, and the rules that keep fixtures small, safe, deterministic, and governance-compliant.

## 📘 Overview

### Purpose

- Provide **small, deterministic GeoJSON fixture files** for local development, demos, and UI tests of the Cesium globe/map integration.
- Define **what is allowed** in this directory (and what must live elsewhere, e.g., `data/**`).
- Prevent fixture drift that can accidentally become “production data” or introduce sensitive content.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small GeoJSON samples used to validate Cesium rendering, interaction (hover/click), styling, and camera behaviors | Canonical datasets or evidence products (these belong in `data/<domain>/{raw,work,processed}/` with STAC/DCAT/PROV) |
| Synthetic or heavily simplified public geometry for UI-only scenarios | Any data requiring provenance, update scheduling, or governance review as a dataset |
| Regression fixtures for known UI bugs (edge cases) | Large files that bloat the web bundle / slow CI or dev builds |

### Audience

- **Primary:** Frontend contributors working in `web/cesium/**` on GeoJSON rendering, layers, and interaction logic.
- **Secondary:** Reviewers/maintainers validating fixture changes and ensuring governance + safety constraints.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include: **GeoJSON**, **FeatureCollection**, **Cesium DataSource**, **fixture**, **deterministic**, **redaction/generalization**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline and invariants |
| Markdown protocol + governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Required reference for governed docs |
| Cesium web client | `web/cesium/` | Frontend | Cesium UI implementation root (assumed from this path) |
| GeoJSON fixtures directory | `web/cesium/assets/fixtures/geojson/` | Frontend | This folder |

### Definition of done (for this document)

- [ ] Front-matter complete + valid and `path:` matches file location
- [ ] Rules for what belongs here are explicit (fixtures vs canonical data)
- [ ] Validation steps are listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations are explicit for fixture content
- [ ] Footer refs are present (do not remove)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/geojson/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (frontend) | `web/` | React/Map UI (includes Cesium); must not read Neo4j directly |
| Cesium UI | `web/cesium/` | Cesium-specific UI code and assets |
| Assets | `web/cesium/assets/` | Static assets used by the Cesium UI |
| Fixtures | `web/cesium/assets/fixtures/` | Small dev/test/demo fixtures (non-canonical) |
| GeoJSON fixtures | `web/cesium/assets/fixtures/geojson/` | GeoJSON fixture files used by the UI |
| Canonical data | `data/` | Raw/work/processed domain data + catalogs (STAC/DCAT/PROV) |
| API boundary | `src/server/` | Contracted API access (UI must use APIs, not direct graph reads) |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 fixtures/
            └── 📁 geojson/
                ├── 📄 README.md
                └── 🧾 *.geojson
~~~

> Note: Specific fixture filenames are intentionally not enumerated here unless they exist in-repo. Keep this README synchronized with the actual `.geojson` files present.

## 🧭 Context

### Background

This directory exists to support **UI development and testing** of Cesium features without requiring a live backend, network access, or a full local dataset stack.

Fixtures are *not* a replacement for the canonical pipeline:
- **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
Fixtures live at the UI edge and are meant to be small and disposable.

### Constraints / invariants (must hold)

- **No UI direct-to-graph reads:** the web client must never bypass the API boundary to query Neo4j directly.
- Fixtures must not encourage bypassing the contracted API layer in production.
- Fixtures must not introduce sensitive locations, private data, or culturally restricted information.

### When to use fixtures vs canonical data

Use fixtures when you need:
- A deterministic geometry to reproduce a render/interaction bug.
- Offline development for styling or interaction logic.
- A minimal “smoke” geometry to test a new UI layer type.

Do **not** use fixtures when you need:
- Real domain data with provenance requirements.
- Anything that should be discoverable via STAC/DCAT or cited in Story Nodes.
- Anything requiring update cadence tracking.

## 📦 Data & Metadata

### GeoJSON expectations (fixtures)

Fixture GeoJSON files should:

- Be valid GeoJSON (prefer `FeatureCollection`).
- Use lon/lat coordinates appropriate for typical web globe mapping (keep CRS assumptions explicit in code where possible).
- Be **small** (aim for KBs, not MBs) and **fast to load**.
- Avoid extremely dense geometries; simplify when feasible for UI tests/demos.

### Naming conventions (recommended)

Use descriptive, stable names that communicate intent:

- `synthetic__points__basic.geojson`
- `synthetic__lines__antimeridian_edge.geojson`
- `public__ks_boundary__simplified.geojson` *(only if truly public + license compatible)*

If a fixture is tied to a bug/regression, include the issue or ticket reference in the PR (not in the filename unless your repo convention requires it — not confirmed in repo).

### Fixture registry (optional but recommended)

Keep a lightweight registry table here (update it as fixtures are added):

| Fixture file | Category | Purpose | Notes |
|---|---|---|---|
| *(add entries)* | basic / edge-case / regression | what it tests | file size, gotchas |

## 🧱 Architecture

### Loading fixtures in Cesium (example pattern)

~~~ts
// Pseudocode only — align with actual Cesium integration code in-repo (not confirmed in repo).
// Goal: load local GeoJSON for offline UI testing.

const url = "/assets/fixtures/geojson/<fixture>.geojson";
// await GeoJsonDataSource.load(url, { clampToGround: true });
// viewer.dataSources.add(dataSource);
~~~

### Boundary rule reminder

- **Fixtures are local-only inputs.**
- Production UI layers must obtain data through **contracted APIs** and/or catalog endpoints, not via hard-coded static fixtures.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Confirm added/modified `.geojson` parses as GeoJSON (no trailing commas, valid geometry)
- [ ] Confirm file size is reasonable for UI asset bundling
- [ ] Confirm no sensitive locations or restricted/culturally sensitive content is included
- [ ] Confirm fixtures are not used as a production data dependency
- [ ] Confirm docs lint / markdown protocol checks pass (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands (not confirmed in repo)

# 1) run UI lint/build
# 2) run UI/unit tests
# 3) run any fixture validation script (if present)
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Fixture-related load errors | Web app runtime | UI telemetry sink (repo-defined) |
| Bundle size/regression | CI | CI logs/artifacts |
| UI test failures | CI | CI logs/artifacts |

## ⚖ FAIR+CARE & Governance

### Review gates

- Any fixture that resembles real-world data must be reviewed for:
  - license compatibility,
  - sensitivity implications,
  - whether it should instead be elevated into the canonical data pipeline.

### CARE / sovereignty considerations

- If a fixture encodes locations that could be sensitive (cultural sites, protected areas, restricted infrastructure), do **not** include it here.
- Prefer synthetic geometries or generalized shapes where any sensitivity risk exists.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium GeoJSON fixtures directory | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

