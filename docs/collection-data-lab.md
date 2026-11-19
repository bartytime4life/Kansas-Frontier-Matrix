# Connected collection metadata and record lab

The Data library links all 189 recovered collections to source metadata,
field roles, related collections, research questions and the record lab at
`/data-lab`. Search includes topics and field names. The machine-readable
`/api/collection-metadata` catalog also describes the existing map layers and
all 22 public relay datasets, including the retained NWM geometry/version hold.
An optional `collection` query selects one known collection; arbitrary table,
SQL and private-store inputs are rejected.

Ten research bundles connect water, weather, infrastructure, historical places,
ecology, geology, communities, environmental records and prepared observations.
Bundles open up to six existing geometry layers together and expose the complete
collection list. Questions are research starting points. They establish neither
causation nor verified row joins. Earthquakes, dams, parks and historical public
lands now carry their previously missed topic memberships.

## Actual record analysis

Loading a collection reads at most five seek pages, at most 250 records, through
the existing bounded archive reader. The response limit, two-reader queue,
cancellation, retained source dates and stale-cache indications remain intact.
The lab labels this as the first identity-ordered records, with unknown collection
totals. It does not describe the sample as representative or statewide coverage.

The profile reports field completeness, eligible numeric values, stored-geometry
availability, returned source IDs, URLs and file digests. Zero stays a value;
nulls, absent fields and blanks stay missing. Numeric identifiers, dates,
coordinates and quality flags are not measurement fields. Measurement units,
parameter identifiers and quality qualifiers form separate summary groups.
Original fill codes and censored values are not silently normalized. A field
summary includes at most twelve groups and explicitly counts additional groups;
the complete loaded source rows remain in the JSON export.

One field and one measurement context can be exported as a GeoJSON layer.
It uses validated longitude/latitude XY geometry, with no geocoding, reprojection
or unit conversion. Source geometry remains unchanged in the record export.
Other contexts, nonnumeric values and missing/invalid geometries are counted
as omissions. Empty layer downloads are disabled.

The research brief includes the question, measured sample scope, recorded value
ranges, example source-time fields, retrieval times, source lineage, exact record
identities and interpretation limits. It and the lab bundle are free downloads.

## Documented FAA fields

The FAA obstacle collection now has definitions for all 31 archived fields.
The [FAA daily format manual, May 21, 2026](https://www.faa.gov/air_traffic/flight_info/aeronav/digital_products/DailyDOF/media/DDOF_README_05-21-2026.pdf)
defines heights in feet and the horizontal/vertical tolerance codes. Accuracy
categories stay out of numeric distributions. AGL and AMSL references and FAA
verification/accuracy categories remain separate in height summary groups and
measurement layers. Unknown codes and original values are retained.

The [FAA FAQ](https://www.faa.gov/air_traffic/flight_info/aeronav/obst_data/odtfaqs/)
explains that quantity can represent an array at a single point. The provider
action date is identified as `YYYYDDD`, not interpreted as a construction or
observation date. KFM-derived coordinates and keys cite the pinned normalizer.
Documentation edition and source-document fingerprint are distinct from the
captured record's edition, retrieval time and AI review credit.

The library dictionary, metadata API, lab JSON, story brief and GeoJSON exports
carry these definitions and their source references. Other collections retain
their explicit unknowns. Previously saved FAA bundles reopen their unchanged
records and question; an obsolete measurement context is reset with a visible
notice. New bundles retain their documented context and dictionary revision.

## Documented USGS water fields

Daily values, field measurements and peaks have sourced definitions for all 54
archived fields, checked against the USGS JSON schemas for
[daily](https://api.waterdata.usgs.gov/ogcapi/v1/collections/daily/schema?f=json),
[field measurements](https://api.waterdata.usgs.gov/ogcapi/v1/collections/field-measurements/schema?f=json)
and [peaks](https://api.waterdata.usgs.gov/ogcapi/v1/collections/peaks/schema?f=json).
The recorded schema fingerprints describe the documentation snapshots, not the
edition or approval of an archived observation.

The value field names `unit_of_measure` as its per-record unit source. Missing
units remain unknown. Field summaries distinguish observing procedures,
sublocations, agencies, control conditions and ratings, in addition to parameter,
reading type, datum, approval and qualifiers. Peak comparison start years stay
separate, and `peak_since` is a time field rather than a numeric measurement.
Water year, calendar year, partial peak dates, observation time, provider refresh
and archive retrieval time retain their different meanings. No unit conversion,
date completion or AI review is inferred.

Earlier pooled field/peak bundles retain their records and question and show a
selection-reset notice. Compatible daily selections remain intact. New documented
contexts reopen exactly; altered contexts are rejected. Exports carry unit sources,
field definitions and citations. Map derivatives use per-row units when stored
geometry is available; this change does not fabricate missing map geometry.

## Station and series context

The station and series dictionaries document all 50 archived fields using the
USGS [combined metadata](https://api.waterdata.usgs.gov/ogcapi/v1/collections/combined-metadata/schema?f=json),
[monitoring-location](https://api.waterdata.usgs.gov/ogcapi/v1/collections/monitoring-locations/schema?f=json)
and [time-series](https://api.waterdata.usgs.gov/ogcapi/v1/collections/time-series-metadata/schema?f=json)
schemas, the [site-unit reference](https://waterservices.usgs.gov/docs/site-service/site-service-details/)
and the pinned KFM field mapping. Aliases identify provider names such as `id`,
`primary`, `begin` and `end`. Altitude uses each row's vertical datum, with unknown
references left unknown; depths and drainage areas retain documented units.
Original horizontal datum and station timezone metadata do not trigger coordinate
or observation-clock conversions. Period boundaries may contain gaps or lag new
observations. Flags and operational thresholds remain metadata.

**Station and series context** links five USGS collections through twelve
documented comparison plans. They expose provider-key namespaces and checks for
captured versions, parameters, units, datums and periods. They do not execute a
record join or choose a current metadata version. Field-measurement series IDs
are kept separate from the daily/peak series namespace.

The lab and brief distinguish provider identity from capture-file/row identity.
Loaded-sample counts expose repeated provider identities and missing keys while
retaining every original row. These counts are not deduplicated station totals.
The metadata API and JSON/story exports carry the same plans and counts. Older
station/series bundles keep their records and question, with an explicit notice
when a former measurement selection now has documented units or metadata roles.

**Reopen a saved lab bundle** reads the file in the browser and restores its
record sample, question, field, context and selected interval where present.
Older JSON downloads reopen their record sample and question. The app checks
record identities, bounds and any saved interval before replacing the current
view. Opening a file makes no archive request. Subsequent exports identify
the file as their input and qualify its supplied source descriptions.

The method is deterministic browser computation. These outputs do not establish
AI review, approval, release or publication. Private intake review credits and
the original data remain unchanged. Unknown definitions, rights, units, CRS,
coverage and review metadata are explicit rather than guessed.

## Local verification and delivery

Run `node --test tests/collection-integration.test.mjs tests/recovered-records.test.mjs
tests/archive-layers.test.mjs`, TypeScript, targeted ESLint and the production
build. Local operational records retain the prior unpublished-source baseline and
real-relay browser checks. The PR carries these additions onto the current
hosted-app branch, preserving its text search, freshness display, record
comparison, URL filters and focus behavior. Topic membership is updated in the
existing shared recovered-topics module.
Do not infer production deployment from a local build or preview. The existing
GoDaddy composition and original Sites preservation rules still apply.

The second inspection added the missing OSM place/building research bundle,
quality-separated statistics, explicit XY-derivative labeling, source-time
examples in briefs, and reliable navigation between collection selections.
