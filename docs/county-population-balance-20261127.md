# County population accounting — 2026-11-27

## User outcome

County Observatory now offers a source-backed accounting view of annual population
change for the same A/B counties and Population year already selected in the
workspace. It adds no route, duplicate catalogue, source fetch or selection state.
The existing investigation link and notebook selections reproduce the analysis;
the global analysis receipt and printed report include its calculations.

The four signed contributions are births, negative deaths, net migration and a
**calculated balance remainder**. Their sum equals the difference between the two
July 1 population estimates. Natural change is a subtotal of births minus deaths
and is never added again.

Two signed waterfalls and exact tables keep the counts visible. Normalized values
use 1,000 times each contribution divided by the mean of the beginning and ending
July 1 estimates. Counts and rates appear together. The history/CSV covers both
selected counties over the five complete intervals ending 2021–2025.

## Source and meaning

Use only the existing public census-mosaic bundle:
public/labs-data/census-mosaic-a3c82ebd5d89619c.json.
Its manifest binds 223,032 bytes, 630 rows, and SHA-256
a3c82ebd5d89619c498db370861f1288eed6199c3ae8ec0407aea999410c7399.
That is 105 Kansas counties × six July 1 estimates in 2020–2025, from Census
Population Estimates Vintage 2025, captured November 16, 2026.

For an interval ending in year y:

- estimate change = population[y] − population[y−1]
- natural change = births[y] − deaths[y]
- calculated balance remainder = estimate change − births[y] + deaths[y] − netMigration[y]
- mean population = (population[y−1] + population[y]) / 2
- contribution per 1,000 mean residents = contribution × 1,000 / mean population

Endpoint estimates are dated July 1. Annual component counts cover July 1 of the
prior year through June 30 of the selected year. The mean-population denominator
follows the [Census county file-layout definition](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2025/CO-EST2025-ALLDATA.pdf).
These normalized values are calculated by KFM from retained counts; they are not
independently captured Census rate fields.

The retained snapshot omits the published residual column. The displayed remainder
is derived from its retained fields, not a separately observed or imported Census
residual. The [Census terms](https://cdn.www.census.gov/programs-surveys/popest/about/glossary/state-and-county.html)
explain why total change can include an amount outside the named demographic
components. This view does not attribute that remainder to migration or a cause.

2020 is unavailable for reconciliation: its component window is partial and the
bundle has no 2019 July 1 estimate. Missing or duplicate endpoints, malformed
counts and inconsistent natural-change fields prevent an invented balance.
No missing values are filled. Negative migration and remainder remain signed;
zero remains a real zero.

The same vintage can revise earlier estimates. Migration is a net balance, not
arrivals, departures, individual tracking, or separate domestic/international
flows. The visual is descriptive accounting, not a causal analysis. Contributions
are not shown as percentages of net change.

## Checkable example

For Sedgwick County in the 2025 interval:

534,386 → 538,433 is +4,047 people.

+6,645 births − 5,093 deaths + 2,447 net migration + 48 calculated remainder
equals +4,047. The mean-population denominator is 536,409.5 people.

The snapshot contains 525 complete county/year intervals; 422 have a nonzero
derived remainder. Those remainders must remain visible.

## Integration and evidence

Source: isolated hosted branch based on ad5065d47f25073b296dc5288ed586897bc36ad7,
then integrated with hosted 3b39f7fcf1388f3bf5741e69fac5335db1ab0ff7.
The owner's Tornado Season Lab and its discovery entries remain in the candidate.
The existing four-source County Observatory loader retains bounded reads, exact
manifest bytes/hash/schema checks, and source availability behavior. Private CSV
values do not enter the population balance. Existing public exports remain free.

The addition is discoverable through the County Observatory navigation and the
Science/Research directory descriptions. Existing county profiles, history, peers,
private CSV, shared views and notebook behavior remain in place.

Meaningful validation includes all 525 exact accounting identities, independently
calculated sample values/rates, unavailable and duplicate/inconsistent cases,
CSV/receipt/print agreement, actual public snapshot binding, native A/B and year
changes, shared-view reopening, the partial 2020 state, and three browser sizes.
The pre-integration population candidate passes the production build, TypeScript,
changed-area ESLint, and the complete standalone Node 24.11.1 suite:
3,974 passed, 25 skipped, zero failed. The earlier build-identity mismatch while
a CSS change was being built remains in the local diagnostic log; the subsequent
frozen-input build and full suite pass. Final integrated CI and rendered
three-size browser acceptance are pending at receipt authoring and are recorded
separately in the delivery record when complete.

The formal screenshot audit is unavailable because Chrome attachment is blocked.
No different-provider visual evaluator agent is available in the current browser
environment. Independent code review and fresh CI screenshot inspection are
separate evidence and are not described as either of those evaluations.

No data import, source admission, dataset release, hosting settings, routing,
credentials, original Sites bindings or persisted-data migration is part of this
addition. Public delivery requires fresh site readback after repository delivery.
