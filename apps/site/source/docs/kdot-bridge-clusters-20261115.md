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

## Walk-in hunting access gets a counted overview (2026-11-19)

The walk-in hunting access layer has about 3,600 tracts. They are outlines, not points, and at
statewide scale they were pale specks that gave no sense of how much land is enrolled where.
Below zoom 8, numbered circles now count the tracts in an area; from zoom 8 only the tracts
themselves are drawn, as before.

- Hovering a circle gives, for example, "364 walk-in hunting tracts in this area · 104,097
  recorded acres · 9 archery-only". Selecting it zooms in one step toward the tracts.
- The acres are the sum of KDWP's recorded acres for those tracts, not a measured area.
- The circles come from a second, display-only map source with one point per tract, placed at
  the middle of the tract's extent. Each point carries only the tract's recorded acres and
  whether it is archery-only: no name, contract reference or note. `app/context-clusters.ts`
  builds it; the tract feed, its fields and its limits are unchanged.
- The tract outlines stay on the map at every zoom, so a single tract can still be selected
  anywhere. The circles follow the layer's opacity slider and read more strongly than the tract
  fill at the same setting.

## What is in this view (2026-11-21)

Every layer drawn as numbered circles — the five bridge layers, National Register places, trail
sites and walk-in hunting access — now says what the map holds right now. With the layer on, its
row under Map layers → On map reads, for example:

> **307 of 19,291 bridges in this view**
> Earliest recorded build year 1900 · longest 3,376 ft · 60 posted with a restriction

- The count is exact. It is taken from the layer's own records inside the map's extent, not from
  the circles, so it does not depend on how the circles happen to group at that zoom.
- The second line uses the same facts and wording as a numbered circle, for everything in view.
- It recounts when the map stops moving. It is not announced to screen readers on every pan.
- When nothing is in view it says how far and in which direction the nearest record is from the
  middle of the map, with a **Go to the nearest** button that moves the map there at the same zoom.
- A hunting tract counts where the middle of its outline falls, as the overview circles do.
- The extent is the whole map, including any part under an open panel, and on a tilted map it is
  the box around what is visible. It is not shown on the globe.

### Go to what stands out

Under the row line, up to two buttons take the map to a record the facts mention:

| Layer | Button |
| --- | --- |
| Bridges | **Show the oldest (1938)** and **Show the longest (3,376 ft)** |
| National Register places | **Show the National Historic Landmark**, or **Show one of 9 National Historic Landmarks** |
| Walk-in hunting access | **Show the largest tract (8,166 acres)** |

- Only records inside the current view are offered, so each press narrows toward something the
  visitor was already looking at. The line then recounts for the new view.
- A tie is called a tie: when several bridges share the earliest recorded year the button reads
  "Show one of 8 from 1955", not "the oldest". Years outside 1800-9998 are ignored, as on the circles.
- The map moves to the record and zooms in only as far as needed for it to stand apart from its
  neighbours (14.5 for a bridge, 13.5 for a Register marker, 12 for a tract). It never zooms out.
- Trail sites have no such button, and neither does a view holding a single record or none.
- The button does not select the record or open its details. The record is at the middle of the
  map, and selecting it works as before.

### In the status bar too

The same counts also sit in the status bar at the bottom of the map, after the map's name, so they
stay in sight while panning with the Layers panel closed:

> Kansas Overview · Kansas statewide · In view: 305 local bridges · 90 Register markers

- One short phrase per counted layer that is on, in a fixed order, up to three; beyond that it
  says how many more layers there are.
- Layers are never added together. Three of the bridge layers (historic, pre-1950, closed) are
  parts of the local list, so each keeps its own name and count.
- It follows the same rules as the row line: exact counts, recounted when the map stops, not
  announced on every pan, not shown on the globe. It is dropped below 760 px, where the bar has
  room only for the map's name.

Code: `app/view-tally.ts` (counting and wording), `app/view-tally-line.tsx` (the row line and the
status-bar line), mounted in `app/page.tsx`. Tests: `tests/view-tally.test.mjs`.
