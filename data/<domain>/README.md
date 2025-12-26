---
title: "KFM Data Domain — <domain>"
path: "data/<domain>/README.md"
version: "v0.1.0"
last_updated: "2025-12-26"
status: "draft"
doc_kind: "DataDomain"
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

doc_uuid: "urn:kfm:doc:data:<domain>:readme:v0.1.0"
semantic_document_id: "kfm-data-<domain>-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data:<domain>:readme:v0.1.0"
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

# KFM Data Domain — `<domain>`

> **Purpose (required):** Define the **governed contract** for the `<domain>` data domain across the canonical pipeline:
> **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.

## 📘 Overview

### Purpose

- Provide a single, versioned, repo-local “front door” for the `<domain>` data domain.
- Define where **domain data**, **catalog artifacts**, and **provenance** live and how they are validated.
- Document constraints that protect governance, sovereignty, and Focus Mode’s **provenance-only** rule.

### Scope

| In Scope | Out of Scope |
|---|---|
| Domain overview, staging locations, metadata alignment, validation gates, and governance notes for `<domain>` | Implementing pipelines, adding API endpoints, or changing ontology labels (those live in their respective subsystem areas) |
| Links/pointers to canonical outputs and contracts | Writing Story Nodes themselves (see `docs/reports/story_nodes/`) |
| Redaction/sensitivity propagation rules for this domain | Defining new governance policy (must follow governed standards; do not invent) |

### Audience

- **Primary:** Data engineers and domain contributors implementing/maintaining `<domain>` ETL and catalogs.
- **Secondary:** Reviewers validating governance, provenance, and downstream integration.

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo; if absent, add or update this link to the canonical glossary)*.
- Terms used here: **domain**, **staging**, **catalog**, **STAC**, **DCAT**, **PROV**, **lineage**, **redaction**, **Focus Mode**.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + invariants) | `docs/MASTER_GUIDE_v12.md` | KFM Core | Canonical ordering and “do not break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | KFM Core | Front-matter + standard sections |
| STAC / DCAT / PROV schemas | `schemas/stac/`, `schemas/dcat/`, `schemas/prov/` | Data/Platform | Validate catalogs against these (paths not confirmed in repo) |
| Domain docs root | `data/<domain>/` | Domain Steward (TBD) | This README + domain governance notes |
| Raw staging (domain) | `data/raw/<domain>/` | Data Eng | Immutable source snapshots |
| Work staging (domain) | `data/work/<domain>/` | Data Eng | Intermediate artifacts (rebuildable) |
| Processed outputs (domain) | `data/processed/<domain>/` | Data Eng | Canonical outputs used for catalogs + graph ingest |
| STAC outputs (domain) | `data/stac/<domain>/` | Catalog stage | STAC Collections/Items for `<domain>` |
| DCAT outputs (domain) | `data/catalog/dcat/<domain>/` | Catalog stage | Discovery/export records |
| PROV outputs (domain) | `data/prov/<domain>/` | Pipeline+Catalog | Provenance bundles (activities/entities/agents) |
| Pipelines | `src/pipelines/` | Data Eng | Domain ETL + catalog build (domain subpath not confirmed) |
| Graph integration | `src/graph/` + `docs/graph/` | Graph Eng | Ontology bindings + ingest mapping (paths not confirmed) |
| API boundary | `src/server/` | API Eng | UI consumes contracts via API only |
| UI | `web/` | Frontend | Layer registry + Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` | Narrative | Evidence-led narrative artifacts |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] Directory layout reflects the canonical staging + catalog locations used by this domain
- [ ] Inputs/outputs + sensitivity notes are documented (even if “TBD” placeholders)
- [ ] STAC/DCAT/PROV alignment policy is explicit for `<domain>`
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations are explicitly stated
- [ ] Footer refs included (do not remove)

## 🗂️ Directory Layout

### This document

- `path`: `data/<domain>/README.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Domain docs (this domain) | `data/<domain>/` | Domain notes, governance notes, source specs |
| Raw staging (canonical) | `data/raw/<domain>/` | Immutable source snapshots |
| Work staging (canonical) | `data/work/<domain>/` | Intermediate transforms; rebuildable |
| Processed outputs (canonical) | `data/processed/<domain>/` | Versioned outputs used by catalogs + graph ingest |
| STAC outputs | `data/stac/<domain>/` | STAC Collections/Items (domain) |
| DCAT outputs | `data/catalog/dcat/<domain>/` | DCAT datasets/distributions (domain) |
| PROV outputs | `data/prov/<domain>/` | Provenance bundles (domain) |
| Graph import | `data/graph/csv/` + `data/graph/cypher/` | Import artifacts (not confirmed in repo) |
| Pipelines | `src/pipelines/` | ETL + catalog build code |
| Graph | `src/graph/` | Ontology + ingest mapping |
| APIs | `src/server/` | Contracted access + redaction enforcement |
| UI | `web/` | Map layers + Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts w/ provenance |

### Expected file tree (domain + canonical staging)

~~~text
📁 data/
├── 📁 <domain>/
│   ├── 📄 README.md                          # (this file)
│   ├── 📁 governance/                        # optional; not confirmed in repo
│   │   ├── 📄 README.md                      # governance index (optional; not confirmed in repo)
│   │   ├── 📄 DATA_CLASSIFICATION.md         # classification rationale (optional; not confirmed in repo)
│   │   ├── 📄 SOURCES_AND_LICENSES.md        # attribution + license mapping (optional; not confirmed in repo)
│   │   └── 📄 QA_CHECKLIST.md                # domain QA gates (optional; not confirmed in repo)
│   ├── 📁 sources/                           # optional; upstream source specs (optional; not confirmed in repo)
│   └── 📄 DOMAIN_NOTES.md                    # optional; domain decisions + assumptions (optional; not confirmed in repo)
├── 📁 raw/
│   └── 📁 <domain>/                          # raw ingests (append-only; never “hand edited”)
├── 📁 work/
│   └── 📁 <domain>/                          # intermediate artifacts (reproducible; safe to delete/rebuild)
├── 📁 processed/
│   └── 📁 <domain>/                          # canonical outputs (schema-validated; versioned)
├── 📁 stac/
│   └── 📁 <domain>/                          # STAC Collections/Items for this domain
├── 📁 catalog/
│   └── 📁 dcat/
│       └── 📁 <domain>/                      # DCAT dataset records and distributions
├── 📁 prov/
│   └── 📁 <domain>/                          # PROV bundles (activities, entities, agents)
└── 📁 reports/
    └── 📁 <domain>/                          # optional evidence artifacts / analysis outputs
~~~

## 🧭 Context

### Background

`<domain>` is a KFM data domain that participates in the system’s governed pipeline. Data and derived evidence must remain **auditable**, **diffable**, and **provenance-linked** to support downstream graph integration, API delivery, and narrative UI (Story Nodes + Focus Mode).

### Assumptions

- Canonical staging roots exist (or will be created) for `data/raw/`, `data/work/`, `data/processed/`, `data/stac/`, `data/catalog/dcat/`, and `data/prov/`.
- Schema validation exists (or will be added) for STAC/DCAT/PROV outputs under `schemas/` *(paths not confirmed in repo)*.
- Domain ownership/stewardship roles are defined in governance docs.

### Constraints / invariants

- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- **API boundary is mandatory:** the UI never queries Neo4j directly; it consumes contracted API responses only.
- Outputs must be deterministic and reproducible:
  - pinned inputs/configs
  - versioned processed outputs
  - PROV bundles that explain lineage

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What is the canonical upstream source list and license mapping for `<domain>`? | TBD | TBD |
| What are the minimal public vs internal outputs (classification) for `<domain>`? | TBD | TBD |
| What schema constraints are required beyond baseline STAC/DCAT/PROV? | TBD | TBD |

### Future extensions

- Add domain-local governance docs under `data/<domain>/governance/` (if not present).
- Add domain-specific schema extensions under `schemas/<domain>/` *(not confirmed in repo; use only if governance-approved)*.
- Add domain evidence artifacts under `data/reports/<domain>/` with STAC assets + PROV links.

## 🗺️ Diagrams

### System / dataflow diagram

~~~mermaid
flowchart LR
  A["ETL runs for DOMAIN<br/>(src/pipelines/...)"] --> B["data/raw/DOMAIN/"]
  B --> C["data/work/DOMAIN/"]
  C --> D["data/processed/DOMAIN/"]
  D --> E["Catalog outputs<br/>STAC/DCAT/PROV"]
  E --> F["Neo4j Graph<br/>(src/graph ingest)"]
  F --> G["API Layer<br/>(src/server)"]
  G --> H["UI<br/>(web/)"]
  H --> I["Story Nodes<br/>(docs/reports/story_nodes/)"]
  I --> J["Focus Mode<br/>(provenance-linked only)"]
~~~

## 📦 Data & Metadata

### Data lifecycle

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/` → `data/stac/<domain>/`
- DCAT + PROV outputs are emitted alongside catalogs:
  - `data/catalog/dcat/<domain>/`
  - `data/prov/<domain>/`
- Use `data/reports/<domain>/` for evidence/analysis outputs **only when they are provenance-linked**.

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| TBD | TBD | TBD | TBD |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed dataset(s) | TBD | `data/processed/<domain>/...` | Domain schema (TBD) |
| STAC collections/items | JSON | `data/stac/<domain>/...` | STAC + KFM profile |
| DCAT dataset records | JSON/TTL (TBD) | `data/catalog/dcat/<domain>/...` | DCAT + KFM profile |
| PROV bundles | JSON-LD/TTL (TBD) | `data/prov/<domain>/...` | PROV-O + KFM profile |

### Sensitivity & redaction

- Identify any fields requiring generalization or omission for public outputs:
  - direct identifiers (PII) — if applicable
  - precise coordinates for restricted/culturally sensitive locations — if applicable
- Rule: **No output may be “less restricted” than any input in its lineage.** (If this domain handles sensitive inputs, document propagation rules here.)

### Quality signals

- Completeness checks (required fields present)
- Geometry validity checks (if spatial)
- Range/unit checks (if numeric)
- Cross-link checks:
  - catalog IDs resolve
  - evidence IDs resolve
  - provenance references resolve

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy (required)

Every dataset or evidence product produced for `<domain>` must have:

- **STAC** Collection + Item(s)
- **DCAT** dataset record (minimum: title/description/license/keywords)
- **PROV-O** activity describing lineage (inputs → transforms → outputs)

### STAC

- Collections involved: `<domain>__<collection_id>` *(placeholder naming; use repo conventions)*
- Items involved: `<domain>__<item_id>` *(placeholder naming; use repo conventions)*
- Extensions: TBD (only if justified and schema-validated)

### DCAT

- Dataset identifiers: TBD
- License mapping: ensure it matches upstream licensing and repo governance expectations
- Publisher/contact mapping: TBD

### PROV-O

- `prov:wasDerivedFrom`: raw → work → processed lineage
- `prov:wasGeneratedBy`: transform activity IDs for each build
- Activity / Agent identities: record tool/run IDs (and humans where appropriate)

### Versioning

- New versions should link predecessor/successor relationships.
- Graph should mirror version lineage (IDs stable, versions explicit).

## 🧱 Architecture

### Subsystem contracts

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation | deterministic, replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated |
| Graph | ontology + migrations + constraints | stable labels/edges |
| APIs | OpenAPI/GraphQL schema + tests | backward compat or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Focus Mode | provenance-linked context bundle | no hallucinated sources |

### Interfaces / contracts

| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | SemVer + changelog |
| API contracts | `src/server/contracts/**` *(or legacy; not confirmed in repo)* | SemVer + contract tests |
| Story Node schema | `schemas/storynodes/` *(not confirmed in repo)* | SemVer + validator |

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes must carry provenance annotations and connect to graph entities.
- Claims surfaced in Story Nodes should resolve to evidence IDs in STAC/DCAT/PROV.

### Focus Mode rule

- Focus Mode only consumes **provenance-linked** content.
- Any predictive or AI-generated content must be:
  - opt-in,
  - labeled as such,
  - shipped with uncertainty/confidence metadata,
  - never presented as unmarked fact.

## 🧪 Validation & CI/CD

### Validation steps (minimum)

- [ ] Markdown protocol checks (front-matter, required sections)
- [ ] Schema validation (STAC/DCAT/PROV outputs)
- [ ] Provenance checks (no orphan PROV refs; lineage links resolve)
- [ ] Secret scan (no tokens/keys)
- [ ] PII scan (if domain contains person-level records)
- [ ] Sensitive location scan (if domain contains restricted locations)
- [ ] Reference/link checks (no broken internal pointers)
- [ ] (If applicable) Graph integrity checks for ingest artifacts
- [ ] (If applicable) API contract tests for endpoints serving this domain
- [ ] (If applicable) UI layer registry schema + a11y checks

### Reproduction (deterministic)

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Run ETL for <domain> (pinned config)
# python -m src.pipelines.<domain>.run --config configs/<domain>.yaml

# 2) Validate catalogs
# python tools/validate_stac.py data/stac/<domain>/
# python tools/validate_dcat.py data/catalog/dcat/<domain>/
# python tools/validate_prov.py data/prov/<domain>/

# 3) Governance scans (only if applicable)
# python tools/scan_pii.py data/work/<domain>/
# python tools/scan_sensitive_locations.py data/processed/<domain>/

# 4) Emit integrity hashes/manifests
# python tools/hash_manifest.py data/processed/<domain>/ > mcp/runs/<run_id>/manifest.sha256
~~~

### Telemetry signals (recommended)

| Signal | Source | Where recorded |
|---|---|---|
| classification_assigned | pipeline/catalog | `docs/telemetry/` + `schemas/telemetry/` *(paths not confirmed)* |
| redaction_applied | pipeline | `data/prov/<domain>/...` |
| promotion_blocked | CI gate | CI logs / report artifact |
| catalog_published | catalog stage | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |

## ⚖ FAIR+CARE & Governance

### Review gates

- Governance review is required when:
  - introducing a new `<domain>` dataset source,
  - changing an artifact’s classification/sensitivity,
  - publishing any dataset derived from sensitive/restricted inputs,
  - adding a new UI layer that could reveal sensitive locations by interaction/zoom.

### CARE / sovereignty considerations

- Identify communities impacted (if any) and protection rules.
- If `<domain>` intersects with sovereignty-controlled areas or culturally sensitive knowledge:
  - prefer coarse/aggregate public products,
  - document redaction/generalization rules,
  - align access rules to `docs/governance/SOVEREIGNTY.md`.

### AI usage constraints

- Allowed:
  - summarization, structure extraction, translation, keyword indexing.
- Prohibited:
  - generating new policy,
  - inferring sensitive locations (directly or indirectly).
- AI may propose classifications, but **human review** must approve any final labels, especially downgrades.

## 🕰️ Version History

| Version | Date | Change summary | Author | PR / Issue |
|---:|---:|---|---|---|
| v0.1.0 | 2025-12-26 | Initial `<domain>` data domain README scaffold | TBD | TBD |

---

## Footer refs (do not remove)

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
---

