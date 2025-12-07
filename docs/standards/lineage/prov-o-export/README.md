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
governance_ref: "../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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
This standard specifies how ETL runs, catalog records, knowledge-graph operations, and documents are turned into deterministic, queryable PROV-O entities, activities, and agents for downstream analysis and Focus Mode overlays. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

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

- ETL & data pipelines (Extract → Transform → Load) and their runs. :contentReference[oaicite:2]{index=2}  
- Catalog-level metadata in **DCAT 3.0** and **STAC 1.x**. :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4}  
- Graph loading and enrichment operations in Neo4j.  
- Documentation artifacts governed by **KFM-MDP v11.2.4**. :contentReference[oaicite:5]{index=5}  
- The mapping of these to **PROV-O Entities, Activities, Agents, Plans, and Bundles**. :contentReference[oaicite:6]{index=6}  

The goal is a **deterministic, reproducible export pipeline** that produces:

- Machine-readable lineage graphs (Turtle, JSON-LD, PROV-JSON).
- Validated against **PROV-O**, **KFM-PROV v11**, and local SHACL shapes.
- Ready for ingestion into triple stores and/or Neo4j-backed lineage views.
- Safe for Focus Mode to query and summarize without altering authoritative content.

This document is **draft / proposed** and MUST be reviewed and approved before being marked **Active / Enforced**.

### 2. Core Principles

1. **Deterministic Lineage**  
   Every exported PROV-O graph MUST be reproducible from:
   - a pinned ETL config (YAML/JSON),
   - a git commit SHA,
   - versioned datasets and schemas. :contentReference[oaicite:7]{index=7}  

2. **Single Lineage Model**  
   All provenance MUST be representable in the PROV-O **Entity–Activity–Agent** pattern with optional Bundles and Plans, avoiding ad-hoc custom vocabularies when PROV-O terms already exist. :contentReference[oaicite:8]{index=8}  

3. **Interoperable Catalogs**  
   Lineage exports MUST link back to DCAT and STAC identifiers for datasets, distributions, and items so that catalog and provenance views remain in sync. :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10}  

4. **Graph-First Semantics**  
   PROV-O exports are designed to be ingestible by both RDF triple stores and KFM’s Neo4j graph, enabling:
   - lineage queries,
   - impact analysis,
   - temporal reasoning (with OWL-Time). :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12}  

5. **FAIR+CARE-Aligned Lineage**  
   Lineage MUST not expose sensitive data; instead, it describes **relationships and processes**, respecting Indigenous data sovereignty and privacy rules while still supporting findability and reusability. :contentReference[oaicite:13]{index=13}  

6. **CI-Enforced**  
   No lineage export is considered valid until:
   - PROV-O schema checks,
   - SHACL shape validation,
   - and coverage tests pass in `.github/workflows/kfm-ci.yml`. :contentReference[oaicite:14]{index=14}  

### 3. Where This Work Lives (Monorepo Surfaces)

This standard directly impacts:

- **Docs**
  - `docs/standards/lineage/prov-o-export/README.md` (this file).
  - `docs/architecture/lineage/prov-graph.md` (graph-level design; proposed).
  - `docs/guides/lineage/prov-o-export-cli.md` (CLI usage guide; proposed).

- **Pipelines**
  - `src/pipelines/lineage/prov_export/`  
    - `config/` — YAML/JSON export configs (per domain / dataset).  
    - `jobs/` — deterministic export jobs (batch + streaming).  
    - `cli.py` — top-level `kfm-provenance export` entrypoint.

- **Graph & API**
  - `src/graph/lineage/prov/` — Neo4j loaders and query helpers for lineage.  
  - `src/api/lineage/prov/` — REST/GraphQL endpoints exposing lineage slices.

- **Data & Catalogs**
  - `data/processed/lineage/prov/` — PROV-O export artifacts (TTL, JSON-LD, PROV-JSON).  
  - `data/releases/lineage/prov/` — versioned release bundles.  
  - `data/stac/lineage/` — STAC Items linking to provenance artifacts. :contentReference[oaicite:15]{index=15}  
  - `data/sources/dcat/` — DCAT entries referencing provenance datasets. :contentReference[oaicite:16]{index=16}  

Implementers MUST ensure these paths exist or adjust this document (and JSON schemas) before promoting the standard to **Active**.

### 4. Author Quickstart (for Lineage Standards & Guides)

When writing documentation related to PROV-O export:

1. Start from this file’s front-matter and **KFM-MDP v11.2.4** scaffolding. :contentReference[oaicite:17]{index=17}  
2. Use only the approved H2 headings from `heading_registry.approved_h2`.  
3. Reference:
   - `KFM-MDP v11.2.4` for Markdown rules,
   - `DCAT 3.0 Implementation Guide` for catalog mapping, :contentReference[oaicite:18]{index=18}  
   - `STAC System Guide` for asset catalogs, :contentReference[oaicite:19]{index=19}  
   - `PROV-O Guide` for provenance modeling. :contentReference[oaicite:20]{index=20}  
4. Explicitly link to:
   - the pipelines that generate the lineage, and
   - the storage locations of exported graphs.

---

## 🗂️ Directory Layout

Target layout for PROV-O export–related components (some paths are proposed and MUST be created during implementation):

~~~text
docs/
├── standards/
│   ├── kfm_markdown_protocol_v11.2.4.md
│   └── lineage/
│       ├── README.md                          # Lineage standards index (proposed)
│       └── prov-o-export/
│           └── README.md                      # This standard
├── architecture/
│   └── lineage/
│       └── prov-graph.md                      # PROV graph & storage design (proposed)
├── guides/
│   └── lineage/
│       └── prov-o-export-cli.md               # CLI usage & examples (proposed)

src/
├── pipelines/
│   └── lineage/
│       └── prov_export/
│           ├── config/                        # YAML/JSON export configs
│           ├── jobs/                          # Batch / streaming export jobs
│           └── cli.py                         # `kfm-provenance export` entrypoint
├── graph/
│   └── lineage/
│       └── prov/
│           ├── neo4j_loader.py                # Load PROV into Neo4j (if used)
│           └── queries.cyp                    # Standard lineage queries
└── api/
    └── lineage/
        └── prov/
            └── router.py                      # REST/GraphQL lineage endpoints

data/
├── processed/
│   └── lineage/
│       └── prov/
│           ├── ttl/                           # PROV-O Turtle exports
│           ├── jsonld/                        # PROV-O JSON-LD exports
│           └── provjson/                      # PROV-JSON exports
├── releases/
│   └── lineage/
│       └── prov/
│           └── v*/                            # Versioned lineage release bundles
└── stac/
    └── lineage/
        └── collections/                       # STAC Collections for provenance assets

schemas/
├── json/
│   └── kfm-lineage-prov-o-export-v0.1.0.schema.json
└── shacl/
    └── kfm-lineage-prov-graph-v0.1.0-shape.ttl
~~~

**Author and Implementer Rules:**

- Each directory above MUST have a `README.md` (or equivalent) once created, describing purpose and data contracts.  
- Any deviation from these paths MUST be reflected here and in the JSON/SHACL schemas.  
- Directory trees MUST use `~~~text` fences and canonical `├──` / `└──` glyphs, per **KFM-MDP v11.2.4**. :contentReference[oaicite:21]{index=21}  

---

## 🧭 Context

KFM already standardizes:

- **Markdown authoring** via KFM-MDP v11.2.4. :contentReference[oaicite:22]{index=22}  
- **Catalog metadata** via DCAT 3.0 and STAC-based systems. :contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24}  
- **Provenance modeling** via W3C PROV-O. :contentReference[oaicite:25]{index=25}  
- **Spatiotemporal semantics** via GeoSPARQL and OWL-Time. :contentReference[oaicite:26]{index=26}  

This standard sits at the intersection of:

- **ETL architecture & pipelines** — where lineage events originate (pipeline runs, data transformations, graph loads). :contentReference[oaicite:27]{index=27}  
- **Catalog layers (DCAT/STAC)** — where datasets and distributions are described and must reference provenance. :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29}  
- **Graph & story systems** — where Focus Mode and Story Nodes need trustworthy lineage overlays rather than inferred or speculative provenance. :contentReference[oaicite:30]{index=30}  

Practically, this means:

- Every **published dataset** SHOULD have:
  - a DCAT Dataset and Distribution,
  - a STAC Collection/Item (if spatial),
  - and at least one PROV-O Entity connected to the processes that generated it.
- Every **ETL pipeline** that materially changes data MUST be represented as a PROV-O Activity linked to:
  - its input and output Entities,
  - its executable Plan (config + code),
  - and its Agents (e.g. GitHub Actions runner, human reviewer). :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32}  

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
    2025-12-01 : Commit 3f2a9c : "Update ETL config for KGS wells"
    2025-12-01 : CI Pipeline : "Build, test, and deploy ETL job"
    2025-12-02 : ETL Run #142 : "Ingest & transform wells → GeoJSON"
    2025-12-02 : Graph Load : "Load wells into Neo4j"
    2025-12-02 : PROV Export : "Emit PROV-O graph for Run #142"
~~~

These timelines should be adapted to real runs in operational documentation (e.g., per project or per dataset).

---

## 🧠 Story Node & Focus Mode Integration

Lineage narratives are powerful but must remain **descriptive**, not normative. This standard ensures that Focus Mode:

- Uses PROV-O graphs as **ground truth** for “how did this get here?” questions.
- Never fabricates provenance beyond what exists in PROV exports.
- Respects transform restrictions defined here and in KFM-MDP. :contentReference[oaicite:33]{index=33}  

### 1. Mapping PROV Nodes to Story Nodes

Typical mapping:

- **Story Node text** describes:
  - a dataset’s origin,
  - key transformations,
  - responsible teams.
- **Story Node links** reference:
  - `target`: a DCAT Dataset or STAC Item ID,
  - `lineage_entity`: a PROV Entity IRI,
  - `activity_run`: a PROV Activity IRI.

Example JSON snippet (in a Story Node spec, not in Markdown):

~~~text
"target": "urn:kfm:dataset:kgs:wells:v2025-12-02",
"lineage_entity": "urn:kfm:prov:entity:data:kgs-wells:v2025-12-02",
"activity_run": "urn:kfm:prov:activity:etl:kgs-wells:run-142"
~~~

Story Nodes MUST NOT introduce new provenance claims; they only narrate what PROV-O already records.

### 2. Focus Mode Allowed Behaviors

Within `ai_transform_permissions` for this doc and for lineage views:

- ✅ May summarize:
  - “What pipeline produced this dataset?”
  - “Which inputs did this result depend on?”
- ✅ May highlight:
  - key Activities,
  - critical Agents (e.g. FAIR+CARE Council approval steps),
  - temporal spans.

- ❌ Must NOT:
  - invent missing lineage links,
  - change or override PROV-O graphs,
  - relax governance or sovereignty constraints.

---

## 🧪 Validation & CI/CD

Lineage export is only useful if it’s **consistently correct**. This standard extends CI/CD with two lineage-specific test profiles, building on existing KFM patterns. :contentReference[oaicite:34]{index=34} :contentReference[oaicite:35]{index=35}  

### 1. Test Profiles (Extended Matrix)

| Test Profile                 | Purpose                                           | Tooling / Workflow Hint                      |
|-----------------------------|---------------------------------------------------|----------------------------------------------|
| `markdown-lint`             | Docs structure & style                            | Markdownlint, custom scripts                  |
| `schema-lint`               | YAML front-matter validation                      | JSON Schema validator                         |
| `metadata-check`            | Required metadata presence                        | Custom validators                             |
| `diagram-check`             | Mermaid syntax & profile checks                   | Mermaid CLI/parser                            |
| `accessibility-check`       | Basic a11y rules                                  | Markdown a11y tools                           |
| `provenance-check`          | Front-matter provenance consistency               | YAML vs footer comparison                     |
| `footer-check`              | Governance footer correctness                     | Regex/AST check                               |
| `prov-export-contract`      | PROV-O & SHACL validation of export graphs        | RDF/SHACL validators, PROV-O vocabulary       |
| `prov-graph-consistency`    | Lineage graph sanity (no invalid cycles, etc.)    | SPARQL/Cypher checks; PROV constraints        |

### 2. Required Validation Steps for Each Export

For each executed **PROV-O export job**:

1. **Schema Validation**
   - Validate exported RDF against PROV-O classes and properties. :contentReference[oaicite:36]{index=36}  
   - Validate against `kfm-lineage-prov-graph-v0.1.0-shape.ttl` SHACL shapes.

2. **Coverage Checks**
   - Ensure minimum coverage thresholds:
     - all released datasets in a given batch have at least one PROV Entity,
     - every PROV Entity representing a dataset links to a DCAT Dataset or STAC Item (if applicable). :contentReference[oaicite:37]{index=37} :contentReference[oaicite:38]{index=38}  

3. **Consistency Checks**
   - Confirm no cycles in revision chains that violate PROV constraints.
   - Ensure temporal consistency (Activity start/end times vs Entity generation times). :contentReference[oaicite:39]{index=39}  

4. **CI Integration**
   - `.github/workflows/kfm-ci.yml` MUST:
     - run `prov-export-contract` and `prov-graph-consistency` on changed lineage artifacts,
     - fail the PR if tests fail,
     - attach validation summaries to build logs.

---

## 📦 Data & Metadata

### 1. Exported Artifact Types

Each PROV-O export SHOULD produce:

- **Turtle (`.ttl`)**
  - Primary RDF serialization for debugging and version control.
- **JSON-LD (`.jsonld`)**
  - Web-friendly provenance for interop with JSON-first systems. :contentReference[oaicite:40]{index=40}  
- **PROV-JSON (`.prov.json`)**
  - Optional, for systems expecting PROV’s JSON profile.

All MUST:

- Declare `@context` including `prov`, `dct`, `dcat`, `stac`, `geo`, and KFM prefixes.
- Use stable IRI patterns derived from:
  - dataset IDs (DCAT/STAC),
  - ETL config IDs,
  - run IDs (timestamps + hashes).

### 2. Minimal Entity Metadata

Every PROV Entity representing a dataset or file SHOULD include:

- `prov:type` (e.g., `prov:Entity`, plus domain type),
- `dct:title`, `dct:description`,
- `dct:identifier` (matching DCAT/STAC IDs),
- `prov:wasDerivedFrom` links for upstream entities,
- `prov:generatedAtTime` (if known).

Catalog entries SHOULD link to these Entities via:

- DCAT: `dcat:Dataset` → `prov:wasGeneratedBy` (Activity),
- or via `prov:wasDerivedFrom` where appropriate. :contentReference[oaicite:41]{index=41}  

### 3. Minimal Activity Metadata

Each ETL or graph Activity MUST include:

- `prov:type` (e.g., `prov:Activity`, plus domain subclass),
- `prov:startedAtTime`, `prov:endedAtTime`,
- `prov:used` (input Entities),
- `prov:generated` (output Entities),
- `prov:wasAssociatedWith` (Agents),
- `prov:qualifiedAssociation` for roles when relevant (e.g., “Data Steward”, “CI Runner”). :contentReference[oaicite:42]{index=42}  

### 4. Agent Metadata

Agents SHOULD be modeled as:

- `prov:SoftwareAgent` for automated systems (e.g., GitHub Actions, Airflow DAGs), :contentReference[oaicite:43]{index=43}  
- `prov:Organization` for institutions (e.g., “KFM FAIR+CARE Council”),
- `prov:Person` for named individuals when allowed by governance.

Links to governance docs (e.g., roles, responsibilities) MUST use the existing governance URLs from front-matter.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT ↔ PROV Mapping

At a high level: :contentReference[oaicite:44]{index=44} :contentReference[oaicite:45]{index=45}  

| KFM Concept                     | DCAT Term                     | PROV-O Term / Pattern                                   |
|---------------------------------|-------------------------------|--------------------------------------------------------|
| Logical dataset                 | `dcat:Dataset`                | `prov:Entity`                                          |
| Dataset distribution (file/API) | `dcat:Distribution`           | `prov:Entity` (file) + `prov:wasDerivedFrom` Dataset   |
| Data service / API             | `dcat:DataService`            | `prov:Entity` and/or `prov:SoftwareAgent`              |
| Dataset version                | `dcat:hasVersion` + `dcat:version` | `prov:wasRevisionOf` between Entities              |
| Dataset series                 | `dcat:DatasetSeries`          | PROV Bundle or higher-level Entity w/ derivations      |

The export pipeline MUST ensure:

- For every `dcat:Dataset`, there is a corresponding PROV Entity IRI.
- Version chains appear both as DCAT versioning and as `prov:wasRevisionOf` links.

### 2. STAC ↔ PROV Mapping

For STAC Items and Collections: :contentReference[oaicite:46]{index=46} :contentReference[oaicite:47]{index=47}  

| KFM Concept        | STAC Field                     | PROV-O Pattern                                        |
|--------------------|--------------------------------|-------------------------------------------------------|
| STAC Item asset    | `assets[*]`                    | `prov:Entity` (one per asset)                         |
| Asset creation     | `properties.datetime`          | `prov:wasGeneratedBy` Activity w/ `prov:endedAtTime`  |
| Collection license | `license`                      | Copied to `dct:license` on Entities                   |
| STAC Item          | GeoJSON Feature + properties   | `prov:Entity` with `geo:hasGeometry` (if relevant)    |

For geospatial Entities, GeoSPARQL terms MAY be used alongside PROV-O: `geo:Feature`, `geo:hasGeometry`, `geo:asWKT`. :contentReference[oaicite:48]{index=48}  

### 3. Provenance Bundles & Catalog Records

Larger exports MAY group provenance into:

- PROV Bundles representing:
  - “lineage for dataset X, version Y”,
  - “lineage for run Z”.
- DCAT CatalogRecords capturing when a dataset’s metadata was registered, separate from when data was generated. :contentReference[oaicite:49]{index=49}  

---

## 🧱 Architecture

### 1. Pipeline View

From the architecture perspective, PROV-O export is a **deterministic ETL pipeline** layered on top of other ETL jobs:

1. **Source Jobs**
   - Ingest and transform domain data (e.g., KGS wells, census, hydrology). :contentReference[oaicite:50]{index=50}  

2. **Catalog Population**
   - Populate DCAT and STAC catalogs (STAC JSON, DCAT RDF).

3. **Lineage Harvest**
   - Read run metadata:
     - ETL configs,
     - CI build metadata,
     - runtime logs (start/end times, statuses).

4. **PROV Graph Construction**
   - Transform harvest data into PROV-O triples:
     - Entities for datasets, distributions, config files,
     - Activities for ETL runs, graph loads,
     - Agents for people, orgs, CI runners. :contentReference[oaicite:51]{index=51}  

5. **Export & Storage**
   - Serialize graphs to Turtle/JSON-LD/PROV-JSON in `data/processed/lineage/prov/`.
   - Version/tag bundles into `data/releases/lineage/prov/`.

6. **Serving & Integration**
   - Optional triple-store deployment.
   - Neo4j lineage view or hybrid RDF→property-graph mapping.
   - API endpoints surfacing lineage per dataset or per run.

### 2. Reproducibility Requirements

- Each export MUST be rerunnable from:
  - a config file in `src/pipelines/lineage/prov_export/config/`,
  - pinned input sources (DCAT/STAC + logs),
  - a specific git commit SHA and pipeline version. :contentReference[oaicite:52]{index=52} :contentReference[oaicite:53]{index=53}  

- Export logs MUST record:
  - config path,
  - commit SHA,
  - input dataset versions,
  - timestamp,
  - export artifact IDs.

### 3. Change Management

Any substantive change to this standard MUST:

1. Update this README, JSON schema, and SHACL shapes.  
2. Update CI workflows for `prov-export-contract` and `prov-graph-consistency`.  
3. Append a new row to **Version History** (below).  
4. Update `provenance_chain` and `sunset_policy` once a stable v1.x is reached.

---

## ⚖ FAIR+CARE & Governance

Lineage is itself an artifact subject to governance:

- **FAIR**
  - **Findable:** stable IRIs, DCAT entries, STAC links. :contentReference[oaicite:54]{index=54} :contentReference[oaicite:55]{index=55}  
  - **Accessible:** open provenance exports licensed under CC-BY 4.0, where appropriate.
  - **Interoperable:** PROV-O, DCAT, STAC, GeoSPARQL, OWL-Time. :contentReference[oaicite:56]{index=56} :contentReference[oaicite:57]{index=57}  
  - **Reusable:** clear licensing and version history.

- **CARE**
  - **Collective Benefit:** lineage helps communities understand how narratives and datasets were constructed, promoting transparency.
  - **Authority to Control:** sensitive provenance (e.g., processes around protected site data) may be kept in restricted bundles; public exports SHOULD be generalized.
  - **Responsibility & Ethics:** lineage MUST NOT expose names or identifying details when governance requires aggregation or anonymization.

- **Governance Hooks**
  - `governance_ref`, `ethics_ref`, and `sovereignty_policy` MUST be consulted for any lineage export involving culturally sensitive or restricted data.
  - FAIR+CARE Council MAY require additional review for specific provenance bundles.

---

## 🕰️ Version History

| Version   | Date       | Status    | Summary                                                                                               |
|----------:|------------|----------|-------------------------------------------------------------------------------------------------------|
| **v0.1.0** | 2025-12-07 | Draft     | Initial PROV-O export standard: defined monorepo surfaces, DCAT/STAC/PROV mappings, CI test profiles, and integration with Focus Mode & FAIR+CARE governance. |

---

<div align="center">

📑 **KFM Lineage — PROV-O Export Standard (Draft v0.1.0)**  
Deterministic Pipelines · Open Provenance · FAIR+CARE-Aligned Lineage  

[📘 Docs Root](../../) · [📂 Lineage Standards Index](../README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>

