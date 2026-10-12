<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-pmtiles-range-diagnostics
title: Pass 32 PMTiles range diagnostics - governed implementation source map
type: exploratory-intake-source-map
version: v1.0.0
status: proposed; fixture-only; read-only
owners: OWNER_TBD - PMTiles steward; UI steward; security steward; release steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; exploratory; pass-32; non-authoritative
owning_root: docs/
responsibility: reconcile Pass 32 card KFM-P32-FEAT-0013 with the existing partial-read compatibility verifier and a bounded Explorer diagnostics projection
truth_posture: CONFIRMED source statement and repository verifier / PROPOSED app-local display / NEEDS VERIFICATION hosted exact-head checks and human review
related:
  - ../../../tools/validators/pmtiles/verify_partial_read.py
  - ./pass-32-pmtiles-partial-read-source-map.md
  - ../../../apps/explorer-web/src/features/pmtiles_range_diagnostics/README.md
  - ../../../fixtures/ui/pmtiles_range_diagnostics_projection/README.md
tags: [kfm, pass-32, pmtiles, range, diagnostics, explorer, structural-hold]
[/KFM_META_BLOCK_V2] -->

# Pass 32 PMTiles range diagnostics

## Source statement

Pass 32 card `KFM-P32-FEAT-0013` proposes a diagnostics surface showing Range-header, cache, ETag, sidecar, and headless-render results for PMTiles artifacts. Its atlas `spec_hash` is `sha256:1abffb98626cb8d413a0ce9ef0dcc0c9593b94421c527d993366bd80cf4adaf3`. The same source keeps PMTiles and other map artifacts downstream of evidence, policy, catalog closure, and release.

## Current repository reconciliation

KFM already contains a deterministic no-network partial-read compatibility verifier. It checks one captured byte range against a supplied containing leaf, PMIDX leaf digest and Merkle root, and PMSIG subject shape. Its successful result is deliberately `STRUCTURAL_HOLD`, not artifact health, because cryptographic verification, authentication of range metadata, Bao/BLAKE3 adoption, whole-archive recomputation, policy, and release remain unresolved.

This change adds only a strict display projection over that bounded result. It does not create a second digest, signature, sidecar, cache, render-health, policy, proof, or release authority.

## Implemented boundary

The adapter accepts detailed diagnostics only for `ANSWER / DIAGNOSTICS_AVAILABLE / STRUCTURAL_HOLD`. It requires:

- canonical observation time and opaque PMTiles artifact reference;
- bounded Range, Content-Range, ETag, and cache states;
- exact PMIDX `VERIFIED`, PMSIG `SHAPE_BOUND`, and cryptographic `UNVERIFIED` states;
- one non-negative verified offset, length, and leaf index;
- the exact current four structural checks;
- the exact current six unresolved holds;
- a bounded headless-render state and optional opaque receipt reference; and
- fixed-false network, archive-read, cryptographic verification, policy, health declaration, release, and publication flags.

A projection that claims cryptographic verification is malformed and renders nothing. Negative outcomes carry no artifact, range, sidecar, check, hold, or render detail. The component has no links, buttons, transport, file access, cache mutation, signing call, or lifecycle action.

## Directory Rules basis

UI code remains under `apps/`; synthetic projections under `fixtures/ui/`; tests in the Explorer harness; source adaptation under `docs/intake/exploratory/`; and generated authoring accountability under `data/receipts/generated/`. The existing validator remains under `tools/validators/pmtiles/`. These are existing responsibility roots under accepted ADR-0029; no parallel map-artifact, digest, signature, policy, proof, release, or publication home is introduced.

## Validation and non-effects

Validation consists of TypeScript compilation, deterministic fixture-resolution checks, Explorer unit tests, browser-fixture typecheck, Playwright checks, and generated-receipt byte binding. Hosted exact-head checks remain pending review evidence after the draft PR opens.

This slice performs no HTTP request, archive read, signature verification, sidecar resolution, policy evaluation, headless-render execution, cache mutation, artifact-health declaration, release, deployment, promotion, publication, or MapLibre source activation.

## Rollback

Before merge, close the draft and abandon its branch. After an authorized merge, revert the additive commit. No archive, sidecar, signature, cache, map, lifecycle, release, deployment, or public state requires restoration.
