<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-tile-artifact-manifest
title: contracts/release/tile_artifact_manifest.md — TileArtifactManifest Contract
type: contract
version: v0.2
status: draft; PROPOSED; map-asset-family; schema-missing; release-artifact-pointer
owners: OWNER_TBD — Release steward · Tile steward · Map/UI steward · Layer steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Rollback steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; tile-artifact-manifest; pmtiles; cog; tile-archive; map-publication; artifact-digest; release-gated; no-artifact-store; no-runtime-authority
tags: [kfm, contracts, release, tile-artifact-manifest, tile-artifact, pmtiles, cog, vector-tiles, raster-tiles, tilejson, digest, release-manifest, map-release-manifest, evidence-ref, rights, sensitivity, rollback]
related:
  - ./README.md
  - ./release_manifest.md
  - ./map_release_manifest.md
  - ./layer_manifest.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../../schemas/contracts/v1/release/tile_artifact_manifest.schema.json
  - ../../policy/release/
  - ../../policy/data/
  - ../../policy/sensitivity/
  - ../../release/
  - ../../data/registry/layers/
  - ../../data/proofs/
  - ../../data/receipts/
  - ../../docs/architecture/release-discipline.md
  - ../../docs/standards/RELEASE_MANIFEST.md
notes:
  - "Expanded from a scaffold created from a domain-document inventory reference."
  - "No `schemas/contracts/v1/release/tile_artifact_manifest.schema.json` was verified in this session; schema behavior remains UNKNOWN / NEEDS VERIFICATION."
  - "`docs/standards/RELEASE_MANIFEST.md` names the map-asset family, including `TileArtifactManifest`, as belonging in its own contracts/schemas homes, not in the standards document."
  - "TileArtifactManifest is an artifact metadata/digest manifest. It must not store PMTiles, COGs, vector tiles, raster tiles, sprites, glyphs, style JSON, proof packs, receipts, public API payloads, UI state, or AI output."
  - "Rollback target for this expansion is previous scaffold blob SHA `30bab07c0746f7c1fe0eef0ef7ae19ae3476fbb0`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# TileArtifactManifest Contract

> `TileArtifactManifest` describes a released or candidate tile artifact by reference, digest, format, coverage, provenance, rights, sensitivity, policy posture, and rollback/correction linkage. It is a manifest for tile artifacts, not the tile artifact itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: TileArtifactManifest" src="https://img.shields.io/badge/object-TileArtifactManifest-0a7ea4">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-missing-red">
  <img alt="Artifacts: referenced only" src="https://img.shields.io/badge/artifacts-referenced__only-lightgrey">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
</p>

**Status:** draft / PROPOSED / schema missing  
**Path:** `contracts/release/tile_artifact_manifest.md`  
**Release manifest companion:** [`./release_manifest.md`](./release_manifest.md)  
**Map release companion:** [`./map_release_manifest.md`](./map_release_manifest.md)  
**Layer release companion:** [`./layer_manifest.md`](./layer_manifest.md)  
**Expected schema path:** `schemas/contracts/v1/release/tile_artifact_manifest.schema.json` — NEEDS VERIFICATION; not found in this session  
**Policy authority:** `policy/release/`, `policy/data/`, `policy/sensitivity/`, rights/access policy roots, not this contract  
**Release artifact authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED target scaffold replaced · CONFIRMED no paired release schema found in this session · CONFIRMED release standards place map-asset family object meaning in contracts/schemas, not the standards doc · PROPOSED fields until schema/fixtures/validator/policy/release integration are implemented

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Boundary with release and map manifests](#boundary-with-release-and-map-manifests) · [Artifact semantics](#artifact-semantics) · [Proposed fields](#proposed-fields) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Exclusions](#exclusions) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`TileArtifactManifest` is the semantic object for a tile artifact that is being evaluated, released, corrected, superseded, withdrawn, or rolled back.

It answers:

- which tile artifact exists;
- which format and artifact class it uses;
- where the artifact is stored or published, by governed ref only;
- which digest or content-addressed identifier verifies it;
- which layer, map release, release manifest, and artifact set reference it;
- what bounds, zoom range, tile matrix, time window, and freshness state apply;
- which evidence, rights, sensitivity, policy, review, validation, and attestation records support it;
- how correction, supersession, withdrawal, cache invalidation, or rollback is handled.

It does not answer:

- what the tile bytes are;
- whether publication is allowed by itself;
- whether a public client may bypass governed map APIs;
- whether the tile artifact is evidence truth;
- whether a release has completed;
- whether a rollback has executed.

---

## Meaning

A `TileArtifactManifest` is artifact metadata plus trust-spine context for tile-oriented map assets.

It may describe artifacts such as:

- PMTiles archives;
- vector tile archives;
- raster tile archives;
- COG-derived tile artifacts;
- TileJSON documents;
- tile sidecars;
- derived sprites/glyphs only if the release decides to treat them as tile-adjacent artifacts;
- other map tile packages accepted by future ADR/release policy.

The manifest should be digest-bound and release-aware. It should support downstream verification without embedding the payload.

---

## Repo fit

| Responsibility | Correct home | Relationship to this contract |
|---|---|---|
| Tile artifact semantic meaning | `contracts/release/tile_artifact_manifest.md` | This contract; PROPOSED. |
| General release binding | `contracts/release/release_manifest.md` | Release package parent. |
| Map release binding | `contracts/release/map_release_manifest.md` | Map-publication envelope that may reference tile artifacts. |
| Layer release bridge | `contracts/release/layer_manifest.md` | Layer-in-release relationship companion. |
| Canonical layer meaning | `contracts/data/layer_manifest.md` | Layer trust-spine authority. |
| Machine schema | `schemas/contracts/v1/release/tile_artifact_manifest.schema.json` | Expected but not verified. |
| Release policy | `policy/release/` | Admissibility / gate authority. |
| Sensitivity/rights policy | `policy/sensitivity/`, rights/access policy roots | Public-safe map exposure decisions. |
| Release artifacts | `release/` or accepted artifact roots | Tile payloads and release records; not this contract. |
| Proofs and receipts | `data/proofs/`, `data/receipts/` or accepted homes | Auditable trust artifacts. |
| Public map/runtime | governed API/UI/map roots | Downstream consumers only. |

---

## Boundary with release and map manifests

| Question | ReleaseManifest | MapReleaseManifest | TileArtifactManifest |
|---|---|---|---|
| What release exists? | In scope. | References/generalizes for map release. | References parent release. |
| Which map surface is published? | May list as release contents. | In scope. | References map/layer context. |
| Which exact tile artifact exists? | May list by ref/digest. | May list by ref/digest. | In scope. |
| What tile format, bounds, zoom range, and digest apply? | Usually summarized. | Usually summarized. | In scope. |
| Does this store tiles? | No. | No. | No. |
| Does this approve publication? | No, not alone. | No, not alone. | No, not alone. |

---

## Artifact semantics

A tile artifact manifest SHOULD preserve:

- artifact identity;
- artifact class and format;
- digest and byte-size/integrity posture;
- storage/publication refs without embedding payloads;
- tile matrix set, coordinate reference system, bounds, min/max zoom, and time coverage where applicable;
- layer and source lineage;
- evidence refs for map-visible claims;
- rights, attribution, terms, embargo, and export constraints;
- sensitivity and redaction/generalization posture;
- validation, build, signing, and provenance attestations;
- release state and rollback target;
- correction, withdrawal, supersession, and invalidation lineage.

---

## Proposed fields

No paired schema was verified in this session. These fields are therefore PROPOSED semantic targets only:

| Field | Meaning | Required posture |
|---|---|---|
| `tile_artifact_manifest_id` | Stable id for the tile artifact manifest. | Deterministic where practical. |
| `artifact_ref` | Governed ref/URI/path to tile artifact. | Must not embed payload. |
| `artifact_kind` | PMTiles, vector_tiles, raster_tiles, cog, tilejson, sidecar, sprite, glyph, other accepted kind. | Finite enum recommended. |
| `media_type` | MIME/media type. | Required for clients/build validation. |
| `digest` | Content digest such as sha256. | Required for release integrity. |
| `byte_size` | Artifact size. | Recommended for integrity checks. |
| `tile_matrix_set` | Tile matrix / tiling profile. | Required for map compatibility where applicable. |
| `crs` | Coordinate reference system. | Required where not implied by format/profile. |
| `bounds` | Public-safe spatial bounds. | Must be generalized if sensitive. |
| `min_zoom` / `max_zoom` | Zoom coverage. | Required for tiled artifacts. |
| `time_window_ref` | Valid/effective/observed time window. | Required when time-aware layer. |
| `layer_manifest_refs` | Layer manifests that use the artifact. | Must resolve. |
| `map_release_manifest_ref` | Map release envelope referencing artifact. | Must resolve for PUBLISHED map use. |
| `release_manifest_ref` | Parent release manifest. | Must resolve for PUBLISHED release use. |
| `evidence_refs` | Evidence refs supporting map-visible claims. | Must resolve where claims depend on evidence. |
| `rights_refs` | Rights/license/terms/attribution refs. | Unknown rights fail closed. |
| `sensitivity_refs` | Sensitivity labels/redaction/generalization refs. | Exact sensitive values must not leak. |
| `policy_decision_refs` | Release/render/access/export policy decisions. | Required for governed exposure. |
| `attestation_refs` | Build/signing/provenance/validation attestations. | Digest-bound and auditable. |
| `rollback_target_ref` | Prior safe artifact/release ref. | Required unless explicitly waived. |
| `correction_lineage_refs` | Corrections/supersessions/withdrawals/invalidation refs. | Must preserve public audit trail. |
| `release_state` | candidate, held, published, superseded, withdrawn, rolled_back, stale. | Finite state recommended. |

---

## Invariants

PROPOSED semantic invariants:

- A tile artifact manifest must reference tile payloads by ref/digest only; it must not store payloads.
- A published tile artifact must resolve to a ReleaseManifest or MapReleaseManifest context.
- Tile artifacts that expose sensitive locations, living-person joins, archaeology, protected species, infrastructure risk, or rights-uncertain data must be generalized, restricted, withheld, or quarantined by policy.
- Digest and artifact identity must be stable enough for cache invalidation, rollback, and audit.
- A tile artifact manifest must not replace LayerManifest, MapReleaseManifest, ReleaseManifest, PolicyDecision, EvidenceBundle, or attestation records.
- Public clients must bind through governed APIs/released manifests, not raw/latest/internal artifact paths.
- Supersession, withdrawal, rollback, and invalidation must be explicit and auditable.

---

## Lifecycle role

`TileArtifactManifest` participates in release-facing map artifact governance:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Lifecycle point | Role |
|---|---|
| PROCESSED | Candidate tile artifact may be built and validated. |
| CATALOG/TRIPLET | Candidate artifact can be cataloged and linked to layer/release candidates. |
| PUBLISHED | Artifact is referenced by ReleaseManifest/MapReleaseManifest and becomes eligible for governed public/restricted serving. |
| PUBLISHED correction | Superseding artifact and invalidation list are recorded. |
| PUBLISHED rollback | Prior safe artifact/release target is restored or referenced. |
| Withdrawn | Artifact remains auditable but is no longer served through public/restricted release surfaces. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| PMTiles, COGs, vector/raster tile payloads | `release/`, lifecycle artifact roots, or accepted artifact stores | Contracts do not store payloads. |
| JSON Schema | `schemas/contracts/v1/release/` or accepted schema home | Schemas own machine shape. |
| Release JSON instances | `release/` | Contracts do not store release records. |
| Proofs, receipts, signatures, DSSE/SLSA/in-toto attestations | `data/proofs/`, `data/receipts/`, signing/release roots | Trust artifacts remain separately auditable. |
| Rego/OPA/equivalent policy rules | `policy/release/`, `policy/data/`, sensitivity/rights roots | Policy owns admissibility. |
| Map runtime/UI/API code | `apps/`, `ui/`, `web/`, packages | Public/render surfaces are downstream. |
| AI-generated map summaries | Governed AI envelopes with evidence/policy/release checks | AI is interpretive, not release authority. |

---

## Validation expectations

NEEDS VERIFICATION before treating this contract as implementation-backed:

- accepted object name and canonical home for `TileArtifactManifest`;
- paired schema creation or compatibility decision;
- fixture home and minimum fixtures for PMTiles, COG, vector tile, raster tile, TileJSON, sensitive generalized artifact, rights-denied artifact, missing digest, missing rollback target, corrected artifact, withdrawn artifact, and rollback artifact;
- validator path and CI wiring;
- policy rules for tile release, render, access, sensitivity, rights, export, and AI interaction;
- proof/receipt binding to artifact digests and ReleaseManifest;
- public API/UI/map tests proving no pre-PUBLISHED or sensitive tile leakage.

---

## Open questions

- Should the paired schema live under `schemas/contracts/v1/release/`, `schemas/contracts/v1/map/`, or `schemas/contracts/v1/layers/`?
- Should PMTiles, COG, TileJSON, sprites, and glyphs use one `TileArtifactManifest` or separate contracts?
- Which tile formats and media types are allowed for public release?
- Which fields are mandatory for CDN/cache invalidation and rollback?
- Should tile artifacts be signed individually or only through `ReleaseManifest`/`MapReleaseManifest`?

---

## Rollback

Rollback is required if this file is used to store tile payloads, publish tiles, bypass ReleaseManifest/MapReleaseManifest, bypass schema/policy/review/evidence/release gates, expose sensitive exact locations, hide correction lineage, or authorize public map/UI/AI exposure directly.

Rollback target for this expansion: previous scaffold blob SHA `30bab07c0746f7c1fe0eef0ef7ae19ae3476fbb0`.

<p align="right"><a href="#top">Back to top</a></p>
