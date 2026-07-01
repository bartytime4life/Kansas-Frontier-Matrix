<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology/invalid/readme
title: Archaeology invalid fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): archaeology domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): cultural-review reviewer; TODO(owner): sensitivity reviewer; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: restricted-review
related:
  - ../golden/README.md
  - ../archaeology-public-safe/README.md
  - ../../archaeology-public-safe/README.md
  - ../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../policy/domains/archaeology/README.md
  - ../../../../contracts/domains/archaeology/
  - ../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../tests/domains/archaeology/
  - ../../../../release/candidates/archaeology/
  - ../../../../data/published/layers/archaeology/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, archaeology, invalid-fixtures, negative-fixtures, expected-error, public-safe, deny-by-default, exact-location-denial, redaction, generalization, no-leak, policy-fixtures, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/archaeology/invalid/README.md`."
  - "This directory is for safe negative Archaeology fixtures and expected failure examples only; invalid examples must not contain the sensitive content they are intended to reject."
  - "Repo search did not surface confirmed invalid payload files in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "Invalid means expected to fail a bounded test, validator, policy helper, no-leak check, or release precheck; it does not authorize storing sensitive payloads."
  - "No tests, validators, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology invalid fixtures

Negative fixture lane for safe Archaeology failure cases under `fixtures/domains/archaeology/invalid/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Lane: invalid" src="https://img.shields.io/badge/lane-invalid-critical">
  <img alt="Default: fail closed" src="https://img.shields.io/badge/default-fail__closed-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/archaeology/invalid/README.md`  
**Fixture posture:** safe negative fixtures for bounded Archaeology failure, denial, no-leak, and release-precheck tests  
**Authority posture:** fixture only; archaeology truth, source truth, sensitivity authority, cultural review, policy authority, lifecycle promotion, release approval, published-layer authority, and public-client permission remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [What invalid means here](#what-invalid-means-here) · [Accepted invalid material](#accepted-invalid-material) · [Exclusions](#exclusions) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Invalid fixtures are expected failure examples. They must be safe enough to store in the repository. A fixture that would expose protected archaeology material is not an invalid fixture; it is material to deny, restrict, quarantine, or remove from the repository.

> [!CAUTION]
> Do not place exact archaeological site geometry, burial/sacred-site detail, human-remains context, collection-security detail, looting-risk exposure, unresolved cultural sensitivity, private-owner detail, or reconstructive redaction clues here. Negative tests should use synthetic placeholders, coarse abstractions, withheld-state payloads, or expected error text.

---

## Purpose

This directory is for Archaeology negative fixtures.

Use this lane for small, public-safe examples that should be rejected by validators, policy helpers, redaction/generalization helpers, no-leak checks, release-precheck helpers, renderer guards, or API-envelope checks. The goal is to make failure behavior explicit without storing the sensitive data that the system is designed to protect.

A passing negative test proves only that the expected failure, denial, hold, abstention, withholding, or error was detected for the fixture. It does not prove a site exists, a candidate is confirmed, a cultural review was completed, a policy decision was issued, a release was approved, or a public answer may be shown.

---

## Placement basis

The requested path exists under `fixtures/domains/archaeology/`, which is a domain-facing fixture segment inside the `fixtures/` responsibility root. Archaeology canonical path guidance states that placement rules are confirmed while specific paths remain proposed until verified, and it carries the lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Invalid fixtures sit outside that lifecycle. They may model expected denial or validation failure, but they do not promote, release, prove, or publish Archaeology material.

---

## What invalid means here

`invalid` means invalid for a **specific bounded check**, not a place to store dangerous examples.

| Invalid for | Meaning | Safe representation |
|---|---|---|
| Schema | Shape should fail validation. | Use missing fields, wrong enum values, or synthetic IDs. |
| Policy helper | Policy should return deny, hold, abstain, or error. | Use reason-code-only or placeholder payloads. |
| No-leak check | Exact-detail request should be withheld. | Use synthetic request and expected withheld response. |
| Redaction/generalization | Unsafe transform should fail. | Use abstract geometry markers, not real locations. |
| Renderer/API guard | Public surface should disable, hide, or redact detail. | Use safe viewer-state payloads. |
| Release precheck | Required review, receipt, rollback, or policy fields are missing. | Use synthetic manifest-shaped examples only. |

Every invalid fixture should document the expected reason, consumer, and safe abstraction used.

---

## Accepted invalid material

This directory may contain:

| Material | Use |
|---|---|
| `invalid_<n>.json` | Safe negative example expected to fail a bounded check. |
| `invalid_<n>.expected_error.txt` | Expected error text, reason code, or reason pattern. |
| `*.input.json` | Synthetic request or input expected to produce denial, withholding, hold, abstention, or error. |
| `*.expected.json` | Expected safe output for the negative case. |
| `*.snapshot.json` | Snapshot-style denied/withheld/disabled viewer or helper output. |
| local README files | Fixture intent, failure mode, safe abstraction, and authority-boundary documentation. |

Good invalid cases include missing sensitivity disposition, missing review record, missing redaction receipt, missing rollback target, attempted exact-detail public request, candidate-confirmation ambiguity, stale or unsigned release-precheck payload, and invalid public-surface payload shape.

---

## Exclusions

Do not place any of the following in this lane:

| Excluded material | Correct action or home |
|---|---|
| Real restricted records, precise protected locations, sensitive cultural context, collection-security detail, or private-owner detail | Deny, restrict, quarantine, or handle in governed restricted storage after review. |
| Red-team payloads that reconstruct protected locations or sensitive context | Keep out of repository; test only with safe abstractions. |
| Lifecycle artifacts | `data/<phase>/archaeology/` under lifecycle rules. |
| EvidenceBundles, proof packs, validation reports, or receipts | Their verified proof/receipt homes. |
| Release manifests, promotion decisions, correction notices, rollback cards, signatures, or release changelog entries | `release/` roots. |
| Policy rules, schemas, contracts, validators, tests, app code, package code, or pipeline logic | Their canonical responsibility roots. |
| Published map layers, public API payloads, or public downloads | Governed published-data roots after release gates close. |

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Archaeology invalid fixtures | `fixtures/domains/archaeology/invalid/` | Documents safe expected-failure examples only. |
| Archaeology golden fixtures | `fixtures/domains/archaeology/golden/` | Sibling stable expected-output lane. |
| Public-safe Archaeology fixtures | `fixtures/domains/archaeology-public-safe/` and `fixtures/archaeology-public-safe/` | Referenced for public-safe fixture posture; not replaced here. |
| Archaeology domain doctrine | `docs/domains/archaeology/` | Referenced, not replaced. |
| Archaeology contracts and schemas | `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/` | Referenced, not duplicated. |
| Archaeology policy | `policy/domains/archaeology/` and related policy roots | Out of scope; fixtures may test policy helpers but do not define policy. |
| Cultural/sensitivity review | Reviewer workflows, receipts, policy decisions, release records | Out of scope; fixture success cannot substitute for review. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Release authority | `release/` roots | Out of scope. |
| Tests and validation proof | `tests/domains/archaeology/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into archaeology truth, source authority, EvidenceBundle authority, policy authority, sensitivity authority, cultural-review authority, release authority, or public-client permission.

---

## Expected layout

Use paired invalid examples and expected errors:

```text
fixtures/domains/archaeology/invalid/
  README.md
  invalid_1.json
  invalid_1.expected_error.txt
```

For request/response no-leak checks:

```text
fixtures/domains/archaeology/invalid/
  exact_detail_request.input.json
  exact_detail_request.expected.json
```

For grouped cases, prefer local READMEs:

```text
fixtures/domains/archaeology/invalid/
  README.md
  missing_review_record/
    README.md
    invalid_1.json
    invalid_1.expected_error.txt
  exact_location_public_request/
    README.md
    request.input.json
    response.expected.json
```

---

## Maintenance checklist

Before adding or changing Archaeology invalid fixtures:

- [ ] Confirm the consuming test, validator, renderer, policy helper, redaction helper, generalization helper, release precheck, or no-leak check.
- [ ] Confirm that the fixture is safe, synthetic, generalized, redacted, withheld, denied-state, or abstracted.
- [ ] Confirm that no exact protected-location, sensitive cultural, collection-security, private-owner, or reconstructive redaction clue is present.
- [ ] Pair each invalid fixture with expected error text, reason code, expected safe output, or consuming-test documentation.
- [ ] Preserve EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, rollback, and correction expectations in fixture intent when modeled.
- [ ] Keep examples compact, deterministic, public-safe, and reviewable.
- [ ] Update this README when fixture layout, test consumers, or validation expectations change.
- [ ] Run the relevant tests, validators, sensitivity checks, and no-leak checks before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct invalid payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed invalid payload files in this directory during this update. |
| Golden sibling posture | CONFIRMED DOC | The sibling golden README defines stable expected-output fixtures and states that golden output is not evidence or release authority. |
| Sensitive-domain posture | CONFIRMED DOC / RUNTIME UNKNOWN | Archaeology policy docs require exact-location and culturally sensitive material to fail closed unless reviewed policy paths allow bounded outputs. |
| Test execution | NOT RUN | No validators, pytest, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define invalid fixture guidance. |
| Repository search for Archaeology invalid fixtures | CONFIRMED SEARCH / NO MATCH | No confirmed invalid payload file was found for this directory in this update. | Search is not a full recursive filesystem listing. |
| `../golden/README.md` | CONFIRMED | Sibling golden fixture posture, fixture-only authority boundary, and public-safe expected-output constraints. | It is not invalid payload inventory or validator proof. |
| `../../../../policy/domains/archaeology/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Deny-by-default policy posture, redaction/generalization/review obligations, finite policy outcomes, and release prerequisites. | Concrete policy files, tests, CI binding, and runtime enforcement remain NEEDS VERIFICATION there. |
| `../../../../docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED RULES / PROPOSED PATHS | Archaeology placement rules, sensitive-domain path posture, and lifecycle invariant. | Specific paths are marked proposed until verified. |

[Back to top](#top)
