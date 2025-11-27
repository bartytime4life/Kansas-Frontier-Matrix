---
title: "🔁 KFM v11.2 — Updater Runners (Idempotent Schedulers · Webhooks · Dry-Run Safety · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/updater/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-commit-hash-or-null>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:pipelines:updater:runners:v11.2.2"
semantic_document_id: "kfm-updater-runners"
event_source_id: "ledger:src/pipelines/updater/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../releases/v11.2.2/updater-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-updater-v11.2.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Architecture"
intent: "updater-scheduling-and-webhooks"
category: "Pipelines · Orchestration · Governance"

fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
classification: "Public (Governed)"
sensitivity: "Mixed"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "Annual review"
sunset_policy: "Superseded by Updater Runners v12"
---

<div align="center">

# 🔁 **KFM v11.2 — Updater Runners**  
### Idempotent Schedulers · Webhooks · Dry-Run Safety  
`src/pipelines/updater/README.md`

**Purpose**  
Define the **architecture, behavior, and governance** of KFM’s **Updater Runners** — the orchestrated executors that run refresh jobs, process webhooks, and coordinate multi-source ETL safely and deterministically.  
They guarantee **idempotent execution**, **dry-run safety**, **concurrency fencing**, and **FAIR+CARE-governed automation** for all autonomous updates.

  
<!-- Badge Row -->
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Scheduling-Idempotent-lightgrey" />

</div>

---

## 📘 1. High-Level Role

Updater Runners form the **execution layer** for:

- Dataset refresh cycles (e.g., daily, weekly, monthly)  
- STAC and DCAT catalog updates  
- Multi-source ETL synchronization runs  
- Governance-led data corrections and backfills  
- Webhook-driven refreshes from external signals (NOAA, USGS, NRCS, etc.)  
- Focus Mode v3 context rebuilds and Story Node regenerations  

They are responsible for **how** data updates are run, not **what** each domain pipeline computes.

Key properties:

- **Idempotent** (same input → same effect, no duplication).  
- **Dry-run safe** (can simulate without side effects).  
- **Concurrency-safe** (guards against overlapping runs).  
- **Governed** (respects FAIR+CARE and sovereignty rules).  
- **Telemetry-rich** (OpenTelemetry, OpenLineage, sustainability metrics).  

---

## 🗂️ 2. Directory Layout (Canonical)

```text
📁 src/
└── 📁 pipelines/
    └── 📁 updater/
        📄 README.md                 — ← This file
        📄 runner.py                 — Python entrypoint for Updater Runner
        📄 runner.mjs                — Node.js entrypoint (parity with Python)
        📁 idempotency/
        │   📄 keygen.py             — Idempotency key generation (Python)
        │   📄 keygen.mjs            — Idempotency key generation (Node)
        │   📄 ledger.py             — Persistence for idempotency state (Python)
        │   📄 ledger.mjs            — Same interface for Node
        📁 publisher/
        │   📄 base.py               — Base publisher abstraction
        │   📄 base.mjs
        │   📄 noop.py               — Dry-run/no-op publisher
        │   📄 noop.mjs
        │   📄 github_actions.py     — Publisher for GitHub Actions artifacts
        │   📄 github_actions.mjs
        📁 scheduler/
        │   📄 cron.yml              — Scheduler definitions (cron patterns)
        │   📄 webhook_validator.py  — HMAC validator (Python)
        │   📄 webhook_validator.mjs — HMAC validator (Node)
        📁 config_templates/
        │   📄 config.example.yml
        │   📄 sources.example.json
        📁 tests/
            📄 test_runner_py.py
            📄 test_runner_mjs.mjs
            📁 fixtures/
                📄 webhook_sample.json
                📄 idempotency_sample.json
```

---

## 🧩 3. Core Design Requirements

### 3.1 Idempotent Execution

All Updater Runner invocations MUST derive an **idempotency key** that uniquely represents:

- Source + time window  
- Trigger context  
- Pipeline version  

A recommended pattern:

```text
idempotency_key = sha256(
  source_id | window_spec | pipeline_version | trigger_type
)
```

The idempotency ledger:

- Records completed runs  
- Prevents re-processing the same logical work  
- Enables safe **retries** and replays  

Duplicate keys MUST result in **no-op** (no side effects).

---

### 3.2 Dry-Run Safety

All mutating operations pass through a **Publisher abstraction**:

- In normal mode:
  - Publisher writes artifacts, updates state, emits events.  
- In dry-run mode:
  - All writes become **noop**.  
  - Telemetry is still emitted with `"dry_run": true`.  
  - The full would-be mutation plan is logged as structured JSONL.

This allows Updater Runners to:

- Test new configs safely  
- Provide governance previews  
- Surface potential changes to Focus Mode before commit

---

### 3.3 Concurrency Fencing

Runners MUST:

- Use concurrency groups at the CI level (e.g., GitHub Actions `concurrency:` key)  
- Acquire dataset- or domain-scoped locks before execution  
- Refuse to start if compatible lock cannot be obtained  

This prevents:

- Double-refresh of the same dataset  
- Overlapping updates that could corrupt STAC/DCAT or tiles  
- Race conditions between watchers + updater runners  

---

### 3.4 Governed Execution

Before performing any side effects, Updater Runners MUST:

- Run Data Contract v11 checks  
- Observe FAIR+CARE + sovereignty policies  
- Respect kill switches / freeze windows declared in config  
- Attach governance metadata to each run (e.g. rationale, ticket ID)  

Governance failure → **no promotion permitted**.

---

## 🧰 4. CLI Entrypoints (Python & Node)

### Python

```bash
python -m updater.runner run \
  --config config.yml \
  --window P1D \
  --dry-run
```

### Node.js

```bash
node runner.mjs run \
  --config config.yml \
  --window P1D \
  --dry-run
```

### Shared Flags

| Flag        | Description                                                |
|-------------|------------------------------------------------------------|
| `--config`  | Path to YAML/JSON configuration                           |
| `--dry-run` | Enable no-op publisher (no mutations)                     |
| `--window`  | Logical lookback window (e.g., `P1D`, `PT6H`)             |
| `--force`   | Override idempotency & safety checks (debug only, governed) |
| `--verbose` | Emit human-readable logs alongside JSONL tracing          |

Python and Node MUST produce **equivalent semantics and JSONL outputs**.

---

## 🔐 5. Webhook Security (HMAC)

Webhook endpoints MUST apply:

- HMAC signature header:  
  - `X-KFM-Signature: sha256=<hex>`  
- Validation steps:
  1. Read raw request body  
  2. Compute `sha256(secret + body)`  
  3. Compare with header  
  4. Reject (`403`) on mismatch  
  5. Log to `webhook_failures.jsonl`  

Webhook payload MUST include:

- `source_id`  
- `trigger`  
- `event_type`  
- `sent_at` (UTC)  
- Optional metadata under `metadata` and `integrity` blocks  

This allows Updater Runners to incorporate external events safely.

---

## 🔁 6. Idempotency Ledger

The idempotency ledger records:

- `run_id`  
- `dataset_id` / `pipeline_id`  
- `idempotency_key`  
- `trigger_type` (`cron`, `webhook`, `manual`, `retry`)  
- `window_spec`  
- `pipeline_version`  
- `start_time_utc` / `end_time_utc`  
- `status` (`success`, `noop`, `failed`)  

Backends:

- **SQLite** (preferred)  
- **Feather/Parquet/JSONL** for debugging or local-only setups  

Duplicate key with `status = success` → run becomes noop.  
Duplicate key with `status = failed` → run MUST go through a **governed retry** path.

---

## 🧮 7. Publisher Abstraction

Publisher is the only component allowed to:

- Write artifacts  
- Update metadata/state  
- Emit deployment events  
- Create GitHub artifacts, STAC/DCAT pushes, etc.

Required interface methods (conceptual):

- `write_file(path, bytes, metadata)`  
- `emit_event(event_type, payload)`  
- `update_state(state_key, value)`  
- `publish_release(release_metadata)`  
- `noop_guard()` to assert dry-run semantics  

Dry-run Publisher:

- Implements same interface  
- Logs intent instead of mutating anything  
- Guarantees that **no API calls with side effects** are performed

---

## 📦 8. Runtime Artifacts & Logs

Per-run outputs SHOULD include:

```text
artifacts/
  run.jsonl              — Top-level run events, one per state change
  event_log.jsonl        — Detailed per-step logs
  idempotency.json       — Ledger record for this run
  publisher_trace.jsonl  — Publisher operations (write_file / emit_event / etc.)
```

All artifacts MUST:

- Be structured (JSON or JSONL)  
- Be schema-valid (updater telemetry schemas)  
- Be attached to CI runs where applicable  

---

## 👥 9. Scheduling & Invocation

### Cron-Based Scheduling

KFM uses standard cron scheduling via:

- GitHub Actions `on.schedule`  
- Airflow / LangGraph scheduler entries  
- External orchestrators (if present)

### Webhook Invocation

Webhook triggers:

- Are handled through `scheduler/webhook_validator.py` or `.mjs`  
- Must pass HMAC validation  
- Translate webhook payload → `updater run` invocation with appropriate flags  

### Manual Invocation

For debugging, operators can run:

```bash
python -m updater.runner run --config config.yml --window P1D --dry-run
```

but such runs MUST be governed in the same way as automated ones.

---

## 📊 10. Telemetry & OpenLineage

Every Updater Runner run MUST:

- Emit OpenTelemetry spans + metrics  
- Emit OpenLineage events with:
  - `job` (pipeline identifier)  
  - `run` (run_id, idempotency_key)  
  - `inputs` / `outputs` (datasets)  

Telemetry aggregated into:

- `releases/<version>/updater-telemetry.json`  
- Central dashboards for:
  - Error rates  
  - Latency  
  - Energy/carbon usage  

---

## ⚖️ 11. FAIR+CARE & Sovereignty

Updater Runners play a critical role in:

- Respecting CARE rules when refreshing data  
- Ensuring runs that might affect sensitive datasets:
  - Pass sovereignty checks  
  - Are linked to governance decisions  
  - Can be fully audited later  

Any violation of CARE or sovereignty rules demands:

- **Immediate halt**  
- Governance council review  
- Postmortem entry in governance ledger  

---

## 🧪 12. Testing Strategy

### Unit Tests

Cover:

- Idempotency key generation  
- Webhook signature verification  
- Publisher behavior (normal + noop)  
- Flag parsing  
- Config loading  

### Integration Tests

Cover:

- End-to-end `cron → idempotency → publish → telemetry` flows  
- Error injection and rollback behavior  
- Race-condition simulation (concurrency groups)  

All tests run in CI jobs under `pipelines-updater-test.yml` (or equivalent).

---

## 🕰 13. Version History

| Version | Date       | Summary                                                                                                  |
|--------:|------------|----------------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; canonical front-matter; added canonical footer; telemetry + governance alignment. |
| v11.0.0 | 2025-11-24 | Initial v11 Updater Runner architecture; defined idempotency, webhook security, and publisher abstraction. |

---

<div align="center">

## 🔁 **Kansas Frontier Matrix — Updater Runners (v11.2.2)**  
*Deterministic automation · Idempotent scheduling · Governance-safe updates*

  
<img src="https://img.shields.io/badge/MCP--DL-v6.3-blue" />
<img src="https://img.shields.io/badge/KFM--MDP-v11.2.2-purple" />
<img src="https://img.shields.io/badge/FAIR%2BCARE-Governed-gold" />
<img src="https://img.shields.io/badge/OpenLineage-v2.5-informational" />
<img src="https://img.shields.io/badge/Automation-Updater_Runners-lightgrey" />

  
© 2025 Kansas Frontier Matrix — MIT License  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to Pipelines](../README.md) ·  
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·  
[📘 KFM Documentation Home](../../../docs/README.md)

</div>
