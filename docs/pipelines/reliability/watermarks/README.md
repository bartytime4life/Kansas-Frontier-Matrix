---
title: "💧 KFM v11 — Event-Time Watermarks & Deterministic Stream Windows (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Reliability standard for event-time watermarks and deterministic window semantics across all KFM streaming pipelines."
path: "docs/pipelines/reliability/watermarks/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability Engineering · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x reliability-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../releases/v11.2.3/reliability-telemetry.json"
telemetry_schema: "../../../schemas/telemetry/eventtime-watermarks-v1.json"

governance_ref: "../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Reliability Standard"
header_profile: "standard"
footer_profile: "standard"

intent: "watermarks"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "streaming"
    - "event-time-aggregation"
    - "replay"
    - "upsert-sinks"

semantic_intent:
  - "reliability"
  - "determinism"
  - "governance"
category: "Pipelines · Reliability · Event-Time"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability Engineering Council"
ttl_policy: "Indefinite (subject to updates in newer versions)"
sunset_policy: "Supersede when v12 reliability standards are adopted"

ontology_alignment:
  cidoc: "E29 Design or Procedure"
  schema_org: "TechArticle"
  prov_o: "prov:Plan"
  owl_time: "ProperInterval"

metadata_profiles:
  - "PROV-O"
  - "FAIR+CARE"

provenance_chain:
  - "docs/pipelines/reliability/README.md"
  - "docs/pipelines/reliability/watermarks/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-reliability-watermarks-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-reliability-watermarks-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:reliability:watermarks:v11.2.3"
semantic_document_id: "kfm-pipelines-reliability-watermarks-v11.2.3"
event_source_id: "ledger:kfm:doc:pipelines:reliability:watermarks:v11.2.3"

ai_training_inclusion: false
ai_focusmode_usage: "Allowed with restrictions"
ai_transform_permissions:
  - "summary"
  - "timeline-generation"
  - "semantic-highlighting"
  - "metadata-extraction"
ai_transform_prohibited:
  - "content-alteration"
  - "speculative-additions"
  - "governance-override"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"

test_profiles:
  - "markdown-lint"
  - "schema-lint"
  - "metadata-check"
  - "provenance-check"
  - "footer-check"
---

<div align="center">

# 💧 KFM v11 — Event-Time Watermarks & Deterministic Stream Windows  

`docs/pipelines/reliability/watermarks/README.md`

**Purpose:**  
Define the **event-time watermark and windowing standard** that guarantees **deterministic, idempotent, and replay-stable** streaming behavior across all KFM pipelines, including ingestion adapters, replay systems, window operators, and downstream upsert sinks.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md) ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)](../../standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../releases/v11.2.3/manifest.zip)

</div>

---

## 💧 1. Overview

Event-time watermarks ensure **deterministic**, **idempotent**, and **replay-stable** aggregation for all KFM streaming pipelines.

This standard governs:

- Ingestion adapters and event-time extraction.  
- Replay systems and deterministic reconstruction.  
- Lineage behaviors and provenance spans.  
- Window operators and close conditions.  
- Downstream upsert logic (SQL, object stores, graph upserts).

KFM v11 uses **event-time semantics exclusively** for correctness — **processing time is never used as a correctness signal**.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/reliability/watermarks/
│
├── 📄 README.md                               # This file
│
├── 📘 policy/                                 # Watermark & lateness definitions
│   ├── 📄 watermark-policy.md                 # Monotonic watermark contract
│   ├── 📄 allowed-lateness.md                 # Allowed-lateness table by domain
│   └── 📄 windowing-modes.md                  # Tumbling, sliding, session windows
│
├── 🧮 operators/                              # Implementation logic
│   ├── 📄 assign-timestamps.md                # Event-time extraction rules
│   ├── 📄 compute-watermark.md                # Max event-time → watermark logic
│   ├── 📄 close-windows.md                    # Conditions for deterministic closure
│   └── 📄 late-pane-handling.md               # Late-pane emission logic
│
├── 🧪 tests/                                  # Deterministic replay tests
│   ├── 📄 replay-determinism.md
│   ├── 📄 monotonic-watermark-tests.md
│   └── 📄 lateness-behavior-tests.md
│
└── 🧩 examples/                               # Reference patterns
    ├── 📄 flink-pattern.md
    ├── 📄 beam-pattern.md
    └── 📄 sql-upsert-pattern.md
~~~

All child documents must:

- Conform to **KFM-MDP v11.2.2**.  
- Reference this standard as the normative source for event-time behavior.

---

## 🧭 3. Watermark Philosophy in KFM v11

KFM’s event-time strategy is built on the following constraints:

- **Monotonicity**  
  Watermarks MUST never move backwards for a given source or partition.

- **Determinism**  
  Replaying historical data with the same input order MUST produce:
  - Identical watermarks.  
  - Identical window boundaries and pane counts.  
  - Identical sink rows.

- **Domain-Aware Lateness**  
  Each dataset defines a strict, documented **allowed-lateness budget** (see `policy/allowed-lateness.md`).

- **Idempotent Sinks**  
  All windows MUST be written with stable `{window_start, window_end, key}` upsert keys (plus `pane` when enabled).

- **Auditable Lineage**  
  Every significant watermark advancement SHOULD generate a **provenance span** and telemetry record, enabling reconstruction and audit.

---

## ⚙️ 4. Minimal Algorithm (Framework-Agnostic)

The canonical event-time watermark algorithm (for a single logical source) is:

~~~text
1. Extract e.event_time (RFC3339)
2. Maintain observed_event_time_max[source]
3. candidate = observed_event_time_max[source] - allowed_lateness[source]
4. watermark[source] = max(previous_watermark, candidate)
5. For each open window:
       if window.end <= watermark[source]:
           close window deterministically
6. Emit on-time and late panes with stable keys
~~~

Properties:

- Works across Flink, Beam, Rust, Python, or SQL-based streaming backends.  
- Allows domain-specific `allowed_lateness[source]` while preserving determinism.  
- Requires event ordering to be stable per source/partition (or partition-specific watermark streams).

This algorithm is enforced across all ingestion pipelines and compute runtimes as the **minimum acceptable behavior**.

---

## 🧱 5. On-Time vs Late-Pane Behavior

KFM defines three categories of events relative to watermarks:

### 5.1 On-Time

- Condition: `window_end <= watermark`.  
- Behavior:
  - Emit a **primary pane** (`pane = 0`).  
  - Close window or mark as “on-time closed”, depending on configuration.

### 5.2 Allowed-Late

- Condition:
  - `event_time < watermark`, and  
  - Event still within `allowed_lateness`.  
- Behavior:
  - Emit an **incremental late pane** (`pane > 0`).  
  - Upsert or merge into existing window aggregates using deterministic keys.

### 5.3 Too-Late (Rejected)

- Condition:
  - Event-time is beyond `allowed_lateness`.  
- Behavior:
  - Event is not applied to the window.  
  - Counted in telemetry as `telemetry.events.late_dropped`.  
  - May be logged as diagnostic or “dead letter” for investigation.

---

## 🧑‍🔧 6. Deterministic SQL Sink Contract

All relational sinks that store watermarked windows MUST follow this primary key contract:

- **Primary Key:**

  `PRIMARY KEY (key, window_start, window_end, pane)`

- **Minimum Columns:**
  - `key`  
  - `window_start`  
  - `window_end`  
  - `value` (aggregate or payload)  
  - `pane` — `0` for on-time, `>0` for late panes  
  - `watermark_emitted_at` — wall-clock time when pane was emitted  
  - `replay_id` — identifier for replay run or load batch

Requirements:

- Sink writes MUST be **idempotent** and **replay-safe**.  
- Replaying the same input MUST converge to the same set of rows and values.  
- Additional audit columns (e.g., `decision_trace`) MAY be added but MUST NOT change semantics.

`examples/sql-upsert-pattern.md` provides concrete SQL examples for major engines.

---

## 📡 7. Telemetry Requirements

Operators MUST emit at least the following metrics:

- `watermark.value_ms` — current watermark in milliseconds since epoch.  
- `watermark.lag_ms` — difference between now and watermark (or domain-specific reference).  
- `events.late` — count of events arriving after watermark (allowed + rejected).  
- `late_panes.count` — number of late panes emitted.  
- `window.close_latency_ms` — latency between `window_end` and actual close time.

OpenTelemetry spans:

- `watermark.advance` — whenever a watermark moves forward.  
- `window.close` — when a window is closed (on-time or late).  
- `late-pane.emit` — when a late pane is emitted.

These metrics MUST conform to `eventtime-watermarks-v1` telemetry schema and be consumable by:

- Reliability dashboards.  
- Alerting systems (e.g., excessive lateness or lag).  
- Replay validation tooling.

---

## 🔁 8. Replay Requirements

Replay mode MUST reconstruct watermarks **exclusively from event order and timestamps**, never from real time or wall-clock-based operators.

A compliant replay MUST produce bit-identical:

- Watermark sequences.  
- Closed windows (boundaries and counts).  
- Pane counts and order.  
- Sink rows (ignoring allowed non-deterministic fields like log timestamps, if any).

Replay validation:

- Implemented via **Deterministic Replay Test Suite** (`tests/replay-determinism.md`).  
- CI/CD MUST include:
  - Forward run → snapshot.  
  - Replay run → snapshot.  
  - Comparison of:
    - Watermark traces.  
    - Window outputs.  
    - Sink tables.

Any discrepancy MUST fail the test suite.

---

## 🧩 9. Framework Reference Patterns

Detailed patterns are provided in:

- `examples/flink-pattern.md` — Flink operators, watermarks, windows, sinks.  
- `examples/beam-pattern.md` — Beam `WithTimestamps`, `Watermark`, and windowing patterns.  
- `examples/sql-upsert-pattern.md` — SQL sink design for idempotent upserts with panes.

Each pattern includes:

- Operator graphs.  
- Upsert keys and table schemas.  
- Telemetry hooks and recommended metric names.  
- Replay and test harness guidance.

---

## ✅ 10. Compliance Checklist

To be considered compliant with this standard, a pipeline MUST satisfy:

- Event-time semantics used **exclusively** for correctness.  
- Watermarks are **monotonic** (no backward movement).  
- Allowed-lateness is **documented** and enforced.  
- Late panes are **enabled** where domain requires incremental updates.  
- Sinks use **deterministic keys** `{key, window_start, window_end, pane}`.  
- Replay produces **identical results** for watermarks and sink data.  
- Telemetry is emitted for every watermark advancement and window close.  
- Provenance spans are **linked to `replay_id`** or equivalent identifiers.

This checklist SHOULD be integrated into:

- Pipeline design reviews.  
- CI policy checks.  
- Reliability audits.

---

## 🏛️ 11. Governance & FAIR+CARE Controls

- Watermark policies are governed by the **Reliability Engineering Council**.  
- Lateness budgets MUST be justified and tied to:
  - Data provenance guarantees.  
  - Ethical and regulatory constraints (FAIR+CARE).  
- All implementations undergo **quarterly review**, including:
  - Monotonicity tests.  
  - Replay determinism tests.  
  - Telemetry coverage audits.

Where streams involve:

- **Sensitive data**, or  
- **Indigenous or community-controlled datasets**  

lateness budgets and retention policies MUST align with:

- `sovereignty_policy`.  
- CARE principles (e.g., limiting retention of personally identifying event sequences).

---

## 🗃️ 12. Version History

| Version  | Date       | Notes                                             |
|----------|------------|---------------------------------------------------|
| v11.2.3  | 2025-12-02 | Initial KFM v11 rebuild; directory-aligned; telemetry schema v1 integrated. |
| v11.2.2  | 2025-11-28 | Added telemetry schema and metric definitions.    |
| v11.2.1  | 2025-11-20 | Added monotonicity tests and replay suite hooks.  |

---

<div align="center">

💧 **KFM v11 — Event-Time Watermarks & Deterministic Stream Windows**  
Deterministic Streams · Replay-Safe Windows · FAIR+CARE-Governed Reliability  

[📘 Pipelines Index](../README.md) · [🛡 Reliability Framework](../README.md) · [⚖ Governance](../../standards/governance/ROOT-GOVERNANCE.md)

</div>