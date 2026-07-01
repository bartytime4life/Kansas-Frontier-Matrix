<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixture/domains/archaeology-public-safe/readme
title: Archaeology public-safe domain fixtures README
type: fixture-readme
version: v0.1.0
status: draft
owners: TODO(owner): archaeology domain steward; TODO(owner): fixture steward; TODO(owner): cultural-review reviewer; TODO(owner): sensitivity reviewer; TODO(owner): policy steward; TODO(owner): release steward; TODO(owner): docs steward
created: NEEDS VERIFICATION - blank file existed before 2026-07-01 expansion
updated: 2026-07-01
policy_label: restricted-review
related:
  - ../../archaeology-public-safe/README.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/CANONICAL_PATHS.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../policy/domains/archaeology/README.md
  - ../../../contracts/domains/archaeology/
  - ../../../schemas/contracts/v1/domains/archaeology/
  - ../../../tests/domains/archaeology/
  - ../../../data/published/layers/archaeology/
  - ../../../release/candidates/archaeology/
  - ../../../docs/doctrine/directory-rules.md
tags: [kfm, fixtures, domains, archaeology, public-safe, synthetic-fixtures, generalized-fixtures, exact-location-denial, deny-by-default, cultural-review, sensitivity-review, redaction, release-gated, non-authoritative]
notes:
  - "This README replaces a blank file at `fixtures/domains/archaeology-public-safe/README.md`."
  - "A root-level `fixtures/archaeology-public-safe/README.md` already exists and is treated here as the sibling legacy/runtime fixture lane; this file must not create a parallel source of authority."
  - "This directory is for public-safe, synthetic or generalized Archaeology domain fixtures only, not source data, exact site data, policy authority, release authority, or published-layer authority."
  - "Archaeology exact site geometry, sacred/burial context, human-remains context, collection-security detail, looting-risk exposure, unresolved cultural sensitivity, and private-owner detail fail closed and must not be placed in this fixture lane."
  - "No tests, validators, cultural-review checks, sensitivity checks, policy checks, release checks, or CI jobs were run during this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology public-safe domain fixtures

Domain-facing public-safe fixture lane under `fixtures/domains/archaeology-public-safe/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: fixtures" src="https://img.shields.io/badge/root-fixtures%2F-6f42c1">
  <img alt="Domain: archaeology" src="https://img.shields.io/badge/domain-archaeology-6e2a8a">
  <img alt="Posture: public safe only" src="https://img.shields.io/badge/posture-public--safe--only-blue">
  <img alt="Default: deny exact location" src="https://img.shields.io/badge/default-deny__exact__location-critical">
  <img alt="Authority: fixture only" src="https://img.shields.io/badge/authority-fixture%20only-critical">
</p>

**Path:** `fixtures/domains/archaeology-public-safe/README.md`  
**Fixture posture:** public-safe, synthetic/generalized, non-truth, non-release Archaeology domain fixture lane  
**Authority posture:** fixture only; Archaeology doctrine, source truth, policy authority, sensitivity authority, cultural review, lifecycle promotion, release approval, published-layer authority, and public-client permission remain in their owning roots  
**Quick links:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Relationship to existing fixture lane](#relationship-to-existing-fixture-lane) · [Accepted fixture material](#accepted-fixture-material) · [Exclusions](#exclusions) · [Authority boundary](#authority-boundary) · [Expected layout](#expected-layout) · [Maintenance checklist](#maintenance-checklist) · [Status notes](#status-notes) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> Files under this directory are fixtures. They are not source data, RAW captures, WORK candidates, QUARANTINE holds, PROCESSED records, catalog records, triplets, EvidenceBundles, proof packs, receipts, policy decisions, release decisions, published Archaeology layers, governed API responses, public map payloads, or archaeological truth.

> [!CAUTION]
> This is a sensitive-domain fixture lane. Do not place exact archaeological site geometry, burial/sacred-site detail, human-remains context, collection-security detail, looting-risk exposure, unresolved cultural sensitivity, private-owner detail, or reconstructive redaction clues here. Use synthetic, generalized, redacted, clipped, aggregated, withheld, or denied-state examples only.

---

## Purpose

This directory is for public-safe Archaeology domain fixtures that exercise UI, renderer, validator, policy-helper, generalization, redaction, no-leak, or release-precheck behavior without exposing sensitive or authoritative archaeological data.

A passing fixture proves only the bounded test expectation attached to that fixture. It does not prove a site exists, a candidate is confirmed, a cultural review was completed, a policy decision was issued, a layer was released, or a public answer may be shown.

---

## Placement basis

The requested path exists under `fixtures/domains/`, which is a fixture responsibility root with a domain-facing segment. Archaeology canonical path guidance says the placement rules are confirmed but specific paths are proposed until verified, and it repeats the core lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This README documents the observed target path as a fixture lane only. It does not decide whether this path should replace, mirror, or supersede the existing root-level public-safe fixture lane. Any future consolidation should be handled as a documented migration or ADR-backed cleanup, not by silent drift.

---

## Relationship to existing fixture lane

A root-level fixture lane already exists at:

```text
fixtures/archaeology-public-safe/
```

That README defines a runtime fixture lane for synthetic, generalized, public-safe Archaeology map/viewer corpora. This `fixtures/domains/archaeology-public-safe/` README must be treated as a **domain-facing companion** unless maintainers later choose a single canonical fixture home.

| Lane | Current posture | This README relationship |
|---|---|---|
| `fixtures/archaeology-public-safe/` | Existing public-safe runtime fixture lane. | Sibling / compatibility lane; not superseded here. |
| `fixtures/domains/archaeology-public-safe/` | Requested domain-facing fixture lane. | Documents domain fixture posture; must not create parallel release or source authority. |

Do not duplicate fixture payloads across both lanes without a migration note, source checksum, purpose statement, and rollback path.

---

## Accepted fixture material

Accepted material must be synthetic or demonstrably public-safe, generalized, reproducible, and small enough for repository review.

| Accepted item | Use | Required posture |
|---|---|---|
| Synthetic generalized features | Renderer, style, legend, hover, selection, or smoke tests. | Non-authoritative; no exact real locations. |
| Generalized-grid fixtures | Public-safe generalized layer tests. | Declare cell or region generalization method. |
| Candidate-state fixtures | Candidate-not-confirmed UI and policy states. | Must not imply confirmed site status. |
| Withheld/denied-state fixtures | No-leak, disabled, denied, redacted, or withheld viewer states. | Include safe reason code and no sensitive payload. |
| Redaction/generalization examples | Test shape of transform metadata. | Must be synthetic or fully safe; not a real receipt. |
| Release-precheck examples | Exercise missing/required release fields. | Must not claim approval or publishability. |
| Fixture manifest | Documents generation method, non-authority, and intended test. | Must state fixture-only and non-release-approved. |

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
| Public-safe Archaeology domain fixtures | `fixtures/domains/archaeology-public-safe/` | Documents fixture-only examples. |
| Existing public-safe runtime fixtures | `fixtures/archaeology-public-safe/` | Referenced sibling lane; not replaced here. |
| Archaeology domain doctrine | `docs/domains/archaeology/` | Referenced, not replaced. |
| Archaeology policy | `policy/domains/archaeology/` and related policy roots | Out of scope; fixtures may test policy helpers but do not define policy. |
| Archaeology contracts and schemas | `contracts/domains/archaeology/`, `schemas/contracts/v1/domains/archaeology/` | Referenced, not duplicated. |
| Cultural/sensitivity review | Steward and reviewer workflows, receipts, policy decisions | Out of scope; fixture text cannot substitute for review. |
| Lifecycle data | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplet/`, `data/published/` | Out of scope. |
| Release authority | `release/` roots | Out of scope. |
| Published public-safe layers | `data/published/layers/archaeology/` | Out of scope. |
| Tests and validation proof | `tests/domains/archaeology/` and validator tooling | Referenced, not claimed as run. |

Do not collapse this fixture lane into archaeology truth, source authority, policy authority, sensitivity authority, cultural-review authority, release authority, EvidenceBundle authority, or public-client permission.

---

## Expected layout

Use compact, inspectable fixture cases:

```text
fixtures/domains/archaeology-public-safe/
  README.md
  <case_name>.input.json
  <case_name>.expected.json
  <case_name>.snapshot.json
```

For schema-style examples, use:

```text
fixtures/domains/archaeology-public-safe/
  valid/
    README.md
    valid_<n>.json
  invalid/
    README.md
    invalid_<n>.json
    invalid_<n>.expected_error.txt
```

For renderer/runtime fixtures, include a local manifest that states fixture generation method, public-safe transformation, non-authority, intended consumer, and rollback/deletion path.

---

## Maintenance checklist

Before adding or changing fixtures here:

- [ ] Confirm the consuming test, validator, renderer, policy helper, redaction helper, generalization helper, release precheck, or no-leak check.
- [ ] Confirm that the fixture is synthetic, generalized, redacted, withheld, or denied-state only.
- [ ] Confirm that no exact protected-location, sensitive cultural, collection-security, private-owner, or reconstructive redaction clue is present.
- [ ] Preserve EvidenceBundle, PolicyDecision, ReviewRecord, RedactionReceipt, ReleaseManifest, rollback, and correction expectations in fixture intent when modeled.
- [ ] Keep examples compact, deterministic, public-safe, and reviewable.
- [ ] Avoid duplicating root-level `fixtures/archaeology-public-safe/` payloads unless a migration note explains why.
- [ ] Update this README and any sibling lane README when fixture layout changes.
- [ ] Run the relevant tests, validators, sensitivity checks, and no-leak checks before claiming validation success.

---

## Status notes

| Item | Status | Notes |
|---|---:|---|
| Target README | CONFIRMED UPDATED | This path existed as a blank file before this update. |
| Existing sibling lane | CONFIRMED | `fixtures/archaeology-public-safe/README.md` exists and defines a public-safe runtime fixture lane. |
| Payload inventory | NEEDS VERIFICATION | No payload files under this target lane were fetched or validated during this update. |
| Placement | CONFIRMED PATH / NEEDS STEWARD REVIEW | The requested path exists; relationship to the existing root-level fixture lane should be settled by maintainers if both carry payloads. |
| Sensitive-domain posture | CONFIRMED DOC / RUNTIME UNKNOWN | Archaeology publication and policy docs require deny-by-default and reviewed redaction/generalization for public surfaces; runtime enforcement was not tested. |
| Test execution | NOT RUN | No validators, sensitivity checks, cultural-review checks, policy checks, release checks, no-leak checks, or CI were run during this README update. |

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | Target existed as a blank file. | Did not define fixture guidance. |
| Repository search for archaeology public-safe fixtures | CONFIRMED SEARCH | Found the existing root-level public-safe fixture lane and Archaeology policy/publication docs. | Search is not a full recursive filesystem listing. |
| `../../archaeology-public-safe/README.md` | CONFIRMED | Existing public-safe fixture lane, exclusions, fixture-only posture, and exact-location denial. | Does not decide whether the new `fixtures/domains/` lane should become canonical. |
| `../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md` | CONFIRMED DOC | Deny-by-default sensitive-domain posture, release separation of duties, evidence/policy/review/release chain, and public-surface limits. | Draft governance reference; machine-readable release artifacts still govern actual decisions. |
| `../../../docs/domains/archaeology/CANONICAL_PATHS.md` | CONFIRMED RULES / PROPOSED PATHS | Archaeology placement rules, sensitive-domain path posture, and lifecycle invariant. | Specific paths are marked proposed until verified. |
| `../../../policy/domains/archaeology/README.md` | CONFIRMED DOC / RUNTIME UNKNOWN | Policy lane scope for deny-by-default, redaction, sovereignty, release, rollback, and review obligations. | Concrete policy files, tests, CI binding, and runtime enforcement remain NEEDS VERIFICATION there. |

[Back to top](#top)
