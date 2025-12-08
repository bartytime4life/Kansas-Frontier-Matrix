---
title: "🌩️ KFM — Event-Driven Atmospheric & Soil Pipelines Overview (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/event-driven/overview.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Pipelines Board · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x event-driven pipelines"

status: "Active / Enforced"
doc_kind: "Architecture Overview"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<sha256-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/pipeline-telemetry.json"
telemetry_schema: "schemas/telemetry/event-driven-pipelines-v3.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask on; sovereign overlays governed)"
sensitivity: "Mixed (public + potentially sensitive joins)"
classification: "Public / Internal (architectural)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/pipelines/soil/sda-async/README.md@v11.2.4"
  - "docs/pipelines/atmo/nexrad/watermarks/finalization-pattern.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:event-driven:overview:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "event-driven-architecture-overview-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "multi-domain"
  applies_to:
    - "etl"
    - "streaming"
    - "stac"
    - "dcat"
    - "graph"
    - "provenance"
    - "telemetry"
    - "story-nodes"
    - "focus-mode"
  impacted_modules:
    - "docs/pipelines/event-driven"
    - "docs/pipelines/soil"
    - "docs/pipelines/atmo"
    - "src/pipelines/soil/*"
    - "src/pipelines/atmo/*"
    - "data/raw/*"
    - "data/processed/*"
    - "data/stac/*"
    - "dist/provenance/*"
---

<div align="center">

# 🌩️ **Event-Driven Pipelines Overview**  
### *Atmospheric Streams · Soil Systems · Deterministic ETL → STAC/DCAT/PROV → Graph → Tiles → Focus Mode*

`docs/pipelines/event-driven/overview.md`

</div>

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 event-driven/
        📄 overview.md                     # ← This file (architecture overview)
        📁 soils/
        │   📄 triggers.md                 # Soil event sources (SDA, parcels, boundaries)
        │   📄 transforms.md               # Canonical soil transforms (CRS, units, stratigraphy)
        │   📄 validations.md              # Schema, geometry, stratigraphy, CARE checks
        │   📄 publication.md              # STAC/DCAT, tiles, graph mapping
        📁 atmo/
        │   📄 triggers.md                 # Atmospheric triggers (NEXRAD, HRRR, etc.)
        │   📄 transforms.md               # Grids, windows, derived fields
        │   📄 validations.md              # Coverage, QC, temporal checks
        │   📄 publication.md              # STAC/time tiles/graph integration
        📁 patterns/
            📄 event-driven-deterministic-ingest.md  # Canonical event-driven pattern (shared)
```

Concrete implementations live under `src/` and follow the pattern‑level docs:

```text
📁 src/
└── 📁 pipelines/
    ├── 📁 soil/
    │   └── 📁 sda_async/                  # SDA async ingestion (event-driven capable)
    └── 📁 atmo/
        └── 📁 nexrad/
            ├── 📁 watermarks/             # NEXRAD watermark/finalization implementation
            └── ...                        # Other atmospheric event-driven pipelines
```

---

## 📘 1. Purpose

This document defines the **canonical event-driven pipeline architecture** for KFM:

- **Atmospheric data**  
  - NEXRAD Level-II, HRRR, other radar/model outputs.

- **Soils data**  
  - USDA SDA (Soil Data Access), parcel‑driven updates, stratigraphy layers.

All event-driven pipelines must conform to:

- **Deterministic ETL** (no hidden time / randomness),  
- **Idempotent replays** with stable outputs,  
- **Formal provenance** (OpenLineage + PROV‑O),  
- **FAIR+CARE governance**, and  
- KFM’s unified distribution spine:

> Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j knowledge graph → API layer → Tiles & Story Nodes → Focus Mode

This overview is authoritative for:

- Pipeline architects & developers,  
- Governance reviewers (FAIR+CARE, IDGB),  
- Focus Mode and Story Node integration work.

---

## 🧱 2. High-Level Pipeline Shape

Conceptual shape for all event-driven pipelines:

```text
Trigger → Ingest → Normalize → Validate → Transform → Publish → Graph → Story Nodes
```

Event sources and orchestration:

- Cloud object events (e.g., **S3 “ObjectCreated”** for NEXRAD/HRRR).  
- **Webhooks** (agency notifications, parcel updates, soil refresh signals).  
- **Scheduled fallbacks** (hourly/daily/weekly) for resilience.  
- **Event-driven determinism**:
  - Idempotency keys,  
  - Write‑Ahead Log (WAL),  
  - Canary → monitor → promote/rollback,  
  - Telemetry spans (energy, carbon, cost, reliability).

For implementation details, pipelines must follow:

- `docs/pipelines/patterns/event-driven-deterministic-ingest.md`.

---

## 🌱 3. Soil Event-Driven Pipelines (SDA & Parcels)

### 3.1 Triggers

Typical soil triggers:

- USDA SDA refresh signals (e.g., SDA metadata changes).  
- New or updated **parcel polygons** or jurisdiction boundaries.  
- **Monthly reconciliation** windows (e.g., scheduled baseline recheck).

Triggers produce structured `RunEvent`s with:

- `source_uri` / SDA query ID / parcel batch ID,  
- `content_hash` (e.g., BLAKE3 of payload),  
- Logical `time_window` (e.g., month, parcel update batch).

Idempotency key (per event-driven pattern):

```text
idempotency_key = blake3(f"{source_uri}|{content_hash}|{time_window}")
```

### 3.2 Core Transforms

Canonical transforms (building on SDA patterns):

- **CRS harmonization**  
  - Soil geometries normalized to a canonical EPSG (e.g., EPSG:4326 or shared project CRS).

- **Attribute & unit normalization**  
  - Soil attributes mapped to canonical names and units (e.g., cm, %, g/cm³).

- **Stratigraphy linkage**  
  - Map units (`mukey`) → components (`cokey`) → horizons (`chkey`) with stratigraphic validation.

- **H3 summarization**  
  - Summary statistics in hexagon grids (e.g., R6–R8) for overlay in Focus Mode.

### 3.3 Validations

Soil pipelines must enforce:

- **Schema continuity**  
  - Parity with previous releases (no unintentional column or type drift).

- **Geometry validity & area sanity**  
  - No self‑intersections, slivers, or “impossible” areas/centroids.

- **Stratigraphic sanity**  
  - Horizon depth ordering and non-overlap (per SDA async pattern).

- **Provenance completeness**  
  - All runs must emit PROV‑O bundles, link SDA queries, and record configs.

- **CARE / masking when joined**  
  - If soil is joined with sensitive layers (e.g., archaeology, ecology), data generalization rules apply.

### 3.4 Publication Targets

Soil event-driven outputs publish to:

- **STAC Collections + Items**  
  - `soil_mu.parquet`, `soil_co.parquet`, `soil_ch.parquet`, plus derived hex summaries.

- **DCAT Datasets** (auto-derived)  
  - Created via KFM STAC→DCAT derivation, not hand-crafted.

- **Tiles**  
  - Vector/raster tiles for MapLibre/Cesium.  
  - Indexed by version, not just “latest”.

- **Neo4j graph**  
  - Nodes:
    - `:SoilMapUnit`, `:SoilComponent`, `:SoilHorizon`, `:DatasetVersion`.  
  - Relationships:
    - `:HAS_COMPONENT`, `:HAS_HORIZON`, `:DERIVES_FROM`, `:PRODUCED_BY`.

- **Story Nodes (optional)**  
  - Soil classification changes, boundary shifts, or major SDA updates.

---

## 🌩️ 4. Atmospheric Event-Driven Pipelines (NEXRAD & HRRR)

### 4.1 Triggers

Atmospheric pipelines use:

- **Object store events**  
  - e.g., S3 “ObjectCreated” from NEXRAD / HRRR buckets.

- **Distributor webhooks**  
  - External vendor/agency signals for new atmospheric products.

- **Scheduled fallback**  
  - Hourly or more frequent cron-based backstops in case events are missed.

Events are normalized into `RunEvent`s with:

- `source_uri` (e.g., bucket key),  
- `content_hash`,  
- `time_window` (e.g., volume time or forecast cycle).

### 4.2 Core Transforms

For atmospheric pipelines (NEXRAD, HRRR, etc.):

- **Spatial/temporal clipping**  
  - Focus on Kansas AOIs + buffer, with consistent bounding boxes.

- **Grid homogenization**  
  - Deterministic x/y resolution and projection for rasters/grids.

- **Rolling window statistics**  
  - 1h / 3h / 24h windows for accumulations and rates.

- **QC-driven masking**  
  - Mask incomplete fields relying on QC flags (e.g., NEXRAD quality flags, HRRR QC indicators).

Specialization for NEXRAD watermarks & finalization:

- Event-time watermarks for Level-II volumes,  
- VCP-aware finalization delays,  
- Clear preview vs final product semantics (see NEXRAD watermark module).

### 4.3 Validations

Atmospheric pipelines must enforce:

- **Temporal monotonicity**  
  - No time regressions in published sequences, consistent intervals.

- **Coverage thresholds**  
  - Coverage ≥ 95% over AOI for final products (or flagged exceptions).

- **NaN / missing data budgets**  
  - Enforce allowable rates of missing values per product & window.

- **QC flag consistency**  
  - Ensure products respect QC flags (no mislabeled “good” pixels).

- **Watermark & finalization checks** (for NEXRAD)  
  - Watermark drift, replay consistency, volume completeness, VCP delay enforcement.

### 4.4 Publication Targets

Atmospheric event-driven outputs publish to:

- **Time-enabled tiles**  
  - For MapLibre/Cesium time scrubbing (temporal dimension in tiles + metadata).

- **STAC Items / Collections**  
  - Append-only Items with stable IDs for each time/volume snapshot.

- **Neo4j graph**  
  - Nodes such as `:RadarVolume`, `:AtmosProduct`, `:ForecastCycle`.  
  - Relationships for lineage and derivations.

- **Story Node snapshots**  
  - “New atmospheric window available”, “Severe event timeline update”, etc.

---

## 🛡️ 5. Reliability & Safety Guarantees

Event-driven pipelines must implement the **Event‑Driven Deterministic Ingestion Pattern**:

### 5.1 Idempotency keys

Canonical idempotency key:

```text
idempotency_key = blake3(f"{source_uri}|{content_hash}|{time_window}")
```

Rules:

- Multiple deliveries of the same `(source_uri, content_hash, time_window)` must resolve to **one logical run**.  
- Replays with unchanged inputs produce **identical artifacts**.

### 5.2 WAL & replay safety

- All stateful writes (raw, work, processed, STAC, graph) preceded by **WAL entries**.  
- A run either:
  - Commits all steps as a coherent unit, or  
  - Fully rolls back (no half‑baked data visible).

Replay must:

- Rehydrate from WAL and produce the same final datasets,  
- Preserve STAC and PROV identity and values (subject to allowed numeric tolerance).

### 5.3 Canary, promote & rollback

- **Canary publishes**:
  - Initial STAC & graph writes to canary namespaces / shadow graphs.  
  - Monitors observe correctness, latency, and QA metrics.

- **Promotion**:
  - Only after monitors are green within a defined window,  
  - Feature flags control cutover to new datasets/tiles.

- **Rollback**:
  - Feature flags revert,  
  - Graph pointers reset to last known good version,  
  - Data rolled back using WAL and/or underlying versioned storage (e.g., lakeFS).

### 5.4 Error handling

- **Dead-letter queues** for malformed or repeatedly failing payloads.  
- **Retry strategy**:
  - Exponential backoff,  
  - Deterministic seeds & configs (no divergence on retry).

- **Alerting**:
  - Critical failures emit alerts tied into pipeline SLO dashboards.

---

## 🧾 6. Metadata & Catalog Rules

### 6.1 STAC (authoritative catalogs)

- **Collections**:
  - Describe dataset-level spatial/temporal coverage, license, and lineage.

- **Items**:
  - Must include:
    - `id` (stable),  
    - Asset `href`s,  
    - `type` / mediaType,  
    - `roles`,  
    - `checksum` metadata,  
    - Temporal extent and bounding geometry.

- **Lineage pointers**:
  - `prov:wasGeneratedBy` and `openlineage:runId`,  
  - `kfm:provenance_ref` (PROV-O JSON-LD),  
  - `kfm:telemetry_ref` (telemetry records).

### 6.2 DCAT (automatic derivation)

- All DCAT metadata must be **derived** from STAC using the KFM v11.2.4 crosswalk.  
- No hand-authored DCAT may contradict STAC; STAC is the **single source-of-truth**.

### 6.3 Semantic bindings (GeoSPARQL / CIDOC-CRM / OWL-Time)

- Spatial footprints:
  - WKT and/or GeoJSON geometries; H3 region sets for efficient queries.

- Temporal intervals:
  - Modeled with OWL-Time (intervals, instants) for events and windows.

- Lineage edges:
  - Mapped onto PROV-O entities/activities/agents and optionally expressed via GeoSPARQL & CIDOC-CRM for historical and domain context.

---

## 📖 7. Story Nodes & Focus Mode Integration

Each event-driven pipeline should optionally emit **Story Node bundles** to power narrative interfaces:

- Examples:
  - “New atmospheric window available” (radar/model update).  
  - “Soils classification update applied” (SDA refresh).  
  - “Boundary adjustments propagated” (parcel / jurisdiction change).

Story Node bundles must:

- Reference:

  - Dataset versions (STAC Item IDs, DatasetVersion nodes),  
  - Time windows,  
  - Provenance (PROV bundles, OpenLineage runs).

- Distinguish between:
  - **Preview** vs **final** views for atmospheric data,  
  - **Baseline** vs **incremental** updates for soil data.

Focus Mode uses these bundles to:

- Build multi-layer narratives over time,  
- Provide “explainability” for what changed, when, and why,  
- Reflect governance status (e.g., FAIR+CARE scores, audit findings).

---

## 📊 8. Observability & Telemetry

All event-driven pipelines must emit telemetry conforming to:

- `schemas/telemetry/event-driven-pipelines-v3.json`

Required metrics:

- **Energy usage** (kWh, Joules)  
- **CO₂e estimates** (kg CO₂e)  
- **Cost attribution** (e.g., $/run, $/GB)  
- **Latency histograms** (ingest → final publish)  
- **Error-rate & retry spans**  
- **Data volume metrics** (records/tiles per run)  

Telemetry feeds:

- Reliability & SLO dashboards,  
- FAIR+CARE & sustainability audits,  
- Focus Mode “impact” overlays (optional).

---

## ♻️ 9. Versioning & Reproducibility

Each event-driven pipeline run must produce a **reproducible dataset version**:

- Data versioning:
  - Via lakeFS or equivalent snapshotting/versioned storage.  

- Code & config pinning:
  - Git commit SHA,  
  - Container image tags,  
  - Config snapshots (YAML/JSON).

- Graph representation:
  - Nodes:
    - `:Dataset`, `:DatasetVersion`, `:Run`.  
  - Relationships:
    - `:DERIVES_FROM`, `:GENERATED_BY`, `:VALIDATED_BY`.

Reconstruction of a release requires:

- Raw source availability,  
- Transform code at exact commit,  
- Config snapshot,  
- Telemetry bundle & provenance.

---

## 🧮 10. Version History

| Version | Date       | Author / Steward              | Summary                                                                 |
|---------|------------|-------------------------------|-------------------------------------------------------------------------|
| v11.2.4 | 2025-12-07 | Pipelines Board · FAIR+CARE Council | Initial fully governed event-driven architecture overview under KFM-MDP v11.2.4. |

---

<div align="center">

**Kansas Frontier Matrix (KFM v11)**  
**Deterministic · Ethical · Reproducible · Open**

[⚖️ Root Governance](../\../\../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📚 STAC/DCAT Standards](../\../\../docs/standards/catalogs/) ·  
[📈 Telemetry Schemas](../\../\../schemas/telemetry/)

</div>