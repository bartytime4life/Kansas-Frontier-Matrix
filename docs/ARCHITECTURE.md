---
title: "Kansas Frontier Matrix — Architecture"
path: "docs/ARCHITECTURE.md"
version: "v1.0.0"
last_updated: "2025-12-17"
status: "draft"
doc_kind: "Architecture"
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

doc_uuid: "urn:kfm:doc:architecture:v1.0.0"
semantic_document_id: "kfm-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:architecture:v1.0.0"
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

# Kansas Frontier Matrix — Architecture

## 📘 Overview

### Purpose
- Define the end-to-end architecture of Kansas Frontier Matrix (KFM) and the subsystem contracts that make the pipeline reproducible, governed, and UI-consumable.
- Provide a shared mental model for contributors: what components exist, how they connect, and what invariants must not be broken.

### Scope
| In Scope | Out of Scope |
|---|---|
| Canonical pipeline architecture: ETL → STAC/DCAT/PROV → Graph → APIs → UI → Story Nodes → Focus Mode | Dataset-specific ETL details (document in `docs/pipelines/<domain>/...`) |
| Subsystem boundaries, interfaces, and “do not break” rules | Full API reference (use OpenAPI/GraphQL docs + contract extension docs) |
| Deployment model overview (static-first + optional services) | Infrastructure runbooks / SRE playbooks (not confirmed in repo) |
| Governance + FAIR+CARE implications of architectural choices | Creating new governance policy (prohibited; refer to governed policy docs) |

### Audience
- Primary: KFM maintainers and contributors (data, pipeline, graph, API, UI).
- Secondary: reviewers/partners evaluating provenance, governance, and reproducibility.

### Definitions (link to glossary)
- Link: `docs/glossary.md` (not confirmed in repo)
- Terms used in this doc: ETL, STAC, DCAT, PROV-O, Neo4j, ontology, contract tests, Story Nodes, Focus Mode, layer registry, redaction/generalization, telemetry.

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (pipeline + extension matrix) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical ordering and subsystem contracts |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governs this document structure |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs | Governs narrative artifacts |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Governs endpoint/GraphQL schema changes |
| Pipeline contract | `KFM-PPC v11.0.0` | Governance | The “non-negotiable ordering” |
| Profiles (catalog validation) | `KFM-STAC/DCAT/PROV v11.0.0` | Data/Catalog | Machine validation targets |
| Ontology protocol | `KFM-ONTO v4.1.0` | Graph | Governs labels/relations + migrations |

### Definition of done (for this document)
- [ ] Front-matter complete + valid (and `path` matches file location)
- [ ] Architecture diagrams render (Mermaid)
- [ ] Subsystem contracts + invariants are explicit
- [ ] Interfaces (files/schemas/APIs) are documented clearly
- [ ] Validation gates and reproducible build entry points are listed
- [ ] Governance + CARE/sovereignty considerations explicitly stated

## 🗂️ Directory Layout

### This document
- `path`: `docs/ARCHITECTURE.md`

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | `raw/`, `work/`, `processed/` data by domain |
| Catalogs | `data/stac/` + `docs/data/` | STAC items/collections, DCAT mapping docs, PROV records/docs |
| Pipelines | `src/pipelines/` + `docs/pipelines/` | ETL orchestration, transforms, run logs, reproducibility notes |
| Graph | `src/graph/` + `docs/graph/` | Ontology, constraints, migrations, ingestion tooling |
| APIs | `src/server/` + `docs/` | REST/GraphQL access layer, contract docs (OpenAPI/GraphQL) |
| Frontend | `web/` + `docs/design/` | React map client, layer registry, Focus Mode UX docs |
| Schemas | `schemas/` | JSON schemas for catalogs + telemetry |
| Tests | `tests/` | Contract tests and validation fixtures |
| Story Nodes | `docs/reports/.../story_nodes/` | Governed narrative nodes (markdown) |
| Telemetry | `docs/telemetry/` + `schemas/telemetry/` | Signals, auditability, schema versioning |
| Security | `.github/SECURITY.md` + `docs/security/` | Security policy and implementation standards |
| MCP | `mcp/` | Model cards, experiment reports, SOPs |

### Expected file tree for this sub-area
~~~text
📁 docs/
├─📄 ARCHITECTURE.md
├─📄 MASTER_GUIDE_v12.md
├─📁 templates/
│  ├─📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│  ├─📄 TEMPLATE__STORY_NODE_V3.md
│  └─📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├─📁 governance/
│  ├─📄 ROOT_GOVERNANCE.md
│  ├─📄 ETHICS.md
│  └─📄 SOVEREIGNTY.md
├─📁 graph/
│  └─📄 <ontology-and-migrations-docs>
├─📁 pipelines/
│  └─📄 <etl-and-catalog-build-docs>
└─📁 design/
   └─📄 <ui-and-focus-mode-docs>
~~~

## 🧭 Context

### Background
KFM is designed as an end-to-end geospatial + historical knowledge system that turns heterogeneous raw inputs into interactive map exploration and provenance-led narratives. The architecture is intentionally “static-first” (pre-generated assets whenever possible) but supports a lightweight API layer when dynamic queries are required.

### Assumptions
- Data sources are heterogeneous (raster, vector, text) and must be normalized into stable, reusable intermediate formats.
- Outputs must be reproducible: the same inputs + pinned tooling yield the same results.
- Catalogs and provenance are not optional metadata: they are the primary mechanism for trust, auditability, and UI explainability.
- The UI should remain usable even in “minimal deployment” scenarios (static hosting); dynamic services are an extension, not a baseline requirement.

### Constraints / invariants
- The canonical pipeline ordering is preserved: **ETL → STAC/DCAT/PROV catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Frontend consumes contracts via APIs or pre-built artifacts (no direct graph dependency).
- ETL must be deterministic and replayable; catalogs must be schema-validated.
- Focus Mode is provenance-only: no unsourced narrative; predictive content is opt-in and includes uncertainty metadata.
- UI must not leak sensitive data: layer registry + gating and API-side redaction/generalization are part of the architecture (not an afterthought).

### Open questions
| Question | Owner | Target date |
|---|---|---|
| Confirm canonical locations for API contract docs (OpenAPI + GraphQL schema files) | TBD | TBD |
| Confirm the authoritative location for glossary and shared definitions | TBD | TBD |
| Define the minimal public telemetry set vs restricted telemetry | TBD | TBD |

### Future extensions
KFM expects structured growth via an “Extension Matrix” approach: new capabilities are added across layers in a coordinated, testable way. Canonical next-evolution extension points include:
- (A) **Data**: new domains, new STAC extension profiles.
- (B) **AI evidence**: evidence artifacts as STAC assets, linked into Focus Mode.
- (C) **Graph**: new entity types with explicit provenance.
- (D) **API**: new endpoints with contract tests and redaction/generalization rules.
- (E) **UI**: new layer registry entries with provenance pointers and CARE gating.

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  subgraph Ingest["ETL + Normalization"]
    A["Raw Sources<br/>data/raw/"] --> B["Work Staging<br/>data/work/"]
    B --> C["Processed Outputs<br/>data/processed/"]
  end

  subgraph Catalogs["Catalog Generation"]
    C --> D["STAC Collections + Items<br/>data/stac/"]
    C --> E["DCAT Mapping<br/>docs/data/"]
    C --> F["PROV Lineage Records<br/>docs/data/ + embedded blocks"]
  end

  subgraph Graph["Semantic Core"]
    D --> G["Neo4j Knowledge Graph<br/>ontology + constraints"]
    E --> G
    F --> G
  end

  subgraph Access["Access Services"]
    G --> H["API Layer<br/>REST + GraphQL<br/>src/server/"]
  end

  subgraph UIX["User Experience"]
    C --> I["Static UI Assets + Layer Data<br/>web/"]
    H --> I
    I --> J["Story Nodes<br/>docs/reports/.../story_nodes/"]
    J --> K["Focus Mode<br/>Provenance-led dashboards"]
  end

  subgraph Observability["Governance + Telemetry"]
    A --> T["Run Logs + Validation Artifacts"]
    H --> U["API Telemetry"]
    I --> V["UI Audit Signals"]
  end
~~~

### Optional: Focus Mode sequence diagram
~~~mermaid
sequenceDiagram
  participant UI as React/Map UI
  participant API as API Layer
  participant Graph as Neo4j Graph

  UI->>API: Focus query(entity_id, viewport, time_range)
  API->>Graph: Fetch subgraph + provenance refs (apply redaction)
  Graph-->>API: Context bundle (entities + evidence + lineage)
  API-->>UI: Contracted payload (narrative pointers + citations + audit flags)
~~~

### Optional: deployment view (static-first)
~~~mermaid
flowchart TB
  subgraph Host["Static Host (e.g., Pages/CDN)"]
    W["web/ build artifacts"]
    X["data/processed public assets"]
    Y["data/stac public catalogs"]
  end

  subgraph Services["Optional services (containers)"]
    A1["API service"]
    A2["Neo4j"]
  end

  User["Browser"] --> Host
  User --> A1
  A1 --> A2
  A1 --> Host
~~~

## 📦 Data & Metadata

### Inputs
| Input | Format | Where from | Validation |
|---|---|---|---|
| Geospatial rasters | GeoTIFF/COG | External portals, archives | Raster metadata + projection checks |
| Geospatial vectors | GeoJSON / Shapefile | State/local data hubs, digitized maps | Geometry validity + schema checks |
| Text corpora | TXT/PDF/HTML (normalized) | Historical archives | Language/encoding normalization + citation retention |
| Human-curated annotations | YAML/JSON/MD | Researchers / maintainers | Schema + review gates |

### Outputs
| Output | Format | Path | Contract / Schema |
|---|---|---|---|
| Processed datasets | GeoTIFF/CSV/GeoJSON/etc. | `data/processed/` | Domain schemas (as applicable) |
| STAC catalogs | JSON | `data/stac/` | KFM-STAC v11.0.0 |
| DCAT mapping docs | JSON-LD / docs | `docs/data/` | KFM-DCAT v11.0.0 |
| PROV lineage | JSON-LD / embedded blocks | `docs/data/` + artifacts | KFM-PROV v11.0.0 |
| Graph build / exports | DB + dumps | `src/graph/` tooling | KFM-ONTO v4.1.0 + constraints |
| API schemas | OpenAPI + GraphQL SDL | `docs/` + `src/server/` | Contract-governed |
| UI layer registry | JSON/YAML | `web/` | UI schema checks |
| Story Nodes | Markdown (governed) | `docs/reports/.../story_nodes/` | Story Node v3 template |
| Telemetry | JSON logs/metrics | `docs/telemetry/` | Telemetry schemas |

### Sensitivity & redaction
- Treat sensitivity as an architectural concern: sensitive coordinates and restricted site details must be generalized/redacted **before** reaching unauthenticated clients.
- Enforce gating in both:
  - the API layer (policy enforcement + redaction) and
  - the UI layer registry (prevent unauthorized layers from rendering).

### Quality signals
- Determinism: same inputs yield same outputs (ETL replayability).
- Schema validity: STAC/DCAT/PROV payloads must validate against governed profiles.
- Graph integrity: ontology constraints + migration discipline (no breaking label/edge changes).
- UI integrity: layer registry schema checks + a11y expectations.
- Provenance coverage: Focus Mode requires provenance pointers for every surfaced claim/evidence panel.

### Extension points checklist (for future work)
- [ ] Data: new domain added under `data/<domain>/.`
- [ ] STAC: new collection + item schema validation
- [ ] PROV: activity + agent identifiers recorded
- [ ] Graph: new labels/relations mapped + migration plan
- [ ] APIs: contract version bump + tests
- [ ] UI: layer registry entry + access rules
- [ ] Focus Mode: provenance references enforced
- [ ] Telemetry: new signals + schema version bump

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Every processed dataset is represented as a STAC Collection + Items, including spatial/temporal extents and asset links.
- Evidence artifacts (e.g., model outputs, derived layers) are treated as first-class assets to enable reproducible UI rendering and downstream reuse.

### DCAT
- STAC holdings are mapped into DCAT-compatible dataset descriptions (title, description, license, keywords, publisher/contact metadata).
- DCAT enables cross-catalog interoperability: discovery tools can harvest KFM datasets without needing KFM-specific code.

### PROV-O
- Pipeline steps emit machine-readable lineage information. At minimum, record:
  - `prov:wasGeneratedBy` (the activity/process producing an artifact)
  - `prov:used` (inputs used)
  - `prov:generatedAtTime` (timestamp)
- Provenance must be preserved into the graph and surfaced back to UI/Focus Mode.

### Versioning
- Use STAC versioning links and graph predecessor/successor relationships as applicable.
- API contracts follow backward compatibility rules or require explicit version bumps.

## 🧱 Subsystem contracts (architecture rules)

### Subsystem contracts table
| Subsystem | Contract artifacts | “Do not break” rule | Primary interface(s) |
|---|---|---|---|
| ETL | configs + run logs + validation artifacts | Deterministic, replayable runs | Files in `data/processed/` + lineage logs |
| Catalogs | STAC/DCAT/PROV schemas + validators | Must pass schema validation | JSON catalogs + JSON-LD mappings |
| Graph | ontology + migrations + constraints | Stable labels/edges; migration discipline | Neo4j via Cypher/GraphQL resolvers; exports |
| APIs | OpenAPI/GraphQL schemas + tests | Backward compat or version bump | REST/GraphQL endpoints + context bundles |
| UI | layer registry + a11y + audit affordances | No hidden data leakage | Static assets + contracted API calls |
| Story Nodes | Story Node template + provenance schema | Evidence-led, versioned narratives | Markdown artifacts + graph ingestion links |
| Focus Mode | provenance-linked context bundle | No hallucinated sources | API-provided focus payload + audit flags |
| Telemetry | telemetry schemas + collectors | Observability for performance/security/governance | `docs/telemetry/` outputs + dashboards (not confirmed in repo) |

### Interface discipline
- **File-based interfaces** (preferred): processed assets, catalogs, UI layer payloads.
- **Schema-based contracts** (required): STAC/DCAT/PROV, telemetry, story node front-matter.
- **API-based contracts** (when needed): search, graph queries, Focus Mode context bundles.

### Deployment modes
- **Static-first (baseline)**: host the built `web/` app and public artifacts/cats; enables broad accessibility.
- **Static + API (recommended for richer queries)**: add a small API service and graph backend for dynamic queries and Focus Mode assembly.
- **Local/dev (repro builds)**: containerized environment runs ETL + graph build + UI build deterministically.

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- Focusable entities typically include: Places, Events, People, Datasets, and Story Nodes.
- Focus Mode should present:
  - a map + time window centered on the focus entity
  - the evidence bundle (datasets, assets, citations, lineage)
  - related graph context (neighbors/relationships)
  - governance/audit indicators (redaction applied, sensitivity class, etc.)

### Provenance-linked narrative rule
- Every claim must trace to a dataset / record / asset identifier.
- Predictive/AI-derived content must be: explicit, opt-in, uncertainty-labeled, and provenance-linked to the model run + inputs.

### Optional structured controls
~~~yaml
focus_layers:
  - "TBD"
focus_time: "TBD"
focus_center: [ -98.0000, 38.0000 ]
~~~

## 🧪 Validation & CI/CD

### Validation steps
- [ ] Markdown protocol checks
- [ ] Schema validation (STAC/DCAT/PROV)
- [ ] Graph integrity checks (ontology constraints + migrations)
- [ ] API contract tests (OpenAPI/GraphQL)
- [ ] UI schema checks (layer registry)
- [ ] Security and sovereignty checks (as applicable)

### Reproduction
~~~bash
# Example placeholders — replace with repo-specific commands
# (Commands below are referenced in design docs but may differ in the live repo.)

# 1) Build container environment
docker compose up --build

# 2) Run end-to-end pipeline (ETL -> catalogs -> graph -> web build)
make all

# 3) Run validation + tests
make test
~~~

### Telemetry signals (if applicable)
| Signal | Source | Where recorded |
|---|---|---|
| Pipeline run metadata (inputs, versions, durations) | ETL | `docs/telemetry/` + `schemas/telemetry/` |
| Catalog validation failures | Catalog build | CI logs + telemetry (if enabled) |
| Redaction/generalization counts | API + UI gating | Telemetry + audit panels |
| Focus Mode provenance coverage (%) | API assembly | Telemetry + tests |

## ⚖ FAIR+CARE & Governance

### Review gates
- Architectural changes that introduce new data sources, new public endpoints, new sensitive layers, or new AI narrative behavior require explicit governance review.
- Contract changes (API, ontology, schema) must include tests and documentation updates as part of the same change set.

### CARE / sovereignty considerations
- Sensitive locations and culturally sensitive information must follow documented redaction/generalization rules.
- The architecture assumes “metadata can be open while payload can be restricted” when sovereignty requires it.

### AI usage constraints
- Ensure this document’s AI permissions/prohibitions match intended use (no policy generation; no inferring sensitive locations).
- Focus Mode must not present unsourced narrative or un-audited model outputs.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-17 | Initial architecture doc (aligned to Master Guide v12 + governed templates) | Bartytime |

---
Footer refs:
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
