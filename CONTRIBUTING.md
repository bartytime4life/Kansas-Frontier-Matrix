---
title: "CONTRIBUTING — Kansas Frontier Matrix"
path: "CONTRIBUTING.md"
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

doc_uuid: "urn:kfm:doc:contributing:v1.0.0"
semantic_document_id: "kfm-contributing-v1.0.0"
event_source_id: "ledger:kfm:doc:contributing:v1.0.0"
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

# CONTRIBUTING — Kansas Frontier Matrix

## 📘 Overview

### Purpose
Kansas Frontier Matrix (KFM) is a governed geospatial + historical knowledge system. Contributions must preserve the canonical pipeline ordering and its contracts:

- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

This document describes how to contribute code, data, metadata, ontology/graph semantics, APIs, UI features, and Story Nodes in a way that remains reproducible, reviewable, and standards-compliant.

### Scope
| In scope | Out of scope |
|---|---|
| Bug fixes, features, refactors, docs | Sharing secrets/credentials, bypassing review gates |
| Data ingestion + processing updates | Uploading restricted/sensitive data without governance review |
| STAC/DCAT/PROV catalog updates | “UI talks directly to Neo4j” patterns |
| Graph ontology + migrations | Non-deterministic ETL that can’t be reproduced |
| API endpoints + contract updates | Large unreviewed dumps of raw data artifacts |
| React/Map UI improvements | Unsourced narrative in Focus Mode / Story contexts |

### Audience
- Contributors adding data, docs, code, or narratives.
- Maintainers/reviewers performing governance and CI reviews.
- Data partners who need to understand required metadata + provenance.

### Definitions
- **Master Guide:** `docs/MASTER_GUIDE_v12.md` (canonical pipeline + invariants)
- **STAC:** SpatioTemporal Asset Catalog (assets + Items/Collections)
- **DCAT:** Dataset catalog vocabulary (dataset-level inventory)
- **PROV-O:** W3C provenance model (lineage and reproducibility)
- **Story Node:** Governed narrative artifact tied to evidence IDs and graph/cat references
- **Focus Mode:** Narrative UX that must not contain unsourced claims

### Key artifacts (use these before inventing anything)
| Artifact | Path | Use when |
|---|---|---|
| Master guide | `docs/MASTER_GUIDE_v12.md` | Any change affecting pipeline, contracts, or repo structure |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Default for governed docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Any new/updated narrative node |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Any new endpoint/contract, versioning, or schema changes |
| Governance refs | `docs/governance/*` | Anything touching ethics, sovereignty, sensitivity, access controls |
| Schemas | `schemas/` | Any JSON-LD/JSON schema validation, telemetry, catalogs |

### Definition of done (for any contribution)
- [ ] Change is **scoped** (small PRs preferred; large changes justified and structured)
- [ ] Correct **repo placement** (data vs code vs docs)
- [ ] **Standards alignment** preserved: STAC 1.0 / DCAT 3 / PROV-O where applicable
- [ ] **API boundary** preserved: UI consumes via APIs (no direct graph access)
- [ ] All required **validation + CI** checks pass (see “Validation & CI/CD”)
- [ ] **No secrets / no PII leaks** / no sensitive-location inference
- [ ] Story/Narrative contributions include **evidence IDs** (fact vs inference vs hypothesis)

---

## 🗂️ Directory Layout

### This document
- File: `CONTRIBUTING.md`
- Role: repo-wide contribution protocol + checklists aligned to KFM invariants

### Related repository paths
| Area | Path | Notes |
|---|---|---|
| Data artifacts | `data/` | Raw/work/processed + catalogs + provenance |
| STAC | `data/stac/` | Collections + Items |
| DCAT | `data/catalog/dcat/` | Dataset catalog records |
| PROV | `data/prov/` | Lineage bundles for runs/updates |
| Pipelines | `src/pipelines/` | ETL + catalog generation |
| Graph | `src/graph/` | Neo4j build + ontology bindings |
| APIs | `src/api/` | Service layer (contracts live here) |
| Frontend | `web/` | React/Map client (no direct graph dependency) |
| Docs | `docs/` | Governed documentation and templates |
| Schemas | `schemas/` | Validation contracts for JSON artifacts |
| MCP | `mcp/` | Runs, experiments, model cards, SOPs |
| CI/Workflows | `.github/` | CI checks and security policies |

### Expected file tree for this sub-area
~~~text
📁 .github/
├── 📁 workflows/
├── 📄 SECURITY.md
│
📁 data/
├── 📁 sources/
├── 📁 raw/
├── 📁 work/
├── 📁 processed/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/
│
📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 standards/
└── 📁 architecture/
│
📁 mcp/
├── 📁 runs/
└── 📁 experiments/
│
📁 schemas/
📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 api/
│
📁 web/
│
📄 CONTRIBUTING.md
~~~

---

## 🧭 Context

### Background
KFM is designed to:
- retain raw sources and transformations,
- package outputs into open catalogs (STAC/DCAT/PROV),
- load semantic entities/relationships into a Neo4j graph,
- expose contracts via APIs,
- render map/timeline UI and narratives (Story Nodes + Focus Mode).

### Assumptions
- Contributions are made via pull requests (PRs) and reviewed.
- CI enforces linting, schema validation, and governance checks.
- Repository uses strict placement rules (data in `data/`, code in `src/`/`web/`, docs in `docs/`).

### Constraints / invariants
- **Pipeline ordering is non-negotiable:** ETL → Catalogs → Graph → APIs → UI → Story → Focus Mode.
- **API boundary is non-negotiable:** UI must not read Neo4j directly; contracts live at the API layer.
- **Determinism:** ETL must be idempotent and reproducible; seed-lock stochastic steps.
- **Provenance:** New/updated outputs must be traceable to sources and transformation activities.
- **Narratives:** No unsourced claims in Story Nodes / Focus Mode contexts; label inference/hypothesis.

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Do we require an issue before any PR? | Maintainers | TBD |
| Do we enforce a commit message convention? | Maintainers | TBD |
| What are the size thresholds for large data artifacts in git? | Maintainers | TBD |

### Future extensions
- Add new data domains (new ETL + catalogs + graph mappings + UI layers).
- Add evidence products (AI outputs) that are stored and audited like other artifacts.
- Expand narrative UX via new Story Node types and Focus Mode layouts.

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL] --> B[STAC/DCAT/PROV Catalogs]
  B --> C[Neo4j Graph]
  C --> D[APIs]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: contribution sequence diagram
~~~mermaid
sequenceDiagram
  participant Dev as Contributor
  participant CI as CI Gates
  participant Rev as Reviewer/Maintainer

  Dev->>Dev: Create branch + implement change
  Dev->>CI: Open PR (runs validation)
  CI-->>Dev: Report failures (lint/schema/tests)
  Dev->>CI: Push fixes (rerun CI)
  CI-->>Rev: Green build + artifacts ready
  Rev->>Dev: Review (contracts/governance/quality)
  Rev-->>Dev: Approve / request changes
  Rev->>Rev: Merge when DoD is met
~~~

---

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Source datasets | files/APIs | `data/sources/` manifests + external sources | licensing + checksum + schema checks |
| Raw data drops | many | `data/raw/` | immutability + basic integrity checks |
| Pipeline configs | YAML/JSON | `src/pipelines/` | lint + deterministic behavior |
| Narrative evidence refs | IDs/links | catalogs + graph | must resolve to governed artifacts |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed data | dataset-specific | `data/processed/` | domain schema / validation rules |
| STAC Items/Collections | JSON | `data/stac/items/` + `data/stac/collections/` | STAC profile + extension schema |
| DCAT Dataset records | TTL/JSON-LD | `data/catalog/dcat/` | DCAT profile |
| PROV bundles | JSON-LD (typical) | `data/prov/` | PROV profile |
| Graph mappings/migrations | code + docs | `src/graph/` + `docs/graph/` | ontology + migration tests |
| API contract docs | markdown + schemas | `docs/api/` + `schemas/` | API contract extension |
| UI layers/registry | JSON + code | `web/` (+ schemas) | layer registry schema |
| Story Nodes | markdown | `docs/story_nodes/` (or governed location) | Story Node template + evidence rules |

### Sensitivity & redaction
- Do not include secrets, tokens, or private keys.
- Do not publish personally identifying information unless governance explicitly allows it.
- For culturally sensitive content (including Indigenous materials), follow `docs/governance/SOVEREIGNTY.md` and label restrictions.
- Generalize/blur sensitive locations when required by governance.

### Quality signals
- Reproducibility: reruns produce identical outputs for same inputs.
- Completeness: required fields populated; consistent identifiers.
- Spatial validity: geometries valid; CRS standardized; extents correct.
- Catalog integrity: STAC Items ↔ Collections consistent; links not broken.
- Provenance: every major output has a lineage record.

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Add/modify **STAC Collections** when introducing a new dataset family.
- Add/modify **STAC Items** for each geospatial-temporal asset.
- Validate against the repo’s STAC profile and any extensions used.

### DCAT
- Create/update a **DCAT Dataset** record for each logical dataset series.
- Maintain consistent dataset identifiers and license/publisher mapping.

### PROV-O
- Record provenance for dataset creation and major updates:
  - `prov:Entity` for inputs/outputs
  - `prov:Activity` for pipeline runs/transforms
  - `prov:Agent` for software/maintainers where applicable
- Include stable IDs so provenance can be queried and audited.

### Versioning
- Use STAC versioning links where applicable.
- Use graph predecessor/successor relationships for entity evolution when applicable.
- Bump doc versions when changing contracts or contributor obligations.

---

## 🧱 Architecture & Contract Boundaries

### “No direct graph dependency” rule (UI)
- The UI must only consume **API contracts**.
- The graph is an internal implementation detail behind the API layer.

### Contribution types and what “done” means

#### Documentation
- Use governed templates under `docs/templates/`.
- Keep YAML frontmatter keys intact.
- Avoid broken links and undocumented new conventions.

#### Data / ETL
- Keep raw inputs immutable (no in-place edits under `data/raw/`).
- Make transformations deterministic and logged.
- Emit catalogs (STAC/DCAT) and provenance (PROV) when applicable.

#### Graph / Ontology
- Extend ontology before adding new labels/relationships.
- Provide migrations and integrity tests.
- Ensure stable identifiers and provenance pointers.

#### API / Contracts
- Add/extend endpoints at the API layer.
- Update contract docs + schemas together.
- Prefer backward-compatible changes; otherwise version explicitly.

#### UI (React/Map)
- Consume API responses; do not embed graph queries.
- Validate layer registries/configs via schema checks.
- Maintain accessibility and safe rendering practices.

#### Story Nodes / Focus Mode
- Use Story Node template for any new narrative.
- Every factual claim must map to evidence IDs (datasets/documents).
- Clearly label **fact vs inference vs hypothesis**.

---

## 🧪 Validation & CI/CD

CI is expected to enforce (at minimum) the following gate categories:
- Markdown protocol validation (frontmatter + template conformance)
- JSON schema validation (STAC/DCAT/telemetry and other governed schemas)
- Graph integrity tests (ontology constraints, migrations, relationships)
- API contract tests (schemas, backward compatibility rules)
- UI layer registry schema checks + basic a11y/lint checks
- Security + sovereignty scanning gates where applicable

Local runs:
- Use the repo’s documented scripts/commands for linting, schema validation, and tests.
- If you introduce a new schema or validation step, document how to run it locally.

---

## ⚖️ FAIR+CARE & Governance

- Treat FAIR (Findable, Accessible, Interoperable, Reusable) as a baseline for artifacts and metadata.
- Treat CARE (Collective Benefit, Authority to Control, Responsibility, Ethics) as a baseline for culturally sensitive content and sovereignty rules.
- Any change touching governance/policy, standards compliance, or sensitivity classification **requires human review**.

---

## 🧾 Version History
| Version | Date | Change | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-19 | Initial CONTRIBUTING.md aligned to Master Guide + governed templates | ChatGPT |
