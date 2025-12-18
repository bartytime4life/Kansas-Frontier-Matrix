---
title: "KFM Tools — Architecture"
path: "tools/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-18"
status: "draft"
doc_kind: "Architecture"
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

doc_uuid: "urn:kfm:doc:tools:architecture:v1.0.0"
semantic_document_id: "kfm-tools-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:tools:architecture:v1.0.0"
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

# KFM Tools — Architecture

## 📘 Overview

### Purpose
- Define the role and boundaries of the `tools/` subtree as **governed operational + developer tooling** that supports KFM’s canonical pipeline stages (ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode).
- Establish minimum contracts so tools are **deterministic, reproducible, and provenance-emitting**, and do not bypass governance (especially for sensitive or sovereignty-scoped data).

### Scope
| In Scope | Out of Scope |
|---|---|
| CLI utilities that wrap/drive KFM pipeline steps (run, validate, package, migrate) | Long-lived production logic that belongs in `src/` (pipelines/server/graph) |
| Catalog builders/validators (STAC/DCAT/PROV) and report generators | UI code (`web/`) and direct browser data access patterns |
| Ops-safe helpers (checksums, idempotency checks, dry-run tooling) | Ad-hoc, undocumented one-off scripts without run logs/provenance |
| Developer quality gates (schema checks, markdown protocol checks, geo validity checks) | Anything that requires embedding secrets/credentials in-repo |

### Audience
- Primary: Pipeline engineers, maintainers, CI/CD owners, data stewards
- Secondary: Story node authors/editors, reviewers, contributors (PR authors)

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Tool**: A repo-tracked utility whose purpose is to run or support governed pipeline work.
  - **Run ID**: A unique identifier for a tool execution used in logs/provenance.
  - **Idempotency**: Re-running produces the same outputs (or clean no-op) for the same inputs.
  - **Staging**: Required lifecycle: `data/raw/ → data/work/ → data/processed/ → data/stac/` (+ `data/reports/` as needed).
  - **Catalogs**: STAC (asset-level), DCAT (dataset view), PROV-O (lineage).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Tools index | `tools/README.md` | TBD | Entry points, quickstart, per-tool run recipes |
| Tools architecture | `tools/ARCHITECTURE.md` | TBD | This doc |
| Master guide | `docs/MASTER_GUIDE_v12.md` | TBD | Canonical pipeline + invariants |
| Pipeline code | `src/pipelines/` | TBD | Production ETL/transforms/catalog build |
| Catalog outputs | `data/stac/` + `docs/data/` | TBD | Machine-validated catalogs + mappings |
| Schemas | `schemas/` | TBD | STAC/DCAT/PROV + telemetry schemas |
| Runs & experiments | `mcp/` | TBD | Experiment logs, SOPs, runbooks (as applicable) |
| Tests | `tests/` | TBD | Unit + integration + contract tests |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Tool taxonomy and boundaries are explicit (what belongs in tools vs. src)
- [ ] Run artifact contract specified (logs, provenance, outputs)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `tools/ARCHITECTURE.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs |
| Documentation | `docs/` | Canonical governed docs |
| Graph | `src/graph/` | Ontology bindings, migrations, integrity checks |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build + graph build |
| Schemas | `schemas/` | JSON schemas + telemetry schemas |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Developer/operator utilities (this doc governs) |
| Frontend | `web/` | React + map clients |
| MCP | `mcp/` | Experiments, model cards, SOPs |
| CI / workflows | `.github/` | CI pipelines + policy gates |

### Expected file tree for this sub-area
> NOTE: This is a **recommended layout**; actual tool inventory may differ (not confirmed in repo).

~~~text
📁 tools/
├── 📄 README.md
├── 📄 ARCHITECTURE.md
├── 📁 _shared/                 # shared CLI helpers (logging, config load, run-id)
│   └── 📄 <module>.py
├── 📁 etl/                     # wrappers/helpers for ETL-stage activities
│   ├── 📄 <tool_name>.py
│   └── 📄 <tool_name>.md       # optional runbook for tool (inputs/outputs/risks)
├── 📁 catalogs/                 # STAC/DCAT/PROV generation + validation helpers
│   ├── 📄 <tool_name>.py
│   └── 📁 validators/
│       └── 📄 <tool_name>.py
├── 📁 graph/                    # graph load/export/verification helpers
│   └── 📄 <tool_name>.py
├── 📁 qa/                       # repo-wide validation + lint helpers
│   └── 📄 <tool_name>.py
└── 📁 packaging/                # release/export bundling helpers
    └── 📄 <tool_name>.py
~~~

## 🧭 Context

### Background
KFM is a multi-stage, governance-first system. As the number of datasets, catalogs, graph entities, and narrative products grows, “one-off scripts” become a major source of risk (non-reproducible outputs, missing provenance, inconsistent folder placement, and accidental policy violations). The `tools/` directory exists to make utility work **first-class and governed**.

### Assumptions
- Tools are invoked by humans and CI/CD (local + automated).
- Tools are expected to be cross-platform where practical (path-safe, deterministic).
- Implementation language/framework is **not confirmed in repo**; examples in this doc use generic CLI language and pseudo-structures.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Required data staging is preserved: `data/raw/ → data/work/ → data/processed/ → data/stac/` (+ `data/reports/` as needed).
- Frontend consumes contracts via **APIs** (no direct graph dependency).
- No secrets/credentials in repo; tools must rely on secure runtime injection (env/secret stores).

### Tool taxonomy (governed categories)
| Category | What it does | Must write to | Must emit |
|---|---|---|---|
| Ingestion helpers | Fetch/normalize external sources into staging | `data/raw/` (and/or `data/work/`) | Run log + input source identifiers |
| ETL runners/wrappers | Invoke ETL modules/configs; transform raw → processed | `data/work/`, `data/processed/` | Run manifest + deterministic output hashes |
| Catalog builders | Generate/refresh STAC/DCAT/PROV catalogs | `data/stac/` (+ `docs/data/` mappings if used) | Schema validation results + catalog diffs |
| Graph loaders | Load validated catalog/processed data into graph | Graph store (via governed loaders) | PROV activity/run ID + migration/version ref |
| QA/validation | Lint docs, validate schemas, geometry checks | `data/reports/` (optional) | Machine-readable validation report |
| Packaging/export | Build release bundles, subsets, or shareable artifacts | `releases/` or `data/reports/` | Manifest of included datasets + versions |

### Tool contract (minimum requirements)
All tools under `tools/` MUST:
1. **Be config-driven** (no hard-coded paths/URLs that can’t be overridden).
2. **Be deterministic** when given the same inputs/config/version.
3. **Be idempotent** (safe re-run) or clearly mark when not.
4. **Write outputs only to approved locations** and never to `src/` or `docs/templates/`.
5. **Produce a run manifest** with:
   - run_id, timestamp, tool name/version
   - git commit sha (or container image digest)
   - input identifiers/hashes
   - output identifiers/hashes
   - validation status
6. **Fail fast** on schema/validation failures (no silent partial success).
7. **Never log secrets** and redact sensitive location details when required.

### Where business logic must live
- `tools/` should be **thin wrappers** around reusable modules.
- Reusable implementation code belongs in:
  - `src/pipelines/` (ETL/transforms/catalog build)
  - `src/graph/` (graph loaders, ontology bindings, migrations)
  - `schemas/` (formal contracts)
- Tools may import from `src/` to run modules, but should not duplicate pipeline logic.

### Execution model
Recommended interface conventions (adapt to actual repo tooling):
- Standard flags:
  - `--config <path>` (required for non-trivial tools)
  - `--run-id <id>` (optional; generated if absent)
  - `--dry-run` (recommended default for destructive operations)
  - `--output-dir <path>` (when output location is user-selected)
  - `--force/--overwrite` (explicit override)
- Standard exit behavior:
  - `0` success
  - `>0` failure (validation errors, missing inputs, policy gate failures)

### Idempotency & caching
- Prefer checksum-based caching:
  - If inputs + config + tool version are unchanged, tool should:
    - skip work, or
    - confirm the existing output matches expected hashes, then return success.
- Avoid “hidden state” outside the repo’s governed paths.

### Logging & provenance
Minimum artifacts per run (recommended):
- `data/work/<tool>/<run_id>/run.json` (manifest)
- `data/work/<tool>/<run_id>/logs.txt` (human-readable log)
- `data/work/<tool>/<run_id>/prov.jsonld` (PROV-O bundle or reference)
- `data/reports/<tool>/<run_id>/validation.json` (if validation performed)

Example manifest shape (illustrative; schema not confirmed in repo):
~~~json
{
  "run_id": "TBD",
  "tool": "tools/<category>/<tool_name>",
  "commit_sha": "<latest-commit-hash>",
  "started_at": "2025-12-18T00:00:00Z",
  "inputs": [{ "id": "TBD", "hash": "sha256:TBD" }],
  "outputs": [{ "id": "TBD", "hash": "sha256:TBD", "path": "TBD" }],
  "validations": [{ "name": "schema", "status": "pass|fail", "details": "TBD" }]
}
~~~

### Safety model
- Default behavior is **non-destructive**.
- Any delete/overwrite action requires explicit opt-in flag and should:
  - confirm target scope is limited to a run directory, and
  - avoid deleting outside `data/work/` or a staging sandbox.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical run-manifest schema + path convention? | TBD | TBD |
| Which tools are “blessed” for CI smoke tests vs. local-only? | TBD | TBD |
| What is the approved mechanism for credentials (env vs. secret store) per environment? | TBD | TBD |

### Future extensions
- Tool registry/index that can be rendered into `tools/README.md` automatically.
- Standardized provenance emitter library in `tools/_shared/`.
- A small “fixture dataset pack” for deterministic CI validation of representative tools.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  Dev[Developer / CI] --> Tool[tools/* CLI]
  Tool --> Cfg[Config + Schemas]
  Tool --> Raw[data/raw]
  Tool --> Work[data/work]
  Tool --> Proc[data/processed]
  Proc --> Cat[STAC/DCAT/PROV<br/>data/stac + docs/data]
  Cat --> Graph[Neo4j Graph]
  Graph --> API[API Layer]
  API --> UI[React/Map UI]
  UI --> Story[Story Nodes]
  Story --> Focus[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant User
  participant Tool as tools/<category>/<tool>
  participant FS as data/*
  participant Cat as Catalog Builder/Validator
  User->>Tool: run --config cfg.yml --run-id X
  Tool->>FS: read inputs (raw/work)
  Tool->>FS: write outputs (work/processed)
  Tool->>Cat: generate + validate STAC/DCAT/PROV
  Cat-->>Tool: validation pass/fail + reports
  Tool-->>User: exit code + run manifest location
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Tool config | YAML/JSON | `tools/` or `docs/` (repo-defined) | schema/lint (as applicable) |
| Raw source data | files/archives/APIs | external sources → `data/raw/` | checksums + size/type checks |
| Schemas | JSON Schema | `schemas/` | version-pinned in CI |
| Governance refs | Markdown | `docs/governance/` | link check (optional) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed artifacts | GeoTIFF/GeoJSON/CSV/etc. | `data/processed/` | domain schemas (TBD) |
| Work artifacts | intermediate files | `data/work/` | run manifest contract |
| Catalog artifacts | JSON/JSON-LD | `data/stac/` + `docs/data/` | KFM-STAC/KFM-DCAT/KFM-PROV |
| Validation reports | JSON/Markdown | `data/reports/` | report schema (TBD) |

### Sensitivity & redaction
- If a tool handles culturally sensitive locations or restricted data:
  - do not emit precise coordinates to public outputs,
  - store sensitive runs under a restricted path (policy-defined; not confirmed in repo),
  - ensure logs do not contain raw sensitive attributes.

### Quality signals
- Schema validation (STAC/DCAT/PROV; domain schemas)
- Geometry validity checks (e.g., polygon validity, CRS expectations)
- Checksums for inputs/outputs
- Determinism checks on representative fixtures in CI

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Tools that produce or modify spatiotemporal assets should:
  - update/create a STAC **Collection** for the dataset, and
  - create/update STAC **Item(s)** for produced assets.
- Assets must be linkable to concrete output files and include spatial/temporal extents.

### DCAT
- Tools must ensure dataset-level metadata exists (minimum):
  - title, description, license, keywords
  - publisher/contact mapping (if applicable)
- DCAT is the interoperability view; do not treat it as optional when a dataset is published.

### PROV-O
- Each tool run should map to a PROV **Activity**:
  - `prov:used` for inputs (raw sources, configs, prior artifacts)
  - `prov:wasGeneratedBy` for outputs
  - `prov:generatedAtTime` timestamp
  - an **Agent** identity for the tool + executor (where policy allows)

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- When outputs are superseded:
  - keep prior versions addressable (where storage policy allows),
  - link lineage in STAC + graph.

### Extension points checklist (for future work)
- [ ] Tool: new tool added under `tools/<category>/` and indexed in `tools/README.md`
- [ ] Data: staging preserved (`data/raw/ → data/work/ → data/processed/`)
- [ ] STAC: new/updated collection + item validation added
- [ ] PROV: activity + agent identifiers recorded per run
- [ ] Graph: if tool affects graph, migrations + integrity checks included
- [ ] APIs: if tool changes served outputs, contract versioning considered
- [ ] UI: if tool adds a layer/export, registry + access rules updated
- [ ] Focus Mode: provenance references enforced (no orphan artifacts)
- [ ] Telemetry: new signals + schema version bump (if applicable)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Tools do not directly generate Focus Mode narratives.
- Tools produce datasets, catalogs, and reports that become focusable only after:
  1) catalog validation,
  2) graph ingestion/mapping,
  3) API exposure (contracted),
  4) UI layer registration,
  5) Story Node linkage (when narrative is required).

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- If a tool generates any narrative-ish output (reports, summaries), it must:
  - include provenance pointers,
  - clearly label derived/estimated fields,
  - avoid unsourced claims.

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
- [ ] Graph integrity checks (when applicable)
- [ ] API contract tests (when applicable)
- [ ] UI schema checks (layer registry) (when applicable)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate schemas (STAC/DCAT/PROV)
# <repo-cmd> validate catalogs

# 2) run unit/integration tests
# <repo-cmd> test

# 3) run markdown protocol lint
# <repo-cmd> lint docs
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| tool_run_id | tool manifest | `docs/telemetry/` + `schemas/telemetry/` |
| validation_status | validators | `data/reports/` |
| bytes_written | filesystem | `data/reports/` or telemetry store (TBD) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to tools that:
  - touch sensitive data,
  - modify catalogs,
  - modify graph ingestion paths,
  - or impact public outputs
  should require explicit review (security + data governance as applicable).

### CARE / sovereignty considerations
- Identify communities impacted and protection rules.
- If tools process Indigenous or sovereignty-scoped data, ensure:
  - appropriate access controls,
  - redaction/generalization rules,
  - consent/consultation requirements (per `docs/governance/SOVEREIGNTY.md`).

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Tools that use AI/ML must record:
  - model identifiers/versions,
  - prompts/configs (as allowed),
  - evaluation/uncertainty metadata.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial tools architecture doc | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`