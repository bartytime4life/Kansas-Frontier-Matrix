---
title: "📨 KFM v11.2.3 — Messaging Pipelines Index (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed index and design standard for messaging pipelines in KFM, including SQS FIFO, SNS integrations, event bus routing, and reliability-aware message contracts."
path: "docs/pipelines/messaging/README.md"
version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Event Systems · FAIR+CARE Oversight"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"
status: "Active · Enforced"

commit_sha: ""
previous_version_hash: ""
doc_integrity_checksum: ""

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/eventbus-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/eventbus-v1.json"
governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipelines Index"
intent: "messaging-pipelines-index"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "Collection"
  cidoc: "E31 Document"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/pipelines-messaging-readme-v1.json"
shape_schema_ref: "../../../schemas/shacl/pipelines-messaging-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major messaging pipeline standard revision"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 📨 KFM v11.2.3 — Messaging Pipelines Index  
`docs/pipelines/messaging/README.md`

**Purpose:**  
Serve as the governed root index and design standard for all messaging pipelines in KFM (SQS, SNS, internal event buses, DLQs, retries), enforcing idempotent, provenance-rich, and FAIR+CARE-aligned message contracts.

[Status · Active / Enforced] · [Scope · Messaging Pipelines] · [Reliability · WAL-Aligned · Idempotent]

</div>

---

## 🧵 1. Overview

Messaging pipelines are the **nervous system** of KFM v11: they connect ETL jobs, event-driven updaters, auto-refresh loops, and downstream AI/graph updates.

This index:

- Defines the **directory layout** and required documents under `docs/pipelines/messaging/`.
- Registers **governed messaging patterns**, including SQS FIFO content-based deduplication.
- Specifies the **minimum contracts** for message shape, idempotency, telemetry, and governance.
- Links messaging behavior to **PROV-O**, **DCAT/STAC**, and KFM reliability standards.

All messaging pipelines must be:

- **Deterministic** — reproducible from the same inputs and configs.
- **Provenance-rich** — messages are traceable in the KFM lineage graph.
- **Reliability-aware** — behavior is aligned with WAL, retries, and error budgets.
- **FAIR+CARE-compliant** — especially when messages carry sensitive or sovereignty-constrained data.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/messaging/
│
├── 📄 README.md                               # This file (messaging index)
│
├── 🧵 sqs-fifo-dedup/                         # SQS FIFO content-based deduplication standard
│   └── 📄 README.md
│
├── 🛰️ sns-subscriptions/                      # SNS → SQS / Lambda / HTTP subscriptions & filters
│   └── 📄 README.md
│
├── 🧬 eventbus-routing/                       # Internal event bus routing patterns & contracts
│   └── 📄 README.md
│
├── 🧯 dlq-and-retry/                          # Dead-letter queues, retry, and replay semantics
│   └── 📄 README.md
│
└── 📊 telemetry-and-governance/              # Messaging telemetry, governance, and dashboards
    └── 📄 README.md
~~~

**Directory contract**

- Each subdirectory **MUST** contain:
  - A `README.md` following KFM-MDP v11.2.3.
  - Clear mapping to **pipeline modules**, **graph entities**, and **telemetry fields**.
- Additional subdirectories may be added, but:
  - Names must follow the emoji-prefix standard.
  - A top-level summary row must be registered in section **3. Messaging Pipelines in Scope**.

---

## 📚 3. Messaging Pipelines in Scope

This index tracks messaging standards that apply across KFM:

1. **🧵 `sqs-fifo-dedup/` — SQS FIFO Content-Based Deduplication Guidance**

   - Governs usage of **content-based deduplication** on SQS FIFO queues.
   - Enforces:
     - Canonical **JSON envelope** with `dedupe_key` and `event_id`.
     - Body-based uniqueness semantics (attributes are **not** part of the dedupe hash).
     - CI tests for hash behavior, attribute ignorance, and 5-minute window replay.
   - Path: `docs/pipelines/messaging/sqs-fifo-dedup/README.md`

2. **🛰️ `sns-subscriptions/` — SNS Subscription & Filtering Patterns**

   - Standards for:
     - SNS topics feeding SQS, Lambda, HTTP endpoints.
     - Subject/tags vs structured JSON message practices.
     - Mapping SNS message metadata into KFM provenance and telemetry.
   - Encodes how SNS fan-out events become **graph-safe** and **STAC/DCAT-aligned**.

3. **🧬 `eventbus-routing/` — Internal Event Bus Routing**

   - Defines internal event types, routing keys, and fan-out behavior.
   - Ensures:
     - Event schemas are versioned and documented.
     - Routing respects FAIR+CARE and data sensitivity.
     - Event types map cleanly to Neo4j entities and relationships.

4. **🧯 `dlq-and-retry/` — Dead-Letter and Retry Semantics**

   - Contracts for:
     - DLQ routes and quarantine handling.
     - Backoff strategies and replay procedures.
     - WAL alignment and deterministic re-processing.
   - Integrates with reliability runbooks and error-budget policies.

5. **📊 `telemetry-and-governance/` — Messaging Telemetry & Governance**

   - Defines:
     - Required OpenTelemetry spans and metrics for message flows.
     - Governance checks (policy violations, sensitivity flags).
     - Dashboards and alerts for dedupe collisions, DLQ volume, and replay behavior.

Each subdirectory MUST document:

- **Scope and responsibilities** in the messaging stack.
- **Message schemas and contracts** (JSON shape, required fields).
- **Failure modes and reliability requirements**.
- **Telemetry fields and governance rules**.

---

## 🧱 4. Design Principles for Messaging Pipelines

All messaging pipelines in KFM v11 must adhere to the following principles:

1. **Deterministic Message Shape**

   - Message bodies are fully specified JSON or binary envelopes.
   - No ad hoc “stringly-typed” messages without schema references.
   - Changes to message shape require:
     - Schema versioning.
     - Backward-compatibility notes.
     - CI validation.

2. **Idempotent Semantics**

   - Every message type has a documented **idempotency strategy**:
     - Dedupe keys (for SQS FIFO).
     - Idempotency tokens.
     - Upsert strategies in downstream systems.
   - WAL-backed replays MUST not introduce double-processing when contracts are followed.

3. **Provenance and Lineage**

   - Messages MUST carry:
     - `event_id` (global identifier for PROV-O).
     - Source references (dataset IDs, job IDs, upstream entities).
   - Message handling activities are modeled as PROV `Activity` nodes with:
     - `prov:used` input Entities.
     - `prov:generated` output Entities.
     - `prov:wasAssociatedWith` Agents (services, operators).

4. **Governed Access and Sensitivity**

   - Messaging pipelines cannot bypass:
     - Indigenous data governance.
     - Sensitivity labels or redaction rules.
   - If a message contains data about sensitive sites or communities:
     - Fields may need anonymization or generalization.
     - Access may be restricted at the API or subscription level.

5. **Observability and Testability**

   - All messaging behavior is:
     - Traceable via OpenTelemetry spans and metrics.
     - Covered by CI tests for schema validation, dedupe logic, and retry semantics.

---

## 🧾 5. Required Documentation per Messaging Pipeline

Each messaging pipeline under `docs/pipelines/messaging/` MUST provide at minimum:

1. **README.md**

   - KFM-MDP-compliant front-matter.
   - Overview, scope, and role within KFM.
   - Message schemas and key fields.
   - Reliability and governance sections.

2. **Message Contract(s)**

   - Canonical **JSON schemas** (or equivalent) referenced via:
     - `json_schema_ref`
     - `shape_schema_ref` (e.g., SHACL)
   - Idempotency and deduplication rules:
     - Dedupe key derivation.
     - Replay behavior.
     - DLQ / retry handling.

3. **Test Definitions**

   - CI-facing tests that:
     - Validate message shape.
     - Enforce dedupe and idempotency behavior.
     - Simulate common failure and replay scenarios.

4. **Telemetry Specification**

   - Required metrics and spans:
     - Names, types, units, and cardinality constraints.
   - Examples of critical metrics:
     - Throughput, latency, DLQ volume, error rate, dedupe collisions.

5. **Governance & FAIR+CARE Notes**

   - Any constraints on:
     - Who may publish or subscribe.
     - Which environments (dev/stage/prod) may carry real data.
   - Links to relevant governance standards and runbooks.

---

## 🔗 6. Integration with ETL, Graph, and Story Nodes

Messaging pipelines do not exist in isolation; they connect:

1. **ETL Pipelines**

   - Messages may trigger:
     - New ingests.
     - Incremental updates.
     - Derived product generation.
   - ETL jobs must be documented so that:
     - Their input messages are schema-valid.
     - Their outputs are STAC/DCAT/PROV-O aligned.

2. **Neo4j / Knowledge Graph**

   - Many messages correspond to:
     - Creation or update of graph nodes/relationships.
   - Message schemas must map cleanly to:
     - CIDOC-CRM classes (events, documents, actors).
     - GeoSPARQL features and geometries.
     - OWL-Time intervals.

3. **Story Nodes & Focus Mode**

   - Some messaging events will:
     - Trigger Story Node updates.
     - Influence Focus Mode narratives.
   - Messaging docs must clarify:
     - Which messages may create or update Story Nodes.
     - How provenance and confidence scores are recorded.

---

## ⚖️ 7. FAIR+CARE & Governance Requirements

Messaging pipelines must uphold:

1. **FAIR Principles**

   - **Findable:** Events and their schemas are registered and discoverable.  
   - **Accessible:** Access is controlled but consistently documented.  
   - **Interoperable:** Messages use open, documented formats and references.  
   - **Reusable:** Schemas, contracts, and telemetry standards enable reuse.

2. **CARE Principles**

   - Emphasize:
     - Collective benefit.
     - Authority to control.
     - Responsibility.
     - Ethics.
   - Messaging pipelines may be required to:
     - Obscure or generalize sensitive locations.
     - Apply stricter access controls for certain queues or topics.

3. **Governance Hooks**

   - Auditable configuration: queue names, retention, encryption.
   - Policy checks wired via:
     - Governance refs in front-matter.
     - Telemetry metrics for violations.

---

## 🕰️ 8. Versioning & Change Management

- Any new messaging standard or breaking change MUST:
  - Increment `version`.
  - Update `last_updated`.
  - Document changes in **Version History**.
- Major changes:
  - Require review by the Event Systems Working Group and FAIR+CARE oversight.
- Deprecations:
  - Must specify:
    - Sunset timeline.
    - Migration paths.
    - Impacted pipelines and schemas.

---

## 📘 9. Version History

| Version  | Date       | Notes                                                                                         |
|----------|------------|-----------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial governed messaging pipelines index; registered SQS FIFO dedup and core directory layout. |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

⬅ Back to Pipelines Index · ⬅ Back to KFM Documentation Root · 📜 Governance Charter

</div>