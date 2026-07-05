# tests/cross_domain

Compatibility parent lane for underscore-form cross-domain tests in KFM.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory exists because some KFM documentation and paths use the underscore spelling `tests/cross_domain/`, while another active parent lane uses the hyphenated spelling `tests/cross-domain/`.

This README keeps the underscore path visible without creating a second source of authority.

## Related lanes

| Path | Role | Status |
|---|---|---|
| `tests/cross-domain/README.md` | Hyphenated parent lane. | Confirmed. |
| `tests/cross-domain/habitat-fauna/README.md` | Detailed Habitat x Fauna test lane. | Confirmed. |
| `tests/cross_domain/fauna_habitat/README.md` | Underscore compatibility child lane. | Confirmed. |

## Placement rule

The canonical spelling is not settled. Until an ADR or maintainer decision resolves the path convention, do not duplicate test modules across the hyphenated and underscore trees.

Use one implementation lane and keep the other as a redirect, compatibility note, or migration target.

## Boundary

This directory is a test compatibility/index lane only. It must not become a new domain, a duplicate fixture home, a policy home, a schema home, a contract home, a validator home, a lifecycle data home, or a release home.

## What belongs here

- This README.
- Compatibility notes.
- Migration notes if the underscore path becomes canonical.
- Pointers to the accepted implementation lane.

## What does not belong here

- Duplicate test modules if the hyphenated lane remains active.
- Domain implementation code.
- Contracts or schemas.
- Policy rules.
- Validator implementation.
- Lifecycle or release records.
- Generated text treated as authority.

## Validation

```bash
find tests/cross_domain -maxdepth 5 -type f | sort
find tests/cross-domain -maxdepth 5 -type f | sort
pytest tests/cross-domain tests/policy tests/api || true
```

Replace `|| true` with fail-closed CI behavior once the accepted path and test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should the canonical parent path be `tests/cross-domain/` or `tests/cross_domain/`? | NEEDS VERIFICATION |
| Should underscore files remain redirects after path normalization? | NEEDS VERIFICATION |
| Which path should CI execute? | NEEDS VERIFICATION |
