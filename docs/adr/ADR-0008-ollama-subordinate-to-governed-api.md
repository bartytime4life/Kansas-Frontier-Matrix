<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/adr/0008-ollama-subordinate-to-governed-api
title: "ADR-0008 — Ollama and Local AI Runtimes Are Subordinate to the Governed API"
type: adr
adr_id: ADR-0008
version: v1.4
status: draft
effective_decision_status: proposed
owners:
  - "OWNER_TBD — runtime / governed-AI stewardship assignment is not verified"
reviewers_required:
  - Architecture steward
  - Governed API steward
  - Runtime / governed-AI steward
  - Policy and security reviewer
  - Evidence / citation reviewer
  - Contracts / schemas reviewer
  - Docs steward
created: 2026-05-10
updated: 2026-09-12
policy_label: public
truth_posture: "CONFIRMED current repository source and bounded test surfaces / PROPOSED decision and provider admission / UNKNOWN live runtime, model inventory, deployment, and release use"
owning_root: docs/
responsibility: "Record the proposed local-AI provider boundary, reconcile it with current repository evidence, and keep provider, model, evidence, policy, citation, receipt, release, and publication authority separate."
current_path: docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
supersedes: []
superseded_by: []
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: c6aa9602883eeda6282a7ca981981327674777a1
  target_before_update_blob: 7eeae617986d053699da66c0f5cd0df063902ef7
  adr_index_blob: 0c143676dfd3c1bda16cb44398c5ad5d4a49cf67
  adr_0004_blob: 32a734f02187ef774731337e438fed567a71dc39
  adr_0019_blob: 5c45cbaf0aae510638088913757634ea978c9ec3
  adr_0020_blob: 76cec0944d2174222c7508d7175e492cd834cb41
  adr_0029_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  ollama_integration_doc_blob: 1a2c8445d8ad87ca1a012d8f284c38d907cd7c71
  runtime_ollama_readme_blob: b0708364fa002760383882f18843e31c6c4209c7
  ollama_adapter_blob: 1769a719d6a6df53e001abbc4c67ad486ab5c944
  mock_adapter_blob: 04d37e59b14c9e3b85126cb3380b6221b44e26d1
  mock_adapter_proof_blob: be1b1d2b4178b30ce9be754671a2c42271ad91bc
  governed_api_main_blob: 4eb335c7c0b27f62c7419c478542e8fe40e1ff38
  governed_api_stub_blob: 1870c401a49fb4c7b53ab123e6a80770690bce51
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_abstain_test_blob: 2be20f5d93c03da7677c34b11a31875a00b2ed28
  governed_api_boundary_test_blob: 4035e537e6c52194928df5ab8ceb41a35f5f30ca
  env_example_blob: 5af73215557f4af432157409ff89ab17088d0953
  runtime_response_contract_blob: 9dfc286984b5b52b383753fe6215a2b31df8c876
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  ai_receipt_contract_blob: 1e028525569b6032cd573e71d98df6b961fa70db
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ai_receipt_validator_blob: eb80e77aed15f478c32215c8f773f308a87a092a
  policy_runtime_readme_blob: 80b63e7651429903385066b53c7fb41af3cd1298
  policy_abstain_blob: 9c66097140933eba5aa7011653da12488035ad99
  policy_deny_public_blob: 8d46a90088c046c102b991904e56ecf32d8ae7d3
  policy_evidence_required_blob: 297bd7999bf19c4029bf92df6f1c2f07477c787d
  policy_run_receipt_blob: 5fa096c9d65183b0b3333e05434bbf6f2ab9c0b7
  api_workflow_blob: 84ba16a3c36a1d58b2f6f1059a31ed6354063357
  focus_mock_workflow_blob: fbd56c7cda991ff8f3b804cc0c278e62daaa7abf
related:
  - docs/adr/INDEX.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/architecture/governed-ai/OLLAMA_INTEGRATION.md
  - docs/architecture/governed-ai/MOCK_FIRST.md
  - docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - apps/governed-api/README.md
  - runtime/ollama/README.md
  - runtime/model_adapters/OllamaAdapter.py
  - runtime/model_adapters/MockAdapter.py
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/ai_receipt.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - policy/runtime/README.md
  - tools/validators/validate_ai_receipt.py
  - .github/workflows/api-test.yml
  - .github/workflows/focus-mock-test.yml
tags: [kfm, adr, ollama, local-ai, governed-api, governed-ai, runtime, model-adapter, finite-outcomes, ai-receipt, evidence, policy, citation, no-direct-model-client]
notes:
  - "v1.4 is a documentation-only currentness reconciliation. It does not accept this ADR, activate Ollama, download a model, add a route, deploy a service, release, publish, or merge."
  - "Current source proves a one-line OllamaAdapter placeholder, a bounded no-I/O MockAdapter fixture selector, and a three-route Governed API ABSTAIN scaffold; it does not prove provider invocation or governed-AI end-to-end composition."
  - "The Google Drive AI documents and the Notion reconciliation task were consulted as historical and coordination lineage only. GitHub source at the pinned snapshot controls implementation claims."
  - "ADR-0008 remains draft with effective decision status proposed. Proposed language below is not presently accepted, self-executing, or provider-authorizing."
[/KFM_META_BLOCK_V2] -->

# ADR-0008 — Ollama and Local AI Runtimes Are Subordinate to the Governed API

> Current posture: this record is draft and its effective decision status is proposed. The repository has a bounded mock proof and a Governed API scaffold, but no working Ollama adapter, model invocation path, governed-AI route, approved provider/model profile, or live-runtime proof.

## 1. Status and authority

| Field | Current value |
|---|---|
| Record | ADR-0008 at this exact path |
| Source status | Draft |
| Effective decision status | Proposed — not an accepted architectural decision |
| Updated | 2026-09-12 |
| Decision scope | Proposed placement and limits for local-AI providers, clients, context, finite outcomes, receipts, admission, and rollback |
| Current acceptance effect | None. This ADR does not authorize a daemon, model, endpoint, deployment, release, or publication. |
| Separate accepted authority | ADR-0029 accepts directory-governance placement only; it does not accept ADR-0008 or authorize a runtime. |

The document’s proposed requirements become binding only through a reviewed acceptance that updates both this record and the canonical ADR index consistently. A schema, fixture, workflow, passing test, pull request, commit, merge, local installation, or response does not substitute for that disposition.

## 2. Proposed decision

If accepted, KFM will treat Ollama and every other local or provider-specific AI runtime as an internal, replaceable interpretation provider behind the Governed API. A provider may generate a bounded candidate response only after the governed composition has determined that the request, evidence scope, policy, citation obligations, and caller constraints permit that step.

The provider is not and must never become:

- a public API peer;
- a source of record, evidence resolver, citation validator, policy decision-maker, review authority, or release authority;
- a direct browser client dependency;
- a normal-path reader of canonical or internal stores;
- a writer of evidence, policy, contracts, schemas, source registries, lifecycle records, or published claims;
- proof that an answer is supported merely because it is fluent.

This is a proposed boundary, not a statement that the required composition exists today.

### 2.1 Proposed boundary by responsibility

| Layer | Proposed responsibility after acceptance | What current evidence shows |
|---|---|---|
| Public and review clients | Call KFM’s Governed API and consume a KFM-native finite response envelope. They do not call a provider endpoint or carry provider credentials. | No reviewed end-to-end governed-AI client path was established in this update. |
| Governed API | Own client-facing request validation, response formation, admission checks, and safe failure behavior. | A WSGI scaffold exposes only GET bootstrap, layers, and evidence routes. They return ABSTAIN / NOT_IMPLEMENTED; no AI or Focus route exists. |
| Evidence, policy, citation, and lifecycle surfaces | Independently decide admissibility, scope, rights, sensitivity, citation validity, correction, and release state before and after generation where required. | Contracts, schemas, and policy source files exist, but their relevant runtime semantics and bindings remain proposed or unimplemented. |
| Provider-neutral adapter lane | Isolate provider wire formats and implementation details from the public contract. | runtime/model_adapters/OllamaAdapter.py is a one-line placeholder. |
| Deterministic mock | Support bounded testing through prevalidated fixtures and finite outcomes only. | MockAdapter.py is executable, deterministic, and no-I/O, but does not interpret a request, choose a semantic outcome, call a model, resolve evidence, evaluate policy, validate citations, or emit a receipt. |
| Ollama or another provider | Generate constrained candidate output using only authorized context and capabilities. | No client, daemon control, model selection, provider profile, endpoint invocation, or deployment is established by current source. |

### 2.2 Proposed authority rules

If accepted, the following rules would govern a future provider admission:

- Public and semi-public clients must use the Governed API, not Ollama, a provider SDK, or a provider-native wire format.
- Only governed application logic may assemble provider context from evidence that has passed the applicable authorization, rights, sensitivity, scope, and policy checks.
- Provider output must be treated as a candidate. It must not decide evidence admissibility, policy state, source authority, review state, release state, correction status, or publication.
- The client-facing result must resolve to one finite outcome: ANSWER, ABSTAIN, DENY, or ERROR. Missing evidence, failed citations, rights/sensitivity conflicts, policy failures, and provider/validation failures must not fall through to a fluent answer.
- Any admitted provider must sit behind a reviewed provider-neutral adapter contract. Provider-specific APIs, models, parameters, and diagnostics must not become the public KFM contract.
- Tool, network, filesystem, shell, and external-retrieval capability must be default-deny and expressly admitted by a reviewed provider profile.
- A future AI receipt or equivalent must record accountable joins without retaining private reasoning as evidence or public diagnostics.

These requirements do not approve a particular Ollama release, model family, quantization, context window, deployment topology, license posture, benchmark, tool capability, hardware target, or service-level objective.

## 3. Current repository evidence

The following is the evidence-backed currentness snapshot. It intentionally distinguishes a file or test surface from a working runtime.

| Surface | Confirmed source state | It does not establish |
|---|---|---|
| ADR index and adjacent ADRs | ADR-0008 remains draft/proposed. ADR-0004 and ADR-0019 are also draft/proposed; ADR-0020 is proposed. ADR-0029 is accepted for directory governance. | Acceptance of this local-AI decision, an executable trust membrane, or provider admission. |
| Ollama integration documentation | The architecture document describes a repository-grounded scaffold-only, live-binding-deferred boundary. The runtime/ollama README labels its lane draft and NEEDS VERIFICATION. | A running daemon, installed model, approved configuration, private deployment, or accessible route. |
| Ollama adapter | OllamaAdapter.py contains one placeholder comment. | Any provider call, health check, model selection, input transformation, output validation, or error handling. |
| Default environment example | .env.example selects KFM_MODEL_RUNTIME=mock, describes the Ollama endpoint as inactive in that mode, and uses a loopback URL. | An executable environment loader, current process binding, actual loopback enforcement, daemon, model, secret, or deployment. |
| Mock adapter and proof | MockAdapter.py selects isolated copies from a caller-supplied prevalidated scenario matrix. Its proof checks all four finite outcomes, deterministic selection, isolation, configuration errors, unknown scenarios, and the no-I/O surface. | Semantic generation, policy or evidence evaluation, a live provider, receipt emission, or a governed API integration. |
| Governed API implementation | main.py dispatches GET requests; registry.py contains only bootstrap, layers, and evidence. The stub returns ABSTAIN / NOT_IMPLEMENTED for those routes and safe ERROR envelopes for errors. | An AI route, Focus transport, authentication, evidence resolution, citation validation, policy evaluation, provider call, receipt persistence, release, or publication. |
| Governed API boundary test | Its local app-level scanner forbids direct Ollama imports and checks the known scaffold route set. | Repository-wide enforcement across browsers, scripts, generated assets, dependencies, runtime configuration, infrastructure, or deployment. |
| Runtime response contract and schema | The contract and paired schema are draft/proposed. The schema defines the four outcomes and ANSWER-specific evidence/precision requirements. | An authorized ANSWER, resolved evidence, enforced policy, correct citation, or route-level use. |
| AIReceipt contract, schema, and validator | A draft/proposed shape exists; the validator explicitly limits a pass to schema shape and local consistency. | Runtime receipt creation/persistence, evidence closure, authenticated policy/citation decisions, model approval, release, or publication. |
| Runtime policy source | The README says there is no evaluator binding or governed consumer. Three Rego stubs default deny to false; the run-receipt scaffold defaults allow to false. | An enforcing policy decision, fail-open permission, or runtime gate. |
| CI workflows | api-test runs the scaffold/API shape tests. focus-mock-test keeps an explicit mock Focus hold and runs bounded finite-envelope/mock tests without starting a runtime. | An activated model, provider integration, operational readiness, release, or public service. |

### 3.1 What can safely be inferred

Current source supports only these narrow conclusions:

1. The intended placement is a provider-specific Ollama lane plus a provider-neutral adapter lane.
2. The current concrete Ollama adapter is not implemented.
3. The current mock adapter is a bounded fixture selector, not an AI runtime.
4. The Governed API is an executable but deliberately incomplete scaffold with no AI route.
5. Proposed finite-envelope and receipt shapes are useful contract evidence, not proof of enforcement or runtime authority.
6. The current policy modules are non-enforcing scaffolds.
7. The safe example configuration remains mock-first and loopback-oriented; it does not activate or prove Ollama.

### 3.2 What remains unknown or absent

This update found no evidence sufficient to claim any of the following:

- a live Ollama daemon, model inventory, model digest, license/terms review, resource profile, health check, or activation record;
- an executable provider adapter or endpoint invocation;
- a Governed API AI route, end-to-end Focus request, or client-to-provider composition;
- a binding policy evaluator, evidence resolver, citation validator, or receipt emitter in that path;
- repository-wide prevention of direct model access;
- production isolation, ingress, firewall, telemetry, incident response, rollback runbook, deployment, release, promotion, or publication.

Absence from the reviewed source slice is not a universal absence claim. It is a reason to keep the decision proposed and runtime activation out of scope.

## 4. Acceptance and activation gates

Acceptance of this ADR and activation of any provider are separate decisions. Neither may be inferred from the other.

| Gate | Required evidence before acceptance or activation | Current result |
|---|---|---|
| Decision coherence | Reviewed disposition updates ADR-0008 and the ADR index together; adjacent decision relationships are resolved rather than assumed. | Open — this record remains draft/proposed. |
| Canonical adapter semantics | A reviewed contract/schema authority defines provider-neutral behavior without competing runtime-note authority. | Open — adjacent adapter/envelope records remain proposed. |
| Provider adapter | Executable adapter implements the accepted contract, has deterministic negative-path tests, and remains replaceable without changing public semantics. | Open — OllamaAdapter.py is a placeholder. |
| Governed composition | A declared API route performs request handling, evidence/policy/citation gates, adapter invocation, response validation, and finite failure behavior. | Open — only three non-AI GET scaffold routes exist. |
| Evidence, rights, policy, and citation closure | Bound evaluators and tests prove admissible context construction and fail-closed behavior. | Open — relevant sources are proposed or non-enforcing. |
| Receipt closure | The runtime emits and safely persists or joins a receipt that can be audited without storing private reasoning. | Open — only a proposed shape and local validator exist. |
| Provider and model admission | Reviewed provider/model identity, digest/version, license and terms, data handling, capability restrictions, timeout/resource limits, and kill switch. | Open — no provider/model is admitted. |
| Exposure and operations | Private or loopback binding, secret handling, request limits, safe logs, monitoring, incident response, restore/rollback procedure, and deployment evidence. | Open — no deployment or operational proof was reviewed. |
| Anti-bypass evidence | Tests and review cover clients, scripts, dependencies, generated assets, configuration, infrastructure, and deployment surfaces. | Open — present test coverage is limited to the governed API application scope. |
| End-to-end validation | Bounded integration and negative-path tests demonstrate that no unsupported result escapes as ANSWER and no public client can reach a provider directly. | Open — no end-to-end governed-AI runtime exists. |

Until these gates close under the appropriate authorities, no provider should be activated through KFM. The mock-first example can remain a safe development reference, but it is not itself a runtime admission mechanism.

## 5. Consequences if accepted

The proposed boundary preserves provider replaceability and keeps generated language subordinate to inspectable evidence and governance. It also makes unsupported claims, missing evidence, and policy failures visible as finite outcomes rather than plausible-looking text.

The cost is deliberate: a provider cannot be introduced merely by adding a client library, model endpoint, or local configuration. It requires cross-lane contracts, admission review, operational controls, and evidence-backed validation. That cost is appropriate for a system where source, rights, correction, and release conditions must remain visible.

This ADR would not:

- approve Ollama or any other provider;
- select a model or permit model downloads;
- authorize direct access to internal stores;
- create a public endpoint;
- change release, publication, or deployment status;
- make a model output a source, policy decision, citation validation, or receipt by itself.

## 6. Alternatives rejected by the proposed decision

| Alternative | Why it is unsuitable |
|---|---|
| Browser or reviewer UI talks directly to Ollama | Bypasses the intended public trust boundary and permits provider-native output to masquerade as KFM authority. |
| Ollama reads canonical/internal stores directly | Couples a provider to protected lifecycle data and bypasses explicit evidence, scope, rights, and policy assembly. |
| Provider output is treated as evidence or policy | Confuses generated interpretation with independent source, policy, citation, review, and release authority. |
| Schema, fixture, or green CI equals provider approval | A shape/test signal cannot prove live binding, policy closure, operational security, or release authorization. |
| Historical planning documents authorize current behavior | Google Drive and Notion lineage explains intent and prior reconciliation; only current repository evidence supports implementation claims. |

## 7. Rollback and safe failure

The current repository state is already non-activated with respect to Ollama. This documentation change introduces no runtime behavior to roll back.

If a future admitted provider is later disabled, the governed public contract must continue to fail closed through the available finite outcomes. The provider profile, route binding, and operational controls must have a separately reviewed rollback/kill-switch procedure. Reverting this ADR document alone would not disable a future runtime; runtime changes require their own tracked, reviewed rollback.

No receipt, release record, deployment, publication, or model artifact is created by this ADR update.

## 8. Validation and review focus

Current checks are narrow but valuable:

- the governed API suite covers its scaffold routes and safe envelope behavior;
- the boundary guard checks the governed API source scope for direct Ollama imports;
- the mock proof covers finite outcomes, deterministic fixture selection, and no-I/O limits;
- the finite-envelope workflow runs bounded shape/fixture checks without starting a model runtime;
- the receipt validator checks a proposed receipt file’s local shape and consistency only.

Before proposing acceptance or provider admission, reviewers should verify that each current limitation in Section 4 is either closed with durable evidence or recorded as a hold. A green workflow must be read according to the exact code and job it ran, not as a generalized runtime, security, release, or publication approval.

## 9. Supporting lineage and related records

Repository-grounded companion material:

- [Ollama Integration — Governed Local Runtime Boundary](../architecture/governed-ai/OLLAMA_INTEGRATION.md)
- [Mock-First Discipline and Current Proof Boundary](../architecture/governed-ai/MOCK_FIRST.md)
- [Governed AI Adapter Contract](../architecture/governed-ai/ADAPTER_CONTRACT.md)
- [Governed API README](../../apps/governed-api/README.md)
- [Runtime Ollama lane](../../runtime/ollama/README.md)
- [Runtime model-adapter lane](../../runtime/model_adapters/README.md)
- [ADR index](./INDEX.md)
- [ADR-0004 — Governed API trust membrane](./ADR-0004-apps-governed-api-is-the-trust-membrane.md)
- [ADR-0019 — AI adapter contract and finite envelopes](./ADR-0019-ai-adapter-contract-and-finite-envelopes.md)
- [ADR-0020 — Abstain is a first-class decision](./ADR-0020-abstain-is-a-first-class-decision.md)
- [ADR-0029 — Directory governance standard v2](./ADR-0029-adopt-directory-governance-standard-v2.md)

Supporting external lineage consulted for this update:

- The Notion coordination record Reconcile Drive KFM modernization proposals against repository evidence instructs that Drive remains read-only and that proposed roadmaps must not become repository facts.
- The Google Drive documents KFM Governed AI Extended Pro Source Ledger PDF-Only Architecture Report dated 2026-04-20 and KFM AI Infrastructure – Ollama Integration Overview are historical planning material. Their intended architecture does not prove a provider, deployment, route, policy evaluator, or model is present now.

## 10. Change history

| Version | Date | Change |
|---|---|---|
| v1.4 | 2026-09-12 | Reconciled the record to current GitHub evidence; retained draft/proposed status; made the placeholder/scaffold/mock boundary explicit; recorded Notion and Drive as non-authoritative lineage only. |
| v1.3 | 2026-08-14 | Prior repository-grounded reconciliation. |
| Earlier | 2026-05-10 onward | Initial proposed decision record. |
