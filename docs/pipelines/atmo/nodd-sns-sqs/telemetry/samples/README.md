---
title: "📁 KFM v11.2.3 — NODD Telemetry Samples Specification (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Canonical, redacted OpenTelemetry trace, metric, and log samples for the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/telemetry/samples/README.md"

version: "v11.2.3"
last_updated: "2025-12-04"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Atmospheric Systems · Provenance & Reliability Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x telemetry-samples compatible"
status: "Active · Enforced"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-version-hash>"
doc_integrity_checksum: "<sha256>"

signature_ref: "../../../../../../releases/v11.2.3/signature.sig"
attestation_ref: "../../../../../../releases/v11.2.3/slsa-attestation.json"
sbom_ref: "../../../../../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../../../../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../../../../../releases/v11.2.3/nodd-sns-telemetry.json"
telemetry_schema: "../../../../../../schemas/telemetry/nodd-sns-sqs-v1.json"
energy_schema: "../../../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../../../schemas/telemetry/carbon-v2.json"

governance_ref: "../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Telemetry Samples Specification"
intent: "nodd-sns-sqs-telemetry-samples"
category: "Pipelines · Atmospheric · Telemetry · Samples"

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
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true

ttl_policy: "24 Months"
sunset_policy: "Superseded by next major NODD telemetry samples standard"

header_profile: "standard"
footer_profile: "standard"
---

# 📁 NODD Telemetry Samples Specification  

`docs/pipelines/atmo/nodd-sns-sqs/telemetry/samples/README.md`

Canonical, **redacted** sample telemetry payloads for the NOAA NODD SNS → SQS ingestion pipeline.  
These samples define what **valid traces, metrics, and logs** look like in practice and serve as:

- Ground truth for CI validation of telemetry shape.  
- Human-readable examples for SREs, data engineers, and governance reviewers.  
- Fixtures for dashboards and alert configuration.

⸻

## 🧭 1. Purpose

This document governs the contents of the `samples/` directory:

- Ensures example telemetry payloads are **schema-compliant**, **redacted**, and **FAIR+CARE aligned**.  
- Provides **reference shapes** for:
  - OpenTelemetry traces (spans).  
  - Metrics exports (time-series points / scrapes).  
  - Structured logs (JSON events).  
- Enables **automated validation** that docs, telemetry schemas, and runtime emissions stay in sync.

No sample in this directory may contain:

- Real secrets, credentials, or ARNs.  
- Real user PII or sensitive location details.  
- Unredacted object URIs for sensitive datasets.

⸻

## 🗂 2. Directory Layout (Samples)

This directory sits under `docs/pipelines/atmo/nodd-sns-sqs/telemetry/samples/` and MUST contain:

    docs/pipelines/atmo/nodd-sns-sqs/telemetry/samples/
    │
    ├── 📄 README.md                 # This file (samples spec)
    │
    ├── 📄 example-trace.json        # Canonical, redacted OpenTelemetry trace (single ingest unit)
    ├── 📄 example-metrics.json      # Canonical, redacted metric export (queue age, latency, DLQ)
    └── 📄 example-log.json          # Canonical, redacted structured log entry

Additional sample files MAY be added (e.g., per-dataset variants) but MUST be documented in this README.

⸻

## 🧵 3. Trace Sample — `example-trace.json`

### 3.1 Purpose

`example-trace.json` MUST represent a **single end-to-end ingest unit** for NODD SNS → SQS, including spans for:

- `nodd_sns.message_parse`  
- `nodd_sns.integrity_check`  
- `nodd_sns.metadata_extract`  
- `nodd_sns.stac_register`  
- `nodd_sns.provenance_emit`

### 3.2 Required Characteristics

The trace sample MUST:

- Conform to `telemetry_schema` field names and types for spans.  
- Use **redacted** values for:
  - Object URIs (e.g., hashed or truncated).  
  - Cloud resource identifiers.  
- Include:
  - A single `trace_id` with multiple spans.  
  - Parent-child relationships consistent with the operator chain.  
  - Span attributes:
    - `nodd.dataset`  
    - `nodd.integrity_status`  
    - `nodd.metadata_status`  
    - `nodd.stac_write_status`  
    - `nodd.provenance_status`  

CI MUST parse `example-trace.json` and validate it against the telemetry schema and invariants (e.g., operator ordering).

⸻

## 📊 4. Metrics Sample — `example-metrics.json`

### 4.1 Purpose

`example-metrics.json` MUST represent a **small, bounded** set of metric samples that exercise the primary NODD metrics:

- Queue depth and age.  
- Ingest latency.  
- DLQ counts.  
- Replay counts.  
- Optional energy and carbon metrics.

### 4.2 Required Characteristics

The metrics sample MUST:

- Demonstrate canonical metric names and labels, such as:
  - `nodd_sns.queue_depth{queue,env}`  
  - `nodd_sns.queue_age_seconds{queue,env,quantile}`  
  - `nodd_sns.ingest_latency_seconds_bucket{dataset,env,le}`  
  - `nodd_sns.dlq_messages_total{queue,env,dataset}`  

- Avoid:
  - High-cardinality label values.  
  - Real dataset-specific identifiers disguised as examples.

The format (e.g., OTLP JSON, Prometheus exposition modeled in JSON) MUST match the form used in `telemetry_schema` and CI validation.

⸻

## 📝 5. Log Sample — `example-log.json`

### 5.1 Purpose

`example-log.json` MUST represent a **single structured log entry** for an ingest unit, such as:

- A summary success log, or  
- A validation failure log.

### 5.2 Required Characteristics

The log sample MUST:

- Be valid JSON and include:

  - High-level fields:
    - `timestamp` (RFC3339).  
    - `level` (e.g., `INFO`, `WARN`, `ERROR`).  
    - `message` (human-readable summary).  

  - Correlation fields:
    - `trace_id`, `span_id`.  
    - `wal_id` (if available).  
    - `dataset`.  
    - `object_uri_hash` (not full URI).  

  - Outcome fields:
    - `status` (`success`, `quarantined`, `failed`).  
    - `issues` (list of issue codes, where applicable).

- Contain **no** raw PII, secrets, or unredacted identifiers.  
- Match the logging patterns described in the main telemetry README.

⸻

## 🧼 6. Redaction & Privacy Rules

All samples MUST obey the following redaction rules:

- **Object URIs**:
  - Use hashed or truncated forms (e.g., `hash://...`) rather than real bucket names/keys.  

- **Cloud resource identifiers**:
  - Replace real account IDs, ARNs, and project IDs with placeholders (e.g., `123456789012` → `000000000000`).  

- **Sensitive datasets**:
  - If samples represent datasets that can overlap with sensitive or sovereign content, make sure:
    - Geometries are generalized or synthetic.  
    - No real site coordinates or exact timestamps that could identify protected locations.

- **User/operator identifiers**:
  - Use generic or synthetic agent IDs (`"kfm-nodd-ingest"`, `"operator@example.org"`), not real emails or names.

Redaction MUST preserve **shape and structure** so that examples remain valid against schemas and tests.

⸻

## 🧪 7. CI & Validation Requirements

CI MUST validate this directory and its contents:

- **Schema Validation**:
  - `example-trace.json`, `example-metrics.json`, and `example-log.json` MUST validate against:
    - `telemetry_schema` (for shapes and field types).  
    - Any additional per-sample schema declared in the NODD telemetry spec.

- **Invariants**:
  - Trace sample MUST contain the full operator span chain in the correct order.  
  - Metrics sample MUST include at least one sample for each required metric family.  
  - Log sample MUST include correlation fields and structured issue codes.

- **Redaction Checks**:
  - CI SHOULD ensure no obvious secrets:
    - No patterns matching AWS keys, Cloud ARNs, or real domain names beyond approved examples.  

Any change to sample shapes, fields, or semantics MUST:

- Update this README if behavior or expectations change.  
- Update CI tests that consume and validate these samples.

⸻

## 🕰 8. Version History

| Version  | Date       | Notes                                                                                                 |
|---------:|------------|-------------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial NODD telemetry samples spec; defined trace, metrics, log sample contracts and redaction rules.|

---

<div align="center">

📁 NODD Telemetry Samples · KFM v11.2.3  

Schema-Grounded · Redacted · CI-Validated  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Telemetry](../README.md) ·  
[🧠 Operators](../../operators/README.md) ·  
[⚖ Governance Charter](../../../../../../docs/standards/governance/ROOT-GOVERNANCE.md)

</div>
