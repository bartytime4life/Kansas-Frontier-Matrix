# `schemas/contracts/v1/domains/settlement/`

## Purpose

Draft compatibility index for the singular `settlement` schema path.

This path is not confirmed canonical. The broader working schema lane is `schemas/contracts/v1/domains/settlements-infrastructure/`.

This README is documentation only. It is not a schema file, contract, policy, validator, pipeline, data, registry record, proof, receipt, catalog record, release record, public API behavior, map behavior, or publication authority.

## Status

| Field | Value |
|---|---|
| Status | Draft |
| Owning root | `schemas/` |
| Path role | Compatibility index |
| Canonical posture | PROPOSED / CONFLICTED |
| Working schema lane | `schemas/contracts/v1/domains/settlements-infrastructure/` |
| Current schema inventory | NEEDS VERIFICATION |
| Last reviewed | 2026-07-03 |

## Placement basis

`schemas/` owns machine-checkable shape.

ADR-0001 places domain schemas under `schemas/contracts/v1/domains/<domain>/...`.

Directory Rules keep schemas, contracts, policy, data, registries, proofs, receipts, fixtures, tests, pipelines, and releases in separate responsibility roots.

`docs/domains/settlements-infrastructure/CANONICAL_PATHS.md` identifies `settlements-infrastructure` as the working domain slug and records singular `settlement/` as conflicted path variance.

`contracts/domains/settlement/README.md` treats singular `settlement/` as a compatibility surface, not the canonical Settlements/Infrastructure contract home.

`contracts/domains/settlements-infrastructure/README.md` identifies `contracts/domains/settlements-infrastructure/` as the semantic contract lane and treats singular `settlement/` as a compatibility or variance surface pending ADR.

`schemas/contracts/v1/domains/settlements-infrastructure/README.md` exists as the broader schema lane scaffold, but it still needs expansion and does not prove schema maturity.

Current search found settlements-infrastructure contract and documentation surfaces, but did not confirm concrete settlement `.schema.json` files under this requested singular path.

## Related lanes

```text
schemas/contracts/v1/domains/settlement/                 # this compatibility index
schemas/contracts/v1/domains/settlements-infrastructure/  # broader schema lane
contracts/domains/settlement/                            # contract compatibility surface
contracts/domains/settlements-infrastructure/             # semantic contract lane
docs/domains/settlements-infrastructure/                  # domain doctrine and canonical paths
```

## Candidate schema names

| Candidate | Status |
|---|---|
| `settlement.schema.json` | NEEDS VERIFICATION |
| `municipality.schema.json` | NEEDS VERIFICATION |
| `census_place.schema.json` | NEEDS VERIFICATION |
| `townsite.schema.json` | NEEDS VERIFICATION |
| `ghost_town.schema.json` | NEEDS VERIFICATION |
| `place_identity.schema.json` | NEEDS VERIFICATION |
| `domain_observation.schema.json` | NEEDS VERIFICATION |
| `domain_feature_identity.schema.json` | NEEDS VERIFICATION |
| `domain_validation_report.schema.json` | NEEDS VERIFICATION |
| `public_safe_settlement_summary.schema.json` | NEEDS VERIFICATION |

## What belongs here

- This README.
- Compatibility notes for the singular `settlement` schema path.
- Migration notes after the accepted schema home is decided.
- Links to paired contracts, fixtures, validators, schema registry records, tests, policy references, release references, correction references, and rollback references.

## What does not belong here

- New canonical schema files until placement is resolved.
- Contract prose beyond this boundary README.
- Policy rules.
- Validator code.
- Pipeline code.
- Lifecycle data.
- Source registry records.
- Proof or receipt records.
- Catalog records.
- Release records.
- Public map or API artifacts.

## Review checklist

- [ ] Confirm whether this singular `settlement/` schema path should exist, redirect, or be retired.
- [ ] Confirm whether accepted settlement schemas belong under `schemas/contracts/v1/domains/settlements-infrastructure/`.
- [ ] Confirm paired contract paths.
- [ ] Confirm schema registry records.
- [ ] Confirm fixture paths.
- [ ] Confirm validator paths.
- [ ] Confirm CI schema-test coverage.
- [ ] Confirm policy, source-registry, release, correction, and rollback references.
