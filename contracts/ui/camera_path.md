<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/camera-path-candidate
title: Camera Path Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; non-authoritative
owners: OWNER_TBD — UI steward · Accessibility steward · Map runtime steward · Contract steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; ui; motion; fixture-only
owning_root: contracts/
responsibility: Define the semantic and fail-closed validation boundary for a fixture-only, renderer-neutral camera path candidate.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / no runtime, evidence, policy, admission, release, or publication authority
related:
  - ./view_registry_profile.md
  - ../../docs/architecture/ui/ACCESSIBILITY.md
  - ../../docs/architecture/map-master/README.md
  - ../../schemas/contracts/v1/ui/camera_path.schema.json
  - ../../fixtures/contracts/v1/ui/camera_path/cases.json
  - ../../tools/validators/ui/validate_camera_path.py
  - ../../tests/validators/ui/test_camera_path.py
  - ../../docs/intake/exploratory/camera-path-source-map.md
tags: [kfm, ui, camera-path, view-state, motion, accessibility, fixture-only]
notes:
  - "Adapts the CameraPath proposal from maplibre3d.md without adopting its proposed maplibre-specific schema or runtime paths."
  - "A valid candidate is reviewable motion metadata, not executable playback or scene admission."
[/KFM_META_BLOCK_V2] -->

# Camera Path Candidate

> A deterministic, fixture-only sequence of renderer-neutral view states that
> keeps scene, time, evidence, accessibility, and authority boundaries explicit.

## Status and purpose

| Field | Value |
|---|---|
| Profile | `kfm.camera-path-candidate.v1` |
| State | `PROPOSED` / inactive / review-pending |
| Execution mode | Synthetic fixture validation only |
| Runtime, admission, release, or publication effect | None |

The source proposal treats a `CameraPath` as a governed JSON asset rather than
an opaque renderer animation. This bounded adaptation preserves that useful
idea while removing renderer-specific authority. It validates a sequence,
scene reference, temporal anchor, evidence references, and mandatory motion
alternatives. It does not initialize a renderer, move a camera, resolve a
scene, fetch evidence, or authorize a story or Focus Mode result.

## Required semantics

A candidate must:

- bind to one declared scene-manifest reference;
- carry a closed temporal anchor with `valid_from <= valid_to`;
- contain two to sixty-four view states;
- start at `t_ms = 0`, increase timestamps strictly, and end at the declared
  duration;
- keep evidence references unique and lexically ordered;
- use a deterministic JCS/SHA-256 identity;
- disable autoplay and looping in this first fixture profile;
- provide `DISCRETE_STEPS` as the reduced-motion alternative;
- require a 2D fallback and make outcomes independent of playback; and
- remain fixed-false for runtime execution, evidence resolution, policy,
  3D/plugin admission, release, deployment, publication, and public use.

`MERCATOR` and `GLOBE` are view-state declarations only. Their presence does
not prove renderer support or satisfy a `3DAdmissionDecision`, plugin
admission, accessibility review, EvidenceBundle closure, or release gate.

## Finite validation outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS` | Shape, identity, sequence, time, and boundary checks pass. | Candidate remains `REVIEW_REQUIRED` and inactive. |
| `DENY` | A schema, identity, sequence, time, or authority invariant fails. | No partial path is executed. |
| `ERROR` | The input cannot be boundedly read or parsed. | No candidate values are trusted. |

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Renderer-neutral UI motion meaning | `contracts/ui/` |
| Machine shape | `schemas/contracts/v1/ui/` |
| Synthetic examples | `fixtures/contracts/v1/ui/` |
| Deterministic validation | `tools/validators/ui/` |
| Executable checks | `tests/validators/ui/` |
| Source reconciliation | `docs/intake/exploratory/` |
| Hosted read-only orchestration | `.github/workflows/` |
| AI authoring provenance | `data/receipts/generated/` |

The source suggested `contracts/maplibre/` and
`schemas/contracts/v1/maplibre/`. Those paths are not adopted here:
`contracts/map/` is currently a compatibility boundary, and the proposed
renderer package/home decision is unresolved. The UI family already owns
renderer-neutral view and interaction contracts, so this slice does not create
a parallel map, MapLibre, policy, runtime, or release authority.

## Non-effects

A green result does not:

- create, select, or admit a scene, layer, renderer, adapter, or plugin;
- execute animation, camera movement, network access, or asset loading;
- resolve an `EvidenceRef` or authenticate a scene or release reference;
- evaluate rights, sensitivity, CARE, 3D, plugin, or release policy;
- prove reduced-motion usability, 2D parity, performance, or browser support;
- authorize a story, Focus Mode answer, release, deployment, publication, or
  public use; or
- accept, supersede, or implement ADR-0007.

## Rollback

Before merge, close the draft pull request and delete its branch. After an
authorized merge, revert the additive packet and rerun its focused workflow.
No runtime, data, scene, policy, release, deployment, or public state requires
restoration because the profile is inactive and fixture-only.
