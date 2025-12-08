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

## 1. 🧭 Purpose

This pattern defines the authoritative KFM v11.2.4 method for applying **event-time watermarks** and **finalization delays** to NEXRAD Level‑II ingestion.

It ensures that:

- No **partial-volume** products are published as “final”.  
- Event-time processing is **deterministic across replay** (WAL + reprocessing).  
- Downstream atmospheric products (Focus Mode, Story Nodes, Mesh Atlases, risk layers) see only **stable, reproducible volumes**.

It is a **specialization** of the **Event‑Driven Deterministic Ingestion & Promotion Pattern** for NEXRAD atmospheric data.

---

## 2. 📡 Why Event-Time Watermarks Matter

NEXRAD volume scans arrive:

- **Out of order**,  
- In **bursts**,  
- With **variable completion times** due to:
  - VCP mode,  
  - SAILS / MESO‑SAILS,  
  - AVSET / range‑dependent termination.

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

## 3. 🧱 Canonical Pattern Overview

### 3.1 Principles

- **Event time dominates ingest time**  
  - All windows and aggregations use `event_time` as the primary clock.  

- **Watermark definition**  
  - `watermark(event_time) = event_time - lateness_buffer`.  

- **Finalization** requires both:  
  - Observed volume completeness (all expected tilts/records), **and**  
  - A **VCP-specific finalization delay** to absorb late stragglers.

- **Idempotent final upsert**, keyed by:

  ```text
  (radar_id, volume_id, product_code)
  ```

  and version-tagged for STAC/graph.

### 3.2 Preview vs Final Layers

| Layer       | Purpose                    | When it Publishes                                 |
|------------|----------------------------|---------------------------------------------------|
| **Preview** | Early map responsiveness   | On watermark closure (may be partial / provisional) |
| **Final**   | Stable, authoritative data | After VCP-specific delay & volume completeness    |

Rules:

- Preview products must be **visually distinct** and clearly marked as **non-final**.  
- Only final products are:
  - Indexed into canonical STAC/DCAT collections,  
  - Inserted into the production Neo4j graph,  
  - Used as Story Node / Focus Mode baselines.

---

## 4. 📡 Implementation Model (Streaming)

This pattern is typically implemented using streaming frameworks (e.g., Flink SQL, Beam), but the semantics are framework-independent.

### 4.1 Event-time & watermark definition (Flink SQL example)

Preview window (1‑minute tumbling) with watermark lag:

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

This guarantees:

- Event-time order and late data handling are explicit.  
- Lateness tolerance (`2` minutes here) is **versioned configuration**, not a magic constant.

### 4.2 Finalization stage (volume aggregation)

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

- Aggregation waits until the **current watermark** passes  
  `MAX(event_time) + finalization_delay`.  
- Finalization delay is **VCP-aware** (Section 5).  
- A given `(radar_id, volume_id, product_code)` emits **exactly one final record**.

---

## 5. 🕒 Choosing the Finalization Delay

Finalization delay **must** be tied to the VCP and operational behavior of the radar:

| VCP                     | Typical Duration | Recommended Base Delay |
|-------------------------|------------------|------------------------|
| **12 / 212**            | ~4.5–5 min       | 5 min                  |
| **215 / 35**            | ~6–7 min         | 7 min                  |
| **SAILS / MESO‑SAILS**  | Low-level bursts | +1 min additional buffer |

Guidelines:

- The **effective delay** per volume is:

  ```text
  finalization_delay(vcp, sails_state) =
    base_delay(vcp) + sails_buffer(vcp, sails_state)
  ```

- Finalization delay parameters must be:

  - Captured in configuration (YAML/JSON) under `src/pipelines/atmo/nexrad/config/`,  
  - Logged in PROV‑O as part of the `Activity` parameters,  
  - Included in telemetry for each run.

Changes to delay logic are **backward-incompatible behavior changes** and must:

- Bump the pattern version or pipeline version, and  
- Be documented in Version History with rationale.

---

## 6. 🔒 Deterministic Behavior Requirements

### 6.1 Idempotency

Final outputs must be **idempotent**:

- Final STAC Items and downstream products are keyed by:

  ```text
  (radar_id, volume_id, product_code)
  ```

- Reprocessing the same input stream with the same:

  - Code version,  
  - Config,  
  - Seeds,  

  must generate **bit-identical outputs** (up to allowed floating-point tolerances).

### 6.2 Replay safety

Under WAL or queue replay:

- Watermarks must advance identically;  
- Windows must open and close at the same **event times**;  
- The set of final volumes produced must be identical.

Requirements:

- No hidden `now()` in logic;  
- No dependencies on wall-clock ingestion order;  
- All randomness must use fixed, logged seeds.

### 6.3 STAC, graph, and CARE integration

- **STAC**:
  - Preview products (if cataloged) must live under a **preview** namespace/collection,  
  - Final products are cataloged under the authoritative NEXRAD Collection,  
  - STAC Item properties must include:
    - `nexrad:radar_id`, `nexrad:volume_id`, `nexrad:vcp`,  
    - `kfm:watermark_lag`, `kfm:finalization_delay`,  
    - `openlineage:runId`, `kfm:provenance_ref`, `kfm:telemetry_ref`.

- **Neo4j**:
  - Nodes such as `:RadarVolume`, `:RadarProduct`, `:RadarScanRun` link:
    - `(:RadarVolume)-[:HAS_PRODUCT]->(:RadarProduct)`,  
    - `(:RadarProduct)-[:PRODUCED_BY]->(:RadarScanRun)`.

- **CARE & masking**:
  - When radar products intersect:
    - Tribal lands,  
    - Emergency response overlays,  
    - Sensitive infrastructure footprints,  

    views used in public contexts must apply:

    - Spatial generalization (e.g., H3), or  
    - Data suppression policies documented in PROV & audit logs.

---

## 7. 📁 Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            └── 📁 watermarks/
                📄 finalization-pattern.md      # ← This file
                📁 examples/
                │   📄 minimal-flow.md        # Small end-to-end example
                │   📄 replay-behavior.md     # Replay determinism analysis
                │   📄 qa-tests.md            # QA test matrix & edge cases
                └── 📁 design/
                    📄 vcp-delay-rationale.md # VCP-aware delay rationale

📁 src/
└── 📁 pipelines/
    └── 📁 atmo/
        └── 📁 nexrad/
            ├── 📄 config_watermarks.yaml     # Lateness buffers & VCP delays
            ├── 📄 ingest_stream.py           # NEXRAD event ingestion
            ├── 📄 watermark_logic.py         # Event-time / watermark implementation
            ├── 📄 finalization_job.sql       # Streaming SQL / job definition
            └── 📄 stac_emit.py               # STAC Item & Collection emission

📁 data/
└── 📁 processed/
    └── 📁 atmo/
        └── 📁 nexrad/
            ├── 📁 preview/                   # Optional preview-only products
            └── 📁 final/                     # Final, watermark-stable products

📁 data/
└── 📁 stac/
    └── 📁 atmo/
        └── 📁 nexrad/
            ├── 📁 preview/                   # STAC Collections/Items for preview
            └── 📁 final/                     # STAC Collections/Items for final datasets
```

---

## 8. 🧪 QA / CI Checks

All **atmospheric pipelines** implementing this pattern must pass the following QA/CI checks (per dataset/product):

- **Watermark Drift Check**  
  - Verify that computed watermarks are **consistent across replays** and code versions.  

- **Replay Consistency Check**  
  - Run a controlled replay (same inputs) and assert:
    - Identical set of final volumes,  
    - Identical metadata and STAC manifests.

- **Volume Completeness Audit**  
  - Ensure final products include **all expected tilts/records** per VCP configuration.  
  - Flag missing cuts or abnormal scan counts.

- **VCP-Delay Enforcement Test**  
  - Confirm finalization delay is applied correctly per VCP and SAILS/MESO‑SAILS settings.  

- **STAC Integrity Test**  
  - Validate STAC Collections/Items against `KFM-STAC v11` profiles.  

- **Telemetry Coverage Test**  
  - Ensure telemetry entries exist, conforming to `patterns/nexrad-watermark-v1.json`, covering:
    - Watermark lag distributions,  
    - Event-to-final latency,  
    - Volume counts,  
    - Energy and CO₂e estimates per run.

CI workflows (e.g., `.github/workflows/atmo-nexrad-watermarks.yml`) must fail if:

- Any QA test fails, or  
- STAC/PROV/telemetry artifacts cannot be produced or validated.

---

## 9. 🧠 Story Node & Focus Mode Integration

NEXRAD watermarked products drive several atmospheric Story Nodes:

- **“Fast Storms, Stable Data”**  
  - Explains how event-time watermarks prevent map flicker and inconsistent products.  

- **“Radar Volumes & Flash Flood Storylines”**  
  - Uses finalized reflectivity/derivative fields as stable baselines for hydrology overlays.

Pattern requirements for Story Nodes:

- Story Nodes must reference:
  - Specific **dataset versions** and **volume IDs**, not generic “latest radar”.  
  - STAC IDs and PROV bundles for their underlying NEXRAD products.  

- Focus Mode should support:
  - Toggling **Preview vs Final** modes where appropriate,  
  - Showing watermarked latency metrics in an info panel (e.g., “this volume finalized X minutes after event-time due to VCP Y”),  
  - Highlighting any periods where data is **still within finalization delay windows** (i.e., not yet fully stable).

---

## 10. 🕰️ Version History

| Version  | Date       | Author / Steward              | Summary                                                       |
|----------|------------|------------------------------|---------------------------------------------------------------|
| v11.2.4  | 2025-12-07 | Atmo Pipelines + FAIR+CARE Council | Initial unified NEXRAD watermark & finalization delay pattern under KFM v11.2.4. |

---

<div align="center">

🌩️ **Kansas Frontier Matrix — Atmospheric Pipelines Division**  

[📁 Atmo Pipelines Index](../../README.md) ·  
[📐 Event-Driven Ingest Pattern](../../../patterns/event-driven-deterministic-ingest.md) ·  
[⚖️ Root Governance](../../../../standards/governance/ROOT-GOVERNANCE.md) ·  
[📦 Releases](../../../../../releases/)

</div>