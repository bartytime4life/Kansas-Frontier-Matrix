<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/source/map-service-protocol-assessment
title: Map Service Protocol Assessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed; inactive; fixture-only; no-network; review-required
owners: OWNER_TBD — Source steward · Map steward · Rights reviewer · Validation steward
created: 2026-08-11
updated: 2026-08-11
policy_label: internal; source; map-service; pmtiles; xyz; wmts; wms
owning_root: contracts/
responsibility: Define a bounded protocol-specific assessment for PMTiles, XYZ, WMTS, and WMS source declarations without fetching a service, activating a source, or authorizing release or publication.
truth_posture: CONFIRMED source-card and repository-gap evidence / PROPOSED inactive assessment / NEEDS VERIFICATION human review and hosted exact-head CI
related:
  - ./source_descriptor.md
  - ./source_rights_currentness_assessment.md
  - ./source_health_assessment.md
  - ../data/layer_manifest.md
  - ../../schemas/contracts/v1/source/map_service_protocol_assessment.schema.json
  - ../../fixtures/contracts/v1/source/map_service_protocol_assessment/cases.json
  - ../../tools/validators/source/validate_map_service_protocol_assessment.py
  - ../../tests/validators/test_validate_map_service_protocol_assessment.py
  - ../../docs/intake/exploratory/pass-18-map-service-protocol-assessment-source-map.md
tags: [kfm, source, map, protocol, pmtiles, xyz, wmts, wms, fixture-only]
notes:
  - "Implements the smallest inactive slice of Pass 18 cards KFM-P18-INV-073 and KFM-P18-INV-180."
  - "PASS means locally coherent and ready for human review; it never verifies remote bytes, rights, source authority, release, or public use."
[/KFM_META_BLOCK_V2] -->

# Map Service Protocol Assessment Candidate

> A deterministic, no-network assessment that keeps packaged PMTiles artifacts, XYZ tile templates, WMTS capabilities services, and WMS capabilities services from collapsing into one generic map-source declaration.

## Purpose

Map protocols expose different mutability, discovery, validation, caching, freshness, and failure behavior. A version-pinned PMTiles artifact is not equivalent to an XYZ template, and neither is equivalent to a WMTS or WMS capabilities service.

This profile checks one synthetic declaration against protocol-specific local invariants. It composes `SourceDescriptor`, `SourceRightsCurrentnessAssessment`, `SourceHealthAssessment`, and `LayerManifest` only by opaque reference. It does not resolve those references, contact an endpoint, parse capabilities XML, inspect PMTiles bytes, request a tile, verify terms, mutate a cache, activate a source, register a layer, or publish a map.

## Protocol matrix

| Protocol | Required access surface | Required local evidence kind | Source-use role | Cache and freshness posture |
|---|---|---|---|---|
| `PMTILES` | `LOCAL_IMMUTABLE_ARTIFACT` | `PMTILES_HEADER_ASSESSMENT` | `VERSIONED_ARTIFACT` | Non-placeholder artifact digest, immutable declaration, `IMMUTABLE_VERSIONED`, no remote-health claim. |
| `XYZ` | `REMOTE_TILE_TEMPLATE` | `XYZ_TEMPLATE_ASSESSMENT` | `CONTEXT_ONLY` | Mutable declaration, `REVALIDATE` or `NO_STORE`, freshness-policy and source-health refs. |
| `WMTS` | `REMOTE_CAPABILITIES_SERVICE` | `WMTS_CAPABILITIES_ASSESSMENT` | `CONTEXT_ONLY` | Mutable declaration, `REVALIDATE` or `NO_STORE`, freshness-policy and source-health refs. |
| `WMS` | `REMOTE_CAPABILITIES_SERVICE` | `WMS_CAPABILITIES_ASSESSMENT` | `CONTEXT_ONLY` | Mutable declaration, `REVALIDATE` or `NO_STORE`, freshness-policy and source-health refs. |

The evidence refs are declarations only. The validator never dereferences them and never treats their syntax as proof.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The declared protocol, access surface, local evidence kind, source-use role, cache posture, current rights assessment, attribution, and health posture are internally coherent. | No endpoint, artifact, terms, attribution, rights, health, or evidence is independently verified. |
| `ABSTAIN` | Rights review, cache policy, or source health is due, degraded, or unresolved. | No optimistic default is inferred and no source is activated. |
| `DENY` | The protocol mapping is incoherent, rights are blocked, required attribution is absent, or a remote source is stale or unavailable. | No partial declaration is accepted. |
| `ERROR` | The bounded assessment could not be completed safely. | No candidate state is trusted. |

## Invariants

1. Protocol, access surface, and protocol-evidence kind must match the matrix exactly.
2. PMTiles requires a non-placeholder artifact digest and cannot declare remote freshness or health.
3. XYZ, WMTS, and WMS remain `CONTEXT_ONLY`, cannot carry an artifact digest, and require explicit freshness and health references.
4. Required attribution must have non-empty attribution text.
5. Blocked rights, stale or unavailable remote health, or protocol incoherence deny the assessment.
6. Review-due or unresolved rights, unknown cache posture, and unknown or degraded remote health abstain.
7. Network, activation, fetching, reference resolution, remote-byte verification, rights, cache mutation, layer registration, release, publication, and public-use authority are fixed to `false`.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete candidate except `assessment_id` and `spec_hash`:

```text
spec_hash     = SHA-256(JCS(identity subject))
assessment_id = "kfm:map-service-protocol:" + first_24_hex(spec_hash)
```

Identity binds the protocol declaration, reference-only controls, decision, limitations, and all-false authority surface. It is not a service probe, proof, approval, signature, activation token, or release decision.

## Composition boundary

- `SourceDescriptor` retains source identity, access, rights, cadence, and citation meaning.
- `SourceRightsCurrentnessAssessment` retains detailed rights and terms currentness evaluation.
- `SourceHealthAssessment` retains observed freshness and availability evaluation.
- `LayerManifest` retains layer representation, lineage, exposure, runtime, and release-facing declarations.
- The existing MapLibre source-metadata validator remains a renderer-projection check and is not expanded into protocol or source authority.

This profile contributes only a closed, protocol-specific review seam between those responsibilities.

## Directory Rules basis

Source assessment meaning belongs under `contracts/source/`; machine shape under `schemas/contracts/v1/source/`; synthetic cases under `fixtures/contracts/v1/source/`; deterministic validation under `tools/validators/source/`; executable conformance evidence under `tests/validators/`; hosted orchestration under `.github/workflows/`; source adaptation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

Accepted ADR-0029 and the adopted Directory Rules were consulted. No new root or parallel source, rights, health, evidence, layer, cache, release, or publication authority is created.

## Validation

```bash
python -m unittest -v tests.validators.test_validate_map_service_protocol_assessment
python tools/validators/source/validate_map_service_protocol_assessment.py --fixtures
```

## Rollback

Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this additive packet. It has no runtime consumer and changes no source, endpoint, artifact, cache, layer, registry, release, deployment, or public surface.
