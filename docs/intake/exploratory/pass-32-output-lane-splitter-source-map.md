<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-output-lane-splitter-source-map
title: Pass 32 Output Lane Splitter Source Map
type: source-adaptation-record
version: v0.1.0
status: draft
owners: OWNER_TBD — Data steward · Evidence steward · Validation steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; fixture-only
owning_root: docs/
responsibility: Record the bounded adaptation of Pass 32 output-lane routing into repository artifacts.
truth_posture: cite-or-abstain
related:
  - ../../../contracts/data/output_lane_split_manifest.md
  - ../../../tools/generators/build_output_lane_split.py
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [pass-32, output-lanes, routing, source-map]
[/KFM_META_BLOCK_V2] -->

# Pass 32 Output Lane Splitter Source Map

## Candidate

`KFM-P32-PROG-0020` states that generated proof-of-concept outputs should be
split into feature-vector, scorecard, policy-report, receipt, and prefilter lanes
before review.

The Pass 32 atlas is a downstream carrier. It does not itself authorize repository
placement, implementation, promotion, release, or publication.

## Repository-fit checkpoints

The packet was initially authored against `main@03b37ee771410573f2a2050379417dd2758d1501`. Before delivery, the
placement and non-overlap checks were repeated against
`main@f622ec9fc52dfb762aa39d709094e6c8af749dfb`. At the delivery checkpoint:

- `contracts/data/` is the current semantic-contract family for data-related
  candidates and derived products;
- `schemas/contracts/v1/data/` is the current paired machine-shape lane;
- `tools/generators/` explicitly owns deterministic, reviewable generators that
  write only when requested and never decide authority;
- `tests/generators/` and `fixtures/contracts/v1/data/` are existing
  enforceability roots; and
- ADR-0029 accepts Directory Governance Standard v2.

Current repository search found no exact implementation of the Pass 32 output-lane
splitter card. Nearby catalog, telemetry, prefilter, receipt, scorecard, and
policy-report surfaces remain separate object families and are not replaced.

## Adaptation

The repository slice defines one closed manifest, one deterministic dry-run
generator, strict schema and semantic checks, exact synthetic polarity, a
read-only workflow, and an authoring receipt. Manifest identity is computed
through the repository-owned `packages/hashing` RFC 8785 JCS + SHA-256 helper
rather than a parallel local hashing implementation.

It deliberately does not create physical `feature-vectors/`, `scorecards/`,
`policy-reports/`, `receipts/`, or `prefilter/` data directories. The generator
emits temporary reviewer indexes only into an explicit empty destination.

## Non-effects

No live source access, data ingestion, payload movement, EvidenceBundle
resolution, policy decision, review approval, lifecycle promotion, release,
deployment, publication, or public-use authorization is performed.
