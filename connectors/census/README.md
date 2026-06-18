<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-census-readme
title: connectors/census/ — Census Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Frontier Matrix steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/census/README.md
  - ../../docs/sources/catalog/census/acs-estimates.md
  - ../../docs/sources/catalog/census/tiger-line.md
  - ../../docs/sources/catalog/census/decennial-counts.md
  - ../../docs/sources/catalog/census/decennial-microdata.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, census, acs, decennial, tiger, source-admission, aggregate, administrative, raw, quarantine, governance]
notes:
  - "connectors/census/ is for Census source-family intake and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only; connectors do not write processed, catalog, triplet, published, or release records directly."
  - "Census product families require source-role preservation: aggregate, administrative, vintage-bound, and uncertainty-aware where applicable."
  - "Specific connector modules, endpoints, rate limits, descriptors, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Census Connector

`connectors/census/`

`connectors/census/` is the source-specific connector lane for the U.S. Census source family.

It may contain code and connector documentation that supports governed intake of Census products such as decennial counts, ACS estimates, TIGER/Line geography, historic microdata releases, and historical compilations. It must not become demographic truth, administrative-geometry truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** Census source-family intake and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; Census source-family catalog page CONFIRMED; connector implementation, endpoints, rate limits, descriptors, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> Census connector output is admission material, not proof of a final demographic, settlement, boundary, people, land, or historical claim. Treat Census records as candidates until source descriptors, source roles, vintage, uncertainty, policy checks, evidence closure, review state, and release controls are satisfied.

## Purpose

Use this folder for Census-specific connector code and documentation that supports governed source intake.

A connector may retrieve or stage candidate source material, preserve product-family and vintage metadata, capture endpoint and cadence assumptions, record digests, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── census/
    └── README.md
```

Related roots:

```text
docs/sources/catalog/census/     # Census source-family catalog pages
data/registry/sources/           # source descriptors and activation state
data/raw/                        # admitted raw/staged Census payloads
data/quarantine/                 # held material requiring review
data/receipts/                   # process and validation receipts
data/proofs/                     # EvidenceBundles and proof packs
policy/                          # source, rights, and publication rules
release/                         # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/census/
├── source-family intake logic
├── endpoint and cadence notes
├── admission metadata helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/
  data/quarantine/

NOT HERE:
  processed data
  catalog records
  triplet records
  receipts/proofs as authority
  release decisions
  published artifacts
  policy rules
  schemas/contracts
  source registry rows as authority
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Source adapter | Census API, TIGER/Line, ACS, decennial product adapter | Must preserve product family, vintage, and source role |
| Endpoint note | endpoint pattern, dataset vintage, cadence note | Must remain checkable and descriptor-linked |
| Admission helper | checksum, content type, retrieval timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Source-role helper | aggregate/admin/vintage/uncertainty marker preservation | Must not strengthen source authority |
| Connector docs | README, product-family notes | Must not claim source admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed demographic, ACS, TIGER, boundary, people, land, or historic panel records | `data/processed/` after governed processing |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` |
| Source descriptors or registry rows as authority | `data/registry/sources/` or governed registry homes |
| Receipts and proof packs as authority | `data/receipts/`, `data/proofs/` |
| Published artifacts or public layers | `data/published/` after governed release |
| Release decisions or rollback/correction records | `release/` |
| Policy rules and publication decisions | `policy/` and release-governed decision homes |
| Machine schemas | `schemas/contracts/v1/` |
| Human contracts and object meaning | `contracts/` |
| Reusable domain helper package code | `packages/` |
| Executable transformation pipeline logic | `pipelines/` |
| Declarative pipeline definitions | `pipeline_specs/` |
| Generated reports and build/QA outputs | `artifacts/` |

## Census admission posture

Census source-family intake must preserve product-specific source roles and vintage boundaries:

- Decennial counts are aggregate records, not per-place truth by themselves;
- ACS estimates are aggregate estimates and must preserve uncertainty fields when present;
- TIGER/Line geography is administrative geometry and vintage-bound;
- historical microdata and historical compilations require extra care around disclosure window, living-person posture, and compilation provenance;
- Census geometry can orient other domains but does not automatically prove their canonical claims.

Connector code should preserve source family, product family, vintage, geography unit, retrieval time, source time where available, content digest, source role, aggregation unit, uncertainty fields, limitation notes, and quarantine reason when review is needed.

## Endpoint and product-family posture

Endpoint lists and rate-limit assumptions should be documented as checkable connector configuration, not hard-coded truth.

Before enabling a product-family endpoint, verify:

- source descriptor exists and is active;
- rights/cadence guidance is recorded;
- no-network fixture is available for tests where practical;
- connector emits receipts or admission metadata through the governed downstream path;
- failures result in safe finite outcomes such as `quarantine`, `skip`, or `needs_review`, not silent publication.

## Validation expectations

Before relying on this connector, verify:

- source descriptors and product-family catalog pages exist;
- connector tests use no-network fixtures where practical;
- endpoint, cadence, vintage, and product-family assumptions are documented and configurable;
- output paths are limited to raw/quarantine admission lanes;
- uncertainty, aggregation, and vintage fields are preserved;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/census/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, product family, source role, vintage, aggregation unit, uncertainty, and limitation notes are preserved.
4. Confirm endpoint and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/census/` contents are inventoried.
- [ ] Census product-family coverage is listed and tied to source descriptors.
- [ ] Endpoint, cadence, vintage, and rate assumptions are documented and tested.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/census/` is for Census source-family intake and admission code only. It is not a source of demographic truth, administrative-geometry truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>
