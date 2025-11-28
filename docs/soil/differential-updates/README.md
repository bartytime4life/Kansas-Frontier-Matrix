---
title: "🧭 KFM v11.2.2 — Differential Soil Updates (SDA + gNATSGO) · Deterministic Tile-Level Refresh (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/soil/differential-updates/README.md"
version: "v11.2.2"
last_updated: "2025-11-28"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"
signature_ref: "../../../../releases/v11.2.2/signature.sig"
attestation_ref: "../../../../releases/v11.2.2/slsa-attestation.json"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/soil-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/soil-differential-updates-v11.2.2.json"
lineage_schema: "../../../../schemas/lineage/soil-refresh-lineage-v2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"

status: "Active / Enforced"
doc_kind: "Pipeline Runbook"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/soil"
  applies_to:
    - "sda"
    - "gnatsgo"
    - "differential-updates"
    - "stac"
    - "lineage"
    - "observability"

semantic_intent:
  - "soil-data"
  - "differential-ingestion"
  - "deterministic-refresh"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "Environmental (non-sensitive)"
sensitivity_level: "None"
public_exposure_risk: "Low"

metadata_profiles:
  - "STAC 1.0.0"
  - "DCAT 3.0"
  - "PROV-O"
  - "FAIR+CARE"

immutability_status: "version-pinned"
doc_uuid: "urn:kfm:doc:pipelines:soil:differential-updates:v11.2.2"
semantic_document_id: "kfm-pipelines-soil-differential-updates-v11.2.2"
event_source_id: "ledger:pipelines-soil-differential-updates-v11.2.2"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
diagram_profiles:
  - "mermaid-flowchart-v1"
  - "mermaid-timeline-v1"
---

<div align="center">

# 🧭 **KFM v11.2.2 — Differential Soil Updates (SDA + gNATSGO)**  
### Deterministic Tile-Level Refresh for USDA Soil Products  
`docs/pipelines/soil/differential-updates/README.md`

**Purpose:**  
Implement **content-hash-based differential ingestion** for USDA SDA and gNATSGO soil tiles, reducing compute by 40–60% while preserving strict lineage, CARE protections, and deterministic correctness across all dependent layers.

</div>

---

## 📘 Overview

The **Differential Soil Updates pipeline** introduces a unified **Tile Update Engine** that evaluates each SDA / gNATSGO tile by:

1. Reading STAC metadata (`properties.updated`, `checksum:multihash`, `kfm:tile_id`).  
2. Computing or verifying a **SHA-256 checksum**.  
3. Comparing against the **Soil Tile Registry**.  
4. **Skipping tiles** that have not changed.  
5. **Re-ingesting only new or modified tiles** with deterministic upserts keyed by checksum.

Effects:

- Shorter weekly soil runs.  
- Fewer redundant reads/writes and lower CO₂e footprint.  
- Restart-safe, rollback-safe, and WAL-aligned behavior.  
- Stable joins for all downstream layers (raster + vector + graph).

---

## 🧱 Soil Tile Registry (PostgreSQL)

The **Soil Tile Registry** provides:

- Deterministic keys for each tile.  
- Change detection anchors.  
- WAL alignment and restart safety.  
- Basis for PROV-O lineage.

Example schema (conceptual):

    create table if not exists soil_tile_registry (
      tile_id           text primary key,
      collection        text not null,         -- 'SDA' | 'gNATSGO'
      stac_item_id      text not null,
      stac_asset_href   text not null,
      src_updated_at    timestamptz not null,
      src_checksum      text not null,         -- SHA-256
      last_ingested_at  timestamptz,
      last_status       text,                  -- 'ingested' | 'skipped' | 'failed'
      last_run_id       text
    );

Every tile record provides a stable anchor for:

- ETL decisions (new / changed / unchanged).  
- Rollback pointers.  
- Audit logs and drift checks.

---

## 🔍 Change Detection Logic

In pseudocode, the update engine behaves as:

    def detect_changes(stac_index, registry):
        for asset in stac_index.assets(collections=['SDA', 'gNATSGO']):
            tile_id = derive_tile_id(asset)             # e.g., "11/354/687"
            new_checksum = sha256(asset.bytes)
            new_updated  = asset.properties['updated']

            prev = registry.get(tile_id)
            if not prev:
                yield ('new', tile_id, asset, new_checksum, new_updated)
            elif prev.src_checksum != new_checksum or prev.src_updated_at != new_updated:
                yield ('changed', tile_id, asset, new_checksum, new_updated)
            else:
                yield ('unchanged', tile_id, asset, prev.src_checksum, prev.src_updated_at)

Key properties:

- **Deterministic:** Same inputs, same classification.  
- **Restart-safe:** Classification derives solely from registry + STAC, not intermediate states.  
- **WAL-aligned:** Each tile action becomes a single WAL segment, aiding recovery and reconciliation.

---

## 🧮 DAG Pattern (Airflow / LangGraph / Prefect)

A typical orchestrator flow:

1. **List & Map**  
   - Enumerate STAC assets; expand into tile-level tasks per collection.  

2. **Branch**  
   - `unchanged` → **skip** (record telemetry, no ETL).  
   - `new` / `changed` → **ingest** path.  

3. **Ingest** (for `new` / `changed`)  
   - Read source asset.  
   - Parse horizons + attributes.  
   - Apply KFM soil normalizations (units, CRS, attributes).  
   - Generate GeoParquet layers.  
   - Generate COGs if raster products needed.  
   - Run Great Expectations checks.  
   - Emit OpenTelemetry + OpenLineage events.  

4. **Deterministic Upsert**  
   - Keyed by: `"{collection}:{tile_id}:{src_checksum}"`  

5. **Registry Update**  
   - Update per-tile record with:
     - `last_ingested_at`  
     - `last_status`  
     - `last_run_id`  
     - `src_checksum`, `src_updated_at`

---

## 🗺️ STAC Expectations (Soil Tiles)

Each SDA/gNATSGO STAC Item must include the following **asset-level** fields:

    {
      "href": "s3://kfm/soil/gnatsgo/tiles/11/354/687.parquet",
      "type": "application/x-parquet",
      "roles": ["data"],
      "checksum:multihash": "1220b8f3…",
      "kfm:tile_id": "11/354/687",
      "updated": "2025-11-12T06:04:00Z"
    }

Minimum STAC requirements (KFM-STAC v11):

- `kfm:tile_id` MUST be unique within collection.  
- `checksum:multihash` MUST be present and accurate.  
- `updated` MUST reflect **source** last-updated time (not pipeline ingestion time).  
- Item-level provenance must reference USDA source metadata and version (SDA / gNATSGO release tags).

---

## 🔗 Stable Join Rules

Downstream dependencies (e.g., soil suitability, hydrology-soil joins, archaeology-soil overlays) MUST join on:

- `(tile_id, src_checksum)`

This:

- Freezes downstream interpretation to a precise source snapshot.  
- Prevents silent recomputation of dependent products during stable releases.  
- Enables multiple **soil_release** tags without ambiguity.

Recommended release marker for datasets:

- `soil_release = "2025.11"`

---

## 📓 WAL Requirements

Each tile flow emits a **Write-Ahead Log entry**:

    run_id, tile_id, phase, status, started_at, finished_at, src_checksum, notes

Supports:

- **Restart** after failure at tile granularity.  
- **Point-in-time recovery** to any prior run.  
- **Reconciliation** between registry state and STAC catalog.  

WAL records must be:

- Append-only.  
- Immutable once written.  
- Correlated with OpenLineage run_ids.

---

## 📈 Observability Specification

**Counters**

- `soil.tiles.scanned`  
- `soil.tiles.changed`  
- `soil.tiles.skipped`  
- `soil.tiles.ingested`  

**Timers (histograms)**

- Per-tile ingest duration.  
- Per-phase (parse → normalize → write) latency.

**Events**

- OpenTelemetry logs for:
  - Checksum mismatches.  
  - Great Expectations failures.  
  - Registry write failures.  
- OpenLineage spans for:
  - Tile read.  
  - Tile transform.  
  - Tile upsert.

---

## ♻️ Rollback Procedure

Because artifacts are keyed by `(collection, tile_id, src_checksum)`:

- **Rollback never deletes data**.  
- To rollback, simply move lineage pointers back to a prior `(tile_id, checksum)` set.  
- All variants of a tile may coexist — only references shift.  

Rollback steps:

1. Select previous release or run_id to restore.  
2. Update join tables / STAC Item references to the earlier checksum set.  
3. Confirm with regression checks on derived products.

---

## 🧮 Expected Impact

| Category  | Reduction / Effect | Notes                                                  |
|----------|--------------------|--------------------------------------------------------|
| Compute  | 40–60%             | Most tiles remain unchanged between USDA updates      |
| I/O      | 50%+               | Heavy parquet scans skipped for unchanged tiles       |
| Wall-time| 35–60%             | Faster DAG completion ⇒ more frequent refresh cycles |
| Carbon   | Lower              | Fewer workers and shorter runtimes                    |

---

## 📂 Directory Layout

    docs/pipelines/soil/differential-updates/
    ├── 📄 README.md                         # This file
    ├── 📁 sql/
    │   └── 📄 soil_tile_registry.sql        # Registry DDL and migrations
    ├── 📁 notebooks/
    │   └── 📄 validation.ipynb              # QA checks for changed tiles
    ├── 📁 dags/
    │   └── 📄 differential_soil_dag.py      # Example orchestrator DAG
    ├── 📁 examples/
    │   └── 📄 stac-assets.json              # Example STAC asset payloads
    └── 📁 configs/
        └── 📄 soil-differential-config.yaml # Orchestrator + registry configuration

---

## 🧭 Story Node & Focus Mode Integration

**Focus Prompt Example:**  
> “Explain how KFM decides whether an SDA or gNATSGO tile needs re-ingestion, including checksum comparisons, lineage decisions, and rollback behavior.”

Focus Mode v3 should:

- Describe checksum-based comparison with STAC + registry state.  
- Explain deterministic branching (new / changed / unchanged).  
- Highlight `(tile_id, src_checksum)` as the central lineage anchor.  
- Clarify how rollback works by shifting lineage pointers, not deleting data.  

Atmospheric + soil Story Nodes may combine:

- Soil property changes (e.g., updated horizons).  
- Land-use / hydrology overlays.  
- Archaeological affordances tied to soil changes.

---

## 🕰️ Version History

| Version  | Date       | Notes                                                     |
|----------|------------|-----------------------------------------------------------|
| v11.2.2  | 2025-11-28 | Upgraded to KFM-MDP v11.2.2; emoji tree; telemetry schemas |
| v11.2.0  | 2025-11-20 | Introduced differential update spec, lineage v2, rollback |
| v11.1.x  | 2025-10-10 | Registry + checksum enforcement                           |
| v11.0.x  | 2025-09-01 | Initial soil pipeline modernization                       |

---

<div align="center">

### 🔗 Footer  

[🌐 KFM Home](../../../README.md) · [📚 Standards](../../../standards/README.md) · [📦 STAC Catalog](../../../data/stac/)

</div>
