<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/aggregate-boundary-assessment
title: AggregateBoundaryAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Governance steward · Domain steward · Contract steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; aggregate-boundary; object-family; invariant; consistency
responsibility: Define a fixture-only assessment of one aggregate boundary without creating objects, executing persistence or transactions, resolving references or evidence, changing schemas or registers, or granting lifecycle authority.
truth_posture: "CONFIRMED attached Pass 18 card, attached DDD reference, visual review, connected Drive corroboration, and bounded repository gap; PROPOSED inactive assessment; UNKNOWN family adoption; NEEDS VERIFICATION governance, domain, contract, identity, evidence, and validation review plus hosted exact-head CI"
related:
  - ./object_identity_kind_assessment.md
  - ./object_family_domain_reference_profile.md
  - ../../control_plane/object_family_register.yaml
  - ../../schemas/contracts/v1/governance/aggregate_boundary_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/aggregate_boundary_assessment/cases.json
  - ../../tools/validators/governance/validate_aggregate_boundary_assessment.py
  - ../../tests/validators/governance/test_validate_aggregate_boundary_assessment.py
  - ../../docs/intake/exploratory/pass-18-aggregate-boundary-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# AggregateBoundaryAssessment Candidate

`AggregateBoundaryAssessmentCandidate` is an additive, fixture-only declaration
for one proposed aggregate boundary in one bounded context. It implements the
smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-465`: name a
root, members, invariants, validation scope, and external-reference rules before
treating the boundary as coherent.

The profile is not a mandate to migrate every KFM object family to an aggregate.
Each candidate remains independently reviewed and inactive.

## Boundary declaration

| Concern | Required declaration | Local check |
|---|---|---|
| Root | Exactly one member has role `ROOT`; the root is an entity and matches the aggregate family. | Opaque identity-kind and object-family bindings must be resolved for `PASS`. |
| Members | Canonically ordered root, entity, and value-object refs. | Duplicate or out-of-order member identity is denied. |
| Invariants | Canonical invariant refs with complete declared-scope coverage. | Incomplete or unknown coverage abstains. |
| External references | `ROOT_ONLY`. | External consumers cannot target internal members; internal-operation edges stay inside the boundary. |
| Consistency | Aggregate transaction unit, synchronous internal rules, asynchronous or explicit cross-boundary process. | Cross-aggregate transaction or synchronous-cascade declarations are denied. |

The validator never dereferences a member, invariant, contract, register,
identity assessment, repository, factory, review record, or EvidenceBundle.

## Repository and factory profiles

A repository may be `DECLARED`, `NOT_REQUIRED`, or `UNRESOLVED`. A declared
repository exposes only the root and returns a whole aggregate or proxy; direct
internal-member access is denied. `NOT_REQUIRED` is valid because not every
aggregate needs global access. `UNRESOLVED` abstains.

A factory may likewise be `DECLARED`, `NOT_REQUIRED`, or `UNRESOLVED`. A
declared factory creates the whole aggregate and declares invariant enforcement.
The validator creates nothing and does not prove that referenced code behaves as
declared.

## EvidenceBundle boundary

Cross-domain EvidenceBundle refs are a KFM-specific, proposed adaptation of the
source card's open question. They remain `REFERENCE_ONLY`, outside aggregate
consistency ownership, and non-resolving. They are not aggregate members and do
not become evidence merely because their refs are structurally valid.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic boundary, bindings, root, members, invariants, references, optional access profiles, consistency, review declaration, timestamp, and content identity are locally coherent. |
| `ABSTAIN` | Boundary adoption, register/identity binding, invariant coverage, repository/factory posture, or review state remains unresolved. |
| `DENY` | Root, member, reference, repository, factory, consistency, evidence-boundary, ordering, time, or content-identity declarations contradict the profile. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

`PASS` is a fixture-coherence result only. It is not permission to create,
persist, query, transact on, promote, release, deploy, or publish an aggregate.

## Authority boundary

A validator result does not:

- create, assemble, mutate, persist, query, distribute, or delete an object;
- open, commit, roll back, or coordinate a transaction;
- resolve a semantic contract, register binding, identity assessment, member,
  invariant, reference edge, EvidenceBundle, repository, factory, or review ref;
- change a bounded context, object family, schema, register, policy rule, review
  state, release record, runtime adapter, API, or public surface;
- approve review or authorize promotion, release, deployment, publication, or
  public use.

## Directory Rules basis

Cross-family aggregate-boundary meaning belongs under `contracts/governance/`.
Machine shape, synthetic replay, executable validation, conformance evidence,
read-only CI, source lineage, and authoring provenance stay in their established
responsibility roots. The partial object-family register remains unchanged, and
no bounded-context registry, aggregate registry, repository layer, factory
runtime, transaction manager, or public path is created.

## Validation and rollback

```bash
python -m unittest tests.validators.governance.test_validate_aggregate_boundary_assessment -v
python tools/validators/governance/validate_aggregate_boundary_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive candidate creates no
object, persistence, transaction, register, evidence, review, release,
deployment, publication, or public state that requires restoration.
