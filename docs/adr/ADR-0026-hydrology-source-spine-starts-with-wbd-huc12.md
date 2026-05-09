# ADR-0026: Hydrology source spine starts with wbd_huc12

- **Status:** PROPOSED
- **Date:** 2026-05-09
- **Deciders:** maintainers
- **Consulted:** stewards, domain leads
- **Informed:** contributors

## Context
PR-003 requires one concrete hydrology source descriptor so PR-004 can build a fixture-only proof slice without guessing source authority or rights posture.

## Decision
Use `wbd_huc12` as the first seeded hydrology source descriptor in `data/registry/hydrology/sources/wbd_huc12.yaml` and mirror it with a valid contract fixture.

## Consequences
Hydrology proof-slice work can reference a concrete, public-safe source descriptor; terms or cadence details can still be tightened in a follow-up if steward review finds drift.

## Alternatives considered
Keep all fields as `TBD` and defer source seeding to PR-004; rejected because PR-004 would then mix floor-repair and proof-slice scope.

## Compliance
- `python tools/validators/validate_source_descriptor.py --fixtures`
- `fixtures/contracts/v1/source/source_descriptor/valid/valid_wbd_huc12.json`
