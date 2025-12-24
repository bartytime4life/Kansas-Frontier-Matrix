---
title: "`web/cesium/assets/fixtures/` — Cesium fixture assets (README)"
path: "web/cesium/assets/fixtures/README.md"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:assets:fixtures:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-fixtures-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:fixtures:readme:v1.0.0"
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

# `web/cesium/assets/fixtures/` — Cesium fixture assets

## 📘 Overview

### Purpose

- Provide a **small, deterministic, repo-local** set of assets that can be loaded by the Cesium-based UI for:
  - unit/integration tests (where applicable),
  - development demos and debugging,
  - regression reproduction (“does this still render the same?”).

### Scope

| In Scope | Out of Scope |
|---|---|
| Small, synthetic or redacted fixture assets intended for frontend usage | Canonical datasets (those belong under `data/` with STAC/DCAT/PROV) |
| Files that can be served from the web build without network access | Large binaries, copyrighted media, or non-redistributable sources |
| Fixtures used to validate loaders/parsers/renderers | “Real” sensitive locations or unredacted culturally sensitive content |

### Audience

- Frontend contributors working on `web/cesium/…`
- Test authors adding UI fixtures (snapshot/golden tests, loader tests)
- Reviewers checking licensing/sensitivity before merge

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Fixture: a small, controlled input used to make tests/demos deterministic.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering; UI is downstream of API |
| Markdown protocol + governed doc structure | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Template used by this README |
| Cesium UI code | `web/cesium/` | Frontend | Cesium integration (3D) |
| UI layer registry (expected) | `web/cesium/layers/` | Frontend | Layer definitions (not confirmed in repo) |

### Definition of done (for this document)

- [ ] Front-matter complete and `path` matches file location
- [ ] Fixture placement rules (size, licensing, sensitivity) are explicit
- [ ] Expected directory layout documented (even if some folders don’t exist yet)
- [ ] Validation steps are either repo-accurate or marked **not confirmed in repo**
- [ ] Footer refs present (governance / ethics / sovereignty)

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Frontend (UI) | `web/` | React + map clients |
| Cesium client | `web/cesium/` | Cesium integration and helpers |
| MapLibre client | `web/map/` *(not confirmed in repo)* | 2D map client (if split out) |
| Tests | `tests/` *(not confirmed in repo)* | Unit/integration/contract tests + fixtures |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 fixtures/
            ├── 📄 README.md
            ├── 📁 czml/                 # CZML fixtures (recommended)
            ├── 📁 tilesets/             # 3D Tiles sample tilesets (recommended)
            ├── 📁 gltf/                 # glTF samples (recommended)
            ├── 📁 geojson/              # small GeoJSON overlays (recommended)
            ├── 📁 imagery/              # small raster images used in tests/demos (recommended)
            └── 📁 metadata/             # per-fixture attribution/license sidecars (recommended)
~~~

## 🧭 Context

### Background

Fixtures in this directory are **UI assets**, not data products. They exist to support the web client and keep UI work **deterministic** and reviewable.

### Assumptions

- The frontend build/dev server can serve files in `web/cesium/assets/…` (exact bundler behavior is **not confirmed in repo**).
- The Cesium UI should be testable without relying on external tile servers or network calls.

### Constraints / invariants

- **No canonical data here:** Anything intended to be “real” KFM data must live under `data/` and be cataloged (STAC/DCAT/PROV).
- **Determinism:** Fixtures should be runnable offline (or with network explicitly mocked).
- **Size discipline:** Keep fixtures small. If a large asset is unavoidable, store it elsewhere (e.g., LFS/DVC) and document the pointer (not confirmed in repo).
- **Licensing:** Every fixture must be redistributable. If derived from a third-party source, include attribution + license in a sidecar (see below).
- **Sensitivity:** Do not include restricted locations or culturally sensitive data unless it is appropriately generalized/redacted and approved under governance.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical “fixture size budget” for `web/`? | TBD | TBD |
| Is there an existing fixture manifest/index file for UI assets? | TBD | TBD |
| What test framework(s) consume these fixtures (unit, e2e, snapshot)? | TBD | TBD |

### Future extensions

- Add a lightweight fixture manifest (name, type, intended use, checksums) to help tests discover fixtures deterministically.
- Add “golden rendering” snapshot tests for selected fixtures (if supported by the UI test stack).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[UI code: web/cesium] --> B[Fixture assets: web/cesium/assets/fixtures]
  A --> C[Contracted APIs]
  C --> D[Downstream data products]
  D --> E[STAC/DCAT/PROV + Graph]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant Dev as Developer / Test
  participant UI as Cesium UI
  participant F as Fixture (static asset)

  Dev->>UI: Load a fixture-driven scene
  UI->>F: fetch/resolve local fixture asset
  F-->>UI: bytes/JSON
  UI-->>Dev: Deterministic render / assertion target
~~~

## 📦 Data & Metadata

### Inputs

- Fixture files themselves (e.g., JSON, binary models, images).
- Optional per-fixture sidecar metadata.

**Recommended sidecar file (one per fixture):**

~~~json
{
  "fixture_id": "example-fixture-id",
  "format": "czml|3dtiles|gltf|geojson|png|jpg|…",
  "intended_use": ["unit_test", "integration_test", "demo"],
  "source": {
    "origin": "synthetic|derived",
    "upstream_name": "TBD",
    "upstream_url": "TBD",
    "retrieved_date": "YYYY-MM-DD"
  },
  "license": {
    "spdx": "CC-BY-4.0",
    "attribution": "TBD"
  },
  "checksums": {
    "sha256": "TBD"
  },
  "notes": "TBD"
}
~~~

### Outputs

- Static assets consumed by the Cesium UI and related tests.
- (Optional) metadata sidecars to enable auditability (license + provenance).

### Sensitivity & redaction

- Default expectation: **public, low-risk**.
- If a fixture is derived from sensitive content, document:
  - what was generalized/redacted,
  - what review approved inclusion,
  - and where the authoritative source-of-truth remains (usually under `data/`).

### Quality signals

| Signal | Meaning | How to check |
|---|---|---|
| “Offline-loadable” | Works without network | Load in dev/test with networking disabled |
| Small size | Won’t bloat repo/build | Verify file sizes in review/CI |
| License present | Redistributable | Sidecar metadata or README list includes license |
| Deterministic | Stable outputs | Snapshot/golden tests (if available) |

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- **Not applicable** for UI fixtures as a primary artifact.
- If a fixture is derived from a canonical STAC asset, reference the STAC Item/Asset ID in the sidecar metadata.

### DCAT

- **Not applicable** for UI fixtures as a discovery catalog.
- If fixtures mirror published datasets, ensure DCAT remains the canonical discovery surface (under `data/catalog/dcat/`).

### PROV-O

- **Recommended:** If fixtures are derived from real inputs, capture a minimal provenance note in sidecar metadata:
  - source → transform → fixture artifact
- Do **not** treat fixtures as canonical evidence.

### Versioning

- Changing an existing fixture can break tests unexpectedly.
- Prefer:
  - additive new fixture files, and/or
  - versioned filenames (e.g., `foo_v2.czml`) with explicit deprecation notes.

## 🧱 Architecture

### Components

| Component | Role | Notes |
|---|---|---|
| `web/cesium/` | Cesium UI logic | Loads fixtures via local asset URLs/imports |
| `web/cesium/assets/fixtures/` | Static fixture storage | Must remain small + redistributable |
| Contracted APIs | Runtime data | UI should not query Neo4j directly |

### Interfaces / contracts

- Fixtures are an **implicit contract** between:
  - the Cesium UI asset loader(s), and
  - tests/demos that reference specific fixture paths.
- Breaking changes should be handled like API contracts:
  - add/rename with care,
  - update references atomically,
  - prefer additive patterns.

### Extension points checklist (for future work)

- [ ] Add a schema for fixture sidecar metadata (if desired)
- [ ] Add a manifest index (optional)
- [ ] Add automated size/license checks in CI (not confirmed in repo)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Typically **not directly**.
- Fixtures may be used for UI demos or development previews, but Story Nodes must reference canonical evidence artifacts (datasets, documents) rather than fixtures.

### Provenance-linked narrative rule

- Any user-facing narrative claim must point to an authoritative record/dataset identifier.
- UI fixtures are not considered authoritative evidence.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Asset loads successfully in the Cesium UI
- [ ] No network calls required (unless explicitly mocked/approved)
- [ ] File sizes and count remain reasonable
- [ ] License/provenance sidecar exists for any derived fixture
- [ ] No secrets/PII embedded in fixtures (especially in images or metadata)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) run UI dev server
# <TBD>

# 2) run UI tests that consume fixtures
# <TBD>

# 3) run doc lint / markdown protocol checks
# <TBD>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Fixture size drift | CI / review | CI logs or PR checks (not confirmed in repo) |
| Snapshot diffs | UI test runner | Test artifacts (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when fixture changes introduce:

- new sensitive locations,
- any culturally sensitive content,
- or any license/attribution ambiguity.

### CARE / sovereignty considerations

- Avoid fixtures that encode restricted locations or sensitive cultural sites.
- If inclusion is necessary, follow the sovereignty policy and document redaction/generalization behavior and approvals.

### AI usage constraints

- Allowed: summarize, structure extraction, translation, keyword indexing
- Prohibited: generating policy, inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial Cesium fixtures README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
