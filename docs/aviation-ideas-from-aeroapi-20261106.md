# Aviation and airspace ideas drawn from FlightAware AeroAPI (2026-11-06)

FlightAware's AeroAPI v4 (spec 4.17.1, read from
`https://flightaware.com/commercial/aeroapi/resources/aeroapi-openapi.yml`)
is a paid, per-result-set service: the Personal tier is personal/academic
use only and every call above $5/month is billed. **The owner's direction on
2026-11-06 is to connect no paid or trial service.** This note takes the
*product ideas* in AeroAPI's endpoint catalogue and maps each to what the
Kansas Sky / Aviation layer can build from sources it already has for free:
public ADS-B receiver networks (adsb.lol, adsb.fi), the NOAA Aviation Weather
Center API, the FAA NASR airport/airspace snapshot, the FAA TFR list and the
FAA UAS Facility Map. Nothing here needs a key, an account or a trial.

Policy constraints carried over from `docs/kansas-sky.md`: observed positions
only; no owner, mission or intent inference presented as fact; every derived
label says what it was derived from.

| # | AeroAPI capability | What the site has today | Free-source idea | Size |
|---|---|---|---|---|
| 1 | `status`, `progress_percent`: a human phase for each flight | Raw instruments (altitude, vertical rate, speed) | **Observed phase label** per aircraft: *on surface*, *climbing*, *level*, *descending*, *low near KICT*, from `onGround`, vertical rate, altitude above the nearest facility and distance to it. Shown as "observed phase", never "en route to". | S |
| 2 | `/airports/{id}/flights` arrivals/departures boards (FIDS) | Airports drawn as dots; traffic drawn everywhere | **Observed airport activity board**: for a chosen public-use airport, list aircraft within ~10 NM and below ~3,000 ft above field, split *descending toward*, *climbing away*, *on surface*, with callsign, type, height and age. Pure observation, refreshed with the 20 s feed. | M |
| 3 | `/airports/{id}/flights/counts` | Nothing | **Activity counts** per airport over the retained session (ten minutes regional, one hour selected): aircraft seen low nearby, and a small sparkline. | S |
| 4 | `/airports/{id}` airport info page | NASR fields already in `kansas-aviation-context.json`: runways with ends, elevation, CTAF, pattern altitude, weather station, ownership | **Airport dossier panel**: one click on an airport dot opens runways (with length/surface), elevation, CTAF, pattern altitude, latest METAR, TFRs touching it, LAANC ceiling around it, and the observed activity board from idea 2. | M |
| 5 | `/airports/{id}/delays` | Nothing | **Reported delays** from the FAA NAS Status feed (`nasstatus.faa.gov`, a free government XML feed: ground stops, ground delay programs, closures). Verify the endpoint and its refresh terms before building; mostly reports KMCI-scale airports. | S |
| 6 | `/airports/{id}/weather/forecast` (TAF) | METAR only | **TAF per station** from the same AWC Data API (`/api/data/taf?bbox=`): forecast flight category for the next hours, drawn as a second ring colour on the station disc and listed in the dossier. | S |
| 7 | `/flights/{id}/track` and `/route` with waypoints | Trails; NASR airways drawn | **Airway proximity for the selected trail**: which Victor/T or Jet/Q route the observed trail has been tracking along (within a tolerance), labelled "observed along V10", not "filed via V10". | M |
| 8 | `/flights/{id}/map` static map | Report exports exist elsewhere on the site | **Flight card export**: PNG/SVG of the selected trail over the basemap with callsign, type, observed window, max height and provider attribution (ODbL). | M |
| 9 | Alerts: `arrival`, `departure`, `diverted`, `filed`, `cancelled` push | Nothing | **Session alerts** in the browser only: emergency squawk appears, an aircraft enters a drawn TFR volume, or an aircraft is first observed low near a chosen airport. Browser Notification API, no server, no persistence. | M |
| 10 | `/operators/{id}` and operator fleet views | Callsign shown raw | **Who is over Kansas now**: group observed aircraft by callsign prefix with a small static table of common ICAO operator codes (SWA, UAL, SKW, FDX, UPS, air-ambulance prefixes) plus GA (N-numbers) and the military flag the feed already carries. Counts by group, filter by group. | S |
| 11 | `/aircraft/types/{type}` | ICAO type code shown raw (B738, C172) | **Type decoding** from a curated static table (~120 common types): manufacturer, model, engine class, wake category. Shown beside the code; unknown codes stay raw. | S |
| 12 | `/airports/nearby`, `/airports/{id}/nearby` | Nearest-ground facility used internally | **Nearest airports for the selected aircraft**: three nearest public-use facilities with distance and bearing, from the NASR snapshot. | S |
| 13 | `position_only` flights, `ident_icao` vs `ident_iata` | Hex, callsign, registration | **Identity honesty line**: say explicitly "observed only; no plan or schedule is known to this site" and show callsign vs registration as separate, labelled fields. | S |
| 14 | History endpoints and `/history/aircraft/{reg}/last_flight` | Two prepared ODbL replays | **More prepared replays, by airport day**: the offline converter already exists; add a catalogue grouped by airport and date so "yesterday at KICT" is a recorded replay, prepared offline from adsb.lol history (ODbL). | M |
| 15 | `/schedules`, `/disruption_counts` (cancellations) | Nothing | **Not derivable from free data.** Schedules and cancellations exist only in licensed feeds. Leave out rather than approximate. | — |
| 16 | 15-row pages, `cursor`, `links.next`, `max_pages` | 3,000-row select list | **Paged, proximity-sorted aircraft list**: sort by distance to map centre, page 15 at a time, keep the search filter. Better on phones than one long select. | S |
| 17 | Published OpenAPI document, Postman import, AeroApps samples | Routes documented in prose | **Publish an OpenAPI file for the site's free aviation routes** (`/api/aviation/*`) with the same envelope fields (`retrievedAt`, `evidenceRole`, `limitation`) so others can reuse the Kansas feeds. | S |
| 18 | Foresight ETA predictions | Nothing | **Not derivable.** Do not fake an ETA from ground speed; at most show "at this speed, X min to the state line" labelled as arithmetic. | — |

## Recommended first set

Ideas 1, 2, 4, 6 and 11 give the biggest visible change for the smallest work
and stay entirely on data already loaded or already fetched:

1. **Observed phase label** (idea 1) is a pure function on the existing
   `Aircraft` record plus the nearest-facility lookup that
   `app/aviation-airspace.ts` already does; it goes in the Kansas Sky
   instruments block and the map label.
2. **Airport dossier** (idea 4) reuses NASR fields that are parsed but not
   shown, the METAR records already in memory, and the TFR shapes already
   drawn.
3. **Observed activity board** (idea 2) is the dossier's live section, built
   from the same traffic envelope the map draws.
4. **TAF** (idea 6) is one more fixed-URL AWC product in
   `app/aviation-weather-server.ts`, following the METAR/PIREP pattern.
5. **Type decoding** (idea 11) is a static table beside the code.

Everything else is additive and can follow. Ideas 15 and 18 are listed so the
gap is explicit: the site should say it does not know schedules, cancellations
or ETAs rather than approximate them.
