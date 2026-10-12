<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/source-conflict-influence-assessment-source-map
title: Source Conflict Influence Assessment Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Evidence steward · Source steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded mapping from Full Atlas source-conflict candidates to bounded repository artifacts without treating candidate cards as implementation evidence or authority
truth_posture: CONFIRMED candidate transcription and repository comparison / PROPOSED bounded adaptation pending steward review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/evidence/source_conflict_influence_assessment.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/evidence/claim_field_binding.md
tags: [kfm, atlas, source-conflict, influence, source-map]
[/KFM_META_BLOCK_V2] -->

# Source Conflict Influence Assessment Source Map

## Source cards

| Card | Retained proposal | Bounded implementation |
|---|---|---|
| `KFM-TRIAD-065` | Source-conflict topology and influence accounting | One fixture-only comparison/influence declaration profile. |
| `KFM-CAND-0193` | Classify jointly used sources as consistent, divergent, conflicting, insufficient, inapplicable, or containing revoked evidence. | Closed finite relationship vocabulary and fail-safe overall precedence. |
| `KFM-CAND-0194` | Show inputs, exclusions, axes, conflict class, uncertainty, and influence roles. | Deterministic source, pair, and summary inventories with no payload values. |
| `KFM-CAND-0195` | Define profile, comparison, influence-ledger, and decision-like objects with order-invariance and negative fixtures. | One assessment candidate; no `FederationDecision` or policy authority is created. |

The Full Atlas is a candidate register, not implementation evidence. The packet narrows its programming card because a federation decision would cross policy and claim-authority boundaries.

## Repository reconciliation

- `SourceDescriptor` remains the source-role authority; this schema copies its current enum exactly.
- `ClaimFieldBinding` already preserves field-local conflicts but does not express a complete cross-source pair topology or influence inventory.
- `EvidenceRef` remains unresolved; this validator does not inspect evidence payloads.
- Policy, review, claim, release, and publication decisions remain separate.

Repository search at base `76da0a048590710bd927891d43075d989568bf7d` found no reusable source-conflict influence contract, schema, validator, fixture family, or workflow outside proposal material.

## Path decision

```yaml
path_decision:
  artifact: SourceConflictInfluenceAssessmentCandidate
  proposed_path: contracts/evidence/source_conflict_influence_assessment.md
  artifact_kind: semantic contract
  authority_owner: evidence comparison and influence disclosure
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: source-conflict-influence
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/kfm_full_atlas_seed_cards.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-AUTHROOT-001
    - DIR-SCOPELANE-004
    - DIR-DEP-001
  outcome: PLACE
```

## Non-effects

This packet does not fetch or compare source payloads, alter source roles, resolve evidence, calculate factual confidence, select truth, authorize a claim, evaluate policy, approve review, promote, release, deploy, publish, or authorize public use.
