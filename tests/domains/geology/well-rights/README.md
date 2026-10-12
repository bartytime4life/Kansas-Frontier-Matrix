<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-geology-well-rights-readme
title: Geology Well-Rights Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — People/Land steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; geology; well-rights; owner-privacy; source-rights; no-network; deny-by-default; cross-lane-boundary
tags: [kfm, tests, geology, wells, boreholes, well-rights, source-rights, owner-privacy, water-rights, hydrology, people-land, EvidenceBundle, PolicyDecision, RedactionReceipt, DENY, RESTRICT, ABSTAIN]
related:
  - ../../../../tests/README.md
  - ../../../../fixtures/domains/geology/README.md
  - ../../../../docs/domains/geology/sublanes/boreholes-wells.md
  - ../../../../docs/domains/geology/README.md
  - ../../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../../docs/domains/geology/POLICY.md
  - ../../../../contracts/domains/geology/
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/geology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../policy/domains/geology/
  - ../../../../data/registry/sources/geology/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This file replaces a blank placeholder at tests/domains/geology/well-rights/README.md."
  - "This path is user-requested under the tests root. The folder name is well-rights rather than test_well_rights; treat the path as a test lane unless repo convention later requires migration."
  - "This is a test-lane README only. It does not define water-right law, parcel/title authority, owner identity, hydrology contracts, geology contracts, SourceDescriptor schemas, policy rules, evidence bundles, receipts, release decisions, or published artifacts."
  - "The tested invariant is that geology well/borehole evidence, owner/privacy metadata, source rights, water-right context, hydrology groundwater claims, and people/land ownership claims must not collapse into one another."
  - "The default posture is deterministic and no-network. Live source checks, credentials, real owner records, real exact well coordinates, and real water-right adjudications do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology well-rights tests

> Deterministic, no-network test documentation for proving that geology well and borehole records preserve source rights, owner privacy, hydrology boundaries, and people/land boundaries before any public catalog, map, API, Evidence Drawer, Focus Mode, or release carrier can use them.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology%2Fnatural__resources-brown">
  <img alt="Lane: well rights" src="https://img.shields.io/badge/lane-well__rights-purple">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Exposure: deny by default" src="https://img.shields.io/badge/exposure-deny__by__default-success">
</p>

**Path:** `tests/domains/geology/well-rights/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until paired test files are verified  
**Owning root:** `tests/`  
**Domain segment:** `geology`  
**Test lane:** `well-rights`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED Geology boreholes/wells doctrine treats exact borehole, sample, well-log, and private-well locations as restricted/generalized by default · CONFIRMED Hydrology boundary doctrine owns groundwater-well claims and does not own parcels/title · NEEDS VERIFICATION for actual test modules, fixtures, source-right profiles, hydrology/person-land boundary fixtures, policy engine wiring, redaction receipt emission, CI coverage, and release-gate integration.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected test scope](#expected-test-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested test layout](#suggested-test-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/geology/well-rights/` is the intended home for tests that prove well and borehole records remain boundary-safe when they carry rights, owner-privacy, source-license, water-right, hydrology, or land-context metadata.

This lane should test that a Geology well or borehole record cannot silently become:

- a water-right determination;
- a parcel, title, owner, or land-tenure claim;
- a hydrology groundwater-well canonical claim;
- a public exact well-location release;
- a proof of extraction, production, deposit, reserve, or land ownership;
- a source-rights clearance merely because the record exists;
- an AI or map answer that exposes owner identity, exact location, or proprietary log content.

A passing test here should **not** mean that a water right is legally valid, a well owner is identified, a parcel relation is authoritative, or a public geometry product is released. It should mean only that the well-rights boundary behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Geology appears as a lane segment inside the tests root, not as a repo-root domain folder.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Geology well-rights boundary tests | `tests/domains/geology/well-rights/` | This directory. |
| Synthetic fixtures and expected outcomes | `fixtures/domains/geology/` | Preferred toy inputs and expected envelopes. |
| Boreholes/wells doctrine | `docs/domains/geology/sublanes/boreholes-wells.md` | Referenced doctrine; does not make tests pass. |
| Hydrology boundary doctrine | `docs/domains/hydrology/BOUNDARY.md` | Referenced for groundwater-well and parcel/title boundary. |
| Source rights and source registry | `data/registry/sources/geology/` | Source identity, role, rights, cadence, caveats, and activation state. |
| Semantic contracts | `contracts/domains/geology/`, `contracts/domains/hydrology/` | Referenced by tests, not redefined here. |
| Machine shape | `schemas/contracts/v1/domains/geology/`, `schemas/contracts/v1/domains/hydrology/` | Referenced by tests, not duplicated here. |
| Policy decisions | `policy/domains/geology/`, hydrology/land policy homes if accepted | Referenced by tests, not bypassed here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Expected references; not authored as test truth here. |
| Release decisions | `release/` | Required before public delivery; tests cannot replace it. |

---

## Invariant under test

> **Well-rights metadata is boundary context, not authority collapse.** Geology may carry well/borehole evidence and source-right metadata, but it must not become the canonical authority for water-right law, land ownership, parcel/title identity, hydrology groundwater claims, or public exact private-well exposure.

For this test lane, the invariant decomposes into nine checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source rights | License, embargo, attribution, source access, and reuse posture are explicit before use. | `ABSTAIN` / `DENY`. |
| Owner privacy | Owner identity, private-well identity, parcel link, or contact information is absent, redacted, generalized, or policy-restricted. | `DENY` / `RESTRICT`. |
| Exact well geometry | Exact borehole/private-well geometry is not public by default. | `DENY` / `RESTRICT`. |
| Hydrology boundary | Groundwater-well hydrology claims remain owned by hydrology contracts/records. | validation failure / `ABSTAIN`. |
| People/land boundary | Parcel, title, owner, or water-right holder claims remain owned by people/land or administrative authority lanes. | validation failure / `ABSTAIN`. |
| Source role | Driller logs, regulatory records, owner records, permit records, production records, and interpreted geology evidence remain role-typed. | `DENY` / validation failure. |
| Evidence closure | Claim-bearing statements require `EvidenceRef -> EvidenceBundle` support. | `ABSTAIN`. |
| Public-safe transform | Public carriers use generalized/aggregated/masked geometry with receipt-ready transform metadata. | validation failure / `DENY`. |
| Release path | Any public well-derived carrier has review, policy, release, correction, and rollback linkage. | promotion-blocking failure. |

---

## Expected test scope

Tests in this lane should be small, synthetic, and deterministic. They may validate:

- denial or restriction when a private-well owner, parcel link, or exact point geometry is requested for public exposure;
- rejection of well/borehole records that lack rights, license, source-role, or sensitivity posture;
- rejection of public outputs that expose owner identity, proprietary logs, exact coordinates, or embargoed records;
- preservation of cross-lane ownership: geology evidence cannot overwrite hydrology groundwater-well claims or people/land title/parcel claims;
- rejection of source-role collapse between well log evidence, water-right records, permits, production records, extraction records, reserve estimates, and physical geology claims;
- public-safe generalized or aggregated well-derived outputs when evidence, policy, review, release, and receipt-ready transform metadata are present;
- non-answer outcomes when water-right authority, source rights, owner privacy, or boundary ownership is unresolved.

Live source systems, real water-right adjudications, real owner records, real exact well coordinates, and credentials are out of scope for the default suite.

---

## Fixture posture

Use fixture material from `fixtures/domains/geology/` when possible.

Fixture requirements:

- synthetic and public-safe;
- no real owner identity;
- no real parcel/title record;
- no real exact well or borehole coordinate;
- no live source calls;
- no real source exports;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source role and claim class;
- explicit source-right posture;
- explicit owner/privacy and sensitivity posture;
- explicit hydrology or people/land boundary posture when a cross-lane claim is tested;
- explicit policy/release state where public exposure is tested.

Preferred fixture families:

| Fixture kind | Preferred lane | Example expected outcome |
|---|---|---|
| Public-safe aggregated well-density fixture | `fixtures/domains/geology/valid/` or `golden/` | Allowed as a public-safe carrier with transform metadata. |
| Private well exact point | `fixtures/domains/geology/invalid/` or `tier-transitions/` | `DENY` / `RESTRICT`. |
| Proprietary or embargoed well log | `fixtures/domains/geology/invalid/` | `DENY` / `ABSTAIN`. |
| Missing source-right profile | `fixtures/domains/geology/invalid/` | `ABSTAIN` / validation failure. |
| Owner/parcel leakage example | `fixtures/domains/geology/invalid/` | `DENY` / test failure. |
| Hydrology boundary example | `fixtures/domains/geology/source_role/` | Geology does not claim hydrology ownership. |
| People/land boundary example | `fixtures/domains/geology/source_role/` | Geology does not claim owner/title authority. |

---

## Assertions

A good well-rights test should make the boundary failure visible.

### Positive path

- well/borehole record is synthetic and public-safe;
- source role, source-rights posture, and sensitivity tier are explicit;
- exact geometry is withheld, generalized, masked, or aggregated;
- owner identity and parcel/title details are absent or policy-redacted;
- hydrology and people/land authority are referenced only as bounded context;
- evidence and source references remain attached where a geology claim is made;
- public carrier includes or points to receipt-ready redaction/generalization metadata;
- release-linked output preserves correction and rollback context.

### Negative path

- missing source-rights posture fails closed;
- private-well owner identity cannot appear in public test output;
- exact private-well or sensitive borehole geometry cannot be emitted as public;
- proprietary or embargoed log content cannot be treated as open public evidence;
- well records cannot silently become water-right determinations;
- geology cannot overwrite hydrology groundwater-well authority;
- geology cannot overwrite people/land parcel, owner, title, or land-tenure authority;
- permit, production, extraction, reserve, deposit, and well-log records cannot substitute for each other;
- AI or map text cannot create legal, ownership, or rights authority.

---

## Finite outcomes

This lane should prefer explicit finite outcomes over loose pass/fail text.

| Condition | Expected outcome |
|---|---|
| Public-safe aggregate/generalized well-derived carrier with rights, policy, evidence, review, release, and rollback context | allow public-safe downstream carrier. |
| Exact private-well geometry requested for public exposure | `DENY` or `RESTRICT`. |
| Owner identity, parcel/title, or contact information requested for public exposure | `DENY` or `RESTRICT`. |
| Missing source rights, source role, or sensitivity context | `ABSTAIN` / validation failure. |
| Proprietary or embargoed log content lacks release clearance | `DENY` / `ABSTAIN`. |
| Water-right or ownership authority is unresolved | `ABSTAIN`, not generated answer. |
| Cross-lane authority collapse detected | validation failure / `DENY`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store credentials or tokens;
- store real source exports;
- store real owner identity, parcel/title records, water-right adjudications, or exact well/borehole coordinates;
- define water-right law or legal conclusions;
- create a parallel hydrology, people/land, source-registry, schema, policy, receipt, proof, or release authority;
- bypass source-right or owner-privacy checks with a fixture flag;
- infer rights clearance from file existence, source name, public web availability, map display, or AI wording;
- treat well logs, permits, production records, reserve estimates, water rights, owner records, or physical geology evidence as interchangeable;
- publish, promote, or release anything.

Any test that requires real source records belongs in a gated integration tier with quarantine, source admission, rights review, redaction, receipts, and rollback controls.

---

## Suggested test layout

The exact Python module names remain NEEDS VERIFICATION until the runner and existing test conventions are inspected. A minimal future layout could be:

```text
tests/domains/geology/well-rights/
├── README.md
├── test_source_rights_required.py          # missing license/rights posture fails closed
├── test_private_well_geometry_denied.py    # exact/private/sensitive locations do not publish
├── test_owner_parcel_leakage_denied.py     # owner/title/parcel details do not leak
├── test_hydrology_boundary_preserved.py    # geology does not own groundwater-right claims
└── test_public_safe_aggregate_allowed.py   # generalized/aggregated carrier with receipts/release refs
```

Keep helpers local only when they are test-specific. Shared source-right, policy, redaction, hydrology, people/land, evidence, runtime-envelope, or release behavior belongs under its accepted implementation root, not duplicated here.

---

## Run posture

Default run expectations:

```bash
pytest tests/domains/geology/well-rights
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that the test modules exist. This README does not claim the command currently passes.

Expected CI posture:

- default suite: no-network, synthetic fixtures only;
- fail closed on missing source rights, owner/privacy leakage, exact well geometry exposure, source-role collapse, cross-lane authority collapse, missing policy, missing release state, or missing redaction/aggregation metadata;
- live-source checks: separate gated job only;
- release gate: well-rights failures should block public catalog/API/map/tile/AI carrier promotion.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/geology/well-rights/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof; domain-specific tests belong under `tests/domains/<domain>/`; default suite should avoid sensitive data and live network calls. | Does not prove this lane's modules or pass rate. |
| `docs/domains/geology/sublanes/boreholes-wells.md` | CONFIRMED doctrine / PROPOSED sublane implementation | Boreholes/wells are location-sensitive; exact borehole/sample/well-log/private-well locations default restricted or generalized; public release requires redaction/aggregation, review, and policy decision. | Sublane folder placement is itself PROPOSED and drift-noted; does not prove test modules or enforcement. |
| `docs/domains/hydrology/BOUNDARY.md` | CONFIRMED doctrine / PROPOSED implementation | Hydrology owns groundwater-well claims and explicitly does not own parcels/title; boundary joins must preserve ownership, source role, sensitivity, and evidence support. | Does not define geology well-right tests or people/land implementation. |
| `docs/domains/geology/README.md` | CONFIRMED doctrine / PROPOSED implementation | Geology governs boreholes, well logs, cores, geophysics, geochemistry, mineral occurrences, and resource context while denying exact subsurface/private-well exposure by default. | Does not prove well-rights test files, fixtures, or policy enforcement. |
| `fixtures/domains/geology/README.md` | CONFIRMED | Synthetic, public-safe fixture posture and child lanes for Geology. | Does not prove all fixture payloads or consumers. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist for source-rights present, source-rights missing, exact private-well geometry, owner/parcel leakage, proprietary log embargo, hydrology boundary, people/land boundary, and public-safe aggregate release candidate.
- [ ] SourceDescriptor/source-right profile path is accepted.
- [ ] Geology and hydrology contract/schema paths are accepted.
- [ ] People/land boundary and ownership authority path is accepted before enforcing people/land-specific assertions.
- [ ] PolicyDecision behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle resolver behavior is available to tests or safely stubbed.
- [ ] RedactionReceipt or AggregationReceipt expectations are defined before enforcing them.
- [ ] CI runs the no-network well-rights suite.
- [ ] Failures block public carrier promotion or release candidate approval.

---

## Rollback

Rollback is required if this lane becomes a water-right authority, legal conclusion store, owner/parcel/title registry, hydrology canonical store, source registry, fixture root, lifecycle data store, proof store, receipt store, release-decision root, schema authority, policy authority, public map/API/tile surface, AI surface, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
