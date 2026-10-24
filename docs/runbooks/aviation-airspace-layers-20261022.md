<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/aviation-airspace-layers-20261022
title: Airspace, airport, drone and aviation weather layers
version: v0.3
type: runbook
status: draft
owners: ["@bartytime4life"]
created: 2026-10-22
updated: 2026-10-24
owning_root: docs/
responsibility: Plan, sources, rebuild steps, verification and rollback for the Site aviation layers.
truth_posture: CONFIRMED local implementation, AWC specification and bounded PIREP response readback; rendered and hosted acceptance NOT VERIFIED; no deployment or release.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# Airspace, airport, drone and aviation weather layers

Follows `aviation-intake-20261021.md`. That runbook's held APT candidate lane
and its public hold decision are unchanged. Its disabled surveillance adapters
were changed on 2026-10-24 (see the live traffic follow-up below): adsb.lol and
adsb.fi are display-only; OpenSky stays denied.
This change adds **display context** in the Site, the same evidence role the
Site uses for NOAA radar: not a KFM release, not navigation.

## Plan

| Layer | Data | Status in this change |
|---|---|---|
| Airspace shells (3D), technical labels | FAA NASR Class B/C/D/E, MOA, restricted, alert volumes, cycle 2026-10-29 | Built: pinned product + extrusion layers |
| Drone fly zones, SFC–400 ft AGL | Derived from the same volumes and 14 CFR 107 / 49 U.S.C. 44809 | Built: rule slabs + point verdict |
| "What can fly here at each height" | Volumes + 14 CFR 71 defaults + 14 CFR 91 requirements | Built: airspace column inspector |
| Airports and runways | NASR APT open facilities, public and private use, runway ends, ASOS/AWOS type | Built: points, runway lines; private use added 2026-10-24 |
| Air traffic structure | NASR Victor/Jet/T/Q airway legs with MEA/MAA | Built: airway lines |
| Airport weather | NOAA/NWS AWC METAR (ASOS/AWOS) | Built: live route, flight category, cloud-ceiling discs, density altitude, VFR check |
| Observed traffic signal | NOAA/NWS AWC PIREP | Built: live route, reports at altitude |
| Live aircraft positions | adsb.lol, else adsb.fi (public ADS-B receiver networks) | Built 2026-10-24: `/api/aviation/traffic`, aircraft at altitude tagged with occupied airspace; OpenSky still denied |
| UAS Facility Map grid ceilings | FAA UASFM ArcGIS service | Built 2026-10-24: `/api/aviation/uas-grid`, 3D LAANC cells, ceiling in the point inspector |
| TFRs | FAA TFR list | Built 2026-10-24 as a Kansas list and inspector warning; boundaries not drawn (the list has no geometry) |
| NOTAM activation | FAA NOTAM services | **Not built** |

The data mesh link is the point inspector: one click joins the airspace class
at that point, the drone rule, the nearest station's ceiling and visibility
(checked against that class's VFR minimums), nearby airways and pilot reports.
Stations are joined to airports by NASR's recorded weather-station type, and
METAR cloud ceilings are drawn in the same height frame as the airspace shells.

## Sources

At the original layer build, NASR products were not directly downloadable from
its environment (FAA and AWC hosts were denied by its network policy). The airspace, airport and airway
inputs come from npm packages that pre-process the FAA NASR subscription:
`@squawk/airspace-data@0.9.1`, `@squawk/airport-data@0.9.2`,
`@squawk/airway-data@0.7.3` (MIT; FAA NASR is a U.S. Government work). Each
tarball was verified against its registry `sha512` integrity before extraction;
those strings and the SHA-256 of each data file are inside the product.

Edition: these packages carry cycle **2026-10-29**, which is not yet effective
on 2026-10-22. The current 2026-10-01 cycle was not available. The Site labels
the edition *preview* until 2026-10-29 and *expired* from 2026-11-26. Compared
with the package's 2026-09-03 snapshot, every Kansas Class B, C, D, restricted
and alert area has the same floor and ceiling. Geometry digests differ because
the package's arc tracing changed between versions, so this comparison supports
but does not prove equality with the 2026-10-01 boundaries. Three MOA floors
differ between those versions (Smoky and Cougar Low: SFC to 500 ft AGL; Bison:
SFC to 1,000 ft AGL). Whether that is a charting change or a package
correction was not independently verified.

METAR/PIREP: `https://aviationweather.gov/api/data/{metar,pirep}` with a fixed
Kansas-region bbox. The original build could not fetch upstream responses.
The PIREP correction follow-up below independently checks the specification and
one live response. METAR live acceptance remains unverified by that follow-up.

## Rebuild the product for a new cycle

```bash
npm pack @squawk/airspace-data@<v> @squawk/airport-data@<v> @squawk/airway-data@<v>
# verify each tarball: openssl dgst -sha512 -binary <tgz> | base64 == npm view <pkg>@<v> dist.integrity
python3 pipelines/domains/roads-rail-trade/faa_airspace.py \
  <airspace.geojson.gz> <airports.json.gz> <airways.json.gz> <new-output.json> \
  --source '{"airspace":{...},"airports":{...},"airways":{...}}'
```

Then copy the output to `apps/site/source/public/data/aviation/kansas-aviation-context.json`,
update `AVIATION_CONTEXT_ASSET` (SHA-256, product id, cycle) in
`apps/site/source/app/aviation-airspace.ts`, update the cycle assertions in
both tests, and record a successor Site mirror receipt. A direct FAA NASR
adapter (`connectors/faa/`) remains the preferred future source.

## Verification (local, this change)

- `python -m pytest tests/connectors/test_faa_airspace.py tests/connectors/test_faa_airports.py`
- `apps/site/source`: `node --test tests/aviation.test.mjs tests/layer-explorer.test.mjs`,
  typecheck, lint, build and the full Node suite; results are recorded in the
  successor mirror receipt `site-v268-aviation-layers-overlay-20261022.json`.
- `python tools/qa/site_mirror.py --check` against that successor receipt.

Not run in the original build: browser visual/touch QA of the 3D layers, live
AWC requests, hosted deployment. See the bounded follow-up below for PIREP
readback; browser and hosted acceptance remain separate.

## PIREP parsing correction — October 22, 2026

Inspected `main@472747fe92a343472829234f40e85b47d9c8e694` and both review
findings on [PR #5412](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5412).
Resolved discussion state did not establish a code correction. The follow-up
accepts numeric-string flight levels, classifies `fltLvlType`, and preserves
cloud bases in feet. A 23,000 ft MSL report draws at
`max(0, 23000 - nearestAirportElevationFt) * 0.3048 * exaggeration` metres.
Climb/descent and missing altitudes retain their records in the API and point
inspector, with explicit phase/unavailable text, but create no altitude extrusion.

Independent upstream checks:

- [AWC OpenAPI](https://aviationweather.gov/data/schema/openapi.yaml), retrieved
  October 22 at 19:09 CDT (October 23 at 00:09 UTC): SHA-256
  `4eb4023ea68788001cc601cc70585dc0b04ea3f9c4fb6ac3c3c64e4cb355bf47`.
  `PIREPJSON.items.properties.fltLvl` is a string in hundreds of feet;
  `fltLvlType` enumerates `GRND`, `DURC`, `DURD`, `CRUISE`, `OTHER`, `UNKN`.
  `CloudInfo.items.properties.base` is integer feet. Parsing keeps the existing
  flight-level range 0–600 and validates cloud bases as integer feet 0–60,000.
- One fixed Kansas request to
  `https://aviationweather.gov/api/data/pirep?bbox=36.7,-102.3,40.3,-94.3&format=json&age=3`
  at 19:10 CDT (00:10 UTC) returned HTTP 200, JSON, 1,320 bytes and two records. Both flight levels were
  numbers (230 and 360), with phase `OTHER`. Therefore numeric compatibility is
  retained alongside documented strings. Response SHA-256:
  `d4a9464379636a046b4426a8db79e7cf92b14024d6848f5b6f9f8f2739608092`.
  This transient response is not a committed fixture, source admission, or
  evidence of continuing availability.
- The [FAA NASR index](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/)
  lists October 1 as current and October 29 as preview. The
  [October 29 subscription page](https://www.faa.gov/air_traffic/flight_info/aeronav/aero_data/NASR_Subscription/2026-10-29/)
  is published with download links. This confirms preview publication status;
  it does not requalify package geometry against official FAA bytes. The pinned
  product and its preview/expiry behavior are unchanged.

Synthetic regression coverage includes cruise strings/numbers and zero;
climb/descent with and without numeric levels; unknown/malformed levels; low,
high, zero and invalid cloud bases; missing, stale and out-of-region reports;
and map heights at 1×/3×/6×. No live report is used as a fixture. The successor
mirror receipt is `site-v268-pirep-weather-parsing-overlay-20261022.json`;
generated-work provenance is `genrec-pirep-weather-parsing-20261022.json`.
Independent AI review is distinct from pending human acceptance. No FAA rights,
held APT lane, evidence-role, source-admission or publication decision changes.

## Drone grid and TFR follow-up — October 24, 2026

Owner-directed follow-up after #5412 merged. Two FAA public safety feeds were
added; live ADS-B traffic and private-use airports were deliberately left out
of this change.

- `/api/aviation/uas-grid` pages the FAA UAS Facility Map service
  (`FAA_UAS_FacilityMap_Data/FeatureServer/0`, fields `CEILING`, `APT1_FAAID`,
  `APT1_NAME`) over the Kansas region, 2,000 cells per page, at most 15 pages
  and 30,000 cells. A page with an `error` body, a missing or out-of-range
  `CEILING`, or paging that does not finish fails the whole response: no
  partial grid is drawn. Cached a day at the edge (FAA 56-day cycle).
- `/api/aviation/tfrs` reads the FAA TFR list (`tfr.faa.gov/tfrapi/exportTfrList`)
  and keeps entries with state `KS` or "KANSAS"/", KS" in the text. Several
  field spellings are accepted because the FAA has changed them before. No
  boundaries are drawn: the list has no geometry.
- Neither host was reachable from the build environment, so both parsers
  follow published field names (UASFM fields confirmed only from public
  mirrors) and must be confirmed on the first hosted run.

Verification: build; typecheck; lint (0 errors, 77 unchanged warnings); full
Site suite 1,427 tests (1,425 passed, 0 failed, 2 root-refusal skips); local
Worker smoke 110 checks across 79 routes with 13 provider-only routes; mirror
parity against `site-v268-aviation-drone-grid-tfr-overlay-20261024.json`
(896 files); `tests/qa/test_site_mirror.py` and FAA connector tests (149
passed); topology PASS with 0 new drift.

Rollback: revert the follow-up commit, which restores
`site-v268-privacy-path-redaction-overlay-20261023.json` as the selected
mirror receipt. The routes store nothing.

## Live traffic and private-use airports follow-up — October 24, 2026

Owner direction: "Use any public record. If it is publicly available than it
is within the use of the public", then "Allow it all" for the held items.

- `/api/aviation/traffic` reads `api.adsb.lol/v2/point/38.5/-98.35/250`, and
  if that fails, `opendata.adsb.fi/api/v3/lat/38.5/lon/-98.35/dist/250`.
  adsb.fi documents its `/v2/lat` route as deprecated in favour of v3 (250 NM
  maximum, 1 request per second); adsb.lol needs no key today but says one will
  be required in the future. Both accept `ac` or `aircraft` lists. Positions
  older than 60 seconds, outside the Kansas region plus ~50 NM, or with
  malformed identifiers are dropped. A 15-second shared cache keeps viewers
  well under provider limits. Responses name the provider and its terms
  (adsb.lol: ODbL 1.0; adsb.fi: personal, non-commercial use with attribution).
- `connectors/faa/capture.py:surveillance_decision` records the display-only
  allowance (`ALLOW_DISPLAY_ONLY`, `OWNER_DIRECTED_PUBLIC_RECEIVER_DATA`):
  nothing is ingested, stored or admitted as evidence. OpenSky remains
  `DENY`/`WRITTEN_LICENSE_REQUIRED`.
- The airspace product moved to profile v2: all 533 open facilities in the
  region (188 public use, 345 private use) with a `use` flag and
  `airport_counts`. Heliports are listed but never anchor ground heights (their
  elevation can be a rooftop); the 278 added non-heliport anchors moved 28
  volumes to a closer ground reference. New product
  `sha256:66fd3695e5a481625f8d16923117df47bbbab015e358bdeea21ce9b317c66b86`,
  file SHA-256 `ada5a80a5c54f8af52d1c466504ed08244f3dd3576ce50820936a857dccddc13`,
  rebuilt from the same verified package inputs.
- Neither traffic host was reachable from the build environment; the parser
  follows the readsb JSON format and must be confirmed on the first hosted run.

Verification: build; typecheck; lint (0 errors, 77 unchanged warnings); full
Site suite 1,431 tests (1,429 passed, 0 failed, 2 root-refusal skips); local
Worker smoke 110 checks across 79 routes with 14 provider-only routes; mirror
parity against
`site-v268-aviation-live-traffic-private-airports-overlay-20261024.json`
(899 files); `tests/qa/test_site_mirror.py` and FAA connector tests (141
passed); topology PASS with 0 new drift.

Rollback: revert the follow-up commits, which restores
`site-v268-aviation-uas-grid-request-fix-20261024.json` as the selected mirror
receipt and the v1 product. The route stores nothing.

## Decision for the owner

The intake runbook held public FAA airport rendering behind an aviation release
profile. This change shows airports, airspace and airways as external display
context instead, alongside other provider context, while leaving the KFM
evidence-grade lane held. If airports should stay hidden until that profile
exists, untick or remove the airports toggle; the airspace and weather layers
do not depend on it.

## Rollback

Revert the change. The Site has no persisted state for this layer; the routes
store nothing. Select the predecessor mirror receipt
`site-v268-next-security-overlay-20261022.json` in `tools/qa/site_mirror.py`.
For only the parsing correction, revert its application/docs/tests and receipt
selector together to `site-v268-aviation-layers-overlay-20261022.json`; retain
historical receipts unchanged.
