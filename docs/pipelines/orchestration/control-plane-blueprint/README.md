---
title: "🧭 KFM v11.2.2 — Control-Plane Orchestration Blueprint (Airflow 3.x · OpenLineage · OTel · Diamond⁹ Ω / Crown∞Ω)"
path: "docs/pipelines/orchestration/control-plane-blueprint/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/orchestration-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/control-plane-blueprint-v11.2.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Blueprint"
header_profile: "standard"
footer_profile: "standard"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Operational (non-sensitive)"
public_exposure_risk: "Low"

scope:
  domain: "orchestration"
  applies_to:
    - "airflow"
    - "openlineage"
    - "otel"
    - "wal"
    - "promotion"
    - "deterministic-etl"

semantic_intent:
  - "orchestration-blueprint"
  - "deterministic-etl"
  - "idempotent-retries"
  - "reliability-patterns"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧭 **Control-Plane Orchestration Blueprint**  
### Airflow 3.x · OpenLineage · OpenTelemetry · Deterministic ETL Core  
`docs/pipelines/orchestration/control-plane-blueprint/README.md`

**Purpose**  
Define the official **v11.2.2 control-plane pattern set** for all KFM pipelines, establishing deterministic ETL, idempotent upserts, WAL-safe atomic publication, and unified telemetry + lineage across Airflow 3.x, OpenLineage, and OpenTelemetry.

</div>

---

## 📘 Overview

This blueprint provides:

- A **reference orchestration model** used by all KFM pipelines  
- Deterministic execution patterns for:
  - Branch-based promotion (lakeFS + Airflow)  
  - Strict idempotency using run-state & WAL  
  - Atomic publication & rollback  
- Unified observability and lineage via:
  - **OpenLineage** (dataset dependencies + run facets)  
  - **OpenTelemetry** (metrics, logs, traces)  
  - **PROV-O / STAC v11** metadata sidecars  

It is mandatory for any pipeline running in **production**, **release**, or **staging** control planes.

---

## 🎯 Scope

This directory defines:

- **Airflow 3.x orchestration blueprint** (DAGs, operators, hooks)  
- **Change-detection ingestion patterns** (HTTP, API variation, 304-awareness)  
- **Promotion pipeline pattern** (lakeFS branch-based workflows)  
- **Deterministic ETL**:
  - Run-state pattern  
  - Idempotent upserts  
  - WAL-enabled publication  
- **Observability stack**:
  - OTel traces (task/node-level)  
  - OTel metrics (worker + DAG)  
  - OpenLineage events  

It also provides a **KFM-approved seed** for implementing deterministic ingestion.

---

## 🗂️ Directory Layout

    docs/pipelines/orchestration/control-plane-blueprint/
    ├── 📄 README.md                                 # This file
    │
    ├── 📁 airflow/                                   # Airflow DAGs, operators, hooks
    │   ├── 📁 patterns/                              # Promotion, WAL, idempotency
    │   └── 📁 examples/                              # Deployable Airflow examples
    │
    ├── 📁 lineage/                                   # OpenLineage configs + extractors
    ├── 📁 telemetry/                                 # OTel exporters, resource schemas
    │
    ├── 📁 seeds/                                     # Minimal ingestion seeds (Python)
    │   └── 📄 http-change-detection.py               # Ready-to-run change-detection seed
    │
    └── 📁 tests/                                     # Integration, lint, canary tests
        └── 📄 test_blueprint_integrity.py

---

## 🚀 Reference Implementation — HTTP Change-Detection Seed

This seed enforces:

- `If-Modified-Since` protocol correctness  
- Rejects empty upstream responses  
- WAL write → atomic replace  
- Deterministic exit codes  
- Ready for Airflow, LangGraph, Cron, or standalone  

**KFM-v11.2.2 compliant:**

```python
# http-change-detection.py
import os, sys, requests, pandas as pd

u = os.getenv("SRC") or (sys.argv[1] if len(sys.argv) > 1 else None)
if not u:
    print("Usage: SRC=<url> python http-change-detection.py (or python http-change-detection.py <url>)")
    sys.exit(2)

os.makedirs(".state", exist_ok=True)
s = ".state/last_modified.txt"
ims = open(s).read().strip() if os.path.exists(s) else None
headers = {"If-Modified-Since": ims} if ims else {}

r = requests.get(u, headers=headers, timeout=30)
if r.status_code == 304:
    sys.exit(0)
r.raise_for_status()

last_mod = r.headers.get("Last-Modified", "")
df = pd.DataFrame(r.json())
assert not df.empty, "Upstream returned 0 rows"

os.makedirs(".wal", exist_ok=True)
tmp = ".wal/out.parquet"
dst = "out/data.parquet"
os.makedirs("out", exist_ok=True)

df.to_parquet(tmp)
os.replace(tmp, dst)

open(s, "w").write(last_mod)
print("ok")
```

---

## 🧩 Integration Notes

### Airflow 3.x (GA)
- Native OpenLineage provider  
- Deferrable operators for IO-bound tasks  
- DAG-level lineage + metadata injection  
- Scheduler performance improvements aligned with KFM ETL patterns  

### OpenLineage
- Automated extractors for:
  - requests  
  - Pandas I/O  
  - Parquet/GeoParquet  
- Outputs fully compatible with Marquez and custom lineage sinks  

### OpenTelemetry
- Trace every ingestion + transform step  
- Emit reliable task/node-level spans  
- Resource attributes aligned to KFM telemetry schema  
- Worker-level metrics for SLO dashboards  

---

## 🧱 KFM Control-Plane Guarantees

- **Deterministic transform ordering**  
- **Idempotent run-state enforcement**  
- **Atomic publication with WAL**  
- **lakeFS-safe promotion flow** (release/hotfix)  
- **Full provenance: STAC + PROV-O + DCAT**  
- **FAIR+CARE alignment**  
- **Testable + replayable** control plane  

---

## 🧵 Story Node & Focus Mode Hooks

This blueprint supports:

- Story Node generation after dataset publication  
- Focus Mode v3 contextualization:
  - dataset → run-state → lineage chain  
  - pipeline → narrative summary  

All ETL events can be surfaced as **narrative primitives** using OTel → Story Node transforms.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                      |
|----------|------------|------------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Updated to KFM-MDP v11.2.2; telemetry schemas; emoji tree |
| v11.1.0  | 2025-11-20 | Initial release; Airflow 3.x uplift; deterministic seed    |

---

<div align="center">

### 🔗 Footer  
[📘 KFM Docs](../../../README.md) · [🧭 Governance](../../../standards/governance/ROOT-GOVERNANCE.md) · [🔐 FAIR+CARE](../../../standards/faircare/FAIRCARE-GUIDE.md)

</div>
