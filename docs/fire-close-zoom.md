# Close-zoom fire display

NASA thermal detections retain an animated flame at every zoom. Close views
increase its screen size smoothly, up to 2.1 times the 36 × 48 logical-pixel
image at zoom 17. Its base remains at the provider point. The illustration
faces the viewport in flat, tilted and globe styles rather than flattening
onto a rectangular ground pixel.

Seven unequal translucent flame ribbons, five lighter filaments and four
sparse sparks form a 24-frame loop at approximately 18 frames per second.
Frames use four-times-resolution Canvas images, cache on first use and share
the existing per-map motion ticker. Incident-report symbols reuse the new
artwork with their existing type palette and size behavior.

The former animated ember fill and glowing rectangular edge are removed.
When provider scan and track dimensions are available, a thin, low-opacity
dashed outline still identifies the satellite pixel on the ground. It retains
the existing approximate pass orientation. This is a measurement footprint;
it does not identify a fire perimeter, flame front or burned area.

Flame height, flicker, sparks and apparent brightness are illustrative. They
do not encode radiative power, wind, spread or present activity. The provider
location, acquisition time, confidence, measured attributes, source identity
and Evidence Drawer behavior remain unchanged. A thermal anomaly can be a
non-vegetation heat source. The source boundary and generated AI knowledge
catalog explain the representation.

## Validation and limits

- Nine focused fire tests passed, including actual MapLibre expression
  evaluation for close-zoom growth/capping, source identity, clearing,
  opacity, report symbols, shared motion, reduced motion and hidden tabs.
- Changed-module TypeScript and ESLint passed. The deterministic knowledge
  pack regeneration/check passed; its only semantic change is this display's
  boundary text.
- All 24 frames executed through a recording Canvas context. Five sampled
  frames were visually inspected using Cairo rasterization of the actual
  paths and gradients; this does not reproduce browser shadows or qualify
  the integrated MapLibre rendering.
- Full application build, complete suite, integrated browser/device
  acceptance and live publication remain unverified locally. The available
  checkout predates the hosted source; the candidate uses fetched hosted
  modules in isolation. Connected browser policy blocked a local-file
  preview, so no browser acceptance is claimed.

The changed runtime/test files retain their existing standalone application
owners; this document uses the existing docs root and the generated receipt
uses the existing provenance lane. No new runtime, data, dependency, source
admission or storage authority is introduced (ADR-0029).

Rollback: revert the complete visual change, including source boundary,
generated knowledge pack, test and provenance updates. No data migration is
required.

## Checked image fallback and browser acceptance follow-up — 2026-10-23

PR #5441 has merged into the hosted branch. This follow-up retains its artwork
and source boundaries; it completes the missing-image fallback and adds a
repeatable browser matrix rather than creating another renderer.

Provider circles are suppressed only when every confidence image is actually
registered. Missing Canvas, denied pixel readback, throwing or incomplete
image registration keep confidence-coloured detection points and the original
incident-type markers visible at their exact provider locations. The fallback
radius stays bounded at close zoom. Successful later registration or a style
reload can restore flames. Hidden or zero-opacity layers retain those settings,
and unavailable images do not start a repaint ticker. Generic layer styling
cannot overwrite the renderer's visibility or continually reset its radius.

The ordinary regression suite adds unavailable Canvas, ordinary-Canvas fallback,
readback denial, partial and silent registration failure, recovery, style reload
and no-animation-without-images coverage. Existing source-identity, confidence,
footprint dimensions, opacity, globe sizing and motion gates remain exercised.

`tests/fire-display.browser.mjs` bundles the actual renderer, live-context source
registry and pinned MapLibre runtime into a **test-only component scene**. It
uses synthetic points and a synthetic constant-height DEM, blocks off-origin
HTTP, and creates no production route or provider observations. The matrix
captures desktop and phone viewports at zooms 4, 8, 10, 12, 14, 17 and 20, plus
pitched terrain, pitched globe, globe overview, light background, reduced
motion, opacity zero and image-atlas fallback. It checks real rendered-feature
queries against original source IDs and separately clicks both synthetic source
types in the hydrated Explorer to inspect the actual Evidence Drawer, including
when both Canvas 2D implementations are unavailable. A pinned pre-redesign renderer can be
supplied through `KFM_FIRE_BASELINE_FILE` for matching zoom 8/12/14 screenshots.
The workflow supplies commit `1000a5c4521bb3055e3863110754e924cdda801e` and uploads
`fire-renderer-visual-comparison` artifacts. These are illustrative fixtures,
not acceptance of live fire data or measured terrain.

The cloud browser cannot reach the local workspace listener. Local browser
execution is therefore not claimed. Exact-head CI execution, screenshot review,
full Explorer Evidence Drawer results, physical phones and real provider terrain
must be distinguished from component acceptance. Keep the follow-up
in draft and do not qualify it for publication until the outstanding browser
checks and visual comparison have been reviewed. No publication or deployment
is performed by this change.

All work stays within the existing standalone runtime, tests, workflow and docs
owners under ADR-0029. Roll back this follow-up to restore the prior fallback;
reverting PR #5441 separately restores the earlier rectangular presentation.

The first CI run passed build, TypeScript, all 1,728 ordinary tests and
disposable MySQL checks. Its new browser test caught a fixture-diagnostic bug:
it asked fill/line layers for circle opacity. That test helper is corrected;
the failed run is not counted as browser acceptance. A further style-replacement
regression checks that absent layers cause no visibility writes.
