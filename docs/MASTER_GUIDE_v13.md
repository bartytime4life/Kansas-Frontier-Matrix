---
title: "Kansas Frontier Matrix — Master Guide v13 (Draft)"
path: "docs/MASTER_GUIDE_v13.md"
version: "v13.0.0-draft"
last_updated: "2025-12-29"
status: "draft"
doc_kind: "governed_guide"
license: "CC-BY-4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
mcp_version: "KFM-MCP v11.2.6"
ontology_protocol_version: "KFM-ONTO v11.0.0"
pipeline_contract_version: "KFM-PPC v11.0.0"
stac_profile: "KFM-STAC v11.0.0"
dcat_profile: "KFM-DCAT v11.0.0"
prov_profile: "KFM-PROV v11.0.0"
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_policy: "docs/governance/SOVEREIGNTY.md"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "medium"
classification: "public"
jurisdiction: "Kansas"
doc_uuid: "urn:kfm:doc:master-guide:v13.0.0-draft"
semantic_document_id: "kfm-master-guide-v13"
event_source_id: "kfm-docs"
commit_sha: "TBD"
ai_transform_permissions:
  - "summarize"
  - "structure"
  - "extract_checklists"
ai_transform_prohibited:
  - "invent_citations"
  - "hallucinate_data_sources"
doc_integrity_checksum: "sha256:TBD"
---

# Kansas Frontier Matrix — Master Guide v13 (Draft)

> **Governed document.** This file defines the canonical repo structure and pipeline invariants for KFM v13.
>
> Authoring conventions: `docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md` *(not confirmed in repo)*

---

## 📘 Overview

### Purpose

The Master Guide is the **system + pipeline source of truth** for the Kansas Frontier Matrix (KFM). It defines:
- the canonical pipeline stage ordering,
- the required boundary artifacts (STAC/DCAT/PROV + contracts),
- the repo layout and “one canonical home per subsystem” rule,
- the governance gates for sensitive and sovereign content.

This document **supersedes** `docs/MASTER_GUIDE_v12.md` (retained for traceability).

### Scope

This guide governs:
- ETL staging and publication boundaries (`data/raw/` → `data/work/` → `data/processed/` + catalogs),
- STAC/DCAT/PROV alignment requirements and validation gates,
- graph ingest boundary (Neo4j references catalogs, not raw files),
- API boundary (UI never queries Neo4j directly),
- UI integration rules (React/MapLibre; layer registry; access/redaction enforcement),
- Story Nodes + Focus Mode rules (evidence-first; provenance-linked only),
- minimum CI requirements and governance review triggers.

Out of scope:
- detailed implementation specifics for each domain pipeline (those live under `docs/data/<domain>/`),
- UI rendering implementation details (those live in `web/`),
- internal graph data modeling details (those live in `src/graph/` docs / ontology files),
- operational infrastructure details (those live in repo deployment/runbooks if present).

### Audience

Primary:
- KFM data engineering contributors (ETL + catalog generation),
- domain data stewards (source vetting, domain runbooks, governance tagging).

Secondary:
- KFM architects (contracts + system design),
- governance reviewers (FAIR+CARE + sovereignty compliance),
- API and UI contributors (boundary enforcement; redaction; layer registry; accessibility),
- Story/Focus authors and editors (governed narrative integration).

### Definitions

Preferred glossary: `docs/glossary.md` *(not confirmed in repo)*

Key terms used here:
- **ETL**: Extract-Transform-Load
- **STAC**: SpatioTemporal Asset Catalog (collections/items/assets)
- **DCAT**: Data Catalog Vocabulary (dataset discovery metadata)
- **PROV-O**: W3C Provenance Ontology (lineage: entities/activities/agents)
- **Contract-first**: schemas + API contracts are first-class; changes require versioning + compatibility checks
- **Deterministic pipeline**: idempotent, config-driven transforms; stable outputs for stable inputs
- **Story Node**: governed narrative artifact linked to evidence + graph entities
- **Focus Mode**: context presentation mode that only consumes provenance-linked content
- **FAIR+CARE**: findable/accessible/interoperable/reusable + collective benefit/authority/responsibility/ethics

### Key artifacts

| Artifact | Path / Identifier | Owner | Notes |
|---|---|---|---|
| Master Guide (this doc) | `docs/MASTER_GUIDE_v13.md` | TBD | System & pipeline source of truth (supersedes v12) |
| Master Guide v12 (previous) | `docs/MASTER_GUIDE_v12.md` | TBD | Previous canonical guide; retained for traceability |
| Universal doc template | `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md` | Docs | Governed document structure template |
| Story Node template | `docs/templates/TEMPLATE__STORY_NODE_V3.md` | Docs/Story | Governed narrative template (Story + Focus) |
| API contract extension template | `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md` | API | Template for adding/changing endpoints |
| KFM STAC Profile | `docs/standards/KFM_STAC_PROFILE.md` *(not confirmed in repo)* | Standards | Profile + extensions for STAC (v11) |
| KFM DCAT Profile | `docs/standards/KFM_DCAT_PROFILE.md` *(not confirmed in repo)* | Standards | Profile for DCAT (v11) |
| KFM PROV Profile | `docs/standards/KFM_PROV_PROFILE.md` *(not confirmed in repo)* | Standards | Profile for PROV bundles (v11) |
| v13 Redesign Blueprint | `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo)* | Architecture | Design blueprint for v13 restructure |
| Next Stages Blueprint | `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` *(not confirmed in repo)* | Architecture | Roadmap beyond v13 |
| Full Architecture Vision | `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` *(not confirmed in repo)* | Architecture | Long-term end-to-end vision |
| Governance root | `docs/governance/ROOT_GOVERNANCE.md` | Governance | Program governance and review gates |
| Ethics policy | `docs/governance/ETHICS.md` | Governance | Ethical constraints and review expectations |
| Sovereignty policy | `docs/governance/SOVEREIGNTY.md` | Governance | CARE + sovereignty constraints |
| Story Nodes | `docs/reports/story_nodes/` | Docs/Story | Draft and published story node artifacts |

Example domain modules (if present):
- `docs/data/historical/land-treaties/README.md` *(not confirmed in repo)*
- `docs/data/air-quality/README.md` *(not confirmed in repo)*
- `docs/data/soils/sda/README.md` *(not confirmed in repo)*

### Definition of done

This Master Guide is “v13-ready” when:
- [ ] Front-matter complete and valid
- [ ] Canonical pipeline ordering explicitly stated (and matches diagrams)
- [ ] Repo layout includes canonical homes per subsystem (and aligns with project DataOps roots)
- [ ] Any referenced paths that are missing are marked **“not confirmed in repo”**
- [ ] CI gates are specified (at least at a minimum policy level)
- [ ] Governance triggers and sovereignty safety measures are explicit
- [ ] Story Node + Focus Mode rules are hard-gated by provenance and redaction expectations
- [ ] Version history updated

### What KFM is

KFM is a **geospatial + historical “living atlas”**: it ingests and normalizes heterogeneous sources, catalogs them using STAC/DCAT, captures lineage via PROV, links entities in a Neo4j graph, serves governed access via an API layer, and presents map + narrative experiences (Story Nodes and Focus Mode) where every claim is traceable to evidence.

### The canonical pipeline

This ordering is **non-negotiable**:

1. **ETL**: ingest + normalize → `data/raw/<domain>/` → `data/work/<domain>/` → `data/processed/<domain>/`
2. **Catalogs**:
   - **STAC**: collections + items under `data/stac/collections/` and `data/stac/items/`
   - **DCAT**: dataset discovery under `data/catalog/dcat/`
   - **PROV**: lineage bundles under `data/prov/`
3. **Graph**: ingest cataloged outputs into Neo4j (graph references back to catalogs)
4. **API**: governed access boundary (`src/server/`) enforcing contracts + redaction
5. **UI**: React/MapLibre (and optional extensions), consuming only APIs
6. **Story Nodes**: governed narratives linked to evidence and graph entities
7. **Focus Mode**: provenance-linked context bundle only

### What the v13 redesign introduces

v13 is a structural + governance hardening pass:
- **Contract-first**: schemas and API contracts are first-class repo artifacts; changes trigger versioning + compatibility checks.
- **Evidence-first**: Story Nodes and Focus Mode require provenance-linked citations; no unsourced narrative is allowed.
- **One canonical home per subsystem**: reduces repo drift and duplicate implementations.
- **Filled critical structure gaps**: expected top-level directories such as `schemas/`, `releases/`, and catalog/provenance directories are treated as part of the canonical structure (if used).
- **Story content lifecycle**: story content is organized to support a draft → review → published workflow under `docs/reports/story_nodes/`.

---

## 🗂️ Directory Layout

### This document

- Canonical location: `docs/MASTER_GUIDE_v13.md`
- Status: draft
- Supersedes: `docs/MASTER_GUIDE_v12.md`

### Related repository paths (canonical roots)

KFM’s preferred roots (do not break DataOps conventions):
- `.github/`
- `data/`
- `docs/`
- `mcp/`
- `schemas/`
- `src/`
- `tests/`
- `tools/`
- `web/`
- `releases/` *(if used)*

### Repo top-levels (expected structure)

~~~text
📁 .github/
└── 📁 workflows/

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
├── 📄 MASTER_GUIDE_v13.md
├── 📄 MASTER_GUIDE_v12.md
├── 📁 templates/
│   ├── 📄 TEMPLATE__KFM_UNIVERSAL_DOC.md
│   ├── 📄 TEMPLATE__STORY_NODE_V3.md
│   └── 📄 TEMPLATE__API_CONTRACT_EXTENSION.md
├── 📁 standards/
│   ├── 📄 KFM_MARKDOWN_WORK_PROTOCOL.md         # not confirmed in repo
│   ├── 📄 KFM_STAC_PROFILE.md                   # not confirmed in repo
│   ├── 📄 KFM_DCAT_PROFILE.md                   # not confirmed in repo
│   └── 📄 KFM_PROV_PROFILE.md                   # not confirmed in repo
├── 📁 governance/
│   ├── 📄 ROOT_GOVERNANCE.md
│   ├── 📄 ETHICS.md
│   └── 📄 SOVEREIGNTY.md
├── 📁 architecture/
│   ├── 📄 KFM_REDESIGN_BLUEPRINT_v13.md         # not confirmed in repo
│   ├── 📄 KFM_NEXT_STAGES_BLUEPRINT.md          # not confirmed in repo
│   └── 📄 KFM_VISION_FULL_ARCHITECTURE.md       # not confirmed in repo
├── 📁 data/
│   └── 📁 <domain>/
│       └── 📄 README.md
└── 📁 reports/
    └── 📁 story_nodes/
        ├── 📁 draft/
        └── 📁 published/

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

📁 tools/
📁 tests/
📁 web/
📁 releases/    # if used
~~~

### Documentation map (where to look)

- **System/pipeline contracts**: `docs/MASTER_GUIDE_v13.md`
- **Governed doc templates**: `docs/templates/`
- **Standards and profiles**: `docs/standards/`
- **Governance**: `docs/governance/`
- **Architecture references**: `docs/architecture/`
- **Domain runbooks**: `docs/data/<domain>/README.md`
- **Story Nodes**: `docs/reports/story_nodes/`
- **ETL pipelines**: `src/pipelines/`
- **Graph ingestion + ontology**: `src/graph/`
- **API boundary + contracts**: `src/server/`
- **UI application**: `web/`
- **Experiments/run artifacts**: `mcp/runs/` and `mcp/experiments/`

---

## 🧭 Context

### What’s driving the v13 evolution

v13 focuses on maintainability and trust:
- scaling to more domains and more contributors without repo drift,
- enforcing contract-first development (schemas and API contracts precede implementation),
- strengthening evidence-first narrative constraints (no citations → no story),
- ensuring determinism and end-to-end provenance for all published artifacts.

### Key invariants (must not regress)

1) **Pipeline ordering is absolute**  
ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode.  
No stage may consume data that has not passed the prior stage’s formal outputs and checks.

2) **API boundary rule**  
The UI must never query Neo4j directly; all access is mediated via governed APIs (`src/server/`).

3) **Provenance first**  
All published artifacts are registered with STAC/DCAT and PROV before any graph ingestion or story reference.

4) **Deterministic + idempotent ETL**  
Given the same inputs, transforms produce the same output (or differences are logged and explained). Pipelines must be safe to re-run.

5) **Evidence-first narrative**  
No unsourced narrative is allowed in Story Nodes or Focus Mode. AI-generated text must be disclosed and tied to evidence and uncertainty metadata.

6) **Sovereignty + classification propagation**  
No derived output can be less restricted than any upstream input. Redaction/generalization is documented and enforced across processed data, catalogs, APIs, and UI.

7) **Validation gates on contributions**  
CI must reject changes that break schemas, provenance completeness, security scanning, broken links, or governance requirements.

### Future extensions (beyond v13)

These are optional and should be treated as roadmap items:
- richer evidence discovery (evidence panels, uncertainty indicators, provenance popups),
- telemetry-driven governance dashboards and alerting,
- more formal Story Node workflow automation (draft → review → publish with provenance checks),
- release packaging improvements (signed datasets, SBOMs, provenance attestations).

---

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
  H --> I["Map UI — React · MapLibre"]
  I --> J["Story Nodes (governed narratives)"]
  J --> K["Focus Mode (provenance-linked context bundle)"]
~~~

---

## 📦 Data & Metadata

### Data lifecycle (required staging)

- **Staging areas**:
  - Raw inputs: `data/raw/<domain>/`
  - Intermediates: `data/work/<domain>/`
  - Published outputs: `data/processed/<domain>/`

- **Catalog outputs (required boundary artifacts before publication)**:
  - STAC collections: `data/stac/collections/`
  - STAC items: `data/stac/items/`
  - DCAT dataset entries: `data/catalog/dcat/`
  - PROV lineage bundles: `data/prov/`

A dataset is not “published” until all boundary artifacts exist and validate.

### Domain expansion pattern

When adding a new domain:
1. Create a **domain runbook**: `docs/data/<new-domain>/README.md`
   - sources, licensing, governance classification
   - ingestion procedure and validation steps
   - any domain-specific constraints and redaction policies
2. Place raw sources under `data/raw/<new-domain>/`.
3. Implement deterministic ETL under `src/pipelines/<new-domain>/` (or a shared pipeline with domain configs).
4. Write intermediates to `data/work/<new-domain>/` and outputs to `data/processed/<new-domain>/`.
5. Generate catalogs in canonical locations (`data/stac/`, `data/catalog/dcat/`, `data/prov/`).
6. Ingest into graph via `src/graph/` tooling (graph references back to catalog identifiers).
7. Expose via API (`src/server/`) using contracted endpoints and redaction rules.
8. Register UI layers (layer registry + schema validation) and ensure CARE gating.
9. Write Story Nodes using the template and link to evidence + graph entities.

### Evidence artifact pattern (AI/analysis outputs)

KFM treats analysis outputs as first-class datasets:
- stored under `data/processed/…`,
- cataloged in STAC/DCAT,
- lineage captured in PROV (including model/run metadata as required by policy),
- linked into the graph as artifacts,
- referenced by Story Nodes only with explicit citations and uncertainty disclosures.

---

## 🌐 STAC, DCAT & PROV Alignment

### Alignment policy (required)

- Every published dataset must pass schema validation against the KFM STAC/DCAT/PROV profiles.
- No dataset is accepted without valid metadata in all required catalogs.
- Profiles must be extended through standards (not ad-hoc fields) when a domain needs additional metadata.

### Cross-layer linkage expectations

At minimum:
- STAC items reference their assets (files) and stable identifiers.
- DCAT datasets link to STAC collections/items or distributions that resolve to the same canonical dataset.
- PROV bundles connect raw → work → processed outputs and include:
  - activity/run identifiers,
  - agent (pipeline/tool) identifiers,
  - input/output references (hashes or stable IDs).
- Graph nodes reference catalog IDs (not raw file paths).
- APIs serve catalog identifiers and provenance pointers.
- UI shows evidence and provenance affordances; never bypasses redaction gates.

### Versioning expectations

KFM is versioned both at the dataset level and the system level.

**Dataset level**
- Each dataset has a stable identifier and a semantic version.
- New dataset versions should reference predecessors/successors via metadata and PROV.
- Datasets should be reproducible: version + inputs + run config should reproduce the same processed output.
- Changes in derived artifacts (e.g., a corrected polygon) are tracked through PROV and surfaced in catalogs.

**Schema/profile level**
- STAC/DCAT/PROV profiles are versioned (semantic versioning).
- Any schema change that affects validation is a versioned change; breaking changes require coordination and migration paths.

**Graph/ontology level**
- Graph labels/relationships must remain backwards-compatible unless a deliberate migration is performed.
- Ontology changes require migration scripts and must be documented in version history.

**API level**
- Breaking API changes require versioned endpoints or explicit deprecation plans.
- OpenAPI/GraphQL definitions are contracts; breaking the contract implies a version increment.

**Release level**
- Repository releases follow semantic versioning.
- Major versions (like v13) indicate structural changes; minor versions add compatible features.
- Master Guide updates must reflect release changes.

---

## 🧱 Architecture

### Subsystem contracts (expectations per subsystem)

Each pipeline stage has contract artifacts and invariants:

| Subsystem | Contract artifacts (must exist) | “Do not break” rule |
|---|---|---|
| ETL | pipeline configs; run logs; validation reports | deterministic + replayable runs; stable outputs given stable inputs |
| Catalogs | JSON schemas for STAC/DCAT/PROV; automated validators | no dataset accepted without valid metadata |
| Graph | ontology definitions; migrations; constraints | stable graph schema; changes require explicit migrations |
| APIs | OpenAPI/GraphQL schema; contract tests | backwards-compatible unless version bump declared |
| UI | layer registry; accessibility audits; audit affordances | no data leakage; respects redaction rules; a11y compliance |
| Story/Focus | Story Node templates + schemas; Focus Mode bundle definition | provenance-linked only; no hallucinated/unsourced claims |

### Canonical subsystem homes (one home per subsystem)

- Pipelines (ETL): `src/pipelines/`
- Catalog build/validation tooling: `tools/` and/or `src/pipelines/` (**pick one canonical home; avoid duplicates**)
- Graph build/ingest: `src/graph/`
- API boundary: `src/server/` (contracts under `src/server/contracts/**` if present)
- UI: `web/`
- Schemas: `schemas/` (contract-first: schemas live here, referenced by tools/CI)

### Next-evolution extension points (where to add new capability)

- (A) Data: new domain, new metadata profile extensions (via standards)
- (B) AI evidence: artifacts as STAC assets, linked into Focus Mode
- (C) Graph: new entity types with explicit provenance + ontology mapping
- (D) API: new endpoints with contract tests + redaction rules
- (E) UI: new layer registry entries with provenance pointers + CARE gating

---

## 🧠 Story Node & Focus Mode Integration

### Story Nodes as “machine-ingestible storytelling”

Story Nodes must:
- follow the governed template,
- carry provenance annotations and explicit citations to cataloged artifacts,
- connect to graph entities (Place/Person/Event/Document/etc.) via stable identifiers,
- separate **fact vs inference vs hypothesis**, especially when AI-generated text is used.

In the UI, Story Nodes are shown alongside the map; citations should be clickable and capable of surfacing relevant evidence (catalog metadata, source excerpts, linked map highlights) without bypassing redaction or classification gates.

### Focus Mode rule (hard gate)

- Focus Mode consumes **provenance-linked** content only.
- Any predictive/suggestive content must be:
  - opt-in,
  - accompanied by uncertainty/confidence metadata,
  - prevented from inferring or revealing sensitive locations.

### Story lifecycle (draft → published)

Recommended structure:
- Drafts: `docs/reports/story_nodes/draft/`
- Published: `docs/reports/story_nodes/published/`

Publishing a Story Node should require:
- schema validation + link checks,
- governance review if sensitive or sovereign topics are implicated,
- confirmation that every claim is backed by cataloged evidence.

---

## 🧪 Validation & CI/CD

### Minimum CI gates for v13 contributions

At minimum, CI should enforce:
- Markdown protocol validation (front-matter + required sections)
- Link/reference checks (no orphan pointers; missing files must be marked “not confirmed in repo”)
- JSON schema validation:
  - STAC/DCAT/PROV
  - story node schemas (if present)
  - telemetry schemas (if present)
  - UI layer registry schemas (if present)
- Graph integrity tests (constraints; expected labels/edges)
- API contract tests (OpenAPI/GraphQL schema + resolver tests)
- Security + sovereignty scanning gates (as applicable):
  - secret scan
  - PII scan
  - sensitive-location leakage checks
  - classification propagation checks (no downgrades without review)

### Telemetry signals (recommended)

Suggested events:
- `classification_assigned` (dataset_id, sensitivity, classification)
- `redaction_applied` (method, fields_removed, geometry_generalization)
- `promotion_blocked` (reason, scan_results_ref)
- `catalog_published` (scope, counts, validation_status)
- `focus_mode_redaction_notice_shown` (layer_id, redaction_method)

### Release integrity (optional; at release time)

If the project produces official releases:
- signed artifacts,
- SBOMs,
- provenance attestations,

…these occur at release time rather than on every PR.

---

## ⚖ FAIR+CARE & Governance

### Governance review triggers

Manual review is required for:
- introducing sensitive data/layers (especially sovereign or culturally sensitive content),
- new AI-driven narrative features that could be interpreted as factual,
- new external data sources (license/provenance review),
- new public-facing endpoints or UI features that could expose sensitive info,
- any classification/sensitivity change or new sensitivity rules.

Reviews should be documented in `docs/governance/REVIEW_GATES.md` *(if present; not confirmed in repo)*.

### Sovereignty and safety measures

- **Redaction and generalization must be documented and enforced end-to-end**:
  - in processed datasets (`data/processed/**`),
  - in catalogs (STAC/DCAT flags and notes),
  - in API responses (server-side redaction policies),
  - and in UI rendering (CARE gating; client-side safeguards where needed).
- **No output may be less restricted than any upstream input** in its lineage.

---

## 🕰️ Version History

| Version | Date | Summary | Author |
|---|---|---|---|
| v13.0.0-draft | 2025-12-29 | Initial scaffolding of Master Guide v13 (contract-first + evidence-first; canonical directory layout; supersedes v12) | TBD |
| v12.0.1-draft | 2025-12-27 | Refined v12 to align with Universal Doc template; clarified invariants and boundaries | TBD |
| v12.0.0-draft | 2025-12-17 | Initial scaffolding of Master Guide v12 | TBD |

---

## 📚 References and Source Library

### Canonical repo references (must-read)

- Master Guide template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`

### Architecture references (draft targets)

- v13 redesign blueprint: `docs/architecture/KFM_REDESIGN_BLUEPRINT_v13.md` *(not confirmed in repo)*
- Next stages blueprint: `docs/architecture/KFM_NEXT_STAGES_BLUEPRINT.md` *(not confirmed in repo)*
- Full architecture & vision: `docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md` *(not confirmed in repo)*

### Project source library used to compile this guide (not necessarily committed)

KFM design/system docs:
- “Kansas Frontier Matrix (KFM) Implementation Guide”
- “Kansas Frontier Matrix_ System Structure and Scope”
- “Kansas Frontier Matrix (KFM) System – Visual and Functional Overview”
- “Data Intake Design KFM”
- “Elevating the Kansas Frontier Matrix: Gaps and Proposed Enhancements”
- “Kansas Frontier Matrix – Architecture & Design Audit (v12_v13)”
- “Kansas Frontier Matrix — v13 Redesign Blueprint”
- “KFM Reference Data”

General/technical reference library:
- “Comprehensive Guide to Markdown in Programming and Documentation”
- “The Comprehensive Markdown Guide”
- “Git Notes for Professionals”
- “PostgreSQL Notes for Professionals”, “MySQL Notes for Professionals”
- “Node.js Notes for Professionals”
- “CSS Notes for Professionals”
- “Geoprocessing with Python”, “Python Geospatial Analysis Cookbook”
- “An Introduction to Spatial Data Analysis and Visualisation in R”, “graphical-data-analysis-with-r”
- “Data Science & Machine Learning (Mathematical & Statistical Methods)”
- “Regression Analysis with Python”
- “Bayesian computational methods”
- “Data Mining Concepts & applications”
- “Artificial neural networks — an introduction”
- “AI Foundations of Computational Agents (3rd Ed)”
- “Scalable Data Management for Future Hardware”
- “Spectral Geometry of Graphs”
- “WebGL Programming Guide”, “Computer Graphics using Java 2D & 3D”
- “Designing Virtual Worlds”
- “Scientific Modeling and Simulation — NASA-grade guide”

---

Footer refs:
- Master guide template: `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- Story node template: `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- API contract extension template: `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance: `docs/governance/ROOT_GOVERNANCE.md`
- Ethics: `docs/governance/ETHICS.md`
- Sovereignty: `docs/governance/SOVEREIGNTY.md`
---