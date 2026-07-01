<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology/golden/readme
title: Archaeology golden fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): archaeology domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): cultural-review reviewer; TODO(owner): sensitivity reviewer; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: restricted-review
related:
  - ../README.md
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
tags: [kfm, fixtures, domains, archaeology, golden-fixtures, expected-output, regression-fixtures, public-safe, synthetic-fixtures, exact-location-denial, deny-by-default, redaction, generalization, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/archaeology/golden/README.md`."
  - "This directory is for stable, synthetic, public-safe Archaeology golden fixtures only, not archaeology evidence, site truth, source records, policy authority, sensitivity authority, release authority, or published-layer authority."
  - "Repo search did not surface confirmed golden payload files in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "Golden means stable expected fixture output for a bounded test; it does not mean authoritative, reviewed, released, or true."
  - "No tests, validators, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology golden fixtures

Stable expected-output fixture lane for public-safe Archaeology examples under `fixtures/domains/archaeology/golden/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Lane: golden" src="https://img.shields.io/badge/lane-golden-yellow">
  <img alt="Default: deny exact location" src="https://img.shields.io/badge/default-deny__exact__location-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/archaeology/golden/README.md`  
**Fixture posture:** stable public-safe expected-output fixtures for bounded Archaeology tests  
**Authority posture:** fixture only; archaeology truth, source truth, sensitivity authority, cultural review, policy authority, lifecycle promotion, release approval, published-layer authority, and public-client permission remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [What golden means here](#what-golden-means-here) · [Accepted golden material](#accepted-golden-material) · [Exclusions](#exclusions) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are golden fixtures: stable inputs, expected outputs, or snapshots for bounded tests. They are not source data, site records, EvidenceBundles, proof packs, receipts, PolicyDecisions, ReviewRecords, RedactionReceipts, ReleaseManifests, published Archaeology layers, governed API responses, public map payloads, or archaeological truth.

> [!CAUTION]
> Golden fixtures in this lane must remain synthetic, generalized, redacted, withheld, denied-state, or otherwise public-safe. Do not place exact archaeological site geometry, burial/sacred-site detail, human-remains context, collection-security detail, looting-risk exposure, unresolved cultural sensitivity, private-owner detail, or reconstructive redaction clues here.

---

## Purpose

This directory is for stable Archaeology fixture cases used by regression tests, snapshot tests, renderer tests, validator tests, policy-helper tests, no-leak checks, redaction/generalization checks, and release-precheck helpers.

A golden fixture is useful because it gives reviewers and tests a stable expected result. It is not useful as evidence. A passing golden comparison proves only that the tested code still matches the expected fixture output. It does not prove a site exists, a candidate is confirmed, a cultural review was completed, a policy decision was issued, a release was approved, or a public answer may be shown.

---

## Placement basis

The requested path exists under `fixtures/domains/archaeology/`, which is a domain-facing fixture segment inside the `fixtures/` responsibility root. Archaeology canonical path guidance states that placement rules are confirmed while specific paths remain proposed until verified, and it carries the lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Golden fixtures sit outside that lifecycle. They may model expected outputs for tests, but they do not promote, release, prove, or publish Archaeology material.

---

## What golden means here

`golden` means stable expected fixture output for a **specific bounded test**. It does not mean authoritative, public, reviewed, culturally cleared, or true.

| Golden for | Meaning | Not implied |
|---|---|---|
| Renderer output | Stable expected public-safe style or viewer state. | The layer is released or publishable. |
| Redaction/generalization | Expected transformed shape for a safe synthetic case. | The transform was applied to real sensitive records. |
| Policy helper | Expected safe outcome, denial, hold, or obligation for a fixture case. | A real PolicyDecision exists. |
| Validator | Expected accepted/rejected fixture shape. | All release gates have closed. |
| No-leak check | Expected withheld/disabled/denied public state. | Underlying data exists or may be exposed. |
| Release precheck | Expected missing/required release fields for a synthetic case. | Release authority, signature, rollback card, or public serving permission. |

Every golden fixture should name the consuming test or helper as soon as that consumer exists.

---

## Accepted golden material

Accepted material must be synthetic or demonstrably public-safe, generalized, reproducible, and small enough for repository review.

| Material | Use |
|---|---|
| `*.input.json` | Stable input fixture for a bounded test. |
| `*.expected.json` | Expected public-safe output for the same case. |
| `*.snapshot.json` | Snapshot-style renderer, helper, or validation result. |
| `valid/valid_<n>.json` | Positive schema or helper fixtures if the consuming test expects a valid case. |
| `invalid/invalid_<n>.json` | Negative cases if the golden expectation is a stable rejection or denial output. |
| `invalid/invalid_<n>.expected_error.txt` | Expected error text or reason pattern. |
| local README files | Fixture intent, generation method, test consumer, and authority-boundary documentation. |

Good golden cases include synthetic generalized features, denied exact-location request responses, redacted or generalized shape outputs, candidate-not-confirmed viewer states, safe release-precheck failures, and evidence-drawer placeholder states that clearly do not claim evidence authority.

---

## Exclusions

Do not place any of the following in this lane:

| Excluded material | Correct action or home |
|---|---|
| Real restricted records, precise protected locations, sensitive cultural context, collection-security detail, or private-owner detail | Deny, restrict, quarantine, or handle in governed restricted storage after review. |
| Lifecycle artifacts | `data/<phase>/archaeology/` under lifecycle rules. |
| EvidenceBundles, proof packs, validation reports, or receipts | Their verified proof/receipt homes. |
| Release manifests, promotion decisions, correction notices, rollback cards, signatures, or release changelog entries | `release/` roots. |
| Policy rules, schemas, contracts, validators, tests, app code, package code, or pipeline logic | Their canonical responsibility roots. |
| Published map layers, public API payloads, or public downloads | Governed published-data roots after release gates close. |

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Archaeology golden fixtures | `fixtures/domains/archaeology/golden/` | Documents stable test examples only. |
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

Use paired input and expected-output cases:

```text
fixtures/domains/archaeology/golden/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
```

For snapshot-style fixtures:

```text
fixtures/domains/archaeology/golden/
  <case_name>.snapshot.json
```

For grouped cases, prefer local READMEs:

```text
fixtures/domains/archaeology/golden/
  README.md
  no_leak_exact_location_request/
    README.md
    request.input.json
    response.expected.json
  generalized_renderer_state/
    README.md
    layer.input.json
    render.snapshot.json
```

---

## Maintenance checklist

Before adding or changing Archaeology golden fixtures:

- [ ] Confirm the consuming test, validator, renderer, policy helper, redaction helper, generalization helper, release precheck, or no-leak check.
- [ ] Confirm that the fixture is synthetic, generalized, redacted, withheld, denied-state, or otherwise public-safe.
- [ ] Confirm that no exact protected-location, sensitive cultural, collection-security, private-owner, or reconstructive redaction clue is present.
- [ ] Preserve EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, rollback, and correction expectations in fixture intent when modeled.
- [ ] Keep examples compact, deterministic, public-safe, and reviewable.
- [ ] Pair every expected output with an input, test name, or generation method.
- [ ] Update this README when fixture layout, test consumers, or validation expectations change.
- [ ] Run the relevant tests, validators, sensitivity checks, and no-leak checks before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct golden payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed golden payload files in this directory during this update. |
| Public-safe sibling posture | CONFIRMED DOC | The public-safe domain fixture README defines public-safe, synthetic/generalized, fixture-only posture and exact-location denial. |
| Sensitive-domain posture | CONFIRMED DOC / RUNTIME UNKNOWN | Archaeology policy docs require exact-location and culturally sensitive material to fail closed unless reviewed policy paths allow bounded outputs. |
| Test execution | NOT RUN | No validators, pytest, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define golden fixture guidance. |
| Repository search for Archaeology golden fixtures | CONFIRMED SEARCH / NO MATCH | No confirmed golden payload file was found for this directory in this update. | Search is not a full recursive filesystem listing. |
| `../archaeology-public-safe/README.md` | CONFIRMED | Public-safe domain fixture posture, fixture-only authority boundary, exact-location denial, accepted fixture material. | It is a sibling fixture lane, not golden payload inventory. |
| `../../../../policy/domains/archaeology/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Deny-by-default policy posture, redaction/generalization/review obligations, finite policy outcomes, and release prerequisites. | Concrete policy files, tests, CI binding, and runtime enforcement remain NEEDS VERIFICATION there. |
| `../../../../docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED RULES / PROPOSED PATHS | Archaeology placement rules, sensitive-domain path posture, and lifecycle invariant. | Specific paths are marked proposed until verified. |

[Back to top](#top)
