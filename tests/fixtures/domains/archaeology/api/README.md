<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-api-readme
title: Archaeology API Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-api-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Archaeology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - API steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; archaeology; api-fixtures; synthetic-only; no-network; deny-by-default; review-gated; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, api-fixtures, synthetic-fixtures, no-network, governed-api, ArchaeologyDecisionEnvelope, EvidenceDrawerPayload, LayerManifest, FocusMode, EvidenceBundle, EvidenceRef, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/golden/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../fixtures/domains/archaeology/site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_archaeological_site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../contracts/domains/archaeology/
  - ../../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/api/README.md."
  - "This lane documents test-local expectations for archaeology API-shaped fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Executable tests, API fixture payload inventory, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology API test fixtures

> Test-lane documentation for Archaeology API-shaped fixtures referenced from `tests/fixtures/domains/archaeology/api/`. This path describes safe synthetic envelopes for tests without turning those envelopes into source records, policy approval, release approval, public API implementation, map truth, or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: API test fixtures" src="https://img.shields.io/badge/lane-api__test__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not API" src="https://img.shields.io/badge/boundary-fixtures__not__api-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/api/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology API test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/api`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED canonical Archaeology fixture README exists under `fixtures/domains/archaeology/`; CONFIRMED domain and fixture-test README files identify `tests/` as enforceability proof and keep canonical fixtures, contracts, schemas, policy, lifecycle data, evidence, receipts, and release decisions in separate roots; CONFIRMED archaeology docs describe sensitive publication and governed API posture; NEEDS VERIFICATION for executable API-fixture tests, fixture payload inventory, schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/api/` is a test-local documentation lane for Archaeology API-shaped fixture expectations.

This lane should describe how tests may use synthetic request and response envelopes for governed Archaeology public-surface behavior. It may cover feature/detail resolver fixtures, Evidence Drawer fixtures, layer manifest resolver fixtures, Focus Mode answer fixtures, decision-envelope fixtures, redaction-result fixtures, policy-result fixtures, review-state fixtures, release-state fixtures, correction fixtures, and rollback fixtures.

A passing fixture check here should not mean that an archaeology claim is true, a site exists, a candidate is confirmed, a protected detail is releasable, a public API route exists, a map layer is published, a reviewer approved release, or an AI answer is authoritative. It should mean only that a bounded synthetic API-shaped fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| API-shaped fixture-test expectations | `tests/fixtures/domains/archaeology/api/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Reusable archaeology fixtures | `fixtures/domains/archaeology/` | Canonical fixture root; referenced, not replaced. |
| Archaeology domain tests | `tests/domains/archaeology/` | Consumers and validators; not fixture authority. |
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Confirmed test fixture parent lane. |
| Semantic contracts | `contracts/domains/archaeology/` or ADR-selected equivalent | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/` or ADR-selected equivalent | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |
| Public API and map implementation | App, API, map, tile, and artifact roots | Exercised only through safe synthetic envelopes. |

> [!IMPORTANT]
> Do not use this directory as a public API mock server, production payload dump, source export cache, release store, or substitute for the governed API. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Archaeology API fixtures are synthetic bounded envelopes, not public API authority.** Test fixture success proves only the fixture expectation it was designed to exercise.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixture envelopes use fake identifiers, mock markers, generalized geometry, and reviewable payloads. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, map services, release services, public APIs, or AI runtimes. | `ERROR`. |
| API boundary | API-shaped fixtures do not prove real route names, deployed behavior, DTO maturity, or public service availability. | NEEDS VERIFICATION / validation failure. |
| Sensitivity boundary | Protected or location-sensitive details fail closed unless a synthetic public-safe transform, receipt ref, policy ref, review ref, and release ref are present. | `DENY` / `ABSTAIN`. |
| Candidate boundary | Candidate-shaped fixtures remain candidates and cannot be upgraded into confirmed records by API wording. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like responses include EvidenceRef expectations or explicitly abstain. | `ABSTAIN`. |
| Receipt boundary | Redaction, validation, correction, withdrawal, and rollback refs are explicit where material. | validation failure. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |
| AI boundary | Focus Mode or generated-answer fixtures cite released evidence or abstain. | `ABSTAIN` / `DENY`. |

---

## Expected API Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| Decision envelope fixtures | Verify finite `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` outcomes and reason codes. | Envelope shape is not deployed API proof. |
| Feature/detail fixtures | Verify public-safe feature/detail responses never expose protected detail by default. | Generalized fixture is not source truth. |
| Evidence Drawer fixtures | Verify EvidenceRef and citation expectations are present for claim-like responses. | Evidence stubs are synthetic. |
| Layer manifest fixtures | Verify public layer envelopes require release refs and safe geometry posture. | Layer-shaped fixture is not publication. |
| Focus Mode fixtures | Verify generated or answer-like outputs cite released evidence or abstain. | AI is not root truth. |
| Policy-deny fixtures | Verify unsupported, uncertain, or protected requests fail closed. | Denial examples do not store real restricted data. |
| Redaction receipt fixtures | Verify public-safe transforms include receipt refs and do not embed restricted payloads. | Receipt-shaped fixture is not receipt authority. |
| Correction and rollback fixtures | Verify public carriers can be invalidated by correction, withdrawal, or rollback refs. | Rollback fixture is not rollback approval. |
| No-network fixtures | Verify local deterministic loading and no live service calls. | Integration tests require separate gates. |

---

## Relationship to Canonical Archaeology Fixtures

The canonical Archaeology fixture root already documents synthetic child lanes for golden, invalid, site-shaped, candidate-shaped, publication-transform, steward-review, and valid examples. This `tests/fixtures/.../api/` lane should avoid duplicating those payloads.

| Question | Preferred answer |
|---|---|
| Need a reusable archaeology fixture payload? | Put it under `fixtures/domains/archaeology/`. |
| Need a test-only API wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need source data? | Do not put it here. Use governed source and lifecycle roots. |
| Need policy, schema, or contract authority? | Do not put it here. Use policy, schema, or contract roots. |
| Need release or public API authority? | Do not put it here. Use release and governed API roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local API fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic request envelopes, response envelopes, decision envelopes, Evidence Drawer payloads, layer manifest stubs, Focus Mode answer stubs, and public-surface summaries
- synthetic SourceDescriptor, EvidenceRef, EvidenceBundle stub, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- synthetic valid, invalid, denied, abstention, correction, withdrawal, and rollback cases
- canary values that make trust-membrane bypass, candidate-confirmed collapse, protected-detail exposure, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, API surface, source role, sensitivity posture, evidence ref, redaction receipt ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

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
tests/fixtures/domains/archaeology/api/
|-- README.md
|-- manifest_expectations.json
|-- test_api_fixture_manifest_shape.py
|-- test_api_fixture_no_network.py
|-- test_decision_envelope_finite_outcomes.py
|-- test_feature_detail_fixture_denies_protected_detail.py
|-- test_evidence_drawer_fixture_requires_evidence_ref.py
|-- test_layer_manifest_fixture_requires_release_ref.py
|-- test_focus_mode_fixture_abstains_without_release.py
`-- test_correction_withdrawal_rollback_refs.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/api
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no protected location detail, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal API Fixture Manifest

Synthetic test-local manifests should describe API fixture expectations without carrying real archaeology data.

```json
{
  "fixture_manifest_id": "archaeology-api-test-fixture-manifest-example",
  "domain": "archaeology",
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_candidate_feature/example-fixture.json",
  "fixture_family": "governed_api_decision_envelope",
  "api_surface": "feature_detail_resolver_fixture",
  "source_role": "candidate",
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-api-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-api-001",
  "policy_decision_ref": "policy-decision-fixture-arch-api-001",
  "review_record_ref": "review-record-fixture-arch-api-001",
  "release_manifest_ref": null,
  "expected_outcome": "ABSTAIN",
  "reason_code": "API_FIXTURE_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
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
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; authority roots remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `tests/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines Archaeology domain tests and separates tests from fixture, schema, policy, lifecycle, release, and public-client authority. | Does not prove executable API-fixture tests. |
| `tests/domains/archaeology/fixtures/README.md` | CONFIRMED repo evidence | Defines fixture-test parent lane and confirms canonical fixtures belong outside tests. | Parent is under `tests/domains/`, not `tests/fixtures/`. |
| `docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED repo evidence | Defines placement posture, sensitive-lane path guidance, lifecycle invariant, and exact-location-denial/public-safe release posture. | Specific paths in that doc are marked PROPOSED until verified. |
| `docs/domains/archaeology/SENSITIVITY.md` | CONFIRMED repo evidence | Defines deny-by-default sensitivity posture, redaction, review, receipt, AI, and UI discipline. | Machine-readable enforcement remains in schemas, policy, release, and CI. |
| `docs/domains/archaeology/PUBLICATION_AND_POLICY.md` | CONFIRMED repo evidence | Describes governed API surfaces, policy gates, release manifest, correction, rollback, and AI surface posture. | Route names and implementation details remain PROPOSED where not verified. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/api/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when API fixture wrappers may live here instead of `fixtures/domains/archaeology/`.
- [ ] Confirm API fixture manifest schema, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for API manifest shape, no-network fixture loading, finite outcomes, feature/detail denial, EvidenceRef expectations, redaction receipt refs, release refs, correction refs, and rollback refs.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real source data, production API payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats an API-shaped fixture pass as source truth, candidate confirmation, policy approval, review approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, sensitivity handling, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)