---
title: "KFM — Work Logs: Graph"
path: "data/work/logs/graph/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "draft"
doc_kind: "Readme"
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

doc_uuid: "urn:kfm:doc:data:work:logs:graph:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-graph-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:graph:readme:v1.0.0"
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

# Work Logs — Graph

## 📘 Overview

### Purpose
This directory stores **graph-stage operational logs** produced while building, validating, and/or migrating the KFM knowledge graph (Neo4j). These logs support:
- reproducibility (what ran, when, with which inputs)
- auditing (what was created/changed, what was skipped/redacted)
- troubleshooting (why a run failed or produced warnings)
- CI visibility (machine-readable summaries for GitHub Actions and local runs)

### Scope

| In Scope | Out of Scope |
|---|---|
| Logs from graph ingest/build steps (e.g., STAC/DCAT/PROV → Neo4j) | Raw source datasets (belong under `data/raw/` / `data/sources/`) |
| Graph integrity check outputs (constraints, cardinality, missing refs) | Permanent “system-of-record” metrics (belongs in governed telemetry if/when added) |
| Migration reports and diffs (schema/ontology evolution) | UI/client logs (belong under `web/` tooling or external observability) |
| Redaction/audit notes (what was generalized/omitted) | Secrets/credentials (must never be written here) |

### Audience
- Primary: Data/graph pipeline maintainers, CI maintainers
- Secondary: Reviewers (security/governance), contributors debugging ingestion

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Graph run**: One execution of the graph build/ingest pipeline.
  - **Integrity check**: A deterministic validation against expected constraints/relationships.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| This README | `data/work/logs/graph/README.md` | Repo maintainers | Directory contract + conventions |
| Graph build code | `src/graph/` or `src/pipelines/` | Graph maintainers | Not confirmed in repo (path may differ) |
| PROV bundles | `data/prov/` | Pipeline | Graph logs should reference PROV activity/run IDs |
| STAC/DCAT inputs | `data/stac/`, `data/catalog/dcat/` | Pipeline | Graph logs should reference dataset/item IDs |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose is clear (what goes here, what must not)
- [ ] Naming + minimal metadata conventions documented
- [ ] Validation steps listed and repeatable
- [ ] Security + sovereignty considerations explicitly stated (no secrets / no sensitive locations)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/graph/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Work staging | `data/work/` | Intermediate artifacts not considered “final published data” |
| Work logs (root) | `data/work/logs/` | Cross-stage logs (ETL/catalog/graph/api/ui/ai) |
| Checks (shared) | `data/work/logs/checks/` | Shared validation outputs (not confirmed in repo) |
| Graph code | `src/graph/` | Graph modeling + ingest/build tooling (not confirmed in repo) |
| Graph docs | `docs/graph/` | Ontology + migrations + constraints (not confirmed in repo) |
| Catalogs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` | Inputs + provenance records |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        └── 📁 graph/
            ├── 📄 README.md
            ├── 📁 runs/                     # proposed: one folder per run_id (not confirmed in repo)
            │   └── 📁 <run_id>/
            │       ├── 📄 run.summary.json  # proposed: machine-readable summary
            │       ├── 📄 run.log           # proposed: human-readable text log
            │       ├── 📄 ingest.report.json
            │       ├── 📄 integrity.report.json
            │       └── 📄 errors.ndjson     # proposed: structured error events (optional)
            ├── 📁 migrations/               # proposed: schema/constraint migration logs
            └── 📁 exports/                  # proposed: optional graph export diagnostics
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline order is preserved:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

This directory exists to capture the **graph-stage “run logs + validation”** evidence required for deterministic, reviewable graph builds.

### Assumptions
- The graph builder consumes **catalog outputs** (STAC/DCAT/PROV) rather than raw sources.
- The project may run graph builds locally and in CI; both should emit compatible logs.
- Log payloads should be safe to commit (public/open) unless explicitly marked otherwise.

### Constraints / invariants
- **No secrets, tokens, passwords, connection strings, or private keys** in any log files.
- **No sensitive locations** or restricted coordinates should be emitted to logs unless already generalized upstream.
- **Frontend never reads Neo4j directly**; logs are operational artifacts, not a client contract.
- Graph logs should be **traceable** to catalog/provenance IDs, not ad-hoc filenames.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Should graph logs be committed to git or stored only as CI artifacts? | TBD | TBD |
| Do we require a formal JSON schema for `run.summary.json`? | TBD | TBD |
| Where is the canonical run_id defined (PROV activity ID vs pipeline run UUID)? | TBD | TBD |

### Future extensions
- Extension point A: Add governed telemetry schema under `schemas/telemetry/` for graph run summaries.
- Extension point B: Emit redaction/audit flags suitable for Focus Mode “evidence panels”.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[STAC/DCAT/PROV inputs] --> B[Graph build/ingest]
  B --> C[Neo4j Graph]
  B --> D[data/work/logs/graph<br/>run logs + reports]
  D --> E[CI artifacts / review]
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| STAC items/collections | JSON | `data/stac/` | STAC schema validation (elsewhere) |
| DCAT dataset views | JSON-LD / TTL | `data/catalog/dcat/` | DCAT profile validation (elsewhere) |
| PROV bundles | JSON-LD | `data/prov/` | PROV profile validation (elsewhere) |
| Graph mappings/config | YAML/JSON | `src/graph/` / `src/pipelines/` | Lint + unit tests (not confirmed in repo) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Run summary | JSON | `data/work/logs/graph/runs/<run_id>/run.summary.json` | Proposed (not confirmed in repo) |
| Human log | TXT | `data/work/logs/graph/runs/<run_id>/run.log` | Freeform |
| Ingest report | JSON | `.../ingest.report.json` | Proposed (not confirmed in repo) |
| Integrity report | JSON | `.../integrity.report.json` | Proposed (not confirmed in repo) |
| Error events | NDJSON | `.../errors.ndjson` | Optional |

### Sensitivity & redaction
- Logs must not record:
  - credentials, auth headers, connection URIs with passwords
  - unredacted restricted coordinates
  - raw personally identifying information (PII) extracted from sources
- If an error message contains sensitive strings, the logging layer must **sanitize** before writing.

### Quality signals
Recommended fields (if/when a structured run summary is adopted):
- counts: nodes created/updated, relationships created/updated, items skipped
- warnings: missing references, schema mismatches, unresolvable IDs
- timings: elapsed time per phase (ingest, resolve, validate)
- provenance pointers: PROV activity ID(s), input catalog commit hash, output graph version tag

## 🌐 STAC, DCAT & PROV Alignment

### STAC
Graph log entries should reference STAC Item/Collection IDs (not local filenames), especially for:
- “missing item referenced by …”
- “invalid bbox/geometry for …”
- “asset download failed for …”

### DCAT
Graph logs should reference DCAT dataset identifiers when reporting dataset-level outcomes (e.g., dataset skipped due to license mismatch).

### PROV-O
- Every graph run should be linkable to:
  - `prov:wasDerivedFrom` → input STAC/DCAT entities
  - `prov:wasGeneratedBy` → the graph-build activity/run record
- The **log files are not the provenance record**, but should include pointers to PROV IDs/paths.

### Versioning
- If graph versions are produced, logs should record:
  - predecessor/successor pointers (if available)
  - the git commit SHA used to build the run
  - the catalog version (STAC/DCAT/PROV snapshot identifiers)

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| Catalogs | Produce STAC/DCAT/PROV | JSON/JSON-LD files |
| Graph build | Ingest + model + resolve | CLI/tooling (not confirmed in repo) |
| Neo4j | Persist graph | Accessed via API layer (not directly by UI) |
| Graph logging | Emit run artifacts | `data/work/logs/graph/` |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Run summary schema (proposed) | `schemas/telemetry/` | Semver + changelog (not confirmed in repo) |
| Graph integrity checks | `tests/` + `src/graph/` | Must be deterministic |
| CI pipeline outputs | `.github/` workflows/actions | Artifact retention policy TBD |

### Extension points checklist (for future work)
- [ ] Add a JSON schema for graph run summaries
- [ ] Add CI step to validate run summary schema
- [ ] Add redaction sanitizers to logging layer
- [ ] Add broken-reference audit reporting (STAC/DCAT/PROV ↔ graph)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
This directory is **not** a Focus Mode input. Instead, it supports:
- audit panels (showing whether graph evidence is complete)
- reviewer confidence (tracking ingestion warnings/errors)

### Provenance-linked narrative rule
Any narrative produced downstream must trace to catalog/provenance IDs; logs here help debug those traces.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Ensure logs contain no secrets (secret scanning / grep rules)
- [ ] Ensure structured JSON outputs (if present) are valid JSON
- [ ] Ensure per-run directory naming is stable and collision-free
- [ ] Ensure graph integrity report exists for CI builds (if configured)

### Reproduction
~~~bash
# Placeholder — replace with repo-specific commands once confirmed.
# 1) Build/ingest graph
#    <graph-build-command> --run-id <run_id>
#
# 2) Validate integrity
#    <graph-validate-command> --run-id <run_id>
#
# 3) Confirm logs emitted
#    ls data/work/logs/graph/runs/<run_id>/
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| Graph build duration | Graph build tool | `run.summary.json` (proposed) |
| Node/edge counts | Graph build tool | `ingest.report.json` (proposed) |
| Constraint failures | Integrity checks | `integrity.report.json` (proposed) |
| Redaction events | Sanitizer layer | `run.summary.json` (proposed) |

## ⚖ FAIR+CARE & Governance

### Review gates
- If logs include any sensitive fields or locations: **requires human review** (security + sovereignty).
- If logs are used to justify public narrative decisions: **historian/editor review** recommended.

### CARE / sovereignty considerations
- If Indigenous or culturally sensitive locations are involved, do not emit precise coordinates in logs unless already generalized according to governance rules.

### AI usage constraints
- AI may summarize logs for debugging, but must not infer or reconstruct sensitive locations from partial information.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial `data/work/logs/graph/` README scaffolding | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

