---
title: "🧩 Kansas Frontier Matrix — Pipeline Patterns"
path: "docs/pipelines/patterns/README.md"
version: "v0.1.0"
last_updated: "2025-12-05"
release_stage: "Draft"
lifecycle: "Active Development"
review_cycle: "Quarterly · Pipelines WG & FAIR+CARE Council"
content_stability: "experimental"
commit_sha: "<latest-commit-hash>"
signature_ref: "releases/docs-pipelines-patterns/v0.1.0/signature.sig"
attestation_ref: "releases/docs-pipelines-patterns/v0.1.0/slsa-attestation.json"
sbom_ref: "releases/docs-pipelines-patterns/v0.1.0/sbom.spdx.json"
manifest_ref: "releases/docs-pipelines-patterns/v0.1.0/manifest.zip"
telemetry_ref: "releases/docs-pipelines-patterns/v0.1.0/focus-telemetry.json"
telemetry_schema: "schemas/telemetry/markdown-protocol-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
governance_ref: "../../governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
status: "Draft"
doc_kind: "Guide"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
scope:
  domain: "pipelines"
  applies_to:
    - "etl"
    - "graph"
    - "api"
    - "web"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM Pipelines WG · FAIR+CARE Council"
ttl_policy: "24 months"
sunset_policy: "Superseded when v1.0.0 is released"
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
provenance_chain:
  - "docs/pipelines/README.md@v0.1.0"
provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: false
  must_reference_origin_root: true
json_schema_ref: "schemas/json/docs-pipelines-patterns-v0.1.0.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-patterns-v0.1.0-shape.ttl"
story_node_refs: []
immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:patterns:readme:v0.1.0"
semantic_document_id: "kfm-pipelines-patterns-readme-v0.1.0"
event_source_id: "ledger:kfm:doc:pipelines:patterns:readme:v0.1.0"
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
    - "summary"
    - "timeline-generation"
    - "semantic-highlighting"
    - "3d-context-render"
    - "a11y-adaptations"
    - "diagram-extraction"
    - "metadata-extraction"
  prohibited:
    - "content-alteration"
    - "speculative-additions"
    - "unverified-architectural-claims"
    - "narrative-fabrication"
    - "governance-override"
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
deprecated_fields: []
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Pipeline Patterns README**  
`docs/pipelines/patterns/README.md`

**Purpose:**  
Define the canonical layout and authoring rules for **pipeline pattern documentation** in the KFM monorepo.  
This README explains how to organize pattern guides, keep them CI-safe, and wire them cleanly into ETL → STAC/DCAT/PROV → Neo4j → API → Web.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue "Master Coder Protocol v6.3")]() · [![KFM–MDP v11.2.4](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.4-informational "Markdown Protocol v11.2.4")]() · [![Pipelines](https://img.shields.io/badge/Domain-Pipelines-success "Pipelines Domain")]() · [![Status: Draft](https://img.shields.io/badge/Status-Draft-orange "Draft until reviewed")]()

</div>

---

## 📘 Overview

This document is the **entry point** for all KFM **pipeline pattern** docs:

- Establishes the **directory structure** for pattern guides under `docs/pipelines/patterns/`.
- Defines how pattern docs link to **implementation code** under `src/pipelines/**`.
- Aligns patterns with **STAC/DCAT/PROV** metadata and the **Neo4j** knowledge graph backbone.
- Ensures every pattern is:
  - **Deterministic & config-driven** (MCP 2.0),
  - **Catalog-ready** (STAC/DCAT),
  - **Provenance-complete** (PROV-O),
  - **Story-Node-friendly** for Focus Mode overlays.

Treat this README as the **“index + contract”** for pipeline patterns. If a pattern is not documented here (or linked from here), it isn’t considered a first-class KFM pattern.

---

## 🗂️ Directory Layout

The pipeline pattern docs must match this emoji-based layout:

~~~text
KansasFrontierMatrix/
├── 📂 docs/
│   ├── 📂 pipelines/
│   │   ├── 📄 README.md                 # High-level pipelines index
│   │   ├── 📂 patterns/                 # Pattern catalog (this directory)
│   │   │   ├── 📄 README.md             # Pipeline patterns index (this file)
│   │   │   ├── 📂 batch-etl/            # Nightly/batch ingestion templates
│   │   │   ├── 📂 streaming/            # Kafka/streaming/incremental patterns
│   │   │   ├── 📂 hybrid/               # Lambda/Kappa & mixed-mode designs
│   │   │   ├── 📂 geospatial/           # Spatial ETL & STAC-focused patterns
│   │   │   ├── 📂 ai-ml/                # ML training/inference pipelines
│   │   │   └── 📂 experimental/         # Draft / research patterns (not yet governed)
│   │   └── 📂 sops/                     # Pipeline SOPs (runbooks, incident guides)
│   └── 📂 standards/
│       ├── 📄 kfm_markdown_protocol_v11.2.4.md
│       └── 📂 ...
├── 📂 src/
│   ├── 📂 pipelines/                    # Implementation of pipeline patterns
│   │   ├── 📂 batch/                    # Batch orchestration code (e.g. Airflow)
│   │   ├── 📂 streaming/                # Streaming jobs (e.g. Flink/Kafka Streams)
│   │   ├── 📂 hybrid/                   # Shared hybrid components
│   │   └── 📂 shared/                   # Common libs (logging, metrics, helpers)
│   └── 📂 graph/                        # Neo4j loaders & lineage extractors
└── 📂 data/
    ├── 📂 sources/                      # Source manifests for pipeline inputs
    ├── 📂 raw/                          # Raw ingested data (DVC/LFS-managed)
    ├── 📂 work/                         # Normalized / enriched intermediates
    ├── 📂 processed/                    # Analysis-ready outputs
    └── 📂 stac/                         # STAC Collections & Items for outputs
~~~

### Author Rules

- **Always use emojis**:
  - `📂` for directories, `📄` for Markdown files, in all directory trees.
- Directory trees **must**:
  - Use a fenced code block with `text`,
  - Use `├──` / `└──` glyphs and spaces (no tabs),
  - Include **short inline comments** where helpful.
- Each subdirectory under `docs/pipelines/patterns/` must contain:
  - A `README.md` describing that pattern family,
  - Links to specific pattern docs (e.g. `batch-etl/daily-noaa-sync.md`).

---

## 🧭 Context

Pipeline pattern docs sit between **high-level architecture** and **concrete SOPs**:

- `docs/architecture/*` – overall system design (Neo4j, API, Focus Mode).
- `docs/pipelines/README.md` – big-picture pipeline overview & lifecycle.
- `docs/pipelines/patterns/**` – reusable **design templates** (this space).
- `docs/pipelines/sops/**` – **how to run** and operate concrete pipelines.

Each pattern document should answer:

1. **When to use this pattern** (tradeoffs, constraints).
2. **How it flows** through the KFM stack:  
   raw → work → processed → STAC/DCAT → Neo4j → API → Web.
3. **What must be documented** (config, metadata, provenance).

---

## 🧱 Architecture

Each pattern under `docs/pipelines/patterns/` should:

- Describe the **ETL topology**:
  - Batch vs streaming vs hybrid.
  - Orchestrator (Airflow, Dagster, etc.) and message bus (Kafka, etc.).
- Declare **interfaces**:
  - Expected **inputs** (source manifests in `data/sources/`),
  - Produced **artifacts** in `data/processed/` and `data/stac/`,
  - Graph ingestion contracts for `src/graph/**`.
- Provide a **minimal diagram** (in the pattern doc itself) using `mermaid-flowchart-v1`.

Example architectural bullets a pattern might include:

- **Batch ETL**:
  - Nightly NOAA ingestion, idempotent, partitioned by date.
- **Streaming**:
  - Kafka topic per source, Flink job for windowed aggregation.
- **Hybrid**:
  - Streaming ingest + batch backfill for long history.

---

## 🧪 Validation & CI/CD

KFM CI (`.github/workflows/kfm-ci.yml`) must be able to reason about patterns:

- Every new pattern doc:
  - Must pass **`markdown-lint`**, **`schema-lint`**, **`metadata-check`**, and **`footer-check`**.
  - Should include an example **config file path** and **entrypoint CLI**.
- Pattern-specific tests:
  - Unit/integration tests for code in `src/pipelines/**` should be linked or referenced.
  - If a pattern mandates STAC output, CI should run **STAC validation** against a sample.

Recommended checklist per pattern:

- ✅ Config-driven, seed logged.
- ✅ Inputs and outputs mapped to `data/**` subtrees.
- ✅ STAC/DCAT metadata example included.
- ✅ PROV activities identified (ETL, QA, publish).
- ✅ Links to tests and SOPs.

---

## 📦 Data & Metadata

Pattern docs should be **metadata-aware**:

- For each pattern, specify:
  - How **STAC Items** will be generated for outputs in `data/stac/`.
  - How **DCAT dataset records** will describe collections of outputs.
  - What **PROV entities/activities/agents** are involved (high level).

At minimum, each pattern must:

- Name the STAC Collection(s) it expects.
- Specify `id`, `geometry` strategy (per-item vs shared), and `properties.datetime` semantics.
- Indicate how lineage is expressed:
  - e.g., `prov:wasGeneratedBy` from a named ETL activity to each STAC Item.

---

## 🕰️ Version History

| Version   | Date       | Summary                                                                                                    |
|----------:|------------|------------------------------------------------------------------------------------------------------------|
| **v0.1.0** | 2025-12-05 | Initial draft of pipeline patterns README. Aligned with KFM-MDP v11.2.4, added emoji directory layout and CI/metadata guidance. |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Pipeline Patterns README**  
Deterministic Pipelines · Open Provenance · FAIR+CARE-Aligned Metadata  

[📘 Docs Root](../..) · [📂 Pipelines Index](../README.md) · [⚖ Governance](../../governance/ROOT-GOVERNANCE.md)

</div>