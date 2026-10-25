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
| TFRs | FAA TFR list + NOTAM detail files | Built 2026-10-24 as a Kansas list; 3D volumes from detail files added the same day (see TFR boundaries follow-up) |
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

## Traffic expiry fix — October 24, 2026

Review finding on [PR #5459](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5459)
(merged with the thread resolved but no code change): the browser redrew the
last traffic response after traffic was turned off and on, and kept a position
past the 60-second limit until the next refresh. The control now discards
positions when traffic or the layer is turned off. Between refreshes it expires
each position 60 s after observation: the position's age at retrieval, plus up
to 30 s of edge-cache age, plus the time since this browser received it. The
cache age is clamped so that a wrong browser clock cannot expire every
aircraft. A component test reproduces the toggle case and fails on the merged
control. Successor mirror receipt:
`site-v268-aviation-traffic-expiry-fix-20261024.json`. Rollback: revert the
fix commit, which selects the live-traffic receipt again.

## TFR boundaries follow-up — October 24, 2026

The TFR list has no geometry, but each NOTAM's XNOTAM detail file does:
`https://tfr.faa.gov/download/detail_<id>.xml`, where `6/1234` becomes
`detail_6_1234.xml`. `/api/aviation/tfrs` now reads these for Kansas and
neighbouring-state entries: at most 30 files, six at a time, 8 s and 1 MB each,
and no new reads after a 20 s deadline. It returns each area that reaches the
region as `shapes`, with `detailsChecked` and `detailsFailed` counts.

Field use follows OpenSectional's XNOTAM parser (`src/xnotam_parser.cpp`, read
on 2026-10-24, because the FAA host was unreachable from the build environment):

- **Path.** `XNOTAM-Update/Group/Add/Not/TfrNot/TFRAreaGroup`.
- **Boundary.** `abdMergedArea/Avx` `geoLat`/`geoLong` decimal degrees with a
  hemisphere letter. The alternate `aseShapes` description is ignored.
- **Altitude.** `codeDistVer*`, `valDistVer*` and `uomDistVer*`: `FL` is
  hundreds of feet, `HEI` is above ground, 99999 or more is unlimited, and
  anything else is MSL.

An area with malformed limits or vertices, no boundary, or more than 20,000
vertices is never shortened or guessed. It is left undrawn, and its file is
counted in `detailsFailed`, so the panel warns that boundaries are missing.
Areas wholly outside the region are left out without a count. The detail URL is built
only from ids matching `^\d/\d{1,5}$`. The response stays cached 5 minutes at
the edge. Field names and the detail-file media type must be confirmed on the
first hosted run.

Rollback: revert the follow-up commit; the list-only route returns.

## 2D chart, altitude slices and point ground — October 25, 2026

Owner direction: the flight zones should be viewable as 3D forms, with the same
data displayable in 2D.

- **View switch.** The panel switches between 3D volumes (fill-extrusion,
  tilted camera) and a 2D chart (flat fills, top-down camera). Both are drawn
  from the same GeoJSON sources; each 3D layer id keeps a flat twin.
- **Labels.** 2D airspace labels use sectional notation (ceiling/floor in
  hundreds of feet; `ICT 53/27`).
- **Altitude slice.** `app/aviation-chart.ts` keeps features containing a chosen
  MSL level, or starting below 400 ft AGL for the drone slice. It recovers each
  feature's floor and ceiling from its drawn base/top plus its ground reference
  (`groundFt`, now carried by airspace, drone, TFR and traffic features), so the
  views agree.
- **Point ground.** The picked point's ground uses already-loaded terrain only
  when it agrees with the nearest facility to within 1,000 ft. No new terrain
  requests are made; the tiles stay opt-in. The drone verdict now judges MSL
  floors against that point ground rather than the volume's reference, matching
  the column table.
- **Wording.** The Class G drone text no longer says TFRs are not shown.

- **Side view.** `app/aviation-profile.ts` samples 241 points between two
  clicks (up to 320 NM). Each volume and TFR becomes runs of samples with its
  floor and ceiling in feet MSL over the ground at each sample. The chart
  (0–20,000 ft MSL) shows the ground, the 400 ft AGL drone ceiling, Class A
  shading, and aircraft within 5 km; a text list repeats every crossing. NASR
  charts the Wichita Class C shelf as the full 10 NM circle over the core, so a
  line through Wichita shows the core from the ground inside the shelf from
  2,700 ft.

Rollback: revert the commit; the 3D-only layer, nearest-facility point ground
and no side view return.

## Near-here dossier link — October 25, 2026

Original direction: the aviation data should fit with the Site's other features
as a data mesh. While the aviation layer is shown, it now offers point records to
the page's **Near here** dossier: public-use airports at their FAA NASR
reference points, and METAR stations with their latest observation
(`app/aviation-research.ts`, through the control's `onResearchRecords`).
`app/page.tsx` adds them, validated by the dossier's own `validResearchRecord`,
with an "Airspace, airports & aviation weather" coverage row.

Excluded, with the reasons given in that coverage row:
- airspace volumes and TFR areas, because they are polygons and the dossier
  admits supplied points only;
- private-use strips, so they cannot crowd the 50 nearest records near towns;
- live aircraft, because their positions are transient and dossiers can be
  saved.

Rollback: revert the commit; the dossier returns to its earlier sources.

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


## October 25 native-browser qualification follow-up

Status: candidate corrections, independent review and exact-head hosted checks
pending. #5465 had already merged at d08e613d2cbf41af929a9f4b377b6694035b5ca5;
this follow-up starts at #5466's 965b8783c171a14275e9b25e1ef84c0b174fb9f8 and
preserves its Near-here records. #5467 was open during the final overlap check
and affects aviation point-inspector wiring; recheck its disposition before merge.

Evidence is native Chrome against a local production build of the candidate,
not production or a recording-map mock. The #5465 source copy was verified
against all 901 Git blob hashes before testing. The follow-up preserves the
902-file mirror inventory.

| Scenario | Observed result |
|---|---|
| Desktop, 1707 × 865 CSS pixels | 2D chart, 4,000 ft MSL slice, 3D switch, 3× exaggeration and camera tilt exercised |
| Real mouse A/B clicks plus keyboard pan | Cross-section completed; no underlying county selection or Evidence Drawer opening while drawing |
| Phone, 390 × 844 CSS pixels | Drone slice, keyboard map-center A/B placement, readable 760-pixel chart in a 311-pixel scroll region; document has no horizontal overflow |
| Chart keyboard scrolling | ArrowRight moved scrollLeft to 53.33 CSS pixels |
| Ground without terrain | Point showed 1,633 ft MSL, nearest facility 9K7 at 18.9 km; reference explicitly stated |
| Loaded terrain | Terrain 3D reached DEM-ready; a new point inspection used 1,641 ft MSL terrain elevation at the point |
| Native Escape | Cancelled an armed A/B tool and returned its toggle to off |
| Source uncertainty | Preview NASR cycle warning, missing-observation states, source limits and non-authorization wording visible |
| Reduced motion and DEM spike rejection | Deterministic component/unit tests; native OS/media emulation and a real DEM spike were not forced |

Demonstrated defects corrected: draw clicks and deferred hover previews competed
with evidence selection; the chart shrank to roughly 278 pixels; inaccessible
map-point placement; invalid paths failed silently; labels could imply clearance
from unshaded or incomplete data. The camera honors reduced motion in tests.

Data limitations remain: NASR 2026-10-29 is a preview until its effective date;
TFR parser success is not independent feed-completeness qualification; NOTAM
activation of other airspace is not implemented; ADS-B coverage is partial;
241 profile samples can miss narrow areas; chart height stops at 20,000 ft;
AGL placements depend on approximate ground references; flight levels are
approximated on an MSL axis without pressure correction. This is not certified
navigation, flight-planning or drone-authorization guidance.

No public deployment or Sites synchronization was performed. Revert the follow-up
application changes, receipt selector and receipt regression tests together to
restore the predecessor. Source bytes, provider requests and stored data are
unchanged.

The TFR list included a future-dated NOTAM; the follow-up replaces unqualified
“active” wording with “listed,” exposes retrieval time and requires checking
effective times. Full local suite: 1,448 tests, 1,447 passed, 1 skipped, 0 failed.
Changed-area checks: 44 aviation, 16 local-atlas, 3 hover and 11 scene tests pass;
TypeScript passes; focused ESLint has 0 errors and 42 existing page warnings.
Mirror checks pass: 62 tests, 902 files, 258 withheld paths absent.
