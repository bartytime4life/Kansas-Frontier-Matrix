<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/query-save-recompile-query-run-record-source-map
title: Query-save-recompile QueryRunRecord source adaptation
type: source-map
version: v1.0.0
status: proposed-implemented-as-fixture-profile
owners: OWNER_TBD — Intake steward · Governance steward · Pipeline steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: repository-facing; exploratory-source-adaptation; non-authoritative
related:
  - ../../../contracts/governance/query_run_record.md
  - ../../../contracts/governance/ai_change_proposal.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Query-save-recompile QueryRunRecord source adaptation

## Goal

Adapt the no-network first slice from `Kansas_Frontier_Matrix_Pipeline_Living_Implementation_Manual_v0.3.pdf` to current repository evidence without creating duplicate object families or claiming autonomous loop behavior.

## Source-derived idea

The source manual proposes a governed loop that saves auditable summaries, evidence-resolution records, candidate deltas, validation reports, hashes, and rollback lineage while denying private chain-of-thought, direct publication, raw public paths, and model authority. It names `QueryRunRecord`, `CandidateDelta`, and `RecompileManifest` and recommends a fixture-only first pull request.

## Current repository assay

- `BriefingSignal` and `TemporalAuthorityEnvelope` already have contracts, schemas, fixtures, validators, tests, and workflow surfaces, so they are not recreated.
- `AIChangeProposal` already supplies a deterministic fixture-only candidate-change record with all mutation permissions denied.
- Repository search found doctrine references to `QueryRunRecord` and control-loop concepts but no corresponding machine contract/validator family.
- ADR-0029 is accepted and makes `docs/doctrine/directory-rules.md` the placement authority.

## Implemented adaptation

This slice adds only `QueryRunRecord` as a `PROPOSED_INACTIVE` governance object and references existing `AIChangeProposal` IDs. It includes:

- semantic contract;
- closed Draft 2020-12 schema;
- one bundled valid and fail-closed fixture matrix;
- deterministic no-network validator;
- focused tests;
- least-privilege workflow; and
- generated authoring receipt.

## Explicit deferrals

A later pull request may add `RecompileManifest` plus a no-write compiler over reviewed `AIChangeProposal` fixtures. That slice must independently govern output destinations, rollback targets, compiler identity, input/output byte hashes, no-PUBLISHED behavior, and generated-artifact ownership.

This source map does not activate a model, source, pipeline, scheduler, repository mutation, promotion, release, deployment, or publication path.
