---
title: "🤖 KFM v11 — AI Pipeline Core (Airflow · GE · lakeFS · OpenLineage · OpenTelemetry)"
path: "docs/pipelines/ai/core/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
backward_compatibility: "Guaranteed for v10.x → v11.x pipeline model"
content_stability: "stable"
status: "Active / Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
attestation_ref: "../../../releases/v11.2.3/slsa-attestation.json"
signature_ref: "../../../releases/v11.2.3/signature.sig"

telemetry_ref: "../../../releases/v11.2.3/ai-pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/ai-pipeline-core-v11.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

doc_kind: "Pipeline Group"
intent: "ai-pipeline-core"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-A/General"

classification: "Public (Governed)"
sensitivity: "Low/Moderate"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🤖 **KFM v11 — AI Pipeline Core**  
### Airflow · Great Expectations · lakeFS · OpenLineage · OpenTelemetry  
`docs/pipelines/ai/core/README.md`

**Purpose**  
Define the unified, deterministic, metadata-rich foundation for all KFM AI pipelines.  
Ensure reproducible **ingestion → validation → lineage → versioning → promotion → inference**,  
with full FAIR+CARE and governance alignment.

</div>

---

## 1️⃣ Overview

The **AI Pipeline Core** is the central framework powering all KFM data-to-AI automation.  
It establishes:

- Deterministic ingestion orchestrated with **Airflow**  
- Dynamic schema & data quality checks using **Great Expectations (GE)**  
- Immutable versioning and promotion via **lakeFS**  
- Automatic lineage capture through **OpenLineage**  
- Quantitative operational telemetry via **OpenTelemetry (OTel)**  
- FAIR+CARE-aligned provenance + energy/carbon measurement  
- Standards-based cross-pipeline interoperability (v11.x AI pipeline contract)  

This directory collects all pipeline-level logic used by any KFM domain:

- **Climate**, **air quality**, **hydrology**, **soils**, **archaeology**, **remote sensing**, **ecology**, etc.

---

## 2️⃣ Architecture Summary

### 🔹 Core Lifecycle

1. **Ingest**  
   Airflow operators pull data, apply transforms, normalize timestamps, and extract metadata.

2. **Validate**  
   GE Checkpoints enforce schema, null conditions, ranges, and domain rules.

3. **Version**  
   Data is written to lakeFS (`lakefs://kfm-dev/...`), branched, committed, and promoted.

4. **Lineage**  
   Every DAG task emits OpenLineage events linked to GE, lakeFS, and ETL steps.

5. **Telemetry**  
   All stages export OTel metrics + provenance + energy + carbon signals.

6. **Promotion Gates**  
   Promotion from dev → stage → prod requires:
   - GE success  
   - Lineage completeness  
   - lakeFS commit integrity  
   - OTel health  
   - FAIR+CARE checks  

---

## 3️⃣ Airflow Integration (v11 Model)

All AI DAGs MUST implement:

- Idempotent tasks  
- Deterministic parameters  
- No mutable global state  
- Retries with bounded exponential backoff  
- WAL-anchored checkpoints for all mutations  

**OpenLineage Provider**:

- Hooks automatically into Airflow operators  
- Emits lineage without invasive code changes  
- Tracks all upstream/downstream dataset interactions  

Promotion signals are attached to DAG run metadata:

- `promotion_candidate=true`  
- `ge_checkpoint=<name>`  
- `lakefs_commit_id=<sha>`  
- `otel_trace_id=<id>`  

---

## 4️⃣ Great Expectations Integration

### Requirements

Each pipeline MUST define at least one **GE Checkpoint** that includes:

- Schema expectations  
- Nullity rules  
- Range/domain constraints  
- Temporal consistency checks  
- Optional FAIR+CARE-risk triggers  

GE results feed into:

- GE artifacts directory (non-committed outputs)  
- OpenLineage event metadata  
- lakeFS commit notes  
- Telemetry export stream  

**Validation failure ⇒ automatic rollback / promotion block** under the Reliability framework.

---

## 5️⃣ lakeFS Versioning & Promotion

### Branch Structure

- `kfm-dev` → ephemeral updates, experiments  
- `kfm-stage` → validated artifacts  
- `kfm-prod` → public, guaranteed-safe outputs  

### Promotion Policy

Promotion requires:

- GE success for defined checkpoints  
- OTel metrics above baseline quality thresholds  
- SLO conformance (from Reliability Pipelines)  
- Complete lineage graph (OpenLineage + PROV-O)  
- Harmonized metadata (STAC/DCAT/Story Nodes ready)  

lakeFS commits MUST include metadata such as:

~~~yaml
metadata:
  kfm_version: v11.2.3
  data_domain: <domain>
  ge_checkpoint: <checkpoint>
  lineage_run_id: <run-id>
  otel_trace: <id>
  energy_kwh: <value>
  carbon_gco2: <value>
~~~

---

## 6️⃣ OpenLineage Integration

Lineage captures:

- Dataset inputs/outputs for each task  
- Operators and logical operations  
- GE validation events  
- Versioned lakeFS assets  
- Telemetry correlations (via shared IDs)  
- FAIR+CARE provenance tags (via metadata)  

Lineage events are **mandatory** for:

- Promotion gates  
- Drift-aware auto-updates  
- Reliability scoring  
- Story Node generation  

---

## 7️⃣ OpenTelemetry Integration

### Metrics Collected

- Rows processed  
- Duration / latency per task  
- Resource usage (CPU, memory, I/O)  
- Errors/retries counts  
- Energy (kWh) & carbon (g CO₂-e)  
- GE validation stats  
- lakeFS commit metadata  
- Lineage completeness indicators  

### Export Requirements

- OTLP/gRPC exporters  
- Minimum 1-second resolution for long-running tasks  
- Export on each task boundary  
- Correlation to Airflow run ID and OpenLineage run ID  

---

## 8️⃣ Directory Layout (Emoji-Prefix)

~~~text
docs/pipelines/ai/core/
├── 📄 README.md                         # This file
├── 🌀 airflow/                          # DAG templates, hooks, shared operators
├── 🧪 expectations/                     # Great Expectations suites & checkpoints
├── 🧬 lineage/                          # OpenLineage schemas, templates, validators
├── 🌊 lakefs/                           # Branch & promotion config, commit policies
├── 📡 telemetry/                        # OTel exporters, resource definitions
├── 🛡 governance/                       # Pipeline-level FAIR+CARE / governance rules
└── 🧪 tests/                            # v11 test harness for determinism & metadata
~~~

---

## 9️⃣ Story Node (Focus Mode Integration)

**Summary Story**

The KFM AI Pipeline Core is the backbone of the computational ecosystem.  
It guarantees every AI dataset—soil, climate, hydrology, archaeology, atmosphere—follows a  
rigorous path:

> **Validation → Lineage → Versioning → Telemetry → Reproducibility → Governance**

**Narrative Hooks:**

- “Every dataset leaves a perfect trail of evidence.”  
- “Promotion happens only when the entire system agrees the data is safe.”  
- “Knowledge becomes traceable, measurable, and accountable.”

These narratives feed directly into **Story Nodes v3** and **Focus Mode v3**, tying technical guarantees  
to human-readable, audit-ready stories.

---

## 🔟 Version History

| Version | Date       | Notes                                                     |
|--------:|------------|-----------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Updated to KFM-MDP v11.2.2; safe-fence; emoji layout; telemetry + lineage alignment. |
| v11.2.2 | 2025-11-29 | Full v11 compliance; lineage/telemetry unification; core CI contract clarified.       |
| v11.1.0 | 2025-10-04 | OTel energy/carbon integration                             |
| v11.0.0 | 2025-08-17 | Initial v11 AI pipeline standardization                    |

---

<div align="center">

🤖 **Kansas Frontier Matrix — AI Pipeline Core (v11.2.3)**  
FAIR+CARE · Deterministic · Energy-Aware · Lineage-Guaranteed  

[📘 Docs Root](../../../..) · [🤖 AI Pipelines Index](../README.md) · [🛡 Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>
