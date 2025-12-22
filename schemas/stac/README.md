---
title: "Schemas — STAC (JSON Schema + KFM constraints)"
path: "schemas/stac/README.md"
version: "v1.0.0"
last_updated: "2025-12-22"
status: "draft"
doc_kind: "Guide"
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

doc_uuid: "urn:kfm:doc:schemas:stac:readme:v1.0.0"
semantic_document_id: "kfm-schemas-stac-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:stac:readme:v1.0.0"
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

# Schemas — STAC

## 📘 Overview

### Purpose
- Define what belongs in `schemas/stac/` and how these schemas are used to validate STAC artifacts produced by the KFM Catalog stage.
- Establish directory conventions for **STAC JSON Schemas** plus any **KFM-specific constraints/overlays** used by validators and CI.

### Scope

| In Scope | Out of Scope |
|---|---|
| JSON Schema files for STAC objects (Item, Collection, Catalog if used) | The STAC catalog outputs themselves (`data/stac/**`) |
| KFM overlay constraints that narrow/standardize STAC for KFM | ETL implementations and transformations (`src/pipelines/**`) |
| Guidance for validation, versioning, and change control for STAC schemas | API response contracts (OpenAPI/GraphQL) |
| Pointers to related standards docs (KFM-STAC profile, if present) | UI layer styling/registry schemas (`schemas/ui/**`) |

### Audience
- Primary: catalog maintainers, data engineers, CI maintainers.
- Secondary: domain contributors producing STAC Collections/Items.

### Definitions
- **STAC**: SpatioTemporal Asset Catalog JSON objects (Items, Collections, Catalogs) that describe assets.
- **JSON Schema**: Machine-validated contract for a JSON document shape and constraints.
- **KFM constraints/overlays**: Additional rules beyond baseline STAC schemas to enforce KFM’s contracts (stable IDs, required metadata fields, controlled extensions, etc.).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline ordering and profiles |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture maintainers | Establishes contracts-first approach |
| KFM STAC profile | `docs/standards/KFM_STAC_PROFILE.md` | Standards maintainers | Referenced as canonical profile location (may be placeholder) |
| STAC outputs | `data/stac/collections/**`, `data/stac/items/**` | Catalog pipeline | Consumers: Graph, API, UI |
| DCAT outputs | `data/catalog/dcat/**` | Catalog pipeline | Links dataset-level metadata |
| PROV outputs | `data/prov/**` | Pipeline + catalog | Lineage and auditability |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Directory intent + “what lives here” is explicit
- [ ] Validation expectations are documented and repeatable
- [ ] Versioning expectations for schema evolution are documented
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `schemas/stac/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/**` | Raw/work/processed domain data inputs to catalogs |
| STAC outputs | `data/stac/**` | STAC Collections + Items produced by catalog build |
| Documentation | `docs/**` | Canonical governed docs and templates |
| Pipelines | `src/pipelines/**` | ETL + catalog build code |
| Schemas | `schemas/**` | JSON schemas and contract artifacts |
| Graph | `src/graph/**` + `data/graph/**` | Ontology bindings + import artifacts |
| API boundary | `src/server/**` | Contracted access layer (REST/GraphQL) |
| UI | `web/**` | Map + narrative clients consuming APIs |

### Expected file tree for this sub-area
~~~text
📁 schemas/
└── 📁 stac/
    ├── 📄 README.md
    ├── 📄 <stac-catalog.schema.json>
    ├── 📄 <stac-collection.schema.json>
    ├── 📄 <stac-item.schema.json>
    ├── 📁 extensions/
    │   └── 📄 <extension>.schema.json
    └── 📁 kfm/
        └── 📄 <kfm-overlay>.schema.json
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline places STAC/DCAT/PROV catalogs immediately after ETL. STAC outputs are then consumed downstream by the graph, APIs, and the UI. Schema validation provides a contract boundary so that producers and consumers evolve independently, and so CI can fail deterministically on invalid catalog artifacts.

### Assumptions
- The repository uses the `stac_profile` declared in front-matter: `KFM-STAC v11.0.0`.
- Catalog build emits STAC artifacts into `data/stac/**` (Collections and Items).
- Schema validation is enforced in CI when schemas are present.

### Constraints / invariants
- The canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- UI does not read Neo4j directly; **API boundary** is the access layer for graph content and catalog references.
- Pipelines do not write STAC/DCAT/PROV artifacts into `docs/` (catalogs are evidence artifacts under `data/`).
- Schema changes are treated as contract changes and require explicit versioning and review.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Which STAC extensions are officially supported by `KFM-STAC v11.0.0` for KFM domains? | Standards maintainers | TBD |
| Should KFM store “baseline STAC” schemas and “KFM overlays” separately (recommended: `core/` vs `kfm/`), or only overlays? | Catalog maintainers | TBD |
| What is the canonical validator tooling and where are the commands documented (`tools/`, `src/pipelines/`, CI workflow)? | CI maintainers | TBD |
| Where is the schema changelog tracked for semver bumps (`schemas/stac/CHANGELOG.md` vs global `CHANGELOG.md`)? | Core maintainers | TBD |

### Future extensions
- Add explicit schema bundles per domain (if domain-specific STAC constraints are needed).
- Add shape/constraint equivalents (e.g., SHACL) if RDF/DCAT mappings require it.
- Add test fixtures under `tests/fixtures/stac/**` to lock in contract behavior.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC Collection | JSON | `data/stac/collections/**` | JSON Schema in `schemas/stac/**` |
| STAC Item | JSON | `data/stac/items/**` | JSON Schema in `schemas/stac/**` |
| STAC Catalog | JSON | If used by catalog build | JSON Schema in `schemas/stac/**` |
| Extension fields | JSON | Within Items/Collections | Extension schema or KFM overlay schema |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Validation report | text/json | CI logs (canonical location TBD) | Schema validator config |
| “Pass” STAC artifacts | JSON | `data/stac/**` | `schemas/stac/**` |

### Sensitivity & redaction
- If STAC geometries or asset metadata could reveal restricted locations or culturally sensitive knowledge:
  - Prefer generalization at data production time (ETL/catalog build),
  - Enforce redaction/generalization at the API boundary,
  - Require governance review before publishing related Story Nodes.

### Quality signals
- Schema validation passes for all `data/stac/**` artifacts.
- No broken internal links between Collections and Items (IDs/hrefs resolve under catalog conventions).
- Stable identifiers across rebuilds for unchanged source inputs (deterministic catalog build).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: `data/stac/collections/**`
- Items involved: `data/stac/items/**`
- Extension(s): defined by `docs/standards/KFM_STAC_PROFILE.md` (if populated)

### DCAT
- Dataset identifiers: `data/catalog/dcat/**` (dataset-level metadata that should correspond to STAC Collections where applicable)
- License mapping: recorded at DCAT layer; STAC should not contradict it

### PROV-O
- `prov:wasDerivedFrom`: STAC Items/Collections should be traceable to raw/work/processed sources via PROV bundles
- `prov:wasGeneratedBy`: catalog build activity (run) should be recorded under `data/prov/**`

### Versioning
- Schemas are treated as contract artifacts: use semantic versioning for schema changes and maintain a changelog (location TBD).
- When schema changes require breaking changes in producers/consumers, coordinate via contract tests and (if applicable) API versioning.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | `src/pipelines/**` + run manifests |
| Catalogs | STAC/DCAT/PROV generation | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` |
| Schemas | Contract validation | `schemas/**` (this folder for STAC) |
| Graph | Neo4j ingest + ontology | `src/graph/**` + `data/graph/**` |
| APIs | Serve contracts | `src/server/**` |
| UI | Map + narrative | API calls + catalog endpoints |
| Story Nodes | Curated narrative | `docs/reports/story_nodes/**` |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| STAC JSON Schemas | `schemas/stac/**` | Semver + changelog (location TBD) |
| STAC outputs | `data/stac/**` | Must validate against schemas |
| DCAT outputs | `data/catalog/dcat/**` | Must validate against DCAT schemas |
| PROV outputs | `data/prov/**` | Must validate against PROV profile |

### Extension points checklist
- [ ] STAC: new collection(s) and item(s) defined, schema-validated
- [ ] DCAT: dataset record created/updated and aligned with STAC
- [ ] PROV: activity and agent identifiers recorded for catalog build
- [ ] Graph: STAC/DCAT/PROV IDs referenced on graph nodes
- [ ] API: endpoints expose catalog references via contract
- [ ] UI: layers or narratives reference evidence by ID (no “unsourced narrative”)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode views should be able to cite/resolve evidence by:
  - STAC Item IDs,
  - Collection IDs,
  - PROV activity IDs.

### Provenance-linked narrative rule
- Story Nodes must reference evidence IDs (STAC/DCAT/PROV) for every claim they surface.
- STAC assets referenced in narratives must include provenance and attribution metadata consistent with governance rules.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (this README)
- [ ] Schema validation (STAC artifacts vs `schemas/stac/**`)
- [ ] Link/integrity checks (Collections ↔ Items, IDs/hrefs)
- [ ] Security and sovereignty checks (as applicable to sensitive layers)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate STAC JSON documents against schemas
# <validator> --schema schemas/stac/<stac-item.schema.json> data/stac/items/**/*.json
# <validator> --schema schemas/stac/<stac-collection.schema.json> data/stac/collections/**/*.json

# 2) run repo lint / markdown protocol checks
# <repo-lint-command>

# 3) run contract tests (if schemas are coupled to API behavior)
# <test-command>
~~~

## ⚖ FAIR+CARE & Governance

### Governance review triggers
- Adding or changing schema requirements that may expose new fields in public outputs
- Introducing new STAC extensions that carry sensitive geometry or attributes
- Adding new external data sources that flow into STAC Items/Collections

### CARE / sovereignty considerations
- Document and enforce redaction/generalization rules for any restricted locations before publishing catalog outputs or Story Nodes.

### AI usage constraints
- This document’s front-matter declares allowed AI transforms; prohibited transforms include generating new policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for `schemas/stac/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

