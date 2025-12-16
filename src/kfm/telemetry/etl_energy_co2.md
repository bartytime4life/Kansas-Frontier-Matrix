---
title: "⚡ KFM — ETL Energy & CO₂ Telemetry · OpenTelemetry · STAC · PROV"
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
classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "telemetry"
  applies_to:
    - "src/**"
    - "pipelines/**"
    - "tools/telemetry/**"
    - "schemas/telemetry/**"
    - "data/stac/**"

diagram_profiles:
  - "mermaid-flowchart-v1"

commit_sha: "<latest-commit-hash>"
signature_ref: "././releases/v11.2.6/signature.sig"
provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"

doc_uuid: "urn:kfm:doc:telemetry:etl-energy-co2:v11.2.6"
semantic_document_id: "kfm-telemetry-etl-energy-co2"
event_source_id: "kfm:src:kfm/telemetry:etl_energy_co2.md"

ai_transform_permissions:
  - "summarize"
  - "extract-metadata"
  - "format-normalization"
  - "generate-snippets-from-provided-content-only"
ai_transform_prohibited:
  - "invent-measurements"
  - "invent-governance-status"
  - "fabricate-provenance"
  - "introduce-new-metrics-or-schema-claims-without-review"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"
---

# ⚡ KFM — ETL Energy & CO₂ Telemetry · OpenTelemetry · STAC · PROV

> **Purpose**  
> Provide a minimal, governed pattern to instrument ETL runs with energy (J), network and disk I/O (By), and derived CO₂ (kg CO₂e), emit OpenTelemetry signals, and persist run telemetry into a STAC Item with an attached PROV JSON-LD asset for auditability.

## 📘 Overview

This guide adds **copy-paste instrumentation** to ETL steps that already produce or update STAC Items.

You get:

- OpenTelemetry metrics and traces that collectors can ingest
- Deterministic conversion from **J → kWh → kg CO₂e** with a configurable emission factor
- A stable place to persist per-run telemetry:
  - STAC Item `properties.kfm:telemetry`
  - STAC Asset `telemetry-prov` containing PROV JSON-LD

Non-goals:

- This is not a full power-modeling framework.
- This does not prescribe a single hardware measurement method.
- This does not bypass KFM governance and release processes.

### Quickstart

~~~bash
pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp pystac
~~~

Then adapt the reference implementation below and call:

- `run_etl_job(run_id=..., emission_factor_kg_per_kwh=...)`
- `persist_to_stac_item(item_path=..., tele=...)`

## 🗂️ Directory Layout

Canonical placement and output layout.

~~~text
📦 <repo-root>/
├─ 📂 src/
│  └─ 📂 kfm/
│     └─ 📂 telemetry/
│        └─ 📄 etl_energy_co2.md                    # This guide (governed how-to)
├─ 📂 schemas/
│  └─ 📂 telemetry/
│     ├─ 📄 energy-v2.json                          # Energy telemetry schema
│     └─ 📄 carbon-v2.json                          # Carbon telemetry schema
├─ 📂 tools/
│  └─ 📂 telemetry/
│     └─ 📄 ...                                     # Aggregation / reporting helpers
└─ 📂 data/
   └─ 📂 stac/
      └─ 📂 <domain>/
         └─ 📂 items/
            ├─ 📄 <item-id>.geojson                 # STAC Item
            └─ 📂 assets/
               └─ 📂 telemetry/
                  └─ 📄 <run-id>-prov.jsonld        # PROV JSON-LD asset (run-level)
~~~

Rule:

- Telemetry persistence **must not** write outside the STAC Item directory (or declared output root) for the ETL step.
- If your catalog storage uses a different layout, keep `Asset.href` relative and adjust the write location accordingly.

## 🧭 Context

### Measurement sources

Replace simulated values with real measurements as your environment allows.

Common approaches:

- CPU package energy counters such as RAPL, polled and integrated over time
- BMC/IPMI power reads, integrated over time
- Node-level telemetry via Prometheus node exporter or similar, integrated over time
- Cloud provider energy or power APIs where available

This pattern stays valid regardless of measurement source as long as you output joules and I/O bytes.

### Emission factor governance

CO₂ is derived from energy using an **emission factor**:

- `co2_kg = kwh * emission_factor_kg_per_kwh`

You must treat the emission factor as governed metadata:

- Configure it per region, supplier, or contract
- Record its source and effective date in run notes or dataset governance notes
- Do not present example defaults as authoritative for Kansas without verification

### Metric naming

This pattern uses dot-delimited, OpenTelemetry-style metric names:

- `hw.host.energy` (J)
- `process.network.io` (By)
- `process.disk.io` (By)

If your collector or internal conventions require a different namespace, keep the semantics but rename consistently and update downstream dashboards accordingly.

## 🗺️ Diagrams

~~~mermaid
flowchart LR
  A[ETL job step] --> B[OpenTelemetry metrics and traces]
  B --> C[OTel Collector]
  C --> D[Metrics and traces backends]

  A --> E[STAC Item update]
  E --> F[kfm:telemetry in properties]
  E --> G[telemetry-prov asset]
  G --> H[PROV JSON-LD file]
  E --> I[STAC Catalog and Collection workflows]
  I --> J[Graph ingestion via governed APIs]
~~~

## 🧱 Architecture

Where this pattern fits in the KFM pipeline:

- **ETL stage**: compute or capture run telemetry and persist it with the run outputs
- **Catalog stage**: STAC Items and assets remain the canonical metadata surface for downstream indexing
- **Lineage stage**: PROV JSON-LD enables audit and linkage to run IDs, agents, and generated artifacts
- **Graph stage**: ingestion should read telemetry via catalogs or APIs, not by direct frontend access to the graph
- **UI stage**: the UI consumes telemetry summaries through APIs only

This doc changes no pipeline contracts. It only defines a stable telemetry payload and where it is persisted.

## 📦 Data & Metadata

### Unit conversions

- `kwh = joules / 3_600_000`
- `co2_kg = kwh * emission_factor_kg_per_kwh`

### Minimal telemetry record for STAC

A compact telemetry record stored in the STAC Item should be:

- Numeric, unit-stable fields
- Explicit timestamps
- Explicit emission factor used

Example shape:

~~~json
{
  "run_id": "etl-2025-12-16-0001",
  "started_at": "2025-12-16T12:00:00Z",
  "ended_at": "2025-12-16T12:03:11Z",
  "duration_seconds": 191.0,
  "energy_joules": 55000000.0,
  "energy_kwh": 15.2777777778,
  "emission_factor_kg_per_kwh": 0.4,
  "co2_kg": 6.1111111111,
  "bytes_sent": 12345678,
  "bytes_received": 2222222,
  "bytes_disk_read": 987654,
  "bytes_disk_written": 123456,
  "measurement_method": "simulated",
  "recorded_at": "2025-12-16T12:03:11Z"
}
~~~

### Reference implementation

Copy, paste, and adapt.

~~~python
# Requires:
#   pip install opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp pystac

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

import pystac
from opentelemetry import metrics, trace
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider as SDKTracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor

JOULES_PER_KWH = 3_600_000.0


def utc_now_iso() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def joules_to_kwh(joules: float) -> float:
    return joules / JOULES_PER_KWH


def kwh_to_co2_kg(kwh: float, emission_factor_kg_per_kwh: float) -> float:
    return kwh * emission_factor_kg_per_kwh


@dataclass(frozen=True)
class EtlTelemetry:
    run_id: str
    started_at: str
    ended_at: str
    duration_seconds: float

    energy_joules: float
    energy_kwh: float
    emission_factor_kg_per_kwh: float
    co2_kg: float

    bytes_sent: int
    bytes_received: int
    bytes_disk_read: int
    bytes_disk_written: int

    measurement_method: str
    notes: Optional[str] = None


def init_otel(service_name: str = "kfm-etl", service_version: str = "v11.2.6"):
    resource = Resource.create(
        {
            "service.name": service_name,
            "service.version": service_version,
        }
    )

    metric_reader = PeriodicExportingMetricReader(
        OTLPMetricExporter(),
        export_interval_millis=5000,
    )
    metrics.set_meter_provider(MeterProvider(resource=resource, metric_readers=[metric_reader]))
    meter = metrics.get_meter("kfm.telemetry.energy", "0.1.0")

    trace.set_tracer_provider(SDKTracerProvider(resource=resource))
    tracer = trace.get_tracer("kfm.telemetry.etl", "0.1.0")
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))

    return meter, tracer


METER, TRACER = init_otel()

ENERGY_COUNTER = METER.create_counter(
    "hw.host.energy",
    unit="J",
    description="Host energy in joules",
)
NET_COUNTER = METER.create_counter(
    "process.network.io",
    unit="By",
    description="Process network I/O in bytes",
)
DISK_COUNTER = METER.create_counter(
    "process.disk.io",
    unit="By",
    description="Process disk I/O in bytes",
)


def run_etl_job(
    run_id: str,
    emission_factor_kg_per_kwh: float,
    measurement_method: str = "simulated",
) -> EtlTelemetry:
    started_at = utc_now_iso()
    t0 = time.time()

    with TRACER.start_as_current_span(
        "etl.job",
        attributes={
            "run.id": run_id,
            "kfm.pipeline.stage": "etl",
            "telemetry.measurement_method": measurement_method,
        },
    ) as span:
        # Replace these with real measurements for your environment.
        energy_joules = 55_000_000.0
        bytes_sent, bytes_received = 12_345_678, 2_222_222
        bytes_disk_read, bytes_disk_written = 987_654, 123_456

        ENERGY_COUNTER.add(energy_joules, {"kfm.run_id": run_id})
        NET_COUNTER.add(bytes_sent, {"kfm.run_id": run_id, "network.io.direction": "transmit"})
        NET_COUNTER.add(bytes_received, {"kfm.run_id": run_id, "network.io.direction": "receive"})
        DISK_COUNTER.add(bytes_disk_read, {"kfm.run_id": run_id, "disk.io.direction": "read"})
        DISK_COUNTER.add(bytes_disk_written, {"kfm.run_id": run_id, "disk.io.direction": "write"})

        energy_kwh = joules_to_kwh(energy_joules)
        co2_kg = kwh_to_co2_kg(energy_kwh, emission_factor_kg_per_kwh)

        span.set_attribute("telemetry.energy_joules", energy_joules)
        span.set_attribute("telemetry.energy_kwh", energy_kwh)
        span.set_attribute("telemetry.emission_factor_kg_per_kwh", emission_factor_kg_per_kwh)
        span.set_attribute("telemetry.co2_kg", co2_kg)
        span.set_attribute("telemetry.bytes_sent", bytes_sent)
        span.set_attribute("telemetry.bytes_received", bytes_received)
        span.set_attribute("telemetry.bytes_disk_read", bytes_disk_read)
        span.set_attribute("telemetry.bytes_disk_written", bytes_disk_written)

    ended_at = utc_now_iso()
    duration = time.time() - t0

    return EtlTelemetry(
        run_id=run_id,
        started_at=started_at,
        ended_at=ended_at,
        duration_seconds=duration,
        energy_joules=energy_joules,
        energy_kwh=energy_kwh,
        emission_factor_kg_per_kwh=emission_factor_kg_per_kwh,
        co2_kg=co2_kg,
        bytes_sent=bytes_sent,
        bytes_received=bytes_received,
        bytes_disk_read=bytes_disk_read,
        bytes_disk_written=bytes_disk_written,
        measurement_method=measurement_method,
        notes="Example values only. Replace with real measurements.",
    )


def persist_to_stac_item(item_path: str, tele: EtlTelemetry) -> Dict[str, Any]:
    item_file = Path(item_path)
    item = pystac.Item.from_file(str(item_file))

    item.properties.setdefault("kfm:telemetry", {})
    item.properties["kfm:telemetry"].update(
        {
            **asdict(tele),
            "recorded_at": utc_now_iso(),
            "kfm:energy_schema": "schemas/telemetry/energy-v2.json",
            "kfm:carbon_schema": "schemas/telemetry/carbon-v2.json",
        }
    )

    prov_rel = Path("assets/telemetry") / f"{tele.run_id}-prov.jsonld"
    prov_abs = item_file.parent / prov_rel
    prov_abs.parent.mkdir(parents=True, exist_ok=True)

    prov_doc = {
        "@context": {
            "prov": "http://www.w3.org/ns/prov#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        },
        "@id": f"urn:kfm:prov:activity:{tele.run_id}",
        "@type": "prov:Activity",
        "prov:startedAtTime": {"@value": tele.started_at, "@type": "xsd:dateTime"},
        "prov:endedAtTime": {"@value": tele.ended_at, "@type": "xsd:dateTime"},
        "prov:generated": [
            {
                "@id": f"urn:kfm:telemetry:{tele.run_id}",
                "@type": "prov:Entity",
                "prov:value": {
                    "energy_joules": tele.energy_joules,
                    "energy_kwh": tele.energy_kwh,
                    "co2_kg": tele.co2_kg,
                    "emission_factor_kg_per_kwh": tele.emission_factor_kg_per_kwh,
                    "bytes_sent": tele.bytes_sent,
                    "bytes_received": tele.bytes_received,
                    "bytes_disk_read": tele.bytes_disk_read,
                    "bytes_disk_written": tele.bytes_disk_written,
                    "duration_seconds": tele.duration_seconds,
                    "measurement_method": tele.measurement_method,
                },
            }
        ],
    }
    prov_abs.write_text(json.dumps(prov_doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    item.add_asset(
        "telemetry-prov",
        pystac.Asset(
            href=str(prov_rel).replace("\\", "/"),
            media_type="application/ld+json",
            roles=["metadata", "provenance"],
            title="Run-level telemetry provenance (PROV JSON-LD)",
        ),
    )

    item.save_object(include_self_link=False)

    return {
        "stac_item_path": str(item_file),
        "prov_asset_path": str(prov_abs),
        "run_id": tele.run_id,
    }


# Example usage:
# tele = run_etl_job(run_id="etl-2025-12-16-0001", emission_factor_kg_per_kwh=0.4)
# persist_to_stac_item(item_path="data/stac/<domain>/items/<item-id>.geojson", tele=tele)
~~~

## 🧪 Validation & CI/CD

Minimum checks recommended for CI or local preflight:

- Markdown checks:
  - Exactly one H1
  - Approved H2 headings only
  - No mixed fence styles inside committed files
  - Footer governance links present

- Schema checks:
  - Validate stored telemetry fields against referenced telemetry schemas
  - Validate STAC Item conformance with your STAC validator

Example local validation commands:

~~~bash
# Schema validation patterns will vary depending on your validator tooling.
# Keep these commands consistent with your repo's standard CI tasks.

python -c "import pystac; pystac.Item.from_file('data/stac/<domain>/items/<item-id>.geojson').validate()"
~~~

Operational checks:

- Telemetry numbers must be non-negative
- If `measurement_method` is not simulated, record the measurement source and sampling interval in run notes or a run log

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Persist telemetry under `Item.properties.kfm:telemetry`
- Attach the PROV JSON-LD run record as an asset:
  - `assets.telemetry-prov.href = assets/telemetry/<run-id>-prov.jsonld`
  - `media_type = application/ld+json`

### DCAT

Telemetry is typically a dataset distribution detail rather than the primary dataset record.

Common patterns:

- Treat the STAC Item as the canonical metadata and expose telemetry through STAC assets.
- If DCAT metadata is produced for the dataset, reference the telemetry artifact as an additional distribution when appropriate.

### PROV

Run telemetry is represented as:

- `prov:Activity` identified by `run_id`
- `prov:Entity` for the produced telemetry record
- Optional extensions:
  - `prov:wasAssociatedWith` linking to a CI bot, operator, or runtime agent
  - `prov:used` linking to the dataset inputs that were processed

## ⚖ FAIR+CARE & Governance

- Telemetry can reveal operational characteristics of infrastructure.
  - If exposure is a concern, raise `classification` and adjust publication rules for telemetry assets.
- Emission factor selection is a governance concern.
  - Record factor source, date, and region.
  - Prefer supplier or region-specific factors when available.
- When telemetry is attached to runs processing sensitive datasets:
  - Ensure the run complies with sovereignty and ethical handling requirements.
  - Do not embed sensitive identifiers or disallowed locations inside telemetry notes.

## 🕰️ Version History

| Version     | Date       | Summary |
|------------:|-----------:|---------|
| **v11.2.6** | 2025-12-16 | Initial governed pattern for ETL energy and CO₂ telemetry using OpenTelemetry signals, STAC persistence, and a PROV JSON-LD asset. |

---

🔗 Navigation

- Standards: `docs/standards/README.md`
- Telemetry docs: `docs/telemetry/README.md`
- Governance charter: `docs/standards/governance/ROOT-GOVERNANCE.md`
- FAIR+CARE guide: `docs/standards/faircare/FAIRCARE-GUIDE.md`
- Sovereignty policy: `docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md`