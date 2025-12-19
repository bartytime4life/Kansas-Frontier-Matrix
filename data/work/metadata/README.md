---
title: "KFM Data Work — Metadata README"
path: "data/work/metadata/README.md"
version: "v1.0.0"
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

doc_uuid: "urn:kfm:doc:data:work:metadata-readme:v1.0.0"
semantic_document_id: "kfm-data-work-metadata-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:work:metadata-readme:v1.0.0"
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

# KFM Data Work — Metadata

## 📘 Overview

### Purpose
This directory holds **intermediate metadata artifacts** produced during KFM’s **work-stage** processing. It exists to support repeatable ETL normalization and later catalog creation (STAC/DCAT/PROV) without treating drafts as authoritative outputs.

### Scope

| In Scope | Out of Scope |
|---|---|
| Draft metadata extracted from sources (e.g., header parsing, field detection) | Source files themselves (belongs in `data/raw/` or domain-specific source folders) |
| Schema inference outputs and column dictionaries/codebooks | Final processed datasets (belongs in `data/processed/`) |
| Validation reports (completeness, geometry validity, field ranges) | Final catalog outputs (belongs in `data/stac/`, `data/catalog/dcat/`, `data/prov/`) |
| Draft mappings used to build STAC/DCAT/PROV (non-authoritative) | Secrets/credentials/tokens; any private keys |
| Deterministic run-level manifests/hashes for intermediate steps | PII or sensitive location details that violate governance/sovereignty rules |

### Audience
- Primary: ETL/pipeline maintainers, data curators
- Secondary: Graph/API implementers who need provenance references, reviewers validating data lineage

### Definitions (link to glossary)
- Link: `docs/glossary.md` (**not confirmed in repo**)
- Terms used in this doc: ETL, STAC, DCAT, PROV, manifest, schema inference, redaction

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Metadata work area | `data/work/metadata/` | DataOps | Intermediate metadata only |
| Final STAC outputs | `data/stac/` | Catalog build | Authoritative spatiotemporal catalog |
| Final DCAT outputs | `data/catalog/dcat/` | Catalog build | Authoritative dataset catalog views |
| Final PROV outputs | `data/prov/` | Catalog build | Authoritative lineage bundles |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Directory purpose and “do not place here” rules are explicit
- [ ] Links to authoritative catalog locations are present
- [ ] Validation guidance is listed and repeatable

## 🗂️ Directory Layout

### This document
- `path`: `data/work/metadata/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Raw sources | `data/raw/` | Unmodified ingested sources (governed) |
| Work staging | `data/work/staging/` | Working copies and pre-normalization intermediates |
| Work spatial | `data/work/spatial/` | Intermediate spatial transforms (reprojection, clipping) |
| Work tables | `data/work/tables/` | Intermediate tabular transforms (cleaning, joins) |
| Work processed | `data/work/processed/` | Intermediate processed outputs prior to promotion |
| Processed | `data/processed/` | Curated, versioned processed datasets |
| STAC | `data/stac/` | Authoritative STAC collections/items/assets |
| DCAT | `data/catalog/dcat/` | Authoritative DCAT dataset views |
| PROV | `data/prov/` | Authoritative provenance bundles |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 work/
    └── 📁 metadata/
        ├── 📄 README.md
        ├── 📁 runs/                       # recommended: per-run, deterministic work manifests
        │   └── 📁 <run_id>/
        │       ├── 📄 manifest.json        # inputs/outputs + hashes + timestamps
        │       ├── 📄 validation.json      # checks + warnings (non-authoritative)
        │       └── 📄 mappings.json        # draft field mappings to downstream schemas
        ├── 📁 datasets/                    # recommended: per-dataset metadata workspace
        │   └── 📁 <dataset_id>/
        │       ├── 📁 schema_inference/
        │       ├── 📁 codebooks/
        │       ├── 📁 stac_drafts/         # drafts only; final goes to data/stac/
        │       ├── 📁 dcat_drafts/         # drafts only; final goes to data/catalog/dcat/
        │       └── 📁 prov_drafts/         # drafts only; final goes to data/prov/
        └── 📁 tmp/                         # optional: safe-to-delete scratch (gitignored recommended)
~~~

## 🧭 Context

### Background
KFM’s canonical ordering requires intermediate work to be separated from authoritative catalog and graph products. The `data/work/metadata/` area provides a structured place to keep “how we got here” artifacts (schemas, manifests, validation results) during ETL and catalog assembly.

### Assumptions
- ETL outputs are deterministic and replayable.
- Catalog generation (STAC/DCAT/PROV) promotes vetted artifacts out of `data/work/` into their canonical locations.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- This directory is **not** an authoritative catalog location.
- Frontend/UI must not read work artifacts directly; it consumes contracted outputs via API + catalogs.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Should `data/work/metadata/tmp/` be gitignored by default? | TBD | TBD |
| What is the canonical `run_id` format for work-stage manifests? | TBD | TBD |

### Future extensions
- Add schema lint outputs (JSON Schema / STAC validation) as structured artifacts.
- Add per-dataset “data dictionary” exports for UI audit panels (served via API, not from `data/work/`).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Raw sources] --> B[ETL + normalization]
  B --> C[data/work/metadata (drafts + manifests)]
  C --> D[STAC/DCAT/PROV catalogs]
  D --> E[Neo4j graph]
  E --> F[APIs]
  F --> G[UI + Story Nodes + Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Extracted source metadata | JSON/YAML | ETL extraction step | Required fields + hash check |
| Inferred schema hints | JSON | Profiling step | Consistency + type checks |
| Validation results | JSON | QA step | Must include severity + rule id |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Work manifests | JSON | `data/work/metadata/runs/<run_id>/manifest.json` | Repo-defined (not confirmed) |
| Draft catalog fragments | JSON/JSON-LD | `.../stac_drafts/`, `.../dcat_drafts/`, `.../prov_drafts/` | Must validate before promotion |
| Data dictionaries | CSV/JSON | `.../codebooks/` | Repo-defined (not confirmed) |

### Sensitivity & redaction
- Do not store secrets or credentials.
- Avoid embedding personally identifying information or sensitive locations in intermediate metadata.
- If sensitive content is unavoidable for processing, store only generalized values and keep restricted details in governed, access-controlled locations (**not confirmed in repo**).

### Quality signals
- Hashes for inputs/outputs in manifests
- Validation severity levels (error/warn/info)
- Counts and summaries (null rates, geometry validity counts)

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Draft STAC fragments may be staged here, but **final** STAC Items/Collections must live under `data/stac/`.

### DCAT
- Draft DCAT mappings may be staged here, but **final** DCAT records must live under `data/catalog/dcat/`.

### PROV-O
- Draft lineage bundles may be staged here, but **final** PROV bundles must live under `data/prov/`.

### Versioning
- Work artifacts should be treated as ephemeral unless explicitly promoted.
- Promotion should be linked to a run identifier and include predecessor/successor links where applicable.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | Extract + normalize + emit work metadata | Config + run logs |
| Catalogs | Validate + publish STAC/DCAT/PROV | JSON/JSON-LD outputs |
| Graph | Ingest catalog-linked entities | API layer (no direct UI access) |
| APIs | Serve contracted access to catalogs/graph | REST/GraphQL |
| UI | Render maps/narratives from API outputs | API calls only |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Work manifests | `data/work/metadata/runs/` | Semver if standardized (not confirmed) |
| Catalog schemas | `schemas/` | Semver + changelog (not confirmed) |

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Work metadata does **not** surface directly.
- Only provenance-linked, validated catalog/graph artifacts should be eligible for Story Nodes and Focus Mode.

### Provenance-linked narrative rule
- Any narrative or UI-visible claim must trace to authoritative dataset/catalog IDs, not work drafts.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Work manifests present for each run directory
- [ ] Draft STAC/DCAT/PROV fragments validate before promotion
- [ ] No secrets/PII present in work metadata
- [ ] No authoritative catalog outputs are stored under `data/work/metadata/`

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) run ETL for a dataset
# 2) generate draft metadata + manifests
# 3) validate STAC/DCAT/PROV fragments
# 4) promote validated outputs into canonical catalog directories
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Validation summary | QA step | `data/work/metadata/runs/<run_id>/validation.json` |
| Promotion audit | Catalog build | `data/prov/` (authoritative) |

## ⚖ FAIR+CARE & Governance

### Review gates
- Metadata affecting public narrative outputs should be reviewed during promotion into catalog directories.
- Any sensitive content handling requires governance review per referenced governance docs.

### CARE / sovereignty considerations
- Ensure culturally sensitive sites/locations are not inferred or exposed through intermediate metadata.

### AI usage constraints
- AI may summarize or extract structure from these artifacts, but must not infer sensitive locations or invent policy.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for `data/work/metadata/` | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
