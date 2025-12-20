---
title: "KFM Data Ops — Data Quality Checks"
path: "docs/data-ops/data-quality/checks/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data-ops:data-quality:checks:readme:v1.0.0"
semantic_document_id: "kfm-data-ops-data-quality-checks-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data-ops:data-quality:checks:readme:v1.0.0"
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

# KFM Data Ops — Data Quality Checks

This folder documents **data-quality checks** that protect the KFM pipeline and its governed outputs.

- Parent: `docs/data-ops/data-quality/README.md`
- Root: `docs/data-ops/README.md`
- Canonical system ordering (non-negotiable): **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.

---

## 📘 Overview

### Purpose
- Provide a **catalog + runbook** for data-quality checks and gates applied across KFM.
- Clarify **where checks apply**, **what they protect**, and **how results should be recorded** (schemas + provenance pointers) so downstream consumers (especially Story Nodes / Focus Mode) remain traceable and trustworthy.

### Scope

| In Scope | Out of Scope |
|---|---|
| Check taxonomy, check documentation pattern, required “gates” to keep outputs valid, how to record results and where to link them | Tool-specific implementation details (unless already present in repo), domain-specific one-off cleanup instructions, operational incident response |

### Audience
- Primary: Data/pipeline maintainers, catalog maintainers, graph maintainers
- Secondary: API/UI developers, curators/editors, QA/reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Check**: A deterministic validation/assertion over an artifact (dataset, catalog, graph, contract, UI registry, story bundle).
  - **Gate**: A check (or set of checks) that **must pass** to merge/ship or to publish a governed artifact.
  - **Run ID**: A stable identifier for a pipeline execution; used to link STAC/DCAT/PROV + telemetry.
  - **Provenance**: Evidence chain linking outputs to inputs and activities (PROV-O).
  - **Public vs restricted**: Sensitivity classification for artifacts and logs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline ordering + CI gates) | `docs/MASTER_GUIDE_v12.md` | TBD | Source of truth for invariants and validation gates |
| Data Ops overview | `docs/data-ops/README.md` | TBD | How DataOps is organized |
| Data Quality overview | `docs/data-ops/data-quality/README.md` | TBD | End-to-end quality strategy |
| STAC catalogs | `data/stac/` | TBD | Validation should include item↔collection integrity |
| DCAT catalogs | `data/catalog/dcat/` | TBD | Dataset identifiers + license mapping |
| PROV lineage | `data/prov/` | TBD | Run-level provenance & derivations |
| Telemetry schemas + events | `schemas/telemetry/` + `docs/telemetry/` | TBD | Schema-validated pipeline signals |
| Check definitions (implementation) | not confirmed in repo | TBD | Link here once location is standardized |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Links to parent DataOps/DataQuality docs resolve
- [ ] Check taxonomy present and mapped to pipeline stages
- [ ] Validation & CI gates section reflects current repo expectations
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] “not confirmed in repo” clearly marked where implementation is unknown

---

## 🗂️ Directory Layout

### This document
- `path`: `docs/data-ops/data-quality/checks/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed outputs per domain |
| STAC catalogs | `data/stac/` | Collections + Items + assets |
| DCAT catalogs | `data/catalog/dcat/` | Dataset catalog exports |
| PROV lineage | `data/prov/` | Pipeline run provenance |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog generation |
| Graph | `src/graph/` | Ontology bindings + migrations + loaders |
| APIs | `src/api/` (or repo API path) | Contracted access layer (UI must not query graph directly) |
| Frontend | `web/` | React + map client + layer registry |
| Schemas | `schemas/` | JSON schemas (catalogs, telemetry, contracts) |
| Tests | `tests/` | Unit + integration + contract tests |

### Expected file tree for this sub-area

~~~text
📁 docs/
├── 📁 data-ops/
│   ├── 📄 README.md
│   └── 📁 data-quality/
│       ├── 📄 README.md
│       └── 📁 checks/
│           ├── 📄 README.md   👈 you are here
│           ├── 📁 etl/
│           │   └── 📄 <check-id>.md
│           ├── 📁 catalogs/
│           │   └── 📄 <check-id>.md
│           ├── 📁 graph/
│           │   └── 📄 <check-id>.md
│           ├── 📁 api/
│           │   └── 📄 <check-id>.md
│           ├── 📁 ui/
│           │   └── 📄 <check-id>.md
│           └── 📁 story/
│               └── 📄 <check-id>.md
~~~

> Folder breakdown above is a **documentation pattern**. Implementation locations for executable checks are **not confirmed in repo**.

---

## 🧭 Context

### Background
KFM is a governed geospatial + historical knowledge system. Its credibility depends on:
- deterministic, reproducible pipeline outputs
- schema-valid catalogs (STAC/DCAT/PROV)
- graph integrity
- API contract stability
- Focus Mode’s provenance-only rule (no uncited facts)

Data-quality checks are how we enforce these guarantees consistently, and how we prevent “quiet drift” where outputs slowly stop conforming to contracts.

### Assumptions
- CI runs validation gates on changed artifacts (docs, schemas, catalogs, graph, API, UI registry).
- Pipeline runs can produce provenance pointers and machine-validated reports (schema + integrity).

### Constraints / invariants
- Canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (**no direct graph dependency**).
- Focus Mode must only present provenance-linked content; any predictive/AI content must be explicitly labeled and opt-in.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Where do executable check definitions live (code/config)? | TBD | TBD |
| What is the canonical check-report schema (JSON) and where is it versioned? | TBD | TBD |
| What severity/threshold policy is used for “warn vs fail”? | TBD | TBD |

### Future extensions
- Add a “Quality dashboard” view in telemetry (trend lines for failures/warnings).
- Add anomaly detection for deltas in key metrics (counts, extents, reference integrity) — only if governance permits.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL outputs] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  Q1[[ETL checks]] --- A
  Q2[[Catalog checks]] --- B
  Q3[[Graph integrity checks]] --- C
  Q4[[API contract checks]] --- D
  Q5[[UI registry checks]] --- E
  Q6[[Story evidence checks]] --- F
  Q7[[Focus provenance rule]] --- G
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant CI as CI Runner
  participant ETL as Pipeline
  participant CAT as Catalog Validator
  participant GR as Graph Validator
  participant API as Contract Tests
  participant UI as UI Registry Tests

  CI->>ETL: Run pipeline (deterministic config)
  ETL-->>CI: Outputs + run_id + logs
  CI->>CAT: Validate STAC/DCAT/PROV + telemetry schemas
  CI->>GR: Validate graph integrity constraints
  CI->>API: Run API contract tests
  CI->>UI: Validate layer registry schema
  CI-->>CI: Gate pass/fail + report bundle
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | varies | `data/raw/` or external connectors | Basic parse + checksum (tooling not confirmed in repo) |
| Pipeline outputs | JSON/GeoJSON/Parquet/etc | `data/work/` / `data/processed/` | Structural + semantic checks |
| Catalog artifacts | JSON/RDF | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Schema + integrity checks |
| Schemas | JSON Schema | `schemas/` | Schema lint + version checks |
| UI registries | JSON | `web/` | Schema + link integrity |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Check report bundle | JSON/MD | not confirmed in repo | (report schema not confirmed in repo) |
| CI gate results | logs | CI system | Must be stable & searchable |
| Telemetry events | JSON | (telemetry location in repo) | `schemas/telemetry/` |
| Provenance links | PROV-O | `data/prov/` | KFM-PROV profile |

### Sensitivity & redaction
- Check reports should avoid publishing sensitive coordinates, protected locations, or PII.
- If a check requires inspecting sensitive fields, store the detailed evidence in **restricted logs** and emit only aggregated summaries in public artifacts.

### Quality signals
Candidate (not exhaustive) quality dimensions for checks:
- **Schema validity** (JSON Schema, required fields)
- **Completeness** (required columns/attributes populated)
- **Range/domain validity** (dates, numeric ranges, enumerations)
- **Uniqueness / deduplication** (stable IDs, no unexpected duplicates)
- **Referential integrity** (links resolve: STAC assets, PROV derivations, DCAT refs)
- **Spatial validity** (geometry validity, CRS expectations, bbox sanity)
- **Temporal consistency** (time ranges, ordering, timezone normalization)
- **Provenance completeness** (prov:wasDerivedFrom / prov:wasGeneratedBy present where required)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Checks should ensure:
- Items validate against the STAC profile in use
- Item↔collection integrity holds (no orphaned items)
- Asset hrefs resolve (broken-link checks) where possible

### DCAT
Checks should ensure:
- Dataset identifiers are stable and consistent across releases
- License mapping is present and valid
- Publisher/contact metadata is present where required

### PROV-O
Checks should ensure:
- Outputs link back to inputs via `prov:wasDerivedFrom`
- Outputs are tied to a run/activity via `prov:wasGeneratedBy`
- Activity/agent identifiers are stable enough to support reproducibility/auditing

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships where applicable.
- Prefer “append + supersede” patterns over destructive overwrites for governed outputs.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs |
| Catalogs | STAC/DCAT/PROV generation | JSON/RDF + validators |
| Graph | Neo4j constraints + semantics | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative | API calls |
| Story Nodes | Curated narrative | Catalog + graph references |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/api/` + docs | Contract tests required |
| Layer registry | `web/` | Schema-validated |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + schema validation
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
Quality checks protect Focus Mode by ensuring:
- story nodes only reference resolvable evidence (catalog IDs, document IDs, asset IDs)
- provenance pointers remain intact across pipeline evolution

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Predictive/AI outputs (if any) must include uncertainty/confidence and be opt-in.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Minimum CI gates (expected)
The following gate categories are expected for v12-ready contributions (see Master Guide for the canonical list):
- Markdown protocol validation
- JSON schema validation (STAC/DCAT/telemetry)
- Graph integrity tests
- API contract tests
- UI layer registry schema checks
- Security + sovereignty scanning gates

### Local validation
- not confirmed in repo: the exact local commands/targets (e.g., `make validate`, `npm test`, etc.)
- Add the canonical local steps once build tooling is standardized in-repo.

### Reporting expectations
- Check failures should be actionable (what failed, where, how to reproduce).
- Prefer stable identifiers and links to the relevant schema/doc when possible.

---

## ⚖ FAIR+CARE & Governance
- New checks that affect sensitivity handling, sovereignty rules, or redaction logic require **human review**.
- Check documentation should clearly state whether it may touch restricted locations or culturally sensitive material and how it is generalized/handled.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial Data Quality Checks README scaffold | TBD |

