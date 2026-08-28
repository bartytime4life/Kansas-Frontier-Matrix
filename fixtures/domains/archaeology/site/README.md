<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology/site/readme
title: Archaeology site fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): archaeology domain steward; TODO(owner): fixture steward; TODO(owner): validation steward; TODO(owner): cultural-review reviewer; TODO(owner): sensitivity reviewer; TODO(owner): policy steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: restricted-review
related:
  - ../golden/README.md
  - ../invalid/README.md
  - ../archaeology-public-safe/README.md
  - ../../archaeology-public-safe/README.md
  - ../../../../contracts/domains/archaeology/archaeological_site.md
  - ../../../../contracts/domains/archaeology/candidate_feature.md
  - ../../../../docs/domains/archaeology/OBJECT_FAMILIES.md
  - ../../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../policy/domains/archaeology/README.md
  - ../../../../schemas/contracts/v1/domains/archaeology/
  - ../../../../tests/domains/archaeology/
  - ../../../../release/candidates/archaeology/
  - ../../../../data/published/layers/archaeology/
  - ../../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, archaeology, site-fixtures, archaeological-site, candidate-feature, public-safe, synthetic-fixtures, exact-location-denial, deny-by-default, no-leak, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/archaeology/site/README.md`."
  - "This directory is for safe site-shaped Archaeology fixtures only, not real site records, source data, exact-location data, policy authority, cultural-review authority, release authority, or published-layer authority."
  - "Repo evidence confirms `ArchaeologicalSite` and `CandidateFeature` contracts exist; both preserve publication and exact-detail boundaries."
  - "No direct fixture payloads were found or inspected in this directory during this update, so payload inventory remains NEEDS VERIFICATION."
  - "No tests, validators, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology site fixtures

Site-shaped fixture lane for safe Archaeology examples under `fixtures/domains/archaeology/site/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Lane: site" src="https://img.shields.io/badge/lane-site-blue">
  <img alt="Default: deny exact location" src="https://img.shields.io/badge/default-deny__exact__location-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/archaeology/site/README.md`  
**Fixture posture:** safe, synthetic/generalized site-shaped fixtures for bounded Archaeology tests  
**Authority posture:** fixture only; archaeology truth, source truth, sensitivity authority, cultural review, policy authority, lifecycle promotion, release approval, published-layer authority, and public-client permission remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Site boundary](#site-boundary) · [Accepted site fixture material](#accepted-site-fixture-material) · [Exclusions](#exclusions) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are site-shaped fixtures. They are not real `ArchaeologicalSite` records, candidate confirmations, source data, EvidenceBundles, proof packs, receipts, PolicyDecisions, ReviewRecords, RedactionReceipts, ReleaseManifests, published Archaeology layers, governed API responses, public map payloads, or archaeological truth.

> [!CAUTION]
> Do not place exact protected-location geometry, sensitive cultural context, collection-security detail, private-owner detail, or reconstructive redaction clues here. Site fixtures must use synthetic identifiers, synthetic or coarse generalized geometry, withheld-state payloads, denied-state payloads, or expected-output examples only.

---

## Purpose

This directory is for Archaeology site-shaped fixtures.

Use this lane when tests, validators, renderers, policy helpers, no-leak checks, redaction/generalization helpers, release-precheck helpers, or API-envelope checks need site-like examples without reading or storing real site records.

A passing fixture proves only the bounded test expectation attached to that fixture. It does not prove a site exists, a candidate is confirmed, a cultural review was completed, a policy decision was issued, a release was approved, or a public answer may be shown.

---

## Placement basis

The requested path exists under `fixtures/domains/archaeology/`, which is a domain-facing fixture segment inside the `fixtures/` responsibility root. Archaeology canonical path guidance treats placement rules as confirmed while specific paths remain proposed until verified, and it carries the lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Site fixtures sit outside that lifecycle. They may model expected shape or public-safe behavior, but they do not promote, release, prove, or publish Archaeology material.

---

## Site boundary

`ArchaeologicalSite` is the core reviewed site-identity object in the Archaeology lane, but this fixture directory is not a site registry and must not behave like one.

| Boundary | Fixture consequence |
|---|---|
| `ArchaeologicalSite` is reviewed site identity | Site-shaped fixtures may model fields or responses, but they do not assert a real site exists. |
| `CandidateFeature` is not a confirmed site | Candidate-like fixtures must keep candidate status visible and must not silently promote to site. |
| Exact detail is denied by default | Public-safe site fixtures should use synthetic or generalized geometry and denied/withheld states. |
| Review and policy remain external | Fixture success cannot substitute for `ReviewRecord`, `PolicyDecision`, or cultural/sensitivity review. |
| Release remains external | Fixture success cannot substitute for `ReleaseManifest`, rollback path, signature, or publication decision. |

---

## Accepted site fixture material

Accepted material must be synthetic or demonstrably public-safe, generalized, reproducible, and small enough for repository review.

| Material | Use |
|---|---|
| `*.input.json` | Synthetic site-shaped request or helper input. |
| `*.expected.json` | Expected public-safe output for deterministic tests. |
| `*.snapshot.json` | Snapshot-style viewer, API, policy-helper, or redaction/generalization output. |
| `valid/valid_<n>.json` | Positive schema or helper fixture when a safe site-shaped case is expected to pass. |
| `invalid/invalid_<n>.json` | Negative fixture for missing review, missing policy, attempted exact detail, candidate/site confusion, or unsafe public output. |
| `invalid/invalid_<n>.expected_error.txt` | Expected error text, reason code, or reason pattern. |
| local README files | Fixture intent, generation method, test consumer, and authority-boundary documentation. |

Good site fixture cases include synthetic generalized site summaries, candidate-not-confirmed responses, denied exact-detail requests, redacted site-card previews, withheld evidence-drawer states, and release-precheck examples with missing review or rollback fields.

---

## Exclusions

Do not place any of the following in this lane:

| Excluded material | Correct action or home |
|---|---|
| Real restricted records, precise protected locations, sensitive cultural context, collection-security detail, or private-owner detail | Deny, restrict, quarantine, or handle in governed restricted storage after review. |
| Real site inventories, survey forms, excavation/provenience records, or curation records | Governed lifecycle or restricted storage, not fixtures. |
| Lifecycle artifacts | `data/<phase>/archaeology/` under lifecycle rules. |
| EvidenceBundles, proof packs, validation reports, or receipts | Their verified proof/receipt homes. |
| Release manifests, promotion decisions, correction notices, rollback cards, signatures, or release changelog entries | `release/` roots. |
| Policy rules, schemas, contracts, validators, tests, app code, package code, or pipeline logic | Their canonical responsibility roots. |
| Published map layers, public API payloads, or public downloads | Governed published-data roots after release gates close. |

---

## Authority boundary

| Responsibility | Owning root | This README posture |
|---|---|---|
| Archaeology site fixtures | `fixtures/domains/archaeology/site/` | Documents safe site-shaped test examples only. |
| ArchaeologicalSite semantic contract | `contracts/domains/archaeology/archaeological_site.md` | Referenced, not replaced. |
| CandidateFeature semantic contract | `contracts/domains/archaeology/candidate_feature.md` | Referenced, not replaced. |
| Public-safe Archaeology fixtures | `fixtures/domains/archaeology-public-safe/` and `fixtures/archaeology-public-safe/` | Referenced for public-safe fixture posture. |
| Archaeology domain doctrine | `docs/domains/archaeology/` | Referenced, not replaced. |
| Archaeology schemas | `schemas/contracts/v1/domains/archaeology/` | Referenced, not duplicated. |
| Archaeology policy | `policy/domains/archaeology/` and related policy roots | Out of scope; fixtures may test policy helpers but do not define policy. |
| Cultural/sensitivity review | Reviewer workflows, receipts, policy decisions, release records | Out of scope; fixture success cannot substitute for review. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Release authority | `release/` roots | Out of scope. |
| Tests and validation proof | `tests/domains/archaeology/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into archaeology truth, site registry authority, source authority, EvidenceBundle authority, policy authority, sensitivity authority, cultural-review authority, release authority, or public-client permission.

---

## Expected layout

Use paired input and expected-output cases:

```text
fixtures/domains/archaeology/site/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
```

For schema-style examples:

```text
fixtures/domains/archaeology/site/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For grouped site behavior cases:

```text
fixtures/domains/archaeology/site/
  candidate_not_confirmed/
    README.md
    request.input.json
    response.expected.json
  denied_exact_detail/
    README.md
    request.input.json
    response.expected.json
```

---

## Maintenance checklist

Before adding or changing Archaeology site fixtures:

- [ ] Confirm the consuming test, validator, renderer, policy helper, redaction helper, generalization helper, release precheck, or no-leak check.
- [ ] Confirm that the fixture is synthetic, generalized, redacted, withheld, denied-state, or otherwise public-safe.
- [ ] Confirm that no exact protected-location, sensitive cultural, collection-security, private-owner, or reconstructive redaction clue is present.
- [ ] Keep candidate and confirmed-site semantics separate.
- [ ] Preserve EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, rollback, and correction expectations in fixture intent when modeled.
- [ ] Keep examples compact, deterministic, public-safe, and reviewable.
- [ ] Pair every expected output with an input, test name, or generation method.
- [ ] Run the relevant tests, validators, sensitivity checks, and no-leak checks before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Direct payload inventory | NEEDS VERIFICATION | Repo search did not surface confirmed payload files in this directory during this update. |
| ArchaeologicalSite contract | CONFIRMED DOC / VALIDATOR UNKNOWN | Contract exists and defines object meaning but does not authorize publication, policy approval, or access to restricted detail. |
| CandidateFeature contract | CONFIRMED DOC / VALIDATOR UNKNOWN | Contract exists and preserves candidate-vs-confirmed boundary. |
| Sensitive-domain posture | CONFIRMED DOC / RUNTIME UNKNOWN | Archaeology object-family and policy docs require exact-detail exposure to fail closed unless reviewed policy paths allow bounded outputs. |
| Test execution | NOT RUN | No validators, pytest, cultural-review checks, sensitivity checks, policy checks, release checks, no-leak checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define site fixture guidance. |
| Repository search for Archaeology site fixtures | CONFIRMED SEARCH | Found Archaeology contracts and docs related to site, candidate, publication, policy, and object families. | Search is not a full recursive filesystem listing. |
| `../../../../docs/domains/archaeology/OBJECT_FAMILIES.md` | CONFIRMED DOC | `ArchaeologicalSite` object-family purpose, default T4 posture, candidate/object-family context, and review/release boundaries. | Governance register, not schema, validator, or fixture inventory. |
| `../../../../contracts/domains/archaeology/archaeological_site.md` | CONFIRMED DOC / VALIDATOR UNKNOWN | `ArchaeologicalSite` meaning and explicit non-authorization for publication, policy approval, proof closure, release, rendering, or restricted-detail access. | Contract does not prove fixtures or runtime behavior exist. |
| `../../../../contracts/domains/archaeology/candidate_feature.md` | CONFIRMED DOC / VALIDATOR UNKNOWN | Candidate-vs-confirmed boundary and exclusion from public layer/release/evidence/policy authority. | Contract does not prove fixtures or runtime behavior exist. |
| `../../../../policy/domains/archaeology/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Deny-by-default policy posture and reviewed bounded-output requirements. | Concrete policy files, tests, CI binding, and runtime enforcement remain NEEDS VERIFICATION there. |

[Back to top](#top)
