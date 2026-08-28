<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/time-bucket-playback-manifest-source-map
title: Time-Bucket Playback Manifest Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · UI steward · Temporal steward · Accessibility steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: Reconcile the connected April 16 playback idea and Full Atlas time-bucket triad to current repository authority.
truth_posture: CONFIRMED source reading and current-main comparison / PROPOSED bounded adaptation / NEEDS VERIFICATION human and hosted review
related:
  - ../../../contracts/ui/time_bucket_playback_manifest.md
  - ../../../contracts/ui/camera_path.md
  - ../../../contracts/runtime/verified_rendering_resource_envelope.md
  - ../new-ideas-4-16-source-map.md
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
tags: [kfm, intake, ui, temporal, playback, map, atlas]
[/KFM_META_BLOCK_V2] -->

# Time-Bucket Playback Manifest Source Map

## Source basis

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Connected Google Doc `New Ideas 4-16-26`, inspected 2026-08-10 | Proposes lightweight same-source filtering, coarse epoch source swaps, off-main-thread bucket preparation, digest computation, active-window/cadence display, and numeric time fields. | Dated ideation packet; included renderer snippets and a peer-renderer suggestion that are not repository authority. |
| Full Atlas `KFM-TRIAD-039` / `KFM-CAND-0115..0117` | Recasts filters, epoch buckets, PMTiles, workers, animation windows, and camera transitions as downstream carriers; proposes `TimeBucketManifest`, temporal envelopes, digests, release refs, worker schemas, gaps, fallbacks, and trust-preserving tests. | `PROPOSED` gap-fill family, not an accepted runtime design. |
| Repository April 16 source map | Identifies digest-bound manifests and time-kind-safe UI/API handoffs as the non-duplicate gap. | Exploratory reconciliation only. |

No source bytes, external URLs, real coordinates, restricted records, renderer
code, or peer-renderer dependency is transferred.

## Current-main reconciliation

GitHub open work and local `main@149af17075f7f12d716aa14de439ea22ee6a343e`
were inspected on 2026-08-10. Exact searches found no open pull request,
`TimeBucketManifest`, `TemporalFilterEnvelope`, or executable bucket
manifest packet.

| Existing family | Confirmed responsibility | Retained boundary |
|---|---|---|
| `CameraPathCandidate` | Fixture-only timed camera states and accessibility alternatives. | No artifact bucket selection or time-field binding. |
| `StoryManifest` and Time Banner doctrine | Story and temporal-display vocabulary. | Prose/shape does not validate bucket closure or worker handoff. |
| `VerifiedRenderingResourceEnvelope` | Fixture-only resource and verify-before-render declaration. | Referenced here; not resolved or reimplemented. |
| PMTiles/release integrity families | Artifact identity and release concerns. | This manifest consumes only declared released refs and never verifies or releases them. |

Open reveal-session and denial-explorer PRs were also checked; their governed UI
responsibilities and paths are disjoint.

## Bounded adaptation

| Source pressure | Retained behavior | Safety correction |
|---|---|---|
| Fast scrubbing and epoch swaps | Per-bucket transport hints and derived selection mode. | No renderer or worker code executes. |
| Worker-prepared manifest | Closed message profile, required digest, released refs only. | Raw payloads and unverified URIs are forbidden. |
| Temporal clarity | One time kind/field, half-open intervals, explicit gaps, cadence, precision, freshness, and correction cutoff. | Filters remain carriers rather than truth. |
| Smooth playback | Ordered buckets and safe swap fallback. | Autoplay/loop are off; reduced motion is discrete; no interpolation over gaps. |
| Evidence continuity | Ordered evidence and release references per bucket. | References are declarations, not resolved proof. |

## Path decision

```yaml
path_decision:
  artifact: TimeBucketPlaybackManifestCandidate
  proposed_path: contracts/ui/time_bucket_playback_manifest.md
  artifact_kind: semantic contract
  authority_owner: renderer-neutral temporal playback interaction meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: ui
  scope_id: time-bucket-playback
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - contracts/ui/camera_path.md
    - contracts/runtime/verified_rendering_resource_envelope.md
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
```

Renderer selection, adapter implementation, worker execution, live artifacts,
policy, evidence resolution, release, deployment, and public playback remain
separate future decisions.
