<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbooks/explorer-context-feed-repair
title: Explorer context-feed repair and acceptance
type: runbook
version: v0.1.0
status: proposed; review-pending; no-live-activation
owners: ["@bartytime4life"]
created: 2026-09-22
updated: 2026-09-22
policy_label: public; context-only; no-source-admission; no-release
owning_root: docs/
current_path: docs/runbooks/explorer-context-feed-repair.md
truth_posture: CONFIRMED bounded source inspection; PROPOSED integration; NEEDS VERIFICATION hosted acceptance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 0305c98702cb7b48dfaa9598b3625cb027860855
[/KFM_META_BLOCK_V2] -->

# Explorer context-feed repair and acceptance

**OPEN REPAIR — no deployed fix or source admission is recorded here.**

This runbook consolidates the September 22, 2026 owner report and local repair
handoff for elevation colors, radar, smoke and earthquakes. The screenshot shows
Terrain 3D at 1.0x and "Loading display terrain..."; it does not establish the
color-toggle state, source HTTP results or a shared cause for all four problems.
The [hazard-workspace proposal](../architecture/ui/firemap-inspired-hazard-workspace.md)
describes subsequent usability work. Repair existing connections before adding feeds.

## Pin the correct source before editing

| Evidence | Bound and limitation |
| --- | --- |
| Monorepo base | `0305c98702cb7b48dfaa9598b3625cb027860855`; separate from hosted source |
| Inspected standalone mirror | `c4e5ebe54cba9d7ca9bbee108b442bdf68763f58`, documented as v40 |
| Later hosted record | Issue #4418 comment `5748226637` records owner-private v53 / source `22ac19960c2f72f11f5e4e9b87c7e12f62074d6e` on September 20; not a native readback for this runbook |
| Current source equivalence | Not established; old mirror is not deployment input |
| Full provider-to-pixel acceptance | Not performed by this document or the local decoder tests |

Before operational integration, retrieve the active Site's exact source, saved
version, archive identity, access/bindings and immediately saved predecessor.
Preserve project `appgprj_6aa0b1c41bc08191bfd86003920f1631`, slug
`kansas-frontier-matrix-explorer` and the existing URL. See the repository's
[Site alignment boundary](../../apps/kansas-frontier-matrix-explorer/docs/sites-source-alignment.md).
Do not use that older dated alignment document as a live version readback either.

Recheck main, open PRs, candidate heads, path overlap and applicable AGENTS/README
instructions. Preserve #4024 delivery containment and #4228 topology decisions.
Do not bypass rules, rewrite baselines, mark ready, merge or deploy under a request
that only authorizes repository files and draft PRs.

## Trace request, parse, state and render separately

For each selected source capture configuration state, request path/HTTP/media result,
retrieval time, provider observation/publication/valid time, query bounds/window,
accepted and withheld counts, source/layer IDs, visibility/opacity, renderer errors,
and final displayed result. Keep diagnostic output free of credentials, complete
response bodies, private contributions and sensitive locations. A failed diagnostic
environment is not evidence that the provider itself is down.

Each source needs a bounded terminal outcome and a visible recovery action. Keep
OFF, unsupported time, missing configuration, successful empty, partial coverage,
stale data and request/render errors distinct. Do not hide an optional source's
failure by relabeling it current or inventing data.

## Earthquakes: provider-defined no data

The historical `app/api/live-context/route.ts` uses a generic bounded JSON reader.
USGS documents 204 as its default no-data response, with `nodata=204` or `nodata=404`;
there is no documented `nodata=200` option. The historical reader throws on a missing
body, so a legitimate 204 can become a feed error. This is a source-level/local
reproduction, not proof that every currently blank earthquake view has that cause.

The supplied repair candidate adds a USGS-only response decoder and explicitly
requests `nodata=204`. Its 36 recorded local tests cover empty/populated results,
HTTP errors, malformed bodies, byte limits, invalid UTF-8 and stream failures.
That prior result belongs to the supplied candidate, not a later repository head.
Run fresh tests after porting. Neither the candidate nor this runbook changes the
smoke, radar or alert no-data policies.

At the active fixed-query caller, apply the decoder within the existing timeout and
byte-limit boundary. Retain manual redirect rejection, host/path allowlists, exact
query bounds, event filtering and feature/selection replacement. Validate geometry,
identity, dates and query membership after decoding; a valid outer FeatureCollection
is not full event validation. Preserve the 30-day Present window and single-day UTC
historical window unless a separate query-scope change is reviewed.

Test the actual route for 204, valid 200 empty/populated, malformed 200, 404, 429,
server failure, timeout and oversize. Then verify populated -> empty -> populated
on the same browser/map: old geometry and invalidated selection must clear, without
resetting the camera. Report query window and last successful retrieval separately
from the last event time. Zero returned records is not an earthquake warning or
proof that no event occurred anywhere.

## Terrain: desired colors versus loaded terrain

Historical `app/map-runtime.ts` creates a `raster-dem` color source and `color-relief`
layer, while terrain setup returns LOADING. The color helper catches failures as a
boolean and does not itself prove tiles or pixels; inspect its consuming UI before
claiming a loading state can never finish. MapLibre documents color-relief support
before the later recorded Site version, so a dependency upgrade is not a diagnosis.

Trace toggle -> desired state -> source/layer creation -> source-specific events ->
terminal UI state. Check encoding, requests, CSP/CORS, layer order/visibility/opacity,
style-generation changes and cached-source readiness. Preserve the zoom-11 safety
cap documented by `app/terrain-sources.ts`; it excludes observed high-zoom artifacts.
Do not substitute slope or hillshade under an elevation label.

A non-flat synthetic DEM must visibly produce distinguishable unexaggerated height
colors. Test disable/enable, basemap replacement, 2D/terrain cycles, camera retention,
failed tiles, bounded timeout and retry. Show the quantitative legend and label
exaggeration. A readiness probe must tolerate optional renderer properties without
hiding real failures. Obtain exact-source WebGL screenshots and actual tile results.

## Radar: timestamps are not images

Historical `app/noaa-radar.ts` obtains advertised nowCOAST times via
`/api/noaa-radar/frames`, then requests WMS images separately at exact timestamps.
The reviewed parser requires two frames. A one-frame static fallback would change
that loop contract and needs explicit tests/review; do not fabricate a second frame
or silently expand an unsupported time interval.

Capture the manifest, selected advertised time, one in-bounds WMS image response,
media type, renderer source events and actual layer. Check layer/style identifiers,
EPSG:3857 bounds, retention, network/CSP/CORS and style replacement. Distinguish
manifest failure, image failure, stale frame and successfully delivered transparent
imagery. Never convert failed imagery into a successful transparent PNG.

Use a labeled deterministic positive image to prove rendering, then separately
check the real provider. Test expiry, slow/failing images, retry, frame changes,
hidden/unmounted views and reattachment after style changes. Any relay is a separate
fixed-provider, bounded security review, not an arbitrary-URL workaround.

## Smoke: publication, interpretation and regional coverage

Historical `currentHmsSmoke()` reads NOAA HMS daily KML for a bounded rolling 24-hour
window or historical day. One failed publication produces partial coverage; all
failed publications produce an error. `parseSmokeKml()` validates intervals, density,
geometry and budgets, then filters the Kansas bounding region. Unsupported records
can reject a publication. Reproduce against the actual failing artifact before
loosening parsing rules.

Retain publication day, HTTP outcome, parse category, provider/accepted counts and
coverage intervals. Separate a not-yet-published daily file, valid zero matching
polygons and malformed KML. Preserve original times; do not carry expired polygons
forward or substitute modeled smoke. Successful empty results clear old geometry.

Test populated/empty regional results, one missing day, total failure, invalid KML,
exact interval edges and actual polygon/legend display. Test no external entities,
NetworkLinks or executable description HTML. An HMS footprint is not a surface
PM2.5 reading, plume altitude, fire perimeter, health assessment or all-clear.

## Same-candidate acceptance and rollback

Required packet: exact source/head, toolchain/browser/WebGL capability, bounds/time,
source and response identities, request/parse/render outcomes, screenshots, original
timestamps, errors, retry/recovery and saved-predecessor identity. Report fixture,
local build, hosted CI, real-provider and authenticated-browser evidence separately.

A failed source must not remove the shell or disable unrelated controls. Exercise
opacity/toggles, style replacement, 2D/terrain/supported globe, keyboard, reduced
motion, narrow screens, stale/empty responses and disposal. Recheck source/branch
heads after any modification; old-head tests are not current-head acceptance.

Before merge, human review and exact-head checks remain required. Before Site changes,
obtain the separate deployment decision, save/inspect a candidate and retain the
predecessor. A saved predecessor is a rollback candidate, not a rehearsed recovery.
Abandon an unmerged candidate or review an inverse/forward fix without rewriting
history. Keep provider admission, release, publication and audience changes separate.
No live defect is closed by this runbook, an HTTP 200, local tests or a PR merge.

## Evidence references

- [Inspected v40 mirror](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/c4e5ebe54cba9d7ca9bbee108b442bdf68763f58)
- [Later v53 record](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4418#issuecomment-5748226637)
- [USGS event API](https://earthquake.usgs.gov/fdsnws/event/1/)
- [MapLibre color-relief](https://maplibre.org/maplibre-style-spec/layers/#color-relief)
- [Contribution rules](../../CONTRIBUTING.md) and [adopted Directory Rules](../doctrine/directory-rules.md)
