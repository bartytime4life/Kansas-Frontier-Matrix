<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/renderer-capability-profile
title: Renderer Capability Profile Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; non-authoritative
owners: OWNER_TBD — UI steward · Map runtime steward · Contracts steward · Release steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; ui; renderer; capability; fixture-only
owning_root: contracts/
responsibility: Define the semantic meaning and fail-closed validation boundary of a fixture-only renderer capability declaration behind the accepted adapter seam.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / no renderer admission, runtime probe, release, deployment, or publication authority
related:
  - ../../docs/architecture/map-master.md
  - ../../docs/architecture/maplibre-master.md
  - ../../docs/adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
  - ./view_registry_profile.md
  - ./evidence_drawer_payload.md
  - ../release/tile_artifact_manifest.md
  - ../../schemas/contracts/v1/ui/renderer_capability_profile.schema.json
  - ../../fixtures/contracts/v1/ui/renderer_capability_profile/cases.json
  - ../../tools/validators/ui/validate_renderer_capability_profile.py
  - ../../tests/validators/ui/test_renderer_capability_profile.py
  - ../../docs/intake/exploratory/renderer-capability-profile-source-map.md
tags: [kfm, ui, maplibre, renderer, adapter, capability, substitutability, fixture-only]
notes:
  - "Implements a bounded contract-first slice of the Full Atlas Renderer as Pluggable Component Framework proposal."
  - "Compatibility is kept separate from admission: MapLibre GL JS remains the sole browser-side renderer under ADR-0007."
[/KFM_META_BLOCK_V2] -->

# Renderer Capability Profile Candidate

> A deterministic, fixture-only declaration for asking whether a synthetic
> renderer advertises the capabilities required by one KFM-owned abstract
> interface, without selecting, loading, probing, or admitting that renderer.

## Status and purpose

| Field | Value |
|---|---|
| Profile | `kfm.renderer-capability-candidate.v1` |
| Interface | `kfm.renderer.abstract.v1` |
| State | `PROPOSED` / inactive / review-pending |
| Browser rule | `MAPLIBRE_GL_JS_ONLY` |
| Runtime, release, or publication effect | None |

The source proposal asks for renderer implementations to sit behind an
abstract interface so capability-compatible implementations can be compared
without coupling governed contracts to one library. KFM already has a stronger
accepted browser rule: MapLibre GL JS is the sole browser-side renderer behind
the KFM-owned adapter seam. This profile preserves that rule. It evaluates
synthetic declarations only and never turns capability compatibility into
admission, parity, fitness, or release approval.

## Preserved axes

Each candidate keeps these concerns separate:

- renderer family and runtime surface;
- KFM-owned abstract-interface version;
- governed semantic contracts consumed by the adapter;
- required and declared capability vocabularies;
- mechanically derived compatibility state and disposition;
- accepted browser-renderer and adapter-seam constraints; and
- fixed-false data, query, evidence, policy, release, deployment, publication,
  and public-use authority.

The `implementation_ref` is a synthetic `urn:kfm:synthetic:renderer:*` label.
It is not a package coordinate, URL, executable, installation request, runtime
probe, allowlist entry, or release-manifest selection.

## Deterministic validation

The validator requires canonical lexical ordering, unique capability and
contract lists, repository-local semantic-contract references, JCS plus
SHA-256 identity, and an exact derived compatibility result. It rejects:

- a browser renderer other than `MAPLIBRE_GL_JS`;
- a `HEADLESS` renderer outside `SERVER` or `TEST` surfaces;
- missing, non-contract, URL, package-manager, direct-store, or query material;
- stale missing-capability, compatibility, disposition, digest, or identifier
  fields;
- bypass of the KFM-owned adapter seam; and
- evidence, policy, release, registry-write, deployment, publication, or
  public-use authority claims.

## Finite outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | The declaration is complete for its stated requirement set. | Still `REVIEW_REQUIRED`; no renderer is selected or admitted. |
| `ABSTAIN` | The declaration is valid but lacks part of the requirement set. | No inferred capability, fallback renderer, or runtime probe. |
| `DENY` | Shape, identity, reference, browser-rule, boundary, or complete incompatibility checks fail. | No installation, loading, release, or fallback. |
| `ERROR` | The input cannot be boundedly read or parsed. | No partial result is trusted. |

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Candidate semantic meaning | `contracts/ui/` |
| Machine shape | `schemas/contracts/v1/ui/` |
| Synthetic cases | `fixtures/contracts/v1/ui/` |
| Deterministic validation | `tools/validators/ui/` |
| Executable conformance evidence | `tests/validators/ui/` |
| Hosted read-only orchestration | `.github/workflows/` |
| Source adaptation | `docs/intake/exploratory/` |
| AI authoring provenance | `data/receipts/generated/` |

No new root, renderer registry, package, adapter implementation, policy rule,
runtime probe, or public surface is created.

## Non-effects

A green result does not:

- weaken or supersede ADR-0007;
- declare MapLibre Native parity or admit MapLibre RS;
- install, import, execute, benchmark, or contact a renderer;
- read a store, issue a query, resolve evidence, or evaluate policy;
- change the view registry, artifact manifests, allowlists, or release state;
- approve review, release, deploy, publish, or authorize public use; or
- prove accessibility, security, licensing, supply-chain, performance,
  offline-cache, denial, abstain, or Evidence Drawer parity.

## Rollback

Before merge, close the draft pull request and remove its branch. After an
authorized merge, revert the additive packet and rerun its dedicated workflow.
No renderer, package, registry, policy, runtime, data, release, deployment, or
public state requires restoration.

