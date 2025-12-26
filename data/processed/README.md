---
title: "KFM Data — Processed Outputs"
path: "data/processed/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

doc_uuid: "urn:kfm:doc:data:processed:readme:v1.0.0"
semantic_document_id: "kfm-data-processed-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:processed:readme:v1.0.0"

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

# KFM Data — Processed Outputs

## 📘 Overview

### Purpose

- Define what belongs under `data/processed/` (canonical, publishable outputs) and how it differs from `data/raw/` and `data/work/`.
- Document the minimum expectations for **schema validity**, **versioning**, and **provenance linkage** required before downstream use (catalogs → graph → APIs → UI → Story Nodes/Focus Mode).

### Scope

| In Scope | Out of Scope |
|---|---|
| Canonical processed datasets and derived products intended for reuse | Raw source drops (use `data/raw/`) |
| Versioned outputs suitable for cataloging and graph/API use | Intermediate/scratch artifacts (use `data/work/`) |
| Minimal “promotion to processed” checklist | Implementing ETL logic (lives in `src/pipelines/`) |
| Guidance on connecting processed outputs to STAC/DCAT/PROV | Writing governance policy (lives in `docs/governance/`) |

### Audience

- **Primary:** contributors producing datasets via ETL/transforms and promoting outputs from `data/work/` → `data/processed/`.
- **Secondary:** catalog maintainers, graph/API/UI maintainers, and Story Node authors who rely on processed outputs as citable evidence.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo)*
- Terms used in this doc (non-exhaustive): **raw**, **work**, **processed**, **certified artifact**, **dataset version**, **STAC**, **DCAT**, **PROV**, **classification propagation**, **redaction/generalization**, **no orphan data**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Canonical pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | KFM Core | ETL → catalogs → graph → APIs → UI → story → Focus Mode |
| Data staging contract | `data/raw/` · `data/work/` · `data/processed/` | Data/Pipeline | Required staging areas |
| Catalog outputs | `data/stac/` · `data/catalog/dcat/` · `data/prov/` | Data/Catalog | Some paths may be planned/not confirmed in repo |
| Pipeline implementations | `src/pipelines/` | Engineering | Deterministic ingest/transform/catalog build |
| Schemas (STAC/DCAT/PROV/telemetry/etc.) | `schemas/` | Data/Platform | Schema validation gates |
| API boundary + contracts | `src/server/contracts/` *(or legacy; not confirmed in repo)* | API | UI must consume via APIs, not graph directly |
| Story Nodes | `docs/reports/**/story_nodes/` | Narrative | Evidence-linked narrative artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Directory meaning of `data/processed/` is explicit and non-contradictory to the Master Guide
- [ ] File tree examples are aligned + emoji/connector formatted
- [ ] Validation + promotion checklist is repeatable (commands can be placeholders if marked)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Version History present

## 🗂️ Directory Layout

### This document

- `path`: `data/processed/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Raw landings | `data/raw/` | Raw ingests (append-only; never “hand edited”) |
| Work staging | `data/work/` | Intermediate artifacts (reproducible; safe to delete/rebuild) |
| Processed outputs (this area) | `data/processed/` | Canonical outputs (schema-validated; versioned) |
| STAC catalogs | `data/stac/` | STAC Collections/Items; Assets reference processed artifacts |
| DCAT catalogs | `data/catalog/dcat/` *(planned?)* | DCAT dataset/distribution metadata (not confirmed in repo) |
| PROV bundles | `data/prov/` *(planned?)* | Provenance bundles consumed downstream (not confirmed in repo) |
| ETL + catalog code | `src/pipelines/` | Pipelines and transforms |
| Graph build/ingest | `src/graph/` | Ontology bindings, migrations, ingest rules |
| API layer | `src/server/` *(not confirmed in repo)* | Contracted APIs and redaction enforcement |
| UI | `web/` | React/MapLibre client(s) |
| Narrative | `docs/reports/**/story_nodes/` | Story Nodes used by Focus Mode |

### Expected file tree for this area

> Notes:
> - The staging folders (`data/raw|work|processed|stac`) are canonical; organize content *within them* by domain.
> - Items marked *(recommended)* are conventions, not hard requirements, unless enforced elsewhere in CI.

~~~text
📁 data/
└── 📁 processed/
    ├── 📄 README.md
    ├── 📁 <domain>/
    │   ├── 📁 <dataset_or_product>/
    │   │   ├── 📄 README.md                 (recommended: dataset-level context + rules)
    │   │   ├── 📁 vX.Y.Z/                   (recommended: immutable version directory)
    │   │   │   ├── 📄 <artifacts>           (tables/vectors/rasters/etc.)
    │   │   │   └── 📄 <checksums/manifest>  (recommended: integrity pointers)
    │   │   └── 📄 LATEST                    (optional: pointer file; not required)
    │   └── 📁 <another_dataset_or_product>/
    └── 📁 <another_domain>/
~~~

## 🧭 Context

### Background

KFM’s governed data lifecycle uses required staging areas:

- `data/raw/` → `data/work/` → `data/processed/` → catalogs (`data/stac/` + DCAT/PROV where configured)

`data/processed/` is the **“certified outputs”** boundary: artifacts placed here are intended to be stable, reusable, and safe to reference downstream (catalogs/graph/APIs/UI/narrative).

### What makes an artifact eligible for `data/processed/`

An artifact is eligible for promotion to `data/processed/` when:

- It is produced from raw/work inputs via a **deterministic, replayable** pipeline (or equivalent governed transform).
- It conforms to a declared **schema/contract** (domain-defined) and passes the required validation gates.
- It has clear **license/attribution** and **provenance linkage** (PROV activity + inputs).
- It is **versioned**: new releases create a new version lineage (avoid silent in-place overwrites).
- Its **classification/sensitivity** is consistent with lineage (no “downgrades” without explicit governance review).

### What does *not* belong in `data/processed/`

- Raw vendor dumps, “as-downloaded” files, or anything you cannot reproduce (use `data/raw/`).
- Temporary or exploratory outputs that can be safely deleted (use `data/work/`).
- Code, notebooks, or scripts (code belongs in `src/` and `tools/`).
- Secrets, tokens, private URLs, or other credentials.

### v13 note

Some redesign documents discuss organizing staging under per-domain roots (e.g., `data/<domain>/processed/`). If/when that structure is adopted, this README may be superseded. Until then, `data/processed/` remains the canonical processed staging location per the v12 lifecycle.

## 🗺️ Diagrams

### System / dataflow diagram (where `data/processed/` sits)

~~~mermaid
flowchart LR
  RAW["data/raw (inputs)"] --> WORK["data/work (intermediate)"]
  WORK --> PROC["data/processed (canonical outputs)"]
  PROC --> CAT["STAC/DCAT/PROV catalogs"]
  CAT --> GRAPH["Neo4j graph"]
  GRAPH --> API["APIs"]
  API --> UI["React/Map UI"]
  UI --> STORY["Story Nodes"]
  STORY --> FOCUS["Focus Mode"]
~~~

## 🧠 Story Node & Focus Mode Integration

### How processed outputs surface in Focus Mode

Processed artifacts should be treated as **citable evidence**:

- Catalogs reference them as STAC Assets (and DCAT/PROV where present).
- Story Nodes should reference dataset/asset identifiers (not ad-hoc file paths) whenever possible.
- Focus Mode must only surface content that is **provenance-linked**.

### Provenance-linked narrative rule

- Every narrative claim must trace to a dataset / record / asset identifier.
- Unsourced narrative is invalid for publication in Focus Mode.

### Optional structured controls (if useful)

~~~yaml
focus_layers:
  - "<domain>:<layer-id>"
focus_time: "<ISO-8601 time window>"
focus_center: [ -98.0000, 38.0000 ] # Kansas reference point (example only)
~~~

## 🧪 Validation & CI/CD

### Validation steps (minimum expectations)

Before promoting outputs into `data/processed/`:

- [ ] Secrets scan (no tokens/keys; no private URLs)
- [ ] PII / privacy scan (as applicable)
- [ ] Sensitive-location risk scan (as applicable; avoid publishing exact coordinates when restricted)
- [ ] Schema validation for processed artifacts (domain-defined; required if schema exists)
- [ ] Integrity checks recorded (hashes/manifests) *(recommended)*
- [ ] STAC/DCAT/PROV catalogs updated and validated against the project profiles *(when publishing)*
- [ ] Classification propagation verified (no output is “less restricted” than any input in its lineage)

### Reproduction (deterministic)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run the pipeline that produces/refreshes processed outputs
# python -m src.pipelines.<domain>.<pipeline> --config <config_path>

# 2) Validate catalogs (if produced)
# python tools/validate_stac.py data/stac/<domain>
# python tools/validate_dcat.py data/catalog/dcat/<domain>
# python tools/validate_prov.py data/prov/<domain>

# 3) Governance scans (if required)
# python tools/scan_pii.py data/work/<domain>
# python tools/scan_sensitive_locations.py data/processed/<domain>
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `classification_assigned` | promotion step | `mcp/runs/` *(recommended pointers)* |
| `redaction_applied` | transform step | `data/prov/**` *(recommended)* |
| `promotion_blocked` | CI gate | CI logs / run artifacts |
| `catalog_published` | catalog build | `data/stac/**` + provenance refs |

## 📦 Data & Metadata

### Inputs

Processed outputs are derived from:

| Input | Typical location | Notes |
|---|---|---|
| Raw source artifacts | `data/raw/<domain>/...` | Append-only; preserve source fidelity |
| Intermediate artifacts | `data/work/<domain>/...` | Safe to rebuild; may be pruned |
| Pipeline configs + code | `src/pipelines/` (+ configs) | Deterministic transformations |
| Schemas/contracts | `schemas/**` + `src/server/contracts/**` | Validation gates |

### Outputs

A “processed” dataset typically includes:

| Output | Location | Notes |
|---|---|---|
| Canonical dataset artifacts | `data/processed/<domain>/<dataset>/vX.Y.Z/` | Prefer immutable versioned directories |
| Dataset README | `data/processed/<domain>/<dataset>/README.md` | (recommended) explain schema + provenance expectations |
| Integrity pointers | `mcp/runs/<run_id>/...` or sidecar | Prefer pointers to provenance bundles (avoid duplication) |

### Versioning rules (minimum)

- Prefer “new version + links” over overwriting files in-place.
- Keep predecessor/successor relationships in catalogs and provenance (see next section).

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy

Every new dataset intended for downstream use must have:

- STAC Collection + Item(s)
- DCAT mapping (minimum: title/description/license/keywords)
- PROV activity for the transform that generated it

### Versioning expectations

- New versions link predecessor/successor (catalog-level).
- Graph mirrors version lineage (where graph ingestion exists).
- Avoid overwriting in-place without an explicit lineage trail.

### PROV placement convention

- Prefer each meaningful run to produce (or link to) a PROV activity bundle under `data/prov/**`.
- Prefer `mcp/runs/**` to contain pointers/IDs to PROV, rather than duplicating provenance payloads.

## 🧱 Architecture

### Subsystem contracts (how `data/processed/` is consumed)

| Subsystem | What it consumes from `data/processed/` | “Do not break” rule |
|---|---|---|
| ETL | Produces versioned processed artifacts | deterministic, replayable |
| Catalogs | Reference processed artifacts as STAC Assets | machine-validated to profile |
| Graph | Ingests entities/links derived from processed + catalogs | stable IDs + explicit provenance |
| APIs | Serve contracted views of datasets | redaction enforced; no leakage |
| UI | Uses APIs only (never queries graph directly) | no hidden data leakage |
| Story Nodes | Cite dataset/asset identifiers | provenance-linked facts only |
| Focus Mode | Surfaces evidence-linked context bundles | no hallucinated sources |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/processed/<domain>/...`
- [ ] STAC: new collection/item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## ⚖ FAIR+CARE & Governance

### Review gates

Governance review is required when:

- introducing a new external dataset source,
- changing an artifact’s classification/sensitivity,
- publishing any dataset derived from sensitive/restricted inputs,
- adding a new public-facing endpoint or UI layer that could reveal sensitive locations by interaction/zoom.

### CARE / sovereignty considerations

- Treat any location-bearing records conservatively until domain governance clarifies exposure rules.
- Prefer coarse/aggregate public products when community impacts or sovereignty constraints apply.
- Verify classification propagation: no processed/public output is “less restricted” than any input in its lineage.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing.
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).
- AI may propose classifications, but **human review** must approve any final labels, especially downgrades.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-26 | Initial `data/processed/` README establishing meaning + promotion expectations | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

