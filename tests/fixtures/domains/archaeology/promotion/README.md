<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-promotion-readme
title: Archaeology Promotion Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-promotion-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Archaeology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Promotion steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; archaeology; promotion-fixtures; synthetic-only; no-network; deny-by-default; review-gated; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, promotion-fixtures, PromotionDecision, PromotionReceipt, ReleaseManifest, RollbackCard, RedactionReceipt, PolicyDecision, ReviewRecord, EvidenceBundle, EvidenceRef, MapReleaseManifest, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../api/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../../../contracts/domains/archaeology/
  - ../../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
  - ../../../../../release/manifests/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/promotion/README.md."
  - "This lane documents test-local expectations for archaeology promotion-shaped fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Promotion-shaped fixtures are not PromotionDecision authority, ReleaseManifest authority, release approval, publication approval, or public artifact storage."
  - "Executable tests, promotion fixture payload inventory, schema bindings, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology promotion test fixtures

> Test-lane documentation for Archaeology promotion-shaped fixtures referenced from `tests/fixtures/domains/archaeology/promotion/`. This path describes safe synthetic PromotionDecision, PromotionReceipt, ReleaseManifest, review, policy, receipt, correction, and rollback expectations without turning those examples into release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: promotion test fixtures" src="https://img.shields.io/badge/lane-promotion__test__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not promotion" src="https://img.shields.io/badge/boundary-fixtures__not__promotion-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/promotion/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology promotion test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/promotion`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/fixtures/domains/archaeology/README.md` was not found during authoring; CONFIRMED sibling `api/README.md` exists as a test-local API fixture lane; CONFIRMED canonical Archaeology fixture README exists under `fixtures/domains/archaeology/`; CONFIRMED archaeology publication/policy docs describe EvidenceBundle, PolicyDecision, ReviewRecord, PromotionDecision, PromotionReceipt, ReleaseManifest, RollbackCard, governed API, correction, rollback, and AI-surface posture; NEEDS VERIFICATION for executable promotion-fixture tests, fixture payload inventory, accepted schemas, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/promotion/` is a test-local documentation lane for Archaeology promotion-shaped fixture expectations.

This lane should describe how tests may use synthetic promotion, release-gate, review, policy, receipt, correction, withdrawal, and rollback examples. It may cover PromotionDecision fixtures, PromotionReceipt fixtures, ReleaseManifest-shaped fixtures, MapReleaseManifest-shaped fixtures, RedactionReceipt refs, PolicyDecision refs, ReviewRecord refs, rights-holder review refs, correction refs, withdrawal refs, rollback refs, and public-surface invalidation expectations.

A passing fixture check here should not mean that an archaeology claim is true, a candidate is confirmed, a protected detail is releasable, a promotion was approved, a release manifest was issued, a public layer is published, a reviewer approved release, or an AI answer is authoritative. It should mean only that a bounded synthetic promotion-shaped fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped and subordinate to release, policy, evidence, receipt, and fixture authority roots.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Promotion-shaped fixture-test expectations | `tests/fixtures/domains/archaeology/promotion/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Reusable archaeology fixtures | `fixtures/domains/archaeology/` | Canonical fixture root; referenced, not replaced. |
| Archaeology domain tests | `tests/domains/archaeology/` | Consumers and validators; not fixture authority. |
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Confirmed test fixture parent lane. |
| API-shaped fixture tests | `tests/fixtures/domains/archaeology/api/` | Confirmed sibling lane. |
| Semantic contracts | `contracts/domains/archaeology/` or ADR-selected equivalent | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/` or ADR-selected equivalent | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release and promotion decisions | `release/` roots | Referenced through synthetic refs; not decided here. |
| Public API, map, and artifact implementation | App, API, map, tile, and artifact roots | Exercised only through safe synthetic envelopes. |

> [!IMPORTANT]
> Do not use this directory as a promotion queue, release-candidate store, release manifest store, review record store, policy decision store, receipt store, or public artifact home. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Promotion fixtures are synthetic gate examples, not promotion authority.** Test fixture success proves only that a promotion-shaped envelope has the expected bounded test behavior.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixture envelopes use fake IDs, mock markers, generalized geometry, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, policy services, release services, map services, public APIs, or AI runtimes. | `ERROR`. |
| Promotion boundary | Promotion-shaped fixtures do not approve promotion, create a PromotionDecision, or authorize a ReleaseManifest. | promotion block. |
| Evidence boundary | Promotion-like fixtures cite synthetic EvidenceRef and EvidenceBundle-stub expectations or abstain. | `ABSTAIN`. |
| Policy boundary | PolicyDecision refs are required for allow-like outcomes and denial/abstention examples fail closed. | `DENY` / `ABSTAIN`. |
| Review boundary | ReviewRecord and rights-holder review refs are explicit where materiality requires them. | `DENY` / `ABSTAIN`. |
| Redaction boundary | Public-safe transforms cite RedactionReceipt refs and never embed restricted payloads. | validation failure / `DENY`. |
| Release boundary | ReleaseManifest-shaped fixtures are examples only and cannot activate public carriers. | promotion block. |
| Rollback boundary | RollbackCard refs remain explicit and auditable; rollback is not deletion or silent edit. | validation failure. |
| AI boundary | Focus Mode or answer-like fixtures cite released evidence or abstain. | `ABSTAIN` / `DENY`. |

---

## Expected Promotion Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| PromotionDecision-shaped fixtures | Verify promotion decision fields, finite outcomes, gate refs, and reason codes. | Fixture is not a real PromotionDecision. |
| PromotionReceipt-shaped fixtures | Verify promotion action receipts carry synthetic run, actor, input, output, and reason refs. | Receipt-shaped fixture is not receipt authority. |
| ReleaseManifest-shaped fixtures | Verify release-shaped examples require evidence, policy, review, artifact hash, correction, and rollback refs. | Manifest-shaped fixture is not publication. |
| Review-gate fixtures | Verify reviewer and rights-holder refs are present where policy requires them. | Review refs are synthetic. |
| Redaction receipt fixtures | Verify public-safe transforms include receipt refs and do not embed restricted payloads. | Receipt refs do not release detail. |
| Policy-deny fixtures | Verify unsupported, uncertain, or protected promotion attempts fail closed. | Denial examples do not store real restricted data. |
| Correction and withdrawal fixtures | Verify supersession and withdrawal refs invalidate dependent carriers. | No silent edit. |
| Rollback fixtures | Verify rollback refs point to synthetic prior safe state and preserve audit posture. | Rollback fixture is not rollback approval. |
| No-network fixtures | Verify local deterministic loading and no live service calls. | Integration tests require separate gates. |

---

## Relationship to Canonical Archaeology Fixtures

The canonical Archaeology fixture root already documents synthetic child lanes for golden, invalid, site-shaped, candidate-shaped, publication-transform, steward-review, and valid examples. This `tests/fixtures/.../promotion/` lane should avoid duplicating those payloads.

| Question | Preferred answer |
|---|---|
| Need a reusable archaeology fixture payload? | Put it under `fixtures/domains/archaeology/`. |
| Need a test-only promotion wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need a real promotion decision, release manifest, or rollback card? | Do not put it here. Use release roots. |
| Need policy, schema, or contract authority? | Do not put it here. Use policy, schema, or contract roots. |
| Need a public artifact or API response? | Do not put it here. Use governed release and public-surface roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local promotion fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic PromotionDecision, PromotionReceipt, ReleaseManifest, MapReleaseManifest, CorrectionNotice, WithdrawalNotice, RollbackCard, PolicyDecision, ReviewRecord, RedactionReceipt, ValidationReport, and EvidenceBundle-stub refs
- synthetic release-gate examples for allow-like, deny, abstain, correction, withdrawal, rollback, and stale-state behavior
- synthetic public-surface invalidation envelopes for API, map, layer, Focus Mode, export, and generated-answer carriers
- canary values that make trust-membrane bypass, candidate-confirmed collapse, protected-detail exposure, review-approval leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, promotion case, source role, sensitivity posture, evidence ref, redaction receipt ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from pre-public lifecycle stores, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Precise protected locations, private reviewer notes, real consultation records, collection-security details, or restricted cultural context | Sensitive material requires governed policy, review, redaction, and release controls. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, API implementation, map implementation, pipeline implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/archaeology/promotion/
|-- README.md
|-- manifest_expectations.json
|-- test_promotion_fixture_manifest_shape.py
|-- test_promotion_fixture_no_network.py
|-- test_promotion_decision_fixture_finite_outcomes.py
|-- test_promotion_requires_evidence_policy_review_refs.py
|-- test_redaction_receipt_ref_required_for_public_safe_transform.py
|-- test_release_manifest_fixture_does_not_authorize_publication.py
|-- test_correction_withdrawal_rollback_refs.py
`-- test_focus_mode_fixture_abstains_without_release.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/promotion
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no protected location detail, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Promotion Fixture Manifest

Synthetic test-local manifests should describe promotion fixture expectations without carrying real archaeology data or release authority.

```json
{
  "fixture_manifest_id": "archaeology-promotion-test-fixture-manifest-example",
  "domain": "archaeology",
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_publication_transform_receipt/example-fixture.json",
  "fixture_family": "promotion_gate_decision_envelope",
  "promotion_case": "public_safe_transform_candidate",
  "source_role": "candidate",
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-promotion-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-promotion-001",
  "policy_decision_ref": "policy-decision-fixture-arch-promotion-001",
  "review_record_ref": "review-record-fixture-arch-promotion-001",
  "promotion_decision_ref": null,
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-arch-promotion-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "PROMOTION_FIXTURE_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "PROMOTION_APPROVAL_CANARY",
    "CONFIRMED_SITE_CANARY",
    "PROTECTED_LOCATION_CANARY",
    "REVIEW_APPROVAL_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; release, policy, evidence, and receipt authority remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `tests/fixtures/domains/archaeology/api/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local API fixture posture and notes missing immediate parent index. | Does not prove promotion-fixture tests exist. |
| `tests/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines Archaeology domain tests and separates tests from fixture, schema, policy, lifecycle, release, and public-client authority. | Does not prove executable promotion-fixture tests. |
| `tests/domains/archaeology/fixtures/README.md` | CONFIRMED repo evidence | Defines fixture-test parent lane and confirms canonical fixtures belong outside tests. | Parent is under `tests/domains/`, not `tests/fixtures/`. |
| `docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED repo evidence | Defines placement posture, sensitive-lane path guidance, lifecycle invariant, exact-location denial, and release path separation. | Specific paths in that doc are marked PROPOSED until verified. |
| `docs/domains/archaeology/SENSITIVITY.md` | CONFIRMED repo evidence | Defines deny-by-default sensitivity posture, redaction, review, receipt, AI, and UI discipline. | Machine-readable enforcement remains in schemas, policy, release, and CI. |
| `docs/domains/archaeology/PUBLICATION_AND_POLICY.md` | CONFIRMED repo evidence | Describes EvidenceBundle, PolicyDecision, ReviewRecord, PromotionDecision, PromotionReceipt, ReleaseManifest, RollbackCard, governed API, correction, rollback, and AI surface posture. | Route names and implementation details remain PROPOSED where not verified. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/promotion/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when promotion fixture wrappers may live here instead of `fixtures/domains/archaeology/`.
- [ ] Confirm promotion fixture manifest schema, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for promotion manifest shape, no-network fixture loading, finite outcomes, evidence refs, policy refs, review refs, redaction receipt refs, release refs, correction refs, withdrawal refs, and rollback refs.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real source data, production promotion payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats a promotion-shaped fixture pass as source truth, candidate confirmation, policy approval, review approval, promotion approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, sensitivity handling, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)