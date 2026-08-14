<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-ai-readme
title: Governed AI Subsystem — Architecture README
type: architecture-readme
version: v2.0
status: draft; repository-grounded; explanatory; no-runtime-authority
owners:
  - '@bartytime4life — verified CODEOWNERS review route'
owner_status: 'CODEOWNERS routing is confirmed; governed-AI, API, evidence, policy, citation, security, correction, and release stewardship assignments and independent review remain NEEDS VERIFICATION.'
created: 2026-05-15
updated: 2026-08-14
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: 'Explain how governed-AI responsibilities compose across the Governed API, runtime adapters, contracts, schemas, policy, evidence, receipts, clients, correction, and release without becoming decision, semantic, machine-shape, policy, runtime, or publication authority.'
current_path: docs/architecture/governed-ai/README.md
canonical_relationship: 'CONFLICTED — this folder README and docs/architecture/governed-ai.md are parallel human overviews; no accepted disposition was established in this revision.'
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 710173d51a3a6bf288997df6f3eb4bf7f4da1ef6
  target_prior_blob: 718282655d5752351d46122af1620e37c2bf05c6
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  mock_adapter_blob: 04d37e59b14c9e3b85126cb3380b6221b44e26d1
  mock_adapter_proof_blob: be1b1d2b4178b30ce9be754671a2c42271ad91bc
  runtime_response_contract_blob: 5060aaaa30fea37b6eeea6e1428b9effa6a163bd
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  runtime_response_builder_blob: 5dacededc1bda64292259ba39b6387facafbd1e8
  ai_receipt_contract_blob: f4d8183dbed38f83144f6d9dbde30ae02a01edb8
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ai_receipt_validator_blob: eb80e77aed15f478c32215c8f773f308a87a092a
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 5d7c137d2e78ddfca35a1356a96333ac2e84952b
  explorer_focus_resolver_blob: 45aa4e7479a8c95138f98cc48c846f39a16aec2d
  focus_request_schema_blob: a2f298f014fa299bdec03afbf14ba9937aa95ef8
  focus_response_schema_blob: fd109e4a3c859115d4ad138e9303cf8c5bdd8873
  focus_worker_placeholder_blob: 7715d01fc585b03dedae7bb535591064bd6d055c
inspection_boundary: >
  Current-session GitHub reads covered the complete target, its history and direct-child
  architecture inventory, the parallel flat governed-AI overview, accepted Directory Rules
  placement authority, current governed-AI ADR proposals and the unassigned Focus-boundary
  candidate, runtime adapter inventory and implementations, RuntimeResponseEnvelope and
  AIReceipt contracts/schemas/validators/proofs, Governed API route registration and AI
  source subtree, Explorer Focus resolution, Focus schemas, runtime policy documentation,
  the Focus worker entrypoint, CODEOWNERS, and bounded repository search for citation
  validation. No model daemon, provider endpoint, credential, live evidence resolver,
  policy evaluator, citation service, AIReceipt emitter or store, end-to-end Focus route,
  runtime deployment, public client session, release, correction propagation, rollback
  drill, or publication was exercised.
related:
  - docs/architecture/README.md
  - docs/architecture/governed-ai.md
  - docs/architecture/governed-ai/ADAPTER_CONTRACT.md
  - docs/architecture/governed-ai/AI_RECEIPTS.md
  - docs/architecture/governed-ai/BOUNDARIES.md
  - docs/architecture/governed-ai/CONTINUITY_NOTES.md
  - docs/architecture/governed-ai/FOCUS_FLOW.md
  - docs/architecture/governed-ai/MOCK_FIRST.md
  - docs/architecture/governed-ai/OLLAMA_INTEGRATION.md
  - docs/architecture/governed-ai/PROMPT_INJECTION.md
  - docs/architecture/governed-ai/ROUTE_MAP.md
  - docs/adr/ADR-0004-apps-governed-api-is-the-trust-membrane.md
  - docs/adr/ADR-0008-ollama-subordinate-to-governed-api.md
  - docs/adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md
  - docs/adr/ADR-0020-abstain-is-a-first-class-decision.md
  - docs/adr/ADR-0025-public-client-never-reads-canonical-internal-stores.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-focus-model-adapter-boundary.md
  - docs/doctrine/directory-rules.md
  - apps/governed-api/src/governed_api/routes/registry.py
  - apps/governed-api/src/governed_api/stub.py
  - apps/governed-api/src/ai/README.md
  - apps/explorer-web/src/features/focus_panel/resolver.ts
  - apps/workers/src/ai_focus_worker/main.py
  - runtime/model_adapters/README.md
  - runtime/model_adapters/MockAdapter.py
  - runtime/model_adapters/OllamaAdapter.py
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/ai_receipt.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - schemas/contracts/v1/focus/focus_request.schema.json
  - schemas/contracts/v1/focus/focus_response.schema.json
  - packages/envelopes/src/envelopes/runtime_response.py
  - tools/validators/validate_ai_receipt.py
  - tests/runtime_proof/test_mock_adapter_finite_outcomes.py
  - policy/runtime/README.md
  - .github/workflows/focus-mock-test.yml
tags: [kfm, architecture, governed-ai, focus-mode, model-adapter, runtime-response-envelope, ai-receipt, citation-validation, policy, mock-first, ollama, finite-outcomes, trust-membrane, cite-or-abstain]
notes:
  - 'v2.0 is a same-path repository-grounded rewrite; it changes no runtime, contract, schema, policy, fixture, test, workflow, receipt, release, or publication behavior.'
  - 'Architecture documentation is explanatory. Accepted Directory Rules govern placement; the governed-AI ADRs remain proposed, and the Focus-boundary candidate remains unassigned.'
  - 'MockAdapter and RuntimeResponseEnvelope now have bounded executable proof surfaces, but end-to-end governed AI orchestration remains on HOLD.'
  - 'The former README speculative AIReceipt field list and replay claims were replaced with the current schema-paired field surface and verified implementation limits.'
  - 'The missing STATE_OWNERSHIP.md reference was removed; no replacement file was created.'
[/KFM_META_BLOCK_V2] -->

# Governed AI Subsystem — Architecture README

> **Governed AI is an interpretive subsystem, not a truth source or publication path.** Its intended role is to turn already-governed context into bounded language behind the Governed API while preserving evidence, policy, citation, precision, freshness, correction, receipt, and finite-outcome boundaries. Current repository evidence proves several bounded components, not an operational end-to-end AI route.

[![status](https://img.shields.io/badge/status-draft-d4a72c?style=flat-square)](#2--authority-level)
[![evidence](https://img.shields.io/badge/evidence-repository--grounded-0969da?style=flat-square)](#5--repo-fit)
[![decisions](https://img.shields.io/badge/governed--AI%20ADRs-proposed-6e7781?style=flat-square)](#24--adrs)
[![MockAdapter](https://img.shields.io/badge/MockAdapter-bounded%20selector-2da44e?style=flat-square)](#13--adapter-boundary)
[![API route](https://img.shields.io/badge/governed%20AI%20route-absent-b42318?style=flat-square)](#12--the-governed-ai-request-flow)
[![provider](https://img.shields.io/badge/live%20provider-none%20admitted-6e7781?style=flat-square)](#13--adapter-boundary)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#17--trust-membrane-and-exposure-controls)

> [!IMPORTANT]
> **Architecture explanation is not decision or runtime authority.** This README explains current repository relationships. `contracts/` owns semantic meaning, `schemas/` owns machine shape, `policy/` owns admissibility rule source, implementation roots own executable behavior, and `release/` owns release/correction/rollback decisions. Accepted ADR-0029 and the adopted Directory Rules govern placement; ADR-0008 and ADR-0019 remain proposed.

> [!CAUTION]
> **Bounded proofs must not be promoted into an AI-integration claim.** The repository has a deterministic no-I/O `MockAdapter`, four-outcome `RuntimeResponseEnvelope` fixtures and proof tests, a local AIReceipt validator, and a defensive Explorer Focus projection. It does not have a verified governed-AI API route, executing runtime policy bundle, citation-validation service, evidence-resolution composition, AIReceipt emitter/store, admitted provider, or public AI release.

> [!WARNING]
> **Parallel and overlapping authorities remain unresolved.** This folder README and [`docs/architecture/governed-ai.md`](../governed-ai.md) are competing human overviews. The unassigned [`ADR-focus-model-adapter-boundary`](../../adr/ADR-focus-model-adapter-boundary.md) overlaps the broader proposed [`ADR-0019`](../../adr/ADR-0019-ai-adapter-contract-and-finite-envelopes.md). This revision records those conflicts; it does not settle them by documentation fiat.

**Quick navigation:** [Purpose](#1--purpose) · [Authority](#2--authority-level) · [Belongs](#3--what-belongs-here) · [Exclusions](#4--what-does-not-belong-here) · [Repo fit](#5--repo-fit) · [Tree](#6--proposed-directory-tree) · [Inputs](#7--inputs) · [Outputs](#8--outputs) · [Doctrine](#9--core-doctrine) · [Objects](#10--object-families-and-homes) · [Outcomes](#11--finite-outcomes--the-trust-grammar) · [Flow](#12--the-governed-ai-request-flow) · [Adapters](#13--adapter-boundary) · [Citations](#14--citation-validation) · [Policy](#15--policy-precheck-and-postcheck) · [Receipts](#16--aireceipt-and-replay-discipline) · [Exposure](#17--trust-membrane-and-exposure-controls) · [Validation](#18--validation) · [Siblings](#19--sibling-docs-in-this-folder) · [Anti-patterns](#20--anti-patterns) · [Propagation](#21--update-propagation) · [Rollback](#22--rollback) · [Review](#23--review-burden) · [ADRs](#24--adrs) · [Open work](#25--open-questions-and-verification-backlog) · [Related](#26--related-folders) · [Evidence](#27--last-reviewed)

---

## 1 · Purpose

This README is the human architecture entry point for the **governed-AI responsibility seam**. It explains how KFM intends to compose:

1. a caller-facing Focus or AI-assisted request;
2. governed scope, identity, release, evidence, policy, and sensitivity checks;
3. minimized admissible context;
4. a provider-neutral model-adapter boundary;
5. an untrusted structured candidate;
6. structured-output and citation validation;
7. policy postcheck, precision/freshness/correction disclosure, and finite outcome selection;
8. `RuntimeResponseEnvelope` assembly; and
9. `AIReceipt` accountability where an accepted operation requires one.

This page may explain responsibility, dependency direction, current maturity, conflicts, validation, and rollback. It must not accept an ADR, define canonical object meaning, amend a schema, activate policy, admit a provider, authorize a route, or turn a bounded component test into a public runtime claim.

The former README described this subsystem as the only path for all model-mediated language. That remains an architectural direction, not an accepted repository-wide decision, because the relevant ADRs remain proposed.

---

## 2 · Authority level

| Field | Current value |
|---|---|
| **Path** | `docs/architecture/governed-ai/README.md` — confirmed tracked file |
| **Owning root** | `docs/` |
| **Responsibility** | Cross-root explanatory architecture for the governed-AI subsystem |
| **Authority kind** | Explanatory; not decision, contract, schema, policy, evidence, receipt, runtime, release, or publication authority |
| **Placement basis** | Accepted ADR-0029 adopts Directory Rules v2; existing same-path documentation is retained without structural change |
| **Verified review route** | `.github/CODEOWNERS` routes the repository and relevant roots to `@bartytime4life` |
| **Stewardship** | Governed-AI/API/evidence/policy/citation/security/correction/release stewardship remains `NEEDS VERIFICATION` |
| **Decision status** | ADR-0008 and ADR-0019 are `proposed`; the Focus adapter-boundary candidate is `not-assigned` |
| **Runtime status** | `PARTIAL / HOLD`: bounded component proofs exist; end-to-end governed orchestration is not established |
| **Release/publication effect** | None |

Architecture prose cannot override current contracts, schemas, policy, implementation, or accepted decisions. Conversely, checked-in implementation does not silently accept a proposed ADR.

### Current canonicality conflict

Two tracked human overviews currently describe governed AI:

- this folder landing page, `docs/architecture/governed-ai/README.md`; and
- the flat note, [`docs/architecture/governed-ai.md`](../governed-ai.md).

Both contain substantive architecture material. No accepted ADR, migration note, tombstone, or parent-index disposition was established in the inspected evidence. Their relationship is therefore **CONFLICTED / HOLD**.

---

## 3 · What belongs here

This directory may contain human architecture documents that explain distinct governed-AI concerns across responsibility roots.

Current tracked siblings:

- [`ADAPTER_CONTRACT.md`](./ADAPTER_CONTRACT.md) — provider-neutral adapter architecture.
- [`AI_RECEIPTS.md`](./AI_RECEIPTS.md) — receipt/accountability architecture.
- [`BOUNDARIES.md`](./BOUNDARIES.md) — trust and forbidden-path boundaries.
- [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) — lineage notes.
- [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) — proposed end-to-end Focus flow.
- [`MOCK_FIRST.md`](./MOCK_FIRST.md) — mock-first posture.
- [`OLLAMA_INTEGRATION.md`](./OLLAMA_INTEGRATION.md) — deferred Ollama posture.
- [`PROMPT_INJECTION.md`](./PROMPT_INJECTION.md) — untrusted-content boundaries.
- [`ROUTE_MAP.md`](./ROUTE_MAP.md) — proposed route-family map.
- `README.md` — this repository-grounded landing page.

A new sibling should be added only when the concern cannot be handled accurately by this page, an existing sibling, a per-root README, a contract, policy documentation, a runbook, or an ADR.

---

## 4 · What does NOT belong here

| Responsibility | Owning surface |
|---|---|
| Adapter, provider, route, or finite-envelope decisions | `docs/adr/` |
| AI-as-assistant, cite-or-abstain, trust membrane, or lifecycle doctrine | `docs/doctrine/` |
| RuntimeResponseEnvelope, AIReceipt, PolicyDecision, EvidenceBundle, or Focus object meaning | `contracts/` |
| Machine-checkable fields and compatibility constraints | `schemas/contracts/v1/` |
| Allow, deny, abstain, restrict, redact, or obligation rules | `policy/` |
| Executable model adapters | `runtime/model_adapters/` |
| Governed API orchestration and route registration | `apps/governed-api/` |
| Browser projection and accessibility behavior | `apps/explorer-web/` |
| Worker execution | `apps/workers/` |
| Synthetic proof candidates and executable tests | `fixtures/` and `tests/` |
| Receipt instances and runtime accountability records | accepted `data/` lanes |
| Release, correction, withdrawal, and rollback decisions | `release/` |
| Secrets, credentials, model weights, protected source content, restricted geometry, or private chain-of-thought | never this public documentation path |

Examples here must remain compact, synthetic, public-safe, and explicitly non-authoritative.

---

## 5 · Repo fit

The subsystem spans several responsibility roots. Current evidence does **not** prove they are composed into one operational transaction.

```text
Explorer Focus projection         PARTIAL — defensive client logic, injected resolver
  -> Governed API                 PARTIAL — bootstrap/layers/evidence only; no AI route
  -> Governed API AI subtree      PLACEHOLDER — README and .gitkeep
  -> runtime policy               HOLD — non-enforcing Rego scaffolds
  -> evidence resolution          NOT COMPOSED into an AI route
  -> MockAdapter                  BOUNDED PROOF — deterministic no-I/O selector
  -> OllamaAdapter                PLACEHOLDER
  -> citation validation          NOT ESTABLISHED as executable service
  -> RuntimeResponseEnvelope      BOUNDED PROOF — schema, builder, fixtures, tests
  -> AIReceipt                    BOUNDED SHAPE — schema and validator; no emitter/store
  -> ai_focus_worker              PLACEHOLDER
  -> public governed AI answer    NOT ESTABLISHED
```

### Current maturity matrix

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Governed-AI folder | Ten tracked Markdown files including this README | Documentation exists; sibling accuracy is not implied by presence |
| Parallel flat overview | `docs/architecture/governed-ai.md` exists | Human-overview authority is conflicted |
| `MockAdapter.py` | Deterministic no-I/O selector for prevalidated complete synthetic envelopes | Fixture-selection proof, not semantic adapter or model integration |
| MockAdapter proof | Covers four outcomes, determinism, isolation, malformed configuration, unknown scenario, and no-I/O imports | Component responsibility has bounded proof |
| RuntimeResponseEnvelope | Proposed contract/schema, fixtures, validator, builder, and proof tests | Shape and local candidate-building proof only |
| AIReceipt | Proposed contract/schema plus local validator | Shape/local consistency proof only |
| Governed API registry | `/bootstrap`, `/layers`, `/evidence` | No AI or Focus route is registered |
| Governed API stub | Deterministic `ABSTAIN` with `NOT_IMPLEMENTED` | Trust-membrane placeholder, not an AI route |
| Governed API AI subtree | README and `.gitkeep` | No orchestration implementation |
| Explorer Focus resolver | Defensive projection over an injected resolver and allowlisted evidence refs | Client projection boundary; no direct model, policy, evidence, or store access |
| Focus request/response schemas | Empty permissive proposed scaffolds with `additionalProperties: true` | No usable Focus wire contract is established |
| Runtime policy | Non-enforcing scaffolds; no accepted evaluator or API binding | Policy pre/postcheck is not executable in this path |
| `OllamaAdapter.py` | One-line placeholder | No provider is admitted or invoked |
| `ai_focus_worker/main.py` | One-line placeholder | No worker execution path |
| Citation validator | Bounded repository search surfaced architecture references but no executable service | Implementation remains `NOT ESTABLISHED`; absence claim is search-bounded |
| Focus mock workflow | Exercises bounded envelope and MockAdapter proof and explicitly retains HOLD | Green component proof would not prove runtime integration |

### State distinctions

Keep these separate:

- **file present** — bytes exist;
- **shape proof** — schema/validator accepts and rejects reviewed cases;
- **component proof** — one bounded implementation behaves deterministically;
- **orchestration proof** — components compose in the intended order;
- **policy/evidence closure** — referenced authority resolves and is applicable;
- **runtime proof** — a known revision executed in a controlled environment;
- **release/publication** — a separately authorized outward transition occurred.

No state implies the next.

---

## 6 · Proposed directory tree

This heading is retained for inbound compatibility. The tree below is a **current responsibility map**, not a proposal to create paths.

```text
docs/architecture/governed-ai/            explanatory subsystem documents
apps/governed-api/                         public trust membrane and future orchestration
apps/explorer-web/                         caller projection and trust-visible UI
apps/workers/src/ai_focus_worker/          worker placeholder
runtime/model_adapters/                    provider-neutral adapter lane
runtime/ollama/                            deferred local-provider lane
contracts/runtime/                         RuntimeResponseEnvelope and AIReceipt meaning
schemas/contracts/v1/runtime/              machine shapes
schemas/contracts/v1/focus/                current permissive Focus scaffolds
policy/runtime/                             current non-enforcing policy scaffolds
packages/envelopes/                        bounded envelope helper implementation
fixtures/contracts/v1/runtime/             reviewed synthetic envelope cases
tests/runtime_proof/                       bounded runtime-envelope and adapter proof
data/receipts/                             process memory, not truth or release authority
release/                                   release/correction/rollback decision plane
```

Directory Rules basis: this README stays under `docs/architecture/` because it explains a cross-root subsystem to humans. It does not create a new root, move authority, or convert a compatibility path into canon.

---

## 7 · Inputs

A mature governed-AI operation should accept only explicit, validated, bounded inputs. Current repository support varies.

| Input family | Required meaning | Current posture |
|---|---|---|
| Caller request | Requested task, selected scope, locale, interaction identity, and caller capabilities | Focus schemas are permissive scaffolds; wire contract unresolved |
| Scope context | Geography, time, feature/layer identity, release identity, and precision ceiling | Partially represented across UI/Focus documents; no end-to-end contract proof |
| Evidence context | Allowlisted `EvidenceRef`s that resolve to admissible `EvidenceBundle`s | Explorer projection checks allowlisted refs; runtime resolution not composed |
| Policy context | Effective bundle/version, caller role, sensitivity, rights, and obligations | Runtime Rego is non-enforcing; evaluator binding absent |
| Freshness/correction context | `as_of`, freshness state, supersession, correction, and withdrawal state | Envelope fields exist; source authority and computation remain external |
| Adapter request | Minimized provider-neutral context and output constraints | Proposed by architecture/ADR material; no accepted machine contract established |
| Provider configuration | Explicit provider/model allowlist and resource/security limits | No live provider admitted |

### Input invariants

1. Client-provided evidence references are candidates, not resolved truth.
2. Context minimization happens before the adapter boundary.
3. Raw, quarantine, canonical/internal, restricted, and unpublished stores are not adapter inputs.
4. Prompt text never carries authority merely because it is labeled system or trusted.
5. Unknown rights, sensitivity, release, or correction state fails closed.
6. Private chain-of-thought is neither an input requirement nor a receipt field.

---

## 8 · Outputs

The only intended outward response family is the finite `RuntimeResponseEnvelope`. An `AIReceipt` is separate process memory and never substitutes for the response, evidence, policy, review, release, or publication state.

### Current RuntimeResponseEnvelope shape

The current schema requires:

| Field | Current rule |
|---|---|
| `id` | Required string |
| `spec_hash` | Required `sha256:` identity |
| `version` | Required version string |
| `issued_at` | Required date-time |
| `outcome` | Exactly `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| `reason_code` | Required finite reason string |
| `evidence_refs` | Required unique array |
| `policy_state` | Required policy posture |
| `freshness` | Required freshness posture |
| `correction_state` | Required correction posture |
| `precision_actually_used` | Required for `ANSWER`; forbidden for non-ANSWER outcomes |
| additional properties | Closed at the top level |

The bounded builder validates local shape/profile rules. It does not resolve evidence, evaluate policy, calculate freshness, authorize precision, approve correction closure, or release a response.

### Current AIReceipt shape

The current AIReceipt schema requires exactly these top-level fields:

- `id`
- `run_id`
- `adapter`
- `model_ref`
- `inputs_digest`
- `outputs_digest`
- `policy_decision_ref`
- `citation_validation_ref`
- `outcome`

The schema is closed. The local validator proves bounded shape and consistency only. Runtime emission, persistence, reference resolution, retention, signing, replay, correction propagation, and public exposure are not established.

### Output rules

- `ANSWER` must still be bounded by evidence, policy, freshness, correction, and precision.
- `ABSTAIN`, `DENY`, and `ERROR` are successful finite responses when their conditions apply.
- A provider candidate is untrusted until validation and postcheck complete.
- A receipt records a process; it does not prove the answer true or publishable.
- Debug traces, raw prompts, private reasoning, credentials, internal paths, and protected payloads do not belong in outward envelopes.

---

## 9 · Core doctrine

The subsystem inherits these rules:

1. **EvidenceBundle outranks generated language.**
2. **Cite or abstain.** A consequential statement either resolves support or does not claim it.
3. **Public clients use governed interfaces.** No direct browser-to-model or browser-to-canonical-store path.
4. **AI is interpretive.** It does not decide source authority, rights, sensitivity, review, release, correction, or rollback.
5. **Finite outcomes are first class.** Failure must not degrade into unsupported prose.
6. **Derived stays derived.** Summaries, embeddings, indexes, graphs, and model output remain downstream carriers.
7. **Correction history is preserved.** A later answer does not erase an earlier released state.
8. **Promotion is a governed transition.** A commit, PR, merge, passing test, receipt, or deployment is not publication.
9. **Sensitive context fails closed.** Harmful precision and unclear rights trigger denial, abstention, generalization, staged access, or review.
10. **Determinism is preferred where practical.** Identity, fixtures, diagnostics, and replay inputs should be inspectable.

---

## 10 · Object families and homes

| Object or responsibility | Semantic home | Machine/implementation home | Current posture |
|---|---|---|---|
| RuntimeResponseEnvelope | `contracts/runtime/` | runtime schema, envelope package, validators, fixtures, tests | Bounded proof; proposed profile |
| AIReceipt | `contracts/runtime/` | runtime schema and local validator | Shape proof only |
| Focus request/response | Focus contracts are not established in the inspected path | permissive Focus schemas and UI projection | HOLD |
| Adapter boundary | proposed ADR and architecture docs | `runtime/model_adapters/` | Mock selector proven; live provider absent |
| EvidenceRef/EvidenceBundle | evidence contracts | evidence resolver and governed API composition | Runtime AI composition absent |
| PolicyDecision | policy/decision contracts | evaluator and policy bundle | Runtime binding absent |
| CitationValidationReport | architecture/contract direction | executable service not surfaced in bounded search | NOT ESTABLISHED |
| Release/correction/rollback records | release contracts and decisions | `release/` and accountability lanes | Not exercised by this documentation update |

Do not duplicate one of these object families inside this directory. Architecture pages link to the authority surface; they do not redefine it.

---

## 11 · Finite outcomes — the trust grammar

| Outcome | Use | Minimum safe posture |
|---|---|---|
| `ANSWER` | Admissible, in-scope response | Resolved evidence, allowed policy, validated citations, current/declared freshness, visible correction and precision state |
| `ABSTAIN` | Evidence missing, stale, conflicted, unsupported, or scope too broad | Stable reason code and no fabricated answer |
| `DENY` | Policy, rights, sensitivity, caller capability, or precision blocks exposure | Stable reason code; do not leak protected details through explanation |
| `ERROR` | Tool, resolver, policy, adapter, validator, receipt, or orchestration failure | Stable reason code; no unsafe fallback |

The existing MockAdapter scenario matrix proves selection of all four complete envelope outcomes. It does not prove that real evidence or policy selected the correct outcome.

---

## 12 · The governed AI request flow

### Target architecture

```text
caller request
  -> validate caller-facing request and scope
  -> authenticate/authorize caller
  -> resolve release, evidence, freshness, correction, rights, and sensitivity
  -> policy precheck and context minimization
  -> build provider-neutral adapter request
  -> invoke admitted adapter
  -> parse untrusted structured candidate
  -> structured-output and citation validation
  -> policy postcheck and precision enforcement
  -> assemble RuntimeResponseEnvelope
  -> emit/store AIReceipt when required
  -> return through Governed API
```

### Current stage-by-stage posture

| Stage | Current result |
|---|---|
| Caller Focus projection | Partial defensive TypeScript logic exists |
| Stable Focus wire contract | HOLD; schemas are permissive scaffolds |
| Governed API AI route | Absent from route registry |
| AI orchestration | Placeholder subtree only |
| Evidence/policy composition | Not established |
| Context minimization contract | Proposed in docs/ADR material |
| Mock candidate selection | Implemented bounded proof |
| Live adapter invocation | Absent |
| Structured candidate parsing | Not established end to end |
| Citation validation | Executable service not established |
| Policy postcheck | Not established |
| Final envelope assembly | Local builder exists; orchestration integration absent |
| AIReceipt emission/store | Not established |
| Public governed answer | Not established |

The correct operational classification is **PARTIAL / HOLD**, not implemented and not absent.

---

## 13 · Adapter boundary

The adapter boundary should remain provider neutral and narrow.

### Confirmed current implementations

**MockAdapter**

- loads a predefined scenario matrix;
- requires complete synthetic envelopes for all four outcomes;
- returns deep copies deterministically;
- rejects malformed configuration and unknown scenarios;
- performs no network, subprocess, socket, model, file-write, evidence, policy, citation, receipt, or release operation.

It is therefore a **bounded selector**, not a semantic model adapter.

**OllamaAdapter**

- is a one-line placeholder;
- proves only that a path and filename exist;
- does not establish model discovery, invocation, timeout, resource limits, structured output, health checks, provider identity, or security controls.

### Required provider-admission evidence

Before a live provider can graduate, require at least:

- an accepted adapter boundary and finite-envelope decision;
- explicit provider/model allowlisting and immutable or traceable model identity;
- no direct client access;
- bounded input/output sizes and timeouts;
- no uncontrolled tool or filesystem access;
- deterministic negative fixtures and failure mapping;
- structured-output parsing that fails closed;
- evidence/citation/policy integration outside provider authority;
- AIReceipt emission and retention rules;
- security, privacy, resource, and rollback review.

Provider availability is a runtime fact, not architecture authority.

---

## 14 · Citation validation

Citation validation is a trust-bearing responsibility independent of model fluency.

A mature validator must verify, as applicable:

1. every consequential claim has a citation or the response abstains;
2. references are allowlisted for the current request;
3. each `EvidenceRef` resolves to the intended `EvidenceBundle` or finite failure;
4. cited evidence supports the claim, geography, time, role, precision, and qualification;
5. stale, corrected, superseded, withdrawn, denied, or unresolved support is visible;
6. citations do not expose restricted source text, paths, reasons, or geometry;
7. validator output is finite, deterministic where practical, and receipt-addressable.

### Current implementation boundary

The inspected repository search surfaced citation-validation architecture references and AIReceipt fields, but no executable `CitationValidator` service was established. This is a bounded search result, not a byte-complete proof of global absence.

Until executable behavior is verified:

- do not claim citation closure;
- do not emit `ANSWER` merely because references are syntactically present;
- do not treat `citation_validation_ref` as resolved authority;
- prefer `ABSTAIN` or `ERROR` when the required validation service is unavailable.

---

## 15 · Policy precheck and postcheck

Policy must surround provider invocation rather than live inside the provider.

### Precheck responsibilities

- authenticate/authorize caller and operation;
- verify release, rights, sensitivity, consent, sovereignty, and access posture;
- restrict evidence set and precision;
- minimize prompt/context content;
- deny raw, quarantine, canonical/internal, and unpublished material;
- determine whether provider invocation is allowed at all.

### Postcheck responsibilities

- validate finite outcome and reason code;
- enforce allowed evidence and citation set;
- enforce precision/generalization obligations;
- screen prohibited disclosures and protected details;
- preserve freshness, correction, supersession, and withdrawal state;
- decide whether the candidate may become a RuntimeResponseEnvelope.

### Current policy state

The runtime policy README records non-enforcing Rego scaffolds. No accepted bundle, evaluator, version binding, Governed API consumer, or end-to-end allow/deny proof was established. Policy precheck/postcheck therefore remains **HOLD**.

A policy stub, schema, README, or green syntax test is not a policy decision.

---

## 16 · AIReceipt and replay discipline

AIReceipt is process memory. It is not evidence truth, policy approval, review approval, release authority, correction closure, or publication.

### Current proven boundary

- semantic contract exists;
- closed machine schema exists;
- local validator exists;
- runtime emitter/store/resolver is not established;
- reference targets are not proven resolved;
- signing, retention, replay, correction, and deletion behavior are not established.

### Minimum future replay packet

A replayable operation should bind, through accepted contracts and referenced records:

- exact caller/request identity and scope;
- evidence and release identities used;
- policy decision and effective policy version;
- adapter/model identity;
- deterministic input/output digests;
- citation-validation result;
- finite outcome;
- correction/supersession relationship;
- environment or nondeterminism disclosures needed to interpret replay.

Do not place raw prompts, full sensitive context, credentials, private chain-of-thought, or protected evidence in a receipt merely to make replay easier.

### Correction behavior

A corrected answer should preserve prior receipt identity, identify the corrected or superseding operation, update outward release/correction state through the owning authority, and invalidate affected caches or derived surfaces where applicable. Silent overwrite is not correction.

---

## 17 · Trust membrane and exposure controls

### Allowed public path

```text
public client
  -> Governed API
  -> released/public-safe evidence and policy context
  -> admitted adapter behind the API, when allowed
  -> validation and finite envelope
  -> public client
```

### Denied normal paths

- browser directly to Ollama or another provider;
- browser directly to RAW, WORK, QUARANTINE, canonical/internal, proof, or steward stores;
- provider directly reading repository paths or source stores;
- client-supplied references becoming authoritative without resolution;
- model output bypassing citation/policy postcheck;
- debug/error output leaking prompts, evidence excerpts, policy internals, restricted reasons, or precise protected geometry;
- worker, watcher, receipt, test, or merge writing `PUBLISHED` state by implication.

### Local exposure

A local provider must still use deny-by-default network exposure, explicit binding, least privilege, authenticated API mediation, bounded resources, auditable configuration, and no direct public client traffic. Local does not mean trusted or public-safe.

---

## 18 · Validation

Validation claims must name the layer they prove.

### Confirmed bounded proof

| Proof surface | Current coverage | Does not prove |
|---|---|---|
| RuntimeResponseEnvelope schema/fixtures/tests | Four outcomes, required fields, precision profile, negative cases | Evidence truth, policy choice, citation support, release |
| Envelope builder | Deterministic local candidate assembly and invariants | Governed orchestration or outcome authorization |
| MockAdapter tests | Four scenarios, determinism, isolation, malformed config, unknown scenario, no-I/O | Provider behavior, evidence/policy/citation integration |
| AIReceipt validator | Local shape and cross-field consistency | Emission, storage, reference resolution, retention, replay, signing |
| Explorer Focus resolver tests/logic | Defensive projection and finite client failure posture | Server route, model invocation, evidence resolution, policy enforcement |
| Focus mock workflow | Runs bounded component proof | Whole-system Focus runtime or publication |

### Graduation gates

End-to-end governed AI remains on HOLD until the repository proves at least:

- [ ] accepted adapter/finite-envelope decision and resolved overlap with the unassigned Focus candidate;
- [ ] non-permissive caller and adapter wire contracts;
- [ ] registered Governed API route with authentication and authorization;
- [ ] evidence resolution and allowlist enforcement;
- [ ] executable policy precheck/postcheck with version binding;
- [ ] structured candidate parser and stable failure codes;
- [ ] executable citation validation with negative fixtures;
- [ ] precision, freshness, correction, and supersession enforcement;
- [ ] AIReceipt emission, validation, storage, resolution, retention, and correction behavior;
- [ ] provider admission or explicit mock-only scope;
- [ ] no-direct-client, no-raw-path, prompt-injection, leakage, timeout, and resource-limit tests;
- [ ] hosted exact-head evidence and required-check posture appropriate to risk;
- [ ] rollback and correction drill;
- [ ] release decision for any outward use.

A green component test is necessary evidence for that component and nothing more.

---

## 19 · Sibling docs in this folder

Sibling documents remain useful lineage and design aids, but several predate current implementation evidence. Read them with these bounds:

| Document | Current use | Do not infer |
|---|---|---|
| `ADAPTER_CONTRACT.md` | Proposed adapter/orchestration model | Accepted contract or live provider |
| `AI_RECEIPTS.md` | Receipt design intent | Current schema fields beyond the canonical schema or runtime persistence |
| `BOUNDARIES.md` | Trust-boundary guidance | Enforced policy or route behavior |
| `CONTINUITY_NOTES.md` | Historical continuity | Current authority or implementation |
| `FOCUS_FLOW.md` | Target flow | Registered route or working Focus runtime |
| `MOCK_FIRST.md` | Bounded implementation sequencing | Mock proof equals provider readiness |
| `OLLAMA_INTEGRATION.md` | Deferred provider plan | Ollama admission or current daemon state |
| `PROMPT_INJECTION.md` | Security requirements | Complete executable coverage |
| `ROUTE_MAP.md` | Proposed route map | Current route registration |

The former README referenced `STATE_OWNERSHIP.md`, which is not a tracked sibling in the current directory. This revision removes the broken reference rather than inventing the file.

---

## 20 · Anti-patterns

Do not:

- call bounded envelope proof an operational AI system;
- place model invocation in the browser;
- let a provider select authoritative evidence or policy;
- treat a citation string as evidence resolution;
- treat an AIReceipt as proof of truth or release;
- accept permissive Focus scaffolds as a stable wire contract;
- expose raw prompts, private reasoning, credentials, repository paths, or restricted evidence;
- silently map provider failures to `ANSWER`;
- hide stale, corrected, superseded, withdrawn, denied, or generalized states;
- copy architecture prose into contracts or schemas as a parallel authority;
- use a documentation update to accept an ADR or provider;
- let watchers, workers, tests, commits, PRs, merges, or deployments publish by implication;
- add a second governed-AI overview without a documented authority relationship;
- fabricate replay from file mtimes, commit times, or missing records.

---

## 21 · Update propagation

Update this README when a material governed-AI surface changes, but update the owning authority first or in the same coherent reviewed packet.

| Change | Required companion review |
|---|---|
| RuntimeResponseEnvelope fields/outcomes | Contract, schema, builder, fixtures, tests, compatibility notes |
| AIReceipt fields or lifecycle | Contract, schema, validator, emitter/store, retention/correction docs, tests |
| Adapter interface or provider admission | ADR, adapter contract, runtime implementation, tests, security/runbook |
| Governed API route | Route registry, request/response contracts, authorization, policy, tests, route map |
| Evidence or citation behavior | Evidence contracts/resolver, citation validator, fixtures, reason codes, receipts |
| Policy behavior | Policy source, evaluator/bundle version, fixtures, tests, obligations, rollback |
| Focus client behavior | Focus contracts/schemas, Explorer implementation, accessibility and negative-state tests |
| Release/publication posture | Release manifest/decision, correction, rollback, cache and client behavior |
| Canonical overview disposition | ADR or migration note, parent navigation, inbound links, tombstone/rollback plan |

Do not update this page first and then cite it as authority for the behavior change.

---

## 22 · Rollback

### Documentation rollback

Restore prior blob:

```text
718282655d5752351d46122af1620e37c2bf05c6
```

This reverses the README text only. It does not change adapters, routes, contracts, schemas, policy, tests, receipts, release state, deployment, or public behavior.

### Implementation rollback expectations

Future runtime changes must define their own rollback unit. At minimum preserve:

- previous compatible request/response and adapter contract versions;
- provider disable/deny path;
- prior policy bundle and decision references;
- receipt and correction lineage;
- cache invalidation and client finite-failure behavior;
- no fallback to direct model or internal-store access.

Rollback must not erase evidence of an earlier released answer or receipt.

---

## 23 · Review burden

| Change class | Minimum review posture |
|---|---|
| Editorial clarification in this README | Docs/architecture review route |
| Repository-evidence refresh | Docs plus affected implementation owner |
| Contract/schema field or enum change | Contract/schema/consumer/compatibility review |
| Policy or sensitivity behavior | Policy, security/privacy, affected-domain, and negative-test review |
| New provider or model | Runtime, security, evidence, policy, API, resource, and rollback review |
| New public AI route | API, auth, evidence, policy, citation, UI, accessibility, correction, release review |
| Canonical overview migration | Architecture/docs decision plus link and rollback review |

CODEOWNERS routing is not proof that these reviews occurred or that separation of duties exists.

---

## 24 · ADRs

| Record | Current status | Relevance |
|---|---|---|
| ADR-0004 — Governed API trust membrane | Proposed | Public boundary direction; not accepted |
| ADR-0008 — Ollama subordinate to Governed API | Proposed | Provider subordination and no-direct-client direction |
| ADR-0019 — AI adapter contract and finite envelopes | Proposed | Broad governed-AI decision and current evidence assessment |
| ADR-0020 — Abstain is first class | Proposed | Finite failure direction |
| ADR-0025 — Public client never reads canonical/internal stores | Proposed | Public storage boundary direction |
| ADR-0029 — Directory Governance Standard v2 | **Accepted** | Placement authority for this documentation path and responsibility roots |
| ADR-0035 — repository-wide ADR identity/numbering | Proposed | Does not assign or accept the Focus boundary candidate |
| ADR-focus-model-adapter-boundary | Not assigned | Overlaps ADR-0019; requires fold-in or explicit non-overlap before assignment |

This README does not change any status.

---

## 25 · Open questions and verification backlog

### P0 — authority and trust closure

- Resolve the parallel `governed-ai.md` versus folder-README authority relationship.
- Resolve ADR-0019 overlap with the unassigned Focus adapter-boundary candidate.
- Define accepted caller, adapter-request, adapter-candidate, and final-envelope boundaries.
- Replace permissive Focus scaffolds before declaring a stable wire contract.
- Establish executable evidence, policy, and citation composition before any `ANSWER` route.
- Define AIReceipt emission, storage, resolution, retention, correction, and access policy.

### P1 — bounded implementation

- Register an authenticated mock-only Governed API route with explicit non-public/release posture.
- Implement orchestration over existing synthetic envelope proofs without a live provider.
- Add deterministic citation-validator fixtures and finite reason codes.
- Bind policy precheck/postcheck to a versioned executable bundle.
- Prove no-direct-client, no-internal-store, evidence-allowlist, prompt-injection, leakage, timeout, and error mapping.
- Implement or explicitly retire the AI Focus worker placeholder.

### P2 — provider and operational maturity

- Admit a live provider only after mock-only closure and security/resource review.
- Add provider health, timeout, cancellation, concurrency, and model-identity evidence.
- Define replay and nondeterminism posture.
- Prove correction propagation across API, Explorer, cache, receipt, and release surfaces.
- Establish monitoring that does not log raw sensitive prompts or evidence.

### Unknowns that remain intentionally open

- accepted governed-AI and provider stewards;
- independent review and separation of duties;
- production provider/model selection;
- deployed route, runtime, and network topology;
- public release scope;
- retention jurisdiction and operational incident response.

---

## 26 · Related folders

- [`docs/architecture/README.md`](../README.md)
- [`docs/architecture/ui/README.md`](../ui/README.md)
- [`docs/architecture/governed-api/README.md`](../governed-api/README.md)
- [`apps/governed-api/README.md`](../../../apps/governed-api/README.md)
- [`apps/governed-api/src/ai/README.md`](../../../apps/governed-api/src/ai/README.md)
- [`apps/explorer-web/README.md`](../../../apps/explorer-web/README.md)
- [`apps/workers/src/ai_focus_worker/README.md`](../../../apps/workers/src/ai_focus_worker/README.md)
- [`runtime/model_adapters/README.md`](../../../runtime/model_adapters/README.md)
- [`runtime/ollama/README.md`](../../../runtime/ollama/README.md)
- [`contracts/runtime/README.md`](../../../contracts/runtime/README.md)
- [`schemas/contracts/v1/runtime/README.md`](../../../schemas/contracts/v1/runtime/README.md)
- [`schemas/contracts/v1/focus/README.md`](../../../schemas/contracts/v1/focus/README.md)
- [`policy/runtime/README.md`](../../../policy/runtime/README.md)
- [`packages/envelopes/README.md`](../../../packages/envelopes/README.md)
- [`tests/runtime_proof/README.md`](../../../tests/runtime_proof/README.md)
- [`data/receipts/README.md`](../../../data/receipts/README.md)
- [`release/README.md`](../../../release/README.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)

---

## 27 · Last reviewed

**Reviewed:** 2026-08-14 against `main@710173d51a3a6bf288997df6f3eb4bf7f4da1ef6`.

### Evidence ledger

| Evidence class | Included | Excluded conclusion |
|---|---|---|
| Current repository bytes | Target, sibling inventory, ADRs, routes, implementations, contracts, schemas, policy docs, tests, workflows | Does not prove deployment or release |
| Bounded component tests | Envelope, MockAdapter, Focus projection, local validators | Does not prove orchestration or authority closure |
| Hosted evidence | Prior workflow surfaces were inspected only where explicitly cited by governing ADRs/docs | No exact-head runtime claim for this README update |
| External provider/runtime | Not exercised | No provider availability, security, or performance claim |
| Release/publication | Not exercised | No KFM publication claim |

### Non-effects of this revision

This documentation-only update does not:

- accept or reject an ADR;
- choose a canonical overview;
- alter a contract, schema, policy rule, fixture, test, workflow, route, adapter, worker, receipt, release, correction, or rollback object;
- invoke a provider, resolve evidence, evaluate policy, validate citations, or emit an AIReceipt;
- release, deploy, publish, or change repository settings.

A future revision should update the evidence snapshot rather than preserving stale implementation claims.
