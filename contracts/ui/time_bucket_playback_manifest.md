<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/ui/time-bucket-playback-manifest-candidate
title: Time-Bucket Playback Manifest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; inactive; review-pending; fixture-only; non-authoritative
owners: OWNER_TBD — UI steward · Map runtime steward · Temporal steward · Accessibility steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; ui; temporal; playback; fixture-only
owning_root: contracts/
responsibility: Define a renderer-neutral, digest-bound carrier manifest for governed map time-bucket playback.
truth_posture: PROPOSED source-grounded adaptation / CONFIRMED deterministic fixture validation / no runtime, evidence, policy, release, or publication authority
related:
  - ./camera_path.md
  - ./story_manifest.md
  - ../runtime/verified_rendering_resource_envelope.md
  - ../../schemas/contracts/v1/ui/time_bucket_playback_manifest.schema.json
  - ../../docs/intake/exploratory/time-bucket-playback-manifest-source-map.md
tags: [kfm, ui, temporal, time-bucket, playback, map, accessibility, fixture-only]
notes:
  - "Temporal filters and bucket transports are downstream carriers, never valid-time authority or evidence."
  - "A valid manifest is reviewable metadata, not executable playback."
[/KFM_META_BLOCK_V2] -->

# Time-Bucket Playback Manifest Candidate

A `TimeBucketPlaybackManifestCandidate` declares an ordered set of
digest-bound, released-artifact buckets for a renderer-neutral map playback
surface. It keeps the selected time kind, active window, cadence, precision,
freshness, gaps, evidence, accessibility posture, and transport choice visible
without turning a filter, PMTiles source, Web Worker, or animation into temporal
authority.

## Required semantics

A candidate must:

- select exactly one closed time kind and its corresponding source field;
- bind the playback window to ordered half-open bucket intervals;
- give every bucket a deterministic identity, artifact digest, release
  reference, ordered evidence references, and transport hint;
- make every real gap explicit and reject overlaps or invented continuity;
- derive `FILTER`, `SWAP`, or `HYBRID` selection mode from bucket hints;
- constrain worker messages to digest-bound released references without raw
  payloads or unverified URIs;
- expose active window, cadence, time kind, precision, freshness, bucket
  identity, gaps, reduced-motion state, and evidence links;
- disable autoplay and looping, provide discrete reduced-motion steps, and make
  outcomes independent of playback; and
- remain fixed-false for runtime execution, worker execution, fetches, integrity
  claims, evidence resolution, policy, release, deployment, publication, and
  public use.

## Carrier, time, and evidence boundary

`filter_time_kind` names which clock the player filters. It does not declare
that clock correct. Each bucket repeats the exact matching field so mixed-clock
playback fails closed. Artifact and release references declare inputs but are
not resolved or verified by this profile. The referenced
`VerifiedRenderingResourceEnvelope` is likewise not recomputed here.

Buckets use `[start_inclusive, end_exclusive)` intervals. A gap must be shown,
paused, or disable playback; interpolation is deliberately absent. A source
swap failure retains only the last verified view or stops with an unavailable
state.

## Finite validation outcomes

| Outcome | Meaning | Non-effect |
|---|---|---|
| `PASS / REVIEW_REQUIRED` | Shape, identity, time-kind, ordering, gap, transport, and boundary checks pass. | Candidate remains inactive. |
| `DENY` | A schema, identity, temporal, release-reference, evidence-order, or authority invariant fails. | No partial playback is executed. |
| `ERROR` | Input cannot be boundedly read or parsed. | No candidate values are trusted. |

## Relationship to adjacent families

| Existing family | Responsibility retained |
|---|---|
| `CameraPathCandidate` | Declares camera motion; it does not select temporal artifacts or validate buckets. |
| `StoryManifest` | Declares story structure; it does not become bucket-time authority. |
| `VerifiedRenderingResourceEnvelope` | Owns bounded verify-before-render resource posture; this manifest references, but does not verify, it. |
| Release and evidence families | Own artifact release and evidence truth; declared references are not proof. |

## Directory Rules basis

Renderer-neutral playback interaction meaning belongs in `contracts/ui/`;
machine shape in `schemas/contracts/v1/ui/`; synthetic examples in
`fixtures/contracts/v1/ui/`; deterministic validation in
`tools/validators/ui/`; tests in `tests/validators/ui/`; source
reconciliation in `docs/intake/exploratory/`; read-only orchestration in
`.github/workflows/`; and authoring provenance in
`data/receipts/generated/`.

No `contracts/maplibre/`, runtime adapter, renderer package, policy root, or
release authority is created.

## Validation

```bash
python -m unittest -v tests.validators.ui.test_time_bucket_playback_manifest
python tools/validators/ui/validate_time_bucket_playback_manifest.py --fixtures
```

## Rollback

Revert the additive fixture-only packet. No runtime, worker, data, cache,
artifact, release, deployment, or public state requires restoration.
