---
title: "KFM Dataset Catalog Outputs — data/catalog README"
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

# `data/catalog/` — KFM dataset catalogs

## 📘 Overview

### Purpose

`data/catalog/` is the canonical home for **dataset-level discovery catalogs** emitted by the KFM catalog stage. In v13+ target layout, this primarily means **DCAT** records under `data/catalog/dcat/`.

This directory exists to support the canonical pipeline ordering:

**ETL → STAC/DCAT/PROV → Graph → API → UI → Story Nodes → Focus Mode**

`data/catalog/` focuses on *discovery and distribution metadata* (dataset identity, licensing, publisher/contact, distributions, landing pages), complementing:

- `data/stac/` for spatiotemporal asset-level catalogs (Collections/Items)
- `data/prov/` for lineage and auditability (Activities/Entities/Agents)

### Scope

| In Scope | Out of Scope |
|---|---|
| Folder-level contract for dataset catalogs under `data/catalog/` | Implementing catalog build code (belongs under `src/pipelines/`) |
| DCAT record layout conventions and linkage expectations | Full DCAT field-by-field specification (governed by the KFM-DCAT profile + schemas) |
| Validation expectations and governance notes | UI design, styling, and rendering (belongs under `web/`) |
| How DCAT relates to STAC/PROV/Graph/API | Direct UI access to graph (disallowed; UI consumes APIs only) |

### Audience

- **Primary:** catalog maintainers, data engineers producing DCAT outputs
- **Secondary:** graph/ontology maintainers, API developers, Story Node authors, reviewers/auditors

### Definitions

- Link: `docs/glossary.md` *(not confirmed in repo — add or repair link if the glossary lives elsewhere)*
- Terms used in this doc: DCAT, dataset, distribution, landing page, STAC, PROV, evidence artifact, provenance, redaction.

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Dataset catalogs | `data/catalog/dcat/` | Catalog stage | DCAT outputs (JSON-LD / TTL as adopted) |
| STAC outputs | `data/stac/` | Catalog stage | Collections + Items (spatiotemporal evidence) |
| Provenance | `data/prov/` | ETL + catalog stage | Run and product lineage bundles |
| Schemas | `schemas/` | Contracts/CI | DCAT schema validation targets *(not confirmed in repo)* |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Pipeline ordering + invariants *(not confirmed in repo)* |
| v13 blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Canonical roots + readiness gates *(not confirmed in repo)* |

### Definition of done

- [ ] Front-matter complete and `path` matches file location
- [ ] Folder contract is explicit (what belongs here vs not)
- [ ] Expected directory tree is provided and consistent with `data/README.md`
- [ ] Validation and integrity expectations are listed
- [ ] Governance, sensitivity, and CARE considerations are documented

---

## 🗂️ Directory Layout

### This document

- `path`: `data/catalog/README.md` (must match front-matter)

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/<domain>/{raw,work,processed}/` | Source snapshots → transforms → normalized outputs |
| STAC catalogs | `data/stac/` | STAC Collections + Items |
| Dataset catalogs | `data/catalog/` | Dataset-level catalogs (DCAT) |
| Provenance | `data/prov/` | PROV lineage bundles |
| Graph import artifacts | `data/graph/` | CSV + optional Cypher loaders |
| Pipelines | `src/pipelines/` | ETL + catalog builders |
| Graph subsystem | `src/graph/` | Ontology bindings + graph build |
| API boundary | `src/server/` | Contracted access + redaction gates *(not confirmed in repo)* |
| UI | `web/` | React/Map UI (never reads Neo4j directly) |
| Story Nodes | `docs/reports/story_nodes/` | Narrative artifacts (provenance-linked) |

### Expected file tree

This README documents a minimal, repo-safe structure. If the repo adopts a deeper DCAT sub-structure (e.g., separating dataset vs distribution files), update this tree to match what exists in-repo.

~~~text
📁 data/
└── 📁 catalog/
    ├── 📄 README.md
    └── 📁 dcat/
        ├── 📄 <dataset-id>.jsonld
        ├── 📄 <dataset-id>.ttl
        └── 📄 ...
~~~

### What belongs here

#### `data/catalog/dcat/`

- **DCAT dataset discovery records** produced by the catalog stage.
- One or more files per dataset, depending on adopted serialization:
  - JSON-LD (`.jsonld`) recommended where possible
  - Turtle/RDF (`.ttl`) optional if adopted in the repo

### What does not belong here

- Raw source data snapshots (`data/<domain>/raw/`)
- Intermediate transforms (`data/<domain>/work/`)
- Normalized downstream outputs (`data/<domain>/processed/`)
- STAC Collections/Items (`data/stac/`)
- PROV bundles (`data/prov/`)
- Graph build code or ontology definitions (`src/graph/` + governed docs)
- API contracts and server code (`src/server/`)
- UI configuration/runtime assets (`web/`)

---

## 📦 Data and Metadata

### Inputs

DCAT records are typically derived from a combination of:

| Input | Typical location | Notes |
|---|---|---|
| Domain processed outputs | `data/<domain>/processed/` | What is being cataloged for discovery |
| STAC outputs | `data/stac/` | DCAT distributions may point to STAC Collections/Items or their landing pages |
| Provenance bundles | `data/prov/` | DCAT records should reference lineage IDs where required by profile |
| Domain documentation | `docs/data/<domain>/` | Mapping rationale, licensing, sensitivity notes *(path not confirmed in repo)* |

### Outputs

| Output | Location | Notes |
|---|---|---|
| DCAT dataset record(s) | `data/catalog/dcat/` | Dataset-level discovery metadata |
| Distributions | Inside DCAT records | Should point to downloads, STAC endpoints, landing pages, API endpoints as governed |

### Dataset and distribution intent

- **STAC** answers: “What spatiotemporal items/assets exist?”
- **DCAT** answers: “What dataset exists, who publishes it, under what license, and how do I access it?”
- **PROV** answers: “How was it produced, from what, by whom, and when?”

KFM expects these three to remain **consistent and mutually referential**.

### Naming and stable identifiers

A minimal convention (repo-safe):

- `<dataset-id>` is stable across rebuilds.
- Filenames in `data/catalog/dcat/` should be stable and diff-friendly.
- If datasets are versioned, ensure successor/predecessor relationships are represented consistently across:
  - DCAT record metadata
  - PROV lineage
  - Graph import fixtures and graph nodes
  - API payloads (exposed identifiers)

---

## 🔗 Linkage expectations

### Cross-catalog alignment

For each dataset intended for discovery and downstream use:

- A DCAT dataset record exists under `data/catalog/dcat/`.
- Corresponding STAC Collection(s)/Item(s) exist under `data/stac/` where spatiotemporal assets are present.
- A PROV activity/bundle exists under `data/prov/` describing production lineage.

### Downstream consumption rules

- **Graph ingestion** may reference DCAT dataset IDs as authoritative dataset identifiers.
- **API boundary** should expose DCAT metadata via contracted endpoints and enforce classification/redaction.
- **UI** should consume DCAT metadata only through the API boundary.
- **Story Nodes** should cite DCAT dataset IDs when using dataset-level claims (publisher, license, coverage), and cite STAC/PROV IDs for item-level claims and lineage.

---

## 🧪 Validation and CI

### Minimum checks

- DCAT outputs validate against schemas under `schemas/dcat/` *(not confirmed in repo — align with actual schema registry)*
- Link integrity checks:
  - distributions resolve to valid URLs or stable local IDs (where used)
  - referenced STAC IDs resolve (if referenced by ID)
  - referenced PROV activity IDs resolve (if referenced by ID)
- Determinism:
  - rerunning catalog build with unchanged inputs produces stable IDs and diffable output files
- Governance checks:
  - no restricted locations are exposed in public dataset metadata beyond allowed generalized extents
  - no PII is present in DCAT fields (contacts must be governed and sanitized)

### Reproduction

~~~bash
# Placeholder — replace with repo-specific commands
# 1) Build catalogs (STAC/DCAT/PROV)
# 2) Validate DCAT records against schemas
# 3) Run link integrity checks across STAC/DCAT/PROV
~~~

---

## ⚖ FAIR+CARE and Governance

### Sensitivity and redaction

Even at the dataset level, catalog metadata can leak sensitive information (e.g., overly precise spatial extents, sensitive site names, or distribution links that expose restricted files). Before publishing:

- generalize spatial coverage where required,
- redact or restrict distribution endpoints where required,
- record redaction/generalization in provenance where policy permits.

### Review gates

Human review is required when:

- introducing a new external dataset source,
- adding or changing public distributions/endpoints,
- changing sensitivity/classification labels,
- publishing any dataset derived from sensitive/restricted inputs,
- adding catalog fields that could enable inference of protected locations.

### AI usage constraints

- Allowed: summarization, structure extraction, translation, keyword indexing.
- Prohibited: generating new governance policy or inferring sensitive locations.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-24 | Initial README for `data/catalog/` | TBD |

---

Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- v13 Blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Universal template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
