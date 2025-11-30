---
title: "🌬️ KFM v11 — AirNow Ingest, Time Normalization & Hourly Storage Layer (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/air/airnow/ingest/README.md"
version: "v11.2.3"
last_updated: "2025-11-29"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospherics Working Group · FAIR+CARE Council"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/airnow-ingest-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/airnow-ingest-v11.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"

status: "Active / Enforced"
doc_kind: "Pipeline Module"
intent: "airnow-ingest-normalization-and-hourly-storage"
fair_category: "F1-A1-I2-R3"
care_label: "CARE · Responsible Environmental Data Handling"
classification: "Public"
sensitivity: "Low"
immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "United States · Kansas"
---

<div align="center">

# 🌬️ **KFM v11 — AirNow Ingest, Time Normalization & Hourly Storage Layer**  
`docs/pipelines/air/airnow/ingest/README.md`

**Purpose**  
Define the authoritative, reproducible, FAIR+CARE-aligned **AirNow ingestion standard** for KFM, including:  
- **UTC time normalization & DST-safe timestamp handling**, and  
- **Hourly ingestion cadence & cloud-optimized storage (COG/Zarr)**.  

This module ensures KFM-wide **temporal integrity**, **cross-dataset join safety**, **DST clarity**,  
**cloud-optimized storage**, and **provenance-correct timestamp lineage** for AirNow air-quality datasets.

</div>

---

## 📘 1. Overview

AirNow provides authoritative U.S. air-quality observations, but:

- Timestamps can be **local standard time (LST)**, ambiguous wall-clock time, or UTC.  
- Hourly products (Hourly Data, HourlyObs) arrive with **specific sub-hourly cadence**.  
- Raw files are not directly optimized for cloud-native analytics (COG/Zarr).

In KFM, **temporal correctness and storage efficiency are mandatory** for:

- Atmospheric modeling and forecasting  
- Hydrology and hazards joins (e.g., floods, fire, smoke)  
- Epidemiology and exposure analysis  
- Cross-agency, multi-decade environmental studies  

This module is the **governed standard** for:

- AirNow ingest → canonical UTC normalization  
- Full offset/DST preservation and explicit time semantics  
- Deterministic hourly ingestion cadence & triggers  
- Cloud-optimized storage (COG/Zarr) and STAC/DCAT metadata  
- OpenLineage provenance and telemetry (energy, carbon, anomalies)

---

## 🧩 2. Canonical Timestamp Schema (v11.2.x)

Every AirNow observation MUST include the following canonical fields:

| Field                   | Description                                           | Example                          |
|-------------------------|-------------------------------------------------------|----------------------------------|
| `observed_time_utc`     | Canonical ISO-8601 UTC timestamp                     | `2025-11-28T14:00:00Z`          |
| `station_local_time`    | Reported local wall-clock time (verbatim string)     | `"2025-11-28 08:00"`            |
| `utc_offset_minutes`    | Offset applied to derive UTC (minutes)               | `-360`                          |
| `is_dst`                | Explicit DST status (`true`/`false`, never inferred) | `false`                         |
| `time_basis`            | `reported_LST`, `reported_UTC`, or `unknown`         | `"reported_LST"`                |
| `period_alignment`      | `period_begin` or `period_end`                       | `"period_begin"`                |
| `source_basis`          | How the time arrived from AirNow                     | `"AirNow-LST-Hourly"`           |
| `ingest_method_version` | Deterministic ingest version identifier              | `"v11.2.3"`                     |

### 2.1 Timestamp Rules

- **DST MUST be explicit** via `is_dst`, not inferred from the calendar alone.  
- **Offsets MUST be stored** using `utc_offset_minutes` (no lossy conversions).  
- AirNow hourly feeds are treated as **`period_begin`**; any deviation is **flagged and logged**.  
- Ambiguous inputs MUST be represented with `time_basis: "unknown"` and a **governance flag**.  
- `observed_time_utc` is the sole canonical time basis for joins; local fields are retained for reconstruction.

---

## 🔁 3. Ingest Workflow (v11.2)

~~~mermaid
flowchart TD
    A["Raw AirNow Feeds\n(Hourly Data + HourlyObs)"] --> B["Time Basis Detection\n(LST vs UTC vs ambiguous)"]
    B --> C["UTC Normalization\n(apply offset + DST rules)"]
    C --> D["Local Reconstruction\n(station time + offset + DST flag)"]
    D --> E["Period Alignment Enforcement\n(hourly period_begin)"]
    E --> F["Validation Layer\n(schema + GE + CARE checks)"]
    F --> G["Cloud-Optimized Storage\n(COG · Zarr · GeoParquet)"]
    G --> H["STAC/DCAT Decoration\n(temporal extents + metadata)"]
    H --> I["Lineage & Telemetry\n(OpenLineage + energy/carbon metrics)"]
    I --> J["KFM Lake Output\n(reusable for downstream air pipelines)"]
~~~

**Invariants:**

- Every output record has exactly one canonical `observed_time_utc`.  
- Local times, offsets, and DST flags are preserved as **first-class fields**.  
- Period alignment is standardized to `period_begin` for hourly AirNow outputs.  
- Lineage is recorded for every ingest run, including energy/carbon.

---

## ⏱️ 4. Update Cadence & Trigger Rules

AirNow hourly feeds arrive on **predictable sub-hourly offsets**. KFM normalizes this into deterministic ingestion windows.

### 4.1 Data Arrival Windows

| AirNow Product   | Expected Arrival       | Release Window       | KFM Ingest Trigger |
|------------------|------------------------|----------------------|--------------------|
| Hourly Data File | ~ :25 & :55 past hour  | Data for previous 48h| Ingest at **:00**  |
| Hourly AQ Obs    | ~ :35 past hour        | Previous hour obs    | Ingest at **:40**  |

**Guiding Rules:**

- Ingest only after the **latest complete hour** is available.  
- For resilience, re-ingest a **48-hour rolling window** idempotently.  
- Use queue-based retriers (e.g., 3-stage exponential backoff) with monotonic clock checks.  
- All schedules are explicitly recorded in pipeline specs (not hard-coded in random scripts).

---

## ☁️ 5. Cloud-Optimized Storage Standards

### 5.1 Required Formats

| Data Type          | Primary Format | Fallback | Notes                                  |
|--------------------|----------------|----------|----------------------------------------|
| Hourly AQ rasters  | **COG**        | GeoTIFF  | Band-level overviews enabled           |
| N-D time series    | **Zarr**       | Parquet  | Chunking optimized for object storage  |
| Station time series| **GeoParquet** | CSV      | For station-wise analytics & joins     |

### 5.2 Zarr Chunking Policy

- Target **uncompressed chunk size**: ~1–4 MB.  
- Chunk along **time** and **station** axes for typical access patterns.  
- Avoid pathological chunking (e.g., tiny chunks or overly large monolithic chunks).

### 5.3 Promotion Gate

1. **Raw** → `data/raw/air/airnow/YYYY/MM/DD/`  
2. **Validated** → `data/work/air/airnow/hourly/`  
3. **Optimized** → COG / Zarr / GeoParquet tiles  
4. **Catalogued** → STAC Item & Collection entries  
5. **Governed** → Promotion ledger & PROV journals  
6. **Published** → `/data/stac/air/airnow/collections/...`

Rollback follows WAL + lineage bundle restoration.

---

## 🧪 6. Validation & Quality Rules

### 6.1 Temporal & Structural Validation (Great Expectations / Schema)

- **Completeness:**  
  - `observed_time_utc`, `station_local_time`, `utc_offset_minutes`, `is_dst`, `period_alignment` present.  
- **Consistency:**  
  - `observed_time_utc` is valid ISO-8601 UTC.  
  - `utc_offset_minutes` matches station’s timezone / DST rules.  
  - `is_dst` consistent with date and offset.  
  - `period_alignment == "period_begin"` for hourly products.  
- **Schema:**  
  - All records validate against:
    - `schemas/airnow-timestamps-v11.json`  
    - `schemas/airnow-ingest-v11.json`  

### 6.2 Environmental & FAIR+CARE Checks

- Ensure values fall within domain-specific pollutant ranges.  
- Apply missingness thresholds per pollutant.  
- Verify licensing, usage terms, and absence of unexpected sensitive fields.  
- Confirm exports align with **Responsible Environmental Data Handling**.

---

## 📦 7. Output Formats, STAC & DCAT

### 7.1 GeoParquet / Zarr / COG

Core columns:

- `observed_time_utc`  
- `station_local_time`  
- `utc_offset_minutes`  
- `is_dst`  
- `period_alignment`  
- Pollutant fields (e.g., `ozone_ppb`, `pm25_ugm3`)  
- Station metadata (ID, lat/lon, etc.)

### 7.2 STAC Items & Collections

Each STAC Item MUST include:

- `datetime` = `observed_time_utc`  
- `start_datetime` / `end_datetime` for hourly coverage, if needed  
- Extensions:
  - `projection`, `scientific`, `processing`, `version`  
- KFM fields:
  - `kfm:utcOffset`, `kfm:isDST`, `kfm:periodAlignment`  
- Link to provenance:
  - `kfm:provenance_ref` (OpenLineage Run ID)

Collections describe:

- Spatial coverage (CONUS or subset)  
- Temporal extents  
- Update cadence & ingestion window metadata  

### 7.3 DCAT / JSON-LD

DCAT datasets MUST include:

- `dct:temporal` with hourly or multi-day interval  
- `dct:issued` (first availability)  
- `dct:accrualPeriodicity` (e.g., `"R/PT1H"`)  

---

## 🔗 8. Provenance & Lineage (OpenLineage)

AirNow ingest jobs MUST emit OpenLineage events:

- `job.name`: `airnow_ingest_v11` (or equivalent, versioned)  
- `run.runId`: globally unique run identifier  
- `inputs`: raw AirNow endpoints, station lookup references  
- `outputs`: GeoParquet / Zarr / COG + STAC entries  
- `facets`:
  - `TimeNormalizationFacet` (time_basis, offset, DST, anomalies)  
  - `EnergyFacet` (`energy_wh`)  
  - `CarbonFacet` (`carbon_gco2e`)  

Templates live under:

~~~text
docs/pipelines/air/airnow/ingest/lineage/airnow-ingest-lineage.json
~~~

---

## 🌱 9. Telemetry & Sustainability Metrics

Each AirNow ingest run MUST record:

- `energy_wh` — estimated ingest energy  
- `carbon_gco2e` — estimated CO₂e emissions  
- `runtime_sec` — job runtime  
- `rows_processed` — number of AirNow observations  
- `offset_anomaly_count` — inconsistent offsets  
- `dst_anomaly_count` — DST anomalies  
- `period_alignment_violations` — non-`period_begin` cases  

Telemetry is written to:

~~~text
releases/v11.2.3/airnow-ingest-telemetry.json
docs/reports/telemetry/air/airnow-ingest-*.json
~~~

Used for:

- Sustainability dashboards  
- ETL optimization and cost analysis  
- FAIR+CARE & governance audits  

---

## 🗂️ 10. Directory Layout

~~~text
docs/pipelines/air/airnow/ingest/
├── 📄 README.md                        # This file
│
├── 📁 schemas/                         # Timestamp + ingest schemas
│   ├── 🧩 airnow-ingest-v11.json
│   └── 🕒 airnow-timestamps-v11.json
│
├── 🔁 transformers/                    # UTC normalization + DST + period logic
│   ├── ⏱️ time_normalizer.py
│   └── 📐 period_alignment.py
│
├── 🧪 validators/                      # GE configs + custom checks
│   ├── 🧪 temporal_integrity.yml
│   └── 🧪 hourly_validation.yml
│
├── 📜 lineage/                         # OpenLineage templates & docs
│   └── 🔗 airnow-ingest-lineage.json
│
├── 🧪 tests/                           # Automated verification suite
│   ├── 🧪 test_timestamp_roundtrip.py
│   └── 🧪 test_airnow_period_alignment.py
│
└── 🌐 stac/                            # STAC templates for items/collections
    ├── 🌐 airnow-collection.json
    └── 🌐 item-template.json
~~~

---

## 🧭 11. Version History

| Version | Date       | Summary                                                                                               |
|--------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3 | 2025-11-29 | Merged ingest + hourly ingestion docs; unified cadence, storage, and time normalization into one spec. |
| v11.2.2 | 2025-11-28 | Applied emoji directory layout; expanded validation & telemetry sections for AirNow ingest.           |
| v11.1.0 | 2025-11-28 | Initial AirNow ingest & time normalization reference for KFM v11.                                     |

---

<div align="center">

[📘 Docs Root](../../../..) · [🌬️ Air Pipelines](../../README.md) · [🛡 Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
