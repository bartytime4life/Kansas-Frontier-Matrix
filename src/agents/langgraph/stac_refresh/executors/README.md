---
title: "STAC Refresh Executors"
path: "src/agents/langgraph/stac_refresh/executors/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:src:agents:langgraph:stac-refresh:executors:readme:v1.0.0"
semantic_document_id: "kfm-stac-refresh-executors-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:src:agents:langgraph:stac-refresh:executors:readme:v1.0.0"
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

# STAC Refresh Executors

## 📘 Overview

### Purpose
This directory contains **executor implementations** for the `stac_refresh` LangGraph agent.

An executor is the **runtime boundary** that performs side-effectful work required to refresh KFM catalog artifacts (most directly **STAC**, and potentially adjacent **DCAT** and **PROV** outputs), while keeping execution:
- deterministic and replayable
- observable and auditable
- aligned to KFM governance constraints

### Scope

| In Scope | Out of Scope |
|---|---|
| Defining executor responsibilities and invariants | Defining the entire `stac_refresh` agent graph |
| Adding new executor backends | Defining STAC/DCAT/PROV schemas |
| Execution-time logging, provenance capture expectations | Neo4j ingestion, API serving, UI rendering |
| Safety + redaction rules for executor outputs | Human editorial decisions for Story Nodes |

### Audience
- Primary: KFM developers adding/maintaining `stac_refresh` execution backends
- Secondary: Pipeline maintainers troubleshooting catalog refresh behavior

### Definitions
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Executor**: execution backend used by the agent to perform catalog refresh work
  - **Refresh**: regenerating / validating / syncing STAC, and related metadata products
  - **Catalog outputs**: STAC/DCAT/PROV artifacts produced by the pipeline

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `src/agents/langgraph/stac_refresh/executors/README.md` | repo | Execution-backend guidance |
| Executor implementations | `src/agents/langgraph/stac_refresh/executors/` | repo | One or more backends |
| STAC output roots | `data/stac/` | pipeline | STAC collections + items |
| DCAT output roots | `data/catalog/dcat/` | pipeline | DCAT dataset views |
| PROV output roots | `data/prov/` | pipeline | Lineage bundles |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Executor behavior documented without assuming unverified internals
- [ ] All referenced paths follow KFM staging conventions
- [ ] Validation steps are listed and repeatable
- [ ] Safety + sovereignty considerations are explicit

## 🗂️ Directory Layout

### Expected file tree for this sub-area
~~~text
📁 src/
└── 📁 agents/
    └── 📁 langgraph/
        └── 📁 stac_refresh/
            └── 📁 executors/
                ├── 📄 README.md
                ├── 📄 <executor_module>.py
                ├── 📄 <executor_module>.ts
                └── 📄 <shared_helpers>.<ext>
~~~

> Note: File extensions and module naming are **not confirmed in repo**. This tree is an allowed pattern sketch only.

## 🧭 Context

### Background
KFM’s canonical pipeline ordering is:

**ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**

The `stac_refresh` agent sits adjacent to the **catalog stage**, helping keep catalog artifacts current and valid.

### Assumptions
- The term `stac_refresh` implies “refresh catalog artifacts”, but **the exact operations are not confirmed in repo**.
- Executors are assumed to be the point where side effects occur (filesystem writes, command invocations, validation runs). This is an **inference based on naming**.

### Constraints and invariants
- Pipeline ordering is preserved: **catalog outputs precede graph build and downstream layers**.
- Frontend does not read the graph directly; UI consumes API contracts.
- Executors must not introduce undocumented side channels that bypass governance, provenance, or redaction controls.
- Prefer idempotent operations: reruns should not duplicate artifacts or drift results.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What executor backends exist today? | TBD | TBD |
| How is executor selection configured? | TBD | TBD |
| What is the minimal “refresh” contract across backends? | TBD | TBD |
| What telemetry/run-log schema is used for refresh runs? | TBD | TBD |

## 🗺️ Diagrams

### System and dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React and Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]

  subgraph Agent
    X[LangGraph stac_refresh] --> Y[Executors]
  end

  Y --> B
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Refresh request or plan | object | agent node input | schema or type checks |
| Catalog roots | paths | repo filesystem | path allowlist |
| Optional run context | object | pipeline runtime | required fields present |

> Exact types and schemas are **not confirmed in repo**. Executors should validate inputs defensively.

### Outputs

| Output | Format | Path | Contract or schema |
|---|---|---|---|
| STAC collections | JSON | `data/stac/collections/` | STAC profile |
| STAC items | JSON | `data/stac/items/` | STAC profile |
| DCAT dataset views | JSON-LD or RDF | `data/catalog/dcat/` | DCAT profile |
| PROV bundles | JSON or RDF | `data/prov/` | PROV profile |
| Run logs | JSON / text | `mcp/runs/` or `docs/telemetry/` | not confirmed in repo |

### Sensitivity and redaction
- Do not emit sensitive locations or restricted attributes unless the governing policy and output channel explicitly permit it.
- If a refresh process encounters sensitive assets, it must preserve applicable generalization/redaction rules.

## 🌐 STAC, DCAT and PROV Alignment

### STAC
- Executors should preserve:
  - items ↔ collections integrity
  - stable IDs/keys where applicable
  - link integrity

### DCAT
- If DCAT is refreshed/derived as part of the run, executors should preserve dataset identifiers and license mappings.

### PROV
- Refresh activity should record:
  - `prov:wasDerivedFrom` references back to sources
  - `prov:wasGeneratedBy` run/activity identifiers

> The precise PROV encoding and run identifier conventions are **not confirmed in repo**.

## 🧱 Architecture

### Executor responsibilities
An executor is responsible for:
- running the refresh action in a well-defined environment
- enforcing safe side effects (write locations, command allowlists)
- producing logs/telemetry sufficient for debugging and auditing
- returning a structured result for the agent to route/decide next steps

### Non-responsibilities
Executors should not:
- write directly to Neo4j
- serve API responses
- mutate UI layer registries
- author Story Nodes

### Interface contract
The concrete interface is **not confirmed in repo**. Wherever the “executor base” is defined in this package, keep these rules:

- Inputs must be validated and normalized.
- Outputs must include:
  - success/failure
  - artifact paths or IDs
  - provenance/run metadata
  - warnings (validation failures, partial updates)

## 🧩 Implementing a new executor

### Checklist
- [ ] Choose an execution environment boundary (local process, container, remote runner, etc.)
- [ ] Implement the executor interface used by `stac_refresh`
- [ ] Ensure deterministic behavior with pinned versions/config
- [ ] Constrain write locations to catalog and approved output folders
- [ ] Capture run metadata and provenance
- [ ] Add unit tests and integration tests
- [ ] Update this README with the new executor name and selection mechanism

### Registration
How executors are registered or discovered is **not confirmed in repo**. Common patterns include:
- explicit registry map
- entrypoint-based plugin discovery
- dependency injection via agent config

Document the actual mechanism here once verified.

## 🧪 Validation and CI

### Validation steps
- [ ] Markdown protocol checks
- [ ] STAC schema validation
- [ ] STAC items/collections integrity checks
- [ ] DCAT validation if emitted
- [ ] PROV validation if emitted
- [ ] Graph integrity checks are downstream and should not be run from executors unless explicitly designed

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# Validate STAC
# <repo-command> validate stac --path data/stac

# Validate DCAT
# <repo-command> validate dcat --path data/catalog/dcat

# Validate PROV
# <repo-command> validate prov --path data/prov

# Run tests
# <repo-command> test -k stac_refresh
~~~

## ⚖ FAIR+CARE and Governance

### Review gates
- If an executor changes:
  - output locations
  - redaction/generalization behavior
  - provenance behavior
  - external tool invocation
  - credential handling
  then the change should be flagged as **requires human review**.

### AI usage constraints
- Executors must not generate unsourced narrative content.
- Executors must not infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README scaffold for executors | TBD |
