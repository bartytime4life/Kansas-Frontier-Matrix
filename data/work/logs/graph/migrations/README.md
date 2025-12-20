---
title: "KFM — Graph Migration Logs (data/work/logs/graph/migrations)"
path: "data/work/logs/graph/migrations/README.md"
version: "v1.0.0"
last_updated: "2025-12-20"
status: "active"
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

doc_uuid: "urn:kfm:doc:data:work:logs:graph:migrations:readme:v1.0.0"
semantic_document_id: "kfm-data-work-logs-graph-migrations-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:logs:graph:migrations:readme:v1.0.0"
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

# Graph Migration Logs (`data/work/logs/graph/migrations/`)

## 📘 Overview

### Purpose
This directory stores **run artifacts for graph/Neo4j migrations** (schema/constraints/labels/relationships/ontology bindings) executed by KFM pipeline or ops workflows. Each migration should be traceable, repeatable, and auditable via stored inputs, outputs, and checks.

### Scope
| In Scope | Out of Scope |
|---|---|
| Migration run logs, manifests, pre/post checks, exported summaries, rollback notes | Secrets/credentials, raw source datasets, long-lived canonical schemas (these belong in `schemas/` and `src/graph/`) |

### Audience
- Primary: maintainers running graph migrations; reviewers validating graph integrity
- Secondary: contributors trying to understand “what changed” and “why”

### Definitions (link to glossary)
- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc: migration, run_id, rollback, constraint, index, ontology, provenance

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Graph migration logs | `data/work/logs/graph/migrations/` | Graph/Ops | This folder |
| Graph checks logs | `data/work/logs/graph/checks/` | Graph/Ops | Pre/post validation output |
| Graph exports (optional) | `data/work/logs/graph/exports/` | Graph/Ops | Optional snapshots / dumps |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Expected tree + conventions are explicit
- [ ] No secrets/PII are suggested or stored
- [ ] Reproduction steps are listed (even if command names are TBD)

## 🗂️ Directory Layout

### This document
- `path`: `data/work/logs/graph/migrations/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data work/logs | `data/work/logs/` | Execution logs and validation artifacts |
| Graph subsystem | `src/graph/` | Graph build + ontology bindings + migration code *(exact migration script layout not confirmed in repo)* |
| Schemas | `schemas/` | JSON schemas + telemetry schemas *(and any machine-validated log schemas, if used)* |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 logs/
        └── 📁 graph/
            └── 📁 migrations/
                ├── 📄 README.md
                ├── 📁 20251220_1425__add_place_geom_index__v1/
                │   ├── 📄 manifest.yaml
                │   ├── 📄 plan.md
                │   ├── 📄 apply.log
                │   ├── 📄 checks.pre.json
                │   ├── 📄 checks.post.json
                │   ├── 📄 rollback.md
                │   └── 📄 rollback.log
                └── 📁 _archive/   (optional; for retired/merged runs)
~~~

## 🧭 Context

### Background
KFM’s canonical pipeline routes curated catalogs into the graph layer; when graph structure changes, migrations must be recorded as **explicit, reviewable artifacts** so that downstream APIs/UI remain contract-stable and provenance remains intact.

### Assumptions
- Graph migrations are executed via a controlled workflow (CI or operator-run).
- Each migration has a unique identifier and produces a repeatable log bundle.

### Constraints / invariants
- Preserve canonical pipeline ordering: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- Frontend consumes graph only via APIs (no direct graph dependency).
- Do not store secrets, tokens, or private endpoints in logs.
- If sensitive data could appear in output (e.g., protected site coordinates), store only generalized/redacted forms per governance docs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Are migration logs committed to git or kept as build artifacts only? | TBD | TBD |
| Do we validate `manifest.yaml` against a schema in `schemas/`? | TBD | TBD |
| Where are canonical migration scripts stored under `src/graph/`? | TBD | TBD |

## 📦 Data & Metadata

### Per-migration bundle (recommended)
**Folder name pattern**
- `YYYYMMDD_HHMM__<slug>__v<N>` (example above)

**`manifest.yaml` (recommended fields)**
~~~yaml
migration_id: "20251220_1425__add_place_geom_index__v1"
run_id: "<pipeline-run-id-or-ops-run-id>"
requested_by: "<github-handle-or-service>"
executed_by: "<github-handle-or-service>"
environment: "<dev|staging|prod|local>"
graph_target: "<neo4j-db-name-or-alias>"
git_commit_sha: "<commit-hash>"
started_at: "2025-12-20T14:25:00Z"
ended_at: "2025-12-20T14:31:00Z"

change_kind:
  - "constraint"
  - "index"
  - "label_or_rel_type"
  - "property_backfill"
  - "ontology_binding"

inputs:
  scripts:
    - "<path-to-script-or-inline-ref>"
  configs:
    - "<path-to-config-or-inline-ref>"

outputs:
  logs:
    - "apply.log"
    - "rollback.log"
  checks:
    pre: "checks.pre.json"
    post: "checks.post.json"

prov:
  prov_wasGeneratedBy: "<prov-activity-id>"
  prov_used: ["<prov-entity-id-1>", "<prov-entity-id-2>"]
notes: "TBD"
~~~

### Checks (recommended)
- Pre-migration: connectivity, constraint/index inventory, sample query health checks, record counts.
- Post-migration: constraint/index verification, schema invariants, API contract smoke tests (if applicable), graph integrity checks.

*(Exact check suite is repo-defined; store outputs under `checks.pre.*` and `checks.post.*`.)*

## 🌐 STAC, DCAT & PROV Alignment

### PROV-O linkage (recommended)
- Record `prov:wasGeneratedBy` as the migration activity/run.
- Record `prov:used` for migration scripts/configs and any referenced catalog versions.
- If a migration rewrites entity IDs or merges nodes, ensure version lineage is preserved and cross-referenced in graph/provenance outputs.

## 🧪 Validation & CI/CD

### Validation checklist (per migration)
- [ ] `manifest.yaml` present and complete (or justified if absent)
- [ ] `apply.log` captured (and `rollback.*` captured if executed)
- [ ] Pre/post checks saved
- [ ] No secrets/credentials in artifacts
- [ ] If schema/ontology changed: corresponding docs updated under `docs/graph/` *(path not confirmed in repo)*

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands.
# 1) Run pre-checks
# 2) Apply migration
# 3) Run post-checks
# 4) Export summary (optional)
~~~

## ⚖ FAIR+CARE & Governance

### CARE / sovereignty considerations
If migration artifacts include any location-bearing outputs, ensure they follow classification and redaction rules; do not introduce new sensitive disclosures via logs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-20 | Initial README for graph migration logs | TBD |
---

Footer refs:
- Master pipeline ordering: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
~~~

