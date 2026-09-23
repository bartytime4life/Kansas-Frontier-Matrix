<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/kgs-berkeley-seismic-source-map
title: KGS and Berkeley seismic source qualification for KFM
type: source-map
version: v0.1.0
status: proposed; discovery-only; no-source-activation
owners: ["@bartytime4life"]
created: 2026-09-23
updated: 2026-09-23
policy_label: public; context-only; not-alerting; rights-review-pending
owning_root: docs/
responsibility: Place the user-nominated KGS and Berkeley resources alongside USGS without conflating catalogs, felt reports, station imagery, waveforms or source rights.
truth_posture: CONFIRMED public resource descriptions; PROPOSED KFM use; NEEDS VERIFICATION payload and hosted acceptance
[/KFM_META_BLOCK_V2] -->

# KGS and Berkeley seismic source qualification for KFM

## Scope and provenance

The owner nominated the [USGS map](https://earthquake.usgs.gov/earthquakes/map/),
[Berkeley map](https://earthquakes.berkeley.edu/seismo.real.time.map.html), and
[Kansas Geological Survey earthquake hub](https://www.kgs.ku.edu/Geophysics/Earthquakes/index.html).
This is a source-discovery and implementation-handoff document, not a
SourceDescriptor, admission decision, acquisition permission or public release.
Public descriptions were read on 2026-09-23 UTC; indexing or retrieval time does
not establish the most recent observation or uninterrupted provider operation.

The [USGS offline workflow](../../runbooks/usgs-earthquake-live-history.md) is the
implemented code slice. The existing
[USGS source-family pointer](../../sources/catalog/usgs/earthquake-catalog.md)
remains intact. There is no new KGS or NCEDC client, payload parser, source
activation, station subscription, deployment or alternative connector root here.

## Kansas-first source roles

| Resource | Proposed use in KFM | Keep separate |
|---|---|---|
| USGS recent feeds and dated event queries | Broad recent context and bounded historical catalog candidates for Kansas and surrounding regions. | Preferred catalog solutions, product revisions and source networks; not exhaustive detections or alerts. |
| KGS recent event listing | Kansas local-network context and event links; validate source IDs and update behavior before automation. | KGS event identity versus any matching USGS ID. |
| KGS historical recorded-earthquake workbook | Historical seismicity investigation after workbook-specific validation. | Instrumental/compiled events versus narrative felt reports. |
| KGS historical felt-report workbook and historical publications | Stories, historical perception and intensity context with original date/location uncertainty. | Reporting locality versus epicenter; intensity versus magnitude; report count versus event count. |
| KGS station pages | Provider-owned seismogram links and explanation of Kansas monitoring. | Display images versus digital waveform samples or calibrated ground motion. |
| Berkeley map and NCEDC | Interface reference and separately scoped Northern California comparison/research. | Display carrier versus a catalog service; NCSS/BDSN/DD solutions and waveform products. |

Do not replace one missing source with invented points or silently add source
counts. An association table must preserve both provider IDs, versions, method,
confidence and reviewer decision. Nearby time/space alone is a candidate match,
not proof of identity, independent corroboration or causation.

## KGS: concrete discovery

The [recent listing](https://chasm.kgs.ku.edu/ords/elog.quake5.DisplayQuake2)
exposes provider IDs, UTC/local dates, coordinates, magnitude, county and map
links. It is a short human-facing listing; no stable bulk-API contract, exhaustive
window or guaranteed latency was established. Do not scrape it as a substitute
for the catalog request path or treat its last displayed event as a heartbeat.

The [historical page](https://www.kgs.ku.edu/Geophysics/Earthquakes/historic.html)
links `Historic_Kansas_Felt_Reports.xlsx` and
`Historic_Kansas_Recorded_Earthquakes.xlsx` under a March 18, 2020 page update.
That is a page date, not a verified first/last observation or a frozen dataset
version. It also identifies the 1867-1977 intensity publication and the 1977-1989
Kansas/Nebraska microearthquake report. Those publication intervals must not be
assigned to either spreadsheet without reading its contents.

The spreadsheet download links could not be retrieved through the web tool in
this session; container network access also failed DNS resolution. Workbook
bytes, row counts, headers, date coverage, CRS, time zone and hashes are therefore
**NOT VERIFIED**. No guessed CSV schema, fabricated rows, copied figures or
spreadsheet-derived numeric finding is included in this PR.

For a future workbook receipt: capture the actual linked download URL, unmodified
bytes and SHA-256; inspect sheet names, headers, formulas/external links, blank
and invalid rows, date precision, original time zone, coordinate meaning and
rights notices. Use a non-executing reader. Create separate fixture-backed
adapters only after the real schemas are available. Never interpret a missing
coordinate or date as zero, or place a report locality at an inferred epicenter.

The [full network catalog](https://www.kgs.ku.edu/Geophysics/Earthquakes/data.html)
is requested using a form with name/email and optional organization, date,
magnitude and county fields. The page describes an emailed CSV download link,
typically within 24-48 hours. This is an operator request boundary, not an
anonymous FDSN endpoint. No form was submitted, contact detail transmitted,
mailing-list subscription created, or promised delivery inferred. Import a
received export only after its exact fields, scope and use conditions are checked.

The [network page](https://www.kgs.ku.edu/Geophysics/Earthquakes/network.html)
describes vertical, east-west and north-south station images with half-hour
lines and a three-minute image refresh. A displayed trace does not establish a
new earthquake, location, magnitude, causal source or calibrated amplitude.
Use provider links until raw channels, sample rates, time/response metadata,
units, data gaps and reuse terms are separately qualified. No conversion of
images into fabricated numeric waveforms is permitted.

## Berkeley and NCEDC

Berkeley's map describes a past-week view, magnitude-sized circles, observation
age categories and computer-local time. These are useful design references;
KFM should retain an explicit UTC view and not use marker age as a service-health
signal. This review did not verify the JavaScript map's underlying fetch URLs,
so the page and NCEDC are associated research resources, not a proven identical
transport implementation.

The current [NCEDC FDSN service](https://service.ncedc.org/fdsnws/event/1/)
documents QuakeML, text and GeoJSON, with NCSS as its default catalog, bounded
query parameters and explicit `nodata` behavior. Its older
[help page](https://service.ncedc.org/fdsnws/event/help/index.html) mentions XML/text
only; use the current service contract and actual response validation rather
than blindly copying the older format list or reusing the USGS parser.

The [catalog search notice](https://www.ncedc.org/ncedc/catalog-search.html)
warns about the hosted double-difference catalog's depth datum and points to a
separate current DD catalog. DD is **not selected**. Do not combine DD and NCSS
depths, infer terrain-relative depths, or silently follow a new provider. Any
future choice must pin catalog, producer, method, datum, time interval and terms.

[NCEDC DART](https://www.ncedc.org/ncedc/about-the-dart.html) distinguishes recent
MiniSEED time series from instrument-response metadata. A waveform branch must
retain network/station/location/channel, epoch, gaps and response identity; raw
counts are not corrected velocity or acceleration. This does not clear KFM's
separate Raspberry Shake waveform/provider holds.

## Rights, attribution and public exposure

[KGS terms](https://www.kgs.ku.edu/General/copyright.html) permit use and copying
subject to retained notices and required attribution. The required attribution
is: "The source of this material is the Kansas Geological Survey website at
http://www.kgs.ku.edu/. All Rights Reserved."

[KGS publishing guidance](https://kgs.ku.edu/kgs-publishing-policy-and-guidelines)
adds specific restrictions for publication images and illustrations, including
commercial reuse. Those assets are not copied here. Review terms per downloaded
artifact; do not label all KGS or university content public domain or transfer
USGS rights assumptions to it. This document is not a legal clearance decision.

NCEDC requests dataset acknowledgement, including DOI `10.7932/NCEDC`; the
[catalog page](https://www.ncedc.org/ncedc/catalog-search.html) supplies the citation.
Preserve any additional catalog/network/product references with future data.
No endorsement, release permission or independent review is inferred from a
publicly reachable webpage.

## Product work after qualification

Implement source-specific recent/history controls in the existing map/list/
Evidence Drawer, not a duplicate Site. Preserve camera, event selection, layer
opacity and source/time legends. Reports should include catalog/provider,
origin/update/retrieval times, exact query or archive identity, missing intervals,
source-role caveats, and unresolved overlaps. A historical story may cite a felt
report without turning it into an instrumented earthquake observation.

Potential geology and infrastructure comparisons need separately admitted
spatial/time inputs. Proximity to a fault, well, mine or asset is not proof of
induced seismicity, damage or individual facility risk. KFM must not issue an
all-clear, predict the next earthquake, or replace official emergency guidance.

## Open gates and rollback

KGS payload schemas, artifact-specific rights, operational acquisition and source
placement remain pending. NCEDC catalog/format/producer/coverage qualification
and waveform response handling remain pending. Cross-catalog association,
historical completeness, positive governed API/map evidence and authenticated
Site acceptance remain pending for all three sources.

This intake adds no code under disputed KGS compatibility roots and does not
resolve their placement by assertion. Before adding a KGS implementation, read
current owning-root decisions and reconcile its SourceDescriptor and tests.
Rollback is an ordinary reviewed document inverse while retaining the authoring
receipt. Existing provider policies, historical evidence, #4024 containment and
#4228 authority boundaries remain unchanged.
