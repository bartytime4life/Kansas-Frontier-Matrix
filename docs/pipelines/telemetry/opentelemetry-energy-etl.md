---
title: "⚡ KFM v11.2.x — OpenTelemetry Energy Spans for Nightly ETL (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/telemetry/opentelemetry-energy-etl.md"
version: "v11.2.x"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Energy Systems Board · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v11.x compliant"

status: "Active / Enforced"
doc_kind: "Implementation Guide"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "telemetry"
  applies_to:
    - "etl"
    - "ai-workloads"
    - "ci-cd"
    - "neo4j-lineage"
    - "focus-mode"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public Technical Standard"

opentelemetry_profile: "OTel v1.x (traces/metrics/logs)"
provenance_profile: "W3C PROV-O"
catalog_profiles:
  - "STAC 1.0.x"
  - "DCAT 3.0"

sbom_ref: "releases/v11.2.x/sbom.spdx.json"
manifest_ref: "releases/v11.2.x/manifest.zip"
telemetry_ref: "releases/v11.2.x/otel-energy-etl-telemetry.json"
telemetry_schema: "schemas/telemetry/otel-energy-span-v1.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
energy_standards_ref: "docs/standards/energy/README.md"
faircare_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

doc_uuid: "urn:kfm:doc:pipelines:telemetry:opentelemetry-energy-etl:v11.2.x"
semantic_document_id: "kfm-pipelines-telemetry-opentelemetry-energy-etl"
event_source_id: "ledger:docs/pipelines/telemetry/opentelemetry-energy-etl.md"
immutability_status: "version-pinned"

machine_extractable: true
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "diagram-extraction"
  - "metadata-extraction"
ai_transform_prohibited:
  - "speculative additions"
  - "unverified architectural claims"
  - "governance-override"

accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "24 months"
sunset_policy: "Superseded upon next major telemetry pattern revision"
---

<div align="center">

# ⚡ **OpenTelemetry Energy Spans for Nightly ETL**  
`docs/pipelines/telemetry/opentelemetry-energy-etl.md`

**Attach reproducible energy & carbon metrics to every pipeline run, per node.**

</div>

---

## 📘 Overview

This guide defines how KFM instruments **nightly ETL jobs** with **OpenTelemetry (OTel)** spans that capture:

- CPU/GPU **energy (J)**, wall‑time (s), and utilization (%)  
- Hardware and node identifiers (for per‑node efficiency roll‑ups)  
- Mapping to **grid carbon intensity → gCO₂e** per span and per run  

Emitted telemetry:

- Flows into the **Energy Standards Index** for dashboards and SLO gating.  
- Is linked via **PROV‑O** into dataset lineage.  
- Is surfaced in STAC/DCAT properties for energy‑aware analysis.

Why this matters:

- **Reproducibility** — energy and carbon become **first‑class artifacts** (stored, versioned, queryable).  
- **FAIR+CARE** — transparent, comparable compute costs for equity‑minded governance.  
- **Ops** — bottlenecks localized by node/task; budget alarms tied to error budgets and carbon targets.

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 telemetry/
        📄 opentelemetry-energy-etl.md      # ← This guide

📁 schemas/
└── 📁 telemetry/
    📄 energy-v2.json                       # Canonical energy metrics schema
    📄 carbon-v2.json                       # Canonical carbon metrics schema
    📄 otel-energy-span-v1.json             # OTel span attribute contract

📁 src/
└── 📁 pipelines/
    └── 📁 nightly/
        📁 jobs/
        │   📄 hrrr_ingest.py
        │   📄 usgs_gauges.py
        📁 _otel/
        │   📄 otel_setup.py                # OTel SDK & resource init
        │   📄 energy_exporter.py           # Helper to compute gCO₂e etc.
        │   📄 carbon_factors.py            # Regional grid intensity logic
        │   📄 node_introspection.py        # CPU/GPU power/energy sampling
        └── 📁 dags/
            📄 nightly_graph.py             # Orchestrator wiring OTel into DAG nodes
```

Nightly ETL jobs outside `src/pipelines/nightly/` must **reuse the same OTel helpers** or a domain‑specific wrapper that adheres to `otel-energy-span-v1.json`.

---

## 🧩 Minimal Implementation Pattern

### 1️⃣ Initialize OpenTelemetry per Job / DAG

```python
# src/pipelines/nightly/_otel/otel_setup.py
from opentelemetry import trace, metrics
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

def init_otel(service_name: str, run_id: str):
    """
    Initialize OTel trace + metrics providers for a single KFM ETL run.

    Required attributes:
      - service.name
      - kfm.run_id
      - kfm.component
    """
    resource = Resource.create({
        "service.name": service_name,
        "kfm.run_id": run_id,
        "kfm.component": "etl",
    })

    tracer_provider = TracerProvider(resource=resource)
    tracer_provider.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter())
    )
    trace.set_tracer_provider(tracer_provider)

    metric_reader = PeriodicExportingMetricReader(OTLPMetricExporter())
    meter_provider = MeterProvider(resource=resource, metric_readers=[metric_reader])
    metrics.set_meter_provider(meter_provider)

    return trace.get_tracer(service_name)
```

**Notes**

- `run_id` should come from a deterministic source (e.g., `KFM_RUN_ID` set by CI/orchestrator).  
- Export endpoint (OTLP) is configured via standard OTel env vars or orchestrator secrets.

---

### 2️⃣ Sample Node Energy & Utilization

```python
# src/pipelines/nightly/_otel/node_introspection.py
import pathlib
import psutil
import time

def read_cpu_energy_joules():
    """
    Preferred: read directly from RAPL/SoC counters when available.
    Fallback: return None and let caller use a modelled estimate.
    """
    rapl = pathlib.Path("/sys/class/powercap/intel-rapl:0/energy_uj")
    if rapl.exists():
        # microjoules → joules
        return int(rapl.read_text().strip()) / 1_000_000.0
    return None

def sample_cpu_util_pct(interval_s: float = 1.0) -> float:
    return psutil.cpu_percent(interval=interval_s)

def gpu_power_watts():
    """
    Example: NVIDIA via NVML (pseudo-code).
    Must degrade gracefully to None when unavailable.
    """
    try:
        import pynvml as nv
        nv.nvmlInit()
        h = nv.nvmlDeviceGetHandleByIndex(0)
        return nv.nvmlDeviceGetPowerUsage(h) / 1000.0  # watts
    except Exception:
        return None
```

---

### 3️⃣ Wrap Each ETL Node in an Energy Span

```python
# src/pipelines/nightly/jobs/hrrr_ingest.py
import os, socket, time
from src.pipelines.nightly._otel.otel_setup import init_otel
from src.pipelines.nightly._otel.node_introspection import (
    read_cpu_energy_joules,
    gpu_power_watts,
)
from src.pipelines.nightly._otel.energy_exporter import to_gco2e

RUN_ID = os.environ["KFM_RUN_ID"]
tracer = init_otel("kfm.etl.hrrr_ingest", run_id=RUN_ID)

def run():
    cpu_start_j = read_cpu_energy_joules()
    gpu_w_start = gpu_power_watts()
    t0 = time.time()

    with tracer.start_as_current_span("etl.node.hrrr_ingest") as span:
        span.set_attribute("kfm.node", "hrrr_ingest")
        span.set_attribute("kfm.hostname", socket.gethostname())
        span.set_attribute("kfm.domain", "atmo")
        span.set_attribute("kfm.pipeline_kind", "nightly")

        # --- do the actual work here ---
        # fetch → decode → normalize → write
        # --------------------------------

        t1 = time.time()
        cpu_end_j = read_cpu_energy_joules()
        gpu_w_end = gpu_power_watts()

        duration_s = t1 - t0
        cpu_delta_j = (
            cpu_end_j - cpu_start_j
            if cpu_end_j is not None and cpu_start_j is not None
            else None
        )
        gpu_w_avg = (
            (gpu_w_start + gpu_w_end) / 2.0
            if gpu_w_start is not None and gpu_w_end is not None
            else None
        )

        span.set_attribute("energy.cpu_j", cpu_delta_j)
        span.set_attribute("energy.gpu_w_avg", gpu_w_avg)
        span.set_attribute("timing.duration_s", duration_s)

        gco2e = to_gco2e(cpu_j=cpu_delta_j, gpu_w_avg=gpu_w_avg, duration_s=duration_s)
        span.set_attribute("carbon.gco2e", gco2e)
```

**Required span attributes (see `otel-energy-span-v1.json`):**

- `kfm.run_id`, `kfm.node`, `kfm.component`, `kfm.domain`, `kfm.pipeline_kind`  
- `energy.cpu_j`, `energy.gpu_w_avg` (or modelled equivalent), `timing.duration_s`  
- `carbon.gco2e` (computed via domain‑approved factors)

---

### 4️⃣ Convert Energy → Carbon Using Regional Factors

```python
# src/pipelines/nightly/_otel/carbon_factors.py
from dataclasses import dataclass
from typing import Optional
import datetime as dt

@dataclass
class RegionFactor:
    region_code: str           # e.g. 'SPP_KS', 'MISO', etc.
    intensity_gco2_per_kwh: float

def lookup_factor(ts: dt.datetime, region_code: str) -> RegionFactor:
    """
    Look up grid carbon intensity using time-varying tables
    (hourly preferred, daily fallback, static worst-case fallback).
    """
    # Implementation detail: load from precomputed tables, not live API,
    # so that runs are reproducible.
    raise NotImplementedError

def to_gco2e(cpu_j: Optional[float], gpu_w_avg: Optional[float], duration_s: float,
             region_code: str = "SPP_KS") -> Optional[float]:
    """
    Convert node-level energy to gCO2e using region factors.
    """
    if cpu_j is None and gpu_w_avg is None:
        return None

    cpu_kwh = (cpu_j / 3_600_000.0) if cpu_j is not None else 0.0
    gpu_kwh = (gpu_w_avg * duration_s) / 3_600_000.0 if gpu_w_avg is not None else 0.0
    total_kwh = cpu_kwh + gpu_kwh

    factor = lookup_factor(dt.datetime.utcnow(), region_code)
    return total_kwh * factor.intensity_gco2_per_kwh
```

**Key rule:** intensity tables must be **versioned** and included in provenance (`prov:Entity` with explicit `version` and `source`).

---

## 📈 Aggregation & Dashboards

Nightly aggregation jobs (e.g., `energy_rollup`) should:

- Consume OTel spans from the collector (via metrics or logs backend).  
- Compute:

  - **Per-node efficiency**: `total_j / records_out` (or per MB / per graph node),  
  - **Per-pipeline gCO₂e**: sum of `carbon.gco2e` for all node spans in a run,  
  - **Baseline trends**: 7–30 day rolling averages for energy per record and gCO₂e per run.

- Export results to the **Energy Standards Index** dashboards:

  - **Budget SLO:** `gco2e_per_run ≤ target` for key pipelines,  
  - **Regression Gate:** PRs that increase `gco2e_per_record` or `gco2e_per_node` beyond threshold fail CI.

Suggested backing store:

- OTLP → OTel Collector → time‑series DB (e.g., Prometheus/Mimir via OTLP bridge).  

Roll-ups should also be serialized into JSON artifacts tied to releases, e.g.:

- `releases/v11.2.x/energy-rollup-nightly.json`.

---

## 🌐 Provenance & Catalog Integration

Every energy span set for a pipeline run must be connectable to:

- **PROV‑O**:

  - `prov:Activity` representing the ETL node execution,  
  - Attributes for `energy.cpu_j`, `energy.gpu_kwh`, `carbon.gco2e`, `runtime_s`,  
  - `prov:wasAssociatedWith` referencing KFM agents and infrastructure.

- **STAC / DCAT** (where appropriate):

  - STAC Item `properties` should include:

    ```json
    {
      "kfm:energy_ref": "telemetry/energy/kfm-run-<run-id>.json",
      "kfm:carbon_ref": "telemetry/carbon/kfm-run-<run-id>.json",
      "kfm:otel_span_bundle": "telemetry/otel/spans-kfm-run-<run-id>.json",
      "kfm:energy_schema": "schemas/telemetry/energy-v2.json",
      "kfm:carbon_schema": "schemas/telemetry/carbon-v2.json"
    }
    ```

  - DCAT distributions derived from STAC should preserve references to the energy/carbon telemetry objects.

- **Neo4j lineage**:

  - Node `(:Run {run_id, kind:'nightly', domain:'telemetry'})`  
  - Relationships:

    - `(:Run)-[:HAS_ENERGY_TELEMETRY]->(:TelemetryBundle)`,  
    - `(:Run)-[:GENERATED]->(:DatasetVersion)` for affected datasets,  
    - `(:TelemetryBundle)-[:DESCRIBES_ACTIVITY]->(:Run)`.

The **telemetry bundle** referenced in `telemetry_ref` must conform to `telemetry_schema`.

---

## 🧪 CI & Governance Checks

### CI Requirements

Nightly ETL and other pipelines adopting this pattern must pass:

- **Docs + Schema**:

  - `markdown-lint` for this guide,  
  - `schema-lint` for `energy-v2.json`, `carbon-v2.json`, `otel-energy-span-v1.json`.

- **Instrumentation Checks**:

  - Unit tests for `to_gco2e` and carbon factor lookup.  
  - A test that asserts all **production ETL nodes** register:

    - `energy.cpu_j` or a documented modelled substitute,  
    - `carbon.gco2e` on their main ETL span.

- **Regression Gates**:

  - CI compares `gco2e_per_record` to historical baselines; merges are blocked when regression exceeds configured thresholds unless explicitly waived.

### Governance & FAIR+CARE

- **Energy Systems Board**:

  - Approves carbon intensity tables and methodologies,  
  - Reviews significant changes in energy/CO₂e budget footprints.

- **FAIR+CARE Council**:

  - Reviews how energy/carbon metrics are used in governance and communication,  
  - Ensures no misuse at the individual/PII level (aggregated, system‑level only).

- **Data & Sovereignty**:

  - Energy telemetry is **not** per‑person and contains no PII.  
  - When mapping energy to projects related to sovereign data, avoid attributing carbon costs to specific communities; keep reporting at system or domain layer.

---

## 🧪 Local Smoke Test

Quick local validation for one ETL job:

1. Set a unique run ID:

   ```bash
   export KFM_RUN_ID="$(date +%Y%m%d%H%M%S)"
   ```

2. Run a single job (e.g., HRRR ingest):

   ```bash
   python -m src.pipelines.nightly.jobs.hrrr_ingest
   ```

3. Verify in the OTel backend / collector that:

   - A span named `etl.node.hrrr_ingest` exists,  
   - Attributes include `kfm.run_id`, `energy.cpu_j`, `carbon.gco2e`, `timing.duration_s`.

4. Confirm that the energy/carbon attributes pass validation against:

   - `schemas/telemetry/energy-v2.json`,  
   - `schemas/telemetry/carbon-v2.json`,  
   - `schemas/telemetry/otel-energy-span-v1.json`.

---

## 🕰️ Version History

| Version | Date       | Summary                                                 |
|--------:|------------|---------------------------------------------------------|
| v11.2.x | 2025-12-08 | Initial governed OpenTelemetry energy-span guide for nightly ETL pipelines under KFM v11.2.x. |

---

<div align="center">

⚡ **Kansas Frontier Matrix — OpenTelemetry Energy Spans for Nightly ETL**  

[📘 Docs Root](../../README.md) ·  
[🔌 Energy Standards Index](../../standards/energy/README.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>