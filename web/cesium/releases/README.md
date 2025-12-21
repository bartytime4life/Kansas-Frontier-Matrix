---
title: "Cesium Releases"
path: "web/cesium/releases/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:web:cesium:releases:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-releases-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:releases:readme:v1.0.0"
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

# Cesium Releases

## 📘 Overview

### Purpose
This directory documents and hosts **versioned Cesium-related frontend “release bundles”** needed by the KFM web UI’s Cesium integration.

The intent is to make Cesium runtime assets and related packaging **deterministic, reviewable, and pin-able**, so the UI can load a known-good set of assets without relying on implicit “latest” behavior.

### Scope
| In Scope | Out of Scope |
|---|---|
| Folder structure + naming conventions for Cesium release bundles | Generating geospatial datasets (ETL) |
| “What belongs here vs elsewhere” guidance for UI assets vs cataloged data | STAC/DCAT/PROV generation (Catalog stage) |
| Minimal governance / sensitivity rules for assets committed here | Neo4j/graph modeling and migrations |
| Validation expectations for adding / updating a bundle | API contract design and versioning |

### Audience
- Primary: Frontend engineers working in `web/` and Cesium integration maintainers
- Secondary: Data/catalog engineers (to ensure artifacts are stored in the correct subsystem), reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Release bundle**: A versioned folder containing Cesium runtime assets (and/or KFM-specific Cesium UI assets) needed by the client at runtime.
  - **Layer registry**: JSON config listing UI layers and sensitivity flags (expected under `web/cesium/layers/` in KFM conventions).
  - **Sensitive layer**: A layer or asset whose exact locations/metadata should be generalized or access-controlled.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/releases/README.md` | Frontend | Governs release folder conventions |
| Cesium release bundles | `web/cesium/releases/<release_id>/...` | Frontend | One folder per pinned release |
| Layer registry | `web/cesium/layers/…` | Frontend | Source-of-truth list of UI layers |
| Cataloged data | `data/stac/…` | Data/Catalog | UI should not treat this directory as a data catalog |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Release bundle conventions are explicit (naming, manifest, licensing notes)
- [ ] Constraints/invariants preserved (API boundary, pipeline ordering)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/releases/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Frontend root | `web/` | React + mapping clients |
| Cesium integration | `web/cesium/` | Cesium runtime wiring, layer configs |
| Cesium releases | `web/cesium/releases/` | Versioned runtime bundles |
| Layer registry | `web/cesium/layers/` | Layer definitions + sensitivity flags |
| Data catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Machine-validated catalogs and provenance |

### Expected file tree for this sub-area
~~~text
🌐 web/
└── 🧊 cesium/
    ├── 📦 releases/
    │   ├── 📄 README.md
    │   ├── 📁 <release_id>/
    │   │   ├── 📄 MANIFEST.json
    │   │   ├── 📄 THIRD_PARTY_NOTICES.md
    │   │   └── 📁 assets/
    │   │       └── 📁 ...
    │   └── 📁 <release_id>/
    │       └── 📁 ...
    └── 🗺️ layers/
        └── 📄 <layer_registry>.json
~~~

Notes:
- `MANIFEST.json` and `THIRD_PARTY_NOTICES.md` are **recommended** conventions for traceability and licensing hygiene. If the repo uses different filenames, update this README to match the canonical practice.

## 🧭 Context

### Background
KFM’s frontend supports map-centric exploration and may include a 3D mode powered by Cesium. This introduces a packaging concern: Cesium integrations typically require a set of runtime assets that must be served consistently and versioned to avoid breaking changes.

### Assumptions
- The web application reads **layer definitions** from a registry-style JSON file under `web/cesium/…`.
- “Release bundles” here are treated as **frontend implementation artifacts**, not authoritative datasets.

### Constraints / invariants
- The canonical KFM pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- The frontend must consume data via APIs and contracts — **no direct Neo4j access**.
- This directory must not become a dumping ground for large datasets; datasets should live under `data/` and be cataloged.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we need a single “active release” pointer file (e.g., `CURRENT.json`) or should selection be build-time only? | Frontend | TBD |
| Should release bundles be checked for size and routed to artifact storage/CDN instead of git when large? | Maintainers | TBD |

### Future extensions
- Add a schema for `MANIFEST.json` under `schemas/web/cesium_release_manifest.schema.json` (requires governance + CI wiring).
- Add CI checks that ensure each release bundle includes license notices and checksums.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL outputs] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[Web UI]
  E --> F[Cesium runtime]
  F --> G[Release bundle pinned in web/cesium/releases]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Cesium runtime assets | files | vendored/build output | checksum + size review |
| Layer registry entries | JSON | `web/cesium/layers/` | schema-validated (recommended) |
| Feature data / tiles | API payloads | API layer | contract tests |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Release bundle | folder | `web/cesium/releases/<release_id>/` | `MANIFEST.json` (recommended) |
| UI layer toggles | JSON | `web/cesium/layers/*.json` | schema-validated (recommended) |

### Sensitivity & redaction
- Do not include restricted or sensitive location content directly in frontend bundles.
- If a layer requires generalization/redaction, enforce it through API delivery + layer registry flags (never “bake in” sensitive geometries here).

### Quality signals
- Every release bundle should be:
  - Identified by a stable `release_id`
  - Traceable (source/version recorded in `MANIFEST.json`)
  - Integrity-checked (hashes recorded, optional)

## 🌐 STAC, DCAT & PROV Alignment

This folder is **not** a STAC/DCAT/PROV output location.

Guidance:
- If you are shipping geospatial assets (e.g., 3D Tiles, CZML) as data products, they belong under `data/…` and must be cataloged (STAC/DCAT) with provenance (PROV).
- The UI may reference those assets via API routes, but should not treat this directory as the canonical dataset store.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| APIs | Serve contracted data + apply redaction rules | REST/GraphQL |
| UI (React/Map) | Render 2D/3D maps + narrative panels | API calls |
| Cesium runtime | 3D rendering engine | UI integration layer |
| Release bundles (this dir) | Versioned runtime asset packaging | Build-time and/or runtime selection |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Layer registry | `web/cesium/layers/*.json` | Semver-compatible schema |
| UI ↔ API | `src/server/` + docs | Contract tests required |
| Release manifest (recommended) | `web/cesium/releases/<release_id>/MANIFEST.json` | Semver + changelog |

### Release bundle requirements
Each `web/cesium/releases/<release_id>/` should include:
- A manifest describing the bundle’s provenance (what it is, where it came from, what version).
- License / third-party notices if vendor assets are included.
- A stable internal layout so that the UI can reference assets predictably.

Recommended `MANIFEST.json` shape:
~~~json
{
  "release_id": "cesium-runtime-vX.Y.Z",
  "created_at": "YYYY-MM-DD",
  "source": {
    "type": "vendor|build",
    "name": "CesiumJS",
    "version": "X.Y.Z",
    "ref": "commit/tag/url"
  },
  "integrity": {
    "hash_alg": "sha256",
    "files": {
      "assets/...": "<sha256>"
    }
  },
  "notes": "Human-readable build/release notes."
}
~~~

## 🧠 Story Node & Focus Mode Integration

Cesium release bundles should not embed narrative content.

Rules:
- Story Nodes live under `docs/reports/.../story_nodes/` (or another governed doc location) and are served via API.
- Focus Mode consumes provenance-linked context bundles; do not “shortcut” by hardcoding story content into UI release assets.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter present, headings, fences)
- [ ] UI build succeeds with the new bundle wired in (repo-defined command)
- [ ] Layer registry JSON validates against schema (if schema exists)
- [ ] No sensitive assets accidentally committed (manual review + automated scans)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run frontend lint
# 2) run frontend unit tests
# 3) build web app
# 4) smoke-test Cesium mode loads release assets
~~~

## ⚖ FAIR+CARE & Governance

### Review gates
- If a release bundle changes what layers are visible or alters sensitivity handling:
  - Requires governance review for sovereignty/sensitivity implications.
- If large third-party assets are introduced:
  - Requires license review and size/performance review.

### CARE / sovereignty considerations
- Avoid publishing exact coordinates or culturally sensitive locations through UI artifacts.
- Ensure restricted layers are delivered through APIs with appropriate gating.

### AI usage constraints
- Do not use AI to infer or reconstruct sensitive locations when assembling UI assets.
- Any AI-generated narrative belongs in Story Node workflow with explicit provenance.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial README for Cesium release bundles | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal doc template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
