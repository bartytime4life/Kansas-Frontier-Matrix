# tests/cross-domain

Parent lane for cross-domain tests in KFM.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory is for tests that verify relations between domains keep responsibility boundaries intact.

Cross-domain tests should check that:

- each object remains owned by its correct domain;
- relations cite the owning domain instead of copying its truth;
- evidence, policy, and release posture are preserved;
- unsupported relations abstain, deny, or fail safely;
- test files do not become contracts, schemas, policy, validators, lifecycle records, or release records.

## Current child lanes

| Lane | Purpose | Status |
|---|---|---|
| `habitat-fauna/` | Habitat and Fauna relation tests. | README confirmed; implementation needs verification. |

## Placement note

This path uses `tests/cross-domain/`. Related documentation also mentions `tests/cross_domain/`. The canonical spelling still needs maintainer or ADR confirmation. Do not create a parallel tree without a migration note.

## What belongs here

- Cross-domain test indexes.
- Test modules for domain relation behavior.
- Test-only references to contracts, schemas, policy, fixtures, validators, data, and release records.

## What does not belong here

- Domain implementation code.
- Canonical contracts or schemas.
- Policy rules.
- Validator implementation.
- Lifecycle or release records.
- Generated text treated as authority.

## Validation

```bash
find tests/cross-domain -maxdepth 5 -type f | sort
pytest tests/cross-domain tests/policy tests/api || true
```
