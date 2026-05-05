# REORG Sprint Manifest
Status: CONFIRMED
Date: 2026-05-03
Scope: repo-wide inventory and domain documentation normalization.

## What changed
- Generated full tracked path inventory with functional families.
- Reorganized domain-lane docs into architecture/governance/operations/registers/tracking subhomes.
- Added authority conflict records and compatibility maps.
- Added repo-inventory validators and tests.

## What not to move without ADR
- `contracts/` <-> `schemas/` machine artifacts.
- `policy/` <-> `policies/` executable policy artifacts.
- data lifecycle roots (`data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published`, `data/receipts`, `data/proofs`).
