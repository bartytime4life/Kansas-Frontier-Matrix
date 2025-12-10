---
title: "📡 KFM — STAC Telemetry Integration Overview (Freshness · Energy · SLO State)"
path: "docs/events/remote-sensing/stac-telemetry-overview.md"
version: "v11.2.6"
last_updated: "2025-12-10"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Metadata Council & Reliability Engineering"
content_stability: "stable"

doc_kind: "Technical Overview"
status: "Active"
intent: "stac-telemetry-spec"
semantic_document_id: "kfm-doc-stac-telemetry-overview-v11.2.6"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.6/manifest.zip"
attestation_ref: "../../releases/v11.2.6/slsa-attestation.json"
signature_ref: "../../releases/v11.2.6/signature.sig"

telemetry_schema_ref: "../../schemas/telemetry/stac-telemetry-v11.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

license: "CC-BY 4.0"
markdown_protocol_version: "KFM-MDP v11.2.6"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
---

# 📡 STAC Telemetry Integration Overview

KFM v11.2.6 attaches **operational telemetry** to STAC Items so that the pipeline:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j graph → API → Story Nodes → Focus Mode

can reason about **freshness**, **energy usage**, **CO₂-equivalent intensity**, **lineage run IDs**, and **SLO health** directly at the catalog layer.

These telemetry fields are:

- written by deterministic ETL
- validated in CI and via schemas
- ingested into the graph
- surfaced in Story Nodes and Focus Mode for remote-sensing narratives and SLO reporting

---

## 🗂️ Directory Layout

~~~text
docs/
└── 📁 events/
    └── 📁 remote-sensing/
        ├── 📄 stac-telemetry-overview.md      # This document (KFM STAC telemetry overview)
        ├── 📁 sentinel-2/
        │   └── 📄 README.md                   # Sensor-specific telemetry & SLO notes
        ├── 📁 modis/
        │   └── 📄 README.md
        └── 📁 landsat/
            └── 📄 README.md

schemas/
└── 📁 telemetry/
    └── 📄 stac-telemetry-v11.json             # JSON Schema for telemetry fields on STAC Items

src/
└── 📁 pipelines/
    └── 📁 telemetry/
        └── 📄 stac_telemetry_writer.py        # ETL-side writer for kfm:* telemetry fields

configs/
└── 📁 pipelines/
    └── 📁 telemetry/
        └── 📄 stac-telemetry-writer.yaml      # Config for telemetry calculation & thresholds
~~~

---

## 📘 Overview

This document defines the **STAC telemetry extension** used by KFM for remote-sensing data:

- which **fields** are attached to STAC Items
- how they are **computed** and **updated**
- how they flow through:
  - **ETL & telemetry collectors**
  - **STAC/DCAT/PROV catalogs**
  - **Neo4j (`StacItem` nodes and related entities)**
  - **APIs, Story Nodes, and Focus Mode**

Design principles:

- **Deterministic & reproducible**: same inputs → same telemetry values for a given run.
- **Non-destructive**: telemetry fields may be updated, but core STAC semantics remain immutable.
- **FAIR+CARE aligned**: telemetry must not expose sensitive operational details or violate sovereignty, but must support accountability and sustainability.

---

## 🧩 Telemetry Fields Added to STAC Items

Telemetry fields live under `properties` of STAC Items.

| Field                    | Type    | Description                                                                                 |
|--------------------------|---------|---------------------------------------------------------------------------------------------|
| `kfm:ingest_ts`          | string  | ETL ingest timestamp (ISO 8601, UTC) for the Item.                                         |
| `kfm:freshness_seconds`  | number  | Age of the dataset (seconds between source datetime and ingest timestamp).                 |
| `kfm:etl_kwh_per_gb`     | number  | Estimated ETL energy consumption intensity (kWh per GB processed).                         |
| `kfm:co2eq_g_per_gb`     | number  | Estimated CO₂-equivalent emissions (grams per GB processed).                               |
| `kfm:lineage_run_id`     | string  | Deterministic run identifier for lineage replay and PROV/OpenLineage linking.             |
| `kfm:slo_state`          | string  | SLO conformance state for this Item: `"ok"`, `"warning"`, or `"violation"`.                |

**Mutation rule:**

- Telemetry fields (`kfm:*`) MAY be **updated** after initial publish, via controlled ETL/patch pipelines.
- Core STAC fields (geometry, datetime, assets, collection, etc.) remain **immutable** under this spec.

---

## 📦 Example STAC Item With Telemetry

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "KFM_S2A_2025_12_09_T14SNA",
  "collection": "kfm-sentinel-2-l2a",
  "properties": {
    "datetime": "2025-12-09T14:20:00Z",
    "kfm:ingest_ts": "2025-12-10T01:05:13Z",
    "kfm:freshness_seconds": 16213,
    "kfm:etl_kwh_per_gb": 0.038,
    "kfm:co2eq_g_per_gb": 21.4,
    "kfm:lineage_run_id": "run_78b9f7e3",
    "kfm:slo_state": "ok"
  }
}
~~~

---

## 🧬 Role in the KFM Pipeline

Telemetry values are produced and consumed along the standard pipeline:

1. **Deterministic ETL**
   - Reads remote-sensing sources (e.g., Sentinel-2, MODIS, Landsat).
   - Computes core data products and loads them into work/processed layers.

2. **Telemetry Collector**
   - Observability stack (OTel / metrics) produces per-run energy, timing, and SLO metrics.
   - A deterministic reducer transforms metrics into per-Item telemetry values.

3. **STAC Writer**
   - Applies telemetry values to STAC Items under `properties.kfm:*`.
   - Writes Items under `data/stac/**` with idempotent behavior (same run_id → same telemetry values).

4. **Catalogs & Provenance**
   - STAC Items are cataloged via existing KFM-STAC v11 profile.
   - PROV and/or OpenLineage link `kfm:lineage_run_id` to ETL and telemetry Activities.

5. **Graph Ingestion (Neo4j)**
   - Telemetry properties are mapped to `StacItem` node properties (and optionally to `TelemetrySample` nodes).
   - SLO and sustainability queries run against the graph.

6. **APIs & Story Nodes**
   - APIs expose filtered subsets (e.g., only Items with `kfm:slo_state="violation"`).
   - Story Nodes and Focus Mode use telemetry to:
     - highlight stale or degraded layers
     - explain SLO incidents
     - show energy/carbon footprints over time

---

## 🎛️ Update Flow (Deterministic ETL → STAC)

The canonical **update flow** for telemetry is:

1. **Raw → Work**
   - Remote-sensing data lands in `data/raw/**`, then normalized into `data/work/**`.

2. **Telemetry Collector Emits Metrics**
   - ETL jobs emit per-run metrics: bytes processed, runtime, energy estimates, and SLO measurements.
   - Metrics are written to:
     - `data/events/telemetry/**` (for replay)
     - observability backends (for dashboards)

3. **Telemetry Reducer**
   - A deterministic reducer job maps run-level metrics to per-Item telemetry:
     - `freshness_seconds = ingest_ts - source_datetime`
     - energy and CO₂ per GB based on workload and scaling rules

4. **STAC Telemetry Writer**
   - Applies telemetry fields to STAC Items:
     - merges into `properties.kfm:*`
     - ensures idempotent application per `kfm:lineage_run_id`

5. **SLO Gate**
   - Evaluates thresholds:
     - freshness (max staleness)
     - energy/carbon budgets
     - error rates / retries
   - Sets `kfm:slo_state` accordingly (`ok`, `warning`, `violation`).

6. **Publish or Rollback**
   - If SLO gate passes: Items are marked as **ready** and made visible to APIs/UI.
   - If it fails: the pipeline can:
     - keep previous Items as defaults
     - record a `violation` state
     - raise alerts for Reliability Engineering

---

## 🔍 Querying Telemetry Through STAC API

Telemetry fields are designed for simple, composable filters.

Example query snippets (exact syntax depends on API implementation):

- **Find stale products** (too old at ingest time):

  ~~~text
  properties.kfm:freshness_seconds > 7200
  ~~~

- **Prefer low-carbon products**:

  ~~~text
  properties.kfm:co2eq_g_per_gb < 25
  ~~~

- **Detect SLO violations**:

  ~~~text
  properties.kfm:slo_state = "violation"
  ~~~

- **Filter by ETL run** (for replay / debugging):

  ~~~text
  properties.kfm:lineage_run_id = "run_78b9f7e3"
  ~~~

APIs must **not** expose raw infrastructure identifiers or sensitive topology details; telemetry is a **summarized signal**, not a full trace dump.

---

## 📚 DCAT Integration (Optional Aggregates)

STAC telemetry is primary; DCAT MAY carry **aggregated** telemetry at Dataset level:

- `kfm:telemetry:freshness_p95_seconds` — 95th percentile freshness for a time window.
- `kfm:telemetry:avg_co2eq_g_per_gb` — average CO₂ intensity across Items.
- `kfm:telemetry:slo_state_overview` — high-level SLO state summary for the Dataset.

These are written under DCAT Datasets in `data/catalogs/**` and should be derived **exclusively** from STAC + graph data, not from ad-hoc sources.

---

## 🌐 Neo4j & Graph Integration

Telemetry properties are ingested into the graph for reasoning and visualization.

### Node mapping

- `(:StacItem)` nodes carry:

  - `ingest_ts` (datetime)
  - `freshness_seconds` (integer)
  - `etl_kwh_per_gb` (float)
  - `co2eq_g_per_gb` (float)
  - `lineage_run_id` (string)
  - `slo_state` (string enum)

- Optional `(:TelemetrySample)` nodes can be created when more granular telemetry is needed, linked via:

  - `(:StacItem)-[:HAS_TELEMETRY]->(:TelemetrySample)`

### Lineage links

- `(:StacItem)-[:DERIVED_FROM_RUN]->(:PipelineRun { run_id = kfm:lineage_run_id })`
- `(:PipelineRun)-[:USED]->(:Dataset)` for inputs
- `(:PipelineRun)-[:GENERATED]->(:Dataset)` for outputs

This supports queries like:

- “Show all Items with SLO violations for Sentinel-2 in the last week.”
- “Summarize energy and CO₂ per Collection over a given time range.”
- “Explain an SLO incident by linking Items ↔ runs ↔ Story Nodes.”

---

## 🧪 CI & Validation

Telemetry integration is governed by CI to ensure correctness and stability:

- **Schema validation**
  - `stac-telemetry-v11.json` schema must validate all STAC Items with telemetry.
  - Run as part of `.github/workflows/telemetry-stac.yml`.

- **Determinism checks**
  - Given a fixed input dataset and `lineage_run_id`, telemetry values must be reproducible.
  - CI compares telemetry outputs against approved snapshots in `mcp/experiments/telemetry/**`.

- **SLO logic tests**
  - Unit tests validate mapping from raw metrics → `kfm:slo_state`.
  - Thresholds are configuration-driven (in `stac-telemetry-writer.yaml`).

- **FAIR+CARE / Sovereignty checks**
  - Telemetry must not leak sensitive operational details (e.g., exact cluster IDs).
  - Any region-specific telemetry used for Indigenous or sensitive landscapes must be reviewed by governance bodies before rollout.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                           |
|----------|------------|-----------------------------------------------------------------|
| v11.2.6  | 2025-12-10 | Initial KFM STAC telemetry overview aligned to KFM-MDP v11.2.6. |

---

### ⚖ FAIR+CARE & Governance Footer

This document:

- complies with **KFM-MDP v11.2.6**, **KFM-STAC v11**, **KFM-DCAT v11**, and **KFM-PROV v11**  
- is governed by the **Metadata Council** and **Reliability Engineering**, with co-review by the Governance Council  
- must be updated when telemetry fields, thresholds, or graph mappings are materially changed

Edits require approval from the Metadata Council and Reliability Engineering and must pass
`markdown-lint`, `schema-lint`, `footer-check`, and telemetry validation workflows.

<br/>

<sub>© Kansas Frontier Matrix · CC‑BY 4.0 · Diamond⁹ Ω / Crown∞Ω · Aligned with KFM‑MDP v11.2.6</sub>

<br/>

<div align="center">

📡 **Kansas Frontier Matrix — STAC Telemetry Integration Overview v11.2.6**  
Remote-Sensing Freshness · Energy & Carbon Telemetry · SLO-Aware Catalogs  

[📘 Docs Root](../../README.md) · [📡 Events Index](../README.md) · [📂 Standards Index](../../standards/README.md) · [⚖ Governance Charter](../../standards/governance/ROOT-GOVERNANCE.md)

</div>