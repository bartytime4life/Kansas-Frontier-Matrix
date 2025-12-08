---
title: "⚙️ Kansas Frontier Matrix — LangGraph Agent for Differential Recomputation (STAC Updates → Layer Refresh) (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/agents/langgraph/stac_refresh/README.md"
version: "v11.2.x"
last_updated: "2025-12-08"

release_stage: "Experimental · Governed"
lifecycle: "Active"
review_cycle: "Monthly · Pipelines WG · FAIR+CARE Council"
content_stability: "experimental"
status: "Experimental / Enforced"
doc_kind: "Agent Design"

header_profile: "standard"
footer_profile: "standard"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.x/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.x/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.x/agents-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/agent-stac-refresh-v1.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"

provenance:
  derivation_model: "STAC→DCAT→Neo4j (PROV-O aligned)"
  lineage_hooks: "OpenLineage v1"
---

<div align="center">

# ⚙️ **LangGraph Agent — STAC Differential Recomputation**  
`stac.update` → dependency walk → targeted recompute → validate → publish  
`src/agents/langgraph/stac_refresh/README.md`

**Purpose**  
Define the **governed design** for a LangGraph-based agent that reacts to `stac.update` events, computes a **minimal impacted task set**, executes only the necessary recomputations, validates results, and updates **DCAT + Neo4j lineage** without full-pipeline reprocessing.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Agent_Governance-orange)](../../../../docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![Status: Experimental](https://img.shields.io/badge/Status-Experimental-brightgreen)](../../../../releases/v11.2.x/manifest.zip)

</div>

---

## 📘 Overview

When any upstream dataset (e.g., **HRRR tile**, **USGS gauge**, **LiDAR strip**) emits a `stac.update` event, this LangGraph agent:

1. Loads `graph_refresh_manifest.yaml` to resolve **declarative dependency chains**.  
2. Computes a **minimal impacted set** of downstream tasks (e.g., transport, energy, sediment).  
3. Executes only those tasks whose **inputs changed** (by content hash and/or temporal windows).  
4. Validates outputs with **Great Expectations + OpenLineage** and updates **DCAT + Neo4j** lineage.

Goals:

- Avoid reprocessing entire pipelines for small upstream changes.  
- Keep the **STAC catalog, DCAT views, and Neo4j graph** fresh, consistent, and **PROV-O aligned**.  
- Provide a reusable, **config-driven pattern** for differential recomputation agents in KFM v11.2.x.

---

## 🗂️ Directory Layout

```text
📁 src/agents/langgraph/stac_refresh/
├── 📄 README.md                       # This document (agent design & governance)
├── 📄 agent.py                        # LangGraph DAG definition & entrypoint
├── 📄 graph_refresh_manifest.yaml     # Declarative dependency graph & cache keys
├── 📁 planners/
│   └── 📄 impact_planner.py           # Computes minimal impacted task set
├── 📁 executors/
│   ├── 📄 transport.py                # Transport-related recomputation functions
│   ├── 📄 energy.py                   # Energy-related recomputation functions
│   └── 📄 sediment.py                 # Sediment-related recomputation functions
├── 📁 validators/
│   ├── 📁 expectations/
│   │   └── 📄 suite_stac_refresh.json # Great Expectations suite for agent outputs
│   └── 📄 lineage.py                  # OpenLineage / PROV-O lineage helpers
├── 📁 publish/
│   ├── 📄 dcat_emit.py                # DCAT emission / updates
│   └── 📄 neo4j_lineage.py            # Neo4j lineage mutations (events & edges)
└── 📁 utils/                          # (optional) loader/hash helpers, if extracted
```

Related:

- STAC collections & items: `data/stac/**`  
- DCAT catalogs: `data/dcat/**`  
- OpenLineage configuration: `.github/workflows/*` + `configs/openlineage.yaml`

---

## 🧾 `graph_refresh_manifest.yaml` — Declarative Dependencies

The **manifest** defines dataset → task triggers and cache semantics. It is the **single source of truth** for:

- Which upstream datasets drive which recomputation tasks.  
- Which logical inputs/outputs each task declares.  
- Which **cache keys** are evaluated to decide whether a task must run.

```yaml
version: 1
hash_scheme: "blake3"              # for fast content-ID comparisons
time_window_policy:
  default_backfill_days: 3         # minimal recompute horizon unless overridden

datasets:
  hrrr_grib:
    provides: [met.wind, met.temp, met.precip]
    triggers:
      - transport.update.runoff
      - energy.update.load_curve
  usgs_gauge_hourly:
    provides: [hydro.discharge]
    triggers:
      - transport.update.routing
      - sediment.update.load
  lidar_dtm_v2:
    provides: [geom.dtm]
    triggers:
      - transport.update.flowdir
      - sediment.update.deposition

tasks:
  transport.update.flowdir:
    inputs: [geom.dtm]
    outputs: [transport.flowdir]
    executor: "executors.transport:run_flowdir"
    cache_keys: ["geom.dtm#hash"]
  transport.update.runoff:
    inputs: [met.precip, met.temp]
    outputs: [transport.runoff]
    executor: "executors.transport:run_runoff"
    cache_keys: ["met.precip#hash", "met.temp#hash"]
  transport.update.routing:
    inputs: [transport.flowdir, hydro.discharge]
    outputs: [transport.routing]
    executor: "executors.transport:run_routing"
    cache_keys: ["transport.flowdir#hash", "hydro.discharge#hash"]
  energy.update.load_curve:
    inputs: [met.temp, met.wind]
    outputs: [energy.load_curve]
    executor: "executors.energy:run_load_curve"
    cache_keys: ["met.temp#hash", "met.wind#hash"]
  sediment.update.load:
    inputs: [hydro.discharge, transport.runoff]
    outputs: [sediment.load]
    executor: "executors.sediment:run_sediment_load"
    cache_keys: ["hydro.discharge#hash", "transport.runoff#hash"]
  sediment.update.deposition:
    inputs: [sediment.load, transport.routing]
    outputs: [sediment.deposition]
    executor: "executors.sediment:run_deposition"
    cache_keys: ["sediment.load#hash", "transport.routing#hash"]
```

### Manifest Governance

- Manifest changes must be reviewed by **Pipelines WG** and, when relevant, **FAIR+CARE Council** (for datasets with cultural / sovereignty implications).  
- CI validates the manifest against a **JSON Schema** and runs **dry-run planners** with fixture `stac.update` events.

---

## 🧠 LangGraph DAG (Agent Flow)

The agent is implemented as a **LangGraph DAG** that:

1. Receives a `stac.update` event.
2. Fetches the corresponding STAC Item and manifest.
3. Computes changed inputs and a **topologically sorted runlist** of impacted tasks.
4. Executes tasks with lineage spans and validation.
5. Publishes DCAT & Neo4j updates.

```python
# src/agents/langgraph/stac_refresh/agent.py
from langgraph.graph import StateGraph, END

from planners.impact_planner import plan_impacted_tasks
from validators.lineage import with_lineage_span
from publish.dcat_emit import emit_dcat_updates
from publish.neo4j_lineage import update_neo4j_lineage
from utils import load_manifest, fetch_stac_item, compute_hashes


def on_stac_update(evt):
    stac_item = fetch_stac_item(evt["stac_id"])
    manifest = load_manifest("graph_refresh_manifest.yaml")
    changed_inputs = compute_hashes(stac_item, manifest)
    runlist = plan_impacted_tasks(changed_inputs, manifest)  # topologically sorted minimal set
    return {"stac_item": stac_item, "runlist": runlist, "manifest": manifest}


def execute_task(state):
    task = state["runlist"].pop(0)
    with with_lineage_span(task):
        module, func = task["executor"].split(":")
        out = __import__(module, fromlist=[func]).__dict__[func](task)
    state.setdefault("results", []).append(out)
    return state


def publish(state):
    emit_dcat_updates(state["results"])
    update_neo4j_lineage(state["results"])
    return state


g = StateGraph(dict)
g.add_node("plan", on_stac_update)
g.add_node("exec", execute_task)
g.add_node("publish", publish)
g.set_entry_point("plan")


def has_more(state) -> bool:
    return len(state.get("runlist", [])) > 0


g.add_conditional_edges(
    "exec",
    lambda s: "exec" if has_more(s) else "publish",
    {"exec": "exec", "publish": "publish"},
)
g.add_edge("plan", "exec")
g.add_edge("publish", END)

graph = g.compile()
```

Notes:

- **State object** is a plain `dict` with keys: `stac_item`, `runlist`, `manifest`, `results`.  
- `impact_planner` must honor **cache_keys** and **time_window_policy** to avoid unnecessary recompute.

---

## 🪪 Idempotence & Caching

Idempotence and caching are governed by `cache_keys` in the manifest:

- Each task declares **logical cache keys** in the form `<input>#hash`.  
- The planner computes current hashes for those inputs and compares them to previous runs.  
- If **none of the cache keys changed**, the task is **skipped**.

Executor requirements:

- **Idempotent writes**:
  - Use write-once semantics and atomic output paths (e.g., versioned folders, object keys).  
  - Prefer **content-addressed outputs** where feasible.  
- **Replay-safety**:
  - Re-running the agent with the same STAC Item and manifest must not corrupt downstream data.

---

## ✅ Validation & Lineage

Validation is **mandatory** for all tasks that produce persisted outputs:

- **Great Expectations**:
  - Suite located at `validators/expectations/suite_stac_refresh.json`.  
  - Runs as part of each executor or as a post-task validation step (per task config).

- **OpenLineage / PROV-O**:
  - Each task execution is wrapped in `with_lineage_span(task)`.  
  - Lineage spans capture:
    - Input STAC Item IDs and hashes  
    - Manifest version  
    - Task ID and executor name  
    - Output asset URIs / IDs

Failure behavior:

- On validation failure:
  - Mark task (and agent run) as **failed**.  
  - Emit a **canary DCAT status** (e.g., “validation_failed”).  
  - Halt further downstream tasks in the DAG.

Lineage updates:

- `publish/neo4j_lineage.py` writes:

  ```text
  (:Dataset)-[:HAS_EVENT]->(:RecomputeEvent)-[:UPDATED_STAC]->(:STACItem)
  ```

  plus any additional relationships required for downstream graphs.

---

## 🔁 Temporal Windows & Backfill

Temporal behavior is governed by `time_window_policy` and (optional) per-task overrides:

- `default_backfill_days`: minimal recompute horizon for most tasks.  
- Agent should:
  - Restrict recomputation to **recent windows** unless explicitly overridden.  
  - Allow per-task policies for:
    - Long-range recalculations (e.g., new LiDAR baseline).  
    - Highly-local updates (single tile / hour windows).

Implementation (suggested):

- Use STAC Item `properties["datetime"]` and `start_datetime`/`end_datetime` to determine effective time windows.  
- Pass computed temporal windows into task executors via the `task` object.

---

## 🚀 CI/CD Hooks

A dedicated workflow (e.g., `.github/workflows/agents-stac-refresh-ci.yml`) should:

- **Validate**:
  - `graph_refresh_manifest.yaml` against a manifest JSON Schema.  
  - `agent.py` for LangGraph DAG invariants (no unreachable nodes, correct edge map).

- **Dry-run**:
  - Use fixture `stac.update` payloads to ensure:
    - Single-tile updates do **not** trigger full-graph recomputes.  
    - High-risk datasets trigger appropriate **FAIR+CARE** flags when recomputed.

- **Check governance**:
  - Confirm this agent is **not enabled in production** outside of approved scopes (since it is `Experimental · Governed`).  
  - Ensure telemetry references match `telemetry_schema` and release manifest entries.

---

## 📦 Quick Start (Local Dev)

```bash
export KFM_PROFILE=dev

python -m src.agents.langgraph.stac_refresh.agent \
  --event '{"type":"stac.update","stac_id":"hrrr-2025-12-08T00"}'
```

Expected behavior:

- Agent loads the manifest.  
- Computes impacted tasks for the given STAC Item.  
- Executes executors in dependency order.  
- Prints / logs a summary of executed tasks, validation results, and lineage updates.

---

## 🕰️ Version History

| Version  | Date       | Author / Steward                    | Summary                                                                                  |
|---------:|-----------:|-------------------------------------|------------------------------------------------------------------------------------------|
| v11.2.x  | 2025-12-08 | Pipelines WG · LangGraph Maintainers | Initial governed LangGraph agent design for STAC-driven differential recomputation in KFM v11.2.x. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · ⚙️ Diamond⁹ Ω / 👑 Crown∞Ω Ultimate Certified  

Differential Recomputation · STAC/DCAT/PROV · LangGraph-Orchestrated · CI-Enforced · FAIR+CARE-Aligned  

[🧠 Agents Index](../README.md) • [📚 Pipelines & Agents Standards](../../../../docs/standards/README.md) • [⚖️ Governance Charter](../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>