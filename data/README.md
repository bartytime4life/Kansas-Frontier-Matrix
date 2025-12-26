---
title: "KFM Data Directory README"
path: "data/README.md"
version: "v1.0.2"
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

doc_uuid: "urn:kfm:doc:data:readme:v1.0.2"
semantic_document_id: "kfm-data-readme-v1.0.2"
event_source_id: "ledger:kfm:doc:data:readme:v1.0.2"
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

- Define the **canonical home for KFM datasets and pipeline artifacts**:
  - immutable **raw** source snapshots,
  - intermediate **work** artifacts (rerunnable),
  - governed **processed** outputs (downstream consumption),
  - machine-readable evidence artifacts for discovery + lineage (**STAC/DCAT/PROV**),
  - and (when applicable) **graph ingest fixtures** derived from processed outputs.

- Preserve KFM’s non-negotiable ordering by placement and linkage:

**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### Scope

| In Scope | Out of Scope |
|---|---|
| Data staging outputs (`data/raw/**`, `data/work/**`, `data/processed/**`) | Source code (`src/`) |
| Evidence artifacts: STAC/DCAT/PROV outputs (see “Catalog outputs” below) | UI runtime assets/config (`web/`) |
| Graph ingest fixtures generated from processed outputs (`data/graph/**`) | Story Nodes (`docs/reports/story_nodes/`) |
| Deterministic, diffable outputs and integrity rules (no orphan refs) | API contracts (belongs at the API boundary) |
| Domain packs inside `data/<domain>/` (README + governance + mappings + source notes) | Experiments/run logs (`mcp/`) |

### Audience

- **Primary:** data engineers and contributors running ETL/catalog builds and producing governed datasets.
- **Secondary:** maintainers/reviewers validating catalogs + provenance; curators publishing Story Nodes and Focus Mode content.

### Definitions

- Glossary link: `docs/glossary.md` *(not confirmed in repo)*

Key terms used here:

- **Domain pack:** the minimum set of docs + governance metadata that lets a domain participate in the pipeline.
- **Evidence artifact:** machine-readable metadata + lineage consumed downstream (STAC/DCAT/PROV and derived evidence products).
- **Orphan reference:** an ID used by graph/API/UI/story that cannot be resolved back to evidence (STAC/DCAT/PROV) and/or a governed dataset output.
- **Deterministic pipeline:** reruns produce stable, diffable outputs for the same inputs + config.

### Key artifacts

| Artifact | Path / Identifier | Status / notes |
|---|---|---|
| Master pipeline ordering + invariants | `docs/MASTER_GUIDE_v12.md` | Canonical; ordering is non-negotiable |
| v13 layout guidance (if adopted) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Draft design; used for target path alignment |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Governed Markdown structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Provenance-first narrative requirements |
| Repo structure standard | `docs/standards/KFM_REPO_STRUCTURE_STANDARD.md` | *(not confirmed in repo)* |
| Schema validation | `schemas/` | Source-of-truth validators *(presence not confirmed in repo)* |

### Definition of done

- [ ] Front-matter complete + valid; `path` matches file location
- [ ] Data staging + evidence artifact placement rules documented and consistent with Master Guide
- [ ] “Target / planned” paths are labeled when not confirmed in repo
- [ ] Validation expectations are actionable and deterministic (“validate/fail/skip” behavior)
- [ ] Governance + FAIR+CARE + sovereignty considerations explicitly stated

---

## 🗂️ Directory Layout

### This document

- `path`: `data/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains + staging | `data/` | Raw/work/processed outputs + domain packs |
| ETL + catalog pipelines | `src/pipelines/` | Deterministic transforms; outputs land under `data/**` |
| Catalog evidence | `data/stac/` | STAC Collections/Items (machine-readable discovery/evidence) |
| DCAT evidence | `data/catalog/dcat/` *(v13 target; may not exist yet)* | DCAT dataset/distribution outputs |
| PROV evidence | `data/prov/` *(v13 target; may not exist yet)* | PROV bundles (lineage) |
| Graph build + ontology | `src/graph/` | Ontology-governed ingest + mapping logic |
| Graph ingest fixtures | `data/graph/` | Import-ready CSVs/Cypher (if used) |
| API boundary | `src/server/` *(v13 target; not confirmed in repo)* | Contracts, redaction, query services |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Curated narrative artifacts and assets |
| Domain docs & templates | `docs/data/` | Domain documentation + templates (may include STAC/DCAT templates) |
| MCP | `mcp/` | Run manifests, experiments, model cards, SOPs |

### Target file tree for `data/`

> Notes:
> - Items marked **(planned)** may not exist yet *(not confirmed in repo)*.
> - **Canonical staging** is stage-first: `data/raw/` → `data/work/` → `data/processed/` (organized by domain inside each stage).
> - Domain packs live under `data/<domain>/` (docs/governance), but **bulk datasets** live under the staging folders.

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
│   └── 📁 <domain>/                         # canonical outputs (validated + versioned)
│
├── 📁 stac/
│   ├── 📁 collections/                      # STAC Collections (JSON)
│   ├── 📁 items/                            # STAC Items (JSON)
│   └── 📁 <domain>/                         # optional: domain-scoped STAC (if repo uses this pattern)
│
├── 📁 catalog/                              # (planned) v13 target
│   └── 📁 dcat/                             # DCAT outputs (JSON-LD / TTL as adopted)
│
├── 📁 prov/                                 # (planned) v13 target (PROV bundles)
│
├── 📁 graph/
│   ├── 📁 csv/                              # import-ready CSVs (nodes/edges/etc.)
│   └── 📁 cypher/                           # optional post-import scripts / migrations
│
├── 📁 <domain>/                             # domain pack docs (not bulk data)
│   ├── 📄 README.md                         # required: domain overview + evidence pointers
│   ├── 📁 sources/                          # source notes, licenses, attribution
│   ├── 📁 mappings/                         # crosswalks + field notes (optional)
│   └── 📁 governance/                       # CARE/sensitivity/redaction rules (optional)
│
└── 📁 reports/                              # optional evidence products / analysis outputs
    └── 📁 <domain>/
~~~

### Folder responsibilities

| Folder | Responsibility | Typical producers | Typical consumers |
|---|---|---|---|
| `data/raw/<domain>/` | Immutable source snapshots (append-only; do not mutate in place) | ETL ingest | ETL transforms (read-only) |
| `data/work/<domain>/` | Intermediate transforms (regenerable) | ETL | ETL, validation, QA |
| `data/processed/<domain>/` | Normalized outputs used for catalogs + graph ingest | ETL | Catalog build, graph build, audits |
| `data/stac/**` | STAC Collections + Items (discovery + evidence) | Catalog build | Graph, API, UI, story validation |
| `data/catalog/dcat/**` | DCAT dataset/distribution outputs *(planned)* | Catalog build | API, external exports |
| `data/prov/**` | PROV lineage bundles *(planned)* | ETL + catalog build | Audits, provenance checks, Focus Mode |
| `data/graph/**` | Import fixtures for Neo4j | Graph build | Neo4j loaders / migrations |
| `data/<domain>/**` | Domain pack docs: README + governance + mappings | Data/curation | Reviewers, maintainers, curators |
| `data/reports/<domain>/**` | Optional derived evidence products | ETL/analysis | Story Nodes, Focus Mode contexts |

---

## 📦 Data & Metadata

### Data lifecycle

**Required staging (canonical):**

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`

**Evidence artifacts (machine-readable):**

- STAC: `data/stac/**`
- DCAT: `data/catalog/dcat/**` *(planned; not confirmed in repo)*
- PROV: `data/prov/**` *(planned; not confirmed in repo)*
- Graph fixtures (when used): `data/graph/**`
- Optional evidence products: `data/reports/<domain>/**`

### Domain expansion pattern

A **domain pack** is the minimum set required for a domain to participate in the pipeline.

When adding a new domain:

1. Create **staging folders**:
   - `data/raw/<domain>/`
   - `data/work/<domain>/`
   - `data/processed/<domain>/`

2. Create the **domain pack** (documentation + governance):
   - `data/<domain>/README.md` *(required)*
   - `data/<domain>/sources/` *(recommended: licenses/attribution/source notes)*
   - `data/<domain>/governance/` *(recommended for CARE/sensitivity/redaction notes)*
   - `data/<domain>/mappings/` *(optional: crosswalk docs)*

3. Ensure processed outputs can generate (as applicable):
   - STAC Collection + Item(s)
   - DCAT dataset record(s)
   - PROV activity/bundle(s)
   - Graph import fixtures (if graph-ingested)

4. Link domain pack docs to the evidence outputs:
   - STAC IDs and file paths
   - DCAT dataset IDs (if present)
   - PROV activity IDs (if present)
   - Graph fixture version/run identifiers (if present)

### Data immutability, reproducibility, and versioning

- **Raw (`data/raw/**`)**
  - Append-only snapshots.
  - Never hand-edit in place; ingest new snapshots/versioned pulls instead.

- **Work (`data/work/**`)**
  - Intermediate artifacts that can be deleted and rebuilt.
  - Safe place for normalization, joins, and QA scratch outputs (when reproducible).

- **Processed (`data/processed/**`)**
  - Canonical outputs used downstream.
  - Must be schema-validated (where schemas exist) and versioned (do not overwrite history without explicit governance).

### Large artifacts

- Prefer **pointer/manifest approaches** for very large datasets and binaries (to keep git diffable).
- Exact large-file tooling and pointer formats are **not confirmed in repo**; follow maintainer guidance and CI rules if present.

---

## 🌐 STAC, DCAT & PROV alignment

### Policy for every dataset / evidence product

For each dataset or evidence artifact used downstream:

- **STAC**: Collection + Item(s)
- **DCAT**: dataset/distribution record(s) *(where adopted)*
- **PROV**: activity/bundle describing lineage (inputs → transform → outputs)
- **Version lineage links** reflected in catalogs and (where applicable) the graph

### Docs-side templates vs data-side outputs

Some domains may store **templates** and governance docs under:

- `docs/data/<domain>/**`

This is documentation. Canonical **output evidence** remains in:

- `data/stac/**` (and `data/catalog/dcat/**`, `data/prov/**` if present)

Avoid duplicating “source-of-truth” evidence in both places.

### Identifier and linkage expectations

Graph nodes and APIs should reference (directly or indirectly):

- STAC Item IDs
- DCAT dataset IDs
- PROV activity/bundle IDs

This allows UI and Focus Mode to resolve “what is this data?” into traceable evidence and lineage.

---

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize | Config + deterministic runs producing `data/**` |
| Catalogs | STAC/DCAT/PROV evidence + lineage | JSON/JSON-LD + validators |
| Graph | Neo4j ingest model | Import fixtures + API boundary |
| APIs | Serve contracts; enforce redaction/generalization | REST/GraphQL |
| UI | Map + narrative exploration | API calls only |
| Story Nodes | Curated narrative | Provenance-linked content |
| Focus Mode | Contextual synthesis | Provenance-linked only |

### API boundary rule

- The UI must **not** query Neo4j directly.
- All graph access occurs through the API boundary, which is where monitoring, caching, redaction, and provenance enforcement can be applied.

---

## 🧩 Graph ingest fixtures

### What `data/graph/**` is for

`data/graph/**` contains **import-ready artifacts** generated from `data/processed/**` and catalog evidence:

- `csv/`: nodes and relationships exported for Neo4j import
- `cypher/`: optional post-import scripts, constraints, and migrations (if used)

### Non-negotiable constraints

- Fixtures must use **stable IDs** that match catalog/provenance identifiers wherever applicable.
- Fixtures must not introduce **orphan facts** (entities without evidence IDs).
- Fixtures must not bypass governance: if a fact requires redaction/generalization, it must be reflected in the API boundary and any published story content.

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as evidence-first narrative

- Story Nodes should cite **graph entity IDs** and **STAC/DCAT/PROV evidence IDs**.
- Story Nodes may include local assets (images/excerpts) with attribution, but **source-of-truth evidence** remains catalog + provenance artifacts.

### Focus Mode rule

Focus Mode must only consume **provenance-linked** content. Any predictive or AI-generated content must be:

- clearly marked,
- opt-in,
- and include uncertainty metadata.

---

## 🧪 Validation & CI/CD

### CI behavior contract

- **Validate if present:** if a canonical root exists (or changes), validate its artifacts.
- **Fail if invalid:** schema errors, missing links, or orphan references fail deterministically.
- **Skip if not applicable:** optional roots absent → skip without failing the overall pipeline.

### Minimum checks

- [ ] STAC artifact validation (if validators exist)
- [ ] DCAT/PROV validation (if validators exist)
- [ ] No orphan references (IDs cited by graph/API/UI/story resolve to evidence)
- [ ] Deterministic outputs (reruns produce diffable/stable artifacts)
- [ ] Classification propagation (no output is less restricted than any input in its lineage)
- [ ] Secrets/PII scanning (no credentials; no disallowed sensitive content)

### Recommended integrity checks

- STAC `links[]` integrity and external `assets.*.href` broken-link checks
- Geometry validity + temporal range checks (domain-specific QA)
- Graph fixture referential integrity checks (node/edge cardinality, required keys)

*(Exact commands/tooling not confirmed in repo.)*

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New external data sources
- New sensitive layers (protected locations / culturally sensitive knowledge)
- New AI narrative behaviors that could surface unsourced claims
- New public-facing endpoints exposing data

### Sovereignty safety

Any restricted locations or culturally sensitive knowledge must be protected by:

- geometry generalization where required,
- API-level redaction,
- Story Node review gates before publishing.

---

## 🧭 Context

### Background

KFM’s ability to present maps, timelines, and narratives depends on **traceable evidence**. The `data/` directory establishes where governed datasets and evidence artifacts live so that catalogs, graph ingest, APIs, and UI can remain provenance-linked and auditable.

### Assumptions

- STAC/DCAT/PROV artifacts are treated as evidence products and validated when validators exist.
- Domain staging (`raw/`, `work/`, `processed/`) supports deterministic reruns.
- Some canonical roots (e.g., `schemas/`, `data/catalog/dcat/`, `data/prov/`) may be planned but not yet present *(not confirmed in repo)*.

### Constraints / invariants

- ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode is preserved.
- Frontend consumes contracts via APIs (no direct graph dependency).
- AI transformations are limited to allowed operations in front-matter; prohibited transforms must not be introduced.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical on-disk home for DCAT and PROV in the current repo state: `data/catalog/dcat/` + `data/prov/` vs legacy variants (e.g., `data/catalogs/`, `data/provenance/`, or docs-side storage)? | Maintainers | TBD |
| Do we standardize domains as `air-quality` vs `air_quality` and resolve naming inconsistencies? | Data governance | TBD |
| Do we require domain governance docs under `data/<domain>/governance/` or under `docs/data/<domain>/` (choose one canonical location and link)? | Governance | TBD |
| What is the canonical validator toolchain for STAC/DCAT/PROV in CI? | Data/Platform | TBD |

### Future extensions

- Add per-domain “freshness gates” and classification docs under one canonical location.
- Add releases packaging under `releases/` (manifests/SBOMs/signed bundles) once v13 is adopted *(not confirmed in repo)*.
- Add automated lineage checks linking `mcp/runs/**` to `data/prov/**` when provenance outputs are formalized.

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

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-22 | Initial `data/` README (v12/v13-aligned draft) | TBD |
| v1.0.1 | 2025-12-24 | Align to Universal doc template sections; clarify v13 target tree + “not confirmed” markers; add Context/Diagrams/open questions | TBD |
| v1.0.2 | 2025-12-26 | Standardize canonical staging as `data/raw|work|processed` (domain-scoped inside stages); clarify domain packs vs bulk data; add explicit Architecture + CI behavior contract; label planned DCAT/PROV roots | TBD |

---

Footer refs (do not remove)

- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint (if adopted): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
