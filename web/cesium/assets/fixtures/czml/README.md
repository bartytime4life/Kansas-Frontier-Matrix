---
title: "Cesium CZML Fixtures"
path: "web/cesium/assets/fixtures/czml/README.md"
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

governance_ref: "../../../../../docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "../../../../../docs/governance/ETHICS.md"
sovereignty_policy: "../../../../../docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "Low risk · Synthetic UI fixtures"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:web:cesium:assets:fixtures:czml:readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-assets-fixtures-czml-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:assets:fixtures:czml:readme:v1.0.0"
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

# CZML Fixtures

## 📘 Overview

### Purpose

- Provide a **clear contract** for what belongs in `web/cesium/assets/fixtures/czml/`.
- Keep Cesium fixtures **small, reproducible, and safe** for local development, demos, and automated tests.
- Ensure fixtures remain compatible with KFM’s architecture where the **UI consumes data via APIs** (fixtures are test stand-ins, not a bypass).

### Scope

| In Scope | Out of Scope |
|---|---|
| Small CZML documents used for demos/tests/visual regression | Large binary datasets, production-grade terrain/tiles |
| Synthetic or public-safe trajectories, markers, timelines | Any restricted or sensitive location content |
| Examples demonstrating time-dynamic behaviors | Live graph queries or direct Neo4j access |

### Audience

- Primary: UI contributors working in `web/cesium/`
- Secondary: Maintainers reviewing governance + CI behavior
- Tertiary: Story authors needing a small 3D preview scene

### Definitions

- **CZML**: A JSON document format used by Cesium for time-dynamic entities (positions, paths, properties over time).
- **Fixture**: A deterministic, test-friendly input artifact (no external dependencies unless explicitly documented).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `web/cesium/assets/fixtures/czml/README.md` | UI maintainers | Placement + naming + safety rules |
| Cesium asset models README | `web/cesium/assets/models/README.md` | UI maintainers | 3D models and model licensing guidance |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |

### Definition of done

- [ ] Front-matter complete and `path` matches file location
- [ ] Directory responsibilities + placement rules documented
- [ ] File naming and safety rules documented
- [ ] Validation expectations stated (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/fixtures/czml/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Cesium UI | `web/cesium/` | Cesium-based UI components, loaders, and view logic |
| Cesium assets | `web/cesium/assets/` | Static assets used by Cesium |
| Models | `web/cesium/assets/models/` | glTF/glb and model notes/licenses |
| Fixtures | `web/cesium/assets/fixtures/` | Test/demo inputs for Cesium UI |
| Docs | `docs/` | Governed architecture and system rules |
| Governance | `docs/governance/` | Governance, ethics, sovereignty policies |

### Expected file tree for this sub-area

~~~text
📁 web/
└── 📁 cesium/
    └── 📁 assets/
        └── 📁 fixtures/
            └── 📁 czml/
                ├── 📄 README.md
                ├── 📄 *.czml
                └── 📄 *.czml.json
~~~

> Notes:
> - File extensions are allowed to be either `*.czml` or `*.czml.json`. Use one convention consistently within the repo.
> - Fixtures should remain **text-only** and **diff-friendly**.

## 🧭 Context

### Background

KFM’s UI stack includes a Cesium option for 3D and time-dynamic visualization, with **CZML** serving as a lightweight exchange format for dynamic scenes.

Fixtures in this folder support:
- quick local demos,
- deterministic automated tests,
- preview scenes for narrative workflows.

### Assumptions

- Cesium is a supported UI mode under `web/cesium/`.
- CZML fixtures may be loaded as static assets during development or testing.
- When fixtures represent real-world content, provenance and safety rules still apply.

### Constraints and invariants

- **Canonical pipeline ordering is preserved**: ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.
- **API boundary is preserved**: the UI does not directly query the graph; fixtures are a test-only stand-in for API-provided payloads.
- **No sensitive content**: do not include restricted locations or culturally sensitive information in fixtures.
- **Determinism**: fixtures must replay the same way across machines.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should we add a CZML structural validator in CI | TBD | TBD |
| Do we standardize on `*.czml` vs `*.czml.json` | TBD | TBD |
| Do we require sidecar provenance for non-synthetic fixtures | TBD | TBD |

### Future extensions

- Add a lightweight CZML validation step (JSON parse + required packet checks).
- Add a small suite of “golden” time-dynamic fixtures for visual regression.
- Add 3D Tiles fixtures under a sibling directory when needed.

## 🗺️ Diagrams

### Fixture load flow

~~~mermaid
flowchart LR
  A[Static fixture file<br/>assets/fixtures/czml] --> B[Cesium CzmlDataSource.load]
  B --> C[Viewer.dataSources.add]
  C --> D[Render<br/>timeline + entities]
~~~

### Canonical pipeline placement

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV]
  B --> C[Graph]
  C --> D[API Boundary]
  D --> E[UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| CZML fixture | JSON array of CZML packets | This directory | JSON parse + basic CZML packet checks |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Rendered entities | Cesium runtime objects | In-browser | Cesium CZML interpretation |
| Test artifacts | Screenshots / snapshots | `tests/` or CI artifacts | Repo test conventions |

### Sensitivity and redaction

- Fixtures are expected to be **synthetic** or **public-safe**.
- If you must reference real locations:
  - generalize coordinates,
  - remove precise timestamps if sensitive,
  - follow `docs/governance/SOVEREIGNTY.md`.

### Quality signals

- JSON validity (no trailing commas, valid UTF-8)
- Minimal size and quick load in browser
- Stable identifiers for entities (`id` fields)
- Time intervals behave consistently on the Cesium timeline

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Fixtures are **not** canonical STAC outputs.
- If a fixture is derived from a STAC Item, document:
  - the source Item ID,
  - the asset used,
  - any simplifications applied.

### DCAT

- If a fixture is derived from a published dataset, document the dataset identifier and license constraints.

### PROV-O

- If a fixture is derived from pipeline outputs, capture:
  - `prov:wasDerivedFrom` (dataset or item ID),
  - `prov:wasGeneratedBy` (run or transform identifier),
  - `prov:wasAssociatedWith` (agent or tool).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Fixture CZML file | Deterministic test/demo input | Static asset fetch |
| Cesium loader | Loads CZML into runtime | `CzmlDataSource.load(...)` |
| Cesium viewer | Renders entities + timeline | Viewer API |
| API boundary | Production data source | REST/GraphQL contracts |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI code contracts | `web/` | Semver or repo policy |
| API contracts | `src/server/` + `docs/` | Contract tests required |
| Fixture conventions | This README | Update with fixtures changes |

### Minimal usage example

~~~ts
// Pseudocode example (illustrative only)
import { CzmlDataSource } from "cesium";

async function loadFixture(viewer) {
  const czmlUrl = "/cesium/assets/fixtures/czml/example.czml";
  const ds = await CzmlDataSource.load(czmlUrl);
  viewer.dataSources.add(ds);
}
~~~

## 🧠 Story Node & Focus Mode Integration

### Story Nodes

- A Story Node may reference a 3D preview scene, but any narrative-facing use must remain **provenance-linked**.
- Fixtures intended for narrative preview should be treated as **derived artifacts**, not primary evidence.

### Focus Mode rule

- Focus Mode consumes **provenance-linked** content only.
- Do not treat fixtures as evidence unless they are explicitly linked to canonical dataset identifiers and governance permits it.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] JSON parse check for all `*.czml` and `*.czml.json`
- [ ] Optional: required-packet check (`document` packet present)
- [ ] Optional: size budget enforcement for fixtures
- [ ] Optional: screenshot-based visual regression tests

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate fixtures (json parse / required packets)
# 2) run UI tests / snapshots
# 3) run markdown lint
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| Fixture load failures | UI tests | CI logs + artifacts |
| Visual regression diffs | Snapshot tests | CI artifacts |
| Governance review notes | PR process | PR description + review history |

## ⚖ FAIR+CARE & Governance

### Review gates

- Adding non-synthetic fixtures that encode real-world sensitive locations
- Adding fixtures that are narrative-facing or could be misinterpreted as evidence
- Introducing external URLs or assets with unclear licensing

### CARE and sovereignty considerations

- Assume culturally sensitive content is **high-risk by default**.
- Avoid precise geographies tied to sensitive contexts.
- Follow governance docs for any redaction/generalization requirements.

### AI usage constraints

- This document permits structural extraction, summarization, translation, and keyword indexing.
- Prohibited: generating new policy text or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial CZML fixtures README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

🔙 Back to Fixtures: `../README.md`  
🧭 Back to Cesium Assets: `../../README.md`  
🏠 Back to Master Guide: `../../../../../docs/MASTER_GUIDE_v12.md`
