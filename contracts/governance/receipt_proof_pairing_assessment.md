<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/receipt-proof-pairing-assessment
title: ReceiptProofPairingAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Proof steward · Validation steward · Review steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; governance; receipt; proof; pairing; integrity
responsibility: Define a bounded assessment of one-to-one receipt/proof pairing without resolving evidence, authenticating proof, deciding review or policy, changing lifecycle state, or authorizing release.
truth_posture: CONFIRMED connected-Drive source card and current-repository gap / PROPOSED inactive assessment / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ../../docs/intake/exploratory/pass-25-receipt-proof-pairing-source-map.md
  - ../../schemas/contracts/v1/governance/receipt_proof_pairing_assessment.schema.json
  - ../../fixtures/contracts/v1/governance/receipt_proof_pairing_assessment/cases.json
  - ../../tools/validators/governance/validate_receipt_proof_pairing_assessment.py
  - ../../tests/validators/governance/test_validate_receipt_proof_pairing_assessment.py
tags: [kfm, governance, receipts, proofs, pairing, fixture-only, no-network]
[/KFM_META_BLOCK_V2] -->

# ReceiptProofPairingAssessment Candidate

`ReceiptProofPairingAssessmentCandidate` makes one narrow integrity question testable: for a declared subject and logical key, is there exactly one receipt and exactly one proof, with no orphan, duplicate, subject mismatch, or time inversion?

It adapts Pass 25 card `KFM-P25-IDEA-0017`. The profile does not collapse receipts and proofs into one object. A receipt remains process memory; a proof remains a separately governed claim about validation or integrity. Matching local references does not resolve either object or establish real-world truth.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Every resolved synthetic logical key has one receipt and one proof, canonical ordering, matching subject, coherent time, and bound identity/hash. |
| `ABSTAIN` | At least one structurally coherent reference remains unresolved. |
| `DENY` | An orphan, duplicate logical key, subject mismatch, time inversion, count mismatch, review contradiction, or identity/hash drift exists. |
| `ERROR` | Input cannot be evaluated under the closed schema or bounded parser. |

A `PASS` does not authenticate bytes, evidence, signatures, policy, reviewers, promotion, release, or publication.

## Directory Rules basis

The primary responsibility is cross-object governance integrity, so meaning belongs under `contracts/governance/`. Machine shape, synthetic cases, executable validation, tests, read-only CI, source reconciliation, and authoring accountability remain in their established responsibility roots. No receipt, proof, evidence, release, or publication authority is duplicated.

## Validation

```bash
python -m unittest tests.validators.governance.test_validate_receipt_proof_pairing_assessment -v
python tools/validators/governance/validate_receipt_proof_pairing_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It creates no evidence, proof, lifecycle, release, deployment, cache, or public state requiring operational restoration.
