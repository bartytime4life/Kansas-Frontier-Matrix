---
title: "KFM Data Updates — README"
path: "data/updates/README.md"
version: "v1.0.0"
last_updated: "2025-12-19"
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

doc_uuid: "urn:kfm:doc:data:updates:readme:v1.0.0"
semantic_document_id: "kfm-data-updates-readme-v1.0.0"
event_source_id: "ledger:kfm:doc:data:updates:readme:v1.0.0"
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

# data/updates

## 📘 Overview

### Purpose
`data/updates/` is the **staging + audit** area for *discrete, reviewable update bundles* that propose changes to KFM datasets and/or their derived catalogs.
It exists to make updates:
- **Atomic** (one update = one bundle),
- **Auditable** (who/what/why/when + checksums),
- **Replayable** (ETL consumes a manifest; catalogs/graph are regenerated deterministically).

This directory does **not** replace the canonical lifecycle paths (`data/raw/`, `data/work/`, `data/processed/`, `data/stac/`, `data/catalog/dcat/`, `data/prov/`).

### Scope
| In Scope | Out of Scope |
|---|---|
| Update bundle folders with manifest + inputs + review notes + checksums | Canonical raw/processed datasets (those live under `data/raw/` and `data/processed/`) |
| Change rationale + provenance pointers (issue/ticket IDs, source URLs/IDs, license notes) | Secrets/credentials, private keys, or PII dumps |
| Optional “candidate” catalog deltas for review (if used) | Serving content directly to the UI (UI must only consume via APIs) |

### Audience
- Primary: Data maintainers, ETL/pipeline maintainers, catalog/graph maintainers
- Secondary: Contributors proposing dataset changes, reviewers validating provenance + licensing

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc:
  - **Update bundle**: A directory containing a single proposed change set + manifest + checksums.
  - **update_id**: A stable identifier for the bundle used in logs/PROV.
  - **Run ID**: A pipeline execution identifier recorded in PROV (when available).
  - **Dataset ID**: Stable identifier used in DCAT (and mirrored in graph/API contracts).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Updates root README | `data/updates/README.md` | DataOps | This file |
| Update bundle folder | `data/updates/<update_bundle>/` | Contributor / Maintainer | Naming convention below |
| Update manifest | `data/updates/<update_bundle>/manifest.yaml` | Contributor | Schema TBD |
| Checksums | `data/updates/<update_bundle>/checksums/sha256sums.txt` | Contributor | Required for integrity |
| Review notes | `data/updates/<update_bundle>/notes/` | Reviewer | Human review trace |

### Definition of done (for this document)
- [ ] Front-matter complete + path matches
- [ ] Directory layout + naming convention documented
- [ ] Update bundle minimum required files specified
- [ ] Validation expectations listed (schema + provenance + checksums)
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `data/updates/README.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Update staging | `data/updates/` | Proposed change bundles + manifests + review notes |
| Raw ingestion | `data/raw/` | Canonical raw inputs (after acceptance) |
| Work/intermediate | `data/work/` | Temporary processing outputs |
| Processed outputs | `data/processed/` | Canonical derived datasets |
| STAC catalogs | `data/stac/` | STAC collections + items |
| DCAT catalogs | `data/catalog/dcat/` | DCAT dataset views |
| Provenance | `data/prov/` | PROV bundles for transforms/runs |
| Governing docs | `docs/` | Master guide, standards, templates |

### Expected file tree for this sub-area
~~~text
📁 data/
└── 📁 updates/
    ├── 📄 README.md
    ├── 📁 YYYY-MM-DD__<domain>__<source>__<update_slug>/
    │   ├── 📄 manifest.yaml
    │   ├── 📁 inputs/
    │   │   └── (new/changed source files, or pointers/metadata if too large)
    │   ├── 📁 notes/
    │   │   ├── 📄 CHANGELOG.md
    │   │   └── 📄 REVIEW_NOTES.md
    │   └── 📁 checksums/
    │       └── 📄 sha256sums.txt
    └── 📁 YYYY-MM-DD__<domain>__<source>__<update_slug>/
        └── (repeat per update bundle)
~~~

## 🧭 Context

### Background
KFM is designed to evolve as new sources arrive and existing datasets are corrected or enriched.
To keep the system reproducible and governed, updates should enter the pipeline as explicit, reviewable bundles that can be validated and linked to provenance outputs.

### Assumptions
- Update bundles are intended to be consumed by an ETL/config runner that is **deterministic** and **idempotent**.
- Catalog outputs (STAC/DCAT/PROV) remain the canonical machine-validated “truth” for downstream graph + API + UI.
- Repo-specific commands and manifest schema may exist elsewhere; this README documents a minimal convention.

### Constraints / invariants
- Canonical ordering is preserved: **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs (no direct graph dependency).
- Do not commit secrets/credentials; do not include sensitive locations unless redaction/generalization rules are defined.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical `manifest.yaml` schema? | TBD | TBD |
| Are “candidate catalog deltas” allowed in update bundles, or should catalogs only live in `data/stac/`, `data/catalog/dcat/`, `data/prov/`? | TBD | TBD |
| What is the repo’s standard update naming convention (date + domain + slug vs UUID)? | TBD | TBD |

### Future extensions
- Add `schemas/updates/update_manifest.schema.json` + CI validator.
- Add a GitHub Action workflow to validate checksums + manifest schema on PR.
- Add a PROV “update activity” profile to standardize run identifiers and agents.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  U[Update bundle in data/updates/] --> E[ETL + Normalization]
  E --> R[data/raw + data/work + data/processed]
  R --> C[STAC/DCAT/PROV catalogs]
  C --> G[Neo4j Graph]
  G --> A[API Layer]
  A --> UI[React/Map UI]
  UI --> SN[Story Nodes]
  SN --> FM[Focus Mode]
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Update manifest | YAML | `data/updates/<bundle>/manifest.yaml` | Schema validation (TBD) |
| Update payload | Files / pointers | `data/updates/<bundle>/inputs/` | Checksums + basic format checks |
| Review notes | Markdown | `data/updates/<bundle>/notes/` | Markdown lint (if enforced) |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Canonical raw inputs (post-acceptance) | mixed | `data/raw/<domain>/...` | Domain-specific |
| Canonical derived outputs | mixed | `data/processed/<domain>/...` | Domain-specific |
| STAC items/collections | JSON | `data/stac/...` | STAC 1.0 + profile |
| DCAT datasets | RDF/JSON-LD/Turtle | `data/catalog/dcat/...` | DCAT 3 + profile |
| PROV lineage bundles | RDF/JSON-LD | `data/prov/...` | PROV-O + profile |

### Sensitivity & redaction
- If an update introduces or modifies sensitive content, the update bundle MUST:
  - mark sensitivity in the manifest (field name TBD),
  - include redaction/generalization guidance in `notes/REVIEW_NOTES.md`,
  - avoid committing restricted coordinates or personal identifiers unless explicitly governed.

### Quality signals
- Presence of `sha256sums.txt` for all payload files.
- Manifest includes source attribution + license notes.
- Geometry validity checks for geospatial data (if applicable).
- Record count/range checks for tabular datasets (if applicable).

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- If the update changes spatiotemporal assets, the resulting catalog artifacts belong in:
  - `data/stac/collections/`
  - `data/stac/items/`
- Update bundles SHOULD reference intended STAC IDs in the manifest (field TBD).
- Versioning: prefer predecessor/successor linking in STAC and mirror lineage in graph.

### DCAT
- Update bundles SHOULD reference the target dataset identifier(s) used in DCAT.
- License, publisher, and distribution links should be tracked in the catalog layer, not ad-hoc in the UI.

### PROV-O
- Each accepted update SHOULD result in a PROV activity record (bundle/run) that captures:
  - `prov:wasDerivedFrom` (source IDs, prior dataset versions),
  - `prov:wasGeneratedBy` (pipeline run activity ID),
  - agent attribution (human + pipeline).

### Versioning
- Treat updates as creating a new version of a dataset/artifact when semantics change.
- Keep stable IDs; use successor/predecessor relationships for lineage.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| Update bundle | Staged change proposal | `manifest.yaml` + payload + checksums |
| ETL | Ingest + normalize + validate | Config-driven runner (TBD) |
| Catalogs | STAC/DCAT/PROV generation | JSON/RDF artifacts + validators |
| Graph | Semantic integration | Neo4j build (via pipeline) |
| APIs | Contracted access | REST/GraphQL |
| UI | Map + narrative UX | API calls only |
| Story Nodes | Provenance-linked narrative | docs + graph linkage |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| Update manifest schema | `schemas/updates/` (proposed) | Semver + changelog |
| STAC schemas | `data/stac/` | Profile versioning |
| DCAT schemas | `data/catalog/dcat/` | Profile versioning |
| PROV bundles | `data/prov/` | Profile versioning |

### Extension points checklist (for future work)
- [ ] Add update manifest schema + validator
- [ ] Add checksum verification in CI
- [ ] Add automated “promote update bundle → data/raw” workflow (if desired)
- [ ] Add PROV run linkage for every accepted update
- [ ] Add catalog diff reporting for reviewers

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
If an update bundle introduces new narrative content, it must be placed under the governed docs area and follow the Story Node template. The UI should only render it when the API provides provenance-linked context bundles.

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset ID.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Checksums present and verifiable for bundle payload
- [ ] Manifest schema validation (when schema is defined)
- [ ] Schema validation for any changed STAC/DCAT/PROV artifacts (if included/modified)
- [ ] Markdown lint for notes (if CI enforces)
- [ ] Governance + sovereignty review triggers assessed

### Reproduction
~~~bash
# Repo-specific commands are not defined here.
# Suggested pattern:
# 1) validate the update bundle manifest + checksums
# 2) run ETL for the referenced domain/source
# 3) regenerate STAC/DCAT/PROV and validate schemas
# 4) rebuild graph + run tests
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| update_id | manifest | `data/prov/` (via run activity), or `mcp/runs/` |
| file hash coverage | checksums | CI logs |

## ⚖ FAIR+CARE & Governance

### Review gates
- New external sources or license changes: requires human review.
- New sensitive layers/locations: requires sovereignty + ethics review.
- New public-facing API endpoints: requires contract + security review.

### CARE / sovereignty considerations
- Respect community-defined handling rules for culturally sensitive locations and narratives.
- Do not infer or add precise sensitive locations through AI transforms.

### AI usage constraints
- AI transforms allowed for this doc: summarize, structure extract, translate, keyword index.
- Prohibited: generating new policy or inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial README for update bundle staging | TBD |

---
Footer refs:
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`