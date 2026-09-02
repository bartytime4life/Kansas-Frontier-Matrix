<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-temporal-uniqueness-source-map
title: Pass 18 Temporal Uniqueness Source Map
type: exploratory-source-map
version: v1.0.0
status: confirmed-source-reconciliation; proposed-inactive-implementation
owners: OWNER_TBD — Intake steward · Temporal steward · Data steward · Contract steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-lineage; no-public-authority
owning_root: docs/
responsibility: Reconcile supplied Pass 18 temporal uniqueness guidance with current repository authority and record the bounded implementation decision.
truth_posture: "CONFIRMED supplied card, current-main gap, and placement; PROPOSED inactive assessment; NEEDS VERIFICATION overlap-policy selection, human review, and hosted CI"
related:
  - ../../../contracts/common/temporal_uniqueness_assessment.md
  - ../../../contracts/common/temporal_window.md
  - ../../../contracts/common/period_boundary_predicate_disclosure.md
  - ../../../contracts/data/temporal_slice.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 temporal uniqueness source map

## Source statement

The supplied *KFM Pass 18 Idea Index / Category Atlas* records
`KFM-P18-INV-392`, “Temporal uniqueness constraints include validity
semantics.” Its proposed normalized statement says temporal tables should
define uniqueness over identity plus validity meaning instead of treating date
fields as ordinary appended columns. Its expansion direction proposes a
`temporal_key_profile` for time-aware records.

The card spans physical pages 119–120 and printed pages 116–117. It is planning
evidence. It does not prove repository implementation, name a database primary
key, or authorize table inspection or constraint execution.

## Current repository reconciliation

Inspection was performed against `main@590d3b77dcfd0792fbd183e0b2e1ca4c2d39a581`.

- `TemporalWindow` defines a shared finite temporal value.
- `PeriodBoundaryPredicateDisclosureCandidate` checks declared endpoint
  relations and boundary conventions for two intervals.
- `TemporalAuthorityEnvelope` separates source, validity, retrieval,
  correction, supersession, and lineage roles.
- `TemporalSlice` binds one derived view to time, identity, evidence, and local
  change lineage.
- A Chronicling America source-catalog note carries a narrative Pass 9 claim
  that temporal uniqueness should be validated, but it is not a closed shared
  schema, fixture family, or executable assessment profile.
- No common contract, schema, fixture family, validator, workflow, branch, or
  pull request was found for opaque identity-key digests, single-axis or
  bitemporal peer comparison, explicit pair-conflict rules, or candidate
  overlap-denial and overlap-allowance declarations.

The adjacent contracts and source-catalog note remain authoritative for their
own meanings and are not modified or replaced.

## Adaptation decision

The smallest dependency-closed implementation is one inactive common
assessment profile. It declares canonical identity-field references, opaque
same-key digests, valid-time, transaction-time, or bitemporal axes, explicit
inclusive boundaries, pair-conflict semantics, deterministic state, and
non-executing recommendations.

The source asks which tables need overlap denial versus overlap allowance. This
packet does not settle that policy. A candidate may declare `DENY_OVERLAP`,
`ALLOW_WITH_SUPERSESSION`, or `ALLOW_REVIEWED_PARALLEL`; local allowance
requires lineage or review references and grants no authority to them.

## Directory Rules and non-effects

Connected Directory Rules and accepted ADR-0029 assign shared meaning to
`contracts/common/` and preserve the existing schema, fixture, validator,
test, workflow, intake, and receipt responsibility roots. No table, temporal
database, primary key, trigger, record, source, evidence object, policy
decision, review state, denial, quarantine, release, deployment, publication,
or public route is created or changed.

## Verification posture

- **CONFIRMED:** source-card text, visual page inspection, current-main search,
  branch/PR collision search, and Directory Rules placement.
- **PROPOSED:** the inactive assessment, candidate policies, and machine shape.
- **NEEDS VERIFICATION:** table-specific overlap policy, hosted exact-head CI,
  human review, and any future consumer adoption.
- **UNKNOWN:** which data families, if any, require valid-time,
  transaction-time, or full bitemporal uniqueness.
