<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/registers/continuity-inventory
title: Continuity Inventory - Cross-Domain Review Guide
type: register-guide
version: v0.1
status: draft; repository-grounded; documentation-only; review-required
owners: NEEDS VERIFICATION - domain and documentation stewardship
created: 2026-10-08
created_note: Date of this substantive documentation edition; the tracked path existed earlier.
updated: 2026-10-08
policy_label: repository-facing; cite-or-abstain; no-operational-approval
owning_root: docs/
responsibility: Explain human continuity review and connect domain inventories without certifying migrations, retirements, ownership, or lifecycle decisions.
truth_posture: CONFIRMED pinned repository inventory and source inspection; PROPOSED review-required documentation guide; NEEDS VERIFICATION accountable stewardship and operational acceptance
evidence_snapshot: main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
related:
  - docs/registers/README.md
  - docs/domains/habitat/CONTINUITY_INVENTORY.md
  - docs/domains/settlements-infrastructure/CONTINUITY_INVENTORY.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
[/KFM_META_BLOCK_V2] -->

# Continuity Inventory

Use this register guide when replacing a document, reconciling a source, changing a domain interface or retiring an old path. Its purpose is to preserve useful meaning, identity, evidence and recovery while making each proposed change reviewable.

This is a human navigation and review surface under the [registers boundary](README.md). It neither declares a new canonical machine inventory nor assigns lifecycle or retirement authority.

## What continuity means

| Dimension | Question to answer | Example of a distinction to preserve |
|---|---|---|
| Identity | Is this the same entity, object or document across the change? | A renamed place is not automatically a new municipality; a changed legal identity may require a successor. |
| Meaning and role | Does the source or object still mean the same thing? | A modeled service area cannot silently become an observed boundary. |
| Time | Which dates and intervals retain their meaning? | Retrieval date does not replace source-valid or observation time. |
| Evidence | Can a reader still resolve the original support and correction lineage? | A successor receipt links history instead of overwriting an old reviewed record. |
| Consumer | Which paths, APIs, UI controls or generated outputs still rely on it? | A same-path improvement and a path retirement have different compatibility needs. |
| Recovery | What can be restored without discarding later legitimate work? | Source rollback preserves newer user data unless a separately authorized recovery addresses it. |

The [Settlements/Infrastructure inventory](../domains/settlements-infrastructure/CONTINUITY_INVENTORY.md) supplies identity, role and evidence examples. The [Habitat inventory](../domains/habitat/CONTINUITY_INVENTORY.md) supplies a prior-work disposition vocabulary. Their domain claims remain local to those documents.

## Review vocabulary

| Disposition | Use it when | Evidence to retain |
|---|---|---|
| Keep and extend | The existing surface remains useful and compatible | Exact source, unique content and intended addition |
| Wrap with adapter | Preserve meaning while changing access or representation | Owning interface, explicit mapping and consumer checks |
| Keep as lineage | Prior intent is valuable but not current implementation | Source date and an explicit historical/proposed label |
| Defer | A specific dependency prevents the next step | Missing prerequisite, consequence and revisit trigger |
| Conflicted | Sources or owning boundaries disagree | Both exact references and the decision needed |
| Needs verification | A checkable fact has not been established | The actual check or evidence required |
| Retire | A reviewed successor and retirement decision exist | Authority, consumer migration, compatibility and recovery |

These are human review labels adapted from the existing Habitat guide. They are not machine enum values, permission grants or proof that any listed item has been retired.

## Inventory entry to prepare

For one candidate, record its current path/opaque identity, exact revision or digest, owning responsibility root, source lineage, purpose, consumers, unique content and state. Then record the proposed successor, disposition, rationale, compatibility plan, validation, remaining review, rollback and re-review trigger.

Do not populate an entry with guessed ownership, acceptance or release state. Protected locations, secrets and restricted payloads belong in their authorized stores, not this public-facing summary.

## A complete reconciliation procedure

1. Freeze the old and candidate references and read both.
2. Inventory unique behavior, explanation, links, native children, generated relationships and consumers.
3. Classify each meaningful part. A short file may be a deliberate index; a long file may still be stale.
4. Resolve the owning root before creating, moving or duplicating authority-bearing content.
5. Implement the smallest complete change, retaining history and compatibility where needed.
6. Validate paths, content and actual affected consumers. Separate source checks from deployment and operational acceptance.
7. Read back the delivered result and link its exact revision.
8. Retain unresolved drift in the [drift register](DRIFT_REGISTER.md) or [verification backlog](VERIFICATION_BACKLOG.md) through the owning reviewed workflow.

A documentation-only replacement can complete missing explanation while leaving operational maturity unchanged.

## Current navigation and limits

The two domain inventories linked above exist at `main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`. They are starting points, not an exhaustive audit of every lane. This edition adds no retirement decision and does not certify any existing continuity row as current.

Refresh when a source family, identity rule, canonical path, consumer interface or retention requirement changes. A text rollback restores this guide; it cannot reverse a migration, erase an external publication or restore data already changed.
