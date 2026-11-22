# Live feeds: one good answer kept for its declared lifetime (2026-11-22)

## What was found

Every feed under `/api/live-context` declares how long its answer is good for, in its `Cache-Control`
header (`s-maxage`, with the same `stale-while-revalidate`): a day for National Register places, the
KDWP layers and the trails, an hour for FEMA declarations, fifteen minutes for fire and smoke, five
for earthquakes, thirty seconds for weather alerts.

Nothing was honouring it. On 2026-11-22 the site's CDN answered every one of these requests with
`cf-cache-status: DYNAMIC`, meaning it did not cache them, and two requests two seconds apart to
twelve of the seventeen feeds came back with two different retrieval times. Each visitor who turned
a layer on sent the server back to the provider: 2.3 MB from KDWP for the hunting tracts, 0.8 MB
from NPS for the Register.

That is slow, it is impolite to the providers, and it means any provider hiccup is a visible
failure. The county outlines showed this the same day (see `county-baseline-resilience-20261122.md`).

## What changed (`app/api/live-context/route.ts`)

- **One good answer per feed is kept in the server for the lifetime the feed declares.** Until it
  is up, requests are answered from it, with its original `retrievedAt`.
- **Requests that arrive together share one provider read.**
- **When the lifetime is up and the provider cannot be reached**, the kept answer serves for the
  declared `stale-while-revalidate` window, then the failure is reported as before.
- **A partial answer is read again within five minutes.** A feed reports `partial` when it withheld
  records, and also when part of a read failed (one trail layer down). The second kind should not
  stand for a day, and the two are not told apart here, so both are refreshed soon.
  In practice National Register places, wildlife areas and FEMA declarations report `partial` as
  a matter of course (they always withhold some records), so they are kept for five minutes
  rather than their declared day or hour. That is still one provider read per five minutes
  instead of one per request. Telling the two kinds of partial apart would let them keep longer.

## What did not change

- **No substitute data.** Everything served is an answer the provider gave to this exact request.
  A feed that has had no answer since the server started fails with the same 503 and message.
- **A failure is never kept.** The next request asks the provider again.
- **No-store feeds are untouched**: DeFlock and the congressional districts declare no lifetime and
  are read as before. DeFlock's rule that an unavailable source leaves the layer unavailable is
  not affected.
- **Bridges and county outlines** already keep their own answers and are left to do so.
- **Dated archive requests** (`day=`) are read every time.
- Response bodies, status codes and headers are the same.
- The answer is kept per server process. A restart, which every publish causes, starts empty.

## Turning it off

Set `KFM_LIVE_CONTEXT_KEEP=off` in the host's environment and restart. Every feed then goes back
to one provider read per request, with no code change.

## Tests

`tests/live-context-kept-feeds.test.mjs` runs the real route against a stand-in provider and a
controlled clock: the kept answer and its expiry, the stale window and its end, a failure not being
kept, the five-minute rule for partial answers, shared reads, archive days and the off switch, and
unchanged headers.

`tests/kansas-discovery-layers.test.mjs` hands the route a different stand-in answer on every call
to test parsing, so it now sets the off switch; its assertions are unchanged.
