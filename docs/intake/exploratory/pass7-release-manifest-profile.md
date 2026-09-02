<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass7-release-manifest-profile
title: Pass 7 ReleaseManifest Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; implementation-mapping
owners: OWNER_TBD — Release steward · Source-intake steward
created: 2026-08-08
updated: 2026-08-08
policy_label: internal; exploratory; no-authority
owning_root: docs/
responsibility: Record how Pass 7 KFM-P7-PROG-0003 was adapted to current repository evidence.
truth_posture: CONFIRMED source/repo observations; PROPOSED bounded adaptation
related:
  - ../../../contracts/release/release_manifest.md
  - ../../../schemas/contracts/v1/release/release_manifest.schema.json
  - ../../../tools/validators/release/validate_release_manifest.py
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [pass-7, release-manifest, source-intake, fixture-only]
[/KFM_META_BLOCK_V2] -->

# Pass 7 ReleaseManifest source map

## Source idea

`KFM-P7-PROG-0003` states that a published release should be bound by one signed, hashable ReleaseManifest listing every included dataset, EvidenceBundle, tile archive, and LayerManifest, and that consumers should bind to that fixed manifest instead of a floating `latest` pointer.

## Current repository reconciliation

**CONFIRMED at implementation base `753cda68c468e8d01457c38e563c107a437aa608`:**

- the semantic contract existed and explicitly described its paired schema as a thin placeholder;
- the paired schema required only `id`, made `spec_hash` and `version` optional, and allowed arbitrary additional properties;
- the contract named `tools/validators/release/validate_release_manifest.py`, but that file did not exist;
- the named fixture lane did not exist;
- the deterministic hashing package and established dual-profile LayerManifest pattern were available.

## Adaptation decision

This packet does not create a production release format or consumer. It preserves the legacy schema branch and adds a closed, inactive, fixture-only candidate profile with deterministic identity, finite validation, synthetic fixtures, focused tests, read-only CI, validator-registry membership, and an exact-byte generated authoring receipt.

## Explicit non-effects

This source map and its implementation packet do not resolve refs, verify release payload bytes, validate signatures, evaluate policy, authenticate review, transition lifecycle state, create a persisted release record, update aliases/caches, deploy, publish, or authorize public use.

## Future dependency edge

A later separately reviewed slice may add a no-network consumer-side verifier that reads a **released** manifest projection, verifies exact artifact refs/digests and supporting authority closures, and returns a finite hold/deny result. That work must not use this inactive candidate profile as release authority.
