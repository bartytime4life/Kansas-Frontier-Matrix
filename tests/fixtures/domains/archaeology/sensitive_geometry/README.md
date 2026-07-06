<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-domains-archaeology-sensitive-geometry-readme
title: Archaeology Sensitive Geometry Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; empty-placeholder-replaced; archaeology-sensitive-geometry-test-fixture-lane; PROPOSED / NEEDS VERIFICATION before promotion
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
policy_label: public-doc; tests; fixtures; archaeology; sensitive-geometry-fixtures; synthetic-only; no-network; deny-by-default; redaction-required; generalized-only; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, archaeology, sensitive-geometry, generalized-geometry, redaction, H3, RedactionReceipt, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, EvidenceBundle, EvidenceRef, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../api/README.md
  - ../promotion/README.md
  - ../review/README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../README.md
  - ../../../../domains/archaeology/README.md
  - ../../../../domains/archaeology/fixtures/README.md
  - ../../../../domains/archaeology/fixtures/source_admission/README.md
  - ../../../../../fixtures/domains/archaeology/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_archaeological_site/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_candidate_feature/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_publication_transform_receipt/README.md
  - ../../../../../fixtures/domains/archaeology/synthetic_steward_review/README.md
  - ../../../../../fixtures/domains/archaeology/valid/README.md
  - ../../../../../fixtures/domains/archaeology/invalid/README.md
  - ../../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../../docs/domains/archaeology/MAP_UI_CONTRACTS.md
  - ../../../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../../../contracts/domains/archaeology/sensitivity_transform.md
  - ../../../../../contracts/domains/archaeology/publication_transform_receipt.md
  - ../../../../../contracts/domains/archaeology/steward_review.md
  - ../../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../../policy/domains/archaeology/
  - ../../../../../release/candidates/archaeology/
notes:
  - "This README replaces the empty placeholder content at tests/fixtures/domains/archaeology/sensitive_geometry/README.md."
  - "This lane documents test-local expectations for archaeology sensitive-geometry fixtures. Canonical reusable archaeology fixtures live under fixtures/domains/archaeology/ unless an ADR or parent README says otherwise."
  - "No parent README was found at tests/fixtures/domains/archaeology/README.md during authoring. This lane is self-contained until that parent index is authored."
  - "Sensitive-geometry fixtures must be synthetic and generalized. They must not store protected coordinates, precise site locations, reverse-geocodable hints, or public release approvals."
  - "Executable tests, sensitive-geometry fixture payload inventory, schema bindings, harness wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology sensitive geometry test fixtures

> Test-lane documentation for Archaeology sensitive-geometry fixtures referenced from `tests/fixtures/domains/archaeology/sensitive_geometry/`. This path describes safe synthetic redaction and generalization expectations without storing protected coordinates, site-location truth, map truth, or release approval.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: sensitive geometry fixtures" src="https://img.shields.io/badge/lane-sensitive__geometry__fixtures-purple">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-brown">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: no protected coordinates" src="https://img.shields.io/badge/boundary-no__protected__coordinates-success">
</p>

**Path:** `tests/fixtures/domains/archaeology/sensitive_geometry/README.md`  
**Status:** draft / empty placeholder replaced / Archaeology sensitive-geometry test-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/domains/archaeology/sensitive_geometry`  
**Canonical reusable fixture root:** `fixtures/domains/archaeology/`  
**Default execution posture:** deterministic, synthetic, no-network, generalized fixture envelopes only  
**Truth posture:** CONFIRMED target file existed as an empty placeholder before replacement; CONFIRMED `tests/fixtures/domains/archaeology/README.md` was not found during authoring; CONFIRMED sibling `api/`, `promotion/`, and `review/` README lanes exist as test-local fixture lanes; CONFIRMED canonical `fixtures/domains/archaeology/README.md` exists and says fixtures are examples only, not records, evidence, approvals, release state, or published artifacts; CONFIRMED archaeology sensitivity docs require deny-by-default handling for exact site geometry and RedactionReceipt-backed public-safe transformations; NEEDS VERIFICATION for executable sensitive-geometry tests, fixture payload inventory, accepted schemas, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/domains/archaeology/sensitive_geometry/` is a test-local documentation lane for Archaeology sensitive-geometry fixture expectations.

This lane should describe how tests may use synthetic geometry envelopes to prove that protected location detail is denied, generalized, redacted, abstained, or withheld before any public surface can be shaped. It may cover generalized cell refs, county/region-only placeholders, redaction-result examples, source-to-public transform examples, map-envelope examples, tile-envelope examples, Evidence Drawer geometry summaries, Focus Mode geometry summaries, correction refs, withdrawal refs, and rollback refs.

A passing fixture check here should not mean that an archaeology site exists, a candidate is confirmed, a location is accurate, a geometry is public, a map layer is released, a reviewer approved release, or an AI answer is authoritative. It should mean only that a bounded synthetic sensitive-geometry fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement Basis

Directory Rules place enforceability proof under `tests/`. The canonical reusable fixture root is `fixtures/`. This requested path sits under `tests/fixtures/`, so it must remain test-scoped and subordinate to fixture, policy, evidence, receipt, map, API, and release authority roots.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Sensitive-geometry fixture-test expectations | `tests/fixtures/domains/archaeology/sensitive_geometry/` | This directory. |
| Parent test-fixture lane | `tests/fixtures/domains/archaeology/` | Parent README missing at authoring time; NEEDS VERIFICATION. |
| Reusable archaeology fixtures | `fixtures/domains/archaeology/` | Canonical fixture root; referenced, not replaced. |
| Archaeology domain tests | `tests/domains/archaeology/` | Consumers and validators; not fixture authority. |
| Archaeology fixture tests | `tests/domains/archaeology/fixtures/` | Confirmed test fixture parent lane. |
| API, promotion, and review fixture tests | `tests/fixtures/domains/archaeology/api/`, `promotion/`, `review/` | Confirmed sibling lanes. |
| Sensitivity and transform contracts | `contracts/domains/archaeology/` | Define meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/archaeology/` or ADR-selected equivalent | Define accepted shape; not owned here. |
| Policy authority | `policy/domains/archaeology/` or accepted policy roots | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release and public map decisions | `release/`, map/API/artifact roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not use this directory as a protected-location fixture cache, site-coordinate example folder, map-layer source, release candidate folder, receipt store, review record store, or public artifact home. It is a documentation and test-fixture expectation lane only.

---

## Invariant Under Test

> **Sensitive-geometry fixtures prove denial, redaction, and generalization behavior; they do not store or release protected geometry.**

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/archaeology/`; test-local wrappers require a documented reason. | validation failure. |
| Synthetic-only boundary | Geometry fixtures use fake IDs, mock markers, generalized placeholders, and non-reverse-geocodable examples. | quarantine / validation failure. |
| No-coordinate boundary | Fixtures do not carry exact protected coordinates, raw geometries, precise site footprints, or reverse-geocodable hints. | `DENY` / validation failure. |
| Generalization boundary | Public-safe examples use generalized posture such as region, county, approved cell ref, masked extent, or redacted summary. | `DENY` / `ABSTAIN`. |
| Redaction boundary | Any public-safe transform cites a synthetic RedactionReceipt ref and named profile ref where material. | validation failure / `DENY`. |
| Policy boundary | Exact geometry, insufficient review, missing rights, missing receipt, or missing release state fails closed. | `DENY` / `ABSTAIN`. |
| Review boundary | Reviewer and rights-holder review refs are explicit where materiality requires them. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Claim-like geometry summaries cite synthetic EvidenceRef and EvidenceBundle-stub expectations or abstain. | `ABSTAIN`. |
| Map/UI boundary | Map, tile, layer, screenshot, Focus Mode, and API fixtures cannot bypass redaction, policy, review, or release state. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, map publication, correction approval, or rollback approval. | promotion block. |

---

## Expected Sensitive-Geometry Fixture Families

| Family | Purpose | Boundary |
|---|---|---|
| Exact-geometry denial fixtures | Verify exact or protected geometry examples deny or abstain. | Negative examples must still be synthetic. |
| Generalized geometry fixtures | Verify public-safe generalized carriers keep only allowed geometry posture. | Generalized fixture is not publication. |
| Redaction receipt fixtures | Verify generalized public-safe examples require synthetic receipt refs. | Receipt-shaped refs are not receipt authority. |
| Policy-deny fixtures | Verify missing policy, review, evidence, receipt, or release refs fail closed. | Denial examples do not store restricted detail. |
| Map and tile fixtures | Verify map-like envelopes cannot expose protected geometry or precise hints. | Map-shaped fixture is not map truth. |
| Evidence Drawer fixtures | Verify geometry summaries carry evidence refs or abstain. | Evidence stubs are synthetic. |
| Focus Mode fixtures | Verify answer-like summaries cite released evidence or abstain. | AI is not root truth. |
| Correction and withdrawal fixtures | Verify supersession and withdrawal refs invalidate geometry carriers. | No silent edit. |
| Rollback fixtures | Verify rollback refs point to synthetic prior safe state and preserve audit posture. | Rollback fixture is not rollback approval. |
| No-network fixtures | Verify local deterministic loading and no live geocoding, map, or source calls. | Integration tests require separate gates. |

---

## Relationship to Canonical Archaeology Fixtures

The canonical Archaeology fixture root documents synthetic child lanes for site-shaped, candidate-shaped, publication-transform, steward-review, valid, invalid, and golden examples. This `tests/fixtures/.../sensitive_geometry/` lane should avoid duplicating those payloads.

| Question | Preferred answer |
|---|---|
| Need a reusable archaeology fixture payload? | Put it under `fixtures/domains/archaeology/`. |
| Need a test-only sensitive-geometry wrapper, expectation map, or parametrization file? | This lane may be appropriate if it is clearly test-local. |
| Need exact site geometry or protected coordinates? | Do not put it here. Use governed sensitive lifecycle roots and policy gates; public tests should use synthetic generalized placeholders. |
| Need policy, schema, contract, or receipt authority? | Do not put it here. Use policy, schema, contract, or receipt roots. |
| Need a public map layer, tile, screenshot, API response, or release artifact? | Do not put it here. Use governed release and public-surface roots. |

---

## Accepted Inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- references to canonical Archaeology fixtures under `fixtures/domains/archaeology/`
- test-local sensitive-geometry fixture manifests with fake IDs, mock markers, finite outcomes, and expected reason codes
- synthetic generalized geometry refs such as region-only, county-only, approved-cell-placeholder, masked-extent-placeholder, or no-geometry responses
- synthetic redaction profile refs, RedactionReceipt refs, PolicyDecision refs, ReviewRecord refs, EvidenceBundle-stub refs, ReleaseManifest refs, CorrectionNotice refs, WithdrawalNotice refs, and RollbackCard refs
- synthetic map/API/tile/Focus Mode/public summary envelopes that are already generalized or expected to deny/abstain
- canary values that make exact-geometry leakage, reverse-geocodable hints, policy-decision collapse, review-approval leakage, receipt omission, map-truth leakage, AI-truth leakage, or release approval obvious
- local validation envelopes emitted by test helpers

Safe outputs may include public-safe references and operational fields such as fixture ID, fixture family, geometry posture, redaction profile ref, evidence ref, redaction receipt ref, policy decision ID, review record ID, release ref, finite outcome, reason code, correction ref, withdrawal ref, and rollback ref.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real coordinates, raw geometry, precise site footprints, reverse-geocodable hints, collection-security detail, or restricted cultural context | Sensitive material requires governed policy, review, redaction, and release controls. |
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Direct reads from pre-public lifecycle stores, internal stores, unpublished candidates, or runtime outputs | Bypasses the trust membrane. |
| Secrets, credentials, private endpoints, production logs, or telemetry | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, API implementation, map implementation, pipeline implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested Layout

```text
tests/fixtures/domains/archaeology/sensitive_geometry/
|-- README.md
|-- manifest_expectations.json
|-- test_sensitive_geometry_fixture_manifest_shape.py
|-- test_sensitive_geometry_fixture_no_network.py
|-- test_exact_geometry_fixture_denies.py
|-- test_generalized_geometry_requires_redaction_receipt.py
|-- test_map_tile_fixture_never_exposes_protected_geometry.py
|-- test_focus_mode_geometry_fixture_abstains_without_release.py
|-- test_correction_withdrawal_rollback_geometry_refs.py
`-- test_sensitive_geometry_canaries.py
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run Posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/fixtures/domains/archaeology/sensitive_geometry
```

Required run posture: no network access, no live service calls, no direct lifecycle-store reads, no geocoding, no real secrets, no production logs, no production trust artifacts, no protected location detail, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal Sensitive-Geometry Fixture Manifest

Synthetic test-local manifests should describe sensitive-geometry expectations without carrying real location material.

```json
{
  "fixture_manifest_id": "archaeology-sensitive-geometry-test-fixture-manifest-example",
  "domain": "archaeology",
  "canonical_fixture_ref": "fixtures/domains/archaeology/synthetic_candidate_feature/example-fixture.json",
  "fixture_family": "sensitive_geometry_guardrail",
  "geometry_posture": "generalized_placeholder",
  "raw_geometry_present": false,
  "public_geometry_allowed": false,
  "mock_marker": true,
  "evidence_ref": "evidence-ref-fixture-arch-geom-001",
  "redaction_profile_ref": "redaction-profile-fixture-arch-geom-001",
  "redaction_receipt_ref": "redaction-receipt-fixture-arch-geom-001",
  "policy_decision_ref": "policy-decision-fixture-arch-geom-001",
  "review_record_ref": "review-record-fixture-arch-geom-001",
  "release_manifest_ref": null,
  "rollback_card_ref": "rollback-card-fixture-arch-geom-001",
  "expected_outcome": "ABSTAIN",
  "reason_code": "SENSITIVE_GEOMETRY_FIXTURE_TEST_DOES_NOT_AUTHORIZE_PUBLICATION",
  "must_not_claim": [
    "EXACT_COORDINATE_CANARY",
    "PROTECTED_LOCATION_CANARY",
    "REVERSE_GEOCODE_HINT_CANARY",
    "REVIEW_APPROVAL_CANARY",
    "MAP_TRUTH_CANARY",
    "AI_TRUTH_CANARY",
    "RELEASE_APPROVAL_CANARY"
  ]
}
```

The JSON above is illustrative. Accepted schema, field names, fixture homes, geometry posture vocabulary, reason codes, and CI wiring remain NEEDS VERIFICATION.

---

## Evidence Ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| `Directory Rules.pdf` and repo directory-rule docs | CONFIRMED doctrine | `tests/` is the enforceability root; `fixtures/` is the fixture responsibility root; policy, receipts, release, map, API, and public artifacts remain separate. | Does not prove executable tests, fixture inventory, CI, or pass rates. |
| `fixtures/domains/archaeology/README.md` | CONFIRMED repo evidence | Defines the canonical Archaeology fixture root, child fixture lanes, accepted synthetic examples, exclusions, and verification status. | Payload inventory and test wiring remain NEEDS VERIFICATION. |
| `docs/domains/archaeology/SENSITIVITY.md` | CONFIRMED repo evidence | Defines deny-by-default handling for exact site geometry and requires named redaction profiles, RedactionReceipt, review, and release controls for public-safe transforms. | Machine-readable enforcement remains in schemas, policy, release, and CI. |
| `docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED repo evidence | Defines placement posture, sensitive-lane path guidance, lifecycle invariant, exact-location denial, and release path separation. | Specific paths in that doc are marked PROPOSED until verified. |
| `docs/domains/archaeology/PUBLICATION_AND_POLICY.md` | CONFIRMED repo evidence | Describes governed API surfaces, policy gates, release manifest, correction, rollback, and AI surface posture. | Route names and implementation details remain PROPOSED where not verified. |
| `tests/fixtures/domains/archaeology/api/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local API fixture posture and notes missing immediate parent index. | Does not prove sensitive-geometry tests exist. |
| `tests/fixtures/domains/archaeology/promotion/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local promotion fixture posture and release-boundary discipline. | Does not prove sensitive-geometry tests exist. |
| `tests/fixtures/domains/archaeology/review/README.md` | CONFIRMED sibling lane README | Establishes sibling test-local review fixture posture and review-approval boundary. | Does not prove sensitive-geometry tests exist. |
| GitHub target file before update | CONFIRMED repo evidence | `tests/fixtures/domains/archaeology/sensitive_geometry/README.md` existed as an empty placeholder before replacement. | Placeholder proves path existence only. |
| `tests/fixtures/domains/archaeology/README.md` | CONFIRMED not found in GitHub fetch | Parent index was missing during authoring. | Missing parent should be created before treating this subtree as mature. |

---

## Validation Checklist

- [ ] Confirm whether `tests/fixtures/` is intended as a supported test-local fixture lane or only a compatibility surface.
- [ ] Create or confirm parent indexes at `tests/fixtures/README.md`, `tests/fixtures/domains/README.md`, and `tests/fixtures/domains/archaeology/README.md`.
- [ ] Confirm accepted rules for when sensitive-geometry fixture wrappers may live here instead of `fixtures/domains/archaeology/`.
- [ ] Confirm sensitive-geometry fixture manifest schema, geometry posture vocabulary, reason-code vocabulary, mock-marker requirements, and canary conventions.
- [ ] Confirm fixture payload inventory under `fixtures/domains/archaeology/` before linking tests to payloads.
- [ ] Add executable checks for manifest shape, no-network fixture loading, exact-geometry denial, generalized geometry posture, redaction receipt refs, policy refs, review refs, release refs, correction refs, withdrawal refs, rollback refs, and public-surface canaries.
- [ ] Confirm tests do not use real source feeds, live systems, secrets, production logs, production trust artifacts, restricted details, direct lifecycle-store reads, geocoders, map services, or public artifact writes.
- [ ] Wire this lane into CI only after executable tests and safe fixtures exist.

---

## Rollback

Rollback is required if this lane starts to store real coordinates, raw geometry, protected-location material, source data, production geometry payloads, trust-bearing records, release records, public artifacts, secrets, production logs, binding policy, contract/schema authority, map implementation, API implementation, pipeline implementation, or AI runtime behavior.

Rollback is also required if this lane treats a sensitive-geometry fixture pass as source truth, candidate confirmation, geometry accuracy, policy approval, review approval, redaction approval, release approval, publication approval, map truth, AI truth, correction approval, withdrawal approval, or rollback approval.

Rollback target: restore the previous safe README revision or remove this lane until parent fixture-test indexes, fixture homes, manifest schema, geometry vocabulary, redaction expectations, evidence expectations, policy expectations, release relationship, correction behavior, rollback behavior, and CI integration are reverified.

[Back to top](#top)