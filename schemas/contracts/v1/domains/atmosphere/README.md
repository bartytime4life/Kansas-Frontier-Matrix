# `schemas/contracts/v1/domains/atmosphere/` — Atmosphere Domain Schema Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-domains-atmosphere-readme
title: schemas/contracts/v1/domains/atmosphere/ — Atmosphere Domain Schema Index
version: v1
status: draft
policy_label: public
owners:
  - <schema-steward>
  - <atmosphere-domain-steward>
  - <air-quality-steward>
  - <contract-steward>
  - <validation-steward>
  - <docs-steward>
updated: 2026-07-03
tags: [kfm, schemas, contracts, v1, domains, atmosphere, air, climate, smoke, receipts, registry, json-schema]
[/KFM_META_BLOCK_V2] -->

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![domain](https://img.shields.io/badge/domain-atmosphere-green)
![posture](https://img.shields.io/badge/posture-domain--schema--index-orange)
![canonical](https://img.shields.io/badge/canonical-PROPOSED-yellow)

## Purpose

`schemas/contracts/v1/domains/atmosphere/` is the draft Atmosphere domain schema lane.

This path is for machine-checkable Atmosphere schema shapes: JSON Schema files, schema-family README files, schema index notes, migration notes, and links to paired contracts, fixtures, validators, registry records, tests, policy references, receipt references, and release references.

This path is not a home for Atmosphere contract prose, policy rules, validator code, packages, pipelines, lifecycle data, source registry records, emitted receipts, proof outputs, catalog records, or release records.

This README is documentation only. It is not itself a schema file, contract prose, policy, validator code, lifecycle data, registry data, proof output, receipt instance, source descriptor instance, or release authority.

## Status & authority

| Field | Value |
|---|---|
| Document type | Atmosphere domain schema README |
| Owning root | `schemas/` |
| Requested path | `schemas/contracts/v1/domains/atmosphere/` |
| Status | Draft |
| Authority level | Domain schema index guidance. Schema files, paired contracts, registry records, validators, fixtures, tests, ADRs, policy records, receipt records, release records, and steward decisions outrank this README. |
| Path posture | Current-session evidence confirms this README existed as a greenfield scaffold before this update. |
| Canonical posture | PROPOSED Atmosphere domain schema lane under ADR-0001. Implementation completeness remains NEEDS VERIFICATION. |
| Shorter alias lane | `schemas/contracts/v1/atmosphere/` exists as a compatibility/index lane pointing toward this domain path. |
| Known child lanes | `receipts/` and `registry/` READMEs exist and are draft indexes. |
| Known schema file | `atmosphere_air_decision_envelope.schema.json` exists as a PROPOSED scaffold. |
| Required reviewers | Schema steward, Atmosphere domain steward, air-quality steward where applicable, contract steward, validation steward, policy steward where applicable, release steward where applicable, and docs steward. |

## Placement basis

Current-session evidence confirms `schemas/README.md` defines `schemas/` as the machine-checkable shape root and says schemas pair one-to-one with `contracts/`.

Current-session evidence confirms ADR-0001 says domain-specific schemas nest under `schemas/contracts/v1/domains/<domain>/...`, while `contracts/` retains object meaning and `schemas/` owns machine-checkable shape.

Current-session evidence confirms `schemas/contracts/v1/atmosphere/README.md` is a shorter Atmosphere compatibility lane and points to this domain path as the canonical Atmosphere schema lane.

Current-session evidence confirms `schemas/contracts/v1/domains/atmosphere/receipts/README.md` exists as a draft Atmosphere receipt schema index.

Current-session evidence confirms `schemas/contracts/v1/domains/atmosphere/registry/README.md` exists as a draft Atmosphere registry schema index.

Current-session evidence confirms `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json` exists as a PROPOSED scaffold schema.

Current-session evidence confirms this path already had a greenfield scaffold. This update narrows the README to the actual `schemas/` responsibility: machine-checkable shape and schema-index support only.

## Repo fit

```text
schemas/
├── README.md
└── contracts/
    └── v1/
        ├── atmosphere/                         # shorter compatibility/index lane
        └── domains/
            └── atmosphere/
                ├── README.md                   # you are here
                ├── atmosphere_air_decision_envelope.schema.json
                ├── receipts/
                │   └── README.md
                └── registry/
                    └── README.md

contracts/
└── domains/
    └── atmosphere/                             # semantic meaning; not schema shape

policy/
└── domains/
    └── atmosphere/                             # admissibility/policy; not schema shape

fixtures/
└── domains/
    └── atmosphere/                             # test examples; coverage NEEDS VERIFICATION

data/                                            # lifecycle, registry, proof, receipt roots; not schema home

release/                                         # release decisions and release records; not schema home
```

## Current-session related evidence

| Evidence | Status |
|---|---|
| `schemas/contracts/v1/domains/atmosphere/README.md` | Greenfield scaffold before this update. |
| `schemas/README.md` | Confirms `schemas/` owns machine-checkable shape and pairs with `contracts/`. |
| ADR-0001 | Confirms domain schemas nest under `schemas/contracts/v1/domains/<domain>/...`. |
| `schemas/contracts/v1/atmosphere/README.md` | Existing shorter compatibility index for Atmosphere schema placement. |
| `schemas/contracts/v1/domains/atmosphere/receipts/README.md` | Existing Atmosphere receipts schema index. |
| `schemas/contracts/v1/domains/atmosphere/registry/README.md` | Existing Atmosphere registry schema index. |
| `schemas/contracts/v1/domains/atmosphere/atmosphere_air_decision_envelope.schema.json` | Existing PROPOSED scaffold schema. |

This README does not verify complete Atmosphere schema coverage, schema registry entries, fixture coverage, validator wiring, CI behavior, policy behavior, release integration, runtime behavior, or public API/UI behavior.

## Current schema inventory

| Schema file | Paired contract | Status | Notes |
|---|---|---|---|
| `atmosphere_air_decision_envelope.schema.json` | `contracts/domains/atmosphere/atmosphere_air_decision_envelope.md` in schema metadata; current contract file casing/path alignment remains NEEDS VERIFICATION | PROPOSED / scaffold | Schema has `$schema`, `$id`, title, description, empty `properties`, `additionalProperties: true`, and `x-kfm.status: PROPOSED`. |

## Current child lanes

| Child path | Status | Responsibility |
|---|---|---|
| `receipts/` | Draft index | Atmosphere receipt schema index; must not store emitted receipt instances or collapse receipts with proofs, catalog records, or release records. |
| `registry/` | Draft index | Atmosphere registry schema index; must not store actual registry records or SourceDescriptor instances. |

## Candidate contract inventory

Current-session and prior adjacent evidence indicate these Atmosphere semantic contracts may require paired schemas after steward review:

| Contract surface | Status | Schema note |
|---|---|---|
| `contracts/domains/atmosphere/AtmosphereAirDecisionEnvelope.md` | Observed in current-session related evidence | Paired scaffold schema exists, but path/casing alignment remains NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/AirStation.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/AirObservation.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/PM25Observation.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/OzoneObservation.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/AODRaster.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/ForecastContext.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/AdvisoryContext.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/SmokeContext.md` | Observed in prior Atmosphere evidence | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/WindField.md` | Observed in search results | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/WeatherStation.md` | Observed in search results | Paired schema NEEDS VERIFICATION. |
| `contracts/domains/atmosphere/ClimateNormal.md` | Observed in search results | Paired schema NEEDS VERIFICATION. |

## Schema-lane responsibilities

| Responsibility | Expectation |
|---|---|
| Domain schema index | List Atmosphere schema files and child schema lanes as they are verified. |
| Contract pairing | Link each schema to paired semantic contracts under `contracts/domains/atmosphere/` or another verified contract lane. |
| Alias discipline | Keep `schemas/contracts/v1/atmosphere/` as compatibility/index unless an ADR or migration note changes it. |
| Child-lane discipline | Keep `receipts/` and `registry/` as scoped sublanes with their own review status. |
| Boundary preservation | Keep policy, fixtures, validators, lifecycle data, source registry records, receipt instances, proofs, catalog records, and release records in their own responsibility roots. |
| Drift prevention | Prevent duplicate canonical schema definitions across short alias, domain root, child lanes, and cross-domain lanes. |
| Fixture linkage | Point to valid and invalid fixtures when verified. |
| Validator linkage | Point to validators or CI checks when verified. |
| Registry linkage | Point to schema registry records when verified. |
| Review status | Mark unverified implementation claims as NEEDS VERIFICATION. |

## What belongs here

- This README.
- Machine-checkable Atmosphere JSON Schema files.
- Atmosphere schema-family and child-lane README files.
- Schema index notes.
- Migration notes for Atmosphere schema placement.
- Drift notes about duplicate or stale Atmosphere schema paths.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, receipt references, release references, and tests.

## What does not belong here

- Contract prose.
- Policy rules.
- Validator implementation code.
- Runtime code.
- Packages or pipeline implementation.
- Lifecycle data payloads.
- Source registry records or SourceDescriptor instances.
- Emitted receipt instances.
- Proof outputs.
- Catalog records.
- Release records, release manifests, or release decisions.
- Public API or map/UI behavior.
- Cross-domain schemas that belong under `schemas/contracts/v1/cross/`.
- Generic reusable schemas that belong under `schemas/contracts/v1/common/`.
- Claims that a schema is complete without fixtures, validators, registry records, and review support.

## Schema status values

Use finite status values where possible:

| Status | Meaning |
|---|---|
| `STUB` | Schema exists but is not field-complete. |
| `DRAFT_SCHEMA` | Schema has meaningful fields but still needs review and test support. |
| `ACTIVE_SCHEMA` | Schema has accepted contract pairing, fixtures, validator support, registry record, and review status. |
| `EXTENSION_INDEX` | Child lane indexes extension schemas but has not accepted a concrete schema yet. |
| `MIRROR` | Schema mirrors another accepted schema location. |
| `TRANSITIONAL` | Schema is awaiting migration to the accepted home. |
| `DEPRECATED` | Schema should no longer receive new consumers. |
| `NEEDS_VERIFICATION` | Pairing, fixture, validator, registry, or CI support has not been verified. |

## Minimal schema note

```markdown
# <atmosphere-schema-note-id>

## Status
STUB / DRAFT_SCHEMA / ACTIVE_SCHEMA / EXTENSION_INDEX / MIRROR / TRANSITIONAL / DEPRECATED / NEEDS_VERIFICATION

## Schema path
<schemas/contracts/v1/domains/atmosphere/...>

## Paired contract
<contracts/domains/atmosphere/... or N/A>

## Child lane
<root / receipts / registry / other / N/A>

## Fixtures
<fixtures path or N/A>

## Validator
<tools/validators path or N/A>

## Policy references
<policy path or N/A>

## Receipt or registry references
<data receipt/registry path or N/A>

## Release references
<release path or N/A>

## Notes
<short note grounded in repo evidence>

## Follow-up
<open items or none>
```

## Review checklist

- [ ] Schema has a stable `$id`.
- [ ] Schema has `$schema` set to JSON Schema draft 2020-12 unless an ADR says otherwise.
- [ ] Paired contract path is linked or marked NEEDS VERIFICATION.
- [ ] Schema registry entry is linked or marked NEEDS VERIFICATION.
- [ ] Valid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Invalid fixtures are linked or marked NEEDS VERIFICATION.
- [ ] Validator path is linked or marked NEEDS VERIFICATION.
- [ ] CI/schema-test support is linked or marked NEEDS VERIFICATION.
- [ ] Child-lane placement is justified when schema is not at the Atmosphere schema root.
- [ ] Short alias path does not contain duplicate canonical schema definitions.
- [ ] Policy, data, receipt-instance, registry-instance, proof, catalog, and release records remain outside `schemas/`.
- [ ] Any migration or compatibility claim cites an ADR, migration note, or verified repo evidence.

## Naming guidance

Recommended schema filename pattern:

```text
<object_name>.schema.json
```

Examples:

```text
atmosphere_air_decision_envelope.schema.json
air_station.schema.json
air_observation.schema.json
pm25_observation.schema.json
ozone_observation.schema.json
aod_raster.schema.json
forecast_context.schema.json
advisory_context.schema.json
smoke_context.schema.json
wind_field.schema.json
weather_station.schema.json
climate_normal.schema.json
```

Use lowercase snake_case for schema filenames unless the schema registry or ADR specifies otherwise. If an existing contract path uses CamelCase or hyphenated naming while schema metadata uses snake_case, record the conflict and do not silently rename without migration notes.

## Open verification

- [ ] Confirm CODEOWNERS for `schemas/contracts/v1/domains/atmosphere/`.
- [ ] Confirm complete Atmosphere schema inventory.
- [ ] Confirm whether `atmosphere_air_decision_envelope.schema.json` should remain permissive or become strict.
- [ ] Resolve any casing/path mismatch between `AtmosphereAirDecisionEnvelope.md` and `atmosphere_air_decision_envelope.schema.json`.
- [ ] Confirm whether `receipts/` is an accepted Atmosphere schema subfamily.
- [ ] Confirm whether `registry/` is an accepted Atmosphere schema subfamily.
- [ ] Confirm paired contract paths for all accepted schemas.
- [ ] Confirm schema registry records.
- [ ] Confirm valid fixture paths.
- [ ] Confirm invalid fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, receipt, registry, proof, catalog, and release references for Atmosphere schemas.
- [ ] Confirm whether `schemas/contracts/v1/atmosphere/README.md` remains a compatibility/index lane.
- [ ] Confirm whether `schemas/README.md` should index this Atmosphere domain schema lane.

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-03 |
| Review status | Draft README replacing greenfield scaffold |
| Next review trigger | New Atmosphere schema, child-lane decision, schema-home migration, validator update, fixture update, schema registry update, ADR update, Atmosphere contract update, policy update, receipt/registry reference update, release reference update, or compatibility-lane decision |
