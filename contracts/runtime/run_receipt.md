<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-runtime-run-receipt
title: contracts/runtime/run_receipt.md — RunReceipt Contract
type: contract
version: v0.2
status: draft; PROPOSED; schema-paired; runtime-receipt; execution-audit
owners: OWNER_TBD — Runtime steward · Contracts steward · Schema steward · Policy steward · Source steward · Validation steward · Evidence steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; runtime; run-receipt; execution-audit; provenance; validation-aware; source-aware; no-executable-authority
tags: [kfm, contracts, runtime, run-receipt, receipt, provenance, stage, inputs, outputs, code-ref, spec-hash, source-descriptor-refs, validation-refs, success, partial, fail]
related:
  - ./README.md
  - ./decision_envelope.md
  - ./runtime_response_envelope.md
  - ./ai_receipt.md
  - ../policy/policy_decision.md
  - ../evidence/evidence_bundle.md
  - ../../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../../policy/runtime/
  - ../../fixtures/contracts/v1/runtime/run_receipt/
  - ../../tools/validators/validate_run_receipt.py
  - ../../docs/architecture/contract-schema-policy-split.md
notes:
  - "Expanded from existing schema-paired stub at `contracts/runtime/run_receipt.md`."
  - "Paired schema verified at `schemas/contracts/v1/runtime/run_receipt.schema.json`; schema status is PROPOSED."
  - "The schema requires run_id, stage, inputs, outputs, code_ref, spec_hash, source_descriptor_refs, validation_refs, and outcome; additional properties are false."
  - "RunReceipt records a runtime/stage execution receipt. It is not executable code, not validation proof by itself, not EvidenceBundle, not PolicyDecision, not ReleaseManifest, and not public-client permission."
  - "Rollback target for this expansion is previous blob SHA `4898799e1ee774bb2f49ceb5a477396701c03e5e`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# RunReceipt Contract

> `RunReceipt` records the accountable summary of one governed runtime or pipeline stage execution: what run/stage executed, which inputs and outputs were referenced, which code/spec identity was used, which source descriptors and validation records were attached, and whether the run finished as `SUCCESS`, `PARTIAL`, or `FAIL`. It is a receipt, not the executed code or proof of truth.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Family: runtime" src="https://img.shields.io/badge/family-runtime-0a7ea4">
  <img alt="Object: RunReceipt" src="https://img.shields.io/badge/object-RunReceipt-blueviolet">
  <img alt="Schema: paired" src="https://img.shields.io/badge/schema-paired-green">
  <img alt="Execution: receipt only" src="https://img.shields.io/badge/execution-receipt__only-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/runtime/run_receipt.md`  
**Paired schema:** `schemas/contracts/v1/runtime/run_receipt.schema.json`  
**Schema status:** PROPOSED  
**Validator path named by schema:** `tools/validators/validate_run_receipt.py` — NEEDS VERIFICATION for implementation/wiring  
**Policy authority:** `policy/runtime/`, not this contract  
**Runtime/execution authority:** implementation roots, job runners, workflow engines, and pipeline code, not this contract  
**Truth posture:** CONFIRMED schema pairing and required field surface · CONFIRMED run outcome enum · CONFIRMED additional properties are closed · NEEDS VERIFICATION for validator wiring, fixtures, runtime/pipeline integration, source descriptor resolution, validation report resolution, receipt persistence, and CI enforcement

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Schema-paired field surface](#schema-paired-field-surface) · [Field semantics](#field-semantics) · [Outcome semantics](#outcome-semantics) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Boundaries](#boundaries) · [Validation expectations](#validation-expectations) · [Fixtures](#fixtures) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`RunReceipt` is the accountable receipt for a governed runtime or pipeline stage execution.

It answers:

- which run executed;
- which stage or lifecycle step the run belongs to;
- which input refs were consumed;
- which output refs were produced;
- which code reference and spec hash identify the logic used;
- which source descriptors were relevant;
- which validation reports or validation refs were attached;
- whether the run outcome was `SUCCESS`, `PARTIAL`, or `FAIL`.

It does not answer:

- whether the outputs are true;
- whether outputs are publishable;
- whether promotion is approved;
- whether policy allowed downstream serving;
- whether validation actually passed unless the referenced validation records say so;
- whether public clients may read the outputs;
- whether raw/work/quarantine/canonical stores are exposed.

---

## Meaning

A `RunReceipt` is a provenance and audit receipt. It ties an execution event to the inputs, outputs, code, spec, sources, and validation records that downstream review/policy/release flows may inspect.

A mature governed runtime flow should look like:

```text
bounded inputs
  -> runtime/pipeline stage execution
  -> output refs
  -> validation records
  -> RunReceipt
  -> policy / review / promotion / release checks
  -> governed runtime response or release artifact, if allowed
```

`RunReceipt` does not replace validation reports, evidence bundles, release manifests, or policy decisions. It is the receipt that helps those objects trace what happened.

---

## Schema-paired field surface

The paired schema currently confirms these fields:

| Field | Required | Schema-confirmed shape | Semantic role |
|---|---:|---|---|
| `run_id` | yes | string matching `^[a-z][a-z0-9_:.-]*$` | Stable run identifier. |
| `stage` | yes | string | Runtime/pipeline/lifecycle stage name. |
| `inputs` | yes | array of strings | Input refs consumed by the run. |
| `outputs` | yes | array of strings | Output refs produced by the run. |
| `code_ref` | yes | string | Code, workflow, package, commit, or adapter reference. |
| `spec_hash` | yes | string matching `^sha256:[a-f0-9]{64}$` | Hash binding the run to contract/spec/config identity. |
| `source_descriptor_refs` | yes | array of strings | SourceDescriptor refs relevant to the run. |
| `validation_refs` | yes | array of strings | Validation records/reports attached to the run. |
| `outcome` | yes | enum: `SUCCESS`, `PARTIAL`, `FAIL` | Finite run result. |

The schema also confirms:

```text
additionalProperties: false
```

---

## Field semantics

### `run_id`

Stable identifier for this run receipt.

Requirements:

- must follow the schema pattern;
- should be traceable enough for audit and rollback;
- must not encode secrets, credentials, private input content, or sensitive exact-location values.

PROPOSED convention:

```text
run:<stage>:<date-or-digest>
```

### `stage`

The runtime, pipeline, validation, ingestion, transformation, rendering, AI, or release-adjacent stage represented by the receipt.

The schema currently allows any string. A controlled stage vocabulary is PROPOSED and should align with lifecycle gates and domain/runbook vocabulary before enforcement.

### `inputs`

String refs to inputs consumed by the run.

Inputs should be governed refs, not inline payloads. They may point to staged artifacts, source descriptors, catalog refs, evidence refs, prior outputs, or release candidates according to lifecycle and policy constraints.

### `outputs`

String refs to outputs produced by the run.

Outputs should be refs to governed artifacts or records. A run receipt should not embed produced data or claim public release by itself.

### `code_ref`

Reference to the code, workflow, script, package, image, notebook, adapter, or commit used by the run.

A mature implementation should make this specific enough for reproducibility and review without exposing secrets.

### `spec_hash`

SHA-256 hash binding the run to spec/config/contract lineage.

The schema requires `sha256:<64 lowercase hex>`. This is an integrity hook, not a full proof by itself.

### `source_descriptor_refs`

Refs to SourceDescriptor objects involved in or relied upon by the run.

These preserve source-role visibility and prevent source-role collapse. Refs should resolve for trust-bearing downstream use.

### `validation_refs`

Refs to validation outputs associated with the run.

These may include schema validation, policy validation, source checks, data quality checks, redaction checks, tile validation, receipt/proof checks, or review validation. The receipt links to validation; it does not replace validation.

### `outcome`

Finite run result.

The outcome describes the run completion state only. It does not mean evidence is true, publication is allowed, or public serving is safe.

---

## Outcome semantics

| Outcome | Meaning | Downstream posture |
|---|---|---|
| `SUCCESS` | The run completed and produced outputs according to its immediate execution criteria. | Eligible for downstream validation/review/policy; not automatically publishable. |
| `PARTIAL` | The run completed with missing, degraded, skipped, quarantined, restricted, or failed components. | Requires review and explicit downstream handling; fail closed for public serving unless policy allows safe partial use. |
| `FAIL` | The run failed or could not safely produce governed outputs. | Do not promote or publish outputs; inspect validation/log/receipt refs. |

---

## Invariants

CONFIRMED by paired schema:

- `run_id`, `stage`, `inputs`, `outputs`, `code_ref`, `spec_hash`, `source_descriptor_refs`, `validation_refs`, and `outcome` are required.
- `run_id` must match `^[a-z][a-z0-9_:.-]*$`.
- `spec_hash` must match `^sha256:[a-f0-9]{64}$`.
- `outcome` must be one of `SUCCESS | PARTIAL | FAIL`.
- Additional properties are not allowed.

PROPOSED semantic invariants:

- Run receipts must reference inputs and outputs; they must not embed payloads.
- `SUCCESS` does not mean release/publication approval.
- `PARTIAL` and `FAIL` are first-class states and must not be hidden.
- Source descriptor refs must preserve source-role and provenance context.
- Validation refs must resolve before the run receipt is used for promotion/release decisions.
- A run receipt should not be used as proof of truth without EvidenceBundle/proof/validation context.
- Public clients must not treat RunReceipt as permission to read RAW/WORK/QUARANTINE/canonical/internal stores.
- Corrections, withdrawals, and rollback workflows should be able to trace affected outputs back through run receipts.

---

## Lifecycle role

`RunReceipt` may appear at multiple internal and governed boundary points:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Typical uses:

| Lifecycle point | Role of RunReceipt |
|---|---|
| RAW ingest | Records ingest run and source descriptor refs. |
| WORK / QUARANTINE | Records transformation, quarantine, redaction, or triage runs. |
| PROCESSED | Records derived artifact generation and validation refs. |
| CATALOG / TRIPLET | Records cataloging, graph/triplet projection, and reconciliation runs. |
| Release candidate | Supports promotion/release checks; does not approve release. |
| Runtime serving | May support runtime envelope audit; does not serve payloads. |
| Correction/rollback | Helps trace affected outputs and rebuild/restore safe states. |

---

## Boundaries

| Boundary | Rule |
|---|---|
| RunReceipt vs runtime code | RunReceipt records that a run occurred; code executes elsewhere. |
| RunReceipt vs validation report | RunReceipt references validation; validation report owns pass/fail details. |
| RunReceipt vs EvidenceBundle | RunReceipt records execution provenance; EvidenceBundle supports claims. |
| RunReceipt vs PolicyDecision | RunReceipt may be an input to policy; PolicyDecision records policy outcome. |
| RunReceipt vs ReleaseManifest | RunReceipt may support release; ReleaseManifest binds released contents. |
| RunReceipt vs AIReceipt | RunReceipt covers general run/stage execution; AIReceipt covers AI-mediated runtime accountability. |
| RunReceipt vs public response | RuntimeResponseEnvelope/public API owns client-facing response posture. |

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- validator existence and wiring for `tools/validators/validate_run_receipt.py`;
- fixture coverage under `fixtures/contracts/v1/runtime/run_receipt/`;
- controlled vocabulary for `stage`;
- expected ref formats for `inputs`, `outputs`, `source_descriptor_refs`, and `validation_refs`;
- code-ref format and reproducibility requirements;
- spec-hash canonicalization profile;
- policy behavior for `PARTIAL` and `FAIL` outputs;
- CI tests proving receipts cannot be used as release approval or evidence truth;
- correction/rollback tracing from released artifacts back to run receipts.

---

## Fixtures

Minimum fixture set PROPOSED:

| Fixture | Purpose |
|---|---|
| `valid_success_ingest.json` | Valid ingest/source run receipt. |
| `valid_success_transform.json` | Valid transformation run receipt. |
| `valid_partial_quarantine.json` | Valid partial outcome where some outputs are quarantined or withheld. |
| `valid_fail_validation.json` | Valid failure outcome with validation refs. |
| `valid_release_candidate_support.json` | Run receipt used as support for release candidate review. |
| `invalid_missing_run_id.json` | Confirms required run id. |
| `invalid_bad_run_id_pattern.json` | Confirms run id pattern. |
| `invalid_bad_spec_hash.json` | Confirms SHA-256 hash pattern. |
| `invalid_unknown_outcome.json` | Confirms finite outcome enum. |
| `invalid_extra_property.json` | Confirms additional properties are closed. |

Fixtures must use synthetic/safe refs only.

---

## Open questions

- Should `stage` use a central lifecycle/runtime vocabulary?
- Should `inputs` and `outputs` become structured refs rather than strings?
- Should `code_ref` require commit/image/package digest format?
- Should `spec_hash` refer to contract hash, config hash, workflow hash, or a combined canonical run spec?
- Where are run receipt instances persisted for audit and release review?
- How should RunReceipt link to proof/receipt families beyond validation refs?

---

## Rollback

Rollback is required if this contract is used as executable runtime behavior, proof of truth, validation proof, release approval, policy authority, public API/UI/map/AI permission, or a way to expose raw/work/quarantine/internal outputs.

Rollback target for this expansion: previous blob SHA `4898799e1ee774bb2f49ceb5a477396701c03e5e`.

<p align="right"><a href="#top">Back to top</a></p>
