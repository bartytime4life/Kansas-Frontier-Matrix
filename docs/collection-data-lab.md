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
