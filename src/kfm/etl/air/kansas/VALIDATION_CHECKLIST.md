---
title: "🌬️ KFM — Kansas Air ETL Validation & Evidence Checklist (OpenAQ v3 · AQS · PurpleAir)"
path: "src/kfm/etl/air/kansas/VALIDATION_CHECKLIST.md"
version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE & Reliability Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Checklist"
intent: "kfm-air-etl-validation-evidence-checklist"

header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
doc_uuid: "urn:kfm:doc:air-etl-validation-checklist:kansas:v11.2.6"
semantic_document_id: "kfm-doc-air-etl-validation-kansas"
event_source_id: "ledger:src/kfm/etl/air/kansas/VALIDATION_CHECKLIST.md"
immutability_status: "version-pinned"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
---

# 🌬️ KFM — Kansas Air ETL Validation & Evidence Checklist

## 📘 Overview

This checklist makes **micro‑batch air‑quality ingests** safe, deterministic, and auditable across **OpenAQ v3**, **EPA AQS**, and **PurpleAir**.

It is designed to:
- Detect and quantify **late arriving** and **retroactively edited** observations.
- Emit evidence artifacts that downstream systems can rely on:
  - **STAC** properties + sidecar assets,
  - **W3C PROV‑O** (JSON‑LD) run records,
  - **OpenLineage** events,
  - Validation summaries, delta ledgers, and integrity hashes.
- Prevent “fail‑open” ingestion by enforcing **quarantine and drift gates** at batch level.

In the KFM pipeline, this checklist sits at **ETL** and feeds:
`ETL → catalogs (STAC/DCAT/PROV) → graph → API → frontend → Story Nodes → Focus Mode`.

## 🗂️ Directory Layout

This document lives at:

~~~text
src/kfm/etl/air/kansas/VALIDATION_CHECKLIST.md
~~~

Evidence and outputs for Kansas air ETL SHOULD land under the repo’s data plane. The repo snapshot indicates these domain roots exist:

~~~text
data/
├── air-quality/        # Domain root for air-quality data products (Kansas + providers)
└── updates/            # Incremental update payloads / delta ledgers
~~~

Recommended evidence layout (adjust only if your pipeline is explicitly configured differently):

~~~text
data/
├── air-quality/
│   ├── raw/                       # Provider snapshots (optional if you snapshot elsewhere)
│   ├── work/                      # Normalized intermediates
│   ├── processed/                 # Deterministic outputs (Parquet/CSV/COG as applicable)
│   ├── lineage/
│   │   ├── prov/                  # prov.jsonld per micro-batch
│   │   └── openlineage/           # openlineage.json per micro-batch
│   └── reports/
│       ├── validation/            # row/batch QC summaries
│       └── drift/                 # drift diagnostics
├── stac/
│   └── air-quality/               # STAC Collections/Items for air-quality (if used)
├── dcat/
│   └── datasets/                  # DCAT dataset records (if used)
└── updates/
    └── air-quality/
        └── kansas/                # delta-ledger tables + compact change sets
~~~

Minimum evidence artifacts per micro‑batch window:
- A deterministic output dataset (or “quarantined” marker).
- A validation summary (flag counts + station resolve stats).
- `prov.jsonld` and `openlineage.json`.
- A STAC Item (or Item update) referencing the output plus sidecars.
- A content hash/checksum for each persisted artifact.

## 🧪 Validation & CI/CD

### ✅ 8‑Step Production Checklist

#### 1) Source Envelope & Clock Discipline (Micro‑Batch First)
- **Ingest window:** `[T_start, T_end)` using repository wall‑clock and **provider last‑updated signals**.
- Persist four clocks for every observation row:
  - `source_observed_at` (sensor timestamp, as‑reported)
  - `provider_last_updated_at` (provider “updated” field, if available)
  - `ingest_received_at` (gateway receive time; monotonic within batch)
  - `batch_committed_at` (transaction commit time)
- Streaming fallback (optional): mirror the same four clocks in the message envelope and use a deterministic idempotency key:
  - `{provider}:{station_authoritative_id}:{parameter}:{source_observed_at}`

#### 2) Authoritative Identity & Station Resolve
- Resolve station using a deterministic “3‑key” rule:
  1) **Authoritative ID match**, else
  2) **Proximity match** (H3 and/or distance threshold), else
  3) **Name/alias match** (fuzzy)
- Persist:
  - `station_authority` ∈ {`EPA_AQS`,`PurpleAir`,`OpenAQ_Proxy`,`KFM_Custom`}
  - `station_authoritative_id`
  - `station_geometry_h3_{res}` (H3 indexes for joins; resolution is config‑driven)
  - `identity_confidence` ∈ {`authoritative`,`probable`,`fuzzy`}
- If station cannot be resolved deterministically, keep the record but set:
  - `flag_station_resolved = false`
  - `identity_confidence = "fuzzy"`

#### 3) Row‑Level Validation Flags (Deterministic, Provider‑Aware)
Emit deterministic flags per row (boolean unless noted):

- `flag_value_range` (hard bounds per parameter + unit normalization)
- `flag_rate_of_change` (spike check; parameter‑specific thresholds)
- `flag_missingness` (null/NaN/empty structure)
- `flag_unit_normalized` (unit conversion performed and recorded)
- `flag_calibration_status` (enum/string from provider metadata if available)
- `flag_qc_provider` (string/enum; e.g., AQS qualifier/QC code)
- `flag_station_resolved` (from Step 2)

Composite:
- `flag_authoritative_ok = (flag_station_resolved && flag_value_range && flag_missingness && flag_unit_normalized && flag_rate_of_change)`

Always store:
- `validation_profile_version` (e.g., `air-qc-v3.1`)

#### 4) Update Counting & Retroactivity Detection
- Build deterministic natural key:
  - `nk = hash(provider, station_authoritative_id, parameter, source_observed_at)`
- On upsert:
  - If `nk` exists and payload differs → increment `update_count`
  - Set `last_update_received_at = ingest_received_at`
  - Compute `time_lag_seconds = ingest_received_at - source_observed_at`
  - Set `retroactive_update = (update_count > 0)`
- Maintain a compact delta ledger for every changed record:
  - `changed_fields[]` (field names only; avoid storing full old values unless governed)

#### 5) Batch‑Level Health Gates (Fail‑Safe, Not Fail‑Open)
- **Quorum rule:** if more than `X%` of rows fail `flag_authoritative_ok`, quarantine the batch.
- **Drift rule:** compare last `N` batches vs current (mean/variance/flag rates). If drift exceeds threshold:
  - mark `drift_state ∈ {ok, warn, error}`
  - degrade to staging‑only outputs
- Enforce deterministic replay:
  - WAL + same `[T_start, T_end)` + same configs must reproduce identical outputs.
- Emit batch `severity ∈ {info, warn, error}` into lineage, telemetry, and validation report.

#### 6) STAC Item / Collection Augmentation (Explicit Properties)
Add to STAC Item `properties` (and bubble to Collection summaries where appropriate):

- `kfm:update_count` (integer)
- `kfm:last_update_received_at` (RFC3339)
- `kfm:time_lag_seconds` (number)
- `kfm:retroactive_update` (boolean)
- `kfm:validation_profile_version` (string)
- `kfm:identity_confidence` (enum)
- `kfm:station_authority` (string)
- `kfm:station_authoritative_id` (string)
- `kfm:flags` (object: all `flag_*` fields)
- `kfm:provider_last_updated_at` (RFC3339)
- `kfm:ingest_received_at` (RFC3339)
- `kfm:data_quality_score` (0–1, optional composite)

Assets:
- The STAC Item MUST include sidecars:
  - `prov.jsonld`
  - `openlineage.json`
  - `validation.json` (or `validation.ndjson`) summary

#### 7) PROV Run Emission (W3C PROV‑O JSON‑LD)
Per micro‑batch window, emit:

- **prov:Activity**
  - `id = urn:kfm:activity:air:ingest:{provider}:{T_start}-{T_end}`
  - `prov:startedAtTime` = first `ingest_received_at`
  - `prov:endedAtTime` = `batch_committed_at`
  - attributes: window bounds, counts, `quorum_pass`, `drift_state`, checksums
- **prov:Entity** (inputs): API snapshot/manifests
- **prov:Entity** (outputs): parquet/csv, STAC Item(s), delta-ledger extract (if any)
- **prov:Agent**: orchestration + code identity:
  - `kfm:orchestrator` (e.g., Dagster/Airflow)
  - `kfm:code_commit_sha`

Attach metrics:
- total rows
- rows quarantined
- retroactive updates
- mean/median `time_lag_seconds`

#### 8) OpenLineage Events (Job + Run + Dataset Facets)
Emit per micro‑batch:

- **Job**
  - `kfm.air.kansas.{provider}.microbatch`
- **Run**
  - `runId = uuid5(window_key, code_commit_sha)` (deterministic)
- **Dataset facets**
  - schema URL, documentation link to STAC Item, quality metrics (flag counts), version hash
- **Run facets**
  - `nominalTime = [T_start, T_end)`
  - processing times, drift state, quorum pass/fail, error message (if any)

### CI expectations (high level)
A batch SHOULD NOT be treated as “production‑ready” unless:
- validation summary exists,
- lineage artifacts exist (PROV + OpenLineage),
- STAC item validates (if STAC is emitted),
- integrity hashes/checksums match persisted artifacts,
- quarantine/drift gates are enforced (fail‑closed).

## 🌐 STAC, DCAT & PROV Alignment

### STAC alignment
- STAC is the primary “asset face” for spatiotemporal outputs.
- STAC Items for air ETL must carry:
  - update/retroactivity metadata (`kfm:update_count`, `kfm:retroactive_update`)
  - freshness metadata (`kfm:time_lag_seconds`, `kfm:ingest_received_at`)
  - row‑level QC rollups (`kfm:flags` + `kfm:data_quality_score`)
- Sidecar assets ensure auditability without chasing logs.

### DCAT alignment (if used for publishing)
- DCAT Dataset identifiers should mirror the dataset’s stable KFM id.
- DCAT Distributions should point at:
  - the processed data artifact,
  - and/or the STAC Item/Collection as discoverability metadata.
- Access constraints (e.g., private PurpleAir sensor precision) must be recorded explicitly.

### PROV alignment
- PROV makes the “why/how” queryable:
  - which raw snapshots contributed,
  - which batch produced a record,
  - why a record changed (retroactive update).

## 📦 Data & Metadata

### Minimal STAC `properties` fragment

~~~json
{
  "kfm:update_count": 0,
  "kfm:last_update_received_at": "2025-12-14T03:21:45Z",
  "kfm:time_lag_seconds": 412.3,
  "kfm:retroactive_update": false,
  "kfm:validation_profile_version": "air-qc-v3.1",
  "kfm:identity_confidence": "authoritative",
  "kfm:station_authority": "EPA_AQS",
  "kfm:station_authoritative_id": "201730005",
  "kfm:flags": {
    "flag_value_range": true,
    "flag_rate_of_change": true,
    "flag_missingness": true,
    "flag_unit_normalized": true,
    "flag_calibration_status": "ok",
    "flag_qc_provider": "A",
    "flag_station_resolved": true,
    "flag_authoritative_ok": true
  },
  "kfm:provider_last_updated_at": "2025-12-14T03:21:10Z",
  "kfm:ingest_received_at": "2025-12-14T03:21:45Z",
  "kfm:data_quality_score": 0.96
}
~~~

### Minimal PROV‑O JSON‑LD skeleton

~~~json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    {
      "kfm": "urn:kfm:",
      "kfm:code_commit_sha": { "@type": "xsd:string" },
      "kfm:window_start": { "@type": "xsd:dateTime" },
      "kfm:window_end": { "@type": "xsd:dateTime" }
    }
  ],
  "@id": "urn:kfm:activity:air:ingest:EPA_AQS:2025-12-14T03:00:00Z-2025-12-14T04:00:00Z",
  "@type": "prov:Activity",
  "prov:startedAtTime": "2025-12-14T03:21:45Z",
  "prov:endedAtTime": "2025-12-14T03:22:10Z",
  "kfm:window_start": "2025-12-14T03:00:00Z",
  "kfm:window_end": "2025-12-14T04:00:00Z",
  "prov:wasAssociatedWith": {
    "@id": "urn:kfm:agent:etl:kfm-air",
    "@type": "prov:Agent",
    "kfm:code_commit_sha": "<latest-commit-hash>"
  },
  "prov:used": [
    { "@id": "urn:kfm:entity:air:raw:EPA_AQS:snapshot:2025-12-14T03:21:10Z", "@type": "prov:Entity" }
  ],
  "prov:generated": [
    { "@id": "urn:kfm:entity:air:processed:EPA_AQS:kansas:window:2025-12-14T03", "@type": "prov:Entity" },
    { "@id": "urn:kfm:entity:stac:item:air-quality:kansas:2025-12-14T03", "@type": "prov:Entity" }
  ]
}
~~~

### Minimal OpenLineage event skeleton

~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-14T03:22:10Z",
  "run": {
    "runId": "00000000-0000-0000-0000-000000000000",
    "facets": {
      "nominalTime": { "startTime": "2025-12-14T03:00:00Z", "endTime": "2025-12-14T04:00:00Z" },
      "kfmValidation": {
        "update_count_total": 12,
        "retroactive_update_rows": 12,
        "time_lag_seconds_mean": 410.2,
        "time_lag_seconds_p95": 1200.0,
        "quorum_pass": true,
        "drift_state": "ok"
      }
    }
  },
  "job": { "namespace": "kfm.air.kansas", "name": "epa_aqs.microbatch" },
  "inputs": [
    { "namespace": "https://api.example", "name": "epa_aqs_snapshot", "facets": { "version": { "datasetVersion": "<hash>" } } }
  ],
  "outputs": [
    { "namespace": "kfm.data", "name": "air_quality_kansas_epa_aqs_window_2025_12_14_03", "facets": { "version": { "datasetVersion": "<hash>" } } }
  ],
  "producer": "urn:kfm:producer:air-etl"
}
~~~

### Delta ledger schema (recommended)
A compact delta ledger is the canonical evidence for retroactive edits.

~~~text
delta_ledger (
  nk                       TEXT PRIMARY KEY,
  provider                 TEXT NOT NULL,
  station_authoritative_id TEXT NOT NULL,
  parameter                TEXT NOT NULL,
  source_observed_at       TIMESTAMP NOT NULL,
  ingest_received_at       TIMESTAMP NOT NULL,
  update_count             INTEGER NOT NULL,
  retroactive_update       BOOLEAN NOT NULL,
  changed_fields           TEXT[] NOT NULL,
  payload_hash             TEXT NOT NULL
)
~~~

## 🧠 Story Node & Focus Mode Integration

If air‑quality data is surfaced in Story Nodes or Focus Mode:
- Narrative claims SHOULD be conditioned on:
  - `kfm:data_quality_score`,
  - `kfm:retroactive_update`,
  - `kfm:time_lag_seconds`,
  - and the batch drift state.
- If a Story Node references a time range that later receives a retroactive update:
  - the Story Node SHOULD be eligible for refresh,
  - and provenance links MUST remain stable (so evidence trails don’t break).

Minimum evidence link set for a narrative claim:
- STAC Item link (and assets),
- PROV activity id,
- OpenLineage run id,
- validation summary hash.

## ⚖ FAIR+CARE & Governance

Air data can still be sensitive:
- **PurpleAir** sensors may be colocated with private residences. Treat precise coordinates as potentially sensitive.
  - Prefer storing/publishing **H3‑generalized** station geometry for public catalogs.
  - Retain exact geometry only in governed contexts where policy permits.
- Always store and propagate:
  - license/terms metadata,
  - attribution requirements,
  - access constraints (public vs restricted).

Fail‑closed governance rule:
- If required governance metadata is missing (license, access, sensitivity), do not publish to public catalogs.

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | MDP v11.2.6 compliance update (approved H2 headings + tilde fences); aligned evidence paths to `data/air-quality/` and `data/updates/`; completed minimal STAC/PROV/OpenLineage examples; strengthened privacy/governance guidance for PurpleAir station geometry. |

---

<div align="center">

🌬️ **KFM — Kansas Air ETL Validation & Evidence Checklist (v11.2.6)**  
MIT License · MCP‑DL v6.3 · KFM‑MDP v11.2.6 · KFM‑OP v11 · KFM‑PDC v11

[⬅ Back to Repo Root](../../../../../README.md) ·
[📦 Data Plane](../../../../../data/README.md) ·
[🔄 CI/CD Workflows](../../../../../.github/workflows/README.md) ·
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>

