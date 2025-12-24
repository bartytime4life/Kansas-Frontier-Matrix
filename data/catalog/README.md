---
title: "KFM Catalog Outputs — data/catalog README"
path: "data/catalog/README.md"
version: "v1.0.0"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:catalog:readme:v1.0.0"
semantic_document_id: "kfm-data-catalog-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:catalog:readme:v1.0.0"
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

# `data/catalog/` — KFM catalog outputs

> **Purpose (required):** Define what belongs in `data/catalog/`, how it is structured, and how catalog artifacts link to `data/stac/` and `data/prov/` for graph/API/UI/Story consumption.

## 📘 Overview

### What this folder is
`data/catalog/` is the canonical home for **dataset-level catalog artifacts** produced by the KFM **Catalog** stage. These artifacts make datasets discoverable and interoperable, and provide stable identifiers for downstream stages.

### What belongs here
- **DCAT outputs** (dataset discovery + distributions): `data/catalog/dcat/`
- (Future) additional catalog serializations (only when governed and validated)

### What does not belong here
- STAC artifacts (belong in `data/stac/`)
- Provenance bundles (belong in `data/prov/`)
- Domain data products (belong in `data/<domain>/{raw,work,processed}/`)
- Source code (belongs in `src/`)
- UI assets and configs (belongs in `web/`)
- Narrative Story Nodes (belongs in `docs/reports/story_nodes/`)

### Scope
| In Scope | Out of Scope |
|---|---|
| Directory contract + layout conventions for catalog artifacts | Full DCAT field specification (belongs under `docs/standards/`) |
| Directory-level linkage expectations to STAC + PROV | Implementing pipeline code (belongs under `src/pipelines/`) |
| Validation and governance expectations for published catalog artifacts | External publishing workflows outside the repo |

### Audience
- Primary: catalog maintainers, data engineering maintainers, API maintainers
- Secondary: governance reviewers, graph/ontology maintainers, Story Node authors

### Definition of done
- [ ] Front-matter complete and `path` matches file location
- [ ] Directory tree matches this README
- [ ] Clear boundaries: what belongs here vs elsewhere
- [ ] Linkage expectations to STAC + PROV are documented
- [ ] Validation & CI/CD steps are listed
- [ ] Governance + CARE/sovereignty considerations are explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/catalog/README.md` (must match front-matter)

### Expected tree

~~~text
📁 data/
└── 📁 catalog/
    ├── 📄 README.md
    └── 📁 dcat/
        ├── 📄 README.md
        ├── 📄 dataset--<dataset_id>.jsonld
        ├── 📄 dataset--<dataset_id>.ttl
        └── 📄 catalog.<ext>
~~~

Notes:
- `dcat/` is the canonical DCAT output directory.
- `catalog.<ext>` is optional (only if the repo adopts an aggregate `dcat:Catalog` artifact).
- Exact naming + serialization rules must align with the governed DCAT profile.

## 🧭 Context

### Why this exists
KFM treats **catalog artifacts** as machine-readable “evidence metadata” that downstream stages can rely on:
- Graph ingest can reference stable dataset IDs,
- APIs can expose dataset discovery consistently,
- UI/Story Nodes can cite dataset identifiers,
- Focus Mode can enforce provenance-linked narrative behavior.

### Architecture constraints and invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**
- UI must not access Neo4j directly; all access is through contracted APIs.
- Catalog artifacts should be produced deterministically (no hand-edited drift).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we maintain an aggregate `dcat:Catalog` file in addition to per-dataset records? | TBD | TBD |
| What is the canonical DCAT serialization in-repo (JSON-LD only vs JSON-LD + Turtle)? | TBD | TBD |
| What is the stable `dataset_id` naming convention across domains? | TBD | TBD |

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL & transforms] --> B[data/<domain>/processed]
  B --> C[Catalog build]
  C --> S[STAC<br/>data/stac]
  C --> D[DCAT<br/>data/catalog/dcat]
  C --> P[PROV<br/>data/prov]
  S --> G[Graph]
  D --> G
  P --> G
  G --> API[API boundary]
  API --> UI[UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Where from | Notes |
|---|---|---|
| Processed domain outputs | `data/<domain>/processed/` | Primary material for dataset metadata |
| STAC Collections/Items | `data/stac/**` | Referenced by DCAT distributions for geospatial assets |
| PROV bundles | `data/prov/**` | Referenced for lineage/auditability |

### Outputs
| Output | Location | Notes |
|---|---|---|
| DCAT dataset records | `data/catalog/dcat/` | Canonical dataset discovery artifacts |

### Sensitivity & redaction
- Catalog artifacts must not bypass sovereignty or governance policy.
- If a dataset is restricted, its catalog record must reflect access constraints and avoid linking to restricted distributions in a way that bypasses controls.

## 🌐 STAC, DCAT & PROV Alignment

### Minimum alignment rule
For each dataset/evidence product intended for downstream consumption:
- **STAC** (when spatial/temporal asset catalog is needed): `data/stac/`
- **DCAT** (dataset discovery + distributions): `data/catalog/dcat/`
- **PROV** (lineage + audit): `data/prov/`

### Linkage expectations
- DCAT records should link to:
  - STAC Collection and/or Item identifiers (when applicable), and/or
  - distributions pointing to controlled repo paths or controlled endpoints
- PROV bundles should include activity/entity/agent identifiers that can be referenced from catalog artifacts and mirrored into the graph.

## 🧱 Architecture

### Component responsibilities
| Component | Responsibility | Canonical location |
|---|---|---|
| ETL / pipelines | Deterministic transforms | `src/pipelines/` |
| Catalog artifacts | STAC/DCAT/PROV outputs | `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Graph | Ontology-governed ingest | `src/graph/` (+ `data/graph/` for import artifacts) |
| API boundary | Contracted access + redaction | `src/server/` |
| UI | Map + narrative | `web/` |
| Story Nodes | Evidence-led narratives | `docs/reports/story_nodes/` |

## 🧠 Story Node & Focus Mode Integration

- Story Nodes should cite **dataset identifiers** (DCAT) and **evidence identifiers** (STAC/DCAT/PROV).
- Focus Mode must only present provenance-linked content; any AI-derived narrative must be opt-in and uncertainty-tagged.

## 🧪 Validation & CI/CD

### Minimum checks
- [ ] Markdown protocol checks (KFM-MDP)
- [ ] DCAT artifacts validate against `schemas/dcat/**` (if present)
- [ ] Link integrity checks (distributions resolve; no broken internal refs)
- [ ] No secrets/PII in catalog artifacts
- [ ] Governance checks for restricted/sensitive datasets

### Reproduction

~~~bash
# Placeholder — replace with repo-specific commands
# 1) Run catalog build
# 2) Validate DCAT outputs
# 3) Verify link integrity
~~~

## ⚖ FAIR+CARE & Governance

### Review gates (directory-level)
- New external datasets and new public distributions require governance review.
- Any change that could expose sensitive locations or culturally sensitive knowledge must be reviewed under sovereignty policy.
- Any schema/profile changes require schema maintainer review.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial `data/catalog/` README | TBD |

---

Footer refs:
- Data root: `data/README.md`
- DCAT outputs: `data/catalog/dcat/README.md`
- STAC outputs: `data/stac/README.md`
- Provenance: `data/prov/README.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`


---
title: "KFM DCAT Catalog Output Directory"
path: "data/catalog/dcat/README.md"
version: "v1.0.1"
last_updated: "2025-12-24"
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

doc_uuid: "urn:kfm:doc:data:catalog:dcat:readme:v1.0.1"
semantic_document_id: "kfm-data-catalog-dcat-readme-v1.0.1"
event_source_id: "ledger:kfm:doc:data:catalog:dcat:readme:v1.0.1"
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

# KFM DCAT Catalog Output Directory

> **Purpose (required):** Define what belongs in `data/catalog/dcat/`, how DCAT records are organized, and how they link to STAC and PROV evidence artifacts for downstream Graph/API/UI/Story consumption.

## 📘 Overview

### Purpose
- `data/catalog/dcat/` is the canonical home for **DCAT dataset records** produced by the KFM **Catalog** stage.
- This README documents **directory-level rules** so DCAT outputs remain predictable, discoverable, auditable, and non-duplicated.

### Scope

| In Scope | Out of Scope |
|---|---|
| Directory layout conventions for DCAT records | Full DCAT field-by-field specification |
| Minimum directory-level metadata expectations | ETL + catalog build implementation details |
| How DCAT records connect to STAC + PROV | API endpoint and UI behavior design details |
| Validation expectations and review gates | External publishing workflows outside the repo |

### Audience
- Primary: catalog maintainers, data engineering maintainers, API maintainers
- Secondary: governance reviewers, graph/ontology maintainers, external contributors adding new datasets/domains

### Definitions
- Glossary: `docs/glossary.md` (not confirmed in repo)
- Terms used: DCAT, Dataset, Distribution, JSON-LD, RDF/Turtle, STAC, PROV, stable identifier, version lineage

### Key artifacts
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Parent catalog README | `data/catalog/README.md` | Catalog maintainers | Directory contract for catalog outputs |
| DCAT records (this directory) | `data/catalog/dcat/` | Catalog stage | Dataset discovery + distributions |
| STAC outputs | `data/stac/` | Catalog stage | Geospatial asset catalogs referenced by DCAT |
| PROV bundles | `data/prov/` | ETL + catalog stage | Lineage bundles referenced by DCAT/Graph |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` (not confirmed in repo) | Catalog maintainers | Governs required fields and mappings |
| DCAT schemas | `schemas/dcat/` (not confirmed in repo) | Schemas/CI | Validation targets used by CI |
| Master pipeline invariant | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Pipeline ordering + subsystem boundaries |

### Definition of done
- [ ] Front-matter complete + valid
- [ ] Directory purpose + boundaries are explicit
- [ ] DCAT ↔ STAC/PROV linkage expectations documented
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/catalog/dcat/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Catalog root | `data/catalog/` | Catalog artifacts (DCAT and future) |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset records (JSON-LD/RDF serializations) |
| STAC outputs | `data/stac/` | STAC collections + items (geospatial asset catalogs) |
| PROV outputs | `data/prov/` | PROV lineage bundles for runs/transforms |
| Data domains | `data/<domain>/` | `raw/`, `work/`, `processed/` per domain |
| Pipelines | `src/pipelines/` | ETL + catalog build code (idempotent, deterministic) |
| Graph | `src/graph/` + `data/graph/` | Ontology bindings + import artifacts |
| API boundary | `src/server/` | Contracts + endpoints (UI never reads the graph directly) |
| Frontend | `web/` | React/Map UI + layer registries |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 catalog/
    ├── 📄 README.md
    └── 📁 dcat/
        ├── 📄 README.md
        ├── 📄 dataset--<dataset_id>.jsonld
        ├── 📄 dataset--<dataset_id>.ttl
        └── 📄 catalog.<ext>
~~~

Notes:
- `dataset--<dataset_id>.<ext>` represents **one DCAT dataset record per logical dataset**.
- `catalog.<ext>` is optional, if the repo adopts an aggregate `dcat:Catalog` serialization.
- Naming + serialization rules must match the governed DCAT profile.

## 🧭 Context

### Background
KFM uses open standards to make datasets **discoverable, interoperable, and traceable**. DCAT provides dataset-level metadata suitable for indexing and federation; STAC provides asset-level spatiotemporal metadata; PROV provides lineage and auditability.

### Assumptions
- DCAT artifacts are usually generated (or at minimum validated) by the Catalog stage.
- Dataset identifiers are stable and referenceable from Graph nodes and API payloads.
- Outputs validate against schemas under `schemas/` where available.

### Constraints and invariants
- Canonical flow is preserved: **ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**.
- UI does not query Neo4j directly; all consumption is via API contracts.
- Sensitive or restricted locations and culturally sensitive knowledge must be protected via generalization, redaction, and review gates.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we publish an aggregate `dcat:Catalog` file in addition to per-dataset records? | Catalog maintainers | TBD |
| What is the canonical DCAT serialization in-repo (JSON-LD only vs JSON-LD + Turtle)? | Catalog maintainers | TBD |
| What is the authoritative file naming convention for dataset records (prefix, separator, version segment, etc.)? | Catalog maintainers | TBD |

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[data/<domain>/processed]
  B --> C[Catalog build<br/>src/pipelines]
  C --> S[STAC<br/>data/stac]
  C --> D[DCAT<br/>data/catalog/dcat]
  C --> P[PROV<br/>data/prov]
  S --> G[Graph<br/>src/graph]
  D --> G
  P --> G
  G --> API[API boundary<br/>src/server]
  API --> UI[UI<br/>web]
  UI --> SN[Story Nodes<br/>docs/reports/story_nodes]
  SN --> FM[Focus Mode<br/>provenance-linked only]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Processed domain outputs | domain-dependent | `data/<domain>/processed/` | Domain validation + deterministic pipeline rules |
| STAC collections/items | JSON | `data/stac/**` | STAC profile validation |
| Provenance bundles | JSON-LD / RDF | `data/prov/**` | PROV profile validation |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| DCAT dataset record | JSON-LD or Turtle | `data/catalog/dcat/dataset--<dataset_id>.<ext>` | KFM-DCAT profile + `schemas/dcat/**` (if present) |
| Optional aggregate catalog | JSON-LD or Turtle | `data/catalog/dcat/catalog.<ext>` | KFM-DCAT profile + `schemas/dcat/**` (if present) |

### Sensitivity and redaction
- DCAT records must not expose restricted locations, sensitive coordinates, or culturally protected knowledge.
- If a dataset is restricted, the DCAT record must reflect access constraints and must not provide distribution links that bypass policy.

### Quality signals
- Schema validation passes for all DCAT records (where schemas exist).
- No broken references (distributions resolve to controlled paths/endpoints).
- Provenance completeness: dataset has a PROV activity and traceable inputs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the dataset is geospatial, DCAT distributions should reference:
  - the related STAC Collection and/or Item identifiers, and/or
  - the assets those Items describe (repo path or controlled endpoint).
- Any required STAC extensions must be documented and validated via the STAC profile.

### DCAT
- Dataset identifiers must be stable and referenceable from Graph nodes and API contracts.
- License, publisher/maintainer, and keyword metadata must be consistent with authoritative domain metadata.

### PROV-O
- `prov:wasDerivedFrom`: link dataset outputs to upstream inputs.
- `prov:wasGeneratedBy`: link dataset outputs to a run/activity identifier.
- Activity and agent identities: catalog generation is attributable to a pipeline/run identity.

### Versioning
If datasets are versioned:
- Do not overwrite in-place without lineage.
- Prefer “new version + explicit predecessor/successor links”, mirrored into STAC, PROV, and the graph (when applicable).

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | configs + run logs |
| Catalogs | Produce STAC/DCAT/PROV artifacts | JSON/RDF + validators |
| Graph | Neo4j knowledge graph | Cypher + API layer |
| APIs | Serve contracts + enforce redaction | REST/GraphQL |
| UI | Map + narrative experience | API calls |
| Story Nodes | Curated narrative content | provenance-linked evidence |
| Focus Mode | Contextual synthesis | provenance-linked only |

### Interfaces and contracts
| Contract | Location | Versioning rule |
|---|---|---|
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` (not confirmed in repo) | Semver + changelog |
| DCAT schemas | `schemas/dcat/` (not confirmed in repo) | Semver + changelog |
| API contracts | `src/server/` | Contract tests required |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces downstream
- DCAT dataset identifiers should be referenceable as evidence IDs in API context bundles.
- Story Nodes should cite dataset IDs (DCAT) and/or specific STAC/PROV evidence IDs when referencing dataset-derived claims.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.
- Predictive or AI-generated content is opt-in and must carry uncertainty metadata.

### Optional structured controls

~~~yaml
focus_layers:
  - "TBD"

focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation for DCAT artifacts (`schemas/dcat/**`, if present)
- [ ] Link integrity checks (no broken distribution targets)
- [ ] Graph integrity checks for referenced IDs (where applicable)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands

# 1) Validate DCAT records against schemas
# <command>

# 2) Run repository lint / markdown protocol validation
# <command>

# 3) Run integrity checks (links + referenced IDs)
# <command>
~~~

### Telemetry signals
- Not defined here. If CI emits dataset validation signals, document them under `docs/telemetry/` and `schemas/telemetry/`.

## ⚖ FAIR+CARE & Governance

### Review gates
- Changes to DCAT records that affect licensing, access constraints, or sensitive content require governance review.
- New external data sources must be reviewed for attribution, licensing compatibility, and sovereignty implications.

### CARE and sovereignty considerations
- If a dataset includes Indigenous knowledge, culturally sensitive locations, or restricted site information:
  - apply redaction/generalization rules,
  - document the basis for restriction (without leaking protected details),
  - enforce access controls at the API boundary.

### AI usage constraints
- This document permits summarization/structure extraction/translation/keyword indexing.
- It prohibits generating policy and inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.1 | 2025-12-24 | Align headings + add required Purpose block + parent catalog README link | TBD |
| v1.0.0 | 2025-12-23 | Initial README for DCAT catalog output directory | TBD |

---

Footer refs:
- Parent catalog: `data/catalog/README.md`
- STAC: `data/stac/README.md`
- PROV: `data/prov/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`