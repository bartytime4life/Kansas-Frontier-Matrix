<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/governed-run-chain/v1
title: Governed Run Chain Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - "../../schemas/contracts/v1/governance/quarantine_record.schema.json"
  - "../../schemas/contracts/v1/governance/governed_run_chain.schema.json"
  - "../../schemas/contracts/v1/runtime/run_receipt.schema.json"
  - "../../schemas/contracts/v1/policy/policy_decision.schema.json"
  - "../../schemas/contracts/v1/release/promotion_decision.schema.json"
  - "../../tools/validators/governance/validate_governed_run_chain.py"
  - "../../fixtures/contracts/v1/governance/governed_run_chain/"
  - "../../tests/validators/governance/governed_run_chain/"
tags: [kfm, governance, run-receipt, policy-decision, quarantine, promotion, validation]
notes:
  - "Defines a fixture-first linkage contract; it does not admit sources, mutate lifecycle state, promote, release, or publish."
  - "QuarantineRecord is process-control evidence and must not be collapsed into PolicyDecision, PromotionDecision, ProofPack, or ReleaseManifest."
[/KFM_META_BLOCK_V2] -->

# Governed Run Chain

The `GovernedRunChain` is a reviewable linkage object for one candidate's transition from execution memory through policy and either quarantine/hold or promotion approval.

It binds four already distinct trust surfaces:

1. `RunReceipt` — what the process did;
2. `PolicyDecision` — the finite policy result;
3. `QuarantineRecord` — why the candidate remains outside a higher-trust lifecycle state, when applicable;
4. `PromotionDecision` — an explicit approval record, only when the chain is promotable.

The chain is a validation surface, not a publication object. A valid `PROMOTABLE` chain does not move bytes, write `PUBLISHED`, create a release, or satisfy missing proof/review/signature gates.

## Finite outcomes

| Chain outcome | Required state | Forbidden state |
|---|---|---|
| `PROMOTABLE` | successful run, promotion-family `ANSWER`, no quarantine record, `APPROVE` promotion decision bound to the same run | quarantine record |
| `QUARANTINED` | promotion-family `DENY`, linked `QUARANTINED` record | promotion decision |
| `HELD` | promotion-family `ABSTAIN`, linked `HELD` record | promotion decision |
| `ERROR` | failed run and promotion-family `ERROR` | quarantine or promotion decision |

Unknown, mixed, or contradictory combinations fail closed.

## Linkage invariants

- `GovernedRunChain.spec_hash` must equal `RunReceipt.spec_hash`.
- Any `QuarantineRecord` must repeat the same `subject_ref` and `spec_hash` and must reference the exact `run_id` and `decision_id` embedded in the chain.
- Any `PromotionDecision` must reference the exact embedded `run_id`.
- The embedded `PolicyDecision.policy_family` must be `promotion`.
- `PROMOTABLE` is the only outcome that may carry a promotion decision.
- `QUARANTINED` and `HELD` require an explicit quarantine record so absence cannot be misread as clearance.

## QuarantineRecord semantics

`QuarantineRecord` records a bounded control-plane hold. It carries stable identity, subject, content hash, linked run and policy decision, finite state, reason codes, obligations, and time. `RELEASED` or `REJECTED` records additionally require a resolution reference and resolution time.

A quarantine record is not evidence that the candidate is false, unsafe in every context, or permanently denied. It is evidence that the candidate must not advance until its recorded obligations and authority requirements are resolved.

## Validation boundary

The validator is deterministic and no-network. It checks JSON safety, all referenced schemas, cross-object identity, and the outcome matrix. It does not authenticate identities, resolve references, evaluate OPA, verify signatures, produce proofs, modify repository state, or authorize release.

## Rollback

Rollback is removal of this additive contract/schema/validator/fixture/test packet. No data migration or published-state reversal is required because the slice writes no lifecycle data and activates no source.
