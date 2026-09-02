# Headless render review packet

This inactive, fixture-only continuation partially implements Pass 32 card `KFM-P32-PROG-0016`. A dedicated headless Chromium scenario reuses the existing synthetic mobile PMTiles verification surface, captures a screenshot, records bounded render metrics, emits a digest-bound sidecar, validates the three-file packet, and uploads it as a short-lived CI review artifact.

The packet is deliberately narrower than the source card. It loads the existing 347-byte synthetic PMTiles fixture through the admitted in-memory verification/decode/canvas adapter. It does **not** fetch or load a published PMTiles carrier, boot MapLibre, evaluate style health, verify a cryptographic signature, authorize release, deploy, publish, or establish public-use readiness. Metrics and sidecars therefore retain `SYNTHETIC_FIXTURE_ONLY`, `PROPOSED_INACTIVE`, `NOT_EVALUATED`, and `authority: NONE` markers.

The pure TypeScript builders own the exact metrics and sidecar shapes. The Playwright scenario owns browser observation and temporary file emission. The PMTiles validator owns bounded packet replay. GitHub Actions owns orchestration and short-lived QA upload; the uploaded artifact is review convenience, not repository proof or a release carrier.

The output directory contains exactly:

- `headless-render.png` — a full-page screenshot of the synthetic fixture surface;
- `metrics.json` — mobile viewport, archive/tile size, pixel, timing, request-count, and explicit hold observations;
- `sidecar.json` — SHA-256 bindings for the screenshot and metrics plus the same authority holds.

Rollback is a focused revert of the additive builder, tests, validator, workflow, source map, documentation, and generated receipt. No live source, published carrier, style, registry, policy, release, deployment, or publication state exists to unwind.
