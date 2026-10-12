# RecommendationDecisionAuthorityAssessmentCandidate

Status: **PROPOSED / INACTIVE / FIXTURE-ONLY**
Profile: `kfm.governance.recommendation-decision-authority-assessment.v1`

## Purpose

This additive assessment carrier compares a separately evidenced advisory
`Recommendation` with a separately evidenced formal `Decision`. It can declare
whether no decision is recorded, the recommendation was adopted as written,
adopted with changes, rejected, deferred, or remains unresolved.

A valid assessment proves declaration consistency only. It does **not** create
or authenticate a recommendation, a binding decision, implementation work, a
completed action, or a measured outcome.

## Normative boundary

- A recommendation remains advisory even when its evidence is complete.
- Only a separately identified formal-authority instrument may be represented
  as a decision.
- `ADOPTED_WITH_CHANGES` requires a comparison digest; it cannot be silently
  collapsed into adoption as recommended.
- A decision reference does not prove implementation.
- An implementation reference does not prove completion or measured outcome.
- Downstream references remain links to separate object families.
- Every effect flag is permanently `false` in v1.

## Deterministic identity

The validator removes `assessment_id` and `spec_hash`, canonicalizes the rest
with the repository hashing package, computes SHA-256, and sets:

```text
spec_hash     = sha256:<64 lowercase hexadecimal characters>
assessment_id = recommendation-decision-authority-assessment:<first 24 hex>
```

## Outcome semantics

`PASS` means the declared recommendation, decision, linkage, chronology,
downstream references, deterministic identity, and authority non-effects are
internally consistent. `DENY` means a bounded schema or semantic contradiction.
`ERROR` is reserved for operational failures or identity mismatch.

## Activation posture

The proposal has no authority registry lookup, policy engine, decision write,
workflow execution, database migration, release path, API, or UI. Activation
requires an accepted ADR, named governance owner, authoritative instrument
registry, migration and rollback plan, policy review, and human approval.
