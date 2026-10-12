<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/recursive-traversal-safety-assessment
title: RecursiveTraversalSafetyAssessmentCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Common contract steward · Query steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; common; query; recursive-cte; traversal; safety
responsibility: Define fixture-only recursion termination, depth, breadth, cycle, observation, and receipt declarations without executing a query or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and bounded repository gap; PROPOSED inactive assessment; UNKNOWN runtime adoption; NEEDS VERIFICATION dialect behavior, human review, and hosted exact-head CI"
related:
  - ../governance/query_run_record.md
  - ../../schemas/contracts/v1/common/recursive_traversal_safety_assessment.schema.json
  - ../../fixtures/contracts/v1/common/recursive_traversal_safety_assessment/cases.json
  - ../../tools/validators/validate_recursive_traversal_safety_assessment.py
  - ../../tests/validators/test_validate_recursive_traversal_safety_assessment.py
  - ../../docs/intake/exploratory/pass-18-recursive-traversal-safety-source-map.md
tags: [kfm, common, recursive-cte, hierarchy, lineage, cycle, depth, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-133."
  - "A PASS proves declaration coherence only; it does not prove query execution, termination in a database, evidence, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# RecursiveTraversalSafetyAssessmentCandidate

`RecursiveTraversalSafetyAssessmentCandidate` is an additive, fixture-only profile for declaring safety controls around recursive SQL traversal. It binds a query definition and dialect profile by digest, names traversal identity fields, records finite depth, node, and edge caps, requires an explicit termination predicate and depth-cap justification, and rejects absent cycle handling or silent partial results.

It implements the narrow requirement in supplied Pass 18 card `KFM-P18-INV-133`: recursive CTEs used for hierarchies, networks, route graphs, calendars, or lineage should declare termination, maximum depth, and cycle behavior, with `recursion_depth` and `cycle_detected` available in a query receipt.

## Boundary

A validator `PASS` proves only that:

- the closed candidate shape and deterministic profile hash agree;
- query, dialect, termination, justification, parity, identity, evidence, and limitation declarations satisfy local rules;
- depth, node, and edge caps are finite positive integers;
- cycle handling is explicit and cycle identity fields are drawn from traversal identity;
- depth exhaustion cannot be silently presented as a complete traversal;
- a declared observation agrees with its state and stays within declared guards; and
- any declared execution observation carries an opaque receipt reference.

The validator does not parse or execute SQL, connect to a database, inspect graph rows, resolve references or evidence, prove termination, compare database dialects, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Guard semantics

| Declaration | Required behavior |
|---|---|
| `max_depth` | Positive finite cap on recursive steps. Reaching the cap yields `ABSTAIN`, `DENY`, or `ERROR`, never `SILENT_PARTIAL`. |
| `max_nodes` / `max_edges` | Positive finite breadth caps for implementations that materialize or count visited structure. |
| `termination_predicate` | Digest-bound reference to the stopping rule; unresolved references abstain. |
| `cycle_strategy` | `VISITED_SET`, `PATH_REJECTION`, or `DIALECT_CYCLE_CLAUSE`; `NONE` denies. |
| `cycle_identity_fields` | Canonical non-empty subset of the declared traversal identity fields. |
| `on_cycle` | A cycle must stop and report, abstain, deny, or error; `IGNORE` denies. |

The profile carries no SQL text, parameter values, result rows, node values, edge values, credentials, or connection details.

## Observation semantics

- `NOT_RUN` carries no depth, cycle flag, visited counts, or receipt reference.
- `COMPLETE` carries bounded depth and counts, a false cycle flag, and a receipt reference.
- `DEPTH_LIMIT_REACHED` carries bounded observation fields and a receipt reference, but the overall validator outcome is `ABSTAIN` because the traversal is truncated.
- `CYCLE_DETECTED` carries a true cycle flag and a receipt reference. It may pass only when the declared cycle strategy and response are safe.
- `ERROR` produces validator `ERROR` and grants no authority.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The recursion guard, identity, parity, observation, receipt, and non-authority declarations are locally coherent. |
| `ABSTAIN` | Assessment, parity, a required reference, or a depth-limited traversal remains incomplete or unresolved. |
| `DENY` | A guard, cycle, observation, parity, timestamp, reference-array, limitation, or deterministic-identity declaration is incoherent. |
| `ERROR` | The candidate cannot be parsed or evaluated safely, or declares an assessment or observation error. |

These are validation results only, not proof that a recursive query terminates or returns complete or correct results.

## Directory Rules basis

Reusable traversal-safety meaning belongs under `contracts/common/`. Machine shape, synthetic replay, executable validation, conformance proof, orchestration, source reconciliation, and generated authoring provenance remain in their established responsibility roots.

No query engine, database adapter, graph store, lineage store, evidence store, policy lane, release path, public panel, or new root is created.

## Validation

```bash
python -m unittest tests.validators.test_validate_recursive_traversal_safety_assessment -v
python tools/validators/validate_recursive_traversal_safety_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no query, database, graph, lineage, evidence, policy, lifecycle, review, release, deployment, or public artifact.
