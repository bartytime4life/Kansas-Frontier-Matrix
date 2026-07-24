<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr-0019-ai-adapter-contract-and-finite-envelopes
title: ADR-0019 — AI Adapter Contract and Finite Envelopes
type: adr
adr_id: ADR-0019
version: v1.2
status: draft
effective_decision_status: proposed
owners:
  - "NEEDS VERIFICATION — architecture stewardship"
  - "NEEDS VERIFICATION — governed API and AI-runtime stewardship"
  - "NEEDS VERIFICATION — evidence, policy, citation, security, contracts, schemas, validation, and release stewardship"
reviewers_required:
  - Architecture steward
  - Governed API steward
  - Runtime / governed-AI steward
  - Evidence and citation steward
  - Policy and sensitivity steward
  - Security and privacy reviewer
  - Contracts and schemas stewards
  - Validation and CI stewards
  - Docs steward
created: 2026-05-09
updated: 2026-07-24
policy_label: public
truth_posture: cite-or-abstain
responsibility_root: docs/
current_path: docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
supersedes: []
superseded_by: null
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 9ffa0f56197ea1dad3290626b4c166e2bebc3bff
  target_prior_blob: db55defa15fa709b20c613cf595adc334fe785ba
  adr_index_blob: cf08fae322ac53426f7394d97897fdb942253049
  adr_readme_blob: f1b5d34a53b6c717832d587de54989ce8192bcaa
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  adr_0008_blob: 387b1a1969b2af77b325d2cacd35c19ab13f63f8
  model_adapters_readme_blob: 16456452e03884dabb24c670c41c9e359f679769
  adapter_contract_note_blob: e371e5ca008ecbd0775bea9c2a31ef76131e7575
  ollama_adapter_blob: 1769a719d6a6df53e001abbc4c67ad486ab5c944
  mock_adapter_blob: 2a7b6533c9f073495f868aded9b213a38efe7526
  governed_api_main_blob: bcc8d3a0ddba4b225e962b594d548819df0cbb71
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 5d7c137d2e78ddfca35a1356a96333ac2e84952b
  decision_envelope_schema_blob: 349782c8760f77e432ed1e9239d5ddc2ffe1f9b8
  runtime_response_contract_blob: b81d67dccdd8470e066ab8247eb93c5df67a6679
  runtime_response_schema_blob: 5105d419432a27176a8ee10870d75400cfa2ab8c
  runtime_response_validator_blob: 11ddc64c4299d103b0eef383c2f7bdd3bb12f1f9
  runtime_response_valid_abstain_blob: 87a405408dc8d5ec0d6c789a9584e0a6b62b3c59
  runtime_response_valid_answer_blob: 9d70fe89627260f0c185ac492341e269fff4d108
  ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  runtime_policy_blob: b9bfee731553c504b514f07a6862ef3e68328f02
  focus_mock_workflow_blob: aa97ee5ad099d1e10922d037061abde17ceb3a93
  finite_envelope_placeholder_test_blob: ee28fd9bb6eebee6453d8d8e432d3a0e92bfdd23
  env_example_blob: 5af73215557f4af432157409ff89ab17088d0953
inspection_boundary: >
  Current-session GitHub reads, bounded repository search, ADR inventory and operating
  contract, Directory Rules, adjacent ADR-0008, runtime adapter documentation and
  placeholders, governed API source, runtime contracts and schemas, generic fixtures and
  validator, runtime policy scaffold, Focus mock workflow, placeholder runtime-proof test,
  and safe environment template. No model daemon, provider endpoint, credential, live
  evidence resolver, policy evaluator, citation service, receipt store, deployed API,
  public client, production ruleset, or release environment was exercised.
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
  - contracts/runtime/ai_receipt.md
  - schemas/contracts/v1/runtime/decision_envelope.schema.json
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - fixtures/contracts/v1/runtime/runtime_response_envelope/
  - tools/validators/validate_runtime_response_envelope.py
  - tests/runtime_proof/test_envelope_finite_outcomes.py
  - policy/runtime/README.md
  - .github/workflows/focus-mock-test.yml
  - .env.example
tags: [kfm, adr, governed-ai, model-adapter, provider-neutral, finite-outcomes, decision-envelope, runtime-response-envelope, ai-receipt, mock-first, cite-or-abstain, trust-membrane, no-direct-model-client]
notes:
  - "v1.2 is a same-path repository-grounded modernization; it preserves source metadata draft and effective decision status proposed."
  - "The governed API currently emits deterministic DecisionEnvelope-shaped ABSTAIN scaffolds for three GET routes; it does not invoke a model adapter or emit the full RuntimeResponseEnvelope contract."
  - "MockAdapter.py and OllamaAdapter.py remain one-line placeholders; runtime policy remains a greenfield stub."
  - "RuntimeResponseEnvelope and AIReceipt have substantive PROPOSED contracts/schemas, but operational envelope assembly, citation validation, policy execution, and receipt persistence are not established."
  - "The Focus mock workflow is an explicit readiness HOLD; generic envelope fixtures cover ANSWER and ABSTAIN shape, while the runtime-proof test remains assert-true scaffolding."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0019 — AI Adapter Contract and Finite Envelopes

> **Proposed decision.** KFM will place every model or provider behind one provider-neutral adapter boundary, keep adapter output internal to governed orchestration, and expose only governed finite envelopes through `apps/governed-api/`. Generated language remains interpretation downstream of evidence, policy, citation validation, review, release, correction, and rollback.

[![Decision: proposed](https://img.shields.io/badge/decision-proposed-d4a72c?style=flat-square)](#status)
[![ADR ID: confirmed](https://img.shields.io/badge/ADR--0019-confirmed-0969da?style=flat-square)](#current-repository-evidence)
[![Governed API: ABSTAIN scaffold](https://img.shields.io/badge/governed%20API-ABSTAIN%20scaffold-2da44e?style=flat-square)](#current-implementation-maturity)
[![Adapters: placeholders](https://img.shields.io/badge/adapters-placeholders-6e7781?style=flat-square)](#current-repository-evidence)
[![Mock runtime: hold](https://img.shields.io/badge/mock%20runtime-WORKFLOW__HOLD-b42318?style=flat-square)](#current-implementation-maturity)
[![Publication: none](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#authority-and-publication-boundary)

> [!IMPORTANT]
> **Identity is confirmed; acceptance is not.** [`docs/adr/INDEX.md`](./INDEX.md) uniquely assigns `ADR-0019` to this file. Its source metadata is `draft`, which the ADR operating contract conservatively normalizes to effective decision status `proposed`. Editing this file, merging a pull request, validating a schema, or passing CI does not accept the decision.

> [!CAUTION]
> **The current Governed API is not an AI route.** It registers `/bootstrap`, `/layers`, and `/evidence` and returns deterministic `ABSTAIN` / `NOT_IMPLEMENTED` scaffolds. Those responses are shaped like the current `DecisionEnvelope` schema, not the complete client-facing `RuntimeResponseEnvelope`.

> [!WARNING]
> **A model response is never the public contract.** Browsers, map shells, review tools, exports, and other clients must not call Ollama or another provider directly, render raw provider output, infer evidence or policy from prose, or treat a model result as release or publication authority.

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
| **Decision class** | Provider-neutral model boundary, governed orchestration, finite runtime envelopes, AI accountability, public-client isolation, and provider deactivation |
| **Current repository maturity** | Proposed contracts and shape checks plus deterministic ABSTAIN/readiness scaffolds; no accepted adapter runtime |
| **Implementation effect of this revision** | Documentation only |
| **Publication effect** | None |
| **Supersedes / superseded by** | None / none |

### Acceptance versus implementation

Two independent states must remain visible:

1. **ADR acceptance** would approve the responsibilities, object boundaries, provider-neutral contract posture, and finite-outcome rules in this record.
2. **Implementation graduation** would require accepted contracts and schemas, a deterministic `MockAdapter`, meaningful policy, governed evidence retrieval, citation validation, AIReceipt persistence, complete finite-outcome tests, public-client isolation, provider admission, correction, and rollback.

An accepted ADR without those implementation gates would be governing doctrine, not proof that governed AI is operational. Conversely, an adapter file, installed model, successful provider call, valid envelope, green workflow, or deployed endpoint cannot accept the ADR.

[Back to top](#top)

---

<a id="evidence-boundary"></a>

## Evidence boundary

This revision is grounded in current repository bytes at `main@9ffa0f56197ea1dad3290626b4c166e2bebc3bff`.

### Truth labels

| Label | Meaning in this ADR |
|---|---|
| **CONFIRMED** | Verified from current repository files, tests, workflow source, or exact readback |
| **PROPOSED** | Decision, field, path role, contract, migration, or implementation target not accepted or operationally proved |
| **NEEDS VERIFICATION** | Checkable state not verified strongly enough to act as fact |
| **UNKNOWN** | Not resolved by the inspected surfaces |
| **CONFLICTED** | Tracked surfaces make incompatible claims requiring a reviewed resolution |
| **HELD** | Current automation intentionally blocks graduation while preserving visible readiness checks |

### Inspected surfaces

- canonical ADR index and ADR operating contract;
- Directory Rules and adjacent ADR-0008;
- target ADR prior bytes;
- runtime model-adapter index and descriptive adapter note;
- `MockAdapter.py` and `OllamaAdapter.py`;
- Governed API WSGI application, route registry, and ABSTAIN scaffold;
- `DecisionEnvelope`, `RuntimeResponseEnvelope`, and `AIReceipt` schemas/contracts where present;
- generic RuntimeResponseEnvelope validator and selected fixtures;
- runtime policy stub;
- Focus mock readiness workflow and runtime-proof placeholder test;
- safe environment template.

### What this evidence does not prove

This revision does not prove:

- an executable `ModelAdapter` interface;
- a functioning `MockAdapter`, `NullAdapter`, `OllamaAdapter`, or remote-provider adapter;
- an accepted model or provider;
- a running local daemon or installed model;
- evidence retrieval or `EvidenceRef -> EvidenceBundle` closure;
- policy evaluation or obligation enforcement;
- citation validation;
- prompt-injection resistance;
- structured-output enforcement against an accepted adapter-response schema;
- AIReceipt emission or persistence;
- full RuntimeResponseEnvelope assembly;
- authentication, authorization, rate limiting, or deployed isolation;
- direct-client denial across every language, bundle, proxy, or deployment configuration;
- release, publication, or production readiness.

[Back to top](#top)

---

<a id="context"></a>

## Context

KFM treats AI as an interpretive capability, not a truth source. Evidence, source authority, policy, review, release state, correction lineage, and rollback support outrank generated language.

The architecture needs a stable boundary because provider APIs differ in request shape, output shape, streaming, tool calls, embeddings, model discovery, health reporting, error behavior, and usage metadata. Allowing those differences to leak into public contracts would couple KFM trust semantics to a provider.

The repository also carries several envelope-like objects. Without explicit boundaries, implementers can accidentally:

- return raw provider output as a client payload;
- conflate a policy decision with a client-facing runtime response;
- treat an AI receipt as proof that an answer is true;
- let the adapter itself decide rights, sensitivity, evidence closure, or release state;
- translate every negative state into generic text;
- create competing envelope schemas under runtime-, Focus-, package-, or UI-specific homes;
- store private prompts, sensitive context, or reasoning traces in receipts;
- make a local provider endpoint reachable from browsers.

### Forces

| Force | Architectural pressure |
|---|---|
| Evidence outranks generation | AI must remain downstream of resolvable support |
| Provider churn | Public and internal orchestration contracts must not depend on a vendor API |
| Cite-or-abstain | Missing support must produce a finite non-answer |
| Deterministic validation | Mock-first, no-network fixtures must precede live providers |
| Prompt injection | Retrieved material must be treated as data, not privileged instruction |
| Privacy and sensitivity | Context minimization and strict no-secret/no-raw-sensitive-data rules are required |
| Auditability | AI-mediated events need stable digests and support references |
| Reversibility | Providers and models must be disableable without changing client contracts |
| Public trust membrane | Clients must use governed APIs, never model endpoints or internal stores |

### Scope

This ADR decides:

- the provider-neutral adapter responsibility boundary;
- the separation among adapter execution, internal decision, client-facing envelope, and receipt;
- the finite outcome vocabulary at the governed runtime boundary;
- mock-first and no-network graduation discipline;
- provider/model admission and deactivation posture;
- minimum security, privacy, prompt-injection, citation, and receipt obligations;
- the public-client prohibition on direct model traffic.

This ADR does not decide:

- a specific provider or model;
- pricing, capacity, model quality, or vendor terms;
- the final language-level interface;
- the final `ModelAdapterRequest` or `ModelAdapterResponse` schema;
- final controlled vocabularies for reason codes, policy state, freshness, or correction state;
- the canonical Focus request/response object family;
- a model hosting topology;
- release approval or publication.

[Back to top](#top)

---

<a id="decision"></a>

## Decision

KFM proposes the following coupled architecture.

### D1. Provider-neutral adapter

Every model runtime is accessed through a provider-neutral adapter boundary under the canonical runtime adapter lane. Provider-specific transport, authentication, streaming, health, model discovery, and error translation remain behind that boundary.

The adapter is replaceable infrastructure. It is not:

- evidence authority;
- source authority;
- policy authority;
- citation authority;
- review authority;
- release authority;
- publication authority;
- a client contract.

### D2. Governed orchestration owns the outcome

The adapter returns an internal execution result or error to governed orchestration. The adapter must not independently decide that a response is evidence-supported, policy-allowed, citeable, releasable, or public-safe.

Governed orchestration performs prechecks and postchecks, then emits:

1. an internal `DecisionEnvelope` or equivalent decision object;
2. an `AIReceipt` for an AI-mediated event when one occurred;
3. a client-facing `RuntimeResponseEnvelope`.

### D3. Public finite outcomes

The governed runtime boundary uses exactly:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

No fifth public outcome is introduced for `HOLD`, `REVIEW`, `PARTIAL`, `DEGRADED`, `QUARANTINE`, or provider-specific error names. Those concepts belong in reason codes, obligations, review records, or operational-state fields.

### D4. Mock first

The first executable adapter must be deterministic, local, synthetic, no-network, and fixture-driven. A live provider is not a prerequisite for proving the adapter boundary.

`MockAdapter` graduation requires all four outcomes, invalid shapes, evidence gaps, citation gaps, policy denial, correction/withdrawal posture, adapter failure, safe diagnostics, and receipt behavior.

### D5. No direct model traffic

Browsers and normal public clients may call governed API surfaces only. They must not:

- call Ollama, OpenAI-compatible endpoints, or any provider directly;
- receive provider credentials;
- render raw provider responses;
- use model endpoints as health or capability APIs;
- infer access from model availability.

### D6. No generated truth

Model output may assist synthesis, classification, extraction, summarization, query rewriting, or drafting only within an accepted governed use case. It cannot establish:

- source authority;
- identity;
- evidence closure;
- rights or consent;
- sensitivity tier;
- policy result;
- review approval;
- release state;
- correction or withdrawal state;
- rollback completion;
- publication.

### D7. No private reasoning retention

KFM receipts and logs may store approved hashes, identifiers, timing, finite outcomes, reason codes, model/adapter references, support references, validation references, and safe diagnostics. They must not store private chain-of-thought, hidden reasoning traces, credentials, raw secrets, or unrestricted provider payloads.

### D8. Provider and model admission

A provider/model combination remains disabled until a reviewed admission record establishes:

- provider and model identity;
- immutable or reviewable version/digest;
- rights and terms posture;
- permitted data classes;
- network and tool permissions;
- context-size and output limits;
- timeout and retry policy;
- supported operations;
- deterministic-test profile;
- logging and redaction posture;
- deactivation and rollback procedure;
- accountable owner.

[Back to top](#top)

---

<a id="object-and-vocabulary-boundaries"></a>

## Object and vocabulary boundaries

### Current and proposed object roles

| Surface | Role | Current repository state | Must not become |
|---|---|---|---|
| Provider request/response | Provider-specific wire format inside one adapter | **UNKNOWN / provider-dependent** | Public contract or governance decision |
| `ModelAdapterRequest` / equivalent | Proposed provider-neutral invocation input | **NOT ESTABLISHED as canonical contract/schema** | Raw canonical-store dump or provider credential carrier |
| `ModelAdapterResponse` / equivalent | Proposed internal execution result | **NOT ESTABLISHED as canonical contract/schema** | Public envelope, policy decision, or evidence proof |
| `DecisionEnvelope` | Internal normalized finite decision and obligations | **CONFIRMED PROPOSED contract/schema surface** | Client payload by implication or release decision |
| `RuntimeResponseEnvelope` | Governed API/client-facing finite response posture | **CONFIRMED PROPOSED contract/schema and generic shape fixtures** | Raw model output or evidence store |
| `AIReceipt` | Accountability metadata for an AI-mediated event | **CONFIRMED PROPOSED contract/schema** | Truth proof, chain-of-thought store, or publication authority |
| `EvidenceBundle` | Evidence closure and inspectable support | Separate evidence authority | Generated summary |
| `PolicyDecision` | Policy outcome and obligations | Separate policy authority | Model preference |
| `PromotionDecision` / `ReleaseManifest` | Release-governance state | Separate release authority | Runtime answer |

### Vocabulary split

| Vocabulary | Values | Owner | Meaning |
|---|---|---|---|
| Runtime/policy outcome | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Decision/envelope contracts and policy | Governed response posture |
| Adapter execution status | **PROPOSED controlled set** such as `completed`, `failed`, `timed_out`, `cancelled`, `unavailable` | Adapter contract | Transport/execution result; never public truth |
| Operational state | `NORMAL`, `DEGRADED`, `ESCALATE`, `QUARANTINE`, or accepted equivalents | Runtime/operations contracts | Routing and observability |
| Review state | Review-record vocabulary | Review authority | Human review progress |
| Release decision | Release contract vocabulary | Release authority | Promotion/publication decision |
| Provider error | Provider-specific internally normalized reason | Adapter implementation | Diagnostic input to governed outcome selection |

The adapter must not map every transport error to `ABSTAIN`. A provider outage, malformed structured output, timeout after exhausted policy, or schema-validation failure normally supports `ERROR`. Insufficient evidence or unresolved citations normally supports `ABSTAIN`. Policy prohibition supports `DENY`.

### DecisionEnvelope versus RuntimeResponseEnvelope

The current Governed API stub emits fields accepted by the proposed `DecisionEnvelope` schema:

- `decision_id`;
- `outcome`;
- `policy_family`;
- `reasons`;
- `obligations`;
- `evaluated_at`;
- plus optional compatibility fields.

The stronger `RuntimeResponseEnvelope` requires:

- `id`;
- `spec_hash`;
- `version`;
- `issued_at`;
- `outcome`;
- `reason_code`;
- `evidence_refs`;
- `policy_state`;
- `freshness`;
- `correction_state`.

The proposed mature flow therefore treats the objects as related but distinct:

```text
DecisionEnvelope
  + released/policy-safe payload or safe non-answer
  + evidence / freshness / correction posture
  -> RuntimeResponseEnvelope
```

A separate ADR or contract change may later consolidate them, but this record does not silently collapse one into the other.

### AIReceipt relationship

`AIReceipt` records the AI execution boundary through:

- `id`;
- `run_id`;
- `adapter`;
- `model_ref`;
- input and output digests;
- policy-decision reference;
- citation-validation reference;
- finite outcome.

It does not replace either envelope. A client may receive a safe receipt reference where policy allows, but the receipt is not the rendered answer.

[Back to top](#top)

---

<a id="provider-neutral-adapter-boundary"></a>

## Provider-neutral adapter boundary

### Responsibility contract

The adapter boundary should support these provider-neutral capabilities where admitted:

| Capability | Requirement |
|---|---|
| Structured generation | Produce schema-targeted internal output or a normalized adapter error |
| Embeddings | Optional capability; separate policy/data-class admission required |
| Health | Safe internal health state, never a public model endpoint |
| Model information | Auditable model/provider/profile identity without secrets |
| Capability discovery | Explicit supported operations; no implicit provider feature use |
| Cancellation and timeout | Bounded execution and deterministic failure mapping |
| Usage metadata | Optional safe accounting fields; never authority |
| Tool invocation | Denied by default; explicit allowlist and governed tool adapter required |

No provider-neutral capability is considered implemented merely because the original ADR named a method.

### Proposed request minimum

A future canonical adapter request contract should include or reference:

- request/run/trace identity;
- operation type;
- bounded context identifier or approved context payload;
- evidence-support references;
- governing policy-decision reference;
- requested output schema and schema digest;
- model/profile selection reference;
- deterministic generation parameters where applicable;
- tool and network permissions;
- timeout and cancellation budget;
- sensitivity, rights, audience, purpose, freshness, and correction context;
- receipt and redaction posture.

It must not carry:

- direct source credentials;
- unrestricted RAW, WORK, or QUARANTINE payloads;
- canonical/internal store dumps;
- private keys or tokens;
- unbounded tool access;
- private reasoning instructions to persist;
- public-client-controlled system prompts.

### Proposed response minimum

A future canonical adapter response should include:

- adapter execution identity;
- provider/model/profile reference;
- normalized execution status;
- structured candidate output or safe absence;
- provider-neutral finish reason;
- timing and bounded usage metadata where allowed;
- schema-validation status;
- safe diagnostics;
- input/output digests or digest inputs needed by receipt assembly.

It must not claim:

- evidence resolution;
- citation validity;
- policy approval;
- release approval;
- public safety;
- final finite outcome without orchestration validation.

### Error normalization

Adapters translate provider failures into stable internal categories. Raw provider messages may contain paths, prompts, context fragments, infrastructure identifiers, or sensitive details and therefore must not pass directly to clients.

Proposed internal categories include:

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

The final governed outcome is chosen after policy and context:

- `ABSTAIN` for support insufficiency;
- `DENY` for policy prohibition;
- `ERROR` for machinery/runtime failure;
- `ANSWER` only after every required postcheck passes.

[Back to top](#top)

---

<a id="governed-runtime-flow"></a>

## Governed runtime flow

### Proposed sequence

```text
public request
  -> governed API authenticates and normalizes scope
  -> resolve released or explicitly review-authorized data
  -> resolve required EvidenceRefs to admissible EvidenceBundles
  -> evaluate rights, sensitivity, consent, access, freshness, correction, and release policy
  -> decide whether model invocation is allowed
  -> build bounded provider-neutral adapter request
  -> execute MockAdapter or admitted provider adapter
  -> validate structured output
  -> validate citations and claim-to-evidence support
  -> run post-generation policy and redaction checks
  -> emit internal DecisionEnvelope
  -> emit AIReceipt when AI execution occurred
  -> assemble RuntimeResponseEnvelope
  -> public client renders only permitted fields and obligations
```

### Pre-invocation gates

Model invocation must not occur when:

- no model is needed to answer deterministically;
- scope is unsupported;
- required evidence cannot be resolved;
- rights or sensitivity posture forbids context transfer;
- consent is missing or revoked where required;
- release/correction/withdrawal state forbids use;
- provider/model admission does not permit the data class;
- tool or network permissions are missing;
- the requested output schema is absent or unacceptable.

A pre-invocation `ABSTAIN` or `DENY` may produce no AIReceipt because no AI event occurred. The runtime envelope and policy/run receipts must make that distinction visible.

### Post-invocation gates

An adapter execution cannot become `ANSWER` until:

- structured output validates;
- all consequential claims are supported;
- citations resolve and match claims;
- output contains no prohibited content;
- policy obligations are enforceable by the caller;
- freshness and correction state remain acceptable;
- diagnostics and receipt fields are safely redacted;
- the public envelope is valid.

### No hidden fetches

The adapter may use only:

- context explicitly supplied by governed orchestration;
- tools explicitly admitted for the operation;
- network access explicitly permitted by policy and configuration.

It must not perform hidden source discovery, read local repositories, inspect environment secrets, call arbitrary URLs, access canonical/internal stores, or expand scope without a new governed request.

[Back to top](#top)

---

<a id="finite-outcomes"></a>

## Finite outcomes

| Outcome | Use when | Required response posture |
|---|---|---|
| `ANSWER` | A bounded response is evidence-supported, policy-permitted, citation-valid, fresh enough, correction-safe, release-compatible, schema-valid, and safe to render | Include required evidence refs, notices, obligations, and safe receipt linkage |
| `ABSTAIN` | Evidence, citation support, source authority, scope, corroboration, or freshness is insufficient after allowed narrowing | Explain the support gap safely; preserve reproducible handles; do not guess |
| `DENY` | Access, rights, sensitivity, consent, release state, tool use, provider use, or other policy forbids the operation | Do not reveal protected payload; return safe reason codes and obligations |
| `ERROR` | Adapter, provider, policy engine, validator, schema, configuration, receipt, or infrastructure failure prevents a trustworthy result | Return safe diagnostics; no silent fallback or inferred answer |

### Narrowed answers

When KFM can answer a smaller, less precise, generalized, or otherwise policy-safe scope with adequate evidence, the result may remain `ANSWER` with an explicit narrowed scope. It must not pretend to answer the original broader scope.

### Partial provider output

Partial or streamed provider output is never independently renderable. The governed path may:

- discard it and return `ERROR`;
- validate a complete bounded subset and return a narrowed `ANSWER`;
- return `ABSTAIN` when support is insufficient.

It must not expose incomplete raw text.

### Outcome precedence

Composition across required gates follows the accepted finite-outcome contract. This ADR does not create an independent arithmetic rule. At minimum:

- any unresolved machinery failure prevents `ANSWER`;
- any applicable policy `DENY` prevents `ANSWER`;
- any required evidence/citation `ABSTAIN` prevents an unsupported `ANSWER`;
- `ANSWER` requires all mandatory gates to support rendering.

### Reason codes

Reason codes must be:

- stable;
- machine-readable;
- safe to expose;
- mapped to one finite outcome;
- free of protected content;
- versioned or append-only when public clients depend on them.

Provider-specific error strings are not public reason codes.

[Back to top](#top)

---

<a id="security-privacy-and-prompt-injection"></a>

## Security, privacy, and prompt injection

### Source content is data

Retrieved documents, Markdown, YAML, JSON, metadata, issue text, pull-request text, transcripts, labels, and map attributes are untrusted data. Instruction-shaped content inside evidence does not gain system, developer, policy, or tool authority.

Controls must include:

- clear separation of system policy from retrieved content;
- output-schema enforcement;
- tool allowlists;
- URL and network allowlists;
- context-size limits;
- source-role and sensitivity labels;
- prompt/template versioning and hashing;
- post-generation claim/citation validation;
- safe logging and redaction;
- adversarial fixtures.

### Data minimization

Only context necessary for the bounded operation may reach an adapter. Sensitive fields should be:

- omitted;
- redacted;
- generalized;
- aggregated;
- tokenized;
- replaced with governed references;

as required by policy.

### Living persons, DNA, archaeology, rare species, and infrastructure

Deny-first domains require independent rights, consent, sensitivity, and release gates. A local model does not make sensitive transfer safe. A public source does not automatically authorize inference, joining, embedding, or republication.

### Tool use

Tool use is denied by default. A model may request an action, but governed orchestration decides whether the action is:

- supported;
- authorized;
- scoped;
- replayable;
- auditable;
- reversible.

The model never receives unrestricted shell, filesystem, database, browser, source-registry, or publication access.

### Direct-client and network boundary

- Governed API and model endpoints bind to loopback by default for local development.
- Public clients never receive model endpoint locations.
- Reverse proxies must not expose provider routes by convenience.
- Provider credentials remain in approved secret stores.
- Egress is denied or allowlisted according to the admitted provider profile.
- Streaming must terminate at governed orchestration; raw provider streams do not cross the trust membrane.

### Safe diagnostics

Public diagnostics must not contain:

- prompts;
- hidden instructions;
- chain-of-thought;
- raw evidence;
- personal or restricted data;
- exact sensitive locations;
- provider credentials;
- internal paths;
- stack traces;
- model-host topology.

[Back to top](#top)

---

<a id="receipts-observability-and-retention"></a>

## Receipts, observability, and retention

### AIReceipt minimum

The current proposed schema requires:

- receipt identity;
- run identity;
- adapter;
- model reference;
- input/output digests;
- policy-decision reference;
- citation-validation reference;
- finite outcome.

Those fields are a useful minimum but do not yet prove:

- the referenced objects resolve;
- canonicalization is consistent;
- prompt/template identity is captured;
- output schema identity is captured;
- tool calls are recorded;
- timing and retry behavior are recorded;
- redaction posture is captured;
- receipt persistence is implemented.

### Proposed additional accountability fields

A future version should evaluate whether to add or reference:

- adapter contract version;
- provider profile digest;
- model profile digest;
- prompt/template digest;
- output schema digest;
- bounded context digest;
- evidence-bundle refs actually used;
- policy bundle digest;
- citation-validation summary;
- tool-call receipt refs;
- start/end timestamps and duration;
- timeout/retry count;
- redaction/generalization receipt refs;
- correction/withdrawal lineage;
- runtime and library versions;
- safe failure category.

These are **PROPOSED** until a contract/schema change is reviewed.

### No chain-of-thought storage

Receipts and logs record accountability, not private reasoning. They must not store:

- hidden chain-of-thought;
- unrestricted scratchpads;
- raw system prompts where disclosure is unsafe;
- sensitive raw context;
- full provider payloads by default.

A policy-approved prompt/template may be stored separately as versioned configuration when needed; receipts should ordinarily carry its digest/reference.

### Observability

Metrics may include:

- finite outcomes by route and reason;
- adapter/provider/model profile;
- duration, timeout, retry, and safe error category;
- citation pass/fail/abstain rate;
- policy denial/abstention rate;
- schema-validation failure rate;
- context and output size buckets;
- tool-use counts by admitted capability.

Metrics must preserve telemetry-redaction policy and must not become a covert sensitive-data or prompt store.

### Retention and correction

Retention depends on policy, sensitivity, incident needs, and release significance. A correction, withdrawal, consent revocation, source revocation, or evidence supersession must be able to locate affected receipts and derived outputs without treating the receipt as the canonical answer.

[Back to top](#top)

---

<a id="authority-and-publication-boundary"></a>

## Authority and publication boundary

| Responsibility | Owning surface | Adapter/envelope role |
|---|---|---|
| Human architecture decision | `docs/adr/` | This ADR proposes the boundary |
| Provider-neutral runtime lane | `runtime/model_adapters/` | Adapter cards and implementations after review |
| Provider-specific runtime wiring | `runtime/ollama/`, approved runtime/provider lanes | Internal transport only |
| Semantic object meaning | `contracts/` | Own request, response, envelope, receipt, policy, evidence, and release meaning |
| Machine-checkable shape | `schemas/contracts/v1/` | Own JSON Schema |
| Policy and obligations | `policy/` | Decide admissibility; model cannot override |
| Evidence closure | Evidence contracts, resolvers, `data/proofs/`, approved evidence homes | Resolve support before `ANSWER` |
| Citation validation | Approved validator/service surfaces | Validate generated claims and citations |
| Runtime implementation | `runtime/`, approved packages, and `apps/governed-api/` | Execute bounded orchestration |
| Public API boundary | `apps/governed-api/` | Emit governed RuntimeResponseEnvelope |
| Client rendering | `apps/explorer-web/` and approved public clients | Obey envelope and obligations |
| Receipts and proofs | `data/receipts/`, `data/proofs/` under accepted contracts | Record support and accountability |
| Release, correction, withdrawal, rollback | `release/` | Authorize public state |
| Lifecycle data | `data/` phase roots | Never become direct model/public stores |

A model adapter, envelope, receipt, workflow, or generated answer does not publish anything. Public state still requires the appropriate release, rights, sensitivity, review, correction, and rollback controls.

[Back to top](#top)

---

<a id="current-repository-evidence"></a>

## Current repository evidence

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| ADR identity | **CONFIRMED** in [`INDEX.md`](./INDEX.md) | Exact path is ADR-0019 |
| ADR status | Source `draft`; effective `proposed` | Not accepted |
| Canonical adapter lane | `runtime/model_adapters/README.md` | Provider-neutral runtime handoff lane is documented |
| Compatibility adapter lane | `runtime/adapters/` | Must not become a parallel canonical adapter home |
| Adapter semantic contract | **NOT ESTABLISHED as canonical contract/schema** | `AdapterContract.md` is descriptive runtime guidance only |
| `MockAdapter.py` | One-line placeholder | No deterministic adapter behavior |
| `OllamaAdapter.py` | One-line placeholder | No Ollama client implementation |
| Example runtime selection | `.env.example` sets `KFM_MODEL_RUNTIME=mock` | Safe configuration example only |
| Example Ollama host | Loopback `127.0.0.1:11434` | Does not start or approve Ollama |
| Governed API | Minimal WSGI app with three GET routes | Executable scaffold, not governed AI |
| Governed API response | Deterministic `ABSTAIN` / `NOT_IMPLEMENTED` | Fail-closed DecisionEnvelope-shaped subset |
| `DecisionEnvelope` | Proposed contract/schema present | Internal finite decision surface exists in documentation/schema |
| `RuntimeResponseEnvelope` | Proposed contract/schema, validator, generic fixtures | Shape slice exists; runtime assembly not proved |
| Generic valid envelope fixtures | `ANSWER` and `ABSTAIN` | No generic valid DENY/ERROR fixture in current bounded set |
| Runtime-proof finite-outcome test | `assert True` placeholder | No executable behavioral proof |
| Focus-local runtime envelope schema | Empty permissive PROPOSED scaffold | Competing/unfinished envelope surface |
| `AIReceipt` | Proposed contract/schema present | Accountability shape exists; no persistence or runtime emission proved |
| Runtime policy | README-only greenfield stub | No accepted runtime policy |
| Focus mock workflow | Read-only static checks and explicit holds | No mock request, adapter, model, envelope, or receipt is executed |
| Direct public model client | Not surfaced in bounded search | Not proof of repository-wide absence |
| Provider/model admission registry | **NOT ESTABLISHED** | No model/provider is approved |
| Citation validator integration | **NOT ESTABLISHED** | `ANSWER` support is not operationally proved |
| Release/publication | **DENIED as inference** | No AI response is KFM publication |

### Material corrections in this revision

- Confirms ADR identity and removes obsolete path/number uncertainty.
- Replaces “repo depth unknown” with current repository evidence.
- Corrects the statement that the envelope is the adapter’s public face: the governed API and `RuntimeResponseEnvelope` are the public boundary; adapter output remains internal.
- Separates `DecisionEnvelope`, `RuntimeResponseEnvelope`, and `AIReceipt`.
- Records that `FocusRequest` and canonical adapter request/response contracts remain unresolved.
- Records the placeholder state of both adapter implementations.
- Records the current Governed API’s deterministic ABSTAIN scaffold.
- Records that generic envelope shape validation is not mock runtime proof.
- Records the explicit Focus workflow holds and incomplete four-outcome coverage.
- Adds provider/model admission, deactivation, tool-use, prompt-injection, telemetry, correction, and rollback requirements.

[Back to top](#top)

---

<a id="current-implementation-maturity"></a>

## Current implementation maturity

| Capability | Current state | Graduation requirement |
|---|---|---|
| ADR identity | **CONFIRMED** | Human acceptance review |
| Provider-neutral runtime lane | **CONFIRMED documentation** | Accepted semantic contract and implementation |
| Adapter request/response contract | **NOT ESTABLISHED** | Contract, schema, fixtures, validator, compatibility policy |
| Mock adapter | **PLACEHOLDER** | Deterministic implementation and full test matrix |
| Ollama adapter | **PLACEHOLDER** | Provider admission, loopback isolation, tests, policy, rollback |
| Governed API | **MINIMAL EXECUTABLE ABSTAIN SCAFFOLD** | Auth/policy/evidence/citation/orchestration and full client envelope |
| DecisionEnvelope | **PROPOSED contract/schema** | Accepted semantics, fixtures, validators, caller behavior |
| RuntimeResponseEnvelope | **PROPOSED shape slice** | Full fixture coverage, mock production, client tests, state vocabularies |
| AIReceipt | **PROPOSED contract/schema** | Runtime emission, persistence, ref resolution, retention, redaction |
| Runtime policy | **STUB** | Meaningful rules, fixtures, tests, bundle identity, evaluator |
| Evidence resolution | **NOT ESTABLISHED for AI path** | Resolver integration and negative-state tests |
| Citation validation | **NOT ESTABLISHED for AI path** | Claim/citation contract, validator, fixtures, enforcement |
| Prompt-injection protection | **NOT ESTABLISHED** | Threat model, fixtures, tool/network controls, tests |
| Mock Focus runtime | **WORKFLOW_HOLD** | Accepted command and deterministic fixtures |
| Four-outcome runtime proof | **WORKFLOW_HOLD** | Generated ANSWER/ABSTAIN/DENY/ERROR and invalid/error cases |
| Direct-client enforcement | **PARTIAL structural evidence** | Static, dependency, network, proxy, browser, and deployment checks |
| Provider/model admission | **NOT ESTABLISHED** | Reviewed profile and registry/decision object |
| Production deployment | **UNKNOWN** | Security, operations, review, release, rollback evidence |

### Current Governed API boundary

Current source confirms:

```text
GET /bootstrap -> ABSTAIN / NOT_IMPLEMENTED
GET /layers    -> ABSTAIN / NOT_IMPLEMENTED
GET /evidence  -> ABSTAIN / NOT_IMPLEMENTED
```

The WSGI application:

- permits only registered GET routes;
- returns JSON;
- returns `404` or `405` otherwise;
- does not invoke an adapter;
- does not resolve evidence;
- does not evaluate runtime policy;
- does not validate citations;
- does not emit AIReceipt;
- does not emit the complete RuntimeResponseEnvelope.

### Current Focus workflow boundary

The workflow intentionally confirms that:

- `MockAdapter.py` is still the exact one-line placeholder;
- mock runtime lanes remain README-only;
- Focus request/response schemas remain permissive scaffolds;
- no Focus fixture payload exists;
- no repository-native mock Focus command exists;
- generic RuntimeResponseEnvelope fixtures cover `ANSWER` and `ABSTAIN`;
- the runtime-proof test is still an assert-true placeholder;
- no mock-generated envelope or AIReceipt is produced.

The resulting green state is a **HOLD**, not runtime success.

[Back to top](#top)

---

<a id="implementation-and-convergence-plan"></a>

## Implementation and convergence plan

Use the smallest reversible sequence. Do not activate Ollama first.

### Phase 0 — preserve the hold

- Keep ADR-0019 proposed.
- Keep `KFM_MODEL_RUNTIME=mock`.
- Keep provider endpoints loopback-only.
- Do not add direct browser/provider integrations.
- Preserve explicit workflow holds until reviewed replacements exist.

### Phase 1 — converge object authority

1. Decide the canonical semantic home and names for provider-neutral adapter request/response.
2. Decide whether Focus request/response are callers of the generic adapter contract or separate contracts.
3. Reconcile the generic runtime envelope with the empty Focus-local envelope schema.
4. Pin relationship rules among `DecisionEnvelope`, `RuntimeResponseEnvelope`, `AIReceipt`, `PolicyDecision`, and evidence/citation objects.
5. Define reason-code and state vocabularies or stable registry references.
6. Add migration notes for compatibility paths; do not create parallel authority.

### Phase 2 — implement deterministic MockAdapter

1. Implement one provider-neutral interface in `runtime/model_adapters/` or an ADR-confirmed implementation package.
2. Implement `MockAdapter` without network, clock nondeterminism, hidden I/O, or uncontrolled randomness.
3. Add valid fixtures for all four outcomes.
4. Add invalid fixtures for malformed request, malformed response, unsupported operation, schema mismatch, and unsafe diagnostics.
5. Add evidence-gap, citation-gap, policy-deny, sensitive-data-deny, correction/withdrawal, timeout, tool-deny, and adapter-error cases.
6. Emit deterministic internal adapter results; do not generate public envelopes inside the adapter.

### Phase 3 — wire governed orchestration

1. Add a governed API orchestration path behind authentication/authorization as appropriate.
2. Resolve released or explicitly review-authorized state through governed interfaces.
3. Evaluate pre-invocation policy.
4. Invoke only the admitted mock adapter.
5. Validate structured output and citations.
6. Evaluate post-generation policy and redaction.
7. Emit DecisionEnvelope, AIReceipt, and complete RuntimeResponseEnvelope.
8. Add client contract tests proving raw adapter/provider output cannot escape.

### Phase 4 — receipts and correction

- Persist AIReceipt to an accepted receipt lane.
- Resolve policy and citation refs.
- Link runtime envelope, request/run identity, adapter/model profile, and evidence support.
- Prove redaction and no-chain-of-thought behavior.
- Add correction, withdrawal, consent-revocation, and cache/derivative invalidation tests.
- Define replay and retention posture.

### Phase 5 — provider/model admission

Before Ollama or another provider:

- create a reviewed provider/model profile;
- pin model identity or digest;
- review rights and intended data classes;
- deny public exposure;
- enforce loopback or reviewed network topology;
- configure timeout, rate, context, output, and concurrency limits;
- disable tools by default;
- add no-secret and no-raw-sensitive-data tests;
- implement health and failure normalization;
- prove one-command deactivation and fallback to mock/disabled mode.

### Phase 6 — live adapter canary

- Add provider adapter behind the same contract.
- Run local/restricted canary only.
- Compare finite outcomes and receipt shape against MockAdapter.
- Prove provider substitution does not change client contracts or policy.
- Keep public `ANSWER` disabled until release review permits it.
- Record incident, rollback, and model-revocation procedures.

### Phase 7 — public graduation

Public AI-mediated `ANSWER` requires:

- accepted ADR and contracts;
- full policy/evidence/citation closure;
- secure deployment;
- client obligations;
- observability and redaction;
- correction/withdrawal/rollback;
- accountable review and release state.

[Back to top](#top)

---

<a id="acceptance-gates"></a>

## Acceptance gates

ADR-0019 should remain proposed until reviewers verify the decision is coherent with adjacent ADRs and the following implementation plan is feasible.

### Decision acceptance gates

- [ ] ADR identity, title, status, owners, and affected roots are reviewed.
- [ ] ADR-0004, ADR-0008, ADR-0020, ADR-0025, and relevant evidence/policy/release ADRs are reconciled.
- [ ] The canonical provider-neutral adapter responsibility is approved.
- [ ] The object separation among adapter result, DecisionEnvelope, RuntimeResponseEnvelope, and AIReceipt is approved.
- [ ] The no-direct-model-client and no-generated-truth rules are approved.
- [ ] Mock-first, provider admission, and deactivation rules are approved.
- [ ] The ADR and canonical index move to matching reviewed `accepted` status in the same governed change.

### Implementation graduation gates

- [ ] Canonical adapter request/response contracts exist.
- [ ] Paired closed schemas exist with positive and negative fixtures.
- [ ] `MockAdapter` is executable, deterministic, no-network, and provider-neutral.
- [ ] All four outcomes are produced by behavior tests, not hand-authored fixture files alone.
- [ ] Invalid shapes and runtime failures fail closed.
- [ ] Governed API emits the complete accepted RuntimeResponseEnvelope.
- [ ] Raw adapter/provider output cannot reach a client.
- [ ] Evidence resolution and citation validation gate every consequential `ANSWER`.
- [ ] Meaningful runtime policy and obligations are evaluated.
- [ ] AIReceipt is emitted, persisted, validated, and linked.
- [ ] No chain-of-thought, secret, raw sensitive context, or unsafe diagnostic is persisted or exposed.
- [ ] Prompt-injection and tool-use negative tests exist.
- [ ] Correction, withdrawal, revocation, retention, and rollback paths are tested.
- [ ] Direct-client restrictions are checked across code, dependencies, browser bundles, proxy configuration, and deployment.
- [ ] At least one provider can be disabled without changing the public contract.
- [ ] A live provider is not admitted until its own reviewed gates pass.

### What a green shape test proves

A passing generic RuntimeResponseEnvelope fixture validator proves only that selected JSON examples match the selected proposed schema.

It does not prove:

- a model ran;
- a mock adapter ran;
- evidence resolved;
- citations are valid;
- policy allowed the response;
- a receipt was persisted;
- a public client obeyed obligations;
- release or publication occurred.

[Back to top](#top)

---

<a id="consequences"></a>

## Consequences

### Positive

- Provider changes do not redefine public trust semantics.
- Public clients receive one finite envelope boundary.
- Model execution remains subordinate to evidence and policy.
- Mock-first development permits deterministic no-network CI.
- Negative states become inspectable instead of fluent fallback.
- AIReceipt enables accountability without elevating generated output to truth.
- Provider/model deactivation becomes a configuration and release action rather than a client migration.
- Prompt-injection, tool-use, privacy, and correction controls are treated as architecture concerns.

### Costs

- More contracts and explicit object relationships are required.
- Adapter implementation cannot begin responsibly without convergence work.
- Structured-output and citation validation add latency and complexity.
- Mock fixtures must cover more than happy-path text generation.
- Provider features may be intentionally unavailable when they do not fit the contract.
- Receipt, redaction, and retention design require cross-root review.
- Full direct-client enforcement spans code, dependency graphs, proxies, and deployment.

### Tradeoffs

- Provider neutrality may hide useful provider-specific capabilities. Those may be exposed through optional, explicitly admitted capability profiles without changing the public envelope.
- Determinism can reduce realism. Mock tests prove contracts; separate canaries prove provider behavior.
- Finite outcomes simplify clients but require stable reason and obligation vocabularies.
- Not storing raw prompts or reasoning improves privacy but may limit debugging. Safe digests, approved templates, fixtures, and bounded incident captures are the preferred alternative.

[Back to top](#top)

---

<a id="alternatives-considered"></a>

## Alternatives considered

| Alternative | Decision |
|---|---|
| Browser calls local or hosted model directly | Rejected: bypasses governed API, policy, evidence, receipts, and release |
| Provider SDK objects become public API types | Rejected: provider lock-in and trust-semantic leakage |
| Adapter returns RuntimeResponseEnvelope directly | Rejected: lets provider/runtime layer collapse orchestration, policy, citation, freshness, and correction responsibilities |
| One generic free-text response with optional warnings | Rejected: negative states become ambiguous and unsafe |
| Add `HOLD` or `REVIEW` as a fifth public outcome | Rejected: use `ABSTAIN` plus obligations/review state |
| Make `MockAdapter` optional and start with Ollama | Rejected: loses deterministic no-network proof |
| Store complete prompts/provider payloads for audit | Rejected by default: privacy, sensitivity, injection, and retention risks |
| Treat AIReceipt as proof of correctness | Rejected: receipt records process accountability only |
| Use only RuntimeResponseEnvelope and remove DecisionEnvelope | Deferred: requires contract and caller analysis; current objects have distinct roles |
| Use only DecisionEnvelope as the public shape | Deferred/rejected for current proposal: it lacks the stronger client-facing freshness/correction contract |
| Separate adapter interface per provider | Rejected as canonical approach; provider-specific code stays behind one boundary |

[Back to top](#top)

---

<a id="risk-and-open-question-ledger"></a>

## Risk and open-question ledger

| Risk / question | Current state | Required next step |
|---|---|---|
| Canonical adapter request/response names and homes | **OPEN** | Contract/schema design review |
| `FocusRequest` relationship to adapter request | **OPEN** | Decide caller-specific versus generic object |
| Generic versus Focus-local RuntimeResponseEnvelope schema | **CONFLICTED / unfinished** | Consolidate or document compatibility |
| DecisionEnvelope versus RuntimeResponseEnvelope | **OPEN but bounded here** | Preserve distinct roles until reviewed convergence |
| Reason-code registry | **NOT ESTABLISHED** | Define stable owner/versioning |
| `policy_state`, `freshness`, `correction_state` vocabularies | **NEEDS VERIFICATION** | Contract/schema/policy alignment |
| AIReceipt reference resolution | **NOT ESTABLISHED** | Validators and repository placement |
| Canonicalization of AI input/output digests | **NEEDS VERIFICATION** | Pin accepted canonicalization profile |
| Prompt/template storage and hashing | **OPEN** | Security, privacy, reproducibility review |
| Streaming | **OPEN** | Define governed buffering, cancellation, and no-raw-stream rule |
| Embeddings | **OPEN / separate risk** | Data-class, retention, re-identification, and index policy |
| Tool invocation | **DENY by default** | Capability contract and per-tool governance |
| Provider/model admission object | **NOT ESTABLISHED** | Registry/decision contract and review flow |
| Model rights and redistribution | **NEEDS VERIFICATION per model** | Source/rights review |
| Local daemon exposure | **LOOPBACK example only** | Deployment and network enforcement |
| Direct-client static enforcement | **PARTIAL** | Extend code/dependency/proxy/browser checks |
| Adapter correction and revocation propagation | **NOT ESTABLISHED** | Receipt lineage and downstream invalidation |
| Runtime receipt retention | **OPEN** | Retention and sensitivity policy |
| Public AI `ANSWER` | **NOT AUTHORIZED by current evidence** | All acceptance and release gates |

### High-risk anti-patterns

- importing provider SDK types into public DTOs;
- embedding model endpoint URLs in browser code;
- using a model answer when evidence resolution failed;
- treating a public source as permission to infer or join sensitive data;
- storing raw prompts, provider payloads, or chain-of-thought in receipts;
- enabling unrestricted tools or network access;
- returning a schema-valid envelope whose support refs are unresolved;
- interpreting adapter health as release readiness;
- switching providers without new model/profile identity in receipts;
- suppressing `ABSTAIN` to improve answer-rate metrics;
- treating an AI-generated correction as an approved correction.

[Back to top](#top)

---

<a id="rollback-and-supersession"></a>

## Rollback and supersession

### Documentation rollback

This revision is documentation-only. Roll back by reverting its commit or restoring the prior target blob recorded in the metadata block. That rollback does not alter any runtime, provider, model, policy, receipt, envelope, release, or public state.

### Decision rollback

If ADR-0019 is later accepted and then replaced:

1. author a successor ADR;
2. record reciprocal supersession links;
3. preserve this record;
4. define contract/schema compatibility and data migration;
5. preserve historical receipts under their original versions;
6. update the canonical ADR index;
7. test provider deactivation and public-envelope compatibility.

### Runtime/provider deactivation

Every admitted provider must have a reversible deactivation path:

```text
provider-backed adapter
  -> disabled
  -> deterministic MockAdapter or Null/disabled mode
  -> governed ABSTAIN or DENY envelope
```

Deactivation must not:

- expose raw provider errors;
- silently fall back to another unreviewed provider;
- convert missing evidence into an answer;
- invalidate historical receipts;
- alter public envelope shape without versioning.

### Incident rollback

On provider compromise, model revocation, prompt-injection incident, unsafe output, rights change, consent revocation, or receipt-integrity failure:

- disable the provider/model profile;
- deny or abstain affected operations;
- preserve incident and receipt identifiers;
- identify affected responses and derivatives;
- issue correction/withdrawal records where required;
- invalidate caches, indexes, summaries, exports, and public derivatives;
- return clients to a safe governed envelope state;
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
| Directory Rules responsibility | **CONFIRMED** — `docs/adr/` owns the decision record |
| Canonical runtime adapter lane | **CONFIRMED documentation** |
| Adapter semantic contract/schema | **NOT ESTABLISHED** |
| MockAdapter implementation | **CONFIRMED placeholder** |
| OllamaAdapter implementation | **CONFIRMED placeholder** |
| Governed API executable scaffold | **CONFIRMED** |
| Governed API model invocation | **NOT ESTABLISHED** |
| Governed API complete RuntimeResponseEnvelope | **NOT ESTABLISHED** |
| DecisionEnvelope contract/schema | **CONFIRMED PROPOSED** |
| RuntimeResponseEnvelope contract/schema | **CONFIRMED PROPOSED** |
| RuntimeResponseEnvelope generic validator | **CONFIRMED** |
| Generic valid outcome fixtures | **CONFIRMED ANSWER and ABSTAIN only** |
| Runtime finite-outcome behavior test | **CONFIRMED assert-true placeholder** |
| AIReceipt contract/schema | **CONFIRMED PROPOSED** |
| AIReceipt runtime persistence | **NOT ESTABLISHED** |
| Runtime policy | **CONFIRMED greenfield stub** |
| Focus mock workflow | **CONFIRMED explicit HOLD** |
| Evidence/citation integration | **NOT ESTABLISHED** |
| Prompt-injection and tool-use tests | **NOT ESTABLISHED** |
| Provider/model admission | **NOT ESTABLISHED** |
| Direct-client prohibition | **CONFIRMED doctrine; enforcement incomplete** |
| Local tests and ADR validator for this edit | **NOT RUN** |
| Pull-request automation | **PENDING after PR creation** |
| Release or publication | **NOT CLAIMED** |

Remote repository reads establish exact bytes, source relationships, and declared workflow behavior. They do not substitute for executing a mock adapter, policy evaluator, evidence resolver, citation validator, provider, receipt store, governed client, release gate, or public deployment.

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
- [`Directory Rules`](../architecture/directory-rules.md)

### Current implementation and contract evidence

- [`runtime/model_adapters/README.md`](../../runtime/model_adapters/README.md)
- [`runtime/model_adapters/AdapterContract.md`](../../runtime/model_adapters/AdapterContract.md)
- [`runtime/model_adapters/MockAdapter.py`](../../runtime/model_adapters/MockAdapter.py)
- [`runtime/model_adapters/OllamaAdapter.py`](../../runtime/model_adapters/OllamaAdapter.py)
- [`runtime/model_adapters/mock/README.md`](../../runtime/model_adapters/mock/README.md)
- [`runtime/ollama/README.md`](../../runtime/ollama/README.md)
- [`apps/governed-api/README.md`](../../apps/governed-api/README.md)
- [`Governed API application`](../../apps/governed-api/src/governed_api/main.py)
- [`Governed API route registry`](../../apps/governed-api/src/governed_api/routes/registry.py)
- [`Governed API ABSTAIN scaffold`](../../apps/governed-api/src/governed_api/stub.py)
- [`DecisionEnvelope contract`](../../contracts/runtime/decision_envelope.md)
- [`DecisionEnvelope schema`](../../schemas/contracts/v1/runtime/decision_envelope.schema.json)
- [`RuntimeResponseEnvelope contract`](../../contracts/runtime/runtime_response_envelope.md)
- [`RuntimeResponseEnvelope schema`](../../schemas/contracts/v1/runtime/runtime_response_envelope.schema.json)
- [`RuntimeResponseEnvelope validator`](../../tools/validators/validate_runtime_response_envelope.py)
- [`RuntimeResponseEnvelope fixtures`](../../fixtures/contracts/v1/runtime/runtime_response_envelope/)
- [`AIReceipt contract`](../../contracts/runtime/ai_receipt.md)
- [`AIReceipt schema`](../../schemas/contracts/v1/runtime/ai_receipt.schema.json)
- [`Runtime policy stub`](../../policy/runtime/README.md)
- [`Focus mock readiness workflow`](../../.github/workflows/focus-mock-test.yml)
- [`Finite-envelope runtime-proof placeholder`](../../tests/runtime_proof/test_envelope_finite_outcomes.py)
- [`.env.example`](../../.env.example)

---

## Last reviewed

**2026-07-24** — repository-grounded review against `main@9ffa0f56197ea1dad3290626b4c166e2bebc3bff`.

Review again when:

- this ADR changes status;
- a canonical adapter request/response contract or schema lands;
- `MockAdapter.py` or `OllamaAdapter.py` becomes executable;
- the Governed API adds an AI-mediated route;
- DecisionEnvelope and RuntimeResponseEnvelope are consolidated or rewired;
- the Focus-local envelope schema changes;
- runtime policy becomes executable;
- citation validation or EvidenceBundle resolution is wired;
- AIReceipt persistence lands;
- a provider/model admission record is created;
- direct-client/proxy/deployment enforcement changes;
- six months pass without review.

[Back to top](#top)
