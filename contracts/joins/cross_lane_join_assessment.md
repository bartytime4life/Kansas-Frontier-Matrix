<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/joins/cross-lane-join-assessment
title: CrossLaneJoinAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; dry-run; local-only; non-authoritative
owners: OWNER_TBD — join steward; participating domain stewards; evidence steward; sensitivity steward; validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; cross-domain-join; sql-first; non-publisher; fail-closed
owning_root: contracts/
responsibility: Define a deterministic dry-run assessment for exact-key and synthetic spatial-temporal join candidates while preserving endpoint roles, evidence, sensitivity, and non-publisher effects.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json
  - ../../tools/joins/join_candidates.py
  - ../../fixtures/joins/cross_lane_join_assessment/cases.json
  - ../../tests/joins/test_join_candidates.py
  - ../../tests/joins/README.md
  - ../../docs/intake/exploratory/full-atlas-crosswalk-validator-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "ALLOW means only that the helper may emit a reviewable join candidate. It never means truth, policy permission, release, or publication."
  - "The exact-key lane uses parameterized in-memory SQLite over synthetic fixture values and performs no database or lifecycle write."
[/KFM_META_BLOCK_V2] -->

# CrossLaneJoinAssessment

> **Purpose.** Turn the join lane's documented exact-key and spatial-temporal candidate rules into a deterministic, reviewable, non-publishing assessment without collapsing participating domain authority.

## Source and repository basis

The Full Atlas card “Crosswalk Validator Lane (SQL-First Non-Publisher)” proposes a narrow validator whose rule-level failure counts produce only `ALLOW`, `DENY`, `ABSTAIN`, or `ERROR`, with no `ANSWER` or `HOLD`, and whose lane is never a publisher, schema home, policy home, or receipt store. The existing `tools/joins/README.md` independently proposes `join_candidates.py` and names exact-key, spatial-temporal, source-role conflict, sensitive geometry, living-person denial, and missing-EvidenceRef fixtures as the next smallest safe implementation.

This profile joins those two sources without establishing a crosswalk registry or changing pair-specific semantics.

## Finite validator outcomes

| Outcome | Report status | Meaning |
|---|---|---|
| `ALLOW` | `JOIN_CANDIDATE` | The declared predicate matched and generic evidence, role, sensitivity, living-person, and dependency checks produced no failure. A pair-specific validator and later governance gates remain mandatory. |
| `ABSTAIN` | `NO_JOIN_CANDIDATE`, `EVIDENCE_REF_MISSING`, `SOURCE_ROLE_REVIEW_REQUIRED`, or `SENSITIVITY_REVIEW_REQUIRED` | The helper cannot safely emit an unrestricted candidate under the declared inputs. |
| `DENY` | `LIVING_PERSON_JOIN_DENIED` or `GEOMETRY_PRECISION_BLOCKED` | A bounded privacy or sensitivity rule forbids candidate emission in this fixture profile. |
| `ERROR` | `VALIDATOR_SYSTEM_ERROR` | A declared dependency is unavailable; no candidate assertion is made. |

No `ANSWER`, `HOLD`, promotion, release, or publication state exists.

## Rule-level failure counts

The decision carries a stable six-rule vector:

- `DEPENDENCIES_READY`;
- `EVIDENCE_REFS_PRESENT`;
- `JOIN_PREDICATE_MATCHED`;
- `LIVING_PERSON_SAFE`;
- `SENSITIVITY_SAFE`;
- `SOURCE_ROLES_COMPATIBLE`.

Each rule reports a non-negative failure count. Endpoint source roles remain separately visible, output role is always `CANDIDATE_RELATION`, and inherited sensitivity is the strictest endpoint posture.

## Join mechanics

- `EXACT_KEY` uses a parameterized one-row-per-side SQLite join in an in-memory database. Keys are values, never SQL fragments.
- `SPATIAL_TEMPORAL` compares synthetic spatial-cell refs and timezone-aware intervals with a declared tolerance. It is not a geometry engine and proves no real-world spatial relationship.
- Missing EvidenceRefs abstain. Modeled, aggregate, or candidate role conflicts abstain. Restricted generalized context abstains for sensitivity review. Restricted exact geometry and living-person joins deny.
- `candidate_id` is RFC 8785/SHA-256 over request and endpoints. `spec_hash` binds the complete assessment excluding `assessment_id` and `spec_hash`.

## Non-publisher effects

The decision's effects are schema-fixed to false for lifecycle writes, evidence creation, policy decisions, review decisions, release decisions, publication, and public use. Even `ALLOW` only authorizes emission of the local report to stdout or a caller; it does not authorize any downstream effect.

## Directory Rules basis

Generic relationship meaning belongs in `contracts/joins/`; shape in `schemas/contracts/v1/joins/`; the dry-run helper in `tools/joins/`; synthetic cases in `fixtures/joins/`; tests in `tests/joins/`; authoring provenance in `data/receipts/generated/`. Pair-specific meaning, policy, evidence, receipts, lifecycle data, and release remain in their owning roots.

## Non-effects and rollback

This profile uses synthetic refs, has no network client, writes no file or database, creates no evidence or receipt, and grants no identity, relationship truth, policy, review, release, publication, or public-use authority. Revert the bounded commit to remove it.
