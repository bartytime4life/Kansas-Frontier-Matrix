---
title: "Cesium Imagery Fixtures — README"
path: "web/cesium/assets/fixtures/imagery/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:fixtures:imagery-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-fixtures-imagery-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:fixtures:imagery-readme:v1.0.0"
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

# Cesium Imagery Fixtures

Small, **version-controlled imagery fixtures** for the Cesium portion of the KFM web UI.

These fixtures exist to make local development, CI, and UI regression testing possible **without depending on external tile services** (rate limits, tokens, outages, or changing basemaps).

> Architectural invariant reminder (KFM): **UI never reads Neo4j directly**; data access is via contracted APIs. These fixtures are **static front-end assets** used only to render maps/globes in a deterministic way (they are not an API shortcut).

## 📘 Overview

### Purpose

- Provide **stable** imagery inputs for Cesium demos/tests (and any offline/dev modes).
- Ensure Cesium scenes render **deterministically** in CI (no network variability).
- Keep third-party imagery licensing/attribution **auditable** and centralized.

### Scope

In scope:

- Small tile pyramids (XYZ/TMS-style) and/or single images used as **fixtures**
- Minimal metadata needed to explain **projection**, **tiling scheme**, and **attribution**
- License/NOTICE hygiene for any third-party-derived content

Out of scope:

- Production basemap hosting
- Large regional or global imagery datasets (these belong in governed `data/**` domains with STAC/DCAT/PROV)

### Audience

- Front-end developers working on Cesium integration and rendering behavior
- CI/QA maintainers validating deterministic UI behavior
- Reviewers verifying licensing/attribution compliance

### Definitions

- **Fixture**: a small, committed artifact used for deterministic tests/dev rendering.
- **Imagery**: raster basemap content used by Cesium imagery providers.
- **Attribution**: required credit text (and/or link) mandated by an imagery license.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Cesium assets NOTICE | `web/cesium/assets/NOTICE.md` | UI maintainers | Third-party notices/attribution for assets bundled under `web/cesium/assets/` |
| KFM canonical pipeline reference | `docs/MASTER_GUIDE_v12.md` | KFM Core Team | Pipeline invariants and subsystem boundaries |

### Definition of done (for this directory)

- [ ] Every fixture has an explicit license and attribution trail
- [ ] No fixture requires network access to render
- [ ] Fixture footprint is kept intentionally small (prefer “minimum tiles to test behavior”)
- [ ] `web/cesium/assets/NOTICE.md` is updated when third-party content is introduced

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/imagery/README.md` (must match front-matter)

### Recommended fixture structure

This directory may contain one or more fixture packs. Keep each fixture pack self-contained.

~~~text
web/
└── 🌐 cesium/
    └── 🧰 assets/
        └── 🧪 fixtures/
            └── 🗺️ imagery/
                ├── 📄 README.md
                ├── 🗂️ <fixture-name>/
                │   ├── 🧾 attribution.md        # Required attribution text (and link, if applicable)
                │   ├── 🧬 source.json           # Where it came from + license identifier
                │   └── 🧱 tiles/                # Optional: tile pyramid (scheme documented in source.json)
                │       └── 🧩 {z}/{x}/{y}.png
                └── 🗂️ <fixture-name-2>/...
~~~

### `source.json` minimum fields

Keep fixture metadata simple and machine-readable.

~~~json
{
  "id": "example-fixture",
  "description": "Short description of what this fixture is meant to test.",
  "source": {
    "name": "TBD (provider / dataset)",
    "url": "TBD (source URL)",
    "retrieved_at": "YYYY-MM-DD",
    "license": "TBD (SPDX id if possible)",
    "attribution_required": true
  },
  "tiling": {
    "scheme": "XYZ|TMS|single-image",
    "format": "png|jpg|webp",
    "minzoom": 0,
    "maxzoom": 2
  },
  "spatial": {
    "crs": "EPSG:3857|EPSG:4326|TBD",
    "bbox_wgs84": [-180, -90, 180, 90]
  },
  "integrity": {
    "sha256": "TBD"
  }
}
~~~

## 🧭 Context

### When to use fixtures

Use fixtures when you need to validate:

- imagery provider wiring (URL template paths, request parameters)
- Cesium rendering behavior (layer ordering, alpha blending, gamma/brightness)
- camera/scene defaults in an environment that should not depend on external services

### When NOT to use fixtures

Do **not** use fixtures to:

- ship production basemaps
- replace governed datasets (anything “real” and re-usable should go through **ETL → STAC/DCAT/PROV → Graph → API → UI**)

## 🗺️ Diagrams

### How fixtures typically fit in the UI

~~~mermaid
flowchart LR
  Dev[Developer / CI] --> Web[Web app build]
  Web --> Static[Static asset server]
  Static --> Cesium[Cesium ImageryProvider]
  Cesium --> Scene[Rendered Globe/Scene]
~~~

## 📦 Data & Metadata

### Supported formats

Fixtures may be any of the following, as long as they are small and deterministic:

- Tile pyramids (`{z}/{x}/{y}.*`) for URL-template imagery providers
- Single images used by a “single-tile” style provider

Record the actual format and scheme in `source.json`.

### Size expectations

There is no hard limit enforced by this README alone, but **keep fixtures minimal**:

- Prefer the smallest zoom range that reproduces the behavior you’re testing.
- Avoid adding “pretty” imagery that doesn’t serve a test/dev purpose.

## 🌐 STAC, DCAT & PROV Alignment

By default, these UI fixtures are **not** treated as governed datasets and are **not** cataloged in:

- `data/stac/`
- `data/catalog/dcat/`
- `data/prov/`

If an imagery asset is important enough to be reused across domains and stories, it should be promoted into the data pipeline and receive full STAC/DCAT/PROV treatment.

## 🧱 Architecture

### Boundary rules (non-negotiable)

- These fixtures may help render a base layer, but they must **not** be used to smuggle domain facts into the UI.
- Any domain data shown in Cesium (features, entities, events) still comes from **contracted APIs**, not from static assets in this directory.

## 🧠 Story Node & Focus Mode Integration

- Story Nodes should cite governed evidence artifacts (STAC/DCAT/PROV outputs), not UI fixtures.
- If a Story Node requires a background layer for a screenshot or illustration, prefer a governed dataset or a clearly licensed public-domain background and document it in `NOTICE.md`.

## 🧪 Validation & CI/CD

### Suggested checks (implementation dependent)

- [ ] No broken relative links in `attribution.md`
- [ ] `source.json` present for each fixture pack
- [ ] No secrets/tokens embedded in metadata
- [ ] Fixture assets are reasonably small and reviewable (avoid huge binary diffs)

## ⚖ FAIR+CARE & Governance

- Only include imagery you have the right to redistribute.
- If attribution is required, ensure it is present in:
  - the fixture pack’s `attribution.md`, and
  - `web/cesium/assets/NOTICE.md` (for centralized third-party notices)
- Avoid imagery that could expose sensitive locations or culturally sensitive sites unless explicitly approved under KFM governance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial imagery fixtures README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

