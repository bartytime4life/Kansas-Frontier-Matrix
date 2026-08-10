# Promotion gate status board

Status: **PROPOSED, fixture-only, read-only Explorer feature**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0014` into a bounded reviewer-facing board. It displays projected states for exactly six components named by the source card: source monitor, scorecard, schema validator, OPA decision, attestation, and release-manifest candidate.

The board is a display projection, not a replacement for any governing object. It requires fixed component order, exact state/reason pairing, unique opaque artifact references, recomputed state counts, and a board state derived as `ERROR > DENY > HOLD/NOT_RUN > READY_FOR_REVIEW`.

Even `READY_FOR_REVIEW` is not approval. The projection fixes source-monitor execution, validator execution, policy evaluation, attestation verification, authenticated review, promotion, release, and publication authority to false. The component has no action controls.

## Validation

```bash
npm --prefix apps/explorer-web test -- promotion-gate-status-board.test.ts
npm --prefix apps/explorer-web run build
npm --prefix apps/explorer-web run test:e2e -- promotion-gate-status-board.spec.ts
```

A green result proves only deterministic display-contract parsing and synthetic browser rendering. It does not prove that any referenced artifact exists, that a check ran, or that review, promotion, release, or publication is authorized.
