---
title: "⚡ KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)"
path: "src/kfm/telemetry/etl_energy_co2.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "How-To + Reference"
header_profile: "standard"
footer_profile: "standard"
intent: "etl-energy-co2-telemetry"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

doc_uuid: "urn:kfm:doc:telemetry:etl-energy-co2:v11.2.6"
semantic_document_id: "kfm-telemetry-etl-energy-co2"
event_source_id: "ledger:kfm:doc:telemetry:etl-energy-co2:v11.2.6"
immutability_status: "mutable-plan"

commit_sha: "<latest-commit-hash>"
provenance_chain: []

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "a11y-adaptations"
  - "metadata-extraction"
  - "layout-normalization"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"
---

# ⚡ KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)

> **Purpose**  
> Provide a governed, copy‑paste telemetry pattern for KFM ETL runs that:
> 1) measures energy (J), network/disk bytes, and duration,  
> 2) converts energy → kWh → CO₂ (kg) using a configurable emission factor, and  
> 3) persists the run telemetry into a **STAC Item** with an attached **PROV JSON‑LD** asset, while also emitting **OpenTelemetry** metrics/traces for centralized observability.

---

## 📘 Overview

This page describes a **drop‑in instrumentation pattern** you can embed in any KFM ETL job.

### What you get

- **OpenTelemetry metrics** (OTLP‑exportable) using semantic metric names:
  - `hw.host.energy` (J)
  - `process.disk.io` (By)
  - `process.network.io` (By)
- **CO₂ conversion**: `co2_kg = (energy_joules / 3_600_000) * emission_factor_kg_per_kwh`
- **Persistence**:
  - `STAC Item → properties["kfm:telemetry"]`
  - `STAC Asset → "telemetry-prov"` (PROV JSON‑LD)

### What this does not do

- It does **not** prescribe a single “correct” hardware energy reader. Energy sources vary by platform (RAPL/IPMI/cloud APIs/collector‑side measurement).
- It does **not** guarantee per‑process energy attribution. If you read *host* energy, you may need allocation logic if multiple jobs share a node.

### Quickstart

#### Dependencies

~~~bash
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp pystac
~~~

#### Minimal drop‑in example

~~~python
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import pystac
from opentelemetry import metrics, trace
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider as SDKTracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def joules_to_kwh(joules: float) -> float:
    # 1 kWh = 3,600,000 J
    return float(joules) / 3_600_000.0


def read_proc_disk_io_linux() -> Optional[Dict[str, int]]:
    """
    Best-effort per-process disk I/O using Linux /proc.
    Returns None if not supported.
    """
    p = Path("/proc/self/io")
    if not p.exists():
        return None
    out: Dict[str, int] = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if v.isdigit():
            out[k] = int(v)
    # Keys commonly available: read_bytes, write_bytes
    if "read_bytes" not in out and "write_bytes" not in out:
        return None
    return out


def read_host_energy_joules() -> Optional[int]:
    """
    Placeholder hook. Replace with a real, monotonic host energy counter if available:
    - RAPL (Intel) / sysfs
    - IPMI (BMC)
    - Cloud provider power telemetry
    - Collector-side host metrics receiver
    Return None if unavailable.
    """
    return None


@dataclass(frozen=True)
class TelemetryResult:
    run_id: str
    started_at: str
    ended_at: str
    duration_seconds: float

    energy_joules: Optional[float]
    energy_kwh: Optional[float]
    co2_kg: Optional[float]
    emission_factor_kg_per_kwh: Optional[float]
    emission_factor_source: Optional[str]

    disk_read_bytes: Optional[int]
    disk_write_bytes: Optional[int]
    net_tx_bytes: Optional[int]
    net_rx_bytes: Optional[int]


def build_otel() -> Tuple[Any, Any, Any, Any, Any]:
    resource = Resource.create(
        {
            "service.name": "kfm-etl",
            "service.version": "v11.2.6",
            "deployment.environment": os.getenv("KFM_ENV", "dev"),
        }
    )

    metric_exporter = OTLPMetricExporter()  # configure via OTEL_EXPORTER_OTLP_ENDPOINT
    metric_reader = PeriodicExportingMetricReader(metric_exporter, export_interval_millis=5000)
    metrics.set_meter_provider(MeterProvider(resource=resource, metric_readers=[metric_reader]))
    meter = metrics.get_meter("kfm.telemetry.energy", "0.1.0")

    trace.set_tracer_provider(SDKTracerProvider(resource=resource))
    tracer = trace.get_tracer("kfm.telemetry.etl")
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))

    energy_counter = meter.create_counter(
        "hw.host.energy",
        unit="J",
        description="Host energy consumption in joules (best-effort source).",
    )
    disk_counter = meter.create_counter(
        "process.disk.io",
        unit="By",
        description="Process disk I/O in bytes (read/write).",
    )
    net_counter = meter.create_counter(
        "process.network.io",
        unit="By",
        description="Process network I/O in bytes (tx/rx) (best-effort).",
    )
    return tracer, energy_counter, disk_counter, net_counter, meter


def run_job_with_telemetry(run_id: str) -> TelemetryResult:
    """
    Wrap your ETL work inside this function (or copy the pattern into your script).
    This example uses best-effort measurement hooks and is safe to run when hooks are unavailable.
    """
    tracer, energy_counter, disk_counter, net_counter, _meter = build_otel()

    started_at = utc_now_iso()
    t0 = time.time()

    # Configurable emission factor (kg CO2 per kWh).
    # Set these from your governed config stack (YAML/JSON/env) and record the source string.
    emission_factor = float(os.getenv("KFM_EMISSION_FACTOR_KG_PER_KWH", "0.0")) or None
    emission_factor_source = os.getenv("KFM_EMISSION_FACTOR_SOURCE", None)

    # Baselines
    disk0 = read_proc_disk_io_linux()
    e0 = read_host_energy_joules()

    # NOTE: process-level network bytes are highly platform-dependent.
    # If you can’t measure per-process network bytes safely, set these to None and rely on
    # collector-side host metrics or app-level request accounting.
    net_tx = None
    net_rx = None

    with tracer.start_as_current_span(
        "etl.run",
        attributes={
            "kfm.run_id": run_id,
            "kfm.pipeline_stage": "ETL",
            "kfm.telemetry.profile": "energy-co2-v11.2.6",
        },
    ) as span:
        # ----------------------------
        # Your ETL job body goes here.
        # ----------------------------
        # Example placeholder work:
        time.sleep(0.05)

        # End measurements
        disk1 = read_proc_disk_io_linux()
        e1 = read_host_energy_joules()

        # Disk deltas (Linux /proc/self/io best-effort)
        disk_read = None
        disk_write = None
        if disk0 and disk1:
            disk_read = max(0, int(disk1.get("read_bytes", 0) - disk0.get("read_bytes", 0)))
            disk_write = max(0, int(disk1.get("write_bytes", 0) - disk0.get("write_bytes", 0)))

        # Energy delta (best-effort monotonic counter)
        energy_j = None
        energy_kwh = None
        co2_kg = None
        if e0 is not None and e1 is not None:
            energy_j = float(max(0, int(e1 - e0)))
            energy_kwh = joules_to_kwh(energy_j)
            if emission_factor is not None:
                co2_kg = float(energy_kwh * emission_factor)

        # Emit OTel counters (only when values exist)
        # Attributes should avoid secrets/PII; prefer stable IDs, not hostnames.
        if energy_j is not None:
            energy_counter.add(energy_j, {"hw.id": os.getenv("KFM_HW_ID", "unknown")})

        if disk_read is not None:
            disk_counter.add(disk_read, {"process.pid": str(os.getpid()), "disk.io.direction": "read"})
        if disk_write is not None:
            disk_counter.add(disk_write, {"process.pid": str(os.getpid()), "disk.io.direction": "write"})

        if net_tx is not None:
            net_counter.add(net_tx, {"process.pid": str(os.getpid()), "network.io.direction": "transmit"})
        if net_rx is not None:
            net_counter.add(net_rx, {"process.pid": str(os.getpid()), "network.io.direction": "receive"})

        # Span attributes for quick correlation (don’t treat spans as your canonical audit record).
        span.set_attribute("kfm.telemetry.energy_joules", energy_j if energy_j is not None else "null")
        span.set_attribute("kfm.telemetry.co2_kg", co2_kg if co2_kg is not None else "null")
        span.set_attribute("kfm.telemetry.duration_seconds", time.time() - t0)

    ended_at = utc_now_iso()
    duration = time.time() - t0

    return TelemetryResult(
        run_id=run_id,
        started_at=started_at,
        ended_at=ended_at,
        duration_seconds=float(duration),
        energy_joules=energy_j,
        energy_kwh=energy_kwh,
        co2_kg=co2_kg,
        emission_factor_kg_per_kwh=emission_factor,
        emission_factor_source=emission_factor_source,
        disk_read_bytes=disk_read,
        disk_write_bytes=disk_write,
        net_tx_bytes=net_tx,
        net_rx_bytes=net_rx,
    )


def persist_telemetry_to_stac_item(item_path: str, tele: TelemetryResult) -> str:
    """
    Persist telemetry in STAC Item properties and attach a PROV JSON-LD asset.
    Returns the PROV JSON-LD path written.
    """
    item = pystac.Item.from_file(item_path)

    # Canonical KFM namespaced property bucket
    item.properties.setdefault("kfm:telemetry", {})
    item.properties["kfm:telemetry"].update(
        {
            "run_id": tele.run_id,
            "profile": "energy-co2-v11.2.6",
            "recorded_at": utc_now_iso(),
            "started_at": tele.started_at,
            "ended_at": tele.ended_at,
            "duration_seconds": tele.duration_seconds,
            "energy": {
                "joules": tele.energy_joules,
                "kwh": tele.energy_kwh,
            },
            "carbon": {
                "co2_kg": tele.co2_kg,
                "emission_factor_kg_per_kwh": tele.emission_factor_kg_per_kwh,
                "emission_factor_source": tele.emission_factor_source,
            },
            "io": {
                "disk": {
                    "read_bytes": tele.disk_read_bytes,
                    "write_bytes": tele.disk_write_bytes,
                },
                "network": {
                    "tx_bytes": tele.net_tx_bytes,
                    "rx_bytes": tele.net_rx_bytes,
                },
            },
        }
    )

    # PROV JSON-LD (minimal audit record)
    prov_doc = {
        "@context": "https://openprovenance.org/prov-jsonld/context.jsonld",
        "@graph": [
            {
                "@id": f"urn:kfm:run:{tele.run_id}",
                "@type": "prov:Activity",
                "prov:startedAtTime": tele.started_at,
                "prov:endedAtTime": tele.ended_at,
                "prov:generated": [
                    {
                        "@id": f"urn:kfm:telemetry:{tele.run_id}",
                        "@type": "prov:Entity",
                        "kfm:energy_joules": tele.energy_joules,
                        "kfm:energy_kwh": tele.energy_kwh,
                        "kfm:co2_kg": tele.co2_kg,
                        "kfm:duration_seconds": tele.duration_seconds,
                    }
                ],
            }
        ],
    }

    # Write the PROV JSON-LD alongside the item (adapt to your storage layout)
    item_dir = Path(item_path).resolve().parent
    prov_dir = item_dir / "assets" / "telemetry"
    prov_dir.mkdir(parents=True, exist_ok=True)
    prov_path = prov_dir / f"{tele.run_id}-prov.jsonld"

    prov_path.write_text(json.dumps(prov_doc, ensure_ascii=False, indent=2), encoding="utf-8")

    # Attach as STAC asset (metadata role)
    item.assets["telemetry-prov"] = pystac.Asset(
        href=str(Path("assets/telemetry") / prov_path.name),
        media_type="application/ld+json",
        roles=["metadata"],
        title="PROV JSON-LD telemetry record for ETL run",
    )

    # Persist STAC Item update
    item.save_object()

    return str(prov_path)


# Example:
# tele = run_job_with_telemetry("etl-2025-12-16-0001")
# prov_written = persist_telemetry_to_stac_item("data/stac/items/sample-item.json", tele)
# print("Wrote PROV:", prov_written)
~~~

---

## 🗂️ Directory Layout

~~~text
📁 KansasFrontierMatrix/
├── 📁 src/                                            — Source code (pipelines, graph, APIs, UI)
│   └── 📁 kfm/
│       └── 📁 telemetry/
│           └── 📄 etl_energy_co2.md                    — This governed how‑to + reference
├── 📁 schemas/                                        — Schemas (docs, telemetry, SHACL, mappings)
│   └── 📁 telemetry/                                  — Telemetry schemas (energy, carbon, lineage)
│       ├── 📄 energy-v2.json                           — Energy telemetry schema (expected)
│       └── 📄 carbon-v2.json                           — Carbon telemetry schema (expected)
├── 📁 tools/                                          — Tooling and utilities for governance/validation
│   └── 📁 telemetry/                                  — Telemetry aggregation/validation helpers
└── 📁 docs/                                           — Documentation layer (standards, guides, telemetry)
    └── 📁 standards/
        ├── 📄 README.md                                — Standards index
        ├── 📄 telemetry_standards.md                   — Telemetry governance standard
        ├── 📁 governance/                              — Governance charter and governance standards
        ├── 📁 faircare/                                — FAIR+CARE guidance
        └── 📁 sovereignty/                             — Indigenous data protection & sovereignty policy
~~~

---

## 🧭 Context

KFM telemetry lives at the **ETL → catalog** boundary:

- **ETL** measures run costs (energy/CO₂/I/O/time) and emits metrics to collectors.
- **Catalog** persists an auditable record in:
  - **STAC** (Item‑level metadata)
  - **PROV** (run activity/entity record suitable for governance audits)
- Downstream, telemetry may be ingested into the **graph** and exposed via **APIs** to the UI and Focus Mode, without direct graph access from clients.

> Pipeline flow (canonical): deterministic ETL → STAC/DCAT/PROV catalogs → graph → APIs → UI → Story Nodes → Focus Mode.

---

## 🧱 Architecture

### Design principles

- **Best‑effort measurement with explicit nulls**: if a platform cannot read energy/network counters, record `null` and keep the run auditable.
- **Two lanes**:
  - **OTel lane** for real‑time observability (metrics/traces to a collector)
  - **STAC/PROV lane** for durable governance/audit metadata attached to produced assets

### Recommended adapter points

- `read_host_energy_joules()`:
  - RAPL/IPMI/cloud API/collector‑side host energy
- `read_proc_disk_io_linux()`:
  - per‑process disk bytes via `/proc/self/io` when available
- Network bytes:
  - app‑level accounting (wrap request libraries)
  - eBPF/collector‑side measurement
  - or record `null` and document the limitation

---

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL Job] --> B[Measure: Energy / IO / Duration]
  B --> C[OpenTelemetry Metrics + Traces]
  C --> D[OTLP Collector]
  B --> E[Compute: kWh + CO2]
  E --> F[Persist into STAC Item properties.kfm:telemetry]
  F --> G[Write PROV JSON-LD asset]
  G --> H[Catalog Ingestion]
  H --> I[Graph + APIs]
  I --> J[UI + Focus Mode]
~~~

---

## 📦 Data & Metadata

### Canonical telemetry fields (STAC persistence)

Store telemetry under a namespaced bucket:

- `properties["kfm:telemetry"]` (object)
  - `run_id` (string)
  - `profile` (string; pinned identifier for your schema)
  - `recorded_at`, `started_at`, `ended_at` (RFC3339 timestamps)
  - `duration_seconds` (number)
  - `energy.joules`, `energy.kwh` (number | null)
  - `carbon.co2_kg` (number | null)
  - `carbon.emission_factor_kg_per_kwh` (number | null)
  - `carbon.emission_factor_source` (string | null)
  - `io.disk.read_bytes`, `io.disk.write_bytes` (int | null)
  - `io.network.tx_bytes`, `io.network.rx_bytes` (int | null)

### OTel metric naming

Use OTel semantic metric names where possible and keep attributes minimal and non-sensitive.

Suggested mapping:

| Signal | OTel Metric Name | Unit | Direction attribute |
|---|---|---:|---|
| Host energy | `hw.host.energy` | J | N/A |
| Process disk bytes | `process.disk.io` | By | `disk.io.direction` = `read` / `write` |
| Process network bytes | `process.network.io` | By | `network.io.direction` = `transmit` / `receive` |

### CO₂ conversion and provenance

- Conversion:
  - `energy_kwh = energy_joules / 3_600_000`
  - `co2_kg = energy_kwh * emission_factor_kg_per_kwh`
- Governance requirement:
  - record the emission factor **and** a human‑readable `emission_factor_source` string (utility disclosure, supplier report, region average, etc.)

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC Item

- Telemetry is persisted under:
  - `properties["kfm:telemetry"]`
- PROV is attached as a STAC asset:
  - `assets["telemetry-prov"]` with `media_type="application/ld+json"` and `roles=["metadata"]`

### PROV JSON‑LD

Minimum viable pattern:

- **Activity**: `urn:kfm:run:<run_id>`
- **Entity**: `urn:kfm:telemetry:<run_id>`
- Relationship:
  - Activity `prov:generated` the telemetry entity

Keep the PROV asset small and audit‑friendly; the STAC Item remains the “discovery handle.”

### DCAT (optional)

If you publish dataset‑level DCAT, you may aggregate telemetry (e.g., total CO₂ per release) into:
- DCAT dataset annotations, or
- a release‑scoped distribution artifact (telemetry snapshot)

Do not overload per‑run detail into DCAT unless the catalog requires it.

---

## 🧪 Validation & CI/CD

### Local validation checklist

- Validate STAC JSON:
  - ensure the item remains a valid STAC Item after property/asset injection
- Validate telemetry shapes:
  - ensure `kfm:telemetry.energy` and `kfm:telemetry.carbon` match your pinned schema versions (when present)
- Secrets/PII scan:
  - ensure no endpoints/tokens/hostnames leak into persisted telemetry

### Example commands (adapt to repo tooling)

~~~bash
# 1) Basic JSON lint (example)
python -m json.tool data/stac/items/sample-item.json > /dev/null

# 2) If you have schema validators wired:
#    - validate telemetry object against schemas/telemetry/*
#    - validate STAC via pystac validation tooling
~~~

---

## 🧠 Story Node & Focus Mode Integration

Telemetry can safely support narrative and operational overlays when treated as **evidence**:

- Story Nodes may reference run telemetry to communicate:
  - processing cost, energy footprint, and transparency notes
- Focus Mode may summarize telemetry trends, but must:
  - avoid speculative claims about causality
  - preserve numeric values and units
  - cite the run_id and emission factor source string recorded in metadata

---

## ⚖ FAIR+CARE & Governance

- Treat telemetry as potentially sensitive when it contains:
  - detailed host identifiers, internal topology hints, or location-revealing metadata
- Follow the referenced governance documents:
  - Governance Charter (roles, review, compliance)
  - FAIR+CARE Guide (responsible stewardship and representation)
  - Indigenous Data Protection policy (sovereignty controls and masking rules)
- Required practice:
  - record emission factor source and measurement method notes (even if “unknown”), rather than silently omitting provenance.

---

## 🕰️ Version History

| Version | Date | Notes |
|---|---:|---|
| v11.2.6 | 2025-12-16 | Initial governed pattern for ETL energy/CO₂ telemetry via OpenTelemetry + STAC + PROV. |

---

<div align="center">

⚡ **KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)**  
Transparent Systems · Ethical Metrics · Sustainable Intelligence

[📂 Standards Index](../../../docs/standards/README.md) ·
[📈 Telemetry Standard](../../../docs/standards/telemetry_standards.md) ·
[🏛️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🪶 Indigenous Data Protection](../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md)

© 2025 Kansas Frontier Matrix — MIT  
MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑PDC v11 · KFM‑STAC/DCAT/PROV v11

</div>