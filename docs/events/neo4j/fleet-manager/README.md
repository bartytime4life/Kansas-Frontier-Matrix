---
title: "🕸️ Kansas Frontier Matrix — Neo4j Fleet Manager Integration Overview"
path: "docs/events/neo4j/fleet-manager/README.md"
version: "v11.2.6"
last_updated: "2025-12-11"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Semiannual · Graph Systems Council"
content_stability: "stable"
status: "Active / Canonical"

doc_kind: "event-integration-overview"
intent: "neo4j-fleet-manager-architecture-integration"
semantic_document_id: "kfm-doc-events-neo4j-fleet-manager-overview-v11.2.6"

owner_team: "kfm-graph-systems"
contact: "graph-systems@kfm.example.org"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.6/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.6/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.6/graph-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/graph-systems-v11.json"

governance_ref: "../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"

markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🕸️ Neo4j Fleet Manager — **KFM Integration Overview**  
### Unified Graph Control Plane • Hybrid Ops • Observability • Governance Alignment

`docs/events/neo4j/fleet-manager/README.md`

</div>

---

## 1. Overview

Neo4j introduced **Fleet Manager** as a unified control plane for managing, monitoring, and governing **Neo4j clusters across cloud, hybrid, on‑premises, and local developer environments**.

Within the **Kansas Frontier Matrix (KFM)** pipeline:

Deterministic ETL  
→ STAC / DCAT / PROV catalogs  
→ Neo4j graph fleet  
→ API layer (REST / GraphQL)  
→ React / MapLibre / Cesium frontends  
→ Story Nodes and Focus Mode

Fleet Manager acts as the **graph control and observability layer** for the Neo4j segment of the pipeline, ensuring that:

- graph schemas remain **consistent and governed** across clusters  
- routing targets for **Story Nodes and Focus Mode** are **predictable and reproducible**  
- cluster lifecycle events are captured as **PROV and OpenTelemetry events**  
- FAIR+CARE requirements around **governed graph partitions** are enforceable in practice  

This document explains how Fleet Manager fits inside KFM’s graph architecture as of **v11.2.6**.

---

## 2. Why This Matters for KFM

### 2.1 Centralized Graph Governance

KFM’s knowledge graph spans many governed domains (historical, hydrology, archaeology, treaties, ecology, air quality, energy, and more). Fleet Manager enables:

- **Unified security & access policies** for all Neo4j clusters  
- **Configuration drift elimination** via centrally managed templates and policy checks  
- **Global lifecycle enforcement** (create, scale, patch, decommission) for graph instances  
- **Standardized upgrade pathways** aligned with KFM release trains  

In practice, this means the Graph Systems Council can assert policies **once**, and have them applied uniformly across:

- dev / test / staging clusters  
- production read/write graphs  
- domain‑specific or sovereignty‑scoped graphs  

### 2.2 Observability, Telemetry & Reliability

Fleet Manager emits cluster‑level and instance‑level signals, including:

- health metrics (availability, replica status, query failures)  
- performance metrics (latency, throughput, cache hit ratios)  
- topology & configuration states (cluster size, version, enabled plugins)  
- audit and event logs compatible with **KFM‑PDC v11** lineage models  

These are normalized into KFM’s **graph‑telemetry.json** streams and surface on the **Graph Reliability Board**, where they are correlated with:

- ETL run history  
- STAC/DCAT catalog updates  
- Focus Mode query patterns  
- sustainability and energy traces from telemetry schemas  

### 2.3 Hybrid Multi‑Cluster Requirements

KFM uses multiple graph “tiers”:

- **Local Graphs**  
  - developer sandbox graphs for schema exploration and local Story Node tests  
- **Cloud Graphs** (e.g., Neo4j Aura)  
  - high‑availability workloads, public‑facing API queries, Focus Mode aggregations  
- **Field Graphs**  
  - event ingestion, domain‑specific subgraphs, or air‑gapped environments  

Fleet Manager provides a **single orchestration and governance layer** across these environments, ensuring that:

- policies are **consistent**, even when clusters live in different networks  
- configuration changes are **audited** and **reversible**  
- cluster roles (dev / staging / prod / sovereign) are **explicit and machine‑readable**  

---

## 3. Integration Surfaces

### 3.1 ETL → Data Contract Enforcement

Through **KFM‑PDC v11**, each ETL job that writes to Neo4j includes a **graph contract** section specifying:

- target cluster / database identifiers (as known to Fleet Manager)  
- expected schema versions and indexes  
- allowed write patterns (labels, relationship types, property sets)  
- rollout strategy (blue/green, canary, or maintenance window)  

Fleet Manager participates as:

- a **policy gate**: schema policy and configuration checks must pass before ETL jobs promote data to production graphs  
- a **lineage anchor**: Fleet Manager run IDs and cluster state hashes are recorded as **PROV Activities and Entities**, allowing reconstruction of “what cluster looked like when ETL X ran”  

### 3.2 Neo4j Aura + Self‑Managed Support

KFM’s architecture mandates:

- reproducible developer graph bootstraps  
- deterministic, policy‑aware test sandboxes  
- governed production graphs with clear lifecycle states  

Fleet Manager tracks, per instance:

- Neo4j versions, plugins, and security configuration  
- user and role assignments (mapped to KFM identity & governance models)  
- scheduled maintenance windows and upgrade plans  

This allows KFM’s CI/CD system to validate that:

- **test environments** mirror production where required  
- **sovereign graph environments** adhere to stricter access constraints  
- **upgrades** are rolled out in a **controlled, reversible** manner  

### 3.3 Story Node & Focus Mode Integration

Story Nodes and Focus Mode rely on:

- **persistent graph embeddings** and indexing  
- **valid, fresh relationships** between entities  
- predictable **graph latency and availability**  

Fleet Manager’s health and readiness metrics are ingested into:

- **Focus Mode routing logic**  
  - if a cluster is degraded or undergoing maintenance, Focus Mode can:  
    - degrade gracefully (simpler queries, limited depth)  
    - re‑route to replicas or lag‑tolerant views  
- **Story Node preflight checks**  
  - Story Node engines can validate that required clusters are healthy before generating narratives  

---

## 4. Directory Layout (KFM v11.2.6)

Emoji‑enriched, CI‑safe layout for this event integration module (aligned with `fencing_profile: outer-backticks-inner-tildes-v1`):

~~~text
📂 docs/events/neo4j/fleet-manager/
├── 📝 README.md                  # This document – integration overview & governance context
├── 📜 integration-architecture.md # Detailed architecture diagrams & sequence flows
├── 🧪 test-matrix.md             # Graph reliability + Fleet Manager compatibility test plan
└── 📈 telemetry/                 # Normalized Fleet Manager → KFM telemetry specs & examples
    ├── 📄 fleet-manager-events.schema.json   # JSON Schema for incoming Fleet Manager events
    └── 📄 graph-health-metrics.schema.json   # JSON Schema for graph health & SLO telemetry
~~~

Conventions:

- All additional files under this directory MUST be documented here when added or removed.  
- Any **event schema** that feeds into KFM telemetry MUST live under `telemetry/` and be referenced from this README and from central schema indexes.  
- Changes to this layout require a **governed change request** and CI updates (graph telemetry and documentation checks).

---

## 5. KFM Pipeline Alignment

### 5.1 Deterministic ETL

Fleet Manager does **not** replace ETL but constrains and observes the **graph portion** of the standard pipeline:

Deterministic ETL (configs in `configs/*`)  
→ STAC / DCAT / PROV catalogs (`data/stac`, `data/dcat`, `data/prov`)  
→ Neo4j graph fleet (managed by Fleet Manager)  
→ API layer (`src/api`)  
→ React / MapLibre / Cesium frontends (`src/web`)  
→ Story Nodes / Focus Mode (`docs/story`, Focus engines)

Fleet Manager ensures that across ingestion, processing, and production clusters:

- **schema and index definitions** are consistent for a given graph contract  
- **cluster roles and labels** match their intended function (dev / staging / prod / sovereign)  
- **upgrades and reconfigurations** are orchestrated in alignment with KFM release cycles  

### 5.2 STAC/DCAT → Graph Mapping

Fleet Manager does **not** alter mapping logic from STAC/DCAT to graph entities. That logic remains in:

- `src/pipelines/*` for ETL  
- `src/graph/*` for graph ingestion

Instead, Fleet Manager guarantees that:

- schema endpoints (e.g., labels and relationship types expected by STAC/DCAT mappings) are **present and versioned**  
- ingestion targets (clusters / databases) are **reachable** and in the correct lifecycle state  
- constraints (e.g., uniqueness, existence) are **enforced consistently** so that mapped entities are stable across environments  

### 5.3 Neo4j Cluster Lifecycle

Fleet Manager adds for KFM:

- predictable **upgrade windows** tied to KFM releases (e.g., v11.2.6 → v11.2.7)  
- provenance‑aware **cluster migrations**, where cluster moves or splits are recorded via PROV and telemetry  
- **rolling updates** that do not break ETL, API, or Story Node workloads (with preflight checks in CI)  

### 5.4 API (FastAPI/GraphQL) & UI (MapLibre/Cesium)

Fleet Manager reduces:

- unplanned downtime for graph APIs  
- inconsistent read patterns due to misaligned cluster configurations  
- sudden role or permission mismatches between environments  

API gateways and UI services use Fleet Manager‑backed **service discovery** and **health signals** to:

- pick the correct graph cluster for each request type  
- decide when to shed load or present degraded views instead of hard errors  

---

## 6. FAIR+CARE, Governance & Sovereignty

Fleet Manager supports KFM governance by enabling:

- **consistent audit trails** of who changed what, where, and when at the cluster level  
- **fine‑grained role enforcement** mapped to KFM’s unified permission graph (e.g., domain‑specific or sovereignty‑specific roles)  
- **cluster‑level access provenance**, so queries from sensitive domains (e.g., land treaties, burial sites, oral histories) can be traced back to specific graph instances  
- governed **graph snapshot lifecycles**, including retention, archival, and deletion rules  

Specific to sovereignty and sensitive domains:

- Some datasets must live only on **sovereign clusters** with restricted network exposure.  
- Fleet Manager enforces that **replication targets** for such clusters are governed and documented, or disabled entirely.  
- Any attempt to duplicate or migrate these clusters must pass **governance checks** and may require manual approval from data stewards or sovereignty councils.  

---

## 7. Risks & Considerations

| Category            | Notes                                                                                  |
|---------------------|----------------------------------------------------------------------------------------|
| **Config Drift**    | Largely eliminated, but only if Fleet Manager is treated as the *single* source of truth for cluster config and schema policy. |
| **Security**        | Role and permission models must be mapped into KFM’s unified permission graph; misalignment can create gaps or over‑privilege. |
| **Upgrade Windows** | Must be aligned with KFM‑GOV release cycles and communicated to ETL/API/UI owners, Story Node authors, and domain stewards. |
| **Cost**            | Aura‑based control planes may incur higher costs; mitigation via mixed tiers and right‑sized instances is required.            |
| **Telemetry Flood** | Fleet Manager telemetry can be high‑volume; must be down‑sampled and normalized into KFM’s telemetry schema.                 |

All of these considerations should be tracked in **risk registers** and reviewed during Graph Systems Council meetings.

---

## 8. Next Steps for KFM v11.2.7

For the v11.2.7 cycle, recommended follow‑ups:

1. Define and publish a **graph‑health baseline spec** (SLOs for latency, availability, error budgets) under `docs/standards/graph/`.  
2. Integrate Fleet Manager events into the **KFM OpenTelemetry stream**, via `graph-systems-v11.json`.  
3. Add Fleet Manager lifecycle hooks to **all Neo4j‑targeting ETL charts** (Helm/kustomize or equivalent), including preflight schema checks.  
4. Stand up **graph‑perf regression dashboards** (e.g., time‑series of query latency by cluster / domain).  
5. Expand **Story Node resilience rules** so narrative engines can:  
   - detect degraded graph clusters  
   - choose fallback strategies (alternate clusters, reduced depth, cached summaries)  

Each of these tasks should correspond to a tracked issue or change request, referencing this document.

---

## 9. Version History

| Version   | Date       | Author          | Notes                                                                 |
|-----------|------------|-----------------|-----------------------------------------------------------------------|
| v11.2.6   | 2025-12-11 | `<your-name>`   | Initial Fleet Manager integration overview aligned with KFM‑MDP 11.2.6. |

Update this table whenever structural, telemetry, or governance‑significant changes are made, and ensure associated SBOM, manifest, and telemetry references remain accurate.

---

## ⚖️ Footer

<div align="center">

**📚 Governance Links**  
[Docs Root](../../../README.md) •  
[Standards Index](../../../standards/INDEX.md) •  
[Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

**🔐 Compliance:**  
FAIR+CARE · STAC/DCAT · PROV-O · Neo4j Fleet Manager · KFM‑PDC v11 · OpenTelemetry · SPDX 2.3 · SLSA Level 3

**♻️ Sustainability:**  
Energy & Carbon Telemetry Enabled (ISO 50001 / ISO 14064)

**End of Document**

</div>