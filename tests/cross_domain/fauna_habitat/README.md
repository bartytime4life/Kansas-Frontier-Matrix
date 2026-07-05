# tests/cross_domain/fauna_habitat

Compatibility lane for Fauna x Habitat cross-domain tests.

## Status

Draft. This file was expanded from an empty placeholder on 2026-07-05.

## Purpose

This directory exists because KFM documentation currently references an underscore-form cross-domain test path, while the already-expanded test lane uses the hyphenated path `tests/cross-domain/habitat-fauna/`.

This README keeps the underscore path visible without creating a second source of authority.

## Primary lane

Use this confirmed README as the current detailed test-lane guide:

- `tests/cross-domain/habitat-fauna/README.md`

That lane describes the Habitat x Fauna boundary, current evidence limits, placement warning, authority split, and test expectations.

## Placement note

The canonical spelling is not settled.

Known forms:

| Path | Status |
|---|---|
| `tests/cross-domain/habitat-fauna/` | Detailed README confirmed. |
| `tests/cross_domain/fauna_habitat/` | This compatibility README. |
| `tests/cross_domain/README.md` | Not found in this pass. |

Until an ADR or maintainer decision resolves the spelling, do not duplicate test modules across both forms. Prefer one implementation lane and keep the other as a redirect or compatibility note.

## Boundary

This directory must not become a new domain, a duplicate fixture home, a policy home, a schema home, a contract home, a validator home, a lifecycle data home, or a release home.

## What belongs here

- This README.
- Compatibility notes.
- Migration notes if the underscore path becomes canonical.
- Pointers to the accepted test implementation lane.

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
find tests/cross_domain/fauna_habitat -maxdepth 5 -type f | sort
find tests/cross-domain/habitat-fauna -maxdepth 5 -type f | sort
pytest tests/cross-domain/habitat-fauna tests/policy || true
```

Replace `|| true` with fail-closed CI behavior once the accepted path and test commands are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should the canonical path use `cross-domain/habitat-fauna` or `cross_domain/fauna_habitat`? | NEEDS VERIFICATION |
| Should this file remain a redirect after path normalization? | NEEDS VERIFICATION |
| Which path should CI execute? | NEEDS VERIFICATION |
