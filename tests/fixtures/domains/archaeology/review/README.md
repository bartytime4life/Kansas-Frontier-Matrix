<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-review-readme
title: Archaeology Review Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-review-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Archaeology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Review steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; archaeology; review-fixtures; synthetic-only; no-network; deny-by-default; review-gated; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, review-fixtures, StewardReview, CulturalReview, ReviewRecord, PolicyDecision, EvidenceBundle, EvidenceRef, RedactionReceipt, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../../contracts/domains/archaeology/cultural_review.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../../../schemas/contracts/v1/domains/archaeology/steward_review.schema.json
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/review/README.md."
  - "This lane documents test-local expectations for archaeology review-shaped fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Review-shaped fixtures are not ReviewRecord authority, StewardReview authority, CulturalReview authority, consultation records, policy approval, release approval, or publication approval."
  - "Executable tests, review fixture payload inventory, schema bindings, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology review test fixtures

> Test-lane documentation for Archaeology review-shaped fixtures referenced from `tests/fixtures/domains/archaeology/review/`. This path describes safe synthetic StewardReview, CulturalReview-adjacent, ReviewRecord, policy, evidence, correction, and rollback expectations without turning examples into review approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: review test fixtures" src="https://img.shields.io/badge/lane-review__test__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not review approval" src="https://img.shields.io/badge/boundary-fixtures__not__review__approval-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/review/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology review test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/review`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/fixtures/domains/archaeology/README.md` was not found during authoring; CONFIRMED sibling `api/README.md` and `promotion/README.md` exist as test-local fixture lanes; CONFIRMED canonical `fixtures/domains/archaeology/synthetic_steward_review/README.md` exists and says examples are synthetic and not authoritative project records; CONFIRMED `contracts/domains/archaeology/steward_review.md` defines StewardReview as review posture without becoming evidence, policy approval, cultural review, or release approval by itself; NEEDS VERIFICATION for executable review-fixture tests, fixture payload inventory, accepted schemas, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/review/` is a test-local documentation lane for Archaeology review-shaped fixture expectations.

This lane should describe how tests may use synthetic review examples for StewardReview, CulturalReview-adjacent routing, ReviewRecord refs, reviewer-role presence, evidence review posture, policy recommendation posture, sensitivity escalation posture, correction review, withdrawal review, rollback review, and release-readiness review.

A passing fixture check here should not mean that an archaeology claim is true, a candidate is confirmed, a steward approved a claim, cultural review occurred, consultation happened, policy allows release, a release manifest is valid, a public layer is published, or an AI answer is authoritative. It should mean only that a bounded synthetic review-shaped fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped and subordinate to fixture, review, policy, evidence, receipt, and release authority roots.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Review-shaped fixture-test expectations | `tests/fixtures/domains/archaeology/review/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Reusable review-shaped fixtures | `fixtures/domains/archaeology/synthetic_steward_review/` | Canonical fixture lane; referenced, not replaced. |
| Reusable archaeology fixtures | `fixtures/domains/archaeology/` | Canonical fixture root; referenced, not replaced. |
| Archaeology domain tests | `tests/domains/archaeology/` | Consumers and validators; not fixture authority. |
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Confirmed test fixture parent lane. |
| API and promotion fixture tests | `tests/fixtures/domains/archaeology/api/`, `tests/fixtures/domains/archaeology/promotion/` | Confirmed sibling lanes. |
| Review semantic contracts | `contracts/domains/archaeology/steward_review.md`, `contracts/domains/archaeology/cultural_review.md` | Define object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/` or ADR-selected equivalent | Define accepted shape; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release and promotion decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a review queue, reviewer note store, consultation archive, policy decision store, release approval store, receipt store, or public artifact home. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Review fixtures are synthetic review-posture examples, not review approval.** Test fixture success proves only that a review-shaped envelope has the expected bounded test behavior.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixture envelopes use fake IDs, mock markers, generalized descriptions, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, review systems, policy services, release services, map services, public APIs, or AI runtimes. | `ERROR`. |
| Steward-review boundary | StewardReview-shaped fixtures record review posture only and do not become evidence proof, PolicyDecision, CulturalReview, or release approval. | `DENY` / `ABSTAIN`. |
| Cultural-review boundary | CulturalReview-adjacent fixtures must not imply cultural review, consultation, consent, or rights-holder approval unless a synthetic explicit ref is present. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Review-like fixtures cite synthetic EvidenceRef and EvidenceBundle-stub expectations or abstain. | `ABSTAIN`. |
| Policy boundary | PolicyDecision refs are required for allow-like outcomes and denial/abstention examples fail closed. | `DENY` / `ABSTAIN`. |
| Redaction boundary | Public-safe review summaries cite RedactionReceipt refs and never embed restricted payloads. | validation failure / `DENY`. |
| Release boundary | Review fixture success does not become release approval, publication approval, correction approval, or rollback approval. | promotion block. |
| AI boundary | Focus Mode or answer-like review summaries cite released evidence or abstain. | `ABSTAIN` / `DENY`. |

---

## Expected Review Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| StewardReview-shaped fixtures | Verify review posture fields, reviewed object refs, reviewer-role refs, finite outcomes, and reason codes. | Fixture is not a real StewardReview. |
| CulturalReview-adjacent fixtures | Verify cultural-review routing is explicit and cannot be implied by generic steward review. | Cultural review is not inferred. |
| Evidence review fixtures | Verify evidence refs, unresolved-evidence abstention, and review-routing examples. | Review does not become proof. |
| Policy recommendation fixtures | Verify review recommendation does not replace PolicyDecision. | Recommendation is not policy. |
| Redaction review fixtures | Verify public-safe summaries require redaction receipt refs. | Summary is not release. |
| Correction and withdrawal review fixtures | Verify supersession and withdrawal refs remain auditable. | No silent edit. |
| Rollback review fixtures | Verify rollback review refs remain explicit and separate from rollback approval. | Rollback fixture is not rollback authority. |
| API and Focus Mode review fixtures | Verify public-facing review summaries abstain when release or evidence state is missing. | Public carrier is release-gated. |
| No-network fixtures | Verify local deterministic loading and no live service calls. | Integration tests require separate gates. |

---

## Relationship to Canonical Archaeology Fixtures

The canonical Archaeology fixture root already documents a `synthetic_steward_review/` child lane for small synthetic review-shaped examples. This `tests/fixtures/.../review/` lane should avoid duplicating those payloads.

| Question | Preferred answer |
|---|---|
| Need a reusable review-shaped fixture payload? | Put it under `fixtures/domains/archaeology/synthetic_steward_review/`. |
| Need a test-only review wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need a real ReviewRecord, CulturalReview, consultation note, or rights-holder approval? | Do not put it here. Use governed review, policy, evidence, or release roots. |
| Need policy, schema, or contract authority? | Do not put it here. Use policy, schema, or contract roots. |
| Need a public summary, map layer, or release artifact? | Do not put it here. Use governed release and public-surface roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local review fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic StewardReview, CulturalReview-adjacent, ReviewRecord, PolicyDecision, RedactionReceipt, ValidationReport, EvidenceBundle-stub, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- synthetic review examples for accepted-for-internal-use, needs-more-evidence, policy-deny, abstain, blocked, superseded, withdrawn, correction-required, rollback-required, and release-readiness cases
- synthetic public-summary envelopes for API, map, layer, Focus Mode, export, and generated-answer carriers
- canary values that make review-approval leakage, cultural-review inference, evidence-proof collapse, policy-decision collapse, protected-detail exposure, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, review case, reviewed object ref, reviewer role ref, source role, sensitivity posture, evidence ref, redaction receipt ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from pre-public lifecycle stores, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Real reviewer notes, consultation records, rights-holder communications, collection-security details, or restricted cultural context | Sensitive material requires governed policy, review, redaction, and release controls. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, API implementation, map implementation, pipeline implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/archaeology/review/
|-- README.md
|-- manifest_expectations.json
|-- test_review_fixture_manifest_shape.py
|-- test_review_fixture_no_network.py
|-- test_steward_review_fixture_finite_outcomes.py
|-- test_cultural_review_not_inferred_from_steward_review.py
|-- test_review_requires_evidence_policy_and_receipt_refs.py
|-- test_review_fixture_does_not_authorize_release.py
|-- test_correction_withdrawal_rollback_review_refs.py
`-- test_focus_mode_review_fixture_abstains_without_release.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/review
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no protected detail, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Review Fixture Manifest

Synthetic test-local manifests should describe review fixture expectations without carrying real review material or approval authority.

```json
{
  "fixture_manifest_id": "archaeology-review-test-fixture-manifest-example",
  "domain": "archaeology",
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_steward_review/example-fixture.json",
  "fixture_family": "review_posture_envelope",
  "review_case": "needs_more_evidence_before_release_readiness",
  "review_object_family": "StewardReview",
  "reviewed_object_ref": "candidate-feature-fixture-arch-review-001",
  "source_role": "candidate",
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-review-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-review-001",
  "policy_decision_ref": "policy-decision-fixture-arch-review-001",
  "review_record_ref": "review-record-fixture-arch-review-001",
  "cultural_review_ref": null,
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-arch-review-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "REVIEW_FIXTURE_TEST_DOES_NOT_AUTHORIZE_RELEASE",
  "must_not_claim": [
    "REVIEW_APPROVAL_CANARY",
    "CULTURAL_REVIEW_APPROVAL_CANARY",
    "CONSULTATION_RECORD_CANARY",
    "CONFIRMED_SITE_CANARY",
    "PROTECTED_DETAIL_CANARY",
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
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; contracts, policy, evidence, receipts, release, and public surfaces remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `fixtures/domains/archaeology/synthetic_steward_review/README.md` | CONFIRMED repo evidence | Defines canonical synthetic review-shaped examples and states fixtures are not evidence, approval, release state, or published artifacts. | Payload inventory and validators remain NEEDS VERIFICATION. |
| `contracts/domains/archaeology/steward_review.md` | CONFIRMED repo evidence | Defines StewardReview as governed review posture and separates it from evidence proof, policy decision, cultural review, release approval, and public disclosure. | Paired schema and validator behavior remain NEEDS VERIFICATION. |
| `tests/fixtures/domains/archaeology/api/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local API fixture posture and notes missing immediate parent index. | Does not prove review-fixture tests exist. |
| `tests/fixtures/domains/archaeology/promotion/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local promotion fixture posture and release-boundary discipline. | Does not prove review-fixture tests exist. |
| `tests/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines Archaeology domain tests and separates tests from fixture, schema, policy, lifecycle, release, and public-client authority. | Does not prove executable review-fixture tests. |
| `docs/domains/archaeology/SENSITIVITY.md` and `PUBLICATION_AND_POLICY.md` | CONFIRMED repo evidence | Support deny-by-default, review-gated, receipt-backed, policy-gated, release-gated, correction, rollback, and AI-surface posture. | Machine-readable enforcement remains in schemas, policy, release, and CI. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/review/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when review fixture wrappers may live here instead of `fixtures/domains/archaeology/synthetic_steward_review/`.
- [ ] Confirm review fixture manifest schema, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for review manifest shape, no-network fixture loading, finite outcomes, evidence refs, policy refs, cultural-review non-inference, redaction receipt refs, release refs, correction refs, withdrawal refs, and rollback refs.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real source data, production review payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats a review-shaped fixture pass as source truth, candidate confirmation, policy approval, cultural review approval, consultation proof, review approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, review boundary, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)