---
title: "🌪️ Kansas Frontier Matrix — HRRR Zarr Windowing & Subsetting Pattern (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/atmospheric/hrrr/windowing/README.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Working Group · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Enforced"

doc_kind: "Pipeline Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/hrrr-windowing-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/hrrr-windowing-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.5"
---

<div align="center">

# 🌪️ **HRRR Zarr Windowing & Subsetting Pattern**  
**Deterministic Spatial Windowing · Dask Distributed · STAC Processing Metadata**

`docs/pipelines/atmospheric/hrrr/windowing/README.md`

</div>

---

## 📘 Overview

This pattern specifies how **HRRR Zarr** datasets are lazily windowed, subsetted, and statically recorded for provenance inside the **Kansas Frontier Matrix (KFM)**.

The technique:

- Minimizes compute and I/O for **CONUS-scale** Zarr stores  
- Preserves **determinism and replayability**  
- Avoids cross-run drift by **run-state keys**  
- Emits complete `processing:subset` metadata into downstream **STAC Items** and derived **DCAT** catalogs  

Windowing is done strictly by:

- **Dataset version** (HRRR release / Zarr snapshot)  
- **Forecast cycle hour** (init or valid time, explicitly configured)  
- **Spatial selector**: bbox or polygon (Kansas AOIs, basins, counties, etc.)  
- **Explicit run-state guardrails** for idempotency

All operations use **lazy** execution through **Dask Distributed**, with optional cluster scheduling.

---

## 🧭 Goals

| Goal                  | Description                                                |
|-----------------------|------------------------------------------------------------|
| Deterministic subsets | Same inputs → same outputs, byte-for-byte identical.      |
| Minimal compute       | Load only chunks intersecting AOI.                        |
| Provenance rich       | STAC updated with clear `processing:subset` metadata.     |
| Idempotent            | Duplicate runs skipped via run-state keying.             |
| Scalable              | Handles CONUS Zarr with cheap, selective I/O.             |

---

## 🧱 Architecture Summary

### 1️⃣ Lazy Zarr Opening

- Always open HRRR as **consolidated Zarr**.  
- No eager computations; everything stays lazy until:

  - `.compute()` is explicitly invoked, or  
  - a write to disk (e.g., `to_zarr`, `to_netcdf`, `to_parquet`) is triggered.

### 2️⃣ Spatial Windowing Modes

Two supported selectors (no ad-hoc modes):

| Selector | Use Case                                          |
|----------|----------------------------------------------------|
| **bbox** | Counties, coarse Kansas AOI, static tiles.         |
| **polygon** | Basins, HRUs, Story Node AOIs, sensitive overlays. |

Selectors MUST be:

- Config-driven (YAML/JSON), not embedded as “magic numbers” in code.  
- Referenced in STAC `processing:subset.selectors`.

### 3️⃣ Run-State Guardrail (Idempotency)

Each run MUST compute a **run-state key**:

```text
key = sha256({dataset_version, hour, selector_type, selector_geom, variables})
```

This guardrail prevents duplicate subsetting and ensures deterministic replays:

- Run-state is stored at:

  ```text
  data/run_state/hrrr_window/<sha256>.json
  ```

- If the file already exists with a matching hash → the run MUST **skip** or explicitly **enter replay mode** (for testing).

### 4️⃣ Subsetting Stats (Preflight)

Before heavy compute:

- Derive:

  - chunk structure  
  - variable shapes  
  - estimated byte footprint (`nbytes`)  
  - lon/lat ranges  
  - variable list  

- Save under the run-state JSON for inspection and reproducibility.

### 5️⃣ STAC Output

Generated STAC Items MUST include a `processing:subset` block that records:

- Selector type & parameters  
- Dataset version & Zarr store path  
- Run-state key  
- Variables included  
- Shapes/chunks/estimated bytes  

---

## 🧪 Reference Implementation (Pattern Sketch)

```python
from dask.distributed import Client
import xarray as xr
import hashlib, json, os
from pathlib import Path

client = Client()  # or preconfigured cluster

# Inputs (normally config-driven)
zarr_url = os.environ.get("KFM_HRRR_ZARR_URL", "s3://noaa-hrrr-pds/hrrr.zarr")
dataset_version = os.environ.get("KFM_HRRR_VERSION", "hrrr-v4.1")
hour_iso = "2025-12-08T00:00:00Z"
bbox = (-102.1, 36.9, -94.6, 40.1)  # Kansas-ish

variables = ["t2m", "u10", "v10"]  # example variable list

# Run-state key (idempotency)
payload = json.dumps(
    {
        "dataset_version": dataset_version,
        "hour": hour_iso,
        "bbox": bbox,
        "variables": variables,
    },
    sort_keys=True,
).encode("utf-8")

key = hashlib.sha256(payload).hexdigest()
flag_path = Path("data/run_state/hrrr_window") / f"{key}.json"
flag_path.parent.mkdir(parents=True, exist_ok=True)

if flag_path.exists():
    raise SystemExit(f"[KFM] HRRR window already processed for key={key}; idempotent skip.")

# 1) Open lazily
ds = xr.open_zarr(
    zarr_url,
    consolidated=True,
    storage_options={"anon": True},
)

# 2) Time selection (init/valid should be explicit in config)
sub = ds.sel(time=hour_iso, method="nearest")

lon_name = "longitude" if "longitude" in sub.coords else "lon"
lat_name = "latitude" if "latitude" in sub.coords else "lat"

lon_min, lat_min, lon_max, lat_max = bbox

# 3) Spatial slice
subset = sub[variables].sel(
    {
        lat_name: slice(lat_min, lat_max),
        lon_name: slice(lon_min, lon_max),
    }
)

# 4) Stats without full compute
stats = {
    "variables": sorted(list(subset.data_vars)),
    "coords": {
        "lon_range": [
            float(subset[lon_name].min()),
            float(subset[lon_name].max()),
        ],
        "lat_range": [
            float(subset[lat_name].min()),
            float(subset[lat_name].max()),
        ],
    },
    "chunks": (
        {k: list(v) for k, v in subset.chunks.items()}
        if subset.chunks
        else {}
    ),
    "shape": {v.name: list(v.shape) for v in subset.data_vars.values()},
    "nbytes_est": int(getattr(subset, "nbytes", 0)) or None,
    "key": key,
    "dataset_version": dataset_version,
    "hour_iso": hour_iso,
    "bbox": list(bbox),
}

flag_path.write_text(json.dumps({"stats": stats}, indent=2))
```

---

## 🧬 STAC `processing:subset` Metadata Block

Example of the **required** STAC `properties.processing:subset` structure:

```json
{
  "processing:subset": {
    "technique": "window-by-bbox",
    "dataset": "HRRR",
    "dataset_version": "hrrr-v4.1",
    "source_store": "s3://noaa-hrrr-pds/hrrr.zarr",
    "run_state_key": "<sha256>",
    "forecast_hour": "2025-12-08T00:00:00Z",
    "selector": {
      "type": "bbox",
      "value": [-102.1, 36.9, -94.6, 40.1]
    },
    "variables": ["t2m", "u10", "v10"],
    "shape": { "t2m": [121, 181] },
    "chunks": {
      "t2m": [[31, 31, 31, 28], [32, 32, 32, 32, 53]]
    },
    "bytes:estimated": 123456789,
    "provenance": {
      "software": {
        "xarray": ">=2024.6",
        "dask": "distributed>=2024.6"
      },
      "selectors": {
        "time": "nearest",
        "spatial": "bbox"
      }
    }
  }
}
```

Pattern rules:

- `run_state_key` MUST match the on-disk run-state JSON.  
- `selector.type` MUST be one of: `"bbox"`, `"polygon"`.  
- All `processing:subset` blocks MUST be **JSON-schema-valid** against:

  - `schemas/telemetry/hrrr-windowing-v2.json` (or a dedicated STAC extension schema).

---

## 🔍 Validation Requirements

| Layer        | Validation                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Pre-ingest   | Confirm dataset version, HRRR Zarr structure, and consolidated metadata.   |
| Windowing    | lon/lat monotonicity; AOI coverage; missing tiles < configured threshold.  |
| STAC         | STAC schema + `processing:subset` JSON Schema validation.                  |
| Provenance   | Run-state checksum exists and matches STAC `run_state_key`.                |
| Telemetry    | Energy/carbon + runtime metrics recorded per run (via telemetry schema).   |

Validation SHOULD be implemented as part of the **event-driven deterministic ingest** pattern and wired into CI.

---

## 🗂️ Directory Layout

```text
docs/
  pipelines/
    atmospheric/
      hrrr/
        windowing/
          README.md                  # ← This file (pattern guide)
          examples/
            bbox-basic.md           # Example YAML → bbox windowing run
            polygon-windowing.md    # Polygon-based AOI windowing
            stac-subset-example.json
          tests/
            test-windowing-shapes.py
            test-stac-provenance.py
            fixtures/
```

Associated code and data layout (logical):

```text
src/
  pipelines/
    atmospheric/
      hrrr/
        windowing/
          __init__.py
          run_window.py
          run_state.py
          stac_emit.py
          config.py

data/
  run_state/
    hrrr_window/
      <sha256>.json
  atmospheric/
    hrrr/
      zarr_index/...
      subsets/...

schemas/
  telemetry/
    hrrr-windowing-v2.json
```

---

## 🧮 Integration with Event-Driven Pipelines

This pattern is typically invoked within:

- Event-driven pipelines (S3 notifications, topic messages).  
- Batch re-windowing jobs (backfill or reprocessing).

Integration rules:

- Idempotency MUST be enforced by `run_state_key`.  
- WAL entries MUST be written prior to final writes into `data/atmospheric/hrrr/subsets/`.  
- STAC Items MUST be generated only after successful validation & telemetry logging.  

See also:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`  
- `docs/pipelines/reliability/tests/etl-determinism-suite.md`

---

## 🏁 Version History

| Version | Date       | Notes                                                       |
|--------:|------------|-------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Initial governed pattern under KFM-MDP v11.2.5.            |
| v11.2.3 | 2025-11-30 | Internal atmospheric ETL alignment draft.                  |

---

## 🛡️ Governance Footer

This document is governed by:

- **Atmospheric Working Group**  
- **FAIR+CARE Council**  
- **KFM Documentation & Pipelines Standards**

All modifications MUST:

- Maintain `markdown_protocol_version` alignment.  
- Update `doc_integrity_checksum`, `commit_sha`, and `previous_version_hash`.  
- Pass **docs-lint**, **schema-lint**, and **telemetry-lint** CI checks.

Energy & carbon telemetry:

- Attached via `telemetry_ref`, following `energy_schema` and `carbon_schema`.  
- MUST be recorded for all production windowing runs to support sustainability SLOs.

<div align="center">

🌪️ **Kansas Frontier Matrix — HRRR Windowing Pattern**  

[📘 Docs Root](../../../README.md) ·  
[🌤️ Atmospheric Pipelines Index](../README.md) ·  
[⚖️ Root Governance](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
