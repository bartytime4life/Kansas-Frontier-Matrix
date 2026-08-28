<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-pmtiles-partial-read-source-map
title: Pass 32 PMTiles Partial-Read Verification Source Map
type: exploratory-source-map
version: v0.1
status: draft; triaged; bounded-slice-implemented-in-pr
owners: OWNER_TBD — Intake steward · PMTiles steward · Security steward · Release steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-adaptation; no-authority
related:
  - ../new-ideas-register.md
  - ../../../tools/validators/pmtiles/verify_partial_read.py
  - ../../../tools/validators/pmtiles/verify_merkle.py
  - ../../../docs/standards/pmtiles/PMIDX_SPEC_V1.md
  - ../../../fixtures/pmtiles/attestation/partial-read/README.md
tags: [kfm, pass-32, pmtiles, partial-read, range, merkle, bao, intake, source-map]
notes:
  - "Records a bounded repository adaptation of KFM-P32-PROG-0015 without adopting Bao/BLAKE3 or upgrading the existing split bundle to canonical authority."
  - "The Pass 32 atlas and upstream idea document remain evidence carriers, not implementation, policy, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pass 32 PMTiles Partial-Read Verification Source Map

## Source candidate

| Field | Value |
|---|---|
| Atlas | `KFM_Pass_32_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Stable card | `KFM-P32-PROG-0015` |
| Card title | Bao partial-read verifier |
| Pass 32 status | `NEW` / active / `PROPOSED` |
| Source IDs | `SRC-P32-001` (`New Ideas`) |
| Atlas `spec_hash` | `sha256:d8845c8309d3cac282af0a124bdbe1d7c246d5acefeb012dcc72aa1c414bb5a7` |
| Normalized statement | A verification step should validate partial reads or range-fetched PMTiles content against a signed sidecar before considering render artifacts healthy. |
| Retrieved evidence | Google Drive document `New Ideas` and the Pass 32 atlas, inspected 2026-08-09 |

## Repository reconciliation

**CONFIRMED at base `main@76da0a048590710bd927891d43075d989568bf7d`:**

- `verify_merkle.py` recomputes the complete archive digest, every SHA-256
  chunk leaf, the PMIDX root, and declared single-chunk range boundaries, but
  requires the complete PMTiles archive.
- `validate_attestation_bundle.py` binds the archive, PMIDX, PMSIG subject shape,
  and RunReceipt while retaining cryptographic, unauthenticated-range-metadata,
  policy, and release holds.
- `PMIDX_SPEC_V1.md` states that the existing root commits chunk digests, not the
  `ranges` table or optional `tile_id`; range identity is therefore not
  authenticated by current PMIDX v1.
- the hash-profile readiness matrix records BLAKE3/Bao as readiness-only rather
  than an adopted digest or proof authority;
- PR #1941 added an opt-in declared PMTiles manifest compatibility profile, and
  PR #2274 addressed release-scoped cache decisions including a partial-download
  state. Neither implements captured range-byte verification.
- ADR-0029 is accepted and routes durable validator logic to `tools/`, reusable
  synthetic descriptors to `fixtures/`, enforceability evidence to `tests/`,
  standards to `docs/standards/`, intake adaptation to `docs/intake/`, and
  authoring provenance to `data/receipts/generated/`.

## Bounded adaptation

This change adds `kfm.pmtiles.partial-read.compat.v1`, a deterministic
no-network reference verifier over an explicitly supplied:

1. PMIDX sidecar;
2. PMSIG-shaped companion;
3. captured range response;
4. complete containing-leaf payload;
5. observed complete archive size; and
6. requested offset and length.

The verifier requires the request to match one declared PMIDX range, validates
all current PMIDX range boundaries, binds the captured bytes to the containing
leaf slice, verifies the leaf SHA-256 digest and tree root, and reconciles the
root, archive digest, and `spec_hash` with the PMSIG subject shape.

The positive outcome is deliberately `STRUCTURAL_HOLD` with `authority: NONE`.
It must not be interpreted as a healthy render artifact.

## Idea treatment

| Source pressure | Treatment | Reason |
|---|---|---|
| Verify partial/range-fetched PMTiles bytes | **PARTIALLY IMPLEMENTED** | Exact captured bytes are checked against a supplied committed leaf without rereading the archive. |
| Validate against a signed sidecar | **SHAPE-BOUND / HELD** | PMSIG subject fields are reconciled, but cryptographic verification and approved key trust remain unwired. |
| Use Bao/BLAKE3 outboard proofs | **DEFERRED** | Repository readiness evidence does not adopt this digest/proof profile; silently replacing the existing SHA-256 compatibility lane would create a competing authority. |
| Declare render artifact healthy | **DENIED IN THIS SLICE** | Range metadata, crypto, whole-archive digest, policy, and release remain unresolved. |
| Live HTTP Range client or MapLibre runtime integration | **DEFERRED** | This PR is fixture-only and no-network. |

## Directory Rules basis

| Responsibility | Repository home |
|---|---|
| Durable compatibility verifier | `tools/validators/pmtiles/verify_partial_read.py` |
| Synthetic descriptor matrix | `fixtures/pmtiles/attestation/partial-read/` |
| Enforceability proof | `tests/validators/test_pmtiles_attestation_bundle.py` |
| Implemented compatibility documentation | `docs/standards/pmtiles/PMIDX_SPEC_V1.md` and PMTiles validator README |
| Source adaptation record | this file |
| AI authoring provenance | `data/receipts/generated/genrec-pass32-pmtiles-partial-read-20260809.json` |
| Hosted orchestration | existing `.github/workflows/pmtiles-attestation.yml` |

No new root or parallel schema, hash-profile, signature, key, policy, receipt,
proof, release, publication, or health authority is created.

## Validation and non-effects

The focused suite covers one positive structural hold plus exact denials for
range-byte mismatch, leaf-digest mismatch, undeclared range, PMSIG-root
mismatch, cross-chunk range declarations, symlinked payloads, and invalid
integer bounds. It also exercises the CLI JSON surface and patches common
Python network entry points during direct verification.

The change performs no network request, Range fetch, archive generation outside
temporary tests, signing, key lookup, source activation, policy evaluation,
release decision, lifecycle mutation, cache write, deployment, publication, or
public-map update.

## Deferred dependencies

A later operational implementation would require separately governed decisions
for:

- the canonical digest and range-proof profile, including any Bao/BLAKE3
  adoption and migration from PMIDX v1;
- authentication of range/tile metadata itself;
- cryptographic PMSIG verification and approved key/revocation registry;
- trusted archive-size and HTTP response metadata capture;
- a live range-fetch client with SSRF, redirect, timeout, retry, and size
  controls;
- MapLibre render-health integration;
- policy, rights, sensitivity, release, correction, rollback, and withdrawal
  closure; and
- operational receipts, observability, incident handling, and scale tests.

## Rollback

Before merge, close the draft pull request and remove its review branch. After
an authorized merge, revert the additive commit and rerun the focused PMTiles
workflow. No live source, archive, cache, map layer, lifecycle record, release,
deployment, or public artifact requires restoration.

<p align="right"><a href="#top">Back to top</a></p>
