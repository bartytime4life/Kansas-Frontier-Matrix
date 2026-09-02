<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0019-ai-adapter-contract-and-finite-envelopes
title: ADR-0019 — AI Adapter Contract and Finite Envelopes
type: adr
adr_id: ADR-0019
version: v1.3
status: draft
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture stewardship"
  - "NEEDS VERIFICATION — governed API and governed-AI/runtime stewardship"
  - "NEEDS VERIFICATION — evidence, policy, citation, security, contracts, schemas, validation, correction, and release stewardship"
reviewers_required:
  - Architecture steward
  - Governed API steward
  - Runtime / governed-AI steward
  - Evidence and citation steward
  - Policy and sensitivity steward
  - Security and privacy reviewer
  - Contracts and schemas stewards
  - Validation and CI stewards
  - Correction and release stewards
  - Docs steward
created: 2026-05-09
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f8a0466f6bd246dcf69b88e507efca267e6e5b67
  target_prior_blob: c0bc41cc11b40b1ee87a838a3e80024a2da56c04
  adr_index_blob: 938c5894c36b99e14810918e2c550ab0e92d53b1
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  adr_0008_blob: 7eeae617986d053699da66c0f5cd0df063902ef7
  model_adapters_readme_blob: cfc7a0979ee64041cb93e8140ea514f6ed6e262f
  adapter_contract_note_blob: e371e5ca008ecbd0775bea9c2a31ef76131e7575
  mock_adapter_blob: 04d37e59b14c9e3b85126cb3380b6221b44e26d1
  mock_adapter_proof_blob: be1b1d2b4178b30ce9be754671a2c42271ad91bc
  ollama_adapter_blob: 1769a719d6a6df53e001abbc4c67ad486ab5c944
  governed_api_main_blob: bcc8d3a0ddba4b225e962b594d548819df0cbb71
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 5d7c137d2e78ddfca35a1356a96333ac2e84952b
  decision_envelope_contract_blob: b5120a208910f5e2907874b03af1fc8c7f43363d
  runtime_response_contract_blob: 97ff95ba5527968f3db70cd710682176444e4cde
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  runtime_response_builder_blob: 5dacededc1bda64292259ba39b6387facafbd1e8
  precision_profile_blob: 0a8e43ce3c3a08f253ac720572c866c21b54dd7f
  finite_envelope_proof_blob: 70ca80226bf06c3b28b59096e3812312a00c03b6
  runtime_response_valid_abstain_blob: 87a405408dc8d5ec0d6c789a9584e0a6b62b3c59
  runtime_response_valid_answer_blob: aa41e425597204f3e1902f649a091ffc72a2c29d
  runtime_response_valid_deny_blob: c56865b9441fb305340221fd240d9b641f5390ac
  runtime_response_valid_error_blob: 9197dbcdd978b9b90329f59061cfd6bd916dc1ff
  ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ai_receipt_validator_blob: eb80e77aed15f478c32215c8f773f308a87a092a
  runtime_policy_readme_blob: 80b63e7651429903385066b53c7fb41af3cd1298
  runtime_policy_abstain_blob: 9c66097140933eba5aa7011653da12488035ad99
  runtime_policy_public_deny_blob: 8d46a90088c046c102b991904e56ecf32d8ae7d3
  runtime_policy_evidence_blob: 297bd7999bf19c4029bf92df6f1c2f07477c787d
  runtime_policy_receipt_blob: 5fa096c9d65183b0b3333e05434bbf6f2ab9c0b7
  focus_mock_workflow_blob: fbd56c7cda991ff8f3b804cc0c278e62daaa7abf
inspection_boundary: >
  Current-session GitHub reads over the exact target, canonical ADR index, accepted
  Directory Rules decision and adopted doctrine, adjacent ADR-0008, runtime adapter
  lane and implementations, governed API source, runtime contracts and schemas,
  deterministic envelope builder, precision profile, fixtures, validators, runtime
  proof suites, AIReceipt validator, runtime policy scaffolds, and Focus mock workflow.
  No model daemon, provider endpoint, credential, live evidence resolver, policy
  evaluator, citation service, receipt store, deployed API, public client, production
  ruleset, or release environment was exercised.
related:
  - docs/adr/README.md
  - docs/adr/INDEX.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - docs/adr/ADR-0016-telemetry-redaction-posture.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/doctrine/directory-rules.md
  - docs/architecture/directory-rules.md
  - docs/architecture/governed-ai/README.md
  - docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - docs/architecture/governed-ai/AI_RECEIPTS.md
  - docs/architecture/governed-ai/MOCK_FIRST.md
  - docs/architecture/governed-ai/OLLAMA_INTEGRATION.md
  - apps/governed-api/README.md
  - apps/governed-api/src/governed_api/main.py
  - apps/governed-api/src/governed_api/routes/registry.py
  - apps/governed-api/src/governed_api/stub.py
  - runtime/model_adapters/README.md
  - runtime/model_adapters/AdapterContract.md
  - runtime/model_adapters/MockAdapter.py
  - runtime/model_adapters/OllamaAdapter.py
  - runtime/model_adapters/mock/README.md
  - runtime/ollama/README.md
  - contracts/runtime/decision_envelope.md
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/precision_actually_used.md
  - contracts/runtime/ai_receipt.md
  - schemas/contracts/v1/runtime/decision_envelope.schema.json
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - packages/envelopes/src/envelopes/runtime_response.py
  - fixtures/contracts/v1/runtime/runtime_response_envelope/
  - tools/validators/validate_runtime_response_envelope.py
  - tools/validators/validate_ai_receipt.py
  - tests/runtime_proof/test_envelope_finite_outcomes.py
  - tests/runtime_proof/test_mock_adapter_finite_outcomes.py
  - tests/runtime_proof/README.md
  - policy/runtime/README.md
  - policy/runtime/abstain_on_missing_evidence.rego
  - policy/runtime/deny_unpublished_public.rego
  - policy/runtime/evidence_required.rego
  - policy/runtime/run_receipt.rego
  - .github/workflows/focus-mock-test.yml
  - .env.example
tags: [kfm, adr, governed-ai, model-adapter, provider-neutral, finite-outcomes, decision-envelope, runtime-response-envelope, precision-disclosure, ai-receipt, mock-first, cite-or-abstain, trust-membrane, no-direct-model-client]
notes:
  - "v1.3 is a same-path documentation-only evidence refresh. Source status remains draft and effective decision status remains proposed."
  - "Accepted ADR-0029 and docs/doctrine/directory-rules.md govern placement. The legacy architecture copy remains a compatibility dependency, not the writable authority."
  - "MockAdapter.py is now an executable deterministic no-I/O selector for prevalidated synthetic envelopes, and repository-owned tests cover all four finite outcomes. It is not a semantic adapter, evidence resolver, policy engine, provider runtime, or receipt emitter."
  - "RuntimeResponseEnvelope now has four-outcome fixtures, an ANSWER-only precision profile, a deterministic candidate builder, and bounded proof tests. Contract prose, schema/profile, package documentation, and governed route integration are not fully converged."
  - "AIReceipt has a local validator, but runtime emission, persistence, reference resolution, retention, and correction propagation are not established."
  - "OllamaAdapter.py remains a one-line placeholder; runtime Rego remains non-enforcing scaffold source; the Governed API has no AI-mediated route; mock Focus remains held."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0019 — AI Adapter Contract and Finite Envelopes

> **Proposed decision.** Every model or provider remains behind one provider-neutral adapter boundary. Adapter output stays internal to governed orchestration. Public and semi-public clients receive only a governed finite `RuntimeResponseEnvelope` through the Governed API, after evidence, policy, citation, precision, freshness, correction, and release checks appropriate to the operation. Generated language remains interpretation, never authority.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0019-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Directory Rules: accepted](https://img.shields.io/badge/Directory%20Rules-v2%20accepted-2da44e?style=flat-square)](#current-repository-evidence)
[![MockAdapter: bounded selector](https://img.shields.io/badge/MockAdapter-bounded%20selector-2da44e?style=flat-square)](#current-implementation-maturity)
[![Finite envelopes: four-outcome proof](https://img.shields.io/badge/finite%20envelopes-four--outcome%20proof-2da44e?style=flat-square)](#current-implementation-maturity)
[![Governed API: ABSTAIN scaffold](https://img.shields.io/badge/governed%20API-ABSTAIN%20scaffold-f59e0b?style=flat-square)](#current-implementation-maturity)
[![Live provider: none admitted](https://img.shields.io/badge/live%20provider-none%20admitted-6e7781?style=flat-square)](#current-implementation-maturity)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity and placement are confirmed; acceptance is not.** The canonical ADR index uniquely assigns `ADR-0019` to this file with source metadata `draft` and effective status `proposed`. Accepted ADR-0029 makes `docs/doctrine/directory-rules.md` the writable Directory Rules authority. Neither fact accepts this decision, admits a model, activates a runtime, or proves a governed AI route.

> [!CAUTION]
> **The bounded MockAdapter proof is not a model integration.** `MockAdapter.py` now selects deep-copied, prevalidated synthetic envelopes for all four finite outcomes without network, files, clocks, randomness, tools, or secrets. It does not interpret a request, select an outcome semantically, resolve evidence, evaluate policy, validate citations, call a provider, assemble an AIReceipt, or serve a client.

> [!WARNING]
> **A model response is never the public contract.** Browsers, map shells, review tools, exports, and other clients must not call Ollama or another provider directly, render raw provider output or streams, infer evidence or policy from prose, or treat a model result, schema pass, receipt, workflow, pull request, merge, or deployment as release or publication authority.

**Quick navigation:** [Status](#status) · [Evidence](#evidence-boundary) · [Context](#context) · [Decision](#decision) · [Objects](#object-and-vocabulary-boundaries) · [Adapter](#provider-neutral-adapter-boundary) · [Flow](#governed-runtime-flow) · [Outcomes](#finite-outcomes) · [Security](#security-privacy-and-prompt-injection) · [Receipts](#receipts-observability-and-retention) · [Authority](#authority-and-publication-boundary) · [Current evidence](#current-repository-evidence) · [Maturity](#current-implementation-maturity) · [Convergence](#implementation-and-convergence-plan) · [Acceptance](#acceptance-gates) · [Consequences](#consequences) · [Alternatives](#alternatives-considered) · [Risks](#risk-and-open-question-ledger) · [Rollback](#rollback-and-supersession) · [Verification](#verification-checklist) · [References](#references)

---

<a id="status"></a>

## Status

| Field | Current value |
|---|---|
| **ADR ID** | `ADR-0019` — unique and confirmed in [`INDEX.md`](./INDEX.md) |
| **Tracked path** | `docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md` |
| **Source metadata** | `draft` |
| **Effective decision status** | `proposed` |
| **Record edition** | `v1.3` — repository-evidence refresh; proposed decision preserved |
| **Decision class** | Provider-neutral model boundary, governed orchestration, finite runtime envelopes, precision disclosure, AI accountability, public-client isolation, and reversible provider deactivation |
| **Current repository maturity** | Bounded executable selector, candidate builder, validators, fixtures, and proof tests; no accepted semantic adapter contract, governed AI route, active runtime policy, admitted provider, or public AI release |
| **Implementation effect of this revision** | Documentation and generated provenance only |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Acceptance and graduation are separate transitions

1. **ADR acceptance** would approve the provider-neutral boundary, responsibility split, finite outcome vocabulary, mock-first posture, no-direct-client rule, and provider-admission discipline.
2. **Component graduation** would prove one bounded implementation responsibility, such as deterministic fixture selection or candidate construction.
3. **Governed runtime graduation** would require composed evidence resolution, policy execution, citation validation, structured output, AIReceipt emission, complete RuntimeResponseEnvelope assembly, consumer enforcement, correction, and rollback.
4. **Provider admission** would approve one exact provider/model/profile for named data classes, capabilities, network posture, and limits.
5. **Public release** would require separate reviewed release evidence for the exact route and operation.

A component can graduate without the ADR being accepted. An ADR can be accepted without a runtime being operational. A provider call, valid envelope, green workflow, pull request, merge, or deployment cannot collapse these transitions.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in repository bytes inspected at `main@f8a0466f6bd246dcf69b88e507efca267e6e5b67`.

### Truth labels

| Label | Meaning in this ADR |
|---|---|
| **CONFIRMED** | Verified from current repository bytes, contracts, schemas, tests, workflow source, validators, or exact readback |
| **PROPOSED** | Decision, semantic rule, field, profile, migration, or implementation target not accepted or operationally proved |
| **NEEDS VERIFICATION** | A concrete check remains before relying on the claim |
| **UNKNOWN** | The inspected surfaces do not resolve the state |
| **CONFLICTED** | Current tracked surfaces make incompatible claims or expose competing profiles |
| **HELD** | Current automation or governance intentionally prevents a maturity claim while preserving bounded checks |

### Maturity ladder

| Level | Meaning | Current posture |
|---|---|---|
| **1. Doctrine and responsibility boundaries** | ADRs, Directory Rules, trust-membrane docs, runtime-lane docs, and object-family prose | **CONFIRMED broad; ADR-0019 remains proposed** |
| **2. Shape and bounded component proof** | Paired schemas, fixtures, validators, deterministic candidate builder, no-I/O selector, and standard-library tests | **CONFIRMED partial and substantive** |
| **3. Semantic orchestration proof** | Accepted adapter request/response contract, semantic outcome selection, evidence/policy/citation composition, AIReceipt emission | **HELD / not established** |
| **4. Governed consumer proof** | Authenticated Governed API route, complete envelope, public-client enforcement, no raw/provider leakage, correction propagation | **HELD / not established** |
| **5. Admitted provider and release-significant operation** | Reviewed provider/model profile, secure deployment, observed operation, release, incident response, rollback | **UNKNOWN / not established** |

### Inspected surfaces

- canonical ADR index, accepted ADR-0029, and adopted Directory Rules v2;
- adjacent ADR-0008 and the prior ADR-0019 bytes;
- canonical runtime model-adapter lane and descriptive adapter note;
- bounded `MockAdapter.py`, one-line `OllamaAdapter.py`, and selector proof;
- Governed API WSGI app, route registry, and ABSTAIN scaffold;
- `DecisionEnvelope`, `RuntimeResponseEnvelope`, `precision_actually_used`, and `AIReceipt` contracts/schemas;
- deterministic RuntimeResponseEnvelope candidate builder;
- four-outcome valid fixtures, invalid fixtures, validators, and standard-library proof suites;
- AIReceipt validator and proposed receipt contract;
- runtime policy documentation and four non-enforcing Rego scaffolds;
- Focus mock workflow, including its bounded finite-envelope job and explicit mock-Focus hold.

### What this evidence proves

It proves that current repository bytes include:

- a documented canonical provider-neutral adapter lane;
- an executable deterministic no-I/O scenario selector;
- four finite valid RuntimeResponseEnvelope fixture outcomes;
- bounded shape, alias, precision, fixture-polarity, selector, isolation, and no-I/O tests;
- a deterministic candidate builder with ANSWER-only evidence and precision checks;
- a schema-bound `precision_actually_used` profile;
- a local AIReceipt shape and consistency validator;
- a minimal Governed API whose registered GET routes fail closed with deterministic scaffolds;
- workflow source that runs the bounded selector and envelope suites.

### What this evidence does not prove

It does not prove:

- an accepted provider-neutral invocation contract or canonical `ModelAdapterRequest`/`ModelAdapterResponse`;
- semantic outcome selection by a model adapter;
- a functioning Ollama or remote-provider adapter;
- a running model daemon, installed model, or admitted provider/model profile;
- evidence retrieval or `EvidenceRef -> EvidenceBundle` closure in an AI path;
- executable runtime policy, obligation enforcement, or policy bundle identity;
- claim-to-evidence citation validation;
- prompt-injection resistance across a composed runtime;
- AIReceipt emission, persistence, reference resolution, retention, or correction propagation;
- Governed API assembly of the current complete RuntimeResponseEnvelope;
- authentication, authorization, rate limiting, egress controls, or deployed model isolation;
- repository-wide direct-client denial across code, dependencies, generated bundles, proxies, and deployment;
- release, publication, or production readiness.

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM treats AI as an interpretive capability, not a truth source. Evidence, source authority, policy, review, release state, correction lineage, and rollback support outrank generated language.

The architecture needs a stable provider-neutral boundary because model systems differ in request shape, output shape, streaming, tools, embeddings, model discovery, health reporting, errors, rate limits, context limits, usage metadata, rights, and deployment posture. Allowing those differences to leak into public contracts would couple KFM trust semantics to a provider.

KFM also carries several envelope-like objects. Without explicit boundaries, implementers can accidentally:

- return raw provider output as a client payload;
- let a fixture selector masquerade as semantic orchestration;
- conflate a policy decision with a client-facing runtime response;
- treat an AI receipt as proof that an answer is true;
- infer supported precision from map zoom, formatting, model confidence, or requested resolution;
- let an adapter decide evidence closure, rights, sensitivity, or release state;
- translate every negative state into generic text;
- create competing envelope schemas in runtime-, Focus-, package-, or UI-specific homes;
- store private prompts, sensitive context, provider diagnostics, or reasoning traces in receipts;
- make a loopback or hosted model endpoint reachable from browsers;
- advertise a green bounded test as operational governed AI.

### Forces

| Force | Architectural pressure |
|---|---|
| Evidence outranks generation | AI remains downstream of resolvable support |
| Provider churn | Public and orchestration contracts remain provider-neutral |
| Finite failure | Unsupported, prohibited, and broken states remain distinct |
| Precision honesty | An ANSWER discloses actual evidence-supported precision, not requested or displayed precision |
| Public-client isolation | Clients consume governed envelopes, never provider traffic |
| Sensitive data | Context transfer is minimized and denied where authority is unclear |
| Deterministic CI | Mock-first proof must work without network, secrets, models, clocks, or randomness |
| Accountability | AI-mediated events are digest-bound without storing private reasoning |
| Correction and revocation | Prior responses and receipts remain traceable and invalidatable |
| Reversibility | Provider/model activation and route integration have explicit disable paths |
| No parallel authority | Contracts, schemas, policy, runtime, receipts, and release remain in their owning roots |

### Why bounded component proof matters

The repository has advanced beyond placeholder-only evidence. That improvement is material, but its boundary must stay visible:

```text
four-outcome fixtures
  -> deterministic selector
  -> closed candidate builder
  -> shape and precision tests
  != semantic outcome selection
  != evidence/policy/citation composition
  != governed route
  != provider admission
  != release
```

This ADR protects that distinction so each next implementation slice can be useful without overclaiming the system.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

KFM proposes the following coupled architecture.

### D1. Provider-neutral adapter

Every model runtime is accessed through one provider-neutral adapter boundary in the canonical runtime adapter lane. Provider-specific transport, authentication, streaming, model discovery, health, limits, and error translation remain behind that boundary.

The adapter is replaceable infrastructure. It is not:

- evidence or source authority;
- policy or citation authority;
- sensitivity, consent, or rights authority;
- review or release authority;
- publication authority;
- a public client contract.

### D2. Governed orchestration owns the outcome

The adapter returns a bounded internal execution result or error to governed orchestration. It must not independently decide that generated material is evidence-supported, policy-allowed, citation-valid, precise enough, fresh, correction-safe, releasable, or public-safe.

Governed orchestration owns the composed result and, when applicable, emits:

1. a `DecisionEnvelope` or equivalent internal normalized decision;
2. an `AIReceipt` for the AI-mediated event;
3. a client-facing `RuntimeResponseEnvelope`.

### D3. Public finite outcomes

The governed runtime boundary uses exactly:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

No fifth public outcome is introduced for `HOLD`, `REVIEW`, `PARTIAL`, `DEGRADED`, `QUARANTINE`, or provider-specific status. Those concepts belong in safe reason codes, obligations, review records, operational state, or correction state.

### D4. Mock first

The first executable proof remains deterministic, local, synthetic, no-network, no-secret, and fixture-driven.

The current `MockAdapter` satisfies only a bounded selector responsibility. A later semantic mock adapter must still prove request validation, explicit scenario semantics, safe outcome selection, evidence/policy/citation handoff, receipt behavior, and composed orchestration without hidden I/O.

### D5. No direct model traffic

Browsers and ordinary public clients call governed interfaces only. They must not:

- call Ollama, OpenAI-compatible endpoints, or another provider directly;
- receive provider credentials or endpoint locations;
- render raw provider responses or streams;
- use provider health or model discovery as a public capability API;
- infer access or truth from model availability.

### D6. No generated truth

Model output may assist bounded synthesis, classification, extraction, summarization, query rewriting, or drafting only within an admitted use case. It cannot establish:

- source authority or identity;
- evidence closure;
- rights, consent, or sensitivity;
- actual spatial, temporal, or attribute precision;
- policy result or obligation completion;
- review approval;
- release, correction, withdrawal, or rollback state;
- publication.

### D7. No private reasoning retention

Receipts and logs may store approved hashes, identifiers, timing, finite outcomes, safe reasons, model/adapter references, evidence and decision references, validation references, and safe diagnostics. They must not store private chain-of-thought, unrestricted scratchpads, credentials, raw secrets, or unrestricted provider payloads.

### D8. Provider and model admission

A provider/model/profile remains disabled until a reviewed admission record establishes:

- provider, model, profile, version, and digest identity;
- rights and terms posture;
- permitted data classes and audiences;
- network, egress, tool, and retrieval permissions;
- context, output, timeout, retry, rate, and concurrency limits;
- supported operations and structured-output profile;
- deterministic fixture and canary plan;
- logging, redaction, retention, and incident posture;
- deactivation, correction, and rollback procedure;
- accountable owner and review state.

### D9. Precision disclosure belongs to the governed envelope

An `ANSWER` must disclose the spatial, temporal, and attribute precision actually supported by the evidence and transforms when the accepted envelope profile requires it. Requested precision, map zoom, rendering resolution, formatting, interpolation, resampling, and model confidence cannot substitute.

Negative outcomes must not carry precision details that could leak protected or unsupported information.

### D10. Component evidence must not be promoted by implication

A selector, candidate builder, schema, fixture, validator, receipt, test, workflow, or successful provider call proves only its declared responsibility. Runtime, consumer, provider-admission, and release claims require composed evidence at those layers.

[Back to top](#top)

---

<a id="object-and-vocabulary-boundaries"></a>

## Object and vocabulary boundaries

### Object roles

| Surface | Role | Current repository state | Must not become |
|---|---|---|---|
| Provider request/response | Provider-specific wire format inside one adapter | **UNKNOWN / provider-dependent** | Public contract or governance decision |
| `ModelAdapterRequest` / equivalent | Provider-neutral invocation input | **NOT ESTABLISHED as canonical contract/schema** | Raw store dump, credential carrier, or public-client prompt |
| `ModelAdapterResponse` / equivalent | Internal execution result | **NOT ESTABLISHED as canonical contract/schema** | Public envelope, policy decision, or evidence proof |
| `MockAdapter` scenario matrix | Prevalidated synthetic finite-outcome examples | **CONFIRMED bounded selector input** | Semantic truth set or production response source |
| `DecisionEnvelope` | Internal finite decision, reasons, and obligations | **CONFIRMED PROPOSED contract/schema surface** | Public response or release decision by implication |
| `RuntimeResponseEnvelope` | Governed client-facing finite response posture | **CONFIRMED PROPOSED schema/profile, fixtures, builder, and proof** | Raw model output, payload store, or publication |
| `precision_actually_used` | ANSWER-only actual precision disclosure | **CONFIRMED PROPOSED schema-bound profile** | Confidence score, policy allow, or fitness approval |
| `AIReceipt` | Accountability metadata for an AI-mediated event | **CONFIRMED PROPOSED contract/schema and local validator** | Truth proof, reasoning store, or publication authority |
| `EvidenceBundle` | Evidence closure and inspectable support | Separate evidence authority | Generated summary |
| `PolicyDecision` | Policy result and obligations | Separate policy authority | Model preference |
| `PromotionDecision` / `ReleaseManifest` | Release-governance state | Separate release authority | Runtime response |

### Vocabulary split

| Vocabulary | Values | Owner | Meaning |
|---|---|---|---|
| Governed runtime outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Decision/envelope contracts and policy | Public or semi-public response posture |
| Adapter execution status | **PROPOSED controlled set**, such as `completed`, `failed`, `timed_out`, `cancelled`, `unavailable` | Adapter contract | Internal transport/execution state |
| Safe adapter error | Stable internal code, such as `TIMEOUT` or `OUTPUT_SCHEMA_INVALID` | Adapter implementation/contract | Input to orchestration; not public truth |
| Policy state | Accepted policy vocabulary | Policy authority | Admissibility and obligations |
| Freshness state | Accepted temporal/freshness vocabulary | Contract/policy authority | Whether support is usable for the operation |
| Correction state | Accepted correction/withdrawal vocabulary | Correction/release authority | Whether a prior result is current, corrected, withdrawn, or affected |
| Review state | Review-record vocabulary | Review authority | Human review progress |
| Release decision | Release contract vocabulary | Release authority | Promotion and public-state decision |

A provider outage, timeout, malformed structured output, schema-validation failure, or receipt-integrity failure normally supports `ERROR`. Insufficient evidence, unresolved citations, or unsupported scope normally supports `ABSTAIN`. Policy prohibition supports `DENY`.

### DecisionEnvelope versus RuntimeResponseEnvelope

The current Governed API scaffold emits fields compatible with a bounded `DecisionEnvelope` shape. The stronger client-facing `RuntimeResponseEnvelope` binds:

- stable identity, version, spec hash, and issuance time;
- one finite outcome and safe reason code;
- evidence references;
- policy, freshness, and correction state;
- `precision_actually_used` for `ANSWER` under the current proposed schema profile.

The mature composition remains:

```text
DecisionEnvelope
  + policy-safe response payload or safe non-answer
  + evidence / precision / freshness / correction posture
  -> RuntimeResponseEnvelope
```

This ADR does not silently collapse the two objects. A future convergence change must update contracts, schemas, fixtures, validators, builders, consumers, migration notes, and this ADR or a successor.

### RuntimeResponseEnvelope profile drift

Current repository evidence is not fully converged:

- the schema, precision profile, candidate builder, and proof tests implement `precision_actually_used`;
- the RuntimeResponseEnvelope contract prose still emphasizes the earlier ten-field surface;
- package documentation contains older scaffold assumptions;
- the Governed API emits a DecisionEnvelope-shaped subset, not the complete runtime envelope.

This is **CONFLICTED / HELD**, not permission to choose whichever profile is convenient. Producers and consumers must bind to one reviewed profile and version.

### AIReceipt relationship

`AIReceipt` records the AI execution boundary through adapter/model references, input/output digests, policy and citation-validation references, and finite outcome. A local validator now proves bounded shape and consistency behavior.

The receipt does not replace either envelope. Runtime emission, persistence, reference resolution, canonicalization, retention, correction lineage, and public-safe exposure remain unproved.

[Back to top](#top)

---

<a id="provider-neutral-adapter-boundary"></a>

## Provider-neutral adapter boundary

### Responsibility contract

An admitted adapter may support the following provider-neutral capabilities:

| Capability | Requirement |
|---|---|
| Structured generation | Produce schema-targeted internal output or a normalized adapter error |
| Embeddings | Optional and separately admitted for data class, retention, re-identification, and index policy |
| Health | Safe internal health state; never a public model endpoint |
| Model information | Auditable provider/model/profile identity without secrets |
| Capability discovery | Explicit supported operations; no implicit provider feature use |
| Cancellation and timeout | Bounded execution with deterministic failure mapping |
| Usage metadata | Optional safe accounting fields; never authority |
| Tool invocation | Denied by default; explicit tool adapter and policy required |
| Streaming | Buffered and terminated inside orchestration; no raw stream crosses the trust membrane |

The existence of a method name, provider SDK, or local daemon does not establish an admitted capability.

### Current bounded MockAdapter contract

The current selector:

- accepts a non-empty mapping of scenario IDs to prevalidated envelope mappings;
- requires all four finite outcomes;
- deep-copies registered scenarios and responses;
- returns scenario IDs in deterministic order;
- fails closed on malformed or incomplete matrices;
- fails safely for unknown scenarios without echoing the untrusted scenario value;
- imports only bounded standard-library surfaces;
- performs no file, network, model, clock, random, secret, or dynamic-execution access.

It does not:

- accept a canonical adapter request;
- evaluate scope or evidence;
- choose an outcome from policy or facts;
- validate the full envelope shape;
- call a model;
- emit a receipt;
- create a public response.

### Proposed request minimum

A future canonical adapter request should include or reference:

- request, run, trace, and operation identity;
- bounded use-case and context profile;
- evidence-support references;
- policy-decision reference;
- requested output schema and digest;
- model/provider profile reference;
- deterministic generation parameters where applicable;
- tool and network permissions;
- timeout and cancellation budget;
- sensitivity, rights, audience, purpose, freshness, and correction context;
- receipt, telemetry, and redaction posture.

It must not carry:

- provider credentials;
- unrestricted RAW, WORK, or QUARANTINE material;
- canonical/internal store dumps;
- private keys or tokens;
- unbounded tool access;
- instructions to persist private reasoning;
- public-client-controlled system policy.

### Proposed response minimum

A future canonical adapter response should include:

- adapter execution and correlation identity;
- provider/model/profile reference;
- normalized execution status;
- structured candidate output or safe absence;
- provider-neutral finish or failure category;
- timing and bounded usage metadata where allowed;
- output-schema validation state;
- safe diagnostics;
- input/output digest material needed by receipt assembly.

It must not claim:

- evidence resolution;
- citation validity;
- policy approval;
- precision authority;
- release approval;
- public safety;
- the final finite outcome without orchestration checks.

### Error normalization

Adapters translate provider failures into stable internal categories. Raw provider messages may contain prompts, context fragments, internal paths, hostnames, source details, or sensitive information and must not pass directly to clients.

Candidate internal categories include:

- `ADAPTER_UNAVAILABLE`;
- `MODEL_UNAVAILABLE`;
- `TIMEOUT`;
- `CANCELLED`;
- `CONTEXT_LIMIT`;
- `OUTPUT_SCHEMA_INVALID`;
- `TOOL_DENIED`;
- `RATE_LIMITED`;
- `PROVIDER_ERROR`;
- `CONFIGURATION_ERROR`.

[Back to top](#top)

---

<a id="governed-runtime-flow"></a>

## Governed runtime flow

### Proposed sequence

```text
public or restricted request
  -> Governed API authenticates, authorizes, and normalizes scope
  -> resolve released or explicitly review-authorized state
  -> resolve required EvidenceRefs to admissible EvidenceBundles
  -> evaluate rights, sensitivity, consent, access, freshness, correction, and release policy
  -> decide whether a deterministic answer is sufficient
  -> decide whether model invocation is permitted
  -> build bounded provider-neutral adapter request
  -> execute deterministic mock or admitted provider adapter
  -> validate structured candidate output
  -> validate claim-to-evidence support and citations
  -> apply post-generation policy, redaction, and precision checks
  -> emit internal DecisionEnvelope
  -> emit AIReceipt when an AI event occurred
  -> assemble complete RuntimeResponseEnvelope
  -> client renders only permitted fields, precision disclosures, notices, and obligations
```

### Pre-invocation gates

A model must not be invoked when:

- no model is necessary for a deterministic response;
- the operation is unsupported;
- required evidence cannot be resolved;
- rights or sensitivity forbids context transfer;
- consent is missing or revoked where required;
- release, correction, or withdrawal state forbids use;
- the provider/model profile does not admit the data class or operation;
- tool or network permissions are absent;
- the requested output schema is absent or unacceptable;
- the request exceeds context, time, rate, or purpose bounds.

A pre-invocation `ABSTAIN` or `DENY` may produce no AIReceipt because no AI execution occurred. The governed response and non-AI run receipts must preserve that distinction.

### Post-invocation gates

An adapter execution cannot become `ANSWER` until:

- structured output validates;
- consequential claims are supported;
- citations resolve and match claims;
- actual supported precision is disclosed;
- output contains no prohibited content;
- obligations are enforceable by the caller;
- freshness and correction state remain acceptable;
- diagnostics and receipt fields are safely redacted;
- the complete public envelope validates;
- the operation remains within the exact release and audience scope.

### No hidden fetches

The adapter may use only:

- context explicitly supplied by governed orchestration;
- tools explicitly admitted for the operation;
- network access explicitly permitted by policy and provider configuration.

It must not discover sources silently, read repositories or environment secrets, call arbitrary URLs, access canonical/internal stores, or expand scope without a new governed request.

### Composition boundary

The current selector and candidate builder are lower-level components:

```text
prevalidated fixtures -> MockAdapter selector
explicit authority-bearing inputs -> RuntimeResponseEnvelope candidate builder
```

They are not substitutes for the composed sequence above. A mature route must prove the seams among evidence, policy, citation, adapter, receipt, envelope, consumer, correction, and release.

[Back to top](#top)

---

<a id="finite-outcomes"></a>

## Finite outcomes

| Outcome | Use when | Required response posture |
|---|---|---|
| `ANSWER` | A bounded response is evidence-supported, policy-permitted, citation-valid, precise enough for the disclosed scope, fresh enough, correction-safe, release-compatible, schema-valid, and safe to render | Include required evidence refs, actual precision, notices, obligations, and safe receipt linkage |
| `ABSTAIN` | Evidence, citation support, source authority, scope, corroboration, freshness, or precision is insufficient after allowed narrowing | Explain the support gap safely; preserve reproducible handles; do not guess |
| `DENY` | Access, rights, sensitivity, consent, release state, tool use, provider use, or another policy forbids the operation | Do not reveal protected payload or precision; return safe reason codes and obligations |
| `ERROR` | Adapter, provider, policy engine, validator, schema, configuration, receipt, or infrastructure failure prevents a trustworthy result | Return safe diagnostics; no silent fallback or inferred answer |

### Narrowed answers

When KFM can answer a smaller, generalized, less precise, or otherwise policy-safe scope with adequate evidence, it may return `ANSWER` for that explicit narrowed scope. It must disclose actual precision and must not pretend to satisfy the broader request.

### Partial or streamed provider output

Partial provider output is never independently renderable. The governed path may:

- discard it and return `ERROR`;
- validate a complete bounded subset and return a narrowed `ANSWER`;
- return `ABSTAIN` when support is insufficient.

It must not expose incomplete raw text or raw provider streams.

### Outcome precedence

Composition follows the accepted finite-outcome contract and policy, not a provider-specific arithmetic shortcut. At minimum:

- an unresolved machinery failure prevents `ANSWER`;
- an applicable policy `DENY` prevents `ANSWER`;
- a required evidence or citation `ABSTAIN` prevents unsupported `ANSWER`;
- `ANSWER` requires every mandatory gate to support the exact rendered scope.

### Reason codes

Reason codes must be:

- stable and machine-readable;
- safe to expose;
- mapped to one finite outcome;
- free of protected content;
- versioned or append-only when clients depend on them.

Provider messages, exception strings, stack traces, prompts, and model-generated explanations are not public reason codes.

[Back to top](#top)

---

<a id="security-privacy-and-prompt-injection"></a>

## Security, privacy, and prompt injection

### Retrieved content is data

Documents, Markdown, YAML, JSON, metadata, issues, pull requests, transcripts, labels, map attributes, and source payloads are untrusted data. Instruction-shaped content inside them does not gain system, policy, developer, or tool authority.

Required controls include:

- separation of system policy from retrieved content;
- bounded context construction;
- output-schema enforcement;
- tool and URL allowlists;
- egress and network controls;
- context and output limits;
- source-role, rights, and sensitivity labels;
- prompt/template versioning and hashing;
- post-generation claim and citation validation;
- safe logging, redaction, and retention;
- adversarial fixtures and composed runtime tests.

### Data minimization

Only context necessary for the bounded operation may reach an adapter. Sensitive fields should be omitted, redacted, generalized, aggregated, tokenized, or replaced with governed references as policy requires.

### Deny-first domains

Living-person, DNA/genomic, archaeology, rare-species, critical-infrastructure, private-land, culturally sensitive, and other harmful-precision operations require independent rights, consent, sensitivity, and release gates. A local model does not make context transfer safe. A public source does not automatically authorize joining, embedding, inference, or republication.

### Tool use

Tools are denied by default. A model may propose an action, but governed orchestration decides whether it is supported, authorized, scoped, replayable, auditable, and reversible.

The model never receives unrestricted shell, filesystem, database, browser, source-registry, deployment, or publication access.

### Direct-client and network boundary

- Governed API and local model endpoints bind to loopback by default in local development.
- Public clients never receive provider endpoint locations.
- Reverse proxies do not expose provider routes by convenience.
- Credentials remain in approved secret stores.
- Egress is denied or allowlisted by provider profile.
- Streaming terminates inside governed orchestration.
- Generated browser bundles, proxies, service configs, and deployment manifests require direct-client checks.

### Safe diagnostics

Public diagnostics must not contain:

- prompts or hidden instructions;
- chain-of-thought or scratchpads;
- raw evidence or sensitive context;
- personal or restricted data;
- exact protected locations;
- provider credentials;
- internal paths or topology;
- stack traces or raw provider errors.

[Back to top](#top)

---

<a id="receipts-observability-and-retention"></a>

## Receipts, observability, and retention

### AIReceipt minimum

The proposed AIReceipt shape currently binds:

- receipt and run identity;
- adapter and model reference;
- input and output digests;
- policy-decision reference;
- citation-validation reference;
- finite outcome.

The local validator proves schema shape and selected local consistency constraints, including safe JSON handling, nonempty reference fields, and rejection of zero placeholder digests.

It does not prove that:

- referenced objects resolve;
- canonicalization is accepted or consistent;
- prompt/template or output schema identity is recorded;
- tool calls are recorded;
- timing, retries, and redaction posture are complete;
- runtime emission or persistence exists;
- correction or revocation can locate affected derivatives.

### Proposed additional accountability fields

A future reviewed contract may add or reference:

- adapter contract version;
- provider and model profile digests;
- prompt/template digest;
- output schema digest;
- bounded context digest;
- EvidenceBundle refs actually used;
- policy bundle digest;
- citation-validation summary;
- tool-call receipt refs;
- start/end timestamps and duration;
- timeout and retry count;
- redaction/generalization receipt refs;
- actual precision profile reference;
- correction/withdrawal lineage;
- runtime and library versions;
- safe failure category.

These remain **PROPOSED** until contract, schema, fixture, validator, producer, and migration changes are reviewed.

### No chain-of-thought storage

Receipts and logs record accountability, not private reasoning. They must not store hidden chain-of-thought, unrestricted scratchpads, raw system prompts where disclosure is unsafe, sensitive raw context, or complete provider payloads by default.

A policy-approved prompt/template may be versioned separately. Receipts should ordinarily carry its digest or reference.

### Observability

Safe metrics may include:

- finite outcomes by route and reason;
- adapter/provider/model profile;
- duration, timeout, retry, and safe error category;
- citation pass/fail/abstain rate;
- policy deny/abstain rate;
- schema-validation failure rate;
- context and output size buckets;
- tool-use counts by admitted capability;
- envelope profile and precision-disclosure version.

Metrics must preserve telemetry-redaction policy and must not become a prompt, evidence, sensitive-data, or identity store.

### Retention, correction, and revocation

Retention depends on policy, sensitivity, incident needs, and release significance. A correction, withdrawal, consent revocation, source revocation, provider compromise, model revocation, or evidence supersession must be able to locate affected receipts and derivatives without treating the receipt as the canonical answer.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

| Responsibility | Owning surface | Adapter/envelope role |
|---|---|---|
| Human architecture decision | `docs/adr/` | This ADR proposes the boundary |
| Placement authority | accepted [`ADR-0029`](./ADR-0029-adopt-directory-governance-standard-v2.md) and [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) | Own path responsibility; do not prove behavior |
| Provider-neutral runtime lane | `runtime/model_adapters/` | Adapter cards, bounded implementation, and runtime handoff |
| Provider-specific runtime wiring | `runtime/ollama/` and approved provider/runtime lanes | Internal transport only |
| Semantic object meaning | `contracts/` | Own request, response, envelope, receipt, policy, evidence, and release meaning |
| Machine-checkable shape | `schemas/contracts/v1/` | Own JSON Schema |
| Reusable side-effect-minimal helpers | `packages/` after profile and package admission | Build candidates; no authority |
| Policy and obligations | `policy/` | Decide admissibility; model cannot override |
| Evidence closure | Evidence contracts, resolvers, and approved proof/evidence homes | Resolve support before `ANSWER` |
| Citation validation | Approved validator/service surfaces | Validate claim-to-evidence support |
| Runtime orchestration | approved runtime/package/application implementation | Compose checks and emit internal results |
| Public API boundary | `apps/governed-api/` | Emit complete governed RuntimeResponseEnvelope |
| Client rendering | `apps/explorer-web/` and approved clients | Obey outcome, precision, notices, and obligations |
| Receipts and proofs | accepted `data/receipts/` and `data/proofs/` lanes | Record accountability and support |
| Release, correction, withdrawal, rollback | `release/` | Authorize public state and corrections |
| Lifecycle data | `data/` phase roots | Never become direct model/public stores |

This same-path ADR update belongs under `docs/adr/`. It creates no new root, runtime lane, contract home, schema home, policy home, receipt home, proof home, release lane, route, provider profile, or publication state.

A model adapter, selector, candidate builder, envelope, receipt, validator, workflow, or generated answer does not publish anything. Public state still requires identity, rights, sensitivity, evidence, policy, review, release, correction, and rollback support appropriate to consequence.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Verified state at the pinned base | Safe conclusion |
|---|---|---|
| ADR identity and status | ADR-0019 is unique; source `draft`, effective `proposed` | Identity is confirmed; decision is not accepted |
| Directory authority | ADR-0029 accepted exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` | Same-path placement is governed; legacy architecture copy is compatibility only |
| Canonical adapter lane | `runtime/model_adapters/README.md` | Provider-neutral runtime handoff lane is documented |
| Compatibility adapter lane | `runtime/adapters/` | Must not become a parallel canonical adapter home |
| Adapter semantic contract | Runtime note only; canonical request/response contract/schema absent | Provider-neutral invocation semantics remain unresolved |
| `MockAdapter.py` | Executable deterministic no-I/O fixture selector | Bounded component proof, not semantic adapter or runtime |
| Mock selector tests | Seven substantive unittest cases over four outcomes | Determinism, isolation, failure, safe lookup, and no-I/O proof only |
| `OllamaAdapter.py` | One-line placeholder | No Ollama client implementation |
| Governed API | Minimal WSGI app with three GET routes | Executable fail-closed scaffold, not governed AI |
| Governed API response | Deterministic `ABSTAIN` / `NOT_IMPLEMENTED` DecisionEnvelope-shaped subset | No adapter invocation or complete RuntimeResponseEnvelope |
| `DecisionEnvelope` | Proposed canonical contract/schema | Internal finite decision shape exists; policy execution is separate |
| `RuntimeResponseEnvelope` | Proposed contract, schema, validator, fixtures, candidate builder, proof suite | Substantive shape/component slice; no route composition |
| Finite fixture matrix | Valid `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`; corresponding invalid cases | Four-outcome machine-shape proof |
| Precision disclosure | Proposed profile, schema conditionals, builder checks, proof tests | ANSWER-only actual precision is encoded; consumer adoption unproved |
| Runtime envelope drift | Contract prose, schema/profile, package docs, and route shape differ | Profile convergence remains held |
| `AIReceipt` | Proposed contract/schema plus local validator | Shape/local consistency proof; no runtime emission or persistence |
| Runtime policy | Substantive README plus four tiny proposed Rego scaffolds | No accepted executable policy behavior |
| Focus mock workflow | Read-only bounded checks; finite-envelope job runs both suites; mock-Focus job records HOLD | CI source proves intended bounded checks, not operational Focus |
| Focus request/response | Descriptive contracts and permissive proposed schemas | Canonical relationship to adapter request remains unresolved |
| Direct public model client | Not surfaced in bounded inspection | Not proof of repository-wide absence |
| Provider/model admission | Not established | No provider/model approved |
| Citation validation integration | Not established for AI path | `ANSWER` support is not operationally proved |
| Production deployment | Unknown | No operational or release claim |
| Publication | Denied as inference | No AI response is KFM publication |

### Material corrections since v1.2

- `MockAdapter.py` is no longer a one-line placeholder; it is a bounded deterministic selector.
- Four valid finite outcomes and substantive selector/shape proof suites now exist.
- RuntimeResponseEnvelope has an ANSWER-only precision profile and a deterministic candidate builder.
- AIReceipt now has a substantive local validator.
- Runtime policy is no longer README-only, but its four Rego files remain non-enforcing scaffolds.
- The Focus workflow now contains a substantive finite-envelope job while retaining the mock-Focus hold.
- `OllamaAdapter.py`, semantic adapter request/response, governed AI route composition, evidence resolution, citation validation, receipt persistence, provider admission, and public release remain unimplemented or unproved.
- Accepted Directory Rules authority now belongs at `docs/doctrine/directory-rules.md`.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Capability | Current state | Graduation requirement |
|---|---|---|
| ADR identity | **CONFIRMED** | Human decision review |
| Directory placement | **CONFIRMED under accepted ADR-0029** | No further path decision for same-path edit |
| Provider-neutral runtime lane | **CONFIRMED documentation** | Accepted semantics and implementations |
| Canonical adapter request/response | **NOT ESTABLISHED** | Contract, schema, fixtures, validator, compatibility policy |
| Mock fixture selector | **BOUNDED EXECUTABLE COMPONENT** | Keep responsibility narrow or add reviewed semantic layer |
| Mock semantic adapter | **NOT ESTABLISHED** | Deterministic request/outcome semantics and composed tests |
| Ollama adapter | **PLACEHOLDER** | Provider admission, implementation, isolation, tests, rollback |
| Governed API | **MINIMAL EXECUTABLE ABSTAIN SCAFFOLD** | Auth, evidence, policy, citation, orchestration, complete envelope |
| DecisionEnvelope | **PROPOSED contract/schema** | Accepted semantics, fixtures, validators, caller behavior |
| RuntimeResponseEnvelope shape | **PROPOSED SUBSTANTIVE SLICE** | Profile convergence and governed consumer integration |
| RuntimeResponseEnvelope builder | **BOUNDED CANDIDATE BUILDER** | Package/profile admission and route composition |
| Precision disclosure | **PROPOSED SCHEMA-BOUND PROFILE** | Contract convergence and API/UI adoption |
| AIReceipt | **PROPOSED contract/schema + local validator** | Runtime emission, persistence, ref resolution, retention, correction |
| Runtime policy | **NON-ENFORCING SCAFFOLDS** | Meaningful rules, tests, bundle identity, evaluator, obligations |
| Evidence resolution | **NOT ESTABLISHED for AI path** | Resolver integration and negative-state tests |
| Citation validation | **NOT ESTABLISHED for AI path** | Claim/citation contract, validator, fixtures, enforcement |
| Prompt-injection protection | **NOT ESTABLISHED as composed proof** | Threat model, adversarial fixtures, tool/network tests |
| Mock Focus runtime | **WORKFLOW_HOLD** | Accepted request/response profile, fixtures, command, composed behavior |
| Four-outcome shape/selector proof | **CONFIRMED BOUNDED** | Do not over-promote; integrate only after higher-layer gates |
| Direct-client enforcement | **PARTIAL structural evidence** | Static, dependency, generated-bundle, proxy, browser, deployment checks |
| Provider/model admission | **NOT ESTABLISHED** | Reviewed profile and registry/decision object |
| Production deployment | **UNKNOWN** | Security, operations, review, release, correction, rollback evidence |

### Current Governed API boundary

Current source confirms:

```text
GET /bootstrap -> ABSTAIN / NOT_IMPLEMENTED
GET /layers    -> ABSTAIN / NOT_IMPLEMENTED
GET /evidence  -> ABSTAIN / NOT_IMPLEMENTED
```

The WSGI application permits registered GET routes, returns JSON, and returns `404` or `405` otherwise. It does not invoke an adapter, resolve evidence, execute runtime policy, validate citations, emit AIReceipt, or assemble the current complete RuntimeResponseEnvelope.

### Current Focus workflow boundary

The workflow intentionally preserves two distinct facts:

1. **`mock-focus-flows`: HELD.** Runtime mock and adapter child lanes remain bounded; Focus schemas and policy remain proposed scaffolds; no operational Focus fixture or command executes.
2. **`finite-envelope-shape`: bounded proof.** Repository-owned unittest suites exercise the four-outcome fixtures, no-I/O selector, envelope profile, alias, precision invariants, negative fixtures, and validator wiring.

A green workflow conclusion therefore proves bounded source/test behavior only. It is not a mock Focus request, model call, evidence resolution, policy execution, citation validation, receipt emission, client response, release, or publication.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use the smallest reversible sequence. Do not activate Ollama first.

### Phase 0 — preserve bounded truth

- Keep ADR-0019 proposed.
- Keep `KFM_MODEL_RUNTIME=mock` as a safe example.
- Keep provider endpoints loopback-only.
- Preserve the bounded selector and four-outcome proof.
- Keep mock Focus held until its complete dependency set exists.
- Do not advertise the selector or candidate builder as governed AI.

### Phase 1 — converge object authority

1. Choose canonical provider-neutral adapter request/response names and semantic home.
2. Define paired schemas, positive/negative fixtures, validators, and compatibility rules.
3. Decide whether Focus request/response call the generic adapter contract or remain a separate caller contract.
4. Reconcile the generic RuntimeResponseEnvelope contract prose with the precision profile, schema, builder, tests, and package documentation.
5. Preserve distinct roles for DecisionEnvelope, RuntimeResponseEnvelope, AIReceipt, PolicyDecision, EvidenceBundle, and release objects.
6. Define stable reason, policy-state, freshness, and correction vocabularies or registry references.
7. Record compatibility migration; do not create parallel authority.

### Phase 2 — graduate semantic deterministic mock behavior

1. Keep the existing selector as a bounded primitive or rename it through a reviewed migration if necessary.
2. Implement one deterministic semantic mock adapter over the accepted request/response contract.
3. Use no network, provider, secrets, hidden files, clocks, or uncontrolled randomness.
4. Cover all four outcomes from request scenarios rather than selecting already-finished public envelopes only.
5. Add malformed request/response, unsupported operation, evidence gap, citation gap, policy deny, sensitive-data deny, correction/withdrawal, timeout, tool deny, and adapter error cases.
6. Emit an internal adapter result, not a public RuntimeResponseEnvelope.

### Phase 3 — compose governed orchestration

1. Add an authenticated/authorized Governed API orchestration path.
2. Resolve released or explicitly review-authorized state through governed interfaces.
3. Evaluate pre-invocation policy.
4. Invoke only the admitted deterministic mock adapter.
5. Validate structured output and claim-to-evidence citations.
6. Apply post-generation policy, redaction, and actual-precision checks.
7. Emit DecisionEnvelope, AIReceipt, and the complete accepted RuntimeResponseEnvelope.
8. Add client and boundary tests proving raw adapter/provider output cannot escape.

### Phase 4 — receipts, correction, and invalidation

- Persist AIReceipt to an accepted receipt lane.
- Resolve policy and citation references.
- Pin canonicalization and prompt/template/output-schema identity.
- Prove no-chain-of-thought, no-secret, and safe-diagnostic behavior.
- Add correction, withdrawal, consent-revocation, evidence-supersession, and provider-revocation propagation.
- Inventory and invalidate caches, indexes, summaries, exports, and other derivatives.
- Define replay and retention posture.

### Phase 5 — provider/model admission

Before Ollama or another provider:

- create a reviewed provider/model/profile record;
- pin identity or digest;
- review rights, data classes, and intended uses;
- deny public exposure by default;
- enforce loopback or reviewed network topology;
- configure timeout, rate, context, output, and concurrency limits;
- disable tools by default;
- add no-secret and no-sensitive-context tests;
- implement health and failure normalization;
- prove one-command deactivation and fallback to mock/disabled mode.

### Phase 6 — restricted provider canary

- Add the provider adapter behind the same accepted contract.
- Run local or restricted canary only.
- Compare finite outcomes, diagnostics, and receipt shape against deterministic mock expectations.
- Prove provider substitution does not alter public contracts or policy semantics.
- Keep public `ANSWER` disabled until separate release review permits it.
- Record incident, rollback, model-revocation, and rights-change procedures.

### Phase 7 — public graduation

Public AI-mediated `ANSWER` requires:

- accepted ADR and contracts;
- complete evidence, policy, citation, precision, freshness, and correction closure;
- secure deployment and direct-client isolation;
- enforceable consumer obligations;
- safe observability and retention;
- correction, withdrawal, invalidation, and rollback;
- accountable human review and release state.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

ADR-0019 remains proposed until its decision is reviewed independently of implementation maturity.

### Decision acceptance gates

- [ ] ADR identity, title, source/effective status, owners, reviewer classes, and affected roots are reviewed.
- [ ] ADR-0004, ADR-0008, ADR-0010, ADR-0016, ADR-0020, ADR-0025, ADR-0029, and relevant evidence/policy/release records are reconciled.
- [ ] The canonical provider-neutral adapter responsibility is approved.
- [ ] The separation among adapter result, DecisionEnvelope, RuntimeResponseEnvelope, AIReceipt, PolicyDecision, EvidenceBundle, and release objects is approved.
- [ ] The four public outcomes and ANSWER precision-disclosure posture are approved.
- [ ] No-direct-model-client, no-generated-truth, no-private-reasoning-retention, mock-first, provider-admission, and deactivation rules are approved.
- [ ] The ADR and canonical index move to matching reviewed `accepted` status in one governed change.

### Component proof gates

- [x] A bounded no-I/O selector exists and requires all four outcomes.
- [x] Selector tests prove deterministic isolation and fail-closed configuration/lookup behavior.
- [x] Four-outcome RuntimeResponseEnvelope fixtures exist.
- [x] Standard-library tests prove closed shape, alias, outcome, and precision invariants.
- [x] A deterministic RuntimeResponseEnvelope candidate builder exists.
- [x] A local AIReceipt validator exists.
- [ ] Exact-head hosted results for the final ADR update are inspected.
- [ ] Component documentation is reconciled with current bytes without overclaiming composition.

### Governed runtime graduation gates

- [ ] Canonical adapter request/response contracts and paired schemas exist.
- [ ] Positive and negative fixtures cover their semantics.
- [ ] A deterministic semantic mock adapter processes accepted requests.
- [ ] All four outcomes arise from behavior tests, not hand-authored public envelopes alone.
- [ ] Invalid shapes and runtime failures fail closed.
- [ ] Governed API emits the complete accepted RuntimeResponseEnvelope.
- [ ] Raw adapter/provider output and streams cannot reach a client.
- [ ] Evidence resolution and citation validation gate every consequential `ANSWER`.
- [ ] Actual precision is disclosed and supported.
- [ ] Meaningful runtime policy and obligations execute.
- [ ] AIReceipt is emitted, persisted, validated, and linked.
- [ ] No reasoning trace, secret, raw sensitive context, or unsafe diagnostic is retained or exposed.
- [ ] Prompt-injection, tool-use, URL, egress, and context-boundary negative tests exist.
- [ ] Correction, withdrawal, revocation, retention, cache invalidation, and rollback are tested.
- [ ] Direct-client restrictions are checked across code, dependencies, generated assets, proxies, and deployment.
- [ ] At least one provider can be disabled without changing public envelope shape.
- [ ] A live provider is not admitted until its separate gates pass.

### What current green tests prove

A passing selector, builder, schema, fixture, validator, or workflow proves only the responsibility asserted by that surface. It does not prove that a model ran, evidence resolved, policy allowed a response, citations matched claims, an AIReceipt was persisted, a client obeyed obligations, or release/publication occurred.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Provider changes do not redefine public trust semantics.
- Public clients receive one finite governed envelope boundary.
- Model execution remains subordinate to evidence, policy, citation, precision, correction, and release.
- Mock-first development supports deterministic no-network CI.
- Component proof can advance without pretending the whole runtime exists.
- Negative states remain inspectable instead of becoming fluent fallback.
- ANSWER precision becomes explicit rather than implied by display or request.
- AIReceipt enables accountability without elevating generated output to truth.
- Provider/model deactivation becomes a governed configuration/release action rather than a client migration.
- Prompt injection, tools, privacy, retention, and correction become architecture concerns.

### Costs

- More explicit contracts, profiles, fixtures, validators, and object relationships are required.
- Current profile drift must be reconciled before a stable public envelope API is declared.
- Structured-output, citation, precision, and policy checks add latency and complexity.
- Mock fixtures must cover negative and adversarial behavior, not only generated text.
- Provider-specific features may remain unavailable when they do not fit the admitted contract.
- Receipt, canonicalization, redaction, retention, and invalidation need cross-root review.
- Direct-client enforcement spans code, dependencies, build output, proxies, and deployment.
- A bounded selector may need compatibility treatment when semantic adapter interfaces land.

### Tradeoffs

- Provider neutrality can hide useful provider-specific capabilities. Optional capabilities may be exposed through explicit admitted profiles without changing the public envelope.
- Determinism can reduce realism. Deterministic tests prove contracts; restricted canaries prove provider behavior.
- Finite outcomes simplify clients but require stable reason and obligation vocabularies.
- Not storing raw prompts or reasoning protects privacy but limits debugging. Digests, approved templates, synthetic fixtures, and bounded incident captures are preferred.
- Precision disclosure increases envelope complexity but prevents stronger public claims than evidence supports.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Decision |
|---|---|
| Browser calls local or hosted model directly | Rejected: bypasses Governed API, policy, evidence, receipts, and release |
| Provider SDK types become public API types | Rejected: provider lock-in and trust-semantic leakage |
| Adapter returns RuntimeResponseEnvelope directly | Rejected: collapses orchestration, policy, citation, precision, freshness, and correction responsibilities |
| Current fixture selector is declared the canonical ModelAdapter | Rejected: it selects prevalidated envelopes and has no request or semantic outcome contract |
| One free-text response with optional warnings | Rejected: negative states and obligations become ambiguous |
| Add `HOLD` or `REVIEW` as a fifth public outcome | Rejected: use `ABSTAIN` with safe reason/obligation/review state |
| Make deterministic mock proof optional and begin with Ollama | Rejected: loses no-network contract proof |
| Store complete prompts/provider payloads for audit | Rejected by default: privacy, injection, sensitivity, and retention risk |
| Treat AIReceipt as correctness proof | Rejected: it records process accountability only |
| Infer precision from map zoom, requested resolution, or model confidence | Rejected: actual evidence-supported precision controls |
| Use only RuntimeResponseEnvelope and remove DecisionEnvelope | Deferred: requires caller and policy-contract analysis |
| Use only DecisionEnvelope as the public shape | Deferred/rejected for current proposal: it lacks the stronger client-facing freshness/correction/precision profile |
| Separate canonical adapter interface per provider | Rejected: provider-specific code remains behind one boundary |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Risk / question | Current state | Required next step |
|---|---|---|
| Canonical adapter request/response names and homes | **OPEN** | Contract/schema design review |
| Current `MockAdapter` future compatibility | **OPEN but bounded** | Preserve as primitive or migrate explicitly |
| `FocusRequest` relationship to adapter request | **OPEN** | Decide caller-specific versus generic object |
| Generic versus Focus-local RuntimeResponseEnvelope | **CONFLICTED / compatibility alias partially present** | Consolidate or document migration |
| RuntimeResponseEnvelope prose versus precision schema/profile | **CONFLICTED** | One reviewed profile and synchronized docs/code/tests |
| Package docs versus current candidate builder | **STALE / NEEDS VERIFICATION** | Package/source README evidence refresh |
| DecisionEnvelope versus RuntimeResponseEnvelope | **OPEN but bounded here** | Preserve distinct roles until reviewed convergence |
| Reason-code registry | **NOT ESTABLISHED** | Define stable owner and versioning |
| Policy, freshness, and correction vocabularies | **NEEDS VERIFICATION** | Contract/schema/policy alignment |
| AIReceipt reference resolution and persistence | **NOT ESTABLISHED** | Producer/store/validator and correction flow |
| AI input/output canonicalization | **NEEDS VERIFICATION** | Pin accepted canonicalization profile |
| Prompt/template storage and hashing | **OPEN** | Security, privacy, reproducibility review |
| Streaming | **OPEN** | Governed buffering, cancellation, and no-raw-stream rule |
| Embeddings | **OPEN / separate risk** | Data class, retention, re-identification, and index policy |
| Tool invocation | **DENY by default** | Capability contract and per-tool governance |
| Provider/model admission object | **NOT ESTABLISHED** | Registry/decision contract and review flow |
| Model rights and redistribution | **NEEDS VERIFICATION per model** | Source/rights review |
| Local daemon exposure | **LOOPBACK example only** | Deployment and network enforcement |
| Direct-client static enforcement | **PARTIAL** | Extend code/dependency/bundle/proxy/browser checks |
| Runtime Rego semantics | **NON-ENFORCING SCAFFOLDS** | Accepted bundle, evaluator, fixtures, and tests |
| Adapter correction/revocation propagation | **NOT ESTABLISHED** | Receipt lineage and downstream invalidation |
| Runtime receipt retention | **OPEN** | Retention and sensitivity policy |
| Public AI `ANSWER` | **NOT AUTHORIZED by current evidence** | All runtime and release gates |

### High-risk anti-patterns

- importing provider SDK types into public DTOs;
- embedding model endpoints in browser code or generated assets;
- using a model answer after evidence resolution failed;
- treating public source availability as permission to infer or join sensitive data;
- storing prompts, provider payloads, or reasoning traces in receipts;
- enabling unrestricted tools or network access;
- returning a schema-valid envelope with unresolved support refs;
- treating selector, builder, adapter health, or workflow success as release readiness;
- switching providers without new profile identity in receipts;
- suppressing `ABSTAIN` to improve answer-rate metrics;
- presenting requested or rendered precision as actual support;
- treating an AI-generated correction as an approved correction.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback

This revision is documentation-only. Roll back by reverting its commit or restoring prior target blob `c0bc41cc11b40b1ee87a838a3e80024a2da56c04`, then remove or supersede the paired generated-work receipt. That rollback changes no runtime, provider, model, policy, receipt instance, envelope instance, release, or public state.

### Decision rollback

If ADR-0019 is later accepted and replaced:

1. author a successor ADR;
2. record reciprocal supersession links;
3. preserve this record;
4. define contract/schema/profile and data compatibility;
5. preserve historical receipts under original versions;
6. update the canonical ADR index;
7. test provider deactivation and public-envelope compatibility.

### Runtime/provider deactivation

Every admitted provider must have a reversible deactivation path:

```text
provider-backed adapter
  -> disabled
  -> deterministic mock or null/disabled mode
  -> governed ABSTAIN, DENY, or ERROR envelope
```

Deactivation must not expose provider errors, silently select an unreviewed fallback, convert missing evidence into an answer, invalidate historical receipts, or alter public envelope shape without versioning.

### Incident rollback

On provider compromise, model revocation, prompt-injection incident, unsafe output, rights change, consent revocation, evidence supersession, schema/profile mismatch, or receipt-integrity failure:

- disable the provider/model profile;
- deny or abstain affected operations;
- preserve incident and receipt identifiers;
- identify affected responses and derivatives;
- issue correction or withdrawal records where required;
- invalidate caches, indexes, summaries, exports, and public derivatives;
- return clients to a safe governed finite state;
- require reviewed reactivation.

[Back to top](#top)

---

<a id="verification-checklist"></a>

## Verification checklist

| Check | Result |
|---|---|
| ADR identity and exact path | **CONFIRMED** |
| Source metadata | **CONFIRMED draft** |
| Effective decision status | **CONFIRMED proposed** |
| Same-path documentation update | **PASS** |
| Canonical Directory Rules authority | **CONFIRMED accepted under ADR-0029** |
| Canonical runtime adapter lane | **CONFIRMED documentation** |
| Canonical adapter request/response contract/schema | **NOT ESTABLISHED** |
| Bounded MockAdapter selector | **CONFIRMED executable** |
| Mock selector proof | **CONFIRMED substantive source** |
| Semantic mock adapter | **NOT ESTABLISHED** |
| OllamaAdapter implementation | **CONFIRMED placeholder** |
| Governed API executable scaffold | **CONFIRMED** |
| Governed API model invocation | **NOT ESTABLISHED** |
| Governed API complete RuntimeResponseEnvelope | **NOT ESTABLISHED** |
| DecisionEnvelope contract/schema | **CONFIRMED PROPOSED** |
| RuntimeResponseEnvelope schema/profile/builder | **CONFIRMED PROPOSED bounded implementation** |
| Four finite valid outcome fixtures | **CONFIRMED** |
| Finite-envelope proof suite | **CONFIRMED substantive source** |
| RuntimeResponseEnvelope profile convergence | **CONFLICTED / HELD** |
| AIReceipt contract/schema | **CONFIRMED PROPOSED** |
| AIReceipt local validator | **CONFIRMED executable source** |
| AIReceipt runtime emission/persistence | **NOT ESTABLISHED** |
| Runtime policy | **CONFIRMED non-enforcing scaffolds** |
| Focus mock workflow | **CONFIRMED bounded proof plus explicit HOLD** |
| Evidence/citation integration | **NOT ESTABLISHED** |
| Prompt-injection and tool-use composed tests | **NOT ESTABLISHED** |
| Provider/model admission | **NOT ESTABLISHED** |
| Direct-client prohibition | **CONFIRMED doctrine; enforcement incomplete** |
| Local repository-native test suite for this edit | **NOT RUN — no mounted checkout** |
| Hosted exact-head checks | **PENDING after draft PR creation** |
| Release or publication | **NOT CLAIMED** |

Remote repository reads establish exact bytes, source relationships, and declared test/workflow behavior. They do not substitute for executing a policy evaluator, evidence resolver, citation validator, provider, receipt store, governed client, release gate, or public deployment.

[Back to top](#top)

---

<a id="references"></a>

## References

### Governing and adjacent ADRs

- [`docs/adr/README.md`](./README.md)
- [`docs/adr/INDEX.md`](./INDEX.md)
- [`ADR-0004 — Governed API Trust Membrane`](./ADR-0004-apps-governed-api-is-the-trust-membrane.md)
- [`ADR-0008 — Ollama Subordinate to Governed API`](./ADR-0008-ollama-subordinate-to-governed-api.md)
- [`ADR-0010 — Deny by Default for Sensitive Domains`](./ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md)
- [`ADR-0011 — Receipts vs Proofs vs Manifests vs Catalog`](./ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md)
- [`ADR-0016 — Telemetry Redaction Posture`](./ADR-0016-telemetry-redaction-posture.md)
- [`ADR-0020 — Abstain Is a First-Class Decision`](./ADR-0020-abstain-is-a-first-class-decision.md)
- [`ADR-0025 — Public Client Never Reads Canonical/Internal Stores`](./ADR-0025-public-client-never-reads-canonical-internal-stores.md)
- [`ADR-0029 — Adopt Directory Governance Standard v2`](./ADR-0029-adopt-directory-governance-standard-v2.md)
- [`Canonical Directory Rules`](../doctrine/directory-rules.md)
- [`Legacy Directory Rules compatibility body`](../architecture/directory-rules.md)

### Current implementation and contract evidence

- [`runtime/model_adapters/README.md`](../../runtime/model_adapters/README.md)
- [`runtime/model_adapters/AdapterContract.md`](../../runtime/model_adapters/AdapterContract.md)
- [`runtime/model_adapters/MockAdapter.py`](../../runtime/model_adapters/MockAdapter.py)
- [`runtime/model_adapters/OllamaAdapter.py`](../../runtime/model_adapters/OllamaAdapter.py)
- [`runtime/model_adapters/mock/README.md`](../../runtime/model_adapters/mock/README.md)
- [`runtime/ollama/README.md`](../../runtime/ollama/README.md)
- [`Governed API application`](../../apps/governed-api/src/governed_api/main.py)
- [`Governed API route registry`](../../apps/governed-api/src/governed_api/routes/registry.py)
- [`Governed API ABSTAIN scaffold`](../../apps/governed-api/src/governed_api/stub.py)
- [`DecisionEnvelope contract`](../../contracts/runtime/decision_envelope.md)
- [`DecisionEnvelope schema`](../../schemas/contracts/v1/runtime/decision_envelope.schema.json)
- [`RuntimeResponseEnvelope contract`](../../contracts/runtime/runtime_response_envelope.md)
- [`RuntimeResponseEnvelope schema`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json)
- [`Actual precision contract profile`](../../contracts/runtime/precision_actually_used.md)
- [`RuntimeResponseEnvelope candidate builder`](../../packages/envelopes/src/envelopes/runtime_response.py)
- [`RuntimeResponseEnvelope validator`](../../tools/validators/validate_runtime_response_envelope.py)
- [`RuntimeResponseEnvelope fixtures`](../../fixtures/contracts/v1/runtime/runtime_response_envelope/)
- [`Finite-envelope proof`](../../tests/runtime_proof/test_envelope_finite_outcomes.py)
- [`MockAdapter finite-outcome proof`](../../tests/runtime_proof/test_mock_adapter_finite_outcomes.py)
- [`Runtime-proof boundary`](../../tests/runtime_proof/README.md)
- [`AIReceipt contract`](../../contracts/runtime/ai_receipt.md)
- [`AIReceipt schema`](../../schemas/contracts/v1/runtime/ai_receipt.schema.json)
- [`AIReceipt validator`](../../tools/validators/validate_ai_receipt.py)
- [`Runtime policy boundary`](../../policy/runtime/README.md)
- [`Runtime abstain scaffold`](../../policy/runtime/abstain_on_missing_evidence.rego)
- [`Runtime public-deny scaffold`](../../policy/runtime/deny_unpublished_public.rego)
- [`Runtime evidence-required scaffold`](../../policy/runtime/evidence_required.rego)
- [`Runtime receipt scaffold`](../../policy/runtime/run_receipt.rego)
- [`Focus mock and finite-envelope workflow`](../../.github/workflows/focus-mock-test.yml)
- [`.env.example`](../../.env.example)

### Source artifact used for this revision

- `Pasted text(20260814-150503).txt` — KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0; used as the implementation and delivery contract, not repository implementation evidence.

[Back to top](#top)

---

## No-loss and change ledger

| Prior surface | v1.3 disposition |
|---|---|
| ADR identity, path, draft/proposed status, no publication effect | **RETAINED** |
| D1–D8 provider-neutral, orchestration, finite outcomes, mock-first, no-direct-client, no-generated-truth, no-private-reasoning, admission decisions | **RETAINED and sharpened** |
| Object separation among adapter output, DecisionEnvelope, RuntimeResponseEnvelope, AIReceipt, EvidenceBundle, policy, and release | **RETAINED** |
| Security, prompt-injection, data minimization, tool, network, diagnostic, and receipt boundaries | **RETAINED and expanded** |
| MockAdapter placeholder claim | **SUPERSEDED** by current bounded executable selector evidence |
| Two-outcome fixture and assert-true test claims | **SUPERSEDED** by four-outcome fixtures and substantive selector/shape proofs |
| Runtime policy README-only claim | **SUPERSEDED** by substantive documentation plus four non-enforcing Rego scaffolds |
| RuntimeResponseEnvelope shape-only claim | **EXPANDED** with precision profile, deterministic candidate builder, tests, and explicit profile drift |
| AIReceipt validator uncertainty | **UPDATED** to confirmed local validator while preserving no-emission/no-persistence boundary |
| Governed API, Ollama, evidence, citation, provider admission, correction, and release gaps | **RETAINED** because current evidence does not close them |
| Directory Rules compatibility path as apparent authority | **CORRECTED** to accepted canonical doctrine path plus legacy compatibility body |
| Implementation sequence, acceptance gates, consequences, alternatives, risks, and rollback | **RETAINED and updated** for current evidence |

No policy behavior, contract meaning, schema shape, fixture, validator, test, workflow, package, application, data object, provider profile, model runtime, release record, deployment, or publication state changes in this documentation slice.

## Change log

| Version | Date | Change |
|---|---|---|
| `v1.3` | 2026-08-14 | Refreshed against current main; adopted Directory Rules placement; bounded executable MockAdapter selector; four-outcome fixtures/proofs; RuntimeResponseEnvelope precision profile and candidate builder; AIReceipt validator; runtime Rego scaffold inventory; profile-drift and composition boundaries; updated gates, risks, and rollback. Decision remains proposed. |
| `v1.2` | 2026-07-24 | Repository-grounded modernization separating adapter output, DecisionEnvelope, RuntimeResponseEnvelope, and AIReceipt; documented placeholder adapters, Governed API ABSTAIN scaffold, mock workflow hold, security, admission, and rollback. |
| Earlier | 2026-05 to 2026-07 | Initial proposed provider-neutral adapter and finite-envelope decision plus planning refinements. |
