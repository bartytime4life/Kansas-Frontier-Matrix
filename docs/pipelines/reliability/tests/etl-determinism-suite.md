---
title: "🧪 KFM v11.2.x — Deterministic ETL Reliability Test Suite (Replay · WAL Recovery · Idempotent Upserts)"
path: "docs/pipelines/reliability/tests/etl-determinism-suite.md"
version: "v11.2.x"
last_updated: "2025-12-08"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"

status: "Active / Enforced"
doc_kind: "Test Suite"
header_profile: "standard"
footer_profile: "standard"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash>"
doc_integrity_checksum: "<sha256-of-this-file>"

sbom_ref: "releases/v11.2.x/sbom.spdx.json"
manifest_ref: "releases/v11.2.x/manifest.zip"
telemetry_ref: "releases/v11.2.x/reliability-tests-telemetry.json"
telemetry_schema: "schemas/telemetry/reliability-tests-v2.json"
energy_schema: "schemas/telemetry/energy-v2.json"
carbon_schema: "schemas/telemetry/carbon-v2.json"

governance_ref: "docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "docs/standards/faircare/FAIRCARE-GUIDE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
ontology_protocol_version: "KFM-OP v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

scope:
  domain: "pipelines.reliability"
  applies_to:
    - "etl"
    - "streaming-ingest"
    - "batch-replay"
    - "graph-upsert"
    - "catalogs"

backward_compatibility: "v10.x → v11.x"
fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (auto-mask rules apply)"
classification: "Internal/Public Docs (Open)"
---

<div align="center">

# 🧪 **Deterministic ETL Reliability Test Suite**  
Replayability · WAL Recovery · Idempotent Upserts under Load  

`docs/pipelines/reliability/tests/etl-determinism-suite.md`

</div>

---

## 📘 Overview

This suite validates three **non‑negotiable reliability guarantees** across KFM pipelines:

1. **Replayability** — bit‑for‑bit stable outputs when re‑running the same inputs.  
2. **WAL Recovery** — crash/kill during critical sections replays to an identical committed state.  
3. **Idempotent Upserts** — repeated inserts/merges produce no duplicates or drift in **Neo4j** and **Parquet** targets.

Synthetic fixtures exercise both:

- **Soil** — grid soil moisture/texture (batch ETL, partitioned by date).  
- **HRRR** — smart subsets of 2‑m temperature and precipitation (stream windows, event‑time + watermarks).

All tests emit **telemetry** conforming to:

- `schemas/telemetry/reliability-tests-v2.json`  
- `schemas/telemetry/energy-v2.json`  
- `schemas/telemetry/carbon-v2.json`  

and are wired into the KFM CI workflows as **hard gates** for pipeline changes.

---

## 🗂️ Directory Layout

```text
📁 docs/
└── 📁 pipelines/
    └── 📁 reliability/
        └── 📁 tests/
            📄 etl-determinism-suite.md      # ← This file (test suite spec)

📁 src/
└── 📁 tests/
    └── 📁 reliability/
        📄 __init__.py
        📄 conftest.py
        📁 seeds/
        │   📄 soil_small.parquet
        │   📄 soil_med.parquet
        │   📄 hrrr_subset.zarr.index
        📁 profiles/
        │   📄 lakefs_dev.yaml
        │   📄 lakefs_ci.yaml
        📁 cases/
        │   📄 test_replay_soil_batch.py
        │   📄 test_replay_hrrr_stream.py
        │   📄 test_wal_recovery_batch.py
        │   📄 test_wal_recovery_stream.py
        │   📄 test_idempotent_upsert_parquet.py
        │   📄 test_idempotent_upsert_neo4j.py
        │   📄 test_under_load_mix.py
        └── 📁 utils/
            📄 lakefs_branch.py
            📄 golden_hash.py
            📄 time_control.py
            📄 seed_control.py

📁 data/
└── 📁 test-snapshots/
    📁 soil_batch_v1/
    📁 hrrr_stream_v1/
    📄 manifest.sha256                     # Golden hashes for snapshot dirs
```

All paths above are **illustrative contracts**; concrete file names may vary but structure must remain isomorphic for CI and docs‑lint to pass.

---

## ✅ Test Matrix & SLOs

| ID | Capability         | Mode   | Data      | Window            | SLO / Expected Guarantee                               |
|----|--------------------|--------|-----------|-------------------|--------------------------------------------------------|
| R1 | Replayability      | Batch  | Soil      | D‑1               | Byte‑identical outputs (dir hash equality)            |
| R2 | Replayability      | Stream | HRRR      | t‑15m tumbling    | Event‑time equality + watermark invariants            |
| W1 | WAL Recovery       | Batch  | Soil      | D‑1               | Commit atomicity; 0 partial files after recovery      |
| W2 | WAL Recovery       | Stream | HRRR      | t‑15m             | Exactly‑once effects after replay                     |
| I1 | Idempotent Upsert  | Batch  | Soil→Parq | D‑1               | Stable PK counts; no PK dupes; stable dir hash        |
| I2 | Idempotent Upsert  | Graph  | Neo4j     | rolling 24h       | Stable `(:DatasetVersion)` counts; no dup relationships |
| L1 | Load Mix           | Mixed  | Soil+HRRR | 30–60 min window  | p95 latency < SLO; 0 drift vs golden snapshot         |

**Must‑pass condition:** all rows R1–L1 must be green for any release that ships changes to:

- ETL patterns,  
- lakeFS/WAL logic,  
- Neo4j upsert semantics,  
- streaming windowing/watermarking code.

---

## 🧩 Determinism Controls

To ensure **deterministic behavior**, tests enforce:

- **Seed locking**  
  - `PYTHONHASHSEED=0`  
  - NumPy / PyTorch / RNG seeds fixed (e.g., `43210`)  
  - All random ops routed through a shared `kfm_rng(seed)` helper.

- **Filesystem & object isolation**  
  - lakeFS branches per test case, e.g. `reliability/r1/<commit-sha>`.  
  - No writes to shared “prod” branches or buckets.

- **Time control**  
  - Wall‑clock frozen via time‑control fixtures for batch.  
  - Streams operate on **event‑time** with fixed watermarks; replays must see identical orderings.

- **Canonicalization**  
  - Stable sort order (on PKs) before Parquet write.  
  - Dtype pinning (no implicit up/down casts).  
  - CRS pinning for geospatial tests (e.g., always EPSG:3857 or EPSG:4326).  
  - Parquet writer options fixed (row group size, compression codec, dictionary encoding).

- **Resource & environment pinning (CI)**  
  - OS image (`ubuntu-latest` + `self-hosted-lakefs` matrix).  
  - Dependency lockfile enforced (e.g., `poetry.lock` / `requirements.lock`).

Any violation of these controls is considered **a test design bug** and must be resolved prior to pipeline changes.

---

## 🧪 PyTest Skeletons

### 1️⃣ Replayability — Soil (Batch)

```python
# src/tests/reliability/cases/test_replay_soil_batch.py
import hashlib
import pathlib

from kfm.etl.soil_batch import run as run_soil
from kfm.tests.utils import lakefs_branch, force_seed, canonicalize_parquet_dir


def _dir_hash(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    for f in sorted(path.rglob("*.parquet")):
        h.update(f.read_bytes())
    return h.hexdigest()


def test_replay_soil_batch(tmp_path, lakefs_branch):
    force_seed(43210)

    out1 = run_soil(date="2025-08-01", branch=lakefs_branch, out_dir=tmp_path / "run1")
    out2 = run_soil(date="2025-08-01", branch=lakefs_branch, out_dir=tmp_path / "run2")

    canonicalize_parquet_dir(out1)
    canonicalize_parquet_dir(out2)

    assert _dir_hash(out1) == _dir_hash(out2)
```

---

### 2️⃣ Replayability — HRRR (Stream, Event‑Time)

```python
# src/tests/reliability/cases/test_replay_hrrr_stream.py
from kfm.stream.hrrr import run_window
from kfm.tests.utils import fixed_event_clock


def test_replay_hrrr_stream(fixed_event_clock):
    w1 = run_window(start="2025-08-01T00:00Z", length="15m", seed=43210)
    w2 = run_window(start="2025-08-01T00:00Z", length="15m", seed=43210)

    assert w1.metrics["records_out"] == w2.metrics["records_out"]
    assert w1.hash == w2.hash
    assert w1.watermark_state == w2.watermark_state
```

---

### 3️⃣ WAL Recovery — Soil (Batch)

```python
# src/tests/reliability/cases/test_wal_recovery_batch.py
from kfm.etl.core import run_with_wal, inject_failure


def test_wal_recovery_batch(tmp_path):
    inject_failure.at("post-transform.pre-commit")  # kill before commit

    r1 = run_with_wal("soil_batch", date="2025-08-01", out_dir=tmp_path / "runA")
    # second attempt: no failure
    inject_failure.clear()
    r2 = run_with_wal("soil_batch", date="2025-08-01", out_dir=tmp_path / "runA")

    assert r1.status == "aborted"
    assert r2.status == "committed"
    assert r2.output_hash is not None
    # WAL table: exactly one committed record for this content_hash
```

---

### 4️⃣ WAL Recovery — HRRR (Stream)

```python
# src/tests/reliability/cases/test_wal_recovery_stream.py
from kfm.stream.core import run_tick_with_wal, inject_failure


def test_wal_recovery_stream():
    inject_failure.at("sink.apply")
    t1 = run_tick_with_wal("hrrr", tick="2025-08-01T00:15Z")

    inject_failure.clear()
    t2 = run_tick_with_wal("hrrr", tick="2025-08-01T00:15Z")

    assert t1.status == "aborted"
    assert t2.status == "committed"
    assert t2.exactly_once_effects is True
```

---

### 5️⃣ Idempotent Upsert — Parquet Target

```python
# src/tests/reliability/cases/test_idempotent_upsert_parquet.py
from kfm.targets.parquet import upsert_partition, stats


def test_idempotent_upsert_parquet(tmp_path):
    pk = ["grid_id", "ts"]

    for _ in range(3):
        upsert_partition(
            target_dir=tmp_path / "soil",
            src="seeds/soil_small.parquet",
            pk=pk,
        )

    s = stats(tmp_path / "soil")
    assert s.pk_dupes == 0
    assert s.row_count == s.unique_pk_count
```

---

### 6️⃣ Idempotent Upsert — Neo4j MERGE

```python
# src/tests/reliability/cases/test_idempotent_upsert_neo4j.py
from kfm.graph.neo4j import merge_dataset_version, counts


def test_idempotent_merge_neo4j():
    for _ in range(3):
        merge_dataset_version(
            dataset="soil",
            version="2025-08-01",
            pk=["grid_id", "ts"],
        )

    c = counts(labels=["DatasetVersion", "Observation"])

    assert c.dup_nodes == 0
    assert c.dup_rels == 0
```

---

### 7️⃣ Under Load — Mixed Workload

```python
# src/tests/reliability/cases/test_under_load_mix.py
import concurrent.futures as cf

from kfm.tests.load import soil_batch_job, hrrr_stream_job, graph_merge_job
from kfm.tests.utils import golden_snapshot_hash


def test_under_load_mix(tmp_path):
    jobs = [soil_batch_job(), hrrr_stream_job(), graph_merge_job()]

    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        list(ex.map(lambda fn: fn(tmp_path), jobs * 3))

    assert golden_snapshot_hash(tmp_path) == "b2f1e2a9..."  # golden baseline
```

---

## 🔒 WAL Rules (Batch & Stream)

Core **WAL safety** rules (aligned with KFM idempotent patterns):

1. **Temp first:** write temp objects with UUID suffix in a work area.  
2. **Intent log:** write WAL record (`state="precommit"`) including content hashes.  
3. **Commit:** atomic rename/move from temp → final path; flip WAL to `state="committed"`.  
4. **Recovery:** on startup, scan WAL; for any `precommit` entries:
   - delete temp objects,  
   - replay stage or roll back,  
   - ensure no partially visible outputs.

Batch and streaming implementations may differ, but **WAL semantics must be equivalent** and verified by W1/W2 tests.

---

## 📊 Telemetry & SLO Gating

Each test run must emit:

- **OTel spans** under `kfm.reliability.*`  
- Attributes:
  - `kfm.test_id`, `kfm.test_suite`, `kfm.commit_sha`  
  - `timing.duration_s`, `energy.kwh`, `carbon.gco2e`, `io.bytes`, `mem.max_mb`  

CI gates:

- Fail if:
  - Any test returns non‑zero exit code,  
  - Required telemetry fields missing for reliability spans,  
  - p95 duration or energy per test regresses > configured threshold vs 7‑day median.

Telemetry bundles are archived under:

- `releases/v11.2.x/reliability-tests-telemetry.json`

and validated against `schemas/telemetry/reliability-tests-v2.json`.

---

## 🧱 Data Fixtures

**Soil Fixtures**

- Synthetic grids (2–5 km), columns:
  - `grid_id`, `ts`, `moisture`, `texture`, `qc_flag`  
- Designed to:
  - Test PK uniqueness,  
  - Validate deterministic partitioning (by date / grid).

**HRRR Fixtures**

- Zarr index subset:
  - Variables: 2‑m temperature, accumulated precipitation.  
  - Windows: 15‑minute tumbling with allowed lateness = 10 minutes.  
- Designed to:
  - Exercise event‑time & watermark logic,  
  - Test backfill replay behavior.

Fixtures **must not** contain sensitive coordinates; they are synthetic or publicly safe.

---

## 🧹 Isolation & Cleanup

- Each test case uses a dedicated **lakeFS branch**: `reliability/<test-id>/<commit-sha>`.  
- Temp objects are GC’d automatically after commit or rollback.  
- WAL records older than 7 days in test environments may be pruned, but not before the next full reliability run.

---

## 🧾 CI Wiring (GitHub Actions)

```yaml
name: reliability-suite

on:
  push:
    paths:
      - "src/**"
      - "docs/pipelines/reliability/**"
      - "schemas/telemetry/reliability-tests-v2.json"
  pull_request:
    paths:
      - "src/**"
      - "docs/pipelines/reliability/**"

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install deps
        run: pip install -e .[tests]
      - name: Run Determinism Suite
        env:
          PYTHONHASHSEED: "0"
        run: |
          pytest -q src/tests/reliability --maxfail=1 --disable-warnings
```

---

## ✅ Exit Criteria

The **Deterministic ETL Reliability Test Suite** is considered satisfied for a release when:

- All tests (R1–L1) pass on:
  - `ubuntu-latest`, and  
  - at least one `self-hosted-lakefs` runner.  
- Golden snapshot hashes are unchanged **or** updated via a governance‑approved process.  
- Graph and Parquet counts & hashes show **no unexplained drift**.  
- WAL recovery behavior is verified via W1/W2 test logs.  
- Telemetry bundles are valid and archived for the release.

---

## 🕰️ Version History

| Version | Date       | Notes                                                                 |
|--------:|------------|-----------------------------------------------------------------------|
| v11.2.x | 2025-12-08 | Initial governed suite covering replay, WAL recovery, idempotent upserts, and mixed load. |

---

<div align="center">

🧪 **Kansas Frontier Matrix — Deterministic ETL Reliability Test Suite**  

[📘 Pipelines Index](../../README.md) ·  
[🧩 Patterns](../../patterns/README.md) ·  
[⚖️ Root Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>