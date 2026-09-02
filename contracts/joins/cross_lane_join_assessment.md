<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/joins/cross-lane-join-assessment
title: CrossLaneJoinAssessment Contract
type: contract
version: v0.1.0
status: proposed; fixture-first; dry-run; local-only; non-authoritative
owners: OWNER_TBD — join steward; participating domain stewards; evidence steward; sensitivity steward; validation steward
created: 2026-08-09
updated: 2026-09-02
policy_label: repository-facing; cross-domain-join; sql-first; non-publisher; fail-closed
owning_root: contracts/
responsibility: Define a deterministic dry-run assessment for exact-key and synthetic spatial-temporal join candidates while preserving endpoint roles, evidence, sensitivity, and non-publisher effects.
truth_posture: cite-or-abstain
related:
  - ../common/temporal_window.md
  - ../../schemas/contracts/v1/joins/cross_lane_join_assessment.schema.json
  - ../../tools/joins/join_candidates.py
  - ../../fixtures/contracts/v1/joins/cross_lane_join_assessment/cases.json
  - ../../tests/joins/test_join_candidates.py
  - ../../tests/joins/test_cross_lane_scope_precedence.py
  - ../../tests/joins/test_cross_lane_synthetic_role_guard.py
  - ../../tests/joins/test_cross_lane_temporal_boundary_guard.py
  - ../../tests/joins/test_cross_lane_domain_alias_guard.py
  - ../../tests/joins/test_cross_lane_domain_alias_dependency_guard.py
  - ../../tests/joins/README.md
  - ../../control_plane/domain_lane_register.yaml
  - ../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../docs/intake/exploratory/full-atlas-crosswalk-validator-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "ALLOW means only that the helper may emit a reviewable join candidate. It never means truth, policy permission, release, or publication."
  - "The exact-key lane uses parameterized in-memory SQLite over synthetic fixture values and performs no database or lifecycle write."
  - "Same-domain endpoints are outside this cross-lane profile and abstain with CROSS_DOMAIN_PAIR_REQUIRED; callers must route them to a domain-local validator."
  - "Unresolved domain aliases recorded by the projection-only domain-lane register are review signals, never normalization authority; alias/canonical pairs abstain with DOMAIN_ALIAS_REVIEW_REQUIRED."
  - "Missing EvidenceRefs and restricted generalized sensitivity review retain their explicit routes before unresolved-alias review; alias collision never suppresses evidence or sensitivity obligations."
  - "If the unresolved-alias projection is unavailable, malformed, or a symlink, the helper fails closed as VALIDATOR_SYSTEM_ERROR with DOMAIN_ALIAS_REGISTER_UNAVAILABLE; missing or redirected projection is never interpreted as an empty alias set."
  - "The generic seam does not own a repository-wide source-role crosswalk. Equal roles may continue to candidate proof, but any unequal role vector abstains for pair/domain-owned compatibility review."
  - "Zero-tolerance SPATIAL_TEMPORAL intervals that only touch at one boundary abstain; this profile does not invent repository-wide interval-boundary inclusivity."
  - "CLI modes are mutually exclusive and long options require exact spelling; fixture or derive mode never silently ignores an explicit assessment file."
[/KFM_META_BLOCK_V2] -->

# CrossLaneJoinAssessment

> **Purpose.** Turn the join lane's documented exact-key and spatial-temporal candidate rules into a deterministic, reviewable, non-publishing assessment without collapsing participating domain authority.

## Source and repository basis

The Full Atlas card “Crosswalk Validator Lane (SQL-First Non-Publisher)” proposes a narrow validator whose rule-level failure counts produce only `ALLOW`, `DENY`, `ABSTAIN`, or `ERROR`, with no `ANSWER` or `HOLD`, and whose lane is never a publisher, schema home, policy home, or receipt store. The existing `tools/joins/README.md` independently proposes `join_candidates.py` and names exact-key, spatial-temporal, source-role conflict, sensitive geometry, living-person denial, and missing-EvidenceRef fixtures as the next smallest safe implementation.

This profile joins those two sources without establishing a crosswalk registry or changing pair-specific semantics.

## Finite validator outcomes

| Outcome | Report status | Meaning |
|---|---|---|
| `ALLOW` | `JOIN_CANDIDATE` | The declared predicate matched across two distinct domain lanes and generic evidence, role, sensitivity, living-person, dependency, and unresolved-alias checks produced no failure. A pair-specific validator and later governance gates remain mandatory. |
| `ABSTAIN` | `NO_JOIN_CANDIDATE`, `EVIDENCE_REF_MISSING`, `SOURCE_ROLE_REVIEW_REQUIRED`, or `SENSITIVITY_REVIEW_REQUIRED` | The helper cannot safely emit an unrestricted cross-lane candidate under the declared inputs. Same-domain requests are `NO_JOIN_CANDIDATE` with `CROSS_DOMAIN_PAIR_REQUIRED`; unresolved alias/canonical domain pairs are `NO_JOIN_CANDIDATE` with `DOMAIN_ALIAS_REVIEW_REQUIRED`; zero-tolerance temporal boundary-touch requests are `NO_JOIN_CANDIDATE` with `TEMPORAL_BOUNDARY_AMBIGUOUS`; any unequal source-role vector is `SOURCE_ROLE_REVIEW_REQUIRED` until pair/domain authority resolves compatibility. |
| `DENY` | `LIVING_PERSON_JOIN_DENIED` or `GEOMETRY_PRECISION_BLOCKED` | A bounded privacy or sensitivity rule forbids candidate emission in this fixture profile. |
| `ERROR` | `VALIDATOR_SYSTEM_ERROR` | A declared dependency is unavailable, or the projection required to conservatively detect unresolved domain aliases cannot be read or validated; no candidate assertion is made. |

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

`SOURCE_ROLES_COMPATIBLE` is intentionally conservative at this generic responsibility root. Current cross-domain architecture records that KFM has no accepted repository-wide crosswalk that can declare two distinct source-role classes equivalent or compatible for a relationship. Therefore equal role values may continue to fixture-only candidate proof, while **every unequal role vector** fails closed to `SOURCE_ROLE_REVIEW_REQUIRED` with `SOURCE_ROLE_CONFLICT` and `RESOLVE_SOURCE_ROLE_COMPATIBILITY`. That includes observed/regulatory/administrative mismatches as well as modeled, aggregate, candidate, and mixed synthetic/non-synthetic pairs. The pair-specific or participating-domain validator may later establish a legitimate compatibility rule without letting this generic helper invent one.

`JOIN_PREDICATE_MATCHED` is the effective cross-lane candidate predicate. It fails when the declared exact-key or spatial-temporal predicate does not match, when both endpoints declare the same domain, **or when their raw domain values form an unresolved alias/canonical pair recorded by the projection-only domain-lane register**. Same-domain inputs return `ABSTAIN` / `NO_JOIN_CANDIDATE` with reason `CROSS_DOMAIN_PAIR_REQUIRED` and obligation `ROUTE_TO_DOMAIN_LOCAL_VALIDATOR`; the helper does not relabel domain-local work as a cross-domain relation. Unresolved alias/canonical pairs return `ABSTAIN` / `NO_JOIN_CANDIDATE` with reason `DOMAIN_ALIAS_REVIEW_REQUIRED` and obligation `ROUTE_TO_DOMAIN_ALIAS_REVIEW`. The helper does not normalize either endpoint, does not accept the proposed register as semantic authority, and does not turn an unresolved compatibility name into a second independently governed domain.

The unresolved-alias projection is also a validator dependency. If `control_plane/domain_lane_register.yaml` cannot be read, is a symlink, cannot be parsed, or cannot be exposed as a coherent `unresolved_aliases` mapping plus lane inventory, the helper cannot prove that a raw pair is free of unresolved alias collision. Duplicate YAML mapping keys are ambiguous and invalid at this boundary; last-value-wins parsing must not erase an alias review signal. Structural validation also requires unique, non-blank canonical lane IDs; exact non-blank alias names and targets; targets that resolve to a registered lane; and no self-reference, registered-lane alias key, or alias chain. An unknown or chained target can otherwise make a true alias/canonical pair appear unrelated and reach candidate proof. The helper therefore returns `ERROR` / `VALIDATOR_SYSTEM_ERROR` with reason `DOMAIN_ALIAS_REGISTER_UNAVAILABLE`, obligation `REPAIR_DOMAIN_ALIAS_REGISTER_DEPENDENCY`, and a non-zero `DEPENDENCIES_READY` failure count. This fail-closed dependency behavior does not elevate the register into identity authority; it only prevents absence, ambiguity, or corruption of the conservative review projection from being misread as evidence that no aliases exist.

For `SPATIAL_TEMPORAL`, zero-tolerance intervals that only touch at `left.valid_to == right.valid_from` or `right.valid_to == left.valid_from` also fail `JOIN_PREDICATE_MATCHED`. The shared `TemporalWindow` contract explicitly treats boundary inclusivity as compatibility-significant rather than globally settled, so this join profile must not silently choose closed-interval semantics. Boundary-touch inputs therefore return `ABSTAIN` / `NO_JOIN_CANDIDATE` with reason `TEMPORAL_BOUNDARY_AMBIGUOUS` and obligation `ROUTE_TO_PAIR_TEMPORAL_SEMANTICS`. A genuine interval overlap remains eligible, and a positive declared tolerance remains an explicit bounded comparison rule rather than an implied repository-wide time convention.

Disposition precedence preserves mandatory trust routes. Same-domain scope routing remains first because the generic cross-lane helper does not own domain-local work. For distinct raw domains, unavailable dependencies produce `ERROR`, and living-person or blocked sensitive geometry produces `DENY`. Missing EvidenceRefs then retain `EVIDENCE_REF_MISSING`, and restricted generalized context retains `SENSITIVITY_REVIEW_REQUIRED`, before an unresolved alias collision can route the request to alias review. Alias review never downgrades a system error or privacy/sensitivity denial, and never hides evidence or sensitivity-review obligations.

## Join mechanics

- Both endpoints must declare distinct `domain` values. Same-domain requests are routed away from this profile and never emit `JOIN_CANDIDATE`.
- Raw domain values that form an unresolved alias/canonical pair in `control_plane/domain_lane_register.yaml` are also routed to review. That projection is consumed only as a conservative collision signal: the helper preserves both raw domain values and never normalizes, registers, accepts, or migrates a domain identity.
- The unresolved-alias projection is required to make that conservative check. Missing, unreadable, symlinked, malformed, structurally invalid, or duplicate-key projection data produces `VALIDATOR_SYSTEM_ERROR`; it never degrades to an empty alias inventory or an `ALLOW` candidate.
- `EXACT_KEY` uses a parameterized one-row-per-side SQLite join in an in-memory database. Keys are values, never SQL fragments.
- `SPATIAL_TEMPORAL` compares synthetic spatial-cell refs and timezone-aware intervals with a declared tolerance. It is not a geometry engine and proves no real-world spatial relationship.
- A zero-tolerance spatial-temporal boundary touch abstains instead of inventing inclusive-end semantics. Pair-specific temporal policy must resolve the boundary; positive tolerance is explicit and remains bounded to candidate comparison.
- Missing EvidenceRefs abstain. Any unequal source-role pair abstains for pair/domain-owned compatibility review because the generic seam owns no accepted global crosswalk. Restricted generalized context abstains for sensitivity review. Restricted exact geometry and living-person joins deny.
- `candidate_id` is RFC 8785/SHA-256 over request and endpoints. `spec_hash` binds the complete assessment excluding `assessment_id` and `spec_hash`.
- `--derive` validates the fully sealed assessment before stdout. A malformed or schema-invalid input returns a bounded `FAIL` result and never emits a schema-invalid assessment as successful output.
- CLI modes are mutually exclusive and long options are not abbreviated. `--fixtures` cannot be combined with assessment files or `--derive`, and `--derive` cannot be combined with assessment files, so an explicit input is never silently ignored; `--` remains available for a dash-prefixed filename.

## Non-publisher effects

The decision's effects are schema-fixed to false for lifecycle writes, evidence creation, policy decisions, review decisions, release decisions, publication, and public use. Even `ALLOW` only authorizes emission of the local report to stdout or a caller; it does not authorize any downstream effect.

## Directory Rules basis

Generic relationship meaning belongs in `contracts/joins/`; shape in `schemas/contracts/v1/joins/`; the dry-run helper in `tools/joins/`; synthetic cases in `fixtures/contracts/v1/joins/`; tests in `tests/joins/`; authoring provenance in `data/receipts/generated/`. Pair-specific meaning, source-role compatibility, domain alias acceptance or migration, policy, evidence, receipts, lifecycle data, and release remain in their owning roots. `control_plane/domain_lane_register.yaml` remains a projection-only review aid; consuming its unresolved-alias rows as a fail-closed signal, and treating loss of that signal as a validator dependency error, does not promote it into domain identity authority. Refusing a symlink at that canonical path also prevents another responsibility root from silently supplying the projection bytes.

## Non-effects and rollback

This profile uses synthetic refs, has no network client, writes no file or database, creates no evidence or receipt, and grants no identity, relationship truth, policy, review, release, publication, or public-use authority. Revert the bounded commit to remove it.
