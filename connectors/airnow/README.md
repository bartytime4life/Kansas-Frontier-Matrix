<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-airnow-readme
title: connectors/airnow/ — AirNow Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere/Air steward · Source steward · Connector steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/sources/catalog/epa/airnow-api.md
  - ../../data/registry/sources/
  - ../../data/raw/atmosphere/
  - ../../data/quarantine/atmosphere/
  - ../../data/receipts/atmosphere/
  - ../../data/proofs/atmosphere/
  - ../../policy/
  - ../../release/
tags: [kfm, connectors, airnow, epa, atmosphere, air, aqi, source-admission, raw, quarantine, governance]
notes:
  - "connectors/airnow/ is for AirNow source-specific intake and admission code only."
  - "Connector output may enter data/raw/ or data/quarantine/ only."
  - "AirNow is near-real-time AQI context; final use depends on source descriptors, policy, evidence, review, and release controls."
  - "Specific connector modules, endpoint shape, cadence, descriptors, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# AirNow Connector

`connectors/airnow/`

`connectors/airnow/` is the source-specific connector lane for EPA AirNow intake and admission helpers.

It may contain code and connector documentation that supports governed intake of AirNow near-real-time AQI context. It must not become atmosphere truth, AQS archive authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** AirNow source-specific intake and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; AirNow source catalog page CONFIRMED as a documentation scaffold; connector implementation, endpoint shape, cadence, descriptors, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder for AirNow-specific connector code and documentation that supports governed source intake.

A connector may retrieve or stage candidate source material, preserve AirNow metadata, record retrieval context, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── airnow/
    └── README.md
```

Related roots:

```text
docs/sources/catalog/epa/airnow-api.md  # AirNow source-product catalog page
data/registry/sources/                  # source descriptors and activation state
data/raw/atmosphere/                    # admitted raw/staged AirNow payloads
data/quarantine/atmosphere/             # held material requiring review
data/receipts/atmosphere/               # process and validation receipts
data/proofs/atmosphere/                 # EvidenceBundles and proof packs
policy/                                  # source and publication rules
release/                                 # release decisions and rollback/correction state
```

> [!NOTE]
> Existing source documentation includes a proposed topology using `connectors/epa/airnow/`. This README covers the user-requested `connectors/airnow/` path and marks final connector placement as `NEEDS VERIFICATION` until an ADR or migration note settles direct-source versus EPA-family connector layout.

## Authority boundary

```text
connectors/airnow/
├── source-specific intake logic
├── endpoint and cadence notes
├── admission metadata helpers
├── source-role preservation helpers
└── connector documentation

OUTPUT LIMIT:
  data/raw/atmosphere/
  data/quarantine/atmosphere/

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
| Source adapter | AirNow client or endpoint adapter | Must preserve source role and retrieval context |
| Endpoint note | endpoint pattern, cadence note | Must remain checkable and descriptor-linked |
| Admission helper | checksum, content-type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Connector docs | README, endpoint notes, source-role notes | Must not claim admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed atmosphere or AQI records | `data/processed/` after governed processing |
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

## AirNow admission posture

AirNow connector output should preserve the anti-collapse boundaries documented for KFM atmosphere/air intake:

- AirNow AQI should not be treated as pollutant concentration by default;
- AirNow near-real-time context should not be treated as the final AQS archive;
- AirNow public context should be displayed only after governed release controls;
- AirNow-derived records should preserve observed time, ingested time, source role, and preliminary status;
- later AQS records may supersede or correct preliminary AirNow context.

## Validation expectations

Before relying on this connector, verify:

- source descriptors and source catalog pages exist;
- connector tests use no-network fixtures where practical;
- endpoint and cadence assumptions are documented and configurable;
- output paths are limited to raw/quarantine admission lanes;
- policy checks are invoked where required;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/airnow/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, source role, caveats, preliminary status, observed time, and ingested time are preserved.
4. Confirm endpoint and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/airnow/` contents are inventoried.
- [ ] AirNow source coverage is tied to a source descriptor.
- [ ] Endpoint and cadence assumptions are documented and tested.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] Final connector placement versus `connectors/epa/airnow/` is resolved or documented.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/airnow/` is for AirNow source-specific intake and admission code only. It is not a source of atmosphere truth, AQS authority, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>
