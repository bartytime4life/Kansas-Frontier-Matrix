<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/representation-fitness-assessment
title: RepresentationFitnessAssessment Contract
type: contract
version: v1.0.0
status: proposed; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — evidence steward; spatial representation steward; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; representation; fitness-for-use; fail-closed
owning_root: contracts/
responsibility: Define how one released or candidate representation is assessed against one declared use without turning visual clarity into evidence authority.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/evidence/representation_fitness_assessment.schema.json
  - ../../tools/validators/evidence/validate_representation_fitness_assessment.py
  - ../../fixtures/contracts/v1/evidence/representation_fitness_assessment/
  - ../../tests/evidence/test_representation_fitness_assessment.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "The assessment is use-specific. A representation may be fit for public orientation and unfit for an operational decision."
  - "A PASS-like fitness result is not truth, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# RepresentationFitnessAssessment

> **Purpose.** Make representation limits machine-checkable by binding CRS, spatial support, scale or resolution, declared precision, temporal support, source role, evidence, and intended use to a finite fitness result.

## Source basis

- *KFM Components Pass 18* KFM-11 requires explicit CRS, scale, resolution, time, uncertainty, and mediation, and its expansion agenda calls for representation and fitness-for-use acceptance criteria.
- *KFM Components Pass 13* and *Pass 15* identify the first common schema wave as the path from doctrine to reviewable machinery.

These documents are design evidence, not proof that this profile previously existed in the repository.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `FIT` | Every dimension is supported for the declared use. |
| `CONDITIONALLY_FIT` | No dimension is unsupported or unknown, but at least one condition and a visible obligation remain. |
| `NOT_FIT` | At least one dimension is unsupported for the declared use. |
| `UNKNOWN` | Support cannot be resolved strongly enough to claim fitness. |

## Fail-closed rules

- Declared precision cannot be finer than nominal source resolution.
- Candidate material cannot be `FIT` or `CONDITIONALLY_FIT`.
- Synthetic material cannot be fit for operational decisions; any positive synthetic use requires `REALITY_BOUNDARY_REQUIRED`.
- A generalized high-consequence representation cannot be marked unconditionally fit.
- Conditional results require obligations; `NOT_FIT` and `UNKNOWN` require reason codes.
- `spec_hash` binds the canonical JSON object excluding the hash field itself.

## Directory Rules basis

Semantic meaning belongs in `contracts/evidence/`; machine shape in `schemas/contracts/v1/evidence/`; deterministic checks in `tools/validators/evidence/`; fixtures in `fixtures/contracts/v1/evidence/`; tests in `tests/evidence/`; authoring provenance in `data/receipts/generated/`. These are existing responsibility roots adopted through ADR-0029; no new authority root is introduced.

## Non-effects and rollback

This profile is fixture-only. It does not read or write lifecycle data, admit a source, resolve evidence, decide policy, approve review, release an artifact, or publish a map. Revert the bounded commit to remove it; no public or lifecycle state requires reversal.
