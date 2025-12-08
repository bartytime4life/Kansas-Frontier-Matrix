---
title: "🤖 Kansas Frontier Matrix — Agents & Orchestration Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/agents/README.md"
version: "v11.2.4"
last_updated: "2025-12-08"

release_stage: "Stable · Governed (Index)"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Pipelines WG · FAIR+CARE Council"
content_stability: "stable"
status: "Active / Canonical"
doc_kind: "Agents Index"

header_profile: "standard"
footer_profile: "standard"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-hash>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../releases/v11.2.4/agents-telemetry.json"
telemetry_schema: "../../schemas/telemetry/agents-index-v1.json"
energy_schema: "../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../docs/standards/faircare/FAIRCARE-GUIDE.md"
---

<div align="center">

# 🤖 **Kansas Frontier Matrix — Agents & Orchestration Index**  
`src/agents/README.md`

**Purpose**  
Serve as the **canonical index and governance wrapper** for all **agents & orchestration components** in the Kansas Frontier Matrix (KFM), including LangGraph-based agents, pipeline orchestrators, lineage repair helpers, and future Focus Mode–aware agents.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../LICENSE)  
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Agents-orange)](../../docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![Status: Canonical](https://img.shields.io/badge/Status-Agents_Index-brightgreen)](../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

KFM **agents** are governed, config-driven orchestration surfaces that sit between:

> **Deterministic ETL & STAC/DCAT/PROV pipelines**  
> → **Neo4j Knowledge Graph**  
> → **APIs & Frontends**  
> → **Story Nodes & Focus Mode**

They:

- React to **events** (e.g., `stac.update`, lineage alerts, telemetry thresholds).  
- Plan and execute **minimal, deterministic recomputation** or **targeted workflows**.  
- Emit **telemetry, PROV-O, and OpenLineage** records.  
- Respect **FAIR+CARE** and **sovereignty** constraints defined in standards and pipeline docs.

This index:

- Describes the **agents surface area**.  
- Defines the **directory layout** under `src/agents/`.  
- Outlines **governance, CI/CD, and telemetry expectations**.  
- Points to concrete agent designs (e.g., LangGraph STAC Refresh Agent).

---

## 🗂️ Directory Layout

```text
📁 repo-root/
├── 📁 src/
│   └── 📁 agents/
│       ├── 📄 README.md                      # This document (global agents index)
│       └── 📁 langgraph/
│           ├── 📄 README.md                  # LangGraph Agents Index
│           └── 📁 stac_refresh/
│               ├── 📄 README.md              # Agent design: STAC differential recomputation
│               ├── 📄 agent.py               # LangGraph DAG implementation
│               ├── 📄 graph_refresh_manifest.yaml
│               ├── 📁 planners/
│               ├── 📁 executors/
│               ├── 📁 validators/
│               └── 📁 publish/
├── 📁 docs/
│   └── 📁 standards/
│       ├── 📄 README.md                      # Global standards index
│       ├── 📁 governance/
│       │   └── 📄 ROOT-GOVERNANCE.md         # Root governance
│       ├── 📁 faircare/
│       │   └── 📄 FAIRCARE-GUIDE.md          # FAIR+CARE guidance
│       └── 📁 events/
│           └── 📄 README.md                  # Event standards index (contracts for agents)
└── 📁 schemas/
    └── 📁 telemetry/
        ├── 📄 agents-index-v1.json           # Telemetry schema for this index (inventory & health)
        ├── 📄 agents-langgraph-index-v1.json
        └── 📄 agent-stac-refresh-v1.json
```

> ⚠️ **New agents MUST:**
> - Live under `src/agents/<framework_or_family>/<agent_name>/`, and  
> - Include a **governed `README.md`** and telemetry schema references, and  
> - Be **registered in this index** before any production use.

---

## 🧩 Agent Categories

### 1️⃣ LangGraph Agents

**Path:** `src/agents/langgraph/`  

LangGraph agents:

- Use **LangGraph DAGs** to orchestrate planning, execution, and publishing steps.  
- Typically react to **event streams** and **STAC/DCAT changes**.  
- Must be:
  - Config-driven (YAML/JSON manifests),  
  - Deterministic (pure functions + explicit state),  
  - Fully instrumented with OpenLineage and telemetry.

Current example:

| Agent Path                       | Status                     | Purpose                                                         |
|----------------------------------|----------------------------|-----------------------------------------------------------------|
| `langgraph/stac_refresh/`        | ✅ Experimental · Governed | Differential recomputation on `stac.update` events; recompute only impacted layers and update DCAT/Neo4j. |

---

### 2️⃣ Future Agent Families (Reserved)

The following families are **reserved** for future governed expansion:

| Family Path                      | Intended Purpose                                               | Governance Note               |
|----------------------------------|----------------------------------------------------------------|--------------------------------|
| `focus/`                         | Agents coordinating Focus Mode queries and Story Node flows   | Requires Focus Mode governance |
| `lineage/`                       | Agents for lineage repair, enrichment, and anomaly response   | Requires lineage governance   |
| `alerting/`                      | Agents that respond to telemetry / SLO alerts with workflows  | Requires Reliability review   |

Any new family:

- Must define its own **index README** under `src/agents/<family>/README.md`.  
- Must link back to this global index and relevant **standards docs**.

---

## 🧱 Common Agent Design Pattern

Regardless of framework, KFM agents should follow a shared design pattern:

1. **Event Intake**
   - Validate incoming events against **event standards** (`docs/standards/events/**`).  
   - Extract identifiers (dataset/STAC IDs, time windows, run IDs, risk flags).

2. **Planning**
   - Load **config/manifest** (YAML/JSON).  
   - Build an internal representation of affected **datasets, tasks, or Story Nodes**.  
   - Compute a **minimal impacted set** (no full-graph recomputes by default).

3. **Execution**
   - Orchestrate work via the chosen framework (e.g., LangGraph).  
   - Use **typed state objects** (dicts or Pydantic models) with clear contracts.  
   - Wrap execution in **OpenLineage spans** and governance-aware logging.

4. **Validation**
   - Apply **Great Expectations** or equivalent where data is written.  
   - Validate **lineage completeness** (Neo4j, STAC/DCAT links, PROV bundles).

5. **Publishing & Lineage**
   - Write updated **STAC/DCAT** items via shared adapters.  
   - Update **Neo4j** nodes/edges and optional PROV bundles.  
   - Ensure events and updates align with **event schemas** and **Fair+CARE** rules.

6. **Telemetry & SLOs**
   - Emit telemetry that conforms to:
     - `telemetry_schema`,  
     - `energy_schema`, `carbon_schema` when applicable.  
   - Track run-level metrics (success, duration, recompute scope).

---

## ⚙️ Governance & CI/CD

### Governance

Agents are governed under:

- `governance_ref` — Root governance & decision-making.  
- `ethics_ref` — FAIR+CARE & sovereignty guidance.

Agents **must not**:

- Bypass schema versioning / deprecation standards.  
- Mutate datasets or graph state outside of documented, deterministic pipelines.  
- Introduce hidden side effects or untracked outputs.

### CI/CD Expectations

A shared agents workflow (e.g. `.github/workflows/agents-ci.yml`) should:

- Lint and type-check all `src/agents/**` code.  
- Validate all **manifests/configs** against schemas.  
- Run **unit and integration tests** (including planner dry-runs for event-driven agents).  
- Verify each agent has:
  - A **governed README** with front-matter.  
  - Telemetry references consistent with `schemas/telemetry/**`.  
  - Links to relevant standards (events, pipelines, governance).

CI must block:

- Agents with missing or invalid docs.  
- Removal or renaming of agents without manifest and governance updates.  
- Any divergence from FAIR+CARE / sovereignty rules in agent behavior.

---

## 🌿 FAIR+CARE & Sovereignty

Agents may orchestrate workflows that touch:

- **Culturally sensitive data** (e.g., heritage sites, community-linked layers).  
- **Sovereignty-governed regions** or datasets (see sovereignty policies).

Requirements:

- Preserve upstream **sensitivity flags and sovereignty markers** (e.g., `x-indigenous`, `x-sovereignty-scope`) in all recomputed outputs.  
- Never reduce masking/generalization levels below upstream requirements.  
- Defer to FAIR+CARE and sovereignty governance when:
  - Creating new views or recomputed layers.  
  - Proposing public-facing Story Node updates.

Any new agent intended to handle such data must be **explicitly flagged** in this index (risk category, governance contacts).

---

## 📡 Telemetry, Energy & Carbon

Agents are responsible for emitting **structured telemetry** that:

- Uses `telemetry_schema` for:
  - Agent runs, health, recompute scope, and error modes.  
- Uses `energy_schema` / `carbon_schema` where energy & carbon can be estimated.

Example metrics:

- Number of impacted tasks vs total possible tasks per event.  
- Distribution of agent run latency, error rates, and retry counts.  
- Energy/carbon per recompute run (for heavy workloads).

These metrics support:

- Reliability & SLO dashboards.  
- FAIR+CARE sustainability audits.  
- Governance evaluations of recomputation policies.

---

## 🕰️ Version History

| Version | Date       | Author / Steward                     | Summary                                                                                      |
|--------:|-----------:|--------------------------------------|----------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Pipelines WG · Agents Maintainers    | Initial Agents & Orchestration Index; defined layout, governance expectations, and CI/telemetry hooks. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · 🤖 Diamond⁹ Ω / 👑 Crown∞Ω Ultimate Certified  

Deterministic ETL → STAC/DCAT/PROV → Neo4j Graph → API → React/MapLibre/Cesium → Story Nodes → Focus Mode  

[⚙️ LangGraph Agents Index](./langgraph/README.md) • [📚 Standards Home](../../docs/standards/README.md) • [⚖️ Governance Charter](../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>