<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/hydrology/nwis-county-capture
title: USGS Water Data County Capture Manifest Contract
type: semantic-contract
version: v0.1.0
status: proposed-captured-input-profile
owners: OWNER_TBD — Hydrology steward · USGS connector steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; captured-input-only; no-network; non-authoritative
owning_root: contracts/
responsibility: Define the bounded meaning of a county-scoped modern USGS Water Data capture manifest without performing transport, admission, evidence closure, or publication.
truth_posture: cite-or-abstain
related:
  - ../../../connectors/usgs/water_data/nwis_county_capture.py
  - ../../../schemas/contracts/v1/domains/hydrology/nwis_county_capture_manifest.schema.json
  - ../../../fixtures/connectors/usgs/water_data/nwis_county_capture/valid_capture.json
  - ../../../docs/intake/exploratory/pass-32-nwis-county-capture-source-map.md
  - usgs_water_api_cutover.md
[/KFM_META_BLOCK_V2] -->

# USGS Water Data County Capture Manifest

**Status:** `PROPOSED` captured-input profile

## Purpose

Define a deterministic, offline normalization boundary for county-scoped monitoring-location metadata and daily values already captured from the modern USGS Water Data OGC API.

The helper follows the current official two-stage pattern: query `monitoring-locations` for a county, then query `daily` using the resulting monitoring-location IDs. It plans one credential-free daily request per location to avoid ambiguous multi-value encoding. Pagination is complete only when every non-final page has exactly one safe `rel=next` link and the final page has none.

## Preserved meaning

- Monitoring locations are `ADMINISTRATIVE` source material, not observations.
- Daily values are `AGGREGATE_DAILY`, not instantaneous readings.
- `Approved` and `Provisional` remain distinct values; neither is coerced.
- Decimal observation values remain source strings to preserve precision.
- Parameter code, statistic ID, date, unit, qualifier, last-modified timestamp, time-series ID, monitoring-location ID, county, and captured-page digests remain explicit.
- Exact captured page content is bound by SHA-256; normalized output intentionally does not reproduce source geometry.

## Modern API request plan

The plan uses only `https://api.waterdata.usgs.gov/ogcapi/v0/collections/.../items`, emits `f=json`, explicit query fields, bounded page limits, and `FOLLOW_REL_NEXT_UNTIL_ABSENT`. It never embeds an API key. A later authorized transport adapter may inject credentials from runtime configuration, but this helper cannot read credentials or perform transport.

## Fail-closed rules

Normalization fails for incomplete/unsafe pagination, duplicate features, cross-county locations, location-ID mismatches, unknown or missing daily captures, cross-location observations, request parameter/statistic drift, out-of-window dates, non-decimal values, unsupported approval states, timezone-free last-modified values, duplicate JSON keys, non-finite JSON, symlinks, or oversized input.

## Trust boundary

A valid manifest proves only deterministic shape, source-role separation, request/capture binding, and internal closure for supplied bytes. It does not prove that transport occurred, an API response is authentic/current, a source is activated, rights are clear, RAW admission happened, hydrologic interpretation is correct, evidence is resolved, or any promotion, release, warning, operational decision, publication, or public use is authorized.

## Rollback

Remove this contract and its paired connector helper, schema, fixture, tests, workflow, source map, README update, and generated receipt. The slice creates no network, lifecycle, registry, release, or public state.
