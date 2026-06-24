<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-source-ingest-receipt
title: contracts/source/ingest_receipt.md — IngestReceipt Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; source-ingest-receipt; integrity-bound
owners: OWNER_TBD — Source steward · Ingest steward · Contracts steward · Schema steward · Policy steward · Validation steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; source; ingest-receipt; source-admission; provenance; digest; lifecycle-aware; no-release-authority
tags: [kfm, contracts, source, ingest-receipt, receipt, source-id, run-id, started-at, finished-at, success, partial, fail, bytes-in, sha256, provenance, source-admission]
related:
  - ./README.md
  - ./source_descriptor.md
  - ./doctrine_artifact_descriptor.md
  - ../runtime/run_receipt.md
  - ../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../policy/source/
  - ../../fixtures/contracts/v1/source/ingest_receipt/
  - ../../tools/validators/validate_ingest_receipt.py
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/work/
  - ../../data/quarantine/
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from a generic schema-paired stub at `contracts/source/ingest_receipt.md`."
  - "Paired schema verified at `schemas/contracts/v1/source/ingest_receipt.schema.json`; schema status is PROPOSED."
  - "The schema requires id, source_id, run_id, started_at, finished_at, outcome, bytes_in, and digests; additional properties are false."
  - "IngestReceipt records a source ingest event and content digests. It is not SourceDescriptor, not RunReceipt, not EvidenceBundle, not PolicyDecision, not ReleaseManifest, and not publication approval."
  - "Rollback target for this expansion is previous stub blob SHA `e15e622390e9bb4fdfb0da53188075b92a8f11c5`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# IngestReceipt Contract

> `IngestReceipt` records that source material was captured or ingested into a governed KFM lifecycle lane: which source descriptor was involved, which run performed ingest, when it started and finished, whether it ended as `SUCCESS`, `PARTIAL`, or `FAIL`, how many bytes were captured, and which SHA-256 digests pin the captured inputs. It is an ingest receipt, not source truth, not a release decision, and not a substitute for `SourceDescriptor` or `RunReceipt`.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/source" src="https://img.shields.io/badge/root-contracts%2Fsource-blue">
  <img alt="Object: IngestReceipt" src="https://img.shields.io/badge/object-IngestReceipt-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Integrity: sha256" src="https://img.shields.io/badge/integrity-sha256-0a7ea4">
  <img alt="Boundary: receipt not truth" src="https://img.shields.io/badge/boundary-receipt__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/source/ingest_receipt.md`  
**Paired schema:** `schemas/contracts/v1/source/ingest_receipt.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_ingest_receipt.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/source/`, not this contract  
**Lifecycle authority:** lifecycle/data roots, ingest pipelines, and source registry records, not this contract  
**Truth posture:** CONFIRMED target was a generic schema-paired stub · CONFIRMED paired schema exists and points to this contract · CONFIRMED finite outcome enum and digest pattern · CONFIRMED additional properties are closed · NEEDS VERIFICATION for validator wiring, fixtures, ingest pipeline integration, source descriptor resolution, receipt persistence, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Outcome semantics](#outcome-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`IngestReceipt` is the source-family receipt for an ingest/capture event.

It answers:

- which ingest receipt was emitted;
- which `source_id` was involved;
- which `run_id` performed or coordinated the ingest;
- when ingest started and finished;
- whether ingest ended as `SUCCESS`, `PARTIAL`, or `FAIL`;
- how many bytes were captured;
- which SHA-256 digests pin captured blobs, source files, payloads, responses, or normalized intake units.

It does not answer:

- whether the source claims are true;
- whether the source is admitted for all uses;
- whether rights/sensitivity policy allows public use;
- whether downstream derived artifacts are valid;
- whether material can move from RAW/WORK/QUARANTINE to PROCESSED/CATALOG/PUBLISHED;
- whether a release is approved;
- whether runtime/API/UI/AI clients may access the captured material.

---

## Meaning

An ingest receipt is process memory for source capture. It binds a source ingest run to time, outcome, byte count, and content digests.

A mature governed source ingest flow should look like:

```text
SourceDescriptor / source-admission posture
  -> source ingest run
  -> captured material in RAW or WORK/QUARANTINE
  -> IngestReceipt with digests and outcome
  -> validation / policy / review / transformation
  -> downstream receipts and lifecycle transitions if allowed
```

`IngestReceipt` is narrower than `RunReceipt`: it records source ingest/capture details. A `RunReceipt` may summarize a larger pipeline stage and reference source descriptors, validations, inputs, outputs, code, and spec lineage.

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable ingest receipt identifier. |
| `source_id` | yes | string | SourceDescriptor/source registry id involved in ingest. |
| `run_id` | yes | string | Ingest run identifier. |
| `started_at` | yes | date-time string | Ingest start timestamp. |
| `finished_at` | yes | date-time string | Ingest finish timestamp. |
| `outcome` | yes | enum: `SUCCESS`, `PARTIAL`, `FAIL` | Finite ingest result. |
| `bytes_in` | yes | integer, minimum `0` | Count of bytes received/captured. |
| `digests` | yes | object with at least one property; values match `^sha256:[a-f0-9]{64}$` | Named SHA-256 digests for captured content units. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `id`

Stable identifier for this ingest receipt.

It should be unique and traceable. It must not encode secrets, credentials, private URLs, tokens, or sensitive payload values.

PROPOSED convention:

```text
ingest:<source_id>:<date-or-run-suffix>
```

### `source_id`

Reference to the source identity being ingested.

The field should resolve to a governed `SourceDescriptor` or accepted source registry entry before downstream use. An unresolved `source_id` must fail closed for promotion or public use.

### `run_id`

Identifier for the ingest run.

This may align with a runtime `RunReceipt.run_id`, pipeline run id, workflow id, job id, or source-refresh runbook id. It should support cross-reference without requiring clients to access execution logs directly.

### `started_at`

Timestamp when the ingest attempt began.

### `finished_at`

Timestamp when the ingest attempt finished.

A mature validator should verify `finished_at` is not earlier than `started_at`. The current schema does not express that temporal relation.

### `outcome`

Finite result of the ingest attempt.

This is a run/capture outcome, not policy admissibility, validation success, or release approval.

### `bytes_in`

Number of bytes received or captured by the ingest process.

`0` may be valid for `FAIL` or some metadata-only runs, but should be scrutinized for `SUCCESS` unless the ingest profile explicitly permits it.

### `digests`

Named content digests for captured materials.

The schema requires at least one digest and requires each value to match `sha256:<64 lowercase hex>`. Keys may name blobs, source files, API payloads, archive members, snapshots, manifests, normalized capture units, or safe synthetic test payloads.

---

## Outcome semantics

| Outcome | Meaning | Downstream posture |
|---|---|---|
| `SUCCESS` | Ingest completed according to immediate capture criteria and produced digest-pinned material. | Eligible for validation, policy, source review, and lifecycle transition checks; not automatically publishable. |
| `PARTIAL` | Ingest completed with missing, skipped, truncated, restricted, quarantined, or failed components. | Must be reviewed and normally fail closed for public or promotion use unless policy explicitly permits a safe partial. |
| `FAIL` | Ingest failed or could not safely capture source material. | Do not promote or publish; inspect logs/validation/run receipts and retry or quarantine as appropriate. |

---

## Invariants

CONFIRMED by paired schema:

- `id`, `source_id`, `run_id`, `started_at`, `finished_at`, `outcome`, `bytes_in`, and `digests` are required.
- `id` must match `^[a-z][a-z0-9_:.-]*$`.
- `started_at` and `finished_at` must be date-time strings.
- `outcome` must be one of `SUCCESS | PARTIAL | FAIL`.
- `bytes_in` must be an integer greater than or equal to `0`.
- `digests` must contain at least one property.
- Every digest value must match `sha256:<64 lowercase hex>`.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- `source_id` should resolve to a governed SourceDescriptor before downstream use.
- IngestReceipt should be emitted before captured source material is used for transformation, evidence assembly, cataloging, graph projection, or public release.
- `SUCCESS` does not mean the source is trusted, admissible, valid, or publishable.
- `PARTIAL` and `FAIL` must remain first-class outcomes and must not be hidden by downstream convenience code.
- Digest mismatch invalidates the captured material until re-ingested or corrected.
- Ingest receipts should be immutable; corrections should supersede rather than silently edit.
- Public clients must not use IngestReceipt as permission to read RAW/WORK/QUARANTINE/internal source material.

---

## Lifecycle role

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical uses:

| Lifecycle point | Role of IngestReceipt |
|---|---|
| RAW intake | Records source capture and pins raw payload digests. |
| WORK / QUARANTINE | Records partial, restricted, failed, or review-required captures. |
| PROCESSED | Supports traceability into transformations and validation reports. |
| CATALOG / TRIPLET | Supports provenance and source-role visibility. |
| Release candidate | May support release review, but does not approve release. |
| Correction/rollback | Helps identify which captured payloads and derived outputs are affected by source changes. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| IngestReceipt vs SourceDescriptor | SourceDescriptor governs source identity/role/rights/sensitivity; IngestReceipt records a capture event. |
| IngestReceipt vs RunReceipt | IngestReceipt is source-ingest-specific; RunReceipt summarizes broader runtime/pipeline stage execution. |
| IngestReceipt vs ValidationReport | ValidationReport owns validation pass/fail details; IngestReceipt pins captured inputs. |
| IngestReceipt vs EvidenceBundle | EvidenceBundle supports claims; IngestReceipt supports source-capture provenance. |
| IngestReceipt vs PolicyDecision | Policy decides admissibility; receipt records ingest outcome. |
| IngestReceipt vs ReleaseManifest | ReleaseManifest binds published artifacts; ingest receipt does not publish. |
| IngestReceipt vs source raw data | Receipt contains refs/digests, not source payloads. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for `tools/validators/validate_ingest_receipt.py`;
- fixture coverage under `fixtures/contracts/v1/source/ingest_receipt/`;
- temporal validation that `finished_at >= started_at`;
- source_id resolution against SourceDescriptor/source registry records;
- digest calculation profile and canonicalization for API payloads, archives, streamed content, and normalized snapshots;
- policy behavior for unresolved, credentialed, closed, restricted, or rights-unknown sources;
- behavior for `PARTIAL` ingest and zero-byte cases;
- linkage to runtime `RunReceipt` where a larger pipeline run exists;
- correction/supersession workflow for re-ingest and source refresh.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_success_single_payload.json` | Successful ingest with one digest. |
| `valid_success_multi_digest.json` | Successful ingest with multiple named captured units. |
| `valid_partial_missing_member.json` | Partial ingest where some members failed or were withheld. |
| `valid_fail_zero_bytes.json` | Failed ingest with zero bytes and digest posture to be reviewed. |
| `invalid_missing_source_id.json` | Confirms required source id. |
| `invalid_bad_id_pattern.json` | Confirms receipt id pattern. |
| `invalid_bad_digest_pattern.json` | Confirms SHA-256 digest value pattern. |
| `invalid_empty_digests.json` | Confirms `minProperties: 1`. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |

Fixtures must use synthetic/safe source ids and synthetic digest values only.

---

## Open questions

- Should `source_id` use the same pattern as the SourceDescriptor schema (`kfm://source/...` or `src:...`)?
- Should `run_id` be required to match a `RunReceipt.run_id` when a runtime receipt exists?
- Should schema express `finished_at >= started_at` through a custom validator?
- Should `digests` keys have a controlled vocabulary such as `raw_payload`, `headers`, `manifest`, `normalized_snapshot`, or `archive_member:<name>`?
- Where are IngestReceipt instances persisted: `data/registry/sources/`, `data/raw/.../_receipts/`, `receipts/source/`, or another governed root?

---

## Rollback

Rollback is required if this contract is used as source truth, SourceDescriptor replacement, runtime execution summary, validation proof, policy decision, release approval, source payload storage, public API permission, or AI/source authority.

Rollback target for this expansion: previous stub blob SHA `e15e622390e9bb4fdfb0da53188075b92a8f11c5`.

<p align="right"><a href="#top">Back to top</a></p>
