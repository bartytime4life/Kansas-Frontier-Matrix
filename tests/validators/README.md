<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION
title: validators
type: standard
version: v1
status: draft
owners: @bartytime4life
created: YYYY-MM-DD
updated: 2026-04-13
policy_label: public
related: [../README.md, ../../.github/README.md, ../../.github/CODEOWNERS, ../../.github/workflows/README.md, ../../tools/ci/README.md, ../../tools/attest/README.md, ../../tools/validators/promotion_gate/README.md, ../../contracts/README.md, ../../schemas/README.md, ../../schemas/promotion/decision-envelope.schema.json, ../../schemas/promotion/promotion-record.schema.json, ../../schemas/promotion/promotion-prov.schema.json, ../../schemas/promotion/promotion-bundle.schema.json, ../../schemas/promotion/promotion-bundle-diff-policy.schema.json, ../../policy/README.md, ../../policy/promotion_bundle_diff_policy.json, ../fixtures/promotion/, ../e2e/runtime_proof/README.md, ./test_promotion_gate_e2e.py, ./test_bundle_diff_policy.py, ./test_validate_bundle_diff_policy.py, ../ci/test_render_promotion_review_handoff.py]
tags: [kfm, tests, validators, promotion, verification, fail-closed, diff-policy, review-handoff]
notes: [Updated as a child tests-lane README from adjacent repo documentation and KFM doctrine to reflect the fuller promotion-gate thin slice: bundle diff, checked-in diff-policy evaluation, policy schema validation, and downstream review handoff artifacts. Direct branch inventory for tests/validators/ still remains bounded where not re-enumerated from a mounted checkout.]
[/KFM_META_BLOCK_V2] -->

# validators

Validator- and gate-focused proof surface for KFM promotion decisions, derived trust objects, and adjacent fail-closed machine checks.

> [!IMPORTANT]
> **Status:** experimental  
> **Owners:** `@bartytime4life`  
> **Path:** `tests/validators/README.md`  
> **Repo fit:** child lane of `tests/`; primary current subject is `tools/validators/promotion_gate/`; renderer handoff belongs in `tools/ci/` and renderer proof belongs in `tests/ci/`; attestation support belongs in `tools/attest/`; canonical law remains upstream in `contracts/`, `schemas/`, and `policy/`  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Current evidence snapshot](#current-evidence-snapshot) · [Directory tree](#directory-tree) · [Quickstart](#quickstart) · [Usage](#usage) · [Validator proof contract](#validator-proof-contract) · [Diagram](#diagram) · [Coverage matrix](#coverage-matrix) · [Definition of done](#definition-of-done) · [FAQ](#faq) · [Appendix](#appendix)

![status](https://img.shields.io/badge/status-experimental-orange)
![owners](https://img.shields.io/badge/owners-%40bartytime4life-1f6feb)
![path](https://img.shields.io/badge/path-tests%2Fvalidators%2FREADME.md-0b7285)
![lane](https://img.shields.io/badge/lane-validator%20proof-6f42c1)
![posture](https://img.shields.io/badge/posture-fail--closed-critical)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20%7C%20INFERRED%20%7C%20PROPOSED-2ea043)

> [!WARNING]
> Recent adjacent documentation repeatedly references `tests/validators/test_promotion_gate_e2e.py`, `test_bundle_diff_policy.py`, and `test_validate_bundle_diff_policy.py`, but the directly surfaced top-level public-tree snapshot available in this review pass did not independently enumerate `tests/validators/`. This README therefore documents the lane conservatively and keeps broader inventory claims visibly bounded.

> [!NOTE]
> `tests/validators/` is not a generic bucket for “harder tests.”  
> In KFM, this lane should prove that validators, gated decisions, derived trust objects, checked-in policy interpretations, and downstream renderer handoff inputs behave **deterministically**, **fail closed**, and remain **review-visible** without silently publishing anything.

---

## Scope

`tests/validators/` is the proof lane for validator-oriented behavior inside the broader `tests/` surface.

Use this lane when the subject under test is a validator or governed gate that must prove:

- finite machine outcomes
- schema-valid emitted objects
- explicit failure semantics
- stable negative-path behavior
- reviewer handoff artifacts that remain subordinate to upstream truth
- checked-in policy evaluation over already-produced machine artifacts
- schema validation of checked-in policy files that influence governed review
- downstream renderer handoff compatibility without re-owning renderer contracts

This lane is especially natural for the current promotion thin slice because the adjacent subject docs already describe a validator chain that moves from candidate preparation to a `DecisionEnvelope`, then onward to reviewer summaries and derived trust objects, then onward again to prior/current bundle comparison and diff-policy classification, and now onward further to a composed promotion review handoff document.

This lane is **not** the right home for:

- helper-rendering behavior owned by [`../../tools/ci/README.md`](../../tools/ci/README.md)
- renderer-proof assertions owned by [`../ci/README.md`](../ci/README.md)
- contract-example and valid/invalid fixture authority owned by contract/schema surfaces
- broad request-time runtime proof packs better placed under `../e2e/`
- policy source files or release logic that should remain visible in their own governed homes

### Truth labels used in this README

| Label | Meaning here |
| --- | --- |
| **CONFIRMED** | Directly supported by surfaced repo-facing documentation or stable KFM doctrine in this session |
| **INFERRED** | Strongly suggested by adjacent docs, but not freshly re-proven as checked-out lane inventory |
| **PROPOSED** | Recommended lane shape or future coverage pattern consistent with current doctrine |
| **UNKNOWN** | Not surfaced strongly enough to describe as current repo fact |
| **NEEDS VERIFICATION** | Path, command, or implementation detail that should be rechecked against the working branch before merge |

[Back to top](#validators)

---

## Repo fit

**Path:** `tests/validators/README.md`  
**Role:** directory README for validator- and gate-focused proof surfaces inside the governed `tests/` boundary.

| Direction | Surface | Why it matters |
| --- | --- | --- |
| Parent | [`../README.md`](../README.md) | `tests/` is the governed proof surface; this lane stays subordinate to that contract |
| Governance | [`../../.github/README.md`](../../.github/README.md) | caller and review-routing boundary |
| Ownership | [`../../.github/CODEOWNERS`](../../.github/CODEOWNERS) | confirms current owner coverage for `/tests/` |
| Workflow boundary | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | orchestration belongs there, not in test prose |
| Primary subject lane | [`../../tools/validators/promotion_gate/README.md`](../../tools/validators/promotion_gate/README.md) | current documented thin slice for validator behavior |
| Renderer handoff | [`../../tools/ci/README.md`](../../tools/ci/README.md) | summaries and composed review handoff are rendered there; this lane proves validator behavior instead |
| Renderer proof neighbor | [`../ci/README.md`](../ci/README.md) | keeps review-handoff rendering proof separate from validator proof |
| Attestation neighbor | [`../../tools/attest/README.md`](../../tools/attest/README.md) | attestation state may be consumed here, but signing/verification logic lives elsewhere |
| Canonical law | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md) | tests may validate against these surfaces, but must not quietly replace them |
| Promotion schemas | [`../../schemas/promotion/decision-envelope.schema.json`](../../schemas/promotion/decision-envelope.schema.json), [`../../schemas/promotion/promotion-record.schema.json`](../../schemas/promotion/promotion-record.schema.json), [`../../schemas/promotion/promotion-prov.schema.json`](../../schemas/promotion/promotion-prov.schema.json), [`../../schemas/promotion/promotion-bundle.schema.json`](../../schemas/promotion/promotion-bundle.schema.json) | current promotion thin slice emits trust objects validated against these schemas |
| Diff-policy schema | [`../../schemas/promotion/promotion-bundle-diff-policy.schema.json`](../../schemas/promotion/promotion-bundle-diff-policy.schema.json) | validator proof now includes schema validation of the checked-in bundle diff-policy file |
| Checked-in diff-policy | [`../../policy/promotion_bundle_diff_policy.json`](../../policy/promotion_bundle_diff_policy.json) | bundle drift interpretation now flows through a checked-in policy data surface rather than Python constants only |
| Shared fixtures | [`../fixtures/promotion/`](../fixtures/promotion/) | the current promotion slice already points to shared candidate fixtures there |
| Adjacent e2e lane | [`../e2e/runtime_proof/README.md`](../e2e/runtime_proof/README.md) | keeps request-time runtime proof distinct from validator-lane proof |

### Working rule

Reach for `tests/validators/` when the change needs to prove **machine-checkable gate behavior**.

Do **not** reach for it when the change is really about:

- helper rendering only
- renderer Markdown assertions
- schema authority
- policy ownership
- runtime API behavior
- publication itself
- one-off shell orchestration

---

## Accepted inputs

Content that belongs here should remain **test-facing**, **repeatable**, and **safe to review**.

### Typical accepted inputs

- validator-ready candidate fixtures
- shared promotion fixtures from `../fixtures/promotion/`
- declared schemas for emitted objects
- read-only policy inputs or compiled gate expectations
- checked-in policy data used by a validator/evaluator
- machine outputs such as `decision.json`, promotion records, PROV docs, bundle manifests, diff reports, and diff-policy reports
- downstream renderer handoff inputs used only to prove compatibility, not to re-own rendering assertions
- deterministic negative-path fixtures that isolate one failure reason cleanly

### Accepted input profile

| Input family | Typical examples | Keep it here when |
| --- | --- | --- |
| Candidate fixtures | `tests/fixtures/promotion/*.json` | the test needs a stable, reviewable candidate |
| Schema surfaces | `schemas/promotion/*.json` | the test proves emitted-object conformance |
| Policy schema surfaces | `schemas/promotion/promotion-bundle-diff-policy.schema.json` | the test proves checked-in policy files validate before use |
| Checked-in policy data | `policy/promotion_bundle_diff_policy.json` | the test proves interpretation data is reviewable and machine-valid |
| Validator outputs | `decision.json`, `promotion-record.json`, `promotion-prov.json`, `promotion-bundle.json` | the test asserts emitted shape and fail-closed semantics |
| Diff outputs | `promotion-bundle-diff.json` | the test proves prior/current change visibility feeds governed review correctly |
| Diff-policy outputs | `promotion-bundle-diff-policy.json` | the test proves changed-key classification remains finite and review-visible |
| Handoff-compatible outputs | `promotion-review-handoff.md` as a downstream expected artifact reference | the test proves validator outputs remain stable enough for downstream rendering, without asserting renderer formatting here |
| Policy-facing inputs | declared labels, rights fields, gate fixtures | the test checks visible outcomes, not policy authorship |
| Reviewer-facing outputs | Markdown summaries or handoff refs | the test proves downstream compatibility without re-owning renderer logic |
| Trust-chain refs | attestation refs, prior release refs, rollback anchors | the test preserves visibility of trust-bearing state without becoming the attestation lane |

---

## Exclusions

| Does **not** belong here | Put it here instead | Why |
| --- | --- | --- |
| Validator implementation code | [`../../tools/validators/promotion_gate/README.md`](../../tools/validators/promotion_gate/README.md) and the helper path itself | `tests/validators/` proves behavior; it does not become the implementation lane |
| CI summary rendering rules | [`../ci/README.md`](../ci/README.md) and [`../../tools/ci/README.md`](../../tools/ci/README.md) | rendering is adjacent, not primary, here |
| Workflow sequencing, permissions, or branch rules | [`../../.github/workflows/README.md`](../../.github/workflows/README.md) | orchestration belongs at the gatehouse boundary |
| Canonical policy decisions | [`../../policy/README.md`](../../policy/README.md) | tests may assert decision output, but policy remains the source of truth |
| Authoritative schemas or contract meaning | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md) | this lane validates chosen authority; it does not silently redefine it |
| Broad runtime-proof scenarios | [`../e2e/`](../e2e/) | keep this lane validator-focused |
| Unpublished or
