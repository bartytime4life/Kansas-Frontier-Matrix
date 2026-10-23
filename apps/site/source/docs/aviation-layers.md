# Airspace, airports and aviation weather

One specialty layer, **Map layers > Airspace, airports & aviation weather**,
draws Kansas airspace as labelled 3D volumes, shows where small drones need
authorization, and ties live airport weather and pilot reports to the airspace
they occur in. It is display context only: **not navigation, flight planning or
UAS authorization**. Temporary flight restrictions (TFRs), NOTAM activations,
UAS Facility Map grid ceilings and live aircraft positions are not shown.

## Sources and clocks

| Data | Source | Clock |
|---|---|---|
| Airspace volumes, public-use airports and runways, airways | FAA NASR 28-day subscription, cycle 2026-10-29, via the pinned `public/data/aviation/kansas-aviation-context.json` | Valid 2026-10-29 up to (not including) 2026-11-26. Before the 29th the layer says it is a *preview* edition; after the 26th it says *expired*. |
| METAR (ASOS/AWOS station weather) | NOAA/NWS Aviation Weather Center Data API via `/api/aviation/metar` | Each station's own observation time; latest within 90 minutes; refreshed every 5 minutes while shown |
| PIREP (pilot reports) | Same API via `/api/aviation/pireps` | Report time; last 3 hours |

The product file is built by
`pipelines/domains/roads-rail-trade/faa_airspace.py` from a NASR-derived
snapshot whose package integrity and data-file SHA-256 digests are recorded in
the file. The browser checks the file's SHA-256 against
`AVIATION_CONTEXT_ASSET` before parsing it, and refuses any shape drift.
Private-use airports (345 in the region) are withheld; only public-use
facilities are drawn or used as nearest-airport references.

## What is drawn

- **Airspace shells (3D).** Each NASR volume is extruded from its floor to its
  ceiling. Class B and C rings stack into the "upside-down wedding cake";
  Class D and Class E surface areas are dashed. Labels follow chart style:
  `CLASS C · ICT · SFC–5,300 MSL`, `R-3602A MANHATTAN · SFC–FL290`,
  `SMOKY MOA · 500 AGL–below FL180`. Groups: Class B/C/D; Class E surface
  areas (E2–E4); Class E 700/1,200 ft floors (E5–E7, off by default); MOA,
  restricted and alert areas. A 1×, 3× or 6× vertical exaggeration is offered
  because true-scale shells are thin at state zoom.
- **Drone slabs, surface to 400 ft AGL.** Red: restricted/prohibited, no flight
  without the using agency's permission (14 CFR 107.45). Amber: controlled
  airspace reaches the ground, so FAA/ATC authorization (LAANC or DroneZone) is
  required (14 CFR 107.41; 49 U.S.C. 44809(a)(5)). Yellow: MOA or alert area
  reaching low altitude, caution. Unshaded is Class G: up to 400 ft AGL without
  ATC authorization (14 CFR 107.51(b)).
- **Airports and runways.** Blue dots are towered, magenta non-towered. Labels
  give the identifier and field elevation; runways draw from their surveyed end
  points at zoom 10+.
- **Airways.** Victor/T routes (1,200 AGL–below FL180) and Jet/Q routes
  (FL180–FL450), labelled with designation and MEA.
- **METAR stations** coloured by FAA flight category (VFR, MVFR, IFR, LIFR);
  **cloud ceilings** as discs at the reported height above each station.
- **PIREPs** as markers at the reported altitude; urgent reports in red,
  turbulence or icing in orange. Reports with a climb/descent phase or an
  unavailable altitude remain in the point inspector, labelled accordingly;
  they are omitted from the altitude layer rather than drawn at ground level.

## The airspace column

**Pick a point on the map** (or click an airport) to list, surface upward,
every band at that spot: NASR volumes plus the regulatory defaults they sit in
(Class G below the lowest controlled floor, Class E from 14,500 MSL, Class A
FL180–FL600, Class E above FL600). Each band lists who may fly there and how
(ATC contact or clearance, equipment, VFR weather minimums, speed limits) with
the 14 CFR section. The panel also gives:

- the drone verdict for SFC–400 ft AGL and the volume that governs it;
- the nearest METAR within 50 km with density altitude, checked against the
  basic VFR minimums for the surface class (14 CFR 91.155);
- airways within 4 NM and pilot reports within 60 km.

## Heights

Source limits keep their reference: MSL, AGL or SFC. Only the drawing converts
them, to height above a stated ground reference: the associated airport's
elevation for Class B/C/D/E2–E4, otherwise the nearest public-use airport
(distance recorded per volume). Kansas terrain varies, so drawn MSL limits can
be off by the difference between that airport and the local ground; the labels
and the column table always show the official values.

PIREP flight levels accept the AWC API's documented digit strings (for example,
`"230"` = 23,000 ft MSL) and numeric values observed in live JSON. `fltLvlType`
keeps climb (`DURC`) distinct from descent (`DURD`); neither defines one fixed
altitude. Missing or malformed levels remain unavailable. Fixed PIREP drawing
heights subtract the nearest public-use airport's elevation, clamp below-ground
results to the surface, then convert feet to metres and apply the selected
exaggeration. This is an approximate display reference, not a measured terrain
or aircraft position. A genuine reported zero is retained.

The shared AWC `CloudInfo.base` field is already integer feet: 500 stays 500 ft,
and 5,000 stays 5,000 ft. Values outside 0–60,000 ft or with a malformed type
remain unavailable; known cloud cover can remain without an invented base.
Cloud bases never substitute for an aircraft's missing altitude. See the
[AWC OpenAPI specification](https://aviationweather.gov/data/schema/openapi.yaml)
(`PIREPJSON` and `CloudInfo`).

## Limits

- A station observation describes its own site. A missing report is not
  evidence of good weather; few PIREPs do not mean little traffic.
- Live ADS-B/Mode S traffic is not displayed. The aviation intake runbook
  (`docs/runbooks/aviation-intake-20261021.md` in the monorepo) records why:
  OpenSky requires a written licence and adsb.lol's ODbL terms need admission
  review.
- The AWC routes take no caller input, refuse redirects, time out after
  12 seconds, read at most 2 MB and share a 2-minute cache. On failure they
  return an error and the layer shows no substitute observations.

Verification: `tests/aviation.test.mjs`, `tests/layer-explorer.test.mjs`, and
in the monorepo `tests/connectors/test_faa_airspace.py`.
