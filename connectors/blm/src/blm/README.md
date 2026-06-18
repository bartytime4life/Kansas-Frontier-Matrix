<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-src-blm-readme
title: connectors/blm/src/blm/ — BLM Connector Python Package
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Data steward · QA steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../../README.md
  - ../../../README.md
  - ../../tests/README.md
  - ../../../../docs/sources/catalog/blm.md
  - ../../../../data/registry/sources/
  - ../../../../data/raw/
  - ../../../../data/quarantine/
  - ../../../../data/receipts/
  - ../../../../policy/
  - ../../../../tests/
tags: [kfm, connectors, blm, python-package, source-admission, raw, quarantine, governance]
notes:
  - "connectors/blm/src/blm/ is the BLM connector package lane under the connector root."
  - "Package code may support source intake, metadata preservation, endpoint adapters, and raw/quarantine admission outputs only."
  - "Package code must not write processed, catalog, triplet, published, or release records directly."
  - "Specific modules, exports, runtime behavior, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Package

`connectors/blm/src/blm/`

`connectors/blm/src/blm/` is the Python package lane for BLM connector implementation code under `connectors/blm/`.

It may contain BLM source-admission helpers, endpoint adapters, metadata normalization helpers, digest helpers, and raw/quarantine output helpers. It must not become BLM source truth, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Package path:** `connectors/blm/src/blm/`  
> **Responsibility:** BLM connector implementation package only  
> **Truth posture:** README path CONFIRMED; parent BLM connector README CONFIRMED; current package modules, exports, runtime behavior, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this package for BLM connector implementation code that supports governed source intake.

Acceptable package behavior includes:

- building requests for approved BLM source descriptors;
- parsing source metadata without overstating authority;
- preserving source role, vintage, scale, rights posture, and limitation notes;
- computing digests and retrieval metadata;
- preparing raw/quarantine admission outputs;
- returning finite safe outcomes such as `skip`, `quarantine`, or `needs_review` when assumptions fail.

The package must not decide final truth, write processed data, create catalog/triplet records, publish artifacts, create release decisions, or bypass downstream evidence and policy controls.

## Canonical fit

```text
connectors/
└── blm/
    └── src/
        └── blm/
            └── README.md
```

Related roots:

```text
connectors/blm/             # connector root and connector-level README
connectors/blm/tests/       # connector-local tests
docs/sources/catalog/blm.md # BLM source profile
data/registry/sources/      # source descriptors and activation state
data/raw/                   # admitted raw/staged outputs
data/quarantine/            # held material requiring review
policy/                     # source and publication rules
release/                    # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/blm/src/blm/
├── package modules
├── endpoint adapters
├── source metadata helpers
├── digest and receipt-input helpers
└── raw/quarantine output helpers

NOT HERE:
  processed data writers
  catalog/triplet writers
  release decision logic
  policy rule authority
  schema authority
  source registry authority
  generated reports
```

## Allowed module families

| Module family | Example | Required posture |
|---|---|---|
| Endpoint adapters | REST/service metadata adapter | Must be descriptor-linked and testable |
| Metadata parsers | layer metadata, dataset-family parser | Must preserve source limitations |
| Admission helpers | digest, source timestamp, output envelope | Must target raw/quarantine only |
| Failure handling | skip/quarantine/needs-review result | Must avoid silent promotion |
| Test support helpers | local fake clients | Must not become fixture authority |

## Forbidden module behavior

| Forbidden behavior | Correct home |
|---|---|
| Writing processed records | downstream processing pipelines |
| Writing catalog or triplet records | catalog/triplet pipeline stages |
| Emitting release decisions | `release/` governed decision path |
| Defining policy rules | `policy/` |
| Defining schema authority | `schemas/contracts/v1/` |
| Storing source descriptors as authority | `data/registry/sources/` |
| Storing raw/quarantine payloads in code | `data/raw/`, `data/quarantine/` |
| Storing generated reports | `artifacts/` |

## Implementation expectations

Package code should be small, deterministic where practical, and easy to test without live service dependency.

BLM connector package code should preserve:

- source descriptor ID or source-family ID;
- dataset-family ID when available;
- service/layer or record locator;
- retrieval time and source vintage when available;
- content digest;
- source role and authority scope;
- rights posture and limitation notes;
- quarantine reason when review is needed.

## Validation expectations

Before relying on package behavior, verify:

- module exports are documented;
- tests cover request construction, metadata preservation, digest stability, and failure handling;
- no-network fixtures are used where practical;
- raw/quarantine output boundaries are enforced;
- downstream stages, not this package, produce processed, catalog, triplet, proof, and release objects;
- CI invokes or explicitly excludes connector tests.

## Safe change pattern

For changes under `connectors/blm/src/blm/`:

1. Confirm the file is BLM connector package code or package-local documentation.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, source role, rights posture, scale/vintage, and limitation notes are preserved.
4. Confirm endpoint, layer, and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is code-only or documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual package modules are inventoried.
- [ ] Public exports are documented or intentionally absent.
- [ ] Package tests cover source-admission boundaries.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] CI/test-runner behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/blm/src/blm/` is for BLM connector package code only. It supports source intake and raw/quarantine admission boundaries; it is not a source of land truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, fixture authority, or generated-report storage.

<p align="right"><a href="#top">Back to top</a></p>
