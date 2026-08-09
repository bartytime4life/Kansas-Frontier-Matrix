# policy

> **One-line purpose.** `policy/` is KFM's canonical responsibility root for admissibility rules: it decides whether a bounded operation may proceed, must be restricted or held, should abstain, or must fail closed—without becoming semantic truth, machine shape, evidence, runtime implementation, lifecycle storage, release approval, or publication authority.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-readme
title: policy/ — Canonical Admissibility Root
version: v0.3
status: draft; repository-grounded; mixed-maturity; bounded-Rego-evaluation; general-evaluator-unbound; active-bundle-unaccepted; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; accepted policy stewardship and independent approval controls were not established
updated: 2026-08-09
current_path: policy/README.md
owning_root: policy/
base_commit: 41bf408df0458feadd086047a813005b3a052201
prior_blob: fa9378a6a699d0985fd018dbdb9f27c15efcb1c3
directory_governance: ADR-0029 accepted Directory Rules v2 for placement; ADR-0003 remains proposed for the policy/policies compatibility decision
truth_posture: CONFIRMED canonical singular policy root, adopted Directory Rules placement, recursive direct-child inventory, one bounded PROPOSED_INACTIVE Rego release-gate profile with native tests and checksum-pinned OPA 1.19.0 CI, multiple inactive fixture-first policy contracts/schemas/validators/workflows, 18-test structural boundary suite, placeholder policy-runtime package, and broad readiness holds / PROPOSED root contract, active-evaluator sequence, and future consumer binding / CONFLICTED or unresolved source-vs-sources and test-vs-tests child naming plus inactive native-to-outward outcome binding / UNKNOWN repository-wide bundle selector, accepted evaluator, required-check configuration, production consumers, decision receipts, replay, promotion integration, deployment enforcement, and independent release approval
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Root: policy](https://img.shields.io/badge/root-policy%2F-0969da?style=flat-square)](#authority-level)
[![Directory Rules: adopted](https://img.shields.io/badge/Directory%20Rules-v2%20adopted-2da44e?style=flat-square)](#adrs)
[![Bounded Rego lane: tested](https://img.shields.io/badge/bounded%20Rego%20lane-tested-2da44e?style=flat-square)](#validation)
[![General evaluator: unbound](https://img.shields.io/badge/general%20evaluator-unbound-d97706?style=flat-square)](#current-maturity)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [Direct children](#current-direct-child-map) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Maturity](#current-maturity) · [Outcomes](#outcome-vocabularies) · [Authoring](#policy-authoring-contract) · [Sensitive policy](#rights-sensitivity-consent-and-public-exposure) · [Trust membrane](#runtime-and-public-trust-membrane) · [Rollback](#correction-and-rollback) · [Open verification](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion:** `policy/` is the adopted placement for policy source. One bounded, `PROPOSED_INACTIVE` Pass 12 release-gate profile has executable Rego, native Rego tests, exact-polarity fixtures, stable deny reasons, and a dedicated workflow that downloads checksum-pinned OPA 1.19.0. The repository also contains several fixture-first policy profiles with schemas, deterministic validators, tests, and focused workflows. These surfaces do **not** establish a repository-wide active bundle, accepted general evaluator, functional policy-runtime package, authenticated `PolicyDecision` flow, production consumer, promotion authority, release approval, deployment enforcement, or publication.

> [!CAUTION]
> A policy result cannot create evidence, clear rights by assertion, infer consent, downgrade sensitivity, authenticate review, promote lifecycle state, approve release, make generated language authoritative, or turn a map, tile, file path, workflow, commit, or pull request into public truth.

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

Accepted [ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes Directory Rules v2 effective for placement and names singular `policy/` as the policy-source root. [ADR-0003](../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) remains **proposed** for the narrower compatibility and migration decision; its status does not undo the adopted Directory Rules placement.

| Responsibility | Owning surface | `policy/` role |
|---|---|---|
| Policy rules and admissibility | `policy/` | Own reviewed rule source, inactive candidate registries, and policy-family boundaries. |
| Object meaning | [`contracts/policy/`](../contracts/policy/README.md) | Consume meaning; never redefine it here. |
| Machine shape | [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Require accepted shapes; never become schema authority. |
| Evidence and source authority | evidence and registry roots | Evaluate supplied status; never invent it. |
| Evaluation mechanics | [`packages/policy-runtime/`](../packages/policy-runtime/README.md) or an accepted evaluator | Supply accepted rules; do not place reusable runtime code here. |
| Validation and tests | [`tools/validators/policy/`](../tools/validators/policy/README.md), `tests/`, `fixtures/` | Prove bounded shape and semantic behavior; passing is not a decision instance. |
| Release and rollback | [`release/`](../release/README.md) | Supply required gate results; never approve or publish by itself. |
| Public enforcement | governed APIs and applications | Consume normalized decisions; never load policy source directly. |

[Back to top](#top)

---

## Status

| Surface | Current status at `41bf408df045` | Safe conclusion |
|---|---:|---|
| `policy/README.md` | **CONFIRMED v0.2 baseline** | This v0.3 update replaces it in place and preserves the root contract. |
| Singular `policy/` root | **CONFIRMED / adopted placement** | Directory Rules v2 is effective through ADR-0029; no second policy root is authorized. |
| Rego source inventory | **CONFIRMED nonempty** | File presence alone is not activation or correct evaluation. |
| Pass 12 release gate | **CONFIRMED bounded executable profile; `PROPOSED_INACTIVE`** | `policy/rego/release_gate_v1.rego` defaults deny and exposes deterministic reasons. |
| Native Rego tests | **CONFIRMED for one bounded lane** | `release_gate_v1_test.rego` is exercised by its dedicated workflow; no repository-wide native-test convention is accepted. |
| OPA execution | **CONFIRMED in dedicated hosted workflow** | `.github/workflows/pass12-release-policy-v1.yml` checksum-pins OPA 1.19.0 and runs format, unit, fixture-polarity, and deny-reason checks. |
| `policy/bundles/` | **CONFIRMED documentation plus inactive Pass 12 packaging profile** | No non-document bundle payload, accepted manifest, selector, signature, or active bundle is established. |
| Policy runtime | **CONFIRMED `0.0.0` placeholder** | No functional general evaluator, adapter, public API, or consumer library is established. |
| Policy validator lane | **CONFIRMED multiple deterministic Python validators** | They validate inactive contracts, schemas, identities, and bindings; they do not evaluate policy or emit authoritative decisions. |
| `PolicyInputBundle` | **CONFIRMED permissive parent plus explicit profile v1** | The profile checks bounded context for `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`; passing proves coherence only. |
| Decision vocabulary and semantics | **CONFIRMED inactive registries/profiles** | Stable reason, obligation, reviewer-role, and outward-outcome candidates exist; activation and runtime normalization remain unaccepted. |
| Policy evaluation binding | **CONFIRMED declared-only, digest-bound profile** | It binds exact fixture bytes and evaluator declarations; it does not prove evaluator execution or decision authenticity. |
| Obligation carriers | **CONFIRMED fixture-first candidate surfaces** | Structured duties and reduction checks exist without enforcement or release effect. |
| Enforcement maturity | **CONFIRMED fixture-only assessment profile** | A workflow file is not evidence that a check is merge-, promotion-, or runtime-blocking. |
| `policy-test` workflow | **CONFIRMED broad readiness hold plus bounded-lane wiring checks** | It evaluates no repository-wide bundle and emits no `PolicyDecision`, receipt, proof, release, or publication authority. |
| `policy-boundary-guards` | **CONFIRMED 18-test structural/static/API suite** | It protects selected trust boundaries; it is not policy-bundle, rights, sensitivity, or release proof. |
| Active evaluator, bundle selector, decision receipts, governed consumer, promotion integration | **UNKNOWN / NEEDS VERIFICATION** | No complete governed evaluation flow was proved. |
| Required checks and independent approval | **UNKNOWN / NEEDS VERIFICATION** | Workflow presence and CODEOWNERS routing are not branch-protection or separation-of-duties evidence. |

[Back to top](#top)

---

## What belongs here

- this root README and child policy-lane READMEs;
- reviewed Rego, OPA-compatible, or equivalent declarative policy modules;
- operation-specific access, evidence, consent, sensitivity, rights, render, export, AI, lifecycle, promotion, release-gate, correction, and rollback policy source;
- domain-specific admissibility rules under a domain segment, not a new root;
- fail-closed defaults preserving unknown, missing, stale, conflicted, restricted, and false as distinct states;
- stable rule package names, entrypoints, versions, reason codes, obligations, reviewer-role candidates, and supersession notes;
- inactive registries or bundle-packaging profiles whose status and non-effects are explicit;
- synthetic or public-safe native policy tests when the owning policy lane and test convention are reviewable;
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
| Evaluator, adapter, CLI, server, or reusable package code | `packages/`, `apps/`, `runtime/`, or `tools/` by responsibility |
| Validator implementation | `tools/validators/` |
| Reusable generic fixtures and tests | root `fixtures/` and `tests/` |
| Release manifests, approvals, rollback cards, corrections, withdrawals | `release/` |
| Public API routes, UI, MapLibre logic, exports, or AI responses | governed application/runtime roots |
| Real sensitive locations, living-person records, DNA/genomic content, or consent tokens | denied; use synthetic/redacted references |
| A second independently evolving policy root | compatibility or migration only after accepted authority |
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

The permissive parent `PolicyInputBundle` shape remains separate from [`policy_input_bundle_profile_v1`](../contracts/policy/policy_input_bundle_profile_v1.md). The explicit profile makes one bounded subset machine-checkable and fail-closed, but it remains `PROPOSED_INACTIVE`, fixture-only, and non-evaluator.

[Back to top](#top)

---

## Outputs

A policy evaluation may produce:

- an engine-native result such as the Pass 12 profile's `allow`, `deny`, and sorted `deny_reasons`;
- a normalized `PolicyDecision` candidate using the closed outward vocabulary;
- public-safe reason codes and enforceable obligations;
- governed object, bundle, evaluator, review, release, correction, and rollback references;
- receipt-ready input and result digests;
- an explicit readiness hold or operational error.

Policy outputs do **not** by themselves prove a claim, authenticate evidence or review, authorize a lifecycle transition, approve release, satisfy missing rights or sensitivity review, or become public merely because their shape validates or a workflow passes.

[Back to top](#top)

---

## Validation

| Surface | What it proves now | What it does not prove |
|---|---|---|
| `pass12-release-policy-v1` | Checksum-pinned OPA 1.19.0 can format and test the bounded Rego profile; fixtures preserve allow/deny polarity and named deny reasons. | Active bundle selection, cryptographic attestation verification, reviewer authentication, `PolicyDecision` normalization, promotion, release, or publication. |
| `policy-test / OPA readiness hold` | Required files, the bounded Rego lane, its dedicated workflow, the placeholder runtime, and the absence of a repository-wide bundle payload remain explicit. | Repository-wide policy evaluation or an accepted general command. |
| Focused policy validators | Inactive input, decision, binding, obligation, reviewer-role, and maturity candidates satisfy their documented shape and semantic invariants. | Policy execution, consumer enforcement, rights clearance, or release approval. |
| Schema harness | Selected schemas and fixtures validate structurally. | Correct policy, source authority, evidence, rights, sensitivity, or review. |
| `policy-boundary-guards` | Eighteen selected structural/static/API tests in four named modules preserve control-plane, connector/pipeline non-publisher, Explorer adapter/store, and governed-API boundaries. | Policy-bundle evaluation, rights/sensitivity matrices, evidence closure, or release decisions. |

Current command posture:

```bash
# Bounded executable Rego lane — implemented by the dedicated hosted workflow.
opa fmt --fail policy/rego/release_gate_v1.rego policy/rego/release_gate_v1_test.rego
opa test policy/rego/release_gate_v1.rego policy/rego/release_gate_v1_test.rego

# Representative fixture-first policy profile checks.
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_input_bundle_profile_v1.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation_set.py --fixtures

# Structural trust-boundary suite; not a policy evaluator.
make boundary-guards-ci
```

Repository qualifications:

- the root `Makefile` `policy` target still prints a TODO command;
- the OPA binary is installed only by the dedicated workflow; no repository-wide checked-in evaluator or accepted general bundle selector exists;
- the broad `policy-test` job is intentionally static and fail-closed;
- `packages/policy-runtime` remains a comment-only `0.0.0` placeholder;
- Python policy validators are deterministic, no-network candidate validators, not evaluator adapters.

Before executable policy is treated as generally active, require an accepted evaluator and bundle contract, selector and digest binding, complete input assembly, native positive and negative tests, deterministic repository-native command, explicit native-to-outward normalization, reason and obligation enforcement, governed consumer, decision receipts and replay, correction/expiry/rollback tests, sensitive negative cases, read-only CI, and observed required-check plus independent-review evidence.

[Back to top](#top)

---

## Review burden

CODEOWNERS routes `/policy/` changes to `@bartytime4life`. That is review routing, not an accepted stewardship assignment or proof of independent approval.

| Change class | Minimum review posture |
|---|---|
| README-only clarification | Policy-aware maintainer plus docs review. |
| Rule module or native test | Policy steward, affected owner, and validation reviewer. |
| Access/identity/capability | Policy + security/identity + application owner. |
| Rights/consent/living-person/DNA/cultural/archaeology/rare-species/infrastructure | Relevant specialist plus policy, privacy/security, and release reviewer; fail closed without ownership. |
| Bundle, selector, signing, evaluator activation | Policy-runtime, supply-chain/security, validation, and release review. |
| Outcome normalization, reason registry, or obligations | Policy, contracts, schemas, runtime consumer, and API/UI review. |
| Contract/schema change | Contract + schema + policy + validator/test + migration review. |
| Promotion/release/correction/rollback | Policy + release + evidence/proof + operations review with separation of duties where required. |

Accepted policy stewardship, branch-required checks, and independent release approval remain **NEEDS VERIFICATION**.

[Back to top](#top)

---

## Related folders

| Surface | Relationship |
|---|---|
| [`contracts/policy/`](../contracts/policy/README.md) | Semantic policy-object meaning and inactive policy profiles. |
| [`schemas/contracts/v1/policy/`](../schemas/contracts/v1/policy/README.md) | Machine shape; profile maturity remains explicit. |
| [`fixtures/contracts/v1/policy/`](../fixtures/contracts/v1/policy/README.md) | Reusable synthetic contract fixtures. |
| [`fixtures/policy/release_gate_v1/`](../fixtures/policy/release_gate_v1/) | Native Pass 12 Rego input fixtures. |
| `tests/policy/` | Structural trust-boundary tests. |
| `tests/validators/` | Focused candidate-profile validator tests. |
| [`packages/policy-runtime/`](../packages/policy-runtime/README.md) | Proposed evaluator helper; currently a placeholder. |
| [`tools/validators/policy/`](../tools/validators/policy/README.md) | Deterministic policy-profile validators; not evaluators. |
| `data/registry/`, `data/receipts/`, `data/proofs/` | Source context, process memory, and proof support. |
| [`release/`](../release/README.md) | Promotion, release, correction, withdrawal, and rollback authority. |
| [`apps/governed-api/`](../apps/governed-api/README.md) | Public trust-membrane consumer boundary. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Adopted placement and README contract. |
| [`policy-test`](../.github/workflows/policy-test.yml) | Broad fail-closed readiness holds and bounded-lane wiring checks. |
| [`pass12-release-policy-v1`](../.github/workflows/pass12-release-policy-v1.yml) | Exact-head OPA execution for the inactive release-gate profile. |
| [`policy-boundary-guards`](../.github/workflows/policy-boundary-guards.yml) | Eighteen-test structural/static/API trust-boundary suite. |

[Back to top](#top)

---

## Current direct-child map

Directory Rules `ROOT_FULL` requires the root README to map direct children only. The following inventory is verified from the `policy/` tree at `41bf408df0458feadd086047a813005b3a052201`. Presence does not establish adoption, maturity, or equal authority.

```text
policy/
├── README.md
├── access/
├── ai_builder/
├── biotopes/
├── bundles/
├── consent/
├── contract/
├── data/
├── decision/
├── domains/
├── evidence/
├── fixtures/
├── focus/
├── genealogy/
├── geoprivacy/
├── identity/
├── intake/
├── joins/
├── layers/
├── living_persons_geoprivacy.md
├── match-scoring/
├── opa/
├── promotion/
├── proof/
├── redaction/
├── rego/
├── release/
├── review/
├── rights/
├── role/
├── runtime/
├── sensitivity/
├── source/
├── sources/
├── story/
├── supply_chain/
├── telemetry/
├── test/
├── tests/
├── transport/
└── ui/
```

### Child-lane interpretation

| Child family | Current boundary |
|---|---|
| `rego/` | Executable declarative source lane; currently includes the bounded Pass 12 release gate and its native test. |
| `bundles/` | Packaging and selection documentation plus an inactive Pass 12 profile; no accepted executable bundle payload or selector. |
| `decision/` | Inactive candidate registries for decision vocabulary and reviewer roles; not a store for emitted decisions. |
| `domains/` and named domain/topic lanes | Policy source scoped beneath the policy responsibility root; a domain name does not create a new authority root. |
| `fixtures/`, `test/`, `tests/` | Existing policy-local boundaries require continued classification; reusable executable fixtures/tests belong under root `fixtures/` and `tests/`. |
| `source/` and `sources/` | Parallel naming is a drift/ownership question, not evidence of two source-policy authorities. |
| `opa/`, `proof/`, `transport/` | Tracked placeholder or narrow lanes; exact role, writers, and graduation conditions remain **NEEDS VERIFICATION**. |
| `living_persons_geoprivacy.md` | Direct policy source retained at its current path; any move requires reference repair and Directory Rules review. |
| All other children | Existing policy-family lanes. Their README, rule, fixture, consumer, and maturity evidence must be reviewed independently before operational reliance. |

Selected child indexes: [`access/`](./access/) · [`ai_builder/`](./ai_builder/) · [`bundles/`](./bundles/) · [`consent/`](./consent/) · [`decision/`](./decision/) · [`domains/`](./domains/) · [`evidence/`](./evidence/) · [`geoprivacy/`](./geoprivacy/) · [`rights/`](./rights/) · [`sensitivity/`](./sensitivity/) · [`ui/`](./ui/)

[Back to top](#top)

---

## ADRs

| ADR or authority | Status | Relevance |
|---|---:|---|
| [`ADR-0029 — adopt Directory Governance Standard v2`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Makes Directory Rules v2 effective for placement, root classes, and README contracts. |
| [`ADR-0003 — policy/ singular is canonical`](../docs/adr/ADR-0003-policy-singular-is-canonical-%28policies-is-compatibility%29.md) | **PROPOSED** | Compatibility-root and migration decision; not needed to deny a second active policy authority under adopted Directory Rules. |
| [`ADR-0001 — schema home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | **PROPOSED** | Policy schema placement remains configured but not accepted by this ADR. |
| [`ADR-0002 — contracts vs schemas`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | **DRAFT** | Meaning/shape separation. |
| [`ADR-0020 — abstain is first class`](../docs/adr/ADR-0020-abstain-is-a-first-class-decision.md) | **PROPOSED** | Closed outward outcome model. |
| General evaluator, bundle selector, normalization, activation | **NOT ACCEPTED / NEEDS VERIFICATION** | Operational policy-substrate decisions remain open. |

This README may document current bytes and open decisions. It must not accept an ADR, activate a bundle, change a required check, or grant release authority through prose.

[Back to top](#top)

---

## Last reviewed

**2026-08-09** against `main@41bf408df0458feadd086047a813005b3a052201`.

Reviewed:

- the complete v0.2 root README and prior blob `fa9378a6a699d0985fd018dbdb9f27c15efcb1c3`;
- accepted ADR-0029 and the adopted Directory Rules v2 policy/README requirements;
- the recursive `policy/` tree and all direct children;
- ADR-0003, policy/runtime/validator boundaries, and selected child indexes;
- the Pass 12 Rego source, native tests, fixtures, bundle-profile README, and exact-head OPA workflow;
- `policy-test`, `policy-boundary-guards`, and the focused policy-profile workflows;
- explicit input, decision vocabulary/semantics, evaluation binding, obligation, reviewer-role, and enforcement-maturity contract/schema/validator slices;
- the `packages/policy-runtime` placeholder boundary.

Not established:

- branch-protection or ruleset-required check configuration;
- accepted policy steward and independent approver identities;
- repository-wide bundle manifest, selector, signing, or active evaluator;
- functional policy-runtime imports or production consumers;
- authenticated decision emission, persistence, receipts, replay, expiry, correction propagation, or cache invalidation;
- promotion-gate integration, deployment enforcement, release authorization, or public runtime behavior.

[Back to top](#top)

---

## Current maturity

| Level | Evidence required | Root-wide posture |
|---|---|---:|
| M0 — Placeholder | stub README or default-only module | **CONFIRMED in several lanes and in `policy-runtime`** |
| M1 — Boundary documented | responsibility, inputs, outputs, failures, authority split | **CONFIRMED broadly** |
| M2 — Rule or profile candidate | reviewed source, contracts/schemas, synthetic fixtures, stable validator or entrypoint | **CONFIRMED in multiple inactive profiles** |
| M3 — Evaluator-backed proof | accepted evaluator/bundle, native tests, input assembly, normalization, deterministic CI | **PARTIAL only for one bounded Rego profile; general M3 not established** |
| M4 — Governed consumer and replay | consumer, authenticated decisions, receipts, replay, expiry, correction, cache invalidation | **NOT ESTABLISHED** |
| M5 — Release-significant enforcement | required checks, independent review, deployment evidence, promotion/rollback drill | **UNKNOWN / NOT ESTABLISHED** |

The fixture-only [`PolicyEnforcementMaturity`](../contracts/policy/policy_enforcement_maturity.md) profile uses a separate ordered vocabulary—`DESIGNED`, `FIXTURE_TESTED`, `MERGE_BLOCKING`, `PROMOTION_BLOCKING`, `RUNTIME_ENFORCED`. Do not infer a later stage from a workflow file or green run alone. State maturity per lane, exact revision, and evidence chain; a root with several M2 profiles is not an M2 production system.

[Back to top](#top)

---

## Outcome vocabularies

| Axis | Examples | Meaning |
|---|---|---|
| Canonical outward `PolicyDecision.outcome` | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` | Closed four-value candidate schema. |
| Pass 12 engine-native result | `allow: true|false`, `deny_reasons[]` | Bounded Rego profile result; deliberately not normalized into `PolicyDecision`. |
| Other engine-native terms | `ALLOW`, `RESTRICT`, `HOLD`, `DENY`, sometimes `ABSTAIN`/`ERROR` | Lower-level semantics requiring explicit accepted normalization. |
| Validation | `PASS`, `FAIL`, `DENY`, `ERROR`, validator codes | Check result; never policy permission or release state. |
| Workflow readiness | `WORKFLOW_HOLD`, `WORKFLOW_SKIPPED_EXPLICIT` | CI statement that prerequisites are intentionally absent. |
| Lifecycle/release | candidate, held, released, withdrawn, superseded | State-transition vocabulary owned elsewhere. |
| Truth labels | `CONFIRMED`, `PROPOSED`, `UNKNOWN`, `NEEDS VERIFICATION` | Evidence posture; not policy decisions. |

Do not emit native values into a closed outward schema, map abstention to denial, map evaluator failure to denial, or interpret validator pass as release approval. Preserve reasons, obligations, bundle/evaluator identity, exact input digest, and review/release references. If no accepted mapping exists, hold or error rather than invent a value.

[Back to top](#top)

---

## Policy authoring contract

Every material rule should identify:

- stable package, entrypoint, and version;
- explicit input profile and no-hidden-fetch posture;
- fail-closed defaults;
- native and outward outcomes plus accepted normalization;
- public-safe reasons and enforceable obligations;
- evidence, rights, consent, sensitivity, source-role, lifecycle, review, and release dependencies;
- pinned bundle, evaluator, and source identities;
- synthetic fixtures and positive/negative native tests;
- deterministic validator and hosted workflow;
- receipt metadata and replay requirements;
- effective time, supersession, correction, cache invalidation, and rollback.

A new module is not operationally admissible until path, package identity, evaluator version, inputs, default behavior, outcomes, reasons, obligations, tests, bundle membership, consumer, receipts, and rollback are reviewable. Fixture-first profiles must remain visibly inactive until an accepted integration closes those dependencies.

[Back to top](#top)

---

## Rights, sensitivity, consent, and public exposure

When source rights, consent, living-person or genomic data, archaeology/cultural sovereignty, rare species, critical infrastructure, harmful precision, parcel-person joins, or source-role evidence are unresolved, prefer `DENY`, `HOLD`, `ABSTAIN`, redaction, generalization, aggregation, delay, staged access, or steward review.

Client-side hiding is not a security control. Join-induced sensitivity must propagate. Rules and fixtures must not copy real protected payloads into source, tests, logs, reasons, receipts, or documentation. Public-safe reason codes must not reveal the hidden fact they are protecting.

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
11. A bounded fixture profile is not production policy merely because its dedicated CI passes.
12. Promotion, release, correction, withdrawal, and rollback remain separate governed transitions.

[Back to top](#top)

---

## Correction and rollback

Material policy changes should be versioned, preserve prior source/bundle/evaluator/test identities for replay, record supersession and effective time, reevaluate affected decisions and releases, invalidate caches, emit correction or withdrawal records through owning roots, and restore a prior accepted bundle/selector during rollback rather than copying files into an ambiguous state.

This v0.3 README changes no policy behavior. Before merge, close or abandon its draft PR and branch. After merge, revert the README commit and paired generated receipt together, or issue a transparent forward fix. The v0.2 baseline is blob `fa9378a6a699d0985fd018dbdb9f27c15efcb1c3`.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status |
|---|---|---:|
| POL-001 | Is ADR-0003 still proposed in the governing ADR index? | **CONFIRMED proposed at this snapshot** |
| POL-002 | What is the complete recursive policy inventory and per-lane maturity classification? | **PARTIAL — paths inventoried; semantic maturity still needs review** |
| POL-003 | Which repository-wide evaluator, bundle format, manifest, selector, and activation contract are accepted? | **UNKNOWN** |
| POL-004 | Does the bounded Pass 12 native-test pattern become the general Rego test convention? | **NEEDS DECISION** |
| POL-005 | Will explicit `PolicyInputBundle` profile v1 replace, extend, or remain beside the permissive parent shape? | **NEEDS VERIFICATION / MIGRATION DECISION** |
| POL-006 | What accepted mapping joins native engine results to `ANSWER/ABSTAIN/DENY/ERROR`? | **INACTIVE CANDIDATES EXIST; ACTIVE BINDING UNKNOWN** |
| POL-007 | Which reason, obligation, and reviewer-role registries are adopted, versioned, and enforced by consumers? | **PROPOSED_INACTIVE / UNKNOWN ENFORCEMENT** |
| POL-008 | Which governed consumer is the first accepted end-to-end policy slice? | **UNKNOWN** |
| POL-009 | What decision-receipt schema, persistence, authentication, and replay contract are accepted? | **UNKNOWN** |
| POL-010 | Which policy checks are required by repository rules, and how is independent approval enforced? | **UNKNOWN / NEEDS VERIFICATION** |
| POL-011 | How does the Pass 12 native result bind into `PolicyDecision`, PromotionDecision, ReleaseManifest, correction, and rollback? | **NEEDS IMPLEMENTATION** |
| POL-012 | What rollback drill proves prior-bundle restoration and stale-decision invalidation? | **UNKNOWN** |
| POL-013 | How should `source/` versus `sources/` and `test/` versus `tests/` converge without creating parallel authority or losing references? | **DRIFT / NEEDS DIRECTORY REVIEW** |
| POL-014 | What are the intended writer, reader, retention, and graduation rules for placeholder lanes such as `opa/`, `proof/`, and `transport/`? | **NEEDS VERIFICATION** |
| POL-015 | What process updates the OPA version and checksum while preserving reproducibility and supply-chain review? | **NEEDS VERIFICATION** |

[Back to top](#top)

---

## No-loss and evidence ledger

| Baseline element | Disposition in v0.3 |
|---|---|
| Stable path, document ID, and H1 | Preserved |
| Policy-as-code plus documentation purpose | Preserved and bounded |
| Allow/deny/restrict/abstain/redaction/release/promotion/sensitivity scope | Preserved; native and outward vocabularies clarified |
| Singular policy root | Preserved; placement authority updated to accepted ADR-0029 |
| OPA/Rego, bundles, fixtures, runtime, promotion, sensitivity, rights, release, and UI policy | Preserved and reconciled to current implementation evidence |
| Schema/source/application exclusions | Preserved and expanded |
| Inputs, outputs, validation, review, related folders, status | Preserved and refreshed |
| Maturity, authoring, sensitivity, trust membrane, rollback, open verification | Preserved and updated |
| Direct-child navigation | Added as a complete root-only inventory |
| Prior uncertainty about all Rego tests/validators being absent | Repaired: one bounded native lane and multiple candidate validators now exist |
| Prior general evaluator, runtime, consumer, receipt, release, and publication holds | Preserved |

Evidence used includes the v0.2 blob `fa9378a6a699d0985fd018dbdb9f27c15efcb1c3`, accepted ADR-0029, current Directory Rules v2 bytes, ADR-0003, the recursive `policy/` tree, Pass 12 Rego source/tests/fixtures/workflow, `policy-test`, `policy-boundary-guards`, focused policy contract/schema/validator workflows, and the policy-runtime placeholder.

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| short stub | Before 2026-07-23 | Declared purpose, singular root, basic belongs/exclusions, validation/review/related pointers, and `PROPOSED` status | Historical blob recorded in v0.2 |
| v0.2 | 2026-07-23 | Same-path repository-grounded modernization with required README order, authority split, maturity evidence, workflow boundaries, outcome separation, authoring rules, sensitive/public controls, rollback, and verification register | Restore blob `fa9378a6a699d0985fd018dbdb9f27c15efcb1c3` only if paired v0.3 receipt is also removed |
| v0.3 | 2026-08-09 | Repins the root contract to current main; records ADR-0029 adoption, bounded OPA/Rego execution, inactive fixture-first policy profiles, 18 boundary tests, full direct-child inventory, preserved general readiness holds, and updated validation/rollback/open-work boundaries | Revert the v0.3 README and paired generated receipt together |

<p align="right"><a href="#top">Back to top</a></p>
