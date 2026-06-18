<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/connectors-atmosphere-readme
title: connectors/atmosphere/ — Atmosphere Source Connector Lane
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Atmosphere/Air steward · Source steward · Connector steward · Data steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/domains/atmosphere/README.md
  - ../../docs/domains/atmosphere/SOURCE_INDEX.md
  - ../../docs/domains/atmosphere/SOURCE_REGISTRY.md
  - ../../docs/sources/catalog/epa/airnow-api.md
  - ../../data/registry/sources/
  - ../../data/raw/atmosphere/
  - ../../data/quarantine/atmosphere/
  - ../../data/receipts/atmosphere/
  - ../../data/proofs/atmosphere/
  - ../../policy/domains/atmosphere/
  - ../../schemas/contracts/v1/domains/atmosphere/
  - ../../release/
tags: [kfm, connectors, atmosphere, air, weather, smoke, aqi, source-admission, raw, quarantine, governance]
notes:
  - "connectors/atmosphere/ is for atmosphere and air source-specific intake and admission code only."
  - "Connector output may enter data/raw/atmosphere/ or data/quarantine/atmosphere/ only."
  - "Atmosphere connectors preserve source role and anti-collapse boundaries: AQI is not concentration, AOD is not PM2.5, model fields are not observations, and KFM is not an official alerting surface."
  - "Specific connector modules, source coverage, endpoint behavior, tests, fixtures, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Connectors

`connectors/atmosphere/`

`connectors/atmosphere/` is the source-specific connector lane for atmosphere, air-quality, weather, smoke, aerosol, climate, and model-context intake and admission helpers.

It may contain code and connector documentation that supports governed source intake. It must not become atmosphere truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release approval, official alerting, or publication authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `connectors/`  
> **Responsibility:** atmosphere source-specific intake and admission code  
> **Truth posture:** README path CONFIRMED; parent `connectors/` root CONFIRMED as source-specific fetch/admission root; atmosphere documentation root CONFIRMED as canonical domain documentation; connector implementation, source coverage, endpoint behavior, tests, fixtures, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> Atmosphere connector output is admission material. It is not proof of a final air-quality, weather, smoke, aerosol, climate, forecast, or advisory-context claim. Treat source records as candidates until source descriptors, policy checks, evidence closure, review state, and release controls are satisfied.

## Purpose

Use this folder for atmosphere-specific connector code and documentation that supports governed source intake.

A connector may retrieve or stage candidate source material, preserve source metadata, record retrieval context, and produce admission outputs for lifecycle review. It must not decide truth, write processed records, create catalog/triplet authority, close EvidenceBundles, release artifacts, or bypass steward review.

## Canonical fit

```text
connectors/
└── atmosphere/
    └── README.md
```

Related roots:

```text
docs/domains/atmosphere/              # canonical human-facing domain documentation
data/registry/sources/                # source descriptors and activation state
data/raw/atmosphere/                  # admitted raw/staged source payloads
data/quarantine/atmosphere/           # held material requiring review
data/receipts/atmosphere/             # process and validation receipts
data/proofs/atmosphere/               # EvidenceBundles and proof packs
policy/domains/atmosphere/            # policy/admissibility rules
schemas/contracts/v1/domains/atmosphere/ # machine-checkable shapes, pending slug verification
release/                              # release decisions and rollback/correction state
```

## Authority boundary

```text
connectors/atmosphere/
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
| Source adapter | connector for one approved atmosphere source family | Must preserve source role and provenance |
| Endpoint note | endpoint pattern, cadence note | Must remain checkable and descriptor-linked |
| Admission helper | checksum, content type, timestamp, source metadata | Must write only raw/quarantine admission outputs |
| Source-role helper | provisional/aggregate/context marker preservation | Must not strengthen source authority |
| Connector docs | source-specific notes | Must not claim admission or release state unless verified |
| Test references | no-network fixture notes | Tests and fixtures live in their owning roots |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Processed atmosphere, air-quality, weather, smoke, AOD, climate, or model records | `data/processed/` after governed processing |
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

## Atmosphere admission posture

Atmosphere source intake must preserve domain anti-collapse boundaries:

- AQI is not pollutant concentration by default;
- AOD is not PM2.5;
- model fields are not observations;
- low-cost sensor records require correction/caveat/confidence handling before public release;
- advisory context is not an official public instruction surface;
- atmosphere context may inform hazards, agriculture, hydrology, habitat, fauna, and flora, but it does not own those domains' canonical claims.

Connector code should preserve source identity, source role, observed/source time, ingested time, content digest, limitation notes, caveat text, freshness/provisional status, and quarantine reason when review is required.

## Validation expectations

Before relying on this connector, verify:

- source descriptors exist and are active;
- connector tests use no-network fixtures where practical;
- endpoint and cadence assumptions are documented and configurable;
- output paths are limited to raw/quarantine admission lanes;
- policy checks are invoked where required;
- anti-collapse fields and caveats are preserved;
- downstream receipts/proofs/release records are produced only by governed stages outside this connector.

## Safe change pattern

For changes under `connectors/atmosphere/`:

1. Confirm the file is connector code, connector docs, or connector-facing support material.
2. Confirm it does not write processed, catalog, triplet, published, or release records directly.
3. Confirm source descriptors, source role, caveats, preliminary status, observed/source time, and ingested time are preserved.
4. Confirm endpoint and cadence assumptions are configurable and testable.
5. Confirm tests/fixtures are updated or explicitly marked `NEEDS VERIFICATION`.
6. Update docs or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `connectors/atmosphere/` contents are inventoried.
- [ ] Atmosphere source coverage is tied to source descriptors.
- [ ] Endpoint and cadence assumptions are documented and tested.
- [ ] Outputs are verified to enter only raw/quarantine admission lanes.
- [ ] No processed, catalog, triplet, published, release, schema, policy, proof, receipt, registry, or package authority lives here.
- [ ] No-network tests and fixtures are verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`connectors/atmosphere/` is for atmosphere source-specific intake and admission code only. It is not a source of atmosphere truth, policy authority, schema authority, catalog/triplet authority, evidence closure, release authority, official alerting authority, publication authority, or reusable domain package authority.

<p align="right"><a href="#top">Back to top</a></p>
