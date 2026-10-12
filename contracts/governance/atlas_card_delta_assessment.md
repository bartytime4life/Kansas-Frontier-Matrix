# AtlasCardDeltaAssessmentCandidate

**Status:** PROPOSED fixture-only assessment profile

**Profile:** `kfm.governance.atlas-card-delta-assessment-candidate.v1`

**Authority:** comparison support only; no atlas mutation, truth promotion, review approval, release, publication, or public-use authority

## Purpose

`AtlasCardDeltaAssessmentCandidate` turns two synthetic Atlas-card snapshots into a deterministic, reviewable delta. It is the non-visual foundation for a future Atlas diff viewer: consumers can render the assessment, but they do not infer changes independently or treat presentation as authority.

The profile compares stable identity, normalized statement, truth label, evidence references, dependency identifiers, candidate authority families, and the snapshot `spec_hash`. It emits one finite outcome with stable reason codes.

## Required behavior

The validator must:

1. accept exactly one before/after pair, including bounded add and remove cases;
2. require stable card identity across modifications;
3. derive the transition and changed fields from the snapshots;
4. derive added and removed evidence and dependency references;
5. require every declared delta collection to be sorted, unique, and exact;
6. require a changed `spec_hash` when semantic fields change;
7. abstain when a target snapshot remains `UNKNOWN` or `NEEDS_VERIFICATION`;
8. abstain when a target snapshot claims `CONFIRMED` without evidence references;
9. deny any claimed mutation, approval, promotion, release, publication, or public-use effect; and
10. return `PASS`, `ABSTAIN`, `DENY`, or `ERROR` with deterministic reason codes.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared delta exactly matches the bounded snapshots and does not overclaim authority. |
| `ABSTAIN` | The delta is structurally coherent, but the target truth posture is unresolved or unsupported. |
| `DENY` | Identity, delta, hash, ordering, or authority-effect invariants fail. |
| `ERROR` | The caller declares an upstream source/read failure, so a trustworthy comparison cannot be completed. |

## Authority boundary

A passing assessment does not:

- edit either Atlas card;
- decide which snapshot is correct;
- resolve or validate evidence references;
- adopt a proposal or change a truth label;
- approve review, merge, release, publication, or public use;
- create a user interface, dashboard, or canonical Atlas history.

The future visual layer should consume this profile through a governed adapter. It must preserve the finite outcome and reason codes instead of recomputing or visually hiding them.

## Directory Rules basis

- `contracts/governance/` owns the semantic comparison contract.
- `schemas/contracts/v1/governance/` owns its machine shape.
- `fixtures/contracts/v1/governance/` owns deterministic examples.
- `tools/validators/governance/` owns executable comparison.
- `tests/validators/governance/` owns focused proof.
- `docs/intake/exploratory/` preserves the Drive-to-repository source map.
- `.github/workflows/` owns read-only hosted orchestration.
- `data/receipts/generated/` records AI-authoring process memory.

No new root or parallel Atlas, schema, policy, proof, release, or publication authority is created.

## Rollback

Revert the additive feature commit. The profile mutates no Atlas card, registry, evidence object, policy decision, release record, deployment, or published artifact.
