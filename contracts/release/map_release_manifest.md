<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-release-map-release-manifest
title: contracts/release/map_release_manifest.md — MapReleaseManifest Contract
type: contract
version: v0.2
status: draft; PROPOSED; map-publication-envelope; schema-missing; release-manifest-specialization
owners: OWNER_TBD — Release steward · Map/UI steward · Layer steward · Contracts steward · Schema steward · Policy steward · Evidence steward · Rights steward · Sensitivity steward · Rollback steward · Docs steward
created: NEEDS VERIFICATION — file existed before v0.2 expansion
updated: 2026-06-24
policy_label: public; contracts; release; map-release-manifest; map-publication; release-gated; evidence-aware; rights-aware; sensitivity-aware; rollback-aware; no-artifact-store; no-runtime-authority
tags: [kfm, contracts, release, map-release-manifest, release-manifest, maplibre, pmtiles, cog, layer-manifest, style-manifest, tile-artifact-manifest, evidence-ref, rights, sensitivity, attestations, correction-lineage, rollback]
related:
  - ./README.md
  - ./release_manifest.md
  - ./layer_manifest.md
  - ./promotion_decision.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
  - ../data/layer_manifest.md
  - ../data/layer_descriptor.md
  - ../data/layer_catalog_item.md
  - ../map/map_release_manifest/README.md
  - ../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../schemas/contracts/v1/release/map_release_manifest.schema.json
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
  - "`docs/standards/RELEASE_MANIFEST.md` identifies `MapReleaseManifest` as a canonical publication envelope binding artifacts, evidence_refs, rights, sensitivity, release_state, policy result, attestations, correction_lineage, and rollback."
  - "The general `ReleaseManifest` contract already exists at `contracts/release/release_manifest.md`; this contract specializes map-publication semantics and must not replace the general release manifest."
  - "No `schemas/contracts/v1/release/map_release_manifest.schema.json` was verified in this session; schema behavior remains UNKNOWN / NEEDS VERIFICATION."
  - "This contract does not store PMTiles, COGs, style JSON, sprites, glyphs, vector tiles, release artifacts, proofs, receipts, public API payloads, UI state, or AI output."
  - "Rollback target for this expansion is previous scaffold blob SHA `8abbc29834c1a3ea60bd0929d7fe8a1baa18c213`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapReleaseManifest Contract

> Semantic contract for `MapReleaseManifest`, the map-publication envelope that binds released map artifacts to evidence, rights, sensitivity, policy decisions, attestations, correction lineage, and rollback targets. It specializes map release semantics; it does not replace the general [`ReleaseManifest`](./release_manifest.md), store map artifacts, or authorize publication by itself.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts" src="https://img.shields.io/badge/root-contracts-blue">
  <img alt="Object: MapReleaseManifest" src="https://img.shields.io/badge/object-MapReleaseManifest-0a7ea4">
  <img alt="Schema: missing" src="https://img.shields.io/badge/schema-missing-red">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release__gated-critical">
  <img alt="Artifacts: referenced only" src="https://img.shields.io/badge/artifacts-referenced__only-lightgrey">
</p>

**Status:** draft / PROPOSED / schema missing  
**Path:** `contracts/release/map_release_manifest.md`  
**General release contract:** [`./release_manifest.md`](./release_manifest.md)  
**Map/layer bridge contract:** [`./layer_manifest.md`](./layer_manifest.md)  
**Canonical inspected layer contract:** [`../data/layer_manifest.md`](../data/layer_manifest.md)  
**Expected schema path:** `schemas/contracts/v1/release/map_release_manifest.schema.json` — NEEDS VERIFICATION; not found in this session  
**Policy authority:** `policy/release/`, `policy/data/`, `policy/sensitivity/`, rights/access policy roots, not this contract  
**Release artifact authority:** `release/`, not this contract  
**Truth posture:** CONFIRMED target scaffold replaced · CONFIRMED standards doc names MapReleaseManifest and required content · CONFIRMED general ReleaseManifest contract exists but is thin/permissive · PROPOSED MapReleaseManifest fields until schema/fixtures/validator/release integration are implemented

## Quick jumps

[Purpose](#purpose) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Boundary with ReleaseManifest](#boundary-with-releasemanifest) · [Map-publication semantics](#map-publication-semantics) · [Proposed fields](#proposed-fields) · [Invariants](#invariants) · [Lifecycle role](#lifecycle-role) · [Exclusions](#exclusions) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`MapReleaseManifest` is the release-facing envelope for a published map surface.

It answers:

- which map release is being published;
- which map artifacts are included by digest/ref;
- which layer manifests, tile archives, COGs, PMTiles, style fragments, sprites, glyphs, sidecars, and renderer-facing descriptors are part of the release;
- which evidence, rights, sensitivity, policy, review, and attestation records support the release;
- what public, restricted, generalized, or withheld posture applies to the map surface;
- how correction, supersession, withdrawal, or rollback is handled.

It does not answer:

- whether a general release exists — that is `ReleaseManifest`;
- what a layer means — that is `LayerManifest` and its data/layer contracts;
- whether policy allows publication — that is PolicyDecision / policy gate output;
- whether evidence is true — that is EvidenceBundle / evidence resolution;
- whether map artifacts are stored here — artifacts belong to release/artifact roots;
- whether public clients may bypass governed APIs — they may not.

---

## Meaning

A `MapReleaseManifest` is a map-specific publication envelope.

It should bind:

1. **Release identity** — release id, version, spec hash, release state, timestamps.
2. **Map artifacts** — artifact refs/digests for PMTiles, COGs, tile archives, styles, sprites, glyphs, metadata sidecars, tilejson, or other renderer-facing assets.
3. **Layer references** — layer manifest refs, layer descriptor refs, layer catalog item refs, and optional style/layer bundles.
4. **Evidence** — EvidenceRefs/EvidenceBundle refs supporting map-visible claims and layer provenance.
5. **Rights** — license, terms, attribution, redistribution/export limitations, embargo, and rights uncertainty posture.
6. **Sensitivity** — redaction, generalization, withheld exact geometry, public/restricted/quarantine labels, and safe-display constraints.
7. **Policy** — PolicyDecision refs for release, render, access, export, sensitivity, rights, and AI/map interaction where applicable.
8. **Attestations** — signing, build, validation, integrity, or provenance attestations by digest/ref.
9. **Correction lineage** — correction notices, stale-state notices, supersession, withdrawal, and invalidation lists.
10. **Rollback** — rollback target, prior release refs, cache invalidation, and restoration posture.

A `MapReleaseManifest` is not sovereign truth. It is a trust-spine envelope that must reference evidence, policy, release, and artifact records rather than collapse them into one blob.

---

## Repo fit

| Responsibility | Correct home | Relationship to this contract |
|---|---|---|
| General release meaning | `contracts/release/release_manifest.md` | Parent/general release object. |
| Map release semantics | `contracts/release/map_release_manifest.md` | This contract; PROPOSED. |
| Release layer bridge | `contracts/release/layer_manifest.md` | Layer-in-release relationship companion. |
| Canonical layer meaning | `contracts/data/layer_manifest.md` | Inspected layer manifest authority. |
| Layer descriptor/catalog | `contracts/data/layer_descriptor.md`, `contracts/data/layer_catalog_item.md` | Renderer/discovery companions. |
| Machine schema | `schemas/contracts/v1/release/map_release_manifest.schema.json` | Expected but not verified. |
| Release policy | `policy/release/` | Admissibility / gate authority. |
| Sensitivity/rights policy | `policy/sensitivity/`, rights/access policy roots | Public-safe map exposure decisions. |
| Release artifacts | `release/` | Publication process outputs and release records. |
| Layer registry/catalog | `data/registry/layers/`, `data/catalog/` or accepted homes | Discovery state and layer refs. |
| Proofs and receipts | `data/proofs/`, `data/receipts/` or accepted homes | Auditable trust artifacts. |
| Public map/runtime | governed API/UI/map roots | Downstream consumers only. |

---

## Boundary with ReleaseManifest

`ReleaseManifest` is the general release binding. `MapReleaseManifest` is the map-specific envelope when the release includes map artifacts and map-facing constraints.

| Question | ReleaseManifest | MapReleaseManifest |
|---|---|---|
| What release exists? | In scope. | References/generalizes for map release. |
| Which all-purpose release contents are published? | In scope. | Map subset/specialization in scope. |
| Which map artifacts are included? | May list as contents. | In scope with artifact refs/digests and map semantics. |
| What map/layer sensitivity applies? | May reference policy/sensitivity. | In scope as map exposure posture. |
| Which style/tile/layer dependencies matter? | May reference artifacts. | In scope as renderer-facing release dependencies. |
| Does this approve publication? | No, not alone. | No, not alone. |
| Does this store artifacts? | No. | No. |

---

## Map-publication semantics

A map release is not only a set of files. It is a governed public or restricted map surface.

The map envelope must preserve:

- artifact identity and digest integrity;
- layer-to-source and layer-to-evidence lineage;
- rights and attribution posture;
- sensitivity and redaction/generalization posture;
- review and policy decision state;
- release state and rollback target;
- correction, withdrawal, and supersession lineage;
- public-client trust boundary.

Public clients must bind to released artifacts through governed interfaces and release manifests, not floating `latest` paths, raw data, work data, quarantine data, internal stores, graph internals, vector indexes, source APIs, or direct model runtime outputs.

---

## Proposed fields

No paired schema was verified in this session. These fields are therefore PROPOSED semantic targets only:

| Field | Meaning | Required posture |
|---|---|---|
| `map_release_id` | Stable id for the map release envelope. | Deterministic where practical. |
| `release_manifest_ref` | Ref to general ReleaseManifest. | Must resolve for PUBLISHED release use. |
| `release_state` | candidate, held, published, superseded, withdrawn, rolled_back, stale. | Finite state recommended. |
| `contents` | Map release contents by ref. | No payloads; refs/digests only. |
| `artifact_digests` | PMTiles/COG/tile/style/sprite/glyph/sidecar digests. | Required for artifact integrity. |
| `layer_manifest_refs` | Released layer manifest refs. | Must resolve to governed layer manifests. |
| `style_manifest_refs` | Style/style-fragment refs. | Must resolve before map release. |
| `tile_artifact_refs` | Tile archive/PMTiles/COG/tilejson refs. | Must be digest-bound. |
| `evidence_refs` | Evidence refs supporting map-visible claims. | Must resolve to EvidenceBundle where claims depend on evidence. |
| `rights_refs` | Rights/license/terms/attribution refs. | Unknown rights fail closed. |
| `sensitivity_refs` | Sensitivity labels/redaction/generalization refs. | Exact sensitive values must not leak. |
| `policy_decision_refs` | Policy decisions for release/render/access/export. | Must include relevant gate outcomes. |
| `attestation_refs` | Signing/build/provenance/validation attestations. | Must be digest-bound and auditable. |
| `correction_lineage_refs` | Corrections/supersessions/withdrawals/invalidation refs. | Must preserve public audit trail. |
| `rollback_target_ref` | Prior map release or artifact set for rollback. | Required unless explicitly waived. |
| `published_at` | Publication time. | UTC/date-time recommended. |

---

## Invariants

PROPOSED semantic invariants:

- `MapReleaseManifest` must reference a general `ReleaseManifest` or explain why the release model has been split by ADR.
- It must reference map artifacts by digest/ref, not store payloads.
- It must preserve EvidenceRef/EvidenceBundle links for map-visible claims.
- It must carry or reference rights, sensitivity, policy result, attestations, correction lineage, and rollback target before publication.
- It must not publish or expose layers by itself; release policy and release process decide.
- It must not override canonical `LayerManifest`, `LayerDescriptor`, `LayerCatalogItem`, `PolicyDecision`, `EvidenceBundle`, `ReviewRecord`, `CorrectionNotice`, or `RollbackCard` semantics.
- It must fail closed for unknown rights, unresolved evidence, missing rollback target, missing policy decision, missing attestation, or sensitive exact locations lacking redaction/generalization/restriction.
- It must preserve correction, withdrawal, supersession, and rollback history instead of silently mutating public map state.

---

## Lifecycle role

`MapReleaseManifest` applies at the map-publication boundary:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Lifecycle point | Role |
|---|---|
| PROCESSED → CATALOG/TRIPLET | Usually absent or candidate-only; map artifacts may be prepared but not public. |
| CATALOG/TRIPLET → PUBLISHED | Binds map artifacts, layers, evidence, rights, sensitivity, policy, attestations, and rollback into a publishable map release. |
| PUBLISHED → PUBLISHED′ correction | Links corrected/superseding map release and invalidation list. |
| PUBLISHED → prior release rollback | Identifies map release rollback target and public/cache invalidation path. |
| PUBLISHED → withdrawn | Preserves public-safe withdrawal posture and affected artifacts. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| General ReleaseManifest definition | `contracts/release/release_manifest.md` | Avoids duplicate release authority. |
| Canonical LayerManifest definition | `contracts/data/layer_manifest.md` | Avoids duplicate layer authority. |
| JSON Schema | `schemas/contracts/v1/release/` or accepted schema home | Schemas own machine shape. |
| PMTiles, COGs, vector tiles, sprites, glyphs, style JSON | `release/`, lifecycle artifact roots, or accepted artifact stores | Payloads are artifacts, not contract prose. |
| Release JSON instances | `release/` | Contracts do not store release records. |
| Proofs, receipts, signatures, DSSE/SLSA/in-toto attestations | `data/proofs/`, `data/receipts/`, signing/release roots | Trust artifacts remain separately auditable. |
| Rego/OPA/equivalent policy rules | `policy/release/`, `policy/data/`, sensitivity/rights roots | Policy owns admissibility. |
| Map runtime/UI/API code | `apps/`, `ui/`, `web/`, packages | Public/render surfaces are downstream. |
| AI-generated map summaries | Governed AI envelopes with evidence/policy/release checks | AI is interpretive, not release authority. |

---

## Validation expectations

NEEDS VERIFICATION before treating this contract as implementation-backed:

- accepted object name: `MapReleaseManifest` vs `ReleaseManifest` contents specialization;
- paired schema creation or compatibility decision;
- fixture home and minimum fixtures for valid public map release, generalized/restricted map release, rights-denied release, missing rollback target, missing attestation, corrected map release, withdrawn map release, and rollback;
- validator path and CI wiring;
- policy rules for map release, render, access, sensitivity, rights, export, and AI interaction;
- proof/receipt binding to artifact digests and ReleaseManifest;
- public API/UI/map tests proving no pre-PUBLISHED or sensitive layer leakage.

---

## Open questions

- Should `MapReleaseManifest` be a standalone object or a profile of `ReleaseManifest.contents[]`?
- Should the paired schema live under `schemas/contracts/v1/release/`, `schemas/contracts/v1/map/`, or `schemas/contracts/v1/layers/`?
- Should PMTiles/COG sidecars be separate `TileArtifactManifest` objects referenced by this manifest?
- Which exact fields are required before public MapLibre clients can bind to a release?
- Which release gate verifies CDN/cache invalidation and rollback for map artifacts?

---

## Rollback

Rollback is required if this file is used to publish a map, store artifacts, bypass `ReleaseManifest`, bypass schema/policy/review/evidence/release gates, expose sensitive exact locations, hide correction lineage, or authorize public map/UI/AI exposure directly.

Rollback target for this expansion: previous scaffold blob SHA `8abbc29834c1a3ea60bd0929d7fe8a1baa18c213`.

<p align="right"><a href="#top">Back to top</a></p>
