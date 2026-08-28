<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-sources-catalog-drought-monitor-correction-2026-07-25-cutoff
title: USDM data-cutoff correction — 2026-07-25
type: correction-record; source-documentation; temporary
version: v0.1.0
status: active documentation correction; product-page in-place repair pending
owners: NEEDS VERIFICATION — Drought Monitor source steward + docs + temporal/evidence stewards
created: 2026-07-25
updated: 2026-07-25
policy_label: public-review; correction; cite-or-abstain
current_path: docs/sources/catalog/drought_monitor/CORRECTION-2026-07-25-usdm-cutoff.md
truth_posture: >
  CONFIRMED official current cutoff, release cadence, current map release/valid
  dates, and stale repository claim / PROPOSED downstream field model /
  NEEDS VERIFICATION in-place product-page correction, source activation,
  rights, connector behavior, fixtures, validators, release, and publication
related:
  - ./README.md
  - ./drought-monitor.md
  - ../kansas/cross-source-condition-semantics.md
  - ../../../../connectors/drought-monitor/README.md
tags: [kfm, drought-monitor, usdm, correction, temporal-semantics, cutoff, release, supersession]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USDM data-cutoff correction — 2026-07-25

> Temporary, explicit correction record for one stale temporal claim in [`drought-monitor.md`](./drought-monitor.md). This record has no connector, source-activation, data, release, or publication effect.

> [!CAUTION]
> The product page currently states a Tuesday cutoff of `7:00 a.m. Eastern`. The official current U.S. Drought Monitor page states that the data cutoff is each Tuesday at **8:00 a.m. EDT**. Until the product page is corrected in place and validated, consumers must treat the old value as superseded by this correction record.

## Corrected claim

| Field | Stale repository statement | Correct official statement observed 2026-07-25 |
|---|---|---|
| Data cutoff | Tuesday `7:00 a.m. Eastern` | Each Tuesday `8:00 a.m. EDT` |
| Release | Thursday release | Each Thursday `8:30 a.m. Eastern Time` |
| Current map release | Not part of the stale field | July 23, 2026 |
| Current data-valid date | Not part of the stale field | July 21, 2026 |

Official source:

`https://www.droughtmonitor.unl.edu/`

The source-native wording and timezone labels should be preserved. A normalized UTC instant may be added only with explicit timezone evidence for that release.

## Why the distinction matters

USDM is a weekly broad-scale expert-synthesis assessment. These times answer different questions:

- **data cutoff** — latest ordinary evidence window used for the weekly analysis;
- **valid date** — date represented by the map;
- **release time** — when the product becomes available;
- **retrieval time** — when KFM captured the artifact;
- **correction time** — when the source replaced or corrected a released artifact; and
- **supersession time** — when a later release became preferred for current-state use.

Collapsing them into one timestamp can assign evidence to the wrong weekly release, hide latency, and break correction or replay.

## Required future fields

A governed USDM release profile should preserve:

```yaml
source_release_id: deterministic
source_data_cutoff_at: source-native plus normalized instant
source_valid_date: date or explicit interval
source_released_at: source-native plus normalized instant
retrieved_at: kfm capture instant
corrected_at: optional
superseded_at: optional
supersedes_release_id: optional
source_locator: exact official distribution
content_digest: immutable artifact digest
native_format: explicit
geometry_metadata: explicit for spatial artifacts
attribution: exact reviewed value
```

## Artifact separation

Do not collapse:

- polygon or raster spatial products;
- aggregate statistics;
- legends or rendered map images;
- impact markers;
- narrative text; and
- correction notices

into one record type.

Artifacts from the same weekly cycle may share a deterministic release identity while retaining distinct artifact identities, formats, digests, and validation.

## Authority boundary

This correction does not:

- admit or activate a SourceDescriptor;
- authorize live network access;
- validate an endpoint or license;
- fetch or store source bytes;
- create RAW, QUARANTINE, PROCESSED, catalog, triplet, proof, release, or published objects;
- make a drought forecast;
- infer parcel, field, groundwater, reservoir, crop-loss, emergency, or legal conditions; or
- approve public use.

Issue #1645 tracks the larger governed ingestion-profile implementation.

## Validation and closure

Closure requires:

1. an in-place correction of the stale field in `drought-monitor.md`;
2. review of every other cutoff/cadence reference in the repository;
3. no-network temporal fixtures;
4. deterministic release-identity tests;
5. separate spatial-artifact and aggregate-statistics tests;
6. source-rights and attribution review; and
7. explicit correction of any downstream generated documentation that copied the stale value.

After closure, retain this record as correction history or mark it superseded; do not delete the evidence of the prior error.

## Rollback

Before merge, close the draft pull request and abandon the branch. After merge, revert this correction record only through a reviewed pull request. A revert does not make the old `7:00 a.m.` value correct.

[Back to top](#top)
