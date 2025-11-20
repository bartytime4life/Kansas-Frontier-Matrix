---
title: "📐 Kansas Frontier Matrix — Validation & Observability Schemas Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/schemas/README.md"
version: "v11.0.0"
last_updated: "2025-11-20"

review_cycle: "Annual / FAIR+CARE Council & Reliability Board"
commit_sha: "<latest-commit-hash>"

sbom_ref: "../../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/pipelines-validation-observability-schemas-v11.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"

status: "Active / Enforced"
doc_kind: "PipelineSchemaGuide"
intent: "validation-observability-schemas-overview"
role: "pipelines-schema-governance"

fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM Reliability Board"
risk_category: "ETL / Validation / Observability"
redaction_required: false

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "Instant"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../../schemas/json/pipelines-validation-observability-schemas-v11.schema.json"
shape_schema_ref: "../../../../schemas/shacl/pipelines-validation-observability-schemas-v11-shape.ttl"

doc_uuid: "urn:kfm:doc:pipelines:validation-observability-schemas:v11"
semantic_document_id: "kfm-validation-observability-schemas"
event_source_id: "ledger:docs/pipelines/validation-observability/schemas/README.md"
immutability_status: "version-pinned"
doc_integrity_checksum: "<sha256>"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified operational claims"
  - "modifying schema logic"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon next major schema evolution"
---

<div align="center">

# 📐 **Kansas Frontier Matrix — Validation & Observability Schemas Guide**  
`docs/pipelines/validation-observability/schemas/README.md`

**Status:** Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

**Purpose**  
Define and document the **full set of schemas** used to validate KFM’s **validation & observability pipelines**.  
These schemas govern structural validation, semantic rules, FAIR+CARE checks, telemetry formats, and lineage metadata for all pipeline executions.

[![Pipelines](https://img.shields.io/badge/Pipelines-MCP--DL_v6.3-blue)]()  
[![KFM-MDP v11](https://img.shields.io/badge/Markdown-KFM--MDP_v11.0.0-purple)]()  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)]()  
[![Stable](https://img.shields.io/badge/Schema%20Suite-Stable-success.svg)]()

</div>

---

## 📘 Overview

The validation & observability subsystem relies on a **family of schemas** to guarantee:

- Structural correctness of data and telemetry  
- Semantic alignment with ontologies (CIDOC-CRM, OWL-Time, GeoSPARQL, PROV-O)  
- FAIR+CARE-compliant metadata  
- Safe, consistent AI validation behavior  
- Reproducible lineage and telemetry bundles

This guide explains:

- How schemas are organized  
- What each schema class covers  
- How schemas are used inside pipelines  
- How versioning and backwards-compatibility are enforced  
- How to test and extend the schema set safely

---

## 🗂 Directory Layout

```text
docs/pipelines/validation-observability/schemas/
│
├── README.md
│
├── json/
│   ├── telemetry-schema.json
│   ├── validation-run-schema.json
│   ├── dataset-validation-report-schema.json
│   └── ai-validation-result-schema.json
│
├── shacl/
│   ├── graph-validation-shapes.ttl
│   ├── provenance-shapes.ttl
│   └── fair-care-shapes.ttl
│
├── stac-dcat/
│   ├── validation-stac-item-schema.json
│   └── validation-dcat-dataset-schema.json
│
└── examples/
    ├── telemetry/
    ├── validation-reports/
    └── graph-snippets/
```

> The actual file names may evolve; this layout shows the **expected structure and intent** of each folder.

---

## 🧱 Schema Classes

KFM groups schemas for validation & observability into four broad classes:

1. **Structural JSON Schemas** — cover shapes of JSON payloads (telemetry, reports, configs)  
2. **SHACL Graph Shapes** — enforce RDF/graph-level constraints in Neo4j and linked data views  
3. **STAC/DCAT Bridge Schemas** — ensure validation-related datasets expose proper catalog metadata  
4. **Example/Fixture Schemas** — optional additional schemas used to validate test fixtures

Each class participates in **multiple validation gates** across pipelines.

---

## 📦 Structural JSON Schemas (json/)

These are used by **pipeline code** and **tests** to validate payloads.

### 🛰 `telemetry-schema.json`

Defines:

- Shape of telemetry bundles emitted by pipelines  
- Required fields:
  - `pipeline_id`, `run_id`, `dataset_id`  
  - `start_time`, `end_time` (ISO 8601)  
  - `status` (e.g., `success`, `failure`, `partial`)  
  - Summary metrics (rows processed, failures, warnings)  
- Optional fields:
  - Energy/carbon metrics  
  - AI token usage for enriched stages  

Used to ensure **all telemetry files conform to a standard** before being accepted into `releases/*/focus-telemetry.json`.

---

### 🧪 `validation-run-schema.json`

Defines:

- Structure of **per-run validation output**  
- Required sections:
  - `structural_validation`  
  - `semantic_validation`  
  - `fair_care_validation`  
  - `ai_validation` (if applicable)  
- Each section includes:
  - `status`, `issues`, `warnings`, `metrics`  

Pipelines MUST conform to this schema before a run is considered valid and promotable.

---

### 📊 `dataset-validation-report-schema.json`

Defines:

- Aggregated validation report for a dataset version  
- Links multiple `validation_run` outputs into a single document  
- Includes:
  - Dataset identifiers  
  - Version and checksum  
  - Summary of all validation gates  
  - FAIR+CARE summary  
  - Overall `can_promote` flag  

Used by governance and release processes.

---

### 🤖 `ai-validation-result-schema.json`

Defines:

- AI validation result payloads  
- Fields:
  - `model_id`, `model_version`  
  - `input_reference` (e.g., dataset or document ID)  
  - `findings` with evidence & confidence  
  - `guardrail_triggers` (if any)  

Ensures **AI-based checks** remain structured, explainable, and auditable.

---

## 🧬 SHACL Graph Shapes (shacl/)

SHACL shapes are used to validate **graph-level constraints**.

### 🧱 `graph-validation-shapes.ttl`

Covers:

- Node shape patterns for core graph entities used in validation pipelines:
  - Validation runs, datasets, telemetry nodes  
- Ensures:
  - Required relationships (e.g., validation run → dataset)  
  - Expected node types and properties  

Executed via SHACL-compatible tools against Neo4j or exported RDF snapshots.

---

### 🧬 `provenance-shapes.ttl`

Covers:

- PROV-O-compliant modeling of:
  - `prov:Entity` (datasets, reports, telemetry)  
  - `prov:Activity` (validation/observability runs)  
  - `prov:Agent` (systems, operators, automated agents)  
- Ensures:
  - Every dataset has at least one `prov:wasGeneratedBy`  
  - Every activity references input entities and output entities  

Supports trustworthy **lineage and reproducibility**.

---

### 🌐 `fair-care-shapes.ttl`

Covers:

- Graph-level enforcement of FAIR+CARE labels:
  - `care_label`, `access_level`, `sovereignty` references  
- Ensures:
  - Required governance properties exist on sensitive datasets  
  - No conflicting labels (e.g., `Public` combined with `Sensitive` without justification)  

Used by governance dashboards and FAIR+CARE validation pipelines.

---

## 🗺 STAC/DCAT Bridge Schemas (stac-dcat/)

These schemas ensure validation-related datasets are **properly cataloged**.

### 📦 `validation-stac-item-schema.json`

Applied to STAC Items representing:

- Validation reports  
- Telemetry COG/JSON outputs  
- Graph snapshots for audits

Ensures:

- Proper `properties.kfm:*` fields  
- Spatial/temporal extent (if relevant)  
- Links back to the dataset and run IDs  

---

### 📚 `validation-dcat-dataset-schema.json`

Defines a DCAT Dataset profile for **validation & observability** bundles:

- Required DCAT fields:
  - `dct:title`, `dct:description`, `dct:creator`, `dct:license`  
  - `dct:temporal`, `dct:issued`, `dct:modified`  
- `dcat:distribution` entries referencing STAC assets or JSON reports  
- Governance fields:
  - CARE/FAIR tags  
  - Data steward  
  - Classification  

Ensures catalogs **represent validation outputs cleanly and consistently**.

---

## 🧪 Usage in Pipelines

Schemas are used at multiple points:

1. **During pipeline execution**  
   - Validation & observability code imports JSON Schemas to check payloads in-process.  

2. **At validation gates**  
   - STAC/DCAT outputs are checked before being written to `data/processed/` and `releases/`.  

3. **In CI/CD workflows**  
   - Dedicated jobs run schema validators on:
     - `examples/`  
     - Test fixtures  
     - New/changed schemas  

4. **In governance tools**  
   - SHACL shapes are used to validate the graph after major updates.  

If any schema check fails, **dataset promotion is blocked**.

---

## 🔁 Versioning & Backwards Compatibility

Schema versioning principles:

- Increment the `version` field in this README and schema files for meaningful changes.  
- Use **SemVer** style for schema versions (e.g., `1.0.0 → 1.1.0 → 2.0.0`).  
- Major version changes indicate **breaking changes**:
  - Required field removals  
  - Type changes  
  - Cardinality changes  

When possible:

- Provide **migration guidance** from previous schema versions.  
- Maintain compatibility with older validation reports where feasible.  

Any breaking schema change must be:

- Documented in this README under Version History  
- Linked to a governance decision or design doc  

---

## 🧪 Testing & Validation of Schemas

Schemas themselves are subject to:

- **Linting** (JSON/YAML syntax, SHACL syntax)  
- **Schema self-tests** using `examples/` and `fixtures/`  
- **Integration tests** via:
  - `docs/pipelines/validation-observability/tests/`  
  - `src/pipelines/validation/` test modules  

Typical workflow for updating a schema:

1. Update schema file  
2. Add or adjust examples under `examples/`  
3. Update spec docs in `docs/pipelines/validation-observability/tests/specs/`  
4. Run:
   ```bash
   make test-pipelines-validation
   ```  
5. Submit PR with clear description and link to governance decision (if applicable)

---

## 🧭 Extending the Schema Set

When adding a new schema:

1. Decide whether it is:
   - Structural JSON  
   - SHACL graph shape  
   - STAC/DCAT profile  
   - Telemetry or AI-specific  

2. Place it in the appropriate subdirectory.  

3. Add a **brief description** to this README under the relevant section.  

4. Provide:
   - At least one valid example in `examples/`  
   - At least one negative case fixture (if applicable)  

5. Update any dependent documentation or code that uses the schema.

---

## 🕰 Version History

| Version | Date       | Author      | Notes                                                                 |
|--------:|-----------:|------------|-----------------------------------------------------------------------|
| v11.0.0 | 2025-11-20 | KFM Docs AI | Initial v11 schemas guide; covers structural, SHACL, and STAC/DCAT.  |

---

<div align="center">

**Kansas Frontier Matrix — Validation & Observability Schemas v11**  
© 2025 Kansas Frontier Matrix — CC-BY 4.0  

[Back to Validation & Observability](../README.md) ·  
[Back to Pipelines Overview](../../README.md) ·  
[Back to Docs Hub](../../../README.md)

</div>