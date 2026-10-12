<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/verified-rendering-resource-envelope-source-map
title: Verified Rendering Resource Envelope - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Map runtime steward · UI steward · Security steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; intake; map; verification; resource-budget; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from supplied verify-before-render proposals to one bounded runtime assessment without duplicating renderer, verifier, release, policy, review, or publication authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward review, future worker integration, and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/runtime/verified_rendering_resource_envelope.md
  - ../../../contracts/ui/renderer_capability_profile.md
  - ../../../contracts/evidence/verifier_capability_portability.md
  - ../../standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
tags: [kfm, intake, full-atlas, rendering, verification, worker, budget]
notes:
  - "Repository collision review was refreshed against main@169ac1946812b6452a28c38ee57bc78ee41901b8."
  - "The supplied MapLibre operating manual was text-extracted and rendered at pages 11, 12, and 21 for boundary, performance, and rollback QA."
[/KFM_META_BLOCK_V2] -->

# Verified rendering resource envelope - source map

> **Outcome:** `KFM-TRIAD-052` and programming card `KFM-CAND-0156` are adapted into a synthetic, no-network worker-trace and resource-budget assessment. It enforces declared verify-before-decode ordering while performing none of those operations.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied/Drive `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-052`, `KFM-CAND-0154`, `KFM-CAND-0155`, and `KFM-CAND-0156` | Design lineage for chunking, proof/signer stages, resource budgets, cancellation, corruption, truncation, replay, timeout, exhaustion, and worker failure. |
| Supplied `KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual - Revised Working Edition` | Released-only assets, manifest hashes, runtime integrity, proof-in-loop performance budgets, and no forbidden paths | Supporting architecture; rendered pages were inspected, but the working edition does not become repository policy. |
| Existing renderer capability profile | Renderer declaration and accepted MapLibre adapter boundary | UI compatibility authority retained without modification. |
| Existing verifier capability portability assessment | Algorithm, canonicalization, trust, dependency, time, network, and resource-capability declarations | Verification-environment comparison retained without modification. |
| Existing PMTiles attestation standard and validator | Artifact, manifest, index, signature, and partial-read integrity semantics | Integrity authority retained without modification. |
| Directory Rules plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

At `main@169ac1946812b6452a28c38ee57bc78ee41901b8`, renderer compatibility, verifier portability, PMTiles integrity, release binding, and runtime budgets exist as separate families. No common executable candidate was found that checks a synthetic client-worker trace for verification completion before decode/render while closing chunk, queue, concurrency, fetch, decode, heap, and CPU declarations. This is **CONFIRMED for the inspected tree**, not a timeless repository claim.

## Bounded adaptation

The candidate keeps exact release/artifact/proof/signer/verifier/renderer references, expected and declared artifact digests, explicit budgets, observed synthetic usage, contiguous hash chunks, contiguous worker messages, finite fault flags, exact state derivation, deterministic identity, and fixed-false authority flags.

It deliberately excludes artifact or trust-material resolution, network access, hashing, proof parsing, cryptography, signer authentication, decoder or renderer calls, worker execution, retry, fallback selection, evidence resolution, policy decisions, review approval, release, deployment, publication, and public use.

## Why this is not a verifier or renderer

The repo already owns verifier and renderer boundaries. A new implementation here would create a parallel authority and couple the proposal to unselected runtime technology. The safe first slice is a trace-assessment candidate whose `PASS` means only declaration consistency—even when the declared rendering state is blocked, cancelled, or failed.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Bounded runtime-composition meaning | `contracts/runtime/verified_rendering_resource_envelope.md` |
| Canonical machine shape | `schemas/contracts/v1/runtime/verified_rendering_resource_envelope.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/runtime/verified_rendering_resource_envelope/cases.json` |
| Repository validator | `tools/validators/runtime/validate_verified_rendering_resource_envelope.py` |
| Executable evidence | `tests/validators/test_validate_verified_rendering_resource_envelope.py` |
| Hosted read-only orchestration | `.github/workflows/verified-rendering-resource-envelope.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No new root or parallel renderer, verifier, signer, trust, release, policy, review, receipt, proof, or publication home is created.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, all five finite states, exact fixture polarity, chunk and trace closure, fault-message binding, verify-before-decode ordering, every declared resource budget, deterministic identity, parser bounds, no-network behavior, adjacent verifier and renderer boundaries, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. No live byte, worker, decoder, renderer, network, release, or public state is created.
