---
title: "KFM DCAT Catalog Output Directory"
path: "data/catalog/dcat/README.md"
version: "v1.0.0"
last_updated: "2025-12-23"
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

doc_uuid: "urn:kfm:doc:data:catalog:dcat:readme:v1.0.0"
semantic_document_id: "kfm-data-catalog-dcat-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:catalog:dcat:readme:v1.0.0"
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

## 📘 Overview

### Purpose

- This directory is the canonical home for **DCAT dataset records** produced by the KFM **Catalog** stage.
- It documents what belongs in `data/catalog/dcat/`, how records should be structured at a high level, and how they link to STAC and PROV artifacts for downstream consumers.
- It is intended to prevent “mystery duplicates” and keep catalog artifacts in one predictable place.

### Scope

| In Scope | Out of Scope |
|---|---|
| Directory purpose + layout conventions for DCAT records | Full DCAT profile specification details (belongs in `docs/standards/`) |
| Minimum metadata expectations at a directory level | Exact ETL + catalog builder implementation |
| How DCAT records relate to STAC + PROV artifacts | API endpoint design or UI behavior details |
| Validation expectations and review gates | Publishing workflows outside the repo (external portals, hosting) |

### Audience

- Primary: catalog maintainers, data engineering maintainers, API maintainers
- Secondary: governance reviewers, external contributors adding new datasets/domains

### Definitions

- Link: `docs/glossary.md`
- Terms used in this doc: DCAT, Dataset, Distribution, JSON-LD, RDF, STAC, PROV, stable identifier, version lineage

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 | `docs/MASTER_GUIDE_v12.md` | KFM core maintainers | Canonical pipeline ordering + invariants |
| Redesign Blueprint v13 | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | KFM core maintainers | Canonical paths for catalog outputs |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Catalog maintainers | DCAT field constraints and required mappings |
| DCAT validation schemas | `schemas/dcat/` | Catalog maintainers | Machine-validation inputs used by CI |
| STAC catalogs | `data/stac/` | Catalog maintainers | Geospatial collections/items referenced by DCAT distributions |
| PROV bundles | `data/prov/` | Pipeline maintainers | Lineage for dataset generation and catalog builds |

### Definition of done

- [ ] Front-matter complete + valid
- [ ] Directory purpose + boundaries are explicit
- [ ] DCAT ↔ STAC/PROV linkage expectations are documented
- [ ] Validation steps are listed and repeatable
- [ ] Governance + CARE/sovereignty considerations are explicitly stated

## 🗂️ Directory Layout

### This document

- `path`: `data/catalog/dcat/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset records (JSON-LD/RDF serializations) |
| STAC outputs | `data/stac/` | STAC collections + items (geospatial asset catalogs) |
| PROV outputs | `data/prov/` | PROV lineage bundles for runs and transforms |
| Data domains | `data/<domain>/` | `raw/`, `work/`, `processed/` per domain |
| Pipelines | `src/pipelines/` | ETL + catalog build code (idempotent, deterministic) |
| Graph | `src/graph/` + `data/graph/` | Ontology bindings + import artifacts |
| API boundary | `src/server/` | Contracts + endpoints (UI never reads the graph directly) |
| Frontend | `web/` | React/Map UI + layer registries |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 catalog/
    └── 📁 dcat/
        ├── 📄 README.md
        ├── 📄 dataset--<dataset_id>.jsonld
        ├── 📄 dataset--<dataset_id>.ttl
        └── 📄 catalog.<ext>
~~~

Notes:
- `dataset--<dataset_id>.<ext>` represents one DCAT dataset record per logical dataset.
- `catalog.<ext>` is optional, if the repo adopts an aggregate `dcat:Catalog` serialization.
- Exact naming + serialization rules must match `docs/standards/KFM_DCAT_PROFILE.md`.

## 🧭 Context

### Background

KFM uses open standards to make datasets **discoverable, interoperable, and traceable** across the pipeline. DCAT provides dataset-level metadata suitable for indexing and federation across catalogs, while STAC and PROV provide asset-level metadata and lineage.

DCAT records can describe datasets that:
- point to **STAC collections/items** when the dataset is geospatial, and/or
- point to **tabular or document assets** (e.g., CSVs) when the dataset is non-geospatial.

### Assumptions

- DCAT records in this directory are **catalog artifacts**, typically generated (or at least validated) as part of the Catalog stage.
- Identifiers are **stable** and suitable for referencing from graph nodes and API payloads.
- Catalog artifacts validate against schemas under `schemas/`.

### Constraints and invariants

- Canonical flow is preserved: ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode.
- UI does not query Neo4j directly; all consumption is via API contracts.
- Sensitive or restricted locations and culturally sensitive knowledge must be protected via:
  - generalization where required,
  - API-level redaction,
  - review gates and auditability.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| Do we publish an aggregate `dcat:Catalog` file (`catalog.jsonld` or `catalog.ttl`) in addition to per-dataset records? | Catalog maintainers | TBD |
| What is the canonical DCAT serialization in-repo (JSON-LD only vs JSON-LD + Turtle)? | Catalog maintainers | TBD |
| What is the authoritative file naming convention for dataset records (prefix, separator, version segment, etc.)? | Catalog maintainers | TBD |

### Future extensions

- Add SHACL shape bundles (or equivalent constraints) under `schemas/dcat/` if needed for richer validation.
- Add a catalog export/publish step (outside repo scope) that republishes DCAT artifacts to an external portal.
- Add explicit predecessor/successor links for dataset versions, mirrored into the graph.

## 🗺️ Diagrams

### System and dataflow

~~~mermaid
flowchart LR
  A[ETL<br/>src/pipelines] --> B[data/<domain>/processed]
  B --> C[Catalog build<br/>src/pipelines]
  C --> S[STAC<br/>data/stac]
  C --> D[DCAT<br/>data/catalog/dcat]
  C --> P[PROV<br/>data/prov]
  S --> G[Neo4j graph<br/>src/graph]
  D --> G
  P --> G
  G --> API[API boundary<br/>src/server]
  API --> UI[UI<br/>web]
  UI --> SN[Story Nodes<br/>docs/reports/story_nodes]
  SN --> FM[Focus Mode<br/>provenance-linked only]
~~~

### Optional: sequence diagram

~~~mermaid
sequenceDiagram
  participant UI as UI
  participant API as API
  participant Graph as Graph
  participant DCAT as DCAT files

  UI->>API: request dataset metadata (dataset_id)
  API->>Graph: fetch dataset node + provenance refs
  API->>DCAT: load DCAT record by dataset_id
  Graph-->>API: context bundle + IDs
  DCAT-->>API: DCAT dataset metadata
  API-->>UI: contracted payload with citations/refs
~~~

## 📦 Data and Metadata

### Inputs

| Input | Format | Where from | Validation |
|---|---|---|---|
| Processed domain outputs | domain-dependent (CSV/GeoJSON/etc.) | `data/<domain>/processed/` | domain validation + deterministic pipeline rules |
| STAC collections/items | JSON | `data/stac/**` | STAC profile validation |
| Provenance bundles | JSON-LD / RDF | `data/prov/**` | PROV profile validation |

### Outputs

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| DCAT dataset record | JSON-LD or Turtle | `data/catalog/dcat/dataset--<dataset_id>.<ext>` | KFM-DCAT profile + `schemas/dcat/**` |
| Optional aggregate catalog | JSON-LD or Turtle | `data/catalog/dcat/catalog.<ext>` | KFM-DCAT profile + `schemas/dcat/**` |

### Sensitivity and redaction

- DCAT records must not expose restricted locations, sensitive coordinates, or culturally protected knowledge.
- If a dataset is restricted, the DCAT record should reflect access constraints and ensure distribution links do not bypass policy.

### Quality signals

- Schema validation passes for all DCAT records.
- No broken references:
  - Distribution URLs/paths resolve inside the repo or at controlled endpoints.
  - Identifiers referenced by graph/API are consistent.
- Provenance completeness: the dataset has a PROV activity and traceable inputs.

## 🌐 STAC, DCAT and PROV Alignment

### STAC

- Collections involved: datasets may map to one or more STAC collections.
- Items involved: DCAT distributions may point at STAC items or at the assets referenced by STAC.
- Extensions: any required extensions must be documented in the STAC profile and validated.

### DCAT

- Dataset identifiers: DCAT dataset identifiers must be stable and referenceable from graph nodes and API contracts.
- License mapping: DCAT license must reflect the dataset’s license and any attribution requirements.
- Contact and publisher mapping: ensure dataset-level publisher/maintainer metadata is captured (per DCAT profile).
- Distribution links: represent where the dataset can be accessed (repo paths or controlled endpoints).

### PROV-O

- `prov:wasDerivedFrom`: link dataset outputs to their upstream inputs.
- `prov:wasGeneratedBy`: link dataset outputs to a run/activity identifier.
- Activity and agent identities: catalog generation should be attributable to a pipeline/run identity.

### Versioning

- If the dataset is versioned, predecessor/successor relationships should be represented consistently across:
  - DCAT metadata
  - STAC versioning links
  - PROV lineage
  - Graph relationships

## 🧱 Architecture

### Components

| Component | Responsibility | Interface |
|---|---|---|
| ETL | Ingest + normalize sources | configs + run logs |
| Catalogs | Produce STAC/DCAT/PROV artifacts | JSON/RDF + validators |
| Graph | Neo4j knowledge graph | Cypher + API layer |
| APIs | Serve contracts | REST/GraphQL |
| UI | Map + narrative experience | API calls |
| Story Nodes | Curated narrative content | linked to graph + evidence |
| Focus Mode | Contextual synthesis | provenance-linked only |

### Interfaces and contracts

| Contract | Location | Versioning rule |
|---|---|---|
| Data schemas | `schemas/` | Semver + changelog |
| API schemas | `src/server/` + `docs/api/` | Contract tests required |
| UI layer registry | `web/**/layers/**` | Schema-validated |

### Extension points checklist

- [ ] Data: new domain under `data/<domain>/...`
- [ ] STAC: new collection + item(s) validated
- [ ] DCAT: dataset record added/updated under `data/catalog/dcat/`
- [ ] PROV: activity + agent identifiers recorded under `data/prov/`
- [ ] Graph: dataset + evidence nodes reference STAC/DCAT/PROV IDs
- [ ] APIs: contracts expose dataset metadata without leaking restricted content
- [ ] UI: new dataset layers/entries added via registry and API only
- [ ] Focus Mode: provenance references enforced end-to-end
- [ ] Telemetry: validation signals recorded (if applicable)

## 🧠 Story Node and Focus Mode Integration

### How this work surfaces in Focus Mode

- DCAT dataset identifiers should be referenceable as evidence IDs in context bundles.
- Story Nodes should cite dataset IDs and/or specific STAC/PROV evidence IDs when referencing dataset-derived claims.

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

## 🧪 Validation and CI

### Validation steps

- [ ] Markdown protocol checks
- [ ] Schema validation for DCAT artifacts (`schemas/dcat/**`)
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

## ⚖ FAIR+CARE and Governance

### Review gates

- Changes to DCAT records that affect licensing, access constraints, or sensitive content require governance review.
- New external data sources must be reviewed for attribution, licensing compatibility, and sovereignty implications.

### CARE and sovereignty considerations

- If a dataset includes Indigenous knowledge, culturally sensitive locations, or restricted site information:
  - apply redaction/generalization rules,
  - document the basis for restriction,
  - ensure access controls are enforced at the API boundary.

### AI usage constraints

- This document permits summarization/structural extraction/translation/keyword indexing.
- It prohibits generating policy and inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-23 | Initial README for DCAT catalog output directory | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
