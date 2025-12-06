---
title: "🧩 Kansas Frontier Matrix — Schema Validation Workflow (`schema-lint.yml`) (Diamond⁹ Ω / Crown∞Ω)"
path: "docs/workflows/schema-lint.yml.md"

version: "v11.2.4"
last_updated: "2025-12-06"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Continuous · Autonomous"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
signature_ref: "releases/v11.2.4/signature.sig"
attestation_ref: "releases/v11.2.4/slsa-attestation.json"
sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/schema-lint-telemetry.json"
telemetry_schema: "schemas/telemetry/schema-lint-workflow-v11.2.4.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

status: "Active / Enforced"
doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"

scope:
  domain: "ci-cd-workflows"
  applies_to:
    - ".github/workflows/schema-lint.yml"
    - "schemas/**"
    - "docs/**"
    - "data/**"

fair_category: "F1-A1-I2-R2"
care_label: "FAIR+CARE Governance Aligned"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Public"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

ttl_policy: "24 months"
sunset_policy: "Superseded by Schema Validation Workflow v12"

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
  - "docs/workflows/schema-lint.yml.md@v10.2.4"
  - "docs/workflows/schema-lint.yml.md@v10.1.0"
  - "docs/workflows/schema-lint.yml.md@v9.9.0"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/kfm-markdown-protocol-v11.2.4.schema.json"
shape_schema_ref: "schemas/shacl/kfm-markdown-protocol-v11.2.4-shape.ttl"
story_node_refs: []

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:workflows:schema-lint-yml:v11.2.4"
semantic_document_id: "kfm-workflow-schema-lint-yml-v11.2.4"
event_source_id: "ledger:kfm:doc:workflows:schema-lint-yml:v11.2.4"
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
  - "metadata-check"
  - "diagram-check"
  - "accessibility-check"
  - "provenance-check"
  - "footer-check"

ci_integration:
  workflow: ".github/workflows/schema-lint.yml"
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
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

deprecated_fields:
  - "old_markdown_standard_v10.4"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Schema Validation Workflow (`schema-lint.yml`)**  
`docs/workflows/schema-lint.yml.md`

**Purpose**  
Define the **governed GitHub Actions workflow** that validates **JSON, YAML, STAC, DCAT, and PROV schemas** used across the Kansas Frontier Matrix (KFM).  
This workflow ensures that **schemas, examples, and configuration files** remain **valid, consistent, and interoperable**, forming a reliable foundation for ETL pipelines, catalogs, the knowledge graph, and Focus Mode.

<img src="https://img.shields.io/badge/Docs·MCP-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.4-purple" />
<img src="https://img.shields.io/badge/License-CC--BY%204.0-green" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governance%20Aligned-orange" />
<img src="https://img.shields.io/badge/Status-Automated-brightgreen" />

</div>

---

## 📘 Overview

### 1. Workflow Intent

`schema-lint.yml` is the **schema integrity gate** for KFM. It validates:

- ✅ **JSON Schemas** for docs, telemetry, pipelines, Story Nodes, and metadata.  
- ✅ **YAML/JSON Configs** (pipelines, ETL params, workflow configs) against those schemas.  
- ✅ **STAC/DCAT/PROV Shapes** (JSON/JSON-LD, SHACL) used by KFM catalogs.  
- ✅ **Examples & Test Fixtures** under `schemas/` and `docs/` to prevent drift.  

By enforcing consistent schemas, this workflow protects:

- Deterministic ETL behavior,  
- Catalog interoperability (STAC/DCAT),  
- Knowledge graph ingestion (Neo4j, PROV, CIDOC-CRM),  
- Focus Mode transformers that rely on stable document/telemetry formats.

### 2. Role in the KFM Pipeline

Within:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → React/MapLibre/Cesium frontend → Story Nodes → Focus Mode

`schema-lint.yml` acts as:

- A **contract validator** that runs before data or docs are considered valid for production.  
- A **change guard** that blocks breaking schema changes from reaching catalogs, graph, or UIs.

---

## 🗂️ Directory Layout

~~~text
📁 docs/
└── 📁 workflows/
    📄 README.md                           — CI/CD & governance workflows index
    📄 schema-lint.yml.md                  — ← This schema validation workflow spec

📁 .github/
└── 📁 workflows/
    📄 schema-lint.yml                     — GitHub Actions workflow (schema validation)

📁 schemas/
├── 📁 json/                               — JSON Schemas (docs, pipelines, Story Nodes, telemetry)
├── 📁 shacl/                              — SHACL shapes for graph and RDF structures
└── 📁 examples/                           — Example payloads & fixtures for validation

📁 tools/
└── 📁 schemas/
    📄 validate_json_schemas.py            — Validates JSON Schemas themselves
    📄 validate_payloads.py                — Validates examples/configs against schemas
    📄 validate_shacl.py                   — Runs SHACL checks for RDF/graph data
    📄 summarize_schema_lint.mjs           — Aggregates validation results to summary JSON/MD

📁 reports/
└── 📁 self-validation/
    📁 schemas/
        📄 schema_validation.json          — Detailed per-file results
        📄 shacl_validation.json           — SHACL validation outcomes
        📄 payload_validation.json         — Config/example validation results
        📄 lint_summary.json               — Canonical machine-readable summary
        📄 summary.md                      — Human-readable summary for PRs

📁 releases/
└── 📁 v11.2.4/
    📄 schema-lint-telemetry.json          — Aggregated schema-lint telemetry
    📄 sbom.spdx.json                      — SBOM for validators and dependencies
    📄 manifest.zip                        — Release manifest (configs, versions, checksums)
~~~

---

## 🧭 Context

### 1. Triggers & Scope

| Trigger            | Paths                                  | Notes                                    |
|-------------------:|----------------------------------------|------------------------------------------|
| `pull_request`     | `schemas/**`, `configs/**`, `docs/**`  | Blocks merges with schema-breaking changes |
| `push` (protected) | `schemas/**`, `configs/**`, `docs/**`  | Required on `main` & `release/**`        |
| `workflow_dispatch`| —                                      | Manual re-runs for schema migrations     |

**Primary coverage:**

- JSON/JSON-LD schemas under `schemas/json/**`.  
- SHACL shapes under `schemas/shacl/**`.  
- Example payloads under `schemas/examples/**` and `docs/**` that declare a `$schema` or `schema_ref`.  
- Pipeline and workflow configs under `configs/**`.

### 2. Relationship to Other Workflows

- **Upstream:** Developer changes to schemas or configs.  
- **Peers:**
  - `docs-lint.yml` — structure & Markdown compliance.  
  - `faircare-validate.yml` — FAIR+CARE data and doc validation.  
  - `stac-validate.yml` — STAC/DCAT catalog validation.  
- **Downstream:**
  - ETL pipelines that rely on validated contracts.  
  - Catalog and graph loaders that assume stable schema structure.  
  - Frontend and Focus Mode that depend on well-typed responses.

---

## 🗺️ Diagrams

### Schema Validation Flow

~~~mermaid
flowchart LR
    A["PR / Push / Manual Trigger"] --> B["Checkout & Install Validators"]
    B --> C["Validate JSON Schemas & Examples"]
    C --> D["Validate SHACL Shapes & RDF Structures"]
    D --> E["Summarize Results (JSON · MD)"]
    E --> F["Upload Artifacts · Emit Telemetry"]
    F --> G["Governance Ledger · Downstream Pipelines"]
~~~

---

## 🧠 Story Node & Focus Mode Integration

### 1. Story Nodes

Schema validation runs may produce Story Nodes such as:

- `urn:kfm:story-node:infra:schema-lint:<run_id>`  
  - Summarizes schemas checked, failures found, and impacted areas.  

- `urn:kfm:story-node:infra:schema-evolution:<schema_id>`  
  - Describes the evolution of a key schema (e.g., telemetry, Story Node JSON).

Story Nodes reference:

- `reports/self-validation/schemas/lint_summary.json` for the run.  
- Specific schemas by `semantic_document_id` or schema ID.  
- Governance decisions around breaking or non-breaking schema changes.

### 2. Focus Mode

Focus Mode can:

- Summarize **schema health** for a given domain (e.g., telemetry, Story Nodes).  
- Show **change history** and highlight breaking vs. additive changes.  
- Link from documentation (guides, standards) to the latest schema validation results.

Focus Mode must not:

- Override schema definitions or declare a schema “safe” without matching reports.  
- Invent validation results; it may only present recorded outcomes.

---

## 🧪 Validation & CI/CD

### 1. Conceptual Workflow YAML

~~~yaml
name: "Schema Lint (Governed)"

on:
  pull_request:
    paths:
      - "schemas/**"
      - "configs/**"
      - "docs/**"
  push:
    branches: ["main", "release/**"]
    paths:
      - "schemas/**"
      - "configs/**"
      - "docs/**"
  workflow_dispatch: {}

permissions:
  contents: read

concurrency:
  group: schema-lint-${{ github.ref }}
  cancel-in-progress: true

jobs:
  schema-lint:
    runs-on: ubuntu-22.04
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install validators
        run: |
          pip install -r requirements.txt
          pip install jsonschema ruff
          pip install pyshacl rdflib

      - name: Validate JSON Schemas
        run: |
          mkdir -p reports/self-validation/schemas
          python tools/schemas/validate_json_schemas.py \
            --schemas schemas/json \
            --out reports/self-validation/schemas/schema_validation.json

      - name: Validate example payloads & configs
        run: |
          python tools/schemas/validate_payloads.py \
            --schemas schemas/json \
            --examples schemas/examples \
            --configs configs \
            --out reports/self-validation/schemas/payload_validation.json

      - name: Validate SHACL shapes
        run: |
          python tools/schemas/validate_shacl.py \
            --shapes schemas/shacl \
            --out reports/self-validation/schemas/shacl_validation.json

      - name: Summarize results
        run: |
          node tools/schemas/summarize_schema_lint.mjs \
            --inputs "reports/self-validation/schemas/*.json" \
            --markdown "reports/self-validation/schemas/summary.md" \
            --json "reports/self-validation/schemas/lint_summary.json"

      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: schema_lint_reports
          path: reports/self-validation/schemas/

      - name: Emit telemetry
        run: |
          python scripts/emit_telemetry.py \
            --kind schema_lint \
            --summary reports/self-validation/schemas/lint_summary.json \
            --out schema_lint_telemetry.json

      - name: Append telemetry to unified log
        run: |
          python scripts/merge_telemetry.py \
            --in  schema_lint_telemetry.json \
            --dest releases/v11.2.4/schema-lint-telemetry.json
~~~

### 2. Quality Gates

The job **must fail** if:

- Any JSON Schema is invalid or references missing definitions.  
- Any example or config fails validation against its declared schema.  
- Any SHACL shape fails or produces critical constraint violations.  
- Summary reports cannot be generated.

Schema changes that are **breaking** should be:

- Clearly flagged in the summary,  
- Linked to migration guidance where available.

---

## 📦 Data & Metadata

### 1. Inputs

- `schemas/json/**` — JSON Schemas (telemetry, docs, Story Nodes, pipelines, etc.).  
- `schemas/shacl/**` — SHACL shapes for RDF / graph structures.  
- `schemas/examples/**` — Known-good examples for regression.  
- `configs/**` — Pipeline configs and other structured files that must match schemas.

### 2. Outputs & Artifacts

| Artifact Path                                                | Purpose                                      |
|--------------------------------------------------------------|----------------------------------------------|
| `reports/self-validation/schemas/schema_validation.json`     | JSON Schema validation results               |
| `reports/self-validation/schemas/payload_validation.json`    | Example/config validation results            |
| `reports/self-validation/schemas/shacl_validation.json`      | SHACL constraint outcomes                    |
| `reports/self-validation/schemas/lint_summary.json`          | Canonical machine-readable summary           |
| `reports/self-validation/schemas/summary.md`                 | Human-readable PR summary                    |

Telemetry is appended to:

- `releases/v11.2.4/schema-lint-telemetry.json`

with metrics such as schemas_checked, failures, runtime, energy, and carbon.

---

## 🌐 STAC, DCAT & PROV Alignment

### 1. DCAT

Schema validation outputs may be represented as a DCAT Dataset:

- `dct:title`: "KFM Schema Validation Reports".  
- `dct:description`: "Automated JSON/SHACL schema validation summaries for KFM."  
- `dct:identifier`: stable dataset ID, with per-run entries.  

Distributions:

- `lint_summary.json` (`application/json`).  
- `summary.md` (`text/markdown`).  
- Optional compressed bundles of raw validation outputs.

### 2. STAC

If CI outputs are cataloged alongside other datasets:

- STAC Collection: `kfm-schema-lint`.  
- Items:
  - `id`: `schema-lint-<run_id>`.  
  - `properties.datetime`: run completion time.  
  - `assets`:
    - `summary-json` → `lint_summary.json`  
    - `summary-md` → `summary.md`

Non-spatial governance data can use `geometry: null`.

### 3. PROV-O

For each run:

- **Entity**: `ex:SchemaLintReport_<run_id>` (lint summary + detailed JSON).  
- **Activity**: `ex:SchemaLintRun_<run_id>`.  
- **Agent**: `ex:KFM_CI_Bot` (`prov:SoftwareAgent`).

Key relations:

- `ex:SchemaLintRun_<run_id> prov:used` → schema sources at specific commit.  
- `ex:SchemaLintReport_<run_id> prov:wasGeneratedBy ex:SchemaLintRun_<run_id>`.  
- `ex:SchemaLintRun_<run_id> prov:wasAssociatedWith ex:KFM_CI_Bot`.

---

## 🧱 Architecture

### 1. Module Boundaries

- **Workflow**: `.github/workflows/schema-lint.yml`  
- **Validators**: `tools/schemas/*.py` and `*.mjs`  
- **Schemas**: `schemas/json/`, `schemas/shacl/`, `schemas/examples/`  
- **Reports**: `reports/self-validation/schemas/`  
- **Telemetry**: `releases/v11.2.4/schema-lint-telemetry.json`

The workflow:

- Keeps logic in reusable scripts (not inlined in YAML).  
- Uses configuration in `schemas/` and `configs/` for deterministic behavior.

### 2. Determinism & Reproducibility

- All validation rules are schema-driven; no hidden heuristics.  
- For a given commit:
  - Same schemas + same configs → identical validation results.  
- Tooling versions (Python, jsonschema, pyshacl, Node) should be pinned in `requirements.txt` and lockfiles.

---

## ⚖ FAIR+CARE & Governance

### 1. FAIR

| Principle        | Implementation                                               |
|-----------------:|--------------------------------------------------------------|
| **Findable**     | Schemas and reports in predictable paths; catalog entries   |
| **Accessible**   | Public schemas with clear licenses                          |
| **Interoperable**| JSON Schema, SHACL, STAC/DCAT, PROV, and KFM profiles       |
| **Reusable**     | Versioned schemas, examples, and validation histories       |

### 2. CARE

While schemas are typically non-sensitive, they encode:

- Governance constraints,  
- Data handling expectations,  
- Sovereignty-aware fields (e.g., `care_tag`, `indigenous_rights_flag`).

Schema-lint ensures those constraints remain:

- Present,  
- Well-typed,  
- Not accidentally removed in refactors.

### 3. Governance Hooks

- Breaking changes may require:
  - Governance review,  
  - Migration notes or scripts,  
  - Updates to dependent pipelines and docs.  

Schema-lint and its telemetry form part of the **governance evidence** used by councils and working groups.

---

## 🕰️ Version History

| Version    | Date       | Author          | Summary                                                                                                                        |
|-----------:|------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **v11.2.4** | 2025-12-06 | `@kfm-arch`     | Aligned with KFM-MDP v11.2.4; expanded front-matter; added STAC/DCAT/PROV alignment, Story Node hooks, telemetry wiring, and CI integration details. |
| v10.2.4   | 2025-11-12 | `@kfm-arch`     | Introduced telemetry v3 schema for schema-lint; unified artifact paths; improved summary aggregation.                          |
| v10.1.0   | 2025-11-10 | `@kfm-arch`     | Added SHACL validation step; expanded coverage to configs and examples.                                                       |
| v9.9.0    | 2025-11-08 | `@kfm-arch`     | Initial governed schema-lint workflow documentation.                                                                          |

---

<div align="center">

🧩 **Kansas Frontier Matrix — Schema Validation Workflow (`schema-lint.yml`)**  
Semantic Contracts · FAIR+CARE Governance · Sustainable CI/CD  

[⬅ Back to Workflows Index](./README.md) ·  
[📘 Docs Root](../README.md) ·  
[⚖ Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>

