<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/threshold-policy-registry
title: ThresholdPolicyRegistry Candidate Contract
type: contract
version: v0.1.0
status: draft; PROPOSED_INACTIVE; unresolved-values-only; non-evaluator
owners: OWNER_TBD — Policy steward · Domain stewards · Validation steward · Release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; policy; thresholds; materiality; persistence; review-required; no-live-values
owning_root: contracts/
responsibility: Define the semantic meaning and non-effects of an inactive registry of unresolved threshold-policy slots.
related:
  - ../../policy/README.md
  - ../../policy/thresholds/README.md
  - ../../policy/thresholds/registry.v1.json
  - ../../schemas/contracts/v1/policy/threshold_policy_registry.schema.json
  - ../../fixtures/contracts/v1/policy/threshold_policy_registry/
  - ../../tools/validators/policy/validate_threshold_policy_registry.py
  - ../../tests/validators/test_validate_threshold_policy_registry.py
  - ../../docs/intake/exploratory/threshold-policy-registry-source-map.md
truth_posture: CONFIRMED repeated cross-domain registry pressure and absent canonical registry on authoring base / PROPOSED inactive unresolved-slot registry / UNKNOWN accepted values, stewards, consumers, evaluator binding, release enforcement, and production use
[/KFM_META_BLOCK_V2] -->

# ThresholdPolicyRegistry candidate

> Define one reviewable place to name unresolved threshold-policy slots without
> adopting the illustrative numbers found in source packets or domain notes.

## Status and boundary

This profile is `PROPOSED_INACTIVE`. Every entry is deliberately `UNRESOLVED`,
`UNBOUND`, and `HOLD`; every operator, value, unit, effective date, and
supersession reference is `null`.

A validator `PASS` proves only that the inactive registry has a closed shape,
deterministic identity, canonical ordering, resolvable repository pressure
references, and explicit non-effects. It does not make any threshold correct,
accepted, active, scientific, or suitable for a watcher or public decision.

## Why this slice exists

Pass 20 `EXP-008` calls for a cross-domain threshold-policy registry. The
attached and Drive idea sources include illustrative materiality, persistence,
AOD/FRP, soil-moisture, ozone, and CDL-drift values. Current domain files repeat
that thresholds are policy choices rather than universal scientific absolutes,
but no canonical cross-domain registry was found on the authoring base.

Copying those numbers into active policy would overclaim evidence and authority.
This first slice instead creates stable review slots and makes the missing
decisions machine-visible.

## Responsibility split

| Responsibility | Surface |
|---|---|
| Object meaning | `contracts/policy/threshold_policy_registry.md` |
| Machine shape | `schemas/contracts/v1/policy/threshold_policy_registry.schema.json` |
| Inactive candidate policy source | `policy/thresholds/registry.v1.json` |
| Synthetic examples | `fixtures/contracts/v1/policy/threshold_policy_registry/` |
| Deterministic validation | `tools/validators/policy/validate_threshold_policy_registry.py` |
| Behavior proof | `tests/validators/test_validate_threshold_policy_registry.py` |
| Read-only orchestration | `.github/workflows/threshold-policy-registry.yml` |
| Source adaptation and path decision | `docs/intake/exploratory/threshold-policy-registry-source-map.md` |

Directory Rules place semantic meaning in `contracts/`, machine shape in
`schemas/`, reviewed policy source in singular `policy/`, fixtures and tests in
their proof roots, and reusable validation in `tools/validators/`. No new root,
runtime store, source registry, release lane, proof store, or publication path is
created.

## Registry model

The candidate registry carries one record per threshold-policy question:

- a stable threshold ID, domain, metric, and threshold class;
- a bounded purpose statement;
- `value_state: UNRESOLVED`;
- null operator, value, unit, effective date, and supersession reference;
- `binding_state: UNBOUND` and `review_state: HOLD`;
- sorted reason codes requiring a value decision and steward review;
- sorted steward-role candidates;
- proposal-lineage evidence references; and
- repository `pressure_refs` showing where the unresolved question is already
  documented.

`pressure_refs` are not consumers and create no binding. They are checked only
for safe repository-relative syntax and file existence in the tested checkout.

## Deterministic rules

The validator enforces:

1. closed Draft 2020-12 JSON Schema shape;
2. RFC 8785 JCS plus SHA-256 identity over every field except `spec_hash`;
3. lexically sorted, unique threshold IDs;
4. sorted and unique reason, steward, evidence, and pressure-reference arrays;
5. the exact unresolved reason pair `NO_VALUE_ADOPTED` and
   `STEWARD_REVIEW_REQUIRED`;
6. existing, repository-relative pressure references with no symlinks;
7. null values and no consumer binding; and
8. false-valued authority flags.

## Adoption discipline

A later proposal to resolve even one slot must be a separate review unit. It
must name the domain owner, metric definition, unit, operator, effective window,
evidence basis, sensitivity analysis, negative fixtures, intended consumers,
compatibility posture, correction path, and rollback target. It must also decide
whether the value belongs in cross-domain policy or a domain-owned profile.

Schema validity or registry membership can never substitute for that review.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_threshold_policy_registry.py' \
  --verbose

python tools/validators/policy/validate_threshold_policy_registry.py \
  --registry

python tools/validators/policy/validate_threshold_policy_registry.py \
  --fixtures

python -m pytest tests/schemas/test_common_contracts.py \
  -q -k threshold_policy_registry
```

## Non-effects

This slice does not:

- adopt a numeric, categorical, or temporal threshold;
- define a scientific conclusion or emergency trigger;
- bind a watcher, detector, map, analysis, or policy evaluator;
- fetch or activate a source;
- evaluate policy or emit a `PolicyDecision`;
- mutate lifecycle, registry, receipt, proof, review, or release state; or
- authorize promotion, release, publication, notification, or public use.

## Rollback

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the isolated implementation commit. Because all slots
remain inactive, unresolved, and unbound, rollback requires no source
deactivation, data migration, decision correction, release withdrawal, cache
invalidation, or public notice.
