---
title: "KFM tools/dev — Developer Tooling"
path: "tools/dev/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-22"
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

doc_uuid: "urn:kfm:doc:tools-dev-readme:v1.0.0-draft"
semantic_document_id: "kfm-tools-dev-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:tools-dev-readme:v1.0.0-draft"
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

# tools/dev — Developer Tooling

## 📌 Summary

### Change summary

- Adds a governed README for `tools/dev/` explaining what belongs here, what does not, and how developer tooling should align with KFM’s pipeline contracts.

### Why this matters

- KFM’s canonical pipeline ordering is non-negotiable. Developer tooling should support the pipeline and its contracts without introducing alternate sources of truth.
- A clear `tools/dev/` scope reduces onboarding friction and helps contributors reproduce CI gates locally.

## 🗂 Directory Layout

### This document

- `path`: `tools/dev/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Dev tooling | `tools/` | Utilities for development, operations, and repo maintenance |
| Pipelines | `src/pipelines/` | ETL jobs, transforms, catalog builders, graph build inputs |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC/DCAT/PROV evidence artifacts |
| Graph | `src/graph/` | Ontology bindings, ingest, migrations |
| API boundary | `src/server/` | Contracted access layer, redaction, access controls |
| Frontend | `web/` | React/Map UI (consumes APIs, not direct-to-graph) |
| Schemas | `schemas/` | STAC/DCAT/PROV/Story Node/UI/Telemetry schemas |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts and Focus Mode sources |

### Expected file tree for this sub-area

~~~text
📁 tools/
└── 📁 dev/
    ├── 📄 README.md
    ├── 📁 scripts/                # Optional: local dev utilities (lint, validate, smoke tests)
    ├── 📁 ci/                     # Optional: local entrypoints mirroring CI gates
    ├── 📁 docker/                 # Optional: local-only Docker/Compose helpers
    ├── 📁 fixtures/               # Optional: small, non-sensitive test fixtures for tooling
    └── 📁 docs/                   # Optional: tool-specific notes, scoped to dev tooling
~~~

## 🧭 Context

### Scope

- Developer-only utilities: validation, formatting, local orchestration, and reproducibility helpers.
- Scripts in this folder may read repository artifacts across stages, but should not become a second implementation of a canonical subsystem (ETL, catalogs, graph, API, UI).

### Non-goals

- Shipping production services or runtime code from `tools/dev/`.
- Defining new pipeline policies or contracts. Canonical rules belong in governed docs (e.g., `docs/MASTER_GUIDE_v12.md`).

### Key invariants

- Pipeline ordering remains canonical and must not be bypassed.
- `web/` must not query Neo4j directly; graph access is via the API boundary.
- Derived data outputs are not code: if a tool generates datasets, they belong under `data/<domain>/processed/` and require STAC/DCAT/PROV plus validation.

## 🗺️ Diagrams

### Typical local workflow

~~~mermaid
flowchart LR
  DEV[Developer] --> TOOL[tools/dev script]
  TOOL --> LINT[Repo lint and markdown protocol]
  TOOL --> SCHEMA[Schema validation<br/>schemas/*]
  TOOL --> TESTS[Unit and integration tests]
  SCHEMA --> ARTIFACTS[Artifacts validated<br/>data/stac + data/catalog/dcat + data/prov]
  TESTS --> PR[Pull request]
  LINT --> PR
  ARTIFACTS --> PR
~~~

## 📦 Data & Metadata

### Inputs

- Repository source code and configs (e.g., `src/`, `web/`, `schemas/`)
- Repository artifacts to validate (e.g., `data/stac/`, `data/catalog/dcat/`, `data/prov/`)
- Optional local environment variables for local testing
  - Do not commit secrets or credentials

### Outputs

- Human-readable reports (lint output, schema validation results, test summaries)
- Temporary build artifacts
  - Keep local and ignored, or place in a clearly-scoped workspace
- If a tool emits formal artifacts that participate in the pipeline (catalogs, provenance bundles), write them to canonical locations and ensure they validate

### Schemas and contracts touched

- STAC schemas: `schemas/stac/`
- DCAT schemas: `schemas/dcat/`
- PROV schemas: `schemas/prov/`
- Story Node schemas: `schemas/storynodes/`
- UI layer registry schemas: `schemas/ui/`
- Telemetry schemas: `schemas/telemetry/`

## 🌐 STAC, DCAT, and PROV alignment

### What dev tools may validate

- STAC Collections and Items (`data/stac/**`)
- DCAT dataset records (`data/catalog/dcat/**`)
- PROV lineage bundles (`data/prov/**`)

### Notes

- This folder should not define alternative “mini-profiles” for STAC/DCAT/PROV.
- If new constraints are needed, they belong in `schemas/` and the appropriate governed standard docs.

## 🧱 Architecture

### Where dev tooling sits in the system

- `tools/dev/` is supportive infrastructure: it helps contributors run validations and reproduce CI gates locally.
- Canonical subsystem homes remain:
  - ETL + transforms: `src/pipelines/`
  - Graph: `src/graph/`
  - API boundary and contracts: `src/server/`
  - UI: `web/`

### Recommended conventions

> These are recommended conventions for `tools/dev/` and may require maintainer review if adopted as enforced policy.

- Prefer explicit, self-documenting entrypoints
  - Each script should have `--help` usage and clear “what it changes” messaging
- Prefer safe defaults
  - Read-only validation by default
  - If writing, require an explicit apply flag (e.g., `--write`, `--apply`) and document outputs
- Keep outputs diffable and reproducible
  - Deterministic operations where possible (fixed seeds, stable ordering, pinned versions)
- Never introduce forbidden boundaries
  - No UI direct-to-graph access
  - Keep tooling aligned with API contracts and schema validations

### Extension points checklist

- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

### Risks

- Accidental modification of pipeline artifacts (especially `data/processed/` and `data/stac/**`) leading to non-reproducible diffs
- Introducing tooling that bypasses contracts (e.g., direct writes into Neo4j without provenance)

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Tools in this folder may include validators to ensure Story Nodes:
  - have valid front matter
  - reference existing evidence IDs
  - comply with redaction and sovereignty rules

### Provenance-linked narrative rule

- Every Story Node claim shown in Focus Mode must trace to a dataset, record, or asset ID.

### Optional structured controls

~~~yaml
# Optional defaults for local Focus Mode previews, if implemented
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
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
# Example placeholders — replace with repo-specific commands.

# 1) run doc + markdown protocol checks
# <command>

# 2) validate schemas against artifacts (STAC/DCAT/PROV/storynodes/ui)
# <command>

# 3) run unit and integration tests
# <command>
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| TBD | TBD | `docs/telemetry/` + `schemas/telemetry/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Changes that alter validation gates, schema checks, or data-writing behavior should be reviewed by maintainers for the affected subsystem.
- Tooling that touches redaction, sensitivity, or sovereignty controls requires governance review.

### CARE / sovereignty considerations

- Ensure tooling does not expose or export restricted locations or culturally sensitive information.
- If tooling produces reports or artifacts, treat them as governed outputs when they contain sensitive content.

### AI usage constraints

- Ensure tooling that generates summaries or narratives does not bypass the “no unsourced narrative” rule.
- Any AI-generated content must be explicitly marked and provenance-linked where applicable.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-22 | Initial `tools/dev/` README scaffold | TBD |

---

Footer refs:

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

