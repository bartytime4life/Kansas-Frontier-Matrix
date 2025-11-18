---
title: "🔁 Kansas Frontier Matrix — Unified Reliable Pipelines & Blue/Green Promotion Architecture v11 (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/architecture/reliable-pipelines.md"
version: "v11.0.0"
last_updated: "2025-11-18"
review_cycle: "Quarterly / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/pipelines-reliable-v2.json"
governance_ref: "../../docs/standards/governance/DATA-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Active / Enforced"
doc_kind: "Architecture · Standard"
intent: "reliable-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "CARE / Indigenous-partnered · Operational Safety"
sensitivity_level: "Medium"
public_exposure_risk: "Low"
indigenous_rights_flag: true
data_steward: "KFM FAIR+CARE Council"
risk_category: "Operational Reliability"
redaction_required: false
provenance_chain:
  - "src/pipelines/architecture/reliable-pipelines.md@v1.0.0"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.3.1"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.4.0"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.4.1"
  - "src/pipelines/architecture/reliable-pipelines.md@v10.4.2"
previous_version_hash: "<previous-sha256>"
ontology_alignment:
  cidoc: "E7 Activity"
  schema_org: "TechArticle"
  owl_time: "TemporalEntity"
  prov_o: "prov:Plan"
  geosparql: "geo:FeatureCollection"
json_schema_ref: "../../schemas/json/pipelines-reliable-pipelines-v11.schema.json"
shape_schema_ref: "../../schemas/shacl/pipelines-reliable-pipelines-v11-shape.ttl"
doc_uuid: "urn:kfm:doc:pipelines-reliable-pipelines-v11.0.0"
semantic_document_id: "kfm-doc-pipelines-reliable-pipelines"
event_source_id: "ledger:src/pipelines/architecture/reliable-pipelines.md"
immutability_status: "mutable-plan"
doc_integrity_checksum: "<sha256>"
ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summaries"
  - "semantic-highlighting"
  - "a11y-adaptations"
ai_transform_prohibited:
  - "execution-control-changes"
  - "governance-weakening"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
jurisdiction: "Kansas / United States"
classification: "Public Document"
role: "architecture"
lifecycle_stage: "stable"
ttl_policy: "Review required every 12 months"
sunset_policy: "Superseded upon new protocol release"
---

<div align="center">

# 🔁 **Kansas Frontier Matrix — Unified Reliable Pipelines & Blue/Green Promotion Architecture v11**  
`src/pipelines/architecture/reliable-pipelines.md`

**Purpose**  
Define the reliable pipelines pattern for KFM: **blue/green dataset promotion, WAL checkpoints, retries, lineage diffs, and instant rollback**, wired into CI/CD, telemetry, and governance, and aligned with **Data & AI pipeline reliability**.

</div>

--- ✦ ---

## 📘 1. Overview

This document defines the canonical “boringly safe” data and model update pattern for the Kansas Frontier Matrix (KFM):

> Always build and validate on a non-live **green** copy, then atomically flip the pointer from **blue → green** when it’s proven safe, with **WAL-backed retries and instant rollback**.

**Scope**

- **Datasets:** tabular, vector, raster, tiles, embeddings, graph loads.  
- **Metadata:** STAC/DCAT, JSON-LD, PROV-O, Neo4j graph projections.  
- **AI/ML:** embeddings, classifiers, Focus Mode models, explainability overlays.  
- **Downstream:** web maps (MapLibre), 3D (Cesium), Story Nodes, Focus Mode v2.5+.

All pipelines described here MUST comply with:

- **MCP-DL v6.3** (documentation-first)  
- **KFM-MDP v11** (Markdown & docs protocol)  
- **FAIR+CARE**, energy & carbon telemetry, and immutable provenance  

---

## 🎯 2. Purpose & Consumers

The purposes of this architecture are to:

- Provide a **single, enforceable pattern** for all KFM pipelines and updaters.  
- Ensure **idempotent, observable, rollback-safe** behavior across ingestion, ETL, graph updates, and publishing.  
- Serve as **the single source of truth** for blue/green dataset promotion and rollback.

**Primary consumers**

- Pipeline authors (Python, SQL, Neo4j, STAC tooling).  
- Architecture and SRE teams.  
- FAIR+CARE Council and governance bodies reviewing reliability & cultural risk.

---

## 📍 3. Scope

### In Scope

All pipeline code under `src/pipelines/**` that:

- Reads from `data/sources/**`, `data/raw/**`, or external APIs/streams.  
- Writes to `data/work/**`, `data/processed/**`, `data/stac/**`, or Neo4j.  

All pipelines that:

- Perform ETL (batch or streaming).  
- Update KFM knowledge graph or catalogs.  
- Feed Focus Mode, Story Nodes, maps, tiles, or public APIs.

### Out of Scope

- Pure frontend logic with no pipeline involvement.  
- One-off notebooks that never promote artifacts or models to production.  
- External providers’ internal architectures.

---

## 📚 4. Definitions

- **Pipeline / Updater** — repeatable process ingesting, transforming, validating, and publishing data/knowledge into KFM.  
- **Trigger** — Cron, event, or manual signal that launches a run, encapsulated in a trigger envelope.  
- **Idempotency Key (run-level)** — hash derived from trigger envelope and config to prevent duplicate processing.  
- **Natural Key (record-level)** — minimal, stable identity (e.g., `(station_id, date)`).  
- **Content Hash** — hash of the normalized, non-ephemeral record.  
- **Blue Dataset** — currently live dataset bundle.  
- **Green Dataset** — candidate bundle under validation.  
- **Checkpoint** — persisted cursor for safe resume (offset, page, date).  
- **WAL** — append-only log of intended effects and steps prior to mutation.  
- **Promotion Contract** — machine-readable “what must be true before green goes live.”  
- **Lineage Diff** — machine and human readable summary of changes between blue and green.  

---

## 🏗 5. Directory Layout (Reference Pattern)

This layout shows where reliable-pipeline assets live and how they relate to data, WAL, manifests, and CI.

~~~text
src/
  pipelines/
    architecture/
      reliable-pipelines.md       ← this file
    cli/
      kfm-dataset-build.py        ← builds green (ingest → normalize → index → embed → tile)
      kfm-dataset-validate.py     ← runs gates, writes validation reports
      kfm-dataset-promote.py      ← atomic blue/green promotion + rollback hooks
      kfm-lineage-diff.py         ← computes PROV-O + STAC/DCAT diffs (blue vs green)
    libs/
      wal/
        wal_writer.py             ← append-only write-ahead log helpers
        wal_reader.py             ← replay / debug
      promotion/
        promotion_plan.py         ← promotion contract model
        pointer_switch.py         ← file/registry/graph pointer flips
      validation/
        schema_check.py           ← schema + contract checks
        stac_dcat_check.py        ← metadata checks
        geo_spatial_check.py      ← GeoJSON/GeoTIFF/GeoSPARQL checks
        ai_drift_bias_check.py    ← model drift & bias gates
        energy_a11y_check.py      ← telemetry budgets & a11y gates

data/
  work/
    staging/
      hydrology_v10/
        v10.4.2-green/            ← build target (non-live)
        logs/
          wal/
            2025-11-18T02-31Z_ingest.ndjson
            2025-11-18T02-42Z_normalize.ndjson
            2025-11-18T02-55Z_embed.ndjson
        validation/
          schema.json
          stac.json
          ai_drift.json
          energy_a11y.json

  releases/
    hydrology_v10/
      blue/                       ← currently live dataset bundle
      green/                      ← candidate live; promoted after checks
      current -> ./blue           ← atomic symlink / pointer to live
      history/
        v10.4.1/
          manifest.zip
          sbom.spdx.json
          lineage.graph.jsonld
        v10.4.2/
          manifest.zip
          sbom.spdx.json
          lineage.graph.jsonld
          lineage.diff.json       ← computed by kfm-lineage-diff.py

wal/
  hydrology_v10/
    2025-11-18T02-31Z_ingest.ndjson
    2025-11-18T02-42Z_normalize.ndjson
    2025-11-18T02-55Z_embed.ndjson

.github/
  workflows/
    dataset-promotion-hydrology.yml   ← reference GitHub Action (Appendix A)
~~~

---

## 🔑 6. Core Concepts

### 6.1 Blue/Green Datasets

- **Blue** — the currently live, query-facing dataset bundle.  
  - Used by Neo4j loaders, APIs, web, Story Nodes, Focus Mode.  
  - Always healthy and fully validated.  

- **Green** — the candidate replacement for blue.  
  - Built in staging (`data/work/staging/.../v{N}-green`).  
  - Subject to all validation gates, drift/bias checks, and governance approval.  
  - Becomes live **only** via atomic pointer flip.  

**Implementation Patterns**

1. **Filesystem pointer**

- `data/releases/{dataset}/{blue,green}/`  
- `data/releases/{dataset}/current -> ./blue` or `./green`  

2. **Registry / graph pointer**

- `(:Dataset {slug:"hydrology_v10"})-[:LIVE_AT]->(:Release {version:"v10.4.2"})`

### 6.2 Write-Ahead Log (WAL)

Every critical step writes a WAL entry before mutating state:

~~~json
{
  "wal_version": "v1",
  "dataset": "hydrology_v10",
  "release": "v10.4.2",
  "step_id": "normalize",
  "seq": 2,
  "inputs": [
    "s3://kfm-raw/hydrology/noaa/...",
    "file://data/work/staging/hydrology_v10/v10.4.2-green/raw/*.parquet"
  ],
  "outputs": [
    "file://data/work/staging/hydrology_v10/v10.4.2-green/normalized/*.parquet"
  ],
  "started_at": "2025-11-18T02:42:10Z",
  "finished_at": "2025-11-18T02:42:42Z",
  "exit_code": 0,
  "hashes": {
    "inputs_sha256": "...",
    "outputs_sha256": "..."
  },
  "telemetry": {
    "energy_kwh": 0.12,
    "carbon_kgco2e": 0.03,
    "node": "etl-node-01"
  }
}
~~~

**WAL guarantees**

- **Replayability** — re-run from last successful step (seq) without guessing state.  
- **Auditability** — full trace of inputs/outputs and resource use.  
- **Debuggability** — post-mortem of failures.

### 6.3 Promotion Contracts

Promotion contracts define what must be true before green becomes live:

- Identity: `dataset_slug`, `candidate_version`, `blue_version`.  
- Required checks:
  - Schema & data contracts.  
  - STAC/DCAT completeness and validity.  
  - Spatial & temporal sanity.  
  - AI drift & bias thresholds.  
  - Energy & carbon budgets.  
  - A11y & UX contracts (where applicable).  
- Approval policy:
  - Auto-approve if all gates pass & diffs within allowed bounds.  
  - Manual review for sensitive or high-impact deltas; FAIR+CARE review if needed.  

Contracts live as:

- Schema: `schemas/pipelines/promotion-contract-v1.json`  
- Instances: `data/releases/{dataset}/{version}/promotion-contract.json`

### 6.4 Lineage Diff (Blue vs Green)

For each candidate release:

1. Capture lineage:

- `lineage-blue.graph.jsonld`  
- `lineage-green.graph.jsonld`  

2. Run `kfm-lineage-diff.py` to produce:

- `lineage.diff.json` (machine-readable)  
- `lineage.diff.md` (human-readable, linked into governance docs)  

Diff focuses on:

- Entity & count changes (features, sites, tiles, rasters, embeddings, nodes/edges).  
- Spatial changes (bboxes, H3 coverage deltas).  
- Temporal changes (slices added/removed, coverage shifts).  
- Model & pipeline hashes (model version, hyperparameters, training-data snapshots).  
- Governance flags (Indigenous/tribal/community-sensitive impacts).

### 6.5 Retry & Rollback Model

- **Retry**  
  - Each step may be retried N times with backoff.  
  - WAL consulted to identify failed step and safe resume point.  

- **Rollback**  
  - If post-promote monitors deem green unhealthy:
    - Immediately flip pointer back to blue.  
    - Emit rollback WAL entry and governance event.  
    - Blue must remain intact and queryable at all times.  

---

## 🔁 7. Lifecycle: From Staging to Live

### 7.1 High-Level Flow (Mermaid)

~~~mermaid
flowchart LR
  subgraph Staging
    A[Ingest to staging vN-green]
    B[Transform / Normalize]
    C[Index / Embed / Tile]
  end

  subgraph Validation
    D[Schema & Contracts]
    E[STAC/DCAT & Geo Checks]
    F[AI Drift & Bias Gates]
    G[Energy & A11y Budgets]
  end

  subgraph Promotion
    H[Lineage Diff (blue vs green)]
    I[Approval (Auto/Manual)]
    J[Atomic Pointer Flip<br/>blue → green]
  end

  subgraph PostPromote
    K[Canary Queries & Dashboards]
    L[Runtime Error & Latency Monitors]
    M[Focus Mode / Story Node Smoke Tests]
  end

  A --> B --> C --> D
  D --> E --> F --> G --> H --> I --> J --> K --> L --> M

  I -->|reject| R[Fail / Rollback (stay on blue)]
  K -->|alert| R
  L -->|alert| R
  M -->|alert| R
~~~

### 7.2 Detailed Steps

1. **Stage (Build Green)**  
   - CLI: `kfm-dataset-build.py`  
   - Ingest raw data → staging `v{N}-green/raw/`  
   - Transform/normalize → curated schema  
   - Index, embed, tile as needed  
   - Write WAL entries for each step  

2. **Validate (Run Gates)**  
   - CLI: `kfm-dataset-validate.py`  
   - Gates:
     - Schema & contracts (`docs/contracts/data-contract-*.json`)  
     - STAC/DCAT validity (schemas, extents, license, provenance)  
     - Spatial/Geo: topology, projection, GeoSPARQL  
     - AI Drift & Bias: metrics vs blue  
     - Telemetry: energy, carbon, runtime, storage vs budgets  
   - Outputs: `validation/*.json` and CI artifacts  

3. **Lineage Diff**  
   - CLI: `kfm-lineage-diff.py`  
   - Inputs: blue/green lineage graphs  
   - Outputs: `lineage.diff.json`, `lineage.diff.md`  

4. **Review & Approval**  
   - Auto-approval when low-risk.  
   - Manual review for larger diffs or CARE-sensitive changes.  

5. **Atomic Pointer Flip**  
   - CLI: `kfm-dataset-promote.py`  
   - Flip filesystem/registry pointer in a single operation.  
   - Update registry/graph pointers transactionally.  
   - Append new release to `history/`.  

6. **Post-Promote Monitoring**  
   - Canary queries (APIs, maps, Story Nodes, Focus Mode).  
   - Monitors: error rates, latency, cache misses, tile failures, ML performance canaries.  
   - If instability → rollback to blue, record incident.

---

## ✅ 8. Reliability Guarantees

The reliable pipelines architecture guarantees:

1. **Safety**

- No direct writes to live blue data.  
- Always promote via green + pointer flip.  
- Blue remains viable for immediate rollback.

2. **Determinism & Reproducibility**

- WAL logs deterministic steps with hashes.  
- Each release has **manifest + SBOM + lineage**.  
- Re-running with same inputs & config produces identical hashes or explicit diffs.

3. **Governance & Provenance**

- Every promotion emits:
  - Promotion contract instance.  
  - Lineage diff.  
  - Telemetry summary.  
- These are attached to:
  - Governance ledger.  
  - FAIR+CARE evaluations.  
  - Story Node / Focus Mode release logs.

4. **Observability**

- Telemetry wired via YAML `telemetry_ref` & `telemetry_schema`.  
- Dashboards show:
  - Energy/carbon time series.  
  - Success/failure rates, retries, DLQ entries.  
  - Promotion history & rollbacks.

---

## 🧪 9. CI/CD Integration Model (Hydrology v10 Example)

The reference GitHub Action orchestrates blue/green promotion for `hydrology_v10`:

- **Trigger sources**: `workflow_dispatch`, `push`, scheduled.  
- **Jobs**:
  1. `build-green`  
  2. `validate-green`  
  3. `lineage-diff`  
  4. `promote-green`  
  5. `post-promote`  

Each job:

- Runs in a clean environment.  
- Uses `python -m` or `kfm-*` CLIs.  
- Uploads reports and artifacts.  
- Fails hard on any gate violation.

(See the full YAML in the snippet you provided; this doc defines the architecture and patterns those workflows must follow.)

---

## ✅ 10. Promotion Checklist (Copy-Paste)

Use this checklist in governance templates, PRs, and CI logs for any dataset promotion.

1. **Build Green**

- [ ] Raw data ingested to `staging/.../v{N}-green`.  
- [ ] Transform/normalize completed.  
- [ ] Indexes/tiles/embeddings built.  
- [ ] WAL entries present for all steps.  

2. **Run Gates**

- [ ] Schema & contract checks PASSED.  
- [ ] STAC/DCAT valid; extents and licenses consistent.  
- [ ] Geo & topology checks PASSED.  
- [ ] AI drift & bias within thresholds.  
- [ ] Energy & carbon within budgets.  
- [ ] A11y/UX checks (if applicable) PASSED.  

3. **Lineage Diff**

- [ ] Blue vs green diffs computed.  
- [ ] High-risk changes reviewed.  
- [ ] FAIR+CARE implications assessed.  

4. **Approval**

- [ ] Promotion contract satisfied.  
- [ ] Required sign-offs recorded (including Indigenous-partnered/CARE approvals where relevant).  

5. **Atomic Promotion**

- [ ] Pointer flipped (blue → green).  
- [ ] New release recorded in history with manifest + SBOM.  
- [ ] CI green.  

6. **Post-Promote**

- [ ] Canary queries OK.  
- [ ] Monitors stable (no elevated errors/latency).  
- [ ] Focus Mode / Story Node smoke tests pass.  
- [ ] No rollback triggered within observation window.

---

## 🧯 11. Failure Modes & Playbook

### 11.1 Build Failure (Staging)

- Signal: `kfm-dataset-build` exits non-zero; WAL entries show `exit_code != 0`.  
- Actions:
  - Do not modify blue or green pointers.  
  - Use WAL to pinpoint broken step and inputs.  
  - Fix cause; rerun from last successful `seq`.  

### 11.2 Validation Gate Failure

- Signal: `kfm-dataset-validate` marks gate(s) failed.  
- Actions:
  - Promotion contract fails.  
  - No pointer flip allowed.  
  - Investigate; if CARE gate fails, notify FAIR+CARE Council.

### 11.3 Post-Promote Regression

- Signal: canaries or monitors detect elevated error/latency or ML drift.  
- Actions:
  - Flip pointer back to blue (rollback).  
  - Emit rollback WAL + governance event.  
  - Attach lineage diff, WAL subset, and telemetry to postmortem.

### 11.4 Mixed State

- Design goal: never mix blue and green under a single live pointer.  
- If detected:
  - Roll back to last known-good blue release.  
  - Block further promotions until state is corrected.

---

## 🎯 12. Integration with Focus Mode & Story Nodes

Reliable pipelines provide stable, reproducible targets for:

- **Story Nodes v3**  
  - Nodes reference explicit dataset releases and lineage snapshots.  
  - Narratives can safely reference “Hydrology v10.4.2 (green→live on 2025-11-18)” with context.

- **Focus Mode v2.5+**  
  - Predictive overlays (e.g., climate futures) tied to specific releases.  
  - Explainability overlays (SHAP/LIME) bound to model versions & data snapshots.  

Reliability patterns ensure Focus Mode can always reconstruct the data context for any prior narrative.

---

## 🕰️ Version History

| Version | Date       | Author                               | Summary                                                                                     |
|--------:|------------|----------------------------------------|---------------------------------------------------------------------------------------------|
| v11.0.0 | 2025-11-18 | FAIR+CARE Council · Architecture WG   | Merged all prior reliable pipeline & blue/green patterns into a unified v11 architecture; added WAL, promotion contracts, lineage diffs, and telemetry v2 alignment. |
| v10.4.2 | 2025-11-18 | Architecture WG                       | Added Reliable Pipelines & Blue/Green Dataset Promotion spec; WAL, promotion contracts, lineage diffs, CI templates. |
| v10.4.1 | 2025-11-18 | Architecture WG                       | Refined v10.4 architecture; clarified orchestration patterns for Airflow/Dagster/Temporal. |
| v10.4.0 | 2025-11-15 | Pipeline Architecture Team            | Unified reliable pipeline spec; aligned with Markdown MDP v10.4 and ontology mappings.      |
| v10.3.1 | 2025-11-13 | Pipeline Architecture Team            | “Reliable Pipeline Architecture Guide”.                                                     |
| v1.0.0  | 2025-11-15 | ETL/Updaters Working Group            | Initial “Reliable Updaters” pattern.                                                        |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT License  
Unified Reliable Pipelines & Blue/Green Promotion Architecture v11 · FAIR+CARE Certified · Indigenous-Partnered · Sovereignty-Aware  
Diamond⁹ Ω / Crown∞Ω Ultimate Certified · MCP-DL v6.3  

[Back to Pipeline Architecture](../README.md)

</div>