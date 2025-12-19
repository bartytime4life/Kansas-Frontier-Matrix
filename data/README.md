---
title: "KFM Data Directory (data/)"
path: "data/README.md"
version: "v0.1.0-draft"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data-readme:v0.1.0-draft"
semantic_document_id: "kfm-data-readme-v0.1.0-draft"
event_source_id: "ledger:kfm:doc:data-readme:v0.1.0-draft"
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

# KFM Data Directory (data/)

## 📘 Overview

### Purpose
This directory is the canonical home for **KFM data assets** across the pipeline:
- staged source inputs (**raw → work → processed**)
- catalog outputs (**STAC / DCAT / PROV**)
- domain-scoped organization for datasets that feed the graph, APIs, and UI experiences.

### Scope
In scope for `data/`:
- **Domain data** staged by pipeline phase (raw/work/processed; plus optional reports)
- **Catalog JSON outputs** (STAC Collections + Items; DCAT dataset views; PROV lineage bundles)

Out of scope for `data/`:
- source code (goes in `src/`)
- documentation (goes in `docs/`)
- experiment/run artifacts (goes in `mcp/`)

### Audience
- ETL/pipeline developers
- data contributors and curators
- catalog/metadata maintainers
- graph ingestion maintainers

### Definitions
- **Domain:** a top-level dataset family, typically stored under `data/<domain>/`
- **Raw:** original source material (immutably preserved once committed)
- **Work:** intermediate transforms and normalization outputs (regeneratable)
- **Processed:** analysis-ready / normalized / derived datasets
- **STAC:** SpatioTemporal Asset Catalog (Collections + Items)
- **DCAT:** Dataset Catalog Vocabulary (dataset-level metadata “views”)
- **PROV:** W3C PROV-O lineage describing activities, agents, and derivations

### Key artifacts
- Domain staging directories: `data/<domain>/{raw,work,processed,stac}/`
- Global catalogs:
  - `data/stac/collections/` (STAC Collections)
  - `data/stac/items/` (STAC Items)
  - `data/catalog/dcat/` (DCAT dataset records)
  - `data/prov/` (PROV lineage bundles)

### Definition of done
A dataset/domain addition is “done” when:
- inputs are staged through raw/work/processed (as applicable)
- STAC Collection + Item(s) exist and validate
- DCAT dataset record exists (minimum: title/description/license/keywords)
- PROV lineage exists for the transform activity that generated outputs
- docs exist for the new domain under `docs/<domain>/` or `docs/data/<domain>/` (choose one canonical location and link)

### Related repository paths
| System / Area | Canonical location | What it governs |
|---|---|---|
| Data domains | `data/` | Raw/work/processed organization per domain |
| STAC | `data/stac/` | STAC Collections + Items |
| DCAT | `data/catalog/dcat/` | DCAT dataset views/records |
| PROV | `data/prov/` | PROV lineage bundles (JSON-LD) |
| Domain docs | `docs/<domain>/` or `docs/data/<domain>/` | Domain narrative + mappings + evidence notes |

### Expected file tree for this sub-area
~~~text
📁 data/
├── 📄 README.md
├── 📁 <domain>/
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   └── 📁 stac/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
├── 📁 prov/
└── 📁 reports/   # optional: generated summaries/figures (when required)
~~~

## 🧭 Context

### Background
KFM’s canonical system ordering is:
- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

The `data/` directory is where the **staged inputs** and **catalog outputs** live to support this chain.

### Assumptions
- Pipelines are intended to be deterministic and replayable, with artifacts traceable via provenance.
- Catalog outputs (STAC/DCAT/PROV) are treated as first-class, machine-validated artifacts.

### Constraints / invariants
- Do not publish unsourced claims in narrative contexts; data outputs must remain provenance-linked.
- Catalog outputs must stay consistent with their corresponding staged datasets.
- Apply governance/ethics/sovereignty policies when handling sensitive data (see refs in front matter).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A["ETL + Normalization"] --> B["Staged Data (raw/work/processed)"]
  B --> C["Catalogs (STAC/DCAT/PROV)"]
  C --> D["Neo4j Graph"]
  D --> E["API Layer"]
  E --> F["Web UI (Map + Story Nodes + Focus Mode)"]
~~~

## 📦 Data & Metadata

### Required staging lifecycle
Staging follows the required lifecycle:
- `raw/` → `work/` → `processed/` → catalog outputs (`stac/`, plus global STAC/DCAT/PROV locations)

### Organizing by domain + stage
Data is organized **by domain and by stage**. Example domain layout:
- `data/environment/raw/`
- `data/environment/work/`
- `data/environment/processed/`
- `data/environment/stac/` (domain-local STAC JSONs, when used)

### Catalog outputs (global)
Where catalog outputs live:
- STAC JSON:
  - `data/stac/collections/`
  - `data/stac/items/`
- DCAT dataset records:
  - `data/catalog/dcat/`
- PROV lineage bundles:
  - `data/prov/`

### When adding a new dataset/domain
1. Create the domain directory and stage folders:
   - `data/<domain>/raw/`
   - `data/<domain>/work/`
   - `data/<domain>/processed/`
   - `data/<domain>/stac/` (if producing domain-local STAC)
2. Add domain documentation:
   - `docs/<domain>/` **or** `docs/data/<domain>/` (choose one canonical location and link)
3. Ensure catalog artifacts exist and validate:
   - STAC Collection + Item(s)
   - DCAT dataset record
   - PROV lineage bundle for the generating transform activity

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Use STAC **Collections** to define dataset groupings and metadata.
- Use STAC **Items** to represent individual assets/records, linking to staged outputs.

### DCAT
- Maintain DCAT dataset records as “views” for discovery and dataset-level metadata.

### PROV
- Produce PROV lineage (JSON-LD) capturing:
  - the transform activity
  - responsible agents (as modeled)
  - input and output derivations

### Versioning
- New dataset versions should link predecessor/successor.
- The graph should mirror dataset version lineage.