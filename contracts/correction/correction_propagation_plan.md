<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/correction/correction-propagation-plan
title: CorrectionPropagationPlan Contract
type: semantic-contract; derivative-invalidation planning
version: v0.1.0
status: proposed; fixture-only; no-network; non-executing
owners: OWNER_TBD — Correction steward · Release steward · Runtime steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; correction; rollback; derivative-invalidation
related:
  - ./correction_notice.md
  - ./supersession_notice.md
  - ../../schemas/contracts/v1/correction/correction_propagation_plan.schema.json
[/KFM_META_BLOCK_V2] -->

# CorrectionPropagationPlan

A `CorrectionPropagationPlan` is a deterministic dependency inventory for carrying one correction, supersession, withdrawal, or rollback into affected derivative surfaces. It makes stale carriers visible before rebuilding; it does not execute invalidation, repoint an alias, issue a release, delete history, or authorize publication.

## Source basis

The KFM correction doctrine requires append-only lineage, derivative invalidation, stale/superseded/withdrawn visibility, alias repointing, cache/index invalidation, and preservation of prior release history. The research agenda asks how corrections propagate to tiles, graphs, APIs, caches, Focus Mode, Story Nodes, exports, and citations. The briefing integration blueprint gives an explicit ten-step correction cascade and requires completion evidence.

## Invariants

- declared surface kinds exactly match the entry inventory;
- entries are canonical and duplicate-free;
- public and semi-public carriers cannot be left at `REVIEW_ONLY`;
- `COMPLETED` dynamically requires a completion-receipt reference;
- alias repointing or republishing requires a replacement release and matching target reference;
- timestamps cannot be later than the observation time;
- summary counts and overall outcome are recomputed;
- all mutation, release, publication, and history-deletion claims remain false.

## Finite outcomes

`PASS` validates a coherent ready or completed plan; `ABSTAIN` signals a blocked dependency; `DENY` covers closure or integrity failure; `ERROR` covers explicit propagation error or unreadable input. A pass does not prove downstream systems consumed the plan.

## Directory Rules basis

Meaning belongs in `contracts/correction/`; shape in `schemas/contracts/v1/correction/`; synthetic dependency inventories in `fixtures/contracts/v1/correction/`; validation in `tools/validators/correction/`; tests in `tests/validators/`; CI in `.github/workflows/`; and generated authoring provenance in `data/receipts/generated/`.

## Validation

```bash
python -m unittest tests.validators.test_validate_correction_propagation_plan -v
python tools/validators/correction/validate_correction_propagation_plan.py --fixtures
```

## Rollback

Revert the additive packet. No cache, alias, release, public route, or historical object is changed by this profile.
