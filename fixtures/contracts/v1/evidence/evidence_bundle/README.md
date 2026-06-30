# `evidence_bundle` fixtures

Fixture root for the KFM `evidence_bundle` contract schema examples.

## Inventory

| Lane | File | Role |
|---|---|---|
| `valid/` | `valid_1.json` | Positive fixture with `bundle_id` and the required top-level fields. |
| `invalid/` | `invalid_1.json` | Negative fixture that omits required `bundle_id`. |
| `invalid/` | `invalid_1.expected_error.txt` | Current expected-error matcher: `required`. |

## Schema and harness

| Item | Path | Status |
|---|---|---|
| Schema | `../../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json` | CONFIRMED |
| Contract doc | `../../../../../contracts/evidence/evidence_bundle.md` | CONFIRMED |
| Validator wrapper | `../../../../../tools/validators/validate_evidence_bundle.py` | CONFIRMED / NOT RUN |
| Schema test harness | `../../../../../tests/schemas/test_common_contracts.py` | CONFIRMED / NOT RUN |

## Notes

- This file replaces a blank README.
- This directory contains fixture inputs only.
- Schema authority stays with the schema file.
- Contract meaning stays with the contract doc.
- Validator and pytest behavior were not executed during this README update.

## Maintenance checklist

- Keep passing examples under `valid/valid_<n>.json`.
- Keep failing examples under `invalid/invalid_<n>.json`.
- Keep expected error text beside the invalid fixture it describes.
- Update fixtures when the schema changes.
- Run the relevant schema tests before promotion.
