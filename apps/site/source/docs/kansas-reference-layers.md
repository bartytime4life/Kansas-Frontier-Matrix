# Kansas land-record, transport, and hazard overlays

Local Explorer follow-up, 2026-10-02. Start at **Map layers**. Topic buttons
remain above the scrolling list and can switch from Earth Engine imagery to
**BLM land records**, **Roads, rail & bridges**, or **Hazards** without changing the basemap.
Changing topic clears the previous search. Unrelated Daylight controls appear
only in All sources. Opacity remains under each source's Options.

| Topic | Provider layer | Minimum map zoom |
| --- | --- | --- |
| BLM land records | Kansas PLSS townships / sections / intersected divisions | 8 / 11 / 12 |
| BLM land records | MLRS oil-and-gas lease cases, authorized / closed, direct PLSS matches only | 9 / 9 |
| Roads & rail | KDOT LRS County public road reference | 9 |
| Roads & rail | KDOT active / abandoned railroads, separate switches | 8 / 8 |
| Hazards | FEMA Kansas NFHL flood hazard zones | 14 |

Selected layers below their display scale show **Zoom to layer**, including
when the service has connected but has no tiles at the wider view. The action
keeps a camera already within the Kansas bounds and respects reduced motion.
Regional raster overlays disclose when they need **Use flat map**. Current
references remain held at historical atlas frames; **Use Present** is explicit.
No control silently changes the atlas year to make a layer appear.

Roads and rails use KDOT's unchanged geometry rendered in EPSG:3857, with gold
road lines, cyan active rails, and orange dashed abandoned rails. These colors
are display styling, not provider classifications of road width or severity.
Each survey/transport opacity is preserved independently even with multiple
line-image overlays. Provider errors retain the existing bounded retry and
source-status behavior. Disabled layers do not start imagery requests.

## Source meanings and limits

- [KDOT LRS County](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/LRS_County/MapServer/4)
  is the route reference for Kansas public roads, including state and non-state
  systems. It does not provide live traffic, closures, routing, or road width.
- [KDOT Railroads](https://kanplan.ksdot.gov/arcgis_web_adaptor/rest/services/Transportation/Railroads/MapServer)
  supplies distinct active and abandoned designations. Neither designation
  establishes current train movement, access rights, or the date a track changed.
- [BLM CadNSDI](https://gis.blm.gov/arcgis/rest/services/Cadastral/BLM_Natl_PLSS_CadNSDI/MapServer)
  supplies survey reference, not parcel ownership. Township/division requests
  use `STATEABBR='KS'`; sections use `PLSSID LIKE 'KS%'`.
- [BLM MLRS oil-and-gas lease case disposition](https://gis.blm.gov/nlsdb/rest/services/Fluid_Minerals/Oil_Gas_Leases_Case_Disp/MapServer)
  supplies separate provider-current authorized and closed images. Each requests
  `GEO_STATE='KS'` and only `QLTY` scores 0–3, which BLM identifies as direct
  PLSS matches. The fixed filter omits calculated, section-level, county-level,
  mixed-quality and unmapped cases. On 2026-10-03 the service count under that
  filter was 298 authorized and 139 closed; these are moving service counts,
  not a captured inventory. A PLSS-derived display polygon is not an exact
  lease or mineral-rights footprint. Case status is not drilling, production,
  access, ownership, or a reconstructed history. The Site does not yet provide
  case-level inspection, immutable capture, evidence, or release for MLRS.
  Provider legend and links stay available with each layer; blank map areas do
  not prove an absence of land interests.

BLM mining-claim layers returned zero Kansas cases in the inspected national
service on 2026-10-03. Of five Kansas authorized right-of-way records found in
the inspected service, four were section-level geocodes. Neither family is
presented as a spatial overlay here; both need a source-specific review before
addition. These point-in-time checks are not a claim that BLM has no Kansas
records in other systems.

### On-demand BLM identifier inspection

In each PLSS layer's **Options**, enable the layer in a Present flat-map view and
choose **Inspect map center**. The fixed query asks the same BLM layer and Kansas
filter used for its image overlay. It returns only provider identifiers and
selected source fields: township/first/intersected division ID and label,
principal meridian where supplied, source document date, revision date and
source reference. The `OBJECTID` link opens that BLM ArcGIS survey feature's
attributes; it is not a GLO patent, plat, or field note.
No polygon coordinates, private parcel records or raw provider response are
stored by this Site read. Provider text is displayed as text, not followed as a
link. Missing dates are explicitly unreported; retrieval time is separate.

Each inspected feature now has a manual [official BLM GLO](https://glorecords.blm.gov/)
search handoff. The visible, copyable reference contains only a validated Kansas
PLSS township ID, a provider township label and meridian when available, a
numbered section when the provider calls it a section, and the inspected map
center. Open GLO and search Kansas by its map or land-description controls;
verify any resulting document in GLO. The Site does not assert a document match,
construct an undocumented GLO deep link, download a GLO document, or treat the
PLSS image as a patent footprint. BLM says its GLO collection does not contain
every federal title record. A missing search result is not evidence that no
record or land interest exists.

The server checks a count, then at most ten point-intersecting features in
`OBJECTID` order. Both requests share a 12-second deadline; the count is limited
to 4 KiB and the feature response to 64 KiB. Malformed counts, provider errors,
redirects, inconsistent pages and duplicate identities fail closed. A count
above ten or an out-of-scope record remains visibly partial. The provider may
change between count and feature requests, so this is a current inspection,
not a transactionally frozen inventory. Moving the map, disabling the layer,
canceling, or unmounting discards pending results; prior checked results retain
their original query point. Kansas search bounds are enforced on the server.

BLM's source geometry is a publication grid derived from survey and other
control records. An identifier does not prove ownership, legal description,
title, exact corner position, access or a GLO patent footprint. No reviewed GLO
records or KFM land release are created. Live provider checks on 2026-10-03
returned one township, one section and one intersected record for a Wichita
sample point; that proves only those bounded source responses.

- [FEMA NFHL layer 28](https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer/28)
  is limited to Kansas panel identifiers (`DFIRM_ID LIKE '20%'`). Provider zone
  colors and hatching are retained, with a linked provider legend. Effective
  dates vary by panel. The image is not observed inundation, a warning, or a
  property determination. Check the [FEMA Map Service Center](https://msc.fema.gov/portal/home)
  for effective maps and amendments. Blank coverage is not evidence of no risk.

Existing warnings, radar, smoke, fire, earthquakes, gauges, model guidance,
lightning, and disaster declarations remain separate Hazards choices. Storm
Events and drought/algal-bloom families remain explicitly held. This is not
complete hazard coverage or a safety guarantee.

All these layers are free public service displays and external context only.
No immutable acquisition, historical edition, source admission, evidence release,
or data activation is created. Feature-level dates cannot be inferred from the
date an image tile was fetched. The underlying basemap keeps its own embedded
roads; the new controls govern the additional KDOT overlays.

## Implementation, validation, and recovery

`app/kansas-reference-layers.ts` owns fixed Site display definitions, consumed
by the existing `app/live-context.ts` map renderer and source manifest. Controls
remain in `app/page.tsx`, `app/layer-workspaces.ts`, and the existing layer CSS.
`app/blm-plss-records.ts`, `app/api/blm-plss-records/route.ts` and
`app/blm-plss-inspector.tsx` own the separate on-demand attribute read.
Tests remain in `tests/`; documentation remains here. This reuses the Site
application responsibility under Directory Rules v2 and accepted ADR-0029.
It does not create a parallel source registry or acquisition pipeline.

Focused validation: `node --test tests/kansas-reference-layers.test.mjs
tests/disaster-blm-layers.test.mjs tests/map-composition.test.mjs
tests/temporal-sweep.test.mjs tests/terrain-performance.test.mjs` (one command),
then TypeScript, production build, and the full Site test suite. Tests exercise
separate visibility and opacity, style replacement, globe suppression, scale
guidance, fixed source/filter selection, temporal holds, and source discovery.

Live provider probes on 2026-10-02 returned nontransparent 256-pixel PNGs for
all three BLM layers, all three KDOT overlays, and FEMA near Wichita/Topeka.
The servers returned CORS permission for the local Explorer origin. A separate
FEMA sample was transparent. These checks prove those service responses only;
they do not prove complete coverage or browser rendering. API metadata requests
to FEMA were intermittently reset while the tested image requests succeeded.

Browser acceptance remains separate: the app browser's admin-policy check was
unavailable during this repair. No visual journey is marked passed.

The MLRS slice starts from local source `d3224129c59b05b8134144116790efb049198d72`.
Application rollback restores that source and its saved build after preserving
newer work. The earlier survey/transport slice began at
`b1c92e0dd580ff3cc03847936aefbb88dfae905d`. Neither slice needs a database
migration, credential change, data-store replacement, or source activation.
Hosted publication is separate.
