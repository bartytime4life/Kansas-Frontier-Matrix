# Archaeology fixtures

`fixtures/domains/archaeology/`

Status: draft / fixture index.

This directory groups Archaeology-domain fixture lanes used by bounded tests, validators, helpers, renderer checks, and documentation examples. Files here are examples only. They are not authoritative project records, source records, evidence, approvals, release state, or published artifacts.

## Child lanes

| Lane | Purpose | Status |
|---|---|---|
| `golden/` | Stable expected-output examples. | README present; payload inventory NEEDS VERIFICATION. |
| `invalid/` | Negative examples and expected failures. | README present; payload inventory NEEDS VERIFICATION. |
| `site/` | Site-shaped fixture examples. | README present; payload inventory NEEDS VERIFICATION. |
| `synthetic_archaeological_site/` | Synthetic site-shaped examples. | README present; payload inventory NEEDS VERIFICATION. |
| `synthetic_candidate_feature/` | Synthetic candidate-shaped examples. | README present; payload inventory NEEDS VERIFICATION. |
| `synthetic_publication_transform_receipt/` | Synthetic transform-receipt-shaped examples. | README present; payload inventory NEEDS VERIFICATION. |
| `synthetic_steward_review/` | Synthetic review-shaped examples. | README present; payload inventory NEEDS VERIFICATION. |
| `valid/` | Positive examples for bounded checks. | README present; payload inventory NEEDS VERIFICATION. |

## Repo fit

Upstream references:

- `../../../docs/domains/archaeology/OBJECT_FAMILIES.md`
- `../../../docs/domains/archaeology/CANONICAL_PATHS.md`
- `../../../policy/domains/archaeology/README.md`
- `../../../docs/doctrine/directory-rules.md`

Downstream consumers may include:

- `../../../tests/domains/archaeology/`
- `../../../schemas/contracts/v1/domains/archaeology/`
- archaeology fixture-specific helpers or renderer checks, when implemented

## Accepted material

This fixture root may contain:

- small synthetic `*.input.json` examples
- small `*.expected.json` examples
- snapshot examples for bounded tests
- `valid/valid_<n>.json` examples inside child lanes
- `invalid/invalid_<n>.json` examples inside child lanes
- `invalid/invalid_<n>.expected_error.txt` files
- local README files that explain fixture intent and boundaries

## Exclusions

Do not use this fixture root for:

- authoritative records
- source-system exports
- EvidenceBundles, proof packs, or receipt storage
- policy rules or policy decisions
- review approvals
- release manifests, release candidates, or published artifacts
- app, package, pipeline, validator, or schema implementation code

## Maintenance notes

- Keep examples synthetic, compact, deterministic, and reviewable.
- Keep each fixture tied to a known test, validator, renderer check, helper, or documentation example.
- Keep pass/fail expectations explicit.
- Update this parent index when child lanes are added, removed, renamed, or promoted.
- Run relevant tests before claiming fixture validity.

## Verification status

- Parent README: updated from a greenfield stub.
- Child README coverage: PARTIAL; based on current search and recent updates.
- Payload inventory: NEEDS VERIFICATION.
- Tests and validators: NOT RUN.
