---
title: "⚙️ Kansas Frontier Matrix — LangGraph Agents Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "src/agents/langgraph/README.md"
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

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/agents-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/agents-langgraph-index-v1.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
---

<div align="center">

# ⚙️ **Kansas Frontier Matrix — LangGraph Agents Index**  
`src/agents/langgraph/README.md`

**Purpose**  
Serve as the **canonical index** and **governance wrapper** for all **LangGraph-based agents** in the Kansas Frontier Matrix (KFM), including STAC-driven recomputation, pipeline orchestration helpers, and future Focus Mode–aware agents.

[![Docs · MCP_v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../docs/README.md)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](../../../LICENSE)  
[![FAIR+CARE](https://img.shields.io-badge/FAIR%2BCARE-Agents-orange)](../../../docs/standards/faircare/FAIRCARE-GUIDE.md)  
[![Status: Canonical](https://img.shields.io/badge/Status-Agents_Index-brightgreen)](../../../releases/v11.2.4/manifest.zip)

</div>

---

## 📘 Overview

LangGraph agents in KFM are **governed orchestration surfaces** that sit between:

> **Deterministic ETL & STAC/DCAT/PROV pipelines**  
> → **Neo4j Knowledge Graph**  
> → **Story Nodes & Focus Mode**

They:

- React to **events** (e.g., `stac.update`, lineage alerts, telemetry thresholds).  
- Plan and execute **minimal recomputation** or **targeted workflows**.  
- Emit **telemetry, PROV-O, and OpenLineage** records.  
- Respect **FAIR+CARE** and **sovereignty** constraints defined in standards and pipeline docs.

This index:

- Describes the **LangGraph agents surface area**.  
- Defines the **directory layout** for agents under `src/agents/langgraph/`.  
- Outlines **governance, CI/CD, and telemetry** expectations.  
- Points to concrete agent designs (e.g., STAC Refresh Agent).

---

## 🗂️ Directory Layout

```text
📁 repo-root/
├── 📁 src/
│   └── 📁 agents/
│       └── 📁 langgraph/
│           ├── 📄 README.md                        # This index (LangGraph agents overview & governance)
│           └── 📁 stac_refresh/
│               ├── 📄 README.md                    # Agent design: STAC differential recomputation
│               ├── 📄 agent.py                     # LangGraph DAG implementation
│               ├── 📄 graph_refresh_manifest.yaml  # Declarative dependency + cache manifest
│               ├── 📁 planners/                    # Impact planners
│               ├── 📁 executors/                   # Domain-specific recompute functions
│               ├── 📁 validators/                  # GE + lineage validation helpers
│               └── 📁 publish/                     # DCAT + Neo4j publishing adapters
├── 📁 docs/
│   └── 📁 standards/
│       ├── 📄 README.md                            # Standards index
│       ├── 📁 governance/
│       │   └── 📄 ROOT-GOVERNANCE.md               # Root governance
│       ├── 📁 faircare/
│       │   └── 📄 FAIRCARE-GUIDE.md                # FAIR+CARE guidance
│       └── 📁 events/
│           └── 📄 README.md                        # Event standards index (event contracts for agents)
└── 📁 schemas/
    └── 📁 telemetry/
        ├── 📄 agent-stac-refresh-v1.json           # Telemetry schema for STAC refresh agent
        └── 📄 agents-langgraph-index-v1.json       # Telemetry schema for this index (catalog & health)
```

> ⚠️ Additional LangGraph agents MUST be added under `src/agents/langgraph/<agent_name>/` and **registered in this index** before use in production.

---

## 🧩 LangGraph Agents in KFM

### Current & Planned Agents

| Agent Path                                        | Status        | Purpose                                                         |
|---------------------------------------------------|---------------|-----------------------------------------------------------------|
| `stac_refresh/`                                   | ✅ Experimental · Governed | Differential recomputation on `stac.update` events; recompute only impacted layers and update DCAT/Neo4j. |
| _`focus_orchestration/`_ (reserved)               | 🟡 Planned     | Coordinate Focus Mode queries & Story Node transitions.        |
| _`lineage_repair/`_ (reserved)                    | 🟡 Planned     | Repair/augment lineage when upstream data or schemas shift.    |

Only **documented** and **governed** agents (like `stac_refresh`) may be enabled in production environments.

---

## 🧱 Architectural Role

LangGraph agents play a specific role in the KFM pipeline:

- **Inputs:**
  - Event streams (`stac.update`, lineage violations, telemetry thresholds).  
  - Declarative configs (manifests, YAML configs).  
  - STAC/DCAT metadata and prior Neo4j state.

- **Core responsibilities:**
  - Compute **minimal impacted subgraphs** (datasets, tasks, Story Nodes).  
  - Orchestrate **deterministic retries and recomputations**.  
  - Attach **OpenLineage spans** and **PROV-O derivations**.  
  - Emit **STAC, DCAT, and graph updates** that pass validation.

- **Outputs:**
  - Updated **STAC items** and DCAT datasets.  
  - Neo4j **event and lineage nodes**.  
  - Telemetry for:
    - Agent-level SLOs,  
    - Energy/carbon metrics,  
    - FAIR+CARE governance events.

Agents must treat themselves as **pipeline participants**, not free-form automation:

- Config-driven (no hard-coded paths or secrets).  
- Deterministic (same inputs → same outputs).  
- Re-runnable with **explicit run IDs** and snapshot references.

---

## ⚙️ Common Agent Design Pattern

All LangGraph agents should adhere to a shared pattern:

1. **Event Intake**  
   - Validate incoming event against **event standards** (`docs/standards/events/**`).  
   - Extract identifiers (STAC ID, dataset ID, time window, run ID).

2. **Planning**  
   - Load config/manifest (YAML/JSON).  
   - Build an in-memory representation of the **impact graph**.  
   - Select **minimal impacted units** (datasets, tasks, Story Nodes).

3. **Execution (LangGraph DAG)**  
   - Represent planning, execution, and publishing steps as nodes.  
   - Use **typed state objects** (dict or Pydantic) with clear contracts.  
   - Wrap each node execution in:
     - **OpenLineage span**,  
     - Governance-aware logging.

4. **Validation**  
   - Apply Great Expectations or equivalent to outputs (datasets, STAC items).  
   - Validate metadata and lineage completeness.

5. **Publishing & Lineage**  
   - Emit STAC/DCAT updates via standard adapters.  
   - Update Neo4j lineage and event nodes.  
   - Write or update PROV bundles and optional OpenLineage runs.

6. **Telemetry & SLOs**  
   - Emit structured logs and metrics to `telemetry_ref` using `telemetry_schema`.  
   - Attach energy/carbon estimates for sustainability reporting (where appropriate).

---

## 🧪 Governance & CI Expectations

### Governance

- All LangGraph agents are governed under:

  - `governance_ref` — Root KFM governance.  
  - `ethics_ref` — FAIR+CARE guide and sovereignty rules.  

- Agents must not:
  - Circumvent deprecation or sunset rules for STAC items or schemas.  
  - Create or modify datasets outside of documented, deterministic pipelines.  
  - Introduce **undocumented side effects** (e.g., hidden writes).

### CI/CD

A shared agents workflow (e.g. `.github/workflows/agents-langgraph-ci.yml`) should:

- Lint and type-check all code under `src/agents/langgraph/**`.  
- Validate **manifests** (`graph_refresh_manifest.yaml`, etc.) against schemas.  
- Run **unit tests** for planners and DAG wiring.  
- Dry-run key agents (like `stac_refresh`) with fixture events to:
  - Ensure **minimal recomputation** for small inputs.  
  - Confirm proper **telemetry and lineage** emission.  
- Ensure that:
  - New agents include a `README.md` with **front-matter and governance**.  
  - Telemetry and energy/carbon references are consistent with schemas.

Any violation blocks merge until addressed and, where needed, approved by **Pipelines WG** + **FAIR+CARE Council**.

---

## 🌿 FAIR+CARE & Sovereignty

LangGraph agents may touch **culturally sensitive data** or **sovereignty-linked layers** via STAC & graph operations.

Agents must:

- Respect FAIR+CARE by:
  - Preserving provenance and sensitivity markers from upstream data.  
  - Ensuring downstream layers carry forward appropriate flags and masking rules.

- Respect sovereignty by:
  - Never downscaling masking/generalization constraints from upstream layers.  
  - Handling events marked with sovereignty flags (`x-indigenous`, `x-sovereignty-scope`) in a more conservative, governed mode (e.g., no auto-publish without review).

Whenever a new agent is proposed that touches such data, this index should be updated to:

- Flag its **risk category**.  
- Link to specific **governance or sovereignty policies**.

---

## 📡 Telemetry: Health, Energy & Carbon

Agents are responsible for emitting **structured telemetry** that conforms to:

- `telemetry_schema` — agent-level runs and health checks.  
- `energy_schema` / `carbon_schema` — energy & carbon metrics where estimable.

Examples of metrics:

- Agent run count, success ratio, mean/percentile latency.  
- Number of tasks recomputed vs total possible tasks.  
- Energy and carbon estimates per agent run (especially for heavy recomputation).

These feed:

- Reliability dashboards,  
- FAIR+CARE sustainability reports,  
- Governance audits for recomputation policies.

---

## 🕰️ Version History

| Version | Date       | Author / Steward                     | Summary                                                                                   |
|--------:|-----------:|--------------------------------------|-------------------------------------------------------------------------------------------|
| v11.2.4 | 2025-12-08 | Pipelines WG · LangGraph Maintainers | Initial LangGraph Agents Index; defined directory layout, governance expectations, and CI/telemetry hooks. |

---

<div align="center">

© 2025 Kansas Frontier Matrix Project  
Master Coder Protocol v6.3 · FAIR+CARE Certified · ⚙️ Diamond⁹ Ω / 👑 Crown∞Ω Ultimate Certified  

LangGraph-Orchestrated · Differential & Event-Driven · CI-Enforced · FAIR+CARE- & Sovereignty-Aligned  

[⚙️ STAC Refresh Agent](./stac_refresh/README.md) • [📚 Pipelines & Agents Standards](../../../docs/standards/README.md) • [⚖️ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>