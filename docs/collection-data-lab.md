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
