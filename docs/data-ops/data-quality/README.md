---
title: "DataOps — Data Quality"
path: "docs/data-ops/data-quality/README.md"
version: "v0.1.0"
last_updated: "2025-12-20"
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

doc_uuid: "urn:kfm:doc:data-ops:data-quality:readme:v0.1.0"
semantic_document_id: "kfm-data-ops-data-quality-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:data-ops:data-quality:readme:v0.1.0"
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

# DataOps — Data Quality

## 📘 Overview

### Purpose
This document defines **data quality expectations** and **validation gates** for Kansas Frontier Matrix (KFM)
data products across the canonical pipeline (ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode).
It is the entry point for DataOps contributors implementing or reviewing data quality checks.

### Scope
| In Scope | Out of Scope |
|---|---|
| Dataset/asset validation rules and quality gates by pipeline stage | Runtime infrastructure observability not tied to dataset correctness (e.g., CPU/memory dashboards) |
| Schema checks (STAC/DCAT/PROV + internal JSON schemas) | Editorial/historical interpretation beyond provenance/citation requirements |
| Geospatial validity checks (CRS/geometry/bbox/time range) | UI design details (tracked under UI/design docs) |
| Provenance completeness (PROV lineage + source IDs) | Security policy authoring (tracked under governance/security docs) |
| Quality reporting conventions (what to log, what to block on) | Tool-specific implementation details unless standardized in repo |

### Audience
- Primary: DataOps / ETL maintainers, catalog maintainers, graph ingest maintainers
- Secondary: API maintainers, UI maintainers, reviewers doing release readiness checks

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc:
  - **Quality gate**: A blocking validation step that must pass before progressing to the next pipeline stage.
  - **Validation**: Deterministic checks that produce pass/fail (and structured diagnostics).
  - **Quality signal**: Quantitative measurement (counts, rates, summaries) used to detect drift or defects.
  - **Run ID**: Identifier for a deterministic pipeline execution used in PROV lineage and run logs.
  - **Asset**: A data artifact tracked in catalogs (e.g., STAC Item assets, datasets referenced by DCAT).

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline invariants) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline ordering and “do-not-break” rules |
| Universal governed doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Required structure for docs in this repo |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Story/UX | For provenance-linked narrative artifacts |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | For new/changed endpoints that surface quality/audit data |
| Catalog outputs | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | DataOps | Machine-validated metadata + lineage bundles |
| Schema registry | `schemas/` | DataOps | JSON Schemas and validation contracts |
| Run artifacts (preferred) | `mcp/runs/` | DataOps | Run logs / reports / experiment artifacts |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Quality gates defined per pipeline stage (ETL, Catalog, Graph, API/UI consumption)
- [ ] Checks are deterministic, reproducible, and produce actionable diagnostics
- [ ] Sensitivity/sovereignty constraints are explicitly handled (no leakage in quality outputs)
- [ ] Validation steps are listed and repeatable
- [ ] Open questions are tracked with owners

## 🗂️ Directory Layout

### This document
- `path`: `docs/data-ops/data-quality/README.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac outputs (per domain) |
| STAC outputs | `data/stac/` | STAC Collections + Items |
| DCAT outputs | `data/catalog/dcat/` | DCAT dataset views/records |
| PROV outputs | `data/prov/` | Lineage bundles (activities, agents, entities) |
| Pipelines | `src/pipelines/` | ETL + catalog + transforms (implementation) |
| Graph | `src/graph/` | Graph build, ontology bindings, constraints |
| Schemas | `schemas/` | JSON Schemas + telemetry schemas |
| Tests | `tests/` | Unit/integration/contract tests |
| MCP run logs | `mcp/runs/` | Run artifacts and evidence products |

### Expected file tree for this sub-area
~~~text
📁 docs/
├── 📁 data-ops/
│   ├── 📄 README.md
│   └── 📁 data-quality/
│       ├── 📄 README.md
│       ├── 📁 checks/
│       │   └── 📄 README.md
│       ├── 📁 metrics/
│       │   └── 📄 README.md
│       └── 📁 runbooks/
│           └── 📄 README.md
~~~

## 🧭 Context

### Background
KFM’s value depends on **reliable, provenance-linked** assets that can be safely surfaced via APIs and UI,
including Focus Mode narratives. Data quality is enforced by:
1) deterministic ETL + normalization,
2) machine-validated catalogs (STAC/DCAT/PROV),
3) graph integrity constraints,
4) contract-tested APIs that do not leak sensitive data,
5) UI/Story consumption that requires provenance for every claim.

### Assumptions
- Pipeline execution is deterministic and idempotent where required.
- Validation is automated and runs in CI for changed artifacts wherever feasible.
- Data quality checks do not introduce new “truth”; they detect defects and block unsafe releases.

### Constraints / invariants
- **ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode** ordering is preserved.
- Frontend consumes data through **API contracts** (no direct graph access).
- Focus Mode narrative must be **provenance-linked** (no unsourced narrative).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What is the canonical location + schema for machine-readable quality reports per run? | TBD | TBD |
| Which schema validator(s) are standardized for STAC/DCAT/PROV and internal JSON schemas? | TBD | TBD |
| What is the minimal “v12-ready” quality gate set for new datasets? | TBD | TBD |
| Do we surface quality/audit flags via API to UI? If so, which contract? | TBD | TBD |

### Future extensions
- Extension point A: Standardize a **Quality Report schema** under `schemas/` and publish per run under `mcp/runs/<run_id>/...`.
- Extension point B: Add “quality summary” assets to STAC Items (as non-authoritative diagnostics) and link them in PROV.
- Extension point C: Add regression tests for known-bad geometry/metadata edge cases.

## 🗺️ Diagrams

### System / dataflow diagram (with quality gates)
~~~mermaid
flowchart LR
  A[Raw Sources] --> B[ETL + Normalization]
  B --> G1{Gate 1: Parse/Normalize}
  G1 --> C[STAC/DCAT/PROV Catalogs]
  C --> G2{Gate 2: Catalog Validation}
  G2 --> D[Neo4j Graph]
  D --> G3{Gate 3: Graph Integrity}
  G3 --> E[APIs]
  E --> G4{Gate 4: Contract + Redaction}
  G4 --> F[UI + Story Nodes]
  F --> G5{Gate 5: Provenance Required}
  G5 --> H[Focus Mode]
~~~

### Optional: sequence diagram (validation and publication)
~~~mermaid
sequenceDiagram
  participant ETL as ETL Runner
  participant VAL as Validator
  participant CAT as Catalogs (STAC/DCAT/PROV)
  participant GR as Graph Build
  participant API as API Layer

  ETL->>VAL: Validate raw → normalized artifacts
  VAL-->>ETL: Pass/fail + diagnostics
  ETL->>CAT: Write STAC/DCAT/PROV outputs
  CAT->>VAL: Validate catalogs + link integrity
  VAL-->>CAT: Pass/fail + diagnostics
  CAT->>GR: Graph ingest/build uses catalogs
  GR->>VAL: Graph constraints + provenance edges
  VAL-->>GR: Pass/fail + diagnostics
  GR->>API: Publish contracted access
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Raw sources | PDF/CSV/GeoJSON/Shapefile/GeoTIFF/etc. | `data/raw/` or controlled ingest | checksums + type detection + parse success |
| ETL configs | YAML/JSON | `src/pipelines/` | schema lint + deterministic run config |
| Schemas | JSON Schema | `schemas/` | schema lint + versioning rules |
| Governance refs | Markdown | `docs/governance/` | required links + review gates |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Normalized artifacts | domain-specific | `data/work/` → `data/processed/` | domain rules + deterministic transforms |
| STAC Collections/Items | JSON | `data/stac/collections/`, `data/stac/items/` | STAC + KFM profiles |
| DCAT dataset records | RDF/JSON-LD | `data/catalog/dcat/` | DCAT 3 + KFM profile |
| PROV lineage bundles | JSON/RDF | `data/prov/` | PROV-O + KFM profile |
| Validation diagnostics | JSON/Markdown | `mcp/runs/` (preferred) | (TBD schema) |

### Sensitivity & redaction
- Quality tooling must not leak:
  - sensitive locations (exact coordinates) when the underlying record is restricted,
  - PII found in source documents,
  - restricted community knowledge.
- Public artifacts should prefer **aggregated** quality signals (counts/rates) over raw samples.

### Quality signals
Quality signals should be **deterministic** and **actionable**, and should separate:
- **Blocking validations (gates)**: must pass to proceed.
- **Non-blocking signals**: recorded for monitoring/drift detection.

#### Quality dimensions (standard vocabulary)
| Dimension | Examples | Notes |
|---|---|---|
| Completeness | required fields present, non-null ratios | Must include provenance fields when required |
| Validity | schema conformance, type/range checks | Prefer schema-first, then semantic checks |
| Consistency | stable IDs, cross-file referential integrity | Especially between catalogs ↔ graph ingest |
| Uniqueness | duplicate IDs, duplicate geometries | Must not break stable identifiers |
| Accuracy | reconcile to authoritative references | Only when an authority is cited and permitted |
| Timeliness | updated timestamps, freshness windows | Only relevant when data updates periodically |

#### Minimum quality gates (draft)
| Gate | Stage | Blocks release? | Minimum checks (examples) |
|---|---|---:|---|
| G1 | ETL + normalization | Yes | parse success, checksum recorded, deterministic transforms |
| G2 | STAC/DCAT/PROV catalogs | Yes | schema validation, broken-link checks, required metadata present |
| G3 | Graph build/ingest | Yes | node/edge constraints, provenance linkage, stable IDs |
| G4 | API layer | Yes | contract tests, authorization/redaction behavior |
| G5 | Story/Focus consumption | Yes | provenance-linked narrative rule; citations must resolve |

#### Asset-type checklist (draft)
| Asset type | Required checks (minimum) |
|---|---|
| Tabular (CSV/Parquet) | schema/types, row counts, primary key uniqueness (if defined), missingness thresholds (if defined), value ranges (if defined) |
| Text (PDF/TXT/HTML extract) | extraction success, encoding normalization, page/segment counts, provenance to source file, PII scan (if governance requires) |
| Vector (GeoJSON/Shapefile) | CRS defined, geometry validity, bbox sanity, topology warnings logged, temporal coverage if present |
| Raster (GeoTIFF) | CRS defined, geotransform present, bbox/time coverage, nodata handling, resolution metadata |
| Time series | monotonic time index, missing intervals, outliers flagged, units/scale documented |

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Collections and Items must validate against the adopted STAC profile and required extensions.
- Items ↔ Collections integrity and asset link integrity are treated as **blocking**.

### DCAT
- Dataset records must include minimum required descriptive metadata (title/description/license/keywords) per DCAT 3 expectations.
- If DCAT records reference distributions/assets, those references must resolve.

### PROV-O
- Required lineage fields:
  - `prov:wasDerivedFrom`: source IDs / source assets
  - `prov:wasGeneratedBy`: pipeline activity/run ID
  - Agents responsible for generation (human or system identity)
- Quality outputs should link to the same run ID used for STAC/DCAT generation where applicable.

### Versioning
- New versions of cataloged artifacts should link predecessor/successor (catalog layer) and be mirrored in graph lineage.

## 🧱 Architecture

### Components
| Component | Responsibility | Interface |
|---|---|---|
| ETL | ingest + normalize + pre-catalog validation | configs + run logs |
| Catalogs | STAC/DCAT/PROV outputs + validation | JSON/RDF + validator |
| Graph | enforce ontology + constraints + provenance linkage | API layer consumes graph |
| APIs | serve contracted access + redaction behavior | REST/GraphQL contracts |
| UI | render map/narrative + display provenance + warnings | API calls only |
| Story Nodes | curated narrative artifacts w/ provenance | docs + graph refs |
| Focus Mode | contextual synthesis w/ provenance constraints | evidence bundle |

### Interfaces / contracts
| Contract | Location | Versioning rule |
|---|---|---|
| JSON schemas | `schemas/` | Semver + changelog |
| Catalog profiles | `data/stac/` + `data/catalog/dcat/` + `data/prov/` | Schema validation required |
| API schemas | `src/server/` + `docs/` | Backward compat or version bump |
| Layer registry | `web/` | Schema-validated + redaction aware |

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/...`
- [ ] STAC: collection + item validation + integrity checks
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: provenance/audit display rules + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: quality signals schema/versioning

## 🧠 Story Node & Focus Mode Integration

### How data quality surfaces in Focus Mode
- Focus Mode must be able to:
  - warn when provenance is incomplete,
  - hide/withhold restricted details based on sovereignty policy,
  - show citations that resolve to catalog IDs.

### Provenance-linked narrative rule
- Every factual claim must trace to a dataset / record / asset ID (catalog or document reference).
- Predictive content (if any) must be opt-in and carry uncertainty/confidence metadata.

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV + internal JSON schemas)
- [ ] Catalog integrity checks (items↔collections, broken links)
- [ ] Graph integrity checks
- [ ] API contract tests
- [ ] UI schema checks (layer registry) where applicable
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas (stac/dcat/prov + internal)
# 2) run unit/integration tests
# 3) run doc lint / markdown protocol validation
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Gate pass/fail by stage | validators | `mcp/runs/` |
| Schema validation summary | validators | `mcp/runs/` |
| Broken-link counts | catalog integrity checks | `mcp/runs/` |
| Geometry invalid counts | geospatial validators | `mcp/runs/` |

## ⚖ FAIR+CARE & Governance

### Review gates
- New datasets, new public endpoints, or new sensitive layers require governance review as defined in governance refs.

### CARE / sovereignty considerations
- If a dataset can expose culturally sensitive locations or community knowledge:
  - apply generalization/redaction rules,
  - ensure access controls exist at the API layer,
  - avoid publishing raw samples in public quality artifacts.

### AI usage constraints
- Documentation generation must not imply prohibited AI actions (e.g., inferring sensitive locations).
- Any AI-assisted summaries must remain provenance-linked and non-speculative.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v0.1.0 | 2025-12-20 | Initial draft for DataOps/Data Quality sub-area | TBD |
---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

