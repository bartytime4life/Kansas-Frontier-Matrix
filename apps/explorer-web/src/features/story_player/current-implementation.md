# Story Player current implementation

**Status:** PROPOSED / bounded consumer slice / no live route / no publication authority  
**Base:** `main@3ea2ab5701074168b0dab32e94dccae8dbcc0d4f`

This note records the first executable Story Player slice under the existing `apps/explorer-web/src/features/story_player/` responsibility boundary. It does not supersede the feature README or StoryManifest contract.

## Confirmed in this slice

`index.tsx` now consumes one already-governed `kfm.ui.story-manifest.public-safe.v1` projection and produces a bounded Story Player view model. Playback is enabled only when the manifest declares `READY / ANSWER`, `authoritative=false`, `projection_only=true`, and the existing StoryManifest trust/support posture is fully public-safe: cleared rights, public sensitivity, allowed policy, reviewed state, released support, current freshness, non-superseded correction posture, and non-empty evidence, citation, policy, release, and review references.

For `ABSTAIN`, `DENY`, `ERROR`, stale, unreleased, superseded, malformed, or otherwise non-playable projections, node playback is withheld. The consumer is 2D-only and carries public-safe evidence/citation references for later governed UI handoff.

Focused Vitest coverage lives at `apps/explorer-web/tests/story-player.test.ts` and exercises READY, stale/unreleased, denied rights/sensitivity, upstream error, supersession, malformed boundary flags, duplicate/unsorted constituents, missing governed response, and anti-bypass source checks.

## Explicit non-effects

This slice does not:

- fetch a StoryManifest or StoryNode;
- read `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, or `data/published` from the browser;
- resolve EvidenceRefs or EvidenceBundles;
- execute policy, review, promotion, release, correction, or rollback;
- render a map or import MapLibre/Cesium/model clients;
- expose a live route or connect the feature to Explorer navigation;
- dereference StoryNode bodies;
- author or publish a story;
- create truth, evidence, policy, review, release, deployment, or publication authority.

The StoryManifest contract/schema/validator remain the machine authority for the fixture profile. This app-local consumer performs defensive checks only and must not be represented as a replacement schema validator.

## Directory Rules basis

The existing Story Player README and adopted Directory Rules place app-local playback/composition code under `apps/explorer-web/src/features/story_player/`; app unit proof belongs under the existing `apps/explorer-web/tests/` lane. No schema, contract, policy, release, source, registry, proof, or lifecycle authority is relocated or duplicated.

## Still needs verification

Live governed-API StoryManifest transport, route wiring, StoryNode resolution, Evidence Drawer integration, map/time continuity, accessibility interaction behavior, telemetry emission, Story policy execution, released-story discovery, browser playback, 3D handoff, and public deployment remain **NEEDS VERIFICATION**.

## Rollback

Revert the Story Player implementation/test/documentation commits. No external state, source activation, release, deployment, publication, cache, or data migration is created by this slice.
