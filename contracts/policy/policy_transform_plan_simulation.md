<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-transform-plan-simulation
title: PolicyTransformPlanSimulation Contract
type: semantic-contract
version: v1.0.0
status: proposed
owners:
  - NEEDS VERIFICATION — policy steward
  - NEEDS VERIFICATION — privacy/sensitivity steward
  - NEEDS VERIFICATION — validation steward
  - NEEDS VERIFICATION — release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: public-doctrine; fixture-only; proposed-inactive; no-network; no-effects; fail-closed
related:
  - policy_obligation_reduction.md
  - ../../schemas/contracts/v1/policy/policy_transform_plan_simulation.schema.json
  - ../../tools/validators/policy/validate_policy_transform_plan_simulation.py
  - ../../fixtures/contracts/v1/policy/policy_transform_plan_simulation/README.md
  - ../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "This contract describes a deterministic simulation record only."
  - "It neither evaluates policy nor applies a transform."
  - "The source packet calls this concern Gate E, but ADR-0018 remains proposed; this contract therefore uses the explicit lifecycle phase PROCESS_TO_CATALOG_SIMULATION and claims no promotion-gate letter authority."
[/KFM_META_BLOCK_V2] -->

# PolicyTransformPlanSimulation

## Status

`PolicyTransformPlanSimulation` is a **PROPOSED_INACTIVE**, **FIXTURE_ONLY**, no-network profile. It checks whether a proposed transform plan is at least as restrictive as a separately validated `PolicyObligationReduction` snapshot.

It is the smallest safe bridge between:

1. a policy result that emits mechanical obligations;
2. deterministic maximum-severity obligation reduction; and
3. a later enforcement component that may apply transforms and write a `TransformReceipt`.

This profile stops before step 3.

## Source-derived strategy

The source packet separates two responsibilities:

- policy returns numeric/mechanical obligations;
- the publish pipeline enforces them.

It also proposes a simulation stage before enforcement and requires the enforcement stage to fail closed when any obligation is missing or mismatched. This contract implements only the simulation concern.

The source uses the label “Gate E” for process-to-catalog simulation. KFM's tracked `ADR-0018` also discusses an A–G promotion vocabulary but remains **proposed** and records unresolved gate semantics. To avoid silently accepting or colliding with that proposal, the machine field is:

```text
lifecycle_phase = PROCESS_TO_CATALOG_SIMULATION
```

No gate letter is normative in this profile.

## Preconditions

A simulation candidate may consume only a pinned reduction snapshot declaring:

```text
validator_profile  = kfm.policy.policy-obligation-reduction.v1
validation_outcome = PASS
```

The embedded snapshot must carry three linked identities:

```text
reduction_id     = "policy-obligation-reduction:" + first_24_hex(spec_hash)
result_spec_hash = SHA256(JCS(required result projection))
spec_hash        = content identity of the complete reduction record
```

The first relation prevents an arbitrary reduction ID from being paired with a different record hash. The projection hash prevents the embedded `required` dimensions from drifting independently of the snapshot. The simulator still does not authenticate the declaration or resolve the complete reduction record. The caller remains responsible for supplying and resolving a separately validated, content-pinned reduction.

## Dominance rules

The simulator compares each obligation dimension independently. A plan satisfies the reduction only when all dimensions are at least as restrictive.

### Effective transform order

```text
NONE < FUZZ_DATE < GENERALIZE < SUPPRESS
```

The plan's effective transform is derived as follows:

```text
record_action = SUPPRESS                            -> SUPPRESS
otherwise geometry_action in {GENERALIZE,SUPPRESS} -> GENERALIZE
otherwise date_action = FUZZ                        -> FUZZ_DATE
otherwise                                            -> NONE
```

Geometry-only suppression does not equal whole-record suppression.

### Independent dimensions

A plan must also preserve or exceed:

- maximum `generalize_distance_m`;
- maximum `date_fuzz_days`;
- required geometry suppression;
- latest `embargo_until`;
- the exact contributing obligation set;
- the exact source policy-reference set;
- the exact union of reason codes.

A stronger record action does not erase the other declared dimensions. This keeps the future enforcement and receipt burden inspectable.

## Assessment outcomes

The simulation assessment has two finite outcomes:

| Outcome | Meaning |
|---|---|
| `SATISFIES` | Every declared dimension is at least as restrictive. |
| `INSUFFICIENT` | One or more dimensions are weaker, missing, or bound to the wrong obligation/policy/reason set. |

`INSUFFICIENT` is a valid simulation result. It is not a malformed record. The validator returns `PASS` when an `INSUFFICIENT` record accurately stores the deterministic assessment.

Stable insufficiency codes are:

```text
TRANSFORM_TOO_WEAK
GENERALIZE_DISTANCE_TOO_SMALL
DATE_FUZZ_TOO_SMALL
GEOMETRY_SUPPRESSION_REQUIRED
EMBARGO_TOO_EARLY
CONTRIBUTOR_SET_MISMATCH
POLICY_REF_SET_MISMATCH
REASON_CODE_SET_MISMATCH
```

## Deterministic identity

The record uses the repository's RFC 8785 JCS plus SHA-256 implementation.

```text
spec_hash = SHA256(JCS(record without spec_hash and simulation_id))
simulation_id = "policy-transform-plan-simulation:" + first_24_hex(spec_hash)
```

No implicit rounding, source lookup, policy evaluation, or transform occurs during identity construction.

## Required enforcement preconditions

Every plan must state that later execution requires:

- verified input `spec_hash`;
- an output `spec_hash`;
- a `TransformReceipt`;
- a current policy recheck;
- accountable review;
- a rollback target.

These declarations do not satisfy those requirements. They preserve the future enforcement boundary.

## Governance and non-effects

Every governance flag is fixed to `false`:

- `policy_evaluated`;
- `transform_applied`;
- `repository_mutated`;
- `canonical_state_mutated`;
- `promotion_authorized`;
- `release_authorized`;
- `publication_authorized`;
- `public_use_authorized`;
- `network_accessed`.

A green validation proves only schema conformance, source snapshot ID/hash/projection consistency, deterministic simulation identity, exact stored assessment, and fixture-profile integrity. It does not prove policy authenticity, source admissibility, rights, sensitivity, evidence closure, transform correctness, output bytes, geometry/time behavior, review, release, publication, or public safety.

## Directory Rules basis

ADR-0029 accepts Directory Governance Standard v2. The file family follows existing responsibility roots:

| Responsibility | Home |
|---|---|
| semantic object meaning | `contracts/policy/` |
| machine shape | `schemas/contracts/v1/policy/` |
| synthetic examples | `fixtures/contracts/v1/policy/` |
| deterministic validator | `tools/validators/policy/` |
| tests | `tests/validators/` |
| read-only CI orchestration | `.github/workflows/` |
| generated authoring accountability | `data/receipts/generated/` |

No new root or parallel schema, contract, policy, source, registry, proof, receipt, release, or publication authority is created.

## Future enforcement boundary

A later, separately reviewed enforcement slice must:

1. resolve and authenticate the current reduction and policy decisions;
2. verify input bytes and `spec_hash`;
3. apply geometry, time, suppression, and embargo behavior before delivery;
4. verify transformed output bytes and spatial/temporal behavior;
5. write a `TransformReceipt` binding inputs, obligations, algorithms, outputs, and hashes;
6. re-run policy and release checks;
7. preserve correction and rollback targets;
8. keep public clients on governed transformed projections.

This profile must not be reused as proof that any of those effects occurred.

## Rollback

Before merge, close the pull request and delete its feature branch. After an authorized merge, revert the implementation commit or merge commit. Because the profile is inactive and fixture-only, rollback requires no source deactivation, data migration, cache invalidation, release withdrawal, or public correction.
