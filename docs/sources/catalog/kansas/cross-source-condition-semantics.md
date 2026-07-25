<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-kansas-cross-source-condition-semantics
title: Cross-source condition semantics — USDM, Kansas Mesonet, and KDHE HAB
type: source-semantics-note; documentation-only
version: v0.1.0
status: proposed; no source activation
owners: NEEDS VERIFICATION — source, temporal, spatial, domain, rights, evidence, and release stewards
created: 2026-07-25
updated: 2026-07-25
policy_label: public-review; cite-or-abstain; fail-closed
related:
  - ./README.md
  - ./kansas-mesonet.md
  - ./kdhe-harmful-algal-blooms.md
  - ../drought_monitor/drought-monitor.md
  - ../drought_monitor/CORRECTION-2026-07-25-usdm-cutoff.md
tags: [kfm, source-role, temporal-semantics, spatial-semantics, usdm, mesonet, kdhe]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Cross-source condition semantics

> Relates U.S. Drought Monitor classifications, Kansas Mesonet point-and-depth observations, and KDHE harmful-algal-bloom advisories while preserving each source’s identity, role, scale, time, limitations, and correction lineage.

> [!IMPORTANT]
> Co-location and correlation do not make sources interchangeable. This page authorizes no source activation, live access, derived dataset, release, alert, or publication.

## Source-role matrix

| Source | Native object | Required interpretation |
|---|---|---|
| U.S. Drought Monitor | Weekly D0–D4 broad-scale expert-synthesis classification | Not a forecast, sensor reading, parcel condition, groundwater-recovery finding, crop-loss amount, emergency declaration, or local restriction |
| Kansas Mesonet | Timestamped in-situ station observations by sensor depth | Preserve station, depth, variable, unit, quality state, and station-relative saturation semantics |
| KDHE HAB | Volatile Watch/Warning/Hazard advisory snapshot, possibly zoned | Preserve water-body identity, native level, source vintage, scope, conflicts, and KDHE/local-authority separation |

## Official source snapshot

### USDM

`https://www.droughtmonitor.unl.edu/`

Observed 2026-07-25:

- current map released July 23, 2026;
- data valid July 21, 2026;
- cutoff each Tuesday at 8:00 a.m. EDT; and
- release each Thursday at 8:30 a.m. Eastern Time.

### Kansas Mesonet

- `https://secondary.mesonet.ksu.edu/agriculture/soilmoist/`
- `https://offsite.mesonet.ksu.edu/about/soilmoist/page`

The source exposes volumetric water content, percent saturation, and seven-day change by station and depth. Percent saturation is calculated against each station’s historical dry-to-wet range; it is not one statewide scale.

### KDHE HAB

- `https://www.kdhe.ks.gov/777/Harmful-Algal-Blooms`
- `https://www.kdhe.ks.gov/m/newsflash/home/detail/2059`

The current table and July 24 press release disagree on Kirwin Lake’s county. Preserve both values and emit `IDENTITY_CONFLICT` until governed identity evidence resolves the discrepancy.

## Required temporal fields

| Source | Separate time fields |
|---|---|
| USDM | data cutoff, valid date/interval, release, retrieval, correction, supersession |
| Mesonet | observation, retrieval, quality-control update, station-metadata version |
| KDHE HAB | source update/publication, retrieval, first/last observation, lifting, correction, supersession |

Do not use one generic timestamp. Preserve source-native timezone wording and add normalized UTC only when conversion evidence is explicit.

## Required spatial fields

### USDM

Keep spatial products and aggregate statistics as separate artifacts linked by deterministic release identity. Polygon membership is not parcel truth.

### Mesonet

Keep station identity, coordinate version, sensor depth, variable, unit, missing-sensor state, and quality state. Do not create an interpolated statewide surface without a separately reviewed model and release.

### KDHE HAB

Keep native water-body name, stable identifier or unresolved state, county text, whole-water-body versus zone scope, geometry reference, and geometry confidence. Do not substitute a county polygon or guessed centroid for unresolved geometry.

## Cross-source relation

A derived relation must retain independent source-record identifiers and record:

- relation purpose;
- temporal-overlap method;
- spatial-overlap or nearest-station method;
- scale mismatch and uncertainty;
- source-role compatibility;
- algorithm/version;
- evidence references; and
- correction and invalidation behavior.

Permitted use includes contextual comparison. It must not claim causation or replace one source with another.

## Fail-closed rules

Reject or quarantine any operation that:

- collapses all source times into one timestamp;
- represents USDM as a forecast or local observation;
- omits Mesonet station or sensor depth;
- averages station-relative saturation into a statewide drought class;
- clears an advisory because a row or source retrieval is missing;
- generalizes a zone advisory to an entire water body;
- resolves a water body from name and county alone when official sources conflict; or
- lets a connector or derived relation write release or published authority.

## Rights, evidence, and release

Before automated ingestion, verify access methods, terms, attribution, rate limits, redistribution, and any required written authorization. Unknown rights default to deny or quarantine.

Any cross-source output remains a candidate until source descriptors, immutable evidence, validation, policy, review, release, correction, and rollback gates close. A passing join test is not source admission or publication approval.

## Correction and rollback

See the [USDM cutoff correction](../drought_monitor/CORRECTION-2026-07-25-usdm-cutoff.md) and the [KDHE HAB conflict profile](./kdhe-harmful-algal-blooms.md).

Before merge, close the draft pull request and abandon the branch. After merge, revert only the scoped documentation through review; preserve prior source statements and correction lineage.

[Back to top](#top)
