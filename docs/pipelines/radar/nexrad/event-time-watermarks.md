---
title: "🌩️ Kansas Frontier Matrix — Event-Time Watermarks for NEXRAD Ingest (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/radar/nexrad/event-time-watermarks.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Radar Working Group · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Ingest Standard"
header_profile: "standard"
footer_profile: "standard"

markdown_protocol_version: "KFM-MDP v11.2.4"
mcp_version: "MCP-DL v6.3"
license: "CC-BY 4.0"

scope:
  domain: "atmo.radar.nexrad"
  applies_to:
    - "etl"
    - "streaming-ingest"
    - "watermarks"
    - "stac"
    - "catalogs"
    - "graph"
    - "telemetry"

fair_category: "F1-A1-I1-R1"
care_label: "Mixed · CARE-sensitive"
sensitivity: "Mixed (enable dynamic generalization & tribal review)"
classification: "Public / Internal (governed ingest standard)"

commit_sha: "<latest-commit>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/ingest-radar-telemetry.json"
telemetry_schema: "schemas/telemetry/pipelines-radar-ingest-v3.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "docs/standards/sovereignty/RADAR-SOVEREIGNTY-GUIDE.md"
---

<div align="center">

# 🌩️ **Event-Time Watermarks for NEXRAD Ingest (KFM v11.2.4)**  
`docs/pipelines/radar/nexrad/event-time-watermarks.md`  

**Deterministic ingest · AVSET-safe · WAL-replayable · STAC/DCAT/PROV-aligned**

</div>

---

## 🗂️ Directory Layout (KFM v11.x Monorepo)

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 radar/
        └── 📁 nexrad/
            📄 event-time-watermarks.md          # ← This ingest standard
            📁 watermarks/                       # Finalization & delay patterns (canary/final)
            📁 qc/
            │   📄 tilt-detection.md
            │   📄 avset-rules.md
            │   📄 wedges.md
            📁 lineage/
            │   📄 prov-patterns.md
            └── 📁 sops/
                📄 ingest-runbook.md             # Operational SOPs (alerts, incident steps)
```

Implementation and tests MUST mirror this layout logically:

```text
📁 src/
└── 📁 pipelines/
    └── 📁 radar/
        └── 📁 nexrad/
            📄 ingest.py                         # Event-time keyed ingest
            📄 qc.py                             # Tilt/AVSET/wedge metrics
            📄 watermark_gate.py                 # Implements this standard
            📄 stac_emit.py                      # STAC item creation
            📄 graph_emit.py                     # Neo4j upserts for RadarVolume/QC

📁 data/
└── 📁 radar/
    └── 📁 nexrad/
        📁 raw/                                 # Raw Level-II/III blobs
        📁 work/                                # Decoded headers/tilts
        📁 processed/                           # Volume-level composites
        📁 stac/                                # STAC Items/Collections
```

---

## 📘 Overview

This document defines the authoritative **ingest-layer contract** for **event-time watermarking** of **NEXRAD Level-II and Level-III** radar volumes within the Kansas Frontier Matrix (KFM).

Event-time watermarks guarantee:

- Determinism across ingest replays and environment changes  
- Stable ordering of radar volumes in the presence of jitter and delay  
- Correct behavior when **AVSET**, SAILS/MESO-SAILS, and truncation occur  
- Safe multi-sensor joins (e.g., with HRRR, gauges, satellite)  
- Consistent behavior under **WAL replay** and **idempotent ETL node patterns**

This ingest standard should be read alongside:

- `docs/pipelines/atmo/nexrad/watermarks/finalization-pattern.md`  
  (preview vs. final volume finalization & delay pattern)  
- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`  
  (event-driven WAL + promotion pattern)  

---

## 🧭 Purpose

The goals of this specification are to:

1. **Guarantee temporal integrity** for all radar-aligned ETL pipelines.  
2. **Prevent premature publishing** of partial or truncated volumes as “final”.  
3. **Support distributed ingestion** (SNS/SQS/Kafka/S3 triggers) without race conditions.  
4. **Enable deterministic recovery** after outages, restarts, and late-arriving volumes.  
5. **Expose standardized quality + watermark metadata** into STAC → DCAT → PROV → Neo4j.

All NEXRAD ingest pipelines in KFM **MUST** implement this pattern to be considered production-grade.

---

## ⏱️ Event-Time Watermark Semantics

### 1️⃣ Event-Time Definition

```text
event_time = radar_volume.start_timestamp
```

- Derived from the Level-II/III header timestamp with **millisecond or microsecond precision**.  
- Used as the **primary time axis** for stream windows, joins, and catalog time stamping:
  - STAC `properties.datetime`
  - Graph `RadarVolume.event_time`

### 2️⃣ Watermark Emission Rule

A watermark **W(t)** may be emitted only when:

```text
ingest_clock_now >= t + lateness_allowed
```

Baseline parameters:

| Parameter          | Default | Notes                                                                 |
|--------------------|---------|-----------------------------------------------------------------------|
| `lateness_allowed` | 4 min   | Tuned to 99.9p delay including replays, network jitter, AVSET cases. |
| `max_wait_cap`     | 6 min   | Hard cap for degraded mode; used with explicit “degraded” flag.      |

Per-site overrides may be configured, but must remain **≤ max_wait_cap** and recorded in provenance.

### 3️⃣ BLOCK Conditions (No Publish)

A volume MUST NOT be promoted when any of the following holds:

- Missing any **required VCP or tilt** defined by the site’s **radar profile**.  
- `AVSET = true` **and** upper tilts missing or truncated.  
- Detected azimuthal holes ≥ **20°** (spatial wedge).  
- Duplicate `volume_id` within a **15s window** for the same site/VCP.  
- `event_time < last_emitted_watermark` (strict **out-of-order violation**).  

Such volumes MUST be:

- Routed to a **partial/quarantine tier** (e.g., `radar/nexrad/partial/`), and  
- Marked as `kfm.qc.publish_decision = "quarantine"` in STAC/graph.

### 4️⃣ PROMOTE Conditions (Allow Publish)

A radar volume is safe to promote to the canonical processed tier when:

```text
all_required_tilts_present == true
AND vertical_completeness == "full"
AND spatial_wedge_deg < 20
AND watermark_passed == true
```

And there is **no stricter site-specific rule** being violated (e.g., severe storm operations with additional tilt requirements).

---

## 🧪 Validation & QC Logic

### Required QC Fields

The following fields MUST be computed during ingest and stored:

- In STAC Item `properties`  
- On the `:RadarVolume` and linked `:QCReport` nodes in Neo4j  

```json
{
  "kfm.radar.avset": false,
  "kfm.radar.required_tilts_present": 16,
  "kfm.radar.required_tilts_total": 16,
  "kfm.radar.vertical_completeness": "full",
  "kfm.radar.spatial_wedge_deg": 4.2,
  "kfm.radar.watermark_passed": true,
  "kfm.qc.publish_decision": "promote"
}
```

**Partial / Quarantined volumes** MUST use:

```json
{
  "kfm.radar.vertical_completeness": "partial",
  "kfm.qc.publish_decision": "quarantine"
}
```

and be excluded from:

- Final time-series products  
- Focus Mode “final” radar narratives  
- Any derived layers that claim to serve **complete volume coverage**

---

## 🌐 STAC / DCAT / PROV Integration

### STAC Requirements

For each NEXRAD volume:

- **Collection**: `kfm-radar-nexrad` (or site-specific derived collections).  
- **Item** properties:

  ```json
  {
    "kfm:radar:site": "KICT",
    "kfm:radar:vcp": 212,
    "kfm:radar:event_time": "2025-08-01T00:05:32Z",
    "kfm:radar:avset": false,
    "kfm:radar:required_tilts_present": 16,
    "kfm:radar:required_tilts_total": 16,
    "kfm:radar:vertical_completeness": "full",
    "kfm:radar:spatial_wedge_deg": 4.2,
    "kfm:radar:watermark_passed": true,
    "kfm:qc:publish_decision": "promote",
    "kfm:watermark:lateness_allowed_s": 240,
    "kfm:watermark:max_wait_cap_s": 360
  }
  ```

- Add `roles` on assets or items:

  - `"quality"`, `"watermark-metrics"`  

- Add `links` for provenance:

  - `rel="prov:wasGeneratedBy"` for ingest activity,  
  - `rel="prov:used"` for the raw Level-II/III blobs.

### DCAT Emission

Derived DCAT metadata MUST reflect:

- Watermark completeness under `dct:provenance`.  
- QC details under `dqv:QualityAnnotation` or equivalent.  

Where applicable, DCAT datasets capturing NEXRAD products should:

- Indicate whether only **full** volumes are exposed,  
- Note any filtered subsets (e.g., partial volumes available behind an internal flag).

### Neo4j Pattern

Canonical graph pattern:

```text
(:RadarVolume { site, volume_id, vcp, event_time })
  -[:HAS_QC]->(:QCReport {
        avset,
        required_tilts_present,
        required_tilts_total,
        vertical_completeness,
        spatial_wedge_deg,
        publish_decision
    })
  -[:HAS_WATERMARK]->(:Watermark {
        event_time,
        lateness_allowed_s,
        max_wait_cap_s,
        watermark_passed
    })
```

Graph nodes must be updated via **idempotent MERGE patterns** so replayed ingest events do not create duplicates.

---

## 🧱 Deterministic Replay & WAL Model

All upstream triggers (S3 events, Kafka messages, etc.) MUST produce **WAL entries** that include:

```json
{
  "event_time": "2025-08-01T00:05:32Z",
  "site": "KICT",
  "volume_id": "KICT_20250801_000532_V06",
  "arrival_time": "2025-08-01T00:05:49Z",
  "qc_summary_hash": "sha256:...",
  "raw_md5": "md5:...",
  "state": "pre-wm-qc"
}
```

Replay rules:

1. **Order by `event_time` (primary)**, then tie-breakers (site, volume_id).  
2. Recompute QC + watermark conditions deterministically.  
3. Promote or quarantine using the same rules as the original run.  
4. Emit lineage with a stable **derivation hash** that captures:
   - raw content digests,  
   - QC summary hash,  
   - watermarks + thresholds.

WAL must be compatible with the **Event-Driven Deterministic Ingestion & Promotion Pattern** at:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`

---

## 🧰 Pipeline Placement

Event-time watermark logic belongs in the ingest chain as:

1. **Raw Fetch**  
   - Ingest Level-II/III files from S3 / NEXRAD feeds.  
2. **Header Decode**  
   - Extract event_time, volume_id, VCP, site, AVSET flags.  
3. **Tilt Enumeration**  
   - Inspect tilt coverage, reflectivity/velocity tilts, elevation angles.  
4. **QC Stage**  
   - Compute wedge metrics, completeness scores, duplicate detection.  
5. **Watermark Gate (THIS STANDARD)**  
   - Check watermark eligibility; block or allow volume promotion.  
6. **STAC Item Creation**  
7. **DCAT Derivation**  
8. **Neo4j Insertion**  
9. **Cache / Tile Publication**  

Volumes **must not** skip the watermark gate on any production path.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                                   |
|--------:|------------|-----------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Full KFM-MDP alignment; spatial wedge rules; partial volume quarantine; AVSET guardrails. |
| v11.2.3 | 2025-12-03 | Added derivation hash crosswalk and explicit QC property requirements.                  |
| v11.2.0 | 2025-11-20 | Initial governed version of NEXRAD event-time watermark ingest standard.               |

---

## 🏛️ Governance & Footer

This ingest standard is governed by:

- **Radar Working Group**  
- **FAIR+CARE Council**  
- **Sovereignty Board** (via `RADAR-SOVEREIGNTY-GUIDE.md`)

All changes require:

- 2-reviewer sign-off (Radar WG + Governance), and  
- Updated `doc_integrity_checksum` and telemetry references in the SBOM/manifest.

Energy, carbon, and sovereignty policies are enforced via:

- `telemetry_schema` and `energy_schema` / `carbon_schema`, and  
- The sovereignty policy at `docs/standards/sovereignty/RADAR-SOVEREIGNTY-GUIDE.md`.

<div align="center">

🌩️ **Kansas Frontier Matrix — NEXRAD Event-Time Watermarks**  

[📘 Docs Root](../../README.md) ·  
[📡 Radar Pipelines Index](../README.md) ·  
[⚖️ Root Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>