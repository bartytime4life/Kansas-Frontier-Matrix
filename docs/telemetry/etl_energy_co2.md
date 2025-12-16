---
title: "⚡ KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)"
path: "docs/telemetry/etl_energy_co2.md"

version: "v11.2.6"
last_updated: "2025-12-16"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "How‑To + Reference"
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

owner: "KFM Core · Reliability Engineering"

classification: "Public"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"

immutability_status: "mutable-plan"
doc_uuid: "urn:kfm:doc:telemetry:etl-energy-co2:v11.2.6"
semantic_document_id: "kfm-telemetry-etl-energy-co2-v11.2.6"
event_source_id: "ledger:kfm:doc:telemetry:etl-energy-co2:v11.2.6"
doc_integrity_checksum: "<sha256>"

commit_sha: "<latest-commit-hash>"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.6.md@v11.2.6"
  - "docs/standards/telemetry_standards.md@v11.2.6"

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
  - "layout-normalization"

ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "unverified-architectural-claims"
  - "narrative-fabrication"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
---

# ⚡ KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)

## 📘 Overview

> **Purpose**  
> Provide a governed, copy‑paste pattern to:
> 1) measure **energy (J)** plus **network/disk bytes**,  
> 2) compute an auditable **CO₂ estimate (kg)** using a declared emission factor, and  
> 3) persist a per‑run telemetry summary into a **STAC Item** with an attached **PROV JSON‑LD** asset—while emitting **OpenTelemetry semantic metrics** for centralized collection.

This pattern is designed for **ETL jobs** in the KFM pipeline:
ETL → STAC/DCAT/PROV catalogs → graph ingestion → APIs → UI/Focus Mode.

### What this is (and is not)

- ✅ **Metadata + observability layer** for ETL runs (energy/carbon/I/O + provenance)
- ✅ Compatible with CI‑driven workflows (deterministic unit conversions; explicit config)
- ❌ Not a full carbon lifecycle model (no Scope‑3 inference; no supplier‑verified accounting)
- ❌ Not a promise of per‑process energy attribution (most sources are **host‑level**)

### Metrics (OTel semantic names)

This doc standardizes on these OpenTelemetry metric names (units in UCUM):
- `hw.host.energy` (J) — host energy (monotonic counter; add deltas)
- `process.network.io` (By) — bytes transferred
- `process.disk.io` (By) — bytes transferred

> Note: The relevant OpenTelemetry semantic conventions are still evolving; keep metric naming behind a configuration toggle if your collectors require a migration period.

### Quickstart (Python)

~~~bash
pip install \
  opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp \
  pystac python-dateutil

# Optional (recommended for bytes counters):
pip install psutil
~~~

~~~python
"""
KFM — ETL Energy & CO₂ Telemetry (OpenTelemetry · STAC · PROV)

Drop-in goals:
- Measure energy (J) with a pluggable reader (RAPL/IPMI/cloud APIs); compute deltas
- Measure process/network/disk bytes (psutil if available)
- Convert J → kWh → kg CO₂ using a declared emission factor + source string
- Emit OpenTelemetry semantic metrics: hw.host.energy, process.network.io, process.disk.io
- Persist a roll-up into STAC Item properties.telemetry and attach PROV JSON-LD as an asset

This snippet is intentionally small and offline-friendly.
"""

from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

import pystac
from dateutil.parser import isoparse

from opentelemetry import metrics, trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.trace import TracerProvider as SDKTracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

try:
    import psutil  # optional
except Exception:
    psutil = None


# ----------------------------
# Helpers
# ----------------------------
JOULES_PER_KWH = 3_600_000.0

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def joules_to_kwh(j: float) -> float:
    return float(j) / JOULES_PER_KWH

def safe_mkdir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def read_intel_rapl_energy_joules() -> Optional[float]:
    """
    Minimal Linux Intel RAPL reader:
    sums /sys/class/powercap/intel-rapl:*/energy_uj (microjoules) → joules.

    Returns None if not available.
    """
    root = Path("/sys/class/powercap")
    if not root.exists():
        return None

    total_uj = 0
    found = False
    for fp in root.glob("intel-rapl:*/energy_uj"):
        try:
            total_uj += int(fp.read_text().strip())
            found = True
        except Exception:
            continue

    if not found:
        return None

    return total_uj / 1_000_000.0  # microjoules → joules


@dataclass(frozen=True)
class Snapshot:
    t: float
    energy_j: Optional[float]
    net_sent: Optional[int]
    net_recv: Optional[int]
    disk_read: Optional[int]
    disk_write: Optional[int]

def take_snapshot() -> Snapshot:
    energy_j = read_intel_rapl_energy_joules()

    if psutil:
        net = psutil.net_io_counters()
        disk = psutil.disk_io_counters()
        return Snapshot(
            t=time.time(),
            energy_j=energy_j,
            net_sent=int(getattr(net, "bytes_sent", 0)),
            net_recv=int(getattr(net, "bytes_recv", 0)),
            disk_read=int(getattr(disk, "read_bytes", 0)),
            disk_write=int(getattr(disk, "write_bytes", 0)),
        )

    return Snapshot(
        t=time.time(),
        energy_j=energy_j,
        net_sent=None,
        net_recv=None,
        disk_read=None,
        disk_write=None,
    )

def delta(a: Optional[int | float], b: Optional[int | float]) -> Optional[float]:
    if a is None or b is None:
        return None
    return float(b) - float(a)


# ----------------------------
# OpenTelemetry bootstrap
# ----------------------------
def init_otel(service_name: str, service_version: str) -> None:
    resource = Resource.create({"service.name": service_name, "service.version": service_version})

    metric_exporter = OTLPMetricExporter()  # configure via OTEL_EXPORTER_OTLP_ENDPOINT
    metric_reader = PeriodicExportingMetricReader(metric_exporter, export_interval_millis=5000)
    metrics.set_meter_provider(MeterProvider(resource=resource, metric_readers=[metric_reader]))

    trace.set_tracer_provider(SDKTracerProvider(resource=resource))
    trace.get_tracer_provider().add_span_processor(SimpleSpanProcessor(OTLPSpanExporter()))


# ----------------------------
# Core recorder
# ----------------------------
@dataclass
class TelemetryConfig:
    run_id: str
    job_type: str
    emission_factor_kg_per_kwh: float
    emission_factor_source: str  # REQUIRED for audits
    host_hw_id: str
    host_hw_name: str
    process_pid: int

@dataclass
class TelemetryResult:
    run_id: str
    started_at: str
    ended_at: str
    duration_seconds: float

    energy_joules: Optional[float]
    energy_kwh: Optional[float]
    co2_kg: Optional[float]

    bytes_sent: Optional[float]
    bytes_received: Optional[float]
    disk_bytes_read: Optional[float]
    disk_bytes_write: Optional[float]

    emission_factor_kg_per_kwh: float
    emission_factor_source: str


class TelemetryRecorder:
    def __init__(self, cfg: TelemetryConfig):
        self.cfg = cfg
        self.start = None
        self.end = None
        self.started_at = None
        self.ended_at = None

        meter = metrics.get_meter("kfm.telemetry.energy", "0.1.0")
        self.energy_counter = meter.create_counter("hw.host.energy", unit="J", description="Host energy (joules)")
        self.net_counter = meter.create_counter("process.network.io", unit="By", description="Process network bytes transferred")
        self.disk_counter = meter.create_counter("process.disk.io", unit="By", description="Process disk bytes transferred")

        self.tracer = trace.get_tracer("kfm.telemetry.tracer", "0.1.0")

    def __enter__(self) -> "TelemetryRecorder":
        self.started_at = utc_now_iso()
        self.start = take_snapshot()
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.ended_at = utc_now_iso()
        self.end = take_snapshot()

    def finalize(self) -> TelemetryResult:
        if not self.start or not self.end or not self.started_at or not self.ended_at:
            raise RuntimeError("TelemetryRecorder must be used as a context manager")

        dur = float(self.end.t - self.start.t)

        d_energy = delta(self.start.energy_j, self.end.energy_j)
        d_sent = delta(self.start.net_sent, self.end.net_sent)
        d_recv = delta(self.start.net_recv, self.end.net_recv)
        d_read = delta(self.start.disk_read, self.end.disk_read)
        d_write = delta(self.start.disk_write, self.end.disk_write)

        # Guardrails
        if d_energy is not None and d_energy < 0:
            d_energy = None  # counter wrap or reader mismatch
        for vname, v in (("sent", d_sent), ("recv", d_recv), ("read", d_read), ("write", d_write)):
            if v is not None and v < 0:
                raise ValueError(f"Negative byte delta detected ({vname}={v}). Check counter source.")

        energy_kwh = joules_to_kwh(d_energy) if d_energy is not None else None
        co2_kg = (energy_kwh * self.cfg.emission_factor_kg_per_kwh) if energy_kwh is not None else None

        # Emit OTel metrics as deltas (counters)
        if d_energy is not None:
            self.energy_counter.add(
                d_energy,
                {"hw.id": self.cfg.host_hw_id, "hw.name": self.cfg.host_hw_name},
            )

        if d_sent is not None:
            self.net_counter.add(d_sent, {"process.pid": self.cfg.process_pid, "network.io.direction": "transmit"})
        if d_recv is not None:
            self.net_counter.add(d_recv, {"process.pid": self.cfg.process_pid, "network.io.direction": "receive"})

        if d_read is not None:
            self.disk_counter.add(d_read, {"process.pid": self.cfg.process_pid, "disk.io.direction": "read"})
        if d_write is not None:
            self.disk_counter.add(d_write, {"process.pid": self.cfg.process_pid, "disk.io.direction": "write"})

        # Emit a trace span with roll-up attributes for correlation
        with self.tracer.start_as_current_span(
            "etl.job",
            attributes={"job.id": self.cfg.run_id, "job.type": self.cfg.job_type},
        ) as span:
            span.set_attribute("telemetry.duration_seconds", dur)
            if d_energy is not None:
                span.set_attribute("telemetry.energy_joules", d_energy)
                span.set_attribute("telemetry.energy_kwh", energy_kwh)
            if co2_kg is not None:
                span.set_attribute("telemetry.co2_kg", co2_kg)
                span.set_attribute("telemetry.emission_factor_kg_per_kwh", self.cfg.emission_factor_kg_per_kwh)
                span.set_attribute("telemetry.emission_factor_source", self.cfg.emission_factor_source)
            if d_sent is not None:
                span.set_attribute("telemetry.bytes_sent", d_sent)
            if d_recv is not None:
                span.set_attribute("telemetry.bytes_received", d_recv)

        return TelemetryResult(
            run_id=self.cfg.run_id,
            started_at=self.started_at,
            ended_at=self.ended_at,
            duration_seconds=dur,
            energy_joules=d_energy,
            energy_kwh=energy_kwh,
            co2_kg=co2_kg,
            bytes_sent=d_sent,
            bytes_received=d_recv,
            disk_bytes_read=d_read,
            disk_bytes_write=d_write,
            emission_factor_kg_per_kwh=self.cfg.emission_factor_kg_per_kwh,
            emission_factor_source=self.cfg.emission_factor_source,
        )


# ----------------------------
# Persistence: STAC + PROV JSON-LD asset
# ----------------------------
def persist_to_stac(item_path: Path, out_assets_dir: Path, result: TelemetryResult) -> Dict[str, Any]:
    """
    Writes:
      - STAC Item properties.telemetry (roll-up summary)
      - Asset: telemetry-prov (PROV JSON-LD)
      - Optional: telemetry-json (raw roll-up summary)
    """
    safe_mkdir(out_assets_dir)

    item = pystac.Item.from_file(str(item_path))

    # Persist roll-up
    item.properties.setdefault("telemetry", {})
    item.properties["telemetry"].update({
        "run_id": result.run_id,
        "started_at": result.started_at,
        "ended_at": result.ended_at,
        "duration_seconds": result.duration_seconds,

        "energy_joules": result.energy_joules,
        "energy_kwh": result.energy_kwh,
        "co2_kg": result.co2_kg,

        "bytes_sent": result.bytes_sent,
        "bytes_received": result.bytes_received,
        "disk_bytes_read": result.disk_bytes_read,
        "disk_bytes_write": result.disk_bytes_write,

        "emission_factor_kg_per_kwh": result.emission_factor_kg_per_kwh,
        "emission_factor_source": result.emission_factor_source,

        "recorded_at": utc_now_iso(),
    })

    # Write raw telemetry JSON (optional but useful for audits)
    telemetry_json_name = f"{result.run_id}-telemetry.json"
    telemetry_json_path = out_assets_dir / telemetry_json_name
    telemetry_json_path.write_text(json.dumps(item.properties["telemetry"], ensure_ascii=False, indent=2), encoding="utf-8")

    # PROV JSON-LD (minimal, explicit prov:Activity + prov:Entity)
    prov_name = f"{result.run_id}-telemetry-prov.jsonld"
    prov_path = out_assets_dir / prov_name

    prov_doc = {
        "@context": {
            "prov": "http://www.w3.org/ns/prov#",
            "xsd": "http://www.w3.org/2001/XMLSchema#",
            "kfm": "urn:kfm:",
        },
        "@graph": [
            {
                "@id": f"urn:kfm:run:{result.run_id}",
                "@type": "prov:Activity",
                "prov:startedAtTime": {"@value": result.started_at, "@type": "xsd:dateTime"},
                "prov:endedAtTime": {"@value": result.ended_at, "@type": "xsd:dateTime"},
                "kfm:job_type": "etl",
            },
            {
                "@id": f"urn:kfm:entity:telemetry:{result.run_id}",
                "@type": "prov:Entity",
                "prov:wasGeneratedBy": {"@id": f"urn:kfm:run:{result.run_id}"},
                "prov:value": item.properties["telemetry"],
            },
        ]
    }
    prov_path.write_text(json.dumps(prov_doc, ensure_ascii=False, indent=2), encoding="utf-8")

    # Attach assets with stable keys
    item.add_asset("telemetry-json", pystac.Asset(
        href=str(telemetry_json_path.as_posix()),
        media_type="application/json",
        roles=["metadata"],
        title="ETL telemetry roll-up (JSON)"
    ))
    item.add_asset("telemetry-prov", pystac.Asset(
        href=str(prov_path.as_posix()),
        media_type="application/ld+json",
        roles=["metadata", "provenance"],
        title="ETL telemetry provenance (PROV JSON-LD)"
    ))

    item.save_object(include_self_link=False)
    return {"stac_item": str(item_path), "telemetry_json": str(telemetry_json_path), "telemetry_prov": str(prov_path)}


# ----------------------------
# Example usage
# ----------------------------
if __name__ == "__main__":
    init_otel(service_name="kfm-etl", service_version="v11.2.6")

    cfg = TelemetryConfig(
        run_id=f"etl-{utc_now_iso().replace(':','').replace('-','')}",
        job_type="example-etl",
        emission_factor_kg_per_kwh=0.40,  # EXAMPLE ONLY — configure per region/provider
        emission_factor_source="TBD (document utility / regional grid factor source)",
        host_hw_id=os.getenv("KFM_HW_ID", "host-unknown"),
        host_hw_name=os.getenv("KFM_HW_NAME", "kfm-node"),
        process_pid=os.getpid(),
    )

    with TelemetryRecorder(cfg) as rec:
        # Simulate work
        time.sleep(1.0)

    result = rec.finalize()

    # Persist into a STAC item (adjust these paths to your repo layout)
    item_path = Path("data/stac/items/sample-item.json")
    assets_dir = Path("mcp/runs") / result.run_id / "assets"
    persist_to_stac(item_path=item_path, out_assets_dir=assets_dir, result=result)
~~~

## 🗂️ Directory Layout

~~~text
📂 docs/
├── 📂 telemetry/
│   ├── 📄 etl_energy_co2.md                 # This document (canonical home)
│   └── 📄 README.md                         # Telemetry index (if present)
│
├── 📂 standards/
│   ├── 📄 telemetry_standards.md            # Repo standard for telemetry naming & schemas
│   ├── 📂 governance/
│   │   └── 📄 ROOT-GOVERNANCE.md
│   ├── 📂 faircare/
│   │   └── 📄 FAIRCARE-GUIDE.md
│   └── 📂 sovereignty/
│       └── 📄 INDIGENOUS-DATA-PROTECTION.md
│
📂 mcp/
└── 📂 runs/
    └── 📂 <run_id>/
        └── 📂 assets/
            ├── 📄 <run_id>-telemetry.json         # Roll-up (optional but recommended)
            └── 📄 <run_id>-telemetry-prov.jsonld  # PROV JSON-LD (auditable)

📂 data/
└── 📂 stac/
    └── 📂 <collection>/
        └── 📂 items/
            └── 📄 <item_id>.geojson               # STAC Item embeds telemetry + links assets
~~~

## 🧱 Architecture

### Data flow (recommended)

1. **Measure**:
   - Host energy counter (J) via a pluggable reader (RAPL/IPMI/cloud power APIs)
   - Network/disk byte counters (By) from OS counters (e.g., `psutil`)
2. **Compute**:
   - `energy_kwh = energy_joules / 3_600_000`
   - `co2_kg = energy_kwh * emission_factor_kg_per_kwh`
3. **Emit (OTel)**:
   - Send metrics and a correlating span via OTLP for centralized observability
4. **Persist (catalog)**:
   - Store a stable roll‑up inside the STAC Item (`properties.telemetry.*`)
   - Attach a PROV JSON‑LD asset for audits / lineage ingestion

### Determinism contract

- Unit conversions MUST be pure and deterministic.
- All configurable constants (emission factor + source) MUST be passed via configuration (env/config/CLI), not hardcoded.
- Telemetry persistence MUST not mutate any STAC fields other than the defined telemetry extension keys + asset links.

## 📦 Data & Metadata

### Telemetry roll-up shape (recommended)

~~~json
{
  "run_id": "etl-20251216T000000Z",
  "started_at": "2025-12-16T00:00:00Z",
  "ended_at": "2025-12-16T00:05:12Z",
  "duration_seconds": 312.0,

  "energy_joules": 55000000.0,
  "energy_kwh": 15.2777777778,
  "co2_kg": 6.1111111111,

  "bytes_sent": 12345678.0,
  "bytes_received": 2222222.0,
  "disk_bytes_read": 987654.0,
  "disk_bytes_write": 12345.0,

  "emission_factor_kg_per_kwh": 0.40,
  "emission_factor_source": "regional grid factor (utility disclosure / verified source)",
  "recorded_at": "2025-12-16T00:05:12Z"
}
~~~

### Required audit fields

- `emission_factor_kg_per_kwh` MUST be recorded.
- `emission_factor_source` MUST be recorded (human-readable string sufficient).
- If energy measurements are estimated (not sensor-based), record the method in a separate field (e.g., `energy_method`).

## 🌐 STAC, DCAT & PROV Alignment

### STAC Item embedding

- STAC Item → `properties.telemetry.*` (roll-up)
- Assets:
  - `telemetry-json` (optional) → JSON roll-up for audits
  - `telemetry-prov` (required for governed runs) → PROV JSON‑LD

### PROV JSON‑LD minimum

- `prov:Activity` identified by `run_id`
- `prov:Entity` representing the telemetry record
- `prov:wasGeneratedBy` linking telemetry entity → run activity

### DCAT note

This pattern is STAC-first. If you publish telemetry as a distributable artifact, register it as a `dcat:Distribution` in your DCAT layer (implementation depends on your KFM-DCAT packaging rules).

## 🧪 Validation & CI/CD

Minimum checks for a governed ETL job that adopts this pattern:

- **Schema checks**
  - Telemetry payload validates against the repo telemetry schema (if enforced)
  - PROV JSON‑LD parses as JSON‑LD and includes required `prov:*` nodes
- **Safety checks**
  - No secrets/credentials appear in telemetry outputs
  - No PII is introduced by default (hostnames/IPs/usernames must be avoided or hashed)
- **Numerical sanity checks**
  - All byte deltas are non-negative
  - Energy delta is non-negative (or treated as unavailable)
  - CO₂ only computed when energy is known and emission factor is declared

## ⚖ FAIR+CARE & Governance

- **Honesty in reporting:** CO₂ is an *estimate* based on the declared emission factor and measurement scope (host-level vs job-level).
- **Data minimization:** Do not store raw hostnames, IPs, usernames, or cloud instance IDs unless governance explicitly allows it. Prefer stable internal IDs.
- **Sovereignty awareness:** Telemetry can indirectly expose sensitive operational context (locations, schedules). Apply masking/generalization where required by policy.
- **Traceability:** Always record the emission factor source and the measurement method so audits can reproduce the computation.

### 🔗 Navigation

- 📘 Standards → `docs/standards/README.md`
- 📁 Telemetry Docs → `docs/telemetry/README.md`
- 🛡️ Governance Charter → `docs/standards/governance/ROOT-GOVERNANCE.md`

## 🕰️ Version History

Version | Date | Notes
---|---|---
v11.2.6 | 2025-12-16 | Initial governed ETL energy + CO₂ telemetry pattern (OTel metrics + STAC embedding + PROV JSON‑LD asset)