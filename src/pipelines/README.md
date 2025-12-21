---
title: "KFM Pipelines — src/pipelines"
path: "src/pipelines/README.md"
version: "v0.1.0"
last_updated: "2025-12-21"
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

doc_uuid: "urn:kfm:doc:src:pipelines:readme:v0.1.0"
semantic_document_id: "kfm-src-pipelines-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:src:pipelines:readme:v0.1.0"
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

# src/pipelines — Pipelines

## 📘 Overview

### Purpose

- Define the **canonical intent and boundaries** of the pipelines subsystem: `src/pipelines/` contains pipeline code that produces governed, replayable outputs for KFM’s end-to-end flow.
- Capture the **non-negotiable constraints** that keep the repository architecture synced:
  - pipelines produce data and provenance artifacts under `data/`
  - catalogs are generated into `data/stac/`, `data/catalog/dcat/`, and `data/prov/`
  - UI never reads the graph directly (API boundary enforced elsewhere)

### Scope

| In Scope | Out of Scope |
|---|---|
| Pipeline code under `src/pipelines/` (ETL + transforms + catalog-build logic/orchestration) | Full domain-specific operational details (belongs in domain runbooks) |
| Emission expectations for run artifacts (PROV + run manifest) | Cloud deployment specifics (belongs in `tools/` or external ops repos) |
| Directory conventions for where outputs live (`data/<domain>/...`) | API contracts (belongs in `src/server/contracts/`) |
| Pointers to canonical runbooks and downstream consumers | UI implementation details (belongs in `web/`) |

### Audience

- Primary: pipeline / data engineering contributors, catalog maintainers
- Secondary: graph/ontology maintainers, API maintainers, reviewers running CI gates

### Definitions (link to glossary)

- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: **domain**, **raw/work/processed**, **STAC**, **DCAT**, **PROV**, **run manifest**, **idempotent**, **deterministic**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Pipeline code | `src/pipelines/` | Pipelines maintainers | ETL + transforms + catalog build code |
| Domain runbooks | `docs/pipelines/<domain>/` | Domain owners | Canonical “how to run” instructions per domain |
| Domain outputs | `data/<domain>/{raw,work,processed}/` | Data domain owners | Required staging layout per domain |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog maintainers | Generated artifacts; must validate against schemas |
| Schemas | `schemas/` | Contract owners | Validation source-of-truth for catalogs (and more) |
| Downstream graph | `src/graph/` + `data/graph/` | Graph owners | Graph ingests from processed + catalog + provenance artifacts |
| API boundary | `src/server/` | API owners | The only supported access path to graph + catalogs |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Canonical paths reflect current repo invariants
- [ ] “Do not break” rules are explicit (determinism/idempotency, provenance emission, no catalogs in `docs/`)
- [ ] Validation/CI expectations are stated
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `src/pipelines/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Domain folders + raw/work/processed outputs |
| Pipeline runbooks | `docs/pipelines/` | Per-domain run instructions + assumptions |
| Catalog outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Generated STAC/DCAT/PROV artifacts |
| Schemas | `schemas/` | JSON Schema (and optional shapes) used in validation |
| Graph | `src/graph/` + `data/graph/` | Graph build/import artifacts and bindings |
| API boundary | `src/server/` | Contracted access; redaction/generalization enforced here |
| UI | `web/` | React-based UI; consumes APIs and catalog endpoints only |
| Releases | `releases/` | Versioned artifacts (may include run manifests) |
| Tests | `tests/` | Unit/integration/contract tests |
| Tools | `tools/` | Dev tooling, validation helpers, scripts |

### Expected file tree for this sub-area

The repository conventions describe `src/pipelines/` as the pipeline code area, with subfolders such as `etl/` and `catalog/`. Exact per-domain layout is defined in domain runbooks.

~~~text
src/pipelines/
├── README.md
├── etl/                 # extraction + parsing + normalization (domain entrypoints)
│   └── <domain>/...      # domain-specific; see docs/pipelines/<domain>/
└── catalog/             # STAC/DCAT/PROV builders (or orchestration code)
    └── <catalog_type>/...# implementation-specific (not confirmed in repo)
~~~

## 🧭 Context

### Background

KFM’s canonical system ordering is preserved end-to-end:

**ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**

This directory implements the **ETL/pipeline portion** of that flow, producing governed outputs for downstream subsystems.

### Assumptions

- Domains have one canonical name and one canonical home under `data/<domain>/...` (domain naming standardization is an open question).
- Pipelines are repeatable/replayable, with deterministic transformations and stable identifiers.
- Per-domain operational steps (inputs, parameters, credential handling, schedules) are documented in `docs/pipelines/<domain>/`.

### Constraints / invariants

Non-negotiables for anything under `src/pipelines/`:

- **Canonical ordering** is preserved: ETL work precedes catalog generation; catalogs precede graph ingestion.
- Pipelines are **idempotent** (re-running doesn’t duplicate/compound outputs) and **deterministic** (same inputs/config → same outputs).
- Every pipeline run emits:
  - a **PROV activity bundle** under `data/prov/`
  - a **run manifest** (location may be `data/prov/` or `releases/<version>/`)
- Pipelines **never write STAC/DCAT/PROV** artifacts into `docs/`.
- **Data outputs are not code**: derived datasets belong under `data/<domain>/processed/`, not under `src/`.
- **No UI direct-to-graph reads**: the UI must not query Neo4j directly; graph access is via `src/server/`.

### Open questions

(Tracked in v13 planning; copied here for visibility.)

| Question | Owner | Target date |
|---|---|---|
| Standardize domain naming (e.g., `air-quality` vs `air_quality`) and resolve inconsistencies | Data governance | v13.0.0 |
| Minimum schema set required for “CI green” in v13 (stac/dcat/prov/storynodes/ui/telemetry) | Contracts owners | v13.0.0 |
| Adopt SHACL validation for JSON-LD bundles now or later? | Catalog + graph owners | v13.1.0 |

### Future extensions

- Add new domains following the domain expansion pattern (below).
- Treat “evidence products” as first-class artifacts with STAC assets + PROV lineage.
- Expand pipeline validation gates (schema + integrity + provenance completeness).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL + transforms<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>src/graph]
  C --> D[API boundary<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram (conceptual)

~~~mermaid
sequenceDiagram
  participant Runner as Pipeline Runner
  participant Data as data/<domain>/{raw,work,processed}
  participant Prov as data/prov
  participant Cat as data/stac + data/catalog/dcat
  Runner->>Data: write staged outputs (raw/work/processed)
  Runner->>Prov: emit PROV bundle + run manifest
  Runner->>Cat: build catalogs from processed outputs
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- Domain staging is required:
  - `data/<domain>/raw/` → `data/<domain>/work/` → `data/<domain>/processed/`
- Catalog artifacts are emitted to:
  - STAC: `data/stac/collections/` and `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`

### Run artifacts (required)

Every execution must produce, at minimum:

- A PROV activity bundle in `data/prov/`
- A run manifest (location: `data/prov/` or `releases/<version>/`)

Implementation details (exact filenames, schema, and run-id strategy) belong in domain runbooks unless standardized in `schemas/`.

### Domain expansion pattern

- New domains go under `data/<domain>/...`
- New domain pipeline runbooks go under `docs/pipelines/<domain>/...`
- Pipeline code for a domain should live under `src/pipelines/etl/<domain>/...` (or another single canonical location within `src/pipelines/`)

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy (pipeline responsibilities)

- Catalog build consumes **processed** outputs and emits:
  - STAC Items/Collections
  - DCAT dataset records
  - PROV lineage bundles for transforms and builds
- Catalog artifacts must validate against schemas in `schemas/`.
- Catalog artifacts must not be written into `docs/`.

### Versioning expectations

- Preserve stable identifiers for catalogs and lineage records where possible.
- When producing new versions, link predecessor/successor relationships (exact mechanics depend on schema and domain contract; not confirmed in repo).

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL / transforms | deterministic transforms + repeatable run instructions + staged outputs | idempotent + deterministic |
| Provenance | PROV activity bundle + run manifest per execution | provenance is first-class at boundaries |
| Catalogs | STAC/DCAT/PROV outputs + schema validation | machine-validated artifacts |
| Graph ingestion | graph import artifacts referencing STAC/DCAT/PROV IDs | ingest only from processed + catalogs + provenance |
| APIs | contracted access to graph + catalogs | UI never reads graph directly |

### Next-evolution extension points

- (A) Data: new domain with staged outputs + runbook
- (B) Evidence: new derived evidence products as STAC assets with PROV
- (C) Validation: richer schema and integrity checks in CI
- (D) Orchestration: standardized runner interface (not confirmed in repo)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Pipelines provide the **evidence layer**:
  - processed datasets
  - catalog entries (STAC/DCAT)
  - provenance bundles (PROV)
- Story Nodes and Focus Mode consume provenance-linked content; pipelines must make provenance discoverable and stable.

### Provenance-linked narrative rule

- Every claim presented in Story Nodes / Focus Mode must trace to a dataset / record / asset ID and its provenance chain.

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (as applicable)
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (when graph import artifacts are produced)
- [ ] API contract tests (when pipeline outputs affect API payloads)
- [ ] Security and sovereignty checks (when sensitive layers/sources exist)

### Reproduction

Per-domain run steps must be documented in `docs/pipelines/<domain>/`.

~~~bash
# Example placeholders — replace with repo-specific commands or link to the runbook

# 1) run domain ETL pipeline
# 2) generate catalogs (STAC/DCAT/PROV)
# 3) validate schemas in schemas/
# 4) run unit/integration tests
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run manifest | pipeline runner | `data/prov/` or `releases/<version>/` |
| PROV activity bundle | pipeline runner | `data/prov/` |
| Catalog validation report | catalog build | (not confirmed in repo) |

## ⚖ FAIR+CARE & Governance

### Review gates

Pipeline changes may require governance review when they introduce:

- New external data sources
- New potentially sensitive layers / locations
- New narrative-affecting AI behaviors (if any evidence products are ML-derived)
- New public-facing artifacts that affect API/UI outputs

### CARE / sovereignty considerations

- Do not infer or expose sensitive locations.
- If a domain includes restricted/sensitive data, enforce generalization/redaction at the API boundary and document the rules in the domain runbook.

### AI usage constraints

- Any AI-produced evidence artifacts must be opt-in where required and must carry uncertainty/confidence metadata (and still be provenance-linked).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-21 | Initial `src/pipelines/` README scaffold | TBD |

---

Footer refs:

- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
