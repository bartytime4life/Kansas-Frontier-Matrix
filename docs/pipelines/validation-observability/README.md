---
title: "🛰️ Kansas Frontier Matrix — Data Validation & Observability Framework (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/validation-observability/README.md"
version: "v11.0.0"
last_updated: "2025-11-18"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/validation-observability-v1.json"
governance_ref: "../../standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "etl-validation"
fair_category: "F1-A2-I1"
care_label: "CARE-Data-Quality"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Data Quality & Observability"
redaction_required: false
provenance_chain:
  - "docs/pipelines/validation-observability/README.md@v10.4.x"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../../schemas/json/validation-observability-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/validation-observability-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:pipelines:validation-observability-v11.0.0"
semantic_document_id: "kfm-doc-pipelines-validation-observability"
event_source_id: "ledger:docs/pipelines/validation-observability/README.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified historical claims"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon new protocol release"
---

<div align="center">

# 🛰️ **Kansas Frontier Matrix — Data Validation & Observability Framework**

`docs/pipelines/validation-observability/README.md`

**Purpose**  
Define the **complete KFM v11 validation–observability–lineage framework** used to ensure every dataset is trustworthy, reproducible, FAIR+CARE aligned, and safely promotable through **ETL → AI → Knowledge Graph → STAC → Story Nodes → Focus Mode**.

</div>

--- ✦ ---

## 1. Overview

KFM uses a **multi-layer validation stack** paired with **full observability and lineage instrumentation**:

1. **Frictionless** — ingest-level schema contracts  
2. **pandera** — transform-level DataFrame schemas  
3. **Great Expectations (GE)** — publish-level expectation suites + Data Docs  
4. **Observability** — cron/run health & job duration (e.g., Sentry Cron, metrics)  
5. **Lineage** — OpenLineage events + Marquez (or equivalent) UI  
6. **Provenance** — validation & telemetry outputs linked into STAC, PROV-O, Story Nodes, and Focus Mode narratives  

Every pipeline must pass all required layers before promotion to any **blue/green** release.

---

## 2. Directory Layout

~~~text
src/pipelines/
├── _validation/
│   ├── contracts/              # Frictionless tabular-level schemas
│   ├── schemas/                # pandera schemas for DF transforms
│   ├── expectations/           # Great Expectations suites + checkpoints
│   ├── docs/                   # GE Data Docs build artifacts
│   └── reports/                # JSON outputs from all validators
├── ingest/
├── transform/
├── publish/
└── monitoring/
    ├── lineage/                # OpenLineage emitters
    └── cron/                   # Cron monitoring wrappers (e.g., Sentry, Prometheus jobs)
~~~

Provenance/telemetry layout:

~~~text
provenance/
  validation/
    frictionless/
    pandera/
    great_expectations/
  lineage/
  telemetry/
~~~

---

## 3. Layer 1 — Frictionless Ingest Contracts

**Purpose:** Validate **external incoming data** at the system boundary.

- All STAC sources, CSVs, Parquets, shapefiles, and remote-sensing derivatives must include a **`datapackage.yaml`** contract.  
- Pipelines run `frictionless validate datapackage.yaml` before loading anything.  
- Validation produces a **machine-readable JSON report** stored at:

~~~text
provenance/validation/frictionless/<run_id>.json
~~~

**Failure behavior:** Hard block ingest. Nothing flows into `data/raw/**` or staging if Frictionless fails.

**STAC Integration:**

~~~json
{ "rel": "validation", "href": "./provenance/validation/frictionless/<run_id>.json" }
~~~

---

## 4. Layer 2 — pandera Transform Schemas

**Purpose:** Guarantee types, constraints, geographic boundaries, and temporal correctness **within transformations**.

- Supported backends: **pandas, Dask, Polars**  
- Schemas live in: `src/pipelines/_validation/schemas/`  

Required checks (domain-dependent):

- Type coercion & non-null constraints  
- Unique IDs / natural keys  
- Bounding boxes within Kansas (and subregions, if defined in contracts)  
- Temporal validity and ordering (no impossible or overlapping intervals)  

Example (simplified):

~~~python
import pandera as pa
from pandera import typing as pat

class ClimateStations(pa.SchemaModel):
    station_id: pat.Series[int] = pa.Field(unique=True)
    lat: pat.Series[float] = pa.Field(ge=36.5, le=40.5)
    lon: pat.Series[float] = pa.Field(ge=-102.1, le=-94.6)
    date: pat.Series[pa.DateTime] = pa.Field(nullable=False)
~~~

**Failure behavior:** Transform aborts; error details are serialized to:

~~~text
provenance/validation/pandera/<run_id>.json
~~~

---

## 5. Layer 3 — Great Expectations (GE) Publish Gate

**Purpose:** Validate **post-transform outputs** before loading into:

- Neo4j knowledge graph  
- STAC datasets & DCAT catalogs  
- Story Node assets  
- AI training/evaluation corpora  

**Artifacts:**

- Expectation Suites: `src/pipelines/_validation/expectations/*.json`  
- Checkpoints: `src/pipelines/_validation/expectations/checkpoints/*.yml`  
- Data Docs: built under `src/pipelines/_validation/docs/` and uploaded as CI artifacts  

Example checkpoint run:

~~~text
ge checkpoint run --name kfm_pre_publish --runtime_variables batch_id=<sha>
~~~

**Failure behavior:** CI hard block. Promotion to any **blue/green** tier is denied.

---

## 6. Observability Layer

### 6.1 Cron / Job Monitoring

Every scheduled pipeline job MUST register:

- `status = in_progress` at start  
- `status = ok` on success  
- `status = error` on failure  
- `duration` (required for energy/carbon telemetry)  

Cron wrappers under:

~~~text
src/pipelines/monitoring/cron/<job>.py
~~~

may update Sentry, Prometheus, or custom metrics sinks.

### 6.2 Metrics Captured

Core metrics:

- Run frequency and on-time execution  
- Missed or delayed runs  
- Runtime distribution & anomalies  
- Error signatures (stack traces, categorized causes)  
- Energy usage & carbon estimates (ISO 50001 / 14064-aligned)  

These metrics flow into telemetry as specified in `telemetry_schema`.

---

## 7. Lineage Layer — OpenLineage & UI

All pipelines emit **OpenLineage events** containing:

- Job name  
- `run_id`  
- Input dataset URIs (STAC assets, tables, etc.)  
- Output dataset URIs  
- Schema fingerprints / hashes  
- `commit_sha` and pipeline version  

A lineage UI (Marquez or equivalent) MUST support:

- Full **graph of lineage** across datasets, runs, models, and Story Nodes  
- Dataset impact analysis (for changes & rollbacks)  
- Run-level metadata (durations, parameters, environment)  
- Governance/audit views for FAIR+CARE reviews  

**STAC Integration:**

~~~json
{ "rel": "lineage", "href": "./provenance/lineage/<run_id>.json" }
~~~

---

## 8. Provenance Integration (FAIR+CARE)

All validation + observability outputs MUST be stored under a common provenance tree:

~~~text
provenance/
  validation/
    frictionless/
    pandera/
    great_expectations/
  lineage/
  telemetry/
~~~

**PROV-O modeling:**

- `prov:Activity` → pipeline job / run  
- `prov:Entity` → datasets, artifacts, models  
- `prov:Agent` → pipeline owners / automation agents  
- `prov:wasGeneratedBy` → `run_id`  
- `prov:qualifiedUsage` → validation reports, telemetry references  

Story Nodes and Focus Mode v3 reference validation + telemetry evidence to support **narrative transparency**, e.g.:

> “This overlay uses data that passed Frictionless + pandera + GE validation on 2025-11-18, with telemetry-confirmed runtime behavior and documented lineage.”

---

## 9. CI / CD Enforcement

CI MUST:

1. Run **Frictionless** validation on ingest data changed in a PR.  
2. Run **pandera** checks on modified transformations.  
3. Run **GE Checkpoints** on any publish-ready data.  
4. Upload artifacts: validation reports (JSON) + GE Data Docs.  
5. Block merge on ANY validation failure.

On release:

- All validation artifacts are included or referenced in the **release manifest**:
  - `manifest.zip`  
  - STAC/DCAT metadata with `rel: "validation"` and `rel: "lineage"` links  
- Telemetry summaries (including energy/carbon) are referenced via `telemetry_ref` and `telemetry_schema`.

---

## 10. Minimal Code Examples (Pseudocode)

### 10.1 pandera Schema

~~~python
class ClimateStations(pa.SchemaModel):
    station_id: pat.Series[int] = pa.Field(unique=True)
    lat: pat.Series[float] = pa.Field(ge=36.5, le=40.5)
    lon: pat.Series[float] = pa.Field(ge=-102.1, le=-94.6)
    date: pat.Series[pa.DateTime]
~~~

### 10.2 Great Expectations Checkpoint Run

~~~text
ge checkpoint run --name kfm_pre_publish --runtime_variables batch_id=<sha>
~~~

### 10.3 Frictionless Validation

~~~text
frictionless validate datapackage.yaml --json > reports/frictionless_<run_id>.json
~~~

### 10.4 OpenLineage Event (Conceptual)

~~~text
emit_event(
  job="ingest-noaa",
  run_id=new_run_id(),
  inputs=[...],
  outputs=[...],
  commit_sha="<commit>",
  pipeline_version="v11.0.0"
)
~~~

---

## 11. Required Pipeline Wiring

Every production pipeline MUST wire:

- `validate_ingest()` → Frictionless contracts  
- `validate_transform()` → pandera schemas  
- `validate_publish()` → GE checkpoint  
- `record_lineage()` → OpenLineage + PROV-O events  
- `record_telemetry()` → runtime + energy/carbon metrics  
- `write_provenance()` → validation + telemetry reports under `provenance/**`  

No dataset or model is allowed to bypass these gates on its path into a public or blue/green release.

---

## 12. Governance Compliance

This framework implements and makes enforceable:

- **MCP-DL v6.3** — pipeline behavior & validation are fully documented.  
- **FAIR** — validation outputs are stored with well-structured metadata and resolvable references.  
- **CARE** —  
  - Collective Benefit: higher-quality data reduces downstream harm.  
  - Authority to Control: Indigenous-partnered rules for sensitive gates & datasets.  
  - Responsibility: explicit monitoring & remediation when gates fail.  
  - Ethics: transparent, auditable, non-extractive data usage.  
- **Diamond⁹ Ω / Crown∞Ω certification** — reliability, transparency, and sustainability of validation operations.  

---

## 13. Versioning & Backwards Compatibility

All validation schemas/configs (Frictionless, pandera, GE) MUST specify:

- `schema_version`  
- `last_modified`  
- `breaking_change = true|false`  

Before applying updates:

- Run compatibility checks on representative historical data.  
- For breaking changes:
  - Update governance notes.  
  - Update STAC/DCAT metadata where required.  
  - Document impact in release notes.

---

## 14. Future Extensions (v11.3+ Roadmap)

Planned enhancements:

- ML-specific validation:
  - SHAP drift detection  
  - Embedding stability metrics  
- Temporal anomaly detection on ETL durations & resource usage  
- Focus Mode v3 narratives with **inline validation evidence** and **telemetry overlays**  
- AI assistants that propose contract/expectation updates from repeated failure patterns  

---

## 🕰️ Version History

| Version | Date       | Author                               | Summary                                                                                     |
|--------:|------------|----------------------------------------|---------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-18 | FAIR+CARE Council · Architecture WG   | Upgraded Data Validation & Observability Framework to KFM-MDP v11; added FAIR+CARE, OpenLineage, telemetry v1 alignment, and provenance integration. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Data Validation & Observability Framework v11 · FAIR+CARE Certified · Sovereignty-Aware  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified · MCP-DL v6.3  

[Back to Pipelines Documentation](../README.md)

</div>
