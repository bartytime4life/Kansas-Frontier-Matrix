---
title: "📊 KFM v11 — Metric Cardinality Management & Safe Label Design (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/telemetry/metrics/cardinality/README.md"
version: "v11.2.2"
last_updated: "2025-11-30"
review_cycle: "Quarterly · Telemetry Governance · FAIR+CARE Council"
status: "Active / Enforced"

commit_sha: "<latest>"
previous_version_hash: "<previous>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/otel-metrics.json"
telemetry_schema: "../../../../schemas/telemetry/metric-cardinality-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.1"
doc_kind: "Guideline"
intent: "Define safe label practices, prevent time-series explosions, and enforce observability guardrails."
fair_category: "Reusability"
care_label: "CARE-Respect"
---

<div align="center">

# 📊 **KFM v11 — Metric Cardinality Management & Safe Label Design**  
**Observability Standard · OpenTelemetry · Prometheus · Grafana Mimir**

</div>

KFM’s telemetry system must remain **fast, cheap, predictable, and provenance-clean**.  
High cardinality is the primary threat to metric-system stability.  
This document formalizes the **Approved Label Set**, the **Forbidden Attributes List**, and the **Governed Mitigation Workflow**.

---

## 1. 🎯 Purpose
- Prevent runaway **time-series explosion** in Prometheus/Mimir.  
- Create **stable, aggregatable** metric identities across KFM pipelines.  
- Enforce **FAIR+CARE**, anonymization, and Indigenous data-sovereignty constraints.  
- Ensure **trace/log correlation** happens through spans—not through metric labels.

---

## 2. 🧱 What Counts as Cardinality
A unique time series is defined by:

```
<metric_name> { label_a = "...", label_b = "...", … }
```

A volatile or unbounded label produces thousands (or millions) of series.

**Red flags:**  
- Identifiers (UUIDs, user_id, STAC IDs)  
- Raw file paths  
- Timestamps in labels  
- Geographic coordinates  
- Exact URLs  
- Dynamic H3 cells  
- Per-feature or per-pixel values

---

## 3. 🟩 Approved Low-Cardinality Labels (Whitelist v11.2)

**Global Labels (allowed everywhere):**
- `service`  
- `pipeline`  
- `component`  
- `region`  
- `dataset`  
- `dataset_release`  
- `status` (`ok|warn|error`)  
- `method`  
- `layer`  
- `zoom_bin` (categorical: `z<=8`, `9-12`, `13+`)  
- `phase` (`ingest`, `transform`, `upsert`)  
- `op` (`read`, `write`, `merge`, `tile`)  

**Why:**  
Bounded, predictable, semantically meaningful, and aggregation-friendly.

---

## 4. 🛑 Forbidden High-Cardinality Attributes (Do Not Use)
These labels are banned in metrics across all of KFM:

- `user_id`  
- `request_id`, `session_id`, `trace_id`, `span_id`  
- `tile_id`, `feature_id`, `stac_id`  
- `http_url`, `file_path`, `s3_path`  
- `timestamp`, `ts`, or any dynamic time token  
- `x`, `y`, `lat`, `lon`, `elev` (raw)  
- `h3` (full resolution)  
- `sensor_id` (unbounded)  
- Full instrument names from scientific datasets

**Reason:**  
They create **unbounded label cardinality** and violate CARE protections.

---

## 5. 🧭 Design Patterns (Correct vs Incorrect)

### Good
```
kfm_ingest_total{source="usgs", status="ok"}
kfm_tile_build_seconds{layer="soil", zoom_bin="9-12", method="gdal"}
kfm_graph_upserts_total{op="merge", dataset_release="v11.2"}
```

### Bad
```
kfm_ingest_total{stac_id="20251129T..."}           # unbounded
kfm_tile_build_seconds{http_url="/tiles/11/345"}   # near-infinite
kfm_graph_upserts_total{feature_id="abc123"}       # one series per feature
```

---

## 6. 📉 Reducing Cardinality: Mandatory Techniques

### 6.1 Binning / Categorization
- Zoom levels → `zoom_bin`
- Elevation → `elev_bin` (≤250m, 250–1000m, >1000m)
- File size → `size_class`
- Resolution → `low|med|high`

### 6.2 Template Normalization
Convert:

`/api/users/9991/items/551?ts=...`  
→  
`/api/users/:id/items/:id`

### 6.3 Put volatility in **traces/logs**, not metrics
Metrics = stable aggregates  
Traces = per-request  
Logs = contextual details

---

## 7. 📊 Query Hygiene (PromQL)

Examples:

```
sum by (dataset, status) (rate(kfm_ingest_total[5m]))
```

```
histogram_quantile(0.95,
  sum by (le, layer) (rate(kfm_tile_build_seconds_bucket[15m]))
)
```

Guideline: aggregate by **small, bounded label sets**.

---

## 8. 🧪 Observability Governance Controls

### 8.1 Active Series Budget (ASB)
Each service receives a cardinality budget.
- Hard limit → reject new labelsets  
- Soft limit → alert + governance record stored in lineage

### 8.2 Spike Detection
Triggers:
- New labelset count increases > 30% in 5 minutes  
- New dimension appears in any metric

### 8.3 Automatic Quarantine
If a label is classified as **High-Risk**:
- WAL auto-suppresses offending series  
- Mimir ruler inserts deny-match relabel rule  
- Ticket auto-generated for Telemetry Council

---

## 9. 📜 Required Metadata in Metric Definitions
Every metric added to KFM must define:

```
metric_name:
  stability: "stable|experimental"
  cardinality: "low|bounded"
  allowed_labels:
    - "status"
    - "layer"
  forbidden_labels:
    - "tile_id"
    - "feature_id"
  lineage_ref: "path/to/prov.json"
  owner: "team"
  review: "quarterly"
```

---

## 10. 📂 Directory Layout

```
docs/
  telemetry/
    metrics/
      cardinality/
        README.md        # this file
        patterns.md      # best practices
        governance.md    # enforcement rules
        review-log.md    # quarterly audits
```

---

## 11. 🧩 Focus Mode / Story Node Integration
Cardinality anomalies automatically generate:
- A Story Node under **"Telemetry → Cardinality Events"**  
- Narrative overlays for DAGs  
- Provenance entries (PROV-O `prov:Activity` with `prov:wasInformedBy` links)

---

## 12. 🪵 Version History
- **v11.2.2** — Full rewrite, governance integration, binning standardization.  
- **v11.1.0** — Introduced label whitelist + forbidden list.  
- **v10.x** — Early draft patterns, non-enforced.

---

<div align="center">

**KFM v11 — Observability with Purpose**  
[📘 Documentation](../../../../README.md) • [⚖️ Governance](../../../standards/governance/ROOT-GOVERNANCE.md) • [📡 Telemetry](../../README.md)

</div>
