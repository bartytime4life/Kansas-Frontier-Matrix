<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-lf-readme
title: connectors/lf/ — LANDFIRE Short-Code Compatibility Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward for LANDFIRE · Habitat steward · Flora steward · Fauna steward · Hazards steward · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; compatibility-lane; noncanonical-path; short-code-compatibility; landfire-source; rights-gated; sensitivity-gated; no-publication
proposed_path: connectors/lf/README.md
truth_posture: CONFIRMED path exists / NONCANONICAL compatibility README / CANONICAL-CANDIDATE HOME CONFIRMED AS connectors/landfire/ BY SOURCE PROFILE / OPEN-DSC-14 NEEDS ADR
related:
  - ../README.md
  - ../landfire/README.md
  - ../../docs/sources/catalog/landfire/README.md
  - ../../docs/sources/catalog/landfire/landfire.md
  - ../../docs/domains/habitat/README.md
  - ../../docs/domains/flora/README.md
  - ../../docs/domains/fauna/README.md
  - ../../docs/domains/hazards/README.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../data/registry/sources/
  - ../../fixtures/
  - ../../schemas/contracts/v1/source/
  - ../../policy/sensitivity/
  - ../../policy/rights/
  - ../../release/
tags: [kfm, connectors, lf, landfire, land-cover, vegetation, fuels, habitat, flora, fauna, hazards, compatibility, source-admission, raw, quarantine, governance]
notes:
  - "This README fills a previously blank `connectors/lf/` path."
  - "The LANDFIRE catalog README says v0.1 referenced `connectors/lf/` as a two-letter abbreviation and v0.2 corrects to `connectors/landfire/`."
  - "Both LANDFIRE placements remain beyond the nine Directory Rules §7.3 canonical connector families until OPEN-DSC-14 is resolved by ADR or migration decision."
  - "This `lf` path is therefore short-code compatibility only, not a canonical connector root."
  - "Connector output may enter RAW or QUARANTINE handoff only; downstream validation, EvidenceBundle closure, rights/sensitivity review, catalog/triplet projection, release review, publication, correction, and rollback remain outside this folder."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# LANDFIRE Short-Code Compatibility Connector Lane

> Compatibility README for the existing two-letter `connectors/lf/` path. The LANDFIRE source profile identifies this as a v0.1 short-code abbreviation and corrects v0.2 placement to `connectors/landfire/`. This path is **not** a canonical connector root.

<p>
  <img alt="Status: compatibility" src="https://img.shields.io/badge/status-compatibility-yellow">
  <img alt="Canonicality: noncanonical path" src="https://img.shields.io/badge/canonicality-noncanonical__path-orange">
  <img alt="Canonical candidate: connectors/landfire" src="https://img.shields.io/badge/canonical__candidate-connectors%2Flandfire-orange">
  <img alt="Open item: OPEN-DSC-14" src="https://img.shields.io/badge/open-OPEN--DSC--14-orange">
  <img alt="Lifecycle: RAW or QUARANTINE only" src="https://img.shields.io/badge/lifecycle-RAW%20%7C%20QUARANTINE%20only-orange">
</p>

> [!IMPORTANT]
> **Status:** compatibility / noncanonical-path README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/lf/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `NONCANONICAL` compatibility path · `CONFIRMED` LANDFIRE profile redirects v0.2 work to `connectors/landfire/` · `NEEDS VERIFICATION` final ADR disposition under OPEN-DSC-14  
> **Boundary:** source-admission compatibility only; no direct publication, no source activation, no rights/sensitivity bypass.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Admission posture](#admission-posture) · [Anti-collapse rules](#anti-collapse-rules) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/lf/` is retained here only as a short-code compatibility lane because the two-letter path already exists.

The LANDFIRE source-family README says v0.1 referenced `connectors/lf/` and v0.2 corrects the placement to `connectors/landfire/`. The same README also states that LANDFIRE is not one of the nine Directory Rules §7.3 canonical connector families and remains under OPEN-DSC-14 until ADR ratification or migration.

This path must not become a separate LANDFIRE connector root, land-cover authority store, schema root, source registry, release root, proof root, fixture dump, live harvester, public API, or publication surface.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/lf/` | Existing two-letter short-code compatibility path. | **CONFIRMED path / NONCANONICAL** |
| `connectors/landfire/` | v0.2 full-name LANDFIRE connector-family candidate. | **CONFIRMED by source profile / BEYOND §7.3 / OPEN-DSC-14** |
| `docs/sources/catalog/landfire/README.md` | LANDFIRE source-family catalog README. | **CONFIRMED** |
| `docs/sources/catalog/landfire/landfire.md` | LANDFIRE product/profile detail. | **NEEDS VERIFICATION in this response** |
| `data/registry/sources/` | SourceDescriptor authority. | **Outside connector / NEEDS VERIFICATION for entries** |
| `fixtures/` | Candidate fixture root. | **NEEDS VERIFICATION** |
| `policy/rights/` and `policy/sensitivity/` | Rights and sensitivity authority. | **Outside connector** |
| `release/` | Release and publication controls. | **Out of scope for this compatibility lane** |

[Back to top ↑](#top)

---

## Accepted inputs

Accepted content for this noncanonical compatibility path:

- README-level migration and compatibility notes;
- links to the fuller `connectors/landfire/` path;
- notes that prevent the `lf` abbreviation from becoming a parallel authority;
- temporary fixture or test notes only if explicitly migration-bound;
- adapter notes for LANDFIRE source metadata only if retained here by ADR or migration note;
- quarantine criteria for unresolved rights, source role, product identity, classification vocabulary, raster/vector form, version, geometry, endpoint/access method, or source-shape issues.

New implementation code should prefer `connectors/landfire/` unless an ADR says otherwise.

---

## Exclusions

This folder must not contain or imply authority over:

- canonical connector-family status;
- public release decisions;
- direct writes to processed, catalog, triplet, published, proof, receipt, or release stores;
- SourceDescriptor authority records;
- policy or schema authority;
- generated summaries presented as authoritative land-cover, vegetation, habitat, fuel, or disturbance truth;
- source activation without SourceDescriptor, rights, sensitivity, source-role, provenance, and review checks.

Redirect implementation and source-family authority to `connectors/landfire/` once verified and accepted by ADR or migration decision.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/lf/README.md` | **CONFIRMED** | Target file existed and was blank before this update. | Does not prove implementation files, tests, or CI. |
| `docs/sources/catalog/landfire/README.md` | **CONFIRMED** | Source profile says `connectors/lf/` was a v0.1 two-letter abbreviation and v0.2 corrects to `connectors/landfire/`; it also says LANDFIRE remains beyond §7.3 until OPEN-DSC-14 is resolved. | Does not prove endpoint availability, rights clearance, activation, or implementation. |
| `connectors/landfire/` | **NEEDS VERIFICATION** | Named as v0.2 corrected placement by source profile. | Actual files, code, fixtures, tests, and CI remain unverified here. |

---

## Admission posture

Expected behavior for LANDFIRE source-admission work routed through this compatibility path:

- no live source access unless explicitly enabled and reviewed;
- no source fetch without an accepted SourceDescriptor and activation decision;
- no implicit publication from retrieved source material;
- no collapse of LANDFIRE products with CDL, NLCD, GAP, USNVC crosswalks, or generated summaries;
- preserve source ID, source URI, product identity, product version, classification vocabulary, raster/vector form, thematic role, geometry/uncertainty, license/rights, review state, and release-class metadata;
- unresolved rights, sensitivity, source role, product identity, classification, version, geometry, endpoint, freshness, or schema drift routes to quarantine or abstention.

---

## Anti-collapse rules

The LANDFIRE short-code compatibility lane must preserve the following controls:

1. `connectors/lf/` is compatibility-only unless an ADR says otherwise.
2. v0.2 LANDFIRE work points to `connectors/landfire/`, pending OPEN-DSC-14 resolution.
3. `landfire/` itself remains beyond the nine canonical §7.3 connector families until ratified or migrated.
4. LANDFIRE native classifications must be preserved; crosswalks are advisory unless a later governed contract says otherwise.
5. LANDFIRE source products must be admitted per SourceDescriptor and source role.
6. Public release is a governed state transition, not a connector output.
7. Derived summaries, maps, tiles, joins, analyses, and AI explanations are downstream carriers, not sovereign truth.

---

## Validation

Compatibility-lane validation should check that:

- this path is not treated as canonical without ADR/migration evidence;
- SourceDescriptor references are required for activation;
- product identity, product version, classification vocabulary, geometry, source URI, rights, sensitivity, and source vintage are explicit where available;
- LANDFIRE material remains distinct from peer land-cover source families and crosswalk outputs;
- malformed or incomplete records fail closed;
- records with unresolved rights, sensitivity state, source role, product identity, classification, version, geometry, freshness, or access method route to quarantine;
- connector output is limited to RAW or QUARANTINE handoff;
- no connector run writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level validation, policy-as-code, EvidenceBundle closure, release review, public caveats, and rollback remain outside this compatibility lane.

[Back to top ↑](#top)

---

## Rollback

Rollback is required if this README is used to justify canonical-family status, direct publication, source activation, source-role collapse, rights/sensitivity bypass, or direct writes beyond RAW/QUARANTINE handoff.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the file was blank before this update, a safe rollback is to restore the blank placeholder or replace this document with a shorter redirect-only README until canonical placement is resolved.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual `connectors/landfire/` implementation files. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Resolve OPEN-DSC-14 for LANDFIRE family placement. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm whether this two-letter `lf` path should remain. | **NEEDS VERIFICATION** | ADR or migration decision. |
| Confirm SourceDescriptor homes and LANDFIRE product IDs. | **NEEDS VERIFICATION** | Source registry entries and accepted schemas. |
| Confirm current access methods, product versions, and terms. | **NEEDS VERIFICATION** | Source steward review and current source documentation. |
| Confirm rights and sensitivity handling. | **NEEDS VERIFICATION** | Rights review, sensitivity review, and policy references. |
| Confirm fixture strategy and CI wiring. | **NEEDS VERIFICATION** | Fixture registry, workflow files, and test logs. |

---

## Maintainer note

Do not build new authority here. This existing two-letter path should either stay a clear compatibility pointer or be removed after migration. Implementation should converge under `connectors/landfire/` unless an ADR says otherwise.

[Back to top ↑](#top)
