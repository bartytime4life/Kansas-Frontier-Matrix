---
title: "🔁 KFM Updater Runners — Idempotent Schedulers, Webhooks & Dry-Run Safety (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/updater/README.md"
version: "v10.4.2"
last_updated: "2025-11-16"
review_cycle: "Quarterly · Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.4.2/sbom.spdx.json"
manifest_ref: "../../../releases/v10.4.2/manifest.zip"
telemetry_ref: "../../../releases/v10.4.2/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-updater-v1.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Architecture"
intent: "updater-scheduling-and-webhooks"
fair_category: "F1-A1-I1-R1"
care_label: "C1-A1-R1-E1"
---

<div align="center">

# 🔁 **KFM Updater Runners — Idempotent Schedulers, Webhooks & Dry-Run Safety**  
`src/pipelines/updater/README.md`

**Purpose**  
Define standardized **Python** and **Node.js** update runners for dataset refresh jobs with **idempotency**,  
**dry-run safety**, **structured JSON logs**, **concurrency fencing**, **artifact export**, and  
**HMAC-validated webhook ingestion**.  
All mutating behavior flows through a **Publisher** abstraction that supports full no-op during `--dry-run`.

</div>

---

# 🎯 Design Goals

- **Idempotent execution**  
  Compute a stable key (e.g., `sha256(source_url|etag|window|pipeline_version)`) to prevent duplicate work.

- **Dry-run safety**  
  All writing operations are routed through a `Publisher` that becomes a **no-op** when `--dry-run` is active.

- **Audit & reproducibility**  
  Emit structured JSON logs (`run.jsonl`) and upload all artifacts for PR review.

- **Deterministic scheduling**  
  GitHub Actions **cron**, **scheduled dispatch**, and **HMAC-validated webhooks** (fan-in).  
  Uses **concurrency groups** to prevent overlapping runs.

- **Runtime-agnostic**  
  Python + Node.js CLIs expose identical flags, idempotency logic, and publisher semantics.

---

# 🧰 CLI Entrypoints

## Python
```bash
python -m updater run --config config.yml --dry-run
````

## Node.js

```bash
node updater.mjs run --config config.yml --dry-run
```

**Shared flags:**

| Flag              | Description                                        |
| ----------------- | -------------------------------------------------- |
| `--config CONFIG` | Load YAML/JSON configuration                       |
| `--dry-run`       | Disable all mutating side-effects                  |
| `--window`        | Optional “lookback period” for incremental sources |
| `--verbose`       | Human-readable logs in addition to JSONL           |
| `--force`         | Override idempotency for debugging                 |

---

# 📦 Runtime Folder Layout

```text
src/pipelines/updater/
├── README.md                             # This document
│
├── runner.py                              # Python entrypoint (dispatcher)
├── runner.mjs                             # Node.js entrypoint (dispatcher)
│
├── idempotency/
│   ├── keygen.py                          # Stable key generator
│   ├── keygen.mjs                         # Mirror implementation for Node.js
│   ├── ledger.py                          # SQLite/JSONL idempotency store
│   └── ledger.mjs                         # JS equivalent
│
├── publisher/
│   ├── base.py                            # Publisher interface (Python)
│   ├── base.mjs                           # Publisher interface (Node)
│   ├── noop.py                            # No-op publisher for --dry-run
│   ├── noop.mjs                           # JS version
│   ├── github_actions.py                  # Publisher for GH artifact upload + outputs
│   └── github_actions.mjs                 # JS version
│
├── scheduler/
│   ├── cron.yml                           # GitHub cron entry
│   ├── webhook_validator.py               # HMAC validation logic
│   └── webhook_validator.mjs              # JS version
│
└── config_templates/
    ├── config.example.yml                 # Example configuration
    └── sources.example.json               # Multi-source incremental fetch example
```

---

# 🔐 Webhook Security (HMAC)

**Required header:**

```
X-KFM-Signature: sha256=<hex>
```

**Process:**

1. Extract raw request body
2. Compute `sha256(secret | body)`
3. Compare with provided signature
4. Reject if mismatch (403)
5. Log failure into `webhook_failures.jsonl`

Webhook requests MUST also include:

* `source_id`
* `trigger`
* `sent_at`
* `event_type`
* `integrity.version`

---

# 🔁 Idempotency Model

### Key design

```
idempotency_key = sha256(source_url | etag | window | pipeline_version)
```

### Ledger behavior

* If key exists → mark job as **NOOP**
* If key is new → record and continue
* Ledger entries contain:

  * `run_id`
  * `dataset_id`
  * `key`
  * `timestamp`
  * `source_metadata`
  * `pipeline_version`

Ledger implementation:

* `ledger/idempotency.sqlite` (preferred)
* JSONL fallback (`ledger.jsonl`) for environments without SQLite

---

# 🧮 Publisher Abstraction

All side effects must flow through the **Publisher** interface.

### Required methods

| Method                         | Description                       |
| ------------------------------ | --------------------------------- |
| `write_file(path, bytes)`      | Write file or artifact            |
| `emit_event(name, payload)`    | Emit telemetry event              |
| `update_metadata(key, value)`  | Update state/metadata             |
| `publish_release(tag, assets)` | Attach files to GH Release        |
| `noop_guard()`                 | Ensure no side-effects if dry-run |

### Dry-run mode

* All mutating operations routed to `noop`
* Logging still enabled
* Artifacts optionally written to a temp folder
* Telemetry events labeled with `"dry_run": true`

### GitHub Actions publisher

* Writes artifacts using `ACTIONS_RUNTIME_TOKEN`
* Exposes outputs via `set-output`
* Applies concurrency fences automatically

---

# 🧪 Logs & Artifacts

Every run must emit:

```
run.jsonl
event_log.jsonl
idempotency.json
publisher_trace.jsonl
```

Artifacts folder structure:

```text
artifacts/
├── run.jsonl                        # All structured logs from the run
├── event_log.jsonl                  # Telemetry-like event firehose
├── idempotency.json                 # idempotency key + ledger state
└── publisher_trace.jsonl            # Ordered record of publisher activity
```

---

# 🧭 Scheduling Model

### GitHub Actions

* **cron-based**: `0 * * * *` (hourly)
* **repository_dispatch** from webhook fan-in
* **workflow_dispatch** for manual testing
* **concurrency:** `pipelines-updater-${{ matrix.dataset }}`

### Webhook fan-in

All incoming webhook events (various external providers) normalize into a unified schema:

```
{
  "source_id": "noaa-stations",
  "trigger": "etag-change",
  "event_type": "update",
  "sent_at": "2025-11-16T06:12:01Z",
  "metadata": {},
  "integrity": {
    "version": "v1",
    "signature": "sha256=..."
  }
}
```

---

# 🧩 Standard Run Lifecycle

```text
Watcher/Event → Idempotency → Validator → Transform → Publish → Telemetry → Ledger
```

### 1. Trigger

Webhook or cron schedules the run.

### 2. Idempotency

If previously processed → no-op.

### 3. Validate

Config + schema + content checks.

### 4. Transform

Normalize → convert → update metadata.

### 5. Publish

Artifacts, Releases, PR comments (if enabled).

### 6. Telemetry

Structured events appended to `event_log.jsonl`.

### 7. Ledger update

Record the completed state.

---

# 📈 Telemetry & Observability

Telemetry events must follow:

* `types/telemetry.ts` schemas
* Include `"dry_run": true` when applicable
* Store in `publisher_trace.jsonl`
* Send to the observability backend (optional)
* Exclude PII and sensitive file paths
* Include:

  * `run_id`
  * `duration_ms`
  * `dataset`
  * `source_id`
  * `trigger`
  * `idempotency_state`
  * `artifact_count`

---

# 📜 Governance & FAIR+CARE Requirements

All updater runners must:

### ✔ Follow CARE-labeled data access rules

### ✔ Prevent unreviewed data propagation

### ✔ Attach provenance metadata to all artifacts

### ✔ Validate license information

### ✔ Emit ethical review signals when anomalies appear

### ✔ Reject malformed artifacts or ambiguous deltas

### ✔ Ensure dry-run never mutates protected locations

Governance failures → **CI BLOCK**.

---

# 🧪 Testing Requirements

### Unit Tests

* idempotency keygen
* webhook validation
* publisher no-op behavior
* configuration loading
* JSON logging

### Integration Tests

* “cron → updater → artifacts → ledger”
* concurrency fences
* dry-run safety
* event emission + artifact layout

### Negative-path Tests

* malformed webhook
* invalid signature
* publisher write failures (should not crash)
* corrupted ledger entries
* invalid config file

Test structure:

```text
tests/
├── unit/pipelines/updater/
└── integration/pipelines/updater/
```

---

# 🕰 Version History

| Version | Date       | Summary                                                                                      |
| ------: | ---------- | -------------------------------------------------------------------------------------------- |
| v10.4.2 | 2025-11-16 | Added full architecture, folder trees, governance rules, runtime parity, and scheduler model |
| v10.4.1 | 2025-11-15 | Initial updater runner README                                                                |

```
