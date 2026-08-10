<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-nwis-county-capture-source-map
title: Pass 32 NWIS County Capture Source Map
type: source-adaptation-record
version: v0.1.0
status: draft
owners: OWNER_TBD — Hydrology steward · USGS connector steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; captured-input-only
owning_root: docs/
responsibility: Record how Pass 32 KFM-P32-PROG-0010 and its Drive source were narrowed to a no-network modern USGS Water Data capture normalizer.
truth_posture: cite-or-abstain
related:
  - ../../../contracts/domains/hydrology/nwis_county_capture.md
  - ../../../connectors/usgs/water_data/nwis_county_capture.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 32 NWIS County Capture Source Map

## Candidate

Pass 32 card `KFM-P32-PROG-0010` proposes a small county-scoped NWIS fetcher that writes source-pinned hydrology inputs for validation. The Drive document `New Ideas 5-17-26` adds fixed-time, bounded-retry, explicit-fill, EvidenceBundle, and public-runtime cautions.

Those sources are proposals. Their example legacy `waterservices.usgs.gov/nwis/dv` transport is not copied into this implementation.

## Current primary-source reconciliation

USGS now documents the modern Water Data OGC API at `api.waterdata.usgs.gov`:

- legacy `/nwis/dv` maps to the `daily` collection;
- site metadata maps to `monitoring-locations`;
- a county workflow first queries monitoring locations, then uses their IDs to query the desired data collection;
- `county_code`, `monitoring_location_id`, `parameter_code`, and `statistic_id` are queryable;
- date/interval filtering uses RFC 3339/ISO 8601 `datetime` values;
- result pagination follows `rel=next` until absent; and
- daily values preserve value as a string, unit, approval state, qualifier, and last-modified time.

Official references inspected on 2026-08-10:

- `https://api.waterdata.usgs.gov/docs/ogcapi/`
- `https://api.waterdata.usgs.gov/docs/ogcapi/migration/`
- `https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/queryables`
- `https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/queryables`
- `https://api.waterdata.usgs.gov/ogcapi/v0/collections/monitoring-locations/schema`
- `https://api.waterdata.usgs.gov/ogcapi/v0/collections/daily/schema`

## Repository reconciliation

Authoring inspection base: `main@52675a800825c071ddc9df9476b543c49d73efd8`.
Delivery base: `main@7c69e025e2b274be4a19f49fa37e22401a2fe757`. Intervening merges added separately reviewed NDVI computation, STAC link-closure, and correctable atmospheric-event packets; their paths are disjoint from this connector slice.

The repository already has a draft `connectors/usgs/water_data/` product lane, a modern-versus-legacy cutover assessment, hydrology ingest boundaries, and a placeholder `tests/domains/hydrology/test_usgs_water_normalizer.py`. It did not contain an executable county capture normalizer or an exact open PR for `KFM-P32-PROG-0010` immediately before authoring.

Directory Rules place source-specific acquisition/admission under `connectors/`; therefore the Drive suggestion `tools/ingest/fetch_nwis.py` is adapted into the existing product connector rather than creating a parallel tool authority.

## Bounded implementation

This slice deliberately stops before live transport. It:

- builds modern credential-free request plans;
- accepts only already captured FeatureCollections;
- verifies pagination closure and safe `next` URLs;
- binds captured pages with SHA-256;
- preserves county/site/parameter/statistic/time/value/unit/approval/qualifier/last-modified fields;
- keeps site metadata administrative and daily values aggregate; and
- emits strict stdout-only normalized validation input.

It does not retry, sleep, contact USGS, read an API key, write RAW/QUARANTINE, emit an ingest receipt, activate a source, resolve evidence, interpret stream conditions, produce an alert, promote, release, deploy, publish, or authorize public use. Transport, rate-limit behavior, live response drift, SourceDescriptor activation, rights, and EvidenceBundle integration remain `NEEDS VERIFICATION`.

## Placement

The connector helper extends the existing `connectors/usgs/water_data/` lane. Semantic meaning, machine shape, reusable synthetic input, enforcement tests, source adaptation, authoring provenance, and scoped CI stay in their established roots under accepted ADR-0029 and Directory Rules.

## Source references

- Pass 32 atlas attachment: `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf#KFM-P32-PROG-0010`.
- Drive: `https://docs.google.com/document/d/1cDAPrrPt_AxMB3lBH4z-wQGwKmcGEUt-nOMLLsAlxQQ` (`New Ideas 5-17-26`).
