<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/map-release-manifest/v1
title: MapReleaseManifest Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-06-24
updated: 2026-08-07
policy_label: public-with-gates
related:
  - ../../schemas/contracts/v1/map/map_release_manifest.schema.json
  - ../../tools/validators/map/validate_map_release_manifest.py
  - ../../fixtures/contracts/v1/map/map_release_manifest/
  - ../../tests/map/test_map_release_manifest.py
  - ../map/map_release_manifest/README.md
  - ./release_manifest.md
  - ./tile_artifact_manifest.md
  - ./rollback_card.md
  - ./withdrawal_notice.md
tags: [kfm, release, map, map-release-manifest, evidence, rights, sensitivity, catalog, rollback]
notes:
  - "Semantic authority remains under contracts/release; the existing map schema family owns this object's machine shape."
  - "Fixture-first and PROPOSED_INACTIVE. Validation creates no release, publication, cache invalidation, or rollback authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapReleaseManifest Contract

`MapReleaseManifest` is the map-specific publication envelope that binds released or release-candidate map artifacts to layer and style manifests, evidence, catalog closure, policy, rights, sensitivity, review, attestations, correction lineage, cache invalidation, and rollback.

> [!IMPORTANT]
> The paired schema, fixtures, validator, tests, and workflow form a **fixture-first, no-network profile**. A valid synthetic manifest does not publish a map, approve a release, resolve evidence or policy, invalidate a cache, execute rollback, or authorize a public client.

## Authority split

| Responsibility | Owning surface |
|---|---|
| General release meaning | `contracts/release/release_manifest.md` |
| Map-release semantic specialization | `contracts/release/map_release_manifest.md` |
| Machine shape | `schemas/contracts/v1/map/map_release_manifest.schema.json` |
| Compatibility pointer | `contracts/map/map_release_manifest/README.md` |
| Artifact descriptions | referenced `TileArtifactManifest`, `LayerManifest`, and `StyleManifest` objects |
| Policy, rights, sensitivity, review | separate decision and review records |
| Emitted release/correction/rollback records | `release/` and governed data roots |
| Validation | `tools/validators/map/`, fixtures, tests, and read-only CI |

The `map/` schema family is retained because it already exists and groups map-facing machine shapes. This contract does not create a parallel release schema.

## Required semantic closure

A map release manifest carries:

- deterministic map-release identity and release state;
- a reference to the governing general release;
- immutable, digest-bound map artifact descriptions;
- released layer and style manifest references;
- STAC, DCAT, and PROV catalog references;
- evidence, policy, rights, sensitivity, review, and attestation references;
- a public-boundary record that forbids RAW, WORK, QUARANTINE, canonical-store, unreleased-artifact, and direct-model exposure;
- correction, supersession, withdrawal, and cache-invalidation lineage;
- a verified rollback target and rollback card where publication is declared.

The manifest references these object families. It does not absorb or replace them.

## Release states

| State | Minimum meaning |
|---|---|
| `CANDIDATE` | Review and closure remain pending; no `published_at` value. |
| `HELD` | Rights, sensitivity, evidence, or policy is unresolved. |
| `PUBLISHED` | Map artifact, catalog, evidence, policy, rights, sensitivity, review, attestation, and rollback references are present. |
| `STALE` | A released map package is no longer current for its declared scope. |
| `SUPERSEDED` | A newer release is named and cache invalidation is recorded. |
| `WITHDRAWN` | A withdrawal notice and cache invalidation are recorded. |
| `ROLLED_BACK` | The rollback target, card, verification, restoration receipt, and cache invalidation are recorded. |

State reason codes are explicit, sorted, and stable. A friendly map surface must not hide stale, superseded, withdrawn, denied, or rollback state.

## Artifact rules

Each artifact description binds:

- stable artifact identity and type;
- immutable artifact reference;
- SHA-256 digest;
- media type and cache policy;
- Range and CORS capability where PMTiles or COG delivery requires them.

Floating `latest` tags are denied. A digest field does not make an artifact proof; signing, catalog, evidence, policy, and release closure remain separate.

## Public-safety rules

1. Public clients use governed APIs and released artifacts only.
2. RAW, WORK, QUARANTINE, canonical stores, unreleased fetches, and direct model outputs are structurally forbidden.
3. `UNKNOWN` or `DENIED` rights or sensitivity cannot support `PUBLISHED`.
4. `GENERALIZED`, `RESTRICTED`, or `WITHHELD` geometry requires a redaction/generalization receipt.
5. PMTiles and COG artifacts declared as published require Range and CORS support.
6. A style, tile, screenshot, popup, or AI answer remains a downstream carrier, not sovereign truth.

## Deterministic identity

The canonical projection removes `map_release_id` and `spec_hash`, serializes the remaining object as sorted compact UTF-8 JSON with non-finite values denied, and computes SHA-256.

- `spec_hash = sha256:<64 lowercase hex>`
- `map_release_id = map-release:<first 24 hex characters of spec_hash>`

Set-like reference arrays and artifact entries are sorted and unique.

## Validation boundary

The deterministic validator checks:

- bounded UTF-8 JSON, duplicate keys, and non-finite numbers;
- Draft 2020-12 schema conformance;
- canonical ordering and deterministic identity;
- published closure for artifacts, catalogs, evidence, decisions, review, attestations, and rollback;
- rights/sensitivity and generalized-geometry rules;
- immutable/digest-pinned artifact references;
- Range/CORS rules for PMTiles and COG;
- finite stale, superseded, withdrawal, and rollback semantics;
- no-public-internal-path invariants.

It does not fetch artifacts, verify live HTTP headers, resolve evidence or catalog records, authenticate reviews, evaluate policy, verify signatures, authorize release, alter caches, execute rollback, deploy, or publish.

## Lifecycle and rollback

A manifest may describe a candidate or synthetic release state, but this profile writes no lifecycle or release state. Promotion remains a governed transition backed by independently reviewed evidence, policy, proof, correction, and rollback records.

Rollback of this implementation is a commit revert restoring the previous semantic contract and scaffold schema. No map release or public artifact is changed by removing the fixture profile.

<p align="right"><a href="#top">Back to top</a></p>
