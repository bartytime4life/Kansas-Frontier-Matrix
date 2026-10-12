<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-32-ndvi-delta-computation-source-map
title: Pass 32 NDVI Delta Computation Source Map
type: source-adaptation-record
version: v0.1.0
status: draft
owners: OWNER_TBD — Agriculture steward · Remote-sensing steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; fixture-or-captured-input-only
owning_root: docs/
responsibility: Record how Pass 32 KFM-P32-PROG-0005 and its Drive source were narrowed to a no-network deterministic computation packet.
truth_posture: cite-or-abstain
related:
  - ../../../contracts/domains/agriculture/ndvi_delta_computation.md
  - ../../../tools/generators/compute_ndvi_delta.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 32 NDVI Delta Computation Source Map

## Candidate and source evidence

Pass 32 card `KFM-P32-PROG-0005` proposes an NDVI module that computes baseline and recent medians, thresholds deltas, and suppresses non-vegetated or cloud-contaminated pixels.

The Drive document `New Ideas 5-17-26` supplies the underlying proposal: `(B08-B04)/(B08+B04)`, a 30-day baseline median, a 4–7-day recent median, cloud-item fraction below `0.20`, pixel cloud masking, a `±0.12` delta threshold, and suppression below baseline NDVI `0.15`. It also proposes minimum patch area and multi-acquisition persistence; those spatial/persistence concerns remain owned by the existing vegetation connectivity gate and are not duplicated here.

Both documents are proposal evidence, not repository or scientific authority.

## Repository reconciliation

Inspection base: `main@52675a800825c071ddc9df9476b543c49d73efd8`.

The repository already contains:

- an HLS NDVI zonal materiality validator over precomputed summaries;
- an NDVI readiness validator;
- a vegetation connectivity gate over precomputed components; and
- a future-computation boundary in the environmental indicator evidence profile.

Those surfaces expressly do not calculate NDVI. No exact `KFM-P32-PROG-0005` implementation or open PR was found immediately before authoring.

## Bounded adaptation

The new generator performs only local per-cell arithmetic over explicit synthetic or captured reflectance observations. It freezes integer units and rounding, filters both scene-level and pixel-level clouds, calculates baseline/recent medians, applies the proposed floor and delta threshold, and emits a strict non-authoritative result.

It intentionally does not:

- fetch STAC/HLS assets or open COG/raster bytes;
- derive a 30-day or 7-day window from timestamps;
- perform geometric, area, patch, connectivity, or persistence analysis;
- create environmental evidence, policy, promotion, release, or public claims.

Future raster and temporal-window integration requires separately governed source, projection, resolution, nodata, resampling, spatial-unit, and scientific-fitness decisions.

## Placement

The calculation is an explicit deterministic generator under `tools/generators/`; semantic meaning, machine shape, fixtures, tests, source adaptation, authoring provenance, and scoped CI use their existing canonical roots. Accepted ADR-0029 and Directory Rules govern those placements. No new root or public package API is created.

## Source references

- Pass 32 atlas attachment: `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf#KFM-P32-PROG-0005`.
- Drive: `https://docs.google.com/document/d/1cDAPrrPt_AxMB3lBH4z-wQGwKmcGEUt-nOMLLsAlxQQ` (`New Ideas 5-17-26`).
- Repository basis: `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` and `docs/doctrine/directory-rules.md`.
