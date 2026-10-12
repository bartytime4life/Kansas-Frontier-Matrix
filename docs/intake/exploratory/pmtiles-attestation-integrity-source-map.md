<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-intake-exploratory-pmtiles-attestation-integrity-source-map
title: PMTiles Attestation Integrity Idea Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED; non-authoritative
owner: TODO-intake-steward-plus-pmtiles-steward-plus-evidence-steward
created: 2026-08-02
updated: 2026-08-02
policy_label: internal-governance; exploratory-intake; no-public-path
owning_root: docs/
responsibility: maps attached PMTiles ideas to bounded repository-grounded implementation, deferral, and uncertainty without treating the source as accepted architecture or ecosystem proof
truth_posture: cite-or-abstain; source proposals remain proposals
related:
  - ../../standards/pmtiles/PMIDX_SPEC_V1.md
  - ../../../tools/validators/pmtiles/README.md
  - ../../../fixtures/pmtiles/attestation/README.md
notes:
  - "The attached source is used as a proposal input only. Current ecosystem and product claims were not promoted to repository truth by this work."
  - "This map grants no dependency admission, signature trust, policy approval, release authority, or publication authority."
[/KFM_META_BLOCK_V2] -->

# PMTiles attestation integrity idea source map

This source map records how the PMTiles ideas in `New Ideas 5-10-26.pdf` were
assayed against repository evidence at
`main@5ce95ca390e766945f587d694be046c070b11fc1`.

Input binding: `sha256:cee602df9dee8a7baf3c94c25431a706c6eb683977a175b83273a78277bbe201`.
The attached source bytes are not added to the repository by this change.

The attached paper is treated as a **PROPOSED idea source**, not as proof of
current ecosystem facts, accepted architecture, dependency admission, signer
trust, policy closure, or release readiness.

The exact 127-byte header layout, movable-section boundary, 16 KiB root-directory
limit, compression and tile-type enums, zero-as-unknown counters, metadata
object requirement, and directory encoding were checked against the upstream
[`PMTiles Version 3 Specification`](https://github.com/protomaps/PMTiles/blob/8b8ddea4dbff1b0104cf2bebf2f7ff35c91b41d5/spec/v3/spec.md)
on 2026-08-02. That format reference does not validate KFM-specific
attestation, governance, or publication claims.

## Evidence-to-change map

| Source idea | Source location | Repository-grounded treatment |
|---|---|---|
| Bind PMTiles bytes to a compact integrity sidecar and shared `spec_hash`. | `New Ideas 5-10-26.pdf`, pp. 2–3 | **ADAPTED.** The repo already wires a split PMIDX/PMSIG/RunReceipt profile. This change binds PMIDX leaves to actual archive chunks and reconciles the shared digest, root, and `spec_hash` across that existing bundle. |
| Let a client or validator check byte ranges against archive commitments. | pp. 2–4 | **PARTIALLY ADAPTED FOR OFFLINE VALIDATION.** Declared PMIDX ranges are bounds-checked and tied to archive-derived chunks. The root does not commit the PMIDX range table or `tile_id`, so range metadata and tile identity remain unauthenticated; client-side Bao proofs are not claimed. |
| Add deterministic validator gates, valid/invalid fixtures, and CI. | pp. 5, 7, 11, 14 | **IMPLEMENTED AS A BOUNDED COMPATIBILITY GATE.** Synthetic mutation descriptors drive no-network unit tests and CI. Failures use finite non-echoing reason codes. |
| Fail publication when signature or governed prerequisites are missing. | pp. 5 and 14 | **PRESERVED AS HOLD/DENY.** Structural success never becomes publication approval; the existing workflow still deliberately denies candidate bundles after shape-only signature inspection. |
| Add BLAKE3, Bao outboard proofs, DSSE/cosign signing, delta bundles, and client streaming verification. | pp. 2–5 and 16 | **DEFERRED / NEEDS VERIFICATION.** Those dependencies, proof formats, trusted keys, signer registry, delta semantics, and canonical profile are not established by this slice. |

## Why this is a compatibility slice

Current repository surfaces conflict:

| Surface | Observed posture at the pinned base |
|---|---|
| `docs/standards/PMTILES.md` | Draft monolithic sidecar profile using BLAKE3. |
| `docs/standards/pmtiles/PMIDX_SPEC_V1.md` plus current tools/workflow | Split PMTiles + PMIDX + PMSIG + RunReceipt profile using SHA-256. |
| `docs/adr/ADR-0023-geo-manifest-signs-every-pmtiles-cog-release.md` | Proposed GeoManifest plus DSSE direction; not an accepted migration authority. |

The lowest-risk reversible move is therefore to make the already-executed split
profile internally consistent and testable. Selecting a canonical profile would
change dependency, schema, filename, policy, and migration decisions and is not
smuggled into this implementation.

## Confirmed implementation boundary

The focused offline suite confirms:

- exact PMTiles v3 header-field decoding and bounded metadata parsing;
- complete archive digest and chunk-leaf recomputation;
- current PMIDX Merkle and range binding semantics;
- PMSIG and RunReceipt shape plus digest/root/`spec_hash` reconciliation;
- duplicate-key, nonfinite-number, size, symlink, and non-echo failure posture;
- compatibility with the current development PMSIG and RunReceipt producers.

It does not confirm source correctness, complete tile-directory semantics,
authenticated range metadata or tile identity, cryptographic signature validity,
key trust, Rego outcomes, rights/sensitivity
closure, release state, rollback readiness, deployment, or publication.
