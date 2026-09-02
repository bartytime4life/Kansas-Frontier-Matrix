<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-obligation-reduction
title: PolicyObligationReduction Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Policy steward · Contracts steward · Schema steward · Validation steward · Release steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/policy/policy_obligation_reduction.schema.json
  - ../../fixtures/contracts/v1/policy/policy_obligation_reduction/
  - ../../tools/validators/policy/validate_policy_obligation_reduction.py
  - ../../tests/validators/test_validate_policy_obligation_reduction.py
  - ../../packages/hashing/src/hashing/core.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, policy, obligations, reduction, geoprivacy, date-fuzzing, embargo, fail-closed, deterministic]
notes:
  - "This contract defines a fixture-only deterministic reducer over obligations that have already been issued elsewhere."
  - "It does not run OPA, decide policy, apply a transform, mutate data, or authorize promotion or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# PolicyObligationReduction Contract

> **Purpose.** Define one deterministic, inspectable, non-authoritative record for combining already-issued policy obligations without weakening any input obligation.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Algorithm | `kfm-policy-obligation-max-severity-v1` |
| Machine shape | `schemas/contracts/v1/policy/policy_obligation_reduction.schema.json` |
| Validator | `tools/validators/policy/validate_policy_obligation_reduction.py` |
| Live policy engine | None |
| Transform executor | None |
| Promotion or release effect | None |
| Public-use effect | None |

A conforming record proves only that a bounded set of declared obligation objects was reduced according to the deterministic mechanistics in this contract and that the record reproduces those mechanics.

It does **not** prove that:

- an accepted policy bundle issued any input obligation;
- OPA, Conftest, or another policy decision point ran;
- the policy inputs were complete, current, authentic, or authorized;
- a sensitivity, rights, consent, evidence, review, or release decision is valid;
- a generalization, date fuzz, geometry suppression, whole-object suppression, or embargo was applied;
- a repository, canonical record, lifecycle object, API response, map artifact, export, release, or publication may be changed.

## Source-derived design

The supplied *New Ideas 3-7-2026* packet proposes mechanical geoprivacy obligations rather than prose-only policy results. It describes:

- a ranked transform where `SUPPRESS` outranks `GENERALIZE`, which outranks `FUZZ_DATE`, which outranks `NONE`;
- the maximum declared geometry-generalization distance;
- the maximum declared date-fuzz interval;
- geometry suppression when any contributing obligation requires it;
- the latest declared embargo date;
- Gate E simulation before Gate F enforcement;
- receipt-backed, fail-closed handling rather than client-only hiding.

This contract implements only the deterministic reduction step. Policy evaluation, enforcement, transform receipts, release integration, and public delivery remain separate governed work.

## Directory Rules basis

ADR-0029 adopts Directory Rules v2 and treats paths as authority claims. This slice uses existing responsibility roots:

| Responsibility | Path family |
|---|---|
| Semantic meaning of a policy object | `contracts/policy/` |
| Machine-checkable shape | `schemas/contracts/v1/policy/` |
| Synthetic positive and negative examples | `fixtures/contracts/v1/policy/` |
| Validation implementation | `tools/validators/policy/` |
| Validator tests | `tests/validators/` |
| Read-only CI orchestration | `.github/workflows/` |
| Generated authoring accountability | `data/receipts/generated/` |

No new root, policy-rule authority, source registry, schema home, release home, proof home, or publication path is created.

## Object meaning

A `PolicyObligationReduction` binds six concerns without collapsing their authority:

1. **Subject and operation** — the object and operation for which the obligations were assembled.
2. **Declared inputs** — obligation carriers that are already present and explicit.
3. **Mechanical reduction** — the finite maximum-severity calculation.
4. **Deterministic identity** — RFC 8785 JCS plus SHA-256 over the stable record projection.
5. **Provenance** — input references and the validator implementation used for this fixture profile.
6. **Non-effects** — explicit declarations that the record does not evaluate policy or create authority.

## Input obligation

Each input obligation contains:

| Field | Meaning |
|---|---|
| `obligation_id` | Stable identity of the declared obligation. |
| `policy_decision_ref` | Reference to the decision or candidate decision that supplied it. This profile does not resolve or authenticate the reference. |
| `transform` | Highest whole-record transform declared by that input: `NONE`, `FUZZ_DATE`, `GENERALIZE`, or `SUPPRESS`. |
| `generalize_distance_m` | Minimum geometry-generalization distance required by that input. |
| `date_fuzz_days` | Minimum date-fuzz interval required by that input. |
| `suppress_geometry` | Whether geometry must be omitted regardless of other transform fields. |
| `embargo_until` | Earliest date on which the input would stop requiring embargo, or `null`. |
| `reason_codes  | Stable, sorted, unique reason codes. |

`transform` and `suppress_geometry` are deliberately separate. `SUPPRESS` represents the strongest whole-record transform; `suppress_geometry` represents geometry-only omission and may accompany another transform.

## Reduction mechanics

For a nonempty input set:

```text
transform               = max by NONE < FUZZ_DATE < GENERALIZE < SUPPRESS
generalize_distance_m   = max(all input distances)
date_fuzz_days          = max(all input fuzz intervals)
suppress_geometry       = any(input suppress_geometry is true)
embargo_until           = latest non-null input embargo date, otherwise null
contributing ids        = sorted unique input obligation ids
source policy refs      = sorted unique input policy-decision refs
reason codes            = sorted unique union of all input reason codes
```

The reducer is:

- **order-independent** — permutations produce the same result;
- **idempotent for the same declared input set** — replay produces the same result;
- **monotone** — adding an obligation cannot weaken a mechanical output;
- **loss-visible** — every input identity, policy reference, and reason code remains represented in the result;
- **side-effect free** — the reducer returns a value and does not mutate its inputs.

## Canonical record rules

A stored record is conformant only when:

- `inputs` are sorted by `obligation_id`;
- obligation IDs are unique;
- every input `reason_codes` array is sorted and unique;
- `provenance.input_refs` exactly equals the sorted input obligation IDs;
- result reference arrays and reason codes are sorted and unique;
- the recorded result exactly equals a fresh reduction of the inputs;
- the `spec_hash` matches the RFC 8785 JCS projection;
- `reduction_id` equals `policy-obligation-reduction:` plus the first 24 hexadecimal characters of the same digest;
- all governance flags remain `false`.

The spec-hash projection excludes only `spec_hash` and `reduction_id`; all other declared record fields remain identity-bearing.

## Input coherence

The profile rejects internally contradictory input carriers:

- `GENERALIZE` requires `generalize_distance_m > 0`;
- `FUZZ_DATE` requires `date_fuzz_days > 0`;
- a positive generalization distance requires transform rank `GENERALIZE` or `SUPPRESS`;
- a positive date-fuzz interval requires transform rank `FUZZ_DATE`, `GENERALIZE`, or `SUPPRESS`;
- `NONE` requires both numeric transform fields to be zero;
- an empty input set is invalid.

An embargo or geometry-only suppression may accompany any transform.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape and deterministic semantic checks succeeded. |
| `FAIL` | The record was readable but one or more declared invariants failed. |
| `ERROR` | The record, schema, or bounded parser could not be evaluated safely. |

These are validator outcomes, not policy outcomes and not release decisions.

## Gate relationship

This profile is suitable for a future **Gate E simulation** step:

1. gather already-issued obligations;
2. reduce them deterministically;
3. compare the proposed transform plan with the reduced result;
4. attach receipt-ready metadata;
5. hold on mismatch.

Gate F enforcement remains out of scope. A later enforcement slice must re-evaluate current policy, verify the effective bundle and reviewer authority, apply transforms through a separately governed component, verify output bytes and geometry/time behavior, and emit transform and release receipts.

## Security and privacy posture

- Inputs and fixtures are synthetic.
- The validator reports file-relative names and stable finding codes, not input values.
- No network access is used.
- No precise sensitive geometry, living-person data, DNA/genomic data, archaeology, rare-species location, private parcel, infrastructure detail, secret, token, or credential is required.
- Client-only hiding is not enforcement. A later public system must serve transformed artifacts rather than load precise data and hide it in styling.

## Example

```json
{
  "inputs": [
    {
      "obligation_id": "policy-obligation:habitat-date-fuzz",
      "policy_decision_ref": "policy-decision:habitat-001",
      "transform": "FUZZ_DATE",
      "generalize_distance_m": 0,
      "date_fuzz_days": 365,
      "suppress_geometry": false,
      "embargo_until": "2028-01-01",
      "reason_codes": ["DATE_PRECISION_RESTRICTED"]
    },
    {
      "obligation_id": "policy-obligation:rare-site-generalize",
      "policy_decision_ref": "policy-decision:rare-site-001",
      "transform": "GENERALIZE",
      "generalize_distance_m": 1000,
      "date_fuzz_days": 30,
      "suppress_geometry": false,
      "embargo_until": "2031-01-01",
      "reason_codes": ["EXACT_LOCATION_RESTRICTED"]
    }
  ],
  "result": {
    "transform": "GENERALIZE",
    "generalize_distance_m": 1000,
    "date_fuzz_days": 365,
    "suppress_geometry": false,
    "embargo_until": "2031-01-01",
    "contributing_obligation_ids": [
      "policy-obligation:habitat-date-fuzz",
      "policy-obligation:rare-site-generalize"
    ],
    "source_policy_refs": [
      "policy-decision:habitat-001",
      "policy-decision:rare-site-001"
    ],
    "reason_codes": [
      "DATE_PRECISION_RESTRICTED",
      "EXACT_LOCATION_RESTRICTED"
    ]
  }
}
```

The complete fixture also carries deterministic identity, provenance, invariants, and non-effects.

## Validation

Focused validation:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_policy_obligation_reduction.py' \
  --verbose

python tools/validators/policy/validate_policy_obligation_reduction.py --fixtures

python -m pytest tests/schemas/test_common_contracts.py \
  -q -k policy_obligation_reduction
```

## Compatibility

- The executable `sha256:<64 lowercase hexadecimal>` identity grammar is preserved.
- This slice does not change existing `PolicyDecision`, `PolicyInputBundle`, `SensitivityLabel`, `DecisionEnvelope`, release, or receipt schemas.
- The object is additive and inactive.
- No live consumer, API route, policy bundle, Rego package, source descriptor, lifecycle dataset, map layer, or public product is modified.

## Rollback

Before merge, close the pull request and delete its feature branch.

After an authorized merge, revert the implementation commit or merge commit. Because the profile is fixture-only and inactive, rollback requires no source deactivation, canonical-data migration, cache invalidation, release withdrawal, or public correction.

## Open verification

- Which accepted policy-bundle vocabulary will emit obligation objects?
- Which release gate owns simulation and which owns enforcement?
- Which transform component will produce `TransformReceipt` artifacts?
- Which reviewer classes may approve sensitive-domain obligation profiles?
- Whether a later runtime package should expose this reducer as a stable API.
