<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/expansion-plan
title: Soil implementation expansion plan
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil implementation expansion plan; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - docs/domains/soil/EXPANSION_BACKLOG.md
  - docs/domains/soil/VERIFICATION_BACKLOG.md
  - docs/domains/soil/DEFINITION_OF_DONE.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# soil — EXPANSION_PLAN.md

This plan orders further Soil work around independently reviewable capabilities.
It complements the [expansion backlog](EXPANSION_BACKLOG.md), whose stable item
IDs remain the planning record. It does not set source activation or release dates.

## Starting point

The lane contains executable synthetic checks for public-safe Soil candidates,
station moisture, SMAP L4 support separation, deterministic identity, map units,
components, catalog-closure declarations and SSURGO package drift. Their
existence does not establish an end-to-end ingestion or released product.
See the [verification backlog](VERIFICATION_BACKLOG.md) for open evidence needs.

## Dependency order

| Stage | Reviewable deliverable | Exit evidence |
|---|---|---|
| 1. Confirm one use case | Named object family, geographic support, time/depth meaning and intended audience | Scope excludes unsupported parcel, operational and scientific claims |
| 2. Reconcile vocabulary | Contract, schema and compatibility mapping for the chosen support type | Valid and invalid fixtures plus consumer inventory |
| 3. Bind source identity | Exact product/edition, native identifiers, role, rights, sensitivity and refresh proposal | Source review packet with explicit admission outcome |
| 4. Close offline transformation | Deterministic transform from approved synthetic or permitted local input | Input/output digests, units, clocks, uncertainty and failure behavior |
| 5. Assemble evidence | Candidate identity, EvidenceBundle and validation/correction references | All required support can be reviewed; missing support stays held |
| 6. Review catalog closure | Candidate assessed against every closure dimension | Declaration result and independent resolution evidence |
| 7. Review delivery | Policy, release, rollback and consumer compatibility packet | Separately authorized transition and readback |

Do not schedule stage 7 merely because stage 4 tests are green. Admission,
evidence closure and release have different owners and evidence requirements.

## Choosing the next slice

Prefer a slice with an existing strict contract and a small synthetic corpus.
For example, extending a map-unit identity check can be bounded to native keys,
vintage and support-role handling without downloading a statewide archive.
Before authoring it, inspect [canonical paths](CANONICAL_PATHS.md),
[file placement](FILE_SYSTEM_PLAN.md), and the current tests. Reuse an existing
validator or contract rather than creating another authority home.

Every proposed slice should record:

- exact base commit, current behavior and one observable change;
- affected contracts, schemas, fixtures, validator, consumer and documentation;
- allowed inputs and bounded resource use;
- valid, ambiguous, malformed and rights/sensitivity-denied outcomes;
- deterministic validation commands and expected results;
- migration or compatibility implications, reviewer roles and rollback target.

## Checks before widening scope

The [SSURGO watcher](../../../tools/ingest/ssurgo_watch/ssurgo_watch.py) is
fixture-only; do not turn its presence into a promise of scheduled source access.
The [identity model](IDENTITY_MODEL.md) describes an inactive candidate; do not
promote its identifier to a public canonical ID without review. The
[map guide](MAP_UI_CONTRACTS.md) separately records Site visual context.

If a source contract, rights decision or required method is unknown, retain the
slice as a review candidate and implement only independent bounded checks. If a
new source payload would be large or unbounded, establish extent, history,
expected volume, cache behavior and user control before acquisition.

## Completion and maintenance

A plan item is complete only for its named deliverable. Record exact evidence in
the owning backlog and leave downstream gates open. Revisit this order when an
accepted ADR, source decision, contract or actual consumer changes. Preserve old
item IDs and add supersession links instead of erasing earlier decisions.
