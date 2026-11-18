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

## Outage message (all live-context feeds)

A feed failure answers with HTTP 503 and a JSON sentence saying what is unavailable, what cannot
be inferred and when the provider is checked next. The site's host replaces the body of a 502 or
504 with its own "error code" page, so those statuses hid the sentence; the cause (error or
timeout) is kept in the `X-KFM-Upstream-Failure` header. The layer card and the Status tab show
the sentence; any other failure keeps the generic "Could not load source data" text.

## National Register places use the same counted circles (2026-11-16)

The National Register of Historic Places layer has 1,344 public markers, which piled up in
Wichita, Topeka, Lawrence and Kansas City at statewide scale. Nearby markers are now counted in
one numbered circle that splits on zoom; past zoom 12 every marker sits at its own point with
its name, styled as before.

- A light ring marks a circle that holds a National Historic Landmark.
- Hovering a circle gives its makeup, for example "142 National Register markers in this area ·
  129 buildings · 5 districts · 1 site · 7 structures". Selecting it zooms to where it splits.
- The count is markers, not listings: a listing such as a district can publish several points.
- The feed, its fields and its limits are unchanged. `app/context-clusters.ts` holds the cluster
  settings and the per-source summary used for both bridges and National Register places.

## Trail sites use the same counted circles (2026-11-18)

The trail-sites layer has about 96 public markers. Most sit where the trails leave the Missouri
River, so at statewide scale dozens overlapped around Kansas City. Nearby sites are now counted
in one numbered circle that splits on zoom; from zoom 10 every site sits at its own point with
its name, styled as before.

- Hovering a circle gives its makeup, for example "14 trail sites in this area · 7 NPS-certified ·
  Santa Fe 9 · Oregon 6 · California 7". Selecting it zooms to where it splits.
- A site on a shared corridor counts toward each trail it names, so the trail numbers can add up
  to more than the number of sites.
- The feed, its fields and its limits are unchanged.
