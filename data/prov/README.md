---
title: "KFM PROV Directory Lineage Bundles"
path: "data/prov/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:data:prov:readme:v1.0.0"
semantic_document_id: "kfm-data-prov-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:prov:readme:v1.0.0"
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

# KFM PROV Directory Lineage Bundles

This directory is the **canonical repository location** for provenance outputs (lineage bundles) produced by KFM pipelines and catalog stages.

Path: `data/prov/`

## 📘 Overview

### Purpose

- Store **machine-readable provenance** for KFM transformations so that every output can be traced to its inputs, producing activity, and responsible agent.
- Provide provenance references for **audits**, graph provenance linkage, and Focus Mode “evidence” panels.
- Define the folder-level contract for what belongs in `data/prov/` and what does not.

### Scope

| In Scope | Out of Scope |
|---|---|
| PROV bundles for pipeline runs and/or catalog builds | Raw source data (belongs under `data/<domain>/raw/`) |
| Run-level provenance manifests and integrity metadata | Pipeline code (belongs under `src/pipelines/`) |
| Redaction/generalization notes that apply to provenance artifacts | STAC catalogs (belongs under `data/stac/`) |
| Links (by ID or stable reference) to STAC/DCAT outputs | DCAT catalogs (belongs under `data/catalog/dcat/`) |

### Audience

- Primary: pipeline maintainers, catalog maintainers
- Secondary: graph/ontology maintainers, API developers, UI/Focus Mode implementers, auditors/curators

### Definitions

- Link: `docs/glossary.md` (if present)
- Terms used in this doc:
  - **PROV-O**: W3C provenance model (entities, activities, agents)
  - **Bundle**: a serialized package of PROV statements for a single run or product
  - **run_id**: stable identifier for a pipeline/catal og activity
  - **agent**: the script/service/person responsible for the run (as captured in PROV)

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| PROV bundles | `data/prov/**` | Pipelines + catalog maintainers | Produced by runs/builds |
| PROV schema/profile | `schemas/prov/**` | Catalog maintainers | Validates PROV bundle shape |
| STAC catalogs | `data/stac/**` | Catalog stage | Outputs should reference provenance |
| DCAT records | `data/catalog/dcat/**` | Catalog stage | Outputs should reference provenance |
| Graph build imports | `data/graph/**` | Graph build | Should reference provenance identifiers |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Folder contract is clear: what belongs here, and what does not
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `data/prov/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | Source snapshots → transforms → normalized outputs |
| PROV outputs | `data/prov/` | Lineage bundles and run manifests |
| STAC catalogs | `data/stac/` | STAC collections + items |
| DCAT catalogs | `data/catalog/dcat/` | Dataset catalog records |
| Pipelines | `src/pipelines/` | ETL + transforms that emit PROV |
| Schemas | `schemas/` | JSON schemas (STAC/DCAT/PROV/UI/etc.) |
| Graph | `src/graph/` | Graph build + ontology bindings |
| API boundary | `src/server/` | Contracted access to graph + catalogs |
| UI | `web/` | React/Map clients |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts (provenance-linked) |

### Expected file tree for this sub-area

The exact sub-structure under `data/prov/` is **a repo-local convention**. If the repository already has an established convention, align this tree to match it and keep one canonical layout.

~~~text
📁 data/
└── 📁 prov/
    ├── 📄 README.md
    ├── 📁 runs/
    │   └── 📁 <run_id>/
    │       ├── 📄 prov.jsonld
    │       ├── 📄 manifest.json
    │       └── 📄 integrity.json
    └── 📁 products/
        └── 📁 <product_id>/
            └── 📄 prov.jsonld
~~~

## 🧭 Context

### Background

KFM’s architecture is contract-first and provenance-first. Provenance bundles are required so that:

- catalog artifacts (STAC/DCAT/PROV) remain machine-validatable,
- graph entities can carry references to the evidence that created them,
- Focus Mode can enforce “provenance-linked only” narrative behavior.

### Assumptions

- PROV outputs represent **Activities** (runs/builds), **Entities** (inputs/outputs), and **Agents** (pipelines/services/people).
- PROV bundles are treated as **build artifacts**: most changes should come from pipeline code/config, not hand edits.
- PROV artifacts validate against `schemas/prov/` (KFM-PROV profile).

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- UI consumes contracts via APIs and catalog endpoints (no direct graph dependency).
- Pipelines must not write STAC/DCAT/PROV artifacts into `docs/`.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical `run_id` format? | TBD | TBD |
| What serialization formats are accepted (JSON-LD vs PROV-JSON vs RDF)? | TBD | TBD |
| What fields are required by `schemas/prov/` in this repo? | TBD | TBD |

### Future extensions

- Add signing or checksum enforcement for bundles.
- Record container image/SBOM identifiers for reproducibility.
- Add “redaction justification” logging for sensitive/protected datasets.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL / Pipeline Run] --> P[PROV Bundle]
  A --> S[STAC Items + Collections]
  A --> D[DCAT Dataset Records]
  S --> G[Neo4j Graph]
  D --> G
  P --> G
  G --> API[API Boundary]
  API --> UI[React/Map UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

### Optional sequence diagram

~~~mermaid
sequenceDiagram
  participant UI
  participant API
  participant Graph
  participant Catalog as STAC/DCAT/PROV

  UI->>API: Focus query(entity_id)
  API->>Graph: fetch subgraph + provenance refs
  API->>Catalog: resolve STAC/DCAT/PROV IDs
  Graph-->>API: entities + evidence IDs
  Catalog-->>API: catalog + provenance payloads
  API-->>UI: narrative + citations + provenance panel data
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Pipeline run metadata | JSON | pipeline runtime / orchestrator | required fields present |
| Source references | URI/ID | `data/<domain>/raw/` + external refs | resolvable IDs |
| Output references | URI/ID | `data/<domain>/processed/` + catalogs | resolvable IDs |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| PROV bundle | JSON-LD (recommended) | `data/prov/**/prov.jsonld` | `schemas/prov/**` |
| Run manifest | JSON | `data/prov/**/manifest.json` | repo-defined |
| Integrity metadata | JSON | `data/prov/**/integrity.json` | repo-defined |

### Sensitivity & redaction

- Provenance must not leak restricted locations or sensitive fields.
- If an input/output is restricted, store **generalized identifiers** in PROV where required and ensure redaction actions are logged (without revealing protected details).
- Prefer API-layer redaction for user-facing access; keep internal lineage complete where policy permits.

### Quality signals

- Schema validation passes for all PROV bundles (`schemas/prov/**`).
- Referential integrity: referenced STAC/DCAT IDs resolve.
- No “orphan” data products without provenance linkage.

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: varies by domain.
- Items involved: outputs should carry stable IDs that can be referenced by provenance.
- Extensions: as defined by the repo’s STAC profile.

### DCAT

- Dataset identifiers: as defined by the repo’s DCAT profile.
- License mapping: align with dataset license fields.
- Contact/publisher mapping: align with DCAT records where applicable.

### PROV-O

- `prov:wasDerivedFrom`: link derived entities to their sources.
- `prov:wasGeneratedBy`: link outputs to the run activity.
- Activity/Agent identities: record the pipeline service/script identity and (where appropriate) the human/operator identity.

### Versioning

- Each run/build is a distinct provenance activity.
- When outputs are versioned, ensure predecessor/successor links are reflected consistently in catalogs and the graph.

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV | JSON + validator |
| Graph | Neo4j | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Graph + docs |
| Focus Mode | Contextual synthesis | Provenance-linked |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| PROV schemas | `schemas/prov/` | Semver + changelog |
| STAC schemas | `schemas/stac/` | Semver + changelog |
| DCAT schemas | `schemas/dcat/` | Semver + changelog |
| API contracts | `src/server/contracts/` | contract tests required |

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] DCAT: dataset record updated
- [ ] PROV: activity + agent identifiers recorded under `data/prov/`
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode should be able to show an “evidence / provenance” panel that includes:
  - PROV activity/run identifiers
  - linked STAC/DCAT evidence IDs
  - (optional) redaction/generalization notices

### Provenance-linked narrative rule

- Every claim shown in Focus Mode must trace to a dataset / record / asset ID.
- Predictive or AI-generated content must be opt-in and carry uncertainty metadata.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (stac/dcat/prov)
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol validation
~~~

### Telemetry signals

- Not applicable unless provenance validation results are logged as telemetry (repo-defined).

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that introduce new provenance fields, new sensitive datasets, or new redaction behaviors require human review.
- Any changes to `schemas/prov/**` require review by schema/catalog maintainers.

### CARE / sovereignty considerations

- Follow `docs/governance/SOVEREIGNTY.md` for handling culturally sensitive knowledge and protected locations.
- Do not store secrets/credentials in provenance artifacts.

### AI usage constraints

- PROV artifacts and this README must not be used to infer sensitive locations.
- AI transformation permissions/prohibitions must match the front-matter.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `data/prov/` | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
