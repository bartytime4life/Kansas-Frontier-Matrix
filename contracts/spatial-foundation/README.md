<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-family/spatial-foundation
title: contracts/spatial-foundation/ — Spatial Foundation Semantic Contracts
type: lane-readme; semantic-contract-family
version: v0.1.0
status: draft; PROPOSED; additive
owners: OWNER_TBD — Spatial foundation steward · Contracts steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; spatial-foundation
[/KFM_META_BLOCK_V2] -->

# `contracts/spatial-foundation/`

This lane owns human-readable semantic meaning for cross-domain spatial-foundation objects whose primary responsibility is representation, control, geometry lineage, reference systems, and fitness-for-use rather than any one consuming domain.

It does not own machine schemas, source admission, legal boundary certification, title or ownership evidence, policy, lifecycle data, release decisions, public APIs, or map rendering.

## Current proposed contract

- [`BoundaryDerivationRecord`](./boundary_derivation_record.md) — survey-control observations, adjustment/residual metadata, derived geometry lineage, review outcome, and explicit non-title/non-legal-use limitations.

Machine shape remains under `schemas/contracts/v1/spatial-foundation/`; fixtures, validators, tests, workflows, and generated receipts remain in their own responsibility roots.
