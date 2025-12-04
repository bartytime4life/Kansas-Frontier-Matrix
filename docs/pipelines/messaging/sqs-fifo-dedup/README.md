---
title: "🧵 KFM v11.2.3 — SQS FIFO Content-Based Deduplication Guidance (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed guidance for using Amazon SQS FIFO content-based deduplication safely in KFM pipelines by encoding uniqueness and provenance into the message body."
path: "docs/pipelines/messaging/sqs-fifo-dedup/README.md"
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

doc_kind: "Pipeline Guidance"
intent: "sqs-fifo-dedup-guidance"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Low"
redaction_required: false

ontology_alignment:
  schema_org: "TechArticle"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../../schemas/json/pipelines-messaging-sqs-fifo-dedup-readme-v1.json"
shape_schema_ref: "../../../schemas/shacl/pipelines-messaging-sqs-fifo-dedup-readme-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major SQS FIFO deduplication standard revision"

header_profile: "standard"
footer_profile: "standard"
---

<div align="center">

# 🧵 **KFM v11.2.3 — SQS FIFO Content-Based Deduplication Guidance**  
`docs/pipelines/messaging/sqs-fifo-dedup/README.md`

**Purpose:**  
Define the governed, deterministic contract for using Amazon SQS FIFO **content-based deduplication** in KFM pipelines, so that message uniqueness is encoded safely into the **body** and not lost in attributes.

[Status · Active / Enforced] · [Scope · Messaging Pipelines] · [Reliability · Idempotent · WAL-Aligned]

</div>

---

## 🧵 1. Overview

Amazon SQS FIFO queues guarantee ordered, deduplicated delivery, but only when the producer uses the correct deduplication strategy.  

**Critical fact:** with content-based deduplication enabled, SQS hashes **only the message body**, never the attributes. Attribute-only uniqueness keys are therefore unsafe for reliable ingestion.

KFM enforces deterministic, provenance-aligned message encoding patterns to ensure true idempotence and effectively-once semantics over a WAL-backed pipeline.

---

## 🗂️ 2. Directory Layout (Emoji-Rich · Compliant)

    docs/pipelines/messaging/sqs-fifo-dedup/
    │
    ├── 📄 README.md                          # This file
    │
    ├── 📘 contracts/                         # Message-shape & idempotency rules
    │   ├── 📄 body-deduplication-contract.md
    │   ├── 📄 attribute-safety-notes.md
    │   └── 📄 producer-requirements.md
    │
    ├── 🧪 tests/                             # Deterministic dedupe validation tests
    │   ├── 📄 hash-behavior-test.md
    │   └── 📄 duplicate-window-test.md
    │
    └── 📊 telemetry/                         # Operational traces
        ├── 📄 dedup-metrics.md
        └── 📄 message-provenance-events.md

**Directory contract:**

- `contracts/` captures the canonical body envelope and producer obligations.  
- `tests/` defines CI-facing test cases every SQS FIFO producer must pass.  
- `telemetry/` documents metrics and event formats for observing dedup behavior.

---

## 🧠 3. Key Rule: Content-Based Deduplication Uses Only the Body

When content-based deduplication is enabled on an SQS FIFO queue:

- SQS computes an internal hash (SHA-256-like) **over the message body only**.  
- Message attributes are ignored for deduplication.  
- If uniqueness depends on an attribute (for example, a site ID, dataset UUID, or event timestamp), SQS will treat otherwise-identical bodies as the same message.

**KFM requirement**

Uniqueness keys **MUST** be included in the serialized body, not stored solely as attributes.

Attributes may still be used for routing hints or filtering, but they cannot be the only carrier of uniqueness semantics.

---

## 📌 4. KFM Message Body Contract (Mandatory)

Every SQS FIFO producer in KFM **MUST** embed a canonical JSON envelope in the body:

    {
      "event_id": "<uuid-v7>",
      "event_source": "kfm.<domain>.<pipeline>",
      "event_time": "<RFC3339>",
      "dedupe_key": "<canonical-string>",
      "payload": {}
    }

**Rules**

- `dedupe_key`  
  - MUST uniquely identify the event within the 5-minute SQS dedupe window.  
  - Represents the logical “idempotency key” for the event.

- `event_id`  
  - Provides global provenance for KFM (UUID v7 recommended).  
  - Not used by SQS for dedupe, but required for PROV-O, WAL correlation, and debugging.

- `event_source`  
  - Uses `kfm.<domain>.<pipeline>` (for example, `kfm.remote-sensing.landsat-refresh`).

- `event_time`  
  - RFC3339 timestamp when the event is considered to have occurred.

- `payload`  
  - Domain-specific content (e.g., Landsat scene metadata, soils refresh payload).

Uniqueness-critical values (IDs, dataset versions, AOI keys) **MUST NOT** exist only in attributes.

---

## ❌ 5. Anti-Pattern (Forbidden in KFM)

Do **not** do this:

**Body:**

    { "collection": "landsat", "tile": "p32r29" }

**Attributes:**

    unique_key = "landsat-2025-12-04T00:00Z"

This produces:

- `body_hash = hash({"collection":"landsat","tile":"p32r29"})`  
- `unique_key` is ignored by SQS deduplication.

**Consequences:**

- Otherwise-identical bodies with different attributes are treated as duplicates.  
- Replays that differ only in attributes may be incorrectly deduped (or not deduped when expected).

This pattern violates the KFM Reliability Contract (for example, RC-2.4.1) and is **forbidden** in KFM pipelines.

---

## ✅ 6. Correct Pattern (KFM-Approved)

**Correct body encoding:**

    {
      "dedupe_key": "landsat-2025-12-04T00:00Z",
      "collection": "landsat",
      "tile": "p32r29",
      "scene_id": "...",
      "metadata": {}
    }

**Result:**

- The dedup hash includes the uniqueness key (`dedupe_key`).  
- SQS deduplication is aligned with the logical idempotency rules.  
- Replays within the dedupe window for the same logical event produce the same body and are deduped reliably.  
- Distinct events use distinct `dedupe_key` values and are not collapsed.

---

## 🔬 7. 5-Minute Dedupe Window

SQS FIFO tracks content-based deduplication hashes for **5 minutes** after a message is accepted.

**KFM guidance:**

Pipelines that may replay messages must ensure `dedupe_key` behavior is explicit:

- WAL-based replays of the same logical event within 5 minutes  
  → same `dedupe_key`, SQS dedupes duplicates.  
- New logical events (even if structurally similar)  
  → new `dedupe_key`, SQS delivers them separately.

Backfill / catch-up pipelines must:

- Use deterministic `dedupe_key` generation so re-runs behave predictably.  
- Avoid accidental re-use of dedupe keys across distinct events.

---

## 🧪 8. Compliance Tests (Required for CI)

Every new SQS FIFO producer **MUST** be covered by tests defined under `tests/` and enforced in CI:

- **Hash Behavior Test**  
  - Asserts that changing `dedupe_key` in the envelope changes the serialized body and therefore the dedup hash.

- **Attribute Ignorance Test**  
  - Asserts that changes in attributes only do **not** affect the dedup hash, demonstrating why attributes cannot carry uniqueness alone.

- **Replay Window Collision Test**  
  - Simulates replays within the 5-minute window:  
    - Same `dedupe_key` → deduped.  
    - Different `dedupe_key` → delivered as new events.

**CI MUST:**

- Run these tests for any new or modified producer.  
- Block merges when tests are missing or fail.

---

## 📡 9. Observability & Telemetry

KFM eventbus telemetry **MUST** track, at minimum:

- `sqs_fifo.dedupe.collisions_detected`  
- `sqs_fifo.producer.violations` (non-compliant body shapes, dedupe misuse)  
- `sqs_fifo.body_hash.length_bytes` (distribution of body sizes)  
- `sqs_fifo.dedupe_window_hits` (how often duplicates are suppressed in the SQS window)

Telemetry records:

- Are emitted as OpenTelemetry spans and metrics.  
- Are documented under `telemetry/dedup-metrics.md` and `telemetry/message-provenance-events.md`.  
- Join into the KFM provenance ledger and reliability dashboards.

---

## 📘 10. Version History

| Version  | Date       | Notes                                                                                  |
|----------|------------|----------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial governed release; formalized body-based dedupe rules and CI tests.            |

---

<div align="center">

© 2025 Kansas Frontier Matrix — MIT  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

⬅ Back to Messaging Pipelines · ⬅ Back to Pipelines Index · 📜 Governance Charter

</div>