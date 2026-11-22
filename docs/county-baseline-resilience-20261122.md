# County outlines: one good answer kept, one retry (2026-11-22)

The county outlines (`/api/live-context?feed=census-counties`) and the FEMA declarations feed, which
locates declarations on the same outlines, both read the Census TIGERweb 2020 county layer. It is
a pinned decennial baseline: the same 105 outlines, populations and housing counts every time.

## What went wrong

Just after the publication verified on 2026-11-22, five of nine requests for the county feed
returned 503 "This operation was aborted" after about 18 seconds, and the FEMA feed did the same
once. In the same minutes the Census query hung for 40 seconds on one of three direct requests and
answered the other two in half a second.

The server asked Census afresh on every request that reached it, with a single attempt and an
18-second limit. A cache in front of the server hides that most of the time; after a restart, or
whenever a request gets through, one hung Census connection became a visible failure.

## What changed (`app/county-baseline.ts`)

- **One good answer is kept for a day.** That is the lifetime the feed already declares
  (`s-maxage=86400`). Census is not asked again until the day is up. The answer is returned as it
  was received, with its original retrieval time.
- **Requests that arrive together share one read.** On a cold start the county layer and the FEMA
  feed no longer each open their own Census request.
- **A failed attempt is tried once more.** The first attempt gets 7 seconds and the second 11, so
  the total stays inside the 18 seconds a single attempt used to get.
- **When the day is up and Census cannot be reached**, the kept answer serves for one more day,
  the feed's existing `stale-while-revalidate` window. After that the failure is reported as before.

## What did not change

- No substitute data. Everything served is an answer Census gave for this exact query; nothing is
  bundled, estimated or filled in. If Census has never answered since the server started, the feed
  fails with the same 503 and the same message as before.
- A failure is never remembered: the next request tries Census again.
- An incomplete answer (not exactly 105 valid Kansas counties) is still refused.
- The response body, headers and cache lifetimes of both feeds are unchanged.

## Tests

`tests/county-baseline.test.mjs` covers the kept answer and its expiry, the retry and its time
limits, two failures being reported, an incomplete answer being refused twice, shared reads,
separate editions, the stale window and its end, and that the windows match the feed's headers.
