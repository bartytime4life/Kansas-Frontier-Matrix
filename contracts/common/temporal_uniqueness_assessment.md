<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-uniqueness-assessment/v1
title: TemporalUniquenessAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Temporal steward · Data steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; common; temporal-uniqueness; temporal-key; no-public-authority
owning_root: contracts/
responsibility: Define deterministic identity-plus-period uniqueness assessment semantics without inspecting tables, executing constraints, or creating evidence, policy, review, lifecycle, release, or publication authority.
truth_posture: "CONFIRMED source-card traceability and repository gap; PROPOSED inactive semantics; NEEDS VERIFICATION overlap-policy selection, human review, and consumer adoption"
related:
  - ./temporal_window.md
  - ./period_boundary_predicate_disclosure.md
  - ./temporal_authority_envelope.md
  - ../data/temporal_slice.md
  - ../../schemas/contracts/v1/common/temporal_uniqueness_assessment.schema.json
  - ../../fixtures/contracts/v1/common/temporal_uniqueness_assessment/cases.json
  - ../../tools/validators/validate_temporal_uniqueness_assessment.py
  - ../../tests/validators/test_validate_temporal_uniqueness_assessment.py
  - ../../docs/intake/exploratory/pass-18-temporal-uniqueness-source-map.md
tags: [kfm, common, temporal, uniqueness, valid-time, transaction-time, fixture-only]
notes:
  - "Implements the shared assessment portion of supplied Pass 18 card KFM-P18-INV-392."
  - "Overlap-denial, supersession allowance, and reviewed-parallel allowance are candidate policies; this contract selects no repository-wide default."
[/KFM_META_BLOCK_V2] -->

# TemporalUniquenessAssessmentCandidate

`TemporalUniquenessAssessmentCandidate` evaluates whether one time-aware record
is unique among declared peers that share the same opaque identity-key digest.
It treats identity plus validity semantics as one reviewable temporal key
instead of treating date fields as unrelated appended columns.

## Status and boundary

| Field | Value |
|---|---|
| Profile | `kfm.common.temporal-uniqueness-assessment.fixture.v1` |
| Adoption | `PROPOSED_INACTIVE` |
| Execution | Fixture-only, deterministic, no-network |
| Table or record inspection | Not performed |
| Constraint, denial, or quarantine | Not executed |
| Evidence, policy, review, release, publication | Not performed |
| Public-use authority | Fixed `false` |

The profile composes existing temporal values and disclosures by reference. It
does not alter `TemporalWindow`, declare a database primary key, expose key
values, authenticate lineage or review references, or select a repository-wide
temporal uniqueness policy.

## Temporal key profile

Each candidate binds:

- canonically ordered identity-field references and an opaque subject key
  digest;
- `VALID_TIME`, `TRANSACTION_TIME`, or `BITEMPORAL` comparison axes;
- either `ANY_DECLARED_AXIS_OVERLAP` or
  `ALL_DECLARED_AXES_OVERLAP` as the pair-conflict rule;
- zero or more declared peer records with the same key digest; and
- explicit finite intervals with inclusive start and end flags.

For bitemporal candidates, each peer comparison declares valid time first and
transaction time second. A pair conflicts when its computed overlaps satisfy
the declared pair-conflict rule. No raw business-key value or table row is
carried by this profile.

## Candidate overlap policies

| Mode | Local interpretation |
|---|---|
| `DENY_OVERLAP` | A pair conflict makes the candidate non-unique. |
| `ALLOW_WITH_SUPERSESSION` | A pair conflict is locally allowed only when a directional supersession relation and lineage reference are declared. |
| `ALLOW_REVIEWED_PARALLEL` | A pair conflict is locally allowed only when exception-review references are declared. |

The policy itself may be `UNRESOLVED`, which causes abstention. A reference is
not proof that a policy, lineage record, or review record resolves. These modes
preserve the source card's open question about which tables require overlap
denial versus overlap allowance.

## States and recommendations

The declared state is one of `UNIQUE`, `CONFLICT`, `ALLOWED_OVERLAP`, or
`UNRESOLVED`. A known conflict under the selected candidate policy yields
`DENY`; unresolved profile, policy, record, or window declarations yield
`ABSTAIN`; locally coherent unique or explicitly allowed-overlap declarations
yield `PASS`.

For `CONFLICT`, the packet may recommend `DENY_CANDIDATE` or
`QUARANTINE_CANDIDATE`. For `ALLOWED_OVERLAP`, it recommends
`REVIEW_OVERLAP`. Every recommendation remains non-executing: the schema fixes
`recommendation_only` to `true` and `disposition_executed` to `false`.

## Outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The temporal key, peer axes, intervals, policy declaration, state, and recommendation are locally coherent. |
| `ABSTAIN` | The temporal-key profile, overlap policy, subject, peer, or window remains unresolved. |
| `DENY` | A known overlap violates the candidate policy or a resolved declaration is contradictory. |
| `ERROR` | The candidate cannot be evaluated under the closed schema. |

These outcomes are not table constraints, evidence findings, policy decisions,
review decisions, lifecycle transitions, or public answers.

## Directory Rules basis

Accepted ADR-0029 and connected Directory Rules place shared temporal meaning
under `contracts/common/`, machine shape under `schemas/`, synthetic replay
under `fixtures/`, executable validation under `tools/`, conformance proof
under `tests/`, orchestration under `.github/`, source reconciliation under
`docs/intake/exploratory/`, and generated process memory under
`data/receipts/generated/`. No table, temporal database, policy, release, or
public-surface root is created.

## Validation and rollback

```bash
python -m unittest tests.validators.test_validate_temporal_uniqueness_assessment -v
python tools/validators/validate_temporal_uniqueness_assessment.py --fixtures
```

Before merge, close the draft pull request and abandon its branch. After an
authorized merge, revert this additive packet. It mutates no key, table,
record, interval, evidence object, policy, review state, lifecycle state,
release, deployment, or public surface.
