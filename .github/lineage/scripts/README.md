---
title: "KFM GitHub Lineage Scripts README"
path: ".github/lineage/scripts/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:github:lineage:scripts-readme:v1.0.0"
semantic_document_id: "kfm-github-lineage-scripts-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:github:lineage:scripts-readme:v1.0.0"
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

# Lineage scripts

## 📘 Overview

### Purpose
- Document the **scripts in `.github/lineage/scripts/`** that support KFM’s CI lineage gates: validating provenance artifacts (PROV) and their alignment with catalog outputs (STAC/DCAT), and producing deterministic, audit-friendly results.
- Establish conventions so lineage checks remain **repeatable, deterministic, and contract-first**.

### Scope

| In Scope | Out of Scope |
|---|---|
| Helper scripts intended to be invoked by GitHub workflows for lineage validation and reporting | Authoring the PROV profile itself |
| Checks that ensure provenance artifacts exist and are internally consistent | Implementing full ETL pipelines |
| Cross-link integrity checks across STAC/DCAT/PROV identifiers | UI or API implementation details |
| Repo lint rules specific to lineage scripts (e.g., no YAML front matter in code files) | Adding new domains’ data content |

### Audience
- Primary: repo maintainers responsible for CI gates, schema validation, and provenance integrity
- Secondary: pipeline authors (ETL, catalogs, graph build) and Story Node curators who rely on provenance guarantees

### Definitions
- Glossary: `docs/glossary.md`
- Terms used in this doc:
  - **Lineage**: the traceable chain from source inputs through transforms to outputs
  - **PROV bundle**: a machine-readable record describing activities, entities, and agents for a run or dataset
  - **Evidence artifact**: downstream-consumable metadata outputs (STAC/DCAT/PROV and derived evidence products)
  - **Deterministic CI**: validation behavior that is stable across runs given the same repo state

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | CI and canonical homes guidance |
| PROV outputs | `data/prov/` | Pipelines + catalogs | PROV bundles (per run / per dataset) |
| STAC outputs | `data/stac/collections/` + `data/stac/items/` | Catalog stage | Catalog artifacts for discovery and downstream usage |
| DCAT outputs | `data/catalog/dcat/` | Catalog stage | Dataset records in JSON-LD |
| Schema roots | `schemas/` | Maintainers | Contract validation inputs (STAC/DCAT/PROV/storynodes/ui/telemetry) |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Script conventions documented (inputs, outputs, exit codes, determinism rules)
- [ ] Validation behavior documented and repeatable (local + CI)
- [ ] Clear separation: scripts are “code files” and must not contain YAML front-matter
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory layout

### This document
- `path`: `.github/lineage/scripts/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| GitHub workflows | `.github/workflows/` | CI jobs that call lineage scripts |
| Lineage hub | `.github/lineage/` | Lineage conventions and shared docs |
| Lineage scripts | `.github/lineage/scripts/` | CI helper scripts for validation and reporting |
| PROV bundles | `data/prov/` | Per-run / per-dataset provenance bundles |
| STAC | `data/stac/` | Collections + items consumed by graph/API/UI |
| DCAT | `data/catalog/dcat/` | Dataset records (JSON-LD) for discovery/export |
| Schemas | `schemas/` | JSON Schema/shape bundles used to validate artifacts |
| Pipelines | `src/pipelines/` | Deterministic ETL and catalog builders |
| Tests | `tests/` | Unit/integration tests for validators and scripts |

### Expected file tree
~~~text
📁 .github/
├── 📁 lineage/
│   ├── 📄 README.md
│   └── 📁 scripts/
│       ├── 📄 README.md
│       ├── 📄 <validator_script>.<py|js|sh>
│       ├── 📄 <report_script>.<py|js|sh>
│       └── 📄 <shared_lib>.<py|js>
~~~

## 🧭 Context

### Why this directory exists
KFM treats provenance as a first-class boundary artifact: every dataset generation step should be traceable via PROV, and provenance-linked context is a requirement for downstream presentation modes that restrict to sourced content.

This directory is the CI-facing “glue” that helps keep:
- provenance **present**
- provenance **valid**
- provenance **aligned** with STAC/DCAT and other contracts

### Architectural invariants these scripts must preserve
- **Canonical pipeline order is not negotiable**: ETL → STAC/DCAT/PROV → graph → API → UI → Story Nodes → Focus Mode.
- **UI does not read Neo4j directly**: scripts should not introduce shortcuts that bypass API boundaries.
- **Deterministic CI**: checks should validate if present, fail if invalid, and skip only when not applicable.
- **No YAML front-matter in code files**: keep YAML front matter confined to governed docs like this README.

### What these scripts should do
- Validate existence and shape of **PROV bundles** for targeted runs/datasets.
- Validate that **catalog artifacts** (STAC/DCAT/PROV) are mutually consistent in identifiers and references.
- Produce **machine-readable summaries** suitable for CI logs and review gates.
- Enforce repo lint constraints relevant to lineage.

### What these scripts must not do
- Infer sensitive locations or produce new policy.
- Emit network-dependent results by default (avoid “works on my machine” CI).
- Write catalog artifacts into `docs/` (catalog outputs belong under `data/` canonical homes).

## 🧱 Script conventions

### Naming and placement
- Prefer descriptive names that start with an action verb: `validate_*`, `check_*`, `report_*`.
- Keep scripts small. Shared logic belongs in a shared module in this folder (or a designated `tools/` or `src/` package, if standardized elsewhere).

### CLI contract
- Scripts should support `--help` and return stable exit codes.
- Recommended exit codes:
  - `0`: success (no blocking findings)
  - `1`: validation failure (blocking)
  - `2`: usage error (bad args / missing inputs)
  - `3`: unexpected error (exception)
- Recommended output:
  - human-readable log lines
  - optional JSON summary (path supplied via CLI flag), suitable for attaching as CI artifacts

### Determinism rules
- Deterministic inputs: repo state + explicit CLI args.
- Deterministic outputs: avoid timestamps in outputs unless explicitly required and isolated in metadata fields.

## 🗺️ Diagrams

~~~mermaid
flowchart TB
  PR[Pull request or push] --> CI[GitHub Actions workflow]
  CI --> S[Lineage scripts in .github/lineage/scripts]
  S --> V1[Validate PROV bundles]
  S --> V2[Validate STAC/DCAT/PROV alignment]
  V1 --> R[CI summary + artifacts]
  V2 --> R
  R --> G[Gate: pass/fail with deterministic behavior]
~~~

## 🧪 Validation and CI/CD

### Validation steps
- [ ] Markdown protocol checks for governed docs
- [ ] Schema validation for STAC/DCAT/PROV (and any additional contract artifacts)
- [ ] Cross-reference integrity checks (no orphan references)
- [ ] Deterministic validate/fail/skip behavior in CI
- [ ] Repo lint checks relevant to lineage scripts

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands

# 1) show help for a validator script
# python .github/lineage/scripts/<validator_script>.py --help

# 2) run a validator against canonical homes
# python .github/lineage/scripts/<validator_script>.py \
#   --prov-root data/prov \
#   --stac-root data/stac \
#   --dcat-root data/catalog/dcat \
#   --schemas-root schemas

# 3) run tests if present
# pytest -q
~~~

### Telemetry signals
| Signal | Source | Where recorded |
|---|---|---|
| Lineage gate status | CI job outputs | `docs/telemetry/` + `schemas/telemetry/` (if adopted) |

## 🧠 Story Node and Focus Mode integration

### How this work surfaces in Focus Mode
Lineage scripts protect downstream narrative modes by ensuring that provenance-linked evidence exists and validates before Story Nodes or Focus Mode bundles are treated as publishable.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Provenance-linked content is the only content eligible for strict “no hallucinated sources” surfaces.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## ⚖ FAIR+CARE and governance

### Review gates
- Changes to CI lineage gates should be reviewed by maintainers responsible for:
  - schema/contracts
  - sovereignty and redaction rules
  - Story Node publish validation, if lineage scripts are involved

### CARE and sovereignty considerations
- Lineage scripts must not expose restricted locations or culturally sensitive knowledge through logs, diffs, or CI artifacts.
- If validating Story Nodes or provenance bundles that include sensitive geometry, ensure checks validate redaction/generalization rules without printing raw sensitive data.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use.
- Do not add script behavior that implies generating policy or inferring sensitive locations.

## 🕰️ Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial README for lineage scripts directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
