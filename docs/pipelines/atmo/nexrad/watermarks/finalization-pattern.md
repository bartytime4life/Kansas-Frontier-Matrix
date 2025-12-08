---
title: "🌩️ KFM v11.2.4 — NEXRAD Event-Time Watermark & Finalization Delay Pattern"
path: "docs/pipelines/atmo/nexrad/watermarks/finalization-pattern.md"
version: "v11.2.4"
last_updated: "2025-12-07"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Pipelines · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "Backward compatible with v11.0.x NEXRAD pipelines"

status: "Active / Enforced"
doc_kind: "Pattern"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.4/sbom.spdx.json"
manifest_ref: "releases/v11.2.4/manifest.zip"
telemetry_ref: "releases/v11.2.4/atmo-telemetry.json"
telemetry_schema: "schemas/telemetry/patterns/nexrad-watermark-v1.json"
governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-compliant (auto-mask enabled for sensitive overlays)"
sensitivity: "Mixed (severe weather, emergency overlays, tribal lands)"
classification: "Public / Internal (operational pattern)"

provenance_chain:
  - "docs/standards/kfm_markdown_protocol_v11.2.4.md@v11.2.4"
  - "docs/pipelines/patterns/event-driven-deterministic-ingest.md@v11.2.4"
  - "docs/pipelines/atmo/nexrad/README.md@v11.2.4"

doc_uuid: "urn:kfm:doc:pipelines:atmo:nexrad:watermarks:finalization-pattern:v11.2.4"

test_profiles:
  - "markdown-frontmatter-v11"
  - "markdown-structure-v11"
  - "footer-governance-links-v11"
  - "atmo-nexrad-watermark-pattern-v1"

ci_integration: ".github/workflows/docs-lint.yml"

scope:
  domain: "atmospheric"
  applies_to:
    - "etl"
    - "stac"
    - "graph"
    - "provenance"
    - "telemetry"
    - "lineage"
    - "story-nodes"
  impacted_modules:
    - "docs/pipelines/atmo"
    - "data/raw/atmo/nexrad"
    - "data/processed/atmo/nexrad"
    - "data/stac/atmo/nexrad"
    - "src/pipelines/atmo/nexrad"
    - "src/graph/atmo"
    - "src/api/atmo"
    - "src/web/story-nodes/atmo"
---

<div align="center">

# 🌩️ **NEXRAD Event-Time Watermark & Finalization Delay Pattern**  
`docs/pipelines/atmo/nexrad/watermarks/finalization-pattern.md`

**Diamond⁹ Ω / Crown∞Ω Ultimate Certified**  
**Deterministic · Idempotent · lakeFS-Safe · FAIR+CARE Aligned**

</div>

---

## 📘 Overview

### Purpose

This pattern defines the authoritative KFM v11.2.4 method for applying **event-time watermarks** and **finalization delays** to NEXRAD Level-II ingestion.

It ensures that:

- No **partial-volume** products are published as “final”.  
- Event-time processing is **deterministic across replay** (WAL + reprocessing).  
- Downstream atmospheric products (Focus Mode, Story Nodes, Mesh Atlases, risk layers) see only **stable, reproducible volumes**.

It is a **specialization** of the **Event-Driven Deterministic Ingestion & Promotion Pattern** for NEXRAD atmospheric data.

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            └── 📁 watermarks/
                📄 finalization-pattern.md      # ← This file
                📁 examples/
                │   📄 minimal-flow.md          # Small end-to-end example
                │   📄 replay-behavior.md       # Replay determinism analysis
                │   📄 qa-tests.md              # QA test matrix & edge cases
                └── 📁 design/
                    📄 vcp-delay-rationale.md   # VCP-aware delay rationale

📁 src/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            📄 config_watermarks.yaml           # Lateness buffers & VCP delays
            📄 ingest_stream.py                 # NEXRAD event ingestion
            📄 watermark_logic.py               # Event-time / watermark implementation
            📄 finalization_job.sql             # Streaming SQL / job definition
            📄 stac_emit.py                     # STAC Item & Collection emission

📁 data/
└── 📁 processed/
    └── 📁 atmo/
        └── 📁 nexrad/
            📁 preview/                         # Optional preview-only products
            📁 final/                           # Final, watermark-stable products

📁 data/
└── 📁 stac/
    └── 📁 atmo/
        └── 📁 nexrad/
            📁 preview/                         # STAC Collections/Items for preview
            📁 final/                           # STAC Collections/Items for final datasets
```

---

## 🧭 Context

NEXRAD volume scans arrive:

- **Out of order**,  
- In **bursts**,  
- With **variable completion times** due to:
  - VCP mode,  
  - SAILS / MESO-SAILS,  
  - AVSET / range-dependent termination.

This introduces three hazards:

1. **Partial volumes**  
   - Early frames produce incomplete reflectivity/velocity fields.  
   - UI flicker and unstable quantitative products (QPE, QPF, hail, rotation).

2. **Replay drift**  
   - WAL or queue replays can deliver messages in different orders.  
   - Without a consistent watermark, window boundaries shift between runs.

3. **Non-deterministic aggregations**  
   - Time-window closures depend on arrival order.  
   - “Final” fields differ per run, breaking scientific reproducibility.

**Event-time watermarks + explicit finalization delays** eliminate all three:

- Windows close on **event-time semantics**, not ingest timestamps.  
- Finalization waits for **“enough information” + VCP-aware delay**.  
- Idempotent keys ensure **one canonical final product per (radar, volume, product)**.

---

## 🧱 Architecture

### Canonical pattern overview

**Key principles:**

- **Event time > ingest time** (always)  
- Watermark = `event_time - lateness_buffer`  
- Finalization requires:
  - **Observed completeness** of a volume, plus  
  - **VCP-aligned delay** (Section 🕒 Choosing the Finalization Delay)  
- Deterministic **idempotent upsert** keyed by:

```text
(radar_id, volume_id, product_code)
```

#### Preview vs final

| Layer       | Purpose                    | When it Publishes                                 |
|------------|----------------------------|---------------------------------------------------|
| **Preview** | Early map responsiveness   | On watermark closure (may be partial / provisional) |
| **Final**   | Stable, authoritative data | After VCP-specific delay & volume completeness    |

Preview products must be **visually distinct** and clearly marked as non-final; only final products are:

- Indexed into canonical STAC/DCAT collections,  
- Inserted into the production Neo4j graph,  
- Used as Story Node / Focus Mode baselines.

---

### Implementation model (streaming)

The pattern is generally implemented in a streaming framework (Flink, Beam, etc.), but the semantics are framework-agnostic.

#### Event-time & watermark definition (Flink SQL example)

```sql
CREATE TABLE nexrad_raw (
  radar_id STRING,
  volume_id STRING,
  product_code STRING,
  event_time TIMESTAMP(3),
  payload BYTES,
  WATERMARK FOR event_time AS event_time - INTERVAL '2' MINUTE
);
```

This ensures:

- Event-time order and late data handling are explicit.  
- Lateness tolerance is a **configurable parameter**, not a hard-coded constant.

#### Finalization stage (volume aggregation)

```sql
INSERT INTO nexrad_final
SELECT
  radar_id,
  volume_id,
  product_code,
  aggregate(...) AS product_payload
FROM nexrad_raw
GROUP BY radar_id, volume_id, product_code
HAVING CURRENT_WATERMARK(event_time) >= MAX(event_time) + INTERVAL '7' MINUTE;
```

Semantics:

- Aggregation waits until `CURRENT_WATERMARK(event_time)` passes  
  `MAX(event_time) + finalization_delay`.  
- Finalization delay is **VCP-aware**.  
- Each `(radar_id, volume_id, product_code)` emits **exactly one final record**.

---

### 🕒 Choosing the finalization delay

Finalization delay **must** be tied to the VCP and operational behavior of the radar:

| VCP                     | Typical Duration | Recommended Base Delay |
|-------------------------|------------------|------------------------|
| **12 / 212**            | ~4.5–5 min       | 5 min                  |
| **215 / 35**            | ~6–7 min         | 7 min                  |
| **SAILS / MESO-SAILS**  | Burst low-level cuts | +1 min buffer      |

Effective delay per volume:

```text
finalization_delay(vcp, sails_state) =
  base_delay(vcp) + sails_buffer(vcp, sails_state)
```

Requirements:

- Delay parameters must live in **versioned config** (e.g., `config_watermarks.yaml`).  
- Delay values must be **recorded in PROV-O** for each run.  
- Adjustments require:
  - Governance sign-off,  
  - Version history updates,  
  - Regression tests for replay determinism.

---

### 🔒 Deterministic behavior requirements

#### Idempotency

Final outputs must be **idempotent**:

- Final STAC Items and downstream products are keyed by `(radar_id, volume_id, product_code)`.  
- Reprocessing with identical:
  - Inputs,  
  - Code,  
  - Config,  
  - Seeds,  

  yields **bit-identical** outputs (within defined numeric tolerances).

#### Replay safety

Under WAL/queue replay:

- Watermarks advance identically.  
- Windows open/close at the same event times.  
- Final volume set and manifests are identical.

Therefore:

- No `now()` / wall-clock use inside business logic.  
- Any randomness must be:
  - Seeded deterministically,  
  - Logged in PROV & telemetry.

#### STAC, graph, and CARE integration

- **STAC**:
  - Preview products (if cataloged) → preview collections.  
  - Final products → authoritative NEXRAD collections.  
  - Required properties include:
    - `nexrad:radar_id`, `nexrad:volume_id`, `nexrad:vcp`,  
    - `kfm:watermark_lag`, `kfm:finalization_delay`,  
    - `openlineage:runId`, `kfm:provenance_ref`, `kfm:telemetry_ref`.

- **Neo4j**:
  - Node types:
    - `:RadarVolume`, `:RadarProduct`, `:RadarScanRun`.  
  - Key relationships:
    - `(:RadarVolume)-[:HAS_PRODUCT]->(:RadarProduct)`,  
    - `(:RadarProduct)-[:PRODUCED_BY]->(:RadarScanRun)`.

- **CARE & masking**:
  - If NEXRAD derivatives are combined with:
    - Tribal land boundaries,  
    - Emergency response or shelter locations,  
    - Critical infrastructure,  

    then public-facing layers must apply:

    - Spatial generalization (e.g., H3), and/or  
    - Redaction, per `docs/standards/data-generalization/`.

---

## 🧪 Validation & CI/CD

All **atmospheric pipelines** implementing this pattern must pass the following QA/CI checks:

- **Watermark Drift Check**  
  - Ensure computed watermarks and window closures **match** across replay scenarios.

- **Replay Consistency Check**  
  - Given a fixed input corpus:
    - Final volume IDs and counts match,  
    - STAC manifests and key metadata fields match.

- **Volume Completeness Audit**  
  - For each final volume:
    - All expected tilts/cuts present for the VCP,  
    - No unexpected duplicates or missing scans.

- **VCP-Delay Enforcement Test**  
  - Validate that effective delays conform to config for each VCP and SAILS/MESO state.

- **STAC Integrity Test**  
  - Validate STAC Collections/Items against KFM STAC schemas and profiles.

- **Telemetry Coverage Test**  
  - Confirm telemetry records exist per run with:
    - Latency distributions,  
    - Watermark lag,  
    - Finalization delay,  
    - Volume counts,  
    - Energy & CO₂e estimates.

CI workflows (e.g., `.github/workflows/atmo-nexrad-watermarks.yml`) must **fail** when:

- Any of the above checks fail, or  
- Required STAC/PROV/telemetry artifacts are missing or invalid.

---

## 🧠 Story Node & Focus Mode Integration

NEXRAD products governed by this pattern power multiple atmospheric Story Nodes, including:

- **“Fast Storms, Stable Data”**  
  - Focus: why UX remains stable during rapidly evolving convective events.  

- **“Radar Volumes & Flash Flood Storylines”**  
  - Focus: how finalized volumes feed hydrology and flood-risk narratives.

Pattern requirements:

- Story Nodes must reference:
  - Specific NEXRAD dataset versions, volume IDs, and STAC Items,  
  - Associated PROV bundles (so users can inspect lineage).

- Focus Mode should support:
  - Toggling **preview vs final** visualization where appropriate,  
  - Displaying finalization delay and watermark lag for each volume,  
  - Indicating when data is **within** a finalization window (i.e., caution that more data is pending).

---

## 🕰️ Version History

| Version  | Date       | Author / Steward                          | Summary                                                        |
|----------|------------|-------------------------------------------|----------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | Atmo Pipelines + FAIR+CARE Council        | Initial unified NEXRAD watermark & finalization delay pattern under KFM v11.2.4. |

---

<div align="center">

🌩️ **Kansas Frontier Matrix — Atmospheric Pipelines Division**  

[📁 Atmo Pipelines Index](../../README.md) ·  
[📐 Event-Driven Ingest Pattern](../../../patterns/event-driven-deterministic-ingest.md) ·  
[⚖️ Root Governance](../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📦 Releases](../../../../../releases/)

</div>