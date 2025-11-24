---
title: "🔁 KFM v11 — Updater Runners (Idempotent Schedulers · Webhooks · Dry-Run Safety · Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/pipelines/updater/README.md"
version: "v11.0.0"
last_updated: "2025-11-24"
review_cycle: "Quarterly · FAIR+CARE Council · Reliability Engineering"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/updater-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-updater-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active · Enforced"
doc_kind: "Architecture"
intent: "updater-scheduling-and-webhooks"
semantic_document_id: "kfm-updater-runners"
doc_uuid: "urn:kfm:pipelines:updater:runners:v11.0.0"
machine_extractable: true
classification: "Updater Scheduling Architecture"
sensitivity: "Mixed"
fair_category: "F1-A1-I2-R2"
care_label: "Collective Benefit · Authority to Control · Responsibility · Ethics"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
ttl_policy: "Annual review"
sunset_policy: "Superseded by Updater Runners v12"
---

<div align="center">

# 🔁 **KFM Updater Runners — Idempotent Schedulers, Webhooks & Dry-Run Safety (v11 LTS)**  
`src/pipelines/updater/README.md`

### **Deterministic · Governed · Telemetry-Rich · FAIR+CARE Enforced · Concurrency-Safe**

Updater Runners form the **executive automation layer** for KFM’s dataset refresh, metadata updates, multi-source ETL synchronizations, STAC polling, and governance-aware refresh cycles.

They guarantee:

- **Idempotency**  
- **Dry-run safety**  
- **Structured JSON logs**  
- **HMAC-verified webhook ingestion**  
- **Concurrency fencing**  
- **Telemetry + lineage + governance logging**  
- **No-op correctness under freeze/kill-switch modes**  

</div>

---

## 📘 1. Purpose

Updater Runners standardize **Python + Node.js** execution for autonomous update cycles across:

- Ingest pipelines  
- STAC pipelines  
- ETL pipelines  
- Metadata refresh flows  
- Focus Mode v3 context generation  
- Remote-sensing deltas  
- Story Node v3 content regeneration  
- Governance-led data corrections  

They ensure **deterministic, reversible, reproducible** automation with full integration into:

- WAL  
- Retry/backoff  
- CARE/sovereignty gates  
- Governance ledger  
- OpenLineage v2.5  
- OTel telemetry v11  
- SLO/error-budget systems  

---

## 🧩 2. Core Design Requirements

### 2.1 Idempotent Execution

```
idempotency_key = sha256(source_url | etag | window | pipeline_version)
```

Prevents duplicate processing, ensures WAL-safe replay, and preserves lineage integrity.

### 2.2 Dry-Run Safety

All mutating actions route through a **Publisher abstraction**, guaranteeing:

- Zero mutations on disk  
- Zero API writes  
- Complete JSONL logging  
- Full reproducibility of what *would* have happened  

### 2.3 Concurrency Fencing

All runners must:

- Use **GitHub Actions concurrency groups**  
- Respect **dataset-scoped locks**  
- Avoid multiple overlapping executions for the same pipeline  

### 2.4 Governed Execution

All actions must pass:

- FAIR+CARE gates  
- Sovereignty rules (H3 R7→R9 masking)  
- Data Contract v11 checks  
- Governance ledger updates  
- Telemetry emission compliance  

---

## 🧰 3. CLI Entrypoints (Python + Node)

### **Python**

```bash
python -m updater run --config config.yml --dry-run
```

### **Node.js**

```bash
node updater.mjs run --config config.yml --dry-run
```

### **Shared Flags**

| Flag        | Description |
|-------------|-------------|
| `--config`  | Load YAML/JSON configuration file |
| `--dry-run` | Route all writes to noop publisher |
| `--window`  | Incremental lookback window |
| `--force`   | Override idempotency for debugging |
| `--verbose` | Human-readable logs alongside JSONL |

Runners **must behave identically across languages**, with canonical JSONL outputs.

---

## 📦 4. Runtime Folder Layout (v11)

```text
src/pipelines/updater/
│
├── README.md
│
├── runner.py
├── runner.mjs
│
├── idempotency/
│   ├── keygen.py
│   ├── keygen.mjs
│   ├── ledger.py
│   └── ledger.mjs
│
├── publisher/
│   ├── base.py
│   ├── base.mjs
│   ├── noop.py
│   ├── noop.mjs
│   ├── github_actions.py
│   ├── github_actions.mjs
│
├── scheduler/
│   ├── cron.yml
│   ├── webhook_validator.py
│   └── webhook_validator.mjs
│
└── config_templates/
    ├── config.example.yml
    └── sources.example.json
```

---

## 🔐 5. Webhook Security (HMAC)

### Required Header

```
X-KFM-Signature: sha256=<hex>
```

### Verification Process

1. Extract raw request body  
2. Compute `sha256(secret + body)`  
3. Compare to provided signature  
4. Reject with `403` on mismatch  
5. Log details to `webhook_failures.jsonl`  

Webhooks must include:

- `source_id`  
- `trigger`  
- `event_type`  
- `sent_at`  
- `integrity.version`  

---

## 🔁 6. Idempotency Model (v11)

Idempotency ledger stores:

- `run_id`  
- `dataset_id`  
- `idempotency_key`  
- `timestamp`  
- `source_metadata`  
- `pipeline_version`  

Backends:

- **SQLite** (preferred)  
- **JSONL** fallback  

Duplicate keys → NOOP execution.

---

## 🧮 7. Publisher Abstraction (v11)

All side-effects **must** go through a Publisher.

### Required Interface Methods

| Method | Description |
|--------|-------------|
| `write_file` | Write or update artifact |
| `emit_event` | Emit telemetry event |
| `update_metadata` | Modify state metadata |
| `publish_release` | Upload GH artifacts |
| `noop_guard` | Prevent accidental side effects |

### Dry-Run Mode Guarantees

- All writes become NOOP  
- Telemetry labeled with `"dry_run": true`  
- All potential mutations logged in publisher trace  

---

## 🧪 8. Logs & Artifacts (v11)

Every run produces:

```text
artifacts/
├── run.jsonl
├── event_log.jsonl
├── idempotency.json
└── publisher_trace.jsonl
```

All logs must be:

- Deterministic  
- Structured  
- Ordered by timestamp  
- Validated via JSON Schema  
- Attached to GitHub Actions artifacts  

---

## 🧭 9. Scheduling Model

### GitHub Actions

- `cron` (hourly or domain-specific)  
- `repository_dispatch` (webhook)  
- `workflow_dispatch` (manual)  
- Concurrency groups:  
  ```
  concurrency: updater-${{ matrix.dataset }}
  ```

### Webhook Fan-In

Unified schema:

```json
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

## 🧩 10. Standard Run Lifecycle (v11)

```text
Watcher/Event → Idempotency → Validation → Transform → Publish → Telemetry → Ledger
```

---

## 📈 11. Telemetry Requirements (v11)

Events must include:

- `run_id`  
- `duration_ms`  
- `dataset`  
- `source_id`  
- `trigger`  
- `idempotency_state`  
- `artifact_count`  
- `dry_run` flag  
- `errors`  

Telemetry bundles stored in:

```
releases/<version>/updater-telemetry.json
```

---

## ⚖️ 12. Governance Requirements (FAIR+CARE + Sovereignty)

Updater pipelines must:

- Respect dataset CARE labels  
- Apply sovereignty masking  
- Include governance metadata in logs  
- Write ledger entries for:
  - failures  
  - escalations  
  - sovereignty conflicts  
- Reject malformed deltas or ambiguous evidence  
- Never mutate protected locations in dry-run  

Governance failures = **CI BLOCK + Review Required**.

---

## 🧪 13. Testing Requirements

### Unit Tests

- idempotency  
- webhook signature verification  
- publisher NOOP behavior  
- artifact writing  
- structured logs  
- dry-run flag propagation  

### Integration Tests

- “cron → run → artifacts → ledger”  
- concurrency group tests  
- error injection + graceful recovery  

---

## 🕰️ 14. Version History

| Version | Date | Summary |
|--------:|------|---------|
| v11.0.0 | 2025-11-24 | Complete KFM-MDP v11 rewrite with governance, 
lineage, sovereignty, WAL, concurrency, and telemetry integration. |
| v10.4.2 | 2025-11-16 | Prior version: initial architecture & updater model. |

---

<div align="center">

© 2025 Kansas Frontier Matrix  
**Reliable Automation × Idempotent Scheduling × Governance-Safe Delivery**  
FAIR+CARE · Diamond⁹ Ω / Crown∞Ω · MCP-DL v6.3

</div>