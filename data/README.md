---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.3"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.3"
semantic_document_id: "kfm-data-readme-v1.0.3"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.3"
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

# `data/` — KFM data directory

## 📘 Overview

### Purpose

This README defines the **canonical on-disk contract** for KFM datasets and pipeline artifacts living under `data/`. It exists to keep the system **evidence-first** and **auditable** across the full pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

What this document governs:

- **Where** different kinds of data belong (`raw/`, `work/`, `processed/`) and what “canonical” means.
- **Where evidence metadata + lineage** belong (STAC/DCAT/PROV), and how downstream systems must resolve it.
- **How to avoid orphan references** (graph/API/UI/story must be resolvable back to evidence artifacts).
- **How governance and sensitivity propagate** (no output becomes less restricted than its upstream inputs).

Non-negotiables enforced by this README:

- **Staging is stage-first**: `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`.
- **Catalogs are contracts**: downstream consumers should resolve datasets through STAC/DCAT/PROV rather than “random files.”
- **UI never reads Neo4j directly** (all graph access is through the API boundary).
- Anything not verifiable in the current repo state must be labeled **“not confirmed in repo.”**

### Scope

| In Scope | Out of Scope |
|---|---|
| Staging outputs under `data/raw/**`, `data/work/**`, `data/processed/**` | Source code implementation details (`src/**`) |
| Evidence artifacts and discovery metadata: `data/stac/**` (+ DCAT/PROV roots if present) | UI runtime assets/config (belongs in `web/**`) |
| Graph ingest fixtures derived from processed outputs (`data/graph/**`) | Story Nodes (belongs in `docs/reports/story_nodes/**`) |
| Deterministic placement + integrity rules (no orphan refs; stable IDs) | API contract text (belongs at API boundary docs/contracts) |
| Domain packs under `data/<domain>/` (docs/governance/mappings for the domain) | Experiments + run logs (`mcp/**`) |

### Audience

- **Primary:** data engineers / contributors running ETL + catalog builds and producing governed outputs under `data/**`.
- **Secondary:** reviewers validating catalogs + provenance; graph maintainers; curators producing Story Nodes and Focus Mode views.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo)*

Key terms used here:

- **Domain:** a bounded topic area (e.g., hydrology, historical maps, air quality) with its own inputs, transforms, and outputs.
- **Domain pack:** the minimum set of documentation + governance metadata that lets a domain participate safely in the pipeline.
- **Evidence artifact:** machine-readable metadata + lineage consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Orphan reference:** an ID used by graph/API/UI/story that cannot be resolved back to evidence and/or governed processed outputs.
- **Deterministic pipeline:** same inputs + config produce stable, diffable outputs (idempotent runs; no hidden state).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering is non-negotiable |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | This README follows its section order |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Narrative must be provenance-linked |
| v13 redesign blueprint (design intent) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Draft; used as “target alignment,” not a guarantee of current state |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Authority for classification + review gates |
| Ethics policy | `docs/governance/ETHICS.md` | Governance | Human/Community impact considerations |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | Indigenous/culturally sensitive handling rules |

### Definition of done

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Canonical staging + evidence placement rules documented and consistent with Master Guide ordering
- [ ] “Planned / target / optional” paths are labeled when not confirmed in repo
- [ ] Validation expectations are deterministic (“validate/fail/skip” behavior documented)
- [ ] Governance + FAIR+CARE + sovereignty considerations are explicit
- [ ] The README makes it hard to create orphan references (graph/API/UI/story ↔ evidence)

---

## 🗂️ Directory Layout

### This document

- `path`: `data/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains + staging + evidence | `data/` | Raw/work/processed outputs + evidence artifacts + domain packs |
| ETL + catalog pipelines | `src/pipelines/` | Deterministic transforms; outputs land under `data/**` |
| Graph build + ontology | `src/graph/` | Ontology-governed ingest + mapping logic |
| Graph ingest fixtures | `data/graph/` | Import-ready CSV/Cypher (if used) |
| API boundary | `src/server/` *(not confirmed in repo)* | Contracts, redaction/generalization, query services |
| UI | `web/` | React/Map UI (no direct Neo4j access) |
| Story Nodes | `docs/reports/story_nodes/` | Provenance-first narrative artifacts (draft/published) |
| Schemas | `schemas/` *(not confirmed in repo)* | Validators and contracts (JSON Schema, etc.) |
| MCP run logs / experiments | `mcp/` | Run manifests, experiments, artifacts, SOPs |

### Canonical placement rules

**Canonical staging (required, stage-first):**

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`

**Evidence outputs (machine-readable, consumed downstream):**

- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/` *(planned / not confirmed in repo)*
- PROV: `data/prov/` *(planned / not confirmed in repo)*
- Graph fixtures (when used): `data/graph/**`

**Domain packs (documentation, not bulk data):**

- `data/<domain>/README.md` + `data/<domain>/{sources,mappings,governance}/...`

### Target file tree for `data/`

> Notes:
> - Items marked **(planned)** or **(optional)** may not exist yet *(not confirmed in repo)*.
> - Bulk datasets belong under `raw/`, `work/`, `processed/` (organized by domain).
> - The domain pack folder `data/<domain>/` is for docs/governance/mappings, not bulk exports.

~~~text
📁 data/
├── 📄 README.md
│
├── 📁 raw/
│   └── 📁 <domain>/                         # immutable source snapshots (append-only)
│
├── 📁 work/
│   └── 📁 <domain>/                         # intermediate artifacts (rebuildable)
│
├── 📁 processed/
│   └── 📁 <domain>/                         # canonical governed outputs (validated + versioned)
│
├── 📁 stac/
│   ├── 📁 collections/                      # STAC Collections (JSON)
│   └── 📁 items/                            # STAC Items (JSON)
│
├── 📁 catalog/                              # (planned) DCAT canonical root
│   └── 📁 dcat/                             # DCAT outputs (JSON-LD / TTL as adopted)
│
├── 📁 prov/                                 # (planned) PROV bundles (per run / per dataset)
│
├── 📁 graph/
│   ├── 📁 csv/                              # import-ready CSVs (nodes/edges/etc.)
│   └── 📁 cypher/                           # optional post-import scripts / migrations
│
├── 📁 sources/                              # (optional) global source registry/index
│   └── 📄 <source_index>.json               # (format not confirmed in repo)
│
├── 📁 <domain>/                             # domain pack docs (not bulk data)
│   ├── 📄 README.md                         # required: domain overview + evidence pointers
│   ├── 📁 sources/                          # licenses/attribution/source notes (recommended)
│   ├── 📁 mappings/                         # crosswalks + field notes (optional)
│   └── 📁 governance/                       # CARE/sensitivity/redaction notes (recommended)
│
└── 📁 reports/                              # (optional) derived evidence products / analysis outputs
    └── 📁 <domain>/
~~~

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/raw/<domain>/` | Immutable source snapshots (append-only; do not mutate in place) | ETL ingest | ETL transforms (read-only) |
| `data/work/<domain>/` | Intermediate transforms (regenerable) | ETL | ETL, validation, QA |
| `data/processed/<domain>/` | Canonical outputs used for catalogs + graph ingest | ETL | Catalog build, graph build, audits |
| `data/stac/**` | STAC Collections + Items (discovery + evidence) | Catalog build | Graph, API, UI, story validation |
| `data/catalog/dcat/**` | DCAT dataset/distribution outputs *(planned)* | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles *(planned)* | ETL + catalog build | Audits, provenance checks, Focus Mode |
| `data/graph/**` | Import fixtures for Neo4j | Graph build | Neo4j loaders / migrations |
| `data/<domain>/**` | Domain pack docs: README + governance + mappings | Data/curation | Reviewers, maintainers, curators |
| `data/reports/<domain>/**` | Optional derived evidence products | ETL/analysis | Story Nodes, Focus Mode contexts |

---

## 🔎 Context

### Background

KFM’s maps, timelines, and narratives depend on **traceable evidence**. The `data/` directory provides a deterministic, auditable home for datasets and their evidence artifacts so that catalogs, graph ingest, APIs, and UI remain provenance-linked and reviewable.

### Assumptions

- ETL outputs are reproducible and idempotent (same input + config → same output), with run details recorded somewhere (`mcp/**` and/or PROV outputs).
- STAC is treated as the source-of-truth catalog for spatiotemporal assets; DCAT and PROV are complementary standards where adopted.
- Some canonical roots (`schemas/`, `data/catalog/dcat/`, `data/prov/`, `src/server/`) may be planned but not yet present *(not confirmed in repo)*.

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- UI consumes **APIs only** (no direct Neo4j reads).
- Every published claim or UI layer must resolve to evidence IDs (no orphan references).
- Classification must propagate through lineage (no output is less restricted than any input in its ancestry).
- AI transforms must respect the front-matter allow/deny lists (no new prohibited transforms).

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical on-disk home for DCAT and PROV in current repo state: `data/catalog/dcat/` + `data/prov/` vs legacy/alternate variants? | Maintainers | TBD |
| Do we standardize domain naming (e.g., `air-quality` vs `air_quality`) and enforce it in CI? | Data governance | TBD |
| Do domain governance docs live under `data/<domain>/governance/` or `docs/data/<domain>/` (choose one canonical location + link)? | Governance | TBD |
| What is the canonical validator toolchain for STAC/DCAT/PROV in CI (commands, versions, strictness)? | Data/Platform | TBD |
| Stage-first vs domain-first staging: keep `data/raw|work|processed/<domain>/` or migrate to `data/<domain>/{raw,work,processed}/` as a v13 change? | Maintainers | TBD |

### Future extensions

- Add a canonical “source index” schema under `schemas/` for `data/sources/*.json` *(not confirmed in repo)*.
- Add per-domain freshness gates + classification docs under a single canonical path with CI checks.
- Add releases packaging under `releases/` (manifests/SBOMs/signed bundles) once the repo adopts that workflow *(not confirmed in repo)*.
- Add automated lineage checks linking `mcp/runs/**` → `data/prov/**` once PROV outputs are formalized.

---

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| External source snapshots | CSV/GeoJSON/GeoTIFF/PDF/etc. | Ingested into `data/raw/<domain>/` | Hashing + file integrity + (domain-specific) schema checks |
| Domain pack documentation | Markdown | `data/<domain>/README.md` etc. | Markdown protocol checks |
| Pipeline configs | YAML/JSON/etc. | `src/pipelines/**` *(not confirmed in repo)* | Lint + reproducibility rules |
| Governance policies | Markdown | `docs/governance/**` | Human review gates + policy lint (if present) |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw snapshots | source-native | `data/raw/<domain>/...` | Append-only, hashed |
| Intermediate artifacts | CSV/JSON/Parquet/etc. | `data/work/<domain>/...` | Regenerable; schema where applicable |
| Canonical processed datasets | CSV/GeoJSON/Parquet/etc. | `data/processed/<domain>/...` | Validated + versioned |
| STAC Collections | JSON | `data/stac/collections/*.json` | STAC + KFM profile |
| STAC Items | JSON | `data/stac/items/**/*.json` | STAC + KFM profile |
| DCAT datasets/distributions | JSON-LD / TTL | `data/catalog/dcat/**` *(planned)* | DCAT + KFM profile |
| PROV bundles | JSON-LD / TTL | `data/prov/**` *(planned)* | PROV-O + KFM profile |
| Graph ingest fixtures | CSV/Cypher | `data/graph/**` | Graph ingest contracts *(not confirmed in repo)* |

### Sensitivity & redaction

- If any dataset contains sensitive locations or culturally sensitive knowledge, public-facing outputs must be **generalized/redacted** according to governance policies.
- Redaction and generalization are enforced at the **API boundary** and must be reflected consistently in Story Nodes and Focus Mode.

### Quality signals

- Completeness checks (required keys present, non-null rates)
- Range/domain checks (value plausibility, date bounds)
- Geometry validity checks (if spatial)
- Referential integrity checks (IDs referenced by other artifacts resolve)
- Determinism checks (reruns produce stable diffs)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- **Canonical location:** `data/stac/collections/` and `data/stac/items/`
- Collections involved: *(domain-specific; list in each domain pack README)*
- Items involved: *(domain-specific; list in each domain pack README)*
- Extension(s): *(if adopted; not confirmed in repo)*

### DCAT

- Canonical location: `data/catalog/dcat/` *(planned / not confirmed in repo)*
- Dataset identifiers: *(domain-specific; must cross-link to STAC Collection IDs)*
- License mapping: *(from source and governance metadata)*
- Contact / publisher mapping: *(not confirmed in repo)*

### PROV-O

- Canonical location: `data/prov/` *(planned / not confirmed in repo)*
- `prov:wasDerivedFrom`: raw → work → processed relationships
- `prov:wasGeneratedBy`: which activity/run generated which artifacts
- Activity / Agent identities: tie to run manifests or logs (`mcp/runs/**` and/or `commit_sha`)

### Versioning

- Use STAC Versioning links and graph predecessor/successor relationships as applicable.
- Dataset versioning must be deterministic and diffable; do not silently overwrite history.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + run logs producing `data/**` |
| Catalogs | STAC/DCAT/PROV evidence + lineage | JSON/JSON-LD + validators |
| Graph | Neo4j ingest model | Import fixtures + API boundary |
| APIs | Serve contracts; enforce redaction/generalization | REST/GraphQL *(not confirmed in repo)* |
| UI | Map + narrative exploration | API calls only |
| Story Nodes | Curated narrative | Provenance-linked content |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` *(not confirmed in repo)* | Semver + changelog |
| API schemas | `src/server/` + docs *(not confirmed in repo)* | Contract tests required |
| UI layer registry | `web/` *(exact path not confirmed in repo)* | Schema-validated |

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/raw|work|processed/<domain>/` + `data/<domain>/README.md`
- [ ] STAC: new collection + item(s) created and validated
- [ ] DCAT: dataset/distribution generated (if adopted) and cross-linked
- [ ] PROV: activity + agent identifiers recorded (if adopted)
- [ ] Graph: new labels/relations mapped + migration plan (if needed)
- [ ] APIs: contract version bump + tests (if needed)
- [ ] UI: layer registry entry + access rules (if used)
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump (if used)

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

- Datasets become focusable when they have:
  - a resolvable evidence chain (STAC/DCAT/PROV IDs),
  - stable IDs usable by graph/API/UI,
  - and governance classification that allows surfacing.

### Provenance-linked narrative rule

- Every claim must trace to a dataset / record / asset ID.
- Story Nodes must not introduce “new facts” that bypass evidence artifacts.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Validation steps

- [ ] Markdown protocol checks (front-matter present; template section order)
- [ ] Schema validation (STAC/DCAT/PROV) when schemas/tools exist
- [ ] No orphan references (IDs cited by graph/API/UI/story resolve to evidence)
- [ ] Deterministic outputs (stable IDs; diffable reruns)
- [ ] Graph fixture referential integrity checks (if `data/graph/**` exists)
- [ ] Security + secrets scanning (no credentials; no disallowed sensitive content)
- [ ] Sovereignty checks (generalize/redact sensitive locations where required)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate docs (markdown protocol)
# 2) validate STAC/DCAT/PROV (if toolchain is present)
# 3) run ETL/catalog pipelines (deterministic)
# 4) run graph fixture checks (if applicable)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `run_id` | ETL/Catalog run | `mcp/runs/**` *(not confirmed in repo)* |
| dataset hash | hashing step | PROV bundle or run log *(not confirmed in repo)* |
| validation status | schema validators | CI logs + artifacts *(not confirmed in repo)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Escalate for governance review when introducing:

- new external data sources,
- new sensitive layers (protected locations / culturally sensitive knowledge),
- new AI narrative behavior that could be mistaken for factual content,
- new public-facing endpoints exposing data.

### CARE / sovereignty considerations

- Treat culturally sensitive and Indigenous knowledge as high-risk by default.
- Protect restricted locations by:
  - geometry generalization where required,
  - API-level redaction,
  - Story Node review gates before publishing.

### AI usage constraints

This document explicitly allows only the AI transforms listed in front-matter:

- Allowed: summarize, structure_extract, translate, keyword_index
- Prohibited: generate_policy, infer_sensitive_locations

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `data/` README (v12/v13-aligned draft) | TBD |
| v1.0.1 | 2025-12-24 | Align to Universal doc structure; clarify planned paths and “not confirmed” markers | TBD |
| v1.0.2 | 2025-12-26 | Standardize staging semantics; clarify domain packs vs bulk data; expand CI contract language | TBD |
| v1.0.3 | 2025-12-27 | Tighten template conformity (columns/sections); clarify canonical vs planned roots; add explicit canonical placement rules + domain pack contract | TBD |

---

Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (design intent): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
