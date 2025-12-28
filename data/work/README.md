---
title: "KFM — data/work README"
path: "data/work/README.md"
version: "v1.1.0"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:data:work:readme:v1.1.0"
semantic_document_id: "kfm-data-work-readme-v1.1.0"
event_source_id: "ledger:kfm:doc:data:work:readme:v1.1.0"

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

# data/work — Intermediate Artifacts

> **Purpose (required):** Define what belongs in `data/work/`, how intermediate artifacts must be produced (deterministic + reproducible), and how they are promoted to `data/processed/` for cataloging (STAC/DCAT/PROV), graph ingestion, APIs, and downstream UI/Story/Focus experiences.

## 📘 Overview

### Purpose

This README is the **placement contract** for `data/work/`:

- define **what may exist** in `data/work/` (and what must not),
- enforce **determinism + idempotence** for intermediate artifacts,
- prevent intermediate files from becoming accidental “truth” by defining **promotion rules** into `data/processed/`,
- ensure downstream stages (catalogs → graph → APIs → UI → Story Nodes → Focus Mode) can rely on **stable, provenance-linked evidence artifacts**, not ad hoc work outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Intermediate artifacts produced during transforms, joins, normalization, QA, and staging | Immutable raw snapshots (belongs in `data/raw/`) |
| Per-domain organization under `data/work/<domain>/` | Canonical “certified” outputs (belongs in `data/processed/`) |
| Run-scoped output folders, minimal manifests, and checksums | Authoring catalogs (belongs in `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| Promotion checklist from work → processed | Writing governance policy (belongs in `docs/governance/`) |

### Audience

- **Primary:** ETL / data pipeline contributors implementing deterministic ingest, normalization, and QA.
- **Secondary:** Maintainers and governance reviewers auditing lineage and publication readiness.
- **Tertiary:** Story authors verifying that narrative evidence points to processed + cataloged artifacts.

### Definitions

- Link: `docs/glossary.md` (**not confirmed in repo**)
- Key terms used in this doc:
  - **raw / work / processed**
  - **determinism / idempotence**
  - **run_id**
  - **promotion**
  - **manifest**
  - **redaction**
  - **provenance (STAC/DCAT/PROV)**

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical lifecycle + “do not break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Required sections + front-matter |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | KFM Core | Evidence + narrative contract |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical homes; CI alignment |
| ETL / transforms | `src/pipelines/` | Data Eng | Deterministic, idempotent runs |
| Schemas (STAC/DCAT/PROV + contracts) | `schemas/` | Data/Platform | Schema lint + validation gates |
| Canonical processed outputs | `data/processed/` | Data Eng | Certified artifacts depended on downstream |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Catalog Build | Machine-validated catalogs + lineage bundles |
| Run manifests / run logs | `mcp/runs/` | Maintainers | Prefer pointers; avoid duplicating large artifacts |

### Definition of done

- [ ] Front-matter complete + valid (`path` matches file location).
- [ ] Work-stage placement rules are explicit and actionable (MUST/SHOULD wording where appropriate).
- [ ] Run folder expectations are documented (manifest + parameters + checksums).
- [ ] Promotion-to-processed checklist is repeatable and testable.
- [ ] Governance + CARE/sovereignty considerations are explicit and referenced.
- [ ] Story/Focus rule is explicit: **do not cite `data/work/**` as evidence**.

## 🗂️ Directory Layout

### This document

- `path`: `data/work/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Raw staging | `data/raw/` | Immutable source snapshots (append-only; never edited in place) |
| Work staging | `data/work/` | Intermediate artifacts (reproducible; safe to delete/rebuild) |
| Processed staging | `data/processed/` | Canonical outputs for catalogs + graph ingest (schema-validated; versioned) |
| STAC | `data/stac/` | STAC Collections + Items |
| DCAT | `data/catalog/dcat/` | DCAT dataset records (JSON-LD / TTL as adopted) |
| PROV | `data/prov/` | PROV lineage bundles (per run / per dataset) |
| Domain governance | `data/<domain>/governance/` | Domain-specific governance docs and decisions (**not confirmed in repo**) |
| Pipelines | `src/pipelines/` | ETL + catalog builders + transforms |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, graph build, import fixtures |
| API boundary | `src/server/` | Contracts, redaction rules, query services (**canonical in v13**) |
| UI | `web/` | React/MapLibre UI (must not read Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Draft/published story nodes (**canonical in v13**) |

### Expected file tree for this sub-area

> This is the **recommended** structure. Some directories may not exist yet (**not confirmed in repo**).

~~~text
📁 data/
├── 📁 raw/
│   └── 📁 <domain>/                         # immutable source snapshots (append-only)
├── 📁 work/
│   ├── 📄 README.md                         # you are here
│   └── 📁 <domain>/                         # intermediate artifacts (reproducible; safe to delete/rebuild)
│       ├── 📁 <run_id>/                     # run-scoped output folder (recommended)
│       │   ├── 📄 manifest.json             # inputs/params/outputs pointers (recommended)
│       │   ├── 📄 manifest.sha256           # output checksums (recommended)
│       │   ├── 📁 artifacts/                # pipeline-defined intermediate outputs
│       │   └── 📁 qa/                       # lightweight QA outputs that justify promotion decisions
│       └── 📁 _notes/                       # human notes (optional; keep lightweight)
├── 📁 processed/
│   └── 📁 <domain>/                         # canonical processed outputs (schema-validated; versioned)
├── 📁 stac/
│   └── 📁 <domain>/                         # STAC Collections/Items for the domain (layout domain-defined)
├── 📁 catalog/
│   └── 📁 dcat/                             # DCAT dataset records
├── 📁 prov/                                 # PROV bundles (per run / per dataset)
└── 📁 reports/
    └── 📁 <domain>/                         # optional analysis outputs (domain-defined)
~~~

## 🧭 Context

### Background

KFM uses a staged lifecycle for traceability and reproducibility:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (+ `data/reports/` as needed)

The `data/work/` stage exists to support **deterministic, idempotent transformations** while keeping `data/raw/` immutable and `data/processed/` trustworthy, diffable, and safe to depend on downstream.

### Assumptions

- Work artifacts are **regenerable** from raw inputs + pipeline configuration + parameters.
- Pipelines record enough run metadata to reproduce outputs (at minimum: inputs, parameters, and commit reference).
- Domain-level staging follows `data/<domain>/...` conventions (domain pack concept in v13).

### Constraints / invariants

- **Canonical pipeline order is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **API boundary is enforced:** Frontend consumes contracts via APIs (no direct graph dependency).
- **Raw is immutable; processed is canonical; work is non-canonical.**
- **No unsourced narrative:** Story Nodes / Focus Mode must cite catalog + provenance identifiers, not work-stage files.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we keep any work artifacts in git, or are they always reproducible build outputs? | TBD | TBD |
| Is there (or should there be) a schema for `manifest.json` under `schemas/`? | TBD | TBD |
| What is the retention policy for old `run_id/` folders in `data/work/`? | TBD | TBD |

### Future extensions

- Standardize a `manifest.json` schema (and validator) for `data/work/**` (**not confirmed in repo**).
- Add a `tools/` utility to generate checksum manifests and promotion reports (**not confirmed in repo**).
- Add CI checks that enforce “no downstream dependencies on `data/work/**` paths” (**not confirmed in repo**).

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  RAW["data/raw/<domain>/"] --> WORK["data/work/<domain>/<run_id>/"]
  WORK --> PROC["data/processed/<domain>/"]
  PROC --> CAT["data/stac/ + data/catalog/dcat/ + data/prov/"]
  CAT --> GRAPH["Neo4j Graph"]
  GRAPH --> API["API Layer"]
  API --> UI["UI — React/MapLibre"]
  UI --> STORY["Story Nodes"]
  STORY --> FOCUS["Focus Mode"]
~~~

### Optional: sequence diagram (promotion)

~~~mermaid
sequenceDiagram
  participant ETL as ETL Pipeline
  participant WORK as data/work
  participant PROC as data/processed
  participant CAT as STAC/DCAT/PROV
  ETL->>WORK: emit intermediates + manifest + checksums
  ETL->>ETL: validate + QA
  ETL->>PROC: promote certified outputs
  ETL->>CAT: write/update catalogs + provenance
~~~

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw snapshots | domain-defined | `data/raw/<domain>/` | source-level checks + basic integrity |
| Pipeline config | YAML/JSON/etc | `src/pipelines/` | config schema if present |
| Run parameters | CLI/manifest | `data/work/<domain>/<run_id>/manifest.json` | validate types/required params (**not confirmed in repo**) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Intermediate artifacts | CSV/Parquet/GeoJSON/etc | `data/work/<domain>/<run_id>/artifacts/` | pipeline-defined (avoid treating as stable contracts) |
| QA artifacts | Markdown/JSON | `data/work/<domain>/<run_id>/qa/` | lightweight; supports promotion decisions |
| Run manifest | JSON | `data/work/<domain>/<run_id>/manifest.json` | schema **recommended** (**not confirmed in repo**) |
| Checksums | sha256 list | `data/work/<domain>/<run_id>/manifest.sha256` | deterministic hash list |

### What belongs in `data/work/`

Typical intermediate artifacts (pipeline-defined):

- parsed/normalized tables prior to certification,
- cleaned or reprojected spatial layers (intermediate forms),
- intermediate joins/enrichment outputs,
- deduplicated entity tables before ID stabilization,
- QA summaries supporting promotion decisions.

### What must not live in `data/work/`

- Immutable raw snapshots (use `data/raw/`).
- Certified / published datasets that downstream systems depend on (use `data/processed/`).
- Catalog outputs (use `data/stac/`, `data/catalog/dcat/`, `data/prov/`).
- Secrets/credentials (never in-repo).
- Non-reproducible “one-off” outputs without manifests (use `data/reports/` or an approved external store — **not confirmed in repo**).

### Minimum metadata per `run_id/` folder (recommended)

Recommended `manifest.json` fields (names are suggestions; exact schema not confirmed in repo):

- `run_id` + timestamp
- pipeline reference (commit SHA, pipeline name/version)
- input inventory (paths + hashes) from `data/raw/<domain>/`
- parameters (including fixed random seeds if used)
- output inventory (paths + hashes) under `data/work/<domain>/<run_id>/`
- promotion status: `draft` / `candidate` / `promoted` (**recommended**)

### Sensitivity & redaction

- Treat intermediate join/enrichment outputs conservatively: derived products can increase sensitivity even if sources are open.
- Before promotion:
  - scan for unintended PII,
  - ensure locations/coordinates do not violate sovereignty constraints,
  - ensure redaction rules are implemented at the **API boundary** when needed.

### Quality signals

Recommended checks (domain-dependent):

- schema conformance (where schemas exist),
- geometry validity and CRS correctness (for spatial data),
- referential integrity (stable IDs, no orphan records),
- range checks (dates, numeric fields),
- reproducibility (idempotent re-run yields equivalent outputs).

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Work artifacts are **upstream of cataloging** and should not be treated as STAC Items.
- When an artifact is promoted to `data/processed/`, emit or update:
  - STAC Collection(s) for the dataset domain
  - STAC Item(s) for the promoted assets

### DCAT

- DCAT entries should describe **processed datasets** (not intermediate work outputs).
- Minimum mapping expectations: title, description, license, keywords.

### PROV-O

For promoted datasets, ensure lineage captures:

- `prov:wasDerivedFrom`: the raw input identifiers (and/or their hashes)
- `prov:wasGeneratedBy`: the pipeline activity/run identifier
- `prov:wasAssociatedWith`: agent/tool identity (as available)

### Versioning

- New processed dataset versions should link predecessor/successor in catalogs where supported.
- Graph lineage should mirror dataset version lineage (predecessor/successor relationships).

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run manifests + outputs in `data/**` |
| Catalogs | STAC/DCAT/PROV | Validated JSON/JSON-LD + provenance bundles |
| Graph | Neo4j | Built from cataloged/processed artifacts; queried only via APIs |
| APIs | Serve contracts + apply policy | REST/GraphQL contracts + contract tests |
| UI | Map + narrative | API calls (no direct graph dependency) |
| Story Nodes | Curated narrative | Provenance-linked evidence + templates |
| Focus Mode | Contextual synthesis | Provenance-linked context bundles |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog (**recommended**) |
| Pipeline code | `src/pipelines/` | Deterministic behavior; idempotent reruns |
| Graph ingest mappings | `src/graph/` | Ontology-governed; stable labels/edges |
| API contracts | `src/server/` | Backward compat or version bump |
| UI layer registry | `web/` | Schema-validated registry (**not confirmed in repo**) |

### Extension points checklist (domain pack)

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] Work: deterministic intermediate outputs + manifest + checksums
- [ ] Processed: certified dataset version emitted
- [ ] Catalogs: STAC Collection/Items + DCAT + PROV created/updated
- [ ] Graph: new labels/relations mapped + migration plan (if needed)
- [ ] APIs: contract version bump + tests (if needed)
- [ ] UI: layer registry entry + access rules (if needed)
- [ ] Story: at least one Story Node that cites processed + catalog IDs

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Focus Mode must surface **processed + cataloged** evidence artifacts (STAC/DCAT/PROV).
- Intermediate artifacts in `data/work/**` are not valid evidence anchors.

### Provenance-linked narrative rule

- Every narrative claim must trace to a dataset/record/asset identifier that resolves through catalogs and provenance.
- If a claim depends on a transformation step, the relevant PROV activity/run should be discoverable.

### Optional structured controls (not typically used for work-stage docs)

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps

Work-stage (always):

- [ ] Work artifacts are reproducible from raw inputs (idempotent pipeline rerun yields equivalent outputs).
- [ ] `manifest.json` exists and records inputs + parameters + outputs pointers.
- [ ] `manifest.sha256` exists for artifacts intended to be compared or promoted.
- [ ] No secrets/credentials present.

Promotion-stage (only when moving to `data/processed/`):

- [ ] Processed outputs validated against applicable schemas.
- [ ] STAC/DCAT/PROV outputs emitted/updated and validated to project profiles.
- [ ] Dataset versioning metadata updated (predecessor/successor where applicable).
- [ ] Governance review triggered if sensitivity/classification changes.

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run a pipeline step that produces work artifacts
# python -m src.pipelines.<domain>.ingest --run-id <run_id>

# 2) Generate or update a hash manifest (recommended)
# python tools/hash_manifest.py data/work/<domain>/<run_id>/artifacts > data/work/<domain>/<run_id>/manifest.sha256

# 3) Promote to processed only after validation
# python -m src.pipelines.<domain>.promote_to_processed --run-id <run_id>
~~~

### Telemetry signals (if applicable)

> Recommended only; schema/location not confirmed in repo.

| Signal | Source | Where recorded |
|---|---|---|
| `work_artifact_emitted` | ETL | `mcp/runs/<run_id>/` (pointer-based) |
| `promotion_to_processed` | ETL | `mcp/runs/<run_id>/` + PROV activity |
| `promotion_blocked` | validation/gov scan | `mcp/runs/<run_id>/` |

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:

- introducing a new dataset source,
- changing classification/sensitivity labels,
- publishing any dataset derived from sensitive/restricted inputs,
- adding a UI layer that could reveal sensitive locations by interaction/zoom.

### CARE / sovereignty considerations

- Identify communities impacted and protection rules.
- If a dataset includes culturally sensitive locations, do not publish precise coordinates without an approved sovereignty plan.

### AI usage constraints

This README’s AI permissions/prohibitions are in front-matter. AI may assist with summarization and structure extraction, but must not be used to generate policy or infer sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.1.0 | 2025-12-28 | Rewritten to conform to universal template; tightened placement + promotion contracts; clarified Story/Focus evidence rules | TBD |
| v1.0.0 | 2025-12-26 | Initial `data/work/` README defining intermediate-artifact rules and promotion guidance | TBD |

---

Footer refs:
- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- v13 blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
