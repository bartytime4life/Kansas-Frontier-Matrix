---
title: "KFM Graph Cypher Artifacts — data/graph/cypher"
path: "data/graph/cypher/README.md"
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

doc_uuid: "urn:kfm:doc:data:graph:cypher:readme:v1.0.0"
semantic_document_id: "kfm-data-graph-cypher-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:graph:cypher:readme:v1.0.0"
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

# KFM Graph Cypher Artifacts — `data/graph/cypher`

## 📘 Overview

### Purpose

- This README defines what belongs in `data/graph/cypher/` and how these scripts are intended to be used as **optional post-import Cypher** during/after graph loading.
- It clarifies how these artifacts relate to other graph code and documentation in the repo (ontology, migrations, and pipeline orchestration).

### Scope

| In Scope | Out of Scope |
|---|---|
| Cypher scripts stored under `data/graph/cypher/` as post-import artifacts | Defining the ontology itself (see `docs/graph/` / `src/graph/`) |
| Conventions for safe, reproducible, provenance-linked scripts | Production operations runbooks, credentials, and deployment procedures |
| How these scripts align with STAC/DCAT/PROV identifiers and graph constraints | API contract changes (use API Contract Extension template) |

### Audience

- Primary: Graph / pipeline maintainers working on Neo4j load and post-load normalization.
- Secondary: Data stewards and reviewers validating provenance, sensitivity rules, and reproducibility.

### Definitions (link to glossary)

- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Post-import script**: Cypher executed after a bulk load (e.g., to apply constraints, indexes, or derived relationships).
  - **Migration**: A versioned graph schema/data change tracked as code (typically under `src/graph/migrations/`), distinct from run artifacts.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Post-import Cypher artifacts | `data/graph/cypher/` | Graph pipeline | This directory |
| Graph import CSV artifacts | `data/graph/csv/` | Graph pipeline | Bulk import inputs |
| Graph subsystem code | `src/graph/` | Graph pipeline | Ontology bindings + ingest/build |
| Ontology + graph docs | `docs/graph/` | Graph maintainers | Labels/relations + constraints (canonical) |
| Provenance records | `data/prov/` | Pipeline | W3C PROV lineage outputs |
| Catalogs | `data/stac/`, `data/catalog/dcat/` | Pipeline | Dataset discovery + metadata |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory purpose matches canonical repo structure and graph pipeline ordering
- [ ] Clear separation from versioned graph migrations (`src/graph/migrations/`)
- [ ] Validation steps listed and repeatable (even if commands are placeholders)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `data/graph/cypher/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Graph import artifacts | `data/graph/` | CSV + optional post-import scripts |
| Import CSVs | `data/graph/csv/` | Bulk import tables (nodes/edges) |
| Post-import scripts | `data/graph/cypher/` | Optional Cypher to run after import |
| Graph code + migrations | `src/graph/` | Graph build + ingest + migrations (code) |
| Ontology + constraints docs | `docs/graph/` | Controlled schema documentation |
| Catalogs + provenance | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Metadata + lineage |

### Expected file tree (for this sub-area)

~~~text
📁 data/
├── 📁 graph/
│   ├── 📁 csv/               # Bulk import CSV artifacts (nodes/edges)
│   └── 📁 cypher/            # Optional post-import scripts (this folder)
│       └── 📄 README.md
~~~

> Note: Exact filenames and subfolder conventions for generated scripts are **not governed here** unless explicitly adopted by the pipeline. If you introduce a convention (e.g., ordering prefixes or per-run subfolders), document it under “Constraints / invariants” below and ensure the graph build pipeline enforces it.

## 🧭 Context

### Background

KFM’s canonical pipeline ordering is:

- ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode

This directory supports the **Neo4j graph** stage by holding optional Cypher scripts that may be needed after a bulk import or ingest step.

### Assumptions

- `data/graph/cypher/` is intended for **optional post-import scripts** that complement graph import artifacts (e.g., `data/graph/csv/`).  
- Scripts here should be considered **artifacts** of the graph build/ingest process and should remain consistent with the ontology and governance constraints.

### Constraints / invariants

- **No UI-to-graph shortcut:** UI consumers must not query Neo4j directly; access is mediated by the API layer (contracts live at the API boundary).
- **No secrets in repo:** Cypher scripts must not embed credentials, tokens, connection strings, or private endpoints.
- **Determinism:** When feasible, scripts should be idempotent (use `MERGE` and stable IDs rather than repeated `CREATE`).
- **Ontology alignment:** Labels, relationship types, and required properties must remain consistent with the ontology/constraints governed under `docs/graph/` and implemented under `src/graph/`.
- **Sensitive data handling:** If scripts reference sensitive places/records, ensure they follow redaction/generalization rules and do not disclose protected locations or attributes.

### Open questions

| Question | Why it matters | Status / Owner |
|---|---|---|
| What tool/step executes scripts in `data/graph/cypher/` (e.g., loader, CI job, manual runbook)? | Determines ordering, failure handling, and audit logs | TBD |
| Do we want a naming + ordering convention (e.g., numeric prefixes)? | Ensures deterministic execution order | TBD |
| Should each script include embedded provenance headers (run ID / PROV Activity / dataset IDs)? | Enables traceability and review | TBD |

### Future extensions

- Add a governed convention for:
  - script ordering (prefixes),
  - per-run grouping (`data/graph/cypher/<run_id>/...`),
  - required script headers with provenance identifiers.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/processed/] --> B[Catalog build<br/>STAC/DCAT/PROV]
  B --> C[Graph build / ingest]
  C --> D[Bulk import CSV artifacts<br/>data/graph/csv/]
  C --> E[Optional post-import Cypher<br/>data/graph/cypher/]
  D --> F[Neo4j load]
  E --> G[Post-import execution]
  F --> H[Neo4j graph]
  G --> H
  H --> I[API layer]
  I --> J[Web UI / Story Nodes / Focus Mode]
~~~

~~~mermaid
sequenceDiagram
  participant Pipeline as Graph Build Pipeline
  participant FS as Repo Artifacts (data/graph/*)
  participant Neo as Neo4j
  participant API as API Layer
  Pipeline->>FS: Write CSV import artifacts (data/graph/csv/)
  Pipeline->>FS: Write optional post-import scripts (data/graph/cypher/)
  Pipeline->>Neo: Load CSVs (bulk import / ingest)
  Pipeline->>Neo: Execute post-import Cypher (optional)
  API->>Neo: Query with sensitivity/provenance rules
  API-->>API: Contracted response construction
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Graph-ready entities/edges | CSV / structured exports | `data/graph/csv/` and/or `data/processed/` | Schema checks + stable IDs |
| Catalog identifiers | JSON | `data/stac/`, `data/catalog/dcat/` | STAC/DCAT validation |
| Provenance records | JSON-LD (PROV) | `data/prov/` | PROV profile validation |
| Ontology constraints | Markdown + code | `docs/graph/`, `src/graph/` | Constraint tests + reviews |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Post-import scripts | `.cypher` text | `data/graph/cypher/` | Must align with ontology + governance |
| Updated graph state | Neo4j store | (deployed instance) | Ontology + constraints |

### Sensitivity & redaction

- Do not encode restricted attributes or precise sensitive locations directly in scripts unless the repository classification/sensitivity allows it and governance approves.
- Prefer referencing stable identifiers and leaving sensitive-value handling to governed pipeline transforms and API redaction rules.

### Quality signals

- Idempotent execution (safe re-runs where possible).
- No “orphan” entities: created nodes/edges should include provenance links and required identifiers.
- Script linting / review for destructive patterns (e.g., unbounded deletes).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Collections involved: (TBD — depends on which datasets are being imported)
- Items involved: (TBD — scripts should prefer stable STAC Item IDs when linking document-like entities)

### DCAT

- Dataset identifiers: (TBD — scripts should prefer stable dataset IDs, not free-text names)
- License mapping: handled in catalogs; scripts should not override catalog license metadata

### PROV-O

- `prov:wasDerivedFrom`: link created/updated entities back to dataset/item identifiers where supported
- `prov:wasGeneratedBy`: ensure graph changes can be attributed to a run/activity ID
- Activity / Agent identities: prefer pipeline run identifiers and/or scripted agent IDs

### Versioning

- Use stable IDs and explicit version lineage patterns (where applicable) rather than overwriting meaning of existing labels/relations.

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
| JSON schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + docs | Contract tests required |
| Ontology + graph constraints | `docs/graph/` + `src/graph/` | Version + migrations |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- These scripts should enable reliable graph traversals required by Focus Mode and story queries (e.g., ensuring constraints/indexes exist and that provenance relationships are present).

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.

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
- [ ] Schema validation (STAC/DCAT/PROV) — when scripts reference catalog/provenance IDs
- [ ] Graph integrity checks (constraints, required properties, link integrity)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) (optional) validate Cypher syntax / run against a local/staging Neo4j
# cypher-shell -f data/graph/cypher/<script>.cypher

# 2) run graph integrity checks (repo-specific)
# <graph-integrity-check-command>

# 3) run doc lint
# <doc-lint-command>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Cypher execution logs | Neo4j / pipeline runner | `docs/telemetry/` + `schemas/telemetry/` (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates

- Requires human review when scripts:
  - alter constraints/indexes,
  - touch provenance modeling,
  - touch sensitive datasets/locations,
  - or change semantics of existing labels/relations.

### CARE / sovereignty considerations

- Follow `docs/governance/SOVEREIGNTY.md` and related governance docs.
- Do not introduce scripts that expose or re-identify sensitive locations, communities, or restricted attributes.

### AI usage constraints

- Ensure this document’s AI permissions/prohibitions match intended use (see front-matter).

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for `data/graph/cypher/` | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
