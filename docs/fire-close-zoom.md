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
