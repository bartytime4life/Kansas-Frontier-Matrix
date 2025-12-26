---
title: "KFM Data Catalogs — data/catalog/"
path: "data/catalog/README.md"
version: "v1.0.0"
last_updated: "2025-12-26"
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

# KFM Data Catalogs

> **Purpose (required):** Define what belongs under `data/catalog/`, how DCAT dataset records are organized, and how catalog outputs connect to `data/stac/` and `data/prov/` within the canonical KFM pipeline.

## 📘 Overview

### Scope

| In Scope | Out of Scope |
|---|---|
| DCAT dataset records used for discovery and downstream indexing (`data/catalog/dcat/**`). | Raw source snapshots (`data/<domain>/raw/`). |
| Dataset-level metadata: title/description/license/keywords, publisher/contact, temporal/spatial coverage, and distributions. | Intermediate transforms (`data/<domain>/work/`). |
| Publication-safe metadata meant to be surfaced via API or external catalog exports. | Processed domain outputs (`data/<domain>/processed/`) themselves (only referenced from catalogs). |
| Linkage expectations to STAC and PROV identifiers (how evidence stays traceable). | STAC catalogs (`data/stac/**`) and PROV bundles (`data/prov/**`) themselves (documented elsewhere). |

### Audience

- Catalog maintainers
- ETL/pipeline authors producing catalog outputs
- API/UI maintainers consuming catalog entries
- Governance/audit reviewers validating evidence discoverability + lineage

### Definitions

- Glossary: `docs/glossary.md` (**not confirmed in repo** — update link if glossary lives elsewhere)
- **DCAT**: Dataset discovery vocabulary (dataset-level “what is this dataset?”)
- **STAC**: Asset-level cataloging for spatiotemporal/geospatial items
- **PROV**: Provenance/lineage bundles connecting inputs → activities → outputs

### Key artifacts

| Artifact | Path | Notes |
|---|---|---|
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Canonical pipeline + invariants |
| Data lifecycle + roots | `data/README.md` | Defines `data/stac/`, `data/catalog/dcat/`, `data/prov/` |
| Schema registry | `schemas/README.md` | Contract home for STAC/DCAT/PROV validation (**not confirmed in repo**) |
| Catalog builders | `src/pipelines/` | Producers of STAC/DCAT/PROV (**not confirmed in repo**) |
| API boundary | `src/server/` | Consumer-facing access layer (UI must not bypass) (**not confirmed in repo**) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts that must cite evidence IDs (**not confirmed in repo**) |

### Definition of done

- [ ] Front-matter complete and `path` matches `data/catalog/README.md`.
- [ ] Directory responsibilities and “what lives here vs elsewhere” are explicit.
- [ ] Expected file tree documented (and marked “target” where applicable).
- [ ] Alignment rules for STAC/DCAT/PROV are included.
- [ ] Validation + CI expectations are stated (commands may be placeholders).
- [ ] FAIR+CARE / sovereignty considerations are explicit.
- [ ] Maintainer review completed.

---

## 🗂️ Directory Layout

### This document

- `path`: `data/catalog/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data root | `data/` | Domains + global catalogs |
| DCAT catalogs | `data/catalog/dcat/` | Dataset records (JSON-LD / TTL as adopted) |
| STAC catalogs | `data/stac/collections/` + `data/stac/items/` | Collections + items (JSON) |
| PROV bundles | `data/prov/` | Lineage bundles (JSON-LD / TTL as adopted) |
| Graph import fixtures | `data/graph/` | CSV/Cypher import artifacts (if used) |
| Pipelines | `src/pipelines/` | ETL + catalog builders (**not confirmed in repo**) |
| Schemas/contracts | `schemas/` | Schema validation artifacts (**not confirmed in repo**) |
| API boundary | `src/server/` | Contracted access layer (REST/GraphQL) (**not confirmed in repo**) |
| UI | `web/` | React UI (never reads Neo4j directly) (**not confirmed in repo**) |

### Expected file tree for this sub-area

~~~text
📁 data/
└── 📁 catalog/
    ├── 📄 README.md
    └── 📁 dcat/
        └── 📄 <dataset-id>.jsonld   # or .ttl (as adopted)
~~~

---

## 🧭 Context

### How this fits the canonical pipeline

KFM’s canonical flow is:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

This folder is part of the **STAC/DCAT/PROV** stage: it holds **dataset-level discovery records** that help downstream systems (and external portals) find, understand, and attribute KFM datasets.

### Why DCAT lives here

- **STAC** is optimized for describing **assets/items** with spatial + temporal footprints (maps, rasters, vector layers, imagery, etc.).
- **DCAT** is optimized for describing **datasets** and their **distributions** (files, endpoints, packages, and access methods) in a way that general catalog tools understand.

In KFM, DCAT entries complement STAC by providing a dataset-centric view suitable for API listings and external catalog exports.

### Generated vs curated outputs

Preferred rule:
- Treat `data/catalog/dcat/**` as **pipeline output**.
- If metadata corrections are needed, update the upstream metadata sources (domain manifests, STAC collection fields, or pipeline configs) and **regenerate** DCAT where possible.

If a manual override is unavoidable, document:
- why it’s needed,
- which upstream source is missing,
- and how regeneration should resolve it later.

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  ETL[ETL<br/>data/<domain>/raw → work → processed] --> CAT[Catalog build]
  CAT --> STAC[STAC<br/>data/stac/**]
  CAT --> DCAT[DCAT<br/>data/catalog/dcat/**]
  CAT --> PROV[PROV<br/>data/prov/**]
  STAC --> GRAPH[Graph ingest<br/>Neo4j]
  DCAT --> API[API boundary<br/>src/server]
  GRAPH --> API
  API --> UI[UI<br/>web]
  UI --> STORY[Story Nodes<br/>docs/reports/story_nodes]
  STORY --> FOCUS[Focus Mode]
~~~

---

## 📦 Data & Metadata

### What a DCAT record represents

A DCAT record in `data/catalog/dcat/` should answer, at minimum:

- What is this dataset (title + description)?
- Who publishes/owns it (publisher/contact)?
- Under what terms can it be used (license)?
- What topics does it cover (keywords/themes)?
- How do you access it (distributions: files/endpoints/media types)?
- What time + space does it cover (temporal/spatial coverage where applicable)?

### Distribution hygiene

- Prefer **stable** access paths for distributions (avoid ephemeral locations).
- If distributions point to repo-tracked artifacts, keep links consistent with `data/<domain>/processed/` outputs.
- If distributions point to external storage/endpoints, ensure licenses/terms allow redistribution or at least linking.

### Identifier expectations

- Use **stable, deterministic identifiers** for datasets.
- Avoid renaming dataset IDs after publication; if renames are necessary, express version/lineage (see “Versioning” below).
- Recommended style: **kebab-case** identifiers (repo-wide convention preferred).

---

## 🌐 STAC, DCAT & PROV Alignment

### Policy for every dataset

For each dataset or evidence product intended for downstream use:

- STAC Collection + Item(s) (`data/stac/**`)
- DCAT dataset record (`data/catalog/dcat/**`)
- PROV activity/bundle (`data/prov/**`)
- Version lineage expressed across metadata + graph (when applicable)

### Minimum DCAT mapping

KFM requires at least a minimal DCAT mapping per dataset:

- title
- description
- license
- keywords

Where possible, this can be auto-generated from STAC to keep metadata consistent.

### Common field crosswalk

This is a pragmatic crosswalk used to keep STAC/DCAT in sync (exact profile rules live in schemas/specs):

| STAC concept | DCAT concept |
|---|---|
| `id` | `dct:identifier` |
| `description` | `dct:description` |
| Collection “title” | `dct:title` |
| `assets[].href` | `dcat:downloadURL` (or `dcat:accessURL`) |
| spatial extent | `dct:spatial` |
| temporal extent | `dct:temporal` |
| provider/owner | `dct:publisher` / `dct:creator` |

### Provenance linkage

- Provenance bundles are stored under `data/prov/`.
- DCAT records should enable downstream consumers to trace “how was this produced?” by referencing provenance identifiers or providing pointers that allow the API/graph to resolve provenance.

Mechanism is repo-defined and may use:
- DCAT extension properties, or
- `prov:*` fields if the serialization/profile supports it, or
- an API-resolved reference keyed by dataset ID.

(**Exact linkage mechanism is not confirmed in repo** — keep it consistent with the adopted catalog + schema contracts.)

### Versioning

- Avoid overwriting published catalogs without a lineage trail.
- When producing a new dataset version:
  - generate new STAC/DCAT/PROV artifacts,
  - link to predecessor/successor where the profile supports it,
  - and ensure the graph mirrors the version relationship so UIs can explain change over time.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes and Focus Mode are **evidence-first**:

- Story Nodes should cite:
  - **DCAT dataset IDs** (dataset-level)
  - **STAC item/collection IDs** (asset-level)
  - **PROV activity IDs** (lineage-level)

This ensures any narrative statement can resolve into:
- “what dataset is this?”
- “what asset(s) support it?”
- “how was it produced and from what sources?”

---

## 🧪 Validation & CI/CD

### Validation expectations

- [ ] Markdown protocol checks (front-matter, path match, formatting)
- [ ] DCAT serialization validity (JSON-LD/RDF parse)
- [ ] Contract/schema validation (DCAT profile) (**not confirmed in repo**)
- [ ] Link checks for distribution URLs/paths (no broken references)
- [ ] Sensitivity/sovereignty checks for discovery metadata (no restricted locations or prohibited disclosures)

### Reproduction

~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate DCAT bundles against schema/shapes
# 2) run contract + unit tests
# 3) run markdown lint / repo lint
~~~

---

## ⚖ FAIR+CARE & Governance

- Assume DCAT outputs may be **externally discoverable**; write metadata accordingly.
- Ensure:
  - license/attribution fields are present,
  - contact/publisher information is appropriate,
  - sensitive locations are not exposed (or are generalized) when required by governance.
- Any changes that:
  - downgrade/alter classification,
  - add new external distributions/endpoints,
  - or change licensing terms
  require human review under `docs/governance/*` policies (**paths not confirmed in repo**).

---

## 🕰️ Version History

| Version | Date | Summary |
|---:|---|---|
| v1.0.0 | 2025-12-26 | Initial README for `data/catalog/` (DCAT dataset catalog home). |

---

## ⚖️ Footer

Footer refs (do not remove):

- Master guide: `docs/MASTER_GUIDE_v12.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Data lifecycle: `data/README.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Ethics: `docs/governance/ETHICS.md`
