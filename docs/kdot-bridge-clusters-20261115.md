# KDOT bridges as counted clusters (2026-11-15)

The five bridge layers under Map layers → Roads, rail & bridges used to be images drawn by
KDOT's map service. At statewide scale about 24,900 dots overprinted each other and could only
be shown from zoom 8. They are now read as records and drawn by the Explorer.

## What a visitor sees

- **Numbered circles** count the bridges in an area. Selecting one zooms to where it splits.
  Hovering shows what it holds: the earliest recorded build year, the longest bridge, and how
  many are recorded closed or posted with a restriction.
- **Past zoom 13** every bridge sits at its recorded point, labelled with what it crosses and
  its build year. A bridge that is not near another is never merged, at any zoom.
- **Colour** is the recorded build year in seven eras; a numbered circle uses the average year
  of its bridges. Grey means no year is recorded. **Size** grows with recorded length.
- **Ring**: red is recorded closed to all traffic, amber is posted with a restriction. A
  numbered circle has a red ring when it holds a closed bridge.
- **Selecting a bridge** opens its KDOT record: what it carries and crosses, county, build and
  rebuild year, material and design, length and spans, lanes, daily traffic, recorded status and
  load posting class, historic designation, recorded condition ratings, sufficiency rating,
  last inspection, owner and structure number. The longest and busiest bridge in each inventory
  are marked.
- The layer status text states the count, longest, busiest and earliest recorded year.

## How it is built

| Part | File |
|---|---|
| Record parsing, the slim map record, the full detail record, summaries and colours | `app/kdot-bridges.ts` |
| One shared inventory read per network (state, local), kept for a day, with outage backoff | `app/api/live-context/kdot-bridges.ts` |
| Five feeds on the existing route: `/api/live-context?feed=kdot-bridges-…` | `app/api/live-context/route.ts` |
| Full record for one bridge id: `/api/bridge-detail?id=kdot-local-123` | `app/api/bridge-detail/route.ts` |
| Clustered MapLibre source and four layers per bridge layer | `app/live-context.ts` |
| Cluster zoom, hover summary and detail loading | `app/page.tsx` |

- The provider is read with two fixed statewide queries (`State_Bridges`, `Non_State_Bridges`),
  paged and capped. No visitor coordinates, filters or provider URLs are accepted.
- The historic, built-before-1950 and closed layers are subsets of the local inventory, chosen
  with the same rules as the earlier provider filters, so four layers share one read.
- The map list is slim (id, name, year, length, status ring): about 1 MB for state bridges and
  3.7 MB for local bridges before compression. Everything else is fetched for the one bridge a
  visitor selects.
- If the provider is down the layer is empty and says when the next check is; the wait doubles
  from 1 to 15 minutes. No earlier copy is shown after a failed refresh.

## Limits

- Points are inventory locations, not deck footprints.
- Build years, status, ratings and inspection dates are KDOT's recorded values and may lag.
  They are not a live closure feed, a structural safety determination or navigation advice.
- Provider rows without a usable point in Kansas are left out and counted in the status text.
- External context only; no KFM dataset is acquired or released.
