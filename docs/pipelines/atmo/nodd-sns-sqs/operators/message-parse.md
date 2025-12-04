---
title: "✉️ KFM v11.2.3 — NODD Message Parse Operator Contract (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contract and behavior specification for the message-parse operator in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/message-parse.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x operator-contract compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Pipeline Operator Contract"
intent: "nodd-message-parse-operator"
category: "Pipelines · Atmospheric · Operators"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
classification: "Public"
jurisdiction: "Kansas / United States"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
immutability_status: "version-pinned"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: false
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD message-parse contract"

header_profile: "standard"
footer_profile: "standard"
---

# ✉️ NODD Message Parse Operator — Contract  

`docs/pipelines/atmo/nodd-sns-sqs/operators/message-parse.md`

The **message-parse** operator converts raw **SNS → SQS** notifications from the NOAA NODD program into a **canonical NODD event envelope** used by all downstream operators.

It is:

- Deterministic — same raw message + config → same canonical envelope.  
- Idempotent — repeat parses do not change external state.  
- Side-effect aware — does not fetch objects, write STAC, or mutate the graph; only normalizes the message and emits telemetry.

This operator executes first in the hot-path, immediately after the worker receives an SQS message.

⸻

## 🧭 1. Position in the Operator Chain

Conceptual operator chain for a single NODD ingest unit:

    SNS/SQS Message
      → message-parse
      → integrity-check
      → metadata-extract
      → stac-register
      → provenance-emit

Requirements:

- `message-parse` MUST run before any operator that assumes a canonical envelope shape.  
- Downstream operators MUST NOT attempt to re-interpret raw SNS/SQS payloads.  
- Any parsing failure MUST be explicit and MUST NOT silently default fields.

⸻

## 📥 2. Input Contract

The operator consumes a **raw SQS message** that wraps an SNS notification.

### 2.1 Raw SQS Envelope (Conceptual Shape)

Required structural elements:

- SQS-level fields:
  - `MessageId`  
  - `ReceiptHandle`  
  - `Body` (raw SNS payload as JSON string)  
  - `Attributes` (e.g., `ApproximateReceiveCount`, `SentTimestamp`)  

- SNS-level body (within `Body`):
  - `Type` (e.g., `Notification`)  
  - `MessageId`  
  - `TopicArn`  
  - `Timestamp`  
  - `Subject` (may carry product hints)  
  - `Message` (string containing NODD JSON payload or URL-encoded data)  
  - `MessageAttributes` (key/value attributes such as product, dataset, region)  

The exact SNS payload structure MUST conform to the schema version referenced in the NODD telemetry and SNS schema docs (e.g., message-v1).

### 2.2 Assumptions

- The worker has already validated that:
  - The SQS message is well-formed JSON.  
  - The SNS envelope fields exist (at least `Message` and `TopicArn`).  

If either SQS or SNS envelope structure is missing or corrupt, `message-parse` MUST treat this as a hard parse failure.

⸻

## 📤 3. Output Contract — Canonical NODD Event Envelope

The operator produces a **canonical envelope** used by all downstream NODD operators.

Required fields in the canonical envelope:

- `event_time`  
  - RFC3339 timestamp representing when the upstream event occurred (prefer SNS `Timestamp`; fall back only with documented logic).

- `dataset`  
  - Canonical KFM dataset ID (e.g., `goes-abi`, `nexrad-l2`, `nexrad-l3`, `hrrr`, `surface-obs`).  
  - Derived from SNS `TopicArn`, `MessageAttributes`, and/or payload, using dataset config.

- `object_uri`  
  - Full URI of the object (e.g., `s3://bucket/key`, `https://...`, or provider-specific URI scheme).

- `provider`  
  - Object storage provider, e.g., `aws`, `azure`, `gcp`, or configured value.

- `content_etag`  
  - ETag/checksum advertised by NODD, if present in the message payload.

- `time_range`  
  - Object time window as a structure:  
    - `time_range.start` — RFC3339.  
    - `time_range.end` — RFC3339.  
  - Derived from payload metadata (e.g., observation window, model time step).

- `priority`  
  - Processing priority, e.g., `high`, `normal`, `low`, derived from dataset config and/or message attributes.

- `schema_version`  
  - Canonical message schema version (e.g., `"1.0"`).

Metadata about the source message:

- `raw.sqs_message_id`  
- `raw.sns_message_id`  
- `raw.topic_arn`  
- `raw.subject` (if available)

If the operator cannot derive any of the required canonical fields, it MUST treat the message as a parse failure.

⸻

## 🧩 4. Parsing Rules & Normalization

### 4.1 Dataset Resolution

`dataset` MUST be resolved deterministically using:

- Mapping from `TopicArn` to dataset ID (as declared in `config/sns-topics.yaml`).  
- Potentially refined by `MessageAttributes` (e.g., product subtypes) if necessary.

Rule:

- If no dataset mapping exists for the `TopicArn`, the operator MUST:
  - Mark the message as `unroutable`.  
  - Treat this as a hard failure unless config explicitly allows dropping or separate routing.

### 4.2 Object URI Extraction

The operator MUST extract a single, canonical `object_uri`:

- From JSON in the `Message` field (e.g., `s3://` URL, HTTPS path).  
- Normalized into a consistent URI form (no trailing slashes, normalized case where appropriate).

If multiple URIs are present, dataset-specific config may determine:

- Which one is canonical.  
- Whether to treat extra URIs as errors or additional assets handled later.

### 4.3 Time Range Derivation

The operator:

- Extracts time fields from the message payload (e.g., `start_time`, `end_time`, `valid_time`).  
- Normalizes them to RFC3339 and populates `time_range.start` and `time_range.end`.

Rules:

- If only a single timestamp exists, both start and end may be set to that value with documented semantics.  
- If time fields are missing but required by dataset config:
  - Treat as a parse failure.

### 4.4 Priority Assignment

Priority is resolved from:

- Configured defaults per dataset.  
- Optional overrides via `MessageAttributes` (e.g., `priority = "high"`).

If no priority is present and no default exists:

- Default to a safe, documented value (e.g., `normal`) and record this in telemetry.

⸻

## ✅ 5. Validation & Failure Modes

The operator MUST validate the canonical envelope before returning it.

### 5.1 Required Field Validation

If any required canonical field is:

- Missing  
- Structurally invalid (e.g., non-RFC3339 time)  
- Nonsensical (e.g., `time_range.end < time_range.start`)

Then:

- Mark the parse as a hard failure.  
- Tag with one or more parse issue codes (e.g., `missing_dataset`, `invalid_time_range`).  
- Ensure downstream operators do not receive a partial envelope.

### 5.2 Schema Version Compatibility

The operator asserts that:

- `schema_version` in the embedded payload (if present) is supported.  
- If unsupported:
  - Issue code `unsupported_schema_version`.  
  - Behavior depends on config:
    - Default: hard failure.  
    - Optional: quarantined routing for forward-compatibility experiments.

⸻

## 🧮 6. Determinism & Idempotency

Message-parse MUST be:

- Deterministic:
  - Same SQS message JSON + same configuration → bitwise-equivalent canonical envelope (ordering of object keys aside).  
  - No random or time-of-day-based branches.

- Idempotent:
  - It performs only **in-memory transformation** and telemetry; no external writes.  
  - It can be safely replayed multiple times for the same raw message.

Any non-deterministic behaviors (e.g., environment-specific differences) MUST be eliminated or explicitly documented and minimized.

⸻

## 📊 7. Telemetry Contract

The operator contributes to the NODD telemetry model.

### 7.1 Spans

Recommended span name: `nodd_sns.message_parse`.

Required attributes:

- `nodd.dataset` (if resolved; `unknown` if not).  
- `nodd.topic_arn` (or a safe hash/truncated form).  
- `nodd.parse_status` — `ok`, `failed`.  
- `nodd.schema_version` — parsed schema version.  
- `nodd.parse_issues` — compact issue code list.

Failures MUST mark the span as error and include exception details.

### 7.2 Metrics

At minimum:

- `nodd_sns.messages_parsed_total{dataset, status}`  
- `nodd_sns.parse_failures_total{reason}`  

Where:

- `status` ∈ `{ok, failed}`.  
- `reason` is a low-cardinality bucket (e.g., `missing_required_field`, `unsupported_schema_version`, `unroutable_topic`).

⸻

## ⚙️ 8. Configuration Hooks

The operator is driven by logical configuration declared in:

- `docs/pipelines/atmo/nodd-sns-sqs/config/sns-topics.yaml`  
- `docs/pipelines/atmo/nodd-sns-sqs/config/datasets/*.yaml`

Configurable aspects:

- Topic → dataset mappings.  
- Additional dataset-level message fields to use for time ranges, URIs, and priority.  
- Schema-version compatibility rules (supported versions, deprecation schedule).  
- Handling of unknown topics, datasets, or schema versions (drop vs quarantine vs fail).

Unknown config keys or inconsistent mappings MUST be detected in CI and treated as configuration errors prior to deployment.

⸻

## 🧪 9. Testing & CI Requirements

CI MUST include tests that validate `message-parse` behavior:

- Happy-path:
  - Valid SNS/SQS envelope for each supported dataset → canonical envelope with all required fields set.

- Malformed message:
  - Missing `Message` or non-JSON payload → parse failure with `parse_issues` set appropriately.

- Unsupported schema version:
  - Payload with explicitly unsupported `schema_version` → failure behavior matches config.

- Unmapped topic:
  - `TopicArn` without dataset mapping → `unroutable_topic` issue and configured failure behavior.

- Determinism:
  - Same raw message + config → identical canonical output across multiple runs (with mocks isolating external state).

Changes to parsing logic or canonical envelope shape MUST:

- Update this contract if semantics change.  
- Update or extend the test suite accordingly.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                               |
|---------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned message-parse operator contract for NODD SNS → SQS ingestion.      |

---

<div align="center">

✉️ NODD Message Parse Operator · KFM v11.2.3  

Deterministic · Canonicalizing · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Operators](README.md) ·  
[🛡️ Integrity Check](integrity-check.md) ·  
[📊 Telemetry & SLOs](../telemetry/README.md) ·  
[⚖ Governance Charter](../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>