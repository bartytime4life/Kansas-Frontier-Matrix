# API and UI Surfaces

## API boundaries

- Public and steward routes consume released artifacts only.
- API responses must not expose RAW/WORK/QUARANTINE or restricted stores.

## UI boundaries

- MapLibre layers must be public-safe and release-bound.
- Evidence Drawer must show source role, rights, sensitivity, review, and correction context.
- Focus Mode must produce finite decision outcomes and deny exact-location requests for public users.

## Anti-leak requirement

No side channel (tiles, drawer payloads, graph edges, exports) may reintroduce restricted exact geometry.
