---
title: "Kansas Frontier Matrix — Contributing Guide"
path: "CONTRIBUTING.md"
version: "v1.1.0-draft"
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

doc_uuid: "urn:kfm:doc:contributing:v1.1.0-draft"
semantic_document_id: "kfm-contributing-v1.1.0-draft"
event_source_id: "ledger:kfm:doc:contributing:v1.1.0-draft"
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

# Contributing to Kansas Frontier Matrix

Thanks for helping build **Kansas Frontier Matrix (KFM)**.

KFM is **contract-first** and **evidence-first**: contributions must preserve the canonical pipeline ordering and the **“no unsourced narrative”** rule in any user-facing context (especially Story Nodes and Focus Mode).

**Canonical flow (do not break):**  
**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

---

## 📘 Overview

### Purpose
This guide defines **how** to contribute changes to KFM while preserving architectural invariants, governance requirements (FAIR+CARE + sovereignty), and validation expectations across the pipeline.

### Scope

| In Scope | Out of Scope |
|---|---|
| Docs, templates, runbooks, ADRs | Ad-hoc policies not grounded in repo standards |
| Data domain additions + updates (with provenance + catalogs) | Unsourced narratives presented as fact |
| ETL/pipeline work that writes outputs under `data/**` | Pipelines that write catalog artifacts into `docs/` |
| STAC/DCAT/PROV generation + validation | UI querying Neo4j directly (bypassing API boundary) |
| Graph/ontology mappings + ingest fixtures | Publishing sensitive locations without required redaction/generalization |
| API endpoints, contracts, redaction rules, contract tests | Unreviewed predictive/AI content in Focus Mode |

### Audience
- Primary: contributors adding data, pipelines, catalogs, graph mappings, APIs, UI layers, Story Nodes.
- Secondary: reviewers verifying governance, provenance, and CI readiness.

### Definitions
- Glossary (if present): `docs/glossary.md`
- Key terms used here:
  - **Domain pack**: the minimal set of data + docs + transforms + tests that makes a domain participate in the canonical pipeline.
  - **Evidence product**: a dataset/artifact that can be referenced by Story Nodes and UI with STAC/DCAT/PROV identifiers.
  - **Focus Mode**: provenance-only consumption view (no uncited narrative; predictive content opt-in with uncertainty metadata).

### Key artifacts (what this guide points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + invariants |
| v13 Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Maintainers | v13-ready structure + CI mapping |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs governance | Required doc structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story governance | Provenance-linked narrative format |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API governance | Contract-first endpoint changes |
| Schemas | `schemas/**` | Data/API governance | STAC/DCAT/PROV/story/ui/telemetry validation |

### Definition of done (for this guide)
- [ ] Front-matter complete + valid
- [ ] Canonical pipeline ordering and invariants stated unambiguously
- [ ] Canonical repo layout + “where things go” table included
- [ ] Contribution workflows include stage-specific checklists
- [ ] Validation/CI expectations are listed and repeatable
- [ ] Governance + CARE/sovereignty + sensitivity handling is explicit

---

## 🗂️ Directory Layout

### This document
- `path`: `CONTRIBUTING.md` (must match front-matter)

### Related repository paths (canonical)

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | immutable snapshots → intermediates → normalized outputs |
| Catalog outputs | `data/stac/**`, `data/catalog/dcat/**`, `data/prov/**` | STAC/DCAT/PROV artifacts (machine-validated) |
| Graph import artifacts | `data/graph/csv/**`, `data/graph/cypher/**` | Neo4j loader inputs / graph build exports |
| Pipelines (code) | `src/pipelines/**` | deterministic transforms; write outputs to `data/**` |
| Pipelines (docs/runbooks) | `docs/pipelines/<domain>/**` | domain ETL docs, runbooks, ADR links |
| Graph (code) | `src/graph/**` | ontology bindings, ingest, migrations, constraints |
| API boundary | `src/server/**` | endpoints, redaction, query services |
| API contracts | `src/server/contracts/**` | OpenAPI/GraphQL contracts + tests |
| UI | `web/**` | React/MapLibre (and optional 3D) UI; no direct graph calls |
| Story Nodes | `docs/reports/story_nodes/**` | draft → published narrative nodes |
| Runs/experiments | `mcp/runs/**`, `mcp/experiments/**` | run manifests, logs, artifacts |
| Releases | `releases/**` | signed bundles, manifests, SBOMs, telemetry snapshots |

### Top-level overview (target)

~~~text
📁 .
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
├── 📁 releases/
├── 📄 README.md
├── 📄 LICENSE
├── 📄 CITATION.cff
├── 📄 CHANGELOG.md
├── 📄 CONTRIBUTING.md
├── 📄 SECURITY.md
├── 📄 .editorconfig
├── 📄 .pre-commit-config.yaml
├── 📄 docker-compose.yml
└── 📄 .env.example
~~~

### Canonical homes by stage

| Stage | Canonical home | What belongs here |
|---|---|---|
| ETL / pipelines | `src/pipelines/` | deterministic transforms; run manifests; outputs in `data/**` |
| Domain pipeline docs | `docs/pipelines/<domain>/` | runbooks, domain conventions, known caveats |
| Catalogs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | STAC items/collections; DCAT datasets; PROV bundles |
| Graph | `src/graph/` + `data/graph/` | ontology-governed ingest; import fixtures/CSVs/Cypher |
| API boundary | `src/server/` | contracts; redaction; query services |
| UI | `web/` | map layers, Focus Mode UI, citation rendering |
| Story Nodes | `docs/reports/story_nodes/` | templates; draft; published; assets |
| Releases | `releases/` | manifests; SBOMs; signed bundles; telemetry snapshots |

---

## 🧭 How to contribute (workflow)

### 1) Pick a pipeline stage first
Before writing code or adding data, decide which stage your change primarily impacts:

- **Docs**: templates, governance docs, runbooks, ADRs
- **Data**: new domain pack, new dataset, corrected dataset, new evidence assets
- **ETL**: transforms producing `data/<domain>/{work,processed}`
- **Catalogs**: generating/validating STAC/DCAT/PROV artifacts
- **Graph**: ontology bindings, ingest, migrations, constraints
- **API**: endpoints, query services, redaction/generalization rules, contracts
- **UI**: layers, Focus Mode UI, citation rendering, a11y
- **Story Nodes**: draft/published nodes + provenance

If your change is cross-stage, include a short **impact note** in your PR description covering:
- what changed,
- why it changed,
- which pipeline stages are touched,
- how you validated each stage.

### 2) Use an ADR for ambiguous placement or new invariants
If you’re unsure where your change belongs, open a small PR that adds an ADR proposal under:
- `docs/architecture/adr/`

The ADR should describe: placement, contracts touched, validation plan, and governance implications.

### 3) Keep PRs reviewable
KFM favors smaller PRs that preserve provenance and contract integrity over “mega merges.”
If you must do a large cross-stage change, structure it as:
- PR 1: contracts + schemas + doc updates
- PR 2: pipeline + data outputs + catalogs
- PR 3: graph ingest + API + UI integration
- PR 4: Story Nodes (draft → published) + governance sign-off

---

## 📦 Data & Metadata

### Data lifecycle (required staging)
For each domain under `data/<domain>/`:
- `raw/` — immutable source snapshots (do not “edit in place”; add new versions)
- `work/` — intermediate transforms
- `processed/` — normalized outputs used for catalogs and graph ingest

Global metadata outputs:
- STAC: `data/stac/collections/` and `data/stac/items/`
- DCAT: `data/catalog/dcat/`
- PROV: `data/prov/`
- Graph import: `data/graph/csv/` and `data/graph/cypher/`

### Domain expansion pattern
- New domains go under `data/<domain>/...`
- Domain docs and runbooks go under `docs/pipelines/<domain>/...`
- Choose one canonical doc location for a domain (avoid duplicates); link from `docs/MASTER_GUIDE_v12.md` when appropriate.

### Domain pack (recommended minimum structure)
~~~text
📁 data/<domain>/
├── 📁 raw/
├── 📁 work/
└── 📁 processed/

📁 docs/pipelines/<domain>/
├── 📄 README.md
├── 📄 RUNBOOK.md
└── 📄 DATA_SOURCES.md

📁 src/pipelines/<domain>/
├── 📄 README.md
└── 📁 etl/

📁 data/stac/
├── 📁 collections/
└── 📁 items/

📁 data/catalog/dcat/
└── 📄 <domain>.dcat.jsonld  (or equivalent)

📁 data/prov/
└── 📄 <domain>.<run_id>.prov.json  (or equivalent)
~~~

### Determinism and reproducibility rules
- Pipelines are **idempotent** and **deterministic** given the same inputs/config.
- Pipeline runs should emit provenance (PROV activity bundle) under `data/prov/`.
- Pipelines never write STAC/DCAT/PROV artifacts into `docs/`.

---

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset / evidence product
For each dataset or evidence product you add or update, include:
- STAC Collection + Item(s)
- DCAT mapping record (minimum: title/description/license/keywords)
- PROV activity describing lineage
- Version lineage links reflected in catalogs and the graph

### Graph linkage expectations
Graph nodes should reference:
- STAC Item IDs
- DCAT dataset ID
- PROV activity ID

### Story Node linkage expectations
Story Nodes should link to:
- graph entity IDs,
- STAC/DCAT/PROV evidence IDs,
- local assets with attribution.

### Versioning expectations
- New versions link predecessor/successor.
- Graph mirrors version lineage (so UI and Focus Mode remain traceable over time).

---

## 🧱 Architecture

### Non‑negotiables (architectural invariants)
These are enforced by design and/or CI gates:

1. **No UI direct-to-graph reads**
   - `web/` must never query Neo4j directly; all graph access is via `src/server/`.

2. **No unsourced narrative in governed views**
   - Focus Mode consumes provenance-linked context only.
   - Published Story Nodes must be provenance-linked and validate.

3. **Contracts are canonical**
   - Schemas/specs live in `schemas/`.
   - API contracts live in `src/server/contracts/`.
   - Contracts must validate in CI.

4. **Data outputs are not code**
   - Derived datasets belong under `data/<domain>/processed/`, not under `src/`.

5. **STAC/DCAT/PROV are first-class**
   - STAC, DCAT, and PROV remain required for datasets and evidence products.

6. **Redaction/generalization is layered**
   - Any restricted or sensitive knowledge must be protected consistently across data, catalog, API, and UI layers.

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges + resolvable references |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Next-evolution extension points (use the extension matrix mindset)
- (A) Data: new domain, new STAC extension profiles
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types with explicit provenance
- (D) API: new endpoints with contract tests and redaction policies
- (E) UI: new layer registry entries with provenance pointers and CARE gating

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”
- Draft story nodes live under `docs/reports/story_nodes/draft/`.
- Published story nodes live under `docs/reports/story_nodes/published/<story_slug>/`.
- Published Story Nodes must validate (front-matter, citations, entity references, redaction compliance).

### Focus Mode rule (hard gate)
- Focus Mode only consumes provenance-linked content.
- Predictive or AI-generated content:
  - is **opt-in**,
  - includes **uncertainty metadata**,
  - never appears as unmarked fact.

### Citation expectations (Story Nodes + Focus Mode)
- Use the governed Story Node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`.
- Ensure citations resolve to evidence (dataset/document IDs, STAC/DCAT/PROV IDs, or approved document sources).
- Citation rendering expects the `【source†Lx-Ly】` style references.

### Optional Focus Mode controls (when authoring Story Nodes)
~~~yaml
focus_layers:
  - "TBD"

focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

---

## 🧪 Validation & CI/CD

### Minimum CI gates (baseline)
Your PR should pass the gates relevant to what you changed:

- Markdown protocol validation (front-matter + required section structure)
- Schema validation (STAC/DCAT/PROV/story/ui/telemetry as applicable)
- Story Node validation (if touching `docs/reports/story_nodes/**`)
- Graph integrity tests (if touching graph ingest/constraints/artifacts)
- API contract tests (if touching `src/server/contracts/**` or API behaviors)
- UI layer registry schema checks (if touching `web/**/layers/**`)
- Security + sovereignty scanning gates (where applicable)

### Local development expectations (contract-level)
The exact commands may differ by environment, but the expectations are:

1. Run the pre-commit hooks configured in `.pre-commit-config.yaml`.
2. Run tests relevant to your change (pipelines / server / web).
3. Run validators relevant to your change (schemas/contracts/story nodes/etc.).

Repo lint reminders:
- Do **not** add YAML front-matter to code files. YAML front-matter is for Markdown documents only.
- Prefer `~~~` fences for code blocks inside governed Markdown docs.
- Avoid introducing new canonical roots (duplicate subsystem roots require explicit deprecation markers).

---

## ⚖ FAIR+CARE & Governance

Before submitting changes, check:
- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/governance/REVIEW_GATES.md`

### Governance review triggers
Extra review is typically required for:
- New sensitive layers
- New AI narrative behaviors
- New external data sources
- New public-facing endpoints

### Sovereignty safety
Any restricted locations or culturally sensitive knowledge must be protected by:
- generalization of geometry where required,
- API-level redaction,
- Story Node asset review gates.

### AI usage boundaries (repo-governed)
Allowed transformations for contributors (when used to assist docs/data work):
- summarize
- structure_extract
- translate
- keyword_index

Prohibited actions:
- generate_policy
- infer_sensitive_locations

If you introduce any AI-assisted behavior in the product (API/UI/Story pipeline), it must be:
- explicitly opt-in where required,
- annotated with uncertainty metadata,
- excluded from Focus Mode unless it remains provenance-linked and correctly labeled.

---

## ✅ PR checklist (copy into your PR description)

### General
- [ ] My change fits a single pipeline stage (or clearly explains cross-stage impact).
- [ ] I used the correct canonical home(s) and did not create duplicate subsystem roots.
- [ ] I ran the pre-commit hooks and fixed any failures.
- [ ] I ran relevant tests and validators (schemas/contracts/story nodes/etc.).
- [ ] I did not introduce unsourced narrative in any governed context.

### Data / ETL / Catalog
- [ ] If I added/updated data, it is placed under `data/<domain>/{raw,work,processed}/`.
- [ ] I included STAC/DCAT/PROV outputs (and they validate).
- [ ] Pipeline outputs are deterministic/diffable; provenance is emitted to `data/prov/**`.

### Graph
- [ ] Graph ingest aligns with ontology bindings and uses only processed + catalog + provenance artifacts.
- [ ] Graph nodes reference STAC/DCAT/PROV identifiers where required.
- [ ] No orphan references (entity/evidence/story refs resolve).

### API
- [ ] If I changed the API or contracts, I updated `src/server/contracts/` and tests.
- [ ] Redaction/generalization rules are enforced at the API boundary where applicable.
- [ ] Changes are backward-compatible or explicitly versioned/deprecated.

### UI
- [ ] UI still relies only on `src/server/` (API) for graph data (no direct Neo4j calls).
- [ ] UI layer registry entries validate against `schemas/ui/**` where applicable.
- [ ] Citation rendering and audit/provenance affordances remain intact.

### Story Nodes / Focus Mode
- [ ] Draft story nodes are in `docs/reports/story_nodes/draft/`.
- [ ] Published story nodes are provenance-linked and validate (front-matter, citations, entity refs, redaction).
- [ ] Focus Mode content remains provenance-linked only; any AI content is opt-in and clearly labeled.

---

## 🕰️ Version History

| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0-draft | 2025-12-21 | Initial CONTRIBUTING guide aligned to v13 blueprint | <your-name> |
| v1.1.0-draft | 2025-12-27 | Enriched to universal governed doc structure + stage checklists + v13-ready contracts and CI mapping | <your-name> |

---

## Footer refs

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Redesign Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Templates: `docs/templates/`
- Standards: `docs/standards/`
- Governance: `docs/governance/`
