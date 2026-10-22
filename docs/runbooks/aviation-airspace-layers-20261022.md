<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/aviation-airspace-layers-20261022
title: Airspace, airport, drone and aviation weather layers
version: v0.1
type: runbook
status: draft
owners: ["@bartytime4life"]
created: 2026-10-22
updated: 2026-10-22
owning_root: docs/
responsibility: Plan, sources, rebuild steps, verification and rollback for the Site aviation layers.
truth_posture: CONFIRMED local implementation and tests; upstream AWC response shape NOT VERIFIED from this environment; no deployment or release.
policy_label: public
[/KFM_META_BLOCK_V2] -->

# Airspace, airport, drone and aviation weather layers

Follows `aviation-intake-20261021.md`. That runbook's held APT candidate lane,
its public hold decision and the disabled surveillance adapters are unchanged.
This change adds **display context** in the Site, the same evidence role the
Site uses for NOAA radar: not a KFM release, not navigation.

## Plan

| Layer | Data | Status in this change |
|---|---|---|
| Airspace shells (3D), technical labels | FAA NASR Class B/C/D/E, MOA, restricted, alert volumes, cycle 2026-10-29 | Built: pinned product + extrusion layers |
| Drone fly zones, SFC–400 ft AGL | Derived from the same volumes and 14 CFR 107 / 49 U.S.C. 44809 | Built: rule slabs + point verdict |
| "What can fly here at each height" | Volumes + 14 CFR 71 defaults + 14 CFR 91 requirements | Built: airspace column inspector |
| Airports and runways | NASR APT public-use facilities, runway ends, ASOS/AWOS type | Built: points, runway lines |
| Air traffic structure | NASR Victor/Jet/T/Q airway legs with MEA/MAA | Built: airway lines |
| Airport weather | NOAA/NWS AWC METAR (ASOS/AWOS) | Built: live route, flight category, cloud-ceiling discs, density altitude, VFR check |
| Observed traffic signal | NOAA/NWS AWC PIREP | Built: live route, reports at altitude |
| Live aircraft positions | OpenSky / adsb.lol | **Not built**: rights gates in the intake runbook still apply |
| UAS Facility Map grid ceilings, TFRs, NOTAM activation | FAA UASFM, TFR and NOTAM services | **Not built**: next candidates; not reachable from this environment |

The data mesh link is the point inspector: one click joins the airspace class
at that point, the drone rule, the nearest station's ceiling and visibility
(checked against that class's VFR minimums), nearby airways and pilot reports.
Stations are joined to airports by NASR's recorded weather-station type, and
METAR cloud ceilings are drawn in the same height frame as the airspace shells.

## Sources

NASR products were not directly downloadable from this environment (FAA and
AWC hosts are denied by its network policy). The airspace, airport and airway
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
Kansas-region bbox. Field handling follows the AWC Data API documentation; the
response could not be fetched from this environment, so parsers accept the
documented forms (Unix `obsTime`, hPa altimeter, `"10+"` visibility) and count
anything else as dropped rather than guessing.

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

Not run: browser visual/touch QA of the 3D layers, live AWC requests, hosted
deployment.

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
