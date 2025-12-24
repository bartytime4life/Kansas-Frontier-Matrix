---
title: "Cesium glTF Fixtures — Web UI Test Assets"
path: "web/cesium/assets/fixtures/gltf/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:fixtures:gltf:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-fixtures-gltf-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:fixtures:gltf:readme:v1.0.0"
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

# web/cesium — glTF fixtures

## 📘 Overview

### Purpose
This directory is the **UI-owned home** for small, deterministic **glTF/glb fixtures** used to validate Cesium model loading, rendering, and interaction workflows in the KFM web UI.

These assets are intended to be:
- **Local** (no network fetches required)
- **Small** (fast CI + quick dev iteration)
- **Well-licensed** (clear source + usage rights)
- **Repeatable** (stable outputs across machines/builds)

### Scope

| In Scope | Out of Scope |
|---|---|
| Small `.glb` / `.gltf` fixtures used for UI tests, demos, and reproducible reproduction cases | Production-grade 3D content, large meshes, large textures, 3D Tiles, or “story” assets intended for publication |
| Minimal assets for edge cases (materials, animations, Draco/meshopt, texture variants) | Any asset requiring remote URLs or external CDNs |
| Synthetic fixtures created by contributors | Third-party assets without explicit license + attribution |

### Audience
- Primary: UI contributors working in `web/` and Cesium integration work
- Secondary: QA / reviewers validating regressions and reproducible bug reports

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- glTF: Khronos 3D transmission format; `.glb` = binary container, `.gltf` = JSON + external buffers/textures.
- Fixture: A small, controlled asset used for tests and reproducible debugging.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/assets/fixtures/gltf/README.md` | UI | Contract for fixture hygiene |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governs structure + front-matter expectations |
| Governance | `docs/governance/*` | Governance | Licensing + sensitivity expectations |

### Definition of done (for this document)
- [ ] Front-matter complete + path matches file location
- [ ] Directory layout documented with an emoji-safe tree
- [ ] Clear “add a fixture” rules (license, size, validation)
- [ ] Explicit boundaries: fixtures vs production/story assets
- [ ] Validation steps described (even if repo-specific commands are TBD)

## 🗂️ Directory Layout

### This document
- `path`: `web/cesium/assets/fixtures/gltf/README.md` (must match front-matter)

### Related repository paths (context)
| Area | Path | What lives here |
|---|---|---|
| UI (canonical home) | `web/` | Map layers, Focus Mode UI, citation rendering |
| Cesium UI integration (sub-area) | `web/cesium/` | Cesium-specific UI code + assets (if present) |
| Data domains | `data/` | Raw/work/processed datasets; publishable assets should live here |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Evidence artifacts + provenance bundles |
| API boundary | `src/server/` | UI-facing contracts (UI must not read Neo4j directly) |
| Graph | `src/graph/` | Ontology + ingest (never read directly from UI) |

### Fixture layout (recommended)
This is the recommended, CI-safe layout for this directory (per “outer backticks, inner tildes” fencing practice in governed docs).

~~~text
web/
└── 🌐 cesium/
    └── 🧱 assets/
        └── 🧪 fixtures/
            └── 🧩 gltf/
                ├── 📄 README.md
                ├── 📁 <fixture_slug>/                 # one fixture per folder (recommended)
                │   ├── 🧩 model.glb                   # preferred: single-file, easiest to serve
                │   ├── 🖼️ preview.png                 # optional: used for docs/visual diff
                │   ├── 📄 LICENSE.md                  # required if any third-party source is used
                │   └── 🧾 metadata.json               # recommended: provenance + intent
                └── 📁 _shared/                        # optional: shared textures/buffers for multiple fixtures
~~~

Notes:
- Folder/file names should be **kebab-case** where possible.
- Prefer `.glb` unless a test explicitly needs `.gltf` + external resources.

## 🧭 Context

### Why fixtures live here
- Fixtures used by the UI belong under the **UI canonical home (`web/`)** rather than data domains.
- Fixtures are **test inputs**, not publishable datasets. If a model becomes user-facing or is referenced in narratives, it should be promoted into the data lifecycle with explicit provenance + catalog metadata (STAC/DCAT/PROV).

### Architectural boundary reminders
- The UI should never query Neo4j directly; it should only interact via API contracts.
- These fixtures are static assets served/loaded by the web stack and should not create a new bypass path to restricted data.

## 📦 Data & Metadata

### Inputs
A fixture may be sourced from:
- Synthetic/generated geometry (preferred)
- A third-party model (only if license/attribution are clear and included)

### Required metadata for third-party fixtures
If any fixture is based on third-party work, include:
- `LICENSE.md` (or equivalent) in the fixture folder, capturing:
  - original author/organization
  - license type + terms
  - where it came from (name/identifier; avoid raw URLs unless necessary)
  - any modifications made

### Recommended `metadata.json` schema (lightweight)
~~~json
{
  "id": "example-fixture-slug",
  "title": "Example fixture: material edge-cases",
  "intent": "Reproduces metallic-roughness + normal map behavior for Cesium load tests.",
  "gltf": {
    "format": "glb",
    "version": "2.0"
  },
  "source": {
    "type": "synthetic | third-party",
    "name": "TBD",
    "license": "TBD",
    "attribution_required": true
  },
  "created_by": "TBD",
  "created_at": "YYYY-MM-DD",
  "notes": "Any special loading instructions, known limitations, expected render traits."
}
~~~

## 🌐 STAC, DCAT & PROV Alignment

### Status
**Not applicable by default**: these are UI fixtures, not cataloged datasets.

### Promotion rule (when a model becomes publishable)
If a 3D model is intended to be:
- user-facing content,
- referenced by a Story Node,
- or an evidence artifact,

then do **not** keep it only as a UI fixture. Promote it into the data lifecycle:
- store as a data artifact under `data/**` (domain-appropriate),
- emit/attach provenance under `data/prov/**`,
- and (if relevant) publish discovery metadata under `data/stac/**` and `data/catalog/dcat/**`.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Web UI (`web/`) | Renders and interacts with 3D models | Loads static fixture assets |
| Cesium integration | Loads glTF/glb into the scene | Asset URL or bundled asset handle |
| Tests (not confirmed) | Ensure determinism + prevent regressions | Snapshot / render checks / load success |

### How fixtures should be referenced (pattern)
- Prefer **relative paths** within the web asset system.
- Avoid hard-coding environment-specific absolute paths.
- Do not reference external HTTP(S) resources from inside glTF (textures/buffers should be local or embedded).

## 🧠 Story Node & Focus Mode Integration

### Default rule
Fixtures in this directory should **not** be treated as story evidence or narrative assets.

### If a fixture is used in a narrative
- It must be provenance-linked (dataset/asset identifier + provenance bundle).
- Narrative claims that rely on model-derived observations must trace to a governed evidence artifact (not the fixture folder).

## 🧪 Validation & CI/CD

### Validation steps (recommended)
- [ ] License check: third-party fixtures include `LICENSE.md` and `metadata.json`
- [ ] Offline check: no external URLs embedded in `.gltf`/buffers/textures
- [ ] Format check: glTF 2.0 compatible
- [ ] Size hygiene: fixtures remain small enough for fast CI (threshold **not confirmed in repo**)
- [ ] Smoke test: fixture loads in the Cesium view used by tests or local dev harness (**not confirmed in repo**)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run UI tests that load fixtures
# 2) run any glTF validation step used in CI (if present)
# 3) run markdown lint / protocol checks (if present)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| fixture_load_time_ms | UI test harness | `docs/telemetry/` + `schemas/telemetry/` (if present) |
| fixture_load_failures | UI test harness | `docs/telemetry/` + `schemas/telemetry/` (if present) |

## ⚖ FAIR+CARE & Governance

### Review gates
Changes to this directory should trigger review if they:
- introduce third-party assets (license/attribution required),
- add large binaries that may stress CI,
- add assets that could be culturally sensitive or restricted in nature (apply sovereignty policy).

### CARE / sovereignty considerations
- While these are “just fixtures,” avoid including culturally sensitive heritage models unless governance explicitly approves their use and licensing/access terms.

### AI usage constraints
- Keep the front-matter AI permissions/prohibitions aligned with repo-wide governance references.
- Do not use AI outputs to infer or reconstruct sensitive locations or restricted cultural content from any related assets.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium glTF fixtures | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
