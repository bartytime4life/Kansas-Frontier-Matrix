---
title: "🔁 KFM v11 — Reliable LangGraph Node Execution Engine (WAL · Retry · Rollback · Deterministic Resume)"
path: "src/pipelines/langgraph/reliable-nodes/README.md"
version: "v11.0.1"
last_updated: "2025-11-24"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../../releases/v11.0.0/reliability-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/reliability-execution-engine-v11.json"
governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0"
ontology_protocol_version: "KFM-OP v11.0"
pipeline_contract_version: "KFM-PDC v11.0"
status: "Active / Enforced"
doc_kind: "Execution Engine"
intent: "reliable-langgraph-node-execution"
semantic_document_id: "kfm-execution-engine-langgraph-reliable-nodes"
doc_uuid: "urn:kfm:execution-engine:langgraph:reliable-nodes:v11.0.1"
machine_extractable: true
classification: "Internal Reliability Component"
sensitivity: "Low"
fair_category: "F1-A1-I2-R2"
care_label: "Responsible · Stewardship"
immutability_status: "version-pinned"
accessibility_compliance: "WCAG 2.1 AA+"
jurisdiction: "Kansas / United States"
ttl_policy: "Annual review"
sunset_policy: "Superseded by next execution-engine redesign"
---

<div align="center">

# 🔁 **Reliable LangGraph Node Execution Engine (v11 LTS)**  
`src/pipelines/langgraph/reliable-nodes/README.md`

**Purpose:**  
Define the **governed, deterministic, WAL-backed, retry-safe node execution engine** used across all LangGraph v11 DAGs in KFM — including ETL, AI inference, Story Node generation, hydrology reconstruction, climate downscaling, and autonomous update loops.

</div>

---

## 📘 1. Overview

The **Reliable LangGraph Node Execution Engine** is the v11 KFM **Reliable Execution Subsystem**.

It guarantees:

- Deterministic node execution  
- Stateful recovery from failures (crash-safe)  
- Bounded retries with exponential backoff + jitter  
- Node-level **Write-Ahead Logging (WAL)**  
- Content-addressable caching  
- Safe compensation for side-effects  
- Automatic lineage emission (OpenLineage + PROV-O)  
- Energy & carbon telemetry per attempt  
- Integration with SLOs, error budgets, and kill-switch controls  

This is the same mechanism that powers:

- **KFM Autonomous Update Loop (AUL v11)**  
- Reliable ETL pipelines  
- Climate & hydrology reconstruction DAGs  
- Story Node v3 / Focus Mode v3 production DAGs  

---

## 🗂 2. Directory Layout

```text
src/pipelines/langgraph/reliable-nodes/
│
├── README.md                     # This document
├── node_runner.py                # NodeRunner: WAL + retry + compensation + telemetry
├── cache_store.py                # Content-addressed caching layer
├── wal_store.py                  # WAL writer/reader (atomic, append-only)
├── compensation.py               # Compensation function registry
├── lineage.py                    # OpenLineage + PROV-O event emitter
│
├── policies/
│   ├── retry_policy.py           # RetryPolicy definitions (max_attempts, backoff, jitter)
│   ├── validation_policy.py      # Pre/post validation rules (schema, CARE, governance)
│   └── energy_policy.py          # Energy & carbon telemetry hooks
│
└── examples/
    ├── example_node.py           # Example wrapped LangGraph node
    └── example_graph.py          # Mini DAG demonstrating resume & caching
```

---

## 🧩 3. Core Execution Model

Each LangGraph node is executed via **NodeRunner**:

1. Construct **content-addressed identity**  
2. Check cache → short-circuit if identical result already exists  
3. Acquire any required locks (via higher-level reliability modules)  
4. Create WAL pre-state entry  
5. Execute with configured retry policy  
6. On success, persist post-state and result hash  
7. Emit OpenLineage + PROV-O events  
8. Emit OTel metrics (latency, retries, cache hit/miss, energy/carbon)  
9. Release locks (if applicable)

The design ensures that:

- Failed attempts do not corrupt state  
- Successful attempts can be **replayed logically** without duplication  
- Resume-from-checkpoint is safe and deterministic  

---

## 🧮 4. Content-Addressed Cache

Each node execution is uniquely identified by:

```python
cache_key = sha256(
    f"{node_id}|{code_version}|{inputs_hash}|{data_version}"
)
```

Where:

- `node_id` — LangGraph node name or unique ID  
- `code_version` — commit SHA or version tag  
- `inputs_hash` — hash of the input state subset used by the node  
- `data_version` — data contract version or dataset version fingerprint  

### Behavior

- If `cache_key` exists in `cache_store`, **NodeRunner** returns the cached result  
- Downstream nodes see **identical state** as if the node re-ran  
- Cache invalidation is triggered when:
  - Code changes  
  - Data version changes  
  - Policy changes (e.g., validation rules)  

This makes repeated DAG executions efficient and repeatable.

---

## 📜 5. Write-Ahead Log (WAL) Layout

For each `(run_id, node_id)` combination:

```text
wal/<run_id>/<node_id>/
  ├── pre.json              # Input snapshot + environment metadata
  ├── attempts.json         # List of attempt records (timestamps, statuses)
  ├── post.json             # Final state snapshot + outputs (on success)
  └── compensation.json     # Compensation attempts and failures (optional)
```

### WAL Guarantees

- WAL is append-only and atomic at the file level  
- WAL entries are written before any external side-effects are committed  
- WAL is synced to disk/cloud before NodeRunner signals success  
- Replay tools can reconstruct node state and lineage from WAL alone  

---

## 🔁 6. Retry & Backoff Policies

Retry behaviors are defined in `policies/retry_policy.py`.

### Example Policy

```python
RetryPolicy(
    max_attempts=5,
    base_delay_s=2.0,
    max_delay_s=60.0,
    jitter_factor=0.3,
    retry_on=(TransientError, NetworkError),
    no_retry_on=(ValidationError, GovernanceError)
)
```

### Backoff Formula

```python
delay = min(base_delay_s * 2 ** (attempt - 1), max_delay_s)
delay *= (1.0 + random.uniform(-jitter_factor, jitter_factor))
```

**No-retry** errors (e.g., schema/gov violations) cause immediate node failure, feeding into:

- SLO/error budget logic  
- GE Checkpoint integration  
- Governance/FAIR+CARE alerts  

---

## 🧷 7. Compensation Layer

Certain nodes perform **side-effects** (e.g., write to S3, Neo4j, or external APIs).  

For those, a compensation function may be registered:

```python
def compensate_fn(previous_state, wal_entry):
    # Undo staged artifacts, clean temp objects, or mark lineage as reverted
    ...
```

Compensation:

- Runs when a node fails after partial side-effects  
- Must be idempotent and deterministic  
- Must not violate CARE or sovereignty policies  
- Is logged in `compensation.json`  

This allows safe rollback of **staging artifacts** while preserving full WAL/lineage history.

---

## 🧬 8. Lineage & Telemetry Integration

### Lineage

`lineage.py` emits:

- **PROV-O** entities for node inputs/outputs  
- **OpenLineage v2.5** events with:
  - `job` = pipeline + node  
  - `run` = run_id  
  - `inputs`, `outputs` referencing STAC/DCAT IDs  
  - `facets` including CARE, sovereignty, data contracts  

### Telemetry

Each attempt logs OTel metrics such as:

- `kfm.node_latency_ms`  
- `kfm.node_retries`  
- `kfm.node_cache_hits`  
- `kfm.node_cache_misses`  
- `kfm.node_energy_wh`  
- `kfm.node_carbon_gco2e`  

with labels:

- `pipeline`  
- `node`  
- `env`  
- `dataset_id` (if applicable)  

This feeds Reliability dashboards and SLO/error-budget logic.

---

## 🌐 9. LangGraph Integration Pattern

Nodes are defined as:

```python
from .node_runner import NodeRunner
runner = NodeRunner(...)

def my_node_fn(state):
    # Pure function: state in -> state out
    ...

graph.add_node(
    "my_node",
    lambda state: runner.run(
        node_id="my_node",
        code_version=GIT_SHA,
        inputs=state,
        exec_fn=my_node_fn,
        compensate_fn=my_compensate_fn,  # optional
    )
)
```

### Rules

- `exec_fn` must be **pure** with respect to the passed-in state  
- Side-effects must be isolated and governed via `compensate_fn` or higher-level SOPs  
- NodeRunner must be the **only** gate for node execution in reliability-critical DAGs  

---

## 🧭 10. Relationship to Other Reliability Modules

This engine interoperates with:

- `docs/pipelines/reliability/README.md` — Reliability root spec  
- `docs/pipelines/reliability/idempotency-concurrency/README.md` — idempotency + advisory locks  
- `docs/pipelines/validation-observability/checkpoints-otel/README.md` — GE + OTel validation  
- `docs/pipelines/reliability/slo-error-budgets.md` — SLO + error budgets  
- `docs/pipelines/release/runbooks/rollback-runbook.md` — rollback procedures  

LangGraph node execution is **one layer** of KFM reliability; it leverages idempotency keys, advisory locks, and GE/OTel checkers at higher levels.

---

## 🔒 11. Governance, FAIR+CARE, and Safety

This component must:

- **Not bypass** sovereignty policies or CARE checks  
- Ensure WAL content does not expose sensitive coordinates (when applicable)  
- Emit governance-relevant metadata in lineage events  
- Respect kill-switches and pipeline freezes triggered by governance or reliability modules  
- Avoid re-running nodes on sovereign datasets without explicit approvals when in “red” error-budget zone  

It is a core part of the **Autonomous Systems Safety Charter** for KFM v11.

---

## 🧯 12. Failure Modes & Recovery

### Possible Failures
- WAL write failure  
- Cache corruption  
- Non-deterministic exec_fn behavior  
- Infinite retry due to misconfigured policy  
- Compensation failure  

### Recovery Strategies
- Fallback to previous WAL snapshot  
- Mark node as permanently failed and trigger rollback runbook  
- Invalidate cache keys impacted by corruption  
- Escalate to reliability + governance review for sovereign data  

---

## 🕰 13. Version History

| Version | Date | Summary                                                                 |
|--------:|------|-------------------------------------------------------------------------|
| v11.0.1 | 2025-11-24 | Upgraded to KFM-MDP v11; added lineage/telemetry details and governance hooks. |
| v11.0.0 | 2025-11-24 | Initial description of reliable LangGraph node execution engine.   |

---

<div align="center">

© 2025 Kansas Frontier Matrix — Reliable Pipelines v11  
Diamond⁹ Ω / Crown∞Ω · FAIR+CARE · MCP-DL v6.3  
“Every node is a contract. WAL + cache make it invocable without fear.”  

</div>