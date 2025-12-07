---
title: "📑 KFM Lineage — PROV-O Export Standard"
path: "docs/standards/lineage/prov-o-export/README.md"
version: "v0.1.0"
last_updated: "2025-12-07"
release_stage: "Draft / For Review"
lifecycle: "Planned Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "draft"
commit_sha: "<pending-commit-sha>"
signature_ref: "releases/lineage-prov-o-export/v0.1.0/signature.sig"
attestation_ref: "releases/lineage-prov-o-export/v0.1.0/slsa-attestation.json"
sbom_ref: "releases/lineage-prov-o-export/v0.1.0/sbom.spdx.json"
manifest_ref: "releases/lineage-prov-o-export/v0.1.0/manifest.zip"
telemetry_ref: "releases/lineage-prov-o-export/v0.1.0/lineage-telemetry.json"
telemetry_schema: "schemas/telemetry/lineage-prov-o-export-v0.1.0.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
status: "Draft / Proposed"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
scope:
  domain: "lineage"
  applies_to:
    - "prov-o-export"
    - "lineage-graph"
    - "etl-pipelines"
semantic_intent:
  - "lineage"
  - "export"
  - "governance"
category: "Lineage · PROV-O · Standards"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded when KFM-PROV Export v1.x is adopted"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"
  geosparql: "geo:FeatureCollection"
metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"
provenance_chain: []
provenance_requirements:
  versions_required: false
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: false
json_schema_ref: "schemas/json/kfm-lineage-prov-o-export-v0.1.0.schema.json"
shape_schema_ref: "schemas/shacl/kfm-lineage-prov-graph-v0.1.0-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:lineage:prov-o-export:v0.1.0"
semantic_document_id: "kfm-lineage-prov-o-export-v0.1.0"
event_source_id: "ledger:kfm:doc:standards:lineage:prov-o-export:v0.1.0"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "3d-context-render"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
transform_registry:
  allowed:
    - summary
    - timeline-generation
    - semantic-highlighting
    - 3d-context-render
    - a11y-adaptations
    - diagram-extraction
    - metadata-extraction
  prohibited:
    - content-alteration
    - speculative-additions
    - unverified-architectural-claims
    - narrative-fabrication
    - governance-override
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
heading_registry:
  approved_h2:
    - "📘 Overview"
    - "🗂️ Directory Layout"
    - "🧭 Context"
    - "🗺️ Diagrams"
    - "🧠 Story Node & Focus Mode Integration"
    - "🧪 Validation & CI/CD"
    - "📦 Data & Metadata"
    - "🌐 STAC, DCAT & PROV Alignment"
    - "🧱 Architecture"
    - "⚖ FAIR+CARE & Governance"
    - "🕰️ Version History"
test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "footer-check"
  - "accessibility-check"
  - "diagram-check"
  - "metadata-check"
  - "provenance-check"
  - "prov-export-contract"
  - "prov-graph-consistency"
ci_integration:
  workflow: ".github/workflows/kfm-ci.yml"
  environment: "dev → staging → production"
branding_registry:
  standard: "Scientific Insight × FAIR+CARE Ethics × Sustainable Intelligence"
  architecture: "Designed for Longevity · Governed for Integrity"
  analysis: "Research-Driven · Evidence-Led · FAIR+CARE Grounded"
  data-spec: "Open Data × Responsible Stewardship"
  pipeline: "Deterministic Pipelines · Explainable AI · Open Provenance"
  telemetry: "Transparent Systems · Ethical Metrics · Sustainable Intelligence"
  graph: "Semantics × Provenance × Spatial Intelligence"
layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true
deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 📑 **KFM Lineage — PROV-O Export Standard (Draft v0.1.0)**  
`docs/standards/lineage/prov-o-export/README.md`

**Purpose:**  
Define the canonical, CI-enforced pattern for exporting Kansas Frontier Matrix (KFM) lineage into **W3C PROV-O** graphs, aligned with **DCAT 3.0**, **STAC 1.x**, and **KFM-MDP v11.2.4**.  
This standard specifies how ETL runs, catalog records, knowledge-graph operations, and documents are turned into deterministic, queryable PROV-O entities, activities, and agents for downstream analysis and Focus Mode overlays.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-informational "Markdown Protocol v11.2.4")]() ·
[![PROV-O](https://img.shields.io/badge/Provenance-W3C_PROV--O-purple "W3C PROV-O")]() ·
[![DCAT 3.0](https://img.shields.io/badge/Metadata-DCAT_3.0-teal "W3C DCAT 3.0")]() ·
[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange "Draft / For Review")]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

This standard governs how **lineage information** is exported from KFM into **PROV-O RDF graphs** and related serializations.

It covers:

- ETL and data pipelines (batch + streaming) that produce or transform datasets.
- Catalog-level metadata in **DCAT 3.0** and **STAC 1.x**.
- Graph loading and enrichment operations in Neo4j and related services.
- Documentation artifacts governed by **KFM-MDP v11.2.4**.
- The mapping of all of the above to **PROV-O Entities, Activities, Agents, Plans, Bundles**.

The goal is a **deterministic, reproducible export pipeline** that produces:

- Machine-readable lineage graphs (Turtle, JSON-LD, PROV-JSON).
- Graphs validated against **PROV-O**, **KFM-PROV v11**, and local SHACL shapes.
- Artifacts ready for ingestion into triple stores and/or Neo4j-backed lineage views.
- Lineage overlays for Focus Mode that never override authoritative content.

This document is **Draft / Proposed** and MUST be reviewed and approved before being marked **Active / Enforced**.

### 2. Core Principles

1. **Deterministic Lineage**  
   Every exported PROV-O graph MUST be reproducible from:
   - a pinned ETL config (YAML/JSON),
   - a git commit SHA,
   - versioned datasets and schemas.

2. **Single Lineage Model**  
   All provenance MUST be representable in the PROV-O **Entity–Activity–Agent** pattern, with optional Plans and Bundles, avoiding ad-hoc custom vocabularies where PROV already provides suitable terms.

3. **Interoperable Catalogs**  
   Lineage exports MUST link back to DCAT and STAC identifiers for datasets, distributions, items, and services, keeping catalog and provenance views in sync.

4. **Graph-First Semantics**  
   PROV-O exports MUST be ingestible by both RDF triple stores and KFM’s Neo4j lineage graph, enabling:
   - lineage queries,
   - impact analysis,
   - temporal reasoning (with OWL-Time),
   - spatial overlays (with GeoSPARQL).

5. **FAIR+CARE-Aligned Lineage**  
   Lineage MUST describe relationships and processes, not leak sensitive content. It MUST respect Indigenous data sovereignty and privacy rules, while still supporting discoverability and reuse.

6. **CI-Enforced**  
   No lineage export is considered valid until PROV-O schema checks, SHACL validation, and lineage-specific CI tests pass in `.github/workflows/kfm-ci.yml`.

### 3. Where This Work Lives (Monorepo Surfaces)

This standard directly impacts:

- **Docs**
  - `docs/standards/lineage/prov-o-export/README.md` (this file; normative export rules).
  - `docs/standards/lineage/README.md` (lineage standards index; proposed).
  - `docs/architecture/lineage/prov-graph.md` (lineage graph design; proposed).
  - `docs/guides/lineage/prov-o-export-cli.md` (CLI usage; proposed).

- **Pipelines**
  - `src/pipelines/lineage/prov_export/`
    - `config/` — YAML/JSON export configs per dataset/domain.
    - `jobs/` — deterministic export jobs (batch + streaming).
    - `cli.py` — `kfm-provenance export` entrypoint.

- **Graph & API**
  - `src/graph/lineage/prov/` — Neo4j loaders and query helpers for lineage views.
  - `src/api/lineage/prov/` — REST/GraphQL endpoints exposing lineage slices.

- **Data & Catalogs**
  - `data/processed/lineage/prov/` — PROV-O export artifacts (TTL, JSON-LD, PROV-JSON).
  - `data/releases/lineage/prov/` — versioned release bundles.
  - `data/stac/lineage/` — STAC Collections/Items for provenance assets.
  - `data/sources/dcat/` — DCAT entries referencing provenance datasets.

Implementers MUST ensure these paths exist (or update this document and the schemas accordingly) before promoting this standard to **Active / Enforced**.

### 4. Author Quickstart (for Lineage Docs)

When writing documentation related to PROV-O export:

1. Start from a **KFM-MDP v11.2.4**-compliant template (Standard or Guide).
2. Use only approved H2 headings from `heading_registry.approved_h2`.
3. Explicitly reference:
   - this standard for export rules,
   - the DCAT and STAC guides for catalog mapping,
   - the PROV-O guide for provenance modeling.
4. Always state:
   - which pipelines produce lineage,
   - where exported graphs are stored,
   - how they are validated in CI.

---

## 🗂️ Directory Layout

### 1. Global Monorepo Layout (Canonical)

The KFM lineage components live inside the standard monorepo structure:

~~~text
KansasFrontierMatrix/
├── 📂 docs/                                  # All documentation
│   ├── 📂 standards/                         # Standards & policies (Markdown, FAIR+CARE, governance, etc.)
│   │   └── 📂 lineage/                       # Lineage standards (this standard + siblings)
│   │       ├── 📄 README.md                  # Lineage standards index (proposed)
│   │       └── 📂 prov-o-export/
│   │           └── 📄 README.md              # This PROV-O export standard
│   ├── 📂 architecture/                      # System & subsystem designs (ETL, graph, API, UI, Focus Mode)
│   │   └── 📂 lineage/
│   │       └── 📄 prov-graph.md              # PROV graph & storage design (proposed)
│   ├── 📂 guides/                            # How-to guides, tutorials, SOP-style walkthroughs
│   │   └── 📂 lineage/
│   │       └── 📄 prov-o-export-cli.md       # CLI usage & examples (proposed)
│   ├── 📂 data/                              # Data contracts, source registries, schema notes
│   ├── 📂 analyses/                          # Domain analyses & case studies
│   └── 📄 glossary.md                        # Shared glossary for KFM-wide terminology
├── 📂 src/                                   # Backend & service code
│   ├── 📂 pipelines/
│   │   └── 📂 lineage/
│   │       └── 📂 prov_export/
│   │           ├── 📂 config/                # YAML/JSON export configs
│   │           ├── 📂 jobs/                  # Batch / streaming export jobs
│   │           └── 📄 cli.py                 # `kfm-provenance export` entrypoint
│   ├── 📂 graph/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           ├── 📄 neo4j_loader.py        # Load PROV into Neo4j
│   │           └── 📄 queries.cyp            # Standard lineage queries
│   ├── 📂 api/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           └── 📄 router.py              # REST/GraphQL lineage endpoints
│   └── 📂 tools/                             # Backend utilities, CLIs, migrations
├── 📂 data/                                  # Data lifecycle: raw → work → processed → releases
│   ├── 📂 sources/                           # External dataset manifests (STAC/DCAT-aligned)
│   ├── 📂 raw/                               # Raw ingested data (LFS/DVC; not committed directly)
│   ├── 📂 work/                              # Intermediate normalized / enriched data
│   ├── 📂 processed/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           ├── 📂 ttl/                   # PROV-O Turtle exports
│   │           ├── 📂 jsonld/                # PROV-O JSON-LD exports
│   │           └── 📂 provjson/              # PROV-JSON exports
│   ├── 📂 releases/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           └── 📂 v*/                    # Versioned lineage release bundles
│   └── 📂 stac/
│       └── 📂 lineage/
│           └── 📂 collections/               # STAC Collections for provenance assets
├── 📂 schemas/                               # JSON, JSON-LD, STAC, DCAT, SHACL, telemetry schemas
│   ├── 📂 json/
│   │   └── 📄 kfm-lineage-prov-o-export-v0.1.0.schema.json
│   └── 📂 shacl/
│       └── 📄 kfm-lineage-prov-graph-v0.1.0-shape.ttl
├── 📂 mcp/                                   # Master Coder Protocol artifacts
│   ├── 📂 experiments/
│   ├── 📂 model_cards/
│   └── 📂 sops/
├── 📂 tests/                                 # Automated test suites (unit, integration, lineage checks)
├── 📂 tools/                                 # Repo-level tools, dev utilities, maintenance scripts
└── 📂 .github/                               # CI/CD workflows & GitHub configuration
    └── 📂 workflows/
        └── 📄 kfm-ci.yml                     # CI pipelines (docs-lint, lineage-audit, energy/carbon)
~~~

**Author and Implementer Rules:**

- Every directory above MUST eventually have a `README.md` (or equivalent) describing its purpose and data/contracts.
- Any deviation from these paths MUST be reflected here and in the JSON/SHACL schemas.
- Directory trees MUST use `~~~text` fences and canonical `├──` / `└──` glyphs, per **KFM-MDP v11.2.4**.

---

## 🧭 Context

This standard sits at the intersection of:

- **KFM-MDP v11.2.4** — defines Markdown structure, headings, and metadata for this document.
- **KFM-OP v11** — ontology protocol for entities, activities, agents, time, and space.
- **DCAT 3.0 & STAC 1.x** — catalog layers describing datasets, distributions, and geospatial assets.
- **W3C PROV-O** — provenance ontology used as the canonical lineage model.
- **GeoSPARQL & OWL-Time** — spatial and temporal semantics layered on top of PROV.

Practically, this means:

- Every **published dataset** SHOULD have:
  - a DCAT Dataset and at least one Distribution,
  - a STAC Collection/Item (if spatial),
  - and at least one PROV Entity connected to the processes that generated it.
- Every **ETL pipeline** that materially transforms data MUST be represented as a PROV Activity linked to:
  - input/output Entities,
  - a Plan (config + code),
  - and Agents (people, organizations, software).

The PROV-O export is the **single source of truth** for KFM lineage, and all downstream tools (triple stores, Neo4j, Focus Mode) MUST treat it as authoritative.

---

## 🗺️ Diagrams

### 1. High-Level Lineage Flow

~~~mermaid
flowchart LR
    subgraph Authoring & Code
        A[Docs & Configs<br/>KFM-MDP v11.2.4] --> B[ETL Pipelines<br/>src/pipelines/]
    end

    B --> C[Data Products<br/>data/processed/, STAC, DCAT]
    C --> D[PROV-O Export Job<br/>src/pipelines/lineage/prov_export/]
    D --> E[PROV Graphs<br/>data/processed/lineage/prov/]
    E --> F[Lineage Services<br/>src/api/lineage/prov/]
    F --> G[Focus Mode & Story Nodes<br/>UI overlays]
~~~

This diagram shows how documentation and ETL configs feed pipelines, which generate data products, which are then exported into PROV-O graphs and surfaced through APIs and Focus Mode.

### 2. Timeline of a Lineage Run

~~~mermaid
timeline
    title Example Lineage Run
    2025-12-01 : Commit 3f2a9c : "Update ETL config for wells dataset"
    2025-12-01 : CI Pipeline   : "Build, test, and deploy ETL job"
    2025-12-02 : ETL Run #142  : "Ingest & transform wells → GeoJSON"
    2025-12-02 : Graph Load    : "Load wells into Neo4j"
    2025-12-02 : PROV Export   : "Emit PROV-O graph for Run #142"
~~~

Diagrams MUST be accompanied by short explanatory text (as above) and MUST NOT introduce information that is missing from the surrounding prose.

---

## 🧠 Story Node & Focus Mode Integration

Lineage narratives provide **“how did we get here?”** answers for datasets, maps, and Story Nodes.

This standard ensures that:

- Focus Mode uses PROV-O exports as **ground truth** for lineage questions.
- Story Nodes reference PROV Entities and Activities instead of embedding ad-hoc provenance.
- No speculative or fabricated lineage is generated by AI transforms.

### 1. Mapping PROV to Story Nodes

A typical Story Node might include:

- `target` — a DCAT Dataset or STAC Item ID.
- `lineage_entity` — a PROV Entity IRI representing the dataset version.
- `activity_run` — a PROV Activity IRI representing a pipeline run.

Example (shown here as plain text, defined in JSON elsewhere):

~~~text
"target": "urn:kfm:dataset:kgs:wells:v2025-12-02",
"lineage_entity": "urn:kfm:prov:entity:data:kgs-wells:v2025-12-02",
"activity_run": "urn:kfm:prov:activity:etl:kgs-wells:run-142"
~~~

Story Nodes MUST NOT introduce new provenance claims. They only narrate relationships already present in PROV-O.

### 2. Focus Mode Behaviors

For lineage-related Focus Mode sessions:

- ✅ MAY:
  - Summarize lineage chains associated with a dataset or map view.
  - Highlight key Activities, Agents, and time spans.
  - Explain which upstream datasets contributed to a result.

- ❌ MUST NOT:
  - Create missing links between Entities or Activities.
  - Override or alter PROV-O graphs.
  - Relax governance or sovereignty constraints.

Transform behavior is governed by this document’s `ai_transform_*` and the global KFM governance.

---

## 🧪 Validation & CI/CD

Lineage export is only useful if it is **consistently correct and reproducible**. This standard extends CI/CD with lineage-specific test profiles.

### 1. Test Profiles (Extended Matrix)

The following test profiles, referenced in `test_profiles`, MUST be wired into `.github/workflows/kfm-ci.yml`:

| Test Profile              | Purpose                                           | Tooling / Workflow Hint                      |
|---------------------------|---------------------------------------------------|----------------------------------------------|
| `markdown-lint`           | Docs structure & style                            | Markdownlint / custom scripts                |
| `schema-lint`             | YAML front-matter validation                      | JSON Schema validator                        |
| `metadata-check`          | Required metadata presence                        | Custom validators                            |
| `diagram-check`           | Mermaid syntax & profile checks                   | Mermaid CLI/parser                           |
| `accessibility-check`     | Basic a11y rules                                  | Markdown a11y tools                          |
| `provenance-check`        | Front-matter provenance consistency               | YAML vs footer comparison                    |
| `footer-check`            | Governance footer correctness                     | Regex/AST check                              |
| `prov-export-contract`    | PROV-O & SHACL validation of export graphs        | RDF/SHACL validator, PROV-O vocabulary       |
| `prov-graph-consistency`  | Lineage graph sanity (no invalid cycles, etc.)    | SPARQL / Cypher checks; PROV constraints     |

### 2. Required Validation Steps Per Export

For each PROV-O export job:

1. **Schema Validation**
   - Validate exported RDF against PROV-O classes and properties.
   - Validate against `kfm-lineage-prov-graph-v0.1.0-shape.ttl` SHACL shapes.

2. **Coverage Checks**
   - Every released dataset in the export scope MUST have at least one PROV Entity.
   - Every dataset-Entity SHOULD link to a DCAT Dataset or STAC Item (if applicable).

3. **Consistency Checks**
   - No invalid cycles in revision or derivation chains.
   - Temporal consistency:
     - Activities MUST have `prov:startedAtTime` ≤ `prov:endedAtTime`.
     - Generated Entities MUST NOT precede the Activities that generated them.

4. **CI Integration**
   - CI MUST:
     - Run `prov-export-contract` and `prov-graph-consistency` on changed lineage artifacts.
     - Fail the PR if tests fail.
     - Attach validation summaries to CI logs.

---

## 📦 Data & Metadata

### 1. Exported Artifact Types

Each PROV-O export SHOULD emit:

- **Turtle (`.ttl`)** — primary RDF serialization for debugging and version control.
- **JSON-LD (`.jsonld`)** — web-friendly provenance for JSON-first systems.
- **PROV-JSON (`.prov.json`)** — optional, for systems that expect the PROV JSON profile.

All exports MUST:

- Declare `@context` including `prov`, `dct`, `dcat`, `stac`, `geo`, and KFM-specific prefixes.
- Use stable IRI patterns derived from:
  - dataset IDs (DCAT/STAC),
  - ETL config IDs,
  - run IDs (timestamps + hashes).

### 2. Minimal Entity Metadata

Each PROV Entity representing a dataset or file SHOULD include:

- `prov:type` — base type plus domain type (e.g., dataset vs distribution).
- `dct:title`, `dct:description`.
- `dct:identifier` — aligned with DCAT/STAC identifiers.
- `prov:wasDerivedFrom` — upstream Entities where applicable.
- `prov:generatedAtTime` — if known.

Catalog entries SHOULD link back to these Entities using PROV and DCAT properties.

### 3. Minimal Activity Metadata

Each ETL/graph Activity MUST include:

- `prov:type` — base Activity plus domain subclass where useful.
- `prov:startedAtTime`, `prov:endedAtTime`.
- `prov:used` — input Entities.
- `prov:generated` — output Entities.
- `prov:wasAssociatedWith` — Agents involved.
- Qualified relations where roles matter (e.g., Data Steward vs CI Runner).

### 4. Agent Metadata

Agents SHOULD be modeled as:

- `prov:SoftwareAgent` — automated systems (e.g., CI runners, orchestrators).
- `prov:Organization` — institutional actors (e.g., “KFM FAIR+CARE Council”).
- `prov:Person` — named individuals, where allowed by governance.

Where relevant, roles and responsibilities SHOULD link to governance docs referenced in `governance_ref`, `ethics_ref`, and `sovereignty_policy`.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT ↔ PROV Mapping

High-level mapping between catalog and provenance:

| KFM Concept                     | DCAT Term              | PROV-O Pattern / Notes                                  |
|---------------------------------|------------------------|---------------------------------------------------------|
| Logical dataset                 | `dcat:Dataset`         | `prov:Entity`                                           |
| Dataset distribution (file/API) | `dcat:Distribution`    | `prov:Entity` derived from Dataset                      |
| Data service / API             | `dcat:DataService`     | `prov:Entity` and/or `prov:SoftwareAgent`               |
| Dataset version                | `dcat:hasVersion` etc. | `prov:wasRevisionOf` chain between Entities             |
| Dataset series                 | `dcat:DatasetSeries`   | PROV Bundle or higher-level Entity grouping versions    |

Rules:

- For every `dcat:Dataset`, there SHOULD be a corresponding PROV Entity.
- Version chains MUST appear both in DCAT (versioning terms) and PROV (`prov:wasRevisionOf`).

### 2. STAC ↔ PROV Mapping

For STAC Collections and Items:

| Concept              | STAC Field           | PROV-O Pattern                                  |
|----------------------|----------------------|-------------------------------------------------|
| STAC Item asset      | `assets[*]`          | `prov:Entity` per asset                         |
| Asset creation       | `properties.datetime`| `prov:wasGeneratedBy` Activity + end time       |
| Collection license   | `license`            | copied to `dct:license` on related Entities     |
| Spatial footprint    | `geometry` / `bbox`  | `geo:Feature` + `geo:hasGeometry` (GeoSPARQL)   |

Non-spatial documentation lineage MAY omit geometry or use a generic Kansas bounding box where needed for map overlay behavior.

### 3. Bundles & Catalog Records

- PROV Bundles MAY be used to group:
  - lineage for a dataset version,
  - lineage for a single pipeline run.
- DCAT CatalogRecords MAY describe catalog-entry events separately from dataset generation events.

Bundles MUST NOT contradict the core lineage graph; they are organizational, not authoritative overrides.

---

## 🧱 Architecture

### 1. Pipeline View

From an architecture perspective, PROV-O export is its own deterministic pipeline layered over other ETL jobs:

1. **Source Jobs**
   - Ingest and transform domain data (e.g., wells, hydrology, archaeology).
2. **Catalog Population**
   - Populate DCAT and STAC catalogs.
3. **Lineage Harvest**
   - Read run metadata (ETL configs, CI build metadata, runtime logs).
4. **PROV Graph Construction**
   - Build PROV Entities, Activities, Agents, Plans, Bundles.
5. **Export & Storage**
   - Serialize to Turtle/JSON-LD/PROV-JSON in `data/processed/lineage/prov/`.
   - Bundles for release in `data/releases/lineage/prov/`.
6. **Serving & Integration**
   - Optional triple store deployment.
   - Neo4j lineage views or hybrid RDF→property-graph mapping.
   - API endpoints for dataset- or run-scoped lineage queries.

### 2. Reproducibility Requirements

Each export MUST be rerunnable from:

- A config file under `src/pipelines/lineage/prov_export/config/`.
- Pinned input sources (DCAT/STAC + logs).
- A specific git commit SHA and pipeline version.

Export logs MUST record:

- Config path.
- Commit SHA.
- Input dataset versions.
- Timestamp.
- Export artifact IDs.

### 3. Change Management

Any substantive change to this standard MUST:

1. Update this README and the associated JSON/SHACL schemas.
2. Update CI workflows for `prov-export-contract` and `prov-graph-consistency` (if needed).
3. Append a new row to **Version History**.
4. Update `provenance_chain` and `sunset_policy` once a stable v1.x is reached.

---

## ⚖ FAIR+CARE & Governance

Lineage itself is a governed artifact.

- **FAIR**
  - **Findable:** stable IRIs, catalog entries, and STAC links.
  - **Accessible:** open provenance exports (where allowed) under CC-BY 4.0.
  - **Interoperable:** PROV-O, DCAT, STAC, GeoSPARQL, OWL-Time.
  - **Reusable:** clear licensing, version history, and provenance of lineage itself.

- **CARE**
  - **Collective Benefit:** lineage helps communities understand how data and narratives were constructed.
  - **Authority to Control:** sensitive provenance (e.g., around restricted cultural sites) MAY be held in restricted bundles; public exports SHOULD be generalized.
  - **Responsibility & Ethics:** lineage MUST NOT expose identifying details where governance requires aggregation or anonymization.

Authors and implementers MUST consult `governance_ref`, `ethics_ref`, and `sovereignty_policy` for any lineage export involving culturally sensitive or restricted data.

---

## 🕰️ Version History

| Version   | Date       | Status | Summary                                                                                                                                      |
|----------:|------------|--------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **v0.1.0** | 2025-12-07 | Draft  | Initial PROV-O export standard: defined monorepo surfaces, DCAT/STAC/PROV mappings, lineage CI test profiles, and integration with Focus Mode & FAIR+CARE governance. |

---

<div align="center">

📑 **KFM Lineage — PROV-O Export Standard (Draft v0.1.0)**  
Deterministic Pipelines · Open Provenance · FAIR+CARE-Aligned Lineage  

[📘 Docs Root](../../../) · [📂 Lineage Standards Index](../README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>
