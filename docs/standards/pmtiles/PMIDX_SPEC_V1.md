<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-standards-pmtiles-pmidx-spec-v1
title: PMIDX Sidecar Specification V1
type: standard
version: v1.2-draft
status: draft; PROPOSED; compatibility-profile-only
owner: TODO-pmtiles-steward-plus-schema-steward-plus-security-steward
created: 2026-05-19
updated: 2026-08-09
policy_label: internal-governance; integrity-sidecar; non-authoritative
owning_root: docs/
responsibility: documents the implemented bounded PMIDX v1 compatibility algorithm without selecting a canonical PMTiles profile or granting cryptographic, policy, release, or publication authority
truth_posture: test-or-abstain; implementation claims require current repository evidence
related:
  - PMTILES_ATTESTATION_STANDARD.md
  - ../../../tools/validators/pmtiles/verify_merkle.py
  - ../../../tools/validators/pmtiles/verify_partial_read.py
  - ../../../tools/validators/pmtiles/validate_attestation_bundle.py
  - ../../../fixtures/pmtiles/attestation/README.md
  - ../../../tests/validators/test_pmtiles_attestation_bundle.py
notes:
  - "This draft documents the split SHA-256 compatibility profile already wired by the repository. It does not resolve competing PMTiles profile proposals."
  - "STRUCTURAL_PASS is not signature validity, policy approval, release authorization, or publication eligibility."
  - "The created date is the earliest repository-history date for this path (commit 05d7f7341072eb9e7d79598c738c1c7bff7f5a49); any pre-repository authorship date remains unknown."
[/KFM_META_BLOCK_V2] -->

# PMIDX Sidecar Specification V1

`*.pmidx` is the SHA-256 compatibility sidecar already used by the repository's
split PMTiles attestation workflow. It binds ordered chunks of one PMTiles
archive to a Merkle root and carries the shared build `spec_hash`.

This draft documents the implemented compatibility profile. It does not select
it as the canonical long-term PMTiles profile, accept a proposed ADR, establish
source truth, verify a signature, approve policy, authorize release, or permit
publication.

## Required fields

| Field | Constraint |
|---|---|
| `schema_version` | Exactly `kfm.pmidx.v1`. |
| `spec_hash` | `sha256:` plus 64 hexadecimal characters. |
| `pmtiles_sha256` | SHA-256 digest of the complete PMTiles archive. |
| `merkle.arity` | Integer from 2 through 64; booleans are not integers. |
| `merkle.chunk_bytes` | Integer from 1 byte through 64 MiB. |
| `merkle.root` | Root produced by the algorithm below. |
| `merkle.leaves` | Ordered digest of every archive chunk. |
| `ranges` | Optional ordered, non-overlapping single-chunk commitments. |

The validator accepts PMIDX JSON up to 16 MiB and at most 100,000 leaves or
ranges. Those limits are an implemented validation envelope, not a claim that
every production archive fits it.

## Chunk and tree algorithm

1. Split the archive into half-open chunks
   `[i * chunk_bytes, min(file_size, (i + 1) * chunk_bytes))`.
2. Store `sha256:<hex>` of each chunk in archive order. The leaf count must equal
   `ceil(file_size / chunk_bytes)`.
3. Decode the leaf digests to 32-byte values.
4. At each level, group values in order by `arity`, concatenate the raw digest
   bytes, and SHA-256 the concatenation. The final short group is not padded or
   duplicated.
5. Continue until one digest remains. A single leaf is its own root.

The algorithm preserves current PMIDX v1 behavior. It has no domain-separation
prefix and must not be silently changed under the same profile identifier.

## Range binding

Each range object uses the existing fields `offset`, `length`, and `leaf`, with
optional `tile_id` metadata.

- Bytes are the half-open interval `[offset, offset + length)`.
- `length` must be positive and the interval must remain inside the archive.
- Ranges must be deterministically ordered and non-overlapping.
- A range must fit wholly inside one chunk.
- `leaf` must equal `offset // chunk_bytes` and identify an existing leaf.

PMIDX v1 does not claim that declared ranges cover every tile or every byte.
Coverage policy remains outside this structural validator. The Merkle root
commits archive chunk digests, not the PMIDX JSON document. A locally consistent
`ranges` entry and its optional `tile_id` can therefore be rewritten without
changing the root. PMIDX v1 range metadata is not authenticated and does not
prove tile identity.

## Verification outcome

`verify_merkle.py` returns `STRUCTURAL_PASS` only after recomputing the whole-file
digest, every chunk leaf, the Merkle root, and each declared range-to-leaf
binding. Failures return a finite non-echoing code.

`validate_attestation_bundle.py` additionally reconciles the PMIDX digest, root,
and `spec_hash` with PMTiles metadata, PMSIG, and exactly one RunReceipt subject.
Its success still carries four holds:

- `CRYPTOGRAPHIC_VERIFICATION_UNWIRED`
- `POLICY_EVALUATION_NOT_RUN`
- `RANGE_METADATA_NOT_AUTHENTICATED`
- `RELEASE_AUTHORIZATION_NOT_EVALUATED`

The repository-owned synthetic matrix is under
`fixtures/pmtiles/attestation/`; actual PMTiles bytes are generated only in a
temporary test directory.

## Captured partial-read compatibility check

`verify_partial_read.py` is an opt-in, no-network reference check for a captured
range response. It accepts the existing PMIDX and PMSIG-shaped object plus:

- the captured range bytes;
- the complete bytes of the containing PMIDX leaf;
- the observed complete archive size; and
- the exact requested offset and length.

The requested range must exactly match one declared PMIDX range. The verifier
checks archive-size-to-leaf-count coherence, every declared range boundary, the
supplied leaf length and SHA-256 digest, the captured bytes as the exact slice
of that leaf, the declared Merkle root, and the PMSIG subject's archive digest,
root, and `spec_hash` bindings.

Success is `STRUCTURAL_HOLD`, not `STRUCTURAL_PASS`. The full archive digest is
not recomputed; PMSIG is not cryptographically verified; the PMIDX range table
is not committed by the tree; and Bao/BLAKE3 outboard proofs are not adopted.
The check therefore cannot declare a render artifact healthy or authorize
policy, release, publication, or public use.

## Unresolved profile decision

Repository evidence currently describes more than one PMTiles attestation
shape: a monolithic BLAKE3 sidecar, this split SHA-256 compatibility bundle, and
a proposed GeoManifest/DSSE route. This edit does not collapse those profiles or
declare one canonical. A governed profile decision and migration plan remain
required before changing digest families, filenames, schema authority, or
publication gates.
