<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/pass-18-temporal-reference-integrity-source-map
title: Pass 18 Temporal Reference Integrity Source Map
type: exploratory-source-map
version: v1.0.0
status: confirmed-source-reconciliation; proposed-inactive-implementation
owners: OWNER_TBD — Intake steward · Temporal steward · Data steward · Contract steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-lineage; no-public-authority
owning_root: docs/
responsibility: Reconcile supplied Pass 18 temporal referential-integrity guidance with current repository authority and record the bounded implementation decision.
truth_posture: "CONFIRMED supplied card, current-main gap, and placement; PROPOSED inactive assessment; NEEDS VERIFICATION default failure policy, human review, and hosted CI"
related:
  - ../../../contracts/common/temporal_reference_integrity_assessment.md
  - ../../../contracts/common/temporal_window.md
  - ../../../contracts/common/period_boundary_predicate_disclosure.md
  - ../../../contracts/data/temporal_slice.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 temporal reference integrity source map

## Source statement

The supplied *KFM Pass 18 Idea Index / Category Atlas* records
`KFM-P18-INV-490`, “Temporal referential-integrity gate for history tables.”
Its proposed normalized statement says time-bounded observations should not
point to nonexistent or temporally invalid source, geography, or identity
records. Its expansion direction calls for no-network geography-version and
source-version fixtures.

The card spans physical pages 124–125 and printed pages 121–122. It is planning
evidence. It does not prove repository implementation, authenticate any record,
or authorize a database constraint or lifecycle action.

## Current repository reconciliation

Inspection was performed against `main@97b9cb77bf57b1d1cf75c2768f8e550e399a1345`.

- `TemporalWindow` defines a shared finite temporal value.
- `PeriodBoundaryPredicateDisclosureCandidate` checks interval conventions and
  endpoint relations for two declared windows.
- `TemporalAuthorityEnvelope` records source, time, geography, revision, and
  lineage metadata without resolving those references.
- `TemporalSlice` binds one derived view to time, space, evidence, run
  provenance, and local change lineage.
- No common contract, schema, fixture family, validator, workflow, branch, or
  pull request was found that checks whether a subject's valid-time or
  transaction-time interval is compatible with a referenced source,
  geography, or identity version's interval.

The adjacent contracts remain authoritative for their own meanings and are not
modified or replaced.

## Adaptation decision

The smallest dependency-closed implementation is one inactive common
assessment profile. It declares record presence, role-to-kind consistency,
valid-time, transaction-time, or bitemporal axes, explicit inclusive
boundaries, four finite interval constraints, and deterministic outcomes.

The source asks whether failures should default to denial or quarantine. This
packet does not settle that policy. A violated candidate may carry either
`DENY_CANDIDATE` or `QUARANTINE_CANDIDATE` as a review recommendation, while
`recommendation_only` is fixed true and `disposition_executed` is fixed false.

## Directory Rules and non-effects

Connected Directory Rules and accepted ADR-0029 assign shared meaning to
`contracts/common/` and preserve the existing schema, fixture, validator,
test, workflow, intake, and receipt responsibility roots. No table, database
trigger, foreign key, source record, geography record, identity record,
observation, evidence object, policy decision, review state, quarantine,
release, deployment, publication, or public route is created or changed.

## Verification posture

- **CONFIRMED:** source-card text, visual page inspection, current-main search,
  branch/PR collision search, and Directory Rules placement.
- **PROPOSED:** the inactive assessment and machine shape.
- **NEEDS VERIFICATION:** default failure policy, hosted exact-head CI, human
  review, and any future consumer adoption.
- **UNKNOWN:** which history tables or domain relationships, if any, will adopt
  the profile or require full bitemporal rather than single-axis checks.
