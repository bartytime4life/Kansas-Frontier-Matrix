---
title: "Kansas Frontier Matrix — Pipelines README"
path: "docs/pipelines/README.md"
version: "v1.0.0"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:pipelines:readme:v1.0.0"
semantic_document_id: "kfm-pipelines-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:pipelines:readme:v1.0.0"
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

# Kansas Frontier Matrix — Pipelines

## 📘 Overview

### Purpose

- Define **how pipeline work is organized and documented** in KFM.
- Clarify **what pipelines must produce** (data lifecycle outputs + STAC/DCAT/PROV + provenance/run artifacts) so downstream **graph, API, UI, and Story Nodes** remain contract-valid.
- Enforce **placement rules** so the repository remains auditable and CI-friendly (no “mystery duplicates”, no code in docs, no derived data in `src/`).

### Scope

| In Scope | Out of Scope |
|---|---|
| Pipeline organization, responsibilities, and boundaries across the canonical lifecycle | Implementing a specific domain’s ETL logic line-by-line (belongs in `src/pipelines/<domain>/`) |
| Conventions for documenting pipeline steps (runbooks/recipes) under `docs/pipelines/` | Cloud deployment or orchestration vendor choice *(not confirmed in repo)* |
| Required evidence + lineage outputs (STAC/DCAT/PROV) and where they live | Writing governance policy text (belongs in `docs/governance/`) |
| Rules for file-type correctness and separation of docs vs runnable code | UI design details beyond ensuring data surfaces via APIs |

### Audience

- **Primary:** contributors implementing or updating pipelines (ETL, normalization, catalog build, graph ingest).
- **Secondary:** maintainers reviewing PRs for determinism/contract compliance; governance reviewers; downstream API/UI/Story Node contributors.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc include:
  - **deterministic pipeline**: same inputs + same config ⇒ same outputs (including stable IDs and hashes).
  - **idempotent pipeline**: re-running does not duplicate or drift outputs.
  - **domain pack**: minimal artifact set required for a domain to participate in the full pipeline.
  - **evidence artifact**: STAC/DCAT/PROV outputs (and any derived evidence products) consumed downstream.
  - **run/provenance bundle**: PROV activity + entities linking raw → work → processed → catalog outputs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical pipeline ordering + invariants |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM Core | Canonical roots + contract-first rules |
| Next Stages Blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | KFM Core | Domain expansion + vertical slice goals |
| Schemas registry | `schemas/README.md` *(not confirmed in repo)* | Contracts owners | Validation contracts for outputs and boundaries |
| Pipeline code (canonical) | `src/pipelines/` | Data Eng | Runnable transforms + catalog builders |
| Catalog outputs (canonical) | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Data/Catalog | Evidence + lineage bundles |
| Graph ingest | `src/graph/` (+ `data/graph/` if present) | Graph Eng | Ontology bindings + ingest fixtures |
| API boundary | `src/server/` *(v13 target)* or `src/api/` *(legacy; not confirmed in repo)* | API Eng | Contracted access to graph + provenance |
| UI | `web/` | Frontend | React map/narrative app (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Draft + published nodes |

### Definition of done (for this document)

- [x] Front-matter complete + `path` matches file location
- [x] Canonical pipeline ordering stated and mapped to repo locations
- [x] Placement rules documented (docs vs code, data vs src)
- [ ] Example domain runbook(s) linked from `docs/pipelines/<domain>/` *(depends on domain docs; not required for this file)*
- [ ] Repo lint / markdown lint run (CI or local)
- [ ] Maintainer review

---

## 🗂️ Directory Layout

### This document

- `path`: `docs/pipelines/README.md` (must match front-matter)

### Related repository paths (orientation)

| Area | Path | What lives here |
|---|---|---|
| Pipelines (runnable) | `src/pipelines/` | Deterministic ETL + transforms + catalog builders |
| Pipeline docs | `docs/pipelines/` | Markdown runbooks/recipes for pipelines (**no runnable code**) |
| Data lifecycle | `data/raw/` + `data/work/` + `data/processed/` | Raw inputs, intermediates, canonical processed datasets |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC Items/Collections, DCAT datasets, PROV lineage bundles |
| Graph | `src/graph/` (+ `data/graph/` if present) | Ontology bindings, ingest mappings, import fixtures |
| API boundary | `src/server/` *(v13 target)* | Contracted access + redaction + provenance refs |
| UI | `web/` | React UI + map layer registry (API-only access to graph) |
| Schemas | `schemas/` *(not confirmed in repo)* | Machine-validated contracts (STAC/DCAT/PROV/storynodes/ui/telemetry) |
| Tests | `tests/` | Unit/integration/contract tests validating boundaries |
| Runs / experiments | `mcp/runs/` + `mcp/experiments/` | Run manifests/logs and experiment reports pointing to canonical outputs |

### Expected file tree for this sub-area

> Note: the exact contents may vary by domain; this is the **canonical intent**. If the repo currently deviates, treat this tree as the target for cleanup.

~~~text
📁 docs/
└── 📁 pipelines/
    ├── 📄 README.md                      # This file: conventions + placement rules
    ├── 📁 common/                        # (recommended) shared runbook patterns
    │   ├── 📄 CONVENTIONS.md             # naming, IDs, determinism rules (optional)
    │   └── 📄 VALIDATION_CHECKLIST.md    # STAC/DCAT/PROV + schema checks (optional)
    └── 📁 <domain>/                      # one folder per data domain (recommended)
        ├── 📄 README.md                  # domain pipeline runbook (governed doc)
        ├── 📄 SOURCES_AND_LICENSES.md    # source inventory + license notes (optional)
        ├── 📄 OUTPUTS.md                 # raw/work/processed + catalog outputs (optional)
        └── 📄 VALIDATION.md              # repeatable validation steps (optional)

📁 src/
└── 📁 pipelines/
    ├── 📁 common/                        # shared pipeline utilities (if used)
    └── 📁 <domain>/                      # runnable code + configs for domain ETL/catalog

📁 data/
├── 📁 raw/<domain>/                      # landed source artifacts (as received)
├── 📁 work/<domain>/                     # intermediates during normalization
├── 📁 processed/<domain>/                # canonical processed outputs (data, not code)
├── 📁 stac/
│   ├── 📁 collections/                   # STAC Collections (JSON)
│   └── 📁 items/                         # STAC Items (JSON)
├── 📁 catalog/
│   └── 📁 dcat/                          # DCAT dataset/distribution records
└── 📁 prov/                              # PROV activity/entities bundles (run lineage)
~~~

---

## 🧭 Context

### Canonical ordering (non-negotiable)

KFM is architecture-synced to the lifecycle:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

Pipelines sit at the front of this chain and must produce **evidence + lineage artifacts** that downstream layers can cite and validate.

### Why `docs/pipelines/` exists

- Pipelines are **more than code**: they are governed, auditable procedures.
- Every domain needs a human-readable runbook describing:
  - inputs, outputs, and stable IDs
  - validation steps
  - provenance expectations
  - how the produced catalogs map into graph/API/UI

### Core invariants (enforced by structure)

1. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; all graph access is mediated by the API boundary.

2. **Contracts are canonical**
   - Schemas/specs live in `schemas/` and API contracts under `src/server/contracts/` *(v13 target; not confirmed in repo)*.

3. **Data outputs are not code**
   - Derived datasets belong under `data/<domain>/processed/`, not under `src/`.

4. **File-type correctness**
   - `docs/pipelines/` contains Markdown runbooks/recipes.
   - Runnable scripts live under `src/pipelines/`.
   - If you find “code disguised as docs” (e.g., `.py` with YAML front-matter and Markdown), split it into:
     - a Markdown recipe under `docs/pipelines/`, and
     - a runnable script/module under `src/pipelines/`.

### System flow (orientation)

~~~mermaid
flowchart LR
  A[ETL / Pipelines<br/>src/pipelines] --> B[Catalogs<br/>data/stac + data/catalog/dcat + data/prov]
  B --> C[Graph<br/>src/graph (+ data/graph if present)]
  C --> D[API<br/>src/server]
  D --> E[UI<br/>web]
  E --> F[Story Nodes<br/>docs/reports/story_nodes]
  F --> G[Focus Mode]
~~~

---

## 🔁 What pipelines must produce

### Minimum outputs per domain (conceptual)

Every domain pipeline should make it possible to answer:

- **What did we ingest?** (raw inputs + checksums + licenses)
- **What did we produce?** (processed datasets + catalog metadata)
- **How was it produced?** (PROV lineage: activity/run IDs, inputs/outputs)
- **How do downstream systems cite it?** (stable item/dataset identifiers)

### Canonical output locations

- `data/raw/<domain>/`  
  Landed source artifacts (as received, or as close as feasible), plus source metadata pointers.

- `data/work/<domain>/`  
  Intermediate artifacts (cleaning, normalization, geometry fixes, OCR outputs, etc.).

- `data/processed/<domain>/`  
  Canonical processed outputs used downstream (tables, GeoJSON, parquet, derived rasters, etc.).

- `data/stac/collections/` + `data/stac/items/`  
  STAC metadata for geospatial/temporal assets.

- `data/catalog/dcat/`  
  DCAT dataset/distribution metadata for discovery.

- `data/prov/`  
  PROV bundles that connect raw → work → processed → catalog products (and, where relevant, graph ingest artifacts).

---

## 🧩 Domain packs and extension matrix

### What is a “domain pack”?

A **domain pack** is the minimal set of artifacts required for a domain to participate end-to-end in the KFM lifecycle:

- deterministic pipeline logic
- schemas/contracts (as needed)
- catalog/provenance outputs (STAC/DCAT/PROV)
- graph integration artifacts (as needed)
- API/UI surfacing (as needed)
- documentation + tests

### Extension Matrix (what changes require what artifacts)

| Extension type | Stage | Required artifacts |
|---|---|---|
| Add new data domain | ETL + catalogs + graph | `src/pipelines/<domain>/` + `data/stac/` + `data/catalog/dcat/` + `data/prov/` + `src/graph/mappings` + `schemas/` |
| Add new API endpoint | API | Contract doc + endpoint + tests |
| Add new Story Node | Story | Story Node doc + citations + validation |
| Add new UI layer | UI | Layer registry entry + schema validation |

---

## 📝 How to write a domain pipeline runbook

For each domain, add:

- `docs/pipelines/<domain>/README.md` using `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`.

A good runbook should include:

- **Inputs**
  - source inventory + licenses
  - raw landing path(s)
  - expected refresh cadence (if any)

- **Outputs**
  - processed dataset path(s)
  - STAC collection/item identifiers
  - DCAT dataset identifier(s)
  - PROV activity/run identifiers

- **Determinism rules**
  - stable ID strategy (what keys, what hashes)
  - idempotence strategy (how reruns avoid duplicates)

- **Validation**
  - schema validation steps (STAC/DCAT/PROV + domain schemas)
  - link integrity (STAC item ↔ collection)
  - spot checks for spatial/temporal extents
  - redaction/generalization checks if data can be sensitive

- **Downstream integration**
  - graph ingest mapping notes (labels/relations)
  - API endpoints impacted (if any)
  - UI layers that will consume it (if any)
  - Story Nodes or Focus Mode dependencies (if any)

---

## 🧪 Validation & CI expectations (pipeline-facing)

Pipelines and their outputs should be reviewable with deterministic gates:

- **Schema validation**
  - STAC, DCAT, and PROV outputs validate against the repo’s schema contracts *(schemas path not confirmed in repo)*.
- **Idempotence**
  - repeated runs (same inputs) produce identical stable IDs and content hashes.
- **Catalog integrity**
  - STAC items reference valid collections; links are not broken; required fields present.
- **Provenance completeness**
  - each processed artifact can be traced back to raw inputs and the producing run/activity.
- **Separation rules**
  - no derived data under `src/`
  - no runnable code under `docs/pipelines/`

If commands or tooling differ by domain, the domain runbook must state the exact steps or mark them **not confirmed in repo**.

---

## ⚖ FAIR+CARE & Governance

### Review gates

- Follow: `docs/governance/ROOT_GOVERNANCE.md` *(roles/process not confirmed in this folder)*.
- Any change involving sensitive data classification, redaction/generalization behavior, or sovereignty constraints should be explicitly flagged for human review.

### CARE / sovereignty considerations

- If a pipeline touches culturally sensitive locations, sacred/vulnerable sites, or sovereignty-controlled data:
  - prefer coarse or aggregated public outputs,
  - document redaction/generalization decisions in metadata,
  - ensure access rules align to `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new policy; inferring sensitive locations (directly or indirectly).
- Any classification/sensitivity changes require human approval.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---:|---|---|
| v1.0.0 | 2025-12-27 | Initial pipelines README (conventions + placement rules) | TBD |

---

Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
