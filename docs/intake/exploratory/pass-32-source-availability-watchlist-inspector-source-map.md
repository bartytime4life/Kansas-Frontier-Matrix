<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-source-availability-watchlist-inspector
title: Pass 32 source availability watchlist inspector - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; fixture-only; read-only
owners: OWNER_TBD - Source steward; UI steward; validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; pass-32; non-authoritative
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0016 with the current SourceAvailabilityWatchlist family and a bounded Explorer projection
truth_posture: CONFIRMED source statement and repository foundation / PROPOSED app-local projection / NEEDS VERIFICATION hosted exact-head checks and human review
related:
  - ../../../contracts/source/source_availability_watchlist.md
  - ../../../apps/explorer-web/src/features/source_availability_watchlist/README.md
  - ../../../fixtures/ui/source_availability_watchlist_projection/README.md
tags: [kfm, pass-32, source-availability, watchlist, explorer, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 32 source availability watchlist inspector

## Source statement

Pass 32 card `KFM-P32-FEAT-0016` proposes a watchlist that distinguishes stable source availability from material schema or content changes requiring a candidate work record. Its atlas `spec_hash` is `sha256:5abdf699c160c2341d1c9694a7d0aace32644b22843cde353c415b84eb7dd464`. The source treats the feature as a downstream, user- or operator-visible surface; it does not establish repository implementation or authority.

## Current repository reconciliation

At the inspected campaign base, KFM already has a fixture-first `SourceAvailabilityWatchlist` contract, strict schema, validator, deterministic fixture matrix, focused tests, workflow, and authoring receipt. That family owns aggregate review routing while preserving `SourceHealthAssessment` and `MaterialChangeAssessment` as separate authorities.

The missing bounded consumer is a read-only Explorer projection. This change does not add another source-health or materiality contract. It accepts only a closed public-safe projection derived elsewhere and renders stable, review-required, held, and error entries without creating or executing work.

## Implemented boundary

The adapter enforces:

- exact `ANSWER / ABSTAIN / DENY / ERROR` reason pairing;
- canonical timestamp and opaque KFM-reference syntax;
- one lexically ordered entry per source;
- exact stable/review/hold/error count closure;
- candidate-work references only for material `REVIEW_CANDIDATE` entries;
- coherent availability, change-class, material-kind, route, and reason combinations; and
- fixed-false network, activation, candidate execution, lifecycle write, authority, release, and publication flags.

The component is text-first and has no buttons, links, transport, storage, or lifecycle mutation. Invalid input renders nothing and cannot echo supplied canary detail.

## Directory Rules basis

The current implementation preserves responsibility roots adopted by ADR-0029: UI code under `apps/`, synthetic projection fixtures under `fixtures/ui/`, tests in the Explorer harness, source adaptation under `docs/intake/exploratory/`, and generated authoring accountability under `data/receipts/generated/`. No new root, contract, schema, policy, source, registry, receipt, proof, release, or publication home is created.

## Validation and non-effects

Validation consists of TypeScript compilation of the adapter/component, deterministic fixture-resolution checks, Explorer unit tests, browser-fixture typecheck, Playwright accessibility/render checks, and generated-receipt byte binding. Hosted exact-head checks remain review evidence after the draft PR opens.

This slice performs no source probe, network request, source activation, candidate creation/execution, policy evaluation, repository mutation from issue content, lifecycle write, release, deployment, promotion, publication, or public-source claim.

## Rollback

Before merge, close the draft and abandon its branch. After an authorized merge, revert the additive commit. No source, candidate, lifecycle, cache, release, deployment, or public state requires restoration.
