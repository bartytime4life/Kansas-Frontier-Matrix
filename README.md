---
title: "Kansas Frontier Matrix — Repository README"
path: "README.md"
version: "v1.0.3"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.3"
semantic_document_id: "kfm-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:readme:v1.0.3"
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

# Kansas Frontier Matrix (KFM)

A geospatial + historical knowledge system with **governed data**, **catalogs (STAC/DCAT/PROV)**, **graph semantics (Neo4j)**, **contracted APIs**, and a **map/narrative UI**.

**Canonical pipeline ordering (non‑negotiable):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose

- Provide a single entry point for contributors and readers to understand:
  - what KFM is,
  - how the repository is organized,
  - where artifacts “live” across the pipeline,
  - and which governance/validation rules must not be broken.

### Scope

| In Scope | Out of Scope |
|---|---|
| Repository orientation + canonical pipeline + directory layout + contribution pointers | Full subsystem implementations, deployment specifics, and domain-specific dataset documentation (see domain READMEs + subsystem docs) |

### Audience

- Primary: maintainers and contributors (data, catalog, graph, API, UI, narrative).
- Secondary: reviewers (governance/ethics/sovereignty), historians/editors, external collaborators.

### Definitions

- Glossary: `docs/glossary.md` *(not confirmed in repo — add or repair link if glossary lives elsewhere)*
- Terms used in this doc:
  - **Domain pack**: the minimal governed components that let a domain participate in the pipeline (raw inputs + transforms + catalogs + mappings + validations + docs).
  - **Contract artifact**: machine-validated schema/spec (JSON Schema, OpenAPI, GraphQL SDL, UI registry schema).
  - **Evidence artifact**: catalog + provenance outputs consumed downstream (STAC/DCAT/PROV and derived products).
  - **Story Node**: a provenance-linked narrative artifact designed to render in the UI.
  - **Focus Mode**: an immersive UI view that consumes provenance-linked context only.

### Start here

Recommended reading order (paths are expected; if missing, treat as **not confirmed in repo** and repair links):

1) `docs/MASTER_GUIDE_v12.md` — system + pipeline source of truth (includes extension matrix + invariants)  
2) `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` — canonical roots + minimum contract set + readiness gates *(draft; “if adopted”)*  
3) `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` — near-term roadmap + vertical-slice checklist *(draft)*  
4) `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` — end-to-end architecture vision *(draft)*  
5) Example domain modules (end-to-end integration patterns):
   - `docs/data/historical/land-treaties/README.md`
   - `docs/data/air-quality/README.md`
   - `data/soils/sda/README.md`
6) `docs/README.md` — documentation index *(not confirmed in repo)*  
7) `data/README.md` — data lifecycle + domain layout *(not confirmed in repo)*  
8) `schemas/README.md` — schema registry + minimum contract set *(not confirmed in repo)*  
9) `src/README.md` — subsystem boundaries (pipelines/graph/server) *(not confirmed in repo)*  
10) `mcp/README.md` — experiments, run manifests, model cards, SOPs *(not confirmed in repo)*  
11) `.github/workflows/README.md` — CI gates + validation expectations *(not confirmed in repo)*

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline + invariants + extension matrix |
| v13 redesign blueprint (draft; if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Proposed repo restructuring + readiness gates |
| Next stages blueprint (draft) | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + vertical-slice checklist |
| Full architecture vision (draft) | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end architecture context |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative | Focus Mode narrative artifacts |
| API Contract Extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| Land Treaties module README | `docs/data/historical/land-treaties/README.md` | Historical Data | Example governed domain module integrating full pipeline |
| Air Quality domain notes | `docs/data/air-quality/README.md` | Environmental Data | Example domain notes aligning ETL + catalogs + graph + API + UI + Story |
| Soils SDA guide | `data/soils/sda/README.md` | Environmental Data | Example deterministic ingest guide with validation checklist |

### Definition of done (for this README)

- [ ] Front-matter complete + valid (`path: README.md`)
- [ ] H2 sections match the Universal Doc heading set (no extra H2 headings)
- [ ] Canonical pipeline + invariants stated clearly (pipeline order, API boundary, provenance rules)
- [ ] Canonical roots described (and marked if “not confirmed in repo”)
- [ ] Validation/CI expectations stated (commands may be placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Footer refs preserved (governance + templates + architecture pointers)

---

## 🗂️ Directory Layout

### This document

- `path`: `README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Docs | `docs/` | Canonical governed docs + templates + standards + architecture |
| Data domains + staging | `data/` | Raw/work/processed datasets + domain packs (if adopted) |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC, DCAT, PROV lineage bundles |
| Graph | `src/graph/` + `data/graph/` | ontology-governed ingest + import fixtures |
| Pipelines | `src/pipelines/` | deterministic transforms; outputs written under `data/**` |
| API boundary | `src/server/` | contracted access layer (REST/GraphQL); redaction + provenance refs |
| Frontend | `web/` | React/MapLibre UI; no direct graph access |
| Schemas | `schemas/` | JSON Schemas for catalogs, story nodes, UI registries, telemetry |
| Story Nodes | `docs/reports/story_nodes/` | draft/published narratives + assets |
| MCP / experiments | `mcp/` | experiment logs, run manifests, model cards, SOPs |
| CI | `.github/` | workflows, security policy, issue templates |
| Tests | `tests/` | unit + integration + contract tests |
| Tooling | `tools/` | validators, scripts, repo lint |
| Releases | `releases/` | release manifests/SBOMs/attestations/telemetry snapshots (if used) |

### Repository navigation (where to look first)

| Area | Open first | Why |
|---|---|---|
| Docs | `docs/MASTER_GUIDE_v12.md` | Canonical rules + invariants |
| Architecture | `docs/architecture/` | Blueprints, ADRs, diagrams |
| Data | `data/` | Staging, catalogs, provenance bundles |
| Schemas | `schemas/` | Validation contracts |
| Source | `src/` | Implementation boundaries |
| UI | `web/` | Map layers + Focus Mode experience |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts for Focus Mode |
| MCP | `mcp/` | Experiments + run manifests + model cards (if present) |

### Common contribution patterns (what goes where)

| You are adding/changing… | Put it here | Also update / validate |
|---|---|---|
| New dataset / domain inputs | `data/raw/**` or domain-pack `data/<domain>/raw/**` | STAC/DCAT/PROV + PROV activity; sovereignty scans where applicable |
| Domain governance docs (sources, classification, QA) | `data/<domain>/governance/` *(or `docs/data/<domain>/...` — choose one canonical home and link it)* | Ensure classification propagates into catalogs/API/UI |
| ETL or transforms | `src/pipelines/<domain>/` (or `src/pipelines/common/`) | Determinism (stable IDs) + run logs + provenance |
| Catalog schemas/profiles | `schemas/{stac,dcat,prov}/` | Schema validation + changelog/semver (if adopted) |
| Graph ingest/mappings | `src/graph/` and `data/graph/` | Ontology constraints + import fixtures |
| API endpoints/contracts | `src/server/` and `src/server/contracts/` *(or legacy paths — not confirmed in repo)* | Contract tests + redaction rules at boundary |
| UI layers / registry entries | `web/` (and UI schemas in `schemas/ui/`) | UI registry schema validation + governance gates |
| Story Nodes | `docs/reports/story_nodes/` | Story Node schema validation + provenance-linked citations |
| Experiments / evaluation artifacts | `mcp/` | Keep outputs referenced (not duplicated); record run IDs + pointers to evidence |
| Releases / packaged artifacts | `releases/<tag>/` | SBOM/manifest/attestation pointers + integrity hashes |

### Expected file tree (repo root)

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

> Some directories may not exist yet (**not confirmed in repo**). If a canonical root is missing, treat it as a gap and repair/implement it per the Master Guide + blueprints.

---

## 🧭 Context

### Background

KFM’s core design goal is an **evidence-first, provenance-linked** system where every downstream view (including narrative Focus Mode) remains traceable back to catalog + provenance artifacts.

### Assumptions

- Canonical pipeline ordering is preserved.
- Schema/contracts are treated as first-class artifacts.
- Pipelines are deterministic and reproducible.

### Constraints / invariants

- **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode** is preserved.
- **Frontend consumes contracts via APIs (no direct graph dependency).**
- **Focus Mode only presents provenance-linked content (no uncited facts).**
- Any AI-generated/predictive content (if any) is opt-in, clearly labeled, and includes uncertainty/confidence metadata.
- Classification/sensitivity must **propagate forward**: no output can be less restricted than any input in its lineage.
- For sensitive/restricted contexts (including culturally sensitive materials): never publish raw coordinates or other “re-identifying” spatial precision in public artifacts; generalize/mask as required.
- Prefer meaningful runs to produce (or link to) a PROV activity bundle under `data/prov/**`; keep `mcp/runs/**` as pointers/IDs, not duplicated provenance payloads (if `mcp/` is present).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which paths are currently implemented vs “target layout”? | TBD | TBD |
| Which data layout is canonical per domain: stage-first (`data/raw/<domain>`) vs domain-pack (`data/<domain>/raw`)? | TBD | TBD |
| Are there legacy duplicate roots (e.g., `src/api/` vs `src/server/`, `src/map/` vs `web/`), and what is the migration/deprecation plan? | TBD | TBD |
| Where is the canonical glossary located (and is it complete)? | TBD | TBD |
| Which CI validators exist today (Markdown protocol, schema lint, contract tests, link checks)? | TBD | TBD |
| Story Nodes: confirm current state of `docs/reports/story_nodes/` (draft/published), and whether any legacy path still exists. | TBD | TBD |
| Are domain naming conventions standardized (e.g., `air-quality` vs `air_quality`)? | TBD | TBD |

### Future extensions

- New domains built as domain packs (raw + ETL + catalogs + graph + API + UI + Story Node).
- New evidence products treated as catalog assets and linked into Focus Mode.
- Expanded Story Node types (schema-validated; provenance-linked).
- Composite CI actions / reproducibility kits (if adopted) to standardize validation and regression testing.

---

## 🗺️ Diagrams

### System / dataflow diagram (canonical roots)

~~~mermaid
flowchart LR
  R["Raw sources — data/raw/** or data/&lt;domain&gt;/raw/**"] --> A["ETL — src/pipelines/**"]
  A --> B["STAC/DCAT/PROV — data/stac · data/catalog/dcat · data/prov"]
  B --> C["Graph — src/graph + data/graph"]
  C --> D["API boundary — src/server + contracts"]
  D --> E["UI — web/"]
  E --> F["Story Nodes — docs/reports/story_nodes"]
  F --> G["Focus Mode — provenance-linked"]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI (web/)
  participant API as API (src/server)
  participant Graph as Graph (Neo4j via src/graph)
  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs (with redaction rules)
  Graph-->>API: context bundle + evidence references
  API-->>UI: contracted payload (narrative + citations + audit flags)
~~~

---

## 📦 Data & Metadata

### Data lifecycle and staging patterns

KFM supports a lifecycle concept of **raw → work → processed**, with catalogs + provenance emitted as first-class evidence.

Two patterns may exist (choose **one** per domain; document it in the domain README):

#### Pattern A — stage-first (baseline)

~~~text
📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
└── 📁 <domain>/                # domain module home (docs/governance/runbooks; recommended)
    ├── 📁 governance/
    └── 📄 README.md
~~~

#### Pattern B — domain-pack (draft / if adopted)

~~~text
📁 data/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
└── 📁 <domain>/
    ├── 📁 raw/
    ├── 📁 work/
    ├── 📁 processed/
    ├── 📁 governance/           # recommended
    └── 📄 README.md
~~~

> Do not mix stage-first and domain-pack staging **within the same domain** without an explicit migration note.

### Domain expansion pattern (domain pack checklist)

When formalizing a domain to “plug into KFM”, the expected minimal components include:

- Raw inputs (and/or ingestion scripts) + source manifests
- ETL/processing code (deterministic; stable IDs; reproducible)
- STAC/DCAT/PROV outputs (schema-valid; provenance-complete)
- Graph mappings (ontology-aligned; stable labels/edges)
- API endpoints/queries (contracted; redaction enforced)
- UI layer configs (registry-driven; a11y + governance gates)
- At least a draft Story Node / narrative use-case

See the Master Guide extension matrix and the Next Stages blueprint for how “simple datasets” vs “analysis products” change what layers must be touched.

### Upstream source registries (recommended)

- Represent upstream sources as per-source JSON manifests under `data/sources/**` (or a repo-approved equivalent).
- Minimum fields are expected to cover: `id`, `title`, `description`, `license`, `providers`, `assets`, `spatial`, `temporal`, and `provenance` pointers.
- Pipeline runs should reference these manifests in PROV bundles.

### Provenance placement and run pointers

- Prefer meaningful runs to produce (or link to) a PROV activity bundle under `data/prov/**`.
- If `mcp/runs/**` exists, it should store run IDs + pointers to provenance/evidence, not duplicated provenance payloads.
- If `releases/<tag>/` exists, treat it as packaging (manifest/SBOM/attestation) that references canonical evidence artifacts.

---

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product

For each dataset or evidence product:

- STAC Collection + Item(s)
- DCAT dataset/distribution record (minimum: title/description/license/keywords)
- PROV bundle describing lineage (sources + run/activity identifiers)
- Version lineage links reflected in catalogs and (where applicable) in the graph

### Mapping expectations (recommended)

- Each **STAC Collection** ↔ one `dcat:Dataset` (or equivalent DCAT dataset record).
- Each export bundle (or publishable artifact) ↔ one `dcat:Distribution`.
- PROV bundles should include:
  - `prov:Entity` (Collections, Items, exported files)
  - `prov:Activity` (ETL jobs, OCR runs, geometry generalization, validation)
  - `prov:Agent` (pipelines, maintainers, partner institutions)

### Identifier linkage expectation

Graph nodes and API payloads should reference:
- STAC Item IDs
- DCAT dataset IDs
- PROV activity IDs

This enables Focus Mode to resolve “what is this data?” into a traceable lineage bundle.

### Sensitive geometry and redaction

- Public catalogs should not publish raw sensitive geometries (restricted or culturally sensitive sites).
- When needed, STAC Items may use generalized geometry (centroids/coarse polygons) or omit geometry in public outputs, while preserving provenance and access-controlled internal references.

---

## 🧱 Architecture

### Subsystem contracts (what must exist per subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation outputs | deterministic, replayable |
| Catalogs | schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable IDs, labels, edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story / Focus Mode | provenance-linked context bundle | no uncited facts |

### API boundary rule (non-negotiable)

- The UI does **not** connect to Neo4j directly.
- The API boundary mediates access and enforces provenance + redaction/generalization rules.

### Contract locations (expected)

| Contract type | Canonical location | Notes |
|---|---|---|
| Governed doc templates | `docs/templates/` | Universal / Story Node / API Contract Extension |
| JSON Schemas | `schemas/**` | STAC/DCAT/PROV/story/UI/telemetry |
| API contracts | `src/server/contracts/**` | Legacy `src/api/**` may exist (*not confirmed in repo*) |
| UI registry schemas | `schemas/ui/**` | Registry-driven map layers and Focus Mode inputs |
| Provenance bundles | `data/prov/**` | Prefer one bundle per meaningful run |

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Story Nodes may reference local assets (images/excerpts) with attribution, but the source-of-truth remains catalog + provenance artifacts.

### Focus Mode rule (non-negotiable)

- Focus Mode must only consume **provenance-linked** content.
- Any predictive/AI content must be clearly marked, opt-in, and include uncertainty metadata.

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present**: if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid**: schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable**: optional roots absent → skip without failing the overall pipeline.

### Minimum checks (recommended)

- [ ] Markdown protocol checks (for governed docs)
- [ ] Schema validation (STAC/DCAT/PROV, story nodes, UI registries, telemetry if present)
- [ ] Graph integrity checks (if graph changes)
- [ ] API contract tests (`src/server/contracts/**`)
- [ ] UI registry checks (layer registry schema)
- [ ] Link integrity checks for docs (if tooling exists)
- [ ] Security, PII, sovereignty checks (as applicable)

### Repo lint invariants (recommended gates)

- No YAML front-matter in executable code files (split into docs + metadata).
- No duplicate canonical homes for the same subsystem without explicit deprecation markers.
- No typo-paths (e.g., `README.me`).
- No mixed doc/code artifacts (e.g., scripts under `docs/` that contain runnable code).

### Local reproduction (placeholders)

~~~bash
# NOTE: commands are placeholders; replace with repo-approved tooling.

# 1) validate schemas (STAC/DCAT/PROV/story nodes/UI)
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol checks
# 4) run sovereignty/PII scans (where applicable)

# make validate-schemas
# make test
# make lint-docs
# make scan-governance
~~~

### Optional telemetry signals (if telemetry is implemented)

| Signal | Why it matters |
|---|---|
| `classification_assigned` | proves classification decisions were recorded |
| `redaction_applied` | proves masking/generalization is auditable |
| `promotion_blocked` | proves unsafe promotion was prevented |
| `catalog_published` | proves catalog publication is tracked |
| `focus_mode_redaction_notice_shown` | proves UI disclosure for redaction |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Changes that typically require elevated review:

- Adding new sensitive layers (restricted locations, cultural knowledge, PII, etc.)
- Introducing/changing AI-generated narrative behavior visible to users
- Adding new external data sources
- Adding new public-facing endpoints
- Changing classification/sensitivity for any artifact
- Adding UI layers that could reveal sensitive locations by interaction/zoom

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- Use generalization/redaction for restricted locations.
- Ensure sensitive assets (images/docs) follow review gates before publication.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not imply prohibited actions (e.g., inferring sensitive locations).
- User-facing AI outputs (if any) must remain evidence-led, provenance-linked, and clearly labeled.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial repository README (governed-doc format) | TBD |
| v1.0.1 | 2025-12-23 | Added repo navigation + clarified canonical roots/CI behavior; aligned wording with contract-first guidance | TBD |
| v1.0.2 | 2025-12-24 | Added Next Stages + Full Vision references; clarified data layout options; tightened doc/code separation | TBD |
| v1.0.3 | 2025-12-26 | Aligned H2 headings to Universal template; confirmed blueprint references; clarified staging vs domain-pack patterns; added provenance/run-pointer guidance | TBD |

---

Footer refs (do not remove):
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Full architecture vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API Contract Extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
