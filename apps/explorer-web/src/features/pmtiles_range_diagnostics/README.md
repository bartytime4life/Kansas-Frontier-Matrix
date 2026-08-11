# PMTiles range diagnostics

Status: **PROPOSED, fixture-only, read-only Explorer feature**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0013` into a bounded diagnostic panel over the existing no-network PMTiles partial-read verification work. It makes Range support, Content-Range, ETag, cache state, sidecar binding, structural checks, unresolved holds, and a headless-render result visible without declaring the artifact healthy.

The only detailed outcome is `ANSWER / DIAGNOSTICS_AVAILABLE` with `verification_state: STRUCTURAL_HOLD`. The projection requires the exact current compatibility checks and unresolved holds. It deliberately accepts only `cryptographic_state: UNVERIFIED`; a projection that claims cryptographic verification is malformed and renders nothing.

The component does not fetch an archive, issue a Range request, read a lifecycle store, verify a signature, run a renderer, execute policy, mark an artifact healthy, mutate a cache, or authorize release or publication.

## Validation

```bash
npm --prefix apps/explorer-web test -- pmtiles-range-diagnostics.test.ts
npm --prefix apps/explorer-web run build
npm --prefix apps/explorer-web run test:e2e -- pmtiles-range-diagnostics.spec.ts
```

A green result proves only closed projection parsing and synthetic browser rendering. It does not prove a live endpoint, archive, sidecar, signature, cache, policy result, release, or public artifact.
