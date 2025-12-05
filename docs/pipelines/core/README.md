---
title: "⚙️ KFM v11.2.4 — Core Pipeline Architecture Index"
path: "docs/pipelines/core/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Systems & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x protocol-safe"
status: "Active / Enforced"

doc_kind: "Architecture Index"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "pipelines/core"
  applies_to:
    - "etl"
    - "queues"
    - "backfill"
    - "replay"
    - "telemetry"
    - "provenance"
    - "story-nodes"
    - "focus-mode"
    - "energy"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../releases/v11.2.4/pipelines-core-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/pipelines-core-standards-v1.json"
governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:pipelines:core:index:v11.2.4"
semantic_document_id: "kfm-pipelines-core-index-v11.2.4"
event_source_id: "ledger:kfm:doc:pipelines:core:index:v11.2.4"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# ⚙️ KFM v11.2.4 — Core Pipeline Architecture Index  
`docs/pipelines/core/README.md`

**Purpose:**  
Serve as the canonical index for **core KFM pipeline architecture** — queue patterns, deterministic DAG rules, backfill and replay behavior, telemetry and provenance integration — so all domain pipelines (soil, hydrology, atmospheric, archaeology AI, catalog generation, etc.) share the same governed execution substrate.

</div>

---

## 🗂️ Directory Layout

```text
📂 docs/pipelines/
└── 📂 core/
    ├── 📄 README.md                        # ⚙️ Core Pipeline Architecture Index (this file)
    ├── 📂 queue-architecture/              # 🔁 Queue-centric pipeline architecture standard
    │   └── 📄 README.md                    # 🔁 Queue-Centric Pipeline Architecture
    ├── 📂 patterns/                        # 🧩 Reusable pipeline patterns & building blocks
    │   ├── 📄 retries-and-dlq.md           # Retry, DLQ, and replay patterns
    │   ├── 📄 backfill-watermarks.md       # Backfill & event-time watermark strategies
    │   └── 📄 idempotent-upserts.md        # Idempotent write patterns and keys
    ├── 📂 observability/                   # 📡 Telemetry & SLO patterns for pipelines
    │   ├── 📄 otel-attributes.md           # Required OpenTelemetry attributes for nodes/queues
    │   └── 📄 slo-profiles.md              # Standard SLO profiles for core pipelines
    └── 📂 runbooks/                        # 📒 Operational runbooks for core behaviors
        ├── 📄 backlog-investigation.md     # Backlog and queue health investigation steps
        ├── 📄 replay-procedures.md         # Safe replay/WAL procedures
        └── 📄 incident-triage.md           # Initial triage for pipeline incidents
```

Author rules:

- Any new **core pipeline standard** must be added under `docs/pipelines/core/` with a `README.md` and a clear emoji in this tree.  
- Domain-specific pipeline docs (e.g., soil, hydrology) must link back to this index and to the **queue-architecture** standard if they rely on queues.

---

## 📘 Overview

Core pipeline architecture standards define **how KFM pipelines run**, independent of domain:

- Queue semantics (ordering, dedupe, backpressure).  
- Deterministic DAG node behavior and idempotent handlers.  
- Backfill, event-time watermarks, and replay procedures.  
- Telemetry (OpenTelemetry traces/metrics/logs) and SLOs.  
- Provenance modeling (PROV-O), plus STAC/DCAT alignment for produced datasets.  
- Energy and carbon telemetry integration via KFM energy standards.

This index:

- Provides a **map** of core pipeline-related docs.  
- Clarifies how core standards relate to domain pipelines in `docs/pipelines/*`.  
- Establishes **minimum expectations** that all new pipelines must satisfy before they are considered production-ready.

If a pipeline ingests data and produces outputs consumed by the graph, STAC/DCAT catalogs, or Story Nodes/Focus Mode, it is expected to adhere to these core patterns.

---

## 🧭 Context

In KFM’s end-to-end system:

> Source Systems → **Core Pipeline Architecture (queues, DAGs, backfill)** → STAC/DCAT/PROV → Neo4j → API → Frontend → Story Nodes & Focus Mode

Core pipeline standards:

- Sit **between** external data sources and internal catalogs/graph.  
- Provide **shared guarantees** (determinism, idempotency, observability, replayability) to domain pipelines.  
- Enable **consistent operational behavior** across all ingest and processing flows, regardless of domain.  

This index is upstream of:

- `docs/pipelines/soil/gnatsgo-auto-ingest/README.md`  
- Other domain pipelines (e.g., hydrology, atmospheric, archaeology AI) that must declare how they instantiate or extend these core patterns.

---

## 🧱 Architecture

Core pipeline architecture is built around the **queue-centric model**:

- **Queue-Centric Pipeline Architecture** (`queue-architecture/README.md`) defines:
  - Deterministic DAG node contract (`input_message + config(seed) → output_message`).  
  - Idempotent handlers (idempotency keys, WAL-before-mutation, safe retries).  
  - Queue ordering rules (message groups) and dedupe strategy.  
  - Failure and replay behavior (DLQ, WAL replay, PROV linkage).  
  - Backfill and event-time watermarks.

This index mandates that:

- New pipelines **MUST** declare whether they follow the queue-centric spec directly or via a thin wrapper.  
- Any divergence (e.g., batch-only ETL without queues) must still:
  - Provide deterministic behavior.  
  - Support replay via WAL or equivalent.  
  - Emit telemetry consistent with `queue-architecture-v1.json` where applicable.  

Core architectural expectations:

- **Config-driven** pipelines (no hard-coded environment details).  
- **Versioned transforms** (code + config) recorded in provenance.  
- **Clear ownership** of queues and handlers (documented in runbooks).  
- **Explicit backfill modes** that do not interfere with live flows.

More detailed diagrams and flow descriptions are maintained under `queue-architecture/` and `diagrams/`.

---

## 📦 Data & Metadata

Core pipeline standards define **common metadata** for all queue-based or ETL flows:

- **Message-level metadata**:
  - `message_id`, `message_group`, `idempotency_key`, `attempt_count`, `event_time`.  
- **Handler-level metadata**:
  - `handler_name`, `handler_version`, `pipeline_version`, `config_hash`.  
- **Queue-level metadata**:
  - Queue names, capacity, and associated SLOs/SLA expectations.

These fields must be:

- Present in OpenTelemetry spans and logs (see `observability/otel-attributes.md`).  
- Available for provenance exports (PROV-O).  
- Stable enough to serve as keys in Neo4j or catalog foreign members when necessary.

Core standards also link to:

- **Telemetry schemas** under `schemas/telemetry/queue-architecture-v1.json` and related documents.  
- **Energy and carbon** telemetry schemas for per-node energy accounting (via energy standards).

---

## 🌐 STAC, DCAT & PROV Alignment

Core pipelines are **not tied to a single dataset** but must be modelable in KFM’s metadata and provenance stack:

- **PROV-O**
  - Each handler invocation is a `prov:Activity`.  
  - Input/output messages are `prov:Entity` instances.  
  - Pipelines and services are `prov:Agent` instances.  
  - Replays and backfills are captured as distinct `prov:Activity` with clear relations (`prov:wasDerivedFrom`).

- **STAC/DCAT**
  - When pipelines produce or update datasets:
    - STAC Collections/Items and DCAT Datasets must reference the pipeline and activity IDs that created them.  
    - Core pipeline architecture provides the pattern, while domain docs specify dataset-specific metadata.

This index ensures that **any pipeline following core patterns** can be expressed in:

- System-level provenance graphs.  
- Catalog records tied to specific data products.  

---

## 🧪 Validation & CI/CD

All pipelines built on core architecture must:

- Pass **core CI checks**, which may include (but are not limited to):
  - Determinism tests (re-run subset of messages, compare outputs).  
  - Idempotency tests (replay with same idempotency keys, ensure no double side effects).  
  - Queue and DLQ behavior (inject failures, validate replay behavior).  
  - Telemetry schema validation (`queue-architecture-v1.json`).  

- Integrate with **OpenTelemetry** using attributes defined under `observability/otel-attributes.md`.  

- Define and test **SLOs**:
  - Latency, error rate, backlog size, and age.  
  - SLO burn analysis patterns described under `observability/slo-profiles.md` and `runbooks/slo-burn-analysis.md`.

Core CI/CD pipeline templates should live under:

- `.github/workflows/kfm-ci-pipelines.yml` (or similarly named workflow) and be reusable by domain pipelines.

Any new core standard or pattern added under this index must include:

- A section describing required tests.  
- Example CI snippets or a reference to a shared workflow template.

---

## ⚖ FAIR+CARE & Governance

Core pipeline architecture is primarily **technical**, but it underpins all data flows, including sensitive ones:

- FAIR:
  - *Findable*: pipeline metadata and provenance are discoverable in system catalogs and graphs.  
  - *Accessible*: logs, traces, and metrics for core pipelines are available to maintainers under governance constraints.  
  - *Interoperable*: pipelines are modeled using standard metadata and provenance ontologies.  
  - *Reusable*: patterns and templates can be reused across domains and projects.

- CARE & sovereignty:
  - Core architecture must not undermine **geoethical** or **sovereignty** constraints:
    - Pipelines handling sensitive datasets are expected to integrate with geoprivacy and geoethics standards.  
    - Backfill and replay must not inadvertently expose sensitive data to broader audiences.  
  - Governance bodies (Systems & Reliability Council, FAIR+CARE Council) review:
    - New core patterns.  
    - Changes to queue behavior that might impact how data flows through the system.

Any deviation from core patterns when handling **culturally sensitive** data must:

- Be explicitly documented.  
- Include a risk assessment.  
- Receive FAIR+CARE and sovereignty review.

---

## 🕰️ Version History

| Version | Date       | Status            | Notes                                                               |
|--------:|------------|-------------------|---------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active · Enforced | Initial KFM-MDP v11.2.4–aligned Core Pipeline Architecture Index.   |

Future revisions must:

- Add links to new core pipeline standards and patterns.  
- Update references to telemetry and provenance schemas when they evolve.  
- Keep directory layout and examples consistent with actual repo structure.

---

<div align="center">

⚙️ **KFM v11.2.4 — Core Pipeline Architecture Index**  
Deterministic Pipelines · Queue-Centric Patterns · Observable & Governed  

[📘 Docs Root](../../..) · [⚙ Pipelines Index](../README.md) · [🔁 Queue Architecture Standard](./queue-architecture/README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>