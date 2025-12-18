---
title: "Kansas Frontier Matrix — Architecture"
path: ".github/ARCHITECTURE.md"
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

doc_uuid: "urn:kfm:doc:github:architecture:v1.0.0"
semantic_document_id: "kfm-github-architecture-v1.0.0"
event_source_id: "ledger:kfm:doc:github:architecture:v1.0.0"
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
- Provide a GitHub-facing, system-level architecture overview of Kansas Frontier Matrix (KFM).
- Make the *canonical pipeline ordering* and *subsystem contracts* easy to find for contributors.
- Reduce contract breakage by documenting the main invariants (schema validation, stable ontology, API boundaries, provenance-first narrative).

### Scope
| In Scope | Out of Scope |
|---|---|
| Pipeline stages and non-negotiable ordering | Environment-specific deployment instructions (cloud/IaC/K8s) |
| Repo layout and “where to change what” | Dataset-specific ETL procedures (those belong in `docs/pipelines/` + pipeline folders) |
| Cross-cutting standards: STAC/DCAT/PROV + ontology stability | Deep UI design specs (those belong in `docs/design/`) |
| Story Nodes + Focus Mode contracts (provenance-first) | Detailed endpoint-by-endpoint API docs (those belong in API contract docs) |

### Audience
- Primary: Contributors (data engineering, graph, API, frontend, narrative)
- Secondary: Reviewers (governance, ethics, maintainers), integrators, researchers

### Definitions (link to glossary)
- Link: `docs/glossary.md`
- Terms used in this doc (minimum):
  - **PPC**: Pipeline contract (ordering + invariants)
  - **STAC/DCAT/PROV**: Catalog + interoperability + provenance standards
  - **KFM-ONTO**: Governed ontology for graph labels/relationships
  - **Story Node**: Versioned, machine-ingestible narrative artifact
  - **Focus Mode**: Provenance-only narrative + dashboard UI mode

### Key artifacts (what this doc points to)
| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide v12 (draft) | `docs/MASTER_GUIDE_v12.md` | Maintainers | Canonical pipeline order + extension matrix |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Review gates + rules of engagement |
| Ethics | `docs/governance/ETHICS.md` | Governance | Harm minimization + disclosure |
| Sovereignty | `docs/governance/SOVEREIGNTY.md` | Governance | CARE/Indigenous data constraints |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Maintainers | Template for most docs |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Maintainers | Narrative artifacts + provenance requirements |
| API contract template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | Maintainers | REST/GraphQL contract changes |
| Data catalog docs | `docs/data/` | Data leads | DCAT mappings + catalog notes |
| Graph docs | `docs/graph/` | Graph leads | Ontology, migrations, constraints |
| Pipeline docs | `docs/pipelines/` | Pipeline leads | ETL + transforms + catalog build |
| Frontend app | `web/` | UI leads | React + Map UI code |
| API server | `src/server/` | API leads | FastAPI/GraphQL boundary |
| Graph subsystem | `src/graph/` | Graph leads | Neo4j schema + ingest |
| Pipelines | `src/pipelines/` | Pipeline leads | Deterministic ETL + derived products |

### Definition of done (for this document)
- [ ] Front-matter complete + valid
- [ ] Non-negotiable pipeline ordering is stated plainly
- [ ] Repo navigation (“where to change what”) is included
- [ ] Governance + CARE/sovereignty constraints are explicit
- [ ] Focus Mode provenance-only rule is stated
- [ ] Diagrams render in GitHub (Mermaid)
- [ ] Version history updated for this doc

---

## 🗂️ Directory Layout

### This document
- `path`: `.github/ARCHITECTURE.md` (must match front-matter)

### Related repository paths
| Area | Path | What lives here |
|---|---|---|
| GitHub-facing docs | `.github/` | Contribution + policy docs visible from GitHub |
| Canonical documentation | `docs/` | System specs, standards, governance, design, reports |
| Data lifecycle | `data/` | `raw/ → work/ → processed/ → stac/` |
| Schemas | `schemas/` | JSON schemas, validation profiles, telemetry schemas |
| Pipelines | `src/pipelines/` | Deterministic ETL, transforms, catalog generation |
| Graph | `src/graph/` | Neo4j schema, ingest tooling, migrations |
| API layer | `src/server/` | REST/GraphQL service boundary + contracts |
| Frontend UI | `web/` | React app, Map UI, client state + rendering |
| Tests | `tests/` | Contract tests, schema tests, regression tests |
| Tools | `tools/` | Helper scripts, validators, release utilities |
| MCP / experiments | `mcp/` | Model cards, run logs, experiments (if present) |

### Expected file tree for this sub-area
~~~text
📦 repo-root/
├─ 📁 .github/
│  ├─ 📄 ARCHITECTURE.md        # (this file)
│  ├─ 📄 SECURITY.md            # security policy (if present)
│  └─ 📁 workflows/             # CI workflows (if present)
├─ 📁 docs/
│  ├─ 📄 MASTER_GUIDE_v12.md
│  ├─ 📁 governance/
│  ├─ 📁 templates/
│  ├─ 📁 data/
│  ├─ 📁 graph/
│  ├─ 📁 pipelines/
│  ├─ 📁 design/
│  └─ 📁 reports/
│     └─ 📁 .../
│        └─ 📁 story_nodes/
├─ 📁 data/
│  ├─ 📁 raw/
│  ├─ 📁 work/
│  ├─ 📁 processed/
│  └─ 📁 stac/
├─ 📁 schemas/
├─ 📁 src/
│  ├─ 📁 pipelines/
│  ├─ 📁 graph/
│  └─ 📁 server/
├─ 📁 web/
└─ 📁 tests/
~~~

---

## 🧭 Context

### Background
KFM is a **geospatial + historical knowledge system** built around a governed end-to-end pipeline that transforms raw sources into **interactive map layers** and **provenance-grounded narratives**. The architecture is intentionally modular, but it is also intentionally *contracted*: each layer has a defined role, canonical location in the repo, and explicit “must not break” rules.

### Assumptions
- Pipeline ordering is fixed: **ETL → Catalogs → Graph → APIs → UI → Story Nodes → Focus Mode**.
- Cataloging is mandatory: every published dataset has STAC/DCAT/PROV.
- The Neo4j graph is the semantic core and is governed by KFM-ONTO (labels/relations are stable).
- The frontend does **not** directly query the graph; it consumes data via API contracts.
- Focus Mode is provenance-first: narrative content must be backed by traceable sources.

### Constraints / invariants
- **Non-negotiable pipeline ordering**: artifacts flow forward; feedback flows back through governed pathways.
- **Determinism**: ETL runs must be replayable and stable given the same inputs and pinned tool versions.
- **Schema validation gates**: STAC/DCAT/PROV outputs must pass validation before graph ingest.
- **Stable ontology**: graph labels and relationship types must not be changed casually (migration + review required).
- **Contract-first APIs**: breaking changes require explicit versioning + contract documentation.
- **No unauthorized data leakage**: UI must never reveal restricted/blurred locations without gating.
- **Provenance-only narrative in Focus Mode**: no unsourced facts; AI content must be opt-in and uncertainty-labeled.

### Open questions
| Question | Why it matters | Status | Next step |
|---|---|---|---|
| Is STAC served purely as static catalogs, or via a STAC API service? | Impacts client discovery + hosting | TBD | Document in `docs/data/` |
| What authn/authz model is used for sensitive layers? | Data sovereignty + privacy | TBD | Record in governance docs |
| How are Neo4j schema migrations executed in CI? | Prevents drift / broken queries | TBD | Add/confirm migration SOP |

### Future extensions
KFM is designed for controlled evolution. Typical extension work spans multiple layers:
- New **data domain** (new raw sources + ETL + catalog + graph ingest).
- New **AI evidence product** (derived raster/vector/text artifacts + provenance + new graph entities).
- New **graph schema** (ontology additions + migrations + test fixtures).
- New **API capability** (contract extension + tests + docs).
- New **UI layer / Focus mode behavior** (layer registry + gating + provenance UI).
- New **telemetry & governance checks** (signals + gates + review workflow).

---

## 🗺️ Diagrams

### System / dataflow diagram
~~~mermaid
flowchart LR
  A[Raw sources] --> B[ETL: src/pipelines/]
  B --> B1[data/raw/]
  B1 --> B2[data/work/]
  B2 --> B3[data/processed/]

  B3 --> C[Catalog generation]
  C --> C1[data/stac/ (STAC)]
  C --> C2[docs/data/ (DCAT mappings)]
  C --> C3[PROV lineage (files + graph)]

  C1 --> D[Graph ingest: src/graph/]
  C3 --> D
  D --> E[(Neo4j Knowledge Graph)]

  E --> F[API layer: src/server/]
  F --> G[Frontend UI: web/]
  G --> H[Story Nodes: docs/reports/.../story_nodes/]
  H --> I[Focus Mode: provenance-first dashboards]

  I --> J[User contributions / feedback]
  J --> B
~~~

### Optional: sequence diagram
~~~mermaid
sequenceDiagram
  autonumber
  participant U as User
  participant UI as Web UI (web/)
  participant API as API (src/server/)
  participant G as Graph (Neo4j via src/graph/)
  participant N as Narrative/Focus Transformer (if enabled)

  U->>UI: Click entity / open Story Node / enter query
  UI->>API: Focus request (entity + time + map bounds + options)
  API->>G: Query subgraph + provenance pointers
  G-->>API: Subgraph + entities + dataset refs + lineage IDs
  API-->>UI: Focus payload (data + sources + governance flags)
  alt AI narrative enabled (opt-in)
    UI->>API: Request narrative for this focus context
    API->>N: Provide context + citations + uncertainty policy
    N-->>API: Narrative text + confidence + citations
    API-->>UI: Narrative + explainability bundle
  end
  UI-->>U: Render map/layers/timeline + citations + audit flags
~~~

---

## 📦 Data & Metadata

### Inputs
| Input type | Examples | Where it lands | Notes |
|---|---|---|---|
| Geospatial data | vectors, rasters | `data/raw/` | Normalize formats early |
| Text documents | PDFs, HTML, OCR text | `data/raw/` | Track extraction method |
| Tabular data | CSVs, spreadsheets | `data/raw/` | Validate schema/fields |
| Research annotations | curated notes, links | `docs/` or governed inputs | Must be provenance-linked |

### Outputs
| Output type | Examples | Where it lands | Notes |
|---|---|---|---|
| Processed datasets | GeoTIFF/COG, GeoJSON, Parquet, CSV | `data/processed/` | Deterministic, replayable |
| STAC catalogs | Collections + Items | `data/stac/` | Must validate (KFM-STAC) |
| DCAT mappings | dataset docs / JSON-LD | `docs/data/` | Must validate (KFM-DCAT) |
| PROV lineage | activity/entity links | files + graph | Must validate (KFM-PROV) |
| Graph entities | Place/Event/Person/Dataset/etc | Neo4j via `src/graph/` | Stable ontology required |
| UI layers | layer registry + tiles/COGs | `web/` + hosted assets | Governed access |
| Story Nodes | versioned narratives | `docs/reports/.../story_nodes/` | Cite every claim |

### Sensitivity & redaction
- Sensitive spatial details (e.g., culturally restricted locations) must be **blurred/generalized** when:
  - Rendering in UI
  - Returning from APIs
  - Writing narrative artifacts
- Redaction must be traceable: record *what was generalized*, *why*, and *under what policy* (link to governance + sovereignty docs).
- If sensitivity requires role-based access, the **API boundary** is the enforcement point (UI must not bypass it).

### Quality signals
- Schema validity (STAC/DCAT/PROV) + link integrity (assets, IDs)
- Geometry validity (GeoJSON/WKT correctness; bbox consistency)
- Provenance completeness (no “orphan” assets without lineage pointers)
- Graph integrity (constraints satisfied; ontology stability maintained)
- API contract conformance (OpenAPI/GraphQL schema + tests)
- UI performance + access control checks (no restricted layers exposed)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC
- Every publishable dataset ships as a **STAC Collection** with one or more **STAC Items** under `data/stac/`.
- Each Item includes: `id`, `geometry`, `bbox`, `datetime`/temporal extent, `assets`, and domain `properties`.
- Asset links (COGs, vector tiles, documents) must be stable, checksummed where feasible, and provenance-linked.
- Use the repo’s **KFM-STAC profile** and pinned validators in CI.

### DCAT
- Maintain interoperable dataset descriptions in `docs/data/` (or generated outputs stored there).
- Minimum metadata expectations: title, description, keywords, license, temporal/spatial coverage, distribution links.
- DCAT should map from STAC where possible to avoid drift and duplication.

### PROV-O
- For every derived artifact, record:
  - `prov:used` (source inputs)
  - `prov:wasGeneratedBy` (ETL job / model / curation activity)
  - `prov:generatedAtTime` (timestamp)
- Persist lineage in both:
  - machine-readable artifacts (e.g., lineage blocks / JSON-LD), and
  - the graph (prov-aligned relationships).

### Versioning
- Dataset updates must preserve traceability:
  - Prefer explicit predecessor/successor linkage (e.g., STAC versioning + graph relations).
  - Enable “lock to version” for reproducibility in analysis and UI rendering.

### Extension points checklist (for future work)
- [ ] New data domain added with `data/raw → work → processed` lifecycle
- [ ] STAC/DCAT/PROV generated + validated for the domain
- [ ] Graph ingest + ontology mapping documented and tested
- [ ] API contract extended (if needed) with tests + docs
- [ ] UI layer registry updated with gating + provenance display
- [ ] Story Node(s) created/updated to explain new capability
- [ ] Telemetry signals defined (schema + dashboard hooks) for observability

---

## 🧠 Story Node & Focus Mode Integration

### How this work surfaces in Focus Mode
- **Story Nodes** are the narrative artifacts that bind data + graph context to human-readable explanations.
- **Focus Mode** is where the system converges:
  - map layers + timeline + entity context,
  - narrative text that is *source-cited*,
  - governance/audit flags for sensitive content.

### Provenance-linked narrative rule
- No narrative content is allowed in Focus Mode unless it is backed by provenance-linked sources.
- If AI-generated insight is displayed:
  - it must be clearly labeled as AI,
  - it must include uncertainty/confidence,
  - and it must link back to the evidence items that support it.

### Optional structured controls
~~~yaml
focus_mode:
  entity_id: "<graph-node-id>"
  time_window: ["YYYY-MM-DD", "YYYY-MM-DD"]
  map_bounds: [minLon, minLat, maxLon, maxLat]
  include_layers:
    - "<layer-id>"
  narrative:
    enabled: true
    ai_opt_in: true
    require_citations: true
    uncertainty_required: true
  governance:
    apply_location_generalization: true
    sensitivity_class: "restricted|open|unknown"
~~~

---

## 🧪 Validation & CI/CD

### Validation steps
- [ ] STAC validation passes (KFM-STAC profile)
- [ ] DCAT validation passes (KFM-DCAT profile)
- [ ] PROV validation passes (KFM-PROV profile)
- [ ] Graph migrations apply cleanly to a test DB; constraints pass
- [ ] API contract tests pass (OpenAPI/GraphQL schema + regression)
- [ ] UI schema checks pass (layer registry, gating, a11y as applicable)
- [ ] No restricted/sensitive coordinates leak in fixtures or snapshots
- [ ] Markdown protocol checks pass (front matter, inner fences, links)

### Reproduction (minimum)
~~~bash
# Replace with repo-standard commands / Make targets.
# Examples (TBD):
# make validate
# make test
# make build
~~~

### Telemetry signals (minimum expectations)
| Signal | Emitted by | Stored in | Why it exists |
|---|---|---|---|
| pipeline_run_id | ETL/catalog jobs | `docs/telemetry/` (and/or structured logs) | Traceability and replay |
| schema_validation_status | CI | CI logs + artifacts | Prevent invalid catalogs |
| provenance_coverage | catalog/graph checks | telemetry | Prevent orphan content |
| sensitive_redaction_events | API/UI | telemetry | Governance enforcement |
| focus_mode_latency | API | telemetry | Performance regression detection |

---

## ⚖ FAIR+CARE & Governance

### Review gates
Changes that require explicit review (minimum):
- New external data sources or domains (ingest expansion)
- New ontology labels/relationships or changes to existing ones
- Any API contract change (REST or GraphQL)
- Any change that affects sensitive location handling / disclosure
- Any change that modifies Focus Mode narrative behavior (especially AI output)

### CARE / sovereignty considerations
- Follow sovereignty policy requirements for culturally sensitive information.
- Prefer *generalization* over *omission* when safe (e.g., county-level rather than exact coordinates).
- Ensure the provenance trail records redaction/generalization decisions and references governing policy.

### AI usage constraints
- AI transforms may summarize/structure/translate/index, but must not:
  - generate new governance policy, or
  - infer sensitive locations.
- AI-generated narrative in Focus Mode must be:
  - opt-in,
  - uncertainty-labeled,
  - and fully citation-backed.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v1.0.0 | 2025-12-18 | Initial GitHub-facing architecture overview (pipeline + contracts + invariants) | TBD |

---

### Footer refs
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
- Master Guide: `docs/MASTER_GUIDE_v12.md`
- Templates: `docs/templates/`