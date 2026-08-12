<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-25-receipt-proof-pairing-source-map
title: Pass 25 Receipt/Proof Pairing Source Map
type: source-map
version: v1.0.0
status: proposed; implementation-source-map; review-pending
owners: OWNER_TBD — Intake steward · Evidence steward · Proof steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: docs/
policy_label: internal; intake; pass-25; receipt; proof
responsibility: Reconcile Pass 25 card KFM-P25-IDEA-0017 with current repository surfaces and bound the fixture-only adaptation.
truth_posture: CONFIRMED source and bounded repository search / PROPOSED adaptation / NEEDS VERIFICATION human review
related:
  - ../../../contracts/governance/receipt_proof_pairing_assessment.md
  - ../../../schemas/contracts/v1/governance/receipt_proof_pairing_assessment.schema.json
  - ../../../data/receipts/generated/genrec-pass25-receipt-proof-pairing-20260811.json
tags: [kfm, pass-25, source-map, receipts, proofs, pairing]
[/KFM_META_BLOCK_V2] -->

# Pass 25 Receipt/Proof Pairing Source Map

## Source

Connected Google Drive document **KFM Pass 25 — Idea Index, Category Atlas, and Expansion Dossier**, card `KFM-P25-IDEA-0017`, proposes validating receipts and proof bundles as paired objects so missing proofs, duplicate logical keys, and orphaned proof files cannot silently pass. The atlas preserves the proposal as downstream candidate material and does not claim repository implementation.

## Repository reconciliation

Current `main` contains mature but separate receipt, proof, validation-report, generated-receipt, and domain-proof surfaces. Bounded searches found no exact closed `ReceiptProofPairingAssessmentCandidate` contract/schema/fixture/validator/test/workflow packet and no matching open pull request. Existing object families remain authoritative and are referenced only by opaque synthetic IDs.

## Adaptation decision

Implement one inactive, fixture-only assessment. It checks local cardinality, canonical ordering, subject identity, production time, resolution state, deterministic identity, and content binding. It deliberately does not open files referenced by receipt/proof IDs, verify signatures, resolve EvidenceBundles, decide policy/review, create lifecycle records, or authorize promotion/release/publication.

## Directory Rules decision

Cross-object integrity meaning belongs under `contracts/governance/`; shape under `schemas/contracts/v1/governance/`; replay cases under `fixtures/contracts/v1/governance/`; reusable validation under `tools/validators/governance/`; proof of enforceability under `tests/validators/governance/`; orchestration under `.github/workflows/`; authoring provenance under `data/receipts/generated/`.

## Deferred work

- real receipt/proof registry traversal;
- signature or attestation verification;
- lifecycle-specific pairing profiles;
- policy-significant reviewer rules;
- release-gate integration.

Each requires separate current-repository and authority evidence.
