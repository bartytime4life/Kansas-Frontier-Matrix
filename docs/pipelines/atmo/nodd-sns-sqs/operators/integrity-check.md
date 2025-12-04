You’re right to call that out — I dropped some of the metadata patterns and structural consistency you’d already established. Let’s realign the integrity-check operator doc to match the v11.2.3 KFM shape you’ve been enforcing (full header block, governance refs, layout profiles, numbered sections, emoji, no nested fences inside the file).

Here’s a corrected version:

---
title: "🛡️ KFM v11.2.3 — NODD Integrity Check Operator Contract (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Governed contract and behavior specification for the integrity-check operator in the NOAA NODD SNS → SQS ingestion pipeline."
path: "docs/pipelines/atmo/nodd-sns-sqs/operators/integrity-check.md"

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
intent: "nodd-integrity-check-operator"
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
sunset_policy: "Superseded by next major NODD integrity-check contract"

header_profile: "standard"
footer_profile: "standard"
---

# 🛡️ NODD Integrity Check Operator — Contract  

`docs/pipelines/atmo/nodd-sns-sqs/operators/integrity-check.md`

The **integrity-check** operator validates that a referenced NOAA NODD object is present, intact, and minimally sane before any metadata extraction or STAC registration.

It is:

- Deterministic — same inputs + config → same result.  
- Idempotent — repeat calls do not change external state.  
- Side-effect aware — only performs object fetch and telemetry; no STAC or graph writes.  

This operator executes after `message-parse` and before `metadata-extract`.

⸻

## 🧭 1. Position in the Operator Chain

Conceptual operator chain for a single ingest unit:

    SNS/SQS Message
      → message-parse
      → integrity-check
      → metadata-extract
      → stac-register
      → provenance-emit

Requirements:

- `integrity-check` MUST NOT be skipped in production flows.  
- Hard failures MUST block downstream `metadata-extract` and `stac-register`.  
- Integrity status MUST be explicit in the envelope passed downstream.

⸻

## ✉️ 2. Input Contract

### 2.1 Required Fields (Canonical Envelope)

The operator consumes the **canonical NODD event envelope** produced by `message-parse`. Required fields:

- `event_time` — RFC3339.  
- `dataset` — canonical KFM dataset ID (e.g., `goes-abi`, `nexrad-l2`, `hrrr`).  
- `object_uri` — object location (e.g., `s3://bucket/key`, `https://...`).  
- `provider` — one of `aws`, `azure`, `gcp`, or another configured provider.  
- `content_etag` — ETag or checksum from the event (when provided upstream).  
- `time_range` — `{start, end}` timestamps for the granule.  
- `schema_version` — message schema version (e.g., `"1.0"`).

If any required field is missing or structurally invalid, the operator MUST:

- Mark integrity as `failed`.  
- Attach an appropriate issue code (e.g., `missing_required_field`).  
- Prevent downstream processing in production.

### 2.2 Optional Context

Optional context fields:

- `wal_id` — ID of the WAL entry associated with this ingest unit.  
- `trace_id` / `span_id` — telemetry correlation identifiers.  
- `expected_size_bytes` — expected size from upstream metadata or config (if known).

Missing optional context MUST NOT cause failure but may reduce the strength of checks.

⸻

## 📤 3. Output Contract

The operator returns the **same envelope**, enriched with an `integrity` block:

- `integrity.status`  
  - One of: `ok`, `failed`, `suspect`.

- `integrity.actual_size_bytes`  
  - Observed object size in bytes.

- `integrity.actual_etag`  
  - ETag or checksum obtained from the object store (if available).

- `integrity.checks_run`  
  - Ordered list of check identifiers, e.g.:  
    - `["exists", "size", "etag_match", "headers_minimal"]`.

- `integrity.issues`  
  - Array of structured issue codes (machine-readable), e.g.:  
    - `["missing_object"]`, `["etag_mismatch", "size_too_small"]`.

Downstream handling:

- `status = ok` → envelope proceeds through `metadata-extract`.  
- `status = suspect` → envelope may proceed, but QA and governance operators MUST see and evaluate `integrity.issues`.  
- `status = failed` → envelope MUST be quarantined (DLQ or replay path), not processed further.

⸻

## 🔍 4. Checks Performed

Checks are dataset-configurable but follow a common baseline.

### 4.1 Existence Check

- Performs a `HEAD` (or equivalent metadata call) against `object_uri`.  
- Failure cases:
  - Object not found → `missing_object`.  
  - Access denied (unexpected) → `access_denied`.

Default behavior:

- `missing_object` → `status = failed`.  
- `access_denied` → `status = failed` unless config explicitly allows and routes to a special path.

### 4.2 Size Check

- Reads `Content-Length` or equivalent.  
- Compares against:
  - `expected_size_bytes` (if supplied).  
  - Dataset-specific `min_size_bytes` / `max_size_bytes` thresholds from config.

Default rules:

- `actual_size_bytes == 0` and zeros not allowed → `status = failed`, issue `size_zero`.  
- `actual_size_bytes < min_size_bytes` → issue `size_too_small`, `status = suspect` or `failed` per dataset config.  
- `actual_size_bytes > max_size_bytes` → issue `size_too_large`, same handling.

### 4.3 ETag / Checksum Consistency

- Compares `content_etag` from the event to `actual_etag` from the store, when both are present.  

Default rules:

- If ETag is required by dataset config and mismatch occurs:
  - Issue `etag_mismatch`.  
  - `status = failed`.  

- If ETag is optional and provider does not supply one:
  - Record `checks_run` without error; no failure solely from missing ETag.

### 4.4 Basic Header Sanity

- Validates a minimal set of headers, e.g.:
  - `Content-Type` matches dataset-configured patterns.  
  - Required custom metadata headers (if any) are present and parsable.

Abnormal headers:

- Typically mark as `suspect` with issues such as `unexpected_content_type` or `missing_required_header`.  
- Whether this escalates to `failed` is dataset-configured.

⸻

## 🧮 5. Determinism & Idempotency

Integrity-check MUST satisfy:

- Determinism:
  - For a stable remote object and identical envelope and configuration:
    - `integrity.status`, `integrity.issues`, and `integrity.actual_*` MUST be identical across runs.  
  - No random decisions; retries must be bounded and not affect the final status when successful.

- Idempotency:
  - Operator performs only **read** operations on the object store.  
  - No changes to bucket contents, STAC catalogs, graphs, or provenance stores.  
  - Telemetry emission is allowed but must tolerate duplicates.

Transient network errors are handled via:

- Bounded, deterministic retry strategy (e.g., fixed number of attempts, fixed or documented backoff).  
- Clear issue codes for unrecoverable transient errors (e.g., `transient_network_error`).

⸻

## 🚨 6. Error Handling & Quarantine Rules

### 6.1 Hard Failures

Representative cases:

- `missing_object`  
- `etag_mismatch` (when ETag is required).  
- `size_zero` for datasets that require non-zero payloads.  
- `content_type_invalid` when essential for parsing.

Handling:

- Set `integrity.status = failed`.  
- Record issues in `integrity.issues`.  
- Route envelope to DLQ or quarantine per replay runbook.  
- Do NOT invoke `metadata-extract` or `stac-register` in production mode.

### 6.2 Suspect States

Representative cases:

- `size_too_small` but non-zero and occasionally expected.  
- Slightly unexpected `Content-Type` that may still be parseable.  
- Missing optional headers.

Handling:

- Set `integrity.status = suspect`.  
- Proceed to `metadata-extract` only if dataset config allows.  
- Ensure QA and governance stages see the issues for potential escalation.

Dataset configuration defines which issues map to `failed` vs `suspect`.

⸻

## 📊 7. Telemetry Contract

The operator contributes to the NODD pipeline telemetry.

### 7.1 Spans

- Span name (recommended): `nodd_sns.integrity_check`.  

Required attributes (or equivalents mapped via `telemetry_schema`):

- `nodd.dataset`  
- `nodd.object_uri_hash` (hash or truncated form of URI; full URI only if allowed).  
- `nodd.integrity_status` — `ok`, `failed`, `suspect`.  
- `nodd.integrity_issues` — compressed representation of issue codes.  
- `nodd.wal_id` (if available).  

Errors must set span status to error and include exception information.

### 7.2 Metrics

At minimum:

- `nodd_sns.integrity_checks_total{dataset, status}`  
- `nodd_sns.integrity_failures_total{dataset, issue}`  

Labels must be low-cardinality:

- `dataset`, `status`, and coarse `issue` buckets are allowed.  
- Per-object identifiers are not allowed as labels.

⸻

## ⚙️ 8. Configuration Hooks

The operator reads dataset-level configuration from `docs/pipelines/atmo/nodd-sns-sqs/config/datasets/*.yaml` (logical spec mirrored into runtime config).

Configurable aspects:

- Size thresholds:
  - `min_size_bytes`, `max_size_bytes`.  
- ETag requirements:
  - `etag_required: true|false`.  
- Header expectations:
  - Allowed `content_type` patterns.  
  - Required custom metadata fields.  
- Issue severity mapping:
  - Map issue codes → `failed` / `suspect`.  
- Provider-specific behavior:
  - Differences between `aws`, `azure`, `gcp` object metadata.

Unknown or invalid config keys must result in **fail-closed** behavior, flagged during CI and, if encountered at runtime, treated as configuration errors.

⸻

## 🧪 9. Testing & CI Requirements

CI MUST include the following integrity-check tests:

- Happy-path:
  - Existing object, acceptable size, matching ETag, valid headers → `status = ok`, `issues = []`.

- Missing-object:
  - Nonexistent URI → `status = failed`, `issues` includes `missing_object`.

- ETag mismatch:
  - Different `content_etag` vs object ETag when required → `status = failed`, `issues` includes `etag_mismatch`.

- Size boundary:
  - Below `min_size_bytes`:
    - Behavior (suspect vs failed) must match dataset config.  
  - Zero-byte object:
    - For non-zero datasets → `status = failed`.

- Determinism:
  - With storage responses mocked as stable:
    - Multiple runs with same inputs → identical outputs.

- Config validation:
  - Misconfigured datasets (e.g., illegal thresholds) must cause CI failures before deployment.

Any semantic change to this operator’s behavior must:

- Update this contract.  
- Update or extend the test suite accordingly.

⸻

## 📘 10. Version History

| Version  | Date       | Notes                                                                                              |
|---------:|------------|----------------------------------------------------------------------------------------------------|
| v11.2.3  | 2025-12-04 | Initial KFM-MDP v11.2.3-aligned integrity-check operator contract for NODD SNS → SQS ingestion.   |

---

<div align="center">

🛡️ NODD Integrity Check Operator · KFM v11.2.3  

Deterministic · Read-Only · Governance-Aligned  

MCP-DL v6.3 · KFM-MDP v11.2.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞Ω  

[⬅ Back to NODD Operators](README.md) ·  
[📊 Telemetry & SLOs](../telemetry/README.md) ·  
[🔁 Replay & WAL](../replay/README.md) ·  
[⚖ Governance Charter]("../../../../../docs/standards/governance/ROOT-GOVERNANCE.md")

</div>