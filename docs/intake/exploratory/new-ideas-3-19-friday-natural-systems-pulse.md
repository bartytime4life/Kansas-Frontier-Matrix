<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/new-ideas-3-19/friday-natural-systems-pulse
title: New Ideas 3-19-26 — Friday Natural-Systems Pulse Adaptation Record
type: exploratory-source-adaptation
version: v0.1.0
status: proposed; bounded-implementation-record
owners: OWNER_TBD — Intake steward · Data steward · Natural-systems domain stewards
created: 2026-08-06
updated: 2026-08-06
policy_label: public; exploratory; non-authoritative
related:
  - ../../../contracts/data/friday_natural_systems_pulse.md
  - ../../../contracts/data/material_change_assessment.md
  - ../../../contracts/source/source_ingestion_plan.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, new-ideas, natural-systems, material-change, friday-pulse]
[/KFM_META_BLOCK_V2] -->

# New Ideas 3-19-26 — Friday natural-systems pulse adaptation

## Goal

Record why one idea from the supplied *New Ideas 3-19-26* packet was selected for a dependency-closed repository slice, how it was narrowed to KFM's current trust boundaries, and which neighboring ideas remain deferred.

## Source statement

The packet proposes a Friday bundle spanning soil, air, vegetation, hydrology, and fauna/habitat. Its central behavior is change-triggered emission: compare deterministic metadata identities with the prior published state, emit nothing when nothing material changed, and produce the whole review bundle when any tracked dataset crosses its materiality rule. The packet also sketches action values `NONE`, `REBUILD`, `REVIEW`, and `PR`, plus policy and signed-receipt controls.

The packet is design input, not implementation authority. Its suggested direct scheduling, signing, rebuilding, committing, and pull-request creation are not copied into this slice.

## Repository reconciliation

Repository evidence at selection time established:

- a shared `MaterialChangeAssessment` contract, schema, validator, fixtures, and tests;
- domain-specific materiality adapters already able to produce `NON_EVENT`, `PROMOTION_CANDIDATE`, `HOLD`, or `ERROR` process memory;
- a fixture-only `SourceIngestionPlanCandidate` already covering scheduled ETL, conditional HTTP polling, and event-driven CDC selection; and
- no repository search result for a Friday natural-systems pulse or equivalent five-domain material-change bundle.

The smallest unfilled seam was therefore aggregation over existing material-change results, not another watcher, source adapter, materiality engine, scheduler, or publication workflow.

## Selected adaptation

`FridayNaturalSystemsPulseCandidate`:

- covers exactly `atmosphere`, `fauna_habitat`, `hydrology`, `soil`, and `vegetation`;
- consumes exact-byte-bound shared `MaterialChangeAssessment` fixtures;
- derives `NO_EVENT`, `PULSE_CANDIDATE`, `HOLD`, or `ERROR` with fail-closed precedence;
- makes complete five-domain coverage mandatory;
- binds a Monday-through-Friday UTC window;
- uses deterministic SHA-256 identity; and
- admits only `NONE` or `REVIEW` behavior.

The source vocabulary values `REBUILD` and `PR` remain visible only so attempted automation fails with `EXECUTION_ACTION_NOT_ADMITTED`.

## Why this slice was selected

| Criterion | Assessment |
|---|---|
| Reuses a current shared object | Yes — `MaterialChangeAssessment` |
| Adds a missing, source-derived capability | Yes — deterministic five-domain pulse aggregation |
| Can be proved with synthetic no-network fixtures | Yes |
| Requires source activation or current external terms | No |
| Creates policy, review, release, or publication authority | No |
| Rollback is additive and local | Yes |

## Deferred source-derived candidates

### Operational Friday scheduler and collector

**Deferred.** A live scheduler would need admitted source inputs, current source terms, state storage, retry/idempotency rules, runtime receipts, policy, accountable review, and repository-write authorization. No scheduled trigger is added here.

### Automatic rebuild or pull-request action

**Denied in this profile.** `REBUILD` and `PR` would cross from review process memory into operational mutation. They require separate contracts, repository-control verification, policy, review, and rollback behavior.

### Signed weekly pulse or OCI/ORAS publication

**Deferred.** The packet's Cosign, in-toto, OCI/ORAS, and attestation ideas require real artifact bytes, a reviewed trust root, a patched verifier, signer identity, and release integration. A fixture pulse is not a signature or proof.

### Probabilistic entity-resolution execution

**Deferred.** Candidate scoring, deterministic tie-breaks, canonical merging, and rollback are valuable, but they affect canonical identity and require a separately reviewed object-family and merge-authority boundary. This pulse slice neither scores nor merges entities.

### Live natural-systems source adapters

**Deferred.** The packet discusses multiple evolving water, soil, air, vegetation, and biodiversity sources. Current endpoint behavior, rights, sensitivity, cadence, and redistribution posture must be verified source by source before activation.

## Directory Rules basis

This adaptation record explains source-to-repository reasoning and therefore belongs under the existing `docs/intake/exploratory/` lane. It creates no doctrine, contract, schema, policy, source-registry, evidence, proof, release, or publication authority.

## Non-effects

This record and its companion fixture profile do not activate a source; contact a network; run on Fridays; persist operational state; execute a rebuild; create an issue or pull request; sign an artifact; evaluate policy; authenticate review; promote; release; deploy; publish; or permit public use.
