---
title: "🛰️ Kansas Frontier Matrix — Lineage & Telemetry Integration Layer (OpenLineage × OpenTelemetry · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/instrumentation/README.md"
version: "v11.2.0"
last_updated: "2025-11-27"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.0/manifest.zip"
telemetry_ref: "../../../releases/v11.2.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/instrumentation-openlineage-otel-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active · Enforced"
doc_kind: "Integration Layer"
intent: "instrumentation-root"
category: "Lineage · Telemetry · Observability · Reliability"

fair_category: "F1-A1-I2-R1"
care_label: "Respectful · Minimization · Governance-Led"
sensitivity_level: "Low"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"

sensitivity: "General; lineage & telemetry content may reference protected datasets indirectly — CARE redaction required for linked spatial layers."
risk_category: "Medium Governance"
redaction_required: true

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "SoftwareApplication"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "src/pipelines/instrumentation/README.md@v11.1.0"
  - "instrumentation/openlineage-client@v10.4"
  - "instrumentation/otel-exporters@v10.3"
  - "Focus Mode v3 ID-correlation research"
provenance_requirements:
  versions_required: true
  must_reference_superseded: true
  newest_first: true
  must_reference_origin_root: false

json_schema_ref: "../../../schemas/json/instrumentation-v11.schema.json"
shape_schema_ref: "../../../schemas/shacl/instrumentation-v11-shape.ttl"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "diagram-extraction"
ai_transform_prohibited:
  - "speculative-additions"
  - "content-alteration"
  - "governance-override"
  - "narrative-fabrication"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_version_history: true
requires_directory_layout_section: true
requires_governance_links_in_footer: true

doc_uuid: "urn:kfm:doc:pipelines:instrumentation:v11.2.0"
semantic_document_id: "kfm-instrumentation-openlineage-otel"
event_source_id: "ledger:src/pipelines/instrumentation/README.md"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

classification: "Public Document"
jurisdiction: "Kansas / United States"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded by instrumentation-v12"
---

<div align="center">

# 🛰️ **Lineage & Telemetry Integration Layer**  
`src/pipelines/instrumentation/`

[![OpenLineage](https://img.shields.io/badge/OpenLineage-v1.20-purple)]()
[![OpenTelemetry](https://img.shields.io/badge/OTel-1.x-blue)]()
[![FAIR+CARE](https://img.shields.io/badge/Governance-FAIR%2BCARE-gold)]()
[![Reliability](https://img.shields.io/badge/Reliability-v11.2-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

**Purpose**  
Provide unified **OpenLineage** (spec-compliant dataset/job lineage) and **OpenTelemetry** (traces, metrics, logs) instrumentation for *all* KFM pipelines — LangGraph DAGs, hydrology ETL, archaeology workflows, Focus Mode tasks, and autonomous updaters.

</div>

---

## 📘 1. Scope

This directory implements the **instrumentation backbone** for KFM:

- End-to-end lineage with OpenLineage  
- Distributed tracing & metrics via OpenTelemetry  
- WAL-backed reliability for lineage+trace correlation  
- CARE-aware provenance for protected cultural/archaeological workflows  
- Focus Mode v3 integration (trace → run → narrative)

---

## 🗂️ 2. Directory Layout (v11.2 · Immediate + One Branch · Emojis + Descriptions)

```text
📁 src/pipelines/instrumentation/                  — Lineage + Telemetry integration root
│   📂 lineage/                                    — OpenLineage emitters + dataset/job facets
│   📂 telemetry/                                  — OpenTelemetry tracers, metrics & exporters
│   📂 decorators/                                 — Drop-in decorators for tracing + lineage
│   📂 correlation/                                — run_id ↔ trace_id ↔ focus_id mappers
│   📂 tests/                                      — Unit tests for reliability, lineage & OTel
│   📄 README.md                                   — This governed instrumentation README
```

---

## 🧬 3. Responsibilities (v11.2)

### 3.1 OpenLineage Emission
- `START` / `RUNNING` / `COMPLETE` / `FAIL` events  
- Dataset read/write facets mapped from STAC/DCAT metadata  
- WAL-backed buffering + retry semantics  
- Cross-domain lineage support:
  - LangGraph  
  - Hydrology pipelines  
  - Archaeology H3-protected datasets  
  - Focus Mode narrative sources  

### 3.2 OpenTelemetry (OTLP) Export
- Traces: pipeline → operator → function  
- Metrics: CPU, IO, latency, RAM, energy  
- Logs: structured OTLP logs  
- Collector-agnostic export via HTTP or gRPC  

### 3.3 Cross-System Harmonization
- Unified correlation of:
  - `run_id` (OpenLineage)  
  - `trace_id` (OpenTelemetry)  
  - `focus_id` (Focus Mode v3)  
- Enables:
  - Replay  
  - Root-cause analysis  
  - Narrative reconstruction  
  - Lineage → Story Node v3 linkage  

---

## 🚀 4. Integration Across KFM

### ETL Jobs
Each step (e.g., OCR → NER → Spatialization → Validation → Graph Load) emits:
- OpenLineage events  
- OTel spans + metrics  
- CARE metadata when applicable  

### LangGraph DAGs
Each node receives:
- `span_id`  
- `run_id`  
- dataset/job lineage facets  

### Archaeology Workflows
- CARE → H3 generalization events  
- Protected coordinate lineage  
- Cultural sensitivity labeling  

### Hydrology Pipelines
- Streamflow reconstruction lineage  
- Reservoir WID change tracking  
- Time-series provenance  

### Focus Mode Story Nodes
- Narrative context tied to real lineage + traces  
- Time anchors validated through OWL-Time constructs  

---

## ⚙️ 5. Configuration

### OpenLineage (env-driven)
- `OPENLINEAGE_URL`  
- `OPENLINEAGE_API_KEY`  
- `OPENLINEAGE_NAMESPACE`  
- `OPENLINEAGE_OFFLINE_MODE`

### OpenTelemetry (env-driven)
- `OTEL_EXPORTER_OTLP_ENDPOINT`  
- `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf|grpc`  
- `OTEL_SERVICE_NAME=kfm-pipeline`  
- `OTEL_METRIC_EXPORT_INTERVAL`  
- `OTEL_RESOURCE_ATTRIBUTES`  

> **No hard-coded values**.  
> All config is environment-controlled per KFM security standards.

---

## 🧪 6. Testing Requirements

All instrumentation modules MUST include:

- WAL reliability tests  
- Span count + structure tests  
- Dataset facet validation  
- End-to-end OTLP export (mock collector)  
- run_id ↔ trace_id correlation validation  
- CARE redaction compliance tests  

Tests run automatically under the v11.2 CI matrix.

---

## 🔗 7. Upstream Standards

This directory aligns with:

- **KFM-MDP v11.2.2**  
- **KFM-OP v11**  
- **KFM-STAC v11**  
- **KFM-Reliability v11**  
- **FAIR+CARE governance**  
- **OpenLineage Spec v1.20**  
- **OpenTelemetry 1.x**  

---

## 🕰️ 8. Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| **v11.2.0** | 2025-11-27 | Upgraded to full KFM-MDP v11.2.2; added badges, directory layout, metadata expansions, AI/Focus Mode ID correlation. |
| **v11.1.0** | 2025-11-26 | Unified lineage, traces, WAL-buffering, Focus Mode correlation. |
| **v11.0.0** | 2025-11-20 | Initial OpenLineage + OTLP integration merge. |

---

<div align="center">

**Kansas Frontier Matrix — Lineage & Telemetry Integration Layer**  
*FAIR+CARE Aligned · Open Standards · Diamond⁹ Ω / Crown∞Ω Certified*

[⬅ Back to Pipelines Index](../README.md) ·  
[🏗 Repository Architecture](../../../ARCHITECTURE.md) ·  
[🔐 Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[🛰 Telemetry Schema](../../../schemas/telemetry/instrumentation-openlineage-otel-v11.json)

</div>