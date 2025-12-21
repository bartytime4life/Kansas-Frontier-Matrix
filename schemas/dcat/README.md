---
title: "KFM Schemas — DCAT"
path: "schemas/dcat/README.md"
version: "v1.0.0"
last_updated: "2025-12-21"
status: "draft"
doc_kind: "Reference"
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

doc_uuid: "urn:kfm:doc:schemas:dcat:readme:v1.0.0"
semantic_document_id: "kfm-schemas-dcat-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:schemas:dcat:readme:v1.0.0"
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

# KFM Schemas — DCAT (`schemas/dcat/`)

## 📘 Overview

### Purpose
This README defines what belongs in `schemas/dcat/` and how DCAT-related **contract artifacts** (schemas / shapes / constraints) are organized so that DCAT outputs can be **machine-validated** in CI.

This directory governs the *validation layer* for DCAT artifacts produced in the catalog stage (see `data/catalog/dcat/`).

### Scope

| In Scope | Out of Scope |
|---|---|
| DCAT constraints, schema files, shape bundles, validation guidance | Generating DCAT outputs (pipeline code) |
| How DCAT outputs relate to STAC/PROV/Graph/API boundaries | Full DCAT profile specification text (lives under `docs/standards/`) |
| Naming/versioning conventions for schemas in this folder | Editing datasets or distributions themselves (belongs under `data/…`) |

### Audience
- Primary: catalog maintainers, schema/contract owners
- Secondary: ETL maintainers, graph/API maintainers, governance reviewers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used here:
  - **DCAT**: W3C Data Catalog Vocabulary representation for dataset-level metadata.
  - **Contract artifact**: machine-validated schema/spec used as a CI gate.
  - **Evidence artifact**: generated catalog outputs (e.g., DCAT datasets) consumed downstream.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Schemas root README | `schemas/README.md` | Contracts owners | Top-level schema conventions |
| DCAT schema folder | `schemas/dcat/` | Catalog/contracts owners | This directory |
| DCAT outputs | `data/catalog/dcat/` | Catalog maintainers | Generated evidence artifacts (not schemas) |
| DCAT profile | `docs/standards/KFM_DCAT_PROFILE.md` | Standards owners | Expected canonical spec (verify presence in repo) |
| Master Guide | `docs/MASTER_GUIDE_v12.md` | Core maintainers | Canonical pipeline + invariants |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (`path` matches file location)
- [ ] Clear separation: **schemas** (`schemas/dcat/`) vs **outputs** (`data/catalog/dcat/`)
- [ ] Validation expectations listed (what CI should validate, at minimum)
- [ ] Governance + CARE/sovereignty considerations explicitly stated
- [ ] Links to canonical standards/docs are present

---

## 🗂️ Directory Layout

### This document
- `path`: `schemas/dcat/README.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Schemas root | `schemas/` | Contract artifacts for validation |
| DCAT outputs | `data/catalog/dcat/` | Generated DCAT evidence artifacts |
| STAC outputs | `data/stac/` | STAC collections + items |
| PROV outputs | `data/prov/` | Lineage bundles / run provenance |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| API contracts | `src/server/contracts/` | API contract schemas/specs (not DCAT) |
| Governed docs | `docs/` | Canonical standards, ADRs, guides |

### Expected (or recommended) layout under `schemas/dcat/`
This folder may begin with only `README.md`. Add subfolders only when there is a concrete validation need.

~~~text
📁 schemas/
├── 📁 dcat/
│   ├── 📄 README.md
│   ├── 📁 jsonschema/        # Optional: JSON Schema contracts for DCAT JSON(-LD) renderings
│   ├── 📁 shacl/             # Optional: SHACL shapes for RDF/JSON-LD validation
│   ├── 📁 examples/          # Optional: minimal valid/invalid fixtures for tests
│   └── 📄 CHANGELOG.md       # Recommended when schemas stabilize
└── …
~~~

---

## 🧭 Context

### Where DCAT fits in the canonical pipeline
DCAT artifacts are part of the **catalog layer** that sits between ETL outputs and the graph/API/UI layers.

Key invariants to keep in mind:
- The UI must not read Neo4j directly; it consumes contracted payloads via the API layer.
- Schemas/specs belong under `schemas/` and must validate in CI.
- Generated outputs belong under `data/…` (not under `src/` and not written into `docs/`).  

(See the Master Guide and v13 blueprint for the non-negotiable ordering and contract-first posture.)

### What goes where (hard boundary)
- ✅ `schemas/dcat/**`: machine-validatable **contracts** for DCAT artifacts
- ✅ `data/catalog/dcat/**`: generated **DCAT evidence artifacts** (JSON-LD or other agreed serialization)
- ✅ `docs/standards/**`: human-readable, governed **profile documents**
- ✅ `src/pipelines/**`: code that produces catalog outputs
- ❌ Do not place generated DCAT outputs in `docs/`

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL outputs<br/>data/&lt;domain&gt;/processed] --> B[Catalog build<br/>src/pipelines]
  B --> C[DCAT outputs<br/>data/catalog/dcat]
  C --> D[Schema validation<br/>schemas/dcat]
  D --> E[Downstream consumers<br/>Graph/API/UI/Export]
~~~

---

## 📦 Data & Metadata

### Inputs to DCAT generation (context only)
Typical inputs to DCAT generation include processed datasets and mapping notes:
- `data/<domain>/processed/` (derived datasets)
- `data/<domain>/mappings/` (optional mapping docs: dataset → STAC/DCAT/PROV)

### Outputs validated by these schemas
- `data/catalog/dcat/` should contain DCAT dataset records (and any related catalog documents) emitted by the catalog stage.

### Sensitivity + governance reminder
Even metadata can be sensitive if it:
- links to restricted distributions,
- encodes precise spatial/temporal coverage that should be generalized,
- reveals culturally sensitive locations or communities.

When in doubt, treat fields as sensitive until governance review clears them.

---

## 🌐 STAC, DCAT & PROV Alignment

DCAT schema constraints should support linkage across KFM’s evidence layer:
- **STAC**: asset-level catalogs (items/collections)
- **DCAT**: dataset-level catalog records
- **PROV**: lineage for runs, derivations, and transformations

Recommended linkage targets (contract-level expectations):
- DCAT dataset identifiers should be stable and reusable as references in:
  - PROV bundles (as Entities)
  - Graph nodes (as external IDs / evidence references)
  - API responses (as provenance/evidence pointers)

---

## 🧱 Architecture

### Contract boundaries (non-negotiable)
- `schemas/dcat/` defines **what “valid DCAT output” means** for KFM.
- `src/server/contracts/` defines **what “valid API payload” means** for KFM.
- The UI consumes **API contracts**, not schemas directly.

### What belongs in this folder (practical guidance)
Add a schema/shape when one of these is true:
- DCAT outputs are now part of CI, and we need deterministic pass/fail checks.
- A field becomes required/forbidden by KFM governance.
- A downstream consumer (graph ingest, API export, UI) depends on a stable DCAT structure.

---

## 🧠 Story Node & Focus Mode Integration

Story Nodes should cite *evidence artifacts*, not freeform claims. DCAT dataset records can serve as:
- dataset-level evidence references for Story Nodes, and/or
- provenance anchors that tie narrative claims to governed datasets and distributions.

Any narrative usage still requires:
- provenance-linked evidence
- validation gates appropriate to published content

---

## 🧪 Validation & CI/CD

### Minimum expectations
At minimum, CI should be able to:
- discover schema artifacts under `schemas/dcat/`,
- validate DCAT outputs under `data/catalog/dcat/` against them,
- fail deterministically on invalid artifacts.

### Validator implementation
The specific validator tooling (JSON Schema vs SHACL) is **repo-dependent**.
- If DCAT outputs are JSON(-LD) with a constrained shape, JSON Schema may be sufficient.
- If DCAT outputs are treated as RDF graphs, SHACL shape validation may be required.

~~~bash
# Example only (replace with repo-specific commands):
# 1) Build / generate DCAT outputs
# 2) Validate outputs in data/catalog/dcat/ using schemas in schemas/dcat/
~~~

---

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that require governance review:
- adding/removing required fields affecting attribution, licensing, provenance, or distributions
- altering handling of sensitive coverage fields (spatial/temporal/community)
- introducing new distribution link patterns that expose restricted assets

### CARE / sovereignty considerations
If DCAT records describe Indigenous or culturally sensitive resources:
- ensure sovereignty policy requirements are met
- generalize or omit sensitive geographies where required
- document the governance decision in an ADR or review gate record

### AI usage constraints
This document’s AI permissions/prohibitions in front-matter must remain aligned with:
- no generation of new policy (human-governed)
- no inference of sensitive locations

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-21 | Initial DCAT schemas README | TBD |

---

Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

