---
title: "Contributing to Kansas Frontier Matrix"
path: "CONTRIBUTING.md"
version: "v1.0.0"
last_updated: "2025-12-18"
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

doc_uuid: "urn:kfm:doc:repo:contributing:v1.0.0"
semantic_document_id: "kfm-repo-contributing-v1.0.0"
event_source_id: "ledger:kfm:doc:repo:contributing:v1.0.0"
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

# Contributing to Kansas Frontier Matrix

## 📘 Overview

### Purpose
- This guide defines how to contribute **code, data, metadata, and narrative artifacts** to Kansas Frontier Matrix (KFM).
- The goal is to keep contributions **reproducible**, **governed**, and **traceable** through catalogs (STAC/DCAT/PROV), graph semantics, and API/UI contracts.

### Scope

| In Scope | Out of Scope |
|---|---|
| PR workflow, contribution types, metadata/provenance expectations, governance + sensitivity handling | Publishing secrets, bypassing governance review, adding undocumented “black box” steps |

### Audience
- Primary: Contributors opening PRs (data, graph, API, UI, docs)
- Secondary: Reviewers (governance, sovereignty/ethics, security)

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: **ETL**, **STAC**, **DCAT**, **PROV-O**, **Neo4j**, **Contract**, **Story Node**, **Focus Mode**

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (source of truth) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline order + subsystem inventory |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Required for governed Markdown |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Narrative maintainers | Required for Focus Mode story nodes |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API maintainers | Required for REST/GraphQL contract changes |
| Security policy | `.github/SECURITY.md` | Security reviewers | Vulnerability reporting + standards |

### Definition of done (for a contribution / PR)
- [ ] Front-matter complete (for any governed Markdown introduced/changed)
- [ ] Provenance is maintained (STAC/DCAT/PROV identifiers and lineage are updated as applicable)
- [ ] Validation steps are repeatable (containerized workflow preferred)
- [ ] Governance + CARE/sovereignty considerations are explicitly stated for sensitive content
- [ ] UI does not directly couple to the graph (API boundary preserved)

## 🗂️ Directory Layout

### This document
- `path`: `CONTRIBUTING.md`

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data | `data/` | Raw/work/processed datasets; STAC outputs |
| Catalogs | `data/stac/` | STAC Collections/Items |
| Docs | `docs/` | Master guide, governance, subsystem docs |
| Templates | `docs/templates/` | Universal / Story Node / API Contract templates |
| Pipelines | `src/pipelines/` | ETL + transforms + catalog build |
| Graph | `src/graph/` | Ontology bindings, graph build, migrations |
| APIs | `src/server/` | REST/GraphQL contracts + access layer |
| Frontend | `web/` | React/MapLibre UI |
| Schemas | `schemas/` | JSON schemas and validators |
| Tests | `tests/` | Code + data contract tests |
| Tooling | `tools/` | Validation/lint/release helpers |
| MCP runs | `mcp/runs/` | Run logs, experiment records |

### Expected file tree for this sub-area

~~~text
🌳 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 🤝 CONTRIBUTING.md
├── 📁 .github/
│   ├── 🔒 SECURITY.md
│   └── ⚙️ workflows/
├── 📁 data/
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   └── 📁 stac/
├── 📁 docs/
│   ├── 📄 MASTER_GUIDE_v12.md
│   ├── 📁 governance/
│   ├── 📁 templates/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 reports/
│       └── 📁 story_nodes/
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/
├── 🧪 tests/
└── 🗺️ web/
~~~

## 🧭 Context

### Background
KFM is designed to be a scientific-grade historical atlas: maps, narratives, and “insights” must be traceable to evidence and reproducible processing steps.

### Assumptions
- The recommended dev workflow is containerized (Docker; optional Compose).
- CI runs tests and checks on commits/PRs (metadata validation, build checks, linting).
- Contributions may require domain review (historical accuracy, cultural sensitivity, sovereignty).

### Constraints / invariants
- **Canonical ordering is preserved:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **Frontend consumes contracts via APIs** (no direct graph dependency).
- If your change adds/edits an API: use the API Contract Extension template and include contract tests.

### Open questions

| Question | Owner | Target date |
|---|---|---|
| What are the exact local PR check commands (Make targets / Compose services) in this repo? | TBD | TBD |
| Where are the canonical schema validators invoked from (tools/ scripts)? | TBD | TBD |

### Future extensions
- New datasets and derived evidence products should follow the “extension matrix” pattern (data → catalogs → graph → API → UI → story/focus → telemetry).

## 🗺️ Diagrams

### Contribution flow (conceptual)

~~~mermaid
flowchart LR
  A[Issue / Proposal] --> B[Branch + Implement]
  B --> C[Update STAC/DCAT/PROV + Schemas]
  C --> D[Run checks (containerized)]
  D --> E[Pull Request]
  E --> F[Review (engineering + governance)]
  F --> G[Merge]
  G --> H[CI/CD build + publish artifacts]
~~~

## 📦 Data & Metadata

### Contribution types
- **Data ingestion / new dataset**: add ETL steps + metadata + provenance.
- **Catalog improvements**: STAC/DCAT/PROV enhancements, mappings, validators.
- **Graph changes**: ontology bindings, migrations, derived relationships.
- **API changes**: REST/GraphQL endpoints and contract updates.
- **UI changes**: map layers, Focus Mode UX, accessibility.
- **Story Nodes**: evidence-led narrative artifacts.

### Local workflow (containerized)
If the repo includes Compose and/or Make targets, a typical workflow aligns with:

~~~bash
# Run the stack (if compose exists)
docker compose up

# Regenerate outputs (if make targets exist)
make all
~~~

If the above commands do not exist in your checkout, locate the repo’s actual entry points (Compose file names, Makefile targets, scripts under `tools/`) and update this guide accordingly.

### Adding a dataset (minimum expectations)
1. **Source + license**
   - Document the dataset source and license compatibility.
   - If the license is unclear or incompatible, do not ingest until resolved.

2. **Place raw/work/processed outputs correctly**
   - Raw downloads and snapshots belong under `data/raw/` (or equivalent domain subfolders).
   - Intermediate artifacts belong under `data/work/`.
   - Derived outputs belong under `data/processed/`.
   - Large binary data should use the repo’s large-file strategy (e.g., DVC if configured) rather than bloating Git history.

3. **Update catalogs**
   - Add/modify STAC Collections/Items under `data/stac/`.
   - Add/update DCAT dataset views (location varies; follow repo conventions).
   - Capture provenance events/runs (PROV artifacts; run IDs; links to inputs/outputs).

4. **Update pipeline code**
   - ETL/transforms belong under `src/pipelines/`.
   - Ensure deterministic behavior where possible (fixed seeds for stochastic steps; pinned versions in container builds).

5. **Add tests / validation**
   - Add or extend tests so CI can validate:
     - metadata file validity (JSON well-formedness)
     - link + license presence for catalog entries
     - sample output expectations (geospatial metadata / projection checks where applicable)

6. **Optional: Story Node**
   - If the dataset adds new interpretive narrative value, add a Story Node under `docs/reports/story_nodes/` using the Story Node template.

### Outputs (what a “complete” data PR usually produces)

| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| STAC updates | JSON | `data/stac/` | STAC core + KFM profile |
| Processed layer(s) | GeoJSON/GeoTIFF/etc. | `data/processed/` | Layer/schema contract |
| Provenance record | RDF/JSON-LD/etc. | `mcp/runs/` or `docs/prov/` | KFM PROV profile |
| Tests updated | code | `tests/` | CI gates |

### Sensitivity & redaction
- If your contribution includes sensitive locations or culturally restricted knowledge:
  - Describe required generalization/redaction.
  - Flag required reviewers (sovereignty/ethics) and avoid publishing exact coordinates or restricted details in public outputs.

### Quality signals
- Metadata passes schema validation.
- Geospatial artifacts load and validate (geometry + CRS sanity checks).
- Provenance links resolve (inputs → activity/run → outputs).
- UI remains fast and stable (build succeeds; no runtime errors introduced).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Every new asset intended for discovery should have a corresponding STAC Item/Collection entry.
- Keep validator versions pinned and repeatable.

### DCAT
- Ensure dataset identifiers, license mapping, and publisher/contact metadata are present.
- Align dataset-level descriptions with what is actually ingested and exposed.

### PROV-O
- Use PROV relations (`prov:wasDerivedFrom`, `prov:wasGeneratedBy`) to preserve lineage.
- Record run identifiers and, when relevant, environment provenance (container tag/digest).

### Versioning
- If your change is contract-affecting (schemas, APIs, catalogs), document the version impact and any migration notes.

## ✅ PR checklist (copy/paste into your PR description)

- [ ] I preserved the canonical pipeline ordering.
- [ ] I updated STAC/DCAT/PROV metadata where applicable.
- [ ] I included provenance/run references (IDs, paths, or logs).
- [ ] I ran the repo’s checks locally (or described why not possible).
- [ ] I flagged any sensitivity/sovereignty concerns and requested appropriate reviewers.
- [ ] I did not add secrets, credentials, or private data.

---