---
title: "Kansas Frontier Matrix — README"
path: "Kansas-Frontier-Matrix/README.md"
version: "v12.0.0-draft"
last_updated: "2025-12-17"
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

doc_uuid: "urn:kfm:doc:repo:readme:v12.0.0-draft"
semantic_document_id: "kfm-readme-v12.0.0-draft"
event_source_id: "ledger:kfm:doc:repo:readme:v12.0.0-draft"
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

# Kansas Frontier Matrix (KFM)

Kansas Frontier Matrix (KFM) is a geospatial + historical knowledge system with a governed, provenance-first pipeline that turns raw sources into interoperable catalogs (STAC/DCAT/PROV), a semantic graph, and a map + narrative experience.

The canonical pipeline ordering is **non-negotiable**:
**ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**.

## 📘 Overview

### Purpose
- Provide a single entry point for contributors and reviewers to understand the system shape, governance posture, and where artifacts live.
- Establish “do not break” invariants (ordering, provenance, sovereignty, and contract boundaries).
- Point to the canonical governed docs and templates that control how KFM evolves (v12).

### Scope
| In Scope | Out of Scope |
|---|---|
| Repo orientation, pipeline invariants, artifact locations, governed standards pointers | Full runbooks, dataset-by-dataset documentation, endpoint-by-endpoint API references |
| High-level architecture and extension patterns | Unreviewed ontology invention or policy generation |
| Governance + sovereignty framing | Publishing protected locations or sensitive site coordinates |

### Audience
- Maintainers and contributors (data/ETL, cataloging, graph, APIs, UI)
- Governance and safety reviewers (FAIR+CARE, sovereignty)
- Researchers/educators integrating KFM outputs

### Definitions (link to glossary)
- Glossary (if present): `docs/glossary.md`
- Key terms: **STAC**, **DCAT**, **PROV-O**, **Neo4j**, **Story Nodes**, **Focus Mode**, **FAIR+CARE**, **sovereignty**, **contract boundary**

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline + extension matrix |
| Master Guide v11 (baseline) | `docs/MASTER_GUIDE_v11.md` | Maintainers | Stable baseline (if present) |
| Governed doc templates | `docs/templates/` | Maintainers | Universal / Story Node / API contract templates |
| Governed standards | `docs/standards/` | Governance | Markdown protocol, schema rules, gates |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review triggers + enforcement expectations |
| Ethics | `docs/governance/ETHICS.md` | Governance | Evidence-led content and safety rules |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | CARE and sensitive location handling |
| System architecture | `Kansas-Frontier-Matrix/ARCHITECTURE.md` | Maintainers | High-level boundaries and contracts (if present) |

### Definition of done (for this document)
- [ ] YAML front-matter keys match the governed template (no extra keys added)
- [ ] Canonical pipeline ordering stated and not contradicted elsewhere
- [ ] Repo top-levels and canonical subsystem locations listed
- [ ] Governance + sovereignty posture is explicit (no sensitive leakage)
- [ ] Validation expectations and extension patterns are present
- [ ] No claims require secrets/credentials or private infrastructure details

## 🗂️ Directory Layout

### This document
- `path`: `Kansas-Frontier-Matrix/README.md` (must match front-matter)

### Related repository paths
The following canonical locations are expected (per Master Guide conventions):

| System / Area | Canonical location | What it governs |
|---|---|---|
| Data domains | `data/` | Raw/work/processed/stac organization per domain |
| STAC/DCAT/PROV | `data/stac/` + `docs/data/` | Catalog generation + mappings |
| Graph | `src/graph/` + `docs/graph/` | Ontology, labels, relationships, migrations |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL, transforms, catalog build, graph build |
| APIs | `src/server/` + docs | Contracted access layer (REST/GraphQL) |
| Frontend | `web/` + `docs/design/` | Map layers, Focus Mode UX, accessibility |
| Story Nodes | `docs/reports/.../story_nodes/` + graph | Narrative artifacts with provenance |
| Schemas | `schemas/` | Validation shapes (STAC/DCAT/telemetry/etc.) |
| MCP records | `mcp/` | Experiments, run notes, model cards, logs |
| Testing | `tests/` | Unit/integration/contract tests |
| Tooling | `tools/` | Validators, CLIs, CI helpers |
| Releases | `releases/` | Signed/attested deliverables (if used) |

### Expected file tree for this sub-area
Repo top-level (expected):

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📄 ARCHITECTURE.md
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
├── 📁 .github/
├── 📁 data/
├── 📁 docs/
├── 📁 mcp/
├── 📁 schemas/
├── 📁 src/
├── 📁 tests/
├── 📁 tools/
├── 📁 web/
└── 📁 releases/
~~~

Expanded (illustrative) layout:

~~~text
📁 Kansas-Frontier-Matrix/
├── 📄 README.md
├── 📄 ARCHITECTURE.md
├── 📄 CONTRIBUTING.md
├── 📄 LICENSE
├── 📁 .github/
├── 📁 data/
│   ├── 📁 raw/
│   ├── 📁 work/
│   ├── 📁 processed/
│   └── 📁 stac/
├── 📁 docs/
│   ├── 📄 MASTER_GUIDE_v11.md
│   ├── 📄 MASTER_GUIDE_v12.md
│   ├── 📁 templates/
│   ├── 📁 standards/
│   ├── 📁 governance/
│   ├── 📁 data/
│   ├── 📁 graph/
│   ├── 📁 pipelines/
│   ├── 📁 design/
│   └── 📁 reports/
├── 📁 schemas/
├── 📁 src/
│   ├── 📁 pipelines/
│   ├── 📁 graph/
│   └── 📁 server/
├── 📁 web/
├── 📁 tests/
├── 📁 tools/
├── 📁 mcp/
└── 📁 releases/
~~~

## 🧭 Context

### Background
Kansas-relevant data (historical maps, boundaries, routes, environmental layers, documents, imagery, and derived evidence products) is fragmented across institutions, formats, and time scales. KFM provides a governed system to ingest, catalog, connect, and present this information as a reproducible map + narrative experience with traceable evidence.

### Assumptions
- Pipelines should be deterministic and replayable from versioned configs and recorded inputs.
- Metadata and provenance are first-class outputs, not afterthoughts.
- The UI must remain behind APIs/contracts (no direct graph coupling).
- Narrative experiences must be evidence-led and provenance-linked (especially in Focus Mode contexts).

### Constraints / invariants
- **Ordering is fixed:** ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode.
- **No unsourced narrative** is permitted in Focus Mode contexts.
- Derived datasets belong in `data/processed/` and must be cataloged (STAC/DCAT) and lineage-tracked (PROV).
- Ontology/graph changes must be migration-safe and governed (schema/ontology review where applicable).
- Sensitive and culturally restricted information must be governed and protected (see sovereignty policy).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| What are the canonical “first run” commands (compose/Make/CLI) for this repo snapshot? | Maintainers | TBD |
| What is the public vs restricted data publishing model (by domain)? | Governance reviewers | TBD |
| Where are API contracts documented and how are breaking changes versioned? | Maintainers | TBD |

### Future extensions
- Additional domain datasets through governed extension points (schemas → catalogs → graph mappings → APIs → UI layers).
- “Evidence products” (analyses, derived artifacts) treated as first-class catalog assets, surfaced through Focus Mode with provenance.
- Stronger governance/telemetry signals (security posture, sovereignty flags, audit trails).

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[ETL: ingest + transform] --> B[STAC/DCAT/PROV catalogs]
  B --> C[Neo4j graph]
  C --> D[APIs: REST/GraphQL]
  D --> E[React/Map UI]
  E --> F[Story Nodes]
  F --> G[Focus Mode]
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as Web UI
  participant API as API
  participant Graph as Graph

  UI->>API: Focus query(entity_id, time_range, layer_set)
  API->>Graph: Fetch subgraph + provenance refs (apply redaction)
  Graph-->>API: Context bundle + evidence pointers
  API-->>UI: Contracted payload (context + provenance + audit flags)
~~~

## 📦 Data & Metadata

### Inputs
| Input | Examples | Typical location | Notes |
|---|---|---|---|
| Raw sources | GIS layers, imagery, scans, tables, text corpora | `data/raw/` | Track licenses and provenance |
| Pipeline configs | YAML/JSON configs, mapping files | `src/pipelines/` | Must be versioned and replayable |
| Governance rules | policies, standards, templates | `docs/governance/`, `docs/standards/`, `docs/templates/` | Governed review required |

### Outputs
| Output | Typical format | Typical location | Contract / validation |
|---|---|---|---|
| Processed datasets | GeoJSON/GeoTIFF/COG/CSV/Parquet | `data/processed/` | Domain validation + checksums |
| STAC catalogs | JSON (Collections/Items/Assets) | `data/stac/` | STAC validation required |
| DCAT dataset views | JSON-LD/RDF/exports | `docs/data/` (or `data/stac/` adjunct) | Mapping must be documented |
| PROV lineage bundles | PROV-O compatible RDF/JSON | project-defined | Must link inputs → activities → outputs |
| Graph ingest artifacts | CSV/Parquet/ETL outputs | `src/graph/` (and/or `data/work/`) | Graph integrity tests |
| UI layer registries | JSON/YAML configs | `web/` (project-defined) | Schema-validated where applicable |
| Story Nodes | governed markdown | `docs/reports/.../story_nodes/` | Must reference evidence IDs |

### Sensitivity & redaction
- Do not publish precise coordinates or identifying details for protected or culturally sensitive sites.
- Apply sovereignty policy rules before any public release and before embedding content in narrative contexts.
- Prefer generalized locations (region/county-level) when sensitivity is uncertain.

### Quality signals
- Checksums and stable identifiers for inputs/outputs.
- Schema validation (STAC/DCAT/telemetry) and reproducible pipeline runs.
- Provenance completeness (PROV activities + agents + entities).
- Contract tests for APIs and compatibility checks for UI layer configs.

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- KFM uses STAC to describe datasets as **Collections** and deliverables as **Items/Assets**.
- Every public-facing or narrative-surfaced asset should have a STAC reference (directly or via an evidence bundle).

### DCAT
- KFM uses DCAT as a discovery-oriented “view” of datasets (licensing, publisher, themes, distributions).
- DCAT mappings should be documented alongside STAC outputs to keep dataset metadata coherent.

### PROV-O
- KFM uses PROV-O to capture lineage: raw inputs → ETL activities → processed artifacts → catalogs → graph ingest.
- PROV records should include stable activity IDs (pipeline run IDs), agents, and entity references.

### Versioning
- Dataset versions should not overwrite history; instead record predecessor/successor relationships.
- Graph and narrative outputs should preserve the dataset version context to support reproducible interpretation.

## 🧱 Architecture

### Components
| Component | Responsibility | Primary outputs |
|---|---|---|
| ETL | Ingest, normalize, validate | Processed datasets + run metadata |
| Catalogs | Publish STAC/DCAT/PROV | Catalog JSON + lineage bundles |
| Graph | Semantic integration | Versioned graph data + constraints |
| APIs | Contracted access | REST/GraphQL responses + audit flags |
| UI | Map + narrative UX | Interactive exploration via contracts |
| Story Nodes | Curated narratives | Evidence-linked, versioned markdown |
| Focus Mode | Context synthesis | Provenance-linked context bundles |
| Telemetry | Observability + governance signals | Logs, metrics, reports (schema’d) |

### Interfaces / contracts
| Interface | Location (canonical) | Contract expectation |
|---|---|---|
| STAC outputs | `data/stac/` | Must validate; stable IDs |
| DCAT mappings/views | `docs/data/` | Must map license/publisher/distribution |
| PROV lineage | project-defined | Must connect inputs → activities → outputs |
| Graph model + migrations | `src/graph/` + `docs/graph/` | Governed, migration-safe |
| API contracts | `src/server/` + docs | Versioned; contract-tested |
| UI layer registry | `web/` | Config schema validation; provenance pointers |

### Extension points checklist (for future work)
- [ ] Data: add/ingest new domain sources (deterministic ETL)
- [ ] Catalog: publish STAC Items/Collections for new artifacts
- [ ] Lineage: record PROV activities/agents/entities for transforms
- [ ] Graph: map to governed ontology + apply migrations/constraints
- [ ] API: expose through contracts + add tests (no direct graph coupling)
- [ ] UI: register layers/panels referencing evidence IDs
- [ ] Story/Focus: add Story Nodes and Focus contexts with full provenance
- [ ] Telemetry: add governance signals and validation reporting where needed

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focus Mode surfaces context for a selected focus target (place, event, dataset, asset, entity).
- All surfaced facts must include evidence pointers (dataset IDs, document IDs, STAC assets, and/or PROV activity references).

### Provenance-linked narrative rule
- **Every factual claim** presented in Story Nodes or Focus Mode contexts must trace to a cited evidence identifier.
- Hypotheses must be labeled as such and kept distinct from sourced claims.

### Optional structured controls
~~~yaml
# Example only; do not include protected coordinates.
focus_mode:
  focus_target_id: "TBD"
  time_range: "TBD"
  layer_set: ["TBD"]
  redaction_profile: "default"
~~~

## 🧪 Validation & CI/CD

### Validation steps
- Markdown protocol validation (structure + fencing + front-matter keys)
- Schema validation (STAC/DCAT/telemetry as applicable)
- Graph integrity tests (constraints + migrations)
- API contract tests (REST/GraphQL)
- UI config/schema checks (layer registries, a11y gates where applicable)
- Security/sovereignty checks (PII/secrets scanning + protected-site masking)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# 1) validate schemas (STAC/DCAT/telemetry)
# 2) run unit/integration tests (pipelines/graph/api)
# 3) run doc lint (markdown protocol)
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run metadata | ETL workflows | `mcp/` (run records) |
| Schema validation results | CI workflows | CI logs + reports |
| Governance compliance flags | Review workflow | governance reports (project-defined) |

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that affect any of the following should trigger governance review:
- Pipeline ordering or provenance requirements
- Ontology/graph model changes (new labels/relations, migrations)
- Public-facing API contracts or access/redaction behavior
- UI behaviors that surface narrative or sensitive information
- New datasets with licensing/sovereignty implications
- AI-driven narrative behavior, especially in Focus Mode contexts

### CARE / sovereignty considerations
- Treat culturally sensitive information and protected sites as restricted by default.
- Avoid enabling harm: do not disclose, infer, or reconstruct protected coordinates.
- Apply redaction/generalization policies early (ETL/catalog) and enforce again at API/UI layers.

### AI usage constraints
- Allowed transformations (per front-matter): summarize, structure extraction, translation, keyword indexing.
- Prohibited transformations: generating governance policy and inferring sensitive locations.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.0-draft | 2025-12-17 | README created using the governed Universal Doc template; aligns to Master Guide v12 invariants and canonical subsystem locations. | TBD |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
