---
title: "🌱 Kansas Frontier Matrix — Nightly Soil Ingest Validation Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/soil/nightly-validation.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x compliant"

status: "Active / Enforced"
doc_kind: "Pipeline Pattern"
header_profile: "standard"
footer_profile: "standard"

license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/pipelines-soil-validation-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-soil-validation-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-SOVEREIGNTY.md"
---

<div align="center">

# 🌱 **Kansas Frontier Matrix — Nightly Soil Ingest Validation Pipeline**  
### Deterministic · GE-Verified · Temporal STAC · Neo4j Lineage  
`docs/pipelines/soil/nightly-validation.md`

</div>

---

## 📘 Overview

This document defines the **authoritative, governed pattern** for performing **nightly ingest, validation, drift detection, STAC emission, and Neo4j lineage registration** for soil-model source data (e.g., USDA SDA, SSURGO, NRCS streams).

The pipeline is:

- **Deterministic & idempotent**  
- Compatible with **LangGraph DAG execution**  
- Backed by **lakeFS (or equivalent) snapshotting**  
- Fully integrated with **KFM Story Node and Focus Mode provenance**

Nightly runs evaluate:

1. **Checksum & Metadata Integrity**  
   - SHA-256, file size, partition counts, snapshot identifiers  
2. **Schema Validation**  
   - Column presence, type enforcement, categorical domain checks  
3. **Row-Level Quality**  
   - Non-null fields, allowed domain sets, record-count sanity  
4. **Delta Detection vs Prior Snapshot**  
   - Bytes, fragment count, schema drift, record deltas  
5. **Temporal STAC Item Emission**  
   - New STAC Item per run with temporal extent and provenance fields  
6. **Graph Lineage Upsert**  
   - Neo4j `:SoilIngestEvent` → `:Dataset` → `:STACItem` lineage

All emissions follow **DCAT 3.0**, **STAC 1.0.0**, and **PROV-O** crosswalks defined in KFM catalog standards.

---

## 🗂️ Directory Layout

```text
📁 repo-root/
├── 📁 docs/
│   └── 📁 pipelines/
│       └── 📁 soil/
│           └── 📄 nightly-validation.md         # This document (governed pattern)
├── 📁 src/
│   └── 📁 soil_ingest/
│       ├── 📄 validator.py                      # Main entrypoint (this pattern)
│       ├── 📁 utils/
│       │   ├── 📄 checksums.py                  # SHA-256, manifest hashes
│       │   ├── 📄 deltas.py                     # Delta & drift computation
│       │   ├── 📄 io.py                         # Snapshot loading, I/O helpers
│       │   └── 📄 stac.py                       # STAC item builders & serializers
│       ├── 📁 graph/
│       │   └── 📄 neo4j_loader.py               # Lineage upsert into Neo4j
│       ├── 📁 expectations/
│       │   ├── 📄 sda_checksum_suite.json       # Great Expectations suites: USDA SDA
│       │   └── 📄 nrcs_checksum_suite.json      # Great Expectations suites: NRCS
│       └── 📁 stac/
│           └── 📁 templates/
│               └── 📄 item-soil.json.j2         # Jinja2 template for soil STAC Items
├── 📁 configs/
│   ├── 📄 sources.yaml                          # Soil sources, URIs, formats, risk tiers
│   ├── 📄 neo4j.yaml                            # Graph connection & auth (no secrets in git)
│   └── 📄 run.yaml                              # Nightly run config (schedule, thresholds, env)
├── 📁 data/
│   └── 📁 soil/
│       ├── 📁 snapshots/                        # lakeFS (or equivalent) validated snapshots
│       ├── 📁 validation/                       # Great Expectations run outputs
│       ├── 📁 stac_items/                       # Emitted STAC Items for nightly runs
│       └── 📁 lineage/                          # Exported PROV/lineage bundles (optional)
└── 📁 .github/
    └── 📁 workflows/
        └── 📄 soil-nightly-validation.yml       # CI/CD schedule & guardrails for this pattern
```

---

## 🧩 Pipeline Architecture

The Nightly Soil Ingest Validation Pipeline follows the standard KFM pattern:

> **Deterministic ETL → STAC/DCAT/PROV catalogs → Neo4j Knowledge Graph → API → Story Nodes & Focus Mode**

Core design principles:

- **Config-driven** (no hard-coded paths or thresholds; everything in `run.yaml` + `sources.yaml`).  
- **Reproducible** (snapshot IDs, checksums, GE suites, thresholds logged in telemetry).  
- **Fail-closed** on validation or governance violations.  
- **Minimal privileges**: read-only data access; write-only for STAC items and lineage.

---

## ⚙️ Execution Flow

### 1️⃣ Deterministic Snapshot Loading

- Discover partitions using `pyarrow.dataset` (or equivalent) for efficient scanning.  
- Use **explicit snapshot IDs** (`lakeFS` commit, object version, or equivalent) from `sources.yaml`.

Requirements:

- Each run is tagged with a **`run_id`** and **snapshot identifier**.  
- Snapshot metadata (commit hash, lakeFS branch, object version) is recorded into:
  - Telemetry (`telemetry_ref`)  
  - STAC `properties["kfm:snapshot_id"]`  
  - Neo4j ingestion event node

---

### 2️⃣ Integrity & Quality Validation (Great Expectations)

Validation uses **Great Expectations suites** stored under `src/soil_ingest/expectations/`.

Mandatory rules:

- **Table-level:**
  - Row count min/max sanity bounds (per source & region).  
  - Partition count expectations where applicable.

- **Column-level:**
  - Required columns must exist (e.g., `mukey`, `hzdept_r`, `hzdepb_r`, `texture`, `aws_r`).  
  - Types must match the configured schema (numeric, categorical, datetime).  
  - Categorical domains (e.g., texture class, survey area, hydrologic group) must pass membership checks.  
  - Non-null requirements for key fields (primary keys, essential model variables).

Validation outputs:

- Stored under `data/soil/validation/` per run.  
- Summarized into telemetry (schema `telemetry_schema`) and linked to `run_id`.  
- Used as **gates**: validation failure → pipeline marked degraded and **no STAC/Neo4j emission** for that source.

---

### 3️⃣ Drift & Delta Evaluation

Using `utils.deltas.compute_delta`:

- Compare current snapshot stats vs `state_store["last_stats"]`:
  - Total bytes  
  - Fragment count / partition count  
  - Column count / type signatures  
  - Basic record counts per key partition (if configured)

Thresholds (from `run.yaml`):

- **Soft drift**: below threshold → warn only, but proceed.  
- **Hard drift**: above threshold → mark pipeline `degraded`, require manual review.

Drift metrics:

- Logged to `telemetry_ref` using `telemetry_schema`.  
- Optionally written as time-series to `energy_schema` / `carbon_schema` if drift implies reprocessing costs.

---

### 4️⃣ Temporal STAC Item Emission

For each nightly run **and each source configured**, emit a **new STAC Item** (never overwrite):

- **Temporal fields:**
  - `properties["datetime"]`: end of validation window.  
  - `properties["start_datetime"]`, `properties["end_datetime"]`: coverage of ingest window for **Story Node replay**.

- **Required KFM extensions:**
  - `properties["kfm:checksum:sha256"]` – manifest or snapshot checksum.  
  - `properties["kfm:source"]` – canonical source ID (`USDA_SDA`, `NRCS`, etc.).  
  - `properties["kfm:validator"]` – pipeline name / version (e.g., `soil-nightly-validator-v11.2.4`).  
  - `properties["kfm:run_id"]` – match `run_id` in telemetry and Neo4j.

- **Assets:**
  - Data asset: reference to Parquet / S3 / lakeFS URI (read-only).  
  - Optional derived assets: pre-aggregated tiles or model inputs.

Items are written to `data/soil/stac_items/` and registered in the global STAC catalog.

---

### 5️⃣ Neo4j Lineage Upsert

For each successful source run:

- Upsert `:SoilIngestEvent` node:

  - Example properties:
    - `event_id` (from `run_id`)  
    - `type` (e.g., `"nightly_validation"`)  
    - `source` (`"USDA_SDA"`, `"NRCS"`, etc.)  
    - `checksum`  
    - `bytes`, `fragments`  
    - `passed` (boolean)  
    - `started_at`, `finished_at` (ISO-8601)  

- Linkages:

  ```text
  (:Dataset { name: "soil_usda_sda" })
      -[:HAS_EVENT]->(:SoilIngestEvent { event_id })
      -[:EMITTED_STAC]->(:STACItem { id })
  ```

- Optional:

  - Link to **OpenLineage job & run** entities.  
  - Attach **validation summary** as properties or external JSON reference.

These relationships support Focus Mode, lineage browsers, and audit dashboards.

---

## 🧪 Reference Python (Authoritative Pseudocode)

```python
# src/soil_ingest/validator.py (abridged excerpt)

from datetime import datetime

from utils.io import load_snapshot, snapshot_stats
from utils.checksums import sha256_file
from utils.deltas import compute_delta
from utils.stac import make_stac_item, serialize
from graph.neo4j_loader import upsert_event

def run(cfg):
    t0 = datetime.utcnow()

    # 1. Deterministic snapshot loading
    ds = load_snapshot(cfg["source"]["uri"], cfg["source"]["format"])
    stats = snapshot_stats(ds)

    checksum = sha256_file(cfg["source"]["manifest_path"])

    # 2. Great Expectations run (placeholder)
    # TODO: integrate GE suite reference from cfg["expectations"]["suite"]
    passed, ge_res = True, {}

    # 3. Drift / delta detection
    prev = cfg["state_store"].get("last_stats", {})
    delta = compute_delta(prev, stats)

    # 4. STAC Item emission
    t1 = datetime.utcnow()
    stac_item = make_stac_item(
        collection_id="kfm-soil",
        uri=cfg["source"]["uri"],
        start=t0,
        end=t1,
        checksum=checksum,
        run_id=cfg["run_id"],
        source_id=cfg["source"]["id"]
    )

    serialize(stac_item, cfg["output"]["stac_item_path"])

    # 5. Neo4j lineage upsert
    payload = {
        "event_id": cfg["run_id"],
        "type": "nightly_validation",
        "source": cfg["source"]["id"],
        "snapshot_uri": cfg["source"]["uri"],
        "checksum": checksum,
        "passed": passed,
        "started_at": t0.isoformat(),
        "finished_at": t1.isoformat(),
        "bytes": stats["bytes"],
        "fragments": stats["fragments"],
        "dataset": cfg["source"]["dataset_name"],
        "stac_id": stac_item["id"],
        "delta": delta,
    }

    upsert_event(cfg["neo4j"], payload)

    # Persist state for next run
    cfg["state_store"]["last_stats"] = stats
```

This pseudocode is **illustrative**; production code must:

- Use structured logging,  
- Respect secrets management (no credentials in config files in git), and  
- Emit telemetry conforming to `telemetry_schema`, `energy_schema`, and `carbon_schema`.

---

## 🌐 Story Nodes & Focus Mode Integration

Every nightly STAC Item becomes a **temporal anchor** for soil-related Story Nodes:

- Story Nodes may reference:
  - `kfm:run_id`, `kfm:source`, `kfm:checksum:sha256`  
  - Temporal coverage (`start_datetime`, `end_datetime`)  
  - Validation outcome (`passed` / degraded)

Focus Mode v3 uses these fields to:

- Show **data freshness**, **validation status**, and **drift alerts**.  
- Allow users to **time-travel** soil layers (compare past vs present ingest states).  
- Display **Geoethical Reflection Layers** describing:
  - Input model provenance  
  - Validation strength  
  - Known gaps or caveats from upstream soil data sources

Story Nodes should never bypass this pipeline pattern for soil ingest in production; any soil dataset without a corresponding **nightly-validation lineage** should be treated as **untrusted**.

---

## 📊 SLOs & Reliability Envelope

| Domain               | Target                         | Enforcement Pattern                                       |
|----------------------|--------------------------------|-----------------------------------------------------------|
| Validation success   | ≥ 0.99 over rolling 30 days    | Fail-closed; raise incident to Reliability Council       |
| Drift detection      | < 5% schema/structure change*  | Mark `degraded`; require human review & approval          |
| Runtime              | ≤ 30 minutes per nightly run   | Auto-scale partitions / compute; alert if exceeded       |
| Idempotency          | Zero duplicate events per run  | WAL-tracked `run_id` and `event_id` enforcement          |

\* Thresholds are configured per source in `run.yaml` (e.g., stricter for sovereign-critical datasets).

SLO violations must:

- Emit **high-severity telemetry** entries, and  
- Be visible in observability dashboards shared with Reliability Engineering & FAIR+CARE Council.

---

## ⚖️ Governance, FAIR+CARE & Sovereignty

This pipeline pattern is **governed** under:

- `governance_ref` – overall KFM governance.  
- `ethics_ref` – FAIR+CARE guidance.  
- `sovereignty_policy` – Indigenous Data Sovereignty standards.

Key governance requirements:

- **FAIR+CARE Alignment**
  - Provenance, checksum, and source identifiers must be preserved in STAC & Neo4j.  
  - Derived layers must reference original soil datasets and validation outcomes.

- **Sovereignty**
  - Soil layers intersecting **Indigenous or sovereignty-linked territories** must:
    - Respect masking / generalization rules defined in `sovereignty_policy`.  
    - Be flagged in STAC (`kfm:sovereignty_flag = true`) and in Neo4j lineage.  

- **Compliance**
  - No modification of upstream soil semantics beyond:
    - Unit normalization,  
    - Explicitly documented and reversible transformations.

- **Auditability**
  - All nightly runs must be replayable using:
    - `run_id`,  
    - Snapshot ID, and  
    - GE suite versions logged in telemetry.

If governance or FAIR+CARE checks fail, the pipeline:

1. Marks the run as **failed/degraded**,  
2. Emits a **governance alert**, and  
3. Avoids emitting new STAC/lineage objects until remediated or explicitly overridden by governance processes.

---

## 🪪 Version History

| Version  | Date       | Author / Steward                       | Summary                                                                 |
|---------:|-----------:|----------------------------------------|-------------------------------------------------------------------------|
| v11.2.4  | 2025-12-08 | Soil Pipelines Team · Reliability Eng. | Initial governed release of nightly soil ingest validation pipeline pattern (deterministic, STAC/Neo4j integrated, FAIR+CARE aligned). |

---

<div align="center">

🌱 **Kansas Frontier Matrix — Nightly Soil Ingest Validation Pipeline**  
Documentation-First · Deterministic ETL · STAC/DCAT/PROV · FAIR+CARE · Sovereignty-Respecting  

For governance questions, consult:  
[`docs/standards/governance/ROOT-GOVERNANCE.md`](/docs/standards/governance/ROOT-GOVERNANCE.md)

</div>