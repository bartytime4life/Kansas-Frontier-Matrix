<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/set-operation-provenance-receipt
title: SetOperationProvenanceReceiptCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Source-reconciliation steward · Data-quality steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; provenance; reconciliation; set-operation
responsibility: Define a fixture-only process-memory candidate that distinguishes set-operation semantics, ordered inputs, duplicate policy, row-count bounds, and digest-bound output without executing a query or creating source, evidence, catalog, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption and engine-specific equivalence; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../common/reversible_entity_reconciliation.md
  - ../common/measurement_support_reconciliation.md
  - ./spatial_transform_receipt.md
  - ../../schemas/contracts/v1/evidence/set_operation_provenance_receipt.schema.json
  - ../../fixtures/contracts/v1/evidence/set_operation_provenance_receipt/cases.json
  - ../../tools/validators/evidence/validate_set_operation_provenance_receipt.py
  - ../../tests/validators/evidence/test_validate_set_operation_provenance_receipt.py
  - ../../docs/intake/exploratory/pass-18-set-operation-provenance-receipt-source-map.md
tags: [kfm, evidence, provenance, reconciliation, set-operation, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-068."
  - "A PASS proves declaration and bounded count coherence only; it does not prove query execution, source identity, evidence closure, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# SetOperationProvenanceReceiptCandidate

`SetOperationProvenanceReceiptCandidate` is a bounded process-memory declaration for one cross-source or analytical set operation. It makes the distinction among `UNION` with duplicate removal, `UNION ALL`, `INTERSECT`, `EXCEPT`, symmetric difference, and an explicitly reviewed custom equivalent visible instead of hiding it inside an implementation query.

The candidate implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-068`: record the set operation and duplicate policy because inclusion, exclusion, and duplicate semantics can materially change reconciliation output.

## Boundary

A validator `PASS` proves only that:

- the candidate has a closed schema and deterministic profile hash;
- inputs are digest-bound, uniquely referenced, and canonically ordered;
- `EXCEPT` has one minuend and one subtrahend in order;
- the duplicate policy matches the declared operator;
- declared row counts satisfy only safe operator-specific bounds;
- query-plan, null-semantics, reconciliation-rule, and method references are declared; and
- authority claims remain fixed to `false`.

The validator does not execute SQL, dataframe, graph, or ETL code. It does not inspect records, deduplicate rows, infer equivalence across engines, authenticate a source, resolve a reference, prove that inputs share a schema, establish entity identity, decide evidence or policy, approve review, catalog, promote, release, publish, or authorize public use.

## Closed operator semantics

| Operator | Duplicate policy | Safe local count check |
|---|---|---|
| `UNION_DISTINCT` | `DISTINCT` | Output cannot exceed the sum of input row counts. |
| `UNION_ALL` | `RETAIN_ALL` | Output equals the sum of input row counts. |
| `INTERSECT` | `DISTINCT` | Output cannot exceed the smallest input row count. |
| `EXCEPT` | `DISTINCT` | Exactly two ordered inputs; output cannot exceed the minuend row count. |
| `SYMMETRIC_DIFFERENCE` | `DISTINCT` | Exactly two inputs; output cannot exceed their summed row count. |
| `CUSTOM` | `CUSTOM` | A rationale is required; no arithmetic equivalence is inferred. |

These are fixture-level consistency checks, not completeness proofs. In particular, the validator does not claim an exact count for distinct, intersection, difference, or custom operations.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared operator, input, output, provenance, and disclosure posture is locally coherent. |
| `ABSTAIN` | Execution or a required reference remains incomplete or unresolved. |
| `DENY` | Ordering, roles, duplicate policy, count bounds, public-support disclosure, deterministic identity, or custom semantics are incoherent. |
| `ERROR` | The candidate cannot be evaluated safely or declares execution error. |

These outcomes are not source-admission, evidence, catalog, policy, review, release, or publication decisions.

## Directory Rules basis

The object is process memory for an evidence-affecting reconciliation operation, so semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; repository validation under `tools/validators/evidence/`; executable conformance evidence under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

The packet remains distinct from entity reconciliation and measurement-support reconciliation: it records how declared sets were combined, not whether identities match or measurements are comparable. It creates no query-plan authority, source registry, canonical dataset, evidence store, catalog writer, policy rule, release record, or publication path.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_set_operation_provenance_receipt -v
python tools/validators/evidence/validate_set_operation_provenance_receipt.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source, query, dataset, reconciliation decision, evidence, catalog, policy, lifecycle, review, release, deployment, or public artifact.
