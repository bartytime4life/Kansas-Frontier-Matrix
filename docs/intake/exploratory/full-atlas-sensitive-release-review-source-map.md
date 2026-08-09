<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/intake/exploratory/full-atlas-sensitive-release-review-source-map
title: Full Atlas Sensitive Release Review Source Map
type: source-adaptation-map
version: v0.1.0
status: proposed; exploratory; non-authoritative
owners: ["@bartytime4life"]
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; source-map; governance; sensitive-release
owning_root: docs/
responsibility: Record how the Full Atlas T3/T4 two-person-rule proposal was reconciled with current repository governance objects and narrowed into a fixture-only closure profile.
truth_posture: "CONFIRMED source and repository comparison; PROPOSED contract; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ../../../contracts/governance/sensitive_release_review_closure.md
  - ../../../contracts/governance/review_authority_binding.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Full Atlas Sensitive Release Review Source Map

## Source finding

**CONFIRMED source text:** the Google Drive document `KFM_Full_Atlas_seed_cards` contains the proposal **Two-Person Rule for T3/T4 Release**. Its normalized statement requires a T3/T4 promotion candidate to have at least one reviewer outside the author's role chain and forbids self-approval. Its implementation surface proposes a release-gate policy and no-network fixture tests.

**UNKNOWN in the source:** current repository paths, active policy/runtime behavior, authenticated reviewer identities, release state, and implementation maturity.

## Repository comparison

**CONFIRMED at base `f5efa63a3600f688cb9d6ed0255e20b9dfbac6dc`:** the repository already contains `ReviewRecord`, `StewardshipAssignment`, and a strict fixture-only `ReviewAuthorityBinding` contract/schema/validator. It does not contain a contract or validator named for T3/T4 two-person release closure.

## Adaptation decision

The bounded implementation reuses the full `ReviewAuthorityBinding` object rather than creating a parallel reviewer or authority vocabulary. It adds only:

- T3/T4 scope;
- author role-chain exclusion;
- release-review responsibility;
- release-candidate, policy, evidence, correction, and rollback bindings; and
- a deliberately non-authorizing outcome named `CLOSED_FOR_SEPARATE_RELEASE_GATE`.

It does not implement the source card's later Evidence Drawer display or an executable release policy. Those require separate UI, policy, authentication, and release reviews.

## Directory basis

Accepted ADR-0029 assigns the semantic profile to `contracts/governance/` and its machine shape to `schemas/contracts/v1/governance/`. Fixtures, validator, tests, workflow, and generated authoring receipt remain in their established responsibility roots. No source-proposed path is adopted.
