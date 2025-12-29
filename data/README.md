---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.5"
last_updated: "2025-12-29"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.5"
semantic_document_id: "kfm-data-readme-v1.0.5"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.5"
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

This README defines the **canonical on-disk contract** for KFM datasets and pipeline artifacts that live under `data/`. It exists to keep the system **contract-first**, **evidence-first**, **auditable**, and **deterministic** across the canonical pipeline:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

Authority and precedence:

1. `docs/MASTER_GUIDE_v12.md` defines the **canonical pipeline ordering** and repo invariants.
2. Governance documents under `docs/governance/**` define **classification, sensitivity, review gates, and sovereignty rules**.
3. Schemas and contracts under `schemas/**` and the API boundary define **validation and consumer-facing guarantees**.
4. This README defines **where data and evidence artifacts live on disk**, and how downstream layers must resolve them.

What this document governs:

- **Where** different kinds of data belong (`raw/`, `work/`, `processed/`) and what “canonical” means.
- **Where evidence metadata and lineage** belong (`stac/`, `catalog/dcat/`, `prov/`) and how downstream systems must resolve them.
- **How to avoid orphan references** (graph/API/UI/story identifiers must resolve back to evidence and governed outputs).
- **How governance and sensitivity propagate** (no output becomes less restricted than its upstream inputs).

Non-negotiables enforced by this README:

- **Canonical ordering is non-negotiable:** ETL must produce governed outputs and catalogs **before** graph ingest and user-facing layers.
- **Staging is stage-first for v12:** `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`.
- **Catalogs are boundary artifacts:** downstream consumers resolve datasets through STAC/DCAT/PROV, not ad-hoc file paths.
- **No shortcuts:** do not load raw data directly into the graph, and do not let the UI read Neo4j directly (all access is via the API boundary).
- **One canonical home per subsystem:** if an expected root is missing, add the root in-place (do **not** create alternate roots).
- **Classification propagation is mandatory:** derived outputs cannot be less restricted than any input in their lineage.
- Anything not verifiable in the current repo state must be labeled **“not confirmed in repo.”**

### Scope

| In Scope | Out of Scope |
|---|---|
| Staging outputs under `data/raw/**`, `data/work/**`, `data/processed/**` | Source code implementation details (`src/**`) |
| Evidence artifacts and discovery/lineage metadata: `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | UI runtime assets/config (belongs in `web/**`) |
| Deterministic placement and integrity rules (no orphan refs; stable IDs) | API contract text (belongs at the API boundary docs/contracts) |
| Optional derived evidence products stored under `data/reports/**` | Experiments and run logs (`mcp/**`) |
| Optional graph ingest fixtures derived from processed outputs (`data/graph/**`) | Story Nodes (belongs in `docs/reports/story_nodes/**`) |

### Audience

- **Primary:** data engineers and contributors running ETL + catalog builds and producing governed outputs under `data/**`.
- **Secondary:** reviewers validating catalogs + provenance; graph maintainers; curators producing Story Nodes and Focus Mode views.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*

Key terms used here:

- **Domain:** a bounded topic area (e.g., hydrology, historical maps, air quality) with its own inputs, transforms, and outputs.
- **Evidence artifact:** any derived output treated as **data + metadata** (STAC/DCAT/PROV) before it appears in UI or narrative.
- **Orphan reference:** an ID used by graph/API/UI/story that cannot be resolved back to governed `processed/` outputs and their evidence artifacts.
- **Deterministic pipeline:** same inputs + config produce stable, diffable outputs (idempotent runs; no hidden state).

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering is non-negotiable |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | This README follows its section order |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Curators | Narrative must be provenance-linked |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | Required for API contract changes |
| Markdown guide v13 | `docs/MARKDOWN_GUIDE_v13.md` | Docs | Writing conventions and examples *(not confirmed in repo)* |
| Data intake and ingestion architecture | `docs/architecture/KFM_INGEST_ARCHITECTURE.md` | Maintainers | ETL reproducibility + catalog generation patterns *(not confirmed in repo)* |
| v13 redesign blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | Design intent; not a guarantee of current state *(not confirmed in repo)* |
| Example domain module: Land Treaties | `docs/data/historical/land-treaties/README.md` | Domain steward | Example domain module *(if present)* |
| Example domain module: Air Quality | `docs/data/air-quality/README.md` | Domain steward | Example domain module *(if present)* |
| Example domain module: Soils (SDA) | `data/soils/sda/README.md` | Domain steward | Example domain module *(if present; legacy path possible)* |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Authority for classification + review gates |
| Ethics policy | `docs/governance/ETHICS.md` | Governance | Human/Community impact considerations |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | Indigenous/culturally sensitive handling rules |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Any concrete claim links to a dataset ID / schema / ticket / commit where applicable (or is marked “not confirmed in repo”)
- [ ] Canonical staging + evidence placement rules documented and consistent with the Master Guide ordering
- [ ] “Optional / planned / legacy” paths explicitly labeled when not guaranteed by the repo
- [ ] Validation steps listed and repeatable with deterministic validate/fail/skip behavior
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

> Note: Catalog build/validation tooling may live in `src/pipelines/**` and/or `tools/**`, but must have one canonical home (avoid duplicated “two ways to do the same thing”).

### Minimum required `data/` tree

This is the **v12 canonical** on-disk contract for the `data/` directory.

These roots should exist even if early domains only have placeholder outputs: `data/catalog/dcat/` and `data/prov/` are still part of the contract.

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
└── 📁 prov/                                 # PROV bundles (per run / per dataset)
~~~

### Optional extension roots

Only add these roots if you have an explicit, reviewed need. All contents must still be derived from governed outputs (`data/processed/**`) and must remain provenance-linked.

~~~text
📁 data/
├── 📁 graph/                                # optional: graph import fixtures
│   ├── 📁 csv/                              # import-ready CSVs (nodes/edges/etc.)
│   └── 📁 cypher/                           # optional post-import scripts / migrations
│
├── 📁 sources/                              # optional: global source registry/index (format not confirmed)
│   └── 📄 <source_index>.json
│
└── 📁 reports/                              # optional: derived evidence products / analysis outputs
    └── 📁 <domain>/
~~~

### Canonical placement rules

**Canonical staging:**

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`

**Evidence outputs:**

- STAC: `data/stac/collections/` + `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`

**Domain runbooks:**

- Recommended: `docs/data/<domain>/README.md` (or consistent equivalent)
- Keep dataset/module notes under `data/**` lightweight; link back to the canonical runbook.

Recommended minimum content for each domain runbook:

- Domain scope + boundaries (what is in/out).
- Source list + licensing/attribution notes.
- Dataset inventory with evidence pointers (STAC Collection IDs, key STAC Item patterns, DCAT dataset IDs).
- Governance notes (classification/CARE label, sensitivity, redaction/generalization expectations).
- Refresh cadence + how to reproduce (commands or runbook link), and where run logs/PROV are written.

### v13 layout note

Some design documents describe a domain-first layout like `data/<domain>/{raw,work,processed}/`. Treat this as a **planned migration pattern** unless and until adopted with an explicit migration plan and governance review. Do **not** maintain both layouts in parallel.

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/raw/<domain>/` | Immutable source snapshots (append-only; do not mutate in place) | ETL ingest | ETL transforms (read-only) |
| `data/work/<domain>/` | Intermediate transforms (regenerable) | ETL | ETL, validation, QA |
| `data/processed/<domain>/` | Canonical outputs used for catalogs + graph ingest | ETL | Catalog build, graph build, audits |
| `data/stac/**` | STAC Collections + Items (discovery + evidence) | Catalog build | Graph, API, UI, story validation |
| `data/catalog/dcat/**` | DCAT dataset/distribution outputs | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles | ETL + catalog build | Audits, provenance checks, Focus Mode |
| `data/graph/**` | Graph import fixtures derived from governed outputs | Graph build | Neo4j loaders / migrations |
| `data/sources/**` | Source registry/index | ETL / curation | Audits, attribution tooling |
| `data/reports/**` | Derived evidence products / analysis outputs | ETL/analysis | Story Nodes, Focus Mode contexts |

---

## 🧭 Context

### Background

KFM’s maps, timelines, and narratives depend on traceable evidence. The `data/` directory provides a deterministic, auditable home for datasets and their evidence artifacts so that catalogs, graph ingest, APIs, and UI remain provenance-linked and reviewable.

### Assumptions

- ETL outputs are reproducible and idempotent (same input + config → stable outputs), with run details recorded in `data/prov/**` and/or `mcp/runs/**`.
- STAC is treated as the primary spatiotemporal asset catalog; DCAT and PROV are complementary standards for discovery and lineage.
- “Boundary artifacts” (STAC/DCAT/PROV) are required before a dataset is considered fully publishable into downstream layers.

### Constraints and invariants

- Preserve canonical ordering: **ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**
- UI consumes **APIs only** (no direct Neo4j reads).
- Every published claim or UI layer must resolve to evidence IDs (no orphan references).
- Classification must propagate through lineage (no “restricted → public” leakage without review).
- CI behavior should be deterministic: **validate if present; fail if invalid; skip if not applicable**.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we enforce `docs/data/<domain>/` as the canonical domain-runbook home in CI, and how do we handle legacy exceptions? | Maintainers | TBD |
| Do we standardize domain naming (e.g., `air-quality` vs `air_quality`) and enforce it in CI? | Data governance | TBD |
| What is the canonical validator toolchain for STAC/DCAT/PROV in CI (commands, versions, strictness)? | Data/Platform | TBD |
| If adopting a domain-first `data/<domain>/{raw,work,processed}` layout in v13, what is the migration plan and deprecation policy? | Maintainers | TBD |

### Future extensions

- Add a canonical “source index” schema under `schemas/` for `data/sources/*.json` *(not confirmed in repo)*.
- Add per-domain freshness gates + classification docs with CI checks (promotion blocks when governance is missing).
- Add releases packaging under `releases/` (manifests/SBOMs/signed bundles) once the repo adopts that workflow.
- Add automated lineage checks linking `mcp/runs/**` → `data/prov/**` once PROV outputs are formalized across domains.

---

## 🗺️ Diagrams

### System and dataflow

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph (references back to catalogs)"]
  G --> H["API Layer (contracts + redaction)"]
  H --> I["Map UI (React · MapLibre · optional Cesium)"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked bundle)"]
~~~

### Optional sequence diagram

Evidence resolution happens via the API boundary; clients should never need to know on-disk paths.

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

### Evidence artifact pattern

KFM treats analysis output and AI-generated datasets as first-class datasets with full provenance.

Rules:

- Store governed outputs under `data/processed/<domain>/...` (preferred) or `data/reports/<domain>/...` (explicitly “derived evidence product”).
- Register outputs in STAC (and DCAT where required) and include PROV lineage for how they were produced.
- If an artifact is used by graph/API/UI/story, reference it by evidence identifiers (STAC Item/Collection IDs, DCAT dataset IDs, PROV activity IDs), not ad-hoc file paths.
- Expose artifacts only via the API boundary, applying classification propagation and redaction/generalization consistently.

### Sensitivity and redaction

- If any dataset contains sensitive locations or culturally sensitive knowledge, public-facing outputs must be generalized/redacted according to governance policies.
- Redaction/generalization must be consistent across:
  - the dataset outputs (`data/processed/**`),
  - catalogs (STAC/DCAT metadata),
  - API responses,
  - UI rendering and narrative surfaces.
- Classification propagation is mandatory: no derived artifact may be less restricted than any of its inputs.

### Quality signals

- Completeness checks (required keys present, non-null rates)
- Range/domain checks (value plausibility, date bounds)
- Geometry validity checks (if spatial)
- Referential integrity checks (IDs referenced by other artifacts resolve)
- Determinism checks (reruns produce stable diffs)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC DCAT PROV alignment policy

Every new dataset or evidence artifact that will be used downstream (graph/API/UI/story) must have boundary artifacts:

- **STAC:** a Collection and Item(s) describing the asset(s) and their location/footprint/time (as applicable).
- **DCAT:** a dataset/distribution record enabling discovery (minimum: title, description, license, keywords).
- **PROV:** an activity record describing how it was produced (inputs, tool/run identity, derived outputs, and hashes where available).

### Cross-layer linkage expectations

- STAC assets/links must resolve to governed `data/processed/**` outputs (or an approved external distribution) and carry licensing/attribution fields.
- DCAT distributions should reference the same underlying distributions as STAC (or link to the STAC catalog) to avoid diverging metadata.
- PROV must link raw → work → processed and reference run identifiers/tool versions sufficient to reproduce or audit.
- Graph nodes/edges should store evidence identifiers and metadata pointers, not duplicate full data payloads.
- APIs must return provenance pointers and apply redaction/classification propagation; the UI consumes only the API.

### STAC

- Canonical location: `data/stac/collections/` and `data/stac/items/`
- Minimum expectation: see the alignment policy above; domains document their Collection/Item inventory in the domain runbook.
- Extensions: *(domain-specific; coordinate profile changes rather than adding ad-hoc fields)*

### DCAT

- Canonical location: `data/catalog/dcat/`
- DCAT is the discovery layer for datasets/distributions (complementary to STAC assets).
- Minimum expectation: title, description, license, keywords.
- Cross-linking expectation: DCAT datasets/distributions reference the corresponding STAC Collection(s) and/or exported distributions.

> Some deployments may also publish human-friendly DCAT summaries under `docs/data/<domain>/` or via an API endpoint; the on-disk canonical root remains `data/catalog/dcat/`.

### PROV-O

- Canonical location: `data/prov/`
- PROV provides lineage for each transformation stage and dataset generation activity.
- Minimum expectation: each dataset generation step has a PROV activity record linking raw → work → processed and naming the responsible agent/tool/run.

### Versioning

- Dataset versioning must be deterministic and diffable; do not silently overwrite history.
- Use STAC versioning links and graph predecessor/successor relationships as applicable.

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

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| STAC/DCAT/PROV schema bundles | `schemas/{stac,dcat,prov}/` | Validate in CI |
| Story Node schema | `schemas/story_nodes/` | Validate in CI |
| UI layer registry schema | `schemas/ui/` | Validate in CI |
| Telemetry schema | `schemas/telemetry/` | Validate in CI |
| API contracts | `src/server/` + docs | Contract tests required |

> Schema extensions should live under the canonical `schemas/**` roots (avoid scattering one-off schemas inside domain folders).

### Extension points checklist

- [ ] Data: new domain added under `data/raw|work|processed/<domain>/`
- [ ] Catalogs: STAC Collection + Item(s) created and validated
- [ ] DCAT: dataset/distribution generated (or placeholder declared) and cross-linked
- [ ] PROV: activity + agent identifiers recorded (or placeholder declared)
- [ ] Graph: new labels/relations mapped + migration plan (if needed)
- [ ] APIs: contract version bump + tests (if needed)
- [ ] UI: layer registry entry + access rules (if used)
- [ ] Story Nodes: narrative references and citations updated (if used)
- [ ] Focus Mode: provenance references enforced (hard gate)
- [ ] Telemetry: new signals + schema version bump (if used)

> Cross-cutting note: new analysis products or AI-derived artifacts usually touch all layers (data → catalogs → graph → API → UI → story/focus), not just ETL.

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode

Datasets become focusable when they have:

- a resolvable evidence chain (STAC/DCAT/PROV IDs),
- stable IDs usable by graph/API/UI,
- governance classification that allows surfacing.

### Provenance-linked narrative rule

- Every Story Node claim must trace to a dataset, record, or asset ID.
- Story Nodes must separate **fact**, **inference**, and **hypothesis** explicitly; only facts may be stated as factual.
- Story Nodes must not introduce new “facts” that bypass evidence artifacts.

### Focus Mode hard gate

- Focus Mode consumes **provenance-linked content only** (every element must resolve to STAC/DCAT/PROV and governed outputs).
- Any predictive or AI-synthesized content must be:
  - explicitly opt-in,
  - clearly labeled as non-factual output,
  - accompanied by uncertainty/confidence metadata where applicable,
  - prohibited from inferring or revealing sensitive locations.

### Evidence surfacing expectations

- Story Node citations should be resolvable to evidence artifacts (e.g., a STAC Item, a dataset distribution, or a source document reference).
- When the UI supports it, citations should be actionable (e.g., opening an evidence panel or document viewer, and/or highlighting referenced geometry/time ranges).

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [-98.0000, 38.0000]
~~~

---

## 🧪 Validation & CI/CD

### Minimum validation steps

- [ ] Markdown protocol checks (front-matter present; template section order)
- [ ] STAC/DCAT/PROV schema validation: validate if present; fail if invalid; skip if not applicable
- [ ] PROV linkage checks: raw → work → processed references resolve
- [ ] No orphan references: IDs cited by graph/API/UI/story resolve to evidence artifacts
- [ ] Determinism checks: stable IDs; diffable reruns; idempotence where expected
- [ ] Graph integrity tests (constraints, evidence refs) when graph ingest fixtures are updated
- [ ] API contract tests when API contracts change
- [ ] Security and secrets scanning (no credentials; no disallowed sensitive content)
- [ ] Sovereignty checks (generalize/redact sensitive locations where required)
- [ ] Accessibility lint on UI changes (if applicable)

### Reproduction

Reproducibility expectations:

- Running the same pipeline on the same raw inputs should produce identical `data/processed/**` outputs (except for explicitly allowed timestamp fields).
- Prefer containerized execution and pinned dependency versions to reduce environment drift.

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Validate docs (markdown protocol)
# markdownlint data/ docs/

# 2) Validate STAC/DCAT/PROV (schema + profile)
# ./scripts/validate_all_catalogs.sh

# 3) Run ETL/catalog pipelines (deterministic)
# python -m src.pipelines.<domain_pipeline> --input data/raw/<domain>/ --output data/processed/<domain>/

# 4) Run tests (ETL + graph + API as applicable)
# pytest -q
~~~

### Telemetry signals

| Signal | Source | Where recorded |
|---|---|---|
| `run_id` | ETL/Catalog run | `mcp/runs/**` and/or `data/prov/**` |
| `dataset_hash` | Hashing step | `data/prov/**` and/or run log |
| `validation_status` | Schema validators | CI logs + artifacts |
| `classification_assigned` | Governance gate | Governance logs / review artifacts *(not confirmed in repo)* |
| `redaction_applied` | API boundary / export step | API logs + provenance bundle |
| `promotion_blocked` | Governance/CI gate | CI logs + review notes |
| `story_node_citation_count` | Story build | Telemetry logs *(not confirmed in repo)* |
| `focus_mode_bundle_views` | UI usage | Telemetry logs *(not confirmed in repo)* |

---

## ⚖ FAIR+CARE & Governance

### Review gates

Escalate for governance review when introducing:

- new external data sources,
- new sensitive layers (protected locations / culturally sensitive knowledge),
- new AI narrative behavior that could be mistaken for factual content,
- new public-facing endpoints exposing data,
- any change in classification of existing data.

### CARE and sovereignty considerations

- Treat Indigenous and culturally sensitive knowledge as high-risk by default.
- Protect restricted locations by:
  - geometry generalization where required,
  - API-level redaction,
  - Story Node review gates before publishing,
  - avoiding “inference by synthesis” (do not derive or reveal sensitive locations from combined signals).

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
| v1.0.4 | 2025-12-28 | Sync directory layout with Master Guide; add STAC/DCAT/PROV alignment policy + evidence artifact pattern; add API boundary sequence diagram; clarify DCAT/PROV as canonical roots | TBD |
| v1.0.5 | 2025-12-29 | Reconcile v12 stage-first layout with v13 design notes; split required vs optional `data/` roots; align CI gates, sovereignty safety, and Focus Mode hard gate language | TBD |

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
- Markdown guide v13: `docs/MARKDOWN_GUIDE_v13.md`
- Ingest architecture: `docs/architecture/KFM_INGEST_ARCHITECTURE.md`