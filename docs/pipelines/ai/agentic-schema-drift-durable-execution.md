---
title: "🤖 Kansas Frontier Matrix — Agentic Schema Drift Steward & Durable Execution Integration (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/pipelines/ai/agentic-schema-drift-durable-execution.md"
version: "v11.0.0"
last_updated: "2025-11-22"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v11.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v11.0.0/manifest.zip"
telemetry_ref: "../../releases/v11.0.0/agentic-schema-drift-telemetry.json"
telemetry_schema: "../../schemas/telemetry/agentic-schema-drift-v11.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.0.0"
status: "Draft / Experimental"
doc_kind: "Architecture Guide"
---

# 🤖 Kansas Frontier Matrix — Agentic Schema Drift Steward & Durable Execution Integration

This guide explains how to integrate:

- An **autonomous schema-drift maintenance agent** (inspired by “I Built an AI Agent That Maintains Our Data Pipeline”) :contentReference[oaicite:0]{index=0}  
- **Durable execution for Pydantic AI agents with Prefect** (from Prefect’s “Build AI Agents That Resume from Failure with Pydantic AI”) :contentReference[oaicite:1]{index=1}  

into the **KFM v11** stack:

data → ETL / LangGraph DAGs → Neo4j → APIs → React + MapLibre + Cesium → Story Nodes → Focus Mode v3


## 1️⃣ Why This Matters For KFM v11

KFM is constantly pulling from evolving sources:

- Hydrology and sediment datasets (USGS, Corps, DASC)
- Climate normals and projections
- Remote-sensing products (bathymetry, DEMs, geophysics)
- Archival and heritage metadata (CIDOC-CRM, OWL-Time, GeoSPARQL)

Each time a **source schema changes** (new fields, changed types, renamed attributes), you currently pay a “tax”:

- Broken ETL DAGs
- Invalid STAC / DCAT metadata
- Downstream graph inconsistencies (Neo4j)
- Focus Mode narratives that no longer match data realities

The external work shows two key patterns:

1. Use an **agent** to detect schema drift and propose/implement safe changes instead of manual fire drills. :contentReference[oaicite:2]{index=2}  
2. Wrap the agent in **Prefect durable execution** so that failures resume from the last successful step instead of restarting the whole workflow. :contentReference[oaicite:3]{index=3}  

Together, these map almost perfectly onto KFM’s need for **self-healing ETL** and **governed, reproducible AI tooling**.


## 2️⃣ External Patterns Summarized (Mapped To KFM)

### 2.1 🧪 Autonomous Schema Drift Agent (Plain English article)

Key ideas from “I Built an AI Agent That Maintains Our Data Pipeline”: :contentReference[oaicite:4]{index=4}  

- Upstream systems (e.g., Salesforce) silently add fields or change types overnight.
- Dashboards break even though data is still there; the pipeline does not “understand” the new schema.
- The author builds an **agent** that:
  - Monitors source schemas and diffs against a baseline.
  - Identifies drift (new columns, missing columns, type changes, semantics).
  - Proposes migration plans and transformation patches.
  - Benchmarks different LLMs (GPT, Claude, Gemini) to choose the best model for the task.
  - Automatically reruns the relevant parts of the pipeline after applying changes.

For KFM, this pattern translates to:

- Monitor all **registered KFM collections** (STAC, DCAT, Neo4j schema) for drift.
- Use an **agentic “Schema Drift Steward”** to:
  - Propose STAC / DCAT changes.
  - Propose ETL transformation patches (e.g., new column mapping, type casting).
  - Generate graph-migration Cypher when nodes/relationships need to evolve.


### 2.2 🧷 Durable Execution For Pydantic AI Agents With Prefect

From Prefect’s “Build AI Agents That Resume from Failure with Pydantic AI”: :contentReference[oaicite:5]{index=5}  

- AI agents are fragile: LLM timeouts, rate limits, tool failures, network flakiness.
- Pydantic AI provides **typed agents with structured outputs**.
- Prefect adds:
  - **Durable execution**: workflows resume from the point of failure instead of restarting.
  - **Task-level retries, caching, timeouts** for LLM calls and tool invocations.
  - Standard **observability and scheduling** across AI and non-AI parts of the pipeline.

Typical pattern:

- Define a Pydantic AI `Agent` (e.g., `data_analyst`).
- Wrap it with a `PrefectAgent` that:
  - Exposes the agent as a Prefect flow.
  - Treats each LLM call/tool call as a Prefect task with caching and retry policies. :contentReference[oaicite:6]{index=6}  

For KFM, this means the **Schema Drift Steward** is not just a script but a **Prefect-managed, type-safe, resumable component** in the data platform.


## 3️⃣ KFM v11 Agent Roles

We define two primary agent roles, both implemented with Pydantic AI and orchestrated by Prefect:

1. 🛰️ **Schema Drift Steward**
   - Watches KFM sources (STAC collections, tabular schemas, Neo4j constraints).
   - Detects and explains drift.
   - Proposes and optionally applies migration patches.
   - Emits PROV-O lineage and FAIR+CARE tags for all decisions.

2. 🧪 **Transform Benchmarker**
   - Evaluates multiple candidate transform strategies/models when drift is non-trivial.
   - Benchmarks:
     - Data quality metrics (null rates, ranges, constraint violations).
     - Model impact (if features feed downstream ML).
     - Runtime / cost.
   - Outputs a **ranked, explainable recommendation**.

Both roles must be:

- **Deterministic in interface** (Pydantic schemas).
- **Durable and resumable** (Prefect flows and tasks).
- **Governed** (linked to MCP-DL v6.3 and KFM governance ledgers).
- **Observable** (exporting telemetry bundles for v11 dashboards).


## 4️⃣ Reference Architecture For KFM v11

### 4.1 High-Level Flow

Conceptual flow for schema drift handling:

1. **Detection Layer (non-AI, deterministic)**
   - Compare current source schema (e.g., KDW table, external shapefile, NetCDF, STAC item) to registered baseline.
   - Produce a `SchemaDriftEvent` document:
     - source_id
     - old_schema
     - new_schema
     - change_diff
     - severity (low, medium, high)

2. **Agent Layer (Pydantic AI + LangGraph DAG)**
   - Input: `SchemaDriftEvent`.
   - Tasks:
     - Classify drift type (cosmetic vs structural vs semantic).
     - Propose ETL transform patch.
     - Propose STAC/DCAT schema updates.
     - Propose Neo4j graph migration (if needed).
     - Produce explanations and risk notes.

3. **Execution & Governance Layer (Prefect)**
   - Wrap agent in a `PrefectAgent`-based flow.
   - Each critical step is a Prefect task:
     - Fetch baseline schemas and tests.
     - Call agent.
     - Validate patch against test suite.
     - Apply patch in a **shadow environment**.
     - Run focused regression subset of LangGraph DAG.
   - If all checks pass, promote to production and emit:
     - Telemetry bundle.
     - PROV-O lineage update.
     - Governance log entry.

4. **Downstream Integration**
   - Update:
     - STAC / DCAT collections.
     - Neo4j schema and data.
     - Focus Mode v3 narrative templates and Story Nodes (e.g., “hydrology schema changes in 2025Q4”).
   - Surface events in validation / observability dashboards.


### 4.2 ASCII Architecture Sketch

This is a conceptual map (not a strict component diagram):

    [1] Source Systems (Hydrology, Climate, Remote Sensing, Archival, etc.)
        |
        v
    [2] Schema Snapshotter
        |
        v
    [3] Schema Drift Detector
        |
        v
    [4] SchemaDriftEvent Queue  --->  [Ops Notification / Slack / Email]
        |
        v
    [5] Prefect Flow: kfm_schema_drift_steward
        |
        +--> Task: Load Baseline Schemas
        |
        +--> Task: Run Pydantic AI Schema Drift Steward Agent
        |         (LLM calls, tools, retrieval)
        |
        +--> Task: Validate Proposed Patch (tests, constraints)
        |
        +--> Task: Apply Patch in Shadow Env
        |
        +--> Task: Run Focused LangGraph DAG Subset
        |
        +--> Task: Promote Patch to Prod (if safe)
        |
        +--> Task: Emit Telemetry + PROV + Governance Events
        |
        v
    [6] Updated STAC/DCAT, ETL Code, Neo4j, Focus Mode Narratives


## 5️⃣ Minimal Implementation Blueprint (Pseudo-Code)

Below is implementation-flavored pseudo-code using Pydantic AI and Prefect. It is intentionally abstracted to keep KFM-specific paths and names flexible.

### 5.1 Pydantic Models

    from pydantic import BaseModel
    from typing import List, Dict, Optional

    class FieldChange(BaseModel):
        name: str
        change_type: str  # "added", "removed", "type_changed", "renamed"
        old_type: Optional[str] = None
        new_type: Optional[str] = None
        notes: Optional[str] = None

    class SchemaDriftEvent(BaseModel):
        source_id: str
        source_kind: str            # "stac", "tabular", "netcdf", "neo4j"
        old_schema: Dict[str, str]  # name -> type
        new_schema: Dict[str, str]
        detected_at: str            # ISO 8601
        field_changes: List[FieldChange]
        severity: str               # "low", "medium", "high"

    class TransformPatch(BaseModel):
        etl_patch_id: str
        description: str
        code_diff: str              # unified diff or patch instructions
        stac_updates: Dict[str, str]
        graph_migration_cypher: Optional[str] = None
        breaking_change_risk: str   # "low", "medium", "high"

    class PatchEvaluation(BaseModel):
        patch_id: str
        data_quality_score: float
        test_pass_rate: float
        runtime_delta_seconds: float
        model_impact_notes: str
        overall_recommendation: str  # "accept", "reject", "manual_review"


### 5.2 Schema Drift Steward Agent (Pydantic AI)

    from pydantic_ai import Agent

    schema_drift_steward = Agent(
        model="openai:gpt-4.1-mini",   # example; model selection is configurable
        name="kfm_schema_drift_steward",
        system_prompt=(
            "You are the Schema Drift Steward for the Kansas Frontier Matrix (KFM). "
            "Given a SchemaDriftEvent, propose a safe TransformPatch that preserves "
            "semantic meaning, respects FAIR+CARE, and minimizes breaking changes."
        ),
        result_type=TransformPatch,
    )

    # Example call (inside a Prefect task later):
    # patch: TransformPatch = schema_drift_steward.run(event)


### 5.3 Prefect Durable Execution Wrapper

Pattern adapted from the Prefect Pydantic AI integration: wrap the agent so that LLM/tool calls are **Prefect tasks** with caching and retries. :contentReference[oaicite:7]{index=7}  

    from prefect import flow, task
    from pydantic_ai.providers.prefect import PrefectAgent, TaskConfig

    prefect_schema_drift_agent = PrefectAgent(
        schema_drift_steward,
        model_task_config=TaskConfig(
            retries=3,
            retry_delay_seconds=30,
            cache_ttl_seconds=3600,
        ),
        tool_task_config=TaskConfig(
            retries=2,
            retry_delay_seconds=60,
            cache_ttl_seconds=3600,
        ),
    )

    @task
    def load_baseline(event: SchemaDriftEvent):
        # load baseline schema, tests, and governance constraints
        # from KFM registries and Git-based ETL repo
        ...

    @task
    def validate_patch(patch: TransformPatch, event: SchemaDriftEvent) -> PatchEvaluation:
        # run unit tests, data quality checks, and sample DAG runs
        ...

    @task
    def apply_patch_shadow(patch: TransformPatch, event: SchemaDriftEvent):
        # apply patch in shadow environment (non-production)
        ...

    @task
    def promote_patch(patch: TransformPatch, evaluation: PatchEvaluation):
        # gated promotion logic with governance checks
        ...

    @task
    def emit_governance(patch: TransformPatch, evaluation: PatchEvaluation, event: SchemaDriftEvent):
        # write PROV-O, FAIR+CARE metadata, and telemetry bundle
        ...

    @flow(name="kfm_schema_drift_steward_flow")
    def kfm_schema_drift_steward_flow(event: SchemaDriftEvent):
        baseline = load_baseline(event)
        # durable execution: if the agent or tools fail, Prefect can resume here
        patch: TransformPatch = prefect_schema_drift_agent.run(event)
        evaluation = validate_patch(patch, event)
        apply_patch_shadow(patch, event)

        if evaluation.overall_recommendation == "accept":
            promote_patch(patch, evaluation)
        else:
            # route to manual review workflow
            ...

        emit_governance(patch, evaluation, event)


### 5.4 LangGraph Integration (Optional, Recommended)

Inside the agent itself, you can still use **LangGraph** to orchestrate:

- Retrieval of KFM registries and historical patches.
- Tool calls for:
  - STAC validation.
  - DCAT validation.
  - Graph schema introspection.
  - Telemetry bundle summarization.

Prefect remains the **outer workflow engine** with durable execution; LangGraph remains the **agent runtime** for complex reasoning and tool routing.


## 6️⃣ Benchmarking & Safety In KFM Context

The plain-english article benchmarks different LLMs (GPT, Claude, Gemini) for schema maintenance tasks and uses those results to pick the best fit. :contentReference[oaicite:8]{index=8}  

For KFM, define an **internal benchmark harness**:

- Tasks:
  - Basic drift classification (added/removed/renamed/type-changed fields).
  - Semantic mapping (e.g., `gage_height_ft` vs `water_level_m`).
  - STAC property mapping (e.g., `gsd`, `platform`, `instruments`).
  - Graph migration planning (node/edge additions).

- Metrics:
  - Accuracy of classification compared to a human-labeled gold set.
  - Number of breaking patches caught by tests before promotion.
  - Time-to-repair after drift.
  - Token and runtime cost.

- Safety Policies:
  - No direct production writes without:
    - Passing a minimal test suite.
    - Passing governance checks for FAIR+CARE and data ethics.
  - For high-severity drift, **require human-in-the-loop** even if tests pass.


## 7️⃣ Focus Mode v3 & Story Node Integration

Every schema drift event and patch can itself become **knowledge**:

- Story Node v3:
  - “How KFM adapted to the 2025 Kansas River bathymetry schema change.”
  - “Why a new climate normal field was added and how we harmonized it.”

- Focus Mode v3:
  - When a user is exploring **Kansas River hydrology in 1993–2007**, Focus Mode can:
    - Overlay a timeline of important schema migrations that affect interpretation.
    - Annotate charts or maps with “Data schema changed here; see patch KFM-SCHEMA-2025-11-003.”

Implementation pattern:

- When `emit_governance` runs, it:
  - Writes a concise “narrative summary” of the change.
  - Links to:
    - Telemetry bundle.
    - PROV chain for the impacted dataset.
    - The Prefect run id.
  - Registers a Story Node template entry that Focus Mode can pull into narratives.


## 8️⃣ Governance, Telemetry, FAIR+CARE Hooks

The Schema Drift Steward and Transform Benchmarker must be **first-class governed components**:

- MCP-DL v6.3:
  - All flows registered as governed pipelines.
  - Required metadata:
    - agent_name, agent_version
    - model_name, model_version
    - tools used
    - input and output schemas (Pydantic models)

- Telemetry Bundles:
  - For each run:
    - drift_event_id
    - chosen_patch_id
    - evaluation metrics
    - Prefect run id
    - LangGraph run id (if applicable)
    - energy and carbon metrics (tied into existing energy/telemetry schemas)

- FAIR+CARE:
  - Agent instructions must explicitly enforce:
    - Preservation of data context and meaning.
    - Protection of sensitive heritage locations (e.g., H3 generalization).
    - Respect for tribal and community governance expectations.

- Neo4j / PROV-O:
  - Each patch becomes:
    - A `prov:Activity` linked to:
      - Previous and new dataset versions.
      - Agents (software and human) involved.
      - Governance decisions (e.g., manual overrides).


## 9️⃣ Rollout Plan For KFM v11

A pragmatic rollout strategy:

1. 🥽 Phase 0 — Observation Only
   - Build the Schema Drift Detector and emit `SchemaDriftEvent` objects.
   - No agent, no auto-patching; just dashboards and alerts.

2. 🧪 Phase 1 — Propose-Only Agent
   - Run the Schema Drift Steward agent and produce `TransformPatch` proposals.
   - Do not apply; compare to human patches and collect benchmarks.

3. 🌓 Phase 2 — Shadow Apply
   - Apply patches in a **shadow environment** only.
   - Run a subset of LangGraph DAGs and Focus Mode stories to detect regressions.

4. 🚦 Phase 3 — Gated Auto-Apply
   - Auto-apply low-risk patches that:
     - Pass tests.
     - Have high evaluation scores.
     - Affect non-sensitive collections.
   - Keep medium/high-risk drift behind manual approval.

5. 🌐 Phase 4 — Full Platform Integration
   - Integrate with:
     - KFM-wide validation and observability dashboards.
     - Story Node v3 and Focus Mode v3 narrative surfaces.
     - All relevant STAC/DCAT collections and Neo4j schemas.


## 🔚 Standardized Footer (KFM v11 Navigation)

- ⬅️ [Back to Pipelines & Orchestration](../README.md)  
- 🏛️ [KFM v11 Architecture Index](../../ARCHITECTURE.md)  
- ⚖️ [FAIR+CARE & Governance Standards](../standards/governance/ROOT-GOVERNANCE.md)  
