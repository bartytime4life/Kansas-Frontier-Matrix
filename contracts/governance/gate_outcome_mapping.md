<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/gate-outcome-mapping
title: GateOutcomeMapping Contract
type: semantic-contract; deterministic mapping profile; fixture-only
version: v0.1.0
status: proposed; inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Governance steward · Runtime steward · Release steward · Evidence steward · Policy steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; governance; finite-outcomes; evidence-bound; fail-closed
related:
  - ./README.md
  - ../runtime/decision_envelope.md
  - ../release/promotion_decision.md
  - ../../schemas/contracts/v1/governance/gate_outcome_mapping.schema.json
  - ../../tools/validators/governance/validate_gate_outcome_mapping.py
[/KFM_META_BLOCK_V2] -->

# GateOutcomeMapping

A `GateOutcomeMapping` is a deterministic, fixture-only profile for translating one bounded gate state into an established KFM downstream decision vocabulary. It adapts Pass 22 card `KFM-P22-PROG-0012` without creating a new promotion authority, policy engine, runtime response, release object, or publication path.

## Source-derived rule and repository adaptation

The source candidate calls for finite mapping rather than free-form outcomes: a passing gate proceeds toward promotion or an answer, a failing gate denies, insufficient evidence abstains, and an execution failure errors.

Current repository contracts already define two destination vocabularies:

- `PromotionDecision.decision` uses `APPROVE`, `DENY`, and `ABSTAIN`.
- `DecisionEnvelope.outcome` uses `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`.

To avoid a competing release vocabulary, the source term `PROMOTE` is adapted to `PromotionDecision.decision = APPROVE`. `APPROVE` means eligible to proceed to a separately governed publication stage; it does not publish. Because the current `PromotionDecision` schema has no `ERROR` member, a gate execution error maps to `DecisionEnvelope.outcome = ERROR`, including when the requested surface was promotion.

## Deterministic mapping table

| Gate state | Target surface | Mapped outcome | Destination contract | Validator outcome |
|---|---|---|---|---|
| `PASS` | `PROMOTION` | `APPROVE` | `PromotionDecision` | `PASS` |
| `PASS` | `ANSWER` | `ANSWER` | `DecisionEnvelope` | `PASS` |
| `FAIL` | either | `DENY` | target-appropriate contract | `DENY` |
| `INSUFFICIENT_EVIDENCE` | either | `ABSTAIN` | target-appropriate contract | `ABSTAIN` |
| `ERROR` | either | `ERROR` | `DecisionEnvelope` | `ERROR` |

The profile requires a `RunReceipt` reference and `PolicyDecision` reference for every mapping. A passing or failing gate requires resolved EvidenceBundle support. An insufficient-evidence or error state carries no EvidenceBundle reference and must preserve that absence explicitly.

## Invariants

1. Outcomes and reason codes are closed enumerations; free-form terminal states are invalid.
2. `PASS` requires `evidence_state = RESOLVED` and a non-null `evidence_bundle_ref`.
3. `FAIL` also requires resolved evidence, because denial must be inspectable rather than guessed.
4. `INSUFFICIENT_EVIDENCE` requires `evidence_state = UNRESOLVED` and a null EvidenceBundle reference.
5. `ERROR` requires `evidence_state = ERROR` and a null EvidenceBundle reference.
6. The stored mapped outcome, destination contract, and reason code must exactly equal the deterministic mapping table.
7. A valid mapping grants no execution authority. All governance effects remain false.
8. `mapping_id` and `spec_hash` are deterministic and locally replayable.

## Deterministic identity

`spec_hash` is the repository hashing profile applied to the full JSON object after removing `mapping_id` and `spec_hash`. `mapping_id` is `kfm:gate-outcome-mapping:` plus the first 24 hexadecimal characters of `spec_hash`.

## Directory Rules basis

This object defines cross-family governance semantics, so meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic cases under `fixtures/contracts/v1/governance/`; validation under `tools/validators/governance/`; focused tests under `tests/validators/`; read-only CI under `.github/workflows/`; source adaptation under `docs/intake/exploratory/`; and generated authoring provenance under `data/receipts/generated/`.

No new root or parallel contract, schema, policy, release, proof, receipt, runtime, or publication authority is created.

## Trust boundary and non-effects

A passing profile proves only schema validity, evidence-state consistency, deterministic mapping, identity, and exact fixture replay. It does not:

- evaluate policy or resolve evidence;
- emit a `PromotionDecision` or `DecisionEnvelope`;
- approve, execute, or perform promotion;
- generate or return an answer;
- create a receipt, proof, release, deployment, or publication;
- authorize public use or bypass review, correction, or rollback controls.

## Rollback

Revert the additive fixture-only packet. It has no runtime consumer, source activation, lifecycle write, policy mutation, release mutation, deployment, cache effect, or public artifact.
