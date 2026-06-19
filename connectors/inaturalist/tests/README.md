<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-inaturalist-tests-readme
title: connectors/inaturalist/tests/ — iNaturalist Connector Test Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Test steward · Source steward · Fauna steward · Flora steward · Sensitivity reviewer · Rights reviewer · Validation steward · Docs steward
created: 2026-06-19
updated: 2026-06-19
policy_label: public-doctrine; test-fixtures-only; no-live-network-by-default; no-publication
proposed_path: connectors/inaturalist/tests/README.md
truth_posture: CONFIRMED path exists / PROPOSED test-lane contract / IMPLEMENTATION DEPTH NEEDS VERIFICATION
related:
  - ../README.md
  - ../../../docs/sources/catalog/inaturalist/README.md
  - ../../../docs/sources/catalog/gbif/README.md
  - ../../../docs/sources/catalog/idigbio/README.md
  - ../../../docs/domains/fauna/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../fixtures/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/biodiversity/
  - ../../../policy/sensitivity/
  - ../../../policy/rights/
  - ../../../release/
tags: [kfm, connectors, inaturalist, tests, fixtures, no-network, biodiversity, rights, geoprivacy, source-admission, validation, governance]
notes:
  - "This README replaces a thin greenfield test stub with a governed test-lane README."
  - "The parent connector README and iNaturalist source profile require no activation without SourceDescriptor, per-record rights checks, geoprivacy handling, and source-role discipline."
  - "Tests must prove connector behavior fails closed and cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores."
  - "Fixture data must be synthetic, minimized, redacted, generalized, or explicitly approved for committed use."
  - "Actual test files, fixture inventory, CI wiring, endpoint mocks, and current passing status remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# iNaturalist Connector Tests

> Test-lane README for `connectors/inaturalist/`. These tests should prove the connector remains source-admission only, no-network by default, rights-gated, geoprivacy-aware, and unable to publish.

<p>
  <img alt="Status: experimental" src="https://img.shields.io/badge/status-experimental-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Fixtures: safe only" src="https://img.shields.io/badge/fixtures-safe__only-orange">
  <img alt="Lifecycle: test source admission only" src="https://img.shields.io/badge/lifecycle-source__admission__tests-blue">
</p>

> [!IMPORTANT]
> **Status:** `experimental` test README · **Owner:** `OWNER_TBD`  
> **Path:** `connectors/inaturalist/tests/README.md`  
> **Truth posture:** `CONFIRMED` file exists · `PROPOSED` test-lane contract · `NEEDS VERIFICATION` actual test coverage  
> **Boundary:** tests verify connector admission behavior only; tests must not require live network, secret credentials, or public release paths.

**Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [Accepted inputs](#accepted-inputs) · [Exclusions](#exclusions) · [Evidence ledger](#evidence-ledger) · [Test matrix](#test-matrix) · [Fixture policy](#fixture-policy) · [Validation](#validation) · [Rollback](#rollback) · [Verification backlog](#verification-backlog)

---

## Scope

`connectors/inaturalist/tests/` is the proposed test lane for iNaturalist connector admission behavior.

It may contain fixture-based tests, parser tests, SourceDescriptor-gate tests, rights/geoprivacy handling tests, source-role tests, no-network tests, and fail-closed tests for malformed or incomplete source-shaped records.

It must not contain live credentials, unmanaged real observations, public-release fixtures, production source descriptors, policy authority, schema authority, release authority, or tests that normalize connector output into published truth.

[Back to top ↑](#top)

---

## Repo fit

| Surface | Role | Status |
|---|---|---:|
| `connectors/inaturalist/tests/` | Connector-local test lane. | **CONFIRMED path / NEEDS VERIFICATION coverage** |
| `connectors/inaturalist/README.md` | Parent connector governance README. | **CONFIRMED** |
| `docs/sources/catalog/inaturalist/README.md` | Source profile defining admission constraints. | **CONFIRMED** |
| `fixtures/` | Expected fixture root or companion fixture home. | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/source/` | SourceDescriptor schema home. | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/biodiversity/` | Biodiversity contract home. | **NEEDS VERIFICATION** |
| `policy/sensitivity/` and `policy/rights/` | Policy surfaces that tests may mock or assert against. | **NEEDS VERIFICATION** |
| `release/` | Release controls that tests must not bypass. | **Out of scope for connector-local tests** |

> [!NOTE]
> The parent connector README replaced the older greenfield stub and preserved its unresolved work: endpoints, rate limits, descriptors, fixtures, and ingest receipts must be defined and verified before activation. This test README makes those verification duties testable without claiming they already exist.

[Back to top ↑](#top)

---

## Accepted inputs

Accepted test-lane content:

- synthetic or approved fixture records;
- no-network parser tests;
- SourceDescriptor-required tests;
- rights/license normalization tests;
- geoprivacy and KFM sensitivity gate tests;
- observation-grade and source-role tests;
- taxonomy-controlled-vocabulary tests;
- malformed, incomplete, stale, and unsupported-record tests;
- tests proving connector code writes only RAW or QUARANTINE handoff envelopes;
- tests proving connector code cannot write directly to processed, catalog, triplet, published, proof, receipt, or release stores.

---

## Exclusions

Do not put these in connector-local tests:

- live API credentials;
- tests that require network by default;
- unmanaged real observation payloads;
- fixtures that expose restricted records;
- production source descriptors;
- policy implementations treated as connector-local authority;
- public release fixtures;
- tests that require or produce `PUBLISHED` artifacts;
- generated summaries treated as authoritative biodiversity claims.

[Back to top ↑](#top)

---

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---:|---|---|
| `connectors/inaturalist/tests/README.md` | **CONFIRMED** | Target file exists and previously held a thin greenfield test stub. | Does not prove actual tests or CI. |
| `connectors/inaturalist/README.md` | **CONFIRMED** | Parent connector governance says implementation depth, endpoints, rate limits, descriptors, and source activation remain verification items. | Does not prove test coverage. |
| `docs/sources/catalog/inaturalist/README.md` | **CONFIRMED** | Source profile requires per-record rights handling, geoprivacy handling, source-role discipline, and fail-closed behavior before activation. | Does not prove connector code exists. |
| `connectors/inaturalist/tests/` child files | **NEEDS VERIFICATION** | Test README path exists. | Test modules, fixtures, pytest markers, and CI wiring remain unverified. |

---

## Test matrix

| Test area | Required assertion | Failure posture |
|---|---|---|
| No-network default | Test suite passes using fixtures/mocks without live source access. | Fail closed. |
| SourceDescriptor gate | Connector cannot fetch or admit without an accepted descriptor or explicit test stub. | Fail closed. |
| Rights/license | Records with missing or unsupported rights metadata do not enter promotion-track output. | Quarantine or reject. |
| Geoprivacy | Upstream privacy/obscuration states are preserved and not inferred away. | Quarantine or reject. |
| Sensitivity | Unknown or restricted sensitivity posture does not produce public-ready output. | Quarantine or reject. |
| Source role | iNaturalist remains observation evidence and is not promoted to legal, regulatory, taxonomic, or sensitive-record authority. | Fail closed. |
| Taxonomy | Unresolved or uncontrolled taxonomy cannot pass as confirmed. | Quarantine or reject. |
| Geometry | Missing, invalid, or policy-ineligible geometry cannot pass as public-ready. | Quarantine or reject. |
| Output path | Connector-local tests assert no direct write to processed/catalog/triplet/published/proof/receipt/release stores. | Fail closed. |
| Fixtures | Committed fixtures are synthetic, minimized, redacted, generalized, or approved. | Block commit or quarantine fixture. |

---

## Fixture policy

Fixture data must be safe to commit and safe to review.

Minimum posture:

1. Prefer synthetic fixture records that mimic iNaturalist-shaped payloads without copying live sensitive records.
2. Preserve enough fields to test rights, geoprivacy, grade, taxonomy, date, geometry, source role, and error handling.
3. Do not include credentials, tokens, personal contact fields, or unmanaged exact sensitive records.
4. Mark real or externally derived fixture snippets with source, license, transform, and approval notes.
5. Keep fixture transformations explicit; do not silently generalize, redact, or fabricate fields without a note.

---

## Validation

Connector-local validation tests should check that:

- source metadata is preserved;
- SourceDescriptor references are required for activation;
- observation ID, license, attribution, geoprivacy state, observation grade, taxon fields, event date, geometry, uncertainty, source role, sensitivity, review, and vintage fields are explicit where available;
- malformed or incomplete fixture records fail closed;
- records with unclear rights, unresolved role, unresolved taxon, or unresolved sensitivity route to quarantine or rejection;
- connector tests assert RAW or QUARANTINE handoff only;
- no test writes directly to processed, catalog, triplet, published, proof, receipt, or release stores.

Root-level policy-as-code, release review, EvidenceBundle closure, and rollback tests may exist elsewhere; this folder should only verify connector-local behavior and safe handoff contracts.

[Back to top ↑](#top)

---

## Definition of done

This test-lane README is ready for first review when:

- [ ] Test inventory below `connectors/inaturalist/tests/` is listed.
- [ ] Fixture policy is matched by actual committed fixtures or fixture references.
- [ ] No-network default test is present.
- [ ] SourceDescriptor-required test is present.
- [ ] Rights/license fail-closed tests are present.
- [ ] Geoprivacy and sensitivity gate tests are present.
- [ ] Source-role and anti-collapse tests are present.
- [ ] Taxonomy and geometry validation tests are present.
- [ ] Output-path denial tests are present.
- [ ] CI or local test command is documented after verification.

---

## Rollback

Rollback is required if this README is used to imply passing tests, live connector activation, source access approval, rights approval, sensitivity approval, public release readiness, or implementation maturity that has not been verified.

Rollback target:

```text
commit prior to this update: SHA_TBD_AFTER_GIT_HISTORY_CHECK
```

Because the previous file was a thin greenfield stub, a safe rollback is to restore that stub until actual tests and fixtures are inventoried.

---

## Verification backlog

| Item | Status | Needed evidence |
|---|---:|---|
| Confirm actual test files below this path. | **NEEDS VERIFICATION** | Repo tree or mounted workspace. |
| Confirm fixture locations and fixture safety. | **NEEDS VERIFICATION** | Fixture registry, fixture files, and approval notes. |
| Confirm no-network test marker or default behavior. | **NEEDS VERIFICATION** | Test files and CI config. |
| Confirm SourceDescriptor gate tests. | **NEEDS VERIFICATION** | Test files and source-descriptor schema. |
| Confirm rights/geoprivacy/sensitivity tests. | **NEEDS VERIFICATION** | Test files, policy stubs, and fixture cases. |
| Confirm output-path denial tests. | **NEEDS VERIFICATION** | Test files or sandboxed write assertions. |
| Confirm CI wiring and passing status. | **NEEDS VERIFICATION** | Workflow files and test logs. |

---

## Maintainer note

This README does not claim tests exist or pass. It defines the minimum governed shape of the iNaturalist connector test lane so the old greenfield stub becomes actionable without weakening KFM source-admission, rights, sensitivity, and publication controls.

[Back to top ↑](#top)
