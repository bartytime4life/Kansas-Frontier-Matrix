# AgricultureObservation source map

Status: confirmed source map for a proposed fixture-only contract  
Recorded: 2026-08-10

## Source-to-implementation trace

| Source | Source idea | Repository expression | Truth label |
| --- | --- | --- | --- |
| Supplied *Kansas Frontier Matrix Implementation Reference* | `AgricultureObservation` carries county FIPS, farms, acres, sales class, crop/livestock indicators, and vintage; align with NASS and historical agricultural schedules. | One county-year aggregate observation with explicit farm, acreage, sales, crop, and livestock measure families; digest-bound source unit and classification references. | `PROPOSED` |
| Supplied Pass 20 Part 2 idea atlas, `KFM-IDX-APP-008` | `CountyYearPanel` is backed by `AgricultureObservation` alongside population, economic, access, and geography-version objects. | A standalone digest-addressable evidence object compatible with the panel's `AGRICULTURE` observation slot. | `PROPOSED` |
| Connected Drive architecture brief and repository directory governance | Keep contracts, schemas, fixtures, validators, tests, workflows, source maps, and receipts in their governed homes. | Seven governed artifacts plus a generated authoring receipt; no competing agriculture-domain definition. | `CONFIRMED` |
| Current repository `CountyYearPanel` profile | Panel slots retain observation references and posture rather than embedding source-specific records. | This profile supplies the referenced observation semantics without modifying the panel contract. | `CONFIRMED` |

## Deliberate boundaries

The source wording is broader than this first implementation. This packet does
not connect to NASS, interpret historical schedules, infer a farm or producer,
normalize source taxonomies, calculate frontier status, or create a production
dataset. Those actions require separately reviewed connector, crosswalk,
classification, evidence, and release authority.

The fixture values and references are synthetic conformance material. They are
not Kansas agricultural claims.

## Repository reconciliation

At authoring time, exact object, path, branch, and pull-request probes found no
`AgricultureObservation` implementation or same-purpose open pull request. The
existing agriculture `DomainObservation` remains domain-owned and unchanged;
this cross-domain county-year aggregate is placed with the existing population
and economic evidence profiles.

