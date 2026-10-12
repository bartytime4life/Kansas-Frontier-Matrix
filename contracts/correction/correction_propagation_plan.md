<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/correction/correction-propagation-plan
title: CorrectionPropagationPlan Contract
type: semantic-contract; derivative-invalidation planning
version: v0.1.0
status: proposed; fixture-only; no-network; non-executing
owners: OWNER_TBD — Correction steward · Release steward · Runtime steward
created: 2026-08-08
updated: 2026-09-07
policy_label: internal; correction; rollback; derivative-invalidation; non-authoritative
related:
  - ./correction_notice.md
  - ./correction_impact_assessment.md
  - ./supersession_notice.md
  - ../../schemas/contracts/v1/correction/correction_propagation_plan.schema.json
  - ../../fixtures/contracts/v1/correction/correction_propagation_plan/cases.json
  - ../../tools/validators/correction/validate_correction_propagation_plan.py
  - ../../tests/validators/test_validate_correction_propagation_plan.py
  - ../../.github/workflows/correction-propagation-plan.yml
tags: [kfm, correction, propagation, derivatives, cache, alias, release, rollback]
[/KFM_META_BLOCK_V2] -->

# CorrectionPropagationPlan

> **Profile:** `kfm.correction-propagation.fixture.v1`  \
> **Schema:** `1.0.0`  \
> **Execution profile:** `FIXTURE_ONLY`  \
> **Authority:** none

## Purpose and currentness

`CorrectionPropagationPlan` is a deterministic dependency inventory for one
correction, supersession, withdrawal, or rollback. It identifies affected
derivative surfaces, the proposed action, the current status, and the evidence
needed to close each entry. It makes stale carriers visible before a later
rebuild or release decision.

This contract does not execute invalidation, repoint an alias, rebuild a
derivative, issue a release, delete history, publish a replacement, or grant
public use. It is not a worker queue, cache command, release manifest, or
rollback executor.

The implementation authority snapshot for this refresh is
`main@ec203a9ba11fb83b52245f9523ce36cc1ec6ac66`, inspected on 2026-09-07.
That main includes the previously updated correction-impact README. The prior
propagation-plan README blob was
`b61e7fb0ecd0e68588a29642f3c47e0cb810eff9`.

## Contract shape

The JSON Schema requires these top-level fields:

| Field | Contract meaning |
| --- | --- |
| `object_type` | Constant `CorrectionPropagationPlan`. |
| `schema_version` | Constant `1.0.0`. |
| `profile` | Constant `kfm.correction-propagation.fixture.v1`. |
| `plan_id` | `kfm:correction-propagation:` plus the first 24 hex characters of the canonical spec hash. |
| `observed_at` | RFC 3339 timestamp with a UTC designator or explicit offset. |
| `correction_notice_ref` | Reference to the named correction. |
| `source_release_ref` | Reference to the release or source state being assessed. |
| `replacement_release_ref` | Replacement release reference, or `null` when no replacement is declared. |
| `declared_surface_kinds` | Unique set of surface kinds represented by the entries. |
| `entries` | One or more dependency entries, maximum 100. |
| `summary` | Recomputed counts, public-impact flag, and overall record outcome. |
| `governance` | Fixture-only and all-mutation-false boundary flags. |
| `spec_hash` | SHA-256 hash of the canonical payload excluding `plan_id` and `spec_hash`. |

The canonical identity is computed by the shared
[`packages/hashing` package](../../packages/hashing/README.md). A changed
payload, plan ID, or specification hash is an integrity failure; the validator
does not repair it silently.

## Surface inventory

`declared_surface_kinds` and `entries[].surface_kind` use only these ten
values:

1. `API_PROJECTION`
2. `CATALOG_RECORD`
3. `CITATION_INDEX`
4. `EXPORT_ARTIFACT`
5. `FOCUS_CACHE`
6. `GRAPH_PROJECTION`
7. `MAP_LAYER`
8. `SEARCH_INDEX`
9. `STORY_NODE`
10. `TILE_ARTIFACT`

The declared set must equal the sorted set present in the entries. Every
`artifact_ref` must be unique, and entries must be sorted by
`(surface_kind, artifact_ref)`. These checks prevent a plan from hiding a
duplicate carrier or silently omitting a declared surface.

## Entry semantics

Each entry requires:

| Field | Allowed values and rule |
| --- | --- |
| `surface_kind` | One of the ten canonical surface kinds above. |
| `artifact_ref` | A stable `kfm:` reference. |
| `visibility` | `PUBLIC`, `SEMI_PUBLIC`, or `INTERNAL`. |
| `action` | `INVALIDATE`, `MARK_STALE`, `REBUILD`, `REPOINT_ALIAS`, `REPUBLISH`, `WITHDRAW`, or `REVIEW_ONLY`. |
| `status` | `PENDING`, `BLOCKED`, `COMPLETED`, or `ERROR`. |
| `target_release_ref` | Must match `replacement_release_ref` for alias repoint/republish actions; otherwise must be `null`. |
| `completion_receipt_ref` | Required only for `COMPLETED`; forbidden for every other status. |
| `updated_at` | Timestamp no later than top-level `observed_at`. |
| `reason_codes` | Exactly two unique codes derived from the action and status. |

The validator derives the two reason codes from these maps:

| Action | Reason code |
| --- | --- |
| `INVALIDATE` | `INVALIDATE_DERIVATIVE` |
| `MARK_STALE` | `MARK_STALE` |
| `REBUILD` | `REBUILD_DERIVATIVE` |
| `REPOINT_ALIAS` | `REPOINT_ALIAS` |
| `REPUBLISH` | `REPUBLISH_DERIVATIVE` |
| `WITHDRAW` | `WITHDRAW_DERIVATIVE` |
| `REVIEW_ONLY` | `REVIEW_REQUIRED` |

| Status | Reason code |
| --- | --- |
| `PENDING` | `PENDING_ACTION` |
| `BLOCKED` | `BLOCKED_DEPENDENCY` |
| `COMPLETED` | `COMPLETION_RECORDED` |
| `ERROR` | `PROPAGATION_ERROR` |

An entry with `PUBLIC` or `SEMI_PUBLIC` visibility cannot use `REVIEW_ONLY`.
`REPOINT_ALIAS` and `REPUBLISH` require a non-null replacement release and an
entry target that exactly matches it. All other actions require a null target.

## Summary and finite outcomes

The summary is derived from the entries and must contain:

- `entry_count`;
- `pending_count`, `blocked_count`, `completed_count`, and `error_count`;
- `public_impact`, true when any entry is `PUBLIC` or `SEMI_PUBLIC`; and
- `overall_outcome`.

The record-level `overall_outcome` is recomputed as follows:

| Condition | Record outcome |
| --- | --- |
| Any entry has status `ERROR` | `ERROR` |
| No error and at least one `BLOCKED` entry | `HOLD` |
| Every entry is `COMPLETED` | `COMPLETE` |
| Otherwise | `READY` |

The executable validator reports a separate result boundary:

- valid `READY` or `COMPLETE` records return `PASS` and exit 0;
- a schema or semantic closure failure returns `DENY` and exit 1;
- a record with summary `HOLD` returns `ABSTAIN` and exit 3;
- a record with summary `ERROR`, unreadable input, invalid JSON, or a runtime
  input failure returns `ERROR` and exit 2.

`PASS`, `DENY`, `ABSTAIN`, and diagnostic `ERROR` are validator results; they
are not additional values for the schema-level `overall_outcome`.

## Governance boundary

The `governance` object is schema-constrained to:

| Field | Required value |
| --- | --- |
| `execution_mode` | `FIXTURE_ONLY` |
| `mutation_performed` | `false` |
| `cache_invalidated` | `false` |
| `alias_repointed` | `false` |
| `release_authorized` | `false` |
| `publication_authorized` | `false` |
| `history_deleted` | `false` |

Consequently, a valid plan is evidence for review or later orchestration only.
It is not proof that a downstream carrier consumed the plan or that any cache,
alias, release, public route, or historical object changed.

## Relationship to adjacent correction artifacts

| Artifact | Responsibility | Boundary |
| --- | --- | --- |
| [CorrectionNotice](./correction_notice.md) | Names the correction event and its reason. | Does not enumerate derivative closure. |
| [CorrectionImpactAssessment](./correction_impact_assessment.md) | Assesses the canonical carrier inventory. | Does not plan each dependency or execute it. |
| `CorrectionPropagationPlan` | Records dependency-level actions, statuses, receipts, and summary. | Fixture-only and non-executing. |
| [SupersessionNotice](./supersession_notice.md) | Preserves old/new lineage and supersession intent. | Does not repoint aliases or publish. |
| [Release correction lane](../../release/correction/README.md) | Reviews release-facing repair, withdrawal, supersession, and rollback. | Separate release authority. |

The plan can be an input to a later policy or release review. No later
authority is implied by the plan's presence or by a `PASS` validator result.

## Verified implementation surfaces

The following implementation surfaces were present at the pinned main commit:

- **Schema:** [correction_propagation_plan.schema.json](../../schemas/contracts/v1/correction/correction_propagation_plan.schema.json), blob `3b178bd83c5753a90b30a1549ef5ed587986bd70`.
- **Schema index:** [correction schema family README](../../schemas/contracts/v1/correction/README.md), blob `95ade6418f91db518d4813299b5c25ca05f20815`.
- **Fixture corpus:** [cases.json](../../fixtures/contracts/v1/correction/correction_propagation_plan/cases.json), blob `fc3a0ee85f86b632505d288ce9854442b09edb9b`.
- **Validator:** [validate_correction_propagation_plan.py](../../tools/validators/correction/validate_correction_propagation_plan.py), blob `4cb4f366a21612adf660fae4bb8dacbc67a169ab`.
- **Focused tests:** [test_validate_correction_propagation_plan.py](../../tests/validators/test_validate_correction_propagation_plan.py), blob `2c5647b7d87447ad2c69f373c9e81a26e57a206a`.
- **Workflow:** [correction-propagation-plan.yml](../../.github/workflows/correction-propagation-plan.yml), blob `fd2a6dec2eea84a82bb98e2612f5cf22afe1ef0f`.
- **Source map:** [correction-propagation-plan-source-map.md](../../docs/intake/exploratory/correction-propagation-plan-source-map.md), blob `c720a0669c9a5059611834f2aa0031a81a5bab95`.
- **Generated receipt:** [genrec-correction-propagation-plan-20260808.json](../../data/receipts/generated/genrec-correction-propagation-plan-20260808.json), blob `d6fc4b623cc3e715465bbd84d1488b4b23b7e145`.

The receipt is historical authoring/provenance evidence. It records eight
focused tests, fifteen exact fixture cases, no-network validation, and skipped
hosted exact-head and human-review gates; it does not establish current CI,
approval, release, or publication.

## Validation profile

The native workflow runs the following bounded checks with network disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m py_compile \
  tools/validators/correction/validate_correction_propagation_plan.py \
  tests/validators/test_validate_correction_propagation_plan.py

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python -m unittest tests.validators.test_validate_correction_propagation_plan -v

PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 PYTHONHASHSEED=0 TZ=UTC \
  python tools/validators/correction/validate_correction_propagation_plan.py --fixtures

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/genrec-correction-propagation-plan-20260808.json \
  --repo-root .
```

The fixture suite contains fifteen exact cases: two `PASS`, one `ABSTAIN`, one
diagnostic `ERROR`, and eleven `DENY`. The focused test file covers schema
meta-validation, polarity, every case, no-network behavior, governance flags,
deterministic identity, direct CLI validation, and fixture CLI replay.

The workflow is path-scoped to this contract, its schema, fixture corpus,
validator, tests, hashing package, source map, receipt, and itself. It grants
read-only contents permission and does not mutate runtime or public state.

## Policy and release boundaries

There is no verified executable `policy/correction/` implementation bound to
this plan at the pinned main. General policy context is documented in
[policy/README.md](../../policy/README.md), while rights-correction boundary
guidance is separately documented in
[policy/rights/correction/README.md](../../policy/rights/correction/README.md).
Those documents do not authorize propagation or release.

Release-facing correction review remains separate in
[release/correction/README.md](../../release/correction/README.md) and
[release/correction/rollback/README.md](../../release/correction/rollback/README.md).
The parent [contracts/correction/README.md](./README.md) records unresolved
placement and maturity questions; this README does not silently resolve them.

Correction doctrine and publication architecture are documented in
[corrections-first-class.md](../../docs/doctrine/corrections-first-class.md)
and [publication/CORRECTION.md](../../docs/architecture/publication/CORRECTION.md).
They establish append-only and rollback-aware principles, not executable plan
consumption.

## Evidence and coordination lineage

GitHub is the implementation authority. The current commit, exact blob IDs,
schema, fixtures, validator, tests, workflow, and receipt above are the
repository evidence for this contract.

Notion was consulted read-only:

- [KFM Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447?pvs=204)
  reiterates that GitHub remains implementation authority and that coordination
  records do not authorize merge, release, deployment, or publication.
- [KFM Issue #4228 — Frozen Catalog Correction-Mechanism Decision Package](https://app.notion.com/p/3cfa92021bf681eda2f7c8baa90217b5?pvs=204)
  records a separate correction-mechanism/topology hold; it does not bind this
  propagation plan or authorize consumption.

Google Drive was consulted read-only:

- [KFM System Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI/edit?usp=drivesdk)
  provides durable chronology for GitHub authority, append-only correction
  lineage, rollback review, and the separation of coordination from release or
  publication authority.

These Notion and Drive sources are coordination lineage only. They are not
editable masters, do not supersede GitHub, and do not prove that this plan was
consumed, approved, released, published, or applied to a live carrier.

## Rollback

Before merge, close or abandon the draft PR and preserve the current main
history. After any separately authorized merge, use an ordinary reviewed
forward revert of the single documentation commit. The rollback target for
this README is the prior blob
`b61e7fb0ecd0e68588a29642f3c47e0cb810eff9`.

Do not delete the schema, fixture corpus, validator, tests, workflow, receipt,
or correction history. Reverting this README does not invalidate a cache,
repoint an alias, issue a release, delete history, or restore a public surface.

## Definition of done for a future activation decision

Any move beyond this proposed, fixture-only state requires a separate reviewed
decision that establishes:

- a named correction, release, runtime, and affected-domain owner;
- accepted policy and release/review bindings;
- schema, fixture, validator, test, workflow, and receipt parity;
- authenticated dependency discovery and completion-receipt semantics;
- explicit handling for partial failure, blocked dependencies, stale public
  carriers, cache invalidation, alias movement, and rollback; and
- a capability-separated executor that consumes this plan without treating
  the plan itself as authority.

Until those gates are met, this document is a repository-grounded planning
contract, not an execution or publication declaration.
