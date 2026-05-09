# tools/validators/_common

## Purpose
Shared JSON Schema validation helpers used by top-level and domain validator entrypoints.

## What does NOT belong here
Domain-specific schema assumptions, policy logic, network I/O, or ingestion/publishing workflow code.

## Inputs
Schema paths, fixture file paths, and repo root path for local `$id` registry construction.

## Outputs
Validator instances, deterministic pass/fail exit codes, and per-file validation status lines.

## Validation
Run `python tools/validators/validate_evidence_bundle.py --fixtures`, `make schemas`, and `make test`.

## Review burden
Low-to-moderate: changes here affect all schema validator scripts.

## Related folders
`tools/validators/`, `schemas/contracts/v1/`, `fixtures/contracts/v1/`, `tests/schemas/`.

## ADRs
ADR-0001 (`schemas/contracts/v1/` schema home).

## Last reviewed
2026-05-09.
