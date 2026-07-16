<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runtime-pipelines-readme
title: runtime/pipelines/ — Runtime-to-Pipeline Coordination Boundary
type: readme
version: v0.2
status: draft; repository-grounded; compatibility-index; path-canonicality-conflicted; readme-only; implementation-unconfirmed; schema-paired-runtime-contracts-proposed; ci-unproved; non-authoritative
owners: OWNER_TBD — Runtime steward · Pipeline steward · Pipeline-spec steward · Evidence steward · Policy steward · Rights reviewer · Sensitivity reviewer · Security steward · Receipt steward · Validation steward · Release steward · CI steward · Docs steward
created: 2026-07-05
updated: 2026-07-15
supersedes: v0.1 runtime pipeline handoff guide
policy_label: "public-doctrine; runtime; pipelines; handoff; readme-only; no-executable-pipeline-logic; no-spec-authority; no-network-by-default; minimized-context; evidence-gated; policy-gated; deterministic-identity; finite-outcomes; receipt-aware; retry-safe; no-lifecycle-promotion; no-release-authority; no-public-path; no-secrets; rollback-aware"
current_path: runtime/pipelines/README.md
truth_posture: CONFIRMED target v0.1 README, runtime root v0.2, pipelines root v0.2, pipeline_specs root v0.2, runtime envelope helper README, descriptive FocusRequest adapter note, schema-paired draft/PROPOSED DecisionEnvelope, RuntimeResponseEnvelope, and AIReceipt contracts, pipeline receipt parent README, draft RunReceipt standard, Directory Rules, runtime/release compatibility-index precedent, and bounded absence of selected runtime-pipeline implementation, tests, workflows, and RunReceipt schemas / PROPOSED minimized runtime handoff profile, deterministic identity, caller-level result mapping, retry and cancellation controls, receipt linkage, tests, CI, correction, migration, and rollback / CONFLICTED runtime/pipelines path presence versus omission from the Directory Rules canonical runtime sublane tree; schema-confirmed four-outcome runtime envelopes versus broader caller-level pipeline blocker states; FocusRequest descriptive note versus no verified canonical request contract; RunReceipt doctrine versus proposed field/schema/layout posture / UNKNOWN accepted owners, lane retention, caller allowlist, runtime-pipeline request contract, implementation path, adapters, pipeline-specific receipt subtype, network profile, resource budgets, tests, CI, deployment, consumers, and runtime health / NEEDS VERIFICATION placement ADR or migration note, contract adoption, caller mapping, gate implementation, receipt layout, test collection, substantive CI, correction, migration, and rollback automation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 64cf41a5c5370e72123c487f6946f8c08f85e5b1
  prior_blob: b92695b3226e747b856d0d0685b3885b143b13c6
  runtime_root_blob: c8a0854af5c6ac4854ad5dcc880eb81251a211c3
  pipelines_root_blob: 9fb38acf5a67ca43608617d73a273d06f5f84db5
  pipeline_specs_root_blob: 3a6599898606126604298a281de53e39fdba98ce
  runtime_envelopes_blob: 74350a241ce2a50cac1a4825b961c0356ded4216
  adapter_contract_note_blob: e371e5ca008ecbd0775bea9c2a31ef76131e7575
  decision_envelope_contract_blob: b5120a208910f5e2907874b03af1fc8c7f43363d
  runtime_response_envelope_contract_blob: b81d67dccdd8470e066ab8247eb93c5df67a6679
  ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
  decision_envelope_schema_blob: 349782c8760f77e432ed1e9239d5ddc2ffe1f9b8
  runtime_response_envelope_schema_blob: 5105d419432a27176a8ee10870d75400cfa2ab8c
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  runtime_release_compatibility_readme_blob: ddfde419d5e47568b169431bbf2950d3521cc602
  pipeline_receipts_readme_blob: 6b714cd3b1501d61a83a9d52c82f7887f6c3b368
  run_receipt_standard_blob: 144f6a153ba9223a617e2718bca3e161bf24e605
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - runtime/pipelines/__init__.py was not found
    - runtime/pipelines/handoff.py was not found
    - runtime/pipelines/runner.py was not found
    - runtime/pipelines/orchestrator.py was not found
    - tests/runtime/pipelines/README.md was not found
    - tests/runtime/test_pipelines.py was not found
    - tests/runtime/README.md was not found
    - .github/workflows/pipeline-gate.yml was not found
    - .github/workflows/runtime-pipelines.yml was not found
    - .github/workflows/pipeline-runtime.yml was not found
    - .github/workflows/runtime-test.yml was not found
    - schemas/contracts/v1/receipts/run_receipt.v1.schema.json was not found
    - schemas/contracts/v1/receipts/run_receipt.schema.json was not found
    - contracts/runtime/decision_envelope.md and its paired schema exist with draft/PROPOSED status
    - contracts/runtime/runtime_response_envelope.md and its paired schema exist with draft/PROPOSED status
    - contracts/runtime/ai_receipt.md and its paired schema exist with draft/PROPOSED status
    - the paired runtime schemas close additional properties and confirm ANSWER, ABSTAIN, DENY, and ERROR outcomes
    - no canonical runtime-pipeline request contract was verified; FocusRequest remains descriptive in the adapter note
    - Directory Rules' canonical runtime sublane tree does not list pipelines/; path retention is unresolved
    - commit search for runtime/pipelines surfaced the README-introduction commit and no later path-specific implementation commit
related:
  - ../README.md
  - ../model_adapters/README.md
  - ../model_adapters/AdapterContract.md
  - ../envelopes/README.md
  - ../mock/README.md
  - ../local/README.md
  - ../release/README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../data/receipts/pipeline/README.md
  - ../../contracts/runtime/decision_envelope.md
  - ../../contracts/runtime/runtime_response_envelope.md
  - ../../contracts/runtime/ai_receipt.md
  - ../../schemas/contracts/v1/runtime/decision_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - ../../schemas/contracts/v1/runtime/ai_receipt.schema.json
  - ../../docs/standards/RUN_RECEIPT.md
  - ../../docs/doctrine/directory-rules.md
  - ../../contracts/
  - ../../schemas/
  - ../../policy/
  - ../../fixtures/
  - ../../tests/
  - ../../tools/validators/
  - ../../data/
  - ../../release/
tags: [kfm, runtime, pipelines, runtime-pipeline-handoff, minimized-context, finite-outcomes, receipts, evidence, policy, rights, sensitivity, retries, idempotency, cancellation, observability, no-network, no-publication, correction, rollback]
notes:
  - "This revision changes only runtime/pipelines/README.md."
  - "The lane is README-only; no runtime-pipeline implementation, test suite, dedicated workflow, canonical request contract, pipeline-specific receipt subtype, or deployment is established."
  - "Executable logic stays in pipelines/ and declarative intent stays in pipeline_specs/."
  - "Runtime support is optional and interpretive. It cannot create evidence, validate domain truth, promote lifecycle state, approve release, or publish."
  - "DecisionEnvelope, RuntimeResponseEnvelope, and AIReceipt have canonical contract/schema homes but remain draft/PROPOSED; FocusRequest and the runtime-pipeline request shape remain unverified, and RunReceipt field/schema/layout posture remains partly proposed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Runtime-to-Pipeline Coordination Boundary

`runtime/pipelines/`

> Repository-present boundary for documenting and eventually implementing tightly governed runtime support requested by executable KFM pipelines. Current evidence establishes this README and adjacent draft/PROPOSED schema-paired runtime envelope contracts—not a runtime-pipeline module, accepted runtime-pipeline request contract, approved adapter path, collected test suite, substantive CI gate, receipt emitter, deployment, or operational service.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-README--only-lightgrey)
![pipeline logic](https://img.shields.io/badge/pipeline__logic-pipelines%2F-blue)
![spec authority](https://img.shields.io/badge/spec__authority-pipeline__specs%2F-blue)
![network](https://img.shields.io/badge/network-DENIED__by__default-critical)
![lifecycle](https://img.shields.io/badge/lifecycle-NO__PROMOTION-red)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Quick links:** [Purpose](#purpose) · [Evidence](#status-and-evidence) · [Authority](#authority-and-directory-rules-basis) · [Split](#runtime-pipeline-spec-and-data-split) · [Invariants](#keystone-invariants) · [Eligibility](#caller-and-use-case-eligibility) · [Input](#proposed-handoff-input-contract) · [Minimization](#context-minimization-and-data-handling) · [Identity](#identity-determinism-and-replay) · [Gates](#evidence-policy-rights-and-sensitivity-gates) · [Execution](#runtime-selection-execution-and-resources) · [Retries](#timeouts-retries-cancellation-and-idempotency) · [Outcomes](#finite-outcomes-and-pipeline-mapping) · [Receipts](#receipts-observability-and-audit) · [Lifecycle](#lifecycle-release-and-publication-separation) · [Placement](#placement-contract) · [Tests](#tests-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Validation](#validation-commands) · [Rollback](#rollback-correction-deprecation-and-migration)

> [!IMPORTANT]
> **This README is not implementation proof.** Proposed fields, outcomes, helpers, tests, workflows, receipt subtypes, and thresholds remain `PROPOSED` until backed by accepted contracts, schemas, code, fixtures, test results, workflow evidence, and runtime receipts.

> [!CAUTION]
> **Runtime support is not pipeline authority.** It may help classify, summarize, compare, explain, or surface blockers. It may not define pipeline intent, replace executable pipeline logic, create an EvidenceBundle, satisfy validation merely by returning successfully, or change lifecycle or release state.

> [!WARNING]
> **Generated output is never sovereign evidence.** Factual pipeline decisions must resolve governed evidence. Fluent output without resolvable support is non-authoritative review material and must be rejected, held, denied, or ignored.

---

<a id="purpose"></a>

## Purpose

This README governs the narrow boundary where executable pipeline code may request runtime support without creating a parallel pipeline implementation or bypassing KFM governance.

Candidate uses include bounded interpretation over governed evidence, steward-review summaries, proposed classifications requiring later validation, operator-facing reason explanations, and deterministic mock behavior in tests.

This lane must not become:

- an alternate pipeline runner or spec registry;
- a source connector or lifecycle store;
- canonical contract, schema, policy, receipt, proof, or release authority;
- an unrestricted prompt service or hidden public API;
- a mechanism for generated text to close evidence, validation, review, promotion, or publication gates.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

| Surface | Status | Safe conclusion |
|---|---:|---|
| This README | **CONFIRMED v0.1 before revision** | A handoff guide existed. |
| Direct implementation | **NOT FOUND at checked paths** | No selected module, runner, orchestrator, or handoff implementation is established. |
| Dedicated tests | **NOT FOUND at checked paths** | No selected runtime-pipeline test lane is established. |
| Dedicated workflow | **NOT FOUND at checked paths** | No selected workflow proves gates, retries, receipts, or failure behavior. |
| Runtime root | **CONFIRMED v0.2** | Runtime is subordinate execution support. |
| `pipelines/` root | **CONFIRMED v0.2** | Owns executable pipeline logic—the **how**. |
| `pipeline_specs/` root | **CONFIRMED v0.2** | Owns declarative intent—the **what**. |
| Runtime contracts and schemas | **CONFIRMED schema-paired; draft/PROPOSED** | `DecisionEnvelope`, `RuntimeResponseEnvelope`, and `AIReceipt` have canonical homes and closed schemas; adoption, validators, runtime wiring, and CI remain unproved. |
| Pipeline receipt parent | **CONFIRMED draft README** | Receipt process-memory posture exists; subtype layout and emitted instances remain unresolved. |
| RunReceipt standard | **CONFIRMED draft standard** | Doctrine is strong; canonical field set, schema, and layout remain partly proposed. |

Truth labels:

- **CONFIRMED** — verified from current repository evidence or generated validation.
- **PROPOSED** — design requiring implementation and review.
- **CONFLICTED** — competing names, outcomes, layouts, or authority claims.
- **UNKNOWN** — runtime or operational state not established.
- **NEEDS VERIFICATION** — checkable before reliance but unresolved.

This revision does not establish an accepted runtime-pipeline request API, adopted envelope version, pipeline-specific receipt subtype, caller allowlist, live adapter, network access, implementation, test collection, CI enforcement, deployment, service health, lifecycle behavior, or release readiness.

[Back to top](#top)

---

<a id="authority-and-directory-rules-basis"></a>

## Authority and Directory Rules basis

Directory Rules organize by responsibility:

| Responsibility | Owning root | This lane's role |
|---|---|---|
| Runtime coordination | `runtime/` | May own narrow reusable handoff mechanics after acceptance. |
| Executable pipeline logic | `pipelines/` | Decides whether runtime support is needed and how results affect a run. |
| Declarative pipeline intent | `pipeline_specs/` | Declares profiles, sources, gates, receipt expectations, and failure posture. |
| Meaning and shape | `contracts/`, `schemas/` | Own accepted contracts and schemas. |
| Policy and admissibility | `policy/` | Own allow, deny, restrict, hold, and review decisions. |
| Tests and validators | `fixtures/`, `tests/`, `tools/validators/` | Prove behavior. |
| Lifecycle and trust objects | `data/` | Own lifecycle state, receipts, proofs, and artifacts. |
| Release and reversal | `release/` | Own release, correction, withdrawal, and rollback. |
| Public surfaces | accepted app/package roots | Use governed APIs and released artifacts, not runtime internals. |

**CONFLICTED:** the path exists and is indexed by `runtime/README.md`, but the Directory Rules canonical runtime sublane tree does not list `pipelines/`. Treat it as a compatibility/discovery boundary until a placement decision is recorded.

**NEEDS VERIFICATION:** retain it as a narrow coordination lane, or consolidate the behavior into caller code under `pipelines/`, generic adapters under `runtime/model_adapters/`, and envelope helpers under `runtime/envelopes/`.

Until resolved, do not duplicate runners, specs, contracts, schemas, policies, receipts, tests, or public APIs here.

[Back to top](#top)

---

<a id="runtime-pipeline-spec-and-data-split"></a>

## Runtime, pipeline, spec, and data split

```text
pipeline_specs/ says WHAT should run
pipelines/      says HOW the governed step runs
runtime/        supplies bounded optional execution support
contracts/      define meaning
schemas/        define valid shape
policy/         decides what is allowed
fixtures/tests  prove behavior
receipts/       remember what happened
proofs/         support claims
release/        decides publication and rollback
```

Allowed direction:

```text
accepted spec
  -> executable pipeline
  -> caller-side evidence/policy/sensitivity gates
  -> minimized runtime request
  -> approved adapter or deterministic mock
  -> finite result
  -> caller-side validation and deterministic mapping
  -> receipt-ready facts or receipt reference
  -> blocker, support material, no-op, or review handoff
  -> lifecycle and release decisions remain outside runtime
```

Disallowed:

```text
runtime prompt -> pipeline spec
runtime answer -> validation pass or EvidenceBundle
runtime success -> lifecycle promotion
runtime summary -> release approval
runtime output -> public truth
```

[Back to top](#top)

---

<a id="keystone-invariants"></a>

## Keystone invariants

1. Runtime never changes `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED` state.
2. The caller owns pipeline semantics and all side effects.
3. Evidence and policy outrank runtime output.
4. Context is minimized and purpose-limited.
5. Network, file-system, shell, tool, and secret access are denied by default.
6. Results are finite and machine-validated; free text alone is invalid.
7. Timeouts, denials, abstentions, invalid output, cancellation, and dependency failures remain visible.
8. Retries preserve logical identity and never duplicate side effects.
9. Runtime cannot approve release, correct, withdraw, or roll back.
10. Public clients never read runtime internals directly.
11. Material handoffs remain auditable, correctable, and reversible.
12. Deterministic code is preferred whenever it can perform the task.

[Back to top](#top)

---

<a id="caller-and-use-case-eligibility"></a>

## Caller and use-case eligibility

A future caller should provide:

- pipeline run or dry-run identity;
- accepted spec reference/digest or explicit N/A;
- executable reference and commit;
- bounded operation, domain, geography, time, and lifecycle context;
- resolved source/evidence refs where facts matter;
- policy, rights, sensitivity, sovereignty, access, freshness, correction, and release context;
- expected result profile;
- timeout, retry, cancellation, and resource limits;
- deterministic caller mapping;
- receipt or audit plan.

Eligible uses are interpretive and reversible: review summaries, bounded comparisons, candidate labels requiring later validation, safe blocker explanations, and deterministic mocks.

Denied uses include arbitrary source fetches, missing-evidence generation, policy or rights decisions, deterministic parser replacement, public free-form prompt execution, private chain-of-thought, direct publication, and irreversible side effects.

[Back to top](#top)

---

<a id="proposed-handoff-input-contract"></a>

## Proposed handoff input contract

No canonical runtime-pipeline request object or schema was verified. `DecisionEnvelope`, `RuntimeResponseEnvelope`, and `AIReceipt` exist as draft/PROPOSED schema-paired output/accountability contracts, but they do not define this handoff input. The fields below are a **PROPOSED checklist**, not an API.

| Field group | Minimum content |
|---|---|
| Identity | `handoff_id`, `pipeline_run_id`, attempt/parent IDs, correlation IDs. |
| Caller | pipeline spec ref/digest, executable ref/commit, domain and lifecycle scope. |
| Operation | accepted operation profile and expected result profile. |
| Support | source refs, evidence refs, policy/rights/sensitivity/review refs. |
| Payload | minimized contracted input and canonical digest. |
| Execution | adapter profile, allowed tools, network profile or N/A, timeout and resource profile. |
| Resilience | retry policy, cancellation token/ref, idempotency posture. |
| Audit | receipt context, correction/supersession state, safe trace context. |

Reject or hold when the caller, spec, executable, scope, support refs, profiles, limits, result shape, or idempotency posture is missing or when direct promotion/publication is expected.

[Back to top](#top)

---

<a id="context-minimization-and-data-handling"></a>

## Context minimization and data handling

Allowed context is limited to reviewed excerpts, resolved evidence summaries, access-authorized fields, validation findings, bounded candidates, safe reason text, and deterministic fixtures.

Denied by default:

- full canonical-store or RAW/QUARANTINE dumps;
- credentials, cookies, tokens, private endpoints, or signing material;
- private chain-of-thought or model internals;
- sensitive coordinates without approved need and policy;
- Tribal/cultural material without sovereignty review;
- private living-person, genomic, medical, or landowner material without authorization;
- arbitrary file-system, shell, plugin, or URL access.

Logs may contain stable IDs, safe reason codes, digests, durations, resource counters, profile refs, and outcome class. They must not contain secrets, protected payloads, sensitive prompts, private chain-of-thought, or reconstruction clues for restricted locations or identities.

[Back to top](#top)

---

<a id="identity-determinism-and-replay"></a>

## Identity, determinism, and replay

```text
logical handoff identity =
  pipeline run + spec digest + executable commit
  + operation/adapter profiles + minimized input digest
  + source/evidence/policy state + resource profile
  + retry lineage + correction state
```

Candidate determinism classes:

| Class | Use |
|---|---|
| `DETERMINISTIC` | Byte-stable result; eligible for machine comparison after validation. |
| `SEEDED_BOUNDED` | Seed/version pinned; review or deterministic post-validation required. |
| `NONDETERMINISTIC_REVIEW_ONLY` | Human review material only. |
| `UNREPLAYABLE` | Hold or abstain for consequential use. |

Replay preserves the original attempt and records versions, parameters, input/output digests, evidence/policy refs, validators, receipt linkage, reason for replay, and comparison. It never overwrites history.

[Back to top](#top)

---

<a id="evidence-policy-rights-and-sensitivity-gates"></a>

## Evidence, policy, rights, and sensitivity gates

| Gate | Fail-safe handling |
|---|---|
| Missing scope/spec/executable identity | Reject. |
| Unresolved source or evidence support | Abstain or hold. |
| Policy/access denial | Deny. |
| Unclear rights | Deny, quarantine, or hold. |
| Sensitivity/sovereignty uncertainty | Generalize, quarantine, deny, or hold. |
| Living-person/privacy uncertainty | Deny or hold. |
| Stale, withdrawn, or corrected evidence | Abstain or require corrected refs. |
| Direct release/publication expectation | Reject. |

Runtime may verify gate references and return blockers. It may not turn missing authority into an allow decision.

[Back to top](#top)

---

<a id="runtime-selection-execution-and-resources"></a>

## Runtime selection, execution, and resources

Selection rules:

1. Prefer deterministic code.
2. Prefer deterministic mock fixtures in tests.
3. Use only reviewed operation and adapter profiles.
4. Pin adapter, model/runtime, tools, and versions.
5. Deny unknown fallback adapters and silent model upgrades.
6. Keep provider responses behind normalized, validated result profiles.
7. Require a caller-owned fallback: no-op, abstain, hold, deterministic substitute, or human review.

Default controls:

- no network;
- temporary working space only;
- no lifecycle/release writes;
- no secret discovery or arbitrary shell;
- no dynamic installation or unbounded tool recursion;
- bounded CPU, memory, tokens, bytes, tool calls, retries, concurrency, disk, logs, time, and cost.

An approved network profile must pin destinations, methods, redirects, private-address denial, authentication source, TLS, byte/decompression limits, content types, timeouts, retries, rate/concurrency, logging/redaction, and revocation path.

Resource exhaustion returns a finite failure or hold state, never disguised partial success.

[Back to top](#top)

---

<a id="timeouts-retries-cancellation-and-idempotency"></a>

## Timeouts, retries, cancellation, and idempotency

- Timeouts are bounded and visible.
- Hidden work must stop after cancellation.
- Partial output is rejected unless explicitly contracted and validated.
- Retry only classified transient failures, preserve the logical handoff ID, record attempt lineage, and re-check freshness/policy.
- Never retry policy/rights denial, invalid shape, unresolved evidence, unapproved drift, cancellation, non-idempotent effects, or changed correction/release state without review.

Runtime handoff code must not directly write lifecycle state, emit duplicate receipts, apply corrections, publish notifications, mutate catalog/triplets, approve release, or trigger rollback. The caller owns any side effect after validation.

[Back to top](#top)

---

<a id="finite-outcomes-and-pipeline-mapping"></a>

## Finite outcomes and pipeline mapping

The paired `DecisionEnvelope`, `RuntimeResponseEnvelope`, and `AIReceipt` schemas confirm the closed runtime outcome set `ANSWER | ABSTAIN | DENY | ERROR`. Those schemas are still `PROPOSED`, and their presence does not prove adoption or runtime behavior.

Pipeline states such as `HOLD`, `NEEDS_REVIEW`, `QUARANTINE`, and `NO_OP` remain **caller-owned mappings**, not additional runtime-envelope outcomes. Free text alone is invalid.

Proposed caller mapping:

| Runtime outcome | Caller-owned pipeline mapping |
|---|---|
| `ANSWER` | Treat as `SUPPORTED` only after deterministic validation and all caller gates; otherwise hold/review. |
| `ABSTAIN` | Block the claim, use an approved deterministic fallback, or request review. |
| `DENY` | Stop; preserve safe denial reasons and obligations. |
| `ERROR` | Retry only when classified safe; otherwise hold or fail. |
| No runtime call | Caller may record `NO_OP`; this is not an envelope outcome. |
| Sensitive/ambiguous result | Caller may route to `NEEDS_REVIEW` or `QUARANTINE`; these are lifecycle/review states, not runtime outcomes. |

Minimum result facts should include handoff/attempt IDs, finite class, reason codes, profiles, output/digest, refs actually used, gate states, validators, resource counters, retryability, partial flag, receipt facts/ref, correction state, and safe diagnostics.

Caller-side validation verifies the expected profile, IDs, profiles, size limits, leak checks, support refs, gate states, known outcome/reasons, partial state, output digest, deterministic mapping, no prohibited side effect, and receipt posture.

[Back to top](#top)

---

<a id="receipts-observability-and-audit"></a>

## Receipts, observability, and audit

`AIReceipt` now has a canonical draft/PROPOSED contract and paired closed schema for AI-mediated events. RunReceipt doctrine still requires auditable process memory for consequential governed operations, but no canonical runtime-pipeline receipt subtype or accepted RunReceipt schema/layout was verified.

This lane may return AIReceipt-ready facts when AI mediation occurs, generic receipt-ready facts, or a reference to a receipt emitted by an accepted runner. It must not persist receipts directly, create a parallel receipt authority, or silently select final subtype/layout.

Receipt-ready facts should cover:

- handoff/attempt and parent pipeline IDs;
- spec digest and executable commit;
- operation, adapter, model/runtime, and parameter refs;
- input/output digests;
- source/evidence/policy/rights/sensitivity refs;
- timestamps, duration, resources, outcome, reasons, validators;
- retry/cancellation and correction lineage;
- actor/runner identity and safe error classification.

Safe observability includes timestamps, outcomes, reason counters, latency, sizes, resources, versions, validation failures, denials, stale/correction blockers, retries, and duplicate suppression. Observability is not proof or receipt authority and must avoid sensitive/high-cardinality labels.

Audit must answer who requested the handoff, which run/spec/code it supported, what minimized input and support refs applied, which runtime ran, what result was returned, how it was validated/mapped, whether retries/cancellation occurred, where process memory lives, and what correction/rollback path applies.

[Back to top](#top)

---

<a id="lifecycle-release-and-publication-separation"></a>

## Lifecycle, release, and publication separation

```text
runtime result
  != source admission or RAW capture
  != normalization receipt or ValidationReport
  != EvidenceBundle or catalog/triplet closure
  != release readiness or approval
  != published artifact
  != correction or rollback decision
```

After validation, the caller may add non-authoritative review material, add a blocker, request deterministic validation, route to review, select a pre-approved deterministic branch, abstain/no-op, or prepare receipt-ready facts.

Runtime itself may not write lifecycle stores, emit release records, mark evidence resolved, approve policy/rights, alter review state, publish any API/UI/map/search/graph/notification/answer output, or execute correction/rollback.

[Back to top](#top)

---

<a id="placement-contract"></a>

## Placement contract

May belong here after acceptance:

- provider-neutral runtime-to-pipeline coordination helpers;
- context minimization and safe serialization;
- handoff/attempt identity and digests;
- timeout, cancellation, retry, and idempotency helpers;
- finite-result normalization and output validation;
- receipt-ready fact builders without persistence;
- safe trace/metric helpers;
- handoff documentation and migration notes.

Does not belong here:

| Material | Correct home |
|---|---|
| Domain/lifecycle pipeline logic | `pipelines/` |
| Specs, schedules, and gate configuration | `pipeline_specs/` |
| General model/provider adapters | `runtime/model_adapters/` or accepted adapter lane |
| Canonical meaning and schemas | `contracts/`, `schemas/` |
| Policy decisions | `policy/` and accepted decision homes |
| Source access | `connectors/` |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` |
| Lifecycle data, receipts, proofs | accepted `data/` homes |
| Release/correction/rollback records | `release/` |
| Public API/UI code | accepted application/package roots |
| Secrets or generated output treated as authority | nowhere |

Placement test:

> A file belongs here only when it implements reusable runtime coordination needed by multiple pipeline callers and cannot be owned more clearly by an established responsibility root.

[Back to top](#top)

---

<a id="tests-fixtures-and-ci"></a>

## Tests, fixtures, and CI

No dedicated suite, fixture lane, or workflow was verified at the checked paths.

Minimum future tests — **PROPOSED**:

- import safety and no network/secret/side effect;
- caller authorization and profile pinning;
- context minimization;
- evidence/policy/rights/sensitivity/sovereignty/freshness gates;
- network allowlist and resource limits;
- timeout, cancellation, retry, duplicate suppression, and idempotency;
- adapter/model drift;
- malformed, oversized, partial, or leaking output;
- finite outcome mapping;
- receipt-ready fact stability;
- no lifecycle promotion or release authority;
- logging safety, replay, nondeterminism, and failure injection.

Fixtures must be synthetic, minimized, redacted or approved, immutable, digest-pinned, purpose/rights/sensitivity labeled, secret-free, safe for repository use, and corrected by versioning rather than silent replacement.

Substantive CI should install cleanly, fail on zero tests, validate the pinned runtime envelope/AIReceipt schemas plus any accepted request contract, enforce no-network/import safety, run negative gates and resilience tests, scan leaks, verify lifecycle/release separation, validate receipt artifacts when required, emit machine-readable reports, and fail closed on missing prerequisites.

No current CI claim is made for runtime-pipeline collection, enforcement, receipts, deployment, or health.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

1. **Governance:** confirm lane retention, owners, canonical DTO/receipt homes, callers, operations, and no-network/side-effect defaults.
2. **Contract slice:** adopt pinned versions of the relevant runtime envelope/AIReceipt contracts, define and accept the runtime-pipeline request contract, one operation profile, deterministic fixtures, caller mapping, reasons/obligations, and receipt facts.
3. **Safety harness:** implement minimization, validation, timeout/cancellation/retry/idempotency, and no lifecycle/release writes.
4. **Mock integration:** connect one pipeline dry run to a deterministic mock and prove negative evidence/policy paths.
5. **Reviewed adapter:** add one pinned approved adapter with network/resource/observability controls and review-only nondeterminism.
6. **Operational admission:** add substantive CI, receipt validation, incident/revocation/correction/rollback procedures, and public-path separation.

A proposed future tree may include `handoff.py`, `context.py`, `identity.py`, `outcomes.py`, `validation.py`, `retries.py`, `receipts.py`, and `observability.py`, plus `tests/runtime/pipelines/`. These paths are not repository facts and require placement review before creation.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

This documentation revision is done when it accurately records README-only maturity, preserves authority boundaries, does not canonize proposed DTOs/receipts, defines fail-safe controls, separates proposals from facts, and provides validation and rollback posture.

A future implementation is done only when:

- [ ] lane and owners are accepted;
- [ ] contracts/schemas and callers/operations are accepted;
- [ ] clean install/import and no-network/no-side-effect behavior are proven;
- [ ] minimization and all evidence/policy/sensitivity gates fail closed;
- [ ] finite results and reasons validate;
- [ ] retries/cancellation/idempotency and leak safety are tested;
- [ ] receipt-ready facts or receipts validate;
- [ ] no lifecycle or release authority is proven;
- [ ] substantive CI fails on zero tests or missing artifacts;
- [ ] drift, incident, correction, deprecation, migration, and rollback procedures are tested.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| Area | Open verification |
|---|---|
| Placement | Retain, consolidate, or deprecate this lane; assign owners. |
| Contracts | Runtime-pipeline request contract; adopted DecisionEnvelope/RuntimeResponseEnvelope/AIReceipt versions; reasons, obligations, and caller mappings. |
| Callers | Authorized pipeline lanes, operations, and fallback behavior. |
| Support | Evidence/source refs, policy decisions, rights, sensitivity, sovereignty, privacy, freshness, and correction rules. |
| Execution | Approved adapters/runtimes, version pinning, injection controls, network destinations, resource budgets, timeouts, retries, idempotency, and cancellation. |
| Output | Partial/size policy, deterministic replay, validation, safe diagnostics, and public-safe mapping. |
| Receipts | Receipt subtype, layout, emitter, validators, and audit retention. |
| Tests | Fixture authority, negative coverage, no-promotion/no-release tests, collection, reports, and workflow. |
| Operations | Observability, restricted diagnostics, SLOs, incident response, revocation, correction, migration, and rollback automation. |

[Back to top](#top)

---

<a id="validation-commands"></a>

## Validation commands

Guidance only until implementation and test collection are established:

```bash
find runtime/pipelines runtime/model_adapters runtime/envelopes \
  pipelines pipeline_specs -maxdepth 5 -type f 2>/dev/null | sort

find contracts schemas policy fixtures tests tools/validators \
  data/receipts data/proofs release -maxdepth 6 -type f 2>/dev/null | sort

git grep -nE 'FocusRequest|DecisionEnvelope|RuntimeResponseEnvelope|AIReceipt|RunReceipt' -- \
  runtime pipelines pipeline_specs contracts schemas policy tests fixtures data docs

python -m pytest -q tests/runtime/pipelines
```

Future CI must fail when implementation is claimed but tests are absent/zero, network denial is not enforced, required contracts/schemas or negative tests are missing, receipts required by the profile are absent, or lifecycle/release mutation is observed.

[Back to top](#top)

---

<a id="rollback-correction-deprecation-and-migration"></a>

## Rollback, correction, deprecation, and migration

This change is documentation-only. Before merge, close or abandon the review branch. After merge, transparently revert the merge or restore the prior blob recorded above.

Future implementation rollback must support disabling operation/adapters/network profiles, cancelling work, preventing retries, suppressing duplicate effects, invalidating/superseding affected refs, routing runs to hold/review, restoring deterministic fallback, and preserving audit history.

Corrections are append-only: identify affected scope, issue a superseding version, revalidate affected handoffs/receipts, notify owning stewards when consequential, and preserve rollback targets.

Deprecation or lane migration requires an ADR or migration note, destination ownership, caller inventory, write freeze, contract/schema/test/fixture/receipt continuity, removal validation, and a reversible compatibility period.

---

**Current conclusion:** `runtime/pipelines/` is a repository-present, README-only compatibility and coordination boundary whose canonicality remains unresolved. It may eventually host narrowly reusable runtime handoff mechanics, but it is not pipeline logic, spec authority, evidence, policy, validation, receipt storage, lifecycle state, release authority, or a public interface.

<p align="right"><a href="#top">Back to top</a></p>
