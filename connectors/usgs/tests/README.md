<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-usgs-tests-readme
title: connectors/usgs/tests/ — USGS Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · USGS steward · Test steward · Data steward · Validation steward · Docs steward
created: 2026-06-20
updated: 2026-06-20
policy_label: public; tests-readme; source-admission-only; no-network-fixtures
related:
  - ../README.md
  - ../src/README.md
  - ../src/usgs/README.md
  - ../3dep/README.md
  - ../nhdplus_hr/README.md
  - ../nlcd/README.md
  - ../padus/README.md
  - ../../usgs-earthquake/README.md
  - ../../../docs/sources/catalog/usgs/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../policy/rights/
  - ../../../policy/sensitivity/
tags: [kfm, connectors, usgs, tests, fixtures, no-network, descriptor-gates, source-role, raw, quarantine, receipts, governance]
notes:
  - "Expanded from greenfield stub into a governed test-suite boundary."
  - "Tests under this folder should validate connector helper behavior, not source-family doctrine, SourceDescriptor records, schemas, policy, catalog, proofs, release decisions, API behavior, or UI behavior."
  - "Tests must be offline/deterministic unless explicitly marked integration and gated outside default CI."
  - "Required coverage includes descriptor/config gates, import side effects, source-role separation, raw/quarantine/receipt boundaries, and denial/no-op/rate-limit receipt behavior."
  - "Concrete test files, fixtures, CI wiring, and coverage remain NEEDS VERIFICATION until inventoried."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USGS Connector Tests

> Draft test-suite boundary for USGS connector implementation support. These tests protect the source-admission membrane; they do not activate sources or publish data.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Scope: tests" src="https://img.shields.io/badge/scope-tests-blue">
  <img alt="Network: offline by default" src="https://img.shields.io/badge/network-offline__by__default-green">
  <img alt="Lifecycle: raw quarantine receipts" src="https://img.shields.io/badge/lifecycle-raw%20%7C%20quarantine%20%7C%20receipts-orange">
</p>

`connectors/usgs/tests/`

## Quick jumps

[Status](#status) · [Scope](#scope) · [Directory fit](#directory-fit) · [Required test classes](#required-test-classes) · [Fixture rules](#fixture-rules) · [Forbidden tests](#forbidden-tests) · [Product coverage matrix](#product-coverage-matrix) · [CI posture](#ci-posture) · [Validation](#validation) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

---

## Status

> [!IMPORTANT]
> **Status:** `draft` / `NEEDS VERIFICATION`  
> **Owner:** `OWNER_TBD`  
> **Path:** `connectors/usgs/tests/`  
> **Mode:** connector test-suite boundary  
> **Truth posture:** `CONFIRMED` file path and README content; actual test files, fixtures, markers, CI wiring, and coverage remain `NEEDS VERIFICATION`.

---

## Scope

`connectors/usgs/tests/` is the test home for USGS connector helper behavior.

Tests here may verify import safety, descriptor/config gates, parser field preservation, source-role anti-collapse rules, run-receipt creation, raw/quarantine handoff boundaries, and denial/no-op/rate-limit behavior for USGS connector code.

Tests here must not become source-family doctrine, product doctrine, SourceDescriptor authority, schema authority, rights policy, sensitivity policy, catalog/triplet authority, proof authority, release authority, public API behavior, public UI behavior, or publication authority.

---

## Directory fit

```text
connectors/usgs/
├── README.md
├── src/
│   ├── README.md
│   └── usgs/
│       └── README.md
└── tests/
    └── README.md
```

Related product lanes:

```text
connectors/usgs/3dep/
connectors/usgs/nhdplus_hr/
connectors/usgs/nlcd/
connectors/usgs/padus/
connectors/usgs-earthquake/
```

---

## Required test classes

| Test class | Required checks |
|---|---|
| Import safety | Importing connector modules performs no network calls, filesystem writes, credential reads, or source activation. |
| Descriptor/config gates | Client helpers reject missing or invalid descriptor/config inputs. |
| Parser preservation | Parsers preserve source identifiers, timestamps, versions/epochs, geometry/raster/network metadata, rights/review fields, and digest inputs. |
| Source-role separation | Product helpers preserve observed, modeled, administrative, aggregate, versioned-context, and crowdsourced distinctions. |
| Output boundary | Helpers cannot write processed, catalog, triplet, published, release, API, or UI artifacts. |
| Receipt behavior | Success, failure, denial, no-op, skipped, and rate-limited probes produce explicit receipt payloads where applicable. |
| Fixture determinism | Default tests run without live network and without changing external state. |

---

## Fixture rules

- Fixtures must be small, deterministic, and safe for repository use.
- Fixtures must not contain secrets, credentials, tokens, private keys, or live service responses with hidden obligations.
- Fixtures must preserve enough source shape to test parser behavior without becoming source authority.
- Fixtures must identify whether they represent 3DEP, NHDPlus HR, NLCD, PAD-US, earthquake, or future USGS product surfaces.
- Fixture-derived claims remain test evidence only; they do not create catalog or publication authority.

---

## Forbidden tests

| Forbidden pattern | Reason |
|---|---|
| Live network calls in default tests | Default tests must be deterministic and CI-safe. |
| Credentials required for default tests | Secrets must not be required for ordinary test runs. |
| Writes to lifecycle roots during tests | Tests must not mutate `data/raw`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, or `data/published` unless using isolated temp dirs. |
| Public API/UI assertions from connector tests | Public behavior belongs to governed app/release tests. |
| Schema or policy creation inside connector tests | Schema and policy homes own those authorities. |
| Treating fixtures as truth | Fixtures verify code behavior only. |

---

## Product coverage matrix

| Product lane | Minimum anti-collapse tests |
|---|---|
| `3dep` | LAZ/EPT/COPC/DEM separation, datum/units preservation, nodata/overview metadata, raw/quarantine/receipt output only. |
| `nhdplus_hr` | COMID preservation, WBD package scope, observed geometry vs modeled VAA/topology separation, NFHL/NWIS non-collapse. |
| `nlcd` | Modeled raster role, class-map version preservation, epoch preservation, NLCD/CDL/LANDFIRE/GAP advisory crosswalk posture. |
| `padus` | Version pin, contributor-slice separation, boundary-diff receipt, non-cadastral/non-habitat-truth posture. |
| `earthquake` | Event-update snapshots, observed/model/crowdsourced surface separation, not-alerting boundary. |

---

## CI posture

Default CI should run only offline deterministic tests.

Integration tests that touch live USGS or partner surfaces, large downloads, rate-limit behavior, or credentialed endpoints must be explicitly marked and excluded from default CI unless the project later defines a governed integration-test workflow.

---

## Validation

Before relying on this test suite, verify:

- actual test files are inventoried;
- fixture files are inventoried and safe;
- test markers distinguish unit, fixture, integration, slow, and network tests;
- CI runs the intended offline test subset;
- output tests use temp directories and do not mutate lifecycle roots;
- tests cover import safety, descriptor/config gates, source-role separation, raw/quarantine/receipt boundaries, and product-specific anti-collapse rules.

---

## Rollback

Rollback is required if this README is used to justify live-network default tests, source activation, mutation of lifecycle roots, public release claims, or bypass of descriptor/policy gates.

Rollback target: prior greenfield stub content SHA `5c5e3409f0900fd9cad316c943fd74d9a5847217`.

---

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual tests and fixtures are inventoried.
- [ ] Default tests are verified offline and deterministic.
- [ ] Import side effects are tested and absent.
- [ ] Descriptor/config gates are tested.
- [ ] Product-specific source-role separation tests exist.
- [ ] Output-boundary tests prove no processed/catalog/triplet/published/release/API/UI writes occur.
- [ ] Receipt behavior is tested for success, failure, denial, no-op, skipped, and rate-limited cases where applicable.
- [ ] CI behavior is verified or marked `NEEDS VERIFICATION`.

---

## Status summary

`connectors/usgs/tests/` is a draft test-suite boundary for USGS connector implementation support. It is not USGS source-family doctrine, product doctrine, SourceDescriptor authority, policy authority, schema authority, catalog/triplet authority, proof closure, release authority, public API behavior, public UI behavior, or pipeline authority.

<p align="right"><a href="#top">Back to top</a></p>
