# IIIF Historic Overlay Readiness Assessment

Status: `PROPOSED_INACTIVE`  
Authority: fixture-only metadata and integrity preflight. It is not an evidence, policy, promotion, release, or publication authority.

## Purpose

`IIIFHistoricOverlayReadinessAssessment` turns the bounded, repository-owned checklist in
`docs/standards/IIIF.md` into deterministic no-network validation for historic-map overlays.

The profile preserves the anti-collapse boundary between:

1. upstream IIIF identity and as-delivered response bytes;
2. georeference annotation evidence and its exact byte digest;
3. interpretive warp metadata such as GCPs, mask, transform, and uncertainty;
4. upstream rights statements and KFM rights/CARE review state;
5. browser rendering plugins; and
6. release/public-use authority.

A visually successful warp is never evidence that the overlay is accurate, rights-cleared, or released.

## Finite outcomes

- `READY`: the declared fixture metadata is eligible for a later evidence-, policy-, and runtime-aware gate.
- `HOLD`: the declaration is coherent but an expected prerequisite is unresolved.
- `DENY`: the declaration contains an explicit public-safety, rights/CARE, or trust-membrane violation.
- `ERROR`: the candidate is malformed or a declared integrity binding is internally inconsistent.

Precedence is `ERROR > DENY > HOLD > READY`.

## Readiness rules

A `READY` candidate must:

- record the served IIIF Image and Presentation API versions;
- retain the upstream manifest/info identities and exact captured-byte digests;
- preserve capture metadata and as-delivered bytes;
- bind the exact Georeference Annotation bytes by SHA-256;
- contain a non-empty GCP set and closed resource mask;
- record the transform method and overlay uncertainty;
- carry upstream rights state into an explicit KFM rights state;
- have CARE review complete when applicable;
- use only an allowlisted, version-pinned browser warp plugin;
- expose no RAW/WORK path and allow no unreleased browser fetch;
- resolve to an EvidenceBundle reference; and
- name a rollback target.

Legacy IIIF 2.1.1 input may be admitted only when an explicit downstream normalization reference is present.
Presentation API `4.0-preview` is monitoring-only and therefore remains `HOLD`.

## Integrity boundary

For fixture-only validation, `annotation_payload_utf8` represents the exact captured annotation byte
sequence. `annotation_digest` is recomputed as SHA-256 over those UTF-8 bytes. The validator does not
claim JSON-LD canonicalization or remote-resource equivalence.

## Non-effects

A passing assessment does not:

- fetch or validate a live IIIF service;
- authenticate a SourceDescriptor, rights statement, EvidenceBundle, policy result, consent grant, or reviewer;
- georeference or warp an image;
- calculate transform RMS error;
- validate a remote JSON-LD context;
- activate Allmaps or any other browser plugin;
- expose a source or create a public route;
- authorize promotion, release, deployment, publication, or public use.

All governance booleans are fixed false and `release_ref` is fixed null.
