<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-governed-ai-readme
title: Governed AI Subsystem — Architecture README
type: architecture-readme
version: v2.1.0-draft
status: draft; repository-grounded; active-landing-page; explanatory; no-runtime-authority
owners:
  - '@bartytime4life — verified CODEOWNERS review route'
owner_status: 'CODEOWNERS routing is confirmed; governed-AI, Governed API, evidence, policy, citation, security, privacy, correction, release, UI, and accessibility stewardship assignments and independent review remain NEEDS VERIFICATION.'
created: 2026-05-15
updated: 2026-08-20
policy_label: public
truth_posture: cite-or-abstain
owning_root: docs/
responsibility: 'Provide the current human landing page for the governed-AI subsystem and explain how Governed API, evidence, policy, citation, adapters, finite envelopes, receipts, clients, correction, and release responsibilities compose without becoming decision, semantic, machine-shape, policy, runtime, review, release, or publication authority.'
current_path: docs/architecture/governed-ai/README.md
canonical_relationship: 'CONFIRMED CURRENT TOPOLOGY — same-path survivor and active subsystem landing page after merged PR #3149 removed docs/architecture/governed-ai.md; this status is a repository-navigation fact, not runtime, semantic, policy, or release authority.'
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 21cdb5ff7d630a39f70fc03d44b31b91eb63b1aa
  target_prior_blob: 9e1071bb69910bde3f364d319923c4db00637639
  retired_flat_overview_path: docs/architecture/governed-ai.md
  retired_flat_overview_pr: 3149
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  adapter_architecture_blob: d38351198939b63a57e583cb404a0daf379fa3a4
  ai_receipts_architecture_blob: 721bf4647f49a510a597d7b3c4d305bc70fa3097
  boundaries_architecture_blob: 6bd100cfe7a7727df9d729bf211e24c2303c7974
  continuity_architecture_blob: f99bf873de43433af6b427278e96d2af4e436f61
  focus_flow_architecture_blob: 6f6d98f4101acfe686d20d31665317240d705f42
  mock_first_architecture_blob: 7d123cab64a6da5dd6a191dd5b42d44418f3da23
  ollama_architecture_blob: 1a2c8445d8ad87ca1a012d8f284c38d907cd7c71
  prompt_injection_architecture_blob: ebc8af5bf8d9937ee0c387b3c022bead10ac8e3c
  route_map_architecture_blob: d7284c1129629925e2c54b90382932d7775581d6
  governed_api_routes_blob: 3418168d0b267160d6ad6dd87f289e880ef4a024
  governed_api_stub_blob: 371e60d9f96c78e31c8a1e6109d19dee5da4213b
  mock_adapter_blob: 04d37e59b14c9e3b85126cb3380b6221b44e26d1
  ollama_adapter_blob: 1769a719d6a6df53e001abbc4c67ad486ab5c944
  runtime_response_schema_blob: 8b86e7db8b18b65a56a4e639dfc54e1b2db93155
  ai_receipt_schema_blob: 2e0bebdb3a38acbc3c58a919db46970c6e829b4a
  ai_receipt_builder_blob: 5fe03c96f22ea99b3e8689b92c7ee23d4fc12a65
  evidence_resolver_readme_blob: d64f112e9fe6538178c74dd31cc751235781c7f3
  citation_validation_contract_blob: 29c507e76a9c15c44f2c195b7342e93630cdc701
  generated_receipt_lane_blob: 5a67f8d743306799a014590ccb45fa9f1177f16a
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
inspection_boundary: >
  Current-session GitHub reads covered the complete prior README; current main;
  the governed-AI direct-child inventory; merged PR #3149 and its one-file deletion;
  accepted Directory Rules v2 and ADR-0029; current governed-AI companions;
  Governed API route registration and fail-closed stubs; Focus request/response
  scaffolds; model-adapter implementations; RuntimeResponseEnvelope and AIReceipt
  schemas; the AIReceipt candidate builder; the internal non-authoritative evidence
  resolver; CitationValidationReport meaning; and generated-receipt requirements.
  No model daemon, provider endpoint, credential, authenticated AI route, grant store,
  authoritative evidence service, active policy evaluator, composed citation service,
  AIReceipt emitter or durable store, deployed Focus operation, runtime log, release
  environment, correction propagation, rollback drill, or publication was exercised.
related:
  - docs/architecture/README.md
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
  - runtime/model_adapters/MockAdapter.py
  - runtime/model_adapters/OllamaAdapter.py
  - contracts/runtime/runtime_response_envelope.md
  - contracts/runtime/ai_receipt.md
  - contracts/evidence/citation_validation_report.md
  - schemas/contracts/v1/runtime/runtime_response_envelope.schema.json
  - schemas/contracts/v1/runtime/ai_receipt.schema.json
  - schemas/contracts/v1/focus/focus_request.schema.json
  - schemas/contracts/v1/focus/focus_response.schema.json
  - packages/envelopes/src/envelopes/ai_receipt.py
  - packages/evidence-resolver/README.md
  - data/receipts/generated/README.md
  - schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, architecture, governed-ai, focus-mode, model-adapter, evidence-resolver, runtime-response-envelope, ai-receipt, citation-validation, policy, mock-first, ollama, finite-outcomes, trust-membrane, cite-or-abstain]
notes:
  - 'v2.1.0-draft closes the README-local navigation and authority fallout from merged PR #3149 without recreating the retired flat overview.'
  - 'The same-path landing page remains explanatory; accepted Directory Rules govern placement, while governed-AI route, adapter, and provider decisions remain proposed or unassigned.'
  - 'Eight companions now carry repository-grounded updates from 2026-08-19 or 2026-08-20; PROMPT_INJECTION.md remains proposal-era and ROUTE_MAP.md retains known stale flat-overview metadata.'
  - 'Current bounded proof includes the internal evidence-resolver candidate, CitationValidationReport fixture profile, RuntimeResponseEnvelope helpers, MockAdapter selector, and AIReceipt builders and validators; no end-to-end AI operation is established.'
  - 'This revision changes documentation and its generated authoring receipt only.'
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed AI Subsystem — Architecture README

> **Governed AI is an interpretive subsystem, not a truth source or publication path.** Its intended role is to turn already-governed context into bounded language behind the Governed API while preserving evidence, policy, citation, precision, freshness, correction, receipt, and finite-outcome boundaries. Current repository evidence proves several bounded components, not an operational end-to-end AI route.

[![status](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#2--authority-level)
[![landing page](https://img.shields.io/badge/landing%20page-current%20survivor-0969da?style=flat-square)](#current-canonicality-conflict)
[![runtime](https://img.shields.io/badge/runtime-PARTIAL%20%2F%20HOLD-d4a72c?style=flat-square)](#5--repo-fit)
[![API route](https://img.shields.io/badge/governed%20AI%20route-absent-b42318?style=flat-square)](#12--the-governed-ai-request-flow)
[![provider](https://img.shields.io/badge/live%20provider-none%20admitted-6e7781?style=flat-square)](#13--adapter-boundary)
[![publication](https://img.shields.io/badge/publication-none-6e7781?style=flat-square)](#17--trust-membrane-and-exposure-controls)

> [!IMPORTANT]
> **Architecture explanation is not decision or runtime authority.** This README explains current repository relationships. `contracts/` owns semantic meaning, `schemas/` owns machine shape, `policy/` owns admissibility rule source, implementation roots own executable behavior, and `release/` owns release, correction, withdrawal, and rollback decisions. Accepted ADR-0029 and the adopted Directory Rules govern placement; the governed-AI route, adapter, provider, and Focus-boundary decisions remain proposed or unassigned.

> [!CAUTION]
> **Bounded proofs must not be promoted into an AI-integration claim.** The repository has a deterministic no-I/O `MockAdapter`, a closed four-outcome `RuntimeResponseEnvelope`, an internal non-authoritative evidence-resolver candidate, a fixture-first `CitationValidationReport` profile, AIReceipt candidate builders and validation, and defensive Explorer Focus projection. It does not have a verified governed-AI API route, active composed policy/evidence/citation transaction, AIReceipt emitter/store, admitted provider, deployed Focus operation, or public AI release.

> [!WARNING]
> **The flat overview has been retired.** Merged [PR #3149](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3149) removed `docs/architecture/governed-ai.md`; this README is now the tracked subsystem landing page and same-path survivor. That repository-topology fact does not accept an ADR or create runtime authority. Stale references to the retired path elsewhere in the repository remain inherited documentation debt and require a separate bounded cleanup.

**Quick navigation:** [Purpose](#1--purpose) · [Authority](#2--authority-level) · [Belongs](#3--what-belongs-here) · [Exclusions](#4--what-does-not-belong-here) · [Repo fit](#5--repo-fit) · [Tree](#6--proposed-directory-tree) · [Inputs](#7--inputs) · [Outputs](#8--outputs) · [Doctrine](#9--core-doctrine) · [Objects](#10--object-families-and-homes) · [Outcomes](#11--finite-outcomes--the-trust-grammar) · [Flow](#12--the-governed-ai-request-flow) · [Adapters](#13--adapter-boundary) · [Citations](#14--citation-validation) · [Policy](#15--policy-precheck-and-postcheck) · [Receipts](#16--aireceipt-and-replay-discipline) · [Exposure](#17--trust-membrane-and-exposure-controls) · [Validation](#18--validation) · [Siblings](#19--sibling-docs-in-this-folder) · [Anti-patterns](#20--anti-patterns) · [Propagation](#21--update-propagation) · [Rollback](#22--rollback) · [Review](#23--review-burden) · [ADRs](#24--adrs) · [Open work](#25--open-questions-and-verification-backlog) · [Related](#26--related-folders) · [Evidence](#27--last-reviewed)

---

<a id="1--purpose"></a>
## 1 · Purpose

This README is the human architecture entry point for the **governed-AI responsibility seam**. It explains how KFM intends to compose:

1. a caller-facing Focus or AI-assisted request;
2. governed scope, identity, release, evidence, policy, rights, and sensitivity checks;
3. minimized admissible context;
4. a provider-neutral model-adapter boundary;
5. an untrusted structured candidate;
6. structured-output and citation validation;
7. policy postcheck, precision, freshness, and correction disclosure;
8. one finite `RuntimeResponseEnvelope`; and
9. separate `AIReceipt` accountability when an accepted operation requires it.

This page may explain responsibility, dependency direction, current maturity, conflicts, validation, correction, and rollback. It must not accept an ADR, define canonical object meaning, amend a schema, activate policy, admit a provider, authorize a route, approve review, release an artifact, or turn a bounded component test into a public runtime claim.

The governing sequence is:

```text
scope
  -> authenticate and authorize
  -> resolve release, evidence, freshness, and correction state
  -> policy precheck and context minimization
  -> provider-neutral adapter
  -> structured candidate validation
  -> citation validation
  -> policy postcheck and precision enforcement
  -> finite RuntimeResponseEnvelope
  -> separate AIReceipt accountability
  -> governed client projection
```

Every step remains subordinate to evidence, policy, review, release, correction, and rollback.

---

<a id="2--authority-level"></a>
## 2 · Authority level

| Field | Current value |
|---|---|
| **Path** | `docs/architecture/governed-ai/README.md` — confirmed tracked file |
| **Owning root** | `docs/` |
| **Responsibility** | Current human landing page and cross-root architecture explanation for the governed-AI subsystem |
| **Authority kind** | Explanatory; not decision, contract, schema, policy, evidence, receipt, runtime, review, release, or publication authority |
| **Placement basis** | Accepted ADR-0029 adopts Directory Rules v2; this existing same-path architecture document receives `PLACE` |
| **Current topology** | Same-path survivor after merged PR #3149 removed the former flat overview |
| **Verified review route** | `.github/CODEOWNERS` routes the repository and relevant roots to `@bartytime4life` |
| **Stewardship** | Governed-AI, API, evidence, policy, citation, security, privacy, correction, release, UI, and accessibility stewardship remains `NEEDS VERIFICATION` |
| **Decision status** | Governed-AI route, adapter, provider, and Focus-boundary decisions remain proposed or unassigned |
| **Runtime status** | `PARTIAL / HOLD`: bounded component proofs exist; end-to-end governed orchestration is not established |
| **Release/publication effect** | None |

Architecture prose cannot override current contracts, schemas, policy, implementation, evidence, review, or release records. Conversely, checked-in implementation does not silently accept a proposed ADR.

<a id="current-canonicality-conflict"></a>
### Current landing-page relationship

The previous edition correctly recorded a conflict between two tracked overviews. That conflict changed when merged [PR #3149](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3149) deleted `docs/architecture/governed-ai.md` as a one-file retirement. Current repository topology therefore has one governed-AI subsystem landing page: this README.

The safe conclusion is bounded:

- **CONFIRMED:** this README is the surviving tracked landing page and folder entrypoint.
- **CONFIRMED:** the deleted flat file is no longer a current repository path.
- **NEEDS VERIFICATION:** all inbound links, prose references, document registries, and cached or external consumers have not been closed by this README update.
- **PROPOSED / HOLD:** any broader claim of architectural canonicality beyond current navigation still depends on accepted decisions and consumer closure.

This revision does not recreate the retired file, add an alias, rewrite every stale reference, or change another document's authority.

---

<a id="3--what-belongs-here"></a>
## 3 · What belongs here

This directory contains human architecture documents that explain distinct governed-AI concerns across responsibility roots.

Current tracked siblings:

- [`ADAPTER_CONTRACT.md`](./ADAPTER_CONTRACT.md) — repository-grounded provider-neutral adapter boundary and current mock proof.
- [`AI_RECEIPTS.md`](./AI_RECEIPTS.md) — repository-grounded AIReceipt architecture and accountability boundary.
- [`BOUNDARIES.md`](./BOUNDARIES.md) — repository-grounded trust-membrane and forbidden-path reference.
- [`CONTINUITY_NOTES.md`](./CONTINUITY_NOTES.md) — repository-grounded continuity, lineage, and correction limits.
- [`FOCUS_FLOW.md`](./FOCUS_FLOW.md) — current client proof and proposed server-side Focus flow.
- [`MOCK_FIRST.md`](./MOCK_FIRST.md) — deterministic mock-first sequencing and proof boundary.
- [`OLLAMA_INTEGRATION.md`](./OLLAMA_INTEGRATION.md) — deferred provider-specific local-runtime boundary.
- [`PROMPT_INJECTION.md`](./PROMPT_INJECTION.md) — proposal-era security doctrine requiring evidence refresh and broken-reference repair.
- [`ROUTE_MAP.md`](./ROUTE_MAP.md) — repository-grounded executable route inventory with known stale flat-overview metadata.
- `README.md` — this landing page and subsystem map.

A new sibling should be added only when the concern cannot be handled accurately by this page, an existing sibling, a per-root README, a contract, policy documentation, a runbook, or an ADR.

---

<a id="4--what-does-not-belong-here"></a>
## 4 · What does NOT belong here

| Responsibility | Owning surface |
|---|---|
| Adapter, provider, route, or finite-envelope decisions | `docs/adr/` |
| AI-as-assistant, cite-or-abstain, trust membrane, or lifecycle doctrine | `docs/doctrine/` |
| RuntimeResponseEnvelope, AIReceipt, PolicyDecision, EvidenceBundle, CitationValidationReport, or Focus object meaning | `contracts/` |
| Machine-checkable fields and compatibility constraints | `schemas/contracts/v1/` |
| Allow, deny, abstain, restrict, redact, or obligation rules | `policy/` |
| Executable model adapters | `runtime/model_adapters/` |
| Governed API orchestration and route registration | `apps/governed-api/` |
| Browser projection and accessibility behavior | `apps/explorer-web/` |
| Worker execution | `apps/workers/` |
| Reusable evidence or envelope implementation | `packages/` |
| Synthetic proof candidates and executable tests | `fixtures/` and `tests/` |
| Receipt instances and process-accountability records | governed `data/receipts/` lanes |
| Release, correction, withdrawal, and rollback decisions | `release/` and their governing object families |
| Secrets, credentials, model weights, protected source content, restricted geometry, private review notes, or private chain-of-thought | never this public documentation path |

Examples here must remain compact, synthetic, public-safe, and explicitly non-authoritative.

---

<a id="5--repo-fit"></a>
## 5 · Repo fit

The subsystem spans several responsibility roots. Current evidence does **not** prove that they are composed into one operational transaction.

```text
Explorer Focus projection         PARTIAL — defensive client logic, injected resolver
  -> Governed API                 PARTIAL — /bootstrap, /layers, /evidence only
  -> Governed API AI subtree      PLACEHOLDER — documentation/scaffold only
  -> evidence resolution          BOUNDED INTERNAL CANDIDATE — non-authoritative
  -> runtime policy               HOLD — no composed evaluator binding proved
  -> MockAdapter                  BOUNDED PROOF — deterministic no-I/O selector
  -> OllamaAdapter                PLACEHOLDER — one comment line
  -> citation report              BOUNDED PROFILE — contract/schema/validator, not a service
  -> RuntimeResponseEnvelope      BOUNDED PROOF — closed schema, helpers, fixtures, tests
  -> AIReceipt                    BOUNDED SHAPE/BUILD — no emitter or durable store
  -> ai_focus_worker              PLACEHOLDER
  -> public governed AI answer    NOT ESTABLISHED
```

### Current maturity matrix

| Surface | Confirmed state | Safe conclusion |
|---|---|---|
| Governed-AI folder | Ten tracked Markdown files including this README | Documentation exists; presence does not prove every statement current |
| Retired flat overview | Merged [PR #3149](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3149) removed `docs/architecture/governed-ai.md` | This README is the current same-path survivor; stale consumers remain separate debt |
| Modernized companions | Eight companions were repository-grounded on 2026-08-19 or 2026-08-20 | Their evidence snapshots are bounded and do not create runtime authority |
| `PROMPT_INJECTION.md` | Proposal-era May 2026 document with a missing `STATE_OWNERSHIP.md` reference and speculative fields | Useful doctrine lineage; current repo claims need refresh |
| `ROUTE_MAP.md` | Current route inventory, but metadata still references the retired flat overview | Route facts are useful; document-relationship text needs later correction |
| `MockAdapter.py` | Deterministic no-I/O selector for prevalidated complete synthetic envelopes | Fixture-selection proof, not semantic adapter or model integration |
| RuntimeResponseEnvelope | Closed proposed schema, fixtures, validators, helpers, and proof tests | Shape and local candidate-building proof only |
| AIReceipt | Closed proposed nine-field schema, validator, candidate builder, and mock-outcome projection | Bounded construction proof; no runtime emitter/store |
| Governed API registry | `/bootstrap`, `/layers`, `/evidence` | No AI or Focus route is registered |
| Governed API stubs | Deterministic `ABSTAIN / NOT_IMPLEMENTED`, with fail-closed error shape | Trust-membrane scaffold, not an AI route |
| Governed API AI subtree | Documentation and scaffold only | No composed orchestration implementation |
| Explorer Focus resolver | Defensive projection over an injected resolver and allowlisted evidence refs | Client projection boundary; no direct model or store authority |
| Focus request/response schemas | Empty permissive proposed scaffolds with `additionalProperties: true` | No stable Focus wire contract is established |
| Internal evidence resolver | Standard-library `v1alpha1` candidate with `authoritative: false` | `RESOLVED` only continues governed checks; no public answer or AI composition |
| CitationValidationReport | Proposed fixture-first contract/schema/validator family over declared states | Internal consistency proof; no source/evidence/policy/release authentication |
| Runtime policy | Repository policy surfaces exist; composed evaluator binding is not proved | Policy precheck/postcheck remains `HOLD` for an AI transaction |
| `OllamaAdapter.py` | One-line placeholder | No provider is admitted or invoked |
| `ai_focus_worker/main.py` | Placeholder | No worker execution path |
| Hosted workflows | Component-focused workflows exist for mock, envelope, receipt, evidence, and citation surfaces | A green component workflow would not prove end-to-end runtime or release |

### State distinctions

Keep these separate:

- **file present** — bytes exist;
- **shape proof** — schema/validator accepts and rejects reviewed cases;
- **component proof** — one bounded implementation behaves deterministically;
- **orchestration proof** — components compose in the intended order;
- **policy/evidence/citation closure** — referenced authorities resolve and are applicable;
- **runtime proof** — a known revision executed in a controlled environment;
- **release/publication** — a separately authorized outward transition occurred.

No state implies the next.

---

<a id="6--proposed-directory-tree"></a>
## 6 · Proposed directory tree

This heading is retained for inbound compatibility. The tree below is a **current responsibility map**, not a proposal to create paths.

```text
docs/architecture/governed-ai/            subsystem explanation and navigation
apps/governed-api/                         public trust membrane and future orchestration
apps/explorer-web/                         caller projection and trust-visible UI
apps/workers/src/ai_focus_worker/          worker placeholder
runtime/model_adapters/                    provider-neutral adapter lane
runtime/ollama/                            deferred provider-specific runtime lane
contracts/runtime/                         RuntimeResponseEnvelope and AIReceipt meaning
contracts/evidence/                        evidence and citation-report meaning
schemas/contracts/v1/runtime/              runtime machine shapes
schemas/contracts/v1/focus/                permissive Focus scaffolds
schemas/contracts/v1/evidence/             evidence and citation-report machine shapes
policy/runtime/ and policy/focus/           admissibility rule sources and documentation
packages/envelopes/                        bounded envelope/receipt candidate helpers
packages/evidence-resolver/                internal non-authoritative resolver candidate
fixtures/ and tests/                        synthetic cases and bounded proof
sites under data/receipts/                  process memory; never truth or release authority
release/                                   release/correction/withdrawal/rollback decisions
```

Directory Rules basis: this README remains under `docs/architecture/` because it explains a cross-root subsystem to humans. It does not create a new root, move authority, or convert a compatibility path into canon.

---

<a id="7--inputs"></a>
## 7 · Inputs

A mature governed-AI operation should accept only explicit, validated, bounded inputs. Current repository support varies.

| Input family | Required meaning | Current posture |
|---|---|---|
| Caller request | Requested task, selected scope, locale, interaction identity, and caller capabilities | Focus schemas are permissive scaffolds; wire contract unresolved |
| Scope context | Geography, time, feature/layer identity, release identity, and precision ceiling | Partially represented; no end-to-end contract proof |
| Evidence context | Allowlisted `EvidenceRef`s that resolve to admissible `EvidenceBundle`s | Internal candidate exists; authoritative service composition absent |
| Policy context | Effective bundle/version, caller role, sensitivity, rights, consent, sovereignty, and obligations | Composed runtime evaluation not established |
| Freshness/correction context | `as_of`, freshness, supersession, correction, withdrawal, and release state | Envelope fields and evidence-history objects exist; transaction binding absent |
| Adapter request | Minimized provider-neutral context and output constraints | Proposed by architecture/ADR material; no accepted machine contract established |
| Provider configuration | Explicit provider/model allowlist and resource/security limits | No live provider admitted |

### Input invariants

1. Client-provided evidence references are candidates, not resolved truth.
2. Context minimization happens before the adapter boundary.
3. RAW, WORK, QUARANTINE, canonical/internal, restricted, and unpublished stores are not normal adapter inputs.
4. Prompt text never carries authority merely because it is labeled system, trusted, or policy.
5. Unknown rights, sensitivity, release, review, or correction state fails closed.
6. Private chain-of-thought is neither an input requirement nor a receipt field.
7. Untrusted text from users, evidence, connectors, tools, and model output remains data, never instructions to the control plane.

---

<a id="8--outputs"></a>
## 8 · Outputs

The intended outward response family is the finite `RuntimeResponseEnvelope`. An `AIReceipt` is separate process memory and never substitutes for the response, evidence, policy, review, release, correction, or publication state.

### Current RuntimeResponseEnvelope profile

The current closed schema requires:

| Field | Current rule |
|---|---|
| `id` | Required string with bounded identity pattern |
| `spec_hash` | Required `sha256:` identity |
| `version` | Required version string |
| `issued_at` | Required date-time |
| `outcome` | Exactly `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` |
| `reason_code` | Required finite reason string |
| `evidence_refs` | Required unique array; at least one for `ANSWER` |
| `policy_state` | Required policy posture |
| `freshness` | Required freshness posture |
| `correction_state` | Required correction posture |
| `precision_actually_used` | Required for `ANSWER`; forbidden for non-`ANSWER` outcomes |
| additional properties | Denied at the top level |

The bounded builder validates local shape/profile rules. It does not resolve evidence, evaluate policy, calculate freshness, authorize precision, approve correction closure, or release a response.

### Current AIReceipt profile

The closed AIReceipt schema requires exactly these top-level fields:

- `id`
- `run_id`
- `adapter`
- `model_ref`
- `inputs_digest`
- `outputs_digest`
- `policy_decision_ref`
- `citation_validation_ref`
- `outcome`

The candidate builder performs bounded local checks over caller-supplied values. The validator and focused tests prove shape and limited consistency only. Runtime emission, persistence, reference resolution, retention, signing, replay, correction propagation, and public exposure are not established.

### Output rules

- `ANSWER` must be bounded by resolved evidence, allowed policy, validated citations, current or declared freshness, correction state, and supported precision.
- `ABSTAIN`, `DENY`, and `ERROR` are successful finite responses when their conditions apply.
- A provider candidate is untrusted until structured validation and postcheck complete.
- A receipt records a process; it does not prove the answer true or publishable.
- Debug traces, raw prompts, private reasoning, credentials, internal paths, and protected payloads do not belong in outward envelopes.

---

<a id="9--core-doctrine"></a>
## 9 · Core doctrine

The subsystem inherits these rules:

1. **EvidenceBundle outranks generated language.**
2. **Cite or abstain.** A consequential statement either resolves support or does not claim it.
3. **Public clients use governed interfaces.** No direct browser-to-model or browser-to-canonical-store path.
4. **AI is interpretive.** It does not decide source authority, rights, sensitivity, review, release, correction, or rollback.
5. **Finite outcomes are first class.** Failure must not degrade into unsupported prose.
6. **Derived stays derived.** Summaries, embeddings, indexes, graphs, maps, and model output remain downstream carriers.
7. **Correction history is preserved.** A later answer does not erase an earlier released state.
8. **Promotion is a governed transition.** A commit, pull request, merge, passing test, receipt, deployment, or badge is not publication.
9. **Sensitive context fails closed.** Harmful precision and unclear rights trigger denial, abstention, generalization, staged access, delay, or review.
10. **Determinism is preferred where practical.** Identity, fixtures, diagnostics, and replay inputs should be inspectable.
11. **Receipts, proofs, reports, decisions, releases, and publications remain separate object families.**
12. **Documentation states boundaries; it does not execute them.**

---

<a id="10--object-families-and-homes"></a>
## 10 · Object families and homes

| Object or responsibility | Semantic home | Machine/implementation home | Current posture |
|---|---|---|---|
| RuntimeResponseEnvelope | `contracts/runtime/` | runtime schema, envelope package, validators, fixtures, tests | Bounded proof; proposed profile |
| AIReceipt | `contracts/runtime/` | strict schema, validator, candidate builders, focused tests | Bounded shape/build proof; no emitter/store |
| Focus request/response | No accepted semantic contract established in the inspected path | permissive Focus schemas and client projection | `HOLD` |
| Adapter boundary | proposed ADR and architecture docs | `runtime/model_adapters/` | Mock selector proven; production seam and live provider absent |
| EvidenceRef/EvidenceBundle | `contracts/evidence/` | internal evidence-resolver candidate and validators | Non-authoritative internal alpha; not composed into AI route |
| VerificationStateHistory | `contracts/evidence/` | schema, validator, and bounded resolver replay | Bounded evidence-history support; no operational store |
| PolicyDecision | policy/decision contracts | evaluator and policy bundle | Runtime AI binding absent |
| CitationValidationReport | `contracts/evidence/` | strict proposed schema, fixture validator, tests, workflow | Declaration-consistency proof; no composed citation service |
| GENERATED_RECEIPT | generated-receipt contract/schema | `data/receipts/generated/` and validator | Authoring provenance only; not runtime AIReceipt or review authority |
| Release/correction/rollback records | release contracts and decisions | `release/` and accountability lanes | Not exercised by this documentation update |

Do not duplicate one of these object families inside this directory. Architecture pages link to the authority surface; they do not redefine it.

### Non-collapse rules

- `EvidenceRef` is not `EvidenceBundle`.
- Resolver `RESOLVED` is not `ANSWER`, policy `ALLOW`, review approval, or release.
- Citation `PASS` is not evidence truth, source admission, rights clearance, or public authorization.
- `AIReceipt` is not a `GENERATED_RECEIPT`, EvidenceBundle, proof, policy decision, review record, release manifest, or publication record.
- RuntimeResponseEnvelope is not an answer store, canonical evidence object, or release manifest.
- A browser projection, fixture, test, workflow, commit, or merge is not release or publication.

---

<a id="11--finite-outcomes--the-trust-grammar"></a>
## 11 · Finite outcomes — the trust grammar

| Outcome | Use | Minimum safe posture |
|---|---|---|
| `ANSWER` | Admissible, in-scope response | Resolved evidence, allowed policy, validated citations, current or declared freshness, visible correction state, supported precision |
| `ABSTAIN` | Evidence missing, stale, conflicted, unsupported, unresolved, or scope too broad | Stable reason code and no fabricated answer |
| `DENY` | Policy, rights, sensitivity, caller capability, consent, sovereignty, or precision blocks exposure | Stable reason code; do not leak protected details through explanation |
| `ERROR` | Tool, resolver, policy, adapter, validator, receipt, or orchestration failure | Stable reason code; no unsafe fallback |

A safe default precedence is:

1. malformed input or failed component state -> `ERROR`;
2. explicit rights, sensitivity, access, consent, sovereignty, or purpose prohibition -> `DENY`;
3. unresolved, stale, conflicted, corrected, withdrawn, or inadequate support -> `ABSTAIN`;
4. `ANSWER` only after every required positive gate closes.

The MockAdapter scenario matrix proves selection of all four complete synthetic envelope outcomes. It does not prove that real evidence or policy selected the correct outcome.

---

<a id="12--the-governed-ai-request-flow"></a>
## 12 · The governed AI request flow

### Target architecture

```text
caller request
  -> validate request and scope
  -> authenticate and authorize caller
  -> resolve release, evidence, freshness, correction, rights, and sensitivity
  -> policy precheck and context minimization
  -> build provider-neutral adapter request
  -> invoke admitted adapter
  -> parse untrusted structured candidate
  -> validate structure and citations
  -> policy postcheck and precision enforcement
  -> assemble RuntimeResponseEnvelope
  -> emit/store AIReceipt when required
  -> return through Governed API
```

### Current stage-by-stage posture

| Stage | Current result |
|---|---|
| Caller Focus projection | Partial defensive TypeScript logic exists |
| Stable Focus wire contract | `HOLD`; schemas are permissive scaffolds |
| Governed API AI route | Absent from route registry |
| AI orchestration | Placeholder subtree only |
| Evidence resolution | Internal non-authoritative candidate exists; authoritative service composition absent |
| Policy composition | Not established |
| Context minimization contract | Proposed in docs and ADR material |
| Mock candidate selection | Implemented bounded proof |
| Live adapter invocation | Absent |
| Structured candidate parsing | Not established end to end |
| Citation validation | Fixture-first report validation exists; composed service absent |
| Policy postcheck | Not established |
| Final envelope assembly | Local builder exists; orchestration integration absent |
| AIReceipt candidate construction | Bounded helper and tests exist |
| AIReceipt emission/store | Not established |
| Public governed answer | Not established |

The correct operational classification is **PARTIAL / HOLD**, not implemented and not absent.

---

<a id="13--adapter-boundary"></a>
## 13 · Adapter boundary

The adapter boundary should remain provider-neutral and narrow.

### Confirmed current implementations

**MockAdapter**

- loads a caller-supplied fixed scenario matrix;
- requires complete synthetic envelopes covering all four finite outcomes;
- returns isolated deep copies deterministically;
- rejects malformed configuration and unknown scenarios;
- performs no network, subprocess, socket, model, file-write, evidence, policy, citation, receipt, or release operation.

It is therefore a **bounded selector**, not a semantic model adapter.

**OllamaAdapter**

- is a one-line placeholder;
- proves only that a path and filename exist;
- does not establish model discovery, invocation, timeout, resource limits, structured output, health checks, provider identity, receipt generation, or security controls.

### Required provider-admission evidence

Before a live provider can graduate, require at least:

- an accepted adapter boundary and finite-envelope decision;
- explicit provider/model allowlisting and traceable model identity;
- no direct client access;
- bounded input/output sizes, timeouts, cancellation, and resource limits;
- no uncontrolled tool, network, subprocess, or filesystem access;
- deterministic negative fixtures and failure mapping;
- structured-output parsing that fails closed;
- evidence, citation, and policy integration outside provider authority;
- AIReceipt emission and retention rules;
- security, privacy, rights, operations, correction, and rollback review.

Provider availability is a runtime fact, not architecture authority.

---

<a id="14--citation-validation"></a>
## 14 · Citation validation

Citation validation is a trust-bearing responsibility independent of model fluency.

A mature operation must verify, as applicable:

1. every consequential claim has a citation or the response abstains;
2. references are allowlisted for the current request;
3. each `EvidenceRef` resolves to the intended `EvidenceBundle` or finite failure;
4. cited evidence supports the claim, geography, time, role, precision, and qualification;
5. stale, corrected, superseded, withdrawn, denied, or unresolved support is visible;
6. citations do not expose restricted source text, paths, reasons, or geometry;
7. validator output is finite, deterministic where practical, and receipt-addressable.

### Current implementation boundary

The repository now contains a proposed, closed `CitationValidationReport` contract/schema, deterministic fixture validator, negative and positive cases, focused tests, and workflow wiring. That bounded profile derives `PASS`, `ABSTAIN`, `DENY`, or `ERROR` from caller-declared upstream states. It does not contact a source, resolve an EvidenceRef, authenticate an EvidenceBundle, evaluate policy, authenticate review, verify release, or authorize publication.

No composed citation-validation service was established in the inspected governed-AI route because no such route exists. Until composition is proved:

- do not claim citation closure for a live answer;
- do not emit `ANSWER` merely because references are syntactically present;
- do not treat `citation_validation_ref` as resolved authority;
- prefer `ABSTAIN` or `ERROR` when required validation is unavailable.

---

<a id="15--policy-precheck-and-postcheck"></a>
## 15 · Policy precheck and postcheck

Policy must surround provider invocation rather than live inside the provider.

### Precheck responsibilities

- authenticate and authorize caller and operation;
- verify release, rights, sensitivity, consent, sovereignty, and access posture;
- restrict evidence set and precision;
- minimize prompt and context content;
- deny RAW, WORK, QUARANTINE, canonical/internal, and unpublished material;
- determine whether provider invocation is allowed at all.

### Postcheck responsibilities

- validate finite outcome and reason code;
- enforce allowed evidence and citation set;
- enforce precision and generalization obligations;
- screen prohibited disclosures and protected details;
- preserve freshness, correction, supersession, withdrawal, and release state;
- decide whether the candidate may become a RuntimeResponseEnvelope.

### Current policy state

Repository policy surfaces and documentation exist, but no accepted effective bundle, evaluator binding, Governed API consumer, or end-to-end AI allow/deny proof was established. Policy precheck and postcheck therefore remain **HOLD** for an operational AI transaction.

A Rego file, schema, README, or green syntax test is not a PolicyDecision.

---

<a id="16--aireceipt-and-replay-discipline"></a>
## 16 · AIReceipt and replay discipline

AIReceipt is process memory. It is not evidence truth, policy approval, review approval, release authority, correction closure, or publication.

### Current proven boundary

- proposed semantic contract exists;
- closed nine-field machine schema exists;
- deterministic candidate builder exists;
- MockAdapter-outcome-to-receipt candidate projection and focused tests exist;
- local validator and path-scoped workflow exist;
- runtime emitter, durable store, resolver, and query surface are not established;
- referenced policy and citation records are not proven resolved by receipt validation;
- signing, retention, replay, correction, supersession, and deletion behavior are not established.

### Minimum future replay packet

A replayable operation should bind, through accepted contracts and referenced records:

- exact caller/request identity and scope;
- evidence and release identities used;
- policy decision and effective policy version;
- adapter and model identity;
- deterministic input and output digests;
- citation-validation result;
- finite outcome;
- correction or supersession relationship;
- environment or nondeterminism disclosures needed to interpret replay.

The current AIReceipt schema does not carry all of those fields. Future expansion requires contract/schema/consumer compatibility work; documentation must not invent them as present.

Do not place raw prompts, full sensitive context, credentials, private chain-of-thought, or protected evidence in a receipt merely to make replay easier.

### Correction behavior

A corrected operation should preserve prior receipt identity, identify the correcting or superseding operation through the owning object families, update outward release/correction state, and invalidate affected caches or derived surfaces where applicable. Silent overwrite is not correction.

---

<a id="17--trust-membrane-and-exposure-controls"></a>
## 17 · Trust membrane and exposure controls

### Allowed public path

```text
public client
  -> Governed API
  -> released and public-safe evidence/policy context
  -> admitted adapter behind the API, when allowed
  -> validation and finite envelope
  -> public client
```

### Denied normal paths

- browser directly to Ollama or another provider;
- browser directly to RAW, WORK, QUARANTINE, canonical/internal, proof, or steward stores;
- provider directly reading repository paths or source stores;
- client-supplied references becoming authoritative without resolution;
- model output bypassing citation or policy postcheck;
- debug/error output leaking prompts, evidence excerpts, policy internals, restricted reasons, or precise protected geometry;
- worker, watcher, receipt, test, commit, merge, or deployment writing `PUBLISHED` state by implication.

### Local exposure

A local provider must still use deny-by-default network exposure, explicit binding, least privilege, authenticated API mediation, bounded resources, auditable configuration, and no direct public client traffic. Local does not mean trusted or public-safe.

### Sensitive contexts

Archaeology, cultural and sacred places, rare species, living-person and genomic data, private land, critical infrastructure, hazards, and unclear-rights material remain denied, generalized, quarantined, staged, delayed, or abstained until qualified authority supports exposure. Aggregation, embeddings, graph projection, maps, tiles, or generated summaries do not automatically declassify the source.

---

<a id="18--validation"></a>
## 18 · Validation

Validation claims must name the layer they prove.

### Confirmed bounded proof

| Proof surface | Current coverage | Does not prove |
|---|---|---|
| RuntimeResponseEnvelope schema, fixtures, validators, helpers, and tests | Four outcomes, required fields, precision profile, negative cases, deterministic candidate assembly | Evidence truth, policy choice, citation support, release |
| MockAdapter tests | Four scenarios, determinism, isolation, malformed configuration, unknown scenario, no-I/O | Provider behavior, evidence/policy/citation integration |
| AIReceipt schema, validator, builders, projection, and tests | Closed nine-field candidates and bounded consistency | Emission, storage, reference resolution, retention, replay, signing |
| Evidence-resolver fixtures and tests | Internal deterministic candidate resolution, verification-history replay, no-network negatives | Authoritative evidence closure, policy, public outcome, release |
| CitationValidationReport fixtures and validator | Closed report shape, declared-state consistency, finite results, deterministic identity | Source contact, evidence authentication, rights/policy/review/release authority |
| Explorer Focus resolver tests and logic | Defensive projection and finite client failure posture | Server route, model invocation, authoritative evidence resolution, policy enforcement |
| Component workflows | Path-scoped no-network checks | Whole-system Focus runtime, deployment, release, or publication |

### Graduation gates

End-to-end governed AI remains on HOLD until the repository proves at least:

- [ ] accepted adapter/finite-envelope decision and resolved overlap with the unassigned Focus candidate;
- [ ] non-permissive caller, adapter-request, adapter-candidate, and final-response contracts;
- [ ] registered Governed API route with authentication and authorization;
- [ ] authoritative EvidenceRef-to-EvidenceBundle resolution and allowlist enforcement;
- [ ] executable policy precheck/postcheck with effective-version binding;
- [ ] structured candidate parser and stable failure codes;
- [ ] composed citation validation with negative fixtures;
- [ ] precision, freshness, correction, supersession, withdrawal, and release enforcement;
- [ ] AIReceipt emission, validation, storage, resolution, retention, and correction behavior;
- [ ] provider admission or explicit mock-only scope;
- [ ] no-direct-client, no-internal-store, prompt-injection, leakage, timeout, cancellation, and resource-limit tests;
- [ ] hosted exact-head evidence and required-check posture appropriate to risk;
- [ ] rollback and correction drill;
- [ ] release decision for any outward use.

A green component test is necessary evidence for that component and nothing more.

---

<a id="19--sibling-docs-in-this-folder"></a>
## 19 · Sibling docs in this folder

| Document | Current use | Current caution |
|---|---|---|
| `ADAPTER_CONTRACT.md` | Repository-grounded adapter seam and bounded mock proof | Production seam and provider admission remain proposed |
| `AI_RECEIPTS.md` | Current schema-paired receipt architecture, builders, validator, and proof | No operational emitter, store, retention, or correction path |
| `BOUNDARIES.md` | Current trust boundaries, API stubs, resolver candidate, object-family separation | Bounded guards are not deployed end-to-end enforcement |
| `CONTINUITY_NOTES.md` | Current continuity and lineage architecture | No live continuity runtime or durable AIReceipt store |
| `FOCUS_FLOW.md` | Current client proof and proposed server orchestration | No registered Focus route or public operation |
| `MOCK_FIRST.md` | Current deterministic mock proof and sequencing | Mock proof does not establish provider readiness |
| `OLLAMA_INTEGRATION.md` | Current repository-grounded deferred provider plan | OllamaAdapter remains a placeholder; daemon/model state unknown |
| `PROMPT_INJECTION.md` | Useful security doctrine and threat vocabulary | Proposal-era evidence, missing `STATE_OWNERSHIP.md` reference, and speculative receipt fields require modernization |
| `ROUTE_MAP.md` | Current executable route inventory and legacy taxonomy crosswalk | Metadata and prose still reference the retired flat overview |

Read each page within its declared evidence snapshot. A newer date or larger document does not automatically outrank contracts, schemas, policy, code, tests, or accepted decisions.

---

<a id="20--anti-patterns"></a>
## 20 · Anti-patterns

Do not:

- call bounded envelope proof an operational AI system;
- place model invocation in the browser;
- let a provider select authoritative evidence or policy;
- treat resolver `RESOLVED` as `ANSWER`;
- treat a citation string or report `PASS` as evidence resolution or release;
- treat an AIReceipt or GENERATED_RECEIPT as truth, review, or publication authority;
- accept permissive Focus scaffolds as a stable wire contract;
- expose raw prompts, private reasoning, credentials, repository paths, or restricted evidence;
- silently map provider failures to `ANSWER`;
- hide stale, corrected, superseded, withdrawn, denied, or generalized states;
- copy architecture prose into contracts or schemas as a parallel authority;
- use a documentation update to accept an ADR or provider;
- let watchers, workers, tests, commits, pull requests, merges, deployments, or receipts publish by implication;
- recreate the retired flat overview or add a second landing page without an explicit authority, migration, consumer, and rollback decision;
- fabricate replay from file modification times, commit times, or missing records.

---

<a id="21--update-propagation"></a>
## 21 · Update propagation

Update this README when a material governed-AI surface changes, but update the owning authority first or in the same coherent reviewed packet.

| Change | Required companion review |
|---|---|
| RuntimeResponseEnvelope fields or outcomes | Contract, schema, builder, fixtures, tests, compatibility notes |
| AIReceipt fields or lifecycle | Contract, schema, validator, builders/emitter/store, retention/correction docs, tests |
| Evidence resolver behavior | Evidence contracts, schemas, fixtures, validator, consumers, policy/release boundaries |
| Citation report or service behavior | Contract, schema, validator, fixtures, reason codes, policy/release integration |
| Adapter interface or provider admission | ADR, adapter contract, runtime implementation, tests, security/runbook |
| Governed API route | Route registry, request/response contracts, authorization, policy, tests, route map |
| Policy behavior | Policy source, evaluator/bundle version, fixtures, tests, obligations, rollback |
| Focus client behavior | Focus contracts/schemas, Explorer implementation, accessibility and negative-state tests |
| Release/publication posture | Release manifest/decision, correction, rollback, cache and client behavior |
| Landing-page or path retirement | Parent navigation, inbound links, registries, aliases/tombstones if required, validation, rollback |

Do not update this page first and then cite it as authority for a behavior change.

---

<a id="22--rollback"></a>
## 22 · Rollback

### Documentation rollback

Restore immediate prior target blob:

```text
9e1071bb69910bde3f364d319923c4db00637639
```

and remove only the generated authoring receipt added with this revision. That reverses the README refresh without recreating `docs/architecture/governed-ai.md` or changing adapters, routes, contracts, schemas, policy, tests, evidence, receipts, release state, deployment, or public behavior.

### Implementation rollback expectations

Future runtime changes must define their own rollback unit. At minimum preserve:

- previous compatible request/response and adapter contract versions;
- provider disable or deny path;
- prior policy bundle and decision references;
- evidence, receipt, and correction lineage;
- cache invalidation and client finite-failure behavior;
- no fallback to direct model or internal-store access.

Rollback must not erase evidence of an earlier released answer, receipt, correction, or withdrawal.

---

<a id="23--review-burden"></a>
## 23 · Review burden

| Change class | Minimum review posture |
|---|---|
| Editorial clarification in this README | Docs/architecture review route |
| Repository-evidence refresh | Docs plus affected implementation owner |
| Contract/schema field or enum change | Contract/schema/consumer/compatibility review |
| Evidence or citation behavior | Evidence, citation, policy, validation, and affected consumer review |
| Policy or sensitivity behavior | Policy, security/privacy, affected-domain, and negative-test review |
| New provider or model | Runtime, security, evidence, policy, API, resource, operations, and rollback review |
| New public AI route | API, authentication, evidence, policy, citation, UI, accessibility, correction, and release review |
| Landing-page retirement or path migration | Architecture/docs decision plus consumer, fragment, link, and rollback review |

CODEOWNERS routing is not proof that these reviews occurred or that separation of duties exists.

---

<a id="24--adrs"></a>
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

Merged [PR #3149](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/3149) retired a duplicate documentation path. It did not accept or reject any governed-AI ADR. This README changes no decision status.

---

<a id="25--open-questions-and-verification-backlog"></a>
## 25 · Open questions and verification backlog

### P0 — authority and trust closure

- Resolve ADR-0019 overlap with the unassigned Focus adapter-boundary candidate.
- Define accepted caller, adapter-request, adapter-candidate, and final-envelope boundaries.
- Replace permissive Focus scaffolds before declaring a stable wire contract.
- Establish authoritative evidence, executable policy, and composed citation validation before any `ANSWER` route.
- Define AIReceipt emission, storage, resolution, retention, correction, access, and deletion policy.
- Repair remaining active references to retired `docs/architecture/governed-ai.md` through a separately bounded consumer-aware cleanup.

### P1 — bounded implementation and documentation closure

- Register an authenticated mock-only Governed API route with explicit non-public and no-release posture.
- Implement orchestration over existing synthetic proof surfaces without a live provider.
- Bind policy precheck/postcheck to a versioned executable bundle.
- Prove no-direct-client, no-internal-store, evidence-allowlist, prompt-injection, leakage, timeout, cancellation, and error mapping.
- Implement or explicitly retire the AI Focus worker placeholder.
- Modernize `PROMPT_INJECTION.md` against current contracts, schemas, paths, receipts, and tests.
- Refresh `ROUTE_MAP.md` metadata and relationship prose after flat-overview retirement.

### P2 — provider and operational maturity

- Admit a live provider only after mock-only closure and security/resource review.
- Add provider health, timeout, cancellation, concurrency, and model-identity evidence.
- Define replay and nondeterminism posture.
- Prove correction propagation across API, Explorer, cache, receipt, and release surfaces.
- Establish monitoring that does not log raw sensitive prompts or evidence.

### Unknowns that remain intentionally open

- accepted governed-AI and provider stewards;
- independent review and separation of duties;
- production provider and model selection;
- deployed route, runtime, and network topology;
- public release scope;
- retention jurisdiction and operational incident response.

---

<a id="26--related-folders"></a>
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
- [`contracts/evidence/README.md`](../../../contracts/evidence/README.md)
- [`schemas/contracts/v1/runtime/README.md`](../../../schemas/contracts/v1/runtime/README.md)
- [`schemas/contracts/v1/focus/README.md`](../../../schemas/contracts/v1/focus/README.md)
- [`schemas/contracts/v1/evidence/README.md`](../../../schemas/contracts/v1/evidence/README.md)
- [`policy/runtime/README.md`](../../../policy/runtime/README.md)
- [`policy/focus/README.md`](../../../policy/focus/README.md)
- [`packages/envelopes/README.md`](../../../packages/envelopes/README.md)
- [`packages/evidence-resolver/README.md`](../../../packages/evidence-resolver/README.md)
- [`tests/runtime_proof/README.md`](../../../tests/runtime_proof/README.md)
- [`data/receipts/README.md`](../../../data/receipts/README.md)
- [`data/receipts/ai/README.md`](../../../data/receipts/ai/README.md)
- [`data/receipts/generated/README.md`](../../../data/receipts/generated/README.md)
- [`release/README.md`](../../../release/README.md)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md)

---

<a id="27--last-reviewed"></a>
## 27 · Last reviewed

**Reviewed:** 2026-08-20 against `main@21cdb5ff7d630a39f70fc03d44b31b91eb63b1aa`.

### Evidence ledger

| Evidence class | Included | Excluded conclusion |
|---|---|---|
| Current repository topology | Target, ten-file folder inventory, merged PR #3149 deletion, current main | Does not prove every stale consumer is repaired |
| Current repository bytes | Companions, routes, stubs, adapters, contracts, schemas, policy docs, packages, tests, and receipt requirements | Does not prove deployment or release |
| Bounded component proof | Envelope, MockAdapter, AIReceipt builders/validator, evidence resolver, citation report, Focus projection | Does not prove orchestration or authority closure |
| Hosted exact-head evidence | Pending after feature-branch and draft-PR creation | No hosted result is claimed here before it exists |
| External provider/runtime | Not exercised | No provider availability, security, performance, or model-rights claim |
| Release/publication | Not exercised | No KFM release or publication claim |

### Non-effects of this revision

This documentation-only update does not:

- recreate the retired flat overview, rewrite all remaining stale consumers, or change another document's authority;
- accept or reject an ADR;
- alter a contract, schema, policy rule, fixture, test, workflow, route, adapter, worker, package, evidence object, runtime receipt, release, correction, or rollback record;
- invoke a provider, resolve authoritative evidence, evaluate policy, compose citation validation, or emit a runtime AIReceipt;
- release, deploy, publish, activate a source or provider, or change repository settings.

Future revisions should refresh the pinned evidence snapshot rather than preserving stale implementation claims.
