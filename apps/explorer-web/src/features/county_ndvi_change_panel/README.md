# County NDVI change panel

Status: **fixture-first Explorer component; not production-wired**.

This feature adapts Pass 32 cards `KFM-P32-FEAT-0005` and
`KFM-P32-IDEA-0011` into a read-only county NDVI candidate panel. It displays
the source-requested baseline window, recent window, candidate delta threshold,
changed-area percentage, cluster count, and evidence state without acquiring
any analytical, policy, release, or publication authority.

## Projection boundary

The app-local profile `kfm.explorer.county-ndvi-change.fixture.v1` accepts one
synthetic Kansas county scope, non-overlapping UTC windows, internally coherent
NDVI millionths, a bounded changed-area ratio and cluster count, and two
digest-bound upstream references. Candidate classification is recomputed from
the declared medians, delta, and threshold. Unknown fields, incoherent
arithmetic, mutable references, overlapping windows, or authority overreach
fail closed and render nothing.

`REFERENCED_NOT_RESOLVED` is the only accepted evidence state. The panel makes
the evidence gap visible; it does not upgrade references into an EvidenceBundle
or a supported environmental claim.

## Authority boundary

The panel does not fetch STAC/HLS assets, open raster bytes, calculate NDVI,
aggregate counties, detect clusters, resolve evidence, evaluate policy,
interpret environmental conditions, mutate lifecycle state, promote, release,
deploy, publish, or authorize public use. Negative outcomes carry no county,
metric, or reference detail.

## Placement

- `apps/explorer-web/src/adapters/` owns strict app-local parsing.
- `apps/explorer-web/src/features/county_ndvi_change_panel/` owns fixed display
  behavior.
- `fixtures/ui/county_ndvi_change_projection/` owns synthetic display packets.
- `apps/explorer-web/tests/` owns unit and browser proof.

These are established responsibility roots under accepted ADR-0029 and
Directory Rules v2. The county remains a composition scope, not a domain or
root, and the existing NDVI computation and vegetation-connectivity semantics
are referenced rather than copied.

## Production hold

Production wiring remains **HOLD** until a reviewed governed API can emit this
exact projection from accepted upstream computations and resolvable evidence.
The browser must not ingest RAW/WORK/QUARANTINE data, raster payloads, or
internal analytical objects directly.

## Validation

```text
pnpm --filter explorer-web exec vitest run tests/county-ndvi-change-panel.test.ts
pnpm --filter explorer-web exec playwright test --config=playwright.config.ts tests/browser/county-ndvi-change-panel.spec.ts
pnpm --filter explorer-web build
```

## Rollback

Revert the adapter, feature, fixtures, tests, source map, and authoring receipt
together. This additive component creates no source, evidence, policy,
lifecycle, promotion, release, deployment, publication, or public-use state.
