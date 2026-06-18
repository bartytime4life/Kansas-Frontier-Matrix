<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-src-readme
title: connectors/blm/src/ — BLM Connector Source Tree
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Connector steward · Source steward · Data steward · QA steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ./blm/README.md
  - ../tests/README.md
  - ../../../docs/sources/catalog/blm.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../policy/
  - ../../../tests/
tags: [kfm, connectors, blm, src, source-tree, python-package, source-admission, raw, quarantine, governance]
notes:
  - "connectors/blm/src/ is the source-tree container for the BLM connector package."
  - "Implementation code below this tree may support BLM source intake and raw/quarantine admission boundaries only."
  - "Source-tree code must not write processed, catalog, triplet, published, or release records directly."
  - "Specific package layout, modules, exports, runtime behavior, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector Source Tree

`connectors/blm/src/`

`connectors/blm/src/` is the source-tree container for the BLM connector implementation package.

It may contain package directories such as `blm/` and package-local documentation. It must not become BLM source truth, schema authority, policy authority, catalog/triplet authority, proof authority, release authority, publication authority, fixture authority, or generated-report storage.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Source-tree path:** `connectors/blm/src/`  
> **Responsibility:** BLM connector source-tree container only  
> **Truth posture:** README path CONFIRMED; parent BLM connector README CONFIRMED; package README for `connectors/blm/src/blm/` CONFIRMED; current source-tree inventory, modules, exports, runtime behavior, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder as the package source tree for the BLM connector.

Code below this tree may support governed source intake by:

- building requests for approved BLM source descriptors;
- preserving source-family and dataset-family identifiers;
- parsing source metadata without strengthening authority;
- preserving vintage, scale, rights posture, source role, and limitation notes;
- computing digests and retrieval metadata;
- preparing raw/quarantine admission outputs;
- returning finite safe outcomes such as `skip`, `quarantine`, or `needs_review` when assumptions fail.

The source tree must not decide final truth, write processed data, create catalog/triplet records, publish artifacts, create release decisions, or bypass downstream evidence and policy controls.

## Canonical fit

```text
connectors/
└── blm/
    └── src/
        ├── README.md
        └── blm/
            └── README.md
```

Related roots:

```text
connectors/blm/             # connector root and connector-level README
connectors/blm/src/blm/     # Python package lane
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
connectors/blm/src/
├── package source tree
├── package folders
├── package-local documentation
└── importable connector code

NOT HERE:
  processed data writers
  catalog/triplet writers
  release decision logic
  policy rule authority
  schema authority
  source registry authority
  fixture authority
  generated reports
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Package directory | `blm/` | Must remain connector implementation package |
| Package-local docs | package README | Must not claim runtime behavior unless verified |
| Connector modules | endpoint, metadata, admission helpers | Must preserve source boundaries |
| Test helpers | local fake clients, small helper utilities | Must not become fixture authority |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed records | downstream processing lanes |
| Catalog or triplet records | catalog/triplet pipeline stages |
| Release decisions | `release/` governed decision path |
| Policy rules | `policy/` |
| Machine schemas | `schemas/contracts/v1/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` |
| Raw or quarantine payloads | `data/raw/`, `data/quarantine/` |
| Fixture authority | accepted fixture roots |
| Generated reports | `artifacts/` |

## Source-tree expectations

The source tree should be small, importable, and testable without live service dependency where practical.

Implementation below `connectors/blm/src/` should:

- avoid hard-coded authority assumptions;
- keep source identifiers separate from normalized internal identifiers;
- preserve retrieval metadata and digests;
- use explicit finite failure outcomes;
- leave processed/catalog/triplet/proof/release outputs to downstream governed stages;
- keep module boundaries readable enough for source, data, QA, and connector stewards to review.

## Validation expectations

Before relying on this source tree, verify:

- package modules are inventoried;
- imports and exports are documented or intentionally absent;
- tests cover request construction, metadata preservation, digest stability, and failure handling;
- no-network fixtures are used where practical;
- raw/quarantine output boundaries are enforced;
- CI invokes or explicitly excludes connector tests.

## Safe change pattern

For changes under `connectors/blm/src/`:

1. Confirm the file is BLM connector source code, package-local documentation, or source-tree support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, source role, rights posture, scale/vintage, and limitation notes are preserved.
4. Confirm endpoint, layer, and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is code-only or documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual source-tree modules are inventoried.
- [ ] Package layout is documented.
- [ ] Public exports are documented or intentionally absent.
- [ ] Source-tree tests cover source-admission boundaries.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, fixture, or report authority lives here.
- [ ] CI/test-runner behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/blm/src/` is the BLM connector source-tree container only. It supports source intake and raw/quarantine admission boundaries; it is not a source of land truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, fixture authority, or generated-report storage.

<p align="right"><a href="#top">Back to top</a></p>
