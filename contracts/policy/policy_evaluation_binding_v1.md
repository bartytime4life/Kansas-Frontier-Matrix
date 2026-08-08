<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/policy/policy-evaluation-binding-v1
title: Policy Evaluation Binding v1
type: contract-profile
version: v0.1
status: draft; PROPOSED_INACTIVE; fixture-only; non-evaluator
owners: OWNER_TBD — Policy steward · Contracts steward · Validation steward · Release steward
created: 2026-08-08
updated: 2026-08-08
policy_label: repository-facing; policy; provenance; digest-binding; non-evaluator
owning_root: contracts/
truth_posture: exact-byte binding only; no evaluator authority
related:
  - ./policy_input_bundle_profile_v1.md
  - ./policy_decision_semantics_profile_v1.md
  - ../../schemas/contracts/v1/policy/policy_evaluation_binding_v1.schema.json
  - ../../tools/validators/policy/validate_policy_evaluation_binding_v1.py
[/KFM_META_BLOCK_V2] -->

# Policy Evaluation Binding v1

> **Purpose.** Bind one exact `PolicyInputBundle` fixture, one exact `PolicyDecision` fixture, and the evaluator declaration they share, without executing policy or authenticating the decision.

## Meaning

This profile records deterministic provenance for a future evaluator boundary. It requires SHA-256 digests for the exact input and decision files and requires the declared evaluator bundle reference/version to equal the evaluator declaration already present in the bound `PolicyInputBundle`.

It is deliberately **PROPOSED_INACTIVE**. A passing binding proves byte identity and declaration coherence only. It does not prove that OPA, Rego, or another evaluator executed; that a decision is authentic; that evidence, rights, consent, sensitivity, or review is sufficient; or that promotion, release, deployment, publication, or public use is authorized.

## Directory Rules basis

Semantic meaning remains in `contracts/policy/`; machine shape in `schemas/contracts/v1/policy/`; deterministic checking in `tools/validators/policy/`; fixtures in `fixtures/contracts/v1/policy/`; tests in `tests/validators/`; and read-only CI in `.github/workflows/`. No new authority root is created.

## Required binding

- binding id and profile version;
- repository-relative input path and SHA-256;
- repository-relative decision path and SHA-256;
- evaluator bundle reference and version;
- execution mode fixed to `DECLARED_ONLY`;
- all authority flags fixed false.

The validator rejects traversal, symlinks, missing files, digest mismatch, malformed JSON, input-profile mismatch, decision-schema mismatch, evaluator declaration mismatch, and any authority escalation.

## Rollback

Close the draft PR before merge or revert the additive commit after merge. No policy runtime, lifecycle state, release record, deployment, or public artifact is mutated.
