---
title: "Cesium Demo Models — README"
path: "web/cesium/assets/models/demo/README.md"
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

doc_uuid: "urn:kfm:doc:web:cesium:demo-models-readme:v1.0.0"
semantic_document_id: "kfm-web-cesium-demo-models-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:web:cesium:demo-models-readme:v1.0.0"
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

# Cesium Demo Models — README

## 📘 Overview

### Purpose

- Provide a **small, license-clean set of 3D demo models** for the KFM Cesium UI (local development, smoke tests, examples).
- Define **conventions** for adding/replacing models so the UI stays fast, reviewable, and governance-safe.

### Scope

| In Scope | Out of Scope |
|---|---|
| Small demo models (e.g., `.glb`), optional thumbnails, and per-model licensing/attribution | Authoritative domain datasets (those belong under `data/**` with STAC/DCAT/PROV) |
| Models used only as **UI fixtures** (icons/markers/demo buildings) | Large/production tilesets or heavy assets without an explicit review path |
| Deterministic, offline-friendly assets checked into repo | Any model requiring remote fetch at runtime (unless explicitly approved) |
| Clear provenance/attribution notes for third-party models | Anything with unclear rights, proprietary terms, or missing attribution |

### Audience

- **Primary:** Frontend contributors working on Cesium features and UI layers.
- **Secondary:** Reviewers validating licensing, performance budgets, and governance safety.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo)*
- **glTF / GLB:** Standard 3D model format; prefer `.glb` (binary) for distribution.
- **3D Tiles:** Streaming format for large geospatial 3D content (generally out of scope for this demo directory).
- **Attribution:** The minimal license + source information required to redistribute a model.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + constraints |
| UI/graph boundary invariant | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Arch | “No UI direct-to-graph reads” |
| Governance / ethics / sovereignty | `docs/governance/` | Governance | Applies to all repo content (including UI assets) |
| Cesium demo models (this area) | `web/cesium/assets/models/demo/` | Frontend | Demo-only assets for Cesium |

### Definition of done (for this document)

- [x] Front-matter complete + valid (`path` matches file location)
- [x] Conventions for adding models are explicit (format, naming, licensing)
- [ ] At least one demo model is present and loads in Cesium *(not confirmed in repo)*
- [ ] Reviewer confirms license + attribution files for all third-party assets
- [ ] Performance budgets documented and followed

## 🗂️ Directory Layout

### This document

- `path`: `web/cesium/assets/models/demo/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| UI (Cesium/Map) | `web/` | Front-end code + runtime assets |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) |
| Graph | `src/graph/` | Graph build/ingest + ontology bindings |
| Data / catalogs | `data/` | Domain data + STAC/DCAT/PROV evidence artifacts |
| Docs / standards | `docs/` | Governed documentation, templates, governance refs |

### Expected file tree for this sub-area

Recommended convention for demo assets (adjust if the UI already expects a different structure):

~~~text
web/cesium/assets/models/demo/
│
├── 📄 README.md
│
├── 📁 <model-id>/
│   ├── 🧩 model.glb                  # Preferred: single-file GLB
│   ├── 🖼️ preview.png                # Optional: thumbnail for docs / UI pickers
│   ├── 📄 LICENSE.md                 # Required if third-party (or a pointer to license)
│   └── 📄 ATTRIBUTION.md             # Required: source + author + link + notes
│
└── 📁 _notes/                        # Optional: internal notes, conversion logs, etc.
    └── 📄 CONVERSION_NOTES.md
~~~

## 🧭 Context

### Background

Cesium UI development often needs **repeatable, offline-friendly 3D models** to validate:

- rendering and lighting
- picking/interaction
- scale/orientation handling
- performance of model loading
- regression testing for UI changes

### Assumptions

- The KFM web application serves `web/**` assets as static files *(implementation details not confirmed in repo)*.
- Demo models are **non-authoritative**: they are UI fixtures, not evidence artifacts.

### Constraints / invariants

- **No UI direct-to-graph reads:** `web/` must never query Neo4j directly; all graph access is via `src/server/`.  
  *(This README restates the invariant; enforcement belongs in code review/CI.)*
- Models here must be **redistributable** and must not introduce license risk.
- Prefer models that are small enough to keep repo clones, CI, and local dev fast.

### Open questions

- Do we want a single “model registry” JSON for the UI to enumerate demo assets? *(not confirmed in repo)*
- Do we enforce file size/triangle count budgets in CI? *(not confirmed in repo)*

### Future extensions

- Add a lightweight validator step that checks:
  - presence of `LICENSE.md` / `ATTRIBUTION.md` for third-party models
  - max file size budget
  - optional glTF validation (tooling to be selected)

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[Demo model asset<br/>web/cesium/assets/models/demo/**] --> B[Web build / static serving<br/>web/**]
  B --> C[Cesium runtime loader<br/>UI scene]
  C --> D[User interaction<br/>inspect/pick/render]

  subgraph Boundary[Non-negotiable boundary]
    E[API layer<br/>src/server/**] --> C
    F[Graph DB<br/>Neo4j] --> E
  end
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant U as User
  participant UI as Web UI (Cesium)
  participant API as API (src/server)
  participant G as Graph (Neo4j)

  U->>UI: open demo scene
  UI->>UI: load local GLB from web assets
  UI->>API: fetch feature metadata (optional)
  API->>G: query (controlled)
  G-->>API: results
  API-->>UI: response
  UI-->>U: render + interact
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Source model (if third-party) | varies | external author/site | License reviewed; attribution captured |
| Converted model | `.glb` | conversion pipeline (tool not fixed) | Loads in Cesium; visually correct |
| Thumbnail (optional) | `.png` | manual capture | Clear, lightweight |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Demo model | `.glb` | `web/cesium/assets/models/demo/<model-id>/model.glb` | None (UI asset) |
| Attribution | `.md` | `.../<model-id>/ATTRIBUTION.md` | Required for third-party |
| License | `.md` | `.../<model-id>/LICENSE.md` | Required for third-party |
| Preview (optional) | `.png` | `.../<model-id>/preview.png` | Optional |

### Sensitivity & redaction

- Do **not** add models that encode sensitive locations, restricted cultural knowledge, or identifiable personal data.
- If a model’s meaning depends on a sensitive location (e.g., sacred site), it should not live here; follow governance pathways first.

### Quality signals

Recommended (soft) budgets for demo assets:

- **File size:** keep models small (aim for single-digit MB) unless explicitly justified.
- **Textures:** avoid huge textures; prefer reasonable resolutions.
- **Geometry:** avoid extremely high poly counts; simplify where possible.
- **Runtime:** ensure acceptable load time in local dev.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- **Not required** for demo UI assets.
- If a model becomes an **evidence artifact** (domain data), it must move into `data/**` and be cataloged with STAC in canonical locations.

### DCAT

- **Not required** for demo UI assets.
- Evidence products must have DCAT dataset records under the canonical catalog location.

### PROV-O

- **Not required** for demo UI assets.
- Minimum provenance for third-party models should be captured in `ATTRIBUTION.md` (source URL, author, license, and any modifications).

### Versioning

- This README uses semver in front-matter.
- If a model is replaced in a breaking way (different orientation/scale/appearance), treat it as a versioned change and note it in PR description.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Demo model assets | Local fixtures for Cesium development | Static file paths |
| Web UI (Cesium) | Loads models and renders scenes | Asset fetch + UI code |
| API boundary (`src/server/`) | Provides metadata, enforces redaction | REST/GraphQL (contracted) |
| Graph (Neo4j) | Stores semantics | Accessed via API only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| UI asset conventions (this doc) | `web/cesium/assets/models/demo/README.md` | Update semver on breaking convention changes |
| API contracts | `src/server/contracts/**` *(not confirmed in repo)* | Contract tests + semver |
| UI schema registry | `schemas/ui/**` *(not confirmed in repo)* | Schema validation |

### Extension points checklist (for future work)

- [ ] Add a model registry (if UI needs enumeration)
- [ ] Add CI size checks for `.glb`
- [ ] Add a “third-party asset checklist” gate (license + attribution)
- [ ] Add an optional glTF validation step

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Demo models may be used for **UI prototyping** only.
- Focus Mode content must remain **provenance-linked**; demo models do not substitute for evidence artifacts.

### Provenance-linked narrative rule

- If a Story Node references any visual/3D asset as evidence, it must cite a real evidence artifact (STAC/DCAT/PROV + graph context), not a demo model.

### Optional structured controls

- If a future UI requires a controlled list of allowed models, define a registry schema and validate it in CI *(not confirmed in repo)*.

## 🧪 Validation & CI/CD

### Validation steps

Minimum manual checks when adding a model:

- [ ] Model loads correctly in Cesium (no missing textures, correct scale/orientation)
- [ ] Third-party models include `LICENSE.md` and `ATTRIBUTION.md`
- [ ] Asset is reasonably sized for repo inclusion
- [ ] No sensitive/restricted content embedded in geometry/textures

### Reproduction

Commands for local dev depend on the repo’s web tooling *(not confirmed in repo)*.  
At minimum, confirm the model is accessible via the web app’s static asset path and render it in a simple Cesium scene.

### Telemetry signals (if applicable)

- Asset load time regressions
- Scene frame-rate regressions
- Bundle size increases (if assets are bundled rather than served statically)

## ⚖ FAIR+CARE & Governance

### Review gates

A reviewer should flag and require explicit review if a change includes:

- third-party assets without clear rights
- any content that could reveal sensitive locations via interaction/zoom
- large binary additions without justification

### CARE / sovereignty considerations

- Treat culturally sensitive representations as high-risk by default.
- Do not include assets that could enable inference of restricted locations or protected knowledge.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing
- Prohibited:
  - generating new policy
  - inferring sensitive locations

## 🕰️ Version History

| Version | Date | Summary | Author | PR / Issue |
|---|---:|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for Cesium demo models directory | TBD | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Master guide: `docs/MASTER_GUIDE_v12.md`

