# `schemas/contracts/v1/domains/habitat/ecoregions/`

## Purpose

Draft schema index for Habitat ecoregion and landscape-regionalization object shapes.

This path is for schema placement notes and future JSON Schema files only. It does not define contract meaning, policy, source registry records, pipeline behavior, data products, or release state.

## Status

| Field | Value |
|---|---|
| Status | Draft |
| Owning root | `schemas/` |
| Parent lane | `schemas/contracts/v1/domains/habitat/` |
| Path role | Ecoregions schema sublane index |
| Canonical posture | NEEDS VERIFICATION |
| Current schema inventory | NEEDS VERIFICATION |
| Last reviewed | 2026-07-03 |

## Placement basis

`schemas/` is the machine-checkable shape root.

ADR-0001 places domain schemas under `schemas/contracts/v1/domains/<domain>/...`.

Directory Rules keep machine shape, contract meaning, policy, data, registries, pipelines, fixtures, tests, and release records in separate responsibility roots.

Habitat domain docs name `schemas/contracts/v1/domains/habitat/` as the Habitat schema lane.

Habitat ecoregions docs name this path as the proposed schema home for ecoregion shapes.

Current search found related docs, source-registry, and pipeline lanes, but did not confirm concrete schema files here.

## Related lanes

```text
schemas/contracts/v1/domains/habitat/ecoregions/   # this schema index
schemas/contracts/v1/domains/habitat/              # parent Habitat schema lane
contracts/domains/habitat/                         # meaning, not schema shape
docs/domains/habitat/sublanes/ecoregions.md        # prose doctrine
data/registry/sources/habitat/ecoregions/          # source descriptors, not schema shape
pipelines/domains/habitat/ecoregions/              # pipeline logic, not schema shape
```

## Candidate schema names

| Candidate | Status |
|---|---|
| `ecoregion.schema.json` | NEEDS VERIFICATION |
| `ecoregion_snapshot.schema.json` | NEEDS VERIFICATION |
| `ecoregion_framework.schema.json` | NEEDS VERIFICATION |
| `ecoregion_level.schema.json` | NEEDS VERIFICATION |
| `ecoregion_context_join.schema.json` | NEEDS VERIFICATION |
| `ecoregion_crosswalk.schema.json` | NEEDS VERIFICATION |
| `ecoregion_public_derivative.schema.json` | NEEDS VERIFICATION |

## What belongs here

- This README.
- Future machine-checkable Habitat ecoregion JSON Schema files after placement is confirmed.
- Schema index notes.
- Schema migration notes.
- Links to paired contracts, fixtures, validators, schema registry records, and tests.

## What does not belong here

- Contract prose.
- Policy rules.
- Validator code.
- Pipeline code.
- Source records.
- Data payloads.
- Receipt records.
- Proof records.
- Catalog records.
- Release records.
- Public map artifacts.
- Claims that a schema is complete without fixtures, validators, registry records, and review support.

## Review checklist

- [ ] Confirm CODEOWNERS.
- [ ] Confirm whether this sublane is accepted or only proposed.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm whether the parent Habitat schema README should index this lane.

## Review trigger

Update this README when an ecoregion schema is added, a schema-home decision is made, a migration note is created, or validator/fixture/schema-registry support is confirmed.
