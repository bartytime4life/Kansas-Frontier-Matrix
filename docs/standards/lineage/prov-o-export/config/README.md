---
title: "📑 KFM Lineage — PROV-O Export Config Standard"
path: "docs/standards/lineage/prov-o-export/config/README.md"
version: "v0.1.0"
last_updated: "2025-12-07"
release_stage: "Draft / For Review"
lifecycle: "Planned Long-Term Support (LTS)"
review_cycle: "Annual · FAIR+CARE Council & Focus Mode Board"
content_stability: "draft"
commit_sha: "<pending-commit-sha>"
signature_ref: "releases/lineage-prov-o-export-config/v0.1.0/signature.sig"
attestation_ref: "releases/lineage-prov-o-export-config/v0.1.0/slsa-attestation.json"
sbom_ref: "releases/lineage-prov-o-export-config/v0.1.0/sbom.spdx.json"
manifest_ref: "releases/lineage-prov-o-export-config/v0.1.0/manifest.zip"
telemetry_ref: "releases/lineage-prov-o-export-config/v0.1.0/lineage-config-telemetry.json"
telemetry_schema: "schemas/telemetry/lineage-prov-o-export-config-v0.1.0.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../../../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
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
    - "prov-o-export-config"
    - "lineage-graph"
    - "etl-pipelines"
semantic_intent:
  - "lineage"
  - "export-config"
  - "governance"
category: "Lineage · PROV-O · Config"
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
sunset_policy: "Superseded when KFM Lineage — PROV-O Export Standard reaches v1.x"
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
json_schema_ref: "schemas/json/kfm-lineage-prov-o-export-config-v0.1.0.schema.json"
shape_schema_ref: "schemas/shacl/kfm-lineage-prov-o-export-config-v0.1.0-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:standards:lineage:prov-o-export:config:v0.1.0"
semantic_document_id: "kfm-lineage-prov-o-export-config-v0.1.0"
event_source_id: "ledger:kfm:doc:standards:lineage:prov-o-export:config:v0.1.0"
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
  - "lineage-config-schema"
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

# 📑 **KFM Lineage — PROV-O Export Config Standard (Draft v0.1.0)**  
`docs/standards/lineage/prov-o-export/config/README.md`

**Purpose:**  
Define the canonical configuration contract for KFM PROV-O export pipelines.  
This standard describes the YAML/JSON configuration structure, required fields, and validation rules so that all PROV-O export jobs are deterministic, reproducible, and CI/audit-ready.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() ·
[![KFM-MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-informational "Markdown Protocol v11.2.4")]() ·
[![PROV-O](https://img.shields.io/badge/Provenance-W3C_PROV--O-purple "W3C PROV-O")]() ·
[![DCAT 3.0](https://img.shields.io/badge/Metadata-DCAT_3.0-teal "W3C DCAT 3.0")]() ·
[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange "Draft / For Review")]()

</div>

---

## 📘 Overview

### 1. Scope and Intent

This document defines the **configuration layer** for the KFM Lineage — PROV-O Export pipeline:

- Specifies the **YAML/JSON schema** for PROV-O export configs.
- Ensures every export is **re-runnable** from a pinned config + git commit + data versions.
- Aligns configuration with **DCAT 3.0**, **STAC 1.x**, and **PROV-O** modeling.
- Provides a single, governed reference for all `src/pipelines/lineage/prov_export/config/` files.

It is subordinate to, and consistent with:

- **KFM Lineage — PROV-O Export Standard** (logical lineage model and export behavior).
- **KFM-MDP v11.2.4** (Markdown authoring).
- **ETL / pipeline architecture standards** (deterministic ETL, MCP 2.0).

### 2. Core Principles

1. **Config-as-Contract**  
   Every PROV-O export is defined entirely by a versioned config file. If it’s not in config, it’s not part of the contract.

2. **Deterministic & Reproducible**  
   Given:
   - a config file,
   - a git commit,
   - and versioned inputs,  
   the export MUST reproduce the same PROV-O graph (modulo timestamps when allowed).

3. **Catalog-First**  
   Configs reference data via **DCAT/STAC identifiers**, not ad-hoc paths, wherever possible.

4. **Graph-Centric**  
   Configs describe how to build **Entities, Activities, and Agents** in PROV-O terms, not how to “pretty-print logs”.

5. **Governed Lineage**  
   Configs MUST respect FAIR+CARE and Indigenous sovereignty constraints; sensitive workflows may require redacted or private exports.

6. **Schema-Enforced**  
   All configs MUST validate against `kfm-lineage-prov-o-export-config-v0.1.0` JSON Schema and SHACL shapes before merge.

### 3. Configuration Artifacts in KFM

This standard governs configs for:

- **Batch PROV-O export jobs** (e.g., per ETL run, per dataset version).
- **Streaming lineage exports** (where events are aggregated into PROV graphs).
- **Hybrid pipelines** that export both RDF triples and Neo4j lineage views.

Configs are stored under:

- `src/pipelines/lineage/prov_export/config/*.yaml`
- Optional JSON equivalents for systems that prefer JSON.

### 4. Author Quickstart (Config Authors)

When adding a new PROV-O export config:

1. **Copy the template**  
   Start from `src/pipelines/lineage/prov_export/config/example-template.yaml`.

2. **Fill in identity & catalog references**  
   - Set `id`, `label`, `version`.
   - Reference DCAT/STAC IDs instead of bare paths where possible.

3. **Bind to ETL runs and datasets**  
   - Link to pipeline IDs, run selectors, and dataset identifiers.
   - Declare input and output roles (prov:PrimarySource, prov:Revision, etc.).

4. **Specify export behavior**  
   - Output directory and formats (TTL, JSON-LD, PROV-JSON).
   - Bundle strategy (per-run, per-dataset, or per-collection).

5. **Configure validation**  
   - Point to SHACL shapes and enable strict mode.
   - Enable/disable Neo4j lineage view loading.

6. **Run CI locally**  
   - Use the CLI helper to run `schema-lint` and `prov-export-contract` before pushing.

---

## 🗂️ Directory Layout

Canonical layout for PROV-O export configs and related artifacts:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   ├── 📂 standards/
│   │   └── 📂 lineage/
│   │       └── 📂 prov-o-export/
│   │           └── 📂 config/
│   │               └── 📄 README.md                  # This document
│   ├── 📂 architecture/
│   │   └── 📂 lineage/
│   │       └── 📄 prov-graph.md                     # Lineage graph design (proposed)
│   └── 📂 guides/
│       └── 📂 lineage/
│           └── 📄 prov-o-export-cli.md              # CLI usage guide (proposed)
├── 📂 src/
│   └── 📂 pipelines/
│       └── 📂 lineage/
│           └── 📂 prov_export/
│               ├── 📂 config/
│               │   ├── 📄 example-template.yaml     # Canonical template
│               │   ├── 📄 kgs-wells.yaml            # Example dataset config
│               │   └── 📄 <project>.yaml            # Additional configs by domain
│               ├── 📂 jobs/
│               │   └── 📄 export_prov.py            # Batch/stream export jobs
│               └── 📄 cli.py                        # `kfm-provenance export` entrypoint
├── 📂 data/
│   ├── 📂 processed/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           ├── 📂 ttl/                          # PROV-O Turtle exports
│   │           ├── 📂 jsonld/                       # PROV-O JSON-LD exports
│   │           └── 📂 provjson/                     # PROV-JSON exports
│   ├── 📂 releases/
│   │   └── 📂 lineage/
│   │       └── 📂 prov/
│   │           └── 📂 v*/                           # Versioned lineage bundles
│   └── 📂 stac/
│       └── 📂 lineage/
│           └── 📂 collections/                      # STAC Collections for lineage artifacts
└── 📂 schemas/
    ├── 📂 json/
    │   └── 📄 kfm-lineage-prov-o-export-config-v0.1.0.schema.json
    └── 📂 shacl/
        └── 📄 kfm-lineage-prov-o-export-config-v0.1.0-shape.ttl
~~~

**Author and Implementer Rules:**

- Every directory above MUST have a `README.md` once created, describing purpose and data contracts.
- Directory trees MUST use:
  - `~~~text` fences,
  - canonical `├──` / `└──` glyphs,
  - `📂` for directories and `📄` for files.
- Any path changes MUST be reflected here **and** in JSON/SHACL schemas.

---

## 🧭 Context

This config standard sits between:

- **ETL & data pipelines** (where logs and run metadata are produced).
- **Catalog layers (DCAT/STAC)** (where datasets and assets are described).
- **Lineage modeling (PROV-O)** (where Entities/Activities/Agents are linked).
- **Knowledge graph & Focus Mode** (where lineage drives explanations and overlays).

Configs provide the **binding**:

- Which ETL runs (Activities) and datasets (Entities) to include.
- How to map pipeline metadata into PROV-O structures.
- Where to store exports and how to surface them via catalogs and APIs.

---

## 🗺️ Diagrams

### 1. Config-Driven Lineage Export Flow

~~~mermaid
flowchart LR
    C[Config File<br/>prov_export/config/*.yaml]
        --> P[ETL / Data Pipelines<br/>src/pipelines/...]
    P --> H[Lineage Harvest<br/>logs, run metadata]
    H --> X[PROV-O Export Job<br/>prov_export/jobs/]
    X --> G[PROV Graph Artifacts<br/>data/processed/lineage/prov/]
    G --> A[APIs & Lineage UI<br/>src/api/lineage/prov/]
    A --> F[Focus Mode & Story Nodes]
~~~

---

## 🧠 Story Node & Focus Mode Integration

- Focus Mode MAY surface **config-derived explanations**, such as:
  - “This dataset’s lineage is exported using config `kgs-wells.yaml`.”
  - “Lineage includes ETL runs matching this selector.”
- Story Nodes SHOULD reference:
  - Dataset IRIs (DCAT/STAC),
  - PROV Entities/Activities/Agents,  
  **not** raw config filenames, except as supporting detail.

Configs themselves:

- Are technical artifacts, usually not end-user narrative targets.
- MUST NOT be altered by Focus Mode; only summarized or highlighted within `ai_transform_permissions`.

---

## 🧪 Validation & CI/CD

### 1. Test Profiles

For this standard, the following apply:

- `markdown-lint` — This README structure and style.
- `schema-lint` — Front-matter validation against the docs schema.
- `metadata-check` — Required metadata fields present.
- `diagram-check` — Mermaid diagrams syntactically valid.
- `accessibility-check` — Structural accessibility (headings, lists).
- `provenance-check` — Consistency between front-matter and Version History.
- `footer-check` — Footer presence and correctness.
- `prov-export-contract` — PROV export artifacts obey PROV-O and KFM-PROV contracts.
- `prov-graph-consistency` — Lineage graphs are structurally sane.
- `lineage-config-schema` — **Config files** validate against `kfm-lineage-prov-o-export-config-v0.1.0`.

### 2. Config Validation Requirements

Every config file MUST:

1. **Schema-validate**  
   - Pass JSON Schema validation (`lineage-config-schema`).
   - Use only allowed keys and enumerations.

2. **Reference-resolve**  
   - DCAT/STAC IDs MUST resolve to known datasets/collections.
   - Pipeline IDs and run selectors MUST correspond to actual ETL jobs.

3. **CI Enforcement**

- `.github/workflows/kfm-ci.yml` MUST:
  - Run `lineage-config-schema` on any changed `prov_export/config/*.yaml`.
  - Fail PRs on any validation error.
  - Optionally attach a summary of impacted exports.

---

## 📦 Data & Metadata

### 1. Top-Level Config Structure (Conceptual)

Each config file MUST follow this high-level structure:

- `id` — Stable identifier for the config (URI-safe string).
- `label` — Human-friendly name.
- `description` — Short description of the export’s purpose.
- `version` — Config version (not dataset or pipeline version).
- `dataset` — References to datasets being described.
- `pipeline` — Link to the originating ETL/processing pipeline.
- `run_selector` — How to pick runs/instances to export.
- `inputs` — Upstream entities (datasets, files, services).
- `outputs` — Downstream entities (datasets, files, services).
- `export` — Export behavior (formats, output locations, bundle strategy).
- `validation` — Validation rules for the export job.
- `graph_mapping` — Neo4j/triple-store integration, if applicable.
- `notes` — Free-form non-normative notes.

### 2. Example Config (YAML, Non-Normative)

~~~yaml
id: "urn:kfm:config:lineage:prov-o-export:kgs-wells:v2025-12-02"
label: "KGS Wells — PROV-O Export"
description: "Export lineage for KGS wells ETL runs into PROV-O graphs."
version: "v0.1.0"

dataset:
  dcat_id: "urn:kfm:dataset:kgs:wells"
  stac_collection: "kfm-kgs-wells"
  stac_item_selector:
    collection: "kfm-kgs-wells"
    match_assets:
      roles: ["data"]
      media_types: ["application/geo+json"]

pipeline:
  id: "etl-kgs-wells"
  repo_path: "src/pipelines/hydrology/kgs_wells/"
  config_ref: "configs/prod.yaml"

run_selector:
  mode: "by-tag"
  tag: "release-2025-12-02"
  min_status: "success"

inputs:
  - id: "raw_kgs_wells_csv"
    role: "prov:PrimarySource"
    kind: "file-glob"
    path: "data/raw/kgs/wells/*.csv"
  - id: "reference_crs"
    role: "prov:Other"
    kind: "doc"
    dcat_id: "urn:kfm:dataset:reference:crs"

outputs:
  - id: "processed_kgs_wells_geojson"
    role: "prov:Generated"
    kind: "stac-items"
    stac_collection: "kfm-kgs-wells"

export:
  base_iri: "https://data.kfm.ks.gov/prov/"
  output_dir: "data/processed/lineage/prov/kgs-wells/2025-12-02/"
  formats:
    - "ttl"
    - "jsonld"
  bundle_strategy: "per-run"
  include_logs: true
  include_config_snapshot: true

validation:
  shacl_shape: "schemas/shacl/kfm-lineage-prov-graph-v0.1.0-shape.ttl"
  strict: true
  fail_on_warnings: false

graph_mapping:
  neo4j:
    enabled: true
    database: "lineage"
    constraint_profile: "kfm-lineage-v1"

notes:
  - "Initial config for KGS wells lineage; treat as experimental until v1.0.0."
~~~

### 3. Required Fields

At minimum, configs MUST include:

- `id`, `label`, `description`, `version`
- `dataset.dcat_id`
- `pipeline.id`
- `run_selector.mode`
- `export.base_iri`, `export.output_dir`, `export.formats`
- `validation.shacl_shape`
- `validation.strict`

All required-ness is enforced via the JSON Schema referenced in front-matter.

---

## 🌐 STAC, DCAT & PROV Alignment

Configs MUST explicitly encode:

- **DCAT**:
  - `dataset.dcat_id` → `dcat:Dataset` IRI.
- **STAC**:
  - `dataset.stac_collection` or `stac_item_selector` → STAC Collections/Items.
- **PROV-O**:
  - `inputs[*].role`, `outputs[*].role` → PROV roles (e.g., `prov:PrimarySource`, `prov:Revision`).
  - Pipeline and run metadata → `prov:Activity` instances.
  - Agents (ETL services, organizations) derived from pipeline context.

This ensures exported graphs can:

- Link Entities to cataloged datasets.
- Express derivation and responsibility via PROV core relations.

---

## 🧱 Architecture

### 1. Config-Driven Export Lifecycle

Conceptual steps:

1. **Config Load**  
   CLI loads a single config file and validates it.

2. **Run Resolution**  
   `run_selector` translates into one or more ETL runs (by tag, date range, ID, etc.).

3. **Harvest**  
   Logs, metrics, and catalog entries are harvested for those runs.

4. **Graph Construction**  
   Entities/Activities/Agents are created following mapping rules in the config.

5. **Serialization & Storage**  
   PROV-O graphs written in configured formats/locations.

6. **Optional Graph Loading**  
   Neo4j / triple-store ingestion for lineage exploration.

### 2. Reproducibility

To re-run an export:

- Pin:
  - config `id` & `version`,
  - git `commit_sha`,
  - dataset versions (via DCAT/STAC),
  - and any external shape/config references.
- Re-run `kfm-provenance export --config <file>`.

If output differs beyond allowed nondeterminism (timestamps, ordering), treat as a regression.

---

## ⚖ FAIR+CARE & Governance

- **FAIR**
  - Configs help make lineage **Findable** and **Reusable** by binding datasets to PROV-O graphs.
  - Use catalog IDs and stable IRIs, not ad-hoc paths.
- **CARE**
  - If a pipeline handles sensitive or restricted data:
    - Configs MUST allow scoping or redaction of exports.
    - Lineage graphs MAY be partitioned into public vs restricted bundles.
  - Governance and sovereignty policies MUST be consulted before enabling public export.

---

## 🕰️ Version History

| Version   | Date       | Status | Summary                                                                                         |
|----------:|------------|--------|-------------------------------------------------------------------------------------------------|
| **v0.1.0** | 2025-12-07 | Draft  | Initial config standard: defined directory layout, config schema expectations, validation rules, and alignment with PROV-O export and catalog standards. |

---

<div align="center">

📑 **KFM Lineage — PROV-O Export Config Standard (Draft v0.1.0)**  
Deterministic Pipelines · Open Provenance · FAIR+CARE-Aligned Lineage  

[📘 Docs Root](../../../../) · [📂 Lineage Standards Index](../../README.md) · [⚖ Governance](../../../../governance/ROOT-GOVERNANCE.md)

</div>

