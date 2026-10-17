# Almanac source references

The owner requested information from both Farmers’ Almanac
(`farmersalmanac.com`) and The Old Farmer’s Almanac (`almanac.com`). The two
publishers remain separate source identities. Current evidence was checked on
2026-10-14 UTC against their public pages, the Farmers’ Almanac FAQ, Yankee
Publishing’s terms and the Library of Congress collection/item metadata.

## Implemented material

The `/almanacs` library contains 13 source references with publisher, subject,
information kind, geographic scope, edition/time label, access result, source
URL, reuse reference and limitations. Publisher/subject/search filters are
local browser projections and make no requests to the publishers. Direct
links from Weather, Agriculture, Sky and History topic guides, the topic index,
About and Source observatory make the library discoverable.

Two exact source images are displayed with credits and original-source links:

| Carrier | Source identity and rights basis | Integrity |
| --- | --- | --- |
| Farmers’ Almanac winter 2026–2027 map | Publisher’s [winter page](https://www.farmersalmanac.com/farmers-almanac-2026-2027-winter-weather-forecast); [FAQ](https://www.farmersalmanac.com/frequently-asked-questions) permits credited weather-map sharing with a link back | 95,630 bytes; SHA-256 `0f8989f55b70f41eac508c0760841f9438c9c51c532fe9f4c7f5d97d90042a09` |
| Old Farmer’s Almanack advertised 1861 edition title page | [LOC image 1089](https://www.loc.gov/resource/rbccpmat.copy0035/?sp=1089), [collection/item 2019713447](https://www.loc.gov/item/2019713447/) and its rights statement identify Early Copyright Records Collection contents as free to use and reuse | 75,706 bytes; SHA-256 `2b216b8c14ae7ecaebacf2257cef3b19719e4d1e601afdc771e80dbeacfcf8d7` |

The total new image payload is **171,336 bytes**. Originals were bounded to
4 MiB and 2 MiB respectively, inspected visually, hashed and copied unchanged.
Their original asset URLs, bytes, dimensions, credit and rights basis remain in
the app’s display metadata. Source/rights readbacks and acquisition integrity
evidence are retained in the task-local sibling evidence directory, outside
the app and deployment tree.

The publisher weather map retains its copyright and narrow sharing permission.
The repository's code license grants no additional rights to that third-party
image; its credit, source link and reuse reference travel with the display.

The weather image is a commercial seasonal outlook, with unverified drawn
region geometry. It is a reference image, not a georeferenced map layer,
observation, calibrated probability, emergency warning or evidence release.
The LOC carrier is a deposited title page from 1860 advertising the 1861
edition, not a full issue. The collection warns that deposited title pages can
describe altered or unpublished works. Its Boston/New England scope is not
silently converted to Kansas. The modern Yankee Publishing source and
historical publisher Swan, Brewer & Tileston remain distinct.

## Restricted modern material

[Yankee Publishing terms](https://ypi.com/terms-of-use/), sections 3, 4 and 9,
restrict copying and automated collection. Modern Old Farmer’s Almanac tables,
forecast text, calendar timestamps and artwork are therefore not imported.
The Farmers’ Almanac FAQ’s map-sharing permission is not generalized to other
images, entire articles, calendars or bulk data. Membership material stays at
the publisher. No open bulk API or redistribution license was verified for
the modern calendars.

The library provides original KFM bibliographic descriptions and source links
for these resources. A failed Wichita weather-page check (HTTP 403) remains
visible as not acquired. No alternate location or stale forecast substitutes
for it. Regional pages and editions retain their independent time scopes.
Traditional lunar gardening, astronomy, frost baselines, publisher predictions
and historical material are not collapsed into one scientific weather layer.

The two Source observatory candidates remain `held` for modern data ingestion.
Neither this library nor private application deployment creates source
admission, an EvidenceBundle, review approval, layer activation or data release.
No publisher account, subscription, credentials, scraper, D1/R2 migration,
automatic acquisition, report/AI inclusion or canonical source registration is
introduced. Modern data import needs source-specific written permission and
supported access, followed by KFM identity, rights, validation, provenance,
sensitivity, review and release gates.

## Placement and rollback

Current Directory Rules v2, accepted ADR-0029 and same-Site preservation
instructions provide the placement basis. This is deployable app presentation
under the standalone Site’s existing `app/`, `public/`, `tests/` and `docs/`
homes, equivalent to containment inside `apps/site/source/` in the monorepo.
`app/almanac-resources.ts` is app bibliographic/display metadata, not a second
canonical registry, contract, policy, schema or released-data home. `public/almanacs/`
contains only the two bounded, credited display carriers. Synced project
`sources/` and private data stores remain unchanged.

Validation covers source/rights identity, asset bytes/digests, link-only
exclusions, held source candidates, access failures, local filters, topic
navigation and browser rendering. Rollback is previous same-Site version v260
or a source revert; no data migration is required.
