# policy

> **One-line purpose.** `policy/` is KFM's canonical responsibility root for admissibility rules: it decides whether a bounded operation may proceed, must be restricted or held, should abstain, or must fail closed—without becoming semantic truth, machine shape, evidence, runtime implementation, lifecycle storage, release approval, or publication authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-readme
title: policy/ — Canonical Admissibility Root
version: v0.2
status: draft; repository-grounded; mixed-maturity; evaluator-unbound; bundle-unaccepted; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; accepted policy stewardship and independent approval controls were not established
updated: 2026-07-23
current_path: policy/README.md
owning_root: policy/
base_commit: 19670ca8e2c8a709fc69cd41173851f8359c8281
prior_blob: 09cd966ab188d5e831960869117522a98274cb7f
truth_posture: CONFIRMED singular policy root, selected child READMEs, nonempty Rego inventory, PolicyDecision shape fixtures, readiness-hold workflows, structural boundary tests, placeholder runtime, and CODEOWNERS routing / PROPOSED root contract and implementation sequence / CONFLICTED policy-result vocabularies and mixed schema placement / UNKNOWN accepted evaluator, active bundle, production consumers, receipt replay, and release integration
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Root: policy](https://img.shields.io/badge/root-policy%2F-0969da?style=flat-square)](#authority-level)
[![Authority: admissibility](https://img.shields.io/badge/authority-admissibility-8250df?style=flat-square)](#authority-level)
[![Rego sources: present](https://img.shields.io/badge/Rego%20sources-present-2da44e?style=flat-square)](#status)
[![Evaluator: unbound](https://img.shields.io/badge/evaluator-unbound-d97706?style=flat-square)](#current-maturity)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Maturity](#current-maturity) · [Outcomes](#outcome-vocabularies) · [Authoring](#policy-authoring-contract) · [Sensitive policy](#rights-sensitivity-consent-and-public-exposure) · [Trust membrane](#runtime-and-public-trust-membrane) · [Rollback](#correction-and-rollback) · [Open verification](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion:** `policy/` is the repository responsibility root for policy and admissibility, and nonempty Rego source exists. Current evidence does **not** establish an accepted evaluator, active bundle, Rego test modules, functional policy-runtime package, complete input contract, dedicated policy validator, decision-receipt flow, or release-gate integration.

> [!CAUTION]
> A policy result cannot create evidence, clear rights by assertion, infer consent, downgrade sensitivity, promote lifecycle state, approve release, make generated language authoritative, or turn a map, tile, file path, commit, or pull request into public truth.

---

## Purpose

`policy/` owns KFM's **admissibility posture** and reviewed policy source.

It answers one bounded question:

> Given an explicit operation, actor or caller, audience, governed object references, source and evidence context, rights, consent, sensitivity, lifecycle state, review state, release context, and policy version, may the operation proceed—and under which enforceable obligations?

Policy decisions should be operation-specific, evidence-aware, reason-coded, obligation-bearing, replayable where practical, and fail-closed when required context is missing or untrusted. `policy/` decides admissibility; it does not decide whether a claim is factually true.

[Back to top](#top)

---

## Authority level

**Canonical responsibility root for admissibility and policy source; non-semantic, non-schema, non-evidence, non-runtime, non-release, and non-publication authority.**

Directory Rules assign admissibility to singular `policy/`. ADR-0003 proposes formally freezing that choice and treating any `policies/` path as compatibility; the ADR remains **proposed**.

| Responsibility | Owning surface | `policy/` role |
|---|---|---|
| Policy rules and admissibility | `policy/` | Own reviewed rule source and policy-family boundaries. |
| Object meaning | [`contracts/policy/`](../contracts/policy/README.md) | Consume meaning; never redefine it here. |
| Machine shape | [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Require accepted shapes; never become schema authority. |
| Evidence and source authority | evidence and registry roots | Evaluate supplied status; never invent it. |
| Evaluation mechanics | [`packages/policy-runtime/`](../packages/policy-runtime/README.md) or accepted evaluator | Supply accepted rules; do not place reusable runtime code here. |
| Validation and tests | [`tools/validators/policy/`](../tools/validators/policy/README.md), `tests/`, `fixtures/` | Prove bounded behavior; passing is not a decision instance. |
| Release and rollback | [`release/`](../release/README.md) | Supply required gate decisions; never approve or publish by itself. |
| Public enforcement | governed APIs and applications | Consume normalized decisions; never load policy source directly. |

[Back to top](#top)

---

## Status

| Surface | Current status | Safe conclusion |
|---|---:|---|
| `policy/README.md` | **CONFIRMED short stub at base** | This v0.2 update replaces it in place. |
| Singular `policy/` root | **CONFIRMED / doctrine-aligned** | Current policy work belongs here unless an accepted ADR changes the split. |
| Rego source inventory | **CONFIRMED nonempty** | Presence does not prove tests, bundle membership, activation, or correct evaluation. |
| Rego test modules | **CONFIRMED absent under the readiness workflow's reviewed rule** | A real evaluator test lane remains unwired. |
| `policy/bundles/` | **CONFIRMED README-only in enforced inventory** | No accepted bundle artifact, manifest, selector, signature, or activation is established. |
| Policy runtime | **CONFIRMED `0.0.0` placeholder** | No functional evaluator is established. |
| Policy validator lane | **CONFIRMED README + `.gitkeep` in enforced inventory** | No accepted dedicated policy validator executes today. |
| `PolicyDecision` shape | **CONFIRMED concrete `PROPOSED` schema** | `outcome` is closed to `ANSWER | ABSTAIN | DENY | ERROR`; shape is not execution. |
| Shape fixtures | **CONFIRMED two valid + three invalid** | Bounded JSON shape polarity is exercised. |
| `PolicyInputBundle` shape | **CONFIRMED permissive `PROPOSED` stub** | Requiring only `id` does not enforce rich policy context. |
| `policy-test` workflow | **CONFIRMED readiness holds** | It evaluates no policy and emits no `PolicyDecision`. |
| `policy-boundary-guards` | **CONFIRMED 15-test structural/static/API suite** | It protects selected trust boundaries; it is not evaluator or release proof. |
| Active evaluator, bundle selector, receipts, release integration | **UNKNOWN / NEEDS VERIFICATION** | No complete governed evaluation flow was proved. |
| Required checks and independent approval | **UNKNOWN / NEEDS VERIFICATION** | CODEOWNERS routing is not branch-protection or separation-of-duties evidence. |

[Back to top](#top)

---

## What belongs here

- this root README and child policy-lane READMEs;
- reviewed Rego, OPA-compatible, or equivalent declarative policy modules;
- operation-specific access, evidence, consent, sensitivity, rights, render, export, AI, lifecycle, promotion, release-gate, correction, and rollback policy source;
- domain-specific admissibility rules under a domain segment, not a new root;
- fail-closed defaults preserving unknown, missing, stale, conflicted, restricted, and false as distinct states;
- stable rule package names, entrypoints, versions, reason codes, obligations, and supersession notes;
- future immutable bundle source and manifest inputs under an accepted `policy/bundles/` contract;
- synthetic or public-safe native policy tests after the repository accepts a colocation convention;
- links to paired contracts, schemas, fixtures, tests, validators, receipts, proofs, consumers, release gates, correction paths, and rollback targets.

A file belongs here because its primary responsibility is **admissibility**, not because it mentions privacy, security, AI, maps, release, or a domain.

[Back to top](#top)

---

## What does NOT belong here

| Do not put this in `policy/` | Correct responsibility |
|---|---|
| Semantic definitions | `contracts/` |
| JSON Schema, DTO, enum, or field shape | `schemas/contracts/v1/` |
| Source payloads, credentials, or registry instances | connectors, secret stores, or accepted `data/registry/` lanes |
| EvidenceBundles, proof packs, citations, or claim truth | evidence/proof roots |
| RAW through PUBLISHED data | `data/<phase>/` |
| Emitted decisions, receipts, reviews, validation reports, or proofs | accepted lifecycle, receipt, proof, review, or report roots |
| Evaluator, adapter, CLI, server, or package code | `packages/`, `apps/`, `runtime/`, or `tools/` by responsibility |
| Validator implementation | `tools/validators/` |
| Generic fixtures and tests | `fixtures/` and `tests/` |
| Release manifests, approvals, rollback cards, corrections, withdrawals | `release/` |
| Public API routes, UI, MapLibre logic, exports, or AI responses | governed application/runtime roots |
| Real sensitive locations, living-person records, DNA/genomic content, or consent tokens | denied; use synthetic/redacted references |
| A second independently evolving policy root | compatibility/migration only after accepted ADR |
| Generated prose presented as a policy grant or approval | governed review; generated language is interpretive only |

[Back to top](#top)

---

## Inputs

Policy evaluation must use an **explicit, versioned input bundle** and must not silently fetch missing facts.

| Input class | Minimum governed context | Fail-closed trigger |
|---|---|---|
| Operation | stable capability, request/candidate ID, family, evaluation time | unknown or overly broad operation |
| Actor and audience | subject/service class, purpose, public/restricted/steward audience | missing identity context where access differs |
| Object and scope | stable refs, domain, space/time scope, requested precision | raw payload substituted for governed refs |
| Source and evidence | SourceDescriptor refs, source roles, EvidenceBundle status, citations, freshness | unresolved source role, terms, or support |
| Rights, consent, sensitivity | license/terms, consent applicability/revocation, classification, transform decisions | unknown, expired, revoked, or unsupported posture |
| Lifecycle, review, release | current/requested state, validation/proof refs, reviewer state, release/correction/rollback refs | skipped state, missing review, or ungoverned public exposure |
| Policy execution | bundle ID/version/digest, evaluator profile/version, entrypoint, input hash | unaccepted or non-replayable evaluator context |

The current `PolicyInputBundle` schema does not enforce this complete context. Schema validity is not policy readiness.

[Back to top](#top)

---

## Outputs

A policy evaluation may produce an engine-native result, a normalized `PolicyDecision` candidate, public-safe reason codes, enforceable obligations, governed references, receipt-ready replay metadata, or an explicit readiness hold.

Policy outputs do **not** by themselves prove a claim, authorize a lifecycle transition, approve release, satisfy missing evidence or rights, or become public merely because their shape validates.

[Back to top](#top)

---

## Validation

| Surface | What it proves now | What it does not prove |
|---|---|---|
| `policy-test / opa-test` | Required files and Rego exist; accepted evaluator prerequisites remain absent. | Any rule was evaluated. |
| `policy-test / fixture coverage` | Reviewed `PolicyDecision` shape inventory and fixtures remain stable. | Correct inputs, rules, reasons, obligations, or bundle identity. |
| Schema harness | Selected schemas and fixtures validate structurally. | Correct policy, rights, sensitivity, or release approval. |
| `policy-boundary-guards` | Fifteen selected structural/static/API trust-membrane tests. | Policy-bundle evaluation or policy-root rule coverage. |

Current command posture:

- the root `Makefile` policy target still prints a TODO command;
- no repository-approved evaluator command, version, bundle selector, or native test convention is established;
- `make boundary-guards-ci` is structural proof, not a policy evaluator;
- shape checks remain separate from rule evaluation.

Before executable policy is treated as active, require an accepted evaluator and bundle, complete input profile, positive/negative native tests, deterministic CI command, reason/obligation enforcement, governed consumer, receipts and replay, correction/expiry/rollback tests, sensitive negative cases, no-network fixtures, read-only CI, and observed required-check success.

[Back to top](#top)

---

## Review burden

CODEOWNERS routes `/policy/` changes to `@bartytime4life`. That is review routing, not an accepted stewardship assignment or proof of independent approval.

| Change class | Minimum review posture |
|---|---|
| README-only clarification | Policy-aware maintainer plus docs review. |
| Rule module | Policy steward, affected owner, and validation reviewer. |
| Access/identity/capability | Policy + security/identity + application owner. |
| Rights/consent/living-person/DNA/cultural/archaeology/rare-species/infrastructure | Relevant specialist plus policy, privacy/security, and release reviewer; fail closed without ownership. |
| Bundle, selector, signing, activation | Policy-runtime, supply-chain/security, validation, and release review. |
| Outcome normalization or obligations | Policy, contracts, schemas, runtime consumer, and API/UI review. |
| Contract/schema change | Contract + schema + policy + validator/test + migration review. |
| Promotion/release/correction/rollback | Policy + release + evidence/proof + operations review with separation of duties where required. |

Accepted policy stewardship and required-review enforcement remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Related folders

| Surface | Relationship |
|---|---|
| [`contracts/policy/`](../contracts/policy/README.md) | Semantic policy-object meaning. |
| [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Machine shape; mixed maturity is documented there. |
| [`fixtures/contracts/v1/policy/`](../fixtures/contracts/v1/policy/README.md) | Reusable shape fixtures. |
| `tests/policy/` | Structural tests and future evaluator-backed proof. |
| [`packages/policy-runtime/`](../packages/policy-runtime/README.md) | Proposed evaluator helper; currently a placeholder. |
| [`tools/validators/policy/`](../tools/validators/policy/README.md) | Policy-validator routing; currently README-only. |
| `data/registry/`, `data/receipts/`, `data/proofs/` | Source context, process memory, and proof support. |
| [`release/`](../release/README.md) | Promotion, release, correction, withdrawal, and rollback authority. |
| [`apps/governed-api/`](../apps/governed-api/README.md) | Public trust-membrane consumer. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Placement and README contract. |
| [`policy-test`](../.github/workflows/policy-test.yml) | Explicit policy readiness holds. |
| [`policy-boundary-guards`](../.github/workflows/policy-boundary-guards.yml) | Structural/static/API trust-boundary suite. |

Selected child indexes: [`access/`](./access/README.md) · [`ai_builder/`](./ai_builder/README.md) · [`bundles/`](./bundles/README.md) · [`consent/`](./consent/README.md) · [`contract/`](./contract/README.md) · [`data/`](./data/README.md) · [`decision/`](./decision/README.md) · [`domains/`](./domains/README.md) · [`evidence/`](./evidence/README.md) · [`focus/`](./focus/README.md)

[Back to top](#top)

---

## ADRs

| ADR | Status | Relevance |
|---|---:|---|
| [`ADR-0003 — policy/ singular is canonical`](../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) | **PROPOSED** | Singular root and plural compatibility treatment. |
| [`ADR-0001 — schema home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Policy schema placement. |
| [`ADR-0002 — contracts vs schemas`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT** | Meaning/shape separation. |
| [`ADR-0020 — abstain is first class`](../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | **PROPOSED** | Closed outward outcome model. |
| Evaluator, bundle, normalization, activation | **NOT ACCEPTED / NEEDS VERIFICATION** | Operational policy substrate decisions remain open. |

This README may document open decisions. It must not accept an ADR or activate a bundle through prose.

[Back to top](#top)

---

## Last reviewed

**2026-07-23** against `main@19670ca8e2c8a709fc69cd41173851f8359c8281`.

Reviewed: complete prior root stub, Directory Rules README order, CODEOWNERS, ADR-0003, selected child READMEs and Rego sources, policy contracts/schemas/fixtures, `policy-test`, policy runtime/validator boundaries, and structural policy-boundary workflow.

Not established: exhaustive recursive inventory; full workflow matrix and branch protection; accepted evaluator/bundle; production consumers; receipts, replay, release integration, rollback execution; accepted stewards or independent approval controls.

[Back to top](#top)

---

## Current maturity

| Level | Evidence required | Root-wide posture |
|---|---|---:|
| M0 — Placeholder | stub README or default-only module | **CONFIRMED in several lanes** |
| M1 — Boundary documented | responsibility, inputs, outputs, failures, authority split | **CONFIRMED in several lanes** |
| M2 — Rule and shape candidate | reviewed source, contracts/schemas, synthetic fixtures, stable entrypoint | **PARTIAL / mixed** |
| M3 — Evaluator-backed proof | accepted evaluator/bundle, native tests, input assembly, normalization, deterministic CI | **NOT ESTABLISHED** |
| M4 — Governed consumer and replay | consumer, receipts, replay, expiry, correction, cache invalidation | **NOT ESTABLISHED** |
| M5 — Release-significant enforcement | required checks, independent review, deployment evidence, rollback drill | **UNKNOWN / NOT ESTABLISHED** |

State maturity per lane and per governed flow. A root with some M2 files is not an M2 system.

[Back to top](#top)

---

## Outcome vocabularies

| Axis | Examples | Meaning |
|---|---|---|
| Canonical outward `PolicyDecision.outcome` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Closed four-value schema. |
| Engine-native results | `ALLOW`, `RESTRICT`, `HOLD`, `DENY`, sometimes `ABSTAIN`/`ERROR` | Lower-level semantics requiring explicit normalization. |
| Validation | `PASS`, `FAIL`, validator codes | Check result; never policy permission. |
| Workflow readiness | `WORKFLOW_HOLD`, `WORKFLOW_SKIPPED_EXPLICIT` | CI statement that prerequisites are intentionally absent. |
| Lifecycle/release | candidate, held, released, withdrawn, superseded | State-transition vocabulary owned elsewhere. |
| Truth labels | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` | Evidence posture; not decisions. |

Do not emit native values into a closed outward schema, map abstention to denial, map evaluator failure to denial, or interpret validator pass as release approval. Preserve reasons, obligations, bundle/evaluator identity, and input hash. If no accepted mapping exists, hold/error rather than invent a value.

[Back to top](#top)

---

## Policy authoring contract

Every material rule should identify stable package/entrypoint/version; explicit input; fail-closed defaults; native and outward outcomes; safe reasons; enforceable obligations; evidence, rights, consent, sensitivity, source-role, lifecycle, and release dependencies; pinned bundle/evaluator identity; synthetic fixtures; positive and negative native tests; receipt metadata; supersession; correction; cache invalidation; and rollback.

A new module is not admissible until path, package identity, evaluator version, inputs, default behavior, outcomes, reasons, obligations, tests, bundle membership, consumer, receipts, and rollback are reviewable.

[Back to top](#top)

---

## Rights, sensitivity, consent, and public exposure

When source rights, consent, living-person or genomic data, archaeology/cultural sovereignty, rare species, critical infrastructure, harmful precision, parcel-person joins, or source-role evidence are unresolved, prefer `DENY`, `HOLD`, `ABSTAIN`, redaction, generalization, aggregation, delay, staged access, or steward review.

Client-side hiding is not a security control. Join-induced sensitivity must propagate. Rules and fixtures must not copy real protected payloads into source, tests, logs, reasons, receipts, or documentation.

[Back to top](#top)

---

## Runtime and public trust membrane

1. Public clients use governed APIs and released, policy-filtered artifacts.
2. Browsers, maps, exports, dashboards, and AI adapters must not load or choose bundles directly.
3. Evaluators receive explicit references and normalized context; no hidden canonical-store fetches.
4. Cache keys bind bundle digest, evaluator version, input hash, audience, purpose, expiry, and correction state.
5. Public reasons are safe; detailed reasons may require restricted review.
6. Obligations are enforced downstream or the operation fails closed.
7. Client filters never replace server-side sensitivity/access decisions.
8. AI may explain decisions with citations; it cannot grant permission or bypass denial/abstention.
9. Evaluation errors never fall back to allow.
10. Evaluator administration and bundle upload are not ordinary public routes.

[Back to top](#top)

---

## Correction and rollback

Material policy changes should be versioned, preserve prior source/bundle/evaluator/test identities for replay, record supersession/effective time, reevaluate affected decisions and releases, invalidate caches, emit correction or withdrawal records through owning roots, and restore a prior accepted bundle/selector during rollback rather than copying files into an ambiguous state.

This v0.2 README changes no policy behavior. Before merge, close the draft PR and abandon its branch. After merge, revert the README commit and generated provenance receipt together. The prior baseline is blob `09cd966ab188d5e831960869117522a98274cb7f`.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---:|
| POL-001 | Is ADR-0003 still proposed in the governing ADR index? | **NEEDS VERIFICATION** |
| POL-002 | What is the complete recursive policy inventory and maturity classification? | **NEEDS VERIFICATION** |
| POL-003 | Which evaluator version and bundle/manifest/selector contract are accepted? | **UNKNOWN** |
| POL-004 | What native-test and fixture placement convention is canonical? | **NEEDS VERIFICATION** |
| POL-005 | When will `PolicyInputBundle` gain a non-permissive operation profile? | **NEEDS VERIFICATION** |
| POL-006 | What mapping joins native results to `ANSWER/ABSTAIN/DENY/ERROR`? | **CONFLICTED / NEEDS ADR** |
| POL-007 | Where are reason-code and obligation registries owned and enforced? | **UNKNOWN** |
| POL-008 | Which governed consumer is the first accepted end-to-end policy slice? | **PROPOSED** |
| POL-009 | What receipt schema and persistence/replay contract are accepted? | **UNKNOWN** |
| POL-010 | Are policy checks required by branch rules, and how is independent approval enforced? | **UNKNOWN / NEEDS VERIFICATION** |
| POL-011 | Which release gates require policy decision, bundle digest, receipt, and replay? | **UNKNOWN** |
| POL-012 | What rollback drill proves prior-bundle restoration and stale-decision invalidation? | **UNKNOWN** |

[Back to top](#top)

---

## No-loss and evidence ledger

| Baseline element | Disposition |
|---|---|
| Stable path and H1 | Preserved |
| Policy-as-code plus documentation purpose | Preserved and bounded |
| Allow/deny/restrict/abstain/redaction/release/promotion/sensitivity scope | Preserved; vocabularies and release authority clarified |
| Singular policy root | Preserved as Directory Rules responsibility; ADR remains proposed |
| OPA/Rego, bundles, fixtures, runtime/promotion/sensitivity/rights/release/UI policy | Preserved and reconciled to current maturity evidence |
| Schema/source/application exclusions | Preserved and expanded |
| Inputs, outputs, validation, review, related folders, status | Preserved and made explicit |
| Required README order, ADRs, last reviewed, rollback | Added |

Evidence used: prior blob `09cd966…`; Directory Rules `2affb080…`; ADR-0003 `cef5528…`; CODEOWNERS `dd2a84a…`; `policy-test.yml` `ba22e40…`; `policy-boundary-guards.yml` `6d442a6…`; policy contract README `e7c409e…`; policy schema README `5129bc9…`; policy runtime README `5a20cfa…`; policy validator README `56ef4bd…`; representative child READMEs and Rego sources.

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| short stub | Before 2026-07-23 | Declared purpose, singular root, basic belongs/exclusions, validation/review/related pointers, and `PROPOSED` status | Blob `09cd966ab188d5e831960869117522a98274cb7f` |
| v0.2 | 2026-07-23 | Same-path repository-grounded modernization with required README order, authority split, maturity evidence, workflow boundaries, outcome separation, authoring rules, sensitive/public controls, rollback, and verification register | Restore prior blob and remove paired generated-work receipt |

<p align="right"><a href="#top">Back to top</a></p>
