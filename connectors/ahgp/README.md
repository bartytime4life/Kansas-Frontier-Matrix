<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-ahgp-readme
title: connectors/ahgp/ — AHGP Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · People/Genealogy steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/ahgp.md
  - ../../docs/sources/catalog/ahgp/
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, ahgp, genealogy, source-admission, raw, quarantine, receipts, governance]
notes:
  - "connectors/ahgp/ is for American Hereditary Genealogy Project source-specific fetch and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only; connectors do not write processed, catalog, triplet, published, or release records directly."
  - "Genealogy source material may include people, family, cemetery, obituary, census, and locality history context and requires rights, sensitivity, evidence, policy, and review controls before any public use."
  - "Specific connector modules, endpoints, rate limits, source coverage, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AHGP Connector

`connectors/ahgp/`

`connectors/ahgp/` is the source-specific connector lane for the **American Hereditary Genealogy Project (AHGP)** source family.

It may contain code and connector documentation that supports governed source intake for AHGP pages and product families. It must not become genealogy truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** AHGP source-specific fetch and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; AHGP source-family catalog stub CONFIRMED; pyproject placeholder CONFIRMED; connector implementation, endpoints, rate limits, descriptors, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> AHGP connector output is admission material, not proof of a people, family, place, cemetery, census, obituary, or locality-history claim. Treat source records as candidates until source descriptors, rights, sensitivity review, evidence closure, policy checks, and release controls are satisfied.

## Purpose

Use this folder for AHGP-specific connector code and documentation that supports governed source intake.

A connector may fetch or stage candidate source material, preserve source-family metadata, capture endpoint and rate-limit assumptions, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── ahgp/
    ├── README.md
    └── pyproject.toml
```

Related roots:

```text
docs/sources/catalog/ahgp.md       # source-family catalog umbrella
docs/sources/catalog/ahgp/         # per-product source catalog pages
data/registry/sources/             # source descriptors and source-family activation state
data/raw/                          # admitted raw/staged source payloads
data/quarantine/                   # held material requiring review
data/receipts/                     # process and validation receipts
data/proofs/                       # EvidenceBundles and proof packs
policy/                            # source, sensitivity, and publication rules
release/                           # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/ahgp/
├── source-specific fetch logic
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
| Source fetch adapter | AHGP page/product-family client | Must preserve source and product-family context |
| Endpoint note | source URL pattern, crawl cadence note | Must remain reviewable and cite source-family descriptor |
| Rate-limit note | polite delay/config reference | Must be configurable and testable |
| Admission helper | checksum, content-type, timestamp, source-family metadata | Must write only raw/quarantine admission outputs |
| Connector docs | README, endpoint notes, product-family notes | Must not claim source admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed people, genealogy, locality, cemetery, obituary, census, or history records | `data/processed/` after governed processing |
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

## AHGP admission posture

AHGP is a source-family connector, not a single sovereign source. The catalog umbrella identifies AHGP as a source family and points to source descriptors, connector code, and per-product catalog entries.

Connector code should preserve:

- source-family identifier;
- product-family identifier when available;
- URL or source locator;
- retrieval time and source time when available;
- content digest;
- source role and caveat text from the registry;
- rights and sensitivity posture;
- quarantine reason when review is needed.

## Endpoint and rate-limit posture

Endpoint lists and rate-limit assumptions should be documented as checkable connector configuration, not hard-coded truth.

Before enabling an endpoint path, verify:

- source descriptor exists and is active;
- rights/cadence guidance is recorded;
- no-network fixture is available for tests where practical;
- connector emits receipts or admission metadata through the governed downstream path;
- failures result in safe finite outcomes such as `quarantine`, `skip`, or `needs_review`, not silent publication.

## Validation expectations

Before relying on this connector, verify:

- source descriptors and per-product source catalog pages exist;
- connector tests use no-network fixtures where practical;
- endpoint and cadence assumptions are documented and configurable;
- output paths are limited to raw/quarantine admission lanes;
- rights and sensitivity checks are invoked where required;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve source refs, provenance notes, review notes, and rollback instructions.
5. Add a drift note if the misplaced connector material was already consumed.

## Safe change pattern

For changes under `connectors/ahgp/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, rights, caveats, and temporal context are preserved.
4. Confirm endpoint and rate-limit assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/ahgp/` contents are inventoried.
- [ ] AHGP source-family coverage is listed and tied to source descriptors.
- [ ] Endpoint and rate-limit assumptions are documented and tested.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/ahgp/` is for AHGP source-specific fetch and admission code only. It is not a source of genealogy truth, registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>
