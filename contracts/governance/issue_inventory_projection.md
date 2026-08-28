# Issue Inventory Projection

## Status and responsibility

**PROPOSED, fixture-backed governance contract.** `IssueInventoryProjection` is a
read-only local projection used by the BriefingSignal routing dry run to verify
that a declared existing-issue target is present and open before proposing
`UPDATE_EXISTING_ISSUE`.

**Directory Rules basis:** semantic meaning belongs under `contracts/`; the
closed machine shape belongs under `schemas/contracts/v1/`; deterministic
samples belong under `fixtures/`; executable validation belongs under
`tools/validators/`; and acceptance behavior belongs under `tests/`. This slice
uses existing governance lanes and creates no root, schema home, policy home,
source home, release home, or proof home.

## Purpose

A BriefingSignal may declare `matched_issue_ids`, but candidate-supplied issue
numbers are not independent repository-state evidence. This projection inserts
a bounded verification stage before any future live GitHub read:

```text
validated BriefingSignal
  -> declared finite route
  -> validated local IssueInventoryProjection
  -> open-target binding or fail-closed HOLD
  -> value-minimized dry-run report
```

The projection contains no issue title, body, comment, label, assignee,
reviewer, permission, ruleset, merge state, or mutation token.

## Profile

`kfm.briefing.issue-inventory.fixture.v1`

Required fields:

| Field | Meaning |
|---|---|
| `profile` | Exact fixture projection profile. |
| `schema_version` | Exact machine-shape version, currently `1.0.0`. |
| `projection_id` | Deterministic ID derived from the projection digest. |
| `repository` | Repository whose issue numbers are represented. |
| `source_ref` | Fixture provenance reference; never a live-state claim. |
| `generated_at` | Canonical UTC-second projection time. |
| `issue_count` | Exact number of projected issue-state rows. |
| `issues[]` | Sorted issue number, `OPEN`/`CLOSED` state, and update time only. |
| `projection_digest` | SHA-256 over canonical JSON excluding ID and digest. |
| `live_state_verified` | Fixed `false`. |
| `authority_created` | Fixed `false`. |
| `repository_mutation_allowed` | Fixed `false`. |

## Deterministic identity

Canonicalization uses UTF-8 JSON with sorted keys, no insignificant whitespace,
and non-ASCII characters preserved. The digest-bearing payload excludes only
`projection_id` and `projection_digest`.

```text
projection_digest = "sha256:" + SHA256(canonical_payload)
projection_id     = "kfm:issue-inventory:" + digest_hex[0:16]
```

Changing repository identity, fixture provenance, generation time, issue
membership, issue state, or issue update time produces a different digest and
ID.

## Routing binding

Only a declared `UPDATE_EXISTING_ISSUE` route requires this projection.

| Projection result | Dry-run disposition |
|---|---|
| No projection supplied | `HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_REQUIRED` |
| Target absent | `HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_TARGET_MISSING` |
| All targets closed | `HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_TARGET_CLOSED` |
| More than one target open | `HOLD_FOR_DEPENDENCY / ISSUE_INVENTORY_AMBIGUOUS_OPEN_TARGETS` |
| Exactly one target open and none missing | `UPDATE_EXISTING_ISSUE / ISSUE_INVENTORY_OPEN_TARGET` |

Closed rows may remain visible in the value-minimized report as IDs when one
other declared target is open. The router never opens, closes, edits, labels,
comments on, assigns, or otherwise mutates an issue.

## Validation and failure posture

The validator rejects:

- duplicate JSON keys, non-finite numbers, symbolic-link inputs, oversized
  inputs, or non-object roots;
- unknown or missing fields;
- duplicate or unsorted issue numbers;
- non-canonical timestamps or issue updates after the projection time;
- issue-count mismatch;
- digest or deterministic-ID mismatch; and
- any true live-state, authority, or mutation flag.

Findings contain stable code and JSON-pointer path only. They do not echo
candidate values.

## Non-effects

A valid projection proves only that a local synthetic fixture conforms to this
profile. It does not prove live GitHub issue state, repository authorization,
issue-writing authority, evidence, source admission, policy, review, proof,
release, deployment, publication, or public truth.

A future live adapter must be a separate, reviewed slice with authenticated
read-only access, retrieval receipts, repository/ref binding, stale-state
handling, rate-limit behavior, and negative tests. It must not mutate issues.

## Rollback

Before merge, close the pull request and abandon the branch. After merge,
revert the bounded commit. No external issue, source, evidence, lifecycle,
release, cache, deployment, or public state is created by this profile.
