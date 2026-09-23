<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/ui/firemap-inspired-hazard-workspace
title: Firemap-inspired hazard workspace
type: architecture
version: v0.1.0
status: proposed; review-pending; no-live-activation
owners: ["@bartytime4life"]
created: 2026-09-22
updated: 2026-09-22
policy_label: public; context-only; no-source-admission; no-release
owning_root: docs/
current_path: docs/architecture/ui/firemap-inspired-hazard-workspace.md
truth_posture: CONFIRMED bounded source inspection; PROPOSED integration; NEEDS VERIFICATION hosted acceptance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 0305c98702cb7b48dfaa9598b3625cb027860855
[/KFM_META_BLOCK_V2] -->

# Firemap-inspired hazard workspace

**PROPOSED DESIGN — not implemented, deployed, or accepted by this document.**

Use [Firemap](https://www.firemap.live/) as a reference for clear hazard exploration,
not as a source of copied code, branding, private APIs, or automatically admitted
data. The September 22, 2026 reference review inspected its public interface,
legend and descriptions; it did not verify live-feed performance or WebGL behavior.
This repository version consolidates that review and the owner-reported elevation,
radar, smoke and earthquake problems into reviewable requirements.

## Scope and authority

Preserve the existing Kansas Frontier Matrix Explorer: one map, camera continuity,
MapLibre, the existing Evidence Drawer, source attribution, explicit Share flow,
Site identity, audience and bindings. See the [UI architecture boundary](README.md)
and the [repository app boundary](../../../apps/kansas-frontier-matrix-explorer/README.md).
The standalone hosted Site and monorepo application are different source histories.
Do not merge a standalone-root mirror into monorepo main or overwrite newer Site
code with an older mirror.

[Repair the existing connections first](../../runbooks/explorer-context-feed-repair.md).
Neither this proposal nor its PR admits a provider, activates a scheduler, changes
rights or policy, approves a release, or proves a rendered map. Firemap's source
choices do not supply Kansas coverage, licensing, freshness, or acceptance evidence.

## Compact controls and active legends

Add one compact Fire / Smoke / Radar / Earthquakes / Wind navigation strip inside
the existing map workspace. Terrain and Water keep their existing entry points.
Unavailable or unqualified categories explain their state; they must not look like
working live toggles. Category navigation opens existing controls or a focused
view without enabling unrelated providers, resetting the camera, changing time,
clearing selection, or constructing another map.

Each source row groups visibility, opacity, hide, retry and provider details with
source role, data time, retrieval time and a short status explanation. Mobile uses
one bottom sheet with a stable close/focus-return action. Attribution, zoom and
emergency-source links remain accessible. Keyboard operation and text explanations
must work without relying on color.

The legend describes selected, display-eligible layers only. Keep detection age,
physical magnitude/severity and service health separate. A stale large earthquake
must not become visually low magnitude just because it is old. Units, provider,
selected observation/valid time and any display exaggeration remain visible.

## Source health is not one LIVE badge

These are proposed UI projections of existing contracts, not a new canonical
schema or a replacement for evidence/policy outcomes:

| Dimension | Proposed values | Meaning |
| --- | --- | --- |
| Configuration | configured / missing / held | Adapter configuration and permission to attempt a request |
| Request | idle / loading / succeeded / failed / timed out | Transport result for this attempt |
| Payload | not checked / accepted / empty / partial / rejected | Validated provider response, including valid zero records |
| Display | off / waiting for style / out of time range / out of bounds / loading / available / failed | Requested layer's display eligibility and readiness |
| Freshness | unknown / current / delayed / expired | Source-specific age policy, not generic browser age |
| Render evidence | not checked / fixture verified / hosted verified | Separate, exact-candidate verification, never inferred from HTTP success |

Bound loading time and expose retry. A successful empty response replaces prior
geometry; a failed refresh never becomes an empty success. If retaining old data,
retain its original timestamp and stale label. Record last success separately from
the current error. A transparent raster can be successfully delivered without
establishing semantic coverage or an all-clear. Radar timestamps do not prove that
the selected image loaded.

Illustrative status copy, not real observations:

- Radar: frame times available; selected image failed; retry available.
- Earthquakes: request succeeded; no catalog events returned for this area and window.
- Smoke: one publication unavailable; coverage is limited to retrieved intervals.
- Elevation colors: source loading timed out; 2D and other layers remain available.

## Scientific roles and provider gates

Agency incidents, official perimeters, satellite thermal detections, analyzed
smoke footprints, surface-monitor measurements and modeled fields remain separate
layers with separate identities and legends. NASA explains that a FIRMS detection
is a flagged pixel, not a fire's precise location or extent. Count detections as
detections, not incidents; do not synthesize authoritative perimeters from clusters.
See the [NASA FIRMS FAQ](https://www.earthdata.nasa.gov/data/tools/firms/faq).

NOAA HMS plume areas are satellite-interpreted smoke context, not a measured
surface PM2.5 concentration or a quantitative vertical profile. See the retained
[NOAA interpretation example](https://ospo.noaa.gov/smoke-data/2024/2024D250410.html).
For additional smoke/air-quality fields verify product, species, level, units,
valid time, model-run/analysis identity, native resolution and display resampling.
ECCC distinguishes wildfire-smoke guidance from total PM2.5, and its RDAQA source
has a coarser grid than a resampled display. Those are reference distinctions, not
permission to connect either product to Kansas. See [ECCC model maps](https://weather.gc.ca/firework/index_e.html)
and [RDAQA documentation](https://eccc-msc.github.io/open-data/msc-data/nwp_rdaqa/readme_rdaqa-datamart_en/).

NASA's documented [FIRMS WMS](https://firms.modaps.eosdis.nasa.gov/mapserver/wms-info/)
requires a MAP_KEY. Verify the active KFM path and account/quota contract before
calling blank fire imagery zero detections. Missing configuration should make no
request. Keep keys out of Git, share links and diagnostics. Any future server relay
requires fixed-host/path routing, bounded parameters, timeouts, payload/media
checks, redirect policy and a reviewed quota strategy; never an arbitrary-URL proxy.
No provider key, credential requirement change or relay is added by this document.

## Time, selection and investigation views

Derive event age from observation time, not retrieval time. Show exact observation,
valid and retrieval times as applicable. Recent-window shortcuts are enabled only
where the existing adapter supports them; do not widen query scope merely to give
every source identical controls. Use actual advertised or retained frames, preserve
gaps and revisions, and distinguish forecast time from observations. Keep Follow
latest visibly different from a pinned historical frame.

A synchronized keyboard-accessible event list and map must resolve the same provider
feature identity into the existing Drawer. Closing it returns focus to the initiating
control. External context selection cannot manufacture an EvidenceBundle. A/B views
retain the camera and disclose both source editions, timestamps, bounds and coverage;
a record appearing after an outage is not necessarily a newly occurring event.

An optional area summary reports returned records alongside missing/stale sources.
Do not count pixels or clusters as provider incidents. Do not infer property exposure,
evacuation routes, travel safety or all-clear conditions. Shared views use the existing
explicit Share action and exclude device geolocation, credentials, private submissions,
restricted geometry and sensitive identifiers. A current-view link is not an immutable
archive unless source editions are pinned and retained.

## Terrain and later wind work

Elevation colors remain unexaggerated DEM heights, distinct from hillshade and slope.
Preserve the existing documented zoom safety cap, labeled vertical exaggeration,
quantitative height legend, desired toggle state across style changes, and finite
failure/retry outcomes. Fixture colors prove renderer behavior only, not source accuracy.

A later wind layer needs a verified source role, vertical level, units, convention,
valid time and resolution. Static arrows serve reduced-motion and low-power modes.
Animation illustrates the supplied field, not measured smoke transport or fire-spread
prediction. Satellite-pass context is later work and may explain opportunities/latency,
not promise detection. Reverify availability and retirement notices before qualification.

## Ordered implementation and acceptance

The identifiers below are document-local work labels, not new GitHub issues or
canonical contract IDs. All implementation packages remain PROPOSED until separately
delivered and verified.

| Package | Work | Required proof |
| --- | --- | --- |
| HZ-01 | Existing earthquake no-data repair | Provider-specific 204; strict invalid/error cases; route and populated-to-empty map replacement |
| HZ-02 | Elevation loading/color repair | Non-flat DEM colors; toggle/style cycles; finite failure/retry; unchanged camera |
| HZ-03 | Radar manifest/image separation | Exact advertised frame; visible image; expired/missing/transparent cases; style reload |
| HZ-04 | Smoke publication/parse/display repair | Populated/empty/partial/failure; exact intervals; strict KML; visible polygon and legend |
| HZ-05 | Compact controls and source health | No second map; desktop/mobile keyboard; no blocked controls; honest status and age |
| HZ-06 | Event list, replay, compare and safe sharing | Same selection identity; focus return; gaps; source/time bindings; privacy negatives |
| HZ-07 | Additional provider qualification | Exact contracts, coverage, rights, sensitivity, bounded fixtures and separate acceptance |

An acceptance packet binds the exact candidate source, browser/WebGL capability,
selected bounds/time, provider response identity, visible result and recovery.
Exercise configured/missing configuration, populated/empty/partial data, malformed,
oversized, slow, failed and expired inputs; retry/unmount; 2D/terrain and supported
globe; opacity/toggle/style changes; keyboard, reduced motion and narrow screens.
Synthetic fixtures remain test-only. Never replace real failures with synthetic
positives, waive validators, or treat a build/HTTP 200/PR merge as hosted acceptance.

## Review and rollback

The owner request authorizes repository authoring and draft-PR delivery, not ready,
merge, deployment or source admission. Preserve issue #4024's path-specific containment
and #4228's Stage 1A accepted / Stage 1B HOLD / Stage 2 unauthorized boundaries.
Human implementation, domain and accessibility review remain pending. Abandon the
unmerged branch or use a separately reviewed inverse after integration; do not
rewrite source history or change the Site to roll back a documentation proposal.
