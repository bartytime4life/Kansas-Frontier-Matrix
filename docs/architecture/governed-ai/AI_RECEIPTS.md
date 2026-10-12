<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/governed-ai/ai-receipts
title: Governed AI — AIReceipt Architecture and Accountability Boundary
type: architecture-standard
version: v2.0
status: draft; repository-grounded; schema-paired; bounded-proof-only; non-authoritative
owners:
  - "@bartytime4life — verified CODEOWNERS review route"
  - "NEEDS VERIFICATION — governed-AI, runtime, evidence, policy, citation, security, privacy, contracts, schemas, validation, correction, retention, and release reviewers"
created: 2026-05-15
updated: 2026-08-19
policy_label: public
owning_root: docs/
responsibility: Explain the current AIReceipt contract/schema, bounded candidate builders, validator and fixture proofs, object-family boundaries, data-minimization rules, unresolved persistence and correction work, and the conditions required before AIReceipt can participate in an operational governed-AI flow.
truth_posture: CONFIRMED current repository evidence / PROPOSED operational composition / UNKNOWN deployed emission, persistence, retention, correction propagation, signing, and release use
repository: bartytime4life/Kansas-Frontier-Matrix
base_commit: 1fbb35ccf3f4d9166c815ded78bfd851e3825ece
target_prior_blob: df65d7b33d359c6721378caaf1e2933c240a9ef3
codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
adr_0019_blob: 5c45cbaf0aae510638088913757634ea978c9ec3
governed_ai_readme_blob: 9e1071bb69910bde3f364d319923c4db00637639
ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
ai_receipt_validator_blob: eb80e77aed15f478c32215c8f773f308a87a092a
ai_receipt_validator_test_blob: f35514538205fbac359520327e7519b3a851cea8
ai_receipt_workflow_blob: 1192926b29a6007b78887ade1058e8e2c6ce8023
ai_receipt_builder_blob: 5fe03c96f22ea99b3e8689b92c7ee23d4fc12a65
ai_receipt_builder_test_blob: 34b07a7f8353ef402f721e234789a6d4f3a5b924
mock_projection_blob: 6b77074f1b47c575abd00fff989ff7d0795bedb1
mock_projection_test_blob: 6ac251c7ea2a17ec2c7bd326880d582cc012e6b4
data_receipts_ai_readme_blob: e2b8971c19ae6edd4f1e6a566eee2ec24d14becc
inspection_boundary: >
  Current-session GitHub reads covered the complete prior target, accepted Directory
  Rules and ADR-0029, CODEOWNERS, the governed-AI parent and adjacent adapter page,
  ADR-0019 status, the runtime AIReceipt contract and strict schema, current valid and
  invalid fixture inventories, the dedicated validator, focused validator tests,
  path-scoped workflow, deterministic candidate builder, MockAdapter projection,
  focused package tests, generated implementation receipts, runtime policy inventory,
  and the documented data/receipts/ai lane. No live model, credential, provider endpoint,
  governed-AI API route, evidence resolver, policy evaluator, citation-validation service,
  receipt emitter or durable store, retention job, correction propagation, signature
  verifier, deployed client, release environment, rollback drill, or publication path was
  exercised.
related:
  - README.md
  - ADAPTER_CONTRACT.md
  - BOUNDARIES.md
  - FOCUS_FLOW.md
  - MOCK_FIRST.md
  - ROUTE_MAP.md
  - ../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../doctrine/directory-rules.md
  - ../../../contracts/runtime/ai_receipt.md
  - ../../../contracts/runtime/runtime_response_envelope.md
  - ../../../contracts/policy/policy_decision.md
  - ../../../contracts/evidence/evidence_bundle.md
  - ../../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../../fixtures/contracts/v1/runtime/ai_receipt/README.md
  - ../../../tools/validators/validate_ai_receipt.py
  - ../../../tests/validators/test_validate_ai_receipt.py
  - ../../../packages/envelopes/src/envelopes/ai_receipt.py
  - ../../../packages/envelopes/src/envelopes/mock_adapter_receipt.py
  - ../../../tests/packages/envelopes/test_ai_receipt_candidate.py
  - ../../../tests/packages/envelopes/test_mock_adapter_ai_receipt_candidate.py
  - ../../../.github/workflows/ai-receipt.yml
  - ../../../data/receipts/ai/README.md
tags: [kfm, architecture, governed-ai, ai-receipt, accountability, runtime, schema, validator, finite-outcomes, citation-validation, policy-decision, digests, no-chain-of-thought, no-publication-authority]
notes:
  - "v2.0 replaces a stale, truncated proposal with a current repository-grounded architecture companion."
  - "The previous page described a larger speculative field set that conflicts with the current closed runtime schema; this revision defers field authority to the contract/schema pair."
  - "This same-path revision changes documentation and its generated authoring receipt only."
  - "No contract, schema, policy, package, runtime, fixture, validator, test, workflow, receipt instance, data layout, release record, deployment, source, or repository setting is changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed AI — AIReceipt Architecture and Accountability Boundary

> **Operating boundary.** `AIReceipt` records a bounded accountability trace for an AI-mediated runtime event. It binds adapter/model identity, caller-supplied input and output digests, policy and citation-validation references, and one finite outcome. It does **not** make generated language true, prove that references resolve, authorize a public answer, or create release or publication authority.

[![status](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-authority)
[![shape](https://img.shields.io/badge/schema-9%20required%20fields-0969da?style=flat-square)](#current-schema-paired-profile)
[![validator](https://img.shields.io/badge/validator-bounded%20offline%20proof-2da44e?style=flat-square)](#validation-and-proof)
[![runtime](https://img.shields.io/badge/runtime%20emitter-HOLD-d4a72c?style=flat-square)](#operational-maturity-and-holds)
[![truth](https://img.shields.io/badge/model%20truth-no-6e7781?style=flat-square)](#object-family-boundaries)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#status-and-authority)

> [!IMPORTANT]
> **This page is explanatory architecture, not field authority.** The semantic contract lives at [`contracts/runtime/ai_receipt.md`](../../../contracts/runtime/ai_receipt.md); the machine shape lives at [`schemas/contracts/v1/runtime/ai_receipt.schema.json`](../../../schemas/contracts/v1/runtime/ai_receipt.schema.json). Policy, citation validation, runtime behavior, persisted receipt instances, and release decisions remain in their owning roots.

> [!CAUTION]
> **A schema-valid receipt is not a governed answer.** The current validator proves closed JSON shape and limited local consistency. It does not resolve `policy_decision_ref` or `citation_validation_ref`, calculate or verify semantic digest coverage, call a model, approve a provider, authorize an answer, promote lifecycle state, release, or publish.

> [!WARNING]
> **Do not store prompts, chain-of-thought, credentials, raw evidence, or protected details in AIReceipt.** The current schema is closed with `additionalProperties: false`; raw payload and hidden-reasoning fields are outside the profile and must remain outside the receipt.

**Quick navigation:** [Status](#status-and-authority) · [Purpose](#purpose-and-scope) · [Current profile](#current-schema-paired-profile) · [Fields](#field-semantics) · [Outcomes](#finite-outcome-vocabularies) · [Construction](#candidate-construction) · [Flow](#target-governed-flow) · [Boundaries](#object-family-boundaries) · [Safety](#data-minimization-and-security) · [Validation](#validation-and-proof) · [Storage](#persistence-retention-and-access) · [Correction](#correction-supersession-and-replay) · [HOLDs](#operational-maturity-and-holds) · [Anti-patterns](#anti-patterns) · [Change](#change-discipline-and-rollback) · [Evidence](#evidence-ledger) · [Related](#related-documents)

---

<a id="status-and-authority"></a>

## Status and authority

| Question | Current evidence-backed answer |
|---|---|
| Is this a tracked architecture document? | **CONFIRMED.** `docs/architecture/governed-ai/AI_RECEIPTS.md` existed at the inspected base. |
| Is the same-path placement valid? | **CONFIRMED.** Accepted ADR-0029 adopts Directory Rules v2; this file remains a human architecture explanation under `docs/`. |
| Was the prior page current? | **No.** It was truncated mid-sentence and described a speculative receipt shape that does not match the current closed schema. |
| Is there a semantic AIReceipt contract? | **CONFIRMED present / PROPOSED status.** [`contracts/runtime/ai_receipt.md`](../../../contracts/runtime/ai_receipt.md) defines the meaning and boundaries. |
| Is there a machine schema? | **CONFIRMED present / PROPOSED status.** The strict Draft 2020-12 schema requires nine fields and denies additional properties. |
| Is there executable validation? | **CONFIRMED, bounded.** A deterministic no-network validator, focused tests, two valid fixtures, three invalid fixtures, and a path-scoped workflow exist. |
| Is there candidate-construction code? | **CONFIRMED, bounded.** A package helper builds exactly the nine schema fields; a second helper projects a prevalidated MockAdapter outcome into that candidate. |
| Is there an operational AIReceipt emitter or durable store? | **No verified implementation.** The inspected evidence does not establish runtime emission, persistence, retention, query, correction, or public projection. |
| Is AIReceipt an accepted architecture decision? | **No.** ADR-0019 remains `proposed`; this page cannot accept it. |
| Does this revision change runtime or publication state? | **No.** It is documentation plus generated authoring provenance only. |

### Directory Rules basis

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [Directory Rules v2](../../doctrine/directory-rules.md) the placement authority. The current file receives `PLACE` as an existing same-path explanatory document. It does not move authority from any other root.

| Responsibility | Owning surface | This page may do |
|---|---|---|
| Human architecture explanation | `docs/architecture/governed-ai/` | Explain current evidence, boundaries, risks, HOLDs, validation, and rollback. |
| Semantic meaning | `contracts/runtime/ai_receipt.md` | Summarize and link; never redefine silently. |
| Machine shape | `schemas/contracts/v1/runtime/ai_receipt.schema.json` | Report the current field grammar; never create a competing shape. |
| Admissibility and access | `policy/` | State required separation; never claim a policy decision occurred. |
| Candidate construction | `packages/envelopes/` | Cite bounded behavior; never infer end-to-end orchestration. |
| Runtime execution | `runtime/` and `apps/` | Record verified maturity; never invent an emitter, route, or store. |
| Fixtures, tests, validators, CI | `fixtures/`, `tests/`, `tools/`, `.github/workflows/` | Cite the exact proof surface and its limits. |
| Receipt instances | governed `data/receipts/` lanes | Describe unresolved storage posture; never treat a README as emitted data. |
| Release, correction, rollback | distinct governed families | Keep these decisions separate from receipt presence. |

[Back to top](#top)

---

<a id="purpose-and-scope"></a>

## Purpose and scope

### Purpose

This page explains how the current `AIReceipt` profile fits into KFM's governed-AI trust membrane. It is intended for runtime, API, evidence, policy, citation, validation, security, correction, and release reviewers who need to distinguish:

1. the current receipt shape;
2. the bounded code that can construct and validate a candidate;
3. the authority-bearing objects that the receipt only references;
4. the runtime and storage work that remains unverified; and
5. the controls required before a receipt can support audit, replay, incident review, correction, or release review.

### In scope

- the current nine-field contract/schema pair;
- finite AI outcomes and separate validator outcomes;
- candidate-builder and MockAdapter projection behavior;
- local shape and consistency validation;
- data minimization, sensitive-content exclusions, and safe findings;
- receipt/evidence/policy/citation/envelope/release boundaries;
- persistence, retention, signing, correction, and replay HOLDs;
- validation commands, graduation criteria, and rollback.

### Out of scope

This page does not:

- accept ADR-0019 or any provider/adaptor decision;
- change the AIReceipt contract or schema;
- define a new reason-code, timestamp, evidence-ref, prompt, token, cost, signature, or retention field;
- admit or call a model;
- implement evidence resolution, policy evaluation, citation validation, a Governed API route, runtime emission, or durable persistence;
- authorize access to `data/receipts/ai/` from public clients;
- release, deploy, promote, publish, or approve generated language.

[Back to top](#top)

---

<a id="current-schema-paired-profile"></a>

## Current schema-paired profile

The current machine authority is a closed JSON object with exactly nine required properties:

```json
{
  "id": "ai_receipt:focus:example-001",
  "run_id": "run-example-001",
  "adapter": "mock",
  "model_ref": "fixture-only",
  "inputs_digest": "sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
  "outputs_digest": "sha256:bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
  "policy_decision_ref": "policy-decision:example-001",
  "citation_validation_ref": "citation-validation:example-001",
  "outcome": "ABSTAIN"
}
```

> [!NOTE]
> This is an illustrative schema-valid shape, not an emitted receipt, policy decision, citation result, answer, or release record.

| Schema rule | Current value |
|---|---|
| JSON Schema dialect | Draft 2020-12 |
| Root type | object |
| Required properties | all nine properties shown above |
| `id` pattern | `^[a-z][a-z0-9_:.-]*$` |
| Digest pattern | `^sha256:[a-f0-9]{64}$` |
| Receipt outcomes | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` |
| Additional properties | denied |
| Schema status | `PROPOSED` |
| Declared validator | `tools/validators/validate_ai_receipt.py` |
| Declared fixture root | `fixtures/contracts/v1/runtime/ai_receipt/` |

### Fields that are not in the current profile

The current schema does **not** contain fields for:

- prompt text, prompt template, or chain-of-thought;
- evidence payloads or direct `evidence_refs`;
- answer text, citations, or a `reason_code`;
- timestamps or duration;
- token counts, cost, temperature, seed, or other generation parameters;
- provider request/response bodies;
- sensitivity labels or redaction details;
- signatures, attestations, review approval, release state, correction state, or rollback target.

Those concerns must remain in their owning objects or require an explicit contract/schema evolution. They must not be inserted as unreviewed extra properties.

[Back to top](#top)

---

<a id="field-semantics"></a>

## Field semantics

| Field | Current role | What it does not prove |
|---|---|---|
| `id` | Stable receipt identifier matching the schema pattern. | It does not prove uniqueness, persistence, or deterministic derivation across implementations. |
| `run_id` | Opaque identifier supplied by the runtime caller. | It does not prove a corresponding log, trace, or model invocation exists. |
| `adapter` | Provider-neutral adapter identifier supplied by the caller or fixed by a bounded projection. | It is not an admitted-provider registry lookup or policy allow decision. |
| `model_ref` | Model/profile reference supplied by the caller. | It does not approve a model, pin weights, prove local/hosted execution, or verify provenance. |
| `inputs_digest` | SHA-256-shaped binding supplied for the bounded input set. | The current builder and validator do not calculate it or prove which bytes/canonicalization profile it covers. |
| `outputs_digest` | SHA-256-shaped binding supplied for the bounded output set. | It does not make output true, cited, safe, released, or byte-reproducible without a canonicalization profile. |
| `policy_decision_ref` | Opaque reference to the governing policy decision. | The current schema/validator do not resolve or authenticate the referenced object. |
| `citation_validation_ref` | Opaque reference to citation validation. | The current schema/validator do not resolve the report or prove that cited evidence supports the output. |
| `outcome` | One closed runtime outcome: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. | `ANSWER` does not itself authorize client display, release, or publication. |

### Reference-resolution rule

For trust-bearing use, `policy_decision_ref` and `citation_validation_ref` must resolve through governed repository/runtime interfaces to compatible, reviewable objects. A non-empty string is only local shape evidence. Until reference resolution and authority checks exist, the receipt remains a bounded candidate or process-memory record.

### Digest rule

The current validator and builder reject all-zero placeholder digests, but they do not define canonicalization. A future reproducible digest profile must specify, at minimum:

- the exact input/output object boundary;
- canonical serialization and character encoding;
- ordering and normalization rules;
- inclusion/exclusion of redacted or sensitive fields;
- algorithm/version identity;
- replay behavior when schemas evolve; and
- correction/supersession handling.

That profile is **PROPOSED** work. This page does not create it.

[Back to top](#top)

---

<a id="finite-outcome-vocabularies"></a>

## Finite outcome vocabularies

Two different closed vocabularies are present and must not be confused.

### AIReceipt runtime outcomes

| Receipt outcome | Bounded meaning | Required caution |
|---|---|---|
| `ANSWER` | The recorded AI-mediated event ended in an answer-like runtime outcome. | Receipt presence alone does not prove evidence, policy, citation, review, release, or client-display eligibility. |
| `ABSTAIN` | The governed path declined to answer. | The current receipt has no reason-code field; inspect the referenced validation/decision/envelope objects. |
| `DENY` | Policy or access posture denied the operation or exposure. | Sensitive denial details must remain controlled; do not echo protected inputs into receipt findings. |
| `ERROR` | The path failed safely. | Do not fall back to an ungoverned answer or silently reinterpret the failure as abstention. |

### Validator outcomes

The dedicated validator emits `PASS`, `FAIL`, or `ERROR` for its own bounded check:

| Validator outcome | Meaning |
|---|---|
| `PASS` | Schema shape and local consistency checks passed. |
| `FAIL` | The candidate was readable but violated schema or local semantic checks. |
| `ERROR` | The input could not be safely processed, for example duplicate keys, non-finite JSON, symlink input, unreadable input, or missing schema. |

`PASS` is not equivalent to `ANSWER`, policy allow, evidence closure, review approval, release, or publication.

[Back to top](#top)

---

<a id="candidate-construction"></a>

## Candidate construction

### Generic candidate builder

[`packages/envelopes/src/envelopes/ai_receipt.py`](../../../packages/envelopes/src/envelopes/ai_receipt.py) provides `build_ai_receipt_candidate(...)`.

**CONFIRMED behavior:**

- accepts every current schema field explicitly;
- requires non-empty string values for runtime identity and refs;
- enforces the `id` and SHA-256 string patterns;
- rejects all-zero digest placeholders;
- enforces the four receipt outcomes;
- returns exactly the nine schema fields; and
- performs no network or model call.

**Explicit non-effects:**

- does not calculate either digest;
- does not resolve evidence, policy, or citations;
- does not validate a provider or model;
- does not persist the candidate;
- does not select public-answer eligibility;
- does not promote, release, deploy, or publish.

### MockAdapter projection

[`packages/envelopes/src/envelopes/mock_adapter_receipt.py`](../../../packages/envelopes/src/envelopes/mock_adapter_receipt.py) projects one prevalidated MockAdapter response into an AIReceipt candidate by:

- reading only `response_envelope["outcome"]`;
- fixing `adapter` to `mock`;
- fixing `model_ref` to `fixture-only`; and
- forwarding caller-supplied digests and authority references to the generic builder.

It does not invoke `MockAdapter`, validate the source response envelope, bind the output digest to response bytes, or create runtime/persistence authority.

### Construction rule

A successful builder return means only that local constructor guards passed. The candidate must still pass the authoritative schema and dedicated validator at the trust boundary, and every authority-bearing reference must be resolved by its owning subsystem before consequential use.

[Back to top](#top)

---

<a id="target-governed-flow"></a>

## Target governed flow

The intended composition is broader than the currently proven builder/validator slice:

```text
caller request
  -> scope, release, evidence, rights, sensitivity and policy precheck
  -> minimized admissible model request
  -> provider-neutral adapter
  -> untrusted structured candidate
  -> output-shape, citation, precision, freshness and policy postcheck
  -> finite RuntimeResponseEnvelope
  -> caller supplies exact refs and canonical digests
  -> AIReceipt candidate builder
  -> AIReceipt schema + bounded validator
  -> reference resolution and authority checks                 [HOLD]
  -> durable receipt persistence and access controls           [HOLD]
  -> correction, supersession, retention and replay support    [HOLD]
```

### Current proof boundary

| Step | Current state |
|---|---|
| Closed AIReceipt schema | **CONFIRMED present / PROPOSED profile** |
| Local candidate construction | **CONFIRMED bounded implementation** |
| Mock outcome projection | **CONFIRMED bounded implementation** |
| Strict no-network shape/local validator | **CONFIRMED implementation** |
| Synthetic fixture and focused test proof | **CONFIRMED repository surfaces** |
| Provider-neutral runtime orchestration | **HOLD / no verified composed path** |
| Policy-decision resolution | **HOLD** |
| Citation-validation resolution | **HOLD** |
| Canonical digest calculation | **HOLD** |
| Runtime emission | **HOLD** |
| Durable persistence/query | **HOLD** |
| Client/public projection | **DENY by default until governed release criteria exist** |

The receipt must remain downstream of evidence and policy. It cannot repair a missing upstream gate by recording that the gate was skipped.

[Back to top](#top)

---

<a id="object-family-boundaries"></a>

## Object-family boundaries

| Object | Owns | AIReceipt relationship |
|---|---|---|
| `EvidenceBundle` | Claim-support evidence, provenance, scope, and source authority. | AIReceipt does not replace or embed it; generated language remains subordinate to evidence. |
| `PolicyDecision` | Admissibility, access, sensitivity, and obligations. | AIReceipt stores only a ref; it does not decide or authenticate policy. |
| Citation-validation result | Whether cited support resolves and supports answer posture. | AIReceipt stores only a ref; it does not validate citations. |
| `RuntimeResponseEnvelope` | Client-facing finite outcome, reason posture, citations, and safe response context under its contract. | AIReceipt is audit/process memory, not the response envelope. |
| Model/provider output | Untrusted candidate language or structure. | AIReceipt may bind an output digest but does not make output authoritative. |
| `RunReceipt` / other process receipts | Accountability for other execution families. | Keep receipt subclasses/families distinct; do not relabel a non-AI process merely because AI assisted authoring. |
| `GENERATED_RECEIPT` | Repository-authoring provenance for AI-authored tracked artifacts. | Separate object family and schema; it is not runtime `AIReceipt`. |
| Proof object | Verifiable support for a bounded claim or transition. | AIReceipt can be referenced as process lineage, never substituted for proof. |
| Release/correction/rollback records | Govern public state, withdrawal, supersession, and recovery. | AIReceipt cannot promote, release, correct, withdraw, or roll back by itself. |
| Logs and telemetry | Operational traces and diagnostics under retention/security policy. | `run_id` may link to them where allowed, but the current profile does not prove linkage. |

### Classification rule

Classify by **what was governed**, not by which tool appeared in the workflow:

- model-mediated runtime event → candidate for `AIReceipt`;
- repository AI authoring → `GENERATED_RECEIPT`;
- data transform → transform/run receipt family;
- validation run → validation receipt/report family;
- release transition → release decision/manifest/receipt family.

A pipeline-build receipt does not become `AIReceipt` merely because AI helped write the pipeline.

[Back to top](#top)

---

<a id="data-minimization-and-security"></a>

## Data minimization and security

### Allowed current payload

Only the nine schema fields belong in the current AIReceipt object. Values should be minimized, opaque where practical, and safe for the receipt's access class.

### Forbidden content

Do not place any of the following in AIReceipt:

- raw prompts, system prompts, hidden instructions, or chain-of-thought;
- provider request/response bodies or answer text;
- credentials, tokens, endpoint secrets, infrastructure internals, or private URLs;
- raw evidence rows, unpublished source excerpts, or canonical/internal-store payloads;
- living-person private data, DNA/genomic material, exact rare-species locations, archaeology coordinates, infrastructure detail, or other protected precision;
- policy denial details that would reveal the restricted fact;
- full exception traces, request headers, environment variables, or filesystem paths;
- unsigned review, release, or publication claims disguised as receipt metadata.

### Safe-error behavior

The current validator reports finding codes and JSON-pointer paths rather than candidate values. It also:

- rejects symbolic-link inputs;
- limits input size and finding count;
- rejects duplicate keys and non-standard non-finite numbers;
- rejects malformed/non-UTF-8 JSON and non-object roots;
- rejects blank required refs/identity fields; and
- rejects all-zero placeholder digests.

Those defenses reduce accidental disclosure. They do not replace threat modeling, authorization, encryption, retention policy, or incident response for any future receipt store.

### Public boundary

Normal public clients must not read `data/receipts/ai/` or any future internal receipt store directly. A public-safe projection, when justified, must expose only the minimum released metadata through a governed API and must remain subordinate to evidence, policy, correction, and release state.

[Back to top](#top)

---

<a id="validation-and-proof"></a>

## Validation and proof

### Current fixture inventory

Repository inventory at the evidence snapshot confirms:

- two positive JSON fixtures under `valid/`;
- three negative JSON fixtures under `invalid/`; and
- expected-error sidecars for the negative fixtures.

Some adjacent fixture README prose still describes the earlier one-positive/one-negative inventory. Current directory bytes and the dedicated source map are stronger evidence for the present count; that documentation drift is outside this file's change scope.

### Dedicated validator scope

[`tools/validators/validate_ai_receipt.py`](../../../tools/validators/validate_ai_receipt.py) proves only:

- safe local JSON ingestion;
- Draft 2020-12 schema conformance;
- non-empty configured identity/reference strings;
- rejection of all-zero digest placeholders;
- deterministic, payload-safe finding output; and
- valid/invalid fixture polarity.

Its serialized result explicitly sets `authority_created` to `false` and identifies the scope as `ai-receipt-shape-and-local-consistency-only`.

### Focused proof files

| Proof surface | What it verifies |
|---|---|
| [`tests/validators/test_validate_ai_receipt.py`](../../../tests/validators/test_validate_ai_receipt.py) | Fixture polarity, blank-ref and zero-digest failures, duplicate-key/non-finite handling, symlink denial, and payload-safe output. |
| [`tests/packages/envelopes/test_ai_receipt_candidate.py`](../../../tests/packages/envelopes/test_ai_receipt_candidate.py) | All four outcomes, deterministic exact-key construction, invalid-field rejection, zero-digest rejection, schema alignment, repository-validator integration, and absence of authority/payload fields. |
| [`tests/packages/envelopes/test_mock_adapter_ai_receipt_candidate.py`](../../../tests/packages/envelopes/test_mock_adapter_ai_receipt_candidate.py) | Mock outcome projection, fixed mock identity, source-response immutability, safe rejection, and preservation of explicit digests/refs. |
| [`.github/workflows/ai-receipt.yml`](../../../.github/workflows/ai-receipt.yml) | Path-scoped, no-network fixture validation plus generated-receipt integrity for the validator closure slice. |

### Reproducible commands

```bash
python -m pytest -q tests/validators/test_validate_ai_receipt.py
python tools/validators/validate_ai_receipt.py --fixtures

PYTHONPATH=packages/envelopes/src \
  python -m pytest -q \
  tests/packages/envelopes/test_ai_receipt_candidate.py

PYTHONPATH=packages/envelopes/src:. \
  python -m pytest -q \
  tests/packages/envelopes/test_mock_adapter_ai_receipt_candidate.py
```

### What passing checks do not establish

Passing all commands above does not establish:

- evidence resolution or factual correctness;
- policy authorization or citation sufficiency;
- digest canonicalization or semantic coverage;
- model/provider approval or a real model call;
- runtime emission, persistence, retention, signing, or access control;
- client rendering, release, correction propagation, rollback, or publication.

[Back to top](#top)

---

<a id="persistence-retention-and-access"></a>

## Persistence, retention, and access

[`data/receipts/ai/README.md`](../../../data/receipts/ai/README.md) documents an AI receipt family lane and two documented domain sublanes. That is **documentation evidence only**.

### Current posture

| Concern | Status |
|---|---|
| Logical receipt family under `data/receipts/` | **CONFIRMED documented** |
| Final subtype/domain directory grammar | **NEEDS VERIFICATION** |
| Actual runtime AIReceipt instances under the lane | **UNKNOWN** |
| Runtime emitter | **HOLD / no verified implementation** |
| Durable store or query API | **HOLD** |
| Access-control policy | **HOLD** |
| Encryption/key management | **HOLD** |
| Retention and deletion schedule | **HOLD** |
| Public-safe projection | **DENY by default / HOLD** |
| Signing or attestation | **HOLD** |

### Required persistence properties before adoption

A future operational store should not be considered complete until it has:

- one accepted logical owner and physical-storage contract;
- append-only or explicitly versioned mutation rules;
- deterministic or collision-resistant identity policy;
- bounded payload size and safe serialization;
- access classes and least-privilege read/write paths;
- encryption and secret-management posture where applicable;
- retention, legal hold, correction, withdrawal, and deletion rules;
- reference-resolution and orphan detection;
- integrity verification and backup/restore evidence;
- audit logging that does not leak sensitive content; and
- a public boundary that denies direct receipt-store access.

This page does not select a database, object-store layout, monthly directory scheme, signature system, or retention period.

[Back to top](#top)

---

<a id="correction-supersession-and-replay"></a>

## Correction, supersession, and replay

### Historical integrity

A receipt should record what occurred at a particular accountability boundary. Corrections should not silently rewrite historical receipt bytes merely to make a past event appear compliant.

### Proposed correction pattern

A future governed correction path should:

1. preserve the original receipt or its immutable digest;
2. emit a separate correction, supersession, invalidation, or withdrawal reference;
3. identify the affected `id`, `run_id`, output digest, policy/citation refs, and downstream response/release objects;
4. propagate stale/withdrawn state through governed APIs, caches, indexes, maps, stories, and AI surfaces where relevant;
5. preserve the reason at the appropriate access class; and
6. record a rollback or recovery target when public state was affected.

This pattern is **PROPOSED**. No current AIReceipt-specific correction schema or propagation proof was established.

### Replay limits

Current code can deterministically rebuild a candidate from identical explicit inputs. That is not full replay. End-to-end replay requires verified:

- canonical input/output serialization;
- exact adapter/model/profile identity;
- evidence, policy, citation, prompt/configuration, and release snapshots;
- deterministic or bounded-nondeterministic runtime posture;
- compatible contract/schema versions; and
- preserved correction/supersession state.

A matching digest proves byte equality for the selected object boundary; it does not prove factual correctness or policy legitimacy.

[Back to top](#top)

---

<a id="operational-maturity-and-holds"></a>

## Operational maturity and HOLDs

### Confirmed bounded implementation

- strict proposed runtime schema;
- semantic contract documentation;
- two valid and three invalid fixtures;
- deterministic no-network validator and focused tests;
- path-scoped hosted workflow;
- exact-key candidate builder and focused tests;
- MockAdapter outcome projection and focused tests;
- generated authoring receipts that bind the validator and builder slices.

### HOLD — required before operational receipt use

- accepted architecture/contract decision or explicit maintained proposed-profile posture;
- canonical input/output digest profile;
- resolvable policy-decision and citation-validation contracts plus runtime resolvers;
- admitted provider/model/profile identity governance;
- composed governed-AI route and runtime orchestration;
- AIReceipt emitter integrated after finite outcome selection;
- durable storage, access control, retention, backup, and query behavior;
- correction, invalidation, supersession, and stale-state propagation;
- incident-response and security review;
- signing/attestation decision and verification path, if required;
- end-to-end tests that prove no raw prompt, chain-of-thought, secret, restricted evidence, or protected precision enters the receipt;
- release review for any public-safe receipt projection; and
- independent human review appropriate to the consequence.

### UNKNOWN

- whether any deployed environment currently emits a shape-compatible AIReceipt;
- whether external systems consume `id` or `run_id` values;
- whether any physical receipt store exists outside the repository;
- whether retention, signing, or audit obligations apply in a target deployment; and
- whether future schema evolution must preserve compatibility with persisted records.

[Back to top](#top)

---

<a id="anti-patterns"></a>

## Anti-patterns

| Anti-pattern | Why it fails | Required response |
|---|---|---|
| Treating `outcome=ANSWER` as public authorization | The receipt does not prove evidence, policy, citation, review, release, or client-display eligibility. | Resolve governing objects and fail closed. |
| Adding speculative fields directly to receipt instances | `additionalProperties: false` makes them invalid and creates schema drift. | Propose contract/schema evolution with fixtures, validators, tests, and migration analysis. |
| Storing raw prompts or chain-of-thought | Expands privacy/security exposure and mistakes hidden reasoning for evidence. | Store only minimized refs/digests in approved objects. |
| Using non-empty refs as proof of resolution | Current validator checks strings, not target objects or authority. | Resolve refs through governed interfaces. |
| Using hash shape as proof of correct binding | A digest can match the wrong or ambiguously serialized bytes. | Adopt a canonicalization profile and verify semantic scope. |
| Relabeling every AI-assisted process receipt as AIReceipt | Collapses object families and loses the actual governed event. | Classify by process responsibility. |
| Treating validator `PASS` as evidence or policy approval | Validator scope is shape/local consistency only. | Keep validation, evidence, policy, proof, and release separate. |
| Writing directly to a public receipt endpoint | Exposes internal process memory and may leak sensitive metadata. | Deny direct public access; use governed, released projections only. |
| Mutating a historical receipt after correction | Erases audit lineage. | Preserve history and emit separate correction/supersession state. |
| Claiming signing, retention, or replay is implemented from architecture prose | No current implementation evidence establishes those controls. | Keep them on HOLD until tested artifacts and runtime evidence exist. |

[Back to top](#top)

---

<a id="change-discipline-and-rollback"></a>

## Change discipline and rollback

### Field or semantic changes

A change to any of the nine fields, their meaning, patterns, outcome vocabulary, or additional-property posture is not a documentation-only change. It must reconcile at least:

- `contracts/runtime/ai_receipt.md`;
- `schemas/contracts/v1/runtime/ai_receipt.schema.json`;
- valid and invalid fixtures;
- `tools/validators/validate_ai_receipt.py`;
- candidate builders and imports;
- focused tests and workflow paths;
- persisted-record compatibility and migration, if any;
- policy/citation/reference-resolution behavior;
- correction and rollback; and
- architecture and operator documentation.

Accepted Directory Rules still apply. Do not create a second AIReceipt contract, schema, policy, receipt, or proof home to avoid a migration.

### Rollback for this documentation revision

Before merge, close the draft pull request and delete the feature branch. After an authorized merge, revert the documentation commit and remove its generated authoring receipt, or restore prior blob `df65d7b33d359c6721378caaf1e2933c240a9ef3`.

Rollback affects explanatory documentation and authorship provenance only. It does not change runtime, policy, evidence, schema, candidate builders, validator behavior, persisted receipts, release, deployment, or publication state.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Limit |
|---|---|---|---|
| Prior `AI_RECEIPTS.md` blob | **CONFIRMED stale/truncated** | Existing path, prior themes, and need for same-path repair. | Its speculative fields and implementation claims are not current authority. |
| [`contracts/runtime/ai_receipt.md`](../../../contracts/runtime/ai_receipt.md) | **CONFIRMED present / PROPOSED** | Semantic purpose, boundaries, and schema pairing. | Does not prove operational runtime emission. |
| [`ai_receipt.schema.json`](../../../schemas/contracts/v1/runtime/ai_receipt.schema.json) | **CONFIRMED** | Exact nine-field closed machine grammar. | Status remains proposed; shape alone creates no authority. |
| Fixture directories | **CONFIRMED inventory** | Two valid and three invalid cases at the evidence snapshot. | Synthetic coverage does not prove production data. |
| [`validate_ai_receipt.py`](../../../tools/validators/validate_ai_receipt.py) | **CONFIRMED implementation** | Safe local parsing, schema validation, local semantic checks, finite validator results. | No reference resolution, policy/citation authentication, or runtime authority. |
| [`test_validate_ai_receipt.py`](../../../tests/validators/test_validate_ai_receipt.py) | **CONFIRMED tests** | Hostile-input and fixture-profile proof. | Test presence is not a current hosted run result for this docs-only branch. |
| [`ai-receipt.yml`](../../../.github/workflows/ai-receipt.yml) | **CONFIRMED workflow** | Dedicated no-network validation for its listed paths. | This architecture page is not in its path filter. |
| [`envelopes.ai_receipt`](../../../packages/envelopes/src/envelopes/ai_receipt.py) | **CONFIRMED bounded implementation** | Deterministic exact-key candidate construction. | Does not compute digests or resolve authority refs. |
| [`envelopes.mock_adapter_receipt`](../../../packages/envelopes/src/envelopes/mock_adapter_receipt.py) | **CONFIRMED bounded implementation** | Copies a prevalidated mock outcome with fixed synthetic identity. | Does not invoke or validate MockAdapter or bind response bytes. |
| Package tests | **CONFIRMED tests** | Four-outcome, deterministic, schema, validator, and safe-failure proof. | Do not establish composed runtime. |
| [`data/receipts/ai/README.md`](../../../data/receipts/ai/README.md) | **CONFIRMED documentation** | Logical receipt-family intent and no-public-path boundary. | Does not prove emitted instances, final layout, retention, access, signing, or integration. |
| [`ADR-0019`](../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md) | **CONFIRMED proposed** | Decision proposal and bounded current architecture context. | Not accepted authority. |
| [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **CONFIRMED accepted** | Placement authority and responsibility-root separation. | Does not adopt AIReceipt semantics or runtime use. |
| Current-session inspection | **CONFIRMED bounded** | Repository-grounded status in this document. | No live runtime, provider, store, deployment, release, or public client was exercised. |

[Back to top](#top)

---

<a id="related-documents"></a>

## Related documents

### Governed-AI architecture

- [Subsystem README](./README.md)
- [Adapter contract architecture](./ADAPTER_CONTRACT.md)
- [Trust boundaries](./BOUNDARIES.md)
- [Focus flow](./FOCUS_FLOW.md)
- [Mock-first posture](./MOCK_FIRST.md)
- [Route map](./ROUTE_MAP.md)

### Authoritative and executable surfaces

- [AIReceipt semantic contract](../../../contracts/runtime/ai_receipt.md)
- [AIReceipt machine schema](../../../schemas/contracts/v1/runtime/ai_receipt.schema.json)
- [AIReceipt fixtures](../../../fixtures/contracts/v1/runtime/ai_receipt/README.md)
- [AIReceipt validator](../../../tools/validators/validate_ai_receipt.py)
- [Validator tests](../../../tests/validators/test_validate_ai_receipt.py)
- [Candidate builder](../../../packages/envelopes/src/envelopes/ai_receipt.py)
- [Mock projection](../../../packages/envelopes/src/envelopes/mock_adapter_receipt.py)
- [Candidate-builder tests](../../../tests/packages/envelopes/test_ai_receipt_candidate.py)
- [Mock-projection tests](../../../tests/packages/envelopes/test_mock_adapter_ai_receipt_candidate.py)
- [Dedicated workflow](../../../.github/workflows/ai-receipt.yml)
- [Documented AI receipt data lane](../../../data/receipts/ai/README.md)

### Governance

- [ADR-0019 — proposed adapter and finite-envelope decision](../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md)
- [ADR-0029 — accepted Directory Rules v2 adoption](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Directory Rules v2](../../doctrine/directory-rules.md)

[Back to top](#top)
