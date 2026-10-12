<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-intake-exploratory-tile-artifact-manifest-pmtiles-profile-source-map
title: TileArtifactManifest PMTiles Compatibility Profile Idea Source Map
type: exploratory-source-map
version: v0.1.0
status: draft; PROPOSED; non-authoritative
owner: TODO-intake-steward
created: 2026-08-03
updated: 2026-08-03
policy_label: internal-governance; exploratory-intake; no-public-path
owning_root: docs/
responsibility: maps attached declared-manifest and PMTiles ideas to bounded repository-grounded implementation, deferral, rejection, and uncertainty without selecting canonical schema, cryptographic, policy, release, or publication authority
truth_posture: cite-or-abstain; source proposals remain proposals
related:
  - ../../standards/PMTILES.md
  - ../../standards/pmtiles/PMTILES_ATTESTATION_STANDARD.md
  - ../../../contracts/release/tile_artifact_manifest.md
  - ../../../tools/validators/pmtiles/validate_attestation_bundle.py
  - ../../../fixtures/pmtiles/attestation/README.md
  - ../NEW_IDEAS_INDEX.md
  - ../new-ideas-register.md
notes:
  - "This source map has one intake-steward authority-owner role; assignment NEEDS VERIFICATION. PMTiles, contracts, schema, validation, security, policy, and release stewards are review roles. CODEOWNERS routes review to @bartytime4life."
  - "The attached sources are proposal inputs only and are not copied into the repository by this change."
  - "This map grants no schema-family decision, dependency admission, signature trust, policy approval, release authority, or publication authority."
[/KFM_META_BLOCK_V2] -->

# TileArtifactManifest PMTiles compatibility profile idea source map

This source map records how the PMTiles/declared-manifest subset on pp. 154–157
of `New Ideas 5-15-26.pdf` was assayed against repository evidence for the
fixture-wired, offline, opt-in local
`kfm.pmtiles.tile-artifact-manifest.compat.v1` upgrade. It is a partial packet
triage, not an inventory or disposition of the full source packet.

## Input bindings

| Input | Binding | Treatment |
|---|---|---|
| `New Ideas 5-15-26.pdf` | `sha256:64dc1c8793ba64a641b12a092201d1cc4e5ac90ce8cdc4a1d7bd54eaf548cc95`; pp. 154–157 | PROPOSED source for the small sidecar, size/SHA-256/`spec_hash`, generator/input declarations, fixed-name, remote-change, receipt, Bao, and DSSE ideas; bytes remain outside the repository. |
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md` | `sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`; lines 1477–1481 and 1565 | PROPOSED synthesis source for PMTiles-attestation placement, fixture-first, fail-closed, and no-network guidance only. |
| [`PMTiles Version 3 Specification`](https://github.com/protomaps/PMTiles/blob/8b8ddea4dbff1b0104cf2bebf2f7ff35c91b41d5/spec/v3/spec.md) | pinned upstream format authority | Supports v3 header, media type, enum, zoom/bounds encoding, compression, and embedded MVT metadata facts; it does not authorize KFM governance or publication claims. |
| [`TileJSON 3.0.0`](https://github.com/mapbox/tilejson-spec/blob/1092200890cae99dd8183f19029568498112c9cd/3.0.0/README.md) | pinned upstream metadata authority | Supports `scheme` defaulting, `vector_layers` id/field-map shape, and general bounds semantics; the stricter KFM bounds envelope is a local narrowing. |

## Evidence-to-change map

| Idea or format fact | Repository-grounded treatment |
|---|---|
| Keep a small deterministic descriptor with archive name/path, byte size, SHA-256, `spec_hash`, generator, and inputs. | **ADAPTED.** The opt-in descriptor uses digest-bound artifact-ref syntax, exact byte size, non-zero syntactically valid SHA-256, `spec_hash`, `tool@version` syntax, and nonempty versioned source-ref syntax. Locator resolution and provenance binding remain holds. |
| Upstream PMTiles/TileJSON facts plus KFM-local narrowing: version, media type, tile format, scheme, zooms, bounds, and vector-layer metadata. This is not attributed to the attached idea packets. | **ADAPTED NARROWLY.** The first compatibility profile is PMTiles v3 + MVT + XYZ only. Archive-bound fields reconcile with local header/metadata evidence; MIME is a profile literal. Raster and MLT profiles remain out of scope. |
| Add deterministic negative fixtures and no-network validation before live activation. | **IMPLEMENTED.** One positive descriptor and an exact reason-code-registered one-fault negative matrix generate all PMTiles and companion bytes in temporary test directories. Parser and metadata-compression boundaries have dedicated tests. |
| Compute a normalized sidecar hash and use fixed production filenames. | **PARTIALLY ADAPTED / HOLD.** The existing bundle `spec_hash` is reconciled, but this slice does not define JCS canonicalization or a production companion-name convention. The descriptor path is always supplied explicitly. |
| Use remote HEAD/ETag/Last-Modified checks to decide whether to emit artifacts. | **REJECTED FOR THIS SLICE.** Network access, remote change detection, cache/CDN behavior, and artifact emission are outside the offline local trust boundary. |
| Add Bao/BLAKE3, DSSE/cosign, Rekor, trusted keys, and streaming range verification. | **DEFERRED / NEEDS GOVERNED DECISION.** Dependencies, proof formats, signer trust, and the range-metadata authentication profile are unresolved. Existing structural holds remain. |
| Emit a release, attestation, or run receipt after validation. | **REJECTED FOR THIS SLICE.** The validator emits only bounded status JSON with `authority: NONE`; it writes no repository or lifecycle artifact. |
| Establish the canonical `TileArtifactManifest` schema shape and home. | **HOLD / NOT DECIDED.** A permissive map-family placeholder coexists with a release contract that proposes another family. Directory governance requires a separate accepted decision before either can become canonical. |

## Why the profile is opt-in and non-canonical

The repository already has a tested PMTiles v3 header, PMIDX, PMSIG-shape, and
RunReceipt-shape reconciliation lane. Extending that validator reuses the
existing responsibility boundary and CI path without creating a second
manifest authority. The new flag does not auto-discover a filename and does not
change default no-flag output. Supplying the flag adds the manifest check and
its explicit holds to the result.

A successful declared-manifest check is `STRUCTURAL_PASS` with
`authority: NONE`. It adds
`TILE_ARTIFACT_MANIFEST_SCHEMA_AUTHORITY_UNRESOLVED`,
`TILE_MANIFEST_DECLARED_PROVENANCE_UNATTESTED`, and
`TILE_MANIFEST_ARTIFACT_REF_REGISTRY_UNRESOLVED`, and retains the existing
cryptographic, unauthenticated-range-metadata, policy, and release holds.

## Field-to-evidence boundary

| Declared field | What this profile actually checks | Remaining hold |
|---|---|---|
| `artifact_name` | Exact local archive basename. | No publication/storage resolution. |
| `artifact_ref` | ASCII ref syntax, SHA-256 suffix, and suffix equality with the declared digest. | Artifact registry is not resolved; locator immutability is not proven. |
| `media_type` | Exact profile literal `application/vnd.pmtiles`. | No archive field carries MIME. |
| `digest`, `byte_size` | Equality with PMIDX whole-file SHA-256 and inspected archive size. | No release identity or promotion. |
| `spec_hash` | Equality with PMTiles metadata and the reconciled companion bundle. | Build specification is not recomputed here. |
| `source_manifest_refs` | Nonempty, unique, ASCII, versioned `kfm://`/`urn:` syntax. | Refs are not resolved or attestation-bound. |
| `generation_tool` | Bounded `tool@version` identifier syntax. | Generator identity and execution are not attested. |
| version, tile format, zoom, bounds | Header equality; bounds use WGS 84 coordinates and KFM's strict `-180 <= west < east <= 180`, `-85.051129 <= south < north <= 85.051129` envelope. | Degenerate TileJSON bounds are intentionally denied; runtime/client compatibility and public-safe coverage are not evaluated. |
| tiling scheme | `xyz`, matching embedded TileJSON `scheme` or its `xyz` default. | No runtime tile-directory traversal. |
| vector layers | Order-independent equality of unique id/field maps with embedded TileJSON metadata. | Field semantics and tile payload contents are not inspected. |

The archive reader in this compatibility lane supports uncompressed and gzip
metadata. Upstream v3 Brotli and Zstandard metadata fail closed and remain a
future compatibility decision.

## Confirmed implementation boundary

The focused offline suite confirms:

- bounded, duplicate-key- and nonfinite-safe descriptor parsing;
- digest-bound artifact-ref syntax and embedded-payload denial;
- archive name, SHA-256, byte-size, and build-`spec_hash` reconciliation;
- PMTiles v3, MVT, XYZ, ordered zoom, and WGS84/WebMercator bounds checks;
- archive-header agreement plus embedded scheme and vector-layer id/field-map agreement;
- nonempty unique versioned source-ref syntax and generator-identifier syntax;
- default bundle behavior remains unchanged when the flag is absent.

It does not confirm canonical schema conformance, source correctness, complete
tile-directory semantics, public-safe geometry, authenticated range metadata,
cryptographic signature validity, key trust, policy outcomes, rights or
sensitivity closure, release state, rollback readiness, runtime loading,
deployment, or publication.
