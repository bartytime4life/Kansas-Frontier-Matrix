<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-tests-readme
title: connectors/blm/tests/ — BLM Connector Tests
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · QA steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../../connectors/README.md
  - ../../../tests/README.md
  - ../../../docs/sources/catalog/blm.md
  - ../../../data/registry/sources/
  - ../../../fixtures/
  - ../../../tools/
tags: [kfm, connectors, blm, tests, fixtures, validation, source-admission, governance]
notes:
  - "connectors/blm/tests/ is for BLM connector test code and test notes only."
  - "Tests here support connector confidence but do not by themselves admit sources, publish artifacts, or prove release readiness."
  - "Fixtures and generated reports belong in their accepted fixture/report roots, not here unless a repo ADR says otherwise."
  - "Specific current test modules, fixture coverage, and CI wiring remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Tests

`connectors/blm/tests/`

`connectors/blm/tests/` is the test sublane for the BLM connector.

It may contain connector-scoped tests and test documentation for BLM intake behavior. It must not become source registry authority, fixture authority, lifecycle data authority, release authority, generated report storage, or a substitute for the canonical `tests/` trust-spine suite.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** BLM connector-scoped tests and test notes  
> **Truth posture:** README path CONFIRMED; BLM connector README CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; canonical `tests/` root CONFIRMED as enforceability root; current test module coverage, fixture coverage, and CI wiring remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder for tests that exercise the BLM connector's source-admission behavior.

These tests should help verify that connector code preserves source role, source identity, dataset-family context, retrieval metadata, scale/vintage notes, rights posture, and raw/quarantine output boundaries.

A passing local connector test does not by itself prove source admission, catalog closure, release readiness, public display safety, or end-to-end KFM trust-spine enforcement.

## Canonical fit

```text
connectors/
└── blm/
    └── tests/
        └── README.md
```

Related roots:

```text
connectors/blm/             # connector code and connector README
tests/                      # canonical enforceability proof root
fixtures/                   # accepted fixture home, if present and verified
tools/                      # validators and test helpers
data/registry/sources/      # source descriptors and source-family activation state
data/raw/                   # raw/staged connector outputs
data/quarantine/            # held material requiring review
artifacts/                  # generated test reports, if produced
```

## Authority boundary

```text
connectors/blm/tests/
├── connector unit tests
├── connector contract tests
├── no-network adapter tests
└── test notes

NOT HERE:
  fixture authority
  source registry rows
  raw/quarantine payloads
  generated reports
  release decisions
  production connector code
  policy rules
  schemas/contracts
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Unit tests | parser, request-builder, metadata-preservation tests | Must not require live network by default |
| Contract-style tests | source descriptor compatibility checks | Must cite canonical schema/descriptor home |
| Fixture references | path notes to accepted fixtures | Fixture payloads belong in accepted fixture roots unless explicitly local and tiny |
| Failure-mode tests | quarantine/skip/needs-review behavior | Must assert finite safe outcomes |
| Test notes | README or test-plan fragments | Must not claim CI pass state unless verified |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Connector implementation code | `connectors/blm/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` |
| Raw or quarantine payloads | `data/raw/`, `data/quarantine/` |
| Processed, catalog, triplet, published, receipt, or proof records | `data/` owning subtrees |
| Release decisions or rollback/correction records | `release/` |
| Policy rules | `policy/` |
| Machine schemas | `schemas/contracts/v1/` |
| Generated reports and build/QA outputs | `artifacts/` |
| End-to-end trust-spine test authority | `tests/` |

## Test expectations

BLM connector tests should verify:

- source descriptor requirement is respected;
- endpoint and dataset-family assumptions remain configurable;
- source-family and dataset-family identifiers are preserved;
- retrieval time and source vintage are preserved when available;
- content digests are stable;
- raw/quarantine output boundaries are enforced;
- no test silently asserts processed/catalog/published/release behavior from connector-only output;
- no-network fixtures are used where practical;
- failures result in finite safe outcomes such as `skip`, `quarantine`, or `needs_review`.

## Fixture posture

Prefer no-network fixtures for connector tests.

Fixture payloads should be tiny, reviewable, non-sensitive, and stored in the accepted fixture root when possible. If a tiny local fixture is kept beside a test, document why and ensure it cannot be confused with source authority or lifecycle data.

## Validation posture

Before relying on this test lane, verify:

- test runner and command are documented;
- fixture paths are current;
- source descriptor/schema references are current;
- CI invokes the relevant tests or explicitly marks them manual;
- generated reports, if any, land in `artifacts/` or the accepted report root;
- connector tests complement, but do not replace, the canonical `tests/` trust-spine suite.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/blm/tests/` contents are inventoried.
- [ ] Test files are tied to connector behaviors and source descriptor expectations.
- [ ] No-network fixture coverage is verified or marked `NEEDS VERIFICATION`.
- [ ] No source registry, lifecycle, release, policy, schema, generated-report, or production-code authority lives here.
- [ ] CI/test-runner behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/blm/tests/` is for BLM connector-scoped tests and test notes only. It is not fixture authority, source registry authority, lifecycle authority, release authority, schema authority, policy authority, generated-report storage, or a replacement for the canonical `tests/` enforceability suite.

<p align="right"><a href="#top">Back to top</a></p>
