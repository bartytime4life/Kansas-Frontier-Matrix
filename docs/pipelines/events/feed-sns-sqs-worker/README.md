---
title: "⚡ KFM v11 — Event-Driven Feed → SQS FIFO → Worker Pipeline (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Deterministic, idempotent event-ingestion pattern using SNS → SQS FIFO → worker → S3, with WAL replay, telemetry, and FAIR+CARE governance."
path: "docs/pipelines/events/feed-sns-sqs-worker/README.md"
version: "v11.2.3"
last_updated: "2025-12-02"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x ingestion-contract compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.3/event-ingest-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/event-ingest-v1.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
license: "CC-BY 4.0"

mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"

status: "Active / Enforced"
doc_kind: "Pipeline"
header_profile: "standard"
footer_profile: "standard"

intent: "event-ingestion"
fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"

scope:
  domain: "pipelines"
  applies_to:
    - "event-ingestion"
    - "sns"
    - "sqs-fifo"
    - "lambda-worker"
    - "wal-replay"

semantic_intent:
  - "reliability"
  - "governance"
  - "supply-chain"
category: "Pipelines · Events · Ingestion"

sensitivity: "General (non-sensitive; auto-mask rules apply)"
sensitivity_level: "None"
public_exposure_risk: "Low"
classification: "Internal"
jurisdiction: "Kansas / United States"
indigenous_rights_flag: false

data_steward: "Reliability Engineering & Event Ingestion WG"
ttl_policy: "Indefinite (subject to architecture evolution)"
sunset_policy: "Supersede when v12 event-ingestion patterns are adopted"

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
  - "docs/pipelines/events/feed-sns-sqs-worker/README.md@v11.2.2"

provenance_requirements:
  versions_required: true
  newest_first: true
  must_reference_superseded: true
  must_reference_origin_root: true

json_schema_ref: "schemas/json/docs-pipelines-events-feed-sns-sqs-worker-v11.2.3.schema.json"
shape_schema_ref: "schemas/shacl/docs-pipelines-events-feed-sns-sqs-worker-v11.2.3-shape.ttl"
story_node_refs: []

immutability_status: "mutable"

doc_uuid: "urn:kfm:doc:pipelines:events:feed-sns-sqs-worker:v11.2.3"
semantic_document_id: "kfm-pipelines-events-feed-sns-sqs-worker-v11.2.3"
event_source_id: "ledger:kfm:doc:pipelines:events:feed-sns-sqs-worker:v11.2.3"

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

# ⚡ Event-Driven Feed → SQS FIFO → Worker Pipeline  

`docs/pipelines/events/feed-sns-sqs-worker/README.md`

**Purpose:**  
Define a **deterministic, idempotent event-ingestion pattern** for KFM: external feed → SNS → SQS FIFO → idempotent worker → S3 versioned storage → telemetry + provenance.  
Designed for **NOAA, USGS, NASA/HydroGNSS, ESA Sentinel**, and other event-driven sources.

[![Docs · MCP v6.3](https://img.shields.io/badge/Docs-MCP_v6.3-blue)](../../../README.md) ·
[![KFM-MDP v11.2.2](https://img.shields.io/badge/KFM%E2%80%93MDP-v11.2.2-informational)](../../../standards/kfm_markdown_protocol_v11.2.2.md) ·
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Compliant-gold)](../../../standards/faircare/FAIRCARE-GUIDE.md) ·
[![Status: Active](https://img.shields.io/badge/Status-Active-success)](../../../../releases/v11.2.3/manifest.zip)

</div>

---

## 🧭 1. Overview

This ingestion pipeline enforces a **governed, replay-safe event pattern**:

- External provider (NOAA, NASA, USGS, STAC hosts, etc.) publishes into an **SNS topic**.  
- SNS → **SQS FIFO** queue with content-based deduplication.  
- An idempotent **worker** (Lambda or container) processes each record.  
- Output written to **S3 versioned bucket** for persistence + provenance.  
- Structured **telemetry** and **energy/carbon metrics** emitted per event.  
- **WAL-style replay** with deterministic idempotency, integrated with LangGraph gates.  
- **FAIR+CARE compliance** for all event metadata and downstream usage.

This pattern is the **baseline** for event ingestion into KFM and MUST be reused or extended rather than re-invented.

---

## 🗂️ 2. Directory Layout (Emoji-Prefix Standard)

~~~text
docs/pipelines/events/feed-sns-sqs-worker/
│
├── 📄 README.md                                  # This file
│
├── 🧰 terraform/                                 # Infra-as-code (SNS, SQS FIFO, DLQ, IAM, retry)
│   ├── 📄 main.tf
│   ├── 📄 sns.tf
│   ├── 📄 sqs.tf
│   ├── 📄 iam.tf
│   └── 📄 variables.tf
│
├── 🧪 tests/                                     # Integration + CI replay tests
│   ├── 📄 fifo-dedup.spec.md
│   ├── 📄 dlq-replay.spec.md
│   └── 📄 schema-validation.spec.md
│
├── 🛠️ worker/                                    # Lambda / containerized worker logic (spec)
│   ├── 📄 handler.py
│   ├── 📄 requirements.txt
│   └── 📄 idempotency.py
│
├── 🧾 samples/                                   # Example SNS → SQS messages
│   ├── 📄 sample-nexrad.json
│   └── 📄 sample-generic.json
│
└── 📚 metadata/                                  # Contracts, schemas, governance
    ├── 📄 event-schema-v1.json
    ├── 📄 ingestion-contract.md
    └── 📄 retry-replay-contract.md
~~~

Code under `worker/` is a **reference implementation**. Production workers MUST live in the appropriate service repos but follow this pattern and contracts.

---

## 🚀 3. Architectural Pattern

This ingestion pipeline enforces:

- **SNS topic** ← external provider (NOAA, USGS, NASA/HydroGNSS, ESA, etc.).  
- **SQS FIFO** queue with content-based deduplication:
  - Avoids double-processing when providers re-send the same event.  
- **DLQ** to capture events failing more than N attempts (default 5).  
- **Strict idempotency** via SHA-256 message derivation key.  
- **S3 versioned writes** for durable, provenance-rich event storage.  
- **Structured telemetry** for reliability, cost, energy, and carbon.  
- **Replay safety** with WAL semantics and deterministic idempotency.  
- **FAIR+CARE alignment**, especially for space-, water-, and land-related datasets.

---

## ⚙️ 4. Infra Creation Snippets (Reference Only)

Infrastructure SHOULD be provisioned via Terraform; CLI below is illustrative.

### 4.1 Create DLQ

~~~bash
aws sqs create-queue \
  --queue-name kfm-updates-dlq.fifo \
  --attributes FifoQueue=true,ContentBasedDeduplication=true,MessageRetentionPeriod=1209600
~~~

### 4.2 Create Main FIFO Queue with DLQ Binding

~~~bash
aws sqs create-queue \
  --queue-name kfm-updates.fifo \
  --attributes FifoQueue=true,ContentBasedDeduplication=true,\
RedrivePolicy="{\"deadLetterTargetArn\":\"$DLQ_ARN\",\"maxReceiveCount\":\"5\"}"
~~~

### 4.3 Bind SNS → SQS

~~~bash
aws sns subscribe \
  --topic-arn "$TOPIC_ARN" \
  --protocol sqs \
  --notification-endpoint "$KFM_QARN"
~~~

All IAM policies MUST be represented in `terraform/iam.tf` with:

- Explicit principals and resources.  
- `aws:SourceArn` constraints for SNS → SQS.  
- No wildcard `*` permissions on S3 or SQS.

---

## 🧠 5. Worker Logic (Deterministic & Idempotent)

Reference Python handler:

~~~python
import hashlib
import json

def idem_key(msg_body: str) -> str:
    return hashlib.sha256(msg_body.encode("utf-8")).hexdigest()

def handle(record):
    body = json.loads(record["Body"])
    key  = idem_key(record["Body"])

    validate_schema(body)          # Contract: metadata/event-schema-v1.json
    validate_checksums(body)       # Integrity: hashes, ETags, etc.

    s3.put_object(
        Bucket=BUCKET,
        Key=f"ingest/events/{key}.json",
        Body=record["Body"].encode("utf-8"),
        ContentType="application/json",
    )

    emit_telemetry("ingest_ok", key=key)
~~~

Worker requirements:

- **Idempotency key** MUST be stable for identical messages (after any normalization rules).  
- Worker MUST avoid side effects that depend on wall-clock or randomness for correctness.  
- Validation MUST precede write; failed validation MUST result in DLQ routing.  
- Telemetry MUST include key identifiers (event id, idem key, replay id where applicable).

---

## 🔁 6. Replay, WAL, and DLQ Behavior

Replay and DLQ semantics:

- Messages are retried up to **5 times**; after that, they are placed in DLQ.  
- A **Replay operator** (e.g., LangGraph-based) consumes DLQ events and:
  - Quarantines irreparable events with full context.  
  - Re-queues events once root causes are corrected.

Each replay event MUST emit:

- `replay_id` — unique identifier for replay execution.  
- `previous_attempts` — count of prior deliveries.  
- `validation_fail_reason` — standardized error codes/messages.  
- `energy_cost_ws` — worker energy estimate in watt-seconds.  
- `carbon_grams_estimated` — CO₂e estimate via energy/carbon schemas.

Contracts for WAL and replay MUST be documented in `metadata/retry-replay-contract.md`.

---

## 🧪 7. Testing Requirements

Tests defined in `tests/` are normative:

- **FIFO Dedup Test** (`fifo-dedup.spec.md`):
  - Verifies content-based deduplication and SHA-256 idempotency.  
  - Confirms multiple identical messages lead to **one** persisted object.

- **DLQ Replay Test** (`dlq-replay.spec.md`):
  - Ensures DLQ replay respects original ordering and WAL semantics.  
  - Confirms replay does not double-write or silently drop recoverable events.

- **Schema Validation Test** (`schema-validation.spec.md`):
  - Validates incoming events against `metadata/event-schema-v1.json`.  
  - Ensures invalid events route to DLQ with correct telemetry and provenance.

CI pipelines for any implementation of this pattern MUST reference or extend these specs.

---

## 📊 8. Telemetry & Energy/Carbon Metrics

Minimum required metrics:

- `event_ingest_latency_ms`  
- `event_dedup_hits`  
- `event_dlq_count`  
- `event_success_total`  
- `event_worker_energy_ws`  
- `event_worker_carbon_g`

Example emitted as a structured record:

~~~json
{
  "event_id": "123e4567-e89b-12d3-a456-426614174000",
  "latency_ms": 215,
  "dedup_hit": false,
  "dlq": false,
  "energy_ws": 4.2,
  "carbon_g": 1.1
}
~~~

OpenTelemetry spans:

- `sns_to_sqs_delivery`  
- `sqs_receive`  
- `contract_validation`  
- `idempotent_write`  
- `wal_replay`

All telemetry MUST validate against:

- `event-ingest-v1.json`  
- `energy-v2.json`  
- `carbon-v2.json`

---

## 🔐 9. IAM & Security Controls

IAM MUST follow **least privilege**:

- Worker role:
  - `sqs:ReceiveMessage`, `sqs:DeleteMessage`, `sqs:GetQueueAttributes` for the target queue.  
  - `s3:PutObject` (and optionally `GetObject`) on the specific ingestion bucket/prefix.  
  - `logs:CreateLogStream`, `logs:PutLogEvents` for logging.  

- SNS topic policy:
  - Restrict subscriptions to the KFM SQS ARN.  
  - Use `aws:SourceArn` and `Condition` blocks to prevent unauthorized subscriptions.

Secrets and sensitive config MUST be:

- Stored in a secret manager or encrypted parameters.  
- Never logged in plaintext.

---

## 🧭 10. Validation & Governance Gates

Recommended LangGraph operators:

- **SchemaGate**  
  - Validates events against:
    - STAC schemas.  
    - NOAA / USGS / mission-specific formats.  
    - `event-schema-v1`.

- **IntegrityGate**  
  - Verifies payload checksums, digital signatures (when present), and size constraints.

- **CARE-SensitiveGate**  
  - Applies auto-redaction for sensitive locations or resources.  
  - Ensures alignment with `sovereignty_policy` and FAIR+CARE.

- **ReplayGate**  
  - Enforces WAL contracts and replay policies:
    - Max replay attempts.  
    - Quarantine thresholds.  
    - Governance logging.

All gates MUST emit spans and logs that can be traced with `event_id` and `replay_id`.

---

## 📚 11. Version History

| Version  | Date       | Notes                                                  |
|----------|------------|--------------------------------------------------------|
| v11.2.3  | 2025-12-02 | Full KFM v11 alignment; energy/carbon telemetry added. |
| v11.2.2  | 2025-11-18 | Added WAL replay contracts and DLQ behavior.           |
| v11.2.0  | 2025-11-01 | Introduced event ingestion pipeline pattern.           |

---

<div align="center">

⚡ **KFM v11 — Event-Driven Feed → SQS FIFO → Worker Pipeline**  
Deterministic Events · WAL-Aware Replay · FAIR+CARE-Governed Ingestion  

[📘 Pipelines Index](../../README.md) · [🛡 Reliability Framework](../../reliability/README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>