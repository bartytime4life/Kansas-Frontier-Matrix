<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/camera-path-source-map
title: Camera Path Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · UI steward · Accessibility steward · Map runtime steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: Reconcile the supplied CameraPath proposal to current repository authority and define one bounded fixture-only implementation slice.
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/ui/camera_path.md
  - ../../architecture/ui/ACCESSIBILITY.md
  - ../../architecture/map-master/README.md
  - ../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, atlas, ui, camera-path, accessibility, source-map]
[/KFM_META_BLOCK_V2] -->

# Camera Path Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Attached `maplibre3d.md`, SHA-256 `5148c85acaef7f299864df5b1804eb07498cb81ab4c4bcc39a9625287ee2817b`, §7.4 | Proposes a JSON `CameraPath` with scene binding, temporal anchor, timed view states, evidence references, and a deterministic hash. | Draft architecture/programming guide; proposed paths and renderer decisions are not repository authority. |
| `docs/architecture/ui/ACCESSIBILITY.md` | Requires discrete camera snapshots under reduced motion, a 2D alternative, and outcomes that do not depend on animation completion. | Architecture prose does not execute playback or prove accessibility conformance. |
| `docs/architecture/map-master/README.md` | Names `ViewState` and `CameraPath` as governed view and cinematic-motion assets. | Vocabulary entry; no current machine-backed object was found. |
| `docs/doctrine/directory-rules.md` and ADR-0029 | Require responsibility-root separation and record `maplibre3d.md` as technology-decision input whose decision remains ADR-scoped. | Placement authority; does not accept a renderer or create runtime behavior. |

## Repository reconciliation

GitHub and local `main@9e76413313b8529091d01be6132d6e987e3f9fae` were inspected on
2026-08-10. No open pull request, current file, or historical pull-request
title for `CameraPath` was found. Current doctrine references the object, but
the repository did not contain its contract, schema, fixtures, validator,
tests, workflow, or generated authoring receipt.

The source proposed `contracts/maplibre/`,
`schemas/contracts/v1/maplibre/`, and an executable runtime module. Current
repository evidence does not support those placements:

- `contracts/map/README.md` explicitly remains a compatibility boundary;
- `packages/maplibre/` is a private placeholder scaffold;
- `packages/maplibre-runtime/` is absent at the inspected base;
- ADR-0007 remains `proposed`, with the physical adapter home unresolved; and
- `contracts/ui/` already owns renderer-neutral view and interaction meaning.

The implementation therefore adds only a renderer-neutral UI candidate. It
does not create either proposed runtime package or accept a renderer decision.

## Bounded adaptation

| Source pressure | Retained behavior | Repository constraint |
|---|---|---|
| Camera movement is reviewable data | Closed, timed view-state array with deterministic identity. | Fixture validation only; no playback or renderer handle. |
| Scene and historical scope stay explicit | One scene ref and ordered valid-time anchor. | References are declarations, not resolved evidence or release state. |
| Motion cannot hide truth | Discrete reduced-motion mode, 2D fallback, autoplay off, outcome independent of playback. | A green fixture is not accessibility proof. |
| Evidence stays attached | Ordered evidence-reference list. | Validator does not resolve or authenticate evidence. |
| Globe/3D paths remain governed | Projection is declared per state. | No 3D or plugin admission is evaluated or authorized. |

## Path decision

~~~yaml
path_decision:
  artifact: CameraPathCandidate
  proposed_path: contracts/ui/camera_path.md
  artifact_kind: semantic contract
  authority_owner: renderer-neutral camera-path candidate meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: ui
  scope_id: camera-path
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/architecture/ui/ACCESSIBILITY.md
    - contracts/ui/view_registry_profile.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

Any runtime adapter, scene registry, policy, admission rule, playback control,
release object, or published story requires a separately reviewed change.

## Non-effects

This packet does not select a renderer, accept ADR-0007, create a MapLibre
runtime home, execute camera motion, resolve a scene or evidence bundle,
evaluate policy, admit 3D or plugins, alter a registry, approve review, release,
deploy, publish, or authorize public use.
