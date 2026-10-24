# Airspace, airports and aviation weather

One specialty layer, **Map layers > Airspace, airports & aviation weather**,
draws Kansas airspace as labelled 3D volumes, shows where small drones need
authorization, and ties live aircraft, airport weather and pilot reports to the
airspace they occur in. It is display context only: **not navigation, flight planning or
UAS authorization**. Active Kansas temporary flight restrictions (TFRs) are
listed but their boundaries are not drawn; NOTAM activations are not shown.

## Sources and clocks

| Data | Source | Clock |
|---|---|---|
| Airspace volumes, public-use airports and runways, airways | FAA NASR 28-day subscription, cycle 2026-10-29, via the pinned `public/data/aviation/kansas-aviation-context.json` | Valid 2026-10-29 up to (not including) 2026-11-26. Before the 29th the layer says it is a *preview* edition; after the 26th it says *expired*. |
| METAR (ASOS/AWOS station weather) | NOAA/NWS Aviation Weather Center Data API via `/api/aviation/metar` | Each station's own observation time; latest within 90 minutes; refreshed every 5 minutes while shown |
| PIREP (pilot reports) | Same API via `/api/aviation/pireps` | Report time; last 3 hours |
| LAANC grid ceilings | FAA UAS Facility Maps (ArcGIS `FAA_UAS_FacilityMap_Data`) via `/api/aviation/uas-grid` | FAA 56-day cycle; read once per session, cached a day at the edge |
| Temporary flight restrictions | FAA TFR list (`tfr.faa.gov/tfrapi/exportTfrList`) via `/api/aviation/tfrs` | Current list; refreshed every 10 minutes while shown |
| Live aircraft | Public ADS-B/Mode S receiver networks via `/api/aviation/traffic`: [adsb.lol](https://adsb.lol/) (ODbL 1.0), else [adsb.fi](https://adsb.fi/) open data (non-commercial, attribution) | Positions no older than 60 seconds; refreshed every 20 seconds while shown, 15-second shared cache |

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
- **LAANC grid (zoom 8+).** Each FAA UAS Facility Map cell is extruded from the
  ground to the altitude LAANC can approve there: 0 ft red (DroneZone request
  only), 50/100/200/300 ft, 400 ft green. Ceiling labels appear at zoom 11.5+.
  A ceiling is the most LAANC can approve, not an approval. If paging the FAA
  service does not finish, no grid is drawn rather than a partial one.
- **TFRs.** Kansas entries from the FAA's national list (matched by state or by
  "KANSAS"/", KS" in the text) appear in the drone section with their NOTAM IDs,
  and the point inspector warns when any are active. Their boundaries and
  times are in each NOTAM at tfr.faa.gov.
- **Airports and runways.** Blue dots are towered, magenta non-towered. Labels
  give the identifier and field elevation; runways draw from their surveyed end
  points at zoom 10+.
- **Airways.** Victor/T routes (1,200 AGL–below FL180) and Jet/Q routes
  (FL180–FL450), labelled with designation and MEA.
- **Live aircraft.** Each aircraft is an arrowhead pointing along its track,
  lifted to its reported altitude (geometric if reported, else barometric) above
  the nearest public-use airport's elevation, and coloured by altitude band;
  emergency squawks (7500, 7600, 7700) are red. At zoom 8+ the label gives
  callsign, type, altitude, ground speed and the airspace the aircraft is in at
  that altitude (for example `CLASS C · ICT`). The panel names the network that
  supplied the positions, with its terms.
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
- airways within 4 NM, pilot reports within 60 km and up to 12 aircraft within
  15 km, each with the airspace it occupies.

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
- Live traffic comes from volunteer receivers. Low-altitude aircraft, aircraft
  without ADS-B and anything out of receiver range are missing, so an empty sky
  is not evidence of no traffic. Positions older than 60 seconds are dropped,
  not extrapolated. Nothing identifies owners, missions or intent. OpenSky is
  not used: its terms require a written licence for this kind of display.
- The traffic route tries adsb.lol, then adsb.fi, with fixed URLs, no caller
  input, no redirects, a 10-second timeout and a 6 MB read limit. If both fail
  it returns an error and no positions are shown.
- The AWC routes take no caller input, refuse redirects, time out after
  12 seconds, read at most 2 MB and share a 2-minute cache. On failure they
  return an error and the layer shows no substitute observations.

Verification: `tests/aviation.test.mjs`, `tests/layer-explorer.test.mjs`, and
in the monorepo `tests/connectors/test_faa_airspace.py`.
