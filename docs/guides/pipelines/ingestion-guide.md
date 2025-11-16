---
title: "📥 Kansas Frontier Matrix — Ingestion Pipeline Guide (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/guides/pipelines/ingestion-guide.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/pipeline-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-ingestion-guide-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4.2"
status: "Active / Enforced"
doc_kind: "Guide"
intent: "ingestion-pipelines"
fair_category: "F1-A1-I1-R1"
care_label: "C2-A2-R1-E1"
kfm_readme_template: "Platinum v7.1"
ci_enforced: true
---

<div align="center">

# 📥 **Kansas Frontier Matrix — Ingestion Pipeline Guide**  
`docs/guides/pipelines/ingestion-guide.md`

**Purpose**  
Define the **canonical KFM ingestion pattern** for pulling remote data into the Kansas Frontier Matrix,  
including **watchers, fetchers, conditional HTTP, checksuming, FAIR+CARE-aware metadata capture,  
telemetry v2, and lineage hooks**.  

This guide is the *entrypoint* for all reliable pipelines: **Ingest → Preprocess → Publish → Lineage**.

</div>

---

# 📘 Overview

Ingestion is the **first stage** in every KFM pipeline.  
It is responsible for:

- Safely pulling data from remote systems  
- Applying **HTTP best practices** (ETag, If-None-Match, Last-Modified)  
- Computing checksums and basic structure checks  
- Creating **Ingest Manifests** for downstream steps  
- Emitting **telemetry v2** and **ledger entries**  
- Respecting FAIR+CARE and governance constraints from the start  

All ingestion code **must be deterministic**, reproducible, and driven by explicit configuration.

---

# 🗂️ Directory Layout (Canonical Ingestion Layer)

~~~text
src/pipelines/
└── ingestion/
    ├── README.md                          # Ingestion architecture (optional per-pipeline)
    ├── watcher.py                         # Watchers (cron/webhook/event listeners)
    ├── fetch_http.py                      # HTTP/HTTPS ingestion (ETag + Last-Modified)
    ├── fetch_filesystem.py                # Local/FS ingestion (data lake, bucket mounts)
    ├── fetch_s3.py                        # S3/compatible object storage ingestion
    ├── fetch_gcs.py                       # GCS ingestion (if used)
    ├── manifest.py                        # IngestManifest representation + helpers
    ├── checksums.py                       # SHA-256/multihash helpers
    ├── telemetry.py                       # Telemetry v2 emission for ingestion
    └── utils.py                           # Shared helpers (path handling, config, logging)

data/
└── work/
    └── ingestion/
        ├── cache/                         # ETag / Last-Modified / hashes
        ├── runs/                          # Per-run manifests, logs
        └── tmp/                           # Ephemeral partial downloads
~~~

This guide defines *patterns* — you may organize concrete pipelines  
under `src/pipelines/<domain>/ingest.py` while reusing these primitives.

---

# 🌐 Ingestion Architecture (KFM-Styled Mermaid)

```mermaid
flowchart TD

subgraph WATCH["Watchers<br/><span style='font-size:12px'>cron · webhook · schedule</span>"]
    W["Watch Events"]
end

subgraph FETCH["Fetch & Snapshot<br/><span style='font-size:12px'>ETag · Last-Modified · checksums</span>"]
    F["Fetch Remote Data"]
    M["Build Ingest Manifest"]
end

subgraph GATE["Ingestion Gate<br/><span style='font-size:12px'>FAIR+CARE · Schema-lite · Size Bounds</span>"]
    G["Basic Validation"]
end

subgraph RECORD["Record & Telemetry<br/><span style='font-size:12px'>Ledger · telemetry.ndjson</span>"]
    L["Ledger Entry"]
    T["Telemetry v2"]
end

W --> F --> M --> G --> L --> T

classDef watch fill:#ebf8ff,stroke:#2b6cb0,color:#1a365d;
classDef fetch fill:#faf5ff,stroke:#805ad5,color:#553c9a;
classDef gate fill:#fffbea,stroke:#dd6b20,color:#7b341e;
classDef record fill:#f0fff4,stroke:#38a169,color:#22543d;

class WATCH watch;
class FETCH fetch;
class GATE gate;
class RECORD record;
````

---

# 1️⃣ Watchers

Watchers are responsible for **triggering ingestion runs**. Examples:

* **GitHub Actions `schedule`** (cron)
* **`repository_dispatch`** triggered by webhooks
* External scheduler (Airflow, Dagster, etc.) calling a CLI

### 1.1 Requirements

* Must be **idempotent** (re-running a watcher without new data → no new run).

* Must embed metadata:

  * `source_id`
  * `source_url` (if HTTP)
  * `trigger` (`cron|webhook|manual`)
  * `window` (time range, if streaming)
  * `pipeline_version`

* Should emit a minimal event to the **ingestion runner**, not do heavy work itself.

### 1.2 Example (GitHub Actions)

```yaml
on:
  schedule:
    - cron: "0 * * * *"
  repository_dispatch:
    types: [ingest_source_changed]
```

---

# 2️⃣ Fetchers

Fetchers retrieve data in a **content-aware** and **bandwidth-efficient** manner.

## 2.1 HTTP Fetcher (`fetch_http.py`)

### Contract

```python
def fetch_http(
    url: str,
    etag_cache_path: Path,
    out_path: Path,
) -> "IngestManifest":
    ...
```

### Behavior

* Load ETag/Last-Modified from `etag_cache_path` (if exists).

* Issue `GET` with appropriate headers:

  * `If-None-Match`
  * `If-Modified-Since`

* If `304 Not Modified`:

  * return manifest with `changed = False`
  * no write to `out_path`

* If `200 OK with body`:

  * write body to `out_path`

  * update `etag_cache_path` with:

    ```json
    {
      "etag": "...",
      "last_modified": "...",
      "content_hash": "sha256-...",
      "fetched_at": "..."
    }
    ```

  * set `changed = True`

## 2.2 Filesystem/S3/GCS Fetchers

Use similar structure:

* `fetch_filesystem.py` — copy/Hard-link from on-disk location (e.g. `data/raw`).
* `fetch_s3.py`, `fetch_gcs.py` — use SDK or `rclone`, compute checksum, build manifest.

---

# 3️⃣ Ingest Manifest

Central to ingestion is the **IngestManifest** object.

## 3.1 Fields

Minimal recommended structure:

```json
{
  "run_id": "ingest-2025-11-16-0001",
  "source_id": "noaa-daily-stations",
  "source_uri": "https://example.org/daily-stations.csv",
  "trigger": "cron",
  "retrieved_at": "2025-11-16T03:11:40Z",
  "changed": true,
  "local_path": "data/work/ingestion/runs/ingest-2025-11-16-0001/input.csv",
  "content_type": "text/csv",
  "content_length": 123456,
  "checksum_sha256": "sha256-abc123...",
  "previous_etag": "W/\"abc\"",
  "current_etag": "W/\"def\""
}
```

## 3.2 Schema

Stored at:

```text
schemas/ingest_manifest.schema.json
```

Validated within unit tests.

---

# 4️⃣ Basic Validation Gate

The ingestion layer performs **simple sanity checks**, not full domain validation.

Examples:

* `content_length` above 0 and below configured maximum.

* For CSV:

  * at least 1 data row
  * header row present

* For JSON:

  * valid JSON parse
  * top-level structure matches expected shape (`array` or `object`)

* For binary assets:

  * expected MIME type
  * non-corrupted ZIP/TAR

If these checks fail:

* The manifest is marked `status = "rejected"`
* No promotion into `data/work/staging/<run_id>/` occurs
* The pipeline records error details into the ledger/telemetry

---

# 5️⃣ FAIR+CARE Touchpoints at Ingest

Even at ingestion, we must consider:

* **Source license** (if known)
* **Sovereignty / jurisdiction** (e.g. Indigenous sources)
* **Data-provider usage conditions**
* Early detection of:

  * possible PII
  * sensitive attributes (e.g. health data, incomes)

These rarely block ingestion *by themselves*, but they must be recorded:

* `careHints[]` in the manifest
* Optionally a `requires_manual_review` flag for downstream stages

---

# 6️⃣ Telemetry v2 for Ingestion

The ingestion step MUST emit telemetry consistent with:

```text
telemetry/pipelines-ingestion-guide-v1.json
```

Minimum fields:

* `pipeline`: `"ingestion"` or domain-specific
* `run_id`
* `source_id`
* `source_uri`
* `trigger`
* `status` (success|noop|failed)
* `http_status` (if HTTP)
* `bytes_fetched`
* `duration_ms`
* `attempt` / `retries`
* energy + CO₂ estimates (optional)

Telemetry is written to:

```text
data/work/tmp/telemetry/ingestion.ndjson
```

…then aggregated into:

```text
releases/v10.4.2/pipeline-telemetry.json
```

---

# 7️⃣ Governance & Ledger Integration

Ingestion runs must append to the **Governance Ledger**:

```text
docs/reports/audit/data_provenance_ledger.jsonl
```

Entry:

```json
{
  "stage": "ingest",
  "run_id": "ingest-2025-11-16-0001",
  "dataset_id": "noaa-daily-stations",
  "source_uri": "https://example.org/daily-stations.csv",
  "checksum_sha256": "sha256-abc123...",
  "careHints": ["license-unknown"],
  "timestamp": "2025-11-16T03:11:40Z",
  "workflow_run_id": "gh-123456",
  "kfm_version": "10.4.2"
}
```

---

# 8️⃣ CI Patterns for Ingestion

Recommended GitHub Actions workflows:

* `ingest-watch.yml`

  * Schedules ingestion
  * Runs `fetch_http.py` / `fetch_s3.py`
  * Writes manifest + telemetry

* `ingest-validate.yml`

  * Validates manifest structure
  * Enforces maximum sizes
  * Optional: run smoke checks on content

In a full pipeline, ingestion is often the first job in a **multi-job workflow** that also runs:

* preprocessing
* publishing
* lineage export

---

# 9️⃣ Example Python Sketch (`fetch_http.py`)

```python
from pathlib import Path
import hashlib, json, time
import requests
from .manifest import IngestManifest

def fetch_http(url: str, etag_cache_path: Path, out_path: Path) -> IngestManifest:
    cache = {}
    if etag_cache_path.exists():
        cache = json.loads(etag_cache_path.read_text())

    headers = {}
    if (etag := cache.get("etag")):
        headers["If-None-Match"] = etag
    if (last := cache.get("last_modified")):
        headers["If-Modified-Since"] = last

    start = time.time()
    r = requests.get(url, headers=headers, timeout=60)

    if r.status_code == 304:
        duration_ms = int((time.time() - start) * 1000)
        return IngestManifest.no_change(url, cache, duration_ms)

    r.raise_for_status()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(r.content)

    checksum = hashlib.sha256(r.content).hexdigest()
    cache = {
        "etag": r.headers.get("ETag"),
        "last_modified": r.headers.get("Last-Modified"),
        "content_hash": checksum,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }
    etag_cache_path.parent.mkdir(parents=True, exist_ok=True)
    etag_cache_path.write_text(json.dumps(cache, indent=2))

    duration_ms = int((time.time() - start) * 1000)
    return IngestManifest.from_http(url, out_path, checksum, cache, duration_ms)
```

---

# 🔟 Developer Checklist (Ingestion)

* [ ] Chosen fetcher (HTTP/S3/FS) is **deterministic**.
* [ ] ETag/Last-Modified caching implemented.
* [ ] `IngestManifest` schema defined and tests added.
* [ ] Basic size/shape validation in place.
* [ ] FAIR+CARE hints recorded.
* [ ] Telemetry v2 events emitted.
* [ ] Governance ledger entry appended.
* [ ] CI workflows for `ingest-watch` and `ingest-validate` added.

---

# 🕰 Version History

| Version | Date       | Summary                                                                                                |
| ------: | ---------- | ------------------------------------------------------------------------------------------------------ |
| v10.4.2 | 2025-11-16 | Initial ingestion-guide.md for KFM v10.4.2; defines canonical watcher/fetch/manifest/telemetry pattern |

---

<div align="center">

**Kansas Frontier Matrix — Ingestion Pipeline Guide (v10.4.2)**
Reliable Ingestion × FAIR+CARE v2 × Telemetry v2 × Governance Ledger
© 2025 Kansas Frontier Matrix — CC-BY 4.0 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified

</div>
