<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-sites-readme
title: Archaeology Sites Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-sites-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Archaeology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Sensitivity steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; archaeology; sites-fixtures; synthetic-only; no-network; deny-by-default; candidate-aware; exact-location-denied; evidence-bound; policy-gated; review-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, sites, site-fixtures, ArchaeologicalSite, CandidateFeature, SiteComponent, StewardReview, CulturalReview, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, EvidenceBundle, EvidenceRef, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../review/README.md
  - ../sensitive_geometry/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_archaeological_site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/OBJECT_FAMILIES.md
  - ../../../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../../../contracts/domains/archaeology/archaeological_site.md
  - ../../../../../contracts/domains/archaeology/candidate_feature.md
  - ../../../../../contracts/domains/archaeology/site_component.md
  - ../../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/sites/README.md."
  - "This lane documents test-local expectations for archaeology site-shaped fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "The canonical reusable site fixture lane observed during authoring is singular: fixtures/domains/archaeology/site/. This plural tests/fixtures/.../sites/ path must not become parallel site authority."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Site-shaped fixtures are not ArchaeologicalSite authority, CandidateFeature confirmation, source records, protected-location records, review approval, policy approval, release approval, or publication approval."
  - "Executable tests, site fixture payload inventory, schema bindings, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology sites test fixtures

> Test-lane documentation for Archaeology site-shaped fixtures referenced from `tests/fixtures/domains/archaeology/sites/`. This path describes safe synthetic site and candidate expectations without turning examples into real site records, candidate confirmation, protected-location storage, review approval, policy approval, map truth, or release authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: sites test fixtures" src="https://img.shields.io/badge/lane-sites__test__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: fixtures not site records" src="https://img.shields.io/badge/boundary-fixtures__not__site__records-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/sites/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology sites test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/sites`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Canonical reusable site fixture lane observed:** `fixtures/domains/archaeology/site/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/fixtures/domains/archaeology/README.md` was not found during authoring; CONFIRMED sibling `api/`, `promotion/`, `review/`, and `sensitive_geometry/` README lanes exist as test-local fixture lanes; CONFIRMED canonical `fixtures/domains/archaeology/site/README.md` exists and identifies site-shaped fixtures as fixture-only, not real site records, source data, exact-location data, policy authority, release authority, or published-layer authority; CONFIRMED `fixtures/domains/archaeology/synthetic_archaeological_site/README.md` exists and says examples are synthetic and not authoritative project records; NEEDS VERIFICATION for executable site-fixture tests, fixture payload inventory, accepted schemas, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/sites/` is a test-local documentation lane for Archaeology site-shaped fixture expectations.

This lane should describe how tests may use synthetic site, site-component, candidate-feature, redacted-site-card, denied-detail, withheld-geometry, review-needed, policy-needed, evidence-needed, release-needed, correction, withdrawal, and rollback examples.

A passing fixture check here should not mean that a site exists, a candidate is confirmed, a site boundary is known, a protected location is public, a reviewer approved release, a policy decision allows exposure, a map layer is published, or an AI answer is authoritative. It should mean only that a bounded synthetic site-shaped fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped and subordinate to fixture, contract, schema, policy, evidence, receipt, release, map, API, and public artifact roots.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Site-shaped fixture-test expectations | `tests/fixtures/domains/archaeology/sites/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Reusable site-shaped fixtures | `fixtures/domains/archaeology/site/` | Canonical observed fixture lane; referenced, not replaced. |
| Reusable synthetic site fixtures | `fixtures/domains/archaeology/synthetic_archaeological_site/` | Canonical observed fixture lane; referenced, not replaced. |
| Reusable candidate fixtures | `fixtures/domains/archaeology/synthetic_candidate_feature/` | Candidate examples; not confirmed sites. |
| Archaeology domain tests | `tests/domains/archaeology/` | Consumers and validators; not fixture authority. |
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Confirmed test fixture parent lane. |
| API, promotion, review, and sensitive-geometry fixture tests | `tests/fixtures/domains/archaeology/api/`, `promotion/`, `review/`, `sensitive_geometry/` | Confirmed sibling lanes. |
| Site semantic contracts | `contracts/domains/archaeology/archaeological_site.md`, `candidate_feature.md`, `site_component.md` | Define object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/` or ADR-selected equivalent | Define accepted shape; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release and public map decisions | `release/`, map/API/artifact roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a site registry, candidate-confirmation queue, protected-location fixture cache, source export cache, review record store, policy decision store, release candidate folder, map-layer source, or public artifact home. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Site-shaped fixtures are synthetic bounded examples, not ArchaeologicalSite truth.** Test fixture success proves only that the fixture expectation it was designed to exercise behaved as expected.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Singular/plural boundary | `fixtures/domains/archaeology/site/` remains the observed canonical reusable lane; this plural test path must not create parallel site authority. | promotion block. |
| Synthetic-only boundary | Site fixtures use fake IDs, mock markers, generalized descriptions, and reviewable payloads. | quarantine / validation failure. |
| Candidate boundary | CandidateFeature-shaped fixtures remain candidates and cannot be upgraded into confirmed sites by labels, helpers, API wording, maps, or generated text. | `DENY` / `ABSTAIN`. |
| No-coordinate boundary | Fixtures do not carry exact protected coordinates, raw geometries, precise footprints, or reverse-geocodable hints. | `DENY` / validation failure. |
| Site-component boundary | SiteComponent examples do not create a whole-site record or imply site confirmation. | validation failure. |
| Evidence boundary | Claim-like site summaries cite synthetic EvidenceRef and EvidenceBundle-stub expectations or abstain. | `ABSTAIN`. |
| Review boundary | Steward, cultural, sensitivity, and rights-holder review refs are explicit where materiality requires them. | `DENY` / `ABSTAIN`. |
| Policy boundary | Missing policy, missing review, missing receipt, missing release state, or exact-detail attempts fail closed. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, map publication, correction approval, or rollback approval. | promotion block. |

---

## Expected Site Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| Site-shaped valid fixtures | Verify safe synthetic ArchaeologicalSite-shaped examples satisfy expected test shape. | Valid fixture is not a real site. |
| Candidate-not-confirmed fixtures | Verify candidate examples retain candidate posture. | Candidate is not a confirmed site. |
| Site-component fixtures | Verify component examples do not imply whole-site truth. | Component is not site authority. |
| Exact-detail denial fixtures | Verify exact or protected detail requests deny or abstain. | Negative examples must still be synthetic. |
| Generalized public-safe fixtures | Verify public-safe site cards use generalized or withheld posture. | Generalized fixture is not publication. |
| Evidence and receipt fixtures | Verify EvidenceRef, RedactionReceipt, and transform refs are present where material. | Refs are synthetic. |
| Review and policy fixtures | Verify review and policy refs are required for allow-like examples. | Fixture is not review or policy authority. |
| API and map fixtures | Verify public-surface carriers cannot expose protected detail or imply confirmation. | Map-shaped fixture is not map truth. |
| Correction and withdrawal fixtures | Verify supersession and withdrawal refs invalidate site carriers. | No silent edit. |
| Rollback fixtures | Verify rollback refs point to synthetic prior safe state and preserve audit posture. | Rollback fixture is not rollback approval. |
| No-network fixtures | Verify local deterministic loading and no live source, geocoding, map, or AI calls. | Integration tests require separate gates. |

---

## Relationship to Canonical Archaeology Fixtures

The canonical Archaeology fixture root documents site-shaped and synthetic site lanes. This `tests/fixtures/.../sites/` lane should avoid duplicating those payloads.

| Question | Preferred answer |
|---|---|
| Need a reusable site-shaped fixture payload? | Put it under `fixtures/domains/archaeology/site/` or another accepted canonical fixture lane. |
| Need a test-only site wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need exact site geometry or protected coordinates? | Do not put it here. Use governed sensitive lifecycle roots and policy gates; public tests should use synthetic generalized placeholders. |
| Need a real `ArchaeologicalSite`, `CandidateFeature`, or `SiteComponent` record? | Do not put it here. Use governed lifecycle and catalog roots. |
| Need policy, schema, contract, evidence, receipt, or release authority? | Do not put it here. Use the owning root. |
| Need a public map layer, tile, screenshot, API response, or release artifact? | Do not put it here. Use governed release and public-surface roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local site fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic ArchaeologicalSite-shaped, CandidateFeature-shaped, SiteComponent-shaped, denied-detail, withheld-detail, generalized-site-card, and no-geometry envelopes
- synthetic EvidenceRef, EvidenceBundle-stub, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and RollbackCard refs
- synthetic map/API/tile/Focus Mode/public summary envelopes that are already generalized or expected to deny/abstain
- canary values that make candidate-confirmed collapse, exact-detail leakage, protected-location hints, site-registry behavior, review-approval leakage, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, object family, candidate/site posture, geometry posture, evidence ref, redaction receipt ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real site records, real candidate records, source-system exports, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Real coordinates, raw geometry, precise site footprints, reverse-geocodable hints, collection-security detail, or restricted cultural context | Sensitive material requires governed policy, review, redaction, and release controls. |
| Direct reads from pre-public lifecycle stores, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, API implementation, map implementation, pipeline implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/archaeology/sites/
|-- README.md
|-- manifest_expectations.json
|-- test_sites_fixture_manifest_shape.py
|-- test_sites_fixture_no_network.py
|-- test_candidate_fixture_not_confirmed_site.py
|-- test_site_fixture_denies_exact_detail.py
|-- test_site_fixture_requires_evidence_policy_review_refs.py
|-- test_site_fixture_does_not_authorize_publication.py
|-- test_correction_withdrawal_rollback_site_refs.py
`-- test_sites_fixture_canaries.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/sites
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no geocoding, no real secrets, no production logs, no production trust artifacts, no protected location detail, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Sites Fixture Manifest

Synthetic test-local manifests should describe site fixture expectations without carrying real site material or release authority.

```json
{
  "fixture_manifest_id": "archaeology-sites-test-fixture-manifest-example",
  "domain": "archaeology",
  "canonical_fixture_ref": "fixtures/domains/archaeology/site/example-fixture.json",
  "fixture_family": "site_guardrail_envelope",
  "object_family": "CandidateFeature",
  "site_posture": "candidate_not_confirmed",
  "geometry_posture": "withheld_or_generalized_placeholder",
  "raw_geometry_present": false,
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-sites-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-sites-001",
  "policy_decision_ref": "policy-decision-fixture-arch-sites-001",
  "review_record_ref": "review-record-fixture-arch-sites-001",
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-arch-sites-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "SITES_FIXTURE_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "CONFIRMED_SITE_CANARY",
    "EXACT_COORDINATE_CANARY",
    "PROTECTED_LOCATION_CANARY",
    "REVIEW_APPROVAL_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, site posture vocabulary, geometry posture vocabulary, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; contracts, schemas, policy, evidence, receipts, release, map, API, and public artifacts remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `fixtures/domains/archaeology/site/README.md` | CONFIRMED repo evidence | Defines the observed canonical site fixture lane as fixture-only, safe, synthetic/generalized, not real site records, source data, exact-location data, policy authority, release authority, or published-layer authority. | Payload inventory and tests remain NEEDS VERIFICATION. |
| `fixtures/domains/archaeology/synthetic_archaeological_site/README.md` | CONFIRMED repo evidence | Defines synthetic archaeology site examples and says fixtures are not authoritative project records, evidence, approval, release state, or published artifacts. | Payload inventory and validators remain NEEDS VERIFICATION. |
| `docs/domains/archaeology/SENSITIVITY.md` | CONFIRMED repo evidence | Defines deny-by-default handling for exact site geometry and requires named redaction profiles, RedactionReceipt, review, and release controls for public-safe transforms. | Machine-readable enforcement remains in schemas, policy, release, and CI. |
| `tests/fixtures/domains/archaeology/api/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local API fixture posture and notes missing immediate parent index. | Does not prove site-fixture tests exist. |
| `tests/fixtures/domains/archaeology/promotion/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local promotion fixture posture and release-boundary discipline. | Does not prove site-fixture tests exist. |
| `tests/fixtures/domains/archaeology/review/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local review fixture posture and review-approval boundary. | Does not prove site-fixture tests exist. |
| `tests/fixtures/domains/archaeology/sensitive_geometry/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local sensitive-geometry fixture posture and no-protected-coordinate boundary. | Does not prove site-fixture tests exist. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/sites/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when site fixture wrappers may live here instead of `fixtures/domains/archaeology/site/`.
- [ ] Confirm whether this plural `sites/` path should remain, crosswalk to singular `site/`, or be retired after migration.
- [ ] Confirm sites fixture manifest schema, site posture vocabulary, geometry posture vocabulary, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for manifest shape, no-network fixture loading, candidate-not-confirmed behavior, exact-detail denial, evidence refs, policy refs, review refs, redaction receipt refs, release refs, correction refs, withdrawal refs, rollback refs, and public-surface canaries.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, geocoders, map services, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real site records, candidate-confirmation records, exact coordinates, raw geometry, protected-location material, source data, production site payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats a site-shaped fixture pass as site truth, candidate confirmation, site boundary proof, geometry accuracy, policy approval, review approval, redaction approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, site vocabulary, geometry vocabulary, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)