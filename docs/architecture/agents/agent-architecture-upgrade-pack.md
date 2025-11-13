---
title: "🧩 Kansas Frontier Matrix — Agent Architecture Upgrade Pack (LangGraph 1.0 • Dynamic Tool Calling • CrewAI 1.4.x)"
path: "docs/architecture/agents/agent-architecture-upgrade-pack.md"
version: "v10.3.1"
last_updated: "2025-11-13"
review_cycle: "Quarterly / FAIR+CARE Council"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../../releases/v10.3.0/sbom.spdx.json"
manifest_ref: "../../../releases/v10.3.0/manifest.zip"
telemetry_ref: "../../../releases/v10.3.0/focus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/agent-upgrade-pack-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧩 **Kansas Frontier Matrix — Agent Architecture Upgrade Pack**  
`docs/architecture/agents/agent-architecture-upgrade-pack.md`

**Purpose:**  
Deliver a fully aligned, memory-rule–compliant **KFM v10.x agent system upgrade**, integrating LangGraph 1.0, Dynamic Tool Calling, and CrewAI 1.4.x.  
Defines architecture, agent governance, DAG orchestration, MCP boundaries, and Focus Mode telemetry mapping.

<img alt="FAIR+CARE" src="https://img.shields.io/badge/FAIR%2BCARE-Compliant-brightgreen" />
<img alt="MCP-DL" src="https://img.shields.io/badge/MCP--DL-v6.3-blueviolet" />
<img alt="Agent Arch" src="https://img.shields.io/badge/AGENT%20ARCH-v10.3.1-orange" />
<img alt="Diamond" src="https://img.shields.io/badge/Diamond⁹Ω%20%2F%20Crown∞Ω-Certified-black" />

</div>


---

## 🗂️ Directory Layout

    docs/architecture/agents/
    ├── agent-architecture-upgrade-pack.md
    ├── langgraph/
    │   ├── overview.md
    │   ├── graph-patterns.md
    │   ├── dynamic-tool-calling.md
    │   └── governance-checkpoints.md
    ├── crewai/
    │   ├── mcp-integrations.md
    │   ├── interceptors.md
    │   └── agent-coordination.md
    └── kfm-integration/
        ├── agent-dag-blueprints/
        │   ├── hydrology.yaml
        │   ├── climatology.yaml
        │   ├── archives.yaml
        │   ├── treaties.yaml
        │   └── mixed-modal.yaml
        └── mcp-servers/
            ├── neo4j-mcp.md
            ├── gdal-mcp.md
            ├── stac-mcp.md
            ├── ocr-mcp.md
            └── nlp-mcp.md

---

## 🧩 Agent Upgrade Summary (2025 Releases)

### 🟦 LangGraph 1.0 (GA — Oct 22, 2025)

- Production-stable DAG architecture  
- Deterministic + agentic nodes  
- Durable state engine  
- Time-travel replay for debugging  
- Human-in-the-loop approval gates  
- OpenTelemetry span integration  
- Explicit sandboxed tool boundaries  

### 🟩 Dynamic Tool Calling (Aug 6, 2025)

- Per-node tool visibility  
- User-role and dataset-sensitivity tool constraints  
- FAIR+CARE tier-aware tooling  
- Condition-based execution routing  
- Error-safe, multi-agent orchestration  

### 🟨 CrewAI 1.4.x (Nov 7, 2025)

- Full KFM MCP server interface (Neo4j, GDAL, STAC, OCR)  
- Interceptor gateways for governance + provenance  
- Coordinated multi-agent flows  
- Retry/backoff mechanics  
- Telemetry events for Focus Mode dashboards  

---

## 🧱 How These Stack Together in KFM v10+

### 🔷 LangGraph = Execution Engine  
Runs all DAG workflows (ETL, KG updates, inference).  
Provides deterministic reproducibility and checkpoint durability.

### 🔷 Dynamic Tool Calling = Governance Firewall  
Controls allowed tooling per node based on:

- Dataset FAIR tier  
- User identity  
- Entity history  
- Temporal context  
- Sensitive-data restrictions  

### 🔷 CrewAI = MCP Gateway  
Connects LangGraph nodes to KFM MCP servers:

- `mcp://neo4j`  
- `mcp://stac`  
- `mcp://gdal`  
- `mcp://ocr`  
- `mcp://nlp`  

CrewAI enforces schema validation, provenance insertion, and lineage stamps.

---

## 🧬 Example KFM Agent DAG Blueprint (Hydrology ETL)

    nodes:
      ingest:
        type: deterministic
        tool: stac_read
      validate:
        type: deterministic
        tool: schema_validator
      raster_ops:
        type: deterministic
        tools: [gdal_warp, gdal_slope, gdal_hillshade]
      llm_assess:
        type: agentic
        allowed_tools: [hydro_classifier, metadata_writer]
      provenance_gate:
        type: approval
        approver: "FAIR+CARE Council"
      write_graph:
        type: deterministic
        allowed_tools: [neo4j_writer]

---

## 🔧 MCP Server Integration

### 🟦 GDAL MCP  
- Tools: warp, slope, hillshade, rasterInfo  
- Strict raster validation  
- GeoTIFF/COG support  
- Emits operation telemetry  

### 🟪 Neo4j MCP  
- Tools: cypher_read, cypher_write, batch_ingest  
- Dynamic Tool Calling prevents unsafe writes  

### 🟩 STAC MCP  
- Tools: search, readItem, getCollection  
- Required for all time-varying environmental datasets  

### 🟧 OCR MCP  
- Tools: ocr_read, text_regions  
- Linked to treaty archive workflows  

### 🟫 NLP MCP  
- Tools: summarize, classify_paragraphs, entity_linker  
- Critical for Story Node construction  

---

## 🔭 Observability & Telemetry

Mapped to KFM’s Focus Mode dashboards:

- `agent.node_start`  
- `agent.node_complete`  
- `agent.tool_call`  
- `agent.tool_denied`  
- `agent.state_checkpoint`  
- `agent.lineage_update`  

CrewAI interceptors append:

- DOI-like provenance hashes  
- FAIR+CARE compliance tags  
- Dataset sensitivity metadata  

---

## 🚀 System-Level Integration Diagram

    flowchart TD
        User --> FocusEngine
        FocusEngine --> LangGraph
        LangGraph -->|Dynamic Tool Selection| CrewAI
        CrewAI -->|MCP| Neo4j
        CrewAI -->|MCP| GDAL
        CrewAI -->|MCP| STAC
        CrewAI -->|MCP| OCR
        CrewAI -->|MCP| NLP
        LangGraph --> Telemetry
        Telemetry --> FocusModeDashboards

---

## 📘 KFM v10+ Incorporation Steps

### Step 1 — Migrate All Orchestration to LangGraph  
Convert ETL + inference + KG-writing pipelines to DAGs.  

### Step 2 — Activate Dynamic Tool Governance  
Apply dataset-sensitivity, FAIR tier, and user-role filters.  

### Step 3 — Register All MCP Servers with CrewAI  
Enable safe read/write access to Neo4j, STAC, GDAL, OCR, NLP.  

### Step 4 — Add Interceptors  
Inject provenance metadata + versioning + telemetry stamps.  

### Step 5 — Enable Observability  
Map agent events to OpenTelemetry + Focus Mode dashboards.  

---

## 🕒 Version History

| Version  | Date       | Notes                                                                 |
|----------|------------|-----------------------------------------------------------------------|
| v10.3.1  | 2025-11-13 | Updated to memory-rule compliance + added directory layout corrections |
| v10.3.0  | 2025-11-13 | Initial release of Agent Architecture Upgrade Pack                    |
