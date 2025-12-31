---
title: "🗃️ KFM data/ README"
path: "data/README.md"
version: "v1.0.0-draft"
last_updated: "2025-12-31"
status: "draft"
doc_kind: "Standard"
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
care_label: "Public · Low-Risk"
sensitivity: "public"
classification: "open"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:data:data-readme:v1.0.0-draft"
semantic_document_id: "kfm-data-readme-v1.0.0-draft"
event_source_id: "ledger:kfm:doc:data:data-readme:v1.0.0-draft"

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

# 🗃️ data/ — Data, Catalogs, and Provenance

## 📘 Overview

This folder is the canonical on-disk home for KFM’s governed data products and the machine-readable metadata that makes them auditable and ingestible.

What lives here
- Domain data at each lifecycle stage: raw → work → processed
- Published boundary metadata:
  - STAC for spatiotemporal assets
  - DCAT for dataset-level cataloging
  - PROV for lineage and reproducibility
- Graph-load exports used to build/refresh the knowledge graph (CSV, and optional Cypher)

What must not happen here
- “Mystery” data drops with no catalog + no provenance
- UI clients reading `data/` directly (UI must consume contracted APIs)
- Manual edits to generated metadata outputs without updating the generating pipeline

Golden rule
- If it isn’t cataloged (STAC/DCAT) and traceable (PROV), it isn’t “published” in KFM.

Quickstart for adding a new dataset
1) Create or pick a domain folder under `data/<domain>/`.
2) Put immutable inputs under `data/<domain>/raw/` and document the source.
3) Build a repeatable ETL that writes intermediates to `data/<domain>/work/` and final artifacts to `data/<domain>/processed/`.
4) Emit/refresh metadata:
   - STAC Item(s) + Collection(s)
   - DCAT dataset record(s)
   - PROV lineage bundle(s)
5) Validate schemas + links, then (only then) refresh the graph and downstream APIs/UI.

## 🗂️ Directory Layout

Core system folders (shared across all domains)

    📁 data/
    ├── 📄 README.md                         — This file
    │
    ├── 📁 stac/                             — Spatiotemporal asset catalog
    │   ├── 📁 collections/                  — STAC Collection JSON (grouping + high-level metadata)
    │   └── 📁 items/                        — STAC Item JSON (per-asset metadata; links to assets)
    │
    ├── 📁 catalog/                          — Dataset-level catalogs
    │   └── 📁 dcat/                         — DCAT datasets (per KFM-DCAT profile)
    │
    ├── 📁 prov/                             — PROV bundles (raw → work → processed lineage)
    │
    ├── 📁 graph/                            — Graph-load exports produced from catalogs/processed
    │   ├── 📁 csv/                          — Neo4j import tables
    │   └── 📁 cypher/                       — Optional graph migrations / complex updates
    │
    └── 📁 <domain>/                         — Domain namespace (repeatable pattern)
        ├── 📄 README.md                     — Domain inventory + pointers to `docs/data/<domain>/`
        ├── 📁 raw/                          — Immutable source inputs (as acquired)
        ├── 📁 work/                         — Reproducible intermediates (safe to regenerate)
        ├── 📁 processed/                    — Published outputs (referenced by STAC/DCAT)
        └── 📁 mappings/                     — Codebooks, join keys, schema alignment, lookups

Domain documentation conventions
- Keep full domain runbooks under: `docs/data/<domain>/README.md` (and subfolders).
- Keep a short “data inventory” README under: `data/<domain>/README.md`.

## 🧭 Context

KFM is contract-first and evidence-first:
- Contract-first: schemas and API contracts are treated as first-class artifacts.
- Evidence-first: stories and UI claims must be traceable to versioned, cataloged evidence.

Canonical pipeline order
ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → UI → Story Nodes → Focus Mode

This README enforces the “boundary artifact” concept:
- STAC/DCAT/PROV are the interface between data production (ETL) and all downstream systems.
- The graph, APIs, and UI should be built from these boundary artifacts, not from ad-hoc files.

Related governing references
- docs/MASTER_GUIDE_v13.md
- docs/standards/KFM_REPO_STRUCTURE_STANDARD.md
- docs/standards/KFM_STAC_PROFILE.md
- docs/standards/KFM_DCAT_PROFILE.md
- docs/standards/KFM_PROV_PROFILE.md
- docs/governance/ROOT_GOVERNANCE.md
- docs/governance/ETHICS.md
- docs/governance/SOVEREIGNTY.md
- docs/governance/REVIEW_GATES.md

## 🗺️ Diagrams

Lifecycle at a glance
- 🧪 Raw Sources → 🔁 ETL → 🧰 Work → ✅ Processed
- ✅ Processed → 🧾 STAC Items/Collections + 📚 DCAT + 🧬 PROV
- 🧾📚🧬 Catalogs → 🕸️ Graph → 🔌 APIs → 🗺️ UI → 🧠 Story Nodes → 🔎 Focus Mode

## 📦 Data & Metadata

Lifecycle staging rules
- raw/
  - Preserve original files and source context.
  - Do not “clean in place.” If you must transform, write to work/ or processed/.
- work/
  - Store intermediate results that are safe to delete + regenerate.
  - Prefer deterministic transforms driven by configs checked into the repo.
- processed/
  - Store final, versioned deliverables that the catalogs point to.
  - Include uncertainty/confidence attributes for modeled/derived layers.

Large-volume data guidance
- Multi-GB rasters and grids are typically stored as files (e.g., GeoTIFF/COG or equivalent) and indexed via STAC.
- Avoid “pixel-per-node” modeling in the graph; represent large rasters at dataset/layer granularity and serve access via APIs (e.g., tile endpoints) where appropriate.

Cloud-derived and modeled layers
- Some pipelines may use cloud services to derive Kansas-focused products (e.g., remote sensing composites).
- Record processing choices (scripts, parameters, model identity, timestamps) in PROV so results are auditable and reproducible.

Evidence artifact pattern
- If an analysis or model run produces a dataset used by the system, it becomes a derived data product:
  - Write outputs to processed/
  - Register them via STAC/DCAT
  - Record the run (inputs, parameters, agents/tools) in PROV
  - Do not present derived outputs as narrative truth without evidence links

Naming and identifiers
- Use stable dataset identifiers that can be referenced in:
  - STAC Item/Collection IDs
  - DCAT dataset IDs
  - Graph node IDs
  - Story Node citations
- If you change an identifier, treat it as a breaking change and update catalogs + downstream links.

## 🌐 STAC, DCAT & PROV Alignment

Minimum “publishable” package per dataset
- ✅ At least one processed artifact in `data/<domain>/processed/`
- ✅ STAC Item(s) referencing those artifact assets in `data/stac/items/`
- ✅ A STAC Collection grouping items in `data/stac/collections/`
- ✅ A DCAT dataset record in `data/catalog/dcat/`
- ✅ A PROV lineage bundle in `data/prov/` that traces raw → work → processed

Cross-layer linkage expectations
- STAC ↔ DCAT: dataset-level identifiers should align (and link) so catalogs agree.
- PROV ↔ STAC/DCAT: every published artifact should have lineage that points back to:
  - source acquisition
  - transformation activities
  - agents/tools
  - output artifacts

Profile extensions
- Do not add ad-hoc metadata fields.
- If a new metadata attribute is required, extend the relevant profile and add/adjust schemas under `schemas/`.

## 🧱 Architecture

Where code that touches data lives
- ETL pipelines: `src/pipelines/`
- Graph build/export: `src/graph/`
- API contracts + implementation: `src/server/`
- UI clients: `web/`

Hard boundaries
- `data/` is the storage + catalog boundary; it is not a public API.
- The UI must use contracted APIs, not direct reads of `data/` or direct queries to Neo4j.
- The graph should load from cataloged artifacts, not from untracked files.

## 🧩 Story Node & Focus Mode Integration

Story Nodes and Focus Mode are evidence consumers:
- Story Nodes may only cite evidence that exists in the catalogs/graph.
- Focus Mode is provenance-only: anything not tied to catalog/prov evidence must be treated as non-publishable draft content.

Implication for data work
- If you expect a dataset to appear in stories or Focus Mode, you must:
  - publish it to processed/
  - register it in STAC/DCAT
  - provide PROV lineage

## ✅ Validation & CI/CD

Minimum checks before merging data changes
- Front-matter and markdown format validation (KFM-MDP compliance)
- STAC schema validation (Items + Collections)
- DCAT validation (dataset records)
- PROV validation (lineage completeness)
- Link integrity:
  - STAC assets resolve to files/URLs
  - DCAT references resolve
  - PROV entities/activities match actual artifacts
- Governance checks:
  - sensitivity/classification labels present
  - restricted content handled per sovereignty policy

Not confirmed in repo
- Exact local command names for validators. Check `tools/` and CI workflows for the authoritative entry points.

## 🛡️ FAIR+CARE & Governance

Defaults
- Assume FAIR+CARE applies to all domains.
- If unsure about care_label or sensitivity, set care_label to "TBD" in domain docs and request governance review.

Sensitive data handling
- Do not publish precise locations for culturally sensitive sites or private individuals.
- Propagate classification and sensitivity from inputs to derived outputs.
- Ensure auditability: lineage + access constraints should be represented in catalogs and enforced at API boundaries.

## 🧾 Version History

- v1.0.0-draft — 2025-12-31 — Initial `data/` README aligned to KFM directory + pipeline contracts.
