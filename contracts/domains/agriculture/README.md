# contracts/domains/agriculture

## Purpose

This directory is the Agriculture domain home for Markdown semantic contracts.

Contracts in this directory define object meaning, ownership boundaries, identity expectations, evidence expectations, lifecycle posture, and review expectations for Agriculture object families.

## Authority level

Draft semantic-contract directory.

Agriculture domain docs name this path as the proposed Markdown contract home. Current implementation coverage remains `NEEDS VERIFICATION` until files, schemas, tests, validators, fixtures, and related governance records are inspected.

## What belongs here

- Agriculture Markdown semantic contracts.
- Agriculture object-family contract READMEs.
- Contract-level compatibility notes.
- Contract validation checklists.
- Rollback notes for contract changes.

## What does not belong here

- JSON Schema files.
- Policy files.
- Validator code.
- Fixture or test data.
- Source registry records.
- Data lifecycle artifacts.
- Evidence/proof objects.
- Release records.
- API or UI implementation files.

## Object-family spine

Agriculture docs name these object families:

1. `CropObservation`
2. `FieldCandidate`
3. `CropRotation`
4. `YieldObservation`
5. `IrrigationLink`
6. `ConservationPractice`
7. `SoilCropSuitability`
8. `AgriculturalEconomyObservation`
9. `SupplyChainNode`
10. `DroughtStressIndicator`
11. `PestStressIndicator`
12. `AggregationReceipt`

Concrete object-level contracts in this directory remain `NEEDS VERIFICATION` unless separately confirmed.

## Related folders

- `contracts/README.md`
- `docs/domains/agriculture/OBJECTS.md`
- `docs/domains/agriculture/OBJECT_FAMILIES.md`
- `schemas/contracts/v1/domains/agriculture/`
- `policy/domains/agriculture/`
- `tests/domains/agriculture/`
- `fixtures/domains/agriculture/`
- `contracts/agriculture/`

## Compatibility note

The older `contracts/agriculture/` path exists and should be treated as a compatibility path until a migration note or ADR resolves the relationship.

## Validation

Before relying on this directory, verify the full file inventory, matching schemas, validators, fixtures, policies, and release posture.

## Rollback

Rollback target: prior scaffold content SHA `23c7287815a79cb6a79ab829ca3a5f7db33f5fc0`.

## Status

Draft. This README is a directory boundary document, not implementation proof.
