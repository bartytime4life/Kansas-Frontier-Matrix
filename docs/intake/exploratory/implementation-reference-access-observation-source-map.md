# AccessObservation source map

Status: confirmed source map for a proposed fixture-only contract  
Recorded: 2026-08-10

## Source-to-implementation trace

| Source | Source idea | Repository expression | Truth label |
| --- | --- | --- | --- |
| Supplied *Kansas Frontier Matrix Implementation Reference* | `AccessObservation` carries travel time, provider presence, service indicators, and method and is useful for policy-oriented frontier analysis. | One county-year aggregate observation with travel-time, distance, provider-count, and service-coverage families plus digest-bound method posture. | `PROPOSED` |
| Supplied Pass 20 Part 2 idea atlas, `KFM-IDX-APP-008` | `CountyYearPanel` is backed by `AccessObservation` alongside population, economic, agriculture, and geography-version objects. | A standalone digest-addressable evidence object compatible with the panel's `ACCESS` observation slot. | `PROPOSED` |
| Connected Drive architecture brief and repository directory governance | Keep contracts, schemas, fixtures, validators, tests, workflows, source maps, and receipts in their governed homes. | Seven governed artifacts plus a generated authoring receipt; no competing roads-domain restriction definition. | `CONFIRMED` |
| Current repository `CountyYearPanel` profile | Panel slots retain observation references and posture rather than embedding source-specific records. | This profile supplies the referenced observation semantics without modifying the panel contract. | `CONFIRMED` |

## Deliberate boundaries

The source wording is broader than this first implementation. This packet does
not run a routing engine, retrieve provider locations, determine eligibility or
live availability, issue emergency advice, evaluate policy, calculate frontier
status, or create a production dataset. Those actions require separately
reviewed connector, method, evidence, policy, and release authority.

The fixture values and references are synthetic conformance material. They are
not Kansas service-access claims.

## Repository reconciliation

At authoring time, exact object, path, branch, and pull-request probes found no
`AccessObservation` implementation or same-purpose open pull request. The
roads, rail, and trade `AccessRestriction` remains domain-owned and unchanged;
this cross-domain county-year aggregate is placed with the existing population
and economic evidence profiles.

