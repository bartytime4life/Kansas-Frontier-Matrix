---
title: "KFM Data Ops — README"
path: "docs/data-ops/README.md"
version: "v0.1.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data-ops:readme:v0.1.0"
semantic_document_id: "kfm-data-ops-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data-ops:readme:v0.1.0"
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

# KFM Data Ops — README

## 📘 Overview

### Purpose
- Define **DataOps conventions** for the KFM repository: data lifecycle (raw → work → processed), catalog outputs (STAC/DCAT/PROV), provenance/versioning, and validation gates.
- Provide a single place to find *where things go* and *what must be updated* when adding or changing data.

### Scope
| In Scope | Out of Scope |
|---|---|
| Data-domain folder conventions (`data/<domain>/...`) | Provisioning infrastructure / cloud resources |
| ETL run determinism, idempotency, logging expectations | Detailed API implementation (see API docs/source) |
| Catalog outputs: STAC, DCAT, PROV | UI implementation details |
| Data release validation checklist and CI expectations | Ontology deep dives (beyond contract boundaries) |
| Dataset versioning + lineage in catalogs/graph | Narrative authoring guidelines (beyond evidence rules) |

### Audience
- Primary: Data engineers, pipeline maintainers, and reviewers responsible for dataset ingestion and catalog production.
- Secondary: Graph/API maintainers who consume catalog outputs, and contributors adding new data sources.

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Data domain**: A top-level dataset area mapped to `data/<domain>/...`.
  - **raw/work/processed**: Stages of the data lifecycle; `work/` is intermediate, `processed/` is normalized output.
  - **STAC / DCAT / PROV-O**: Standards-based metadata and provenance artifacts produced from processed data.
  - **Deterministic + idempotent ETL**: Same input/config yields same output; re-running does not duplicate outputs.
  - **Contract test**: Automated check that an artifact (schema, API, graph, doc) still conforms to published contracts.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering + contracts |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Required structure for governed docs |
| Data domains | `data/` | DataOps | Domain lifecycle folders (`raw/`, `work/`, `processed/`) |
| STAC catalogs | `data/stac/collections/` + `data/stac/items/` | DataOps | Canonical STAC JSON outputs |
| DCAT catalogs | `data/catalog/dcat/` | DataOps | Canonical DCAT outputs |
| PROV provenance | `data/prov/` | DataOps | Canonical provenance outputs |
| Pipeline code | `src/pipelines/` | DataOps | `etl/` + `catalog/` sub-systems |
| Schema contracts | `schemas/` | Maintainers | JSON Schemas for catalogs/telemetry/etc. |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory rules match canonical repo placement guidance
- [ ] Data lifecycle + catalog responsibilities are explicit and actionable
- [ ] Validation steps are listed and repeatable (local + CI)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/data-ops/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains (lifecycle) | `data/<domain>/{raw,work,processed}/` | Raw inputs, intermediate work products, normalized outputs |
| STAC | `data/stac/collections/` + `data/stac/items/` | STAC Collections + Items emitted by catalog builders |
| DCAT | `data/catalog/dcat/` | DCAT dataset records (catalog-level metadata) |
| PROV | `data/prov/` | Provenance bundles (activities, agents, entities) |
| Data docs | `docs/data/<domain>/` | Source notes, assumptions, field dictionaries, limitations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL and catalog build code + governed docs |
| Graph ingestion | `src/graph/` + `docs/graph/` | Load from catalogs into Neo4j; ontology + migrations |
| Schemas | `schemas/` | JSON Schemas + validation artifacts (STAC/DCAT/telemetry, etc.) |
| Governance | `docs/governance/` | Ethics, sovereignty, review gates |
| CI workflows | `.github/workflows/` | CI gates enforcing doc/schema/tests (if present) |

### Expected file tree for this sub-area
~~~text
📁 docs/
└── 📁 data-ops/
    ├── 📄 README.md
    ├── 📁 runbooks/                 (planned; not confirmed in repo)
    │   ├── 📄 RUNBOOK__NEW_DATASET.md
    │   ├── 📄 RUNBOOK__REBUILD_CATALOGS.md
    │   └── 📄 RUNBOOK__BACKFILL_GRAPH.md
    └── 📁 checklists/               (planned; not confirmed in repo)
        └── 📄 CHECKLIST__DATA_RELEASE.md
~~~

## 🧭 Context

### Background
KFM is a pipeline-oriented system where data must move through a **fixed sequence of stages** with well-defined handoffs. DataOps exists to keep those handoffs reliable:

- **ETL produces deterministic, logged, idempotent outputs** (traceable transformations, repeatable runs).
- **Catalog builders emit standards-based metadata artifacts** (STAC/DCAT/PROV) instead of pushing raw data directly into the graph.
- **Graph ingestion consumes catalogs**, and **APIs** are the boundary for UI consumption (no direct UI → graph coupling).

#### Standard workflows (summary)
1. **Add/refresh a dataset**
   - Place source inputs under the correct `data/<domain>/raw/`.
   - Run ETL to produce `data/<domain>/processed/` outputs (plus any intermediates in `work/`).
   - Build/refresh STAC/DCAT/PROV outputs.
   - Run schema + integrity validation locally (and ensure CI passes).
2. **Version a dataset**
   - Produce new processed outputs, update catalogs, and add explicit predecessor/successor links.
3. **Deprecate a dataset**
   - Mark as deprecated in catalog metadata, preserve provenance, and keep old assets accessible unless governance requires removal.

### Assumptions
- Each data domain follows the lifecycle folder convention: `raw/`, `work/`, `processed/`.
- Catalog outputs are treated as **first-class, versioned artifacts**: STAC, DCAT, and PROV.
- CI enforces documentation protocol checks, and (where configured) schema validation for catalog outputs.
- Sensitive or culturally restricted data may require generalization, omission, or restricted handling per governance.

### Constraints / invariants
- **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** is preserved.
- **Frontend consumes contracts via APIs** (no direct graph dependency).
- ETL transformations are **deterministic, logged (with hashes), and idempotent**.
- Any new dataset/change must maintain:
  - Schema-valid STAC/DCAT/PROV
  - Stable identifiers (or explicit version lineage links where identifiers change)

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical run log format + storage path for ETL and catalog builds? | TBD | TBD |
| Which domains currently exist and who owns each domain’s docs + schemas? | TBD | TBD |
| Which CI workflows run STAC/DCAT/PROV schema + integrity validation locally? | TBD | TBD |

### Future extensions
- Add domain-specific runbooks under `docs/data-ops/runbooks/` (new dataset, refresh, deprecation).
- Add a reusable release checklist under `docs/data-ops/checklists/`.
- Add automated “diff” reports for catalog changes (new/changed/removed Items, licenses, extents).

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

### Optional: dataset lifecycle (raw → processed → catalogs → graph)
~~~mermaid
flowchart TD
  S[Source inputs] --> R[data/<domain>/raw/]
  R --> W[data/<domain>/work/]
  W --> P[data/<domain>/processed/]
  P --> STAC[data/stac/items + collections]
  P --> DCAT[data/catalog/dcat]
  P --> PROV[data/prov]
  STAC --> G[Neo4j Graph ingest]
  DCAT --> G
  PROV --> G
~~~

### Optional: sequence diagram (dataset refresh)
~~~mermaid
sequenceDiagram
  participant Dev as DataOps
  participant ETL as ETL Pipeline
  participant Cat as Catalog Builder
  participant Val as Validators
  participant Graph as Graph Loader

  Dev->>ETL: Run domain ETL (raw → processed)
  ETL-->>Dev: processed outputs + logs
  Dev->>Cat: Build STAC/DCAT/PROV
  Cat-->>Dev: catalog artifacts
  Dev->>Val: Validate docs + schemas + integrity
  Val-->>Dev: pass/fail report
  Dev->>Graph: Ingest catalogs into Neo4j
  Graph-->>Dev: ingest summary + audit flags
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source files / URLs | PDF, text, CSV, imagery, web links, geospatial files | External sources or contributor uploads | Record license + source metadata; checksum inputs where possible |
| ETL configuration | YAML / JSON (implementation-defined) | Repo config files | Lint/validate config schema (if present) |
| Domain field dictionary | Markdown | `docs/data/<domain>/` | Doc protocol validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized dataset | CSV/GeoJSON/Parquet/etc. | `data/<domain>/processed/` | Domain contract (implementation-defined) |
| STAC Items + Collections | JSON | `data/stac/items/` + `data/stac/collections/` | STAC 1.0 + KFM-STAC profile |
| DCAT dataset records | RDF/Turtle/JSON-LD (implementation-defined) | `data/catalog/dcat/` | DCAT 3 + KFM-DCAT profile |
| PROV provenance bundles | RDF/Turtle/JSON-LD (implementation-defined) | `data/prov/` | PROV-O + KFM-PROV profile |
| Validation reports | text/JSON | CI artifacts or `mcp/runs/` (if used) | Must be reproducible |

### Sensitivity & redaction
- Identify fields requiring **generalization** (e.g., precise coordinates) or **omission** for public artifacts.
- When sovereignty/CARE rules apply, follow `docs/governance/SOVEREIGNTY.md` and document:
  - What was generalized/omitted
  - Why (policy rationale)
  - How to reproduce the transformation without exposing restricted detail

### Quality signals
- Completeness: required fields present, non-null constraints where applicable
- Validity: geometry validity, coordinate reference system consistency, date/time parsing
- Consistency: stable IDs, deduplication rules, referential integrity to source IDs
- Catalog integrity: STAC links resolve; item extents/time ranges align with assets

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections involved: domain collections under `data/stac/collections/` (naming conventions TBD).
- Items involved: assets under `data/stac/items/` with stable IDs and provenance pointers.
- Extension(s): KFM-STAC profile (see `stac_profile` in front-matter).

### DCAT
- Dataset identifiers: stable identifiers matching domain dataset IDs where possible.
- License mapping: ensure catalog license fields match the recorded source license.
- Contact / publisher mapping: follow governance guidance for attribution practices.

### PROV-O
- `prov:wasDerivedFrom`: processed outputs link to raw source entities.
- `prov:wasGeneratedBy`: processed outputs and catalogs link to an ETL/catalog activity.
- Activity / Agent identities: include contributor/automation agent identities (as allowed) and run configuration fingerprints.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- For breaking data shape changes, ensure contract tests or migration notes accompany the change.

## 🧱 Architecture

### Components
| Component | Responsibility | Input(s) | Output(s) |
|---|---|---|---|
| ETL pipelines | Ingest + normalize domain data deterministically | `data/<domain>/raw/` + configs | `data/<domain>/processed/` + logs |
| Catalog builders | Produce STAC/DCAT/PROV from processed outputs | `processed/` | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Validators | Enforce docs + schemas + integrity | Docs + catalogs + (optional) graph checks | Pass/fail reports |
| Graph loader | Ingest catalogs into Neo4j | STAC/DCAT/PROV artifacts | Neo4j nodes/edges + audit flags |
| API layer | Expose read contracts to UI and other clients | Graph + provenance refs | API responses (contracted) |

### Interfaces / contracts
- **Catalogs are the contract boundary** between ETL outputs and the graph loader.
- Graph loader should ingest from **catalog artifacts**, not raw source files, to keep stages loosely coupled.
- API responses should embed enough provenance pointers for UI/Story Nodes to cite evidence bundles.

### Extension points checklist (for future work)
When introducing a new data domain:
- [ ] Create `data/<domain>/raw/`, `work/`, `processed/` folders (and document expected contents)
- [ ] Add `docs/data/<domain>/README.md` describing sources, licenses, fields, and limitations
- [ ] Add or reuse schemas under `schemas/` (as applicable)
- [ ] Define STAC collection(s) and generate STAC items for assets
- [ ] Publish DCAT dataset record(s)
- [ ] Emit PROV activities/entities/agents capturing lineage + hashes
- [ ] Add validation steps + contract tests to CI

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- DataOps ensures every focusable entity can be tied back to **catalog + provenance references**.
- Focus Mode should be able to display:
  - The evidence bundle (assets/datasets)
  - Provenance pointers (what produced it, from what sources)
  - Any redaction/generalization flags required by governance

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID (no “floating” narrative statements).

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks (front-matter + required section structure)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Catalog integrity checks (links resolve; items ↔ collections integrity)
- [ ] Graph integrity checks (if running ingest/migrations)
- [ ] Backward-compatibility contract checks (APIs/graph interfaces), where applicable

### Reproduction
~~~bash
# Example placeholders — replace with repo-approved commands/scripts.
# 1) validate markdown protocol
# 2) validate STAC/DCAT/PROV schemas + integrity
# 3) run pipeline unit/integration tests
# 4) (optional) run graph/API contract tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| ETL run metadata (run_id, inputs, hashes) | ETL pipelines | `data/prov/` and/or CI artifacts |
| Catalog build summary (counts, diffs) | Catalog builders | CI artifacts |
| Validation failures (schema/link) | Validators | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- Who approves changes? (TBD — see governance docs)
- What requires council/board sign-off? (TBD — see governance docs)

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- For culturally sensitive information, document:
  - whether the location is generalized/blurred
  - whether access must be restricted
  - provenance of the restriction decision

### AI usage constraints
- Ensure this doc’s AI permissions/prohibitions match intended use (see front-matter).
- Do not use AI tooling to infer or publish sensitive locations or identities not present in governed sources.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-19 | Initial Data Ops README | TBD |

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
