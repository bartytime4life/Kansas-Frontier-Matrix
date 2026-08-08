# Mobile PMTiles verification fixture

## Goal

Provide the smallest browser-facing continuation of `ML-Y-111`: verify a
synthetic PMTiles archive and its index/signature-subject/receipt bindings in
memory, extract one PNG tile through a digest-bound range, then decode and
render it under a mobile-emulated viewport.

## Current result

The app-local module
`mobile_pmtiles_verification.ts` accepts an already-bounded fixture packet and
an injected tile-render adapter. It performs no transport and does not import a
renderer. The browser fixture supplies a PNG decoder/canvas adapter and proves
one positive render plus one fail-closed archive-tamper case.

| Surface | Status |
|---|---|
| PMTiles v3 header and metadata | `CONFIRMED` by synthetic tests |
| Archive SHA-256 and PMIDX Merkle binding | `CONFIRMED` by synthetic tests |
| JSON sidecar digests | `CONFIRMED` by synthetic tests |
| PMSIG subject binding | `CONFIRMED` structurally; cryptography remains `HOLD` |
| RunReceipt subject binding | `CONFIRMED` structurally |
| Tile range and tile digest | `CONFIRMED` by synthetic tests |
| PNG decode and canvas render | `CONFIRMED` in mobile-emulated browser test |
| Live MapLibre boot | `HOLD / MAPLIBRE_RUNTIME_UNADMITTED` |
| Policy or release evaluation | `HOLD` |
| Source admission, evidence, promotion, deployment, publication | `DENY` for this fixture |

## Browser boundary

The feature:

- accepts bytes and JSON objects supplied by its caller;
- contains no `fetch`, `XMLHttpRequest`, `WebSocket`, source connector, model
  provider, lifecycle-store, or public endpoint access;
- rejects sidecar drift before tile extraction;
- rejects range or tile-digest drift before decode/render;
- reports finite `PASS`, `DENY`, or `ERROR` outcomes;
- carries `authority: NONE`;
- keeps cryptographic verification, MapLibre runtime admission, and release
  authorization visibly held.

The browser fixture is served only from the local Vite test server. Its
Playwright proof uses a 390 x 844 viewport, device scale factor 3, touch, and
mobile emulation, and asserts that no external request occurs.

## Non-goals

This slice does not:

- install or select `maplibre-gl` or `pmtiles`;
- implement the proposed `@kfm/maplibre` adapter;
- claim a live MapLibre boot;
- verify a cryptographic signature or trust a test key;
- activate a source or admit RAW material;
- create an `EvidenceBundle`, `PolicyDecision`, proof, release manifest, cache,
  deployment, or published map layer;
- certify real-device performance, browser support, hosting Range behavior, or
  offline service-worker behavior.

## Placement

Accepted ADR-0029 keeps app-local map interaction and browser proof under
`apps/explorer-web/`, synthetic PMTiles inputs under `fixtures/pmtiles/`,
cross-language validators under `tools/validators/pmtiles/`, validator proof
under `tests/validators/`, workflow orchestration under `.github/workflows/`,
and generated AI process memory under `data/receipts/generated/`.

## Follow-on gate

The next MapLibre-specific continuation should remain blocked until the
renderer adapter and dependency posture are accepted. That continuation should
replace the injected render adapter with a pinned, governed MapLibre/PMTiles
protocol path while preserving the same archive/index/signature/receipt checks,
mobile budgets, no-external-source test, finite outcomes, and rollback.
