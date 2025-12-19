---
title: "Kansas Frontier Matrix"
path: "README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
status: "active"
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

doc_uuid: "urn:kfm:doc:readme:v1.0.0"
semantic_document_id: "kfm-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:readme:v1.0.0"
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

# Kansas Frontier Matrix

Kansas Frontier Matrix (KFM) is an open-source geospatial + historical knowledge system designed as a living atlas of Kansas, integrating historical, cultural, and ecological data into an interactive map and timeline experience.

This repository is organized around a governed, provenance-first pipeline that supports:
- standards-based catalogs (STAC / DCAT / PROV),
- a Neo4j knowledge graph,
- contracted APIs,
- a React map UI,
- curated Story Nodes,
- and Focus Mode narratives that must remain evidence-linked.

## Quick links

- Master guide: `docs/MASTER_GUIDE_v12.md`
- System documentation: `docs/architecture/` (see PDFs if present)
- Templates:
  - `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
  - `docs/templates/TEMPLATE__STORY_NODE_V3.md`
  - `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

## What KFM is

KFM blends a data hub with a storytelling tool:
- It ingests diverse sources (documents, images, maps, structured GIS layers).
- It standardizes outputs into catalogs and lineage bundles.
- It builds a semantic graph for query and context assembly.
- It serves map + narrative experiences through APIs and a web UI.
- It produces Story Nodes and Focus Mode narratives that always link back to cited source assets.

## Canonical pipeline

The pipeline ordering is non-negotiable:

1. ETL
2. STAC / DCAT / PROV catalogs
3. Neo4j graph
4. APIs
5. React map UI
6. Story Nodes
7. Focus Mode

~~~mermaid
flowchart LR
  A[ETL] --> B[STAC DCAT PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

## Repository layout

The repo is expected to follow this top-level structure:

~~~text
📁 .github/
📁 data/
📁 docs/
📁 mcp/
📁 schemas/
📁 src/
📁 tests/
📁 tools/
📁 web/
📁 releases/
~~~

### Where things go

| Area | Path | What lives here |
|---|---|---|
| Raw and staged data | `data/` | `raw/`, `work/`, `processed/` plus domain subfolders |
| Catalog outputs | `data/stac/` and `data/catalog/dcat/` and `data/prov/` | STAC items/collections, DCAT datasets, PROV lineage |
| Pipelines | `src/pipelines/` | ETL + catalog build + graph build |
| Graph | `src/graph/` | Ontology bindings, migrations, constraints |
| APIs | `src/server/` (or `src/api/` if used) | REST/GraphQL contracts and services |
| Frontend | `web/` | React + MapLibre UI, layer registry, UX |
| Story Nodes | `docs/reports/.../story_nodes/` | Narrative artifacts with provenance |
| Standards and templates | `docs/standards/` and `docs/templates/` | Markdown protocol + governed doc templates |
| Tests | `tests/` | Unit/integration/contract tests |
| Tooling | `tools/` | Validation scripts, helpers |
| Experiments | `mcp/` | Model cards, SOPs, runs, experiments |

## Working agreements and invariants

- Preserve the canonical pipeline ordering.
- Provenance is first-class: every public narrative must trace to source assets.
- Frontend does **not** read Neo4j directly; it consumes contracts through the API layer.
- Pipelines must be deterministic and idempotent.
- Sensitive content must be generalized/redacted according to governance and sovereignty rules.

## Getting started

### Read first

1. `docs/MASTER_GUIDE_v12.md`
2. `docs/templates/` (use templates for all governed docs)
3. `docs/standards/` (Markdown protocol and any catalog/telemetry rules)

### Choose a contribution path

- Data contributor: add sources and metadata, validate catalogs.
- Pipeline contributor: implement/adjust ETL, catalog, or graph build steps.
- Graph contributor: update ontology mappings and migrations.
- API contributor: add/extend endpoints with contract tests.
- UI contributor: add layers and Focus Mode UI behavior.
- Story curator: create Story Nodes with source-linked claims.

## Data lifecycle

Data should move through these stages:

- `data/raw/` → `data/work/` → `data/processed/` → `data/stac/` (plus `data/catalog/dcat/` and `data/prov/`)

Guidelines:
- Keep derived datasets out of `src/`.
- Keep stable identifiers and record version lineage.

## Catalogs and lineage

KFM aligns outputs to:
- STAC for spatiotemporal assets
- DCAT for dataset-level catalog views
- PROV-O for lineage and reproducibility

Expected behavior:
- Each dataset has discoverable catalog metadata.
- Each transformation run has a recorded provenance activity.
- Graph entities can be traced back to catalog item IDs.

## Story Nodes and Focus Mode

Story Nodes are curated narrative artifacts that:
- reference concrete datasets/documents/asset IDs,
- connect to graph entities,
- and render in the UI with citations and audit warnings when applicable.

Focus Mode is the interactive narrative experience that:
- assembles context bundles from API responses,
- enforces provenance-linked claims,
- and exposes optional explanation / uncertainty affordances for predictive content.

## Governance and ethics

KFM is governed under FAIR+CARE principles and sovereignty-aware rules.
When adding new datasets, narrative behaviors, or public endpoints:
- document provenance and license terms,
- tag sensitivity appropriately,
- and follow review gates defined in governance documentation.

## Contributing

### Documentation requirements

All non-trivial changes must include governed documentation updates:
- Use exactly one template from `docs/templates/`.
- Keep YAML front-matter keys intact.
- Record affected pipeline stages.
- List impacted paths and validation steps.

### API changes

If you add or change an endpoint:
- use `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- update schemas and add contract tests

### Story Nodes

If you add a narrative node:
- use `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- ensure every factual claim maps to a cited dataset/document ID

## Validation

Run the repo’s validation pipeline before submitting changes.

~~~bash
# Commands are repo-specific.
# Replace with the actual lint/test/schema validation commands used in this repository.
~~~

## License

- Code: see repository license files (not confirmed here).
- Data/content: see dataset-level license fields in catalogs; some sources may carry additional restrictions.

## Version history

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README scaffold aligned to KFM v12 docs | TBD |
