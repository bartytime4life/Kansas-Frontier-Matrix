# Schema Home Audit

Date: 2026-05-05

## Scope
Audit of machine-schema placement for ADR-0001 enforcement.

## Rule
Machine schemas (`*.schema.json`) must live under `schemas/contracts/v1/`.

Non-canonical surfaces (`contracts/`, `jsonschema/`) are only allowed when documented with exemption phrases:
- human contract docs
- compatibility examples
- generated mirrors

## Audit result
- Command: `python tools/check_schema_home.py`
- Outcome: **PASS**
- Violations found: **0**

## Notes
- Test fixtures for PASS/FAIL scenarios are stored under `fixtures/policy/schema_home/` and intentionally excluded from repository-wide enforcement scanning.
