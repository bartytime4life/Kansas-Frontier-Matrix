<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/analytical-view-manifest
title: AnalyticalViewManifestCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Data contract steward · Analytics steward · Database steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; data; analytics; database-view; materialized-view; manifest
responsibility: Define fixture-only analytical-view definition, upstream, validation, materialization, mutation, predicate-guard, and rollback declarations without creating a view, executing SQL, mutating data, or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive manifest; UNKNOWN database portability and consumer adoption; NEEDS VERIFICATION data, analytics, database, security, and validation review plus hosted exact-head CI"
related:
  - ./layer_manifest.md
  - ../governance/query_run_record.md
  - ../ui/view_registry_profile.md
  - ../../schemas/contracts/v1/data/analytical_view_manifest.schema.json
  - ../../fixtures/contracts/v1/data/analytical_view_manifest/cases.json
  - ../../tools/validators/data/validate_analytical_view_manifest.py
  - ../../tests/validators/data/test_validate_analytical_view_manifest.py
  - ../../docs/intake/exploratory/pass-18-analytical-view-manifest-source-map.md
tags: [kfm, data, analytics, database-view, materialized-view, check-option, fixture-only]
notes:
  - "Implements a dependency-closed adaptation of supplied Pass 18 cards KFM-P18-INV-107 and KFM-P18-INV-311."
  - "A passing manifest never creates or updates a database view."
[/KFM_META_BLOCK_V2] -->

# AnalyticalViewManifestCandidate

`AnalyticalViewManifestCandidate` is an additive data-contract carrier for one
database view, materialized view, or equivalent derived view. It makes the
definition identity, purpose, upstream dependencies, hidden analytical
semantics, validation posture, refresh behavior, mutation posture, predicate
guard, review references, correction path, and rollback target inspectable.

It adapts supplied Pass 18 cards `KFM-P18-INV-107` and
`KFM-P18-INV-311` without creating the proposed SQL contract registry or a
runtime database integration.

## Boundary

A validator `PASS` proves only that the closed synthetic manifest and its
deterministic identity are internally coherent. It does not:

- parse or execute SQL, create/replace/drop a view, or inspect a database catalog;
- authenticate a definition digest, validation report, fixture receipt, policy, review, correction, or rollback reference;
- read, insert, update, delete, deduplicate, aggregate, or materialize data;
- establish source, evidence, rights, sensitivity, or lifecycle truth; or
- promote, release, deploy, publish, or authorize public use.

Raw SQL, parameters, connection strings, credentials, database endpoints, and
table paths are excluded. Definition and dependency identities are opaque refs
and SHA-256 digests only.

## Manifest surfaces

| Surface | Required declaration |
|---|---|
| Identity | Stable view reference, view kind, bounded purpose, and definition digest. |
| Definition | Opaque dialect profile for SQL views and fixed-false raw-SQL storage. |
| Upstream | Canonical dataset references and optional lineage reference. |
| Hidden semantics | Separate join, filter, aggregate, deduplication, and window-disclosure references. |
| Validation | `VALIDATED`, `PARTIAL`, `NOT_VALIDATED`, or `ERROR`, plus opaque report/fixture references. |
| Materialization | Query-time, scheduled, event-driven, manual, not-applicable, or unresolved refresh posture. |
| Mutation | Read-only, governed-updatable, direct-mutation-prohibited, or unresolved. |
| Correction | Review references, correction-policy reference, and rollback target. |

## Mutation and predicate guard

- `READ_ONLY` carries no mutation predicate, check option, or mutation policy.
- `DIRECT_MUTATION_PROHIBITED` carries an explicit mutation-policy reference and no write-through guard.
- `UPDATABLE_GOVERNED` is internal-only in this v1 profile. It must bind the
  manifest's declared filter predicate, a mutation-policy reference, and
  `LOCAL`, `CASCADED`, or `EQUIVALENT_GUARD` predicate preservation.
- `UNRESOLVED` abstains.

The check-option declaration records intended invariant preservation. It does
not prove that a database enforces `WITH CHECK OPTION`, a trigger, a policy, or
an equivalent guard.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, definition, dependencies, validation, refresh, mutation, disclosure, and rollback declarations are coherent. |
| `ABSTAIN` | View kind, validation, or mutation posture remains unresolved or incomplete. |
| `DENY` | The manifest is contradictory, noncanonical, unguarded for write-through use, unsafe for a public candidate, or hash-invalid. |
| `ERROR` | The candidate cannot be read or evaluated safely, or records a validation error. |

These are local validation results, not database, evidence, policy, review,
promotion, release, deployment, or publication decisions.

## Directory Rules basis

An analytical view manifest describes a derived data contract surface, so its
semantic owner is `contracts/data/`, not the UI view registry or governance
record lane. Machine shape, fixtures, validation, tests, read-only CI, source
reconciliation, and authoring accountability stay in existing responsibility
roots.

No database, SQL registry, runtime view registry, lifecycle store, policy lane,
release path, public API, or new root is introduced.

## Validation and rollback

```bash
python -m unittest tests.validators.data.test_validate_analytical_view_manifest -v
python tools/validators/data/validate_analytical_view_manifest.py --fixtures
```

Rollback is one additive commit revert. The profile has no runtime consumer and
creates no database object, data mutation, refresh job, policy, review, release,
deployment, cache, or public artifact.
