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
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-air-etl-validation-evidence-checklist"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

doc_uuid: "urn:kfm:doc:etl:air:kansas:validation-checklist:v11.2.6"
semantic_document_id: "kfm-etl-air-kansas-validation-checklist"
event_source_id: "ledger:src/kfm/etl/air/kansas/VALIDATION_CHECKLIST.md"
immutability_status: "version-pinned"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

classification: "Public Document"
sensitivity: "Mixed (station-level; provider-dependent)"
sensitivity_level: "Low to Medium"
public_exposure_risk: "Dataset-level"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
indigenous_rights_flag: "Dataset-level"
redaction_required: false

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "semantic-highlighting"
  - "metadata-extraction"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "speculative-additions"
  - "unverified-claims"
  - "hallucinated-datasets"
  - "governance-override"
---

<div align="center">

# 🌬️ **KFM — Kansas Air ETL Validation & Evidence Checklist**
`src/kfm/etl/air/kansas/VALIDATION_CHECKLIST.md`

**Purpose**  
Make Kansas air-quality micro-batch ingests safe, reproducible, and auditable across **OpenAQ v3**, **EPA AQS**, and **PurpleAir**, by enforcing deterministic validation, late-data detection, and evidence emission (**STAC properties**, **PROV-O run JSON-LD**, **OpenLineage events**).

<img src="https://img.shields.io/badge/KFM--MDP-v11.2.6-purple" />
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img src="https://img.shields.io/badge/Lineage-PROV%E2%80%91O_%7C_OpenLineage-success" />
<img src="https://img.shields.io/badge/Status-Active%20%2F%20Canonical-brightgreen" />

</div>

---

## 📘 Overview

This checklist is the **operational contract** for Kansas air-quality ingestion runs:

- Micro-batch first (deterministic replay), streaming optional (same envelope).
- Provider-aware validation flags with a stable `validation_profile_version`.
- Late/changed data detection with `update_count`, `retroactive_update`, and `time_lag_seconds`.
- Evidence emission that downstream systems can verify without “trusting the pipeline”.

**Outputs that MUST be emitted per micro-batch (per provider, per window):**
- **STAC metadata**: new/updated Item properties that surface QC + retroactivity.
- **PROV-O run doc**: Activity/Entity/Agent chain for the batch window.
- **OpenLineage event(s)**: Job/Run/Dataset facets for operational lineage.

---

## 🧭 Context

### Where this lives in the KFM pipeline

- **ETL**: provider pulls → normalize → validate → stage/commit.
- **Catalogs**: STAC/DCAT updated to reflect new assets + QA state.
- **Graph**: station identity resolved + relationships updated.
- **API/UI**: consumers use lineage + metadata to detect late edits and quality shifts.

### Definitions used in this checklist

- **Micro-batch window**: `[T_start, T_end)` (half-open interval).
- **Natural key (`nk`)**: deterministic identity for an observation record.
- **Retroactive update**: provider sends new value(s) for an existing `nk`.
- **Quarantine**: batch is committed to staging but blocked from public catalogs/graph load.

---

## 🗺️ Diagrams

~~~mermaid
flowchart TD
  A["Provider API Pull\n(OpenAQ v3 / AQS / PurpleAir)"] --> B["Raw Snapshot\n(provider payload + clocks)"]
  B --> C["Normalize + Station Resolve\n(authoritative→proximity→name)"]
  C --> D["Row-Level Validation\n(flag_* + profile_version)"]
  D --> E["Upsert + Retroactivity\n(nk + update_count + time_lag_seconds)"]
  E --> F["Batch Gates\n(quorum + drift + quarantine)"]
  F --> G["Publishable Outputs\nprocessed tables/streams"]
  G --> H["Catalog + Evidence\nSTAC + PROV + OpenLineage"]
~~~

---

## 🧪 Validation & CI/CD

> Use this section as a **run-time checklist**. Each step includes required fields and evidence.

### Step 1 — Source envelope & clock discipline

- [ ] Define ingest window as `[T_start, T_end)` using repo wall-clock for scheduling.
- [ ] Persist **four clocks** per record (raw, not derived):
  - [ ] `source_observed_at` (sensor timestamp)
  - [ ] `provider_last_updated_at` (provider-side timestamp; field name varies)
  - [ ] `ingest_received_at` (gateway receive time; monotonic where possible)
  - [ ] `batch_committed_at` (transaction commit time for the micro-batch)

**Streaming fallback (optional):**
- [ ] Message envelope contains the same four clocks.
- [ ] Idempotency key exists: `{provider}:{station_key}:{parameter}:{source_observed_at}`.

### Step 2 — Authoritative identity & station resolve

- [ ] Resolve station identity using the **3-key rule**:
  1) authoritative ID match  
  2) proximity match  
  3) name match
- [ ] Persist identity fields:
  - [ ] `station_authority` ∈ {`EPA_AQS`,`PurpleAir`,`OpenAQ_Proxy`,`KFM_Custom`}
  - [ ] `station_authoritative_id`
  - [ ] `identity_confidence` ∈ {`authoritative`,`probable`,`fuzzy`}
- [ ] Persist spatial join keys:
  - [ ] `station_geometry_h3_<res>` (one or more H3 resolutions used for joins)

### Step 3 — Row-level validation flags (deterministic, provider-aware)

- [ ] Emit provider-aware flags (booleans unless noted):
  - [ ] `flag_value_range`
  - [ ] `flag_rate_of_change`
  - [ ] `flag_missingness`
  - [ ] `flag_calibration_status` (enum/string when provided)
  - [ ] `flag_qc_provider` (provider QC/qualifier, if present)
  - [ ] `flag_station_resolved`
- [ ] Emit composite:
  - [ ] `flag_authoritative_ok` = all critical flags pass
- [ ] Persist `validation_profile_version` (example: `air-qc-v3.1`).

### Step 4 — Update counting & retroactivity detection

- [ ] Build deterministic natural key:
  - [ ] `nk = hash(provider, station_authoritative_id, parameter, source_observed_at)`
- [ ] Upsert rules:
  - [ ] If `nk` absent → insert with `update_count = 0`
  - [ ] If `nk` present and payload differs → increment `update_count`
  - [ ] Set `last_update_received = ingest_received_at` when updated
- [ ] Compute:
  - [ ] `time_lag_seconds = ingest_received_at - source_observed_at`
  - [ ] `retroactive_update = (update_count > 0)`
- [ ] Maintain delta ledger:
  - [ ] `changed_fields[]` (field names)
  - [ ] `change_fingerprint` (hash of changed subset; optional)

### Step 5 — Batch-level health gates (fail-safe, not fail-open)

- [ ] Quorum gate:
  - [ ] If `pct_failed_authoritative_ok > threshold` → quarantine
- [ ] Drift gate:
  - [ ] Compare batch stats vs prior rolling window (default 7 batches)
  - [ ] If drift exceeds threshold → stage-only + elevate severity
- [ ] Retry/backoff:
  - [ ] WAL + deterministic replay using the same `[T_start, T_end)`
- [ ] Emit severity:
  - [ ] `severity` ∈ {`info`,`warn`,`error`}

### Step 6 — STAC augmentation (explicit properties)

- [ ] Add/Update STAC Item `properties`:
  - [ ] `kfm:update_count` (integer)
  - [ ] `kfm:last_update_received` (RFC3339)
  - [ ] `kfm:time_lag_seconds` (number)
  - [ ] `kfm:retroactive_update` (boolean)
  - [ ] `kfm:validation_profile_version` (string)
  - [ ] `kfm:identity_confidence` (enum)
  - [ ] `kfm:station_authority` (string)
  - [ ] `kfm:station_authoritative_id` (string)
  - [ ] `kfm:flags` (object containing `flag_*`)
  - [ ] `kfm:provider_last_updated_at` (RFC3339)
  - [ ] `kfm:ingest_received_at` (RFC3339)
  - [ ] `kfm:data_quality_score` (0–1, optional)
- [ ] Ensure STAC Item `assets` includes evidence sidecars when published:
  - [ ] `prov.jsonld`
  - [ ] `openlineage.json`

### Step 7 — PROV run emission (W3C PROV-O JSON-LD)

Per micro-batch:

- [ ] `prov:Activity` id pattern:
  - [ ] `kfm:air:kansas:ingest:{provider}:{T_start}-{T_end}`
- [ ] Activity clocks:
  - [ ] `prov:startedAtTime` = first `ingest_received_at`
  - [ ] `prov:endedAtTime` = `batch_committed_at`
- [ ] Entities:
  - [ ] Inputs: provider snapshot/manifests
  - [ ] Outputs: parquet/csv + STAC Item(s) + optional delta ledger
- [ ] Agent:
  - [ ] `prov:SoftwareAgent` for ETL runner with `code_commit_sha`
- [ ] Metrics attached (as attributes or a sidecar):
  - [ ] `rows_total`, `rows_quarantined`, `retro_updates`, `time_lag_seconds_stats`

### Step 8 — OpenLineage events (job + run + dataset facets)

- [ ] Job naming:
  - [ ] `kfm.air.kansas.{provider}.microbatch`
- [ ] Run id:
  - [ ] `runId = uuid5(window + code_commit_sha)`
- [ ] Dataset facets (source & sink):
  - [ ] schema reference (URL or hash)
  - [ ] data quality metrics (flag counts)
  - [ ] documentation link (STAC href or stable repo path)
  - [ ] version/content hash
- [ ] Run facets:
  - [ ] nominal time `[T_start, T_end)`
  - [ ] processing times
  - [ ] error message (when severity is `error`)
  - [ ] validation summary (update_count/time_lag aggregates)

---

## 📦 Data & Metadata

### Deterministic field contracts (minimum)

**Record fields (normalized layer):**
- `provider`
- `station_authority`, `station_authoritative_id`, `identity_confidence`
- `parameter` (canonical code)
- `unit` (canonical unit)
- `value` (numeric)
- clocks: `source_observed_at`, `provider_last_updated_at`, `ingest_received_at`, `batch_committed_at`
- `nk` (hash)
- `update_count`, `last_update_received`, `time_lag_seconds`, `retroactive_update`
- `validation_profile_version`
- `flag_*` fields (provider-aware)

**Delta ledger (when enabled):**
- `nk`
- `update_count_after`
- `changed_fields[]`
- `change_fingerprint`
- `ingest_received_at`

### Minimal STAC `properties` fragment

~~~json
{
  "kfm:update_count": 0,
  "kfm:last_update_received": "2025-12-14T03:21:45Z",
  "kfm:time_lag_seconds": 412.3,
  "kfm:retroactive_update": false,
  "kfm:validation_profile_version": "air-qc-v3.1",
  "kfm:identity_confidence": "authoritative",
  "kfm:station_authority": "EPA_AQS",
  "kfm:station_authoritative_id": "201730005",
  "kfm:flags": {
    "flag_value_range": true,
    "flag_rate_of_change": true,
    "flag_missingness": false,
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

---

## 🌐 STAC, DCAT & PROV Alignment

### STAC

- Each publishable micro-batch updates one or more STAC Items whose `assets` point to the committed outputs.
- Late/changed data MUST be observable via `kfm:update_count`, `kfm:retroactive_update`, and lag metrics.

### DCAT

- DCAT Dataset/Distribution records SHOULD surface:
  - access constraints (provider and privacy constraints)
  - version/content hash where applicable
  - pointers to STAC as the spatiotemporal catalog surface

### PROV-O

- Raw snapshots, processed outputs, catalogs, and evidence docs are `prov:Entity`.
- Each micro-batch is a `prov:Activity` that `prov:used` inputs and `prov:generated` outputs.
- ETL runner is `prov:SoftwareAgent`, linked via `prov:wasAssociatedWith`.

---

## 🧱 Architecture

### Deterministic upsert rule (reference pseudocode)

~~~text
nk = hash(provider, station_authoritative_id, parameter, source_observed_at)

if not exists(nk):
  insert(record, update_count=0, retroactive_update=false)
else:
  if payload_differs(existing, record):
    update_count = existing.update_count + 1
    retroactive_update = true
    changed_fields = diff_fields(existing, record)
    upsert(record, update_count=update_count, retroactive_update=true, changed_fields=changed_fields)
  else:
    no-op (idempotent replay)
~~~

### Quarantine behavior

- Quarantine keeps artifacts **reproducible and inspectable** but blocks:
  - publication into public STAC/DCAT surfaces
  - graph load into production
  - downstream “public UI” activation

---

## 🗂️ Directory Layout

Recommended (not exhaustive) evidence layout for a single provider micro-batch:

~~~text
📁 data/
├── 📁 air-quality/
│   ├── 📁 processed/
│   │   └── 📁 kansas/
│   │       ├── 📁 openaq-v3/
│   │       ├── 📁 aqs/
│   │       └── 📁 purpleair/
│   └── 📁 reports/
│       └── 📁 self-validation/
│           └── 📁 air-kansas/
│               └── 📁 <provider>/
│                   └── 📁 <T_start>__<T_end>/
│                       ├── 🧾 prov.jsonld
│                       ├── 🧾 openlineage.json
│                       ├── 🧾 validation-summary.json
│                       └── 🧾 delta-ledger.parquet
~~~

---

## 🧠 Story Node & Focus Mode Integration

Focus Mode and Story Nodes can safely use this checklist’s outputs to:

- detect late revisions and avoid presenting stale “facts”
- surface quality caveats (“sensor drift detected”, “batch quarantined”)
- provide provenance links from visualizations back to:
  - the micro-batch Activity (PROV)
  - the exact catalog Item (STAC)
  - the operational run record (OpenLineage)

---

## ⚖ FAIR+CARE & Governance

Air-quality data is generally public, but **station-level exposure can be sensitive**:

- Some PurpleAir devices may be at residences; treat precision as provider- and context-dependent.
- When required by policy or provider terms:
  - generalize geometry (H3) for public surfaces
  - restrict raw coordinates to governed layers
- Never weaken or “assume away” governance:
  - if in doubt, quarantine and escalate to stewards.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | KFM-MDP v11.2.6 alignment: approved H2 registry, inner-tilde fences, required governance footer + version history; tightened deterministic replay and evidence emission rules. |
| v11.2.3 | 2025-12-09 | Initial Kansas air ingest checklist covering micro-batch validation, STAC/PROV/OpenLineage evidence, and late-data detection. |

---

<div align="center">

🌬️ **KFM — Kansas Air ETL Validation & Evidence Checklist (v11.2.6)**  
Deterministic Pipelines · Evidence-Led Lineage · FAIR+CARE Governed

[⬅ Back to Repository Root](../../../../../README.md) ·
[📑 KFM Markdown Protocol](../../../../../docs/standards/kfm_markdown_protocol_v11.2.6.md) ·
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
