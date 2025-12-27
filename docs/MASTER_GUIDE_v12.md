---
title: "Kansas Frontier Matrix — Master Guide v12 (Draft)"
path: "docs/MASTER_GUIDE_v12.md"
version: "v12.0.1-draft"
last_updated: "2025-12-27"
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

doc_uuid: "urn:kfm:doc:master-guide:v12.0.1-draft"
semantic_document_id: "kfm-master-guide-v12.0.1-draft"
event_source_id: "ledger:kfm:doc:master-guide:v12.0.1-draft"
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

# Kansas Frontier Matrix — Master Guide v12 (Draft)

## 📘 Overview

### Purpose

- Define the **canonical ordering** of the Kansas Frontier Matrix (KFM) pipeline and the **non-negotiable contracts** at each boundary (data → catalogs → graph → API → UI → narrative).
- Act as the **repo-level source of truth** for:
  - canonical subsystem homes (one place per subsystem),
  - provenance-first publishing (STAC/DCAT/PROV before narrative),
  - governance and sovereignty guardrails that apply across all domains.

### Scope

| In Scope | Out of Scope |
|---|---|
| Canonical pipeline ordering; canonical repository placement; cross-cutting invariants (provenance, determinism, API boundary); extension rules (new datasets, evidence products, narratives); minimum validation/CI expectations; references to governing templates and design docs. | Low-level implementation details; cloud/ops deployment specifics; domain-specific ETL recipes beyond the standardized pattern; uncited historical interpretation (belongs in Story Nodes with evidence). |

### Audience

- Primary: contributors implementing/maintaining **ETL, catalogs, graph/ontology, APIs, UI, Story Nodes, Focus Mode**.
- Secondary: domain stewards (historians/scientists), governance reviewers, and narrative editors who need to understand what “governed” means in practice.

### Definitions (link to glossary)

- Link: `docs/glossary.md` *(not confirmed in repo; recommended)*.
- Terms used in this doc:
  - **Catalogs**: STAC (assets), DCAT (dataset/distribution discovery), PROV (lineage).
  - **Evidence artifact**: any derived analysis/model output that is treated as **data + metadata** (STAC/DCAT/PROV) before it appears in UI or narrative.
  - **Story Node**: a governed narrative artifact that is machine-ingestible and provenance-linked.
  - **Focus Mode**: an experience that consumes only provenance-linked context bundles (no unsourced narrative).
  - **Contract-first**: schemas + API contracts are first-class artifacts; breaking changes require versioning/compat tests.
  - **Deterministic pipeline**: idempotent, config-driven transforms with logged inputs/outputs and stable IDs.

### Key artifacts (what this doc points to)

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (this doc) | `docs/MASTER_GUIDE_v12.md` | TBD | System + pipeline source of truth |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Default governed doc template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Narrative + Focus Mode surfacing |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | REST/GraphQL contract changes |
| v13 redesign blueprint (draft) | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` | Architecture | Consolidates “one canonical home”, contract-first, evidence-first |
| Next stages blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` | Architecture | Roadmap + gap closure plan |
| Full architecture & vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` | Architecture | End-to-end vision |
| Land Treaties module | `docs/data/historical/land-treaties/README.md` | Domain steward | Example domain module (governance-sensitive) |
| Air Quality module | `docs/data/air-quality/README.md` | Domain steward | Example domain module |
| Soils (SDA) module | `data/soils/sda/README.md` | Domain steward | Example domain module |
| Markdown work protocol | `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` | Docs | *not confirmed in repo* |

### Definition of done (for this document)

- [ ] Front-matter complete + valid
- [ ] All claims link to datasets / schemas / tickets / commits (as applicable)
- [ ] Validation steps listed and repeatable
- [ ] Governance + CARE/sovereignty considerations explicitly stated

### What KFM is (one paragraph)

KFM is an open-source **geospatial + historical** knowledge system (a “living atlas” of Kansas) that ingests heterogeneous sources, publishes governed metadata catalogs (STAC/DCAT/PROV), builds a semantically structured Neo4j graph, and serves evidence through contracted APIs into a map + narrative UI. KFM is designed so that **every narrative claim can be traced to versioned evidence**, and every derived product has explicit lineage.

### The canonical pipeline (non-negotiable ordering)

- **ETL → STAC/DCAT/PROV catalogs → Neo4j graph → APIs → React/Map UI → Story Nodes → Focus Mode**

### What “v12 evolution” means

- A documentation + contracts evolution that:
  - keeps earlier artifacts stable where possible,
  - promotes **contract-first + evidence-first** expectations,
  - adds explicit extension points for new domains, AI evidence artifacts, and narrative UX.

### System inventory (index)

| System / Area | Canonical location | What it governs |
|---|---|---|
| Data staging | `data/raw/` · `data/work/` · `data/processed/` | Deterministic ingestion, normalized outputs |
| STAC | `data/stac/` | Collections + Items for spatiotemporal assets |
| DCAT | `data/catalog/dcat/` | Dataset/distribution discovery views |
| PROV | `data/prov/` | Lineage bundles (activities/entities/agents); run traceability |
| Graph | `src/graph/` | Ontology bindings, ingest/migrations, integrity constraints |
| Pipelines | `src/pipelines/` | ETL jobs, transforms, catalog builders, graph loaders |
| APIs | `src/server/` | Contracted access layer (REST/GraphQL); redaction enforcement |
| Frontend | `web/` | React + MapLibre (+ optional Cesium); layer registry; Focus Mode UX |
| Story Nodes | `docs/reports/story_nodes/` *(pattern)* | Narrative artifacts + provenance annotations |
| Telemetry | `schemas/telemetry/` + `docs/telemetry/` *(if present)* | Observability + governance signals |
| Security | `.github/` + `docs/security/` *(if present)* | CI gates, security standards |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs; provenance pointers |

### “Extension Matrix” (how new capabilities get added)

| Extension | Data | Catalog | Graph | API | UI | Story/Focus | Telemetry |
|---|---|---|---|---|---|---|---|
| New dataset | ✓ | ✓ | optional | optional | optional | optional | optional |
| New analysis product (e.g., evidence artifacts) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| New narrative node type | optional | optional | ✓ | ✓ | ✓ | ✓ | ✓ |
| New security / governance gate | — | — | — | — | — | — | ✓ |

## 🗂️ Directory Layout

### This document

- `path`: `docs/MASTER_GUIDE_v12.md` *(must match front-matter)*

### Related repository paths

| Area | Path | What lives here |
|---|---|---|
| Data domains | `data/` | Staged data + catalog outputs (STAC/DCAT/PROV) |
| Documentation | `docs/` | Canonical governed docs (guides, designs, domain notes) |
| Templates | `docs/templates/` | Governed doc templates (universal/story/API) |
| Architecture | `docs/architecture/` | System designs, roadmaps, ADRs (if present) |
| Schemas | `schemas/` | JSON Schemas (STAC/DCAT/PROV/story/ui/telemetry) |
| Pipelines | `src/pipelines/` | ETL + catalog generation code |
| Graph | `src/graph/` | Ontology bindings + graph build/migrations |
| API boundary | `src/server/` | API service + contracts + redaction logic |
| UI | `web/` | React + map client + Focus Mode UI |
| MCP | `mcp/` | Experiments, runs, model cards, SOPs |
| Tests | `tests/` | Unit + integration tests |
| Tools | `tools/` | Validators, utilities, QA scripts |
| CI | `.github/` | Workflows + policy gates |
| Releases | `releases/` | Versioned packaged artifacts (if used) |

### Repo top-levels (expected)

~~~text
📁 .github/
├── 📁 workflows/
└── 📄 SECURITY.md                         # if present

📁 data/
├── 📁 raw/
│   └── 📁 <domain>/
├── 📁 work/
│   └── 📁 <domain>/
├── 📁 processed/
│   └── 📁 <domain>/
├── 📁 stac/
│   ├── 📁 collections/
│   └── 📁 items/
├── 📁 catalog/
│   └── 📁 dcat/
└── 📁 prov/

📁 docs/
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md
├── 📁 data/
│   └── 📁 <domain>/
└── 📁 reports/
    └── 📁 story_nodes/                    # pattern; draft/published split if defined

📁 mcp/
├── 📁 runs/
└── 📁 experiments/

📁 schemas/
├── 📁 stac/
├── 📁 dcat/
├── 📁 prov/
├── 📁 story_nodes/
├── 📁 ui/
└── 📁 telemetry/

📁 src/
├── 📁 pipelines/
├── 📁 graph/
└── 📁 server/

📁 web/
📁 tests/
📁 tools/
📁 releases/
~~~

### Documentation map

- `docs/MASTER_GUIDE_v12.md` (this guide)
- `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` (draft reference; if adopted)
- `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` (roadmap)
- `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` (vision)
- `docs/standards/` (governed standards; *some items not confirmed in repo*)
- `docs/templates/` (document + MCP templates)

## 🧭 Context

### What’s driving the next evolution

- Scaling to more domains and evidence products, while preserving provenance and sovereignty guardrails.
- Reducing “repo drift” by enforcing **one canonical home per subsystem** and making **schemas/contracts** first-class.

### Key invariants (must not regress)

- **Pipeline ordering is non-negotiable:** ETL → Catalogs → Graph → API → UI → Story Nodes → Focus Mode.
- **API boundary:** the UI never reads Neo4j directly; all access is via contracted APIs.
- **Provenance first:** STAC/DCAT/PROV are produced and validated before graph ingest and before UI/narrative surfacing.
- **Determinism:** ETL and transforms are config-driven, idempotent, logged, and reproducible (hash inputs/outputs).
- **Evidence-first narrative:** no unsourced narrative in Story Nodes or Focus Mode.
- **Sovereignty and classification propagation:** no output is less restricted than any input in its lineage; interactive UI must not leak sensitive locations by zoom/interaction.

### Future extensions (tracked here; details in subsystem docs)

- Candidate discovery outputs (evidence panels, provenance-linked assets, audit flags).
- Stronger telemetry governance signals (classification events, redaction applied, publication gates).
- Expanded story node ingestion/versioning (draft → published workflow, with provenance checks).

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  subgraph Data
    A["Raw Sources"] --> B["ETL + Normalization"]
    B --> C["STAC Items + Collections"]
    C --> D["DCAT Dataset Views"]
    C --> E["PROV Lineage Bundles"]
  end

  C --> G["Neo4j Graph (references back to catalogs)"]
  G --> H["API Layer (contracts + redaction)"]
  H --> I["Map UI — React · MapLibre · (optional) Cesium"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked context bundle)"]
~~~

## 📦 Data & Metadata

### Data lifecycle (required staging)

- `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
- Catalog outputs (boundary artifacts):
  - STAC: `data/stac/collections/` + `data/stac/items/`
  - DCAT: `data/catalog/dcat/`
  - PROV: `data/prov/`

### Domain expansion pattern

- New domains should:
  - stage their data under `data/raw/<domain>/`, `data/work/<domain>/`, `data/processed/<domain>/`,
  - publish STAC/DCAT/PROV artifacts in canonical catalog locations,
  - maintain a domain runbook under `docs/data/<domain>/` (or a consistent equivalent) and link it here.

### Evidence artifact pattern (AI/analysis outputs)

- Evidence artifacts are treated like datasets:
  - generated into `data/processed/<domain>/...`,
  - cataloged (STAC/DCAT) and traced (PROV),
  - optionally linked into the graph as nodes/relationships with explicit provenance,
  - exposed only via APIs that implement redaction and classification rules.

## 🌐 STAC, DCAT & PROV Alignment

### STAC/DCAT/PROV alignment policy (required)

Every new dataset or evidence artifact must have:

- **STAC Collection + Item(s)** (for spatiotemporal assets)
- **DCAT mapping** (minimum title/description/license/keywords + distributions)
- **PROV activity bundle** describing the transformation that produced the outputs (inputs, parameters, tool/run IDs, hashes)

### Cross-layer linkage expectations

- STAC Items must point to assets in `data/processed/**` (or stable storage) and carry license/source attribution.
- DCAT distributions should reference the STAC catalog (or the underlying distribution) for discovery.
- PROV must link raw → work → processed and identify the pipeline/run that created each artifact.
- The graph should reference catalog identifiers (STAC/DCAT IDs and/or stable artifact IDs) rather than duplicating large payloads.

### Versioning expectations

- New versions link predecessor/successor in catalogs and PROV.
- Graph mirrors version lineage (do not break stable labels/edges without an explicit migration/version bump).
- API-breaking changes require versioned endpoints or explicit compatibility strategy.

## 🧱 Architecture

### Subsystem contracts (what must exist for each subsystem)

| Subsystem | Contract artifacts | “Do not break” rule |
|---|---|---|
| ETL | configs + run logs + validation notes | deterministic + replayable |
| Catalogs | STAC/DCAT/PROV schemas + validators | machine-validated outputs |
| Graph | ontology + migrations + constraints | stable labels/edges (unless migrated) |
| APIs | OpenAPI/GraphQL schema + contract tests | backwards compatible or version bump |
| UI | layer registry + a11y + audit affordances | no hidden data leakage |
| Story/Focus | provenance-linked context bundle | no hallucinated/unsourced claims |

### Canonical subsystem homes (one home per subsystem)

- Pipelines: `src/pipelines/`
- Catalog build/validation tooling: `tools/` and/or `src/pipelines/` (keep one canonical home)
- Graph build: `src/graph/`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- UI: `web/`

### Next-evolution extension points (where to add new capability)

- (A) Data: new domain, new STAC extension profiles (if required)
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types with explicit provenance + ontology mapping
- (D) API: new endpoints with contract tests + redaction rules
- (E) UI: new layer registry entries with provenance pointers + CARE gating

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

- Story Nodes must:
  - carry provenance annotations and explicit citations to cataloged artifacts,
  - connect to graph entities (Place/Person/Event/Document/etc.) via stable identifiers,
  - separate fact vs inference vs hypothesis where applicable (especially for AI-generated text).

### Focus Mode rule (hard gate)

- Focus Mode only consumes **provenance-linked** content.
- Any predictive/suggestive content:
  - must be opt-in,
  - must carry uncertainty/confidence metadata,
  - must not infer or reveal sensitive locations.

## 🧪 Validation & CI/CD

### Minimum CI gates for “v12-ready” contributions

- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers)
- JSON schema validation:
  - STAC/DCAT/PROV
  - story node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- Graph integrity tests (constraints, expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Telemetry signals (recommended)

- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

## ⚖ FAIR+CARE & Governance

### Governance review triggers

- New sensitive layers or any content intersecting sovereignty obligations
- New AI narrative behaviors or automated summarization that could be interpreted as “fact”
- New external data sources (license/provenance review)
- New public-facing endpoints or layer interactions that could reveal sensitive locations
- Any classification/sensitivity change or publication derived from restricted inputs

### Sovereignty safety

- Redaction/generalization must be documented and enforced:
  - in datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT),
  - in API responses (redaction policies),
  - and in UI rendering (CARE gating).
- No output may be less restricted than any upstream input in its lineage.

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v12.0.1-draft | 2025-12-27 | Refined to align with Universal Doc template structure; clarified canonical paths, invariants, and contract-first/evidence-first boundaries | TBD |
| v12.0.0-draft | 2025-12-17 | Initial scaffolding | TBD |

---
Footer refs:
- Master guide template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- v13 redesign blueprint (draft reference): `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md`
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md`
- Full architecture & vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---
