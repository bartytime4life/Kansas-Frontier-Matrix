<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-family/validation
title: contracts/validation/ — Validation Assurance Semantic Contracts
type: lane-readme; semantic-contract-family
version: v0.1.0
status: draft; PROPOSED; additive
owners: OWNER_TBD — Validation steward · QA steward · Contracts steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; validation; assurance
[/KFM_META_BLOCK_V2] -->

# `contracts/validation/`

This lane owns human-readable semantic meaning for validation-assurance objects: what was tested, which adversarial profile was used, what survived, how semantic risk is classified, what remains unresolved, and what a result must never be used to authorize.

It does not own test execution, mutation tools, policy approval, merge authority, release decisions, or publication.

## Current proposed contract

- [`ValidatorAssuranceReport`](./validator_assurance_report.md) — deterministic campaign identity, operator set, mutant counts, surviving semantic gaps, bounded finite outcome, and explicit non-authority fields.
