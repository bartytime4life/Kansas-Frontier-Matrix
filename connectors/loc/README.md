<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-loc-readme
title: connectors/loc/ — Library of Congress Connector Family Candidate
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for LOC · Archives steward · People-DNA-Land steward · Genealogy steward · Rights reviewer · Sensitivity reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; connector-family-candidate; beyond-directory-rules-7-3; open-dsc-14; loc-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/loc/README.md
truth_posture: CONFIRMED path exists / PROPOSED beyond §7.3 connector family / OPEN-DSC-14 NEEDS ADR
related:
  - ../README.md
  - ../../docs/sources/catalog/loc/README.md
  - ../../docs/sources/catalog/loc/loc-iiif-presentations.md
  - ../../docs/sources/catalog/loc/loc-historic-maps.md
  - ../../docs/sources/catalog/loc/lcnaf-name-authority.md
  - ../../docs/sources/catalog/loc/lcsh-subject-headings.md
  - ../../docs/sources/catalog/loc/chronicling-america.md
  - ../../docs/domains/archaeology/README.md
  - ../../docs/domains/people-dna-land/README.md
  - ../../docs/domains/genealogy/README.md
  - ../../docs/domains/settlements/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../policy/sources/
  - ../../release/
tags: [kfm, connectors, loc, library-of-congress, lcnaf, lcsh, iiif, chronicling-america, maps, archives, linked-data, source-admission, open-dsc-14, raw, quarantine, governance]
notes:
  - "This README replaces the greenfield stub in `connectors/loc/`."
  - "The LOC catalog README says `connectors/loc/` is proposed beyond Directory Rules §7.3 and awaits OPEN-DSC-14 ADR ratification."
  - "LOC has multiple source surfaces: LCNAF, LCSH, IIIF presentations, historic maps, Chronicling America, and id.loc.gov-linked data."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Library of Congress Connector Family Candidate

> Connector-family candidate README for `connectors/loc/`. The LOC source catalog confirms this path is **proposed beyond the nine Directory Rules §7.3 canonical connector families** and remains subject to `OPEN-DSC-14` ADR or migration decision. This README documents boundaries for source-admission work only; it does not ratify `loc/` as canonical infrastructure.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family status: beyond §7.3" src="https://img.shields.io/badge/family-beyond__%C2%A77.3-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Rights: mixed" src="https://img.shields.io/badge/rights-mixed%20fail--closed-critical">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** `draft` connector-family candidate · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/loc/README.md`  
> **Truth posture:** `CONFIRMED` path exists · `PROPOSED` beyond §7.3 family · `NEEDS VERIFICATION` final ADR disposition under `OPEN-DSC-14`  
> **Boundary:** source-admission only; no source activation, no direct publication, no rights/sensitivity bypass, no canonical-family claim.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/loc/` is a proposed Library of Congress connector-family candidate.

The LOC source catalog says `loc/` is not one of the nine Directory Rules §7.3 canonical connector families. The folder is scaffolded because KFM doctrine expects distinct LOC source surfaces, including LCNAF, LCSH, IIIF presentations, historic maps, Chronicling America, and id.loc.gov-linked data. Final family placement remains pending under `OPEN-DSC-14`.

This path must not become a canonical connector-family root, public source service, schema root, source registry, proof root, release root, fixture dump, or publication surface without ADR or migration evidence.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/loc/` | LOC connector-family candidate. | **CONFIRMED path / PROPOSED beyond §7.3** |
| `docs/sources/catalog/loc/README.md` | LOC source-family catalog README. | **CONFIRMED** |
| `docs/sources/catalog/loc/loc-iiif-presentations.md` | LOC IIIF product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/loc-historic-maps.md` | LOC historic maps product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/lcnaf-name-authority.md` | LCNAF authority product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/lcsh-subject-headings.md` | LCSH product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `docs/sources/catalog/loc/chronicling-america.md` | Chronicling America product/source page. | **CONFIRMED search result / NEEDS FILE REVIEW** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION** |
| `policy/rights/`, `policy/sensitivity/`, `policy/sources/` | Rights, sensitivity, and source policy authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this connector candidate** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this connector-family candidate:

- README-level connector-family orientation;
- source-admission helper notes for LOC sub-sources;
- links to per-sub-source catalog pages;
- migration notes for `OPEN-DSC-14`;
- fixture and test notes only if fixture-safe and explicitly bounded;
- quarantine criteria for unresolved rights, source role, source URI, manifest hash, OCR quality, georeferencing uncertainty, identity authority status, or source-shape issues.

Implementation must require SourceDescriptor and activation gates before any live source access or promotion-track handoff.

---

## Exclusions

This folder must not contain or imply authority over:

- final canonical connector-family status;
- SourceDescriptor authority records;
- policy or schema authority;
- public release decisions;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- generated summaries presented as authoritative archival, identity, map, OCR, or linked-data truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, provenance, and review checks.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/loc/README.md` | **CONFIRMED** | Target file existed as a greenfield stub before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/loc/README.md` | **CONFIRMED** | LOC catalog README says `connectors/loc/` is proposed beyond §7.3 and awaits `OPEN-DSC-14`; it lists LOC sub-sources and admission concerns. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| LOC per-sub-source catalog pages | **CONFIRMED search results / NEEDS FILE REVIEW** | Search found IIIF, maps, LCNAF, LCSH, and Chronicling America pages. | This README did not inspect each file body. |
| Actual connector code under `connectors/loc/` | **NEEDS VERIFICATION** | This README defines expected boundaries. | Actual modules, tests, fixtures, and CI remain unverified. |

---

## Admission posture

Expected behavior for LOC source-admission work:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- preserve source ID, source URI, source role, product/surface identity, rights statement, retrieval timestamp, manifest hash or equivalent source fingerprint, provenance, review state, and release-class metadata;
- preserve uncertainty metadata for OCR, georeferencing, identity matching, and linked-data crosswalks where applicable;
- unresolved rights, sensitivity, source role, source identity, provenance, OCR quality, georeferencing uncertainty, endpoint, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The LOC connector-family candidate must preserve the following controls:

1. `connectors/loc/` remains proposed beyond §7.3 until `OPEN-DSC-14` is resolved.
2. LOC sub-sources must remain distinct: LCNAF, LCSH, IIIF, maps, Chronicling America, and id.loc.gov-linked data are not interchangeable.
3. Identity authority data, subject authority data, OCR text, images, maps, manifests, and georeferencing annotations require different source roles and validation gates.
4. Rights and sensitivity states must be carried forward from the source record and reviewed before promotion.
5. Public release is a governed state transition, not a connector output.
6. Derived summaries, maps, tiles, joins, NER output, authority links, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- SourceDescriptor references are required for activation;
- LOC sub-source identity is explicit;
- source role, source URI, rights, sensitivity, provenance, and retrieval timestamp are explicit where available;
- source fingerprints such as manifest hashes are preserved where applicable;
- OCR, identity matching, linked-data crosswalks, and georeferencing uncertainty do not silently become authoritative claims;
- malformed or incomplete records fail closed;
- unresolved rights, sensitivity state, source role, uncertainty, provenance, freshness, or access method routes to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this connector candidate.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, rights/sensitivity bypass, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

A safe rollback is to restore the prior greenfield stub or replace this document with a shorter candidate-family note until `OPEN-DSC-14` is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Resolve `OPEN-DSC-14` for LOC connector-family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm actual connector code under `connectors/loc/`. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm per-sub-source connector modules or lanes. | **NEEDS VERIFICATION** | Repo tree, package docs, and tests. |
| Confirm SourceDescriptor homes and LOC sub-source IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Keep `connectors/loc/` narrow until the ADR is resolved. It may organize LOC source-admission code and compatibility documentation, but it must not become canonical infrastructure by drift.

[Back to top ↑](#top)
