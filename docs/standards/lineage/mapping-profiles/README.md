---
title: "📑 KFM Lineage — Mapping Profiles Standard"
path: "docs/standards/lineage/mapping-profiles/README.md"
version: "v0.1.0"
last_updated: "2025-12-07"
release_stage: "Draft / For Review"
lifecycle: "Planned Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "draft"
commit_sha: "<pending-commit-sha>"
signature_ref: "releases/lineage-mapping-profiles/v0.1.0/signature.sig"
attestation_ref: "releases/lineage-mapping-profiles/v0.1.0/slsa-attestation.json"
sbom_ref: "releases/lineage-mapping-profiles/v0.1.0/sbom.spdx.json"
manifest_ref: "releases/lineage-mapping-profiles/v0.1.0/manifest.zip"
telemetry_ref: "releases/lineage-mapping-profiles/v0.1.0/lineage-mapping-telemetry.json"
telemetry_schema: "schemas/telemetry/lineage-mapping-profiles-v0.1.0.json"
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
    - "mapping-profiles"
    - "stac-dcat-prov-crosswalks"
    - "lineage-graph"
    - "etl-pipelines"
semantic_intent:
  - "lineage"
  - "mapping"
  - "export"
  - "governance"
category: "Lineage · Mapping Profiles · Standards"
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
sunset_policy: "Superseded when KFM Lineage Mapping Profiles v1.x is adopted"
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
json_schema_ref: "schemas/json/kfm-lineage-mapping-profile-v0.1.0.schema.json"
shape_schema_ref: "schemas/shacl/kfm-lineage-mapping-profile-shapes-v0.1.0.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:lineage:mapping-profiles:v0.1.0"
semantic_document_id: "kfm-lineage-mapping-profiles-v0.1.0"
event_source_id: "ledger:kfm:doc:standards:lineage:mapping-profiles:v0.1.0"
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
  - "mapping-profile-lint"
  - "mapping-profile-crosswalk-check"
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

# 📑 **KFM Lineage — Mapping Profiles Standard (Draft v0.1.0)**  
`docs/standards/lineage/mapping-profiles/README.md`

**Purpose:**  
Define the canonical, CI-enforced pattern for **mapping profiles** that crosswalk the Kansas Frontier Matrix (KFM) lineage and data model to **W3C PROV-O**, **DCAT 3.0**, **STAC 1.x**, and **GeoSPARQL**.  
This standard ensures that KFM entities, activities, and assets can be deterministically mapped into external vocabularies for provenance export, catalog publishing, and Focus Mode overlays, using config-driven profiles instead of ad-hoc code.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-informational "Markdown Protocol v11.2.4")]() ·
[![PROV-O](https://img.shields.io/badge/Provenance-W3C_PROV--O-purple "W3C PROV-O")]() ·
[![DCAT 3.0](https://img.shields.io/badge/Metadata-DCAT_3.0-teal "W3C DCAT 3.0")]() ·
[![STAC 1.x](https://img.shields.io/badge/Geospatial-STAC_1.x-green "OGC STAC 1.x")]() ·
[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange "Draft / For Review")]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

This standard governs how **mapping profiles** are defined, versioned, and validated for:

- Translating **KFM internal entities** (Neo4j nodes, ETL artifacts, docs) into:
  - **PROV-O** Entities, Activities, and Agents,
  - **DCAT 3.0** Datasets, Distributions, DataServices, and DatasetSeries,
  - **STAC 1.x** Items, Collections, and Assets,
  - **GeoSPARQL** Features and Geometries.
- Driving **lineage exports** (see PROV-O Export Standard) and **catalog publishing** from the same mappings.
- Powering **Focus Mode** and **Story Node** overlays with semantically consistent IDs and relationships.

In practice, a mapping profile is a **config artifact** (YAML + RDF/TTL) that declares how:

- KFM labels / types map to external classes.
- KFM properties map to external predicates.
- IRIs, identifiers, and versioning are constructed.
- Spatial/temporal information is represented (GeoJSON/GeoSPARQL + OWL-Time).
- FAIR+CARE and sovereignty constraints are respected in what is exposed.

This document is **draft / proposed** and MUST be promoted to **Active / Enforced** via governance once schemas, pipelines, and tests are in place.

### 2. Core Principles

1. **Mapping-as-Data, Not Code**  
   All semantic crosswalks MUST live in versioned mapping profiles (YAML/RDF), not buried in custom code. Pipelines read mappings; they do not re-encode them.

2. **Single Canonical Profile per Domain × Version**  
   At any time, each domain/dataset series SHOULD have one “active” mapping profile per major lineage schema version, to avoid conflicting exports.

3. **Deterministic & Reproducible**  
   Given a mapping profile, a git commit, and a set of inputs, the resulting PROV-O/DCAT/STAC/GeoSPARQL exports MUST be deterministic.

4. **Re-use Standard Vocabularies First**  
   Mapping profiles MUST prefer PROV-O, DCAT 3.0, STAC 1.x, GeoSPARQL, and OWL-Time terms before introducing KFM extensions.

5. **Round-Trip Awareness**  
   Where feasible, mappings SHOULD support round-tripping (e.g., STAC/DCAT → internal representation) without loss of core identity and provenance.

6. **FAIR+CARE-Aligned Exposure**  
   Mapping profiles MUST be the place where sensitive fields are generalized, redacted, or omitted per FAIR+CARE and sovereignty rules, not ad-hoc in code.

### 3. Where This Work Lives (Monorepo Surfaces)

This standard coordinates several modules:

- **Docs**
  - `docs/standards/lineage/mapping-profiles/README.md` (this file).
  - `docs/standards/lineage/prov-o-export/README.md` (export contract).
  - `docs/guides/lineage/` (how-to guides for authors; proposed).

- **Pipelines**
  - `src/pipelines/lineage/mapping_profiles/` — mapping-aware jobs and CLI.
  - `src/pipelines/lineage/prov_export/` — consumes mapping profiles to build PROV graphs.

- **Graph & API**
  - `src/graph/lineage/mapping/` — Neo4j loaders / Cypher helpers aware of mappings.
  - `src/api/lineage/prov/` — endpoints to surface mapped lineage slices.

- **Data & Schemas**
  - `data/processed/lineage/` — exported graphs, catalogs, and test fixtures.
  - `schemas/json/kfm-lineage-mapping-profile-v0.1.0.schema.json` — JSON Schema for YAML mapping configs.
  - `schemas/shacl/kfm-lineage-mapping-profile-shapes-v0.1.0.ttl` — SHACL for RDF mapping representations.

### 4. Author Quickstart (Mapping Profile Authors)

When adding or editing a mapping profile:

1. **Start from a Template**  
   Copy a profile from `src/pipelines/lineage/mapping_profiles/templates/base_profile.yaml` and the corresponding `profiles/.../README.md`.

2. **Fill Core Metadata**  
   - Profile ID, version, status, domain(s), and coverage.
   - Links to relevant datasets (DCAT/STAC identifiers) and KFM graph label(s).

3. **Define Class & Property Crosswalks**  
   - Map KFM node labels/types → PROV-O/DCAT/STAC/GeoSPARQL classes.
   - Map KFM properties → external predicates, including ID strategies.

4. **Run Local Validation**  
   - `mapping-profile-lint` (schema validation).
   - `mapping-profile-crosswalk-check` (external term validity, SHACL shapes).

5. **Document Intent & Limitations**  
   Explain in the profile README:
   - What the mapping covers (datasets, activities, agents).
   - What is deliberately out of scope (e.g., redacted attributes).
   - Any assumptions about spatial/temporal modeling.

6. **Open PR with Tests**  
   Include:
   - Updated profile files.
   - Example exports (small fixtures).
   - CI passing for mapping-specific tests.

---

## 🗂️ Directory Layout

Canonical layout for mapping-profile–related components (standard emojis, KFM tree style):

~~~text
KansasFrontierMatrix/
├── 📂 docs/                                  # All documentation
│   ├── 📂 standards/                         # Standards & policies (Markdown, FAIR+CARE, governance, etc.)
│   │   ├── 📄 kfm_markdown_protocol_v11.2.4.md      # Markdown authoring protocol
│   │   ├── 📂 lineage/                       # Lineage & provenance standards
│   │   │   ├── 📄 README.md                  # Lineage standards index (proposed)
│   │   │   ├── 📂 prov-o-export/             # PROV-O export standard & guides
│   │   │   │   └── 📄 README.md
│   │   │   └── 📂 mapping-profiles/          # STAC/DCAT/PROV mapping profiles (this standard)
│   │   │       ├── 📄 README.md
│   │   │       ├── 📂 profiles/              # Reusable mapping profile bundles
│   │   │       │   ├── 📂 stac-dcat-prov/    # Default KFM crosswalks (DCAT/STAC/PROV/GeoSPARQL)
│   │   │       │   │   ├── 📄 README.md
│   │   │       │   │   ├── 📄 mappings.ttl   # RDF representation of mapping profile
│   │   │       │   │   └── 📄 examples.md    # Human-readable examples & walkthroughs
│   │   │       │   └── 📂 custom/            # Project- or team-specific profiles
│   │   │       │       └── 📄 README.md
│   │   │       └── 📂 tests/                 # Mapping-profile test cases & fixtures
│   │   │           └── 📄 README.md
│   ├── 📂 architecture/                      # System & subsystem designs
│   ├── 📂 guides/                            # How-to guides, tutorials, SOP-style walkthroughs
│   ├── 📂 data/                              # Data contracts, source registries, schema notes
│   ├── 📂 analyses/                          # Domain analyses & case studies
│   └── 📄 glossary.md                        # Shared glossary for KFM-wide terminology
├── 📂 src/                                   # Backend & service code
│   ├── 📂 pipelines/                         # ETL, AI/ML, orchestration
│   │   └── 📂 lineage/
│   │       └── 📂 mapping_profiles/          # Mapping-profile aware export jobs & helpers
│   │           ├── 📄 cli.py                 # `kfm-lineage mapping` CLI entrypoint
│   │           └── 📂 templates/             # Base templates for mapping configs
│   │               └── 📄 base_profile.yaml
│   ├── 📂 graph/                             # Neo4j schema, loaders, queries
│   │   └── 📂 lineage/
│   │       └── 📂 mapping/                   # Graph-level mapping helpers
│   │           └── 📄 loader.py
│   ├── 📂 api/                               # FastAPI / GraphQL services
│   └── 📂 tools/                             # Backend utilities, CLIs, migrations
├── 📂 schemas/                               # JSON, SHACL, telemetry schemas
│   ├── 📂 json/
│   │   └── 📄 kfm-lineage-mapping-profile-v0.1.0.schema.json
│   └── 📂 shacl/
│       └── 📄 kfm-lineage-mapping-profile-shapes-v0.1.0.ttl
├── 📂 data/                                  # Data lifecycle: raw → work → processed → releases
│   ├── 📂 sources/
│   ├── 📂 raw/
│   ├── 📂 work/
│   ├── 📂 processed/
│   └── 📂 stac/
├── 📂 tests/                                 # Automated test suites
└── 📂 .github/                               # CI/CD workflows & GitHub configuration
    └── 📂 workflows/                         # CI pipelines (kfm-ci, docs-lint, lineage-audit, energy/carbon)
~~~

**Author & Implementer Rules:**

- Directories shown above MUST eventually have a `README.md` describing contracts and contents.
- Any path changes MUST be reflected here and in the associated JSON/SHACL schemas.
- Directory trees MUST use `~~~text` fences with the canonical `├──` / `└──` glyphs and the KFM emoji convention.

---

## 🧭 Context

This standard sits where several KFM standards intersect:

- **ETL & Pipeline Architecture** — mapping profiles drive how ETL outputs and intermediate entities are represented in external catalogs and provenance graphs.
- **Markdown Protocol (KFM-MDP v11.2.4)** — ensures mapping-profile documentation is CI-safe and machine-readable.
- **STAC / DCAT / PROV / GeoSPARQL** — mapping profiles encode the crosswalk from internal models to these external vocabularies.
- **Focus Mode & Story Nodes** — rely on stable, semantic IDs and relationships derived from mapping profiles rather than heuristics.

Operationally:

- ETL pipelines create and update internal entities (files, tables, graph nodes).
- Mapping profiles define how those entities **should appear** in STAC Collections/Items, DCAT Datasets/Distributions/DataServices, and PROV-O Entities/Activities/Agents.
- PROV-O export and catalog exporters consume mapping profiles to generate RDF/JSON artifacts.
- Focus Mode uses those artifacts as ground truth for lineage and metadata overlays.

---

## 🗺️ Diagrams

### 1. Mapping Profiles in the Lineage Pipeline

~~~mermaid
flowchart LR
    subgraph S1[Config & Standards]
        A[Mapping Profiles<br/>YAML + RDF/TTL] --> B[Validation<br/>JSON Schema + SHACL]
        A --> C[Docs & Guides<br/>KFM-MDP v11.2.4]
    end

    subgraph S2[Runtime Pipelines]
        D[ETL Pipelines<br/>src/pipelines/] --> E[Internal Data Products<br/>data/processed/]
        E --> F[PROV-O Export<br/>lineage/prov_export]
        E --> G[Catalog Export<br/>DCAT/STAC]
    end

    B --> F
    B --> G
    F --> H[Lineage Stores<br/>RDF store / Neo4j lineage view]
    G --> I[Catalogs<br/>STAC Collections & DCAT Catalogs]

    H --> J[Focus Mode & Story Nodes]
    I --> J
~~~

### 2. Mapping Profile Lifecycle

~~~mermaid
timeline
    title Mapping Profile Lifecycle (Example)
    2025-12-01 : Author Draft : "Create base mapping for wells dataset"
    2025-12-02 : CI Validates : "mapping-profile-lint & crosswalk checks"
    2025-12-03 : PR Review : "Lineage architect & FAIR+CARE Council"
    2025-12-04 : Merge & Tag : "Profile v0.1.0 used by staging exports"
    2025-12-10 : Production : "Profile promoted; exports and catalogs aligned"
~~~

---

## 🧠 Story Node & Focus Mode Integration

Mapping profiles underpin how Story Nodes and Focus Mode:

- Discover which **external IDs** correspond to a KFM dataset, run, or document.
- Answer questions like:
  - “Which STAC Item and DCAT Dataset correspond to this map layer?”
  - “What PROV-O Entities/Activities explain this dataset’s lineage?”

### 1. Stable Targets for Story Nodes

Story Nodes should:

- Use IDs derived from mapping profiles for:
  - `target` (e.g., DCAT Dataset IRI),
  - `lineage_entity` (PROV-O Entity),
  - `activity_run` (PROV-O Activity),
  - and, when spatial, GeoSPARQL Features.

Example (in a Story Node JSON, not in Markdown):

~~~text
"target": "urn:kfm:dcat:dataset:kgs:wells:v2025-12-02",
"lineage_entity": "urn:kfm:prov:entity:data:kgs-wells:v2025-12-02",
"activity_run": "urn:kfm:prov:activity:etl:kgs-wells:run-142"
~~~

These IRIs SHOULD be constructed via mapping profile rules to ensure consistency.

### 2. Focus Mode Behavior

For mapping-profile–aware views:

- **MAY:**
  - Summarize which external vocabularies a resource is mapped to.
  - Highlight key class/property mappings for a given dataset or pipeline.
  - Show links to STAC Items, DCAT Datasets, and PROV-O Entities/Activities.

- **MUST NOT:**
  - Invent new mappings not present in profiles.
  - Override or “fix” mapping profiles on the fly.
  - Relax governance or sovereignty constraints encoded in the profiles.

---

## 🧪 Validation & CI/CD

Mapping profiles are treated as **contracts** and must be validated rigorously.

### 1. Test Profiles (Extended Matrix)

| Test Profile                        | Purpose                                             | Tooling / Workflow Hint                          |
|------------------------------------|-----------------------------------------------------|--------------------------------------------------|
| `markdown-lint`                    | Docs structure & style                              | Markdownlint, custom scripts                     |
| `schema-lint`                      | YAML front-matter validation                        | JSON Schema validator                            |
| `metadata-check`                   | Required metadata presence                          | Custom validators                                |
| `diagram-check`                   | Mermaid syntax & profile checks                     | Mermaid CLI/parser                               |
| `accessibility-check`              | Basic a11y rules                                    | Markdown a11y tools                              |
| `provenance-check`                 | Front-matter provenance consistency                 | YAML vs footer comparison                        |
| `footer-check`                     | Governance footer correctness                       | Regex/AST-based check                            |
| `mapping-profile-lint`             | Mapping profile schema validation                   | JSON Schema for YAML, SHACL for RDF              |
| `mapping-profile-crosswalk-check`  | Validate external terms and crosswalk completeness  | SPARQL/SHACL checks vs PROV/DCAT/STAC vocabularies |

### 2. Required Validation Steps for Each Profile

For every mapping profile:

1. **Schema Validation**  
   - Validate YAML config using `kfm-lineage-mapping-profile-v0.1.0.schema.json`.  
   - Validate RDF/TTL representation against `kfm-lineage-mapping-profile-shapes-v0.1.0.ttl`.

2. **Crosswalk Checks**  
   - Ensure referenced classes and properties:
     - Exist in PROV-O, DCAT, STAC, GeoSPARQL, or KFM-approved extensions.
     - Are used with correct domain/range where enforced.
   - Verify that required KFM classes/properties for the covered domain are mapped.

3. **Consistency Checks**  
   - Check for duplicate or conflicting mappings for the same KFM label/property within a profile.
   - Prevent conflicting semantic mappings across profiles that claim overlapping coverage (e.g., two active profiles mapping the same KFM label differently).

4. **CI Integration**  
   - `.github/workflows/kfm-ci.yml` MUST:
     - Run mapping-profile tests on changed files under `docs/standards/lineage/mapping-profiles/` and `src/pipelines/lineage/mapping_profiles/`.
     - Fail the PR if any mapping-profile checks fail.
     - Attach validation logs to CI output for review.

---

## 📦 Data & Metadata

Mapping profiles themselves are **data objects**:

- Represented as YAML (authoring) and RDF/TTL (runtime and cataloging).
- Indexed as datasets in DCAT and STAC (e.g., a “Lineage Mapping Profiles” Collection/Series).
- Modeled as `prov:Plan` in PROV-O (plans that govern export Activities).

### 1. Minimal YAML Mapping Profile Skeleton

Conceptual example:

~~~yaml
id: "kfm-lineage-mapping-profile-stac-dcat-prov-v0.1.0"
version: "v0.1.0"
status: "draft"
domain:
  - "hydrology"
  - "wells"
kfm_schema_version: "v11"
applies_to:
  - "kgs-wells"
description: >
  Default mapping profile from KFM internal wells entities to DCAT, STAC, PROV-O, and GeoSPARQL.

iri_patterns:
  dataset_base: "urn:kfm:dcat:dataset:{dataset_id}:{version}"
  item_base: "urn:kfm:stac:item:{collection_id}:{item_id}"
  entity_base: "urn:kfm:prov:entity:{kind}:{id}"
  activity_base: "urn:kfm:prov:activity:{kind}:{run_id}"

class_mappings:
  - name: "dataset_core"
    kfm_label: "Dataset"
    dcat_class: "dcat:Dataset"
    prov_class: "prov:Entity"
    stac_collection: true

  - name: "stac_item"
    kfm_label: "RasterProduct"
    stac_class: "stac:Item"
    prov_class: "prov:Entity"
    geosparql_feature: true

property_mappings:
  - name: "dataset_identity"
    kfm_property: "kfm:semantic_id"
    target:
      - "dct:identifier"
      - "prov:alternateOf"

  - name: "dataset_title"
    kfm_property: "kfm:title"
    target:
      - "dct:title"

  - name: "temporal_coverage"
    kfm_property: "kfm:temporal_extent"
    target:
      - "dct:temporal"

  - name: "geometry"
    kfm_property: "kfm:geometry"
    target:
      - "geo:hasGeometry"
      - "geo:asWKT"

faircare:
  expose_properties:
    - "dct:title"
    - "dct:description"
    - "dct:spatial"
    - "dct:temporal"
  redact_properties:
    - "kfm:exact_site_location"
~~~

Actual schema MUST be defined and enforced by the JSON/SHACL schemas referenced in the front-matter.

### 2. Catalog & Provenance Treatment

- As **DCAT**:
  - Treat each mapping profile as a `dcat:Dataset` with:
    - `dct:title`, `dct:description`, `dct:identifier`, `dct:license`, `dct:modified`.
    - Distributions for YAML and RDF/TTL artifacts.

- As **STAC**:
  - Optionally expose mapping profiles as Items in an internal “documentation/lineage” Collection.

- As **PROV-O**:
  - Model profiles as `prov:Plan` Entities.
  - Link export Activities via `prov:hadPlan` to the profile used.

---

## 🌐 STAC, DCAT & PROV Alignment

This section is intentionally high-level; detailed crosswalks belong in concrete mapping profiles.

### 1. KFM Dataset-Level Mappings

| KFM Concept             | DCAT                       | STAC                          | PROV-O                      | Notes                                         |
|-------------------------|----------------------------|-------------------------------|-----------------------------|-----------------------------------------------|
| Logical dataset         | `dcat:Dataset`             | Collection / Item grouping    | `prov:Entity`               | Abstract dataset identity                     |
| Dataset version         | `dcat:Dataset` + versioning properties | STAC Collection/Item version fields | `prov:Entity` + `prov:wasRevisionOf` | Use DCAT 3.0 versioning where possible       |
| Dataset distribution    | `dcat:Distribution`        | STAC Asset                    | `prov:Entity`               | Files, APIs, tiles, etc.                      |
| Data service / API      | `dcat:DataService`         | STAC API / OGC service        | `prov:SoftwareAgent` / Entity | API entrypoints                             |
| Dataset series          | `dcat:DatasetSeries`       | STAC Collection hierarchy     | PROV Bundle or higher-level Entity | For recurring releases / dataset series |

### 2. Lineage & Process Mappings

| KFM Concept          | DCAT                          | STAC              | PROV-O                         |
|----------------------|-------------------------------|-------------------|---------------------------------|
| ETL run              | Catalog record or provenance note | n/a (metadata) | `prov:Activity`                 |
| Graph load job       | n/a                           | n/a               | `prov:Activity`                 |
| CI pipeline          | n/a                           | n/a               | `prov:Activity` + `prov:Plan`   |
| System / service     | Optional `dcat:DataService`   | STAC API / OGC    | `prov:SoftwareAgent`           |
| Human steward        | `dct:creator` / `dct:publisher` | n/a             | `prov:Person` / `prov:Agent`   |

### 3. Spatial Mappings (GeoSPARQL)

Mapping profiles SHOULD specify:

- Which internal geometry fields map to:
  - `geo:hasGeometry` (Feature → Geometry).
  - `geo:asWKT` / `geo:asGeoJSON` (Geometry → literal).
- Whether feature-level classes (e.g., sites, wells, parcels) are subclasses of `geo:Feature`.
- How to represent bounding boxes vs full geometries when needed.

---

## 🧱 Architecture

### 1. Component Responsibilities

- **Mapping Profiles (Configs)**  
  - Declare crosswalks between KFM and external vocabularies.
  - Are versioned, validated artifacts.

- **Mapping Engine (Pipeline Layer)**  
  - Reads profiles and applies them to internal entities.
  - Produces:
    - DCAT RDF,
    - STAC JSON,
    - PROV-O RDF,
    - GeoSPARQL geometry triples.

- **Export Pipelines**  
  - Use mapping engine outputs to:
    - Write artifacts to `data/processed/lineage/`.
    - Publish STAC/DCAT endpoints.
    - Populate lineage triple store or Neo4j lineage graph.

- **APIs & UI**  
  - Serve lineage and metadata using mapping-derived IDs and relations.
  - Focus Mode consults these APIs and artifacts rather than re-mapping.

### 2. Reproducibility Requirements

For a given export run, logs MUST include:

- Mapping profile ID and version.
- Git commit SHA of mapping engine and profile.
- Input dataset IDs and versions.
- Export artifact IDs (URIs/paths).

Given these, a lineage export MUST be reconstructible.

### 3. Change Management

Any change to mapping-profile semantics MUST:

1. Update:
   - Mapping profile YAML/RDF.
   - Associated tests and fixtures.
   - This standard if patterns or schemas change.
2. Bump mapping profile version (e.g., `v0.2.0`) and record changes in its own README.
3. Add a new row to this document’s Version History if the standard itself changes.
4. Coordinate with the PROV-O Export Standard to ensure consistency.

---

## ⚖ FAIR+CARE & Governance

Mapping profiles are a key mechanism for enforcing FAIR+CARE and sovereignty constraints at the **metadata and lineage layer**.

- **FAIR**
  - **Findable:** stable IRIs and explicit crosswalks to widely-used vocabularies.
  - **Accessible:** open, CC-BY 4.0–licensed profile artifacts in the repo.
  - **Interoperable:** mappings to DCAT, STAC, PROV-O, GeoSPARQL, OWL-Time.
  - **Reusable:** clear documentation, versioning, provenance, and licensing of the mappings themselves.

- **CARE**
  - **Collective Benefit:** mapping profiles support transparent understanding of how data and lineage are presented to communities and partners.
  - **Authority to Control:** profiles MUST encode any constraints on exposing location, identity, or sensitive attributes for Indigenous or culturally sensitive data.
  - **Responsibility & Ethics:** authors MUST consider whether fields should be generalized or omitted from public exports and document these decisions.

- **Governance Hooks**
  - Sensitive profiles (e.g., those involving protected sites) MAY require FAIR+CARE Council review before promotion to production.
  - `governance_ref`, `ethics_ref`, and `sovereignty_policy` in front-matter are normative; authors MUST consult those documents when designing mappings.

---

## 🕰️ Version History

| Version   | Date       | Status | Summary                                                                                                  |
|----------:|------------|--------|----------------------------------------------------------------------------------------------------------|
| **v0.1.0** | 2025-12-07 | Draft  | Initial mapping profiles standard: defined directory layout, mapping-profile schema expectations, CI tests, and high-level STAC/DCAT/PROV/GeoSPARQL alignment. |

---

<div align="center">

📑 **KFM Lineage — Mapping Profiles Standard (Draft v0.1.0)**  
Deterministic Crosswalks · Open Provenance · FAIR+CARE-Aligned Semantics  

[📘 Docs Root](../../../) · [📂 Lineage Standards Index](../README.md) · [⚖ Governance](../../../governance/ROOT-GOVERNANCE.md)

</div>
