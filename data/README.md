---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.4"
last_updated: "2025-12-28"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.4"
semantic_document_id: "kfm-data-readme-v1.0.4"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.4"
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

This README defines the **canonical on-disk contract** for KFM datasets and pipeline artifacts that live under `data/`. It exists to keep the system **evidence-first**, **auditable**, and **contract-driven** across the canonical pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

What this document governs:

- **Where** different kinds of data belong (`raw/`, `work/`, `processed/`) and what “canonical” means.
- **Where evidence metadata + lineage** belong (`stac/`, `catalog/dcat/`, `prov/`) and how downstream systems must resolve it.
- **How to avoid orphan references** (graph/API/UI/story identifiers must resolve back to evidence + governed outputs).
- **How governance and sensitivity propagate** (no output becomes less restricted than its upstream inputs).

Non-negotiables enforced by this README:

- **Staging is stage-first (v12 canonical):** `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`.
- **Catalogs are contracts:** downstream consumers resolve datasets through STAC/DCAT/PROV, not “random files.”
- **UI never reads Neo4j directly** (all graph access is through the API boundary).
- **One canonical home per subsystem:** if a canonical root is missing, add it in-place (do **not** create alternate roots).
- Anything not verifiable in the current repo state must be labeled **“not confirmed in repo.”**

### Scope

| In Scope | Out of Scope |
|---|---|
| Staging outputs under `data/raw/**`, `data/work/**`, `data/processed/**` | Source code implementation details (`src/**`) |
| Evidence artifacts and discovery/lineage metadata: `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | UI runtime assets/config (belongs in `web/**`) |
| Optional graph ingest fixtures derived from processed outputs (`data/graph/**`) | Story Nodes (belongs in `docs/reports/story_nodes/**`) |
| Deterministic placement + integrity rules (no orphan refs; stable IDs) | API contract text (belongs at the API boundary docs/contracts) |
| Optional “derived evidence products” stored under `data/reports/**` | Experiments + run logs (`mcp/**`) |

### Audience

- **Primary:** data engineers / contributors running ETL + catalog builds and producing governed outputs under `data/**`.
- **Secondary:** reviewers validating catalogs + provenance; graph maintainers; curators producing Story Nodes and Focus Mode views.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*

Key terms used here:

- **Domain:** a bounded topic area (e.g., hydrology, historical maps, air quality) with its own inputs, transforms, and outputs.
- **Evidence artifact:** any derived output treated as **data + metadata** (STAC/DCAT/PROV) before it appears in UI or narrative.
- **Orphan reference:** an ID used by graph/API/UI/story that cannot be resolved back to governed `processed/` outputs and their evidence artifacts.
- **Deterministic pipeline:** same inputs + config produce stable, diffable outputs (idempotent runs; no hidden state).

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering is non-negotiable |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | This README follows its section order |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Narrative must be provenance-linked |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required for API contract changes |
| v13 redesign blueprint (design intent) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Draft; target alignment, not a guarantee of current state |
| Example domain module: Land Treaties | `docs/data/historical/land-treaties/README.md` | Domain steward | Example domain module (governance-sensitive) |
| Example domain module: Air Quality | `docs/data/air-quality/README.md` | Domain steward | Example domain module |
| Example domain module: Soils (SDA) | `data/soils/sda/README.md` | Domain steward | Example domain module |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Authority for classification + review gates |
| Ethics policy | `docs/governance/ETHICS.md` | Governance | Human/Community impact considerations |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | Indigenous/culturally sensitive handling rules |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Canonical staging + evidence placement rules documented and consistent with the Master Guide ordering
- [ ] “Optional / planned / legacy” paths are explicitly labeled when not guaranteed by the repo
- [ ] Validation steps listed and repeatable (deterministic validate/fail/skip behavior)
- [ ] Governance + FAIR+CARE + sovereignty considerations explicitly stated
- [ ] The README makes it hard to create orphan references (graph/API/UI/story ↔ evidence)

---

## 🗂️ Directory Layout

### This document

- `path`: `data/README.md` (must match front-matter)

### Related repository paths

Paths listed below reflect the canonical subsystem homes defined by the Master Guide. If a canonical root is missing in your current checkout, treat it as a repo gap (add the root; do not create alternates).

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Expected file tree for this sub-area

> Notes:
> - Bulk datasets belong under `raw/`, `work/`, `processed/` (organized by domain).
> - `catalog/dcat/` and `prov/` are canonical roots even when they contain placeholder outputs.
> - Items marked **(optional)** may not exist for all deployments/domains.

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
├── 📁 catalog/
│   └── 📁 dcat/                             # DCAT outputs (JSON-LD / TTL as adopted)
│
├── 📁 prov/                                 # PROV bundles (per run / per dataset)
│
├── 📁 graph/                                # (optional) graph import fixtures
│   ├── 📁 csv/                              # import-ready CSVs (nodes/edges/etc.)
│   └── 📁 cypher/                           # optional post-import scripts / migrations
│
├── 📁 sources/                              # (optional) global source registry/index
│   └── 📄 <source_index>.json               # (format not confirmed in repo)
│
└── 📁 reports/                              # (optional) derived evidence products / analysis outputs
    └── 📁 <domain>/
~~~

### Canonical placement rules

**Canonical staging (required, stage-first / v12 contract):**

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`

**Evidence outputs (machine-readable, consumed downstream):**

- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`

**Common optional artifacts (when adopted):**

- Graph fixtures (when used): `data/graph/**` (derived from `data/processed/**` and/or catalogs)
- Source registry (when used): `data/sources/**`
- Derived evidence products (when used): `data/reports/**`

**Domain runbooks (documentation, not bulk data):**

- `docs/data/<domain>/README.md` (recommended; see Master Guide “Repo top-levels expected”)

Recommended minimum content for each domain runbook:

- Domain scope + boundaries (what is in/out).
- Source list + licensing/attribution notes.
- Dataset inventory with evidence pointers (STAC Collection IDs, key STAC Item patterns, DCAT dataset IDs).
- Governance notes (classification/CARE label, sensitivity, redaction/generalization expectations).
- Refresh cadence + how to reproduce (commands or runbook link), where run logs/PROV are written.

If a domain also keeps dataset/module notes under `data/<domain>/**` (e.g., a dataset-specific README), keep it lightweight and link back to the canonical runbook.

**v13 proposal note (do not implement ad-hoc):**

- Some design docs describe a domain-first layout like `data/<domain>/{raw,work,processed}/`. Treat this as a **planned migration pattern** (v13) unless and until adopted; do **not** maintain both layouts in parallel without an explicit migration plan + governance review.

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/raw/<domain>/` | Immutable source snapshots (append-only; do not mutate in place) | ETL ingest | ETL transforms (read-only) |
| `data/work/<domain>/` | Intermediate transforms (regenerable) | ETL | ETL, validation, QA |
| `data/processed/<domain>/` | Canonical outputs used for catalogs + graph ingest | ETL | Catalog build, graph build, audits |
| `data/stac/**` | STAC Collections + Items (discovery + evidence) | Catalog build | Graph, API, UI, story validation |
| `data/catalog/dcat/**` | DCAT dataset/distribution outputs | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles | ETL + catalog build | Audits, provenance checks, Focus Mode |
| `data/graph/**` | (Optional) Graph import fixtures derived from governed outputs | Graph build | Neo4j loaders / migrations |
| `data/sources/**` | (Optional) Source registry/index | ETL / curation | Audits, attribution tooling |
| `data/reports/**` | (Optional) Derived evidence products / analysis outputs | ETL/analysis | Story Nodes, Focus Mode contexts |

---

## 🧭 Context

### Background

KFM’s maps, timelines, and narratives depend on **traceable evidence**. The `data/` directory provides a deterministic, auditable home for datasets and their evidence artifacts so that catalogs, graph ingest, APIs, and UI remain provenance-linked and reviewable.

### Assumptions

- ETL outputs are reproducible and idempotent (same input + config → same output), with run details recorded somewhere (`mcp/**` and/or `data/prov/**`).
- STAC is treated as the primary spatiotemporal asset catalog; DCAT and PROV are complementary standards for discovery and lineage.
- Some directories may exist as placeholders until a pipeline stage is implemented (e.g., DCAT/PROV outputs for early domains).

### Constraints / invariants

- Preserve canonical ordering: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**
- UI consumes **APIs only** (no direct Neo4j reads).
- Every published claim or UI layer must resolve to evidence IDs (no orphan references).
- Classification must propagate through lineage (no output is less restricted than any input in its ancestry).
- CI behavior should be deterministic: **validate if present; fail if invalid; skip if not applicable**.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we enforce `docs/data/<domain>/` as the canonical domain-runbook home in CI, and how do we handle legacy exceptions? | Maintainers | TBD |
| Do we standardize domain naming (e.g., `air-quality` vs `air_quality`) and enforce it in CI? | Data governance | TBD |
| What is the canonical validator toolchain for STAC/DCAT/PROV in CI (commands, versions, strictness)? | Data/Platform | TBD |
| When/if adopting the v13 domain-first layout (`data/<domain>/{raw,work,processed}`), what is the migration plan and deprecation policy? | Maintainers | TBD |

### Future extensions

- Add a canonical “source index” schema under `schemas/` for `data/sources/*.json` *(not confirmed in repo)*.
- Add per-domain freshness gates + classification docs with CI checks (promotion blocks when governance is missing).
- Add releases packaging under `releases/` (manifests/SBOMs/signed bundles) once the repo adopts that workflow.
- Add automated lineage checks linking `mcp/runs/**` → `data/prov/**` once PROV outputs are formalized across domains.

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

### Optional: sequence diagram (evidence resolution + API boundary)

~~~mermaid
sequenceDiagram
  participant Client as Web UI
  participant API as API Boundary
  participant Graph as Neo4j Graph
  participant Catalog as STAC/DCAT/PROV

  Client->>API: Request (map layer / focus bundle)
  API->>Catalog: Resolve evidence IDs (STAC/DCAT/PROV)
  API->>Graph: Query (with redaction/generalization rules)
  Graph-->>API: Result + provenance refs
  API-->>Client: Contracted payload (data + evidence links)
~~~

---

## 📦 Data & Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| External source snapshots | CSV/GeoJSON/GeoTIFF/PDF/etc. | Ingested into `data/raw/<domain>/` | Hashing + file integrity + (domain-specific) schema checks |
| Domain runbook | Markdown | `docs/data/<domain>/README.md` | Markdown protocol checks |
| Pipeline configs | YAML/JSON/etc. | `src/pipelines/**` | Lint + reproducibility rules |
| Governance policies | Markdown | `docs/governance/**` | Human review gates + policy lint (if present) |
| Schemas (STAC/DCAT/PROV) | JSON Schema | `schemas/{stac,dcat,prov}/**` | Schema lint + validator tests |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Raw snapshots | source-native | `data/raw/<domain>/...` | Append-only, hashed |
| Intermediate artifacts | CSV/JSON/Parquet/etc. | `data/work/<domain>/...` | Regenerable; schema where applicable |
| Canonical processed datasets | CSV/GeoJSON/Parquet/etc. | `data/processed/<domain>/...` | Validated + versioned |
| STAC Collections | JSON | `data/stac/collections/*.json` | STAC + KFM profile |
| STAC Items | JSON | `data/stac/items/**/*.json` | STAC + KFM profile |
| DCAT datasets/distributions | JSON-LD / TTL | `data/catalog/dcat/**` | DCAT + KFM profile |
| PROV bundles | JSON-LD / TTL | `data/prov/**` | PROV-O + KFM profile |
| Graph ingest fixtures | CSV/Cypher | `data/graph/**` *(optional)* | Graph ingest contracts *(not confirmed in repo)* |
| Derived evidence products | CSV/JSON/PNG/etc. | `data/reports/<domain>/**` *(optional)* | Must be provenance-linked before surfacing |

### Evidence artifact pattern (AI/analysis outputs)

Evidence artifacts (including AI/analysis outputs) are treated as datasets: they must land in a governed output location, be cataloged, and be traceable back to inputs.

- Write governed outputs under `data/processed/<domain>/...` (preferred) or `data/reports/<domain>/...` (if explicitly “derived evidence product”).
- Register outputs in STAC (and DCAT where required), and include PROV lineage for how they were produced.
- If an artifact is used by graph/API/UI/story, reference it by evidence identifiers (STAC Item/Collection IDs, DCAT dataset IDs, PROV activity IDs), not ad-hoc file paths.
- Expose artifacts only via the API boundary, applying classification propagation and redaction/generalization consistently.

### Sensitivity & redaction

- If any dataset contains sensitive locations or culturally sensitive knowledge, public-facing outputs must be **generalized/redacted** according to governance policies.
- Redaction/generalization is enforced at the **API boundary** and must be reflected consistently in Story Nodes and Focus Mode.
- Classification propagation is mandatory: no derived artifact may have a less restrictive classification than any of its inputs.

### Quality signals

- Completeness checks (required keys present, non-null rates)
- Range/domain checks (value plausibility, date bounds)
- Geometry validity checks (if spatial)
- Referential integrity checks (IDs referenced by other artifacts resolve)
- Determinism checks (reruns produce stable diffs)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (required)

Every new dataset or evidence artifact that will be used downstream (graph/API/UI/story) must have:

- **STAC:** a Collection and Item(s) describing the asset(s) and their location/footprint/time (as applicable).
- **DCAT:** a dataset/distribution record enabling discovery (minimum: title, description, license, keywords).
- **PROV:** an activity record describing how it was produced (inputs, tool/run identity, and derived outputs).

### Cross-layer linkage expectations

- STAC assets/links must resolve to governed `data/processed/**` outputs (or an approved external distribution) and carry licensing/attribution fields.
- DCAT distributions should reference the same underlying distributions as STAC (or link to the STAC catalog) to avoid duplicated or diverging metadata.
- PROV must link raw → work → processed and reference run identifiers/tool versions sufficient to reproduce or audit.
- Graph nodes/edges should store evidence identifiers and metadata pointers, not duplicate full data payloads.
- APIs must return provenance pointers and apply redaction/classification propagation; the UI consumes only the API.

### STAC

- **Canonical location:** `data/stac/collections/` and `data/stac/items/`
- Minimum expectation: see the alignment policy above; domains document their Collection/Item inventory in the domain runbook.
- Collections involved: *(domain-specific; list in each domain runbook)*
- Items involved: *(domain-specific; list in each domain runbook)*
- Extension(s): *(if adopted; not confirmed in repo)*

### DCAT

- **Canonical location:** `data/catalog/dcat/`
- DCAT is the discovery layer for datasets/distributions (complementary to STAC assets).
- Minimum expectation: see the alignment policy above (title, description, license, keywords).
- Cross-linking expectation: DCAT datasets/distributions reference the corresponding STAC Collection(s) and/or exported distributions.

> Some deployments may also publish “human-friendly” DCAT summaries under `docs/data/<domain>/` or via an API endpoint; the on-disk canonical root remains `data/catalog/dcat/`.

### PROV-O

- **Canonical location:** `data/prov/`
- PROV provides lineage for each transformation stage and dataset generation activity.
- Minimum expectation: each dataset generation step has a PROV activity record linking raw → work → processed and naming the responsible agent/tool/run (see alignment policy above).

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
| APIs | Serve contracts; enforce redaction/generalization | REST/GraphQL |
| UI | Map + narrative exploration | API calls only |
| Story Nodes | Curated narrative | Provenance-linked content |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| STAC/DCAT/PROV schema bundles | `schemas/{stac,dcat,prov}/` | Validate in CI |
| Story Node schema | `schemas/story_nodes/` | Validate in CI |
| UI layer registry schema | `schemas/ui/` | Validate in CI |
| Telemetry schema | `schemas/telemetry/` | Validate in CI |
| API contracts | `src/server/` + docs | Contract tests required |

> Schema extensions are still expected to live under the canonical `schemas/**` roots (avoid scattering “one-off” schemas inside domain folders).

### Extension points checklist (for future work)

- [ ] Data: new domain added under `data/raw|work|processed/<domain>/`
- [ ] Catalogs: STAC Collection + Item(s) created and validated
- [ ] DCAT: dataset/distribution generated (or placeholder declared) and cross-linked
- [ ] PROV: activity + agent identifiers recorded (or placeholder declared)
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
  - governance classification that allows surfacing.

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
- [ ] Schema validation (STAC/DCAT/PROV): **validate if present; fail if invalid; skip if not applicable**
- [ ] Idempotence check (optional but recommended): run the same pipeline twice and confirm no unintended diffs
- [ ] No orphan references (IDs cited by graph/API/UI/story resolve to evidence)
- [ ] Deterministic outputs (stable IDs; diffable reruns)
- [ ] Security + secrets scanning (no credentials; no disallowed sensitive content)
- [ ] Sovereignty checks (generalize/redact sensitive locations where required)
- [ ] Classification propagation checks (no “restricted → public” leakage without review)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) validate docs (markdown protocol)
# 2) validate STAC/DCAT/PROV (schema + profile)
# 3) run ETL/catalog pipelines (deterministic)
# 4) run graph build + tests (if applicable)
~~~

### Telemetry signals (if applicable)

| Signal | Source | Where recorded |
|---|---|---|
| `run_id` | ETL/Catalog run | `mcp/runs/**` |
| dataset hash | hashing step | `data/prov/**` and/or run log |
| validation status | schema validators | CI logs + artifacts |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Escalate for governance review when introducing:

- new external data sources,
- new sensitive layers (protected locations / culturally sensitive knowledge),
- new AI narrative behavior that could be mistaken for factual content,
- new public-facing endpoints exposing data,
- any change in classification of existing data.

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
| v1.0.1 | 2025-12-24 | Align to Universal doc structure; clarify “not confirmed” markers | TBD |
| v1.0.2 | 2025-12-26 | Standardize staging semantics; clarify domain docs vs bulk data; expand CI contract language | TBD |
| v1.0.3 | 2025-12-27 | Tighten template conformity; clarify canonical vs optional roots; add explicit placement rules | TBD |
| v1.0.4 | 2025-12-28 | Sync directory layout with Master Guide; add STAC/DCAT/PROV alignment policy + evidence artifact pattern; add evidence/API boundary sequence diagram; clarify DCAT/PROV as canonical roots | TBD |

---

Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (design intent): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
