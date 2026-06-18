<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-blm-readme
title: connectors/blm/ — BLM Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Source steward · Connector steward · Land/Cadastral steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/blm.md
  - ../../data/registry/sources/
  - ../../data/raw/
  - ../../data/quarantine/
  - ../../data/receipts/
  - ../../data/proofs/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, blm, bureau-of-land-management, source-admission, public-lands, plss, cadastral, raw, quarantine, governance]
notes:
  - "connectors/blm/ is for Bureau of Land Management source-specific intake and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only; connectors do not write processed, catalog, triplet, published, or release records directly."
  - "BLM material must preserve source role, rights posture, vintage, scale, and local authority limitations."
  - "Specific connector modules, endpoints, rate limits, descriptors, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# BLM Connector

`connectors/blm/`

`connectors/blm/` is the source-specific connector lane for **U.S. Bureau of Land Management (BLM)** intake and admission helpers.

It may contain code and connector documentation that supports governed intake of BLM public-land, land-status, cadastral, PLSS, historic land-record, and selected public geospatial reference material. It must not become land truth, source registry authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** BLM source-specific intake and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; BLM source catalog profile CONFIRMED; connector implementation, endpoints, rate limits, descriptors, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> BLM connector output is admission material, not proof of a final land, access, parcel, road, cultural-resource, ecology, infrastructure, or county-level claim. Treat BLM records as source candidates until source descriptors, rights review, evidence closure, policy checks, and release controls are satisfied.

## Purpose

Use this folder for BLM-specific connector code and documentation that supports governed source intake.

A connector may retrieve or stage candidate source material, preserve BLM metadata, capture endpoint and cadence assumptions, record digests, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── blm/
    └── README.md
```

Related roots:

```text
docs/sources/catalog/blm.md       # BLM source catalog profile
data/registry/sources/            # source descriptors and activation state
data/raw/                         # admitted raw/staged BLM payloads
data/quarantine/                  # held material requiring review
data/receipts/                    # process and validation receipts
data/proofs/                      # EvidenceBundles and proof packs
policy/                           # source, rights, and publication rules
release/                          # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/blm/
├── source-specific intake logic
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
| Source adapter | BLM ArcGIS REST or download client | Must preserve source role and provenance |
| Endpoint note | service URL pattern, layer family, cadence note | Must remain checkable and descriptor-linked |
| Admission helper | checksum, content type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Connector docs | README, endpoint notes, dataset-family notes | Must not claim source admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed land, PLSS, cadastral, land-status, or historic-record data | `data/processed/` after governed processing |
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

## BLM admission posture

BLM connector code should preserve source-family and dataset-family context without overstating authority. The BLM source catalog profile identifies common access families such as Geospatial Business Platform Hub, ArcGIS REST services, land-record entry points, map viewers, General Land Office records, and Mineral & Land Records System access paths.

Connector code should preserve:

- source family and dataset-family identifier;
- service/layer or record locator;
- retrieval time and source vintage when available;
- content digest;
- source role and authority scope;
- rights and review posture;
- scale, generalization, and limitation notes;
- quarantine reason when review is needed.

## Dataset-family posture

BLM materials may support PLSS/CadNSDI, surface-management, access, conservation, recreation, fire, range, vegetation/wildlife, lands/realty, and historic land-record context. Connector code should not turn BLM material into county parcel truth, road authority truth, local access truth, cultural-resource exposure, sensitive ecology exposure, or final legal interpretation.

## Validation expectations

Before relying on this connector, verify:

- source descriptors and source catalog profile exist;
- connector tests use no-network fixtures where practical;
- endpoint, layer, cadence, and dataset-family assumptions are documented and configurable;
- output paths are limited to raw/quarantine admission lanes;
- rights and policy checks are invoked where required;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/blm/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, source role, rights posture, scale/vintage, and limitation notes are preserved.
4. Confirm endpoint, layer, and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/blm/` contents are inventoried.
- [ ] BLM source-family coverage is listed and tied to source descriptors.
- [ ] Endpoint, layer, and cadence assumptions are documented and tested.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/blm/` is for BLM source-specific intake and admission code only. It is not a source of land truth, access truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>
