# Source availability watchlist

Status: **PROPOSED, fixture-only, read-only Explorer feature**.

This feature adapts Pass 32 card `KFM-P32-FEAT-0016` into a bounded display surface over a public-safe projection of the existing `SourceAvailabilityWatchlist` aggregate. It distinguishes stable source availability, material schema/content changes routed to a separately referenced candidate, unresolved holds, and assessment errors.

The adapter accepts only a closed projection with:

- `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- fixed outcome/reason-code pairing;
- canonical timestamps and opaque KFM references;
- lexically ordered, unique source entries;
- exact stable/review/hold/error counts;
- candidate-work references only for `REVIEW_CANDIDATE`; and
- fixed-false network, source-activation, candidate-execution, lifecycle-write, authority, release, and publication flags.

The component is text-first and non-interactive. It does not fetch a source, read RAW/WORK/QUARANTINE or another lifecycle store, resolve health/materiality assessments, create or execute work, evaluate policy, mutate repository state, or authorize promotion, release, deployment, or publication.

## Validation

```bash
npm --prefix apps/explorer-web test -- source-availability-watchlist.test.ts
npm --prefix apps/explorer-web run build
npm --prefix apps/explorer-web run test:e2e -- source-availability-watchlist.spec.ts
```

A green result proves only deterministic projection parsing and browser rendering against synthetic fixtures. It does not prove live source health, current materiality, policy approval, review, release, or public fitness.
