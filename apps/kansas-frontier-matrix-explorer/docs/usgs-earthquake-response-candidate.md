<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/explorer/usgs-earthquake-response-candidate
title: USGS earthquake response decoder candidate
type: note
version: v0.1.1
status: proposed; review-pending; no-live-activation
owners: ["@bartytime4life"]
created: 2026-09-22
updated: 2026-09-23
policy_label: public; context-only; no-source-admission; no-release
responsibility: Document the app-local USGS no-data decoder candidate, caller duties, offline tests, and held live integration.
owning_root: apps/
current_path: apps/kansas-frontier-matrix-explorer/docs/usgs-earthquake-response-candidate.md
truth_posture: CONFIRMED bounded source inspection; PROPOSED integration; NEEDS VERIFICATION hosted acceptance
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_commit: 0305c98702cb7b48dfaa9598b3625cb027860855
[/KFM_META_BLOCK_V2] -->

# USGS earthquake response decoder candidate

**APP-LOCAL CANDIDATE / NO LIVE CALLER / HOSTED INTEGRATION HELD.**

This slice preserves the supplied September 22 repair candidate in the monorepo's
existing application and test homes. The application currently has no live-context
route equivalent to the standalone Site's route. No route, fetch call, source
registration, loader or renderer imports the candidate. Its only consumer in this
change is the test suite. Presence in Git is not a deployed earthquake-feed repair.

## Behavior and limits

[`readUsgsEarthquakeResponse`](../app/usgs-earthquake-response.ts) maps only USGS's
[documented 204 no-data result](https://earthquake.usgs.gov/fdsnws/event/1/) to a new
empty FeatureCollection. Other non-200 statuses fail. Valid 200 outer collections
are preserved; malformed collections, invalid JSON/UTF-8, oversized or broken
streams remain errors. This does not normalize 204 for any other provider.

[`bounded-json.ts`](../app/bounded-json.ts) is preserved byte-for-byte from the
[historical standalone mirror](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/c4e5ebe54cba9d7ca9bbee108b442bdf68763f58/app/bounded-json.ts)
(blob `e990fde4d7d7f64381abff060d12f9c394e9533f`). Its policy is unchanged. Callers must
supply a positive finite byte cap and an independently bounded request/body timeout.
The decoder is not a general network client, media validator, geometry validator,
or evidence-admission boundary. Endpoint/redirect controls, full event identity,
coordinate/time validation and geographic filtering remain caller responsibilities.

The decoder receives a Response; it cannot authenticate its provider. Invoke it
only after a fixed USGS event query, not on arbitrary URLs or other feeds. A future
caller should explicitly request `nodata=204`, reject redirects and unexpected
media types, retain bounded reads under an AbortController deadline, and preserve
the existing query scope. No `nodata=200` fallback is proposed.

## Reproduce locally

From the repository root, using Node.js 22.13 or newer in the supported Node 22 lane:

```bash
node --test apps/kansas-frontier-matrix-explorer/tests/usgs-earthquake-response.test.mjs
```

The test loads the exact candidate TypeScript through Node's built-in type stripping
and rewrites only the module URL for the unchanged bounded reader. Type stripping
is execution, not type checking. The existing application `npm test` glob includes
the new test automatically; package scripts, dependencies and lockfiles are unchanged.

The 36 deterministic tests require no provider calls: historical missing-body
reproduction; specific 204 conversion; generic-reader refusal; empty/populated
200; sequential decoder outputs and independent arrays; HTTP errors; malformed
collections; empty/HTML bodies; declared/streamed byte limits; invalid UTF-8;
stream failure; and a fetch-denial check. Fixture events are synthetic and test-only.
The sequential decoder test is not proof that map geometry or selection clears.

## Validation boundary and next integration

Local focused tests and strict TypeScript checks of the two candidate files are
recorded in the generated receipt and PR body. Full application build, existing
suite, exact-head hosted CI, independent review, real USGS responses and authenticated
Site/WebGL acceptance are separate checks. Do not inherit the supplied archive's
old test counts as new-head evidence without rerunning.

Before porting, obtain the exact current hosted source and saved predecessor.
The [monorepo boundary](../README.md) and [Site alignment record](sites-source-alignment.md)
prohibit substituting the historical standalone root for current main or current
Site. Apply the decoder at the fixed active caller only after review; test route
status/envelopes, malformed/timeout/error outcomes and populated -> empty -> populated
map/selection replacement. Show query window and retrieval time independently from
last event time. No-data is not an all-clear.

Main/source mirror refs, Site identity/audience/bindings, terrain, radar, smoke,
source admission, policy, topology, release, deployment and publication are unchanged.
Keep #4024 containment and #4228 authority boundaries; draft creation is not ready or
merge authorization. Roll back this unintegrated candidate by abandoning its branch
or a reviewed inverse of these added files after integration, preserving the receipt
as historical process memory. Do not change the live Site to undo a local candidate.
